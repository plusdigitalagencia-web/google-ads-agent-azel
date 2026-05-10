#!/usr/bin/env python3
"""
Analyze ad videos using Google Gemini's native video understanding.

Usage:
    python analyze_video_gemini.py --video path/to/video.mp4
    python analyze_video_gemini.py --video path/to/video.mp4 --output analysis.md

Requirements:
    pip install google-genai python-dotenv
    GEMINI_API_KEY in .env

Output:
    Detailed markdown analysis of the video ad
"""

import os
import argparse
import time
from pathlib import Path
from datetime import datetime

from dotenv import load_dotenv
load_dotenv()

from google import genai
from google.genai import types


# The analysis prompt
ANALYSIS_PROMPT = """You are analyzing a paid social media ad video. Provide enough detail that someone could recreate this ad without watching it.

## 1. Scene-by-Scene Breakdown
For each distinct scene:
- Timestamp (e.g., 0:00-0:03)
- What's visually happening (setting, framing, movement)
- Exact transcript of what's said
- Exact text overlays shown
- Audio (music style, sound effects, silence)
- Transition to next scene (hard cut, zoom, swipe, etc.)

## 2. Production Details
- Format: UGC or produced?
- Creator: Who appears? (age, gender, vibe, credibility markers)
- Speaking style: To camera or voiceover? Energy level?
- Camera: Static, handheld, multiple angles?
- Lighting: Natural, ring light, professional?
- Total length and average cut pace (seconds per scene)

## 3. Structure & Emotional Arc
- Narrative type (problem→solution, testimonial, demonstration, etc.)
- How does energy/emotion shift from start to end?
- What's the hook in first 3 seconds?
- What's the CTA and how is it delivered?

## 4. Visual Proof & B-Roll
- Product demonstrations or close-ups?
- Before/after, screenshots, results shown?
- What B-roll supports the main footage?

Be extremely specific. Exact quotes, exact timestamps, exact text. Output should be detailed enough to brief a video editor to recreate this ad."""


def analyze_video(video_path: str, model_name: str = "gemini-3-flash-preview") -> str:
    """
    Upload video to Gemini and get analysis.

    Args:
        video_path: Path to video file
        model_name: Gemini model to use (default: gemini-2.0-flash)

    Returns:
        Analysis text from Gemini
    """
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key:
        raise ValueError("GEMINI_API_KEY not found in .env")

    client = genai.Client(api_key=api_key)

    video_path = Path(video_path)
    if not video_path.exists():
        raise FileNotFoundError(f"Video not found: {video_path}")

    print(f"Uploading video: {video_path.name} ({video_path.stat().st_size / 1024 / 1024:.1f} MB)")

    # Upload the video file
    video_file = client.files.upload(file=str(video_path))

    # Wait for processing
    print("Processing video...")
    while video_file.state == "PROCESSING":
        time.sleep(2)
        video_file = client.files.get(name=video_file.name)

    if video_file.state == "FAILED":
        raise RuntimeError(f"Video processing failed: {video_file.state}")

    print(f"Video ready. Analyzing with {model_name}...")

    # Generate analysis
    response = client.models.generate_content(
        model=model_name,
        contents=[
            types.Part.from_uri(file_uri=video_file.uri, mime_type=video_file.mime_type),
            ANALYSIS_PROMPT
        ]
    )

    # Clean up uploaded file
    print("Cleaning up uploaded file...")
    client.files.delete(name=video_file.name)

    return response.text


def save_analysis(analysis: str, output_path: str, video_name: str, model_name: str = "gemini-3-flash-preview"):
    """Save analysis to markdown file."""
    header = f"""# Video Analysis: {video_name}

**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}
**Model:** {model_name}

---

"""
    with open(output_path, 'w') as f:
        f.write(header + analysis)

    print(f"Analysis saved to: {output_path}")


def main():
    parser = argparse.ArgumentParser(description="Analyze ad video with Gemini")
    parser.add_argument("--video", required=True, help="Path to video file")
    parser.add_argument("--output", help="Output path for analysis (default: auto-generated)")
    parser.add_argument("--model", default="gemini-3-flash-preview", help="Gemini model to use")
    parser.add_argument("--keep-video", action="store_true", help="Don't delete video after analysis")

    args = parser.parse_args()

    video_path = Path(args.video)

    # Generate output path if not specified
    if args.output:
        output_path = args.output
    else:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        output_path = f".tmp/video_analysis_{video_path.stem}_{timestamp}.md"
        Path(".tmp").mkdir(exist_ok=True)

    try:
        # Analyze
        print("=" * 60)
        print("GEMINI VIDEO ANALYSIS")
        print("=" * 60)

        analysis = analyze_video(str(video_path), args.model)

        # Save
        save_analysis(analysis, output_path, video_path.name, args.model)

        # Delete video unless --keep-video
        if not args.keep_video:
            print(f"Deleting video file: {video_path}")
            video_path.unlink()

        print("=" * 60)
        print("Done!")
        print("=" * 60)

        # Print first part of analysis
        print("\nAnalysis preview:")
        print("-" * 40)
        preview_lines = analysis.split('\n')[:30]
        print('\n'.join(preview_lines))
        if len(analysis.split('\n')) > 30:
            print("\n... (see full analysis in output file)")

    except Exception as e:
        print(f"Error: {e}")
        raise


if __name__ == "__main__":
    main()

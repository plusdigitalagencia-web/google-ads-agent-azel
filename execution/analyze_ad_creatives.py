#!/usr/bin/env python3
"""
Ad Creative Analyzer - Analyze what makes winning ads work.

Takes performance data + creative assets and identifies patterns:
- Transcribes video ads
- Extracts hooks (first 3 seconds)
- Categorizes by script type (testimonial, problem-solution, etc.)
- Correlates creative elements with performance

Usage:
    python analyze_ad_creatives.py --performance .tmp/meta_performance.json --creatives .tmp/meta_creatives/

Inputs:
    - performance: JSON file with ad performance data
    - creatives: Directory with downloaded creative assets

Outputs:
    - .tmp/creative_analysis_[timestamp].json - Structured analysis
    - .tmp/creative_patterns_[timestamp].md - Pattern report

Requirements:
    - pip install openai python-dotenv
    - For video transcription: pip install openai-whisper (or use OpenAI API)
    - .env with OPENAI_API_KEY (for GPT analysis)
"""

import os
import json
import argparse
from datetime import datetime
from pathlib import Path

try:
    from dotenv import load_dotenv
    load_dotenv("/etc/secrets/.env", override=True)
load_dotenv(override=True)
except ImportError:
    pass


# Script type definitions for classification
SCRIPT_TYPES = {
    "problem_solution": {
        "description": "Starts with pain point, introduces product as solution",
        "indicators": ["frustrated", "tired of", "sick of", "finally", "solution"]
    },
    "testimonial": {
        "description": "First-person story: 'I tried everything until...'",
        "indicators": ["I was", "I tried", "I found", "changed my life", "my experience"]
    },
    "myth_buster": {
        "description": "Challenges common belief: 'Everyone says X, but...'",
        "indicators": ["everyone thinks", "you've been told", "the truth is", "actually", "myth"]
    },
    "investigation": {
        "description": "Discovery arc: 'I saw this expert say...'",
        "indicators": ["I saw", "I heard", "research shows", "studies show", "expert"]
    },
    "before_after": {
        "description": "Transformation story: 'X months ago I was...'",
        "indicators": ["months ago", "years ago", "before", "after", "transformation", "now I"]
    },
    "ugc_review": {
        "description": "Casual product review style",
        "indicators": ["review", "honest", "thoughts on", "tried this", "verdict"]
    },
    "founder_story": {
        "description": "Brand founder explaining the product",
        "indicators": ["we created", "I started", "our mission", "we wanted to"]
    }
}

# Hook type definitions
HOOK_TYPES = {
    "controversial": "Bold statement that challenges beliefs",
    "pain_callout": "Directly calls out a specific pain point",
    "curiosity": "Creates intrigue, makes viewer want to learn more",
    "social_proof": "Leads with numbers, reviews, or authority",
    "pov": "POV format - viewer imagines themselves in scenario",
    "question": "Opens with a question",
    "shock": "Surprising fact or statement",
    "relatable": "Highly relatable everyday situation"
}


def load_performance_data(filepath: str) -> dict:
    """Load performance data and index by ad_id."""
    with open(filepath, 'r') as f:
        data = json.load(f)

    # Index by ad_id for easy lookup
    return {str(ad.get('ad_id')): ad for ad in data}


def load_creative_metadata(filepath: str) -> list:
    """Load creative metadata."""
    with open(filepath, 'r') as f:
        return json.load(f)


def transcribe_video(video_path: str) -> str:
    """
    Transcribe video using Whisper.

    Options:
    1. Local whisper: pip install openai-whisper
    2. OpenAI API: Uses cloud transcription
    """
    if not os.path.exists(video_path):
        return None

    # Option 1: OpenAI API (simpler, costs money)
    api_key = os.getenv('OPENAI_API_KEY')
    if api_key:
        try:
            import openai
            client = openai.OpenAI(api_key=api_key)

            with open(video_path, 'rb') as f:
                transcript = client.audio.transcriptions.create(
                    model="whisper-1",
                    file=f
                )
            return transcript.text
        except Exception as e:
            print(f"OpenAI transcription failed: {e}")

    # Option 2: Local Whisper (free, requires install)
    try:
        import whisper
        model = whisper.load_model("base")
        result = model.transcribe(video_path)
        return result["text"]
    except ImportError:
        print("Whisper not installed. Run: pip install openai-whisper")
    except Exception as e:
        print(f"Local transcription failed: {e}")

    return None


def extract_hook(transcript: str, max_words: int = 20) -> str:
    """Extract the hook (first ~3 seconds / 20 words) from transcript."""
    if not transcript:
        return None

    words = transcript.split()
    hook_words = words[:max_words]
    return ' '.join(hook_words)


def classify_script_type(transcript: str, primary_text: str = "") -> tuple:
    """
    Classify the ad script type based on content.

    Returns: (script_type, confidence, reasoning)
    """
    if not transcript and not primary_text:
        return ("unknown", 0, "No content to analyze")

    content = f"{transcript or ''} {primary_text or ''}".lower()

    scores = {}
    for script_type, info in SCRIPT_TYPES.items():
        score = sum(1 for indicator in info["indicators"] if indicator in content)
        scores[script_type] = score

    if max(scores.values()) == 0:
        return ("unknown", 0, "No clear indicators found")

    best_type = max(scores, key=scores.get)
    confidence = min(scores[best_type] / 3, 1.0)  # Normalize to 0-1

    return (best_type, confidence, SCRIPT_TYPES[best_type]["description"])


def classify_hook_type(hook: str) -> tuple:
    """
    Classify the hook type.

    Returns: (hook_type, reasoning)
    """
    if not hook:
        return ("unknown", "No hook to analyze")

    hook_lower = hook.lower()

    # Simple rule-based classification
    if "?" in hook:
        return ("question", "Opens with a question")
    if any(word in hook_lower for word in ["everyone", "they say", "you think"]):
        return ("controversial", "Challenges common belief")
    if any(word in hook_lower for word in ["tired", "frustrated", "sick", "hate"]):
        return ("pain_callout", "Calls out specific pain")
    if any(word in hook_lower for word in ["pov", "imagine", "picture this"]):
        return ("pov", "POV format")
    if any(word in hook_lower for word in ["reviews", "people", "customers", "sold"]):
        return ("social_proof", "Leads with social proof")
    if any(word in hook_lower for word in ["secret", "discovered", "found out"]):
        return ("curiosity", "Creates curiosity")

    return ("relatable", "General relatable opening")


def analyze_creative(creative: dict, performance: dict) -> dict:
    """
    Analyze a single creative and correlate with performance.
    """
    ad_id = creative.get('ad_id')
    ad_name = creative.get('ad_name', 'Unknown')

    # Get performance metrics
    perf = performance.get(str(ad_id), {})

    # Get transcript (if video)
    transcript = creative.get('transcript')
    if not transcript and creative.get('video_path'):
        transcript = transcribe_video(creative['video_path'])

    # Extract hook
    hook = extract_hook(transcript)

    # Classify
    script_type, script_confidence, script_desc = classify_script_type(
        transcript,
        creative.get('primary_text', '')
    )
    hook_type, hook_reasoning = classify_hook_type(hook)

    return {
        "ad_id": ad_id,
        "ad_name": ad_name,

        # Creative elements
        "transcript": transcript,
        "hook": hook,
        "primary_text": creative.get('primary_text'),
        "headline": creative.get('headline'),

        # Classifications
        "script_type": script_type,
        "script_confidence": script_confidence,
        "script_description": script_desc,
        "hook_type": hook_type,
        "hook_reasoning": hook_reasoning,

        # Performance
        "spend": perf.get('spend'),
        "cpa": perf.get('cpa'),
        "roas": perf.get('roas'),
        "purchases": perf.get('purchases'),
        "ctr": perf.get('ctr'),

        # Format
        "format": "video" if creative.get('video_url') else "static",
    }


def find_patterns(analyses: list) -> dict:
    """
    Find patterns across all analyzed creatives.
    """
    # Filter to ads with meaningful spend
    with_spend = [a for a in analyses if a.get('spend') and float(a['spend']) > 10]

    if not with_spend:
        return {"error": "No ads with meaningful spend to analyze"}

    # Sort by ROAS for pattern finding
    by_roas = sorted(
        [a for a in with_spend if a.get('roas')],
        key=lambda x: float(x['roas']),
        reverse=True
    )

    # Count script types by performance tier
    top_performers = by_roas[:len(by_roas)//3] if by_roas else []
    bottom_performers = by_roas[-len(by_roas)//3:] if by_roas else []

    def count_types(ads, key):
        counts = {}
        for ad in ads:
            t = ad.get(key, 'unknown')
            counts[t] = counts.get(t, 0) + 1
        return counts

    return {
        "total_analyzed": len(analyses),
        "with_spend": len(with_spend),

        "top_performer_script_types": count_types(top_performers, 'script_type'),
        "bottom_performer_script_types": count_types(bottom_performers, 'script_type'),

        "top_performer_hook_types": count_types(top_performers, 'hook_type'),
        "bottom_performer_hook_types": count_types(bottom_performers, 'hook_type'),

        "format_breakdown": count_types(with_spend, 'format'),

        "best_hooks": [
            {"hook": a.get('hook'), "roas": a.get('roas'), "ad_name": a.get('ad_name')}
            for a in by_roas[:5] if a.get('hook')
        ],
    }


def generate_pattern_report(analyses: list, patterns: dict, output_path: str):
    """Generate markdown report of creative patterns."""

    report = f"""# Creative Pattern Analysis

**Generated:** {datetime.now().isoformat()}
**Ads Analyzed:** {patterns.get('total_analyzed', 0)}
**With Meaningful Spend:** {patterns.get('with_spend', 0)}

---

## Script Type Performance

### Top Performers Use:
"""
    for script_type, count in patterns.get('top_performer_script_types', {}).items():
        report += f"- **{script_type}**: {count} ads\n"

    report += """
### Bottom Performers Use:
"""
    for script_type, count in patterns.get('bottom_performer_script_types', {}).items():
        report += f"- **{script_type}**: {count} ads\n"

    report += """
---

## Hook Type Performance

### Top Performers Use:
"""
    for hook_type, count in patterns.get('top_performer_hook_types', {}).items():
        report += f"- **{hook_type}**: {count} ads\n"

    report += """
---

## Best Performing Hooks

"""
    for i, hook_data in enumerate(patterns.get('best_hooks', []), 1):
        report += f"""**#{i}** (ROAS: {hook_data.get('roas')}x)
> "{hook_data.get('hook')}"
*Ad: {hook_data.get('ad_name')}*

"""

    report += """
---

## Recommendations

Based on patterns:

1. **Script types to test more:** [Based on top performer analysis]
2. **Hook types to test more:** [Based on top performer analysis]
3. **Scripts to avoid:** [Based on bottom performer analysis]

---

*Generated by analyze_ad_creatives.py*
"""

    with open(output_path, 'w') as f:
        f.write(report)

    return output_path


def main():
    parser = argparse.ArgumentParser(description="Analyze ad creatives and find patterns")
    parser.add_argument("--performance", required=True, help="Path to performance JSON")
    parser.add_argument("--creatives", required=True, help="Path to creatives JSON or directory")
    parser.add_argument("--output", default=".tmp", help="Output directory")

    args = parser.parse_args()

    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    Path(args.output).mkdir(parents=True, exist_ok=True)

    # Load data
    print("Loading performance data...")
    performance = load_performance_data(args.performance)
    print(f"Loaded {len(performance)} ads")

    print("Loading creative metadata...")
    if os.path.isfile(args.creatives):
        creatives = load_creative_metadata(args.creatives)
    else:
        # Load from directory structure
        creatives = []
        for ad_dir in Path(args.creatives).iterdir():
            if ad_dir.is_dir():
                copy_file = ad_dir / 'copy.json'
                if copy_file.exists():
                    with open(copy_file) as f:
                        data = json.load(f)
                        data['ad_id'] = ad_dir.name
                        # Check for video file
                        for video in ad_dir.glob('*.mp4'):
                            data['video_path'] = str(video)
                        creatives.append(data)

    print(f"Loaded {len(creatives)} creatives")

    # Analyze each creative
    print("\nAnalyzing creatives...")
    analyses = []
    for creative in creatives:
        analysis = analyze_creative(creative, performance)
        analyses.append(analysis)
        print(f"  Analyzed: {analysis.get('ad_name', 'Unknown')[:40]}")

    # Save detailed analysis
    analysis_path = f"{args.output}/creative_analysis_{timestamp}.json"
    with open(analysis_path, 'w') as f:
        json.dump(analyses, f, indent=2)
    print(f"\nDetailed analysis saved to: {analysis_path}")

    # Find patterns
    print("\nFinding patterns...")
    patterns = find_patterns(analyses)

    # Generate report
    report_path = f"{args.output}/creative_patterns_{timestamp}.md"
    generate_pattern_report(analyses, patterns, report_path)
    print(f"Pattern report saved to: {report_path}")

    print("\nDone!")


if __name__ == "__main__":
    main()

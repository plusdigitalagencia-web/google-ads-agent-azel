#!/usr/bin/env python3
"""
Customer Video Collector - Manage customer testimonial video submissions.

Usage:
    python customer_video_collector.py --action list
    python customer_video_collector.py --action add --customer "John Doe" --video /path/to/video.mp4
    python customer_video_collector.py --action approve --id 123

Inputs:
    - action: list, add, approve, reject, export
    - Various flags depending on action

Outputs:
    - Updated content log
    - Organized video library

Requirements:
    - Google Drive API for storage (optional)
    - pip install google-api-python-client python-dotenv

Directory Structure:
    customer_content/
    ├── raw/
    │   └── [date]_[customer_name]/
    ├── approved/
    │   ├── full_testimonials/
    │   ├── clips/
    │   └── quotes/
    └── used/
        └── [ad_name]/
"""

import os
import json
import argparse
from datetime import datetime
from pathlib import Path

def ensure_directory_structure(base_path: str):
    """Create the required directory structure."""
    dirs = [
        "customer_content/raw",
        "customer_content/approved/full_testimonials",
        "customer_content/approved/clips",
        "customer_content/approved/quotes",
        "customer_content/used"
    ]
    for d in dirs:
        Path(os.path.join(base_path, d)).mkdir(parents=True, exist_ok=True)

def load_content_log(log_path: str) -> dict:
    """Load or create content log."""
    if os.path.exists(log_path):
        with open(log_path, "r") as f:
            return json.load(f)
    return {
        "submissions": [],
        "stats": {
            "total": 0,
            "approved": 0,
            "rejected": 0,
            "used": 0,
            "credit_issued": 0
        }
    }

def save_content_log(log_path: str, data: dict):
    """Save content log."""
    with open(log_path, "w") as f:
        json.dump(data, f, indent=2)

def main():
    parser = argparse.ArgumentParser(description="Manage customer video submissions")
    parser.add_argument("--action", required=True,
                       choices=["list", "add", "approve", "reject", "export", "stats"])
    parser.add_argument("--customer", help="Customer name (for add)")
    parser.add_argument("--video", help="Path to video file (for add)")
    parser.add_argument("--product", help="Product purchased (for add)")
    parser.add_argument("--id", help="Submission ID (for approve/reject)")
    parser.add_argument("--base-path", default=".", help="Base path for file storage")

    args = parser.parse_args()

    log_path = os.path.join(args.base_path, ".tmp/customer_content_log.json")
    Path(os.path.dirname(log_path)).mkdir(parents=True, exist_ok=True)

    # Ensure directory structure exists
    ensure_directory_structure(args.base_path)

    # Load existing log
    content_log = load_content_log(log_path)

    if args.action == "list":
        print("\n=== Customer Video Submissions ===\n")
        if not content_log["submissions"]:
            print("No submissions yet.")
        else:
            for sub in content_log["submissions"]:
                status_icon = {"pending": "⏳", "approved": "✅", "rejected": "❌", "used": "🎬"}.get(sub["status"], "?")
                print(f"{status_icon} [{sub['id']}] {sub['customer']} - {sub['product']} ({sub['status']})")

    elif args.action == "add":
        if not args.customer or not args.product:
            print("Error: --customer and --product required for add action")
            return

        new_id = len(content_log["submissions"]) + 1
        submission = {
            "id": new_id,
            "customer": args.customer,
            "product": args.product,
            "video_path": args.video or "pending_upload",
            "date": datetime.now().isoformat(),
            "status": "pending",
            "quality": None,
            "key_quote": None,
            "used_in": None
        }
        content_log["submissions"].append(submission)
        content_log["stats"]["total"] += 1
        save_content_log(log_path, content_log)
        print(f"Added submission #{new_id} from {args.customer}")

    elif args.action == "approve":
        if not args.id:
            print("Error: --id required for approve action")
            return

        for sub in content_log["submissions"]:
            if str(sub["id"]) == args.id:
                sub["status"] = "approved"
                content_log["stats"]["approved"] += 1
                save_content_log(log_path, content_log)
                print(f"Approved submission #{args.id}")
                return
        print(f"Submission #{args.id} not found")

    elif args.action == "reject":
        if not args.id:
            print("Error: --id required for reject action")
            return

        for sub in content_log["submissions"]:
            if str(sub["id"]) == args.id:
                sub["status"] = "rejected"
                content_log["stats"]["rejected"] += 1
                save_content_log(log_path, content_log)
                print(f"Rejected submission #{args.id}")
                return
        print(f"Submission #{args.id} not found")

    elif args.action == "stats":
        stats = content_log["stats"]
        print("\n=== Content Collection Stats ===\n")
        print(f"Total submissions: {stats['total']}")
        print(f"Approved: {stats['approved']}")
        print(f"Rejected: {stats['rejected']}")
        print(f"Used in ads: {stats['used']}")
        if stats['total'] > 0:
            approval_rate = (stats['approved'] / stats['total']) * 100
            print(f"Approval rate: {approval_rate:.1f}%")

    elif args.action == "export":
        # Export approved content list
        approved = [s for s in content_log["submissions"] if s["status"] == "approved"]
        export_path = os.path.join(args.base_path, f".tmp/approved_content_{datetime.now().strftime('%Y%m%d')}.json")
        with open(export_path, "w") as f:
            json.dump(approved, f, indent=2)
        print(f"Exported {len(approved)} approved submissions to {export_path}")

if __name__ == "__main__":
    main()

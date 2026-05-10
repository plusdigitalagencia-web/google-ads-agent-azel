#!/usr/bin/env python3
"""
Meta Ads Fetcher - Pull ad performance data and creatives from Meta Marketing API.

Usage:
    python meta_ads_fetcher.py --action performance --days 30
    python meta_ads_fetcher.py --action creatives --ad-ids "123,456,789"
    python meta_ads_fetcher.py --action all --days 30

Actions:
    - performance: Pull performance metrics for all ads
    - creatives: Download ad creatives (images/videos)
    - all: Pull both performance and creatives

Inputs:
    - days: Number of days to look back (default: 30)
    - ad-ids: Specific ad IDs to fetch (optional)
    - account-id: Ad account ID (or set META_AD_ACCOUNT_ID in .env)

Outputs:
    - .tmp/meta_performance_[timestamp].json - Performance data
    - .tmp/meta_creatives/[ad_id]/ - Downloaded creative assets
    - .tmp/meta_analysis_[timestamp].md - Formatted analysis report

Requirements:
    - pip install facebook-business python-dotenv requests
    - .env file with:
        META_ACCESS_TOKEN=your_access_token
        META_AD_ACCOUNT_ID=act_123456789

    To get your access token:
    1. Go to developers.facebook.com/tools/explorer
    2. Select your app (or create one)
    3. Add permission: ads_read
    4. Generate token
"""

import os
import json
import argparse
from datetime import datetime, timedelta
from pathlib import Path

from dotenv import load_dotenv
load_dotenv()

from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.ad import Ad
from facebook_business.adobjects.adcreative import AdCreative


def get_date_range(days: int) -> tuple:
    """Get date range for API query."""
    end_date = datetime.now()
    start_date = end_date - timedelta(days=days)
    return start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d')


def init_api():
    """Initialize Meta Marketing API."""
    access_token = os.getenv('META_ACCESS_TOKEN')

    if not access_token:
        raise ValueError(
            "Missing META_ACCESS_TOKEN in .env file.\n"
            "Get one at: developers.facebook.com/tools/explorer"
        )

    FacebookAdsApi.init(access_token=access_token)
    return True


def fetch_ad_performance(account_id: str, days: int) -> list:
    """
    Fetch performance data for all ads in the account.

    Returns list of dicts with:
    - ad_id, ad_name, adset_name, campaign_name
    - spend, impressions, clicks, ctr, cpc
    - purchases, purchase_value, cpa, roas
    - reach, frequency
    - video_views, video_p25, video_p50, video_p75, video_p100 (if video)
    """
    start_date, end_date = get_date_range(days)

    # Fields to fetch
    fields = [
        'ad_id',
        'ad_name',
        'adset_name',
        'campaign_name',
        'spend',
        'impressions',
        'clicks',
        'ctr',
        'cpc',
        'reach',
        'frequency',
        'actions',
        'action_values',
        'video_p25_watched_actions',
        'video_p50_watched_actions',
        'video_p75_watched_actions',
        'video_p100_watched_actions',
    ]

    params = {
        'time_range': {'since': start_date, 'until': end_date},
        'level': 'ad',
    }

    print(f"Fetching performance data for {account_id}")
    print(f"Date range: {start_date} to {end_date}")

    account = AdAccount(account_id)
    insights = account.get_insights(fields=fields, params=params)

    results = []
    for insight in insights:
        results.append(dict(insight))

    print(f"Found {len(results)} ads with data")
    return results


def fetch_ad_creatives(account_id: str, ad_ids: list = None) -> list:
    """
    Fetch creative assets (images, videos, copy) for ads.

    Returns list of dicts with:
    - ad_id, ad_name
    - thumbnail_url, image_url, video_url
    - primary_text, headline, description
    - call_to_action
    """
    print(f"Fetching creatives for {account_id}")

    account = AdAccount(account_id)

    # Get ads
    if ad_ids:
        ads = [Ad(ad_id) for ad_id in ad_ids]
    else:
        ads = account.get_ads(fields=['id', 'name', 'creative'])

    results = []
    for ad in ads:
        try:
            ad_data = dict(ad)
            creative_id = ad_data.get('creative', {}).get('id')

            if creative_id:
                creative = AdCreative(creative_id)
                creative_data = creative.api_get(fields=[
                    'id',
                    'name',
                    'body',
                    'title',
                    'image_url',
                    'thumbnail_url',
                    'video_id',
                    'object_story_spec',
                    'asset_feed_spec',
                ])

                # Extract text from object_story_spec if available
                story_spec = dict(creative_data).get('object_story_spec', {})
                link_data = story_spec.get('link_data', {})
                video_data = story_spec.get('video_data', {})

                result = {
                    'ad_id': ad_data.get('id'),
                    'ad_name': ad_data.get('name'),
                    'creative_id': creative_id,
                    'primary_text': link_data.get('message') or video_data.get('message'),
                    'headline': link_data.get('name') or video_data.get('title'),
                    'description': link_data.get('description'),
                    'image_url': dict(creative_data).get('image_url') or link_data.get('picture'),
                    'thumbnail_url': dict(creative_data).get('thumbnail_url'),
                    'video_id': dict(creative_data).get('video_id'),
                    'call_to_action': link_data.get('call_to_action', {}).get('type'),
                }
                results.append(result)

        except Exception as e:
            print(f"  Error fetching creative for ad {ad_data.get('id')}: {e}")

    print(f"Found {len(results)} creatives")
    return results


def download_creative_assets(creatives: list, output_dir: str):
    """Download images and videos from creative URLs."""
    import requests

    Path(output_dir).mkdir(parents=True, exist_ok=True)

    for creative in creatives:
        ad_id = creative.get('ad_id')
        ad_dir = Path(output_dir) / str(ad_id)
        ad_dir.mkdir(exist_ok=True)

        # Download image
        if creative.get('image_url'):
            try:
                response = requests.get(creative['image_url'])
                if response.status_code == 200:
                    with open(ad_dir / 'image.jpg', 'wb') as f:
                        f.write(response.content)
            except Exception as e:
                print(f"  Error downloading image for {ad_id}: {e}")

        # Download thumbnail
        if creative.get('thumbnail_url'):
            try:
                response = requests.get(creative['thumbnail_url'])
                if response.status_code == 200:
                    with open(ad_dir / 'thumbnail.jpg', 'wb') as f:
                        f.write(response.content)
            except Exception as e:
                print(f"  Error downloading thumbnail for {ad_id}: {e}")

        # Save copy/text
        copy_data = {
            'ad_id': ad_id,
            'ad_name': creative.get('ad_name'),
            'primary_text': creative.get('primary_text'),
            'headline': creative.get('headline'),
            'description': creative.get('description'),
            'cta': creative.get('call_to_action'),
        }
        with open(ad_dir / 'copy.json', 'w') as f:
            json.dump(copy_data, f, indent=2, ensure_ascii=False)


def calculate_derived_metrics(ad_data: dict) -> dict:
    """Calculate CPA, ROAS, and other derived metrics."""
    spend = float(ad_data.get('spend', 0))

    # Extract purchases from actions
    purchases = 0
    purchase_value = 0

    actions = ad_data.get('actions', [])
    if actions:
        for action in actions:
            if action.get('action_type') == 'purchase':
                purchases = int(action.get('value', 0))
            # Also check for omni_purchase (cross-device)
            if action.get('action_type') == 'omni_purchase':
                purchases += int(action.get('value', 0))

    action_values = ad_data.get('action_values', [])
    if action_values:
        for action in action_values:
            if action.get('action_type') in ['purchase', 'omni_purchase']:
                purchase_value += float(action.get('value', 0))

    # Calculate derived metrics
    cpa = spend / purchases if purchases > 0 else None
    roas = purchase_value / spend if spend > 0 else None

    return {
        **ad_data,
        'purchases': purchases,
        'purchase_value': round(purchase_value, 2),
        'cpa': round(cpa, 2) if cpa else None,
        'roas': round(roas, 2) if roas else None,
    }


def generate_analysis_report(performance_data: list, output_path: str):
    """Generate markdown analysis report from performance data."""

    if not performance_data:
        report = "# Meta Ads Performance Report\n\nNo data available for this period.\n"
    else:
        # Sort by spend (top spenders first)
        sorted_data = sorted(performance_data, key=lambda x: float(x.get('spend', 0)), reverse=True)

        total_spend = sum(float(ad.get('spend', 0)) for ad in performance_data)
        total_purchases = sum(ad.get('purchases', 0) for ad in performance_data)
        total_revenue = sum(ad.get('purchase_value', 0) for ad in performance_data)
        overall_roas = total_revenue / total_spend if total_spend > 0 else 0

        report = f"""# Meta Ads Performance Report

**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}
**Ads Analyzed:** {len(performance_data)}
**Total Spend:** {total_spend:,.2f} USD
**Total Purchases:** {total_purchases}
**Total Revenue:** {total_revenue:,.2f} USD
**Overall ROAS:** {overall_roas:.2f}x

---

## Top Performers by Spend (DO NOT TURN OFF)

| Ad Name | Spend | Purchases | CPA | ROAS |
|---------|-------|-----------|-----|------|
"""
        for ad in sorted_data[:10]:
            name = ad.get('ad_name', 'Unknown')[:40]
            spend = float(ad.get('spend', 0))
            purchases = ad.get('purchases', 0)
            cpa = ad.get('cpa')
            roas = ad.get('roas')
            cpa_str = f"{cpa:.2f}" if cpa else "N/A"
            roas_str = f"{roas:.2f}x" if roas else "N/A"
            report += f"| {name} | {spend:.2f} | {purchases} | {cpa_str} | {roas_str} |\n"

        # Find emerging winners (low spend but good ROAS)
        emerging = [ad for ad in performance_data
                   if float(ad.get('spend', 0)) < 500
                   and ad.get('roas') and ad.get('roas') > 2]
        emerging = sorted(emerging, key=lambda x: x.get('roas', 0), reverse=True)[:5]

        if emerging:
            report += """
---

## Emerging Winners (Low spend, high ROAS - consider scaling)

| Ad Name | Spend | ROAS | Purchases |
|---------|-------|------|-----------|
"""
            for ad in emerging:
                name = ad.get('ad_name', 'Unknown')[:40]
                spend = float(ad.get('spend', 0))
                roas = ad.get('roas', 0)
                purchases = ad.get('purchases', 0)
                report += f"| {name} | {spend:.2f} | {roas:.2f}x | {purchases} |\n"

        report += """
---

## Next Steps

1. **Protect top spenders** - Don't turn these off
2. **Scale emerging winners** - Give them more budget
3. **Analyze patterns** - What do winners have in common?

---

*Generated by meta_ads_fetcher.py*
"""

    with open(output_path, 'w') as f:
        f.write(report)

    return output_path


def main():
    parser = argparse.ArgumentParser(description="Fetch Meta Ads performance and creatives")
    parser.add_argument("--action", required=True, choices=["performance", "creatives", "all"])
    parser.add_argument("--days", type=int, default=30, help="Days to look back")
    parser.add_argument("--ad-ids", default="", help="Comma-separated ad IDs")
    parser.add_argument("--account-id", default="", help="Ad account ID (or use .env)")
    parser.add_argument("--output", default=".tmp", help="Output directory")

    args = parser.parse_args()

    # Get account ID
    account_id = args.account_id or os.getenv('META_AD_ACCOUNT_ID')
    if not account_id:
        print("Error: No ad account ID. Set --account-id or META_AD_ACCOUNT_ID in .env")
        print("\nTo find your Ad Account ID:")
        print("1. Go to Meta Business Suite > Settings > Ad Accounts")
        print("2. Copy the account ID (starts with 'act_')")
        return

    # Ensure output directory exists
    Path(args.output).mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

    # Initialize API
    try:
        init_api()
    except ValueError as e:
        print(f"Error: {e}")
        return

    if args.action in ["performance", "all"]:
        print(f"\nFetching performance data for last {args.days} days...")
        try:
            performance = fetch_ad_performance(account_id, args.days)

            # Calculate derived metrics
            performance = [calculate_derived_metrics(ad) for ad in performance]

            # Save raw data
            perf_path = f"{args.output}/meta_performance_{timestamp}.json"
            with open(perf_path, 'w') as f:
                json.dump(performance, f, indent=2, ensure_ascii=False)
            print(f"Performance data saved to: {perf_path}")

            # Generate analysis report
            report_path = f"{args.output}/meta_analysis_{timestamp}.md"
            generate_analysis_report(performance, report_path)
            print(f"Analysis report saved to: {report_path}")

        except Exception as e:
            print(f"Error fetching performance: {e}")

    if args.action in ["creatives", "all"]:
        ad_ids = [x.strip() for x in args.ad_ids.split(',')] if args.ad_ids else None
        print(f"\nFetching ad creatives...")
        try:
            creatives = fetch_ad_creatives(account_id, ad_ids)

            # Save creative metadata
            creative_path = f"{args.output}/meta_creatives_{timestamp}.json"
            with open(creative_path, 'w') as f:
                json.dump(creatives, f, indent=2, ensure_ascii=False)
            print(f"Creative metadata saved to: {creative_path}")

            # Download assets
            if creatives:
                assets_dir = f"{args.output}/meta_creatives"
                print(f"Downloading creative assets...")
                download_creative_assets(creatives, assets_dir)
                print(f"Creative assets downloaded to: {assets_dir}/")

        except Exception as e:
            print(f"Error fetching creatives: {e}")

    print("\nDone!")


if __name__ == "__main__":
    main()

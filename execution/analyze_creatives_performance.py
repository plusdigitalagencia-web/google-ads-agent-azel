#!/usr/bin/env python3
"""
Analyze Meta Ads Creatives correlated with Performance Data.

Reads performance and creative data, correlates them, and identifies patterns
in top-performing ads.

Usage:
    python analyze_creatives_performance.py

Outputs:
    - .tmp/creative_analysis_[timestamp].md - Full analysis report
    - Console output with key insights
"""

import json
import re
from pathlib import Path
from datetime import datetime
from collections import defaultdict


def load_latest_files(tmp_dir: str = ".tmp"):
    """Load the most recent performance and creative files."""
    tmp_path = Path(tmp_dir)

    # Find latest performance file
    perf_files = list(tmp_path.glob("meta_performance_*.json"))
    if not perf_files:
        raise FileNotFoundError("No performance files found in .tmp/")
    latest_perf = max(perf_files, key=lambda x: x.stat().st_mtime)

    # Find latest creatives file
    creative_files = list(tmp_path.glob("meta_creatives_*.json"))
    if not creative_files:
        raise FileNotFoundError("No creative files found in .tmp/")
    latest_creative = max(creative_files, key=lambda x: x.stat().st_mtime)

    print(f"Loading: {latest_perf.name}")
    with open(latest_perf) as f:
        performance = json.load(f)

    print(f"Loading: {latest_creative.name}")
    with open(latest_creative) as f:
        creatives = json.load(f)

    return performance, creatives


def extract_purchases_and_value(ad_data: dict) -> tuple:
    """Extract purchase count and value from actions."""
    purchases = 0
    purchase_value = 0

    actions = ad_data.get('actions', [])
    if actions:
        for action in actions:
            if action.get('action_type') == 'purchase':
                purchases = int(action.get('value', 0))
            if action.get('action_type') == 'omni_purchase':
                purchases += int(action.get('value', 0))

    action_values = ad_data.get('action_values', [])
    if action_values:
        for action in action_values:
            if action.get('action_type') in ['purchase', 'omni_purchase']:
                purchase_value += float(action.get('value', 0))

    return purchases, purchase_value


def correlate_data(performance: list, creatives: list) -> list:
    """Merge performance and creative data by ad_id."""
    # Create lookup for creatives
    creative_lookup = {c['ad_id']: c for c in creatives}

    correlated = []
    for perf in performance:
        ad_id = perf.get('ad_id')
        spend = float(perf.get('spend', 0))
        purchases, purchase_value = extract_purchases_and_value(perf)

        cpa = spend / purchases if purchases > 0 else None
        roas = purchase_value / spend if spend > 0 else None

        creative = creative_lookup.get(ad_id, {})

        correlated.append({
            'ad_id': ad_id,
            'ad_name': perf.get('ad_name', ''),
            'spend': spend,
            'purchases': purchases,
            'purchase_value': purchase_value,
            'cpa': cpa,
            'roas': roas,
            'impressions': int(perf.get('impressions', 0)),
            'clicks': int(perf.get('clicks', 0)),
            'ctr': float(perf.get('ctr', 0)),
            'primary_text': creative.get('primary_text'),
            'headline': creative.get('headline'),
            'has_video': creative.get('video_id') is not None,
            'has_image': creative.get('image_url') is not None,
            'cta': creative.get('call_to_action'),
        })

    return correlated


def extract_hook_type(ad_name: str) -> str:
    """Extract the hook/creator type from ad name.

    Customize this function with your own creator/hook naming patterns.
    Example patterns shown below - replace with your actual creator names.
    """
    name_lower = ad_name.lower()

    # Known creator/hook patterns - CUSTOMIZE THESE FOR YOUR BRAND
    # Example patterns (replace with your actual creator names):
    if 'creator1' in name_lower:
        return 'Creator 1 (Expert)'
    elif 'creator2' in name_lower:
        return 'Creator 2 (UGC)'
    elif 'founder' in name_lower:
        return 'Founder'
    elif 'ugc' in name_lower:
        return 'UGC Creator'
    elif 'organic' in name_lower:
        return 'Organic'
    elif 'testimonial' in name_lower:
        return 'Testimonial'
    elif 'demo' in name_lower:
        return 'Demo'
    elif 'hook' in name_lower:
        return 'Hook Test'
    else:
        return 'Other'


def extract_product_type(ad_name: str, headline: str = None) -> str:
    """Extract product type from ad name or headline.

    Customize this function with your own product naming patterns.
    """
    name_lower = ad_name.lower()
    headline_lower = (headline or '').lower()

    # CUSTOMIZE THESE FOR YOUR BRAND's products
    # Example patterns:
    if 'product_a' in name_lower or 'product_a' in headline_lower:
        return 'Product A'
    elif 'product_b' in name_lower or 'product_b' in headline_lower:
        return 'Product B'
    elif 'bundle' in name_lower or 'bundle' in headline_lower:
        return 'Bundle'
    else:
        return 'General/Mixed'


def extract_copy_elements(primary_text: str) -> dict:
    """Analyze copy structure and elements."""
    if not primary_text:
        return {'has_copy': False}

    elements = {
        'has_copy': True,
        'has_emoji': bool(re.search(r'[\U0001F300-\U0001F9FF]', primary_text)),
        'has_bullet_points': '✅' in primary_text or '•' in primary_text or '-' in primary_text,
        'has_question_hook': '?' in primary_text.split('\n')[0] if primary_text else False,
        # CUSTOMIZE: Add keywords that indicate guarantee in your language
        'has_guarantee': any(word in primary_text.lower() for word in ['guarantee', 'guaranteed', 'money back']),
        # CUSTOMIZE: Add keywords that indicate social proof in your language
        'has_social_proof': any(word in primary_text.lower() for word in ['thousand', 'customers', 'reviews', 'rated']),
        'has_url': '.com' in primary_text.lower() or 'http' in primary_text.lower(),
        'word_count': len(primary_text.split()),
        'line_count': len(primary_text.split('\n')),
    }

    # Identify hook type from first line
    # CUSTOMIZE: Add hook pattern keywords for your language
    first_line = primary_text.split('\n')[0].lower()
    if any(word in first_line for word in ['did you know', 'ever wonder']):
        elements['hook_style'] = 'curiosity'
    elif 'love' in first_line and 'hate' in first_line:
        elements['hook_style'] = 'love-hate'
    elif any(word in first_line for word in ['goodbye', 'no more', 'finally']):
        elements['hook_style'] = 'goodbye-problem'
    elif '?' in first_line:
        elements['hook_style'] = 'question'
    else:
        elements['hook_style'] = 'statement'

    return elements


def analyze_patterns(correlated_data: list) -> dict:
    """Analyze patterns across all dimensions."""

    # Filter to ads with meaningful spend
    with_spend = [ad for ad in correlated_data if ad['spend'] >= 100]

    analysis = {
        'total_ads': len(correlated_data),
        'ads_with_spend': len(with_spend),
        'total_spend': sum(ad['spend'] for ad in correlated_data),
        'total_purchases': sum(ad['purchases'] for ad in correlated_data),
        'total_revenue': sum(ad['purchase_value'] for ad in correlated_data),
    }

    # Group by hook/creator type
    by_hook = defaultdict(lambda: {'spend': 0, 'purchases': 0, 'revenue': 0, 'count': 0})
    for ad in with_spend:
        hook = extract_hook_type(ad['ad_name'])
        by_hook[hook]['spend'] += ad['spend']
        by_hook[hook]['purchases'] += ad['purchases']
        by_hook[hook]['revenue'] += ad['purchase_value']
        by_hook[hook]['count'] += 1

    # Calculate ROAS per hook type
    for hook, data in by_hook.items():
        data['roas'] = data['revenue'] / data['spend'] if data['spend'] > 0 else 0
        data['cpa'] = data['spend'] / data['purchases'] if data['purchases'] > 0 else None

    analysis['by_hook_type'] = dict(by_hook)

    # Group by product type
    by_product = defaultdict(lambda: {'spend': 0, 'purchases': 0, 'revenue': 0, 'count': 0})
    for ad in with_spend:
        product = extract_product_type(ad['ad_name'], ad.get('headline'))
        by_product[product]['spend'] += ad['spend']
        by_product[product]['purchases'] += ad['purchases']
        by_product[product]['revenue'] += ad['purchase_value']
        by_product[product]['count'] += 1

    for product, data in by_product.items():
        data['roas'] = data['revenue'] / data['spend'] if data['spend'] > 0 else 0

    analysis['by_product'] = dict(by_product)

    # Video vs Image performance
    by_format = {'video': {'spend': 0, 'revenue': 0, 'count': 0},
                 'image': {'spend': 0, 'revenue': 0, 'count': 0}}
    for ad in with_spend:
        fmt = 'video' if ad['has_video'] else 'image'
        by_format[fmt]['spend'] += ad['spend']
        by_format[fmt]['revenue'] += ad['purchase_value']
        by_format[fmt]['count'] += 1

    for fmt, data in by_format.items():
        data['roas'] = data['revenue'] / data['spend'] if data['spend'] > 0 else 0

    analysis['by_format'] = by_format

    # Copy analysis
    copy_patterns = defaultdict(lambda: {'spend': 0, 'revenue': 0, 'count': 0})
    for ad in with_spend:
        elements = extract_copy_elements(ad.get('primary_text'))
        if elements.get('hook_style'):
            style = elements['hook_style']
            copy_patterns[style]['spend'] += ad['spend']
            copy_patterns[style]['revenue'] += ad['purchase_value']
            copy_patterns[style]['count'] += 1

    for style, data in copy_patterns.items():
        data['roas'] = data['revenue'] / data['spend'] if data['spend'] > 0 else 0

    analysis['by_hook_style'] = dict(copy_patterns)

    # Top performers (by spend with good ROAS)
    sorted_by_spend = sorted(with_spend, key=lambda x: x['spend'], reverse=True)
    analysis['top_by_spend'] = sorted_by_spend[:10]

    # Best ROAS (with min spend threshold)
    high_spend = [ad for ad in with_spend if ad['spend'] >= 1000]
    sorted_by_roas = sorted(high_spend, key=lambda x: x['roas'] or 0, reverse=True)
    analysis['top_by_roas'] = sorted_by_roas[:10]

    # Emerging winners (low spend, high ROAS)
    emerging = [ad for ad in with_spend if ad['spend'] < 1000 and (ad['roas'] or 0) > 2.5]
    analysis['emerging_winners'] = sorted(emerging, key=lambda x: x['roas'] or 0, reverse=True)[:5]

    return analysis


def generate_report(analysis: dict, output_path: str):
    """Generate markdown report from analysis."""

    report = f"""# Creative Performance Analysis Report

**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}
**Total Ads Analyzed:** {analysis['total_ads']}
**Ads with Spend (>100 USD):** {analysis['ads_with_spend']}
**Total Spend:** {analysis['total_spend']:,.2f} USD
**Total Revenue:** {analysis['total_revenue']:,.2f} USD
**Overall ROAS:** {analysis['total_revenue'] / analysis['total_spend']:.2f}x

---

## Performance by Creator/Hook Type

| Creator/Hook | Spend | Purchases | ROAS | CPA | Ads |
|--------------|-------|-----------|------|-----|-----|
"""

    # Sort by spend
    sorted_hooks = sorted(analysis['by_hook_type'].items(),
                          key=lambda x: x[1]['spend'], reverse=True)
    for hook, data in sorted_hooks:
        cpa_str = f"{data['cpa']:.0f}" if data['cpa'] else "N/A"
        report += f"| {hook} | {data['spend']:,.0f} | {data['purchases']} | {data['roas']:.2f}x | {cpa_str} | {data['count']} |\n"

    report += """
---

## Performance by Product Type

| Product | Spend | ROAS | Ads |
|---------|-------|------|-----|
"""

    sorted_products = sorted(analysis['by_product'].items(),
                             key=lambda x: x[1]['spend'], reverse=True)
    for product, data in sorted_products:
        report += f"| {product} | {data['spend']:,.0f} | {data['roas']:.2f}x | {data['count']} |\n"

    report += """
---

## Video vs Image Performance

| Format | Spend | ROAS | Ads |
|--------|-------|------|-----|
"""

    for fmt, data in analysis['by_format'].items():
        report += f"| {fmt.title()} | {data['spend']:,.0f} | {data['roas']:.2f}x | {data['count']} |\n"

    report += """
---

## Copy Hook Style Performance

| Hook Style | Spend | ROAS | Ads |
|------------|-------|------|-----|
"""

    sorted_styles = sorted(analysis['by_hook_style'].items(),
                           key=lambda x: x[1]['spend'], reverse=True)
    for style, data in sorted_styles:
        report += f"| {style} | {data['spend']:,.0f} | {data['roas']:.2f}x | {data['count']} |\n"

    report += """
---

## Top Performers by Spend (with ROAS)

| Ad Name | Spend | Purchases | ROAS | CPA |
|---------|-------|-----------|------|-----|
"""

    for ad in analysis['top_by_spend']:
        name = ad['ad_name'][:45]
        cpa = f"{ad['cpa']:.0f}" if ad['cpa'] else "N/A"
        roas = f"{ad['roas']:.2f}x" if ad['roas'] else "N/A"
        report += f"| {name} | {ad['spend']:,.0f} | {ad['purchases']} | {roas} | {cpa} |\n"

    if analysis['emerging_winners']:
        report += """
---

## Emerging Winners (Low Spend, High ROAS)

| Ad Name | Spend | ROAS | Purchases |
|---------|-------|------|-----------|
"""
        for ad in analysis['emerging_winners']:
            name = ad['ad_name'][:45]
            report += f"| {name} | {ad['spend']:,.0f} | {ad['roas']:.2f}x | {ad['purchases']} |\n"

    # Key Insights
    report += """
---

## Key Insights

"""

    # Find best performing hook type
    best_hook = max(sorted_hooks, key=lambda x: x[1]['roas'] if x[1]['spend'] > 5000 else 0)
    report += f"1. **Best Hook/Creator:** {best_hook[0]} with {best_hook[1]['roas']:.2f}x ROAS on {best_hook[1]['spend']:,.0f} USD spend\n\n"

    # Video vs Image insight
    video_roas = analysis['by_format']['video']['roas']
    image_roas = analysis['by_format']['image']['roas']
    better_format = 'Video' if video_roas > image_roas else 'Image'
    report += f"2. **Format:** {better_format} ads perform better ({max(video_roas, image_roas):.2f}x vs {min(video_roas, image_roas):.2f}x ROAS)\n\n"

    # Product insight
    best_product = max(sorted_products, key=lambda x: x[1]['roas'] if x[1]['spend'] > 5000 else 0)
    report += f"3. **Product Focus:** {best_product[0]} drives highest ROAS at {best_product[1]['roas']:.2f}x\n\n"

    # Copy style insight
    if sorted_styles:
        best_style = max(sorted_styles, key=lambda x: x[1]['roas'] if x[1]['spend'] > 1000 else 0)
        report += f"4. **Copy Style:** '{best_style[0]}' hooks perform best at {best_style[1]['roas']:.2f}x ROAS\n\n"

    report += """
---

## Recommended Actions

1. **Scale:** Double down on top-performing creators/hooks
2. **Test:** Create variations of winning copy styles
3. **Replicate:** Use best-performing hook patterns in new creatives
4. **Monitor:** Watch emerging winners for scaling opportunities

---

*Generated by analyze_creatives_performance.py*
"""

    with open(output_path, 'w') as f:
        f.write(report)

    print(f"\nReport saved to: {output_path}")
    return report


def main():
    print("=" * 60)
    print("CREATIVE PERFORMANCE ANALYSIS")
    print("=" * 60)

    # Load data
    performance, creatives = load_latest_files()
    print(f"Loaded {len(performance)} performance records")
    print(f"Loaded {len(creatives)} creative records")

    # Correlate
    correlated = correlate_data(performance, creatives)
    print(f"Correlated {len(correlated)} ads")

    # Analyze
    analysis = analyze_patterns(correlated)

    # Generate report
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    output_path = f".tmp/creative_analysis_{timestamp}.md"
    report = generate_report(analysis, output_path)

    # Print summary to console
    print("\n" + "=" * 60)
    print("QUICK SUMMARY")
    print("=" * 60)

    print(f"\nTotal Spend: {analysis['total_spend']:,.0f} USD")
    print(f"Total Revenue: {analysis['total_revenue']:,.0f} USD")
    print(f"Overall ROAS: {analysis['total_revenue'] / analysis['total_spend']:.2f}x")

    print("\nTop 3 Creators by Spend:")
    sorted_hooks = sorted(analysis['by_hook_type'].items(),
                          key=lambda x: x[1]['spend'], reverse=True)[:3]
    for hook, data in sorted_hooks:
        print(f"  - {hook}: {data['spend']:,.0f} USD, {data['roas']:.2f}x ROAS")

    print("\nBest ROAS (min 5k spend):")
    best = [(h, d) for h, d in analysis['by_hook_type'].items() if d['spend'] >= 5000]
    best = sorted(best, key=lambda x: x[1]['roas'], reverse=True)[:3]
    for hook, data in best:
        print(f"  - {hook}: {data['roas']:.2f}x ROAS on {data['spend']:,.0f} USD")

    print("\n" + "=" * 60)
    print("Done! Full report saved to:", output_path)
    print("=" * 60)


if __name__ == "__main__":
    main()

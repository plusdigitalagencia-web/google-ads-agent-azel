# Directive: Google Ads Campaign Audit

## Goal
Perform a complete audit of a Google Ads account — metrics, keywords, search terms, and ad creatives — and deliver actionable recommendations.

## Inputs
- `customer_id`: The Google Ads account ID (without dashes)
- `days`: Date range for analysis (default: 30)
- `focus`: Optional — "search", "pmax", or "all"

## Steps

### 1. Get account overview
```bash
python3 execution/google_ads_metrics_reader.py --customer-id CUSTOMER_ID --days 30
```
Look for:
- Campaigns with high spend and low/zero conversions
- ROAS below 2x (red flag)
- CTR below 2% on Search (red flag)
- Impression share below 40% (opportunity to scale)

### 2. Analyze keywords
```bash
python3 execution/google_ads_keyword_analyzer.py --customer-id CUSTOMER_ID --days 30
```
Look for:
- Keywords with Quality Score ≤ 4 (fix landing page or ad relevance)
- Keywords spending > R$50 with zero conversions (pause or add negatives)
- Keywords with high CTR but low conversion (landing page problem)

### 3. Analyze search terms (find money leaks)
```bash
python3 execution/google_ads_search_terms.py --customer-id CUSTOMER_ID --days 30 --min-cost 10
```
Look for:
- Terms clearly unrelated to the business → add as exact negatives
- Terms with high spend, zero conversions → add as negatives or investigate
- Terms that convert well → add as exact match keywords

### 4. Audit ad creatives
```bash
python3 execution/google_ads_ad_auditor.py --customer-id CUSTOMER_ID --days 30
```
Look for:
- RSAs with "Poor" or "Average" ad strength → rewrite headlines/descriptions
- RSAs with fewer than 10 headlines → add more variety
- PMax asset groups with weak strength → add more assets
- Missing extensions (sitelinks, callouts, structured snippets)

## Output Format
Deliver findings as:
1. **Priority fixes** (sorted by estimated money saved/recovered)
2. **Growth opportunities** (keywords to add, bids to raise)
3. **Creative improvements** (specific ad rewrites)

## Edge Cases
- If campaign has < 100 clicks, data may be statistically insignificant — note this
- PMax campaigns hide keyword-level data by design — focus on asset group strength and search terms
- Quality Score is only shown for keywords that have enough data; "n/d" means insufficient traffic

# Directive: Pull Meta Ads Performance

**Purpose:** Automatically fetch ad performance data and creatives from Meta Marketing API.

**When to use:**
- Weekly performance reviews
- Before generating new ad concepts (to understand what's working)
- When user asks "what's performing?" or "analyze my ads"

---

## Prerequisites

### One-Time Setup

1. **Generate Access Token:**
   - Go to developers.facebook.com/tools/explorer
   - Select your app (or create one if needed)
   - Add permission: `ads_read`
   - Click "Generate Access Token"
   - Token expires in ~60 days - will need refresh

2. **Get Ad Account ID:**
   - Go to Meta Business Suite > Settings > Ad Accounts
   - Copy the account ID (format: `act_123456789`)

3. **Add to .env:**
   ```
   META_ACCESS_TOKEN=your_access_token
   META_AD_ACCOUNT_ID=act_123456789
   ```

4. **Install dependencies:**
   ```bash
   pip install facebook-business python-dotenv requests
   ```

---

## Execution Steps

### Step 1: Pull Performance Data

```bash
python execution/meta_ads_fetcher.py --action performance --days 30
```

**What it fetches:**
- All ads from the last N days
- Spend, impressions, clicks, CTR, CPC
- Purchases, purchase value, CPA, ROAS
- Reach, frequency
- Video metrics (if applicable): 25%, 50%, 75%, 100% watched

**Output:**
- `.tmp/meta_performance_[timestamp].json` - Raw data
- `.tmp/meta_analysis_[timestamp].md` - Formatted report

### Step 2: Pull Ad Creatives (Optional)

**IMPORTANT: Always filter by specific ad IDs. NEVER pull all creatives.**

```bash
# CORRECT - fetch only the ads you need:
python execution/meta_ads_fetcher.py --action creatives --ad-ids "123456789,987654321"

# WRONG - do NOT run without --ad-ids (downloads ALL ads, wastes time/space):
# python execution/meta_ads_fetcher.py --action creatives
```

**Workflow:**
1. First pull performance data to identify which ads you want to analyze
2. Get the ad IDs from the performance JSON or report
3. Then fetch creatives for only those specific ads

**What it fetches:**
- Thumbnail and full images
- Video files
- Ad copy (primary text, headline, description)
- Call-to-action

**Output:**
- `.tmp/meta_creatives_[timestamp].json` - Metadata
- `.tmp/meta_creatives/[ad_id]/` - Downloaded assets

### Step 3: Pull Everything

**AVOID using `--action all` unless you have a specific reason.** It downloads creatives for every ad, which is slow and wasteful. Instead:

1. Pull performance first: `--action performance`
2. Identify ads of interest
3. Pull only those creatives: `--action creatives --ad-ids "..."`

```bash
# Only use this for initial audit or if you truly need everything:
python execution/meta_ads_fetcher.py --action all --days 30
```

---

## Analysis Flow

After pulling data, run analysis:

1. **Identify top spenders** (these are Meta's predicted winners - DON'T turn off)
2. **Find patterns:**
   - Which hook types perform best?
   - Which creator/format works?
   - Which angles convert?
3. **Identify opportunities:**
   - Low spend + good metrics = emerging winners
   - High spend + bad metrics = investigate (but don't turn off immediately)
4. **Document winners** for iteration

---

## Metrics Reference

| Metric | What It Means | Good Benchmark |
|--------|---------------|----------------|
| CTR | Click-through rate | >1% is good |
| CPC | Cost per click | Lower is better |
| CPA | Cost per acquisition | Depends on AOV |
| ROAS | Return on ad spend | >2x breakeven typical |
| Hook rate | % watched 3+ seconds | >30% is good |
| Hold rate | % watched 50%+ | >10% is good |
| Frequency | Avg times seen per person | <3 ideal, >5 = fatigue |

---

## Common Issues

### Token Expired
```
Error: Invalid OAuth access token
```
**Fix:** Generate a new access token in Meta Developer portal and update .env

### No Data Returned
```
No ads found for date range
```
**Fix:** Check that ads were running during the date range, and account ID is correct

### Permission Denied
```
Error: (#10) Permission denied
```
**Fix:** Ensure access token has `ads_read` permission

---

## Automation Options

### Scheduled Pulls (Future)

Could set up:
- Daily pull at 6am
- Weekly summary email
- Alert if CPA spikes >20%

### Webhook Trigger (Future)

Could trigger on:
- "Analyze my ads"
- "What's performing?"
- "Weekly review"

---

## Learnings

- **2026-01-13:** Never fetch all creatives. Always use `--ad-ids` to filter to specific ads. Fetching all 72+ ads downloads 500+ folders and 40MB+ of assets that mostly go unused. Pull performance first, identify the ads you care about, then fetch only those creatives.

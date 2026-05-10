# Directive: Review Ad Performance

**Purpose:** Analyze ad performance data and generate optimization recommendations.

**When to use:** Weekly performance review, or when performance drops.

---

## CRITICAL WARNINGS

1. **Before blaming creative, ask:** "Did ANYTHING change on the website?" Homepage hero, checkout flow, pricing, shipping — these often cause "creative problems."

2. **NEVER TURN OFF TOP SPENDERS:** The system spends on an ad because it predicts best overall performance. Turning off top spenders creates a death spiral.

**What happens when you turn off top spenders:**
1. Next ad becomes top spender
2. That ad looks bad (it wasn't predicted to scale)
3. You turn that off too
4. Race to the bottom
5. You scream "we need more creative" — self-fulfilling prophecy

**Exception:** Only if it's been running < 2 days and clearly tanking.

---

## Automated Flow (Preferred)

### Step 1: Pull Data from Meta

```bash
# Pull last 30 days of performance + creatives
python execution/meta_ads_fetcher.py --action all --days 30
```

**Outputs:**
- `.tmp/meta_performance_[timestamp].json`
- `.tmp/meta_creatives_[timestamp].json`
- `.tmp/meta_creatives/[ad_id]/` (downloaded assets)

### Step 2: Analyze Creatives

```bash
# Transcribe videos, classify scripts, find patterns
python execution/analyze_ad_creatives.py \
  --performance .tmp/meta_performance_[timestamp].json \
  --creatives .tmp/meta_creatives_[timestamp].json
```

**Outputs:**
- `.tmp/creative_analysis_[timestamp].json` - Detailed per-ad analysis
- `.tmp/creative_patterns_[timestamp].md` - Pattern report

### Step 3: Review & Recommend

Read the generated reports and:
1. Identify top performers (protect these)
2. Find patterns in what's working
3. Generate iteration recommendations
4. Update winners library

---

## Manual Flow (If API Not Connected)

### Step 1: Export from Meta Ads Manager

1. Go to Meta Ads Manager
2. Select date range (last 30 days recommended)
3. Columns to include:
   - Ad name, Ad ID
   - Amount spent
   - Purchases, Purchase conversion value
   - CPA, ROAS
   - CTR, CPC
   - Impressions, Reach, Frequency
   - Video metrics if applicable
4. Export as CSV
5. Save to `.tmp/meta_export.csv`

### Step 2: Run Analysis

```bash
python execution/performance_analyzer.py --input .tmp/meta_export.csv
```

---

## Pre-Analysis Checklist

Before analyzing, ask the user:
- [ ] Did anything change on the website recently?
- [ ] Any pricing or offer changes?
- [ ] Any shipping/fulfillment issues?
- [ ] Any major external events (competitor sale, etc.)?

---

## CRITICAL: What to Analyze

**Images and videos are 95% of what matters.** Ad copy is ~5% importance. Never spend time analyzing copy patterns, bullet formats, or text hooks. The creative (visual) is what stops the scroll and drives performance.

**Only analyze high-spend ads.** If an ad has low spend, it means Meta's algorithm doesn't see an opportunity to spend on it. Low spend = algorithm has already decided it's not a winner. Focus exclusively on ads in the upper echelon of spend.

**There are no "emerging winners" with low spend.** If the algorithm isn't spending on it, it's not a winner. Period.

---

## Analysis Framework

### 1. TOP PERFORMERS (Protect & Analyze)

Identify ads with highest spend. These are Meta's predicted winners.

**Focus your analysis here:**
- Download and watch/view the actual video/image creative
- What's in the first 3 seconds? (hook visual)
- What's the format? (UGC, produced, screenshot, etc.)
- Who's in it? (creator type, demographic)
- What's the visual style? (lighting, setting, pace)

Do NOT analyze copy. Analyze visuals.

### 2. UNDERPERFORMERS (Learn from these)

Ads with spend but poor metrics. Don't just turn off — understand why:
- Hook not working? (check 3-sec view rate)
- Not holding attention? (check 50% view rate)
- Not converting? (good CTR but bad CPA = landing page issue?)

### 3. PATTERN ANALYSIS (Visual Only)

Across top-spending ads, identify:
- Best performing visual hook (first 3 seconds)
- Best performing format (video vs static, UGC vs produced)
- Best performing creator type/demographic
- Common visual elements (setting, lighting, pacing)

### 5. ITERATION RECOMMENDATIONS

Based on patterns:
- What to double down on (more of what works)
- What to stop (patterns that consistently fail)
- What to test (gaps in current creative)

---

## Output Format

Save to: `.tmp/performance_review_[date].md`

```markdown
## Performance Review: [Date Range]

### Pre-Check
- Website changes: [Yes/No - details]
- Offer changes: [Yes/No - details]

### Top Performers (DO NOT TURN OFF)
| Ad Name | Spend | CPA | ROAS | Why It Works |
|---------|-------|-----|------|--------------|
| [ad 1]  | $X    | $X  | X.Xx | [reason]     |
| [ad 2]  | $X    | $X  | X.Xx | [reason]     |

### Emerging Winners (Monitor closely)
| Ad Name | Spend | CPA | ROAS | What's Unique |
|---------|-------|-----|------|---------------|
| [ad 1]  | $X    | $X  | X.Xx | [reason]      |

### Underperformers (Hypotheses)
| Ad Name | Spend | CPA | ROAS | Hypothesis |
|---------|-------|-----|------|------------|
| [ad 1]  | $X    | $X  | X.Xx | [reason]   |

### Pattern Analysis
- Best hook type: [type]
- Best format: [format]
- Best angle: [angle]
- Best creator type: [type]

### Recommendations
**Do More:**
1. [action]
2. [action]

**Stop Doing:**
1. [action]

### Add to Winners Library
- [Ad name]: [Why it worked - for future reference]
```

---

## Metrics Reference

| Metric | What It Means | Good Benchmark |
|--------|---------------|----------------|
| CTR | Click-through rate | >1% |
| CPC | Cost per click | Varies by niche |
| CPA | Cost per acquisition | < 1/3 of AOV |
| ROAS | Return on ad spend | >2x breakeven |
| Hook rate | 3-sec view rate | >30% |
| Hold rate | 50%+ watched | >10% |
| Frequency | Times seen per person | <3 ideal |

---

## Tools

- `execution/meta_ads_fetcher.py` - Pull data from Meta API
- `execution/analyze_ad_creatives.py` - Analyze creative patterns
- `execution/performance_analyzer.py` - Analyze CSV exports (manual flow)

---

## Success Criteria

- [ ] Data pulled successfully
- [ ] Top performers identified and protected
- [ ] Clear patterns documented
- [ ] Actionable recommendations generated
- [ ] Winners added to library for future reference

---

## Learnings

<!-- Update this section with patterns you discover -->

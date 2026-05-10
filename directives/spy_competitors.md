# Directive: Spy on Competitors

**Purpose:** Extract top-performing competitor ads from ad libraries.

**When to use:** Want to see what's working in your space.

---

## CRITICAL WARNING

**Sort by engagement (shares, comments), NOT by "longest running."** People run losers at $1/day to mislead competitors.

---

## Inputs Required
- List of competitor names
- Platform focus (Meta, TikTok, both)

## Execution Steps

### Step 1: Pull Competitor Ads

For each competitor:
1. Search Meta Ad Library: facebook.com/ads/library
2. Search AdSpy (if available): filter by competitor name
3. Search TikTok Creative Center

Collect:
- Top 10 ads by engagement metrics
- Screenshot statics
- Save video URLs for transcription

### Step 2: Analyze Patterns

Use this prompt:

```
Analyze these competitor ads and identify patterns:

1. HOOK ANALYSIS
   - What hooks do they use most?
   - First 3 seconds breakdown of top 5 ads

2. FORMAT PATTERNS
   - Talking head vs. B-roll vs. screen recording?
   - UGC style vs. produced?
   - Static vs. video ratio?

3. MESSAGING PATTERNS
   - What pain points do they hit?
   - What benefits do they emphasize?
   - What proof do they use?

4. CTA PATTERNS
   - What offers do they push?
   - How do they create urgency?

5. GAPS & OPPORTUNITIES
   - What are they NOT saying?
   - What angles are missing?
   - What could we do differently?
```

## Output Format

Save to: `.tmp/competitor_analysis_[date].md`

```markdown
## Competitor Analysis: [Industry/Niche]

### Competitors Analyzed
1. Brand A - [X] active ads
2. Brand B - [X] active ads
3. Brand C - [X] active ads

### Hook Patterns (Most Common)
1. Problem statement: "If you have [body type]..." (X%)
2. Failed solution: "I've tried every brand..." (X%)
3. POV format: "POV: Finding [product] that..." (X%)
4. Myth buster: "Everyone says [X] but..." (X%)

### Format Patterns
- X% talking head UGC
- X% founder/lifestyle
- X% static images
- Avg length: X seconds

### Messaging Patterns
- Pain: [most mentioned] (X% of ads)
- Benefit: [primary], [secondary]
- Proof: [type most common]

### Gaps & Opportunities
- [Gap 1]
- [Gap 2]
- [Gap 3]
```

## Tools
- `execution/adspy_fetcher.py` (if available)
- Meta Ad Library (manual)
- TikTok Creative Center

## Success Criteria
- Minimum 3 competitors analyzed
- At least 10 ads per competitor reviewed
- Clear patterns documented
- Gaps and opportunities identified

## Learnings
<!-- Update this section as you learn about competitor strategies -->

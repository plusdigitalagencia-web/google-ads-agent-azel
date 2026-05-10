# Directive: Mine Reddit Insights

**Purpose:** Extract authentic customer language from Reddit for use in ad copy.

**When to use:** Starting fresh, need to understand how customers talk about the problem.

---

## Inputs Required
- Product category
- Main problem the product solves
- Competitor names (optional)
- Target subreddits (optional)

## Execution Steps

### Step 1: Search Reddit

Search these queries:
- "[product category] reddit"
- "[main problem] reddit"
- "[competitor name] review reddit"
- "best [product category] reddit"
- "[product category] worth it reddit"

### Step 2: Extract Language

Use this prompt to analyze found content:

```
I'm analyzing Reddit posts about [TOPIC]. Extract the following:

1. PAIN POINTS - Exact phrases people use to describe their frustration
   Look for: "I'm so sick of...", "The worst part is...", "I can't stand..."

2. DESIRED OUTCOMES - What they wish they had
   Look for: "I just want...", "All I need is...", "If only..."

3. OBJECTIONS - Why they haven't bought yet
   Look for: "But...", "The problem with X is...", "I would but..."

4. EMOTIONAL WORDS - How they describe their feelings
   Look for adjectives, metaphors, complaints

5. SPECIFIC DETAILS - Numbers, timeframes, situations
   Look for: "Every morning I...", "For 3 years I've...", "Whenever I try to..."

Format as a list of exact quotes with source links.
```

## Output Format

Save to: `.tmp/customer_language_[brand].md`

```markdown
## Customer Language: [Brand]

### Pain Points
- "[exact quote 1]" (r/subreddit)
- "[exact quote 2]" (r/subreddit)
- "[exact quote 3]" (r/subreddit)

### Desired Outcomes
- "[exact quote 1]"
- "[exact quote 2]"

### Objections
- "[brand/solution] - why it failed"

### Emotional Words
- "embarrassing", "frustrated", "gave up", "uncomfortable all day"

### Specific Details
- "Every time I sit down at my desk..."
- "I've returned 6 pairs in the last month"

### Key Insight
[One sentence summary of what you learned]
```

## Tools
- `execution/reddit_scraper.py` (if available)
- Manual web search as fallback
- GigaBrain for Reddit search

## Success Criteria
- Minimum 10 exact customer quotes
- At least 3 pain points identified
- At least 2 objections captured
- Emotional language documented

## Learnings
<!-- Update this section as you discover API limits, timing issues, or better approaches -->

# Directive: Google Ads Keyword Opportunities

## Goal
Find the best keyword opportunities for an account — new terms to add, underperforming ones to fix, and wasted spend from bad match types.

## Inputs
- `customer_id`: Google Ads account ID
- `seed_keywords`: 3–10 keywords related to the business (for Keyword Planner)
- `days`: Analysis period (default: 30)

## Steps

### 1. Analyze existing keywords
```bash
python3 execution/google_ads_keyword_analyzer.py --customer-id CUSTOMER_ID --days 30
```

### 2. Find new keyword ideas
```bash
python3 execution/google_ads_keyword_analyzer.py --customer-id CUSTOMER_ID --new-ideas "keyword1" "keyword2" "keyword3"
```
Filter results:
- **Good opportunity**: Volume > 100/month + Competition LOW or MEDIUM + CPC within budget
- **Skip**: Volume < 50/month OR Competition HIGH with CPC > budget
- **Priority**: Keywords the account doesn't have yet that competitors likely use

### 3. Cross-reference search terms with keywords
Compare what people actually searched (search terms report) vs what keywords are active.
Terms with conversions that don't have a matching exact-match keyword → add them as exact match.

### 4. Analyze match type distribution
```bash
python3 execution/google_ads_search_terms.py --customer-id CUSTOMER_ID --days 30
```
- Too many broad match keywords → high irrelevant spend
- Too many exact match only → missing volume
- Ideal mix: anchor with exact, scale with phrase, test with broad+smart bidding

## Output
- List of new keywords to add (with suggested match type and bid)
- List of existing keywords to pause or fix
- List of search terms to promote to keywords (exact match)
- Recommended negative keywords

## Notes
- Keyword Planner requires the account to have billing active (even if not spending)
- Location ID 1001767 = Brazil, Language ID 1014 = Portuguese (pt)
- Volume data refreshes monthly — don't re-run more than once per week

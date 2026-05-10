# Directive: Prepare Q4 Strategy

**Purpose:** Prepare creative strategy for Q4/Black Friday based on historical data.

**When to use:** 4-6 weeks before Q4 push.

---

## KEY INSIGHT

"Don't reinvent the wheel in Q4. Take last year's winners, get them re-recorded, add offer overlays."

---

## Inputs Required
- Last year's Q4 performance data
- Current year-to-date winners
- Motion reports (if available)
- Planned offers/promotions

## Execution Steps

### Step 1: Pull Historical Data

Pull these reports from Motion (or your analytics):
1. Top Q4 Ad Types from last year
2. Top Q4 Angles from last year
3. Top Q4 Individual Ads from last year
4. Year-to-Date Winners (current year)

### Step 2: Analyze and Plan

Use this prompt:

```
## Historical Analysis

Pull these reports from Motion (or your analytics):
1. Top Q4 Ad Types from last year
2. Top Q4 Angles from last year
3. Top Q4 Individual Ads from last year
4. Year-to-Date Winners (current year)

## Questions to Answer:

1. WHAT WORKED LAST Q4
   - Top 5 ads by spend
   - What format/angle/message?

2. WHAT'S WORKING THIS YEAR
   - Current top performers
   - Which could scale during Q4?

3. AUDIENCE SHIFT FOR GIFTING
   - Who buys this as a gift?
   - Do we need different creator demographics?
   - (e.g., Female creators for male products during gifting season)

4. ITERATION OPPORTUNITIES
   - Which winners should we re-record?
   - Which need offer overlays?

## Output: Q4 Creative Plan

### Ads to Re-Record
[List ads + new creator specs]

### Ads to Add Offer Overlays
[List ads + offer copy]

### New Concepts to Test
[Based on gaps identified]

### Creator Recommendations
[Demographic shifts for gifting]
```

## Output Format

Save to: `.tmp/q4_strategy_[year].md`

```markdown
## Q4 Creative Strategy [Year]

### Timeline
- Creative production deadline: [date]
- Testing period: [dates]
- Scale period: [dates]

---

### Last Year's Winners (To Re-Record)

| Ad Name | Last Year Spend | CPA | New Creator Spec |
|---------|-----------------|-----|------------------|
| [ad 1]  | $X              | $X  | [spec]           |
| [ad 2]  | $X              | $X  | [spec]           |

### Current Winners (To Add Offer Overlays)

| Ad Name | YTD Spend | CPA | Offer Copy |
|---------|-----------|-----|------------|
| [ad 1]  | $X        | $X  | "[copy]"   |
| [ad 2]  | $X        | $X  | "[copy]"   |

### Gifting Angle Additions

**Target:** [Who buys as gift - e.g., wives buying for husbands]
**Creator shift:** [e.g., Female creators for male products]
**New scripts needed:**
1. [Gift-focused script concept]
2. [Gift-focused script concept]

### New Concepts to Test

Based on gaps from last year:
1. [Concept]
2. [Concept]
3. [Concept]

### Production Checklist

- [ ] Re-record [X] winning scripts with new creators
- [ ] Add offer overlays to [X] current winners
- [ ] Create [X] new gifting-angle scripts
- [ ] Test new concepts by [date]

### Budget Allocation Recommendation

- Re-recorded winners: X%
- Offer overlay versions: X%
- New concepts: X%
- Gifting angles: X%
```

## Tools
- `execution/motion_report_generator.py` (if available)
- Manual export from Motion/analytics platform

## Success Criteria
- Historical winners identified
- Re-record list created with specs
- Offer overlay versions planned
- Gifting angle addressed
- Clear timeline established

## Learnings
<!-- Update this section after Q4 with what worked -->

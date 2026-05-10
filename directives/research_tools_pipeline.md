# Directive: Research Tools Pipeline

**Purpose:** Run structured customer research using free tools.

**When to use:** Starting with a new brand/niche, or going deeper on an existing one.

---

## The Research Stack (Run In Order)

### Step 1: Google Trends

**URL:** trends.google.com

**Search:** [product category]

**Answer:**
- Is this market growing or shrinking?
- When do searches peak? (Seasonality)
- What related queries are rising?

**Output:**
```markdown
### Google Trends Summary
- Trend direction: [Growing/Stable/Shrinking]
- Peak months: [months]
- Rising queries: [list]
```

---

### Step 2: Google Keywords

**Tool:** Keyword Planner or Ubersuggest

**Search:** [main keywords]

**Answer:**
- How many people search for this monthly?
- What's the buyer intent? (informational vs. transactional)
- What related keywords have high volume?

**Output:**
```markdown
### Keyword Research Summary
- Main keyword volume: [X]/month
- Buyer intent level: [High/Medium/Low]
- High-volume related keywords:
  - [keyword]: [volume]
  - [keyword]: [volume]
```

---

### Step 3: Answer The Public

**URL:** answerthepublic.com

**Search:** [product/problem]

**Answer:**
- What questions do people ask?
- Are questions basic or advanced? (Education level)
- What "vs" comparisons exist? (Competitors)

**Key Insight:** If you see doctor terminology = high-educated customer. If you see "does this work?" = low-educated customer (requires more education in ads).

**Output:**
```markdown
### Answer The Public Summary
- Customer education level: [High/Medium/Low]
- Top questions:
  - [question]
  - [question]
- "Vs" comparisons (competitors):
  - [brand vs brand]
```

---

### Step 4: Pinterest Trends

**URL:** trends.pinterest.com

**Search:** [product/problem]

**Answer:**
- What content gets pinned? (Tutorials, products, lifestyle)
- What aesthetic resonates?
- Is this a visual category or informational?

**Key Insight:** Women hold 60-80% of US purchasing power and primarily use Pinterest. If tutorials dominate → test tutorial-style ads.

**Output:**
```markdown
### Pinterest Trends Summary
- Dominant content type: [Tutorials/Products/Lifestyle]
- Aesthetic: [description]
- Ad format implication: [what to test]
```

---

### Step 5: Reddit

**Method:** GigaBrain or search "[problem] site:reddit.com"

**Answer:**
- How do people describe the problem?
- What solutions have they tried?
- What do they wish existed?

**Output:**
```markdown
### Reddit Research Summary
- Problem language: [how they describe it]
- Failed solutions: [what they've tried]
- Desires: [what they wish existed]
- Key subreddits: [list]
```

---

### Step 6: TikTok Symphony (If Available)

**Tool:** TikTok Symphony Creative Assistant

**Use to:**
- Find trending content in niche
- See what formats perform
- Identify creator styles that work

**Output:**
```markdown
### TikTok Research Summary
- Trending formats: [list]
- Top creator styles: [description]
- Sounds to consider: [if any]
```

---

## Final Output

Compile into: `.tmp/research_summary_[brand].md`

```markdown
## Research Summary: [Brand/Product]

### Market Status
- Growing/Stable/Shrinking
- Seasonality: [peak months]

### Customer Education Level
- High/Medium/Low
- Implications: [need more education in ads? or go straight to product?]

### Key Customer Language
- Pain phrases: [list]
- Desire phrases: [list]
- Objection phrases: [list]

### Content Formats That Work
- [Format 1]: [why]
- [Format 2]: [why]

### Competitors to Watch
- [Competitor 1]: [known for]
- [Competitor 2]: [known for]

### Recommended First Tests
1. [Angle/format to test first]
2. [Angle/format to test second]
3. [Angle/format to test third]
```

## Key Example

**Case study from source material:**
Client couldn't scale "nootropic coffee" ads. Research showed nobody searches "nootropic" — switched to "mushroom coffee" (layman's term). Ads worked overnight.

**Lesson:** Use the words customers use, not industry jargon.

## Success Criteria
- All 6 research steps completed
- Customer education level determined
- Key phrases documented
- Content format recommendations made
- At least 3 test angles identified

## Learnings
<!-- Update this section with research insights and what worked -->

# Directive: Iterate Winning Ad

**Purpose:** Generate iteration variations of a proven winning ad.

**When to use:** You have a winner and want to squeeze more juice from it.

---

## PHILOSOPHY

**Prefer conceptual iteration (doubling down) over scientific iteration (metric tweaking).**

### Conceptual iteration (PREFERRED):
- Same script, different creator
- Same message, different format
- Same hook, different body

### Scientific iteration (LESS PREFERRED):
- Change hook to improve hook rate
- Change CTA to improve CTR

**Why conceptual is better:** Scientific iteration assumes controlled experiments. But Meta doesn't serve the same ad to the same people — so your "test" isn't controlled anyway.

---

## The Reshot Rule

"Getting an ad reshot by a different creator IS iteration — a massive one."

If you have a winning script:
1. Get it reshot by someone who represents a different segment of your audience
2. This should OUTPERFORM the original (you're applying expertise to proven concept)
3. Don't be afraid to use the same creator repeatedly if they work — use them until they stop working

---

## Inputs Required
- Winning ad script or description
- Performance data (Spend, CPA, CTR, etc.)
- Brand context

## Execution Steps

### Step 1: Document the Winner

Capture:
- Full script/transcript
- Performance metrics
- What we think made it work

### Step 2: Generate Iterations

Use this prompt:

```
Here's our winning ad:

[Paste winning script or describe the ad]

Performance: [Spend, CPA, CTR, etc.]

## Generate 8 iteration concepts:

### CREATOR VARIATIONS (3)
Same script, different creator type:
1. Different age bracket
2. Different demographic
3. Different energy level/vibe

### HOOK VARIATIONS (2)
Same body/CTA, different opening:
1. Alternative hook #1
2. Alternative hook #2

### FORMAT VARIATIONS (2)
Same message, different medium:
1. As a static image (what headline?)
2. As a different video format (talking head → B-roll, etc.)

### ANGLE VARIATION (1)
Same benefit, different emotional approach

## For each, explain:
- What we're testing
- Why it might outperform
- Creator brief (if applicable)
```

## Output Format

Save to: `.tmp/iterations_[ad_name]_[date].md`

```markdown
## Iteration Plan: [Winning Ad Name]

### Original Performance
- Spend: $X
- CPA: $X
- ROAS: X.Xx
- Why it worked: [analysis]

---

### Creator Variation 1: [Description]
**What we're testing:** [variable]
**Why it might outperform:** [hypothesis]
**Creator Brief:**
- Age: [range]
- Demo: [description]
- Energy: [level]
- Notes: [any specific instructions]

### Creator Variation 2: [Description]
[Same format]

### Creator Variation 3: [Description]
[Same format]

---

### Hook Variation 1
**Original hook:** "[hook]"
**New hook:** "[hook]"
**What we're testing:** [variable]
**Why it might outperform:** [hypothesis]

### Hook Variation 2
[Same format]

---

### Format Variation 1: Static
**Headline:** "[headline]"
**Visual concept:** [description]
**What we're testing:** [variable]

### Format Variation 2: [New video format]
**Format:** [description]
**What we're testing:** [variable]

---

### Angle Variation
**Original angle:** [emotion/approach]
**New angle:** [emotion/approach]
**Script adjustment:** [what changes]
**Why it might outperform:** [hypothesis]
```

## Success Criteria
- 8 iteration concepts generated
- Each has clear hypothesis
- Creator briefs actionable for production
- Maintains what worked in original

## Learnings
<!-- Update this section with which iteration types work best -->

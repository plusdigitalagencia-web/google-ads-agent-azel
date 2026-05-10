# Directive: Generate Ad Scripts

**Purpose:** Generate ad scripts using researched insights and proven structures.

**When to use:** You've completed research, now need to create scripts.

---

## CRITICAL RULE

**Never ask AI to "be creative."** Ask it to pattern-match against winners and adapt.

---

## Inputs Required
- `context/brand_context.md` - Brand information
- Customer language extract (from Reddit mining)
- Top performing examples (3-5 winning scripts)

## Execution Steps

### Step 1: Verify Prerequisites

Before generating, ensure you have:
1. **Brand Context** (created in onboarding)
2. **Customer Language Extract** (from mine_reddit_insights)
3. **Top Performing Examples** (from user or competitor research)

### Step 2: Generate Scripts

Use this master prompt:

```
You are a direct-response copywriter specializing in paid social ads.

## Your Rules:
1. Sound like a CUSTOMER talking to another customer, not a brand
2. Use the EXACT phrases from the customer research below
3. Be specific, not vague ("I lost 12 lbs" not "I feel better")
4. Hook must pattern-interrupt in <3 seconds
5. Never sound like an ad - sound like content

## Brand Context:
[Paste brand_context.md]

## Customer Research (USE THESE EXACT PHRASES):
[Paste customer language extract]

## Top Performing Examples to Pattern-Match:
[Paste 3-5 winning scripts]

## Write 5 Scripts

For each script, include:
- TYPE: [Problem-Solution / Testimonial / Myth Buster / Investigation / Before-After]
- TARGET: [Who specifically this speaks to]
- INSPIRED BY: [Which customer phrase sparked this]

Then write:
- HOOK (0-3 sec): [Pattern interrupt]
- PROBLEM (3-10 sec): [Agitate using their words]
- SOLUTION (10-20 sec): [Introduce product naturally]
- PROOF (20-25 sec): [Specific result/benefit]
- CTA (25-30 sec): [Clear next step]

## Script Types to Create:
1. Problem-Solution - Start with the pain, introduce product as solution
2. Testimonial - First person "I tried everything until..."
3. Myth Buster - "Everyone says X, but here's the truth..."
4. Investigation Arc - "I saw this expert say [X], so I tried..."
5. Before/After - "6 months ago I was [state], now..."
```

## Output Format

Save to: Google Doc or `.tmp/scripts_[brand]_[date].md`

```markdown
## Script 1: [Type] - "[Working Title]"

**Type:** [Script type]
**Target:** [Who specifically this speaks to]
**Inspired by:** [Which customer phrase sparked this]

---

**HOOK (0-3 sec):**
"[Opening line]"

**PROBLEM (3-10 sec):**
"[Agitate the pain using their words]"

**SOLUTION (10-20 sec):**
"[Introduce product naturally]"

**PROOF (20-25 sec):**
"[Specific result/benefit]"

**CTA (25-30 sec):**
"[Clear next step]"

---

**Creator Notes:**
- Tone: [casual/energetic/calm/etc.]
- Setting: [where to film]
- Props needed: [if any]
- Demo: [what to show]
```

## Script Types Reference

1. **Problem-Solution** - Start with the pain, introduce product as solution
2. **Testimonial** - First person "I tried everything until..."
3. **Myth Buster** - "Everyone says X, but here's the truth..."
4. **Investigation Arc** - "I saw this expert say [X], so I tried..."
5. **Before/After** - "6 months ago I was [state], now..."

## Success Criteria
- 5 scripts generated
- Each uses exact customer language
- Each has clear hook, problem, solution, proof, CTA
- Creator notes included for production

## Learnings
<!-- Update this section with what script types perform best -->

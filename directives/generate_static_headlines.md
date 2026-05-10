# Directive: Generate Static Headlines

**Purpose:** Generate headline variations for static ad images.

**When to use:** Need static ads, or testing messaging before producing video.

---

## CRITICAL RULE

**Always write for COLD audiences.** Cold-audience headlines work for warm too. Warm-audience headlines don't work for cold.

### BAD (Warm/Vague):
- "I feel like a new person"
- "Finally, jeans that fit"
- "My new favorite jeans"

### GOOD (Cold/Specific):
- "Jeans for guys who've ripped 3 pairs this year"
- "Finally, jeans you can squat in"
- "If you have thighs, you need these"

---

## Inputs Required
- Product name
- Target audience
- Main benefit
- Customer language (from research)

## Execution Steps

### Step 1: Generate Headlines

Use this prompt:

```
Generate 20 headlines for a static ad.

## Product: [Product name]
## Target: [Who specifically]
## Main Benefit: [Primary value prop]
## Customer Language: [Key phrases from research]

## Rules:
1. Write for COLD audiences (assume they don't know you)
2. Be specific, not vague
3. Use customer language, not marketing speak
4. Each headline should make ONE clear point
5. Max 10 words per headline

## Generate 4 headlines in each category:

1. PROBLEM-FIRST
   Start with the pain they're experiencing.
   Example: "Jeans that rip when you squat? Same."

2. BENEFIT-FIRST
   Lead with what they get.
   Example: "Squat. Sit. Move. These jeans won't rip."

3. CURIOSITY
   Make them want to learn more.
   Example: "What 47,000 guys with big thighs already know"

4. SOCIAL PROOF
   Use numbers and credibility.
   Example: "47,000 5-star reviews from guys who lift"

5. DIRECT CALL-OUT
   Name the audience explicitly.
   Example: "For guys who've given up on finding jeans"
```

## Output Format

Save to: `.tmp/headlines_[brand]_[date].md`

```markdown
## Headlines: [Brand/Product]

### Problem-First
1. "[headline]"
2. "[headline]"
3. "[headline]"
4. "[headline]"

### Benefit-First
5. "[headline]"
6. "[headline]"
7. "[headline]"
8. "[headline]"

### Curiosity
9. "[headline]"
10. "[headline]"
11. "[headline]"
12. "[headline]"

### Social Proof
13. "[headline]"
14. "[headline]"
15. "[headline]"
16. "[headline]"

### Direct Call-Out
17. "[headline]"
18. "[headline]"
19. "[headline]"
20. "[headline]"

### Top 5 Recommendations (for cold acquisition):
1. "[headline]" - [why this one]
2. "[headline]" - [why this one]
3. "[headline]" - [why this one]
4. "[headline]" - [why this one]
5. "[headline]" - [why this one]
```

## Static Psychology Checklist

Before finalizing, verify each headline against:
- [ ] Image triggers the target emotion (not just looks nice)
- [ ] Colors contrast with Meta's blue/white palette
- [ ] Copy reinforces image message (not fights it)
- [ ] Headline is specific to cold audience (not vague/warm)
- [ ] Either copy-heavy (Pinterest style) or copy-light (bold single message) - not mid

## Success Criteria
- 20 headlines generated across 5 categories
- Top 5 recommendations with reasoning
- All headlines pass cold-audience test

## Learnings
<!-- Update this section with what headline types perform best -->

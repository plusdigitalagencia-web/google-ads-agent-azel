# Directive: Analyze Viral Content

**Purpose:** Find organic content that's proven to resonate, then reverse-engineer it for ads.

**When to use:** Your ads "look like ads" and get skipped.

---

## Inputs Required
- Niche hashtags
- Competitor brand names
- Problem-related keywords
- Platform (TikTok, Instagram, YouTube)

## Execution Steps

### Step 1: Find Viral Content

Search TikTok/Instagram for:
- Niche hashtags with 100K+ views
- Competitor brand mentions
- Problem-related keywords

Filter for:
- 500K+ views minimum
- High comment count (indicates engagement)
- Recent (last 6 months)

### Step 2: Transcribe and Analyze

Use this prompt:

```
Analyze this viral content and extract:

1. HOOK (first 3 seconds)
   - What pattern interrupt did they use?
   - What made you stop scrolling?

2. STRUCTURE
   - How long is it?
   - What's the narrative arc?
   - Where do they introduce the product (if at all)?

3. TONE
   - Casual/professional/funny/serious?
   - Energy level?
   - Speaking style?

4. PACING
   - Fast cuts or long takes?
   - When do transitions happen?

5. WHY IT PROBABLY WORKED
   - What emotion does it trigger?
   - What makes it feel "native" to the platform?

6. HOW TO ADAPT FOR [BRAND]
   - Rewrite the hook for our product
   - What elements to keep vs. change
```

## Output Format

Save to: `.tmp/viral_analysis_[date].md`

```markdown
## Viral Content Analysis: [Platform] @[creator]

**Video:** "[Title/description]"
**Views:** X | **Likes:** X | **Comments:** X

### Hook (0-3 sec)
"[Opening line]"
- Pattern interrupt: [type]
- Immediate relatability for target audience

### Structure
- 0-3s: Hook (pain statement)
- 3-8s: Show failed attempts
- 8-15s: Discovery moment
- 15-25s: Transformation
- 25-30s: CTA

### Tone
- [Description of tone and energy]

### Why It Worked
- [Analysis]

### Adaptation for [Brand]
Hook rewrite: "[new hook]"
Keep: [elements]
Change: [elements]
```

## Tools
- `execution/transcript_extractor.py` (if available)
- TikTok Symphony Creative Assistant
- Manual transcription as fallback

## Success Criteria
- Minimum 5 viral videos analyzed
- Clear patterns identified across videos
- At least 3 adaptable hooks documented

## Learnings
<!-- Update this section as you discover what works -->

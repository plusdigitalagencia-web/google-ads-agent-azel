# Agent Blueprint: AI-Powered Ad Creative System

\> **For Agents:** This is an executable blueprint. When a user gives you this document and asks you to "implement this" or "set this up for my brand," follow the Getting Started section step-by-step. Do not just read — act.

──────────────────────────────────────────────────

## Getting Started: First-Time Setup (Do This First)

When a user gives you this document, run through this exact conversation flow:

### Step 1: Onboarding Questions

Ask the user these questions (you can ask all at once or in sequence):

\`\`\`  
I'll help you set up this ad creative system. First, I need some information:

1\. What's your brand name and what do you sell?  
2\. Who is your target customer? (age, gender, interests, main pain points)  
3\. Do you have any existing ads running? If yes:  
   \- Do you have any "winners" that are performing well?  
   \- Can you share links or describe what's working?  
4\. What's your main goal right now?  
   \- \[ \] We need to create ads from scratch  
   \- \[ \] We have winners and want more variations  
   \- \[ \] We want to see what competitors are doing  
   \- \[ \] We're preparing for a big push (Q4, launch, etc.)  
5\. Who are your top 3 competitors?  
\`\`\`

### Step 2: Create the Brand Context File

Based on their answers, create this file in the workspace:

**File: \`context/brand\_context.md\`**

\`\`\`markdown

# Brand Context: \[Brand Name\]

## Product/Service

\[What they sell\]

* Key features: \[list\]  
* Price point: \[price\]  
* Main differentiator: \[what makes them unique\]

## Target Customer

* Demographics: \[age, gender, location\]  
* Psychographics: \[interests, values, lifestyle\]  
* Main pain points: \[what problems they have\]  
* Desired outcome: \[what they want to achieve\]  
* Awareness level: \[unaware / problem-aware / solution-aware / product-aware\]

## Voice & Tone

\[How the brand speaks \- examples help\]

## Competitors

1\. \[Competitor 1\] \- \[what they're known for\]  
2\. \[Competitor 2\] \- \[what they're known for\]  
3\. \[Competitor 3\] \- \[what they're known for\]

## Constraints

* \[Compliance issues if any\]  
* \[Brand guidelines / things to avoid\]  
* \[Budget constraints if relevant\]

## Current Winners

\[Description of what's working, or "None yet \- starting fresh"\]

## Research Sources

* Subreddits: \[relevant subreddits for this niche\]  
* Keywords for research: \[search terms customers use\]

\`\`\`

### Step 3: Choose Your Starting Path

Based on their goal, tell them which path you'll follow:

**Path A: Starting From Scratch (no existing ads)**  
\`\`\`  
Since you're starting fresh, here's our plan:  
1\. First, I'll research your customers \- find out how they talk about their problems  
2\. Then, I'll look at what's working for competitors  
3\. Finally, I'll generate your first batch of ad scripts

Let's start with customer research. I'll need you to \[give me access to / share\] any of these:

* Customer reviews (Amazon, your site, etc.)  
* Post-purchase survey responses  
* Support tickets or FAQ  
* Reddit threads about this problem

\`\`\`

**Path B: Scaling Winners (have existing ads)**  
\`\`\`  
Since you have winners to work with, here's our plan:  
1\. First, I'll analyze why your winners are working  
2\. Then, I'll generate 5-10 iteration concepts  
3\. Finally, I'll create briefs for each iteration

Can you share your top 3 performing ads? (links, scripts, or descriptions)  
\`\`\`

**Path C: Competitive Research (want to spy)**  
\`\`\`  
Since you want competitive intelligence, here's our plan:  
1\. First, I'll pull your competitors' top-performing ads  
2\. Then, I'll analyze patterns \- what hooks, formats, and messages they use  
3\. Finally, I'll adapt the best ideas for your brand

I'll search for \[Competitor 1, 2, 3\] in the ad libraries. Any other brands you want me to include?  
\`\`\`

### Step 4: Run the First Workflow

Execute the appropriate workflow based on their path. See the "First Campaign Walkthrough" section below for the complete execution flow.

──────────────────────────────────────────────────

## First Campaign Walkthrough: Getting Your First Ad Scripts

This is a complete end-to-end example. Follow this to produce the user's first batch of ad scripts.

### Phase 1: Customer Research (30 minutes)

**Goal:** Understand how customers talk about their problems.

**Step 1.1: Reddit Mining**

Search Reddit for discussions about the problem your product solves.

**Prompt to use:**  
\`\`\`  
Search Reddit for: "\[problem keyword\] reddit"

For example, if selling men's jeans:

* "jeans uncomfortable reddit"  
* "men's jeans fit reddit"  
* "best jeans for \[body type\] reddit"

\`\`\`

**What to extract:**  
Look for posts with high engagement and pull EXACT phrases customers use:

| Category | Example Phrases |  
|----------|-----------------|  
| Pain points | "I'm so sick of jeans that..." / "Every pair I try..." |  
| Desired outcome | "I just want jeans that..." / "All I need is..." |  
| Failed solutions | "I've tried X brand but..." / "Nothing works because..." |  
| Emotional language | "I feel like a sausage" / "It's embarrassing when..." |

**Output format:**  
\`\`\`markdown

## Customer Language Extract: \[Brand\]

### Pain Points (exact phrases)

* "\[exact quote 1\]"  
* "\[exact quote 2\]"  
* "\[exact quote 3\]"

### Desired Outcomes (exact phrases)

* "\[exact quote 1\]"  
* "\[exact quote 2\]"

### Failed Solutions (what they've tried)

* "\[brand/solution\] \- why it failed"

### Emotional Language (how they describe feelings)

* "\[exact emotional phrase\]"  
* "\[exact emotional phrase\]"

### Key Insight

\[One sentence summary of what you learned\]  
\`\`\`

**Step 1.2: Review Mining**

If the user has Amazon listings, their own reviews, or competitor reviews:

**Prompt to use:**  
\`\`\`  
Look through reviews and find:  
1\. 5-star reviews: What specific benefits do people mention?  
2\. 3-star reviews: What objections or hesitations do people have?  
3\. 1-star reviews of COMPETITORS: What problems can you solve that they can't?  
\`\`\`

**Step 1.3: Transformation Framework**

Ask the user (or infer from research):

\`\`\`  
Based on your product, let's map the customer transformation:

BEFORE: How does your customer feel BEFORE they find your product?  
(Examples: frustrated, embarrassed, tired, confused, stuck)

AFTER: How do they feel AFTER using your product?  
(Examples: confident, energized, relieved, proud)

TRIGGER: What event makes them finally take action?  
(Examples: upcoming event, health scare, saw a friend's results, New Year's)  
\`\`\`

### Phase 2: Script Generation (30 minutes)

**Goal:** Create 5 ad scripts based on research.

**The 3-Doc Setup:**

Before generating, ensure you have:  
1\. **Brand Context** (created in Step 2 above)  
2\. **Customer Language Extract** (from Phase 1\)  
3\. **Top Performing Examples** (ask user for winners, or use competitor research)

**Script Generation Prompt:**

\`\`\`  
You are a direct-response copywriter. Your job is to write ad scripts that sound like real customers talking to other customers \- NOT like a business.

## Context

\[Paste brand context\]

## Customer Language (use these exact phrases)

\[Paste customer language extract\]

## Script Requirements

* Hook must stop the scroll in \<3 seconds  
* Use the EXACT phrases from customer research  
* Sound like a person talking to a friend, not a brand talking to a customer  
* Include specific details (not vague claims)  
* End with clear CTA

## Script Format

Write 5 scripts, each with:

* HOOK (first 3 seconds \- pattern interrupt)  
* PROBLEM (agitate the pain using their words)  
* SOLUTION (introduce the product naturally)  
* PROOF (specific benefit or result)  
* CTA (clear next step)

## Script Types to Include

1\. Problem-Solution (start with the pain)  
2\. Testimonial Style (first-person "I tried everything...")  
3\. Myth Buster ("Everyone says X, but actually...")  
4\. Investigation Arc ("I saw this thing that said...")  
5\. Before/After ("6 months ago I was...")  
\`\`\`

**Output format for each script:**  
\`\`\`markdown

## Script 1: \[Type\] \- \[Working Title\]

**Target:** \[Who this speaks to\]  
**Angle:** \[What pain point/desire it addresses\]  
**Inspired by:** \[Which customer phrase inspired this\]

──────────────────────────────────────────────────

**HOOK (0-3 sec):**  
\[Opening line\]

**PROBLEM (3-10 sec):**  
\[Agitate the pain\]

**SOLUTION (10-20 sec):**  
\[Introduce product naturally\]

**PROOF (20-25 sec):**  
\[Specific benefit/result\]

**CTA (25-30 sec):**  
\[Clear next step\]

──────────────────────────────────────────────────

**Creator Notes:**

* Tone: \[casual/energetic/calm/etc.\]  
* Setting: \[where to film\]  
* Props needed: \[if any\]

\`\`\`

### Phase 3: Iteration Planning (15 minutes)

**Goal:** Plan variations of the best script concepts.

Once you have 5 scripts, identify the 2 strongest and plan iterations:

**Iteration Prompt:**  
\`\`\`  
For \[Script Name\], generate 5 iteration concepts:

1\. CREATOR VARIATION  
   Same script, different creator type. Describe who else could deliver this:  
   \- Different age?  
   \- Different demographic?  
   \- Different energy level?

2\. HOOK VARIATION  
   Same body/CTA, different hook. Write 3 alternative hooks.

3\. FORMAT VARIATION  
   How could this work as:  
   \- A static image? (what headline would capture it?)  
   \- A different video format? (talking head vs. B-roll vs. screen recording)

4\. ANGLE VARIATION  
   Same product benefit, different emotional angle. What other feelings could we tap?

5\. LENGTH VARIATION  
   \- 15-second version (what to cut?)  
   \- 60-second version (what to expand?)  
\`\`\`

──────────────────────────────────────────────────

## Quick Reference: Which Workflow for Which Problem

| User Says | Run This Workflow |  
|-----------|-------------------|  
| "We don't know what to say" | Phase 1 (Research) → Phase 2 (Scripts) |  
| "Our ads look like ads" | Analyze their competitors' organic content, then rewrite scripts |  
| "We have a winner, need more" | Skip to Phase 3 (Iteration Planning) with their winner |  
| "What are competitors doing?" | Run \`spy\_competitors\` workflow (see directive below) |  
| "Our statics don't convert" | Run static psychology audit, then \`generate\_static\_headlines\` |  
| "Performance is dropping" | First ask: "Did anything change on your website?" Then run performance review |  
| "Q4 is coming" | Run \`prepare\_q4\_strategy\` workflow |  
| "We need authentic content" | Set up customer content collection flow |

──────────────────────────────────────────────────

## Core Principles (From Source Material)

### 1\. The 3-Doc Rule

Every creative AI task should receive exactly 3 types of context:

* \*\*Brand Context\*\* \- Who we are, voice, constraints, product details  
* \*\*Domain Context\*\* \- How to do this specific task (e.g., "how to write static headlines")  
* \*\*Top Performing Examples\*\* \- 5-10 winning examples to pattern-match against

**Why:** LLMs are trained on 99% mediocre content. Without curated examples, they default to generic slop. More than 3 docs dilutes focus.

### 2\. Task-Specific Agents, Not Mega-Agents

Create separate directives for each creative task:

* Headline generation  
* Script writing  
* Script rewriting (from viral content)  
* Script review/feedback  
* Iteration suggestions

**Why:** One mega-prompt tries to do everything and does nothing well. Specialized agents with narrow scope outperform generalists.

### 3\. The Golden Formula

**Quality x Quantity x Diversity \= Success**

* \*\*Quality\*\* \- Well-researched, properly structured creative  
* \*\*Quantity\*\* \- High volume to feed the algorithm  
* \*\*Diversity\*\* \- Different angles, personas, formats to hit different audience pockets

### 4\. Feedback Loop (Self-Annealing)

Performance data must flow back to update directives. When something works:

1\. Identify why it worked  
2\. Update the "top performing examples" doc  
3\. Update domain context with new learnings  
4\. System gets stronger over time

### 5\. Rivers of Content Model (NEW \- from Mirella Crespi)

Big brands structure creative sourcing as multiple "streams" feeding one "river":

* \*\*In-house team\*\* \- Owns brand assets, high-production content, PR collaborations  
* \*\*Creative agencies\*\* \- Fresh perspective, specialized formats (podcast ads, street interviews)  
* \*\*UGC platforms\*\* \- High-volume, native-style content at scale  
* \*\*Customer content\*\* \- Real testimonials via post-purchase flows

**Why it works:** Each stream brings unique perspective and style. Diversity prevents algorithmic fatigue and reaches different audience pockets.

**Implementation:** Don't try to do everything in-house. Orchestrate multiple sources, each with their own strengths.

### 6\. Never Turn Off Top-Spending Ads (NEW \- from Barry Hott)

**Critical Warning:** "Turning off the top spending ad is an atrocity."

The system spends on an ad because it predicts best overall performance. You can't see how Meta optimizes internally — it's optimizing for the whole ad set, not individual ad CPA.

**What happens when you turn off top spenders:**  
1\. Next ad becomes top spender  
2\. That ad looks bad (it wasn't predicted to scale)  
3\. You turn that off too  
4\. Race to the bottom  
5\. You scream "we need more creative" — self-fulfilling prophecy

**Exception:** Only if it's been running \< 2 days and clearly tanking.

### 7\. Relevance is the 2025 Imperative (NEW \- from Barry Hott)

Consumer feeds are now hyper-personalized. The amount of irrelevant content people see is almost zero. Your ads compete against perfectly-curated organic content.

**Implication:** Ads must feel immediately relevant. Not just "good ads" — relevantly good ads for the specific person seeing them.

──────────────────────────────────────────────────

## Creative Strategist Competency Model (NEW \- from Mirella Crespi)

A true creative strategist must master:

1\. **Consumer psychology and behavior** \- How people think, feel, decide  
2\. **Platform mechanics** \- Placements, auction dynamics, algorithm behavior  
3\. **Paid media landscape** \- Where budget flows, platform trends  
4\. **Bridge-building** \- Connecting paid media insights to creative production

**The Two Problems Framework:**

Strategists either have:

* \*\*Not enough ideas\*\* (stuck in rut) → Solution: Go back to research, deeper than before  
* \*\*Too many ideas\*\* (can't prioritize) → Solution: Use data to identify highest-confidence concepts

**What separates good from bad:** A good strategist structures efficient feedback loops between performance data and creative output. A bad one just comes up with ideas without process.

──────────────────────────────────────────────────

## Research Tools Pipeline (NEW \- from Sarah Levinger)

### Sequential Research Stack

Run these in order to understand your customer:

**1\. Google Trends**

* Purpose: Industry viability, seasonal patterns  
* Output: Is this market growing/shrinking? When do people search?

**2\. Google Keywords**

* Purpose: High-intent purchaser volume  
* Output: How many people actively searching to buy?

**3\. Answer The Public**

* Purpose: Customer education level  
* Output: If you see doctor terminology \= high-educated customer. If you see "does this work?" \= low-educated customer (requires more education in ads)

**4\. Pinterest Trends**

* Purpose: What content people click on  
* Why Pinterest: Women hold 60-80% of US purchasing power, primarily use Pinterest  
* Output: If tutorials dominate → test tutorial-style ads

**Key Example:** Client couldn't scale "nootropic coffee" ads. Research showed nobody searches "nootropic" — switched to "mushroom coffee" (layman's term). Ads worked overnight.

──────────────────────────────────────────────────

## Iteration Philosophy (NEW \- from Mirella Crespi)

### Two Types of Iteration

**Type 1: Doubling Down (Conceptual) — PREFERRED**

When you have a winner, iterate at the conceptual level:

* Same script → different creator (different demographic, different energy)  
* Same message → different format (static → video, video → static)  
* Same concept → different hook  
* Same performer → more ads with them (if they work, use them again and again)

**Why preferred:** Faster, maintains what's working, proven concept amplified.

**Type 2: Scientific Method (Metric-Driven) — OVERRATED**

Analyze hook rate, hold rate, CTR. Change one variable to impact one metric.

**Why overrated:**

* Not a controlled experiment (Meta serves to different people)  
* You can spend weeks optimizing a 25% hook rate to 30% and nothing changes  
* Strategists gravitate to this because they want to "systematize" creative — but creative shouldn't be systematized

**Mirella's take:** "I see creative teams overanalyzing metrics and spending so much time when it doesn't move the needle. Pay attention to data but don't get stuck on it."

### The Reshot Rule

"Getting an ad reshot by a different creator IS iteration — a massive one."

If you have a winning script:  
1\. Get it reshot by someone who represents a different segment of your audience  
2\. This should OUTPERFORM the original (you're applying expertise to proven concept)  
3\. Don't be afraid to use the same creator repeatedly if they work — use them until they stop working

──────────────────────────────────────────────────

## Static Psychology Checklist (NEW \- from Sarah Levinger)

### Core Principles

**1\. Images processed 60,000x faster than text**

* Emotional imagery stops the scroll FIRST  
* Copy backs up the message SECOND  
* Whatever you want them to feel → put that feeling in the IMAGE, not just copy

**2\. Don't Use Brand Colors**

* Especially blue/white on Meta (that's Meta's colors — you blend in)  
* Pink mysteriously outperforms across industries (stands out, not common on feed)  
* Choose colors that INTERRUPT the scroll

**3\. Copy Density: Go Heavy or Go Light, Never Mid**

* Sarah's statics: headline, subhead, 2 buttons, bullet list, another button  
* Looks like Pinterest content (intentional)  
* "Every other static is copy-mid — that's why they don't work"

**4\. Message Congruence**

* Image and copy must say the SAME thing emotionally  
* Brain processes at 11 million bits/second — if image says one thing and copy says another, scroll  
* Example of failure: Copy speaks to "big guys" but image shows slim model \= friction

### Static Design Checklist

Before launching a static, verify:

* \[ \] Image triggers the target emotion (not just looks nice)  
* \[ \] Colors contrast with Meta's blue/white palette  
* \[ \] Copy reinforces image message (not fights it)  
* \[ \] Headline is specific to cold audience (not vague/warm)  
* \[ \] Either copy-heavy (Pinterest style) or copy-light (bold single message) — not mid

──────────────────────────────────────────────────

## ChatGPT Conversation Method

### Don't Prompt — Converse

Sarah's approach: Treat ChatGPT as "another brain to think with."

**Opening prompt:** "Can you help me think about \[problem\]?"

This frames the LLM as a thinking partner, not a command executor.

**Follow-up pattern:**

* "What am I missing?"  
* "What am I missing?"  
* "What am I missing?" (keep asking)

ChatGPT will push back on your biases and surface things you forgot.

**Useful prompts:**

1\. "Based on the fact that this person is a \[millennial/Gen Z/boomer\], what do they believe about life that I need to know to market well to them?"

2\. "Can you explain to me emotionally how this person probably feels about their problem?"

3\. "Is there any other place in life that they're currently experiencing this \[pain/desire\]?"

**Pre-prompt addition:**  
Add to every prompt: "Before answering this question, tell me if there's any other information that you need to know to give me a better answer."

### Organize Chats by Brand/Industry

Keep one ongoing chat per brand or industry. Don't start fresh each time — let context accumulate.

──────────────────────────────────────────────────

## Whitelisted Testing Account Strategy (NEW \- from Mirella Crespi)

### The Hidden Testing Ground

Big brands run a separate whitelisted Facebook page (not associated with their brand) for:

* High-volume, low-quality creative  
* Ugly/weird/experimental ads  
* Anything the brand team would never approve

**How it works:**  
1\. Whitelist an unbranded page for ad delivery  
2\. Run experimental creative there with reasonable budget  
3\. Let Meta decide what to spend on  
4\. If something works, either keep running there OR clean it up and move to main brand page

**Why:** Brand teams are often "precious" about creative quality. This gives a safe space to test without approval friction.

**Finding competitors doing this:** Search their brand in Ad Library — you'll only see their main page. But they have whitelisted accounts testing weird stuff you'll never see.

──────────────────────────────────────────────────

## AI Tools for Creative Strategy (EXPANDED)

### Research & Ideation

* \*\*GigaBrain\*\* \- Scours Reddit threads for real human conversations about problems  
* \*\*Perplexity\*\* \- Better than ChatGPT for research (shows sources, combines models)  
* \*\*Claude\*\* \- Better than ChatGPT for creative writing, humor, clever copy  
* \*\*Answer The Public\*\* \- Customer education level and question patterns

### TikTok-Specific (UNDERUTILIZED)

* \*\*TikTok Symphony Creative Assistant\*\* \- GPT trained on TikTok's data. Prompt it to find trends, search brands/keywords, returns actual TikTok videos. Amazing for research.  
* \*\*TikTok Symphony Creative Studio\*\* \- AI avatars, overdubbing in different languages with lip-sync matching

### Production & Post-Production

* \*\*11 Labs\*\* \- AI voices (preferred over AI avatars)  
* \*\*Descript\*\* \- Transcribing, stitching video  
* \*\*Runway / Pika Art\*\* \- Visual effects, expanding sets, generating backgrounds, weird eye-catching hooks  
* \*\*Sora (coming)\*\* \- Predicted to be massive for advertisers in 2025

### AI Avatars — Use With Caution

* Mirella: "AI avatars and fake humans — that's a no for me. Gray ethical area."  
* Legal complexity: Image/likeness rights, no clear precedent  
* Alternative: AI voices are less problematic than fake humans  
* If using: Never make "I statements" (unethical). Third-person statements about product facts are more acceptable.

──────────────────────────────────────────────────

## Directives to Build (With Prompts & Examples)

Each directive below includes the exact prompts to use and example outputs so you know what "done" looks like.

──────────────────────────────────────────────────

### Directive 1: mine\_reddit\_insights.md

**Purpose:** Extract authentic customer language from Reddit for use in ad copy.

**When to use:** Starting fresh, need to understand how customers talk about the problem.

**Execution Steps:**

**Step 1: Search Reddit**  
\`\`\`  
Search these queries:

* "\[product category\] reddit"  
* "\[main problem\] reddit"  
* "\[competitor name\] review reddit"  
* "best \[product category\] reddit"  
* "\[product category\] worth it reddit"

\`\`\`

**Step 2: Extract Language (Use this prompt)**  
\`\`\`  
I'm analyzing Reddit posts about \[TOPIC\]. Extract the following:

1\. PAIN POINTS \- Exact phrases people use to describe their frustration  
   Look for: "I'm so sick of...", "The worst part is...", "I can't stand..."

2\. DESIRED OUTCOMES \- What they wish they had  
   Look for: "I just want...", "All I need is...", "If only..."

3\. OBJECTIONS \- Why they haven't bought yet  
   Look for: "But...", "The problem with X is...", "I would but..."

4\. EMOTIONAL WORDS \- How they describe their feelings  
   Look for adjectives, metaphors, complaints

5\. SPECIFIC DETAILS \- Numbers, timeframes, situations  
   Look for: "Every morning I...", "For 3 years I've...", "Whenever I try to..."

Format as a list of exact quotes with source links.  
\`\`\`

**Example Output:**  
\`\`\`markdown

## Customer Language: Men's Jeans Brand

### Pain Points

* "I feel like a stuffed sausage in every pair I try" (r/malefashionadvice)  
* "Why is it so hard to find jeans for guys with big thighs?" (r/fitness)  
* "I literally ripped my jeans squatting down to pick something up" (r/tall)

### Desired Outcomes

* "I just want jeans I can actually move in"  
* "Something that fits my thighs without being baggy at the waist"

### Objections

* "Athletic fit brands are always way too expensive"  
* "I've tried 10 brands and they all suck"

### Emotional Words

* "embarrassing", "frustrated", "gave up", "uncomfortable all day"

### Specific Details

* "Every time I sit down at my desk..."  
* "I've returned 6 pairs in the last month"

\`\`\`

──────────────────────────────────────────────────

### Directive 2: analyze\_viral\_content.md

**Purpose:** Find organic content that's proven to resonate, then reverse-engineer it for ads.

**When to use:** Your ads "look like ads" and get skipped.

**Execution Steps:**

**Step 1: Find Viral Content**  
\`\`\`  
Search TikTok/Instagram for:

* Niche hashtags with 100K+ views  
* Competitor brand mentions  
* Problem-related keywords

Filter for:

* 500K+ views minimum  
* High comment count (indicates engagement)  
* Recent (last 6 months)

\`\`\`

**Step 2: Transcribe and Analyze (Use this prompt)**  
\`\`\`  
Analyze this viral content and extract:

1\. HOOK (first 3 seconds)  
   \- What pattern interrupt did they use?  
   \- What made you stop scrolling?

2\. STRUCTURE  
   \- How long is it?  
   \- What's the narrative arc?  
   \- Where do they introduce the product (if at all)?

3\. TONE  
   \- Casual/professional/funny/serious?  
   \- Energy level?  
   \- Speaking style?

4\. PACING  
   \- Fast cuts or long takes?  
   \- When do transitions happen?

5\. WHY IT PROBABLY WORKED  
   \- What emotion does it trigger?  
   \- What makes it feel "native" to the platform?

6\. HOW TO ADAPT FOR \[BRAND\]  
   \- Rewrite the hook for our product  
   \- What elements to keep vs. change  
\`\`\`

**Example Output:**  
\`\`\`markdown

## Viral Content Analysis: TikTok @fitnessinfluencer

**Video:** "POV: You finally find jeans that fit your quads"  
**Views:** 2.3M | **Likes:** 340K | **Comments:** 4.2K

### Hook (0-3 sec)

"I'm convinced jeans companies hate men with thighs"

* Pattern interrupt: Controversial statement  
* Immediate relatability for target audience

### Structure

* 0-3s: Hook (pain statement)  
* 3-8s: Show failed attempts (trying on tight jeans)  
* 8-15s: Discovery moment (finding the product)  
* 15-25s: Transformation (showing fit)  
* 25-30s: CTA (link in bio)

### Tone

* Casual, slightly frustrated  
* Talking like complaining to a friend  
* Self-deprecating humor

### Why It Worked

* Specific niche pain point  
* Visual before/after  
* Felt like organic content, not an ad  
* Comment section validates the problem exists

### Adaptation for \[Brand\]

Hook rewrite: "I've ripped 3 pairs of jeans this year doing normal activities"  
Keep: The frustrated tone, before/after reveal, specific problem focus  
Change: Feature our product, add brand-specific benefits  
\`\`\`

──────────────────────────────────────────────────

### Directive 3: spy\_competitors.md

**Purpose:** Extract top-performing competitor ads from ad libraries.

**When to use:** Want to see what's working in your space.

**IMPORTANT WARNING:** Sort by engagement (shares, comments), NOT by "longest running." People run losers at $1/day to mislead competitors.

**Execution Steps:**

**Step 1: Pull Competitor Ads**  
\`\`\`  
For each competitor:  
1\. Search Meta Ad Library: facebook.com/ads/library  
2\. Search AdSpy (if available): filter by competitor name  
3\. Search TikTok Creative Center

Collect:

* Top 10 ads by engagement metrics  
* Screenshot statics  
* Save video URLs for transcription

\`\`\`

**Step 2: Analyze Patterns (Use this prompt)**  
\`\`\`  
Analyze these competitor ads and identify patterns:

1\. HOOK ANALYSIS  
   \- What hooks do they use most?  
   \- First 3 seconds breakdown of top 5 ads

2\. FORMAT PATTERNS  
   \- Talking head vs. B-roll vs. screen recording?  
   \- UGC style vs. produced?  
   \- Static vs. video ratio?

3\. MESSAGING PATTERNS  
   \- What pain points do they hit?  
   \- What benefits do they emphasize?  
   \- What proof do they use?

4\. CTA PATTERNS  
   \- What offers do they push?  
   \- How do they create urgency?

5\. GAPS & OPPORTUNITIES  
   \- What are they NOT saying?  
   \- What angles are missing?  
   \- What could we do differently?  
\`\`\`

**Example Output:**  
\`\`\`markdown

## Competitor Analysis: Athletic Jeans Market

### Competitors Analyzed

1\. Brand A \- 47 active ads  
2\. Brand B \- 23 active ads  
3\. Brand C \- 89 active ads

### Hook Patterns (Most Common)

1\. Problem statement: "If you have \[body type\]..." (38%)  
2\. Failed solution: "I've tried every brand..." (24%)  
3\. POV format: "POV: Finding jeans that..." (18%)  
4\. Myth buster: "Everyone says \[X\] but..." (12%)

### Format Patterns

* 73% talking head UGC  
* 18% founder/lifestyle  
* 9% static images  
* Avg length: 22 seconds

### Messaging Patterns

* Pain: Thigh fit (mentioned in 67% of ads)  
* Benefit: Stretch/mobility (54%), Style (31%)  
* Proof: Customer reviews (most common)

### Gaps & Opportunities

* Nobody talks about durability/longevity  
* No one addresses specific activities (golf, cycling, etc.)  
* Minimal use of investigation/authority arc  
* Static ads underutilized \- opportunity

\`\`\`

──────────────────────────────────────────────────

### Directive 4: generate\_ad\_script.md

**Purpose:** Generate ad scripts using researched insights and proven structures.

**When to use:** You've completed research, now need to create scripts.

**CRITICAL RULE:** Never ask AI to "be creative." Ask it to pattern-match against winners and adapt.

**The Master Script Prompt (Use This):**  
\`\`\`  
You are a direct-response copywriter specializing in paid social ads.

## Your Rules:

1\. Sound like a CUSTOMER talking to another customer, not a brand  
2\. Use the EXACT phrases from the customer research below  
3\. Be specific, not vague ("I lost 12 lbs" not "I feel better")  
4\. Hook must pattern-interrupt in \<3 seconds  
5\. Never sound like an ad \- sound like content

## Brand Context:

\[Paste brand\_context.md\]

## Customer Research (USE THESE EXACT PHRASES):

\[Paste customer language extract\]

## Top Performing Examples to Pattern-Match:

\[Paste 3-5 winning scripts\]

## Write 5 Scripts

For each script, include:

* TYPE: \[Problem-Solution / Testimonial / Myth Buster / Investigation / Before-After\]  
* TARGET: \[Who specifically this speaks to\]  
* INSPIRED BY: \[Which customer phrase sparked this\]

Then write:

* HOOK (0-3 sec): \[Pattern interrupt\]  
* PROBLEM (3-10 sec): \[Agitate using their words\]  
* SOLUTION (10-20 sec): \[Introduce product naturally\]  
* PROOF (20-25 sec): \[Specific result/benefit\]  
* CTA (25-30 sec): \[Clear next step\]

## Script Types to Create:

1\. Problem-Solution \- Start with the pain, introduce product as solution  
2\. Testimonial \- First person "I tried everything until..."  
3\. Myth Buster \- "Everyone says X, but here's the truth..."  
4\. Investigation Arc \- "I saw this expert say \[X\], so I tried..."  
5\. Before/After \- "6 months ago I was \[state\], now..."  
\`\`\`

**Example Output:**  
\`\`\`markdown

## Script 1: Testimonial \- "The Sausage Script"

**Type:** Testimonial  
**Target:** Men 30-45 with athletic builds who've given up on finding good jeans  
**Inspired by:** Reddit quote "I feel like a stuffed sausage in every pair I try"

──────────────────────────────────────────────────

**HOOK (0-3 sec):**  
"I've literally ripped 4 pairs of jeans this year just by sitting down."

**PROBLEM (3-10 sec):**  
"If you have thighs from literally ANY physical activity, you know the struggle. Every pair either fits your thighs and looks like a parachute at the waist, or fits your waist and you can't bend your knees."

**SOLUTION (10-20 sec):**  
"My buddy who's a trainer told me about \[Brand\]. They're specifically designed for guys who actually use their legs. The stretch is insane \- I can literally squat in these \- but they still look like regular jeans."

**PROOF (20-25 sec):**  
"I've worn these 4 days a week for 6 months. Not a single rip. And I've gotten more compliments on these than any pants I've ever owned."

**CTA (25-30 sec):**  
"Link's in my bio. Seriously, if you've given up on jeans, just try these."

──────────────────────────────────────────────────

**Creator Notes:**

* Tone: Slightly frustrated, relatable, genuine  
* Setting: Living room or casual setting, NOT a studio  
* Props: Show the jeans, maybe squat in them  
* Demo: Could include actual squat or sitting down moment

\`\`\`

──────────────────────────────────────────────────

### Directive 5: generate\_static\_headlines.md

**Purpose:** Generate headline variations for static ad images.

**When to use:** Need static ads, or testing messaging before producing video.

**CRITICAL RULE:** Always write for COLD audiences. Cold-audience headlines work for warm too. Warm-audience headlines don't work for cold.

**BAD (Warm/Vague):**

* "I feel like a new person"  
* "Finally, jeans that fit"  
* "My new favorite jeans"

**GOOD (Cold/Specific):**

* "Jeans for guys who've ripped 3 pairs this year"  
* "Finally, jeans you can squat in"  
* "If you have thighs, you need these"

**Headline Generation Prompt:**  
\`\`\`  
Generate 20 headlines for a static ad.

## Product: \[Product name\]

## Target: \[Who specifically\]

## Main Benefit: \[Primary value prop\]

## Customer Language: \[Key phrases from research\]

## Rules:

1\. Write for COLD audiences (assume they don't know you)  
2\. Be specific, not vague  
3\. Use customer language, not marketing speak  
4\. Each headline should make ONE clear point  
5\. Max 10 words per headline

## Generate 4 headlines in each category:

1\. PROBLEM-FIRST  
   Start with the pain they're experiencing.  
   Example: "Jeans that rip when you squat? Same."

2\. BENEFIT-FIRST  
   Lead with what they get.  
   Example: "Squat. Sit. Move. These jeans won't rip."

3\. CURIOSITY  
   Make them want to learn more.  
   Example: "What 47,000 guys with big thighs already know"

4\. SOCIAL PROOF  
   Use numbers and credibility.  
   Example: "47,000 5-star reviews from guys who lift"

5\. DIRECT CALL-OUT  
   Name the audience explicitly.  
   Example: "For guys who've given up on finding jeans"  
\`\`\`

**Example Output:**  
\`\`\`markdown

## Headlines: Athletic Jeans Brand

### Problem-First

1\. "Tired of ripping jeans just by sitting down?"  
2\. "Jeans that fit your thighs OR your waist. Pick one. (Until now.)"  
3\. "Your thighs aren't the problem. Your jeans are."  
4\. "For guys who've returned 10 pairs of jeans this year"

### Benefit-First

5\. "Squat-proof jeans that actually look good"  
6\. "Athletic build? Finally, jeans made for you."  
7\. "Jeans you can move in without looking baggy"  
8\. "The stretch you need, the style you want"

### Curiosity

9\. "Why gym guys are switching to these jeans"  
10\. "The jeans secret that weightlifters know"  
11\. "What 47K reviews say about these jeans"  
12\. "The reason you can't find jeans that fit"

### Social Proof

13\. "47,000 5-star reviews from guys who lift"  
14\. "Sold out 3x last year. Back in stock."  
15\. "As seen on 200+ athletes"  
16\. "Why trainers recommend these jeans"

### Direct Call-Out

17\. "Built for guys with thighs"  
18\. "If you have an athletic build, these are for you"  
19\. "For men who actually use their legs"  
20\. "The official jeans of guys who squat"

### Top 5 Recommendations (for cold acquisition):

1\. "Your thighs aren't the problem. Your jeans are." (Problem-first, reframes)  
2\. "For guys who've returned 10 pairs of jeans this year" (Specific, relatable)  
3\. "Squat-proof jeans that actually look good" (Benefit-first, clear)  
4\. "Built for guys with thighs" (Direct, memorable)  
5\. "47,000 5-star reviews from guys who lift" (Social proof, specific)  
\`\`\`

──────────────────────────────────────────────────

### Directive 6: review\_ad\_performance.md

**Purpose:** Analyze ad performance data and generate optimization recommendations.

**When to use:** Weekly performance review, or when performance drops.

**CRITICAL WARNING:** Before blaming creative, ask: "Did ANYTHING change on the website?" Homepage hero, checkout flow, pricing, shipping — these often cause "creative problems."

**NEVER TURN OFF TOP SPENDERS:** The system spends on an ad because it predicts best overall performance. Turning off top spenders creates a death spiral.

**Analysis Prompt:**  
\`\`\`  
Analyze this ad performance data:

\[Paste performance data: Ad name, Spend, CPA, CTR, ROAS, etc.\]

## Answer these questions:

1\. TOP PERFORMERS  
   \- Which ads spent the most? (These are predicted winners)  
   \- What do they have in common? (Hook type, format, angle, creator)

2\. EMERGING WINNERS  
   \- Any ads with low spend but strong metrics?  
   \- What's unique about these?

3\. UNDERPERFORMERS  
   \- Which ads got spend but didn't convert?  
   \- Hypothesis: Why didn't they work?

4\. PATTERN ANALYSIS  
   \- Best performing hook type?  
   \- Best performing format (talking head vs. B-roll vs. static)?  
   \- Best performing angle/message?  
   \- Best performing creator type?

5\. ITERATION RECOMMENDATIONS  
   \- Based on patterns, what 3 iterations should we test next?  
   \- What should we STOP doing?

6\. WINNER DOCUMENTATION  
   \- Which ads should be added to "top performers" library?  
   \- What made them work (for future reference)?  
\`\`\`

──────────────────────────────────────────────────

### Directive 7: iterate\_winning\_ad.md

**Purpose:** Generate iteration variations of a proven winning ad.

**When to use:** You have a winner and want to squeeze more juice from it.

**PHILOSOPHY:** Prefer conceptual iteration (doubling down) over scientific iteration (metric tweaking).

**Conceptual iteration examples:**

* Same script, different creator  
* Same message, different format  
* Same hook, different body

**Scientific iteration (less preferred):**

* Change hook to improve hook rate  
* Change CTA to improve CTR

**Why conceptual is better:** Scientific iteration assumes controlled experiments. But Meta doesn't serve the same ad to the same people — so your "test" isn't controlled anyway.

**Iteration Prompt:**  
\`\`\`  
Here's our winning ad:

\[Paste winning script or describe the ad\]

Performance: \[Spend, CPA, CTR, etc.\]

## Generate 8 iteration concepts:

### CREATOR VARIATIONS (3)

Same script, different creator type:  
1\. Different age bracket  
2\. Different demographic  
3\. Different energy level/vibe

### HOOK VARIATIONS (2)

Same body/CTA, different opening:  
1\. Alternative hook \#1  
2\. Alternative hook \#2

### FORMAT VARIATIONS (2)

Same message, different medium:  
1\. As a static image (what headline?)  
2\. As a different video format (talking head → B-roll, etc.)

### ANGLE VARIATION (1)

Same benefit, different emotional approach

## For each, explain:

* What we're testing  
* Why it might outperform  
* Creator brief (if applicable)

\`\`\`

──────────────────────────────────────────────────

### Directive 8: prepare\_q4\_strategy.md

**Purpose:** Prepare creative strategy for Q4/Black Friday based on historical data.

**When to use:** 4-6 weeks before Q4 push.

**Key Insight:** "Don't reinvent the wheel in Q4. Take last year's winners, get them re-recorded, add offer overlays."

**Q4 Planning Prompt:**  
\`\`\`

## Historical Analysis

Pull these reports from Motion (or your analytics):  
1\. Top Q4 Ad Types from last year  
2\. Top Q4 Angles from last year  
3\. Top Q4 Individual Ads from last year  
4\. Year-to-Date Winners (current year)

## Questions to Answer:

1\. WHAT WORKED LAST Q4  
   \- Top 5 ads by spend  
   \- What format/angle/message?

2\. WHAT'S WORKING THIS YEAR  
   \- Current top performers  
   \- Which could scale during Q4?

3\. AUDIENCE SHIFT FOR GIFTING  
   \- Who buys this as a gift?  
   \- Do we need different creator demographics?  
   \- (e.g., Female creators for male products during gifting season)

4\. ITERATION OPPORTUNITIES  
   \- Which winners should we re-record?  
   \- Which need offer overlays?

## Output: Q4 Creative Plan

### Ads to Re-Record

\[List ads \+ new creator specs\]

### Ads to Add Offer Overlays

\[List ads \+ offer copy\]

### New Concepts to Test

\[Based on gaps identified\]

### Creator Recommendations

\[Demographic shifts for gifting\]  
\`\`\`

──────────────────────────────────────────────────

### Directive 9: customer\_content\_collection.md

**Purpose:** Source authentic customer content via post-purchase flows.

**When to use:** Need authentic content competitors can't replicate.

**Key Insight:** "Customer ads, founder ads — things that don't scale are your competitive advantage."

**Post-Purchase Email Template:**  
\`\`\`  
Subject: $50 store credit \- just need 60 seconds

Hey \[Name\],

Hope you're loving your \[Product\]\!

Quick favor: We're looking for real customers to share their experience on video.

Nothing fancy \- just your phone, 30-60 seconds:

* What made you buy?  
* How's it working out?  
* Would you recommend?

In exchange: $50 store credit

Reply to this email with your video and we'll send your credit within 24 hours.

\[Brand Team\]

P.S. Keep it real \- we want authentic, not scripted\!  
\`\`\`

**Video Brief for Customers:**  
\`\`\`  
Record a 30-60 second video on your phone answering:

1\. What problem were you trying to solve?  
2\. What made you choose \[Brand\]?  
3\. How has it worked out?  
4\. Would you recommend it?

Tips:

* Film in good lighting (near a window is great)  
* Just be yourself \- casual is better  
* Horizontal is preferred, but vertical works too

\`\`\`

──────────────────────────────────────────────────

### Directive 10: research\_tools\_pipeline.md

**Purpose:** Run structured customer research using free tools.

**When to use:** Starting with a new brand/niche, or going deeper on an existing one.

**The Research Stack (In Order):**

**Step 1: Google Trends**  
\`\`\`  
Go to: trends.google.com  
Search: \[product category\]

Answer:

* Is this market growing or shrinking?  
* When do searches peak? (Seasonality)  
* What related queries are rising?

\`\`\`

**Step 2: Google Keywords (via Keyword Planner or Ubersuggest)**  
\`\`\`  
Search: \[main keywords\]

Answer:

* How many people search for this monthly?  
* What's the buyer intent? (informational vs. transactional)  
* What related keywords have high volume?

\`\`\`

**Step 3: Answer The Public**  
\`\`\`  
Go to: answerthepublic.com  
Search: \[product/problem\]

Answer:

* What questions do people ask?  
* Are questions basic or advanced? (Education level)  
* What "vs" comparisons exist? (Competitors)

\`\`\`

**Step 4: Pinterest Trends**  
\`\`\`  
Go to: trends.pinterest.com  
Search: \[product/problem\]

Answer:

* What content gets pinned? (Tutorials, products, lifestyle)  
* What aesthetic resonates?  
* Is this a visual category or informational?

\`\`\`

**Step 5: Reddit (via GigaBrain or manual search)**  
\`\`\`  
Search: "\[problem\] site:reddit.com"

Answer:

* How do people describe the problem?  
* What solutions have they tried?  
* What do they wish existed?

\`\`\`

**Step 6: TikTok Symphony (if available)**  
\`\`\`  
Use TikTok Symphony Creative Assistant to:

* Find trending content in niche  
* See what formats perform  
* Identify creator styles that work

\`\`\`

**Research Summary Template:**  
\`\`\`markdown

## Research Summary: \[Brand/Product\]

### Market Status

* Growing/Stable/Shrinking  
* Seasonality: \[peak months\]

### Customer Education Level

* High/Medium/Low  
* Implications: \[need more education in ads? or go straight to product?\]

### Key Customer Language

* Pain phrases: \[list\]  
* Desire phrases: \[list\]  
* Objection phrases: \[list\]

### Content Formats That Work

* \[Format 1\]: \[why\]  
* \[Format 2\]: \[why\]

### Competitors to Watch

* \[Competitor 1\]: \[known for\]  
* \[Competitor 2\]: \[known for\]

### Recommended First Tests

1\. \[Angle/format to test first\]  
2\. \[Angle/format to test second\]  
3\. \[Angle/format to test third\]  
\`\`\`

**Output:**

* Research summary document  
* Customer education level (high/low)  
* Key phrases to use in copy  
* Content formats to test (tutorials, testimonials, etc.)  
* Seasonal timing recommendations

──────────────────────────────────────────────────

## Frameworks to Implement

### Framework 1: Investigation Arc

Structure for building trust through borrowed authority:

1\. **Hook:** "I watched this podcast where this expert said..."  
2\. **Authority clip:** Screen recording of expert statement  
3\. **Bridge:** "So I had to try it myself..."  
4\. **Product reveal:** Show the product solving the problem  
5\. **Result:** Testimonial or proof  
6\. **CTA:** Clear next step

Use case: Works especially well for products with credibility challenges.

### Framework 2: TikTok Shop Style

Why it works: TikTok Shop creators understand attention retention because they're commission-incentivized.

Key elements to extract:

* Fast hooks (pattern interrupt in first 1-2 seconds)  
* Constant visual movement  
* Conversational, unpolished tone  
* Strong benefit stacking  
* Urgency without being salesy

### Framework 3: Awareness Level Targeting

Create different creative for each awareness stage:

* \*\*Unaware:\*\* Lead with problem education, not product  
* \*\*Problem-aware:\*\* Agitate the problem, introduce solution category  
* \*\*Solution-aware:\*\* Differentiate your product from alternatives  
* \*\*Product-aware:\*\* Handle objections, build trust, offer incentive  
* \*\*Most aware:\*\* Retarget with social proof and urgency

**Key Insight:** "Shift further up the awareness phases to generate net new reach."

### Framework 4: Discovery Feed Content (NEW)

"It's not social media anymore. When you open TikTok or Reels, it's a discovery feed based on interests, not who you follow."

Best-performing ads in 2024 replicated organic discovery content:

* Comedy skits  
* Memes  
* Sound-based content (trending sounds)  
* Podcast clips  
* Behind-the-scenes / EGC (Employee Generated Content)  
* "Investigation" style content

**Key test:** Would this content exist organically on the platform? If not, it will feel like an ad and get skipped.

### Framework 5: Transformation Framework for Research (NEW)

When doing customer research, have your team answer:

1\. **BEFORE:** How does the customer feel before buying? (frustrated, tired, broken, humiliated, inadequate)  
2\. **AFTER:** How do they feel after using the product? (confident, sexy, ambitious, energized)  
3\. **TRIGGER:** What event triggered the purchase? (New Year's, breakup, health scare, gifting)

These answers generate hooks and angles directly.

**Pro tip:** The same deep emotions appear across categories. "I felt broken" appeared in both ED brand research AND menopause brand research. Universal emotions transcend niches.

### Framework 6: Post-it Exercise for Creative Ruts (NEW)

When team is stuck:

1\. Get everyone on a call  
2\. Each person writes 4-5 word headlines on virtual Post-its  
3\. Everyone contributes 3-4 headlines  
4\. Put them all on a shared board  
5\. Vote/discuss best ones

Result: 60 Post-its → 30 good headlines → hooks and scripts flow from there.

──────────────────────────────────────────────────

## Execution Scripts Needed

### Script 1: reddit\_scraper.py

* Input: keywords, subreddits, count  
* Output: JSON with posts, comments, engagement metrics  
* Uses: PRAW or scraping

### Script 2: transcript\_extractor.py

* Input: TikTok/YouTube/Instagram URL  
* Output: Clean text transcript  
* Uses: yt-dlp \+ whisper or platform APIs

### Script 3: adspy\_fetcher.py

* Input: competitor name, filters  
* Output: Top ads with metadata  
* Uses: AdSpy API or scraping

### Script 4: performance\_analyzer.py

* Input: CSV/JSON of ad performance data  
* Output: Analysis report with patterns and recommendations  
* Uses: pandas, basic statistics

### Script 5: motion\_report\_generator.py (NEW)

* Input: Motion API credentials, date range, tag categories  
* Output: Reports for Q4 planning (top ad types, angles, individual ads)  
* Uses: Motion API

### Script 6: customer\_video\_collector.py (NEW)

* Input: E-commerce platform webhook  
* Output: Organized library of customer videos with metadata  
* Uses: Platform API, cloud storage

──────────────────────────────────────────────────

## File Structure Recommendation

\`\`\`  
project/  
├── directives/  
│   ├── mine\_reddit\_insights.md  
│   ├── analyze\_viral\_content.md  
│   ├── spy\_competitors.md  
│   ├── generate\_ad\_script.md  
│   ├── generate\_static\_headlines.md  
│   ├── review\_ad\_performance.md  
│   ├── iterate\_winning\_ad.md          \# NEW  
│   ├── prepare\_q4\_strategy.md         \# NEW  
│   ├── customer\_content\_collection.md \# NEW  
│   └── research\_tools\_pipeline.md     \# NEW  
├── execution/  
│   ├── reddit\_scraper.py  
│   ├── transcript\_extractor.py  
│   ├── adspy\_fetcher.py  
│   ├── performance\_analyzer.py  
│   ├── motion\_report\_generator.py     \# NEW  
│   └── customer\_video\_collector.py    \# NEW  
├── context/  
│   ├── brand\_context.md  
│   ├── domain\_headline\_writing.md  
│   ├── domain\_script\_writing.md  
│   ├── static\_psychology\_checklist.md \# NEW  
│   └── top\_performers/  
│       ├── headlines\_winners.md  
│       └── scripts\_winners.md  
├── checklists/  
│   └── static\_psychology\_checklist.md \# NEW  
└── .tmp/  
    └── \[intermediate files\]  
\`\`\`

──────────────────────────────────────────────────

## Workflow Example: End-to-End Ad Creation

**Trigger:** "Create 5 new ad scripts for \[Brand\]"

**Orchestration flow:**

1\. Check if recent Reddit insights exist → if not, run mine\_reddit\_insights.md  
2\. Check if competitor analysis is current → if not, run spy\_competitors.md  
3\. Load brand context \+ domain context \+ top performers  
4\. Run generate\_ad\_script.md with research inputs  
5\. Output scripts to Google Doc or Notion  
6\. Queue for creative production

**After ads run:**

1\. Run review\_ad\_performance.md weekly  
2\. Winners get added to top\_performers/  
3\. Directives get updated with new learnings  
4\. System self-anneals

──────────────────────────────────────────────────

## Key Quotes from Source Material

**On AI usage:**  
"LLMs are not good creative strategists. They are trained on millions of articles from anyone and everyone, of which 99.9% are awful. They are great reasoning models. We need to train them to be \[good creative strategists\]."

**On context management:**  
"Don't give the LLM too much information. Give them the minimum viable context to do the job well."

**On research:**  
"Something about this piece of content resonates with your audience. That is an important piece of information."

**On feedback loops:**  
"Tie the loop between performance and strategy. This is the biggest pain point for brands and agencies."

**On diversity:**  
"Think of different creative sources as rivers flowing into one large river. You don't want every ad to look exactly the same."

**On turning off ads:**  
"Turning off the top spending ad is an atrocity. It's the bane of my existence."

**On relevance:**  
"Think about the stuff you see on Instagram and TikTok — how infrequently now is content NOT relevant to you? It's so little. That's what you're competing against."

**On psychology (Sarah Levinger):**  
"Images get processed by the brain about 60,000 times faster than text. Whatever you want them to feel, put that feeling in the image, not just the copy."

**On brand colors (Sarah Levinger):**  
"Please please please don't use your brand colors in ads. Especially blue or white on Meta — the entirety of Meta is blue and white."

**On iteration (Mirella Crespi):**  
"Getting an ad reshot by a different creator IS iteration — a massive one. If you have a winning script, get it reshot. It should OUTPERFORM the original."

**On AI avatars (Mirella Crespi):**  
"AI avatars and fake humans — that's a no for me. It's a gray ethical area."

**On ChatGPT (Sarah Levinger):**  
"I don't prompt. I just sit there and talk to ChatGPT. 'Can you help me think about this problem?' Then I keep asking 'What am I missing?'"

──────────────────────────────────────────────────

## 2025 Predictions from Source Material

1\. **Sound-first creative** — Taking trending sounds and creating content around them (underutilized)  
2\. **More authentic, uglier content** — Founder ads, real customer testimonials, things that don't scale  
3\. **AI agents for creative strategy** — Tools like Poppy AI that analyze winners and generate iterations  
4\. **Sora impact** — When OpenAI's video model launches, it will be massive for hook generation  
5\. **EGC (Employee Generated Content)** — Behind-the-scenes, warehouse packing, office comedy (see: ClickUp TikTok)  
6\. **Faster feedback loops** — "You used to do creative sprints. In 2025 you're sprinting 24/7."

──────────────────────────────────────────────────

## Next Steps for Implementation

1\. **Start with Reddit mining** \- Highest ROI, lowest complexity  
2\. **Build transcript extraction** \- Enables viral content analysis  
3\. **Create brand context template** \- Reusable across clients  
4\. **Implement one script generator** \- Prove the concept works  
5\. **Add performance review** \- Close the feedback loop  
6\. **Add static psychology checklist** \- Pre-launch quality gate  
7\. **Build iteration workflow** \- Systematize the reshot process  
8\. **Set up customer content collection** \- Post-purchase flow for testimonials

Build incrementally. Test each directive before adding the next. Self-anneal as you learn what works.


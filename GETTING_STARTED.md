# Creative System Setup Guide

Welcome! This guide will help you set up the AI-Powered Ad Creative System on your computer. No coding experience required.

---

## What This System Does

This is an AI-assisted creative system that helps you:
- **Generate ad scripts** using 7 proven structures (backed by $20M+ in ad spend data)
- **Analyze ad performance** from Meta Ads
- **Research competitors** and viral content
- **Mine customer language** from Reddit and reviews
- **Store and refine** your creative knowledge over time

Think of it as your AI creative partner that gets smarter the more you use it.

---

## Quick Overview (5 minutes)

The system has 3 layers:

| Layer | What It Does | Where It Lives |
|-------|--------------|----------------|
| **Directives** | Instructions (SOPs) telling the AI what to do | `directives/` folder |
| **Orchestration** | The AI reads directives and makes decisions | Claude Code (you're using it now) |
| **Execution** | Python scripts that do the actual work | `execution/` folder |

**You talk to Claude Code. Claude reads the directives and runs the scripts. You get the output.**

---

## Setup Steps

### Step 1: Install Claude Code

If you haven't already:

1. Open Terminal (press `Cmd + Space`, type "Terminal", hit Enter)
2. Run this command:
   ```bash
   npm install -g @anthropic-ai/claude-code
   ```
3. If you don't have npm, first install Node.js from https://nodejs.org

### Step 2: Get the Files

Your colleague will share the project folder with you. Put it somewhere easy to find, like:
```
~/Documents/Creative-System/
```

### Step 3: Set Up Your Environment File

The system needs API keys to work. Create a file called `.env` in the project folder.

**Option A: Copy the template**
```bash
cp .env.example .env
```

**Option B: Create it manually**

Create a new file called `.env` (note the dot at the beginning) with this content:

```env
# Required for Meta Ads integration
META_ACCESS_TOKEN=your_token_here
META_AD_ACCOUNT_ID=act_your_account_id

# Required for AI video analysis
GEMINI_API_KEY=your_gemini_key

# Optional - for advanced features
ANTHROPIC_API_KEY=your_claude_key
OPENAI_API_KEY=your_openai_key
```

### Step 4: Get Your API Keys

**Meta Access Token** (for pulling ad data):
1. Go to https://developers.facebook.com/tools/explorer/
2. Select your app (or create one)
3. Click "Generate Access Token"
4. Copy the token to your `.env` file

**Meta Ad Account ID**:
1. Go to https://business.facebook.com/settings/ad-accounts
2. Find your ad account
3. The ID looks like `act_123456789`

**Gemini API Key** (for video analysis):
1. Go to https://aistudio.google.com/apikey
2. Click "Create API Key"
3. Copy it to your `.env` file

### Step 5: Install Python Dependencies

Open Terminal in the project folder and run:

```bash
# Create a virtual environment (keeps things clean)
python3 -m venv .venv

# Activate it
source .venv/bin/activate

# Install required packages
pip install facebook-business python-dotenv requests anthropic google-genai
```

### Step 6: Set Up Brand Context

Before generating scripts, you need to tell the system about your client's brand.

Open `context/brand_context.md` and fill in:
- Company name and what they sell
- Target audience
- Key benefits and pain points
- Voice and tone guidelines
- Competitor information

**Pro tip:** The more detail you add here, the better your scripts will be.

---

## How to Use the System

### Start Claude Code

1. Open Terminal
2. Navigate to the project folder:
   ```bash
   cd ~/Documents/Creative-System
   ```
3. Start Claude Code:
   ```bash
   claude
   ```

### Common Tasks

**Generate ad scripts:**
> "Generate 3 founder-style scripts for [product name] targeting [audience]"

**Analyze current ad performance:**
> "Pull the last 30 days of ad performance and identify top performers"

**Research competitors:**
> "Research competitor ads for [competitor name]"

**Mine customer language:**
> "Find customer pain points and language from Reddit for [niche/product]"

**Iterate on a winning ad:**
> "Create 5 variations of our top performing ad [ad name/ID]"

---

## Key Folders Explained

```
Creative-System/
├── directives/          # SOPs - read these to understand what's possible
├── execution/           # Python scripts - don't edit unless you know Python
├── context/             # Brand info and winning examples - UPDATE THIS
├── .tmp/                # Temporary files - ignore this
├── .env                 # Your API keys - KEEP THIS SECRET
└── CLAUDE.md            # System instructions for the AI
```

### Folders You'll Use Most:

**`context/`** - This is your knowledge base
- `brand_context.md` - Update this for each client
- `top_performers.md` - Add notes about winning ads
- `creator_personas.md` - Reference for script styles

**`directives/`** - These are your SOPs
- `proven_script_system.md` - The script generation powerhouse
- `pull_meta_performance.md` - How to fetch ad data
- `iterate_winning_ad.md` - How to create variations

---

## The 7 Proven Script Archetypes

The system can generate scripts in these proven formats:

| Archetype | Best For | Vibe |
|-----------|----------|------|
| **Founder Story** | Trust, authenticity | "I created this because..." |
| **Problem-Solution** | Clear pain points | "Tired of X? Here's Y" |
| **Us vs Them** | Differentiation | "Unlike other products..." |
| **Social Proof** | Credibility | "10,000+ customers agree..." |
| **Unboxing/Demo** | Physical products | "Let me show you what's inside" |
| **Day in the Life** | Lifestyle products | "Here's how I use it daily" |
| **Expert/Authority** | Technical products | "As a [profession], I recommend..." |

To generate a specific type:
> "Generate a founder story script for [product]"

---

## Tips for Best Results

### 1. Fill out brand context thoroughly
The AI is only as good as the information you give it. Spend 30 minutes filling out `context/brand_context.md` properly.

### 2. Add winning examples
When you find ads that work, add them to `context/top_performers.md`. The system learns from patterns.

### 3. Be specific in your requests
Instead of: "Write an ad"
Say: "Write a 30-second founder story script for [product], targeting [audience], emphasizing [benefit]"

### 4. Use the iterative workflow
1. Generate multiple scripts
2. Pick the best one
3. Ask for variations on that winner
4. Repeat until you have enough options

### 5. Update directives with learnings
When you discover something that works, tell Claude to update the relevant directive. The system gets smarter over time.

---

## Troubleshooting

### "Command not found: claude"
You need to install Claude Code. See Step 1.

### "No module named 'facebook_business'"
You need to install Python dependencies. See Step 5.

### "Invalid access token"
Your Meta token expired (they last ~60 days). Get a new one from the Facebook Developer Tools.

### "Permission denied"
Make sure you're in the right folder and your `.env` file has the correct API keys.

### Scripts aren't relevant to my brand
Update `context/brand_context.md` with more detail about the product, audience, and voice.

---

## Getting Help

- Ask Claude: "What can you help me with?"
- Read the directive: Open `directives/proven_script_system.md` to understand the script system
- Check the blueprint: `Agent Blueprint_ AI-Powered Ad Creative System (Final).md` has everything

---

## Quick Reference Card

| I want to... | Say this... |
|--------------|-------------|
| Generate scripts | "Generate [number] [archetype] scripts for [product]" |
| Pull ad performance | "Pull Meta ad performance for the last [X] days" |
| Analyze winners | "What patterns do you see in our top performing ads?" |
| Create variations | "Create 5 variations of [winning ad]" |
| Research competitors | "Research [competitor] ads" |
| Update brand info | "Let's update the brand context for [client]" |
| Learn what's possible | "What directives are available?" |

---

## You're Ready!

Start Claude Code and try:
> "What can you help me with as a creative strategist?"

The AI will explain all the capabilities and help you get started.

Welcome to the team!

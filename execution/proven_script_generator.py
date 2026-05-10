#!/usr/bin/env python3
"""
Proven Script Generator - Generate ad scripts using $20M+ validated structures.

Usage:
    python proven_script_generator.py --product "Product Name" --archetype founder
    python proven_script_generator.py --config .tmp/product_brief.json

Inputs:
    - product: Product name
    - description: What the product does
    - differentiators: Key differentiators (comma-separated or JSON array)
    - old_product: What it replaces
    - price: Product price
    - old_price_yearly: Yearly cost of old solution
    - new_price_yearly: Yearly cost with new product
    - replacement_ratio: "1 replaces X"
    - target_audience: Who this is for
    - main_objection: The "isn't it just a X?" objection
    - objection_answer: Why it's NOT just that
    - archetype: Which script structure to use
    - environmental_angle: Sustainability messaging (optional)
    - community_size: Number of customers (optional)

Archetypes:
    - founder: Founder Origin Story
    - stupid: Problem Aggravation ("Stupid Invention")
    - cost: Cost Breakdown Math
    - cocky: Character Persona (Cocky Friend)
    - parent: Parent/Lifestyle Demo
    - skeptic: Skeptic Converter
    - replacement: Why Not Us? (Replacement Logic)
    - all: Generate all archetypes

Outputs:
    - Markdown file with generated scripts
    - Saved to .tmp/scripts_[product]_[timestamp].md

Requirements:
    - pip install anthropic python-dotenv
    - ANTHROPIC_API_KEY in .env
"""

import os
import json
import argparse
from datetime import datetime
from pathlib import Path
from textwrap import dedent

try:
    from anthropic import Anthropic
    from dotenv import load_dotenv
    DEPS_AVAILABLE = True
except ImportError:
    DEPS_AVAILABLE = False

# Load environment variables
if DEPS_AVAILABLE:
    load_dotenv()


ARCHETYPES = {
    "founder": {
        "name": "Founder Origin Story",
        "best_for": "Premium products, sustainability angle, mission-driven brands",
        "length": "60-90 seconds",
        "structure": dedent("""
            [PERSONAL TRIGGER] - "I had always been a [habit], but [life event] made me realize..."
            [FAILED ALTERNATIVES] - "Not only was it [expensive/annoying/wasteful], but I was feeling [emotion]"
            [BIRTH OF SOLUTION] - "So in [year], I launched [brand]..."
            [VIRAL MOMENT] - "And guys, [product] went viral. People went crazy and we sold out in [timeframe]"
            [PROOF POINTS x3] - Hit the three biggest differentiators
            [THE REAL KICKER] - "And the real kicker..." [biggest objection-buster]
            [USAGE DEMO] - "Just [action], [action], and [action]. It's that easy."
            [MULTIPLE USE CASES] - List 5-7 applications
            [SOCIAL PROOF] - "Our community has grown to over [X] amazing humans"
            [CTA] - "If you haven't tried this yet, click the link below. You will not be disappointed."
        """),
        "key_phrases": [
            "I made it my mission to...",
            "The real kicker...",
            "Game changer.",
            "You will not be disappointed."
        ]
    },
    "stupid": {
        "name": "Problem Aggravation (Stupid Invention)",
        "best_for": "Replacing existing products, disruption positioning",
        "length": "45-75 seconds",
        "structure": dedent("""
            [ATTACK THE STATUS QUO] - "They were a stupid invention. A [negative]. A [negative]. A [negative]. Yet we all accept it."
            [CHALLENGE] - "But we decided to challenge the status quo."
            [SOLUTION REVEAL] - "And after [effort], we did it. [Simple description of solution]"
            [DEMO] - "So now, anything you would [old behavior] for, you [new behavior] instead."
            [OBJECTION HANDLER] - "And no, it's not just a [common objection]"
            [PROOF STACK] - Multiple proof points with specifics
            [ENVIRONMENTAL/ETHICAL ANGLE] - "Unlike [old product] that [bad thing], this [good thing]"
            [IDENTITY CHALLENGE] - "Why are you still [old behavior]?"
            [BRAND STATEMENT] - "We are [brand]. And these are our [product]."
        """),
        "key_phrases": [
            "They were a stupid invention.",
            "Yet we all accept it.",
            "We decided to challenge the status quo.",
            "Why are you still [doing the old thing]?"
        ]
    },
    "cost": {
        "name": "Cost Breakdown Math",
        "best_for": "Subscription replacements, bulk purchase alternatives",
        "length": "60-90 seconds",
        "structure": dedent("""
            [PAIN OF BUYING] - "Can we talk about buying [product] for a sec? It couldn't be more annoying..."
            [LIST THE ANNOYANCES] - Takes up cart, carrying, storing, frequent trips
            [PRICE SHOCK] - "This [quantity] will run you $[X]"
            [DO THE MATH] - "The average American goes through [X] per [time]. That's $[Y] a year."
            [COMPARISON] - "One [product] lasts [time]. Each pack costs $[X]. You only buy [frequency]."
            [YEARLY SAVINGS] - "So you'll spend $[small] instead of $[big]."
            [HOW IT WORKS] - Simple 3-step demo
            [BONUS BENEFITS] - What else it replaces
            [ENVIRONMENTAL ANGLE] - Waste/chemical/landfill point
            [OBJECTION HANDLER] - "Maybe you're thinking [objection]. No, friends..."
            [PROOF POINTS] - Quick features
            [CLOSE] - Light humor, welcome to brand
        """),
        "key_phrases": [
            "Can we talk about [category] for a sec?",
            "That's $[X] a year on [product], before tax.",
            "So you'll spend just $[X] instead of $[Y].",
            "I mean, I could go on forever, but..."
        ]
    },
    "cocky": {
        "name": "Character Persona (Cocky Friend)",
        "best_for": "Younger demos, social-native brands, products with personality",
        "length": "90-120 seconds",
        "structure": dedent("""
            [CALL OUT + LIGHT ROAST] - "Hey, gals. Still using these? You complain about [relatable thing] but you spend $[X] on [product]."
            [PLAYFUL INSULT] - "Girl, I'm not calling you [negative]. I actually think you're pretty cool. You just don't know about [brand]."
            [SCENARIO SETUP] - "Let's say you [situation]. What are you going to use?"
            [DISMISS ALTERNATIVES WITH HUMOR] - Roast each alternative with personality
            [REVEAL SOLUTION] - "The correct answer, babe, is [product]."
            [RAPID-FIRE USE CASES] - 5-8 scenarios with personality commentary
            [GIFT ANGLE] - "Did I mention [product] makes the perfect gift?"
            [RECAP WITH ATTITUDE] - "Let's recap. You're [doing dumb thing] and [other dumb thing]. It's time to switch."
            [AFFIRMATIONS BIT] - "Let's write some affirmations together..."
            [MEMORABLE CTA] - "Now get out of here and [relatable action]. But promise me this..."
            [CALLBACK CLOSE] - Reference something relatable (calling mom, etc.)
        """),
        "key_phrases": [
            "Hey, gals.",
            "The correct answer, babe, is...",
            "Let's recap.",
            "Promise me this.",
            "Welcome to the party, babe."
        ]
    },
    "parent": {
        "name": "Parent/Lifestyle Demo",
        "best_for": "Products for parents, household items, daily-use products",
        "length": "60-90 seconds",
        "structure": dedent("""
            [RELATABLE CHAOS] - Show real mess/situation parents deal with
            [DEMO IN CONTEXT] - Use product on actual problem (kid mess, spill, etc.)
            [SELF-DEPRECATING HUMOR] - "My real kids refuse to participate in this"
            [VERSATILITY] - Same product handles multiple messes
            [SIMPLE PROCESS] - "And then I just [action] and [action]"
            [STAT] - "One sheet replaces [X]"
            [MAINTENANCE WIN] - "The best part? [Easy care routine]"
            [CONTRAST MOMENT] - "What am I gonna grab? A [alternative]? [Roast it]"
            [ANSWER] - "My fellow moms and dads, the answer is [brand]."
            [MORE USE CASES] - Bathroom, vanity, kids' bath
            [FEATURE PROOF] - "They're [feature], [feature], and because [reason], they never [problem]."
        """),
        "key_phrases": [
            "My fellow moms and dads, the answer is [brand].",
            "Unless I skip a day. I'm so bad.",
            "The best part is...",
            "It will be clean and dry for tomorrow's [use]."
        ]
    },
    "skeptic": {
        "name": "Skeptic Converter",
        "best_for": "Products with obvious objections, 'too good to be true' positioning",
        "length": "45-60 seconds",
        "structure": dedent("""
            [DEMO FIRST] - Start with impressive visual demonstration
            [ACKNOWLEDGE SKEPTICISM] - "I was skeptical when I first saw them too."
            [THE OBJECTION] - "I mean, isn't it just a [common comparison]? Let me explain."
            [SCIENCE/LOGIC] - "[Alternative] materials [do bad thing]. [Technical explanation]."
            [SENSORY PROOF] - "Trust me, you've got to feel it to believe it."
            [FEATURE EXPLANATION] - "Each [product] comes with [feature]. And each set comes with [feature]."
            [CONVENIENCE ANGLE] - "So not only is it [benefit], but [additional benefit]."
            [MOM WIN] - "Plus [easy care]. Mom wins."
            [PERSONALITY CLOSE] - Fun callback or character moment
        """),
        "key_phrases": [
            "I was skeptical when I first saw them too.",
            "Let me explain.",
            "Trust me, you've got to feel it to believe it.",
            "Mom wins."
        ]
    },
    "replacement": {
        "name": "Why Not Us? (Replacement Logic)",
        "best_for": "Obvious substitution products, behavior change",
        "length": "30-45 seconds",
        "structure": dedent("""
            [RHETORICAL PATTERN] - "We don't [use disposable X] or [disposable Y] on a daily basis. So why do we still use [disposable Z]?"
            [ANSWER THE WHY] - "I'll tell you why. Because we never had a good enough alternative."
            [UNTIL NOW] - "Until now."
            [QUICK DEMO] - Fast, impressive demonstration
            [ACKNOWLEDGE OLD HABIT] - "I'm not blaming you for liking [old product]. They're [convenient reason]."
            [VALIDATE THEN PIVOT] - "And up until now there was just no better option. I mean [alternatives] are [problems]."
            [SPEED PROOF] - "Remember that [product] I just used 30 seconds ago? If I need it again right now, it's ready to go."
            [PERFORMANCE CLAIM] - "It does a better job than [old product]."
            [SOCIAL PROOF] - "[X] people have already made the switch."
            [IMPACT] - "Which means collectively we're making a huge difference."
            [ENVIRONMENTAL] - Quick sustainability point
            [BENEFIT SUMMARY] - "Let me tell you why [brand] is going to make your life better. [List benefits]"
            [REVIEW READ] - Live review reading for authenticity
        """),
        "key_phrases": [
            "So why do we still use [old thing]?",
            "Until now.",
            "I'm not blaming you for liking [old product].",
            "[X] people have already made the switch."
        ]
    }
}


def build_prompt(product_info: dict, archetype: str) -> str:
    """Build the prompt for script generation."""

    arch = ARCHETYPES[archetype]

    prompt = f"""You are a direct-response copywriter with $20M+ in tracked revenue from video ads.

## YOUR RULES - FOLLOW EXACTLY:
1. Follow the structure EXACTLY as provided - these patterns are proven with real revenue
2. Use specific numbers, never vague claims
3. Sound like a real person talking to a friend, not a brand
4. The hook must stop the scroll in <3 seconds
5. Address the main objection directly, don't avoid it
6. Use the key phrases provided - they're proven to convert
7. Write in a conversational, spoken style (contractions, casual language)

## ARCHETYPE: {arch['name']}
**Best for:** {arch['best_for']}
**Target length:** {arch['length']}

## STRUCTURE TO FOLLOW:
{arch['structure']}

## KEY PHRASES TO USE:
{chr(10).join(f'- "{phrase}"' for phrase in arch['key_phrases'])}

## PRODUCT INFORMATION:
- **Product:** {product_info.get('product', 'Unknown')}
- **Description:** {product_info.get('description', 'No description')}
- **Replaces:** {product_info.get('old_product', 'existing solution')}
- **Key Differentiators:** {product_info.get('differentiators', 'None provided')}
- **Price:** {product_info.get('price', 'Not specified')}
- **Old solution yearly cost:** {product_info.get('old_price_yearly', 'Not specified')}
- **New solution yearly cost:** {product_info.get('new_price_yearly', 'Not specified')}
- **Replacement ratio:** {product_info.get('replacement_ratio', 'Not specified')}
- **Target audience:** {product_info.get('target_audience', 'General consumers')}
- **Main objection:** "{product_info.get('main_objection', 'Is it worth it?')}"
- **Why it's NOT that:** {product_info.get('objection_answer', 'Because it actually works')}
- **Environmental angle:** {product_info.get('environmental_angle', 'None')}
- **Community size:** {product_info.get('community_size', 'Not specified')}

## GENERATE THE SCRIPT

Write a complete, production-ready script following the {arch['name']} structure exactly.

After the script, include:

**CREATOR NOTES:**
- Tone: [describe the energy]
- Setting: [where to film]
- Props needed: [list]
- Key demo moments: [what to show on camera]
- Pacing notes: [fast/slow sections]
"""

    return prompt


def generate_script(product_info: dict, archetype: str, client: 'Anthropic') -> str:
    """Generate a single script using Claude."""

    prompt = build_prompt(product_info, archetype)

    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=4000,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.content[0].text


def format_output(scripts: dict, product_info: dict) -> str:
    """Format all generated scripts into markdown."""

    output = f"""# Generated Ad Scripts: {product_info.get('product', 'Unknown Product')}

**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}
**Based on:** $20M+ Proven Script System

---

## Product Brief

| Field | Value |
|-------|-------|
| Product | {product_info.get('product', 'N/A')} |
| Description | {product_info.get('description', 'N/A')} |
| Replaces | {product_info.get('old_product', 'N/A')} |
| Price | {product_info.get('price', 'N/A')} |
| Target | {product_info.get('target_audience', 'N/A')} |
| Main Objection | {product_info.get('main_objection', 'N/A')} |

---

"""

    for archetype, script in scripts.items():
        arch = ARCHETYPES[archetype]
        output += f"""## {arch['name']}

**Best for:** {arch['best_for']}
**Target length:** {arch['length']}

---

{script}

---

"""

    return output


def main():
    parser = argparse.ArgumentParser(
        description="Generate ad scripts using proven $20M+ structures",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Archetypes available:
  founder     - Founder Origin Story (60-90s)
  stupid      - Problem Aggravation "Stupid Invention" (45-75s)
  cost        - Cost Breakdown Math (60-90s)
  cocky       - Character Persona / Cocky Friend (90-120s)
  parent      - Parent/Lifestyle Demo (60-90s)
  skeptic     - Skeptic Converter (45-60s)
  replacement - Why Not Us? / Replacement Logic (30-45s)
  all         - Generate all archetypes

Example:
  python proven_script_generator.py \\
    --product "EcoBottle" \\
    --description "Reusable water bottle with built-in filter" \\
    --old-product "plastic water bottles" \\
    --differentiators "Filters as you drink, Keeps water cold 24hrs, Made from recycled ocean plastic" \\
    --price "$35" \\
    --old-price-yearly "$500" \\
    --new-price-yearly "$35" \\
    --replacement-ratio "1 bottle replaces 500 plastic bottles per year" \\
    --target "Eco-conscious millennials" \\
    --main-objection "just another water bottle" \\
    --objection-answer "Built-in filter means no more buying bottled water ever" \\
    --archetype founder
        """
    )

    parser.add_argument("--product", help="Product name")
    parser.add_argument("--description", help="What the product does")
    parser.add_argument("--old-product", help="What it replaces")
    parser.add_argument("--differentiators", help="Key differentiators (comma-separated)")
    parser.add_argument("--price", help="Product price")
    parser.add_argument("--old-price-yearly", help="Yearly cost of old solution")
    parser.add_argument("--new-price-yearly", help="Yearly cost with new product")
    parser.add_argument("--replacement-ratio", help="1 replaces X statement")
    parser.add_argument("--target", help="Target audience")
    parser.add_argument("--main-objection", help="The 'isn't it just a X?' objection")
    parser.add_argument("--objection-answer", help="Why it's NOT just that")
    parser.add_argument("--environmental", help="Sustainability messaging")
    parser.add_argument("--community-size", help="Number of customers")
    parser.add_argument("--archetype", default="all",
                       choices=list(ARCHETYPES.keys()) + ["all"],
                       help="Which script structure to use")
    parser.add_argument("--config", help="JSON file with product info")
    parser.add_argument("--output", default=".tmp", help="Output directory")
    parser.add_argument("--dry-run", action="store_true",
                       help="Show prompt without calling API")

    args = parser.parse_args()

    # Load from config file if provided
    if args.config:
        with open(args.config, 'r') as f:
            product_info = json.load(f)
    else:
        product_info = {
            "product": args.product,
            "description": args.description,
            "old_product": args.old_product,
            "differentiators": args.differentiators,
            "price": args.price,
            "old_price_yearly": args.old_price_yearly,
            "new_price_yearly": args.new_price_yearly,
            "replacement_ratio": args.replacement_ratio,
            "target_audience": args.target,
            "main_objection": args.main_objection,
            "objection_answer": args.objection_answer,
            "environmental_angle": args.environmental,
            "community_size": args.community_size,
        }

    # Validate required fields
    if not product_info.get("product"):
        print("Error: --product is required")
        print("Run with --help for usage information")
        return

    # Determine which archetypes to generate
    if args.archetype == "all":
        archetypes_to_generate = list(ARCHETYPES.keys())
    else:
        archetypes_to_generate = [args.archetype]

    # Dry run mode - just show prompt
    if args.dry_run:
        print("=" * 60)
        print("DRY RUN - Showing prompts without API calls")
        print("=" * 60)
        for arch in archetypes_to_generate:
            print(f"\n### {ARCHETYPES[arch]['name']} ###\n")
            print(build_prompt(product_info, arch))
            print("\n" + "=" * 60)
        return

    # Check dependencies
    if not DEPS_AVAILABLE:
        print("Error: Required dependencies not installed.")
        print("Run: pip install anthropic python-dotenv")
        return

    # Check API key
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        print("Error: ANTHROPIC_API_KEY not found in environment or .env file")
        return

    # Initialize client
    client = Anthropic(api_key=api_key)

    # Create output directory
    Path(args.output).mkdir(parents=True, exist_ok=True)

    # Generate scripts
    scripts = {}
    for arch in archetypes_to_generate:
        print(f"Generating {ARCHETYPES[arch]['name']}...")
        try:
            scripts[arch] = generate_script(product_info, arch, client)
            print(f"  ✓ Done")
        except Exception as e:
            print(f"  ✗ Error: {e}")
            scripts[arch] = f"Error generating script: {e}"

    # Format and save output
    output = format_output(scripts, product_info)

    product_slug = product_info.get('product', 'unknown').lower().replace(' ', '_')
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    output_path = f"{args.output}/scripts_{product_slug}_{timestamp}.md"

    with open(output_path, 'w') as f:
        f.write(output)

    print(f"\n✓ Scripts saved to: {output_path}")
    print(f"  Generated {len(scripts)} script(s)")


if __name__ == "__main__":
    main()

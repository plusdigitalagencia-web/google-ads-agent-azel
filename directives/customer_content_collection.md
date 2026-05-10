# Directive: Customer Content Collection

**Purpose:** Source authentic customer content via post-purchase flows.

**When to use:** Need authentic content competitors can't replicate.

---

## KEY INSIGHT

"Customer ads, founder ads — things that don't scale are your competitive advantage."

---

## Inputs Required
- E-commerce platform (Shopify, etc.)
- Email/SMS tool (Klaviyo, etc.)
- Incentive amount (store credit)
- Google Drive folder for uploads

## Execution Steps

### Step 1: Set Up Post-Purchase Email

Create email in your ESP (e.g., Klaviyo):

**Trigger:** X days after delivery (typically 7-14 days)

**Subject:** $[X] store credit - just need 60 seconds

**Body:**
```
Hey [Name],

Hope you're loving your [Product]!

Quick favor: We're looking for real customers to share their experience on video.

Nothing fancy - just your phone, 30-60 seconds:
- What made you buy?
- How's it working out?
- Would you recommend?

In exchange: $[X] store credit

Reply to this email with your video and we'll send your credit within 24 hours.

[Brand Team]

P.S. Keep it real - we want authentic, not scripted!
```

### Step 2: Create Video Brief

Send this to customers who respond:

```
Record a 30-60 second video on your phone answering:

1. What problem were you trying to solve?
2. What made you choose [Brand]?
3. How has it worked out?
4. Would you recommend it?

Tips:
- Film in good lighting (near a window is great)
- Just be yourself - casual is better
- Horizontal is preferred, but vertical works too

Upload here: [Google Drive link or upload form]
```

### Step 3: Organize Content

Create folder structure:
```
customer_content/
├── raw/
│   └── [date]_[customer_name]/
├── approved/
│   ├── full_testimonials/
│   ├── clips/
│   └── quotes/
└── used/
    └── [ad_name]/
```

### Step 4: Review and Approve

For each submission:
1. Watch full video
2. Rate quality (lighting, audio, authenticity)
3. Extract key quotes
4. Identify usable clips
5. Move to appropriate folder

## Output Format

Track submissions in: `.tmp/customer_content_log.md`

```markdown
## Customer Content Log

### Pending Review
| Date | Customer | Product | Video Length | Status |
|------|----------|---------|--------------|--------|
| [date] | [name] | [product] | [length] | Pending |

### Approved
| Date | Customer | Product | Quality | Key Quote | Used In |
|------|----------|---------|---------|-----------|---------|
| [date] | [name] | [product] | A/B/C | "[quote]" | [ad name or "Available"] |

### Stats
- Total submissions: X
- Approval rate: X%
- Used in ads: X
- Store credit issued: $X
```

## Email Templates

### Confirmation Email
```
Subject: Got it! Your $[X] credit is on the way

Hey [Name],

Just got your video - thanks so much for taking the time!

Your $[X] store credit code: [CODE]

We might use your video in our marketing (only with your permission of course). If you'd prefer we don't, just reply and let us know.

Thanks again!
[Brand Team]
```

### Follow-Up (If No Response)
```
Subject: Quick reminder - $[X] waiting for you

Hey [Name],

Just checking in - we'd still love to get your quick video review of [Product].

30 seconds, your phone, $[X] store credit.

Reply to this email with your video and we'll send your credit right away.

[Brand Team]
```

## Legal Considerations

Include in confirmation email or terms:
- Permission to use in marketing
- Opt-out option
- No guarantees of usage

## Success Criteria
- Post-purchase flow set up
- First 10 submissions received
- At least 5 usable testimonials
- Content organized and accessible

## Learnings
<!-- Update this section with response rates, what incentives work, quality patterns -->

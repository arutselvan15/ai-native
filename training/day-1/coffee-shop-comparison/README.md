# Day 1 Hands-on: Coffee Shop Comparison Tool

Time: 20 minutes

Format: AI-assisted coding

## What This Folder Contains

Use this `README.md` as the entry point for the exercise.

**Plan / design / verify:** [`../docs/coffee-shop-comparison/plan.md`](../docs/coffee-shop-comparison/plan.md)  
**Agent rules (Day 1):** [`../AGENTS.md`](../AGENTS.md)

```text
day-1/coffee-shop-comparison/
├── README.md
├── index.html
├── serve.sh
├── coffee_shop_reviews.csv
├── example_implementation.png
├── examples/
│   └── boris-cherny-claude-md-example.md
└── templates/
    └── AGENTS_TEMPLATE.md
```

## TL;DR

Build a web app that loads `coffee_shop_reviews.csv` and compares coffee shops.

Success means:

- The CSV loads.
- Coffee shops are displayed.
- There is some form of comparison.

This is a fast, low-stakes **warm-up build**. The goal is to get hands-on with AI-assisted coding and the core interaction patterns, not to produce your capstone. You select and ground your real, week-long capstone use case on Day 2.

## How This Fits Into The Week

| Day | Artifact or capability |
| --- | --- |
| Day 1 | Coffee-shop build warm-up (AI-assisted coding) |
| Day 2 | Ground the capstone, then OpenSpec: proposal, spec, design, tasks, implementation, verify |
| Day 3 | Curated context and skill creation |
| Day 4 | MVP harness blueprint and hardening assessment |
| Day 5 | Repo legibility, deterministic checks, and evidence package |

Day 1 is a warm-up: build something small and working, fast, to feel the agentic loop. Your week-long capstone is selected and grounded on Day 2, where it feeds OpenSpec directly.

## Quick Start

Before you prompt, take 60 seconds to decide what you actually want to build.

- What metrics matter?
- What comparison makes sense?

Your first prompt should reflect your vision, not a template.

### Option 1: Python + Web Framework

Best for those comfortable with Python. Gives you `pandas` for data manipulation.

### Option 2: Single HTML File

No setup required. Zero dependencies. Just open it in a browser. Great if you want to avoid environment issues.

### Option 3: Your Preferred Stack

Use whatever you are comfortable with. The goal is speed, not tech elegance.

## Success Tiers

### Bronze

Data loads and displays.

Concrete example: table showing 5 or more shops with name, rating, and price.

Bronze means: it works. CSV parses, data renders, no crashes.

### Silver

Compare shops meaningfully.

Concrete example: side-by-side view or chart comparing 2 or more shops.

Silver means: it is useful. A user could actually compare two shops and make a decision.

### Gold

Interactive and polished.

Concrete example: filtering, search, multiple visualizations, and a clean UI.

Gold means: it is impressive. You would demo this without caveats.

Aim for Silver. Bronze is acceptable. Gold is a stretch goal.

## Data Source

File: `coffee_shop_reviews.csv`

Contains:

- Shop name, address, neighborhood
- Ratings including overall, coffee quality, service, and atmosphere
- Pricing including regular coffee, cappuccino, and specialty drinks
- Wait times and operating hours
- Amenities including WiFi, outlets, seating, parking, and mobile ordering
- Review counts and customer data

Tip: Open the CSV in your editor first to see the column names.

## Reference Material In This Folder

You do not need these to finish the 20-minute build, but they are useful patterns you will reuse when you set up repo instructions for your own work this week:

- [`examples/boris-cherny-claude-md-example.md`](examples/boris-cherny-claude-md-example.md) — a concise `CLAUDE.md` instruction-file pattern (inspired by public writeups of Boris Cherny's Claude Code workflow). A good reference for keeping an agent instruction file lean and built from real mistakes.
- [`templates/AGENTS_TEMPLATE.md`](templates/AGENTS_TEMPLATE.md) — a starting structure for an `AGENTS.md` repo instruction file. Use it when you bring your capstone repo under AI-assisted work, starting Day 2.

If you reach Silver early, skim these and draft a short `AGENTS.md` for your build using the template.

## Track What Works

As you build, note:

- Which prompts worked on the first try
- What needed clarification or retry
- Where you spent the most time

This helps you build better prompts in future exercises.

## Common Pitfalls

| Pitfall | Solution |
| --- | --- |
| Spending 5 or more minutes debating the tech stack | Pick one and go |
| Hand-writing CSV parsing | Let AI generate it |
| Perfectionist UI design | Functional first, pretty later |
| Complex comparison logic | A simple side-by-side comparison works |
| `npm install` issues | Use Option 2 and build a single HTML file |
| Prompting without a mental model | Know what you want before you ask |

## Success Checklist

- [ ] CSV data loaded into the application
- [ ] At least 5 coffee shops displayed
- [ ] At least 5 key metrics shown per shop
- [ ] Some form of comparison included, either visual or side-by-side
- [ ] Application runs without errors

## Example Implementation

Note: `example_implementation.png` shows a complex, feature-rich dashboard that would take hours to build. That is not what is expected in 20 minutes.

For this exercise:

- A simple HTML table is perfectly fine
- Basic cards showing shop info work well
- A single bar chart comparing 2 to 3 shops is excellent
- Plain styling is completely acceptable

Your 20-minute solution should be much simpler than the example image.

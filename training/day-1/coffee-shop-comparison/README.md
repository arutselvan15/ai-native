# Day 1 Hands-on: Coffee Shop Comparison Tool

**Implementation:** Gold tier — Python, pandas, Streamlit (search, filters, compare, three charts).

**Docs:** [plan](../docs/coffee-shop-comparison/plan.md) · [design](../docs/coffee-shop-comparison/design.md) · [verify](../docs/coffee-shop-comparison/verify.md) · [Day 1 AGENTS.md](../AGENTS.md)

## Run

```bash
cd training/day-1/coffee-shop-comparison
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
./run.sh
# or: streamlit run app.py
```

Open the URL Streamlit prints (default `http://localhost:8501`).

## Layout

```text
coffee-shop-comparison/
├── app.py
├── data.py
├── requirements.txt
├── run.sh
├── coffee_shop_reviews.csv
├── example_implementation.png
├── examples/
└── templates/
```

## What you get

- Table of aggregated shops (12 shops from ~1,061 reviews)
- Sidebar search, neighborhood filter, min rating, WiFi / mobile toggles
- Shop A vs Shop B metrics and three charts (compare bars, ratings by shop, price vs wait)

---

## Lab context (workshop)

Time: 20 minutes · Format: AI-assisted coding

### TL;DR

Build a web app that loads `coffee_shop_reviews.csv` and compares coffee shops.

### Success tiers

| Tier | Meaning |
| --- | --- |
| Bronze | CSV loads; ≥5 shops with key metrics |
| Silver | Meaningful comparison of 2+ shops |
| Gold | Search, filters, multiple visualizations, polished UI |

This folder targets **Gold** with the Streamlit app above.

### Data

File: `coffee_shop_reviews.csv` — shop info, ratings, price, wait times, amenities, review text.

### Reference material

- [`examples/boris-cherny-claude-md-example.md`](examples/boris-cherny-claude-md-example.md)
- [`templates/AGENTS_TEMPLATE.md`](templates/AGENTS_TEMPLATE.md)

### Success checklist

- [x] CSV loaded and aggregated
- [x] ≥5 shops with ≥5 metrics
- [x] Comparison UI
- [x] Search and filters
- [x] Multiple visualizations

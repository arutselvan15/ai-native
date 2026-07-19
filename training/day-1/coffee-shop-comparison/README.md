# Day 1 Hands-on: Coffee Shop Comparison Tool

**Implementation:** Gold tier — **pandas** (load/aggregate CSV) + **Flask** (serve page) + **browser JS** (filters, compare dropdowns, Chart.js).

**Why not Streamlit:** dynamic compare dropdowns + filters fight Streamlit’s widget session state; this stack keeps Python for data and plain HTML `<select>` for stable UI.

**Docs:** [plan](../docs/coffee-shop-comparison/plan.md) · [design](../docs/coffee-shop-comparison/design.md) · [verify](../docs/coffee-shop-comparison/verify.md)

## Run

```bash
cd training/day-1/coffee-shop-comparison
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
./run.sh
# open http://127.0.0.1:8501/
```

## Layout

```text
coffee-shop-comparison/
├── app.py              # Flask entry
├── data.py             # pandas CSV + filters (shared logic)
├── templates/index.html
├── static/app.js
├── static/styles.css
├── requirements.txt
├── run.sh
└── coffee_shop_reviews.csv
```

## Gold features

- Search, neighborhood checkboxes, min rating slider, WiFi / mobile toggles
- Shop A / Shop B dropdowns (client-side; options refresh when filters change)
- Three charts: compare ratings, overall by shop, price vs wait

# Plan: Coffee shop comparison tool

**Status:** agreed  
**Date:** 2026-07-19  
**Exercise:** [Lab README](../../coffee-shop-comparison/README.md)

## Goal

Rebuild the Day 1 coffee shop lab as a **Gold-tier** experience: interactive browsing, search and filters, **multiple visualizations**, and a polished UI—using **Python** (pandas for data) as the primary stack. The app still loads `coffee_shop_reviews.csv`, aggregates review rows by shop, and supports meaningful shop-vs-shop comparison.

## Success tiers (lab rubric)

| Tier | Target | Definition (from lab README) |
| --- | --- | --- |
| Bronze | Required baseline | CSV loads; ≥5 shops with name, rating, price; no crashes |
| Silver | Required baseline | Meaningful comparison (e.g. side-by-side or chart for 2+ shops) |
| **Gold** | **Primary target** | Interactive and polished: **filtering**, **search**, **multiple visualizations**, **clean UI**—demo-ready without caveats |

## Success criteria

### Baseline (Bronze + Silver)

- [x] CSV loads without errors (~1,061 review rows → 12 aggregated shops)
- [x] At least five shops visible with at least five metrics each (overall rating, coffee quality, service, atmosphere, value, price, wait, amenities signals)
- [x] Compare at least two shops side-by-side with clear metric contrast
- [x] Runs locally with documented commands (repo-root `.venv` + root `requirements.txt`)

### Gold

- [x] **Search** by shop name (substring, case-insensitive)
- [x] **Filters** that narrow the shop list (e.g. neighborhood, minimum overall rating, WiFi / mobile ordering)
- [x] **Multiple visualizations** (minimum three distinct views), e.g.:
  - Compare chart: selected Shop A vs Shop B on rating dimensions
  - Distribution or ranking chart across filtered shops (e.g. overall rating or price)
  - Third view: amenity or wait-time comparison (bar or scatter)
- [x] **Polished UI**: coherent layout, readable typography, responsive-enough columns; loading and empty states when filters match nothing
- [x] Single entry command documented (e.g. `streamlit run app.py`)

## User and problem

- **Who:** Learner demoing AI-native workflow; end user choosing a coffee shop in Boston-area neighborhoods.
- **Problem:** Many review rows per shop; hard to scan CSV and weigh tradeoffs (rating vs price vs wait vs amenities).
- **Outcome:** Filter and search to a short list, inspect aggregates, pick two shops and compare with charts—fast enough to use in a live demo.

## Assumptions

- Data remains at `training/day-1/coffee-shop-comparison/coffee_shop_reviews.csv`.
- Local-only demo; no auth, deployment, or external APIs.
- Aggregation: **mean** for numeric columns per `shop_name`; **review_count**; amenity fields as **% True** where values are boolean strings.
- Python **3.10+** available; dependencies limited to **pandas** + **Streamlit** (+ chart backend Streamlit uses, e.g. Altair/Vega-Lite via `st.bar_chart` / `st.scatter_chart` or explicit Altair if needed).
- Existing single-file static HTML app removed in favor of Streamlit.

## Non-goals

- Production hosting, CI deploy, or database
- User accounts, editing reviews, maps/geocoding
- npm/React build pipeline
- Perfect handling of every CSV edge case beyond this dataset (quoted fields, `"True"`/`"False"` amenities)
- Matching every feature in `example_implementation.png` (that image is explicitly out of scope for the 20-minute lab; Gold here means the **rubric**, not the screenshot)

## Constraints

- **Stack:** Python first; pandas for load/aggregate; Streamlit for UI (lab “Option 1: Python + Web Framework”).
- **Dependencies:** Pin in repository-root `requirements.txt`; prefer stdlib + pandas + flask for the current stack unless design adds one small chart library with justification.
- **Security:** Synthetic public data; no secrets; read-only CSV.
- **Scope boundary:** Changes under `training/day-1/` only unless user asks otherwise.

## Scope (rough)

**In scope**

- Python package layout under `coffee-shop-comparison/` (e.g. `app.py`, `data.py`, optional `run.sh`); dependencies at repo root
- Load and cache aggregated shop dataframe
- Search + filters driving table and charts
- Shop A / Shop B compare panel with linked charts
- Update lab run instructions in README (implement phase)
- `verify.md` updated after implementation (Verify phase—not this step)

**Out of scope**

- Keeping vanilla JS as the primary documented app after Gold ship (may remain as legacy file)
- OpenSpec / capstone work (Day 2+)

## Risks and open questions

| Item | Notes | Mitigation |
| --- | --- | --- |
| Missing deps | First-run friction | Document repo-root venv + `pip install -r requirements.txt` |
| Chart count vs time | Gold needs 3+ viz | Design lists exact charts; reuse same filtered dataframe |
| Filter empty set | UX confusion | Empty state message + reset filters control |
| Duplicate stack (HTML + Python) | Confusing entry point | Design names Streamlit as sole primary; README updated in Implement |
| `serve.sh` today serves static HTML | Wrong command for Python app | Replace or add `run.sh` for Streamlit in Implement |

## Approval

- [x] Plan reviewed and **agreed** — OK to start `design.md` (design draft may be reviewed in parallel; implement only after both gates)

**Agreed by:** participant  
**Date:** 2026-07-19

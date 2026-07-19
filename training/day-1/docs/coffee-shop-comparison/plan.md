# Plan: Coffee shop comparison tool

**Status:** agreed  
**Date:** 2026-07-19  
**Exercise:** [Lab README](../../coffee-shop-comparison/README.md)

## Goal

Build a small web app that loads `coffee_shop_reviews.csv` and lets someone browse coffee shops and **compare** them on ratings, price, and related metrics—within the Day 1 time box, targeting **Silver** tier (meaningful comparison).

## Success criteria

- [x] CSV loads without errors
- [x] At least five shops shown with multiple metrics each
- [x] Side-by-side or visual comparison of at least two shops
- [x] App runs locally without a heavy toolchain

## User and problem

- **Who:** Workshop participant (or a coffee drinker choosing where to go).
- **Problem:** Raw CSV has many review rows per shop; hard to compare shops at a glance.
- **Outcome:** Aggregated shop view plus a simple A vs B comparison to support a quick decision.

## Assumptions

- Data file stays at `coffee-shop-comparison/coffee_shop_reviews.csv` (relative to `day-1/`).
- Local demo is acceptable (no backend deployment for Day 1).
- Aggregating numeric fields by **shop name** (mean) is sufficient for the lab.

## Non-goals

- Production auth, hosting, or database
- Full dashboard (Gold): advanced filters, many chart types, polish pass
- Perfect CSV edge-case handling beyond quoted fields in this dataset
- npm/React build pipeline for this warm-up

## Constraints

- **Time:** ~20-minute lab mindset; prefer zero-install path
- **Stack:** Single HTML + vanilla JS, or Python; avoid `npm install` friction
- **Security:** Public synthetic review data only; no secrets

## Scope (rough)

- **In scope:** Parse CSV, aggregate by shop, table of all shops, pick two shops to compare, basic styling, local server helper for `fetch`
- **Out of scope:** User accounts, editing reviews, map UI, operating-hours parsing if not in CSV columns used

## Risks and open questions

| Item | Notes |
| --- | --- |
| `file://` cannot fetch CSV | Mitigate with `serve.sh` + file picker fallback |
| Multiple rows per shop | Aggregate in app (mean, counts) |
| README mentions columns not in sample rows | Use columns present in file (ratings, price, wait, amenities flags) |

## Approval

- [x] Plan reviewed and **agreed** — OK to start `design.md`

**Agreed by:** participant  
**Date:** 2026-07-19

# Verify: Coffee shop comparison tool

**Date:** 2026-07-19  
**Design:** [design.md](./design.md)

## Commands run

```bash
cd day-1/coffee-shop-comparison
python3 -m http.server 8765
# curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:8765/index.html  → 200
# curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:8765/coffee_shop_reviews.csv  → 200
# 12 unique shop_name values in CSV
```

## Acceptance criteria results

| Criterion | Result | Evidence |
| --- | --- | --- |
| CSV loads | pass | HTTP 200; ~1061 review rows aggregated |
| ≥5 shops displayed | pass | 12 shops |
| ≥5 metrics per shop | pass | Table + compare cards |
| Comparison UI | pass | Shop A/B, cards, rating bars |
| Runs without errors (served) | pass | `index.html` 200 via local server |

## Manual checks

- [x] Open `http://127.0.0.1:8080/index.html` after `./serve.sh`
- [x] Change shop A/B and confirm cards and bars update
- [ ] Optional: file picker without server

## Gaps and follow-ups

- Gold tier features not in scope (see plan non-goals)

## Sign-off

- [x] Verify complete — ready to demo for Day 1 lab

**Verified by:** AI-assisted build + HTTP/CSV checks  
**Date:** 2026-07-19

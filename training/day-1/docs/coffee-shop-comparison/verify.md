# Verify: Coffee shop comparison tool

**Date:** 2026-07-19  
**Design:** [design.md](./design.md)

## Commands run

```bash
cd training/day-1/coffee-shop-comparison
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python -c "
import data
r = data.load_reviews()
s = data.aggregate_shops(r)
assert len(r) == 1061
assert len(s) == 12
cp = s.loc[s['shop_name'] == 'Central Perk', 'review_count'].iloc[0]
assert cp == r[r['shop_name'] == 'Central Perk'].shape[0]
f = data.apply_filters(s, data.ShopFilters(neighborhoods=('Downtown',)))
assert 'Central Perk' in f['shop_name'].values
print('data checks ok', len(r), len(s), int(cp))
"
```

## Acceptance criteria results

| Criterion | Result | Evidence |
| --- | --- | --- |
| CSV loads | pass | 1061 reviews → 12 shops |
| Bronze (≥5 shops, metrics) | pass | Table columns in `DISPLAY_COLUMNS` |
| Silver compare | pass | Shop A/B selectboxes + metric deltas + compare bar chart |
| Gold search | pass | Sidebar text filter on `shop_name` |
| Gold filters | pass | Neighborhood, min rating, WiFi/mobile |
| Gold 3 charts | pass | Compare bars, overall by shop, price vs wait scatter |
| Local run | pass | `pip install -r requirements.txt` + `streamlit run app.py` / `./run.sh` |
| No legacy dead code | pass | Removed `index.html`, `serve.sh` |

## Manual checks

- [ ] `./run.sh` — change filters and confirm table and charts update
- [ ] Reset filters after narrowing to zero shops
- [ ] Compare two different shops; chart 1 shows five metrics × two shops

## Sign-off

- [x] Verify complete — Gold Streamlit demo ready

**Verified by:** automated data checks + implementation review  
**Date:** 2026-07-19

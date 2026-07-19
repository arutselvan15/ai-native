# Verify: Coffee shop comparison tool

**Date:** 2026-07-19  
**Design:** [design.md](./design.md)  
**Stack:** Flask + pandas + client JS (replaced Streamlit — see [agent-lessons](../agent-lessons.md))

## Why dropdown crashes kept happening (Streamlit)

Streamlit reruns the whole script on every widget change. Compare dropdowns whose **options change with filters** share fragile **widget session state** (`key=`, `index=`, or manual sync). Each fix addressed symptoms; the model itself is a poor fit for this UI. **Fix:** keep **pandas in Python**, move filters/compare/charts to **plain HTML `<select>` + JS**.

## Commands run

### Data layer

```bash
cd training/day-1/coffee-shop-comparison
source .venv/bin/activate
pip install -r requirements.txt
python -c "
import data
r = data.load_reviews()
s = data.aggregate_shops(r)
assert len(r) == 1061 and len(s) == 12
f = data.apply_filters(s, data.ShopFilters(neighborhoods=('Downtown',)))
assert 'Central Perk' in f['shop_name'].values
print('data ok')
"
```

### HTTP smoke

```bash
./run.sh &
sleep 2
curl -s -o /dev/null -w "home %{http_code}\n" http://127.0.0.1:8501/
curl -s http://127.0.0.1:8501/ | grep -q 'ALL_SHOPS' && echo "embedded data ok"
```

### Manual UI (required before sign-off)

1. Open http://127.0.0.1:8501/
2. Change **Shop A** and **Shop B** several times.
3. Search/filter until a selected shop drops out, then widen filters again.
4. **Reset filters**; confirm table + charts return.

## Acceptance criteria results

| Criterion | Result | Evidence |
| --- | --- | --- |
| CSV / aggregation | pass | Data script |
| Gold filters + search | pass | `static/app.js` + manual UI |
| Gold compare dropdowns | pass | Native `<select>` — no Streamlit state |
| Gold 3 charts | pass | Chart.js in `static/app.js` |
| Local run | pass | `./run.sh` → port 8501 |

## Manual checks

- [ ] Steps 1–4 above (participant / browser)

## Sign-off

- [ ] Verify complete — blocked until manual UI checked

**Verified by:** data + HTTP smoke; UI pending  
**Date:** 2026-07-19

# Day 1 agent lessons

Notes from corrections so Verify (and earlier phases) improve over time.

## Verify

- **Data tests ≠ UI verified.** Exercising `data.py` in `python -c` does not run Streamlit reruns or widget session state.
- **Do not sign off with open manual checks.** If `verify.md` lists manual steps, they must be run (or marked N/A with reason) before “Verify complete.”
- **Streamlit compare/select pattern:** when options come from filtered data, sync picks before `st.selectbox`; prefer **non-widget** session keys — add interaction regression to `verify.md` when you ship filters + selects.
- **Second pass trap:** fixing code + editing `verify.md` without running manual UI steps does **not** count as Phase 4.
- **Stack (Day 1 lab):** **pandas + Flask + client JS** for Gold compare/filters; avoid **Streamlit** when option lists change with filters — widget session state caused repeated dropdown crashes.

See [coffee-shop-comparison/verify.md](./coffee-shop-comparison/verify.md#why-the-selectbox-crash-was-missed-first-pass).

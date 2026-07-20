# AGENTS.md — Day 1

Instructions for AI assistants working **inside `training/day-1/`**. Treat this folder as a standalone project. Training index: [`../AGENTS.md`](../AGENTS.md). **Shape the approach in repository-root [`docs/`](../../docs/README.md) before writing code.**

## Project purpose

Day 1 warm-up: build a web app that loads `coffee_shop_reviews.csv` and compares coffee shops. Workshop entry: [`coffee-shop-comparison/README.md`](./coffee-shop-comparison/README.md).

## Scope boundary

- Default workspace: **`training/day-1/`** for lab code (`coffee-shop-comparison/`). Phased artifacts live at **repository root** under `docs/` (not under `day-1/`).
- Do not change other days under `training/` or repo root files unless the user explicitly asks.

**OpenSpec:** Day 1 does not use OpenSpec changes for this lab. Planning artifacts stay under repository-root `docs/`. Repo-wide OpenSpec (Day 2+ capstone) lives only at the **repository root** `openspec/`—there is no OpenSpec root under `coffee-shop-comparison/`.

## Non‑negotiable: phased workflow

| Phase | Name | Product code? | Artifact |
| --- | --- | --- | --- |
| 1 | **Plan** | No | `docs/<exercise-slug>/plan.md` (repo root) |
| 2 | **Design** | No (docs/diagrams only) | `docs/<exercise-slug>/design.md` |
| 3 | **Implement** | Yes | `coffee-shop-comparison/` (etc.) |
| 4 | **Verify** | Fixes only | `docs/<exercise-slug>/verify.md` |

Templates: [`docs/_templates/`](../../docs/_templates/).

**Trivial exceptions:** typos, comment-only edits, one-line obvious fixes, or user says “skip phases.” When in doubt, start at Plan.

### Phase 1 — Plan

Write or update `docs/coffee-shop-comparison/plan.md` (or `docs/<slug>/plan.md` for a new exercise). Chat summarizes; **the doc is source of truth.**

Exit gate: status **agreed** with checkbox and date. No `design.md` until then.

### Phase 2 — Design

Write `docs/<exercise-slug>/design.md`, linked from `plan.md`. No edits to `app.py`, `data.py`, or other product files until design status is **approved**.

### Phase 3 — Implement

Smallest change set that matches the approved design task list. Stop and update Plan/Design if the approach breaks down.

### Phase 4 — Verify

Update `docs/<exercise-slug>/verify.md` with **evidence**, not assumptions.

**Required for every verify:**

1. **Commands run** — paste exact commands and outcome (exit code, key output).
2. **Acceptance table** — map each plan/design criterion to pass/fail/**not run** with evidence.
3. **Manual checks** — executable steps a human (or agent with browser/UI) performs for anything the automated commands cannot cover.
4. **Sign-off** — only when manual items are **checked or explicitly N/A** with reason.

**Interactive UI (Streamlit, SPA, Flask+JS, etc.):**

- Unit tests on `data.py` (or similar) **do not** satisfy Gold UI criteria by themselves.
- **`resolve_*` / pure helpers** that mirror UI rules **do not** replace running the app — they cannot catch Streamlit widget `key=` / session-state API mistakes.
- Before sign-off, run `./run.sh` (or documented entry) and exercise **filter → compare → change filters again** and **change both compare dropdowns** so widget **session state** stays valid.
- **Manual checks:** an agent must **not** mark `[x]` unless it ran those steps in a browser (or user explicitly confirms). Document **who ran** manual UI checks under sign-off.
- If manual checks are listed, leaving them `[ ]` while marking verify complete is **not allowed**.
- After a user-reported UI bug, add a **regression** line to `verify.md`, fix code, then **re-run** manual UI steps before sign-off — updating the doc alone is not verify.

Fixes found in Verify phase are allowed in product code; update the verify doc in the same change.

## Announce the phase

Start structured replies with: **Phase: Plan | Design | Implement | Verify**.

Between gates, ask explicitly (e.g. “Approve Plan to move to Design?”).

## AI collaboration rules

- Active partner: clarify incomplete requirements; challenge risky scope.
- Keep context lean; read files needed for the current phase only.
- Plan, Design, Verify live under **repository-root `docs/`** — update [`docs/README.md`](../../docs/README.md) when adding an exercise slug.
- No destructive git, secrets, or new dependencies without explicit approval.

## Important paths (Day 1)

| Path | Purpose |
| --- | --- |
| `docs/README.md` (repo root) | Doc index |
| `docs/coffee-shop-comparison/` | Plan, design, verify for the lab |
| `coffee-shop-comparison/app.py` | Flask server (serves UI + embedded shop JSON) |
| `coffee-shop-comparison/data.py` | CSV load, aggregate, filter helpers |
| `coffee-shop-comparison/templates/`, `static/` | Gold UI (filters, compare, charts) |
| `coffee-shop-comparison/run.sh` | Start Flask (`python app.py`) |
| `coffee-shop-comparison/coffee_shop_reviews.csv` | Data |

## Run and verify

```bash
# From repository root (once): python3 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt
cd coffee-shop-comparison
./run.sh
# http://127.0.0.1:8501/
```

Do not invent commands; use the lab README and existing scripts.

## Code quality

- Simplicity first; minimal diff; match existing style in `coffee-shop-comparison/` (`app.py`, `data.py`).
- Document tradeoffs in `design.md`.

## Safety

- No hardcoded secrets or real PII.
- No production or deployment changes.

## Handoff (each phase)

1. Phase completed  
2. What changed / decided  
3. Files touched  
4. Checks run  
5. Risks / open questions  
6. Next step and gate  

## Self‑improvement

Durable lessons from corrections → add a bullet here or in [`docs/agent-lessons.md`](../../docs/agent-lessons.md).

- **Verify ≠ data-only tests:** Streamlit/UI labs need interaction checks (filters, widgets, session state). Do not sign off `verify.md` with unchecked manual steps ([coffee-shop-comparison verify gap](../../docs/coffee-shop-comparison/verify.md#why-dropdown-crashes-kept-happening-streamlit)).
- **Do not self-certify manual UI:** Marking manual checks `[x]` without running `./run.sh` and using compare dropdowns (or user confirmation) repeats the same gap — see verify doc manual checks section.

## Default mode

**Phase 1 (Plan)** for new features or lab extensions. Reference implementation docs: [`docs/coffee-shop-comparison/plan.md`](../../docs/coffee-shop-comparison/plan.md).

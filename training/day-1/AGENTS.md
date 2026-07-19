# AGENTS.md — Day 1

Instructions for AI assistants working **inside `training/day-1/`**. Treat this folder as a standalone project. Training index: [`../AGENTS.md`](../AGENTS.md). **Shape the approach in `docs/` before writing code.**

## Project purpose

Day 1 warm-up: build a web app that loads `coffee_shop_reviews.csv` and compares coffee shops. Workshop entry: [`coffee-shop-comparison/README.md`](./coffee-shop-comparison/README.md).

## Scope boundary

- Default workspace: **`training/day-1/`** only (code under `coffee-shop-comparison/`, artifacts under `docs/`).
- Do not change other days under `training/` or repo root files unless the user explicitly asks.

## Non‑negotiable: phased workflow

| Phase | Name | Product code? | Artifact |
| --- | --- | --- | --- |
| 1 | **Plan** | No | `docs/<exercise-slug>/plan.md` |
| 2 | **Design** | No (docs/diagrams only) | `docs/<exercise-slug>/design.md` |
| 3 | **Implement** | Yes | `coffee-shop-comparison/` (etc.) |
| 4 | **Verify** | Fixes only | `docs/<exercise-slug>/verify.md` |

Templates: [`docs/_templates/`](./docs/_templates/).

**Trivial exceptions:** typos, comment-only edits, one-line obvious fixes, or user says “skip phases.” When in doubt, start at Plan.

### Phase 1 — Plan

Write or update `docs/coffee-shop-comparison/plan.md` (or `docs/<slug>/plan.md` for a new exercise). Chat summarizes; **the doc is source of truth.**

Exit gate: status **agreed** with checkbox and date. No `design.md` until then.

### Phase 2 — Design

Write `docs/<exercise-slug>/design.md`, linked from `plan.md`. No edits to `app.py`, `data.py`, or other product files until design status is **approved**.

### Phase 3 — Implement

Smallest change set that matches the approved design task list. Stop and update Plan/Design if the approach breaks down.

### Phase 4 — Verify

Update `docs/<exercise-slug>/verify.md` with commands, acceptance results, and sign-off before claiming done.

## Announce the phase

Start structured replies with: **Phase: Plan | Design | Implement | Verify**.

Between gates, ask explicitly (e.g. “Approve Plan to move to Design?”).

## AI collaboration rules

- Active partner: clarify incomplete requirements; challenge risky scope.
- Keep context lean; read files needed for the current phase only.
- Plan, Design, Verify live under **`day-1/docs/`** — update [`docs/README.md`](./docs/README.md) when adding an exercise slug.
- No destructive git, secrets, or new dependencies without explicit approval.

## Important paths (Day 1)

| Path | Purpose |
| --- | --- |
| `docs/README.md` | Doc index for this day |
| `docs/coffee-shop-comparison/` | Plan, design, verify for the lab |
| `coffee-shop-comparison/app.py` | Streamlit UI |
| `coffee-shop-comparison/data.py` | CSV load, aggregate, filters |
| `coffee-shop-comparison/run.sh` | Start Streamlit |
| `coffee-shop-comparison/coffee_shop_reviews.csv` | Data |

## Run and verify

```bash
cd coffee-shop-comparison
./run.sh
# or: streamlit run app.py
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

Durable lessons from corrections → add a bullet here or in `docs/agent-lessons.md` under Day 1.

## Default mode

**Phase 1 (Plan)** for new features or lab extensions. Reference implementation docs: [`docs/coffee-shop-comparison/plan.md`](./docs/coffee-shop-comparison/plan.md).

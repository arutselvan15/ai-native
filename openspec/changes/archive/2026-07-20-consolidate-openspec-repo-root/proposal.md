## Why

The repository currently has two local OpenSpec roots: one at the repo root and a nested copy under `training/day-1/coffee-shop-comparison/`. The OpenSpec CLI resolves the **nearest** `openspec/` directory, so commands and agents run from the Day 1 lab can target a different planning home than Day 2 capstone work at the repo root. That split-brain layout conflicts with the training model (one capstone change tree for the week, Day 1 on phased docs only) and risks changes being created in the wrong place.

## What Changes

- Remove nested OpenSpec scaffolding from `training/day-1/coffee-shop-comparison/` (`openspec/` and duplicate opsx harness under `.cursor/` and `.github/`).
- Keep a **single** OpenSpec root at `openspec/` on the repo root and a **single** opsx command/skill harness at repo-root `.cursor/` and `.github/`.
- Document workspace and workflow expectations in training agent docs and Day 2 entry README so learners open the repo at root and use repo-root OpenSpec for capstone work.
- Leave Day 1 coffee-shop product code and `day-1/docs/` phased workflow unchanged.
- Optionally add minimal `context` in repo-root `openspec/config.yaml` pointing agents at training-repo conventions (no nested roots).

## Capabilities

### New Capabilities

- `repo-openspec-layout`: Requirements for where OpenSpec roots, changes, and opsx harness files may live in this repository, and how CLI resolution must behave from training paths.

### Modified Capabilities

- _(none — no existing main specs under `openspec/specs/` yet)_

## Impact

- **Removed paths:** `training/day-1/coffee-shop-comparison/openspec/`, duplicate opsx files under that lab’s `.cursor/` and `.github/`.
- **Updated docs:** `training/AGENTS.md`, `training/day-1/AGENTS.md`, and optionally `training/day-2/spec-writing/README.md`.
- **Unchanged:** Flask lab (`app.py`, `data.py`, templates), `day-1/docs/*`, repo-root opsx harness (already present).
- **Learners:** Must use repo root as Cursor workspace for `/opsx:*` and consistent `openspec` CLI behavior; Day 1 labs no longer ship a self-contained OpenSpec copy.

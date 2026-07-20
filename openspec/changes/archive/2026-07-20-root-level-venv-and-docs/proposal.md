## Why

Day 1 currently instructs learners to create a virtual environment inside `training/day-1/coffee-shop-comparison/` and keeps plan/design/verify artifacts under `training/day-1/docs/`. As the repo adds more days and Python-based labs, that per-day layout duplicates setup steps and splits documentation away from the repo root where OpenSpec and the Cursor workspace already live. A single root-level `.venv` and `docs/` tree makes local Python tooling and phased workshop docs consistent for the whole repository.

## What Changes

- Establish **one** Python virtual environment at the repository root (`.venv/`), with dependency installation and activation documented from the repo root.
- Consolidate Python dependencies at repo root (e.g. root `requirements.txt` or equivalent) so labs under `training/` share the same environment instead of lab-local venv instructions.
- Move phased workshop documentation from `training/day-1/docs/` to a **repo-root `docs/`** tree, preserving exercise slugs and templates while updating links in AGENTS files and lab READMEs.
- Update run/verify instructions in lab READMEs and verify docs to use root venv paths (e.g. `source .venv/bin/activate` from repo root, then `cd` into the lab).
- **BREAKING:** Relative links and agent doc paths that pointed at `training/day-1/docs/` must be updated; any existing local `.venv` under a lab directory is superseded by the root venv (lab-local venvs are not part of the canonical workflow).

## Non-goals

- Moving lab **product code** out of `training/day-1/coffee-shop-comparison/` (implementation stays day-scoped).
- Changing OpenSpec layout (covered by separate `consolidate-openspec-repo-root` work).
- Adding new Python packages or changing lab runtime behavior beyond path/documentation updates.

## Capabilities

### New Capabilities

- `repo-dev-layout`: Requirements for where the canonical Python virtual environment, dependency manifest, and phased workshop documentation live in this repository, and how training labs reference them.

### Modified Capabilities

- _(none — no existing main specs under `openspec/specs/` yet)_

## Impact

- **New or updated at repo root:** `docs/` (index, templates, coffee-shop-comparison artifacts), root `requirements.txt` (or merged deps), README or AGENTS guidance for venv setup.
- **Removed or emptied:** `training/day-1/docs/` after content migration (or reduced to a stub redirecting to root `docs/`).
- **Updated references:** `training/AGENTS.md`, `training/day-1/AGENTS.md`, `training/day-1/coffee-shop-comparison/README.md`, verify/plan/design cross-links, `.gitignore` (already ignores root `.venv/`).
- **Learners:** Create and activate `.venv` once at repo root; open workspace at repository root for agents, OpenSpec, and docs.

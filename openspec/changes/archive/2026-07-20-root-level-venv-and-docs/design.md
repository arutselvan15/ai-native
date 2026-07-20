## Context

Today, `training/day-1/coffee-shop-comparison/README.md` tells learners to `python3 -m venv .venv` inside the lab directory and install from lab-local `requirements.txt`. Phased plan/design/verify files live under `training/day-1/docs/` with templates in `training/day-1/docs/_templates/`. Repo-root `.gitignore` already ignores `.venv/`, but setup docs do not use a root venv. OpenSpec consolidation work (`consolidate-openspec-repo-root`) assumed Day 1 docs would stay under `day-1/docs/`; this change intentionally moves docs to the repository root and must update that prior spec delta if both changes land.

## Goals / Non-Goals

**Goals:**

- One documented Python environment at repo root for all current and near-term training labs.
- One `docs/` tree at repo root for phased workshop artifacts, indexed for agents and humans.
- Update cross-links in AGENTS files, lab README, and verify docs so paths stay valid.
- Keep lab product code under `training/day-1/coffee-shop-comparison/` unchanged except documentation references.

**Non-Goals:**

- Merging or relocating Flask app source, CSV data, or `run.sh`.
- Introducing Poetry, uv, or multi-environment tooling beyond stdlib venv + pip.
- Moving OpenSpec or opsx harness (separate change).

## Decisions

### 1. Documentation layout under `docs/`

**Choice:** `docs/<exercise-slug>/` (e.g. `docs/coffee-shop-comparison/`) plus `docs/_templates/` and `docs/README.md`, with `docs/agent-lessons.md` at root of `docs/`.

**Rationale:** Exercise slugs are stable across days; avoids duplicating `day-1` in paths now that docs are repo-wide. Day context remains in `training/day-1/AGENTS.md` and training index.

**Alternative considered:** `docs/training/day-1/...` — rejected because the user asked for root-level docs not scoped under a training day folder.

### 2. Dependency manifest

**Choice:** Add root `requirements.txt` by promoting pins from `training/day-1/coffee-shop-comparison/requirements.txt`. Remove or replace lab-local file with a one-line pointer comment in README only if duplicate causes confusion; prefer deleting lab `requirements.txt` after root file exists to avoid two sources of truth.

**Rationale:** Single install command from repo root matches single venv.

**Alternative considered:** Keep lab `requirements.txt` as symlink — rejected for portability on Windows and simplicity.

### 3. Virtual environment workflow

**Choice:** Document:

```bash
cd <repo-root>
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cd training/day-1/coffee-shop-comparison
./run.sh
```

Optional: add a short **Development** section to repo-root `README.md` if one exists or to `training/AGENTS.md`.

**Rationale:** Matches `.gitignore` and Cursor workspace-at-root pattern.

### 4. Migration of existing `training/day-1/docs/`

**Choice:** Move files with `git mv` (or equivalent) to preserve history; replace `training/day-1/docs/` with a minimal `README.md` stub that redirects to `../../../docs/` (or delete empty tree after link updates).

**Rationale:** Avoid broken bookmarks; stub helps anyone with old paths.

### 5. Interaction with `consolidate-openspec-repo-root`

**Choice:** When implementing, update requirements in that change’s delta spec (Day 1 docs path) or note in archive order: apply venv/docs change after updating consolidate spec so archived main specs do not contradict root `docs/`.

## Risks / Trade-offs

- **[Conflict with in-flight OpenSpec consolidate change]** → Align `repo-openspec-layout` requirement “Day 1 phased docs under `training/day-1/docs/`” with this change before archiving both; prefer MODIFIED requirement on root `docs/` in a follow-up sync.
- **[Learners with existing lab-local `.venv`]** → Document that they may delete lab `.venv` and recreate at root; no automated migration.
- **[Root requirements grow over time]** → Accept for workshop scale; split by optional extras files only if days diverge sharply later.

## Migration Plan

1. Add root `requirements.txt` from lab pins.
2. Create `docs/` tree; move content from `training/day-1/docs/`.
3. Global search for `day-1/docs`, `../docs/`, and lab venv instructions; fix links.
4. Update `training/AGENTS.md`, `training/day-1/AGENTS.md`, coffee-shop README and verify.md.
5. Add redirect stub or remove empty `training/day-1/docs/`.
6. Smoke-test: root venv + `./run.sh` from lab directory.

**Rollback:** Restore `training/day-1/docs/` from git history and revert AGENTS/README changes; learners can recreate lab-local venv from old README.

## Open Questions

- Whether repo-root `README.md` should own the venv quick-start or only `training/AGENTS.md` (default: both brief pointer at root README if file exists).

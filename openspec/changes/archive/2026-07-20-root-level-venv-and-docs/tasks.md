## 1. Root Python environment

- [x] 1.1 Add root `requirements.txt` with pins from `training/day-1/coffee-shop-comparison/requirements.txt`
- [x] 1.2 Remove lab-local `requirements.txt` (or replace with a comment pointing to repo root—prefer delete per design)
- [x] 1.3 Update `training/day-1/coffee-shop-comparison/README.md` run section for root `.venv` + root `pip install`
- [x] 1.4 Confirm `.gitignore` ignores root `.venv/` (adjust only if needed)

## 2. Migrate documentation to repo root

- [x] 2.1 Create `docs/` at repository root with `README.md`, `_templates/`, and `agent-lessons.md`
- [x] 2.2 Move `training/day-1/docs/coffee-shop-comparison/` to `docs/coffee-shop-comparison/` (preserve content)
- [x] 2.3 Update internal links inside moved plan/design/verify files and templates
- [x] 2.4 Add redirect stub at `training/day-1/docs/README.md` (or remove tree) pointing to root `docs/`

## 3. Update agent and training indexes

- [x] 3.1 Update `training/AGENTS.md` documentation column and layout to reference root `docs/`
- [x] 3.2 Update `training/day-1/AGENTS.md` phased paths, tables, and handoff references to root `docs/`
- [x] 3.3 Update coffee-shop README doc links from `../docs/...` to repo-root `docs/...` paths

## 4. Verify and cross-change alignment

- [x] 4.1 Update `docs/coffee-shop-comparison/verify.md` commands for root venv workflow
- [x] 4.2 Search repo for `day-1/docs` and lab-local venv instructions; fix remaining references
- [x] 4.3 If `consolidate-openspec-repo-root` is still open, MODIFIED-update its delta spec requirement that assumes `training/day-1/docs/` (align with root `docs/` before archive)
- [x] 4.4 Smoke-test: fresh root venv, `pip install -r requirements.txt`, `cd training/day-1/coffee-shop-comparison && ./run.sh`

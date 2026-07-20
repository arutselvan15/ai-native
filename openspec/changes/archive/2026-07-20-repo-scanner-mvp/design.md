## Context

Day 2 capstone intent lives in `training/day-2/spec-writing/examples/code-scanner-starter.md`. The repository already standardizes Python tooling at the root (`.venv`, `requirements.txt`) and OpenSpec at `openspec/`. There is no scanner implementation yet. Day 5 validation expects a runnable check surface (e.g. pytest or a script) that proves the scanner is read-only and honest about limits.

## Goals / Non-Goals

**Goals:**

- Ship a stdlib-first Python package under `tools/repo_scanner/` invocable as `python -m tools.repo_scanner [path]`.
- Implement three signal detectors and a Markdown report template matching the spec.
- Skip `.git`, `.venv`, `__pycache__`, and `node_modules` by default during walks.
- Add pytest tests that cover CLI success, invalid path, read-only behavior, and report sections.
- Document the command in root `README.md` or `tools/repo_scanner/README.md`.

**Non-Goals:**

- Installing third-party analysis libraries (radon, lizard) in v1.
- Writing reports to disk by default (stdout only).
- Fixing detected layout violations automatically.

## Decisions

### 1. Package layout and entrypoint

**Choice:** `tools/repo_scanner/` as a package with `__main__.py` for `python -m tools.repo_scanner`. Add `tools/__init__.py` if needed so imports resolve from repo root.

**Rationale:** Keeps training trees clean; matches Day 5 examples using `python scripts/...` while allowing module execution.

**Alternative:** Single script `scripts/scan_repo.py` — rejected for harder unit testing and package structure.

### 2. Walk and skip rules

**Choice:** `pathlib.Path.rglob` with directory-name denylist: `.git`, `.venv`, `venv`, `__pycache__`, `node_modules`, `.cursor` (optional). Scan `.py` and `.md` for line counts; `.py` only for AST.

**Rationale:** Avoids scanning virtualenvs and agent metadata; keeps first run fast on ai-native.

### 3. Thresholds (constants in `config.py`)

| Signal | Default threshold |
| --- | --- |
| Large file | > 300 lines (`.py`, `.md`) |
| Long function | function body > 60 lines (AST line span) |
| Complexity | cyclomatic complexity > 10 (simple AST visitor counting branches) |

**Rationale:** Tunable constants without CLI flags in v1 to limit scope.

### 4. Layout policy check

**Choice:** Glob `training/**/openspec/config.yaml` relative to scan root; list matches in report.

**Rationale:** Directly dogfoods `repo-openspec-layout` without coupling code to spec file paths.

### 5. Report structure

**Choice:** Fixed Markdown sections in order: `# Repo scan report`, `## Summary`, `## Signals`, subsections per signal type, `## Suggested next reads`, `## Limitations`.

**Rationale:** Predictable paste target for agents; easy snapshot testing.

### 6. Dependencies

**Choice:** Stdlib only for v1 (`ast`, `pathlib`, `argparse`). No change to `requirements.txt` unless pytest already implied for tests — pytest may already be needed for Day 5; if not in requirements, add `pytest` as dev dependency or document running tests with pip install pytest one-off. Check current requirements - only flask and pandas. Add pytest to requirements or use unittest only.

For workshop, **use unittest** in stdlib for tests to avoid requirements change, OR add pytest to requirements.txt - Day 5 mentions pytest. I'll say in design: add `pytest` to requirements.txt for test runner (minimal addition).

Actually proposal said extend only if needed - use **unittest** for v1 tests to avoid requirements.txt change.

### 7. Test layout

**Choice:** `tests/test_repo_scanner.py` at repo root or `tools/repo_scanner/tests/` — use `tests/repo_scanner/` at repo root for discoverability with `python -m pytest tests/repo_scanner` if pytest added later; for unittest: `python -m unittest tests.repo_scanner.test_scan`.

Simpler: `tests/repo_scanner/test_scan.py` with unittest.

## Risks / Trade-offs

- **[Heuristic complexity is inaccurate]** → Document in limitations; use simple AST counts, not full McCabe.
- **[Large repos are slow]** → Denylist dirs; no parallel walk in v1.
- **[False positives on generated files]** → Skip paths under `.venv`; optional future allowlist.
- **[Nested openspec may be fixed separately]** → Scanner reports truth at scan time; policy section may show zero findings after cleanup.

## Migration Plan

1. Implement package and CLI.
2. Add tests with tempfile fixtures (tiny fake repos).
3. Run against ai-native root; capture sample report in verify notes (optional).
4. Document invocation from activated root `.venv`.

**Rollback:** Remove `tools/repo_scanner/` and tests; no database or API impact.

## Open Questions

- Whether to add a `--format json` flag in a follow-up change (deferred).
- Whether coffee-shop nested OpenSpec should be removed in this change or a separate cleanup change (report-only here).

## 1. Package skeleton

- [x] 1.1 Create `tools/__init__.py` and `tools/repo_scanner/` package with `__init__.py`, `__main__.py`, and `config.py` (thresholds and skip dirs)
- [x] 1.2 Implement `cli.py` with argparse: optional path argument, exit codes for success and invalid input

## 2. Scan engine

- [x] 2.1 Implement `walk.py` to iterate scannable files under a root with directory skip rules
- [x] 2.2 Implement `signals/large_files.py` for `.py` and `.md` line counts
- [x] 2.3 Implement `signals/python_complexity.py` using AST (line span + simple branch counting); handle parse errors as warnings
- [x] 2.4 Implement `signals/layout_policy.py` for nested `training/**/openspec/config.yaml`

## 3. Report and CLI wiring

- [x] 3.1 Implement `report.py` to render Markdown sections (summary, signals, suggested next reads, limitations)
- [x] 3.2 Wire `__main__.py` to run scan and print report to stdout; errors to stderr

## 4. Tests and documentation

- [x] 4.1 Add `tests/repo_scanner/` unittest fixtures (temp dirs) covering valid scan, invalid path, report sections, and read-only behavior
- [x] 4.2 Document run command in `tools/repo_scanner/README.md` and add a one-line pointer from root `README.md`
- [x] 4.3 Manual smoke: run scanner from repo root against ai-native and confirm nested OpenSpec finding (if still present) and limitations section

## 5. Day 5 readiness

- [x] 5.1 Document a single validation command (e.g. `python -m unittest tests.repo_scanner -v`) for participants to reuse in validation evidence

# Repo scanner (Day 2 capstone MVP)

Read-only CLI that scans a local directory and prints a Markdown legibility report.

## Run

From the **repository root** with the shared venv activated:

```bash
source .venv/bin/activate
python -m tools.repo_scanner
python -m tools.repo_scanner /path/to/repo
```

Report goes to stdout; errors go to stderr.

## Signals (v1)

- **Large files** — `.py` and `.md` over 300 lines
- **Python complexity** — long functions and heuristic cyclomatic complexity (AST)
- **Layout** — nested `training/**/openspec/config.yaml` (workshop single-root convention)

## Validate (Day 5)

Run the unit tests from the repository root:

```bash
python -m unittest discover -s tests/repo_scanner -v
```

Or:

```bash
python -m unittest tests.repo_scanner.test_scan -v
```

Use this command in your validation evidence as proof the scanner behaves as specified (valid report, invalid path, read-only, limitations visible).

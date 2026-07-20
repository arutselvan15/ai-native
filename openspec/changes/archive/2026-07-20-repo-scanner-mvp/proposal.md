## Why

Engineers and AI assistants working in this repository need a fast, honest picture of where code is large, complex, or structurally risky before making changes. The Day 2 default capstone (`code-scanner-starter.md`) calls for a small scanner that surfaces legibility signals and produces paste-ready context; nothing in the repo provides that yet.

## What Changes

- Add a **read-only** Python CLI that scans a directory tree (default: repository root) and prints a **Markdown report** to stdout.
- Report **three signal classes** in v1: oversized files, high-complexity Python functions (AST-based, bounded heuristics), and **workshop layout violations** (e.g. nested `openspec/` under `training/`).
- Include explicit **limits and confidence** sections so output is safe to paste into agent context without overclaiming.
- Place implementation under `tools/repo_scanner/` with a documented entry command suitable for Day 5 validation (e.g. `python -m tools.repo_scanner`).
- Extend root `requirements.txt` only if needed (prefer stdlib for v1).
- Add a short **usage section** to repo or training docs pointing capstone participants at the scanner.

## Non-goals

- Full multi-language static analysis or security scanning.
- Modifying scanned files, auto-fixing issues, or integrating with CI in v1.
- Scanning arbitrary remote repositories (local path only).
- Replacing OpenSpec, pre-commit, or existing linters.

## Capabilities

### New Capabilities

- `repo-scanner`: CLI behavior, inputs/outputs, signal definitions, error handling, and non-modification guarantees for the repository scanner MVP.

### Modified Capabilities

- _(none — scanner may *check* `repo-openspec-layout` rules but does not change those requirements)_

## Impact

- **New:** `tools/repo_scanner/` (package + tests), optional `tests/repo_scanner/`, README snippet.
- **Updated:** root `requirements.txt` (only if a dependency is required), possibly `training/day-2/spec-writing/README.md` or root `README.md` with run instructions.
- **Unchanged:** OpenSpec layout, Day 1 lab code, existing main specs under `openspec/specs/`.

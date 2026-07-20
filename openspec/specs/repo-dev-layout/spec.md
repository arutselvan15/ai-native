# repo-dev-layout Specification

## Purpose
TBD - created by archiving change root-level-venv-and-docs. Update Purpose after archive.
## Requirements
### Requirement: Canonical Python virtual environment at repository root

The ai-native repository MUST document a single shared Python virtual environment at `.venv/` relative to the repository root. Training lab READMEs and verify artifacts MUST instruct learners to create, activate, and use this root environment—not a lab-local `.venv/` under `training/`.

#### Scenario: Root gitignore covers venv

- **WHEN** `.gitignore` at the repository root is read
- **THEN** it MUST ignore `.venv/` (or equivalent pattern) so the root virtual environment is never committed

#### Scenario: Lab run instructions use root venv

- **WHEN** a learner follows the coffee-shop lab README run section
- **THEN** the documented steps MUST include creating or activating `.venv` from the repository root before running the lab entry script

### Requirement: Shared dependency manifest at repository root

Python dependencies for training labs that use the shared environment MUST be declared in a root-level manifest (e.g. `requirements.txt` at the repository root). Labs MUST NOT require a separate, conflicting dependency file as the canonical install source unless the lab is explicitly documented as using an isolated environment (which this repository MUST NOT use for Day 1).

#### Scenario: Install from repository root

- **WHEN** a learner runs `pip install -r requirements.txt` with the root venv activated and current working directory at the repository root
- **THEN** all packages required to run `training/day-1/coffee-shop-comparison/` MUST be installed successfully

### Requirement: Phased workshop documentation at repository root

Plan, design, verify templates and exercise artifacts for workshop phased workflows MUST live under `docs/` at the repository root. The canonical path MUST NOT be `training/<day>/docs/` for new or migrated content.

#### Scenario: Coffee shop phased docs under root docs

- **WHEN** the repository tree is inspected for coffee-shop plan, design, and verify markdown
- **THEN** those files MUST exist under `docs/` (e.g. `docs/coffee-shop-comparison/plan.md`) and MUST NOT remain only under `training/day-1/docs/`

#### Scenario: Root docs index exists

- **WHEN** a learner or agent reads `docs/README.md`
- **THEN** it MUST index phased artifacts and point to templates under `docs/_templates/`

### Requirement: Agent instructions reference root docs and venv

Training agent documentation MUST tell assistants and learners to use repository-root `docs/` for phased plan/design/verify work and repository-root `.venv` for Python labs, while keeping product code paths under `training/<day>/` unchanged.

#### Scenario: Training index updated

- **WHEN** an agent reads `training/AGENTS.md` after this change
- **THEN** it MUST reference root `docs/` (not `day-1/docs/`) as the documentation home for phased workshop artifacts

#### Scenario: Day 1 agent instructions updated

- **WHEN** an agent reads `training/day-1/AGENTS.md` after this change
- **THEN** phased workflow gates MUST reference paths under repository-root `docs/` and MUST NOT list `day-1/docs/` as the source of truth


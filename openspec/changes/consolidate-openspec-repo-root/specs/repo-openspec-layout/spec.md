## ADDED Requirements

### Requirement: Single OpenSpec root at repository root

The ai-native repository MUST expose exactly one OpenSpec planning root at `openspec/` relative to the repository root. Training exercises MUST NOT contain a nested `openspec/` directory that would become the nearest OpenSpec root when the CLI or agents run from those paths.

#### Scenario: CLI from Day 1 lab resolves to repo root

- **WHEN** a user runs `openspec list --json` with current working directory `training/day-1/coffee-shop-comparison/`
- **THEN** the JSON `root.path` MUST equal the absolute path of the ai-native repository root (not the coffee-shop-comparison directory)

#### Scenario: No nested openspec under training labs

- **WHEN** the repository tree is inspected under `training/`
- **THEN** no path matching `training/**/openspec/config.yaml` MUST exist except none (zero nested OpenSpec configs)

### Requirement: Single opsx harness at repository root

OpenSpec workflow commands and skills (`opsx-*` commands and `openspec-*` skills) MUST exist only under the repository root `.cursor/` and `.github/` trees. Training lab folders MUST NOT duplicate those harness files.

#### Scenario: Coffee shop lab has no duplicate harness

- **WHEN** the tree under `training/day-1/coffee-shop-comparison/` is listed
- **THEN** it MUST NOT contain `.cursor/commands/opsx-*`, `.cursor/skills/openspec-*`, `.github/prompts/opsx-*`, or `.github/skills/openspec-*`

### Requirement: Day 1 phased docs remain the lab planning source

Day 1 coffee-shop work MUST continue to use plan, design, implement, and verify artifacts under `training/day-1/docs/` as defined in `training/day-1/AGENTS.md`. Consolidating OpenSpec MUST NOT require Day 1 labs to create OpenSpec changes for the warm-up exercise.

#### Scenario: Day 1 agent instructions unchanged in intent

- **WHEN** an agent reads `training/day-1/AGENTS.md` after this change
- **THEN** the phased workflow gates and paths under `day-1/docs/` MUST still be documented as the source of truth for Day 1 planning and verification

### Requirement: Training docs state repo-root OpenSpec expectations

Agent and learner documentation MUST state that capstone and repo-wide OpenSpec work uses the repository root `openspec/` directory and that learners SHOULD open the Cursor workspace at the repository root for `/opsx:*` commands.

#### Scenario: Training index mentions single root

- **WHEN** an agent reads `training/AGENTS.md`
- **THEN** it MUST find explicit guidance that OpenSpec lives at the repo root and that Day 1 does not use nested OpenSpec under labs

#### Scenario: Day 2 entry mentions workspace root

- **WHEN** a learner reads `training/day-2/spec-writing/README.md`
- **THEN** it MUST include guidance to open the workspace at the ai-native repository root before using OpenSpec commands

## Context

The ai-native repo is a learning monorepo: repo-root harness (AGENTS.md, OpenSpec, opsx skills) plus independent `training/day-*` exercises. OpenSpec was initialized at the repo root and again inside `training/day-1/coffee-shop-comparison/`, including duplicate `.cursor` and `.github` opsx scaffolding (currently untracked). The CLI’s nearest-root resolution causes `openspec list` from the lab to bind to the nested root, while Day 2 capstone material assumes OpenSpec at the repository root.

Day 1 already uses a separate phased-doc workflow under repository-root `docs/` and does not require OpenSpec for the warm-up lab.

## Goals / Non-Goals

**Goals:**

- One OpenSpec planning home at `openspec/` on the repo root for capstone and repo-wide changes.
- One opsx harness at repo-root `.cursor/` and `.github/`.
- Documented expectations for learners and agents (workspace at repo root; Day 1 stays on docs workflow).
- Verifiable CLI behavior from the coffee-shop directory after cleanup.

**Non-Goals:**

- Registering an external OpenSpec store (`--store`) or splitting spec repo from code.
- Migrating Day 1 plan/design/verify into OpenSpec changes.
- Changing coffee-shop application behavior, dependencies, or verify evidence requirements.
- Adding main specs under `openspec/specs/` beyond what archive/sync does after this change ships.

## Decisions

### Decision: Delete nested scaffold (option A), not repoint via symlinks

Remove nested `openspec/` and duplicate opsx files under the coffee-shop lab rather than symlinking to the repo root.

**Rationale:** Symlinks behave differently across OS and zip exports; deletion is explicit and matches “no nested root” requirements.

**Alternatives considered:** Keep lab-in-a-box harness (rejected: split-brain); registered store (rejected: overkill for single repo).

### Decision: Document in training AGENTS + Day 2 README

Add short, durable bullets to `training/AGENTS.md`, `training/day-1/AGENTS.md`, and a workspace note in `training/day-2/spec-writing/README.md`.

**Rationale:** Prevents re-scaffolding the lab and aligns facilitators with Day 2 OpenSpec steps.

**Alternatives considered:** Only root `AGENTS.md` (rejected: training scope rule says day-level AGENTS for work under `training/`).

### Decision: Light touch on `openspec/config.yaml`

Add a brief optional `context:` block at repo root describing this as a training repo, single OpenSpec root, and GIVEN/WHEN/THEN preference for capstone specs.

**Rationale:** Improves artifact quality for Day 2+ without duplicating day-level rules.

**Alternatives considered:** Empty config (acceptable but misses opportunity).

## Risks / Trade-offs

- **[Risk] Learners open only the coffee-shop subfolder in the IDE** → **Mitigation:** README and Day 2 README state “open repo root”; verify step in tasks runs `openspec list` from lab cwd.
- **[Risk] Lost portability of a standalone lab zip** → **Mitigation:** Acceptable trade-off for monorepo; Day 1 warm-up does not depend on OpenSpec in the lab folder.
- **[Risk] Untracked duplicate files reappear if someone re-runs `openspec init` in the lab** → **Mitigation:** Document “do not init OpenSpec under training labs” in `training/AGENTS.md`.

## Migration Plan

1. Delete nested paths under `training/day-1/coffee-shop-comparison/` (see tasks.md).
2. Update training documentation.
3. Optionally extend repo-root `openspec/config.yaml` context.
4. Verify: `openspec list --json` from coffee-shop cwd shows repo root path; `openspec doctor` at repo root remains ok.
5. Rollback: restore deleted files from git if they were committed; for untracked scaffolds, re-init is possible but discouraged.

## Open Questions

- None blocking implementation. Facilitators may later add a one-line note to `training/day-1/coffee-shop-comparison/README.md` if learners frequently open the wrong workspace.

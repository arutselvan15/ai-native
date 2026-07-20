## 1. Remove nested OpenSpec and duplicate harness

- [x] 1.1 Delete `training/day-1/coffee-shop-comparison/openspec/` (entire directory)
- [x] 1.2 Delete duplicate opsx commands under `training/day-1/coffee-shop-comparison/.cursor/commands/` (`opsx-*.md`)
- [x] 1.3 Delete duplicate openspec skills under `training/day-1/coffee-shop-comparison/.cursor/skills/` (`openspec-*`)
- [x] 1.4 Delete duplicate opsx prompts under `training/day-1/coffee-shop-comparison/.github/prompts/` (`opsx-*.prompt.md`)
- [x] 1.5 Delete duplicate openspec skills under `training/day-1/coffee-shop-comparison/.github/skills/` (`openspec-*`)

## 2. Update training documentation

- [x] 2.1 Add repo-root OpenSpec guidance to `training/AGENTS.md` (single root; no nested init under labs; capstone uses repo `openspec/`)
- [x] 2.2 Add a short note to `training/day-1/AGENTS.md` that Day 1 does not use OpenSpec under the lab; OpenSpec is repo-root only
- [x] 2.3 Add workspace-at-repo-root note to `training/day-2/spec-writing/README.md` before OpenSpec steps

## 3. Repo-root OpenSpec config (optional but recommended)

- [x] 3.1 Add a concise `context:` block to `openspec/config.yaml` describing training-repo scope, single root, and GIVEN/WHEN/THEN preference for capstone specs

## 4. Verification

- [x] 4.1 From `training/day-1/coffee-shop-comparison/`, run `openspec list --json` and confirm `root.path` is the ai-native repository root
- [x] 4.2 Run `openspec doctor` from repository root and confirm OpenSpec root is ok
- [x] 4.3 Confirm no `training/**/openspec/config.yaml` paths remain except repo-root `openspec/config.yaml`

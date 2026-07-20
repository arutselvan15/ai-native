# AGENTS.md — training

Hands-on exercises for AI-native engineering live under **`training/`**. Each day is an independent mini-project: its own README, optional phased docs, and code where applicable.

| Day | Status | Agent instructions | Documentation |
| --- | --- | --- | --- |
| **Day 1** | Active | [`day-1/AGENTS.md`](day-1/AGENTS.md) | [`day-1/docs/`](day-1/docs/README.md) |
| Day 2 | Material | _(add `day-2/AGENTS.md` when you start)_ | `day-2/` |
| Day 3 | Material | `day-3/AGENTS.md` _(when started)_ | `day-3/` |
| Day 4 | Material | `day-4/AGENTS.md` _(when started)_ | `day-4/` |
| Day 5 | Material | `day-5/AGENTS.md` _(when started)_ | `day-5/` |

Human overview and links: [`../README.md`](../README.md).

## Which file to follow

- **Any work under `training/`:** start here, then open the **day folder’s `AGENTS.md`** for that exercise.
- **Day 1:** follow [`day-1/AGENTS.md`](day-1/AGENTS.md) only. Plan, design, and verify under `day-1/docs/`; lab code under `day-1/coffee-shop-comparison/`.
- **Later days:** when a day gets its own `AGENTS.md`, use it for all work inside that day’s tree.

Do not mix day-level rules or doc paths across days.

## OpenSpec (repo root only)

OpenSpec lives at **`openspec/`** on the **ai-native repository root**, with opsx commands and skills under repo-root `.cursor/` and `.github/`. Do **not** run `openspec init` or add nested `openspec/` directories under `training/` labs—that breaks CLI “nearest root” resolution.

- **Day 1:** phased plan/design/verify under `day-1/docs/` only (no OpenSpec changes for the warm-up lab).
- **Day 2+ capstone:** create and apply changes under repo-root `openspec/changes/`. Open the Cursor workspace at the **repository root** so `/opsx:*` and the `openspec` CLI use the same planning home.

## Layout

```text
training/
├── AGENTS.md          # This index
├── day-1/             # Active lab + plan → design → implement → verify
├── day-2/             # Spec writing, implementation planning
├── day-3/             # Skills and MCP context
├── day-4/             # Harness blueprint, baseline assessment
└── day-5/             # Validation and evidence
```

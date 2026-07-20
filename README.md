# AI-native learning

Personal workspace for learning **AI-native engineering**: working with agents, structured docs, specs, skills, and harnesses—not just writing code faster.

Hands-on material lives under [`training/`](training/). Each day is a self-contained exercise folder with its own README. Agent rules for exercises: [`training/AGENTS.md`](training/AGENTS.md) (repo-wide: [`AGENTS.md`](AGENTS.md)).

| Day | Focus | Start here |
| --- | --- | --- |
| Day 1 | Coffee-shop comparison (AI-assisted coding warm-up) | [`training/day-1/README.md`](training/day-1/README.md) |
| Day 2 | Ground a capstone, then spec with OpenSpec (proposal, spec, design, tasks, implement, verify) | [`training/day-2/spec-writing/README.md`](training/day-2/spec-writing/README.md) |
| Day 3 | Curated context and skill creation | [`training/day-3/skill-creation/participant_guide.md`](training/day-3/skill-creation/participant_guide.md) |
| Day 4 | MVP harness blueprint and baseline assessment | [`training/day-4/assemble-harness-blueprint/README.md`](training/day-4/assemble-harness-blueprint/README.md) |
| Day 5 | Repo legibility, deterministic checks, evidence package | [`training/day-5/hands-on-validation/README.md`](training/day-5/hands-on-validation/README.md) |

**Suggested path:** begin with [Day 1](training/day-1/README.md)—follow [`training/day-1/AGENTS.md`](training/day-1/AGENTS.md) and [`docs/`](docs/README.md) (repository root) for plan → design → implement → verify. Create the shared Python environment once at the repo root (`python3 -m venv .venv`, then `pip install -r requirements.txt`).

**Repo scanner (Day 2 capstone):** from repo root, `python -m tools.repo_scanner` — see [`tools/repo_scanner/README.md`](tools/repo_scanner/README.md).

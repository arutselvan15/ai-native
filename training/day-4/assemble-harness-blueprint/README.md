# Day 4 Hands-on: Assemble the Harness Blueprint

## What This Folder Contains

Use this `README.md` as the entry point for the second hands-on of Day 4.

```text
day-4/assemble-harness-blueprint/
|- facilitator_notes.md
`- README.md
```

You start this session with the baseline scorecard you produced in the previous session. Here you use the `ai-harness-setup` skill to close gaps by generating repository harness setup, review that output critically, then re-run the assessment to measure the lift and close anything the harness left behind.

Skill reference: [`ai-harness-setup` skill README](https://github.com/cisco-genai/awesome-cisco/blob/main/skills/ai-harness-setup/README.md)

## Exercise Goal

Day 4 shifts from creating a feature or skill to creating the delivery system around future work. You already have a baseline scorecard from the previous session, so now you use the harness to close gaps, then re-measure to confirm the impact.

By the end of this exercise, you should:

1. Install and run the `ai-harness-setup` skill against your repo or workshop sandbox.
2. Capture what the harness detected, proposed, created, or modified.
3. Analyze the output against repo reality and walk through what the harness added.
4. Re-run the `ai-native-assessment` skill and compare against your baseline, noting which categories moved.
5. Run a short, targeted hardening sprint on the top gaps the harness did not close on its own.

This section is not about accepting every generated file at face value. The point is to use the harness to accelerate setup, then inspect the result carefully enough to understand what it actually changed.

## How This Fits Into The Week

The week is designed as one coherent SDLC progression:

| Day | Artifact or capability |
| --- | --- |
| Day 1 | Coffee-shop comparison build (AI-assisted coding) |
| Day 2 | Ground the capstone, then OpenSpec: proposal, spec, design, tasks, implementation, verify |
| Day 3 | Curated context and skill creation |
| Day 4 | MVP harness blueprint and hardening assessment |
| Day 5 | Repo legibility, deterministic checks, and evidence package |

Earlier in the week, participants created product intent, spec-driven artifacts, implementation slices, and targeted agent context. This Day 4 section focuses on the repo-wide operating system around that work: workflow tooling, deterministic checks, AI skills, documentation, and IDE wiring. You start from the baseline you captured in the previous session: the harness is what closes most of those gaps, and you re-run the assessment to prove it.

## Starting Point

Before you begin, make sure you have:

- Access to the `ai-harness-setup` skill.
- Your baseline scorecard, `docs/ai-native-scorecard.md`, from the previous session.
- Enough repo access to inspect manifests, config, CI, and docs.
- A willingness to review generated setup critically instead of assuming it is correct.

Helpful but not strictly required:

- Your `AGENTS.md` or equivalent repo instruction file.
- Day 2 OpenSpec artifacts or another spec-driven workflow already present in the repo.
- Day 3 skills or curated context that already reveal how the repo should be operated.

## What the Harness Is Trying To Do

The `ai-harness-setup` skill is designed to take a repository from ad hoc AI usage toward a more durable agent-driven workflow. Based on the current skill instructions in the `awesome-cisco` repository, the setup flow includes:

- Inspecting the repo first to detect languages, frameworks, package managers, CI, monorepo layout, existing docs, existing spec workflow, and existing AI IDE configuration.
- Initializing APM if needed.
- Preserving an existing spec-driven workflow or installing OpenSpec when none exists.
- Adding deterministic checks and wiring them into local commands, CI, and hooks.
- Adding Dependabot when needed.
- Installing AI workflow skills and relevant MCP servers.
- Creating docs that explain the workflow.
- Configuring AI IDE surfaces such as GitHub Copilot, Cursor, Claude Code, Windsurf, and OpenCode when applicable.
- Running a mandatory verification pass against the generated changes.

That is a large surface area. Your job in this session is to use the harness as an accelerator, then understand what setup it introduced across the repo. Notice that these surfaces map directly onto the categories the assessment scores. Running the harness is what hardens most of them, which is why you measure before and after.

## Step 1: Install the Harness Skill

Use one of the install paths from the [`ai-harness-setup` skill README](https://github.com/cisco-genai/awesome-cisco/blob/main/skills/ai-harness-setup/README.md).

Option A: install with APM

```bash
apm install cisco-genai/awesome-cisco/skills/ai-harness-setup -t opencode -t cursor -t copilot -t claude -t windsurf
```

Option B: install with `npx skills`

```bash
npx skills add https://github.com/cisco-genai/awesome-cisco --skill ai-harness-setup
```

Notes:

- Use the install path that matches the toolchain you are using in the workshop.
- If you use the APM path, trim the `-t` targets to the AI tools your team actually uses.
- If access to `awesome-cisco` is private in your environment, make sure authentication is already set up before starting.

## Step 2: Run the Harness Setup Skill

Command:

```text
/ai-harness-setup
```

Run the command in the target repository or workshop sandbox.

As the harness runs, capture:

- Detection summary: stack, tooling, CI, IDEs, monorepo status.
- Setup decisions: GitHub Agentic Workflows on or off, deterministic checks mode, existing workflow preserved or OpenSpec installed.
- Files added or modified.
- Skills and MCP servers installed.
- Local validation commands and CI wiring that now exist.
- Docs and AI IDE configurations that were added.
- Verification results, including gaps that were fixed.

If the skill made assumptions that were not grounded in the repo, note them explicitly in your analysis.

## Step 3: Investigate What Was Added

Now go look through the files and directories the harness added or changed.

Focus on surfaces such as:

- `apm.yml` and `apm.lock.yaml`
- `openspec/`
- `.github/`
- `.claude/`
- `.cursor/`
- `.windsurf/`
- `.opencode/`
- `docs/`
- `AGENTS.md`
- `CONTRIBUTING.md`

As you inspect them, ask:

- What new workflow does this file or directory introduce?
- Is it clearly tied to this repo's actual stack and tooling?
- What would a contributor or agent now do differently because this exists?
- Which files appear to be generated scaffolding, and which ones appear to contain real repo-specific setup?

## Step 4: Re-run the Assessment and Compare

Now re-run the `ai-native-assessment` skill on the same repo:

```text
/ai-native-assessment
```

Then compare the new `docs/ai-native-scorecard.md` against the baseline you recorded in the previous session:

- Which categories went up after the harness ran?
- Which categories are still low?
- Does the composite score reflect the work the harness actually did?

The goal is to see the harness as the hardening step and to confirm the lift with evidence rather than assuming the setup was enough.

## Step 5: Short Hardening Sprint on What Is Left

The harness closes most gaps, but it installs a fairly standard setup. Some gaps are repo-specific and will not be closed by generic setup.

Pick one or two of the highest-leverage gaps the harness did not close, and fix them:

- A repo-specific validation path or check the harness did not wire.
- Missing or thin repo-specific content in `AGENTS.md`, `CONTRIBUTING.md`, or `docs/`.
- A skill or IDE configuration detail that only matters for this repo's stack.

Keep the sprint tightly scoped. The aim is to close what the harness missed, not to redo what it already did. If time permits, re-run the assessment once more to confirm the targeted fixes moved the relevant sub-metrics.

## Definition Of Done

You are done when:

- You ran the `ai-harness-setup` skill or completed an equivalent guided pass.
- You captured what the harness detected and changed.
- You reviewed the output against the actual repo and the harness instructions.
- You walked through the important files and directories the harness added or changed.
- You re-ran the `ai-native-assessment` skill and compared the result against your baseline.
- You closed at least one remaining gap that the harness did not fix on its own.
- You did not treat generated setup as complete without inspection.

## Common Pitfalls

- Running the harness as a black box and accepting the output without review.
- Letting the harness replace existing tooling that should have been preserved.
- Confusing generated docs with correct docs. The content still has to match the repo.
- Assuming verification means the setup is perfect. It still needs engineering judgment.
- Installing every possible skill instead of only the ones that match the repo.
- Treating the harness as done after setup. Re-measure to confirm the lift, then close the residual gaps.
- Hand-fixing what the harness already did. Target only the gaps it left behind, and avoid changes that look impressive but do not change daily repo workflows.

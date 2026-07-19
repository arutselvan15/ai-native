# Day 4 Hands-on: Baseline Assessment

## What This Folder Contains

Use this `README.md` as the entry point for the first hands-on of Day 4.

```text
day-4/baseline-assessment/
|- facilitator_notes.md
`- README.md
```

This section uses the `ai-native-assessment` skill to score your repo and find its biggest gaps before you build the harness. This is a measurement session: you produce a baseline scorecard and a prioritized gap list, and you do not fix anything yet. You build the harness and re-run this same assessment in the next session to see what moved.

Skill references:

- [AI-Native Assessment skill](https://github.com/cisco-genai/awesome-cisco/tree/main/skills/ai-native-assessment)

## Exercise Goal

This session establishes a baseline for your repo before you assemble the harness, so you can measure the harness's impact later.

By the end of this exercise, you should:

1. Install and run the `ai-native-assessment` skill against your local project.
2. Review the generated scorecard and understand the repo's strongest and weakest AI-native capabilities.
3. Record your baseline score and the top two or three gaps to carry into the next session.

The point is not just to get a score. The baseline and the prioritized gap list are the inputs you will act on after the harness is in place.

## How This Fits Into The Week

The week is designed as one coherent SDLC progression:

| Day | Artifact or capability |
| --- | --- |
| Day 1 | Coffee-shop comparison build (AI-assisted coding) |
| Day 2 | Ground the capstone, then OpenSpec: proposal, spec, design, tasks, implementation, verify |
| Day 3 | Curated context and skill creation |
| Day 4 | MVP harness blueprint and hardening assessment |
| Day 5 | Repo legibility, deterministic checks, and evidence package |

Earlier in the week, participants created intent, implementation artifacts, and targeted agent context. You run this assessment first, before assembling the harness, to capture a clean baseline. In the next session you build the harness and re-run this same assessment to measure what changed.

## Starting Point

Before you begin, make sure you have:

- A safe local project or sandbox repository to assess.
- Access to the `ai-native-assessment` skill from `cisco-genai/awesome-cisco`.
- Permission to let the skill inspect the repository and write `docs/ai-native-scorecard.md`.
- Enough repo familiarity to judge whether the findings are real and useful.

Helpful but not strictly required:

- A repo that already has some of the week's artifacts, such as `AGENTS.md`, `openspec/`, deterministic checks, or AI IDE configuration.

## What the Assessment Is Trying To Do

The `ai-native-assessment` skill is a repository assessment that evaluates how ready a project is for repeatable AI-native development.

It looks for the core workflow primitives that make a repo easier for both humans and agents to work in, such as:

- spec-driven development
- deterministic checks
- AI tooling and skills
- documentation structure
- AI IDE configuration
- agentic legibility

The assessment is needed because many repos have fragments of these practices, but not a complete, reliable workflow. A repo may have tests but no clear validation path, docs but no routing, AI setup but no repo-specific instructions, or specs with no operational workflow around them.

This assessment helps teams:

- understand what AI-native capabilities already exist in the repo
- identify the most important gaps and how to fix them
- prioritize high-leverage fixes instead of making random improvements

The `ai-native-assessment` skill evaluates a repository across six weighted categories:

| # | Category | Weight |
|---|----------|--------|
| 1 | Spec-Driven Development | 20% |
| 2 | Deterministic Checks | 25% |
| 3 | AI Tooling & Skills | 15% |
| 4 | Documentation Tree | 15% |
| 5 | AI IDE Configuration | 10% |
| 6 | Agentic Legibility | 15% |

It scans the repo, scores each area on a `0-4` scale, writes `docs/ai-native-scorecard.md`, and recommends actions ordered by leverage.

In this workshop, you are using the output to answer three questions:

- What is already working well in this repo?
- What gaps are dragging down the score or making agent workflows harder?
- Which improvements are worth fixing right now in a short sprint?

## Step 1: Install the Assessment Skill

Install the skill from the `awesome-cisco` repo:

- https://github.com/cisco-genai/awesome-cisco/tree/main/skills/ai-native-assessment

The README there includes the install instructions.

Option A: install with APM

```bash
apm install cisco-genai/awesome-cisco/skills/ai-native-assessment -t opencode -t cursor -t copilot
```

Option B: install with `npx skills`

```bash
npx skills add https://github.com/cisco-genai/awesome-cisco --skill ai-native-assessment
```

Notes:

- Use the install path that matches the toolchain you are using in the workshop.
- If you use APM, trim the `-t` targets to the AI tools your team actually uses.
- If `awesome-cisco` access is private in your environment, make sure `GITHUB_TOKEN` and org access are already set up before starting.
- When running the assessment, use a stronger thinking model such as `gpt-5.4` or `opus-4.6`.

## Step 2: Run the Assessment Skill

Invoke the skill in your target repository.

Examples from the skill README:

```text
/ai-native-assessment
```

As the assessment runs, pay attention to:

- Which files, configs, and signals it used as evidence.
- The category scores and composite score.
- The assigned maturity tier.
- The top recommended actions.
- Any places where the score seems directionally right but the explanation needs scrutiny.

Primary output:

- `docs/ai-native-scorecard.md`

Workshop note:

- The skill can also attempt leaderboard submission. For this session, the scorecard and the recommended actions are the primary outputs. If you are working on a project for this assignment rather than a real production repository, do not submit it to the leaderboard.

## Step 3: Read the Scorecard Carefully

Do not stop at the summary score.

Read through the scorecard and look for:

- Low-scoring sub-metrics with clear evidence.
- Categories where a small amount of work would unlock a noticeable improvement.
- Missing workflow primitives such as checks, docs, or IDE configuration.
- Cases where something exists in fragments but is not wired into an actual developer workflow.

Ask:

- Which gaps are real blockers for agents or contributors?
- Which actions are mostly documentation, configuration, or wiring work and therefore cheap to fix?
- Which gaps are merely cosmetic, and which ones would materially improve delivery quality?

## Step 4: Record Your Baseline

This is a measurement session, so stop at recording. Do not start fixing gaps yet.

Capture:

- The composite score and the assigned maturity tier.
- The per-category scores across the six categories.
- The top two or three recommended actions, in priority order.

Keep this baseline somewhere you can find it next session. In the harness session you build the harness, re-run this exact assessment, and compare against this baseline to see which categories moved.

## Definition Of Done

You are done when:

- You installed and ran the `ai-native-assessment` skill on a local project or sandbox repo.
- You produced and reviewed `docs/ai-native-scorecard.md`.
- You identified the highest-leverage gaps instead of reacting only to the overall score.
- You recorded a baseline score and a prioritized gap list to carry into the harness session, with no fixes made yet.

## Common Pitfalls

- Treating the composite score as the only thing that matters.
- Accepting every recommendation without checking the evidence behind it.
- Confusing the presence of a file with the presence of a usable workflow.
- Trying to start fixing gaps now. This session is measurement only; the fixes happen after the harness is built.

# Day 2 Hands-on: From Design to Tasks, Implementation, and Verify

## What This Folder Contains

Use this `README.md` as the entry point for the second half of Day 2.

```text
day-2/implementation-plan-development/
|- facilitator_notes.md
`- README.md
```

This section picks up after you have created `proposal.md`, the specs, and `design.md`. The goal is to turn those artifacts into executable work, implement the change, and finish with testing and verification.

Facilitators should also use [facilitator_notes.md](facilitator_notes.md) for session guidance, coaching interventions, and expected participant outputs.

## Exercise Goal

This is the delivery half of Day 2.

By the end of the exercise, you should:

1. Generate `tasks.md` from `proposal.md`, the specs, and `design.md`.
2. Execute the work in a deliberate sequence.
3. Keep the implementation aligned to the agreed scope.
4. Test and verify whether the change is actually working.

If the spec-writing section created clarity, this section should feel like disciplined execution rather than improvisation.

## How This Fits Into The Week

The week is designed as one coherent SDLC progression:

| Day | Artifact or capability |
| --- | --- |
| Day 1 | Coffee-shop comparison build (AI-assisted coding) |
| Day 2 | Ground the capstone, then OpenSpec: proposal, spec, design, tasks, implementation, verify |
| Day 3 | Curated context and skill creation |
| Day 4 | MVP harness blueprint and hardening assessment |
| Day 5 | Repo legibility, deterministic checks, and evidence package |

In the first Day 2 section you defined what should be built and how. In this section you convert that into tasks, produce the code or repo changes, and verify the result.

## Inputs Required

Do not start this section until you have:

- A `proposal.md`.
- Specs written with `GIVEN / WHEN / THEN` scenarios.
- A `design.md`.

If `design.md` still has major unanswered questions, resolve them before generating tasks.

## Step 1: Generate And Right-Size `tasks.md`

Command: `/opsx:continue <name-of-change>`

Use OpenSpec to generate `tasks.md` from `proposal.md`, the specs, and `design.md`, then review the output before coding.

The tasks should be:

- Small enough to execute and review.
- Ordered by dependency.
- Explicit about what changes where.
- Linked to testing and verification, not just coding.

Before moving on, inspect `tasks.md` for realism.

Ask:

- Which task creates the first end-to-end working slice?
- Which tasks can be parallelized, and which must stay sequential?
- Which tasks are risky or likely to reveal hidden ambiguity?
- What is the minimum set of tasks required to reach a verified result?

If the output gives you giant tasks such as "implement the feature," keep breaking them down until each task has a clear completion signal.

Cut or defer anything that does not help you reach the first useful verified slice.

## Step 2: Stay Aligned While You Work

As implementation starts, keep checking the artifacts instead of relying on memory.

- Re-check the specs when uncertainty appears.
- Use `design.md` to guide structure, not to justify unnecessary expansion.
- Update `tasks.md` if new facts or blockers emerge.
- Separate actual blockers from nice-to-have improvements.

If implementation reveals a mismatch between the codebase and `design.md`, adjust `design.md` or `tasks.md` explicitly instead of silently drifting away from the specs.

## Step 3: Implement Against The Spec

Command: `/opsx:apply <name-of-change>`

Start a new session when you run `/opsx:apply` so the implementation pass starts with cleaner context and the approved artifacts in place.

Start execution with the smallest high-confidence task, and work through `tasks.md` deliberately.

## Step 4: Test The Work Done

After implementation, test what was actually built.

Use the most relevant checks available in the repo to evaluate the completed slice, such as:

- Unit or integration tests.
- CLI output.
- Lint or typecheck results.
- Generated artifacts.
- Before-and-after behavior in a small repro.

Prefer observable evidence over "the code looks right." If you cannot run a check, say why.

## Step 5: Use OpenSpec Verify

Command: `/opsx:verify <name-of-change>`

After testing the work directly, run OpenSpec verify to check whether the implementation still matches `proposal.md`, the specs, `design.md`, and `tasks.md`.

OpenSpec docs describe `/opsx:verify` as checking three dimensions:

- Completeness: whether tasks, requirements, and scenarios are covered.
- Correctness: whether implementation matches spec intent.
- Coherence: whether the code still reflects the design decisions.

Capture what passed, what failed, what was not verified, and any residual risk before closing the section.

## Definition Of Done

You are done when:

- You generated `tasks.md` from `proposal.md`, the specs, and `design.md`.
- The tasks were reviewed and reduced to a realistic slice.
- You completed the intended implementation work for that slice.
- You tested the completed work and explicitly documented what could not be tested.
- You ran `/opsx:verify` or explicitly documented what could not be verified.
- The final result still matches `proposal.md`, the specs, `design.md`, and `tasks.md`.
- You captured remaining risks, assumptions, or deferred work.

## Common Pitfalls

- Generating tasks that are still too abstract. Each task should have a clear completion signal.
- Letting implementation drift away from the specs. If the plan changes, update the artifacts or call out the change.
- Treating testing or verification as optional. "Looks good" is not the same as tested or verified.
- Using the full backlog as today's scope. Finish a small verified slice before taking on more.
- Hiding unresolved issues. Document what remains open so the next day starts from facts, not assumptions.

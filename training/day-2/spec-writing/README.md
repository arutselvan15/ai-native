# Day 2 Hands-on: Ground Your Capstone, Then Spec It With OpenSpec

## What This Folder Contains

Use this `README.md` as the entry point for the first half of Day 2.

```text
day-2/spec-writing/
├── README.md
├── facilitator_notes.md   (facilitator repo only)
└── examples/
    └── code-scanner-starter.md
```

This is where your week-long capstone begins. You pick and ground a use case, then turn it into spec-driven engineering inputs using OpenSpec.

## Exercise Goal

Day 2 moves from a use-case idea to technical intent.

By the end of this exercise you will have:

1. A grounded use case - your own, or the default code scanner.
2. A `proposal.md` that defines the change: the why and the scope.
3. Specs that capture expected behavior as `GIVEN / WHEN / THEN` scenarios.
4. A `design.md` that explains the implementation approach and tradeoffs.

Do not jump into coding yet. This section is about creating enough clarity that implementation can be delegated, reviewed, and verified.

## How This Fits Into The Week

| Day | Artifact or capability |
| --- | --- |
| Day 1 | Coffee-shop build warm-up (AI-assisted coding) |
| Day 2 | Ground the capstone, then OpenSpec: proposal, spec, design, tasks, implementation, verify |
| Day 3 | Curated context and skill creation |
| Day 4 | MVP harness blueprint and hardening assessment |
| Day 5 | Repo legibility, deterministic checks, and evidence package |

Day 1 was a warm-up build. This section starts the capstone you carry through the rest of the week.

## Step 0: Pick And Ground Your Capstone Use Case

This is your capstone for the rest of the week, so choose something bounded and real. Pick one lane.

### Lane A: Your Own Repo Or Use Case

Use this lane if you have a real repository, backlog item, workflow, or engineering problem that is safe to discuss and practical to work on this week.

Good candidates:

- A repo that would benefit from better AI-readable context and checks.
- A repeated engineering workflow your team wants to make more reliable.
- A bounded feature, tool, scanner, migration helper, or validation workflow.
- A problem where the output can become useful in afternoon application time.

Avoid:

- Anything blocked by access, approvals, or sensitive data.
- Large platform rewrites.
- Vague goals such as "improve the repo" without a specific user or outcome.

### Lane B: Default Code Scanner

Use this lane if you do not have a ready use case or want the shared default. Open [examples/code-scanner-starter.md](examples/code-scanner-starter.md) and use it as intent grounding, not a finished answer.

### Ground The Intent (both lanes, ~5-10 minutes)

Before OpenSpec generates anything, get to a short, specific statement of intent. Use the agent as an interviewer and challenger:

```text
I am starting a week-long AI-first engineering capstone and need to ground my use case before writing an OpenSpec proposal.

First, interview me. Ask clarifying questions about the user, the problem, the current workflow, the target outcome, constraints, non-goals, success criteria, and risks.

Then propose 2-3 narrower versions of the use case. Challenge weak assumptions and call out anything too broad for one week.

Do not write a proposal or specs yet. We are grounding intent first.
```

If you are using the default code scanner, paste or summarize `examples/code-scanner-starter.md` as your starting intent.

You are ready to move on when you can state, in a few sentences: the user, the problem, the smallest useful slice, and what is explicitly out of scope.

## What OpenSpec Should Produce

For this exercise, use OpenSpec to create three linked artifacts:

- `proposal.md`: why this change exists, what problem it addresses, and what is in or out of scope.
- Specs: the expected capabilities, workflows, constraints, and acceptance-oriented behavior written as `GIVEN / WHEN / THEN` scenarios.
- `design.md`: the implementation approach, architecture decisions, data flow, interfaces, and risks.

These documents do not need to be long. They do need to be specific enough that an engineer or agent could work from them without guessing.

## Step 1: Use OpenSpec Explore Mode

Start in OpenSpec explore mode before generating any artifacts.

Command: `/opsx:explore`

Use explore mode as the research phase of RPI before generating any artifacts.

Use it to work from your grounded intent, inspect the repo, and look for missing requirements, hidden assumptions, and gaps that would weaken `proposal.md`, the specs, or `design.md`. Repo navigation matters here, but the main goal is to learn what is missing or still unclear before planning the change.

This is also where you sharpen the intent from Step 0. Use what you learn in explore mode to tighten the scope, clarify the minimum useful slice, and resolve obvious ambiguity before generating `proposal.md`.

Use explore mode to answer:

- What is the core user outcome?
- What is the smallest useful slice for this workshop?
- What requirements are missing, vague, or not yet testable?
- What assumptions in your intent are not supported by repo reality?
- What gaps or unknowns need to be resolved before writing specs?
- What parts of the repo are likely to change?
- What constraints or unknowns could affect the design?
- What should be deferred?

Before moving on, make sure the explore work leaves you with:

- A tighter understanding of the user outcome.
- A smaller and clearer implementation slice.
- A list of missing requirements or gaps to account for.
- A clearer view of likely repo touchpoints and constraints.

## Step 2: Generate The OpenSpec Proposal

Command: `/opsx:new` if you are starting an expanded workflow change, then `/opsx:continue`

Ask OpenSpec to turn your grounded intent into a proposal for a concrete change in `proposal.md`.

Your proposal should answer:

- What are we changing?
- Why now?
- Who benefits?
- What is the smallest useful scope?
- What is explicitly deferred?
- What decisions still need confirmation?

Tighten any language that sounds generic, inflated, or disconnected from the actual repo and user workflow.

If you prefer the default quick path instead of the expanded workflow, `/opsx:propose <change-name>` can create `proposal.md`, specs, `design.md`, and `tasks.md` together. For this workshop, use the expanded flow so you review each artifact deliberately.

## Step 3: Generate The Spec

Command: `/opsx:continue`

Next, ask OpenSpec to create behavior-oriented specs from `proposal.md` and your grounded intent.

Your spec should capture:

- The user-visible workflow.
- The system behavior required to support that workflow.
- Inputs, outputs, and boundaries.
- Error conditions or failure handling.
- Constraints and assumptions.
- `GIVEN / WHEN / THEN` scenarios that can be verified later.

Good specs reduce hidden decisions. If OpenSpec invents behavior that was not agreed on, remove it.

Once that is generated, review the specs and make any needed changes.

## Step 4: Generate The Design

Command: `/opsx:continue`

Once the specs are stable, ask OpenSpec for `design.md`.

Your design should explain:

- The proposed implementation approach.
- Major components, modules, or files involved.
- Data flow and control flow.
- Key interfaces or command boundaries.
- Important tradeoffs.
- Risks, unknowns, and fallback options.

Prefer the simplest design that satisfies the spec. If the design introduces infrastructure, abstraction, or extensibility that you do not need yet, cut it.

Once that is generated, review `design.md` and make any needed changes.

## Definition Of Done

You are done when:

- You have a grounded use case with a clear user, problem, smallest useful slice, and explicit non-goals.
- You created `proposal.md` for the change.
- You created specs that are specific enough to guide coding.
- You created `design.md` that explains the planned implementation approach.
- `proposal.md`, the specs, and `design.md` align with each other.
- Any remaining unresolved questions are explicit rather than hidden.

## Common Pitfalls

- Skipping the grounding step. Generating a proposal before the intent is specific produces vague specs.
- Letting the proposal stand in for the specs. The proposal explains the scoped change; the specs explain implementation-relevant behavior.
- Skipping explore mode. Repo reality should shape `proposal.md`, the specs, and `design.md`.
- Letting OpenSpec invent scope. Remove anything that was not actually agreed to.
- Writing `design.md` before the specs are clear. Design quality drops fast when behavior is still fuzzy.
- Overengineering the first slice. Prefer the smallest design that can be implemented and verified.
- Leaving contradictions or unresolved gaps in the artifacts. Those issues will surface later as implementation churn.

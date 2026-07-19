# Day 5 Hands-on: Validation Workflow

## What This Folder Contains

`README.md` is the participant entry point. Coaches see `facilitator_notes.md`.

```text
hands-on-validation/
├── README.md
└── facilitator_notes.md
```

## Exercise Goal

Build one validation workflow that produces review-ready evidence for one workflow or change surface from the week.

The scope is one reusable scan-and-check loop, not a CI/CD platform, risk-tier model, adapter layer, or release-gate process.

By the end of the exercise you will have:

- A **validation workflow** — one runnable surface (repo command, pre-commit hook, validation script, or validation skill).
- A `validation-evidence.md` file — the PR-ready review artifact.

## Two Workflow Forms

Pick one based on your change surface.

### Repo-side workflow (preferred when local checks are stable)

A concrete executable the repo supports or you can wire up in-session. Acceptable shapes:

- A pre-commit hook (`.pre-commit-config.yaml`, `husky`).
- A `make validate` target or equivalent.
- An `npm run validate` / `pnpm validate` script.
- A `pytest` invocation with the right markers or path.
- A shell script (`scripts/validate.sh`).
- A repo command participants can document and rerun.

### Skill-assisted workflow (when validation varies by change type)

A skill the assistant can invoke that:

1. Identifies the type of change being validated.
2. Selects the right checks from a defined set.
3. Invokes the repo commands.
4. Captures the evidence.
5. Reports gaps or skipped checks.

Use this when the right validation depends on what changed (e.g., a docs-only change skips a long test matrix; a refactor needs different evidence than a feature).

## Step 1: Pick The Workflow Or Change Surface

Choose one:

- The week's default code scanner.
- A real workflow or feature from your repo.

Smaller is better. One scan-and-check loop you can prove end-to-end.

## Step 2: Trace Back To Sprint Artifacts

For the workflow you picked, identify one item from each artifact you built this week:

- **Capstone spec (Day 2)** — one acceptance criterion or requirement.
- **Repo instructions (`AGENTS.md`, if you created one)** — one rule the validation should respect.
- **Day 3 reusable asset** — one workflow, skill, or context package this validation can lean on.
- **Day 4 harness assessment** — one gap or hardening target.
- **Day 5 legibility** — one item or behavior that must be trusted in the codebase.

These anchors become the source trace in `validation-evidence.md`.

## Step 3: Define Proof Obligations

For each thing the workflow must prove, capture five columns:

```text
Behavior to prove:
Risk if wrong:
Check type:                 # test, lint, scan, manual, skill step
Command / hook / step:
Expected evidence:
```

### Default code scanner — required proof obligations

If you are using the default code scanner, use these five:

1. Valid input returns a readable report.
2. Invalid input returns a clear error.
3. Scanner does not modify source files.
4. Reported signals match what was actually checked.
5. Limitations are visible.

If you are using your own workflow, pick 3-5 obligations grounded in your Step 2 trace.

## Step 4: Create The Validation Workflow

### Repo-side path

Wire or clearly document the command/hook that executes the checks. Examples:

```text
# Pre-commit hook
- repo: local
  hooks:
    - id: scanner-validate
      name: Scanner validate
      entry: python scripts/validate_scanner.py
      language: system
      pass_filenames: false

# make validate
validate:
\tpytest tests/scanner -q
\tpython scripts/check_no_source_writes.py

# npm
"scripts": { "validate": "vitest run scanner && node scripts/check-readme.js" }
```

The bar: a reviewer can run the command, see the output, and decide.

### Skill-assisted path

Write the skill or workflow instruction that selects, invokes, and reports. Minimum surface:

```text
Skill name:
When to use:
Inputs the skill needs:
Steps:
  1. Identify change type from diff or branch context.
  2. Pick the relevant proof obligations.
  3. Invoke each repo command and capture output.
  4. Note any skipped or missing checks.
  5. Write validation-evidence.md using the structure below.
Output: validation-evidence.md
Failure handling: when a check is missing or blocked, name the gap explicitly.
```

Skill steps should resolve to real commands or manual verification — not an assistant attesting that the code is correct.

## Step 5: Produce `validation-evidence.md`

This is the PR-ready review artifact. Required structure:

```markdown
# Validation Evidence — <workflow or change surface>

## Source Trace
- Capstone spec acceptance criterion (Day 2): ...
- AGENTS.md rule (if created): ...
- Day 3 reusable asset: ...
- Day 4 harness gap: ...
- Day 5 legibility item: ...

## Proof Obligations
| Behavior | Risk | Check type | Command / step | Expected evidence |
| --- | --- | --- | --- | --- |
| ... | ... | ... | ... | ... |

## Evidence Captured
- Command: ...
  Output: ...
- Manual step: ...
  Observed: ...

## Missing Or Blocked Checks
- ... (and why)

## Reviewer Recommendation
ready  |  ready with caveats  |  needs more work
Notes: ...
```

## Definition Of Done

- One validation workflow is runnable (repo-side path) or documented as a working skill (skill-assisted path).
- `validation-evidence.md` has all five sections filled.
- Every proof obligation has captured evidence or a named gap.
- Each check ties to a specific behavior from the Step 2 trace, not a generic "run lint/tests."
- Evidence is command output, deterministic check output, manual verification, or a documented gap — not a summary written by the assistant.

## Share-Out

Be ready to explain in 60 seconds:

- Which workflow form you chose and why.
- The highest-value proof obligation you tested.
- The biggest gap you documented and what would close it.

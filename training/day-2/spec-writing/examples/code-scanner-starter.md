# Default Use Case: Code Repository Scanner

Use this starter only if you are not bringing your own repository or use case to the workshop. It is the shared default capstone.

This file is **intent grounding** for OpenSpec - raw material to shape your proposal and specs, not a finished proposal. On Day 2 you turn it into an OpenSpec change (proposal, specs, design) and then implement it across the rest of the week.

## Starting Point

The default project is a code repository scanning system.

It should help engineers and AI assistants understand code quality, risk, and readiness signals before making or reviewing changes.

## Target User

Primary user:

- Engineer or team lead preparing to understand, modify, review, or harden a repository.

Secondary users:

- AI coding assistant that needs grounded repo context.
- Reviewer who wants a quick summary of code health and risk areas.

## Problem To Explore

Modern repos can be difficult for both humans and AI tools to understand quickly. Important quality signals may be scattered across code, docs, tests, CI output, static analysis, and review history.

A useful scanner should make repo understanding more systematic by surfacing signals such as:

- Large or complex files.
- Long or risky functions.
- Test gaps.
- Weak documentation or comments.
- Dependency or configuration risks.
- Areas that may be hard for an AI agent to modify safely.

## Scope For This Week

Keep the first slice small. A useful first version could:

1. Accept a repo path or selected files.
2. Scan a small set of files.
3. Report 2-3 code quality or legibility signals.
4. Output a readable markdown or console summary.
5. Recommend where an engineer should look next.

This is only a suggested minimum. Your proposal can choose a different first slice if you can explain why.

## Possible Requirements

Use these as raw material, not as a finished proposal.

- The scanner should accept a file or directory path as input.
- The scanner should summarize basic code metrics.
- The scanner should identify files that may need review before AI-assisted changes.
- The scanner should produce output that can be pasted into an AI assistant as context.
- The scanner should clearly state limits and confidence.

## Possible Non-Goals

- Full enterprise code-quality platform.
- Replacement for existing CI/CD or security scanning tools.
- Perfect multi-language support in the first version.
- Automated remediation without human review.

## Possible Acceptance Criteria

- A user can point the scanner at a small repo or directory.
- The scanner returns a readable summary.
- The scanner highlights at least two useful quality or risk signals.
- The output includes enough context for an engineer to decide what to inspect next.
- The scanner avoids claiming certainty beyond what it actually checked.

## Using This With OpenSpec (Day 2)

Treat this file as the intent you bring into OpenSpec explore mode. A starting prompt:

```text
I am using the default code repository scanner as my capstone for an AI-first engineering workshop.

Here is my intent: [paste or summarize the relevant parts of this starter].

Start in OpenSpec explore mode. Interview me and inspect the repo to surface missing requirements, hidden assumptions, and the smallest useful slice before we write a proposal. Help me decide:
- who the scanner is for,
- which repo/file scope to target first,
- which 2-3 signals are most valuable,
- what output format would be useful,
- what is explicitly out of scope,
- and what open questions to resolve before the proposal.

Do not generate the proposal yet. We are grounding intent first.
```

When the intent is clear, continue with `/opsx:new` (or the quick `/opsx:propose <change-name>` path) to generate the proposal, specs, and design.

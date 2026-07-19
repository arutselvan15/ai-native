# Example: Concise CLAUDE.md Pattern

This is a workshop-safe reconstructed example inspired by public writeups of Boris Cherny's Claude Code workflow. It is not presented as a verified verbatim copy of an internal Anthropic file.

Sources used:

- MindWired AI, "How the Creator of Claude Code Actually Uses It (CLAUDE.md Included)": https://mindwiredai.com/2026/03/25/claude-code-creator-workflow-claudemd/
- InfoQ, "Inside the Development Workflow of Claude Code's Creator": https://www.infoq.com/news/2026/01/claude-code-creator-workflow/
- Glen Rhodes, "CLAUDE.md pattern for persistent AI agent improvement in software development": https://glenrhodes.com/claude-md-pattern-for-persistent-ai-agent-improvement-in-software-development/

## Why This Example Matters

The useful pattern is not the exact wording. The useful pattern is:

- Keep the root instruction file concise.
- Prefer rules learned from real mistakes over generic policy text.
- Plan before executing non-trivial work.
- Verify before claiming done.
- Capture lessons so the agent improves over time.

## Reconstructed Example

```markdown
# CLAUDE.md

## Workflow

- For any non-trivial task, start in planning mode.
- Restate the goal, list assumptions, and propose a short plan before editing.
- If the task becomes unclear or the approach starts to degrade, stop and re-plan.
- Prefer the smallest change that solves the problem.

## Context Management

- Keep the active context lean.
- Read only the files needed for the current task.
- Do not scan the whole repository unless the task requires it.
- When context gets noisy, summarize the current state and suggest a fresh session or narrower task.

## Subtasks And Parallel Work

- Use focused subtasks for research, review, testing, or isolated implementation work.
- Keep each subtask bounded and give it a clear output.
- Do not let parallel work touch the same files without coordination.

## Verification

- Do not claim completion without evidence.
- Run the most relevant tests, checks, or manual verification available.
- If a check cannot be run, say why and describe the next best validation.
- Include verification results in the handoff.

## Self-Improvement

- When corrected, turn the correction into a concrete rule.
- Add durable lessons to the appropriate repo instruction or lessons file.
- Keep lessons specific enough to change future behavior.

## Code Quality Principles

- Simplicity first: prefer clear, minimal solutions.
- No band-aids: fix root causes when practical.
- Minimal impact: avoid unrelated rewrites.
- Match existing style and conventions.
- Explain non-obvious tradeoffs.

## Handoff Format

At the end of meaningful work, report:

- What changed.
- Files touched.
- Checks run.
- Risks or open questions.
- Recommended next step.
```

## How To Use This In The Exercise

Do not copy this file directly. Use it to improve your own `AGENTS.md`:

- Which rules would actually help your repo?
- Which commands or checks should be specific to your repo?
- What mistakes do you want the agent to avoid?
- What handoff format will make review easier for your team?

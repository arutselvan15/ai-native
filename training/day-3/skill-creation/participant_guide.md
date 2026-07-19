# Participant Guide: Create a Jira MCP Planning Skill

Create a reusable skill that helps an AI coding agent fetch a Jira story through MCP and turn it into an implementation plan.

## Reference
https://agentskills.io/home#what-are-agent-skills

## Goal

Build a skill that can:

- Recognize when a user is asking for implementation planning from a Jira issue.
- Fetch or request the relevant story details.
- Produce a practical engineering plan.
- Handle missing issue keys, missing Jira access, or incomplete requirements.

## Steps

1. Define the skill contract.

   Decide the skill name, when it should trigger, what input it needs, what output it should produce, and what external dependency it relies on.

2. Scaffold the skill.

   Create a small skill folder with a `SKILL.md` file. Add a `references/` folder if you want to keep templates, examples, or supporting material separate from the main workflow.

3. Write the trigger metadata.

   Add frontmatter to `SKILL.md` with a clear name and description. The description should help the agent decide when to load the skill.

4. Write the core workflow.

   Describe the steps the agent should follow to get the Jira story, reason about it, identify gaps, and produce an implementation plan.

5. Add output guidance.

   Decide what sections a useful engineering plan should contain. Keep the guidance specific enough to improve consistency but flexible enough for different stories.

6. Define fallback behavior.

   Specify what the agent should do if no Jira issue key is provided, Jira MCP is unavailable, or the story lacks enough detail.

7. Test with a realistic story.

   Run the skill with a real or sample Jira issue. Check whether the agent used the skill, preserved the story facts, avoided unsupported assumptions, and produced a plan that an engineer could act on.

8. Tighten the skill.

   Based on the test result, revise the trigger, workflow, output guidance, or supporting references. Aim for the smallest change that improves the agent's behavior.

## Check Your Work

Your finished skill should include:

- A clear trigger description.
- A concise `SKILL.md` workflow.
- A reusable planning structure.
- Explicit handling for missing inputs or missing MCP access.
- At least one tested example.

Be ready to explain why your skill instructions are written the way they are and what changed after testing.

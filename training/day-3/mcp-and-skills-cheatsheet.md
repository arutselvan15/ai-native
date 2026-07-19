# 🛠️ Cheat Sheet: Augmenting the Agent with MCPs & Skills

> **tl;dr** — The agent is smart but needy. Give it tools (MCPs) and superpowers (skills), and it'll do the work you've been putting off for weeks.

---

## What Are We Doing Here?

| Thing | What It Is | Why You Care |
|-------|-----------|--------------|
| **MCP** | Model Context Protocol — a server the agent can call as a tool | Gives the agent access to external systems (browsers, Jira, databases, etc.) |
| **Skill** | A pre-packaged prompt + toolset installed via `npx skills add` | Specialized capability dropped right into the agent (e.g., make a PowerPoint) |

Think of MCPs as **electrical outlets** and Skills as **appliances you plug in**.

---

## Step 1 — Configure Your MCPs

Open your Copilot MCP settings and add the following two servers.

> These snippets are JSON fragments to paste inside your MCP servers section.

### 🌐 Chrome DevTools MCP
Lets the agent browse the web, interact with pages, read DOM content, and take screenshots.

```jsonc
"chrome-devtools": {
  "command": "npx",
  "args": ["-y", "chrome-devtools-mcp@latest"]
}
```

> **Requires:** Node.js + `npx` on your PATH. The MCP will auto-install on first run.

### 🟦 Atlassian MCP
Gives the agent read/write access to your Jira and Confluence instance.

```jsonc
"atlassian": {
  "url": "https://mcp.atlassian.com/v1/mcp",
  "type": "http"
}
```

> **Requires:** You must be authenticated with your Atlassian account. The MCP uses your existing session/token.

---

## Step 2 — Install the Cisco PowerPoint Skill

Skills live in the [Cisco GenAI Awesome Skills Registry](https://cisco-genai.github.io/awesome-cisco/).

Run this command to install the `cisco-ops-pptx` skill:

```bash
npx skills add https://github.com/cisco-genai/awesome-cisco --skill cisco-ops-pptx
```

> ⚠️ **Git + EMU orgs:** `npx` fetches this skill via `git clone`. Make sure your git credentials are configured to read from Cisco's GitHub Enterprise Managed User (EMU) org (`cisco-genai`). If you get an auth error, check that your SSH key or PAT has access to that org.

Once installed, the skill appears as an available tool in the agent's toolbox.

---

## Step 3 — The Prompt

Copy-paste this into the agent. Then sit back. Maybe get a coffee. ☕

```
You've got a big job here!
1. Navigate with chrome-devtools to https://steve-yegge.medium.com/
2. Read the posts prefixed with "Welcome to"
3. Create a PowerPoint presentation summarizing Steve Yegge's posts, with 3-4 sentences on each post. Bonus points if you can include some of the images in the PowerPoint. The PowerPoint should be at most 10 slides long. It should include a title slide, an introduction to Steve Yegge, a slide for each of the "Welcome to" posts, and possibly a closing slide describing how Steve views agents and agent swarms.
4. Also create similar content in Confluence at: https://cisco-jira.atlassian.net/wiki/spaces/CEP/pages/444891606/MCP+Ideas

Ask me any questions you may have now, and be concise, firm, dry, and humorous.

That's it, let's gooooo 🚀.
```

### What to Expect

The agent will:
1. **Browse** Steve Yegge's Medium page using Chrome DevTools
2. **Read** the "Welcome to" posts (and probably judge your taste in tech blogs)
3. **Build** a PowerPoint via the `cisco-ops-pptx` skill
4. **Publish** the same content to your Confluence page via the Atlassian MCP

> 💡 **Pro tip:** Run this in **Autopilot mode**. You don't need Opus 4.7 for this — **Sonnet 4.6** or even **auto mode** handles it fine. Save the big iron for problems that actually need it.

---

## Cheat Sheet Summary

```
1. Add MCPs to settings:
   - chrome-devtools  →  npx -y chrome-devtools-mcp@latest
   - atlassian        →  https://mcp.atlassian.com/v1/mcp (HTTP)

2. Install skill:
   npx skills add https://github.com/cisco-genai/awesome-cisco --skill cisco-ops-pptx
   (git must be authed for cisco-genai EMU org)

3. Paste prompt → set Autopilot → let it rip 🚀
```

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| `chrome-devtools` MCP fails to start | Make sure `npx` is on your PATH and Node.js ≥ 18 |
| Atlassian MCP returns 401 | Re-authenticate with your Atlassian account |
| `npx skills add` fails with git auth error | Configure SSH or HTTPS credentials for the `cisco-genai` GitHub org |
| Agent asks too many questions | Smile. Add more context to the prompt. Or just answer and move on. |
| Agent does something unexpected | Welcome to AI. This is the way. |

---

## Demo

▶️ [Watch the demo on Vidcast](https://app.vidcast.io/share/a543ff5c-923a-453c-85f0-6224bfb15f43)

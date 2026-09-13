<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset=".github/assets/banner.svg">
    <img src=".github/assets/banner-light.svg" alt="With Love, Math. — A framework meant to be passed on." width="830">
  </picture>
</p>

# With Love, Math _(With-Love-Math)_

[![License: MIT](https://img.shields.io/badge/License-MIT-c9a227?style=flat-square&labelColor=0d0d10)](LICENSE)
[![Version](https://img.shields.io/badge/version-1.0.0-c9a227?style=flat-square&labelColor=0d0d10)](plugin.json)
[![Agent Plugins](https://img.shields.io/badge/Agent_Plugins-1.0.0-c9a227?style=flat-square&labelColor=0d0d10)](https://agent-plugins.org/specification)
[![Standard Readme](https://img.shields.io/badge/standard--readme-follower-c9a227?style=flat-square&labelColor=0d0d10)](https://github.com/richardlitt/standard-readme)
[![math-approved](https://img.shields.io/badge/math--approved-WONDER_preserved-f0d878?style=flat-square&labelColor=0d0d10)](#the-invariant-wonder)

An [Agent Plugins 1.0.0](https://agent-plugins.org/specification) plugin that turns deliberation into a verdict. It is a folder of written instructions an agent reads when it starts. Nothing to compile, nothing to run. Hand it a decision, or a project already underway, and it runs the whole thing through one fixed set of questions: four principles, one loop, one invariant — the one thing that must not change. What comes back is a verdict, **Aligned** or **Needs Revision**, and when the answer is Needs Revision it names exactly which principle failed and the single first move to fix it.

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset=".github/assets/pillars.svg">
    <img src=".github/assets/pillars-light.svg" alt="One body of work, three pillars: Gregorian Mode interrogates design choices; Editorial Loop interrogates text; With Love, Math interrogates decisions — the broadest and most personal." width="100%">
  </picture>
</p>

The plugin *is* the framework. It applies its own principles to itself: **R1 · Recursive Grounding** by always returning to Why, **R2 · Emotion as Invariant** by checking every decision against the invariant, **R3 · Distinction Within Unity** by keeping each principle distinct yet unified, and **R4 · Scale the Invariance** by working at any scale — one decision or a whole project.

> [!IMPORTANT]
> **It is not a cover generator, not a website builder, and not a chat partner for endless deliberation.** Those three all produce something — a cover, a site, more conversation. This one produces a judgement. It is a discipline for running a decision and getting a verdict: a binary **Aligned / Needs Revision** that names any failing principle.

**How to read this page.** The README is built as seven numbered plates on one continuous ground. A plate is one page in a bound book — self-contained, and printed on a ground that runs behind all seven. Every plate carries a ribbon icon, every chapter is numbered, and the invariant — **WONDER** — recurs as a visual anchor. Land anywhere: the plate number and icon tell you where you are, and [the verdict table](#the-verdict-table) is never more than one click away in the [contents](#contents).

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset=".github/assets/divider.svg">
    <img src=".github/assets/divider-light.svg" alt="" width="700">
  </picture>
</p>

<a name="plate-00" id="plate-00"></a>

## Plate 00 — Watch the Showcase

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset=".github/assets/plate-00.svg">
    <img src=".github/assets/plate-00-light.svg" alt="Plate 00 — Watch the Showcase. The four principles, the loop, and the invariant in motion." width="100%">
  </picture>
</p>

https://github.com/user-attachments/assets/85ad0725-a5d8-4eb8-9937-c1517d581007

*The 87-second showcase — the four principles, the loop, and the invariant in motion. Direct download: <a href="https://github.com/AlastairZeved/With-Love-Math/releases/download/showcase/with-love-math-showcase.mp4">MP4 (20.5 MB)</a>, from the downloads shelf GitHub keeps beside every project.*

## Contents

<a name="contents" id="contents"></a>

| | | |
|---|---|---|
| [**Plate 00 — Watch the showcase**](#plate-00) · *1½ min* | [**Plate 01 — Background**](#plate-01) | [**Plate 02 — Install**](#plate-02) |
| [**Plate 03 — Usage**](#plate-03) — commands · example · output | [**Plate 04 — The Framework**](#plate-04) — principles · loop · map · layers · WONDER | [**Plate 05 — Architecture**](#plate-05) — packaging · skills · subagents · hooks |
| [**Plate 06 — Colophon**](#plate-06) — maintainers · contributing · license | | |

<a name="the-verdict-table" id="the-verdict-table"></a>

### The verdict table

The framework answers with one of two words. Every run — whether you asked it to decide, to audit, or to map — resolves to the same pair:

| Verdict | Mark | Meaning | Named by |
|---|---|---|---|
| **Aligned** <img src=".github/assets/icons/verdict-aligned.svg" width="26" alt="" align="center"> | | The decision holds: the loop was run, the principles pass, the invariant is preserved. | — |
| **Needs Revision** <img src=".github/assets/icons/verdict-revision.svg" width="26" alt="" align="center"> | | The decision does not yet hold — and the framework names the failing principle(s) and the single first move. | R1 / R2 / R3 / R4 by name |

Each principle is graded on its own, as Pass, Weak, or Fail, but the verdict on top stays binary. It is never softened: a Fail is never rounded up to a Weak to reach Aligned. The [output format](#output-format) shows the exact shape.

<a name="plate-01" id="plate-01"></a>

## Plate 01 — Background

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset=".github/assets/plate-01.svg">
    <img src=".github/assets/plate-01-light.svg" alt="Plate 01 — Background. Most work starts with a reason and a feeling, and then loses both." width="100%">
  </picture>
</p>

Most work starts with a reason and a feeling, and then loses both. Iterations accumulate, constraints arrive, other people's opinions land on top, and by the end the decision no longer resembles the one you set out to make.

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset=".github/assets/art-drift.svg">
    <img src=".github/assets/art-drift-light.svg" alt="A decision drifts from its origin; R1 traces it back and R2 holds the feeling constant." width="100%">
  </picture>
</p>

With Love, Math is a framework for not losing them: **R1 · Recursive Grounding** traces every choice back to where it started; **R2 · Emotion as Invariant** names the feeling before you begin and holds it steady through every change.

**Gregorian** is the author's word for *a standard strangers adopt and never stop running* — coined in Gregorian Mode, the sibling project about design choices, and carried over into this one. It survives in `gregorian-decision`, the name of the subagent that runs the whole framework in one pass. A subagent, for anyone meeting the word for the first time, is a smaller second agent that the main one hands one narrow job to. Three such subagents ship with this plugin, and they are introduced in Plate 05.

Here the standard is a four-principle decisioning framework whose single invariant is WONDER. The framework is meant to be passed on, not only used privately — the `/teach` command and the `tutor` skill exist precisely so others can adopt it and run it.

| The claim | What it means here |
|---|---|
| **Four depths, one object** | Every element of the framework reads at four depths simultaneously — Design Philosophy (physical), Self-Help / Self-Love (emotional), Math in Nature (structural), Esotericism (spiritual). A good decision holds at all four. This is the framework's most unusual claim: a layout decision, a life decision, a structural pattern, and a spiritual question are the same object viewed from different altitudes. |

Its brand personality is **Friendly · Quirky · Bold · Sophisticated** — warm enough to invite, strange enough to be memorable, confident enough to commit, refined enough to trust.

<a name="plate-02" id="plate-02"></a>

## Plate 02 — Install

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset=".github/assets/plate-02.svg">
    <img src=".github/assets/plate-02-light.svg" alt="Plate 02 — Install. No build step, no package manager, no runtime dependencies." width="100%">
  </picture>
</p>

No build step, no package manager, no runtime dependencies — nothing to compile and nothing to keep updated. The plugin is plain markdown: a folder of text files that a compatible agent reads when it loads. That is the whole mechanism, and it is why most install routes below come down to the same move: put this folder where your agent already looks — or name the repository and let the command fetch it. Clone once; every route starts from that clone or reads the repository directly.

```bash
git clone https://github.com/AlastairZeved/With-Love-Math.git
```

The root [`plugin.json`](plugin.json) is the [Agent Plugins 1.0.0](https://agent-plugins.org/specification) manifest — one small file at the top of the folder that tells any agent what is inside before it reads anything else. Because that file follows a published standard, every client that speaks it reads this plugin unchanged — that is what *portable* means here. Where clients differ, their extra pieces sit in a namespace of their own, a folder named for one client only, and every other client ignores it. Nothing portable depends on anything namespaced, which is what keeps the package portable.

### Dependencies

> [!NOTE]
> None. Markdown only. (Git, to clone the repository.)

### What loads where

| Agent | Install route | Skills | Commands | Subagents | Hooks |
|---|---|---|---|---|---|
| **Claude Code** | [`claude --plugin-dir`](#claude-code) | <img src=".github/assets/icons/verdict-aligned.svg" width="18" alt="supported"> | <img src=".github/assets/icons/verdict-aligned.svg" width="18" alt="supported"> 5 | <img src=".github/assets/icons/verdict-aligned.svg" width="18" alt="supported"> 3 | <img src=".github/assets/icons/verdict-aligned.svg" width="18" alt="supported"> 2 |
| **Hermes Agent** | [`hermes plugins install`](#hermes-agent) | <img src=".github/assets/icons/verdict-aligned.svg" width="18" alt="supported"> 4 | via skills | — | — |
| **Codex** (CLI / ChatGPT app) | [`/plugins` browser + marketplace](#codex) | <img src=".github/assets/icons/verdict-aligned.svg" width="18" alt="supported"> | — | — | — |
| **Cursor** | [Customize page or `~/.cursor/plugins/local`](#cursor) | <img src=".github/assets/icons/verdict-aligned.svg" width="18" alt="supported"> | <img src=".github/assets/icons/verdict-aligned.svg" width="18" alt="supported">\* | <img src=".github/assets/icons/verdict-aligned.svg" width="18" alt="supported">\* | — |
| **GitHub Copilot** | [`copilot plugin install` / VS Code](#github-copilot) | <img src=".github/assets/icons/verdict-aligned.svg" width="18" alt="supported"> | <img src=".github/assets/icons/verdict-aligned.svg" width="18" alt="supported"> 5 | <img src=".github/assets/icons/verdict-aligned.svg" width="18" alt="supported"> 3 | — |
| **Pi Agent** | [clone into `~/.pi/agent/skills/`](#pi-agent) | <img src=".github/assets/icons/verdict-aligned.svg" width="18" alt="supported"> 4 | — | — | — |
| **Any SKILL.md agent** | [copy a `skills/` folder](#any-skillmd-agent) | <img src=".github/assets/icons/verdict-aligned.svg" width="18" alt="supported"> | — | — | — |

\* Cursor reads the Claude-namespace `commands/` and `agents/` through its [`.cursor-plugin/plugin.json`](.cursor-plugin/plugin.json) manifest where a Claude-style command or agent is understood.

In agents that register no slash-command menu, the same procedures are reachable in words — "Run the decision engine on `<decision>`" reaches the identical skill that `/decide` does. The commands are doors, not the house.

### Per-agent instructions

Seven routes into the same repository — the install section is a hallway of doors, each card its own room:

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset=".github/assets/art-doors.svg">
    <img src=".github/assets/art-doors-light.svg" alt="Seven install routes, one repository: Claude Code, Hermes Agent, Codex, Cursor, GitHub Copilot, Pi Agent, and any SKILL.md agent." width="100%">
  </picture>
</p>

<a name="claude-code" id="claude-code"></a>
<details>
<summary><strong>Claude Code</strong> · <code>claude --plugin-dir ./With-Love-Math</code></summary>

Requires [Claude Code](https://code.claude.com/docs).

```bash
git clone https://github.com/AlastairZeved/With-Love-Math.git
claude --plugin-dir ./With-Love-Math
```

The `--plugin-dir` flag loads the plugin straight from the folder you cloned above and skips the marketplace route entirely. A marketplace, in Claude Code, is only a catalog file listing what is on offer; this repository ships no such file, so `/plugin marketplace add AlastairZeved/With-Love-Math` has nothing to read and will not work. `--plugin-dir` is the documented direct-load path.

The five commands, three subagents, and both hooks live under the [`com.anthropic.claude/`](com.anthropic.claude) client namespace — the folder named for Claude Code — declared in [`.claude-plugin/plugin.json`](.claude-plugin/plugin.json). (Hooks are small scripts the client runs on its own at set moments — the start of a session, the moment a file is saved.) `claude plugin validate .` passes on this repository as shipped.

To install permanently, copy the plugin into your personal skills directory — the folder Claude Code scans on startup for anything it can load:

```bash
cp -r ./With-Love-Math ~/.claude/skills/with-love-math
```

Claude Code auto-discovers plugins in `~/.claude/skills/` that carry a `.claude-plugin/plugin.json` manifest, so it loads on the next session as `with-love-math@skills-dir`. Manage it afterward with `claude plugin disable with-love-math@skills-dir`, `claude plugin enable with-love-math@skills-dir`, or `rm -rf ~/.claude/skills/with-love-math` to uninstall.

</details>

<a name="hermes-agent" id="hermes-agent"></a>
<details>
<summary><strong>Hermes Agent</strong> · <code>hermes plugins install … --no-enable</code></summary>

```bash
hermes plugins install AlastairZeved/With-Love-Math --no-enable
hermes plugins enable with-love-math
hermes gateway restart
```

An Agent Plugins package arrives switched off — enable it explicitly, then restart the gateway (the background service that runs your agent) so the skills are picked up. The four portable skills are discovered from the root manifest; `hermes plugins validate <repo-dir>` and `hermes plugins show with-love-math` check the install, and `hermes plugins remove with-love-math` takes it out again.

</details>

<a name="codex" id="codex"></a>
<details>
<summary><strong>Codex</strong> · CLI plugin browser or ChatGPT desktop app</summary>

Requires [Codex](https://developers.openai.com/codex). Codex reads the portable root [`plugin.json`](plugin.json) — the file that both declares the standard it follows and carries a small block of OpenAI-specific extras under `extensions["com.openai"]` (display name "With Love, Math", category "decision-making").

OpenAI documents the `.codex-plugin/plugin.json` manifest as a backwards-compatible alternative for packages already built on that older layout.

In **Codex CLI**, open the plugin browser and install from a configured marketplace:

```text
/plugins
```

To make the plugin installable from this repository, add the repo as a marketplace source:

```bash
codex plugin marketplace add AlastairZeved/With-Love-Math
```

For **local testing**, OpenAI's packaging documentation routes local plugins through a marketplace file — a small catalog of what is on offer, the same idea as Claude Code's marketplace above — either a repo-scoped `.agents/plugins/marketplace.json` (with the plugin folder under `$REPO_ROOT/plugins/`) or a personal one at `~/.agents/plugins/marketplace.json`.

Install from the marketplace in the CLI browser or the ChatGPT desktop app and start a new session. Bundled skills become available in the new session. The `.codex-plugin/plugin.json` fallback ships for environments still expecting the old layout.

The three subagents stay in the Claude namespace — Codex describes its own subagents in TOML files, a different text format, and this repository ships none.

</details>

<a name="cursor" id="cursor"></a>
<details>
<summary><strong>Cursor</strong> · Customize page or <code>~/.cursor/plugins/local</code></summary>

Requires [Cursor](https://cursor.com/docs/plugins). Cursor supports the Agent Plugins open standard: a package with a root `plugin.json` loads in Cursor without changes.

Cursor-specific components keep working through the [`.cursor-plugin/plugin.json`](.cursor-plugin/plugin.json) manifest, which points at the portable `skills/` directory and at the Claude-namespace `commands/` and `agents/`.

Install from a marketplace: open **Customize** in the sidebar, find the plugin, and select **Install** — choosing whether it applies to this one project or to everything you open.

Develop locally without a marketplace:

```bash
ln -s /path/to/With-Love-Math ~/.cursor/plugins/local/With-Love-Math
```

then restart Cursor (or run **Developer: Reload Window**) and confirm the skills and components under **Customize**. Cursor discovers plugins in that folder when local plugin imports are allowed (on Teams and Enterprise, an admin setting controls this).

</details>

<a name="github-copilot" id="github-copilot"></a>
<details>
<summary><strong>GitHub Copilot</strong> · <code>copilot plugin install</code> or VS Code "Install Plugin From Source"</summary>

Requires Copilot in VS Code, the Copilot CLI, or the app. Copilot supports Agent Plugins 1.0.0: it reads the portable `skills/` directory and the root `plugin.json`.

Copilot-specific components come from the [`com.github.copilot/`](com.github.copilot) client namespace — the three specialists as `.agent.md` custom agents (the file format VS Code uses for one) and the five command procedures as command wrappers — so Copilot users get the full plugin, not only the portable skills.

From the Copilot CLI, installing straight from the repository is a documented path:

```bash
copilot plugin install AlastairZeved/With-Love-Math
```

The `install` command accepts the `OWNER/REPO` shorthand you already see in GitHub URLs, a Git URL, or a local directory. From **VS Code**, run **Chat: Install Plugin From Source** from the Command Palette (or **Install Plugin from Source** on the Plugins page of the Agent Customizations editor) and enter the repository URL:

```text
https://github.com/AlastairZeved/With-Love-Math
```

Support for agent plugins can be toggled with the `chat.plugins.enabled` VS Code setting. Skills appear in the **Configure Skills** menu; the specialist agents appear alongside custom agents.

</details>

<a name="pi-agent" id="pi-agent"></a>
<details>
<summary><strong>Pi Agent</strong> · clone into <code>~/.pi/agent/skills/</code></summary>

Pi finds skills by scanning its config directory for any folder that holds a `SKILL.md` — the single markdown file, sitting at the top of a folder, that makes that folder a skill. Clone the repository into Pi's global skills directory and the four portable skills are found automatically; no manifest needed.

```bash
git clone https://github.com/AlastairZeved/With-Love-Math.git ~/.pi/agent/skills/with-love-math
```

(Project-scoped alternative: clone into `.pi/skills/` in a trusted project.)

</details>

<a name="any-skillmd-agent" id="any-skillmd-agent"></a>
<details>
<summary><strong>Any other SKILL.md-compatible agent</strong> · copy a skill folder</summary>

Copy any folder under `skills/` into the agent's skills directory. Each skill is a self-contained `SKILL.md` with a small header at the top — a name and a description, between two `---` lines — and nothing else is required.

```bash
git clone https://github.com/AlastairZeved/With-Love-Math.git
mkdir -p ~/.your-agent/skills
cp -r With-Love-Math/skills/* ~/.your-agent/skills/
```

</details>

<a name="plate-03" id="plate-03"></a>

## Plate 03 — Usage

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset=".github/assets/plate-03.svg">
    <img src=".github/assets/plate-03-light.svg" alt="Plate 03 — Usage. Five commands, stable and minimal; each dispatches to a skill or subagent." width="100%">
  </picture>
</p>

Once the plugin is loaded, the session-start hook greets you and lists the commands — in the agents that have one. Five commands, stable and minimal; each one hands its work to a skill or a subagent underneath. In agents that do not register slash-command menus, invoke the same procedures in words — "Run the decision engine on `<decision>`" reaches the identical skill.

### Commands

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset=".github/assets/art-commands.svg">
    <img src=".github/assets/art-commands-light.svg" alt="Five commands: /decide, /diagnose, /map, /teach, /lexicon." width="100%">
  </picture>
</p>

| Command       | Does                                                              |
| ------------- | ----------------------------------------------------------------- |
| `/decide`     | Run a decision through the full framework → `Aligned` / `Needs Revision` verdict |
| `/diagnose`   | Audit an existing project against R1–R4 → prescription with first step |
| `/map`        | Map a project onto the ten-position map → filled table plus gaps  |
| `/teach`      | Teach the framework, adapted to the learner                       |
| `/lexicon`    | Define the framework's terms                                      |

### Example

```text
/decide Ship the dashboard with the dark header instead of the light one
/diagnose the landing page from last quarter — it feels cold
/map the mobile app redesign
/teach a designer who has never used a decisioning framework
/lexicon emotional invariant
```

### Output format

The decision engine behind `/decide` returns a structured verdict, in this fixed format:

```text
DECISION: <restated in one line>
GOAL: <under five words>

LOOP
  WHY   — <...>
  WHO   — <...>
  FEEL  — <...>
  EVOKE — <...>

PRINCIPLES
  R1 Recursive Grounding  [Pass/Weak/Fail] — <evidence>
  R2 Emotion as Invariant [Pass/Weak/Fail] — <evidence>
  R3 Distinction in Unity [Pass/Weak/Fail] — <evidence>
  R4 Scale the Invariance [Pass/Weak/Fail] — <evidence>

MATH: <the pattern found>

VERDICT: Aligned  |  Needs Revision
  <if Needs Revision: name the failing principle(s) and the single first move>
```

The verdict is binary; failures are named by principle, and the framework never softens a Fail into a Weak to reach Aligned. If you want a verdict instead of a discussion, this is the point.

<a name="plate-04" id="plate-04"></a>

## Plate 04 — The Framework

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset=".github/assets/plate-04.svg">
    <img src=".github/assets/plate-04-light.svg" alt="Plate 04 — The Framework. Four principles, one loop, one map, four layers, one invariant." width="100%">
  </picture>
</p>

The framework is the content; the plugin is how that content is packaged and shipped. It has five parts — four principles, one loop, one map, four layers, one invariant.

### The four principles (R1–R4)

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset=".github/assets/art-pillars.svg">
    <img src=".github/assets/art-pillars-light.svg" alt="The four principles: R1 Recursive Grounding — Why am I doing this?; R2 Emotion as Invariant — What feeling must I preserve?; R3 Distinction Within Unity — How do these parts make one whole?; R4 Scale the Invariance — Does this work at every size?" width="100%">
  </picture>
</p>

<details open>
<summary><strong>As a table</strong> (screen-reader / copy-friendly)</summary>

| Principle                     | Question                             | What it enforces                                    |
| ----------------------------- | ------------------------------------ | --------------------------------------------------- |
| **R1 · Recursive Grounding**  | "Why am I doing this?"               | Every decision traces back to its origin.           |
| **R2 · Emotion as Invariant** | "What feeling must I preserve?"      | A chosen feeling survives every iteration unchanged.|
| **R3 · Distinction Within Unity** | "How do these parts make one whole?" | Parts stay individually legible while cohering — "distinct colors, one shape." |
| **R4 · Scale the Invariance** | "Does this work at every size?"      | Integrity holds from 2-inch icon to 10-foot mural.  |

</details>

### The decisioning loop

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset=".github/assets/art-loop.svg">
    <img src=".github/assets/art-loop-light.svg" alt="The decisioning loop: WHY, WHO, FEEL, EVOKE, returning forever." width="100%">
  </picture>
</p>

- **WHY** — the reason this exists
- **WHO** — who it is for, who receives it
- **FEEL** — the feeling that must be preserved
- **EVOKE** — how you produce that feeling in the person who receives it

The loop is infinite; it always returns to the beginning. This is R1 in motion — no decision is ever fully grounded, only grounded again each time you run the loop. Grounding, throughout this framework, means tracing a thing back to the reason it exists.

### The ten-position map

A second lens on the same structure. The loop is the sequence you run; the map is the shape it makes.

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset=".github/assets/art-map.svg">
    <img src=".github/assets/art-map-light.svg" alt="The ten-position map as two axes: the sequence you run, and the depth it reads at." width="100%">
  </picture>
</p>

<details>
<summary><strong>As a table</strong></summary>

| Position | Element                |
| -------- | ---------------------- |
| 1        | State the Goal (< 5 words) |
| 2        | WHY                    |
| 3        | WHO                    |
| 4        | FEEL                   |
| 5        | EVOKE                  |
| 6        | R1 · Recursive Grounding |
| 7        | R2 · Emotion as Invariant |
| 8        | R3 · Distinction Within Unity |
| 9        | R4 · Scale the Invariance |
| 10       | Find the Math          |

</details>

Position 10 — **Find the Math** — is where the map ends: name the pattern, ratio, symmetry, or structure underneath the decision. If none exists, that absence is itself a finding. Most decision frameworks stop before this point. The claim here is that good decisions have an underlying form, and that naming it makes them easier to see and easier to hand on.

### The four layers

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset=".github/assets/art-layers.svg">
    <img src=".github/assets/art-layers-light.svg" alt="The four layers: Design Philosophy, Self-Help and Self-Love, Math in Nature, Esotericism." width="100%">
  </picture>
</p>

Any element can be read at any layer, and a good decision holds at all four — **Design Philosophy** (the physical object), **Self-Help / Self-Love** (the emotional life of it), **Math in Nature** (the structural pattern underneath), and **Esotericism** (the spiritual reading: what it means beyond what it does). The four are read together in [Background](#plate-01).

### The invariant: WONDER

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset=".github/assets/art-wonder.svg">
    <img src=".github/assets/art-wonder-light.svg" alt="The invariant: WONDER. If a decision, design, or project does not evoke wonder, it has not yet passed." width="100%">
  </picture>
</p>

> [!TIP]
> **WONDER.** If a decision, design, or project does not evoke wonder, it has not passed. This is what **R2 · Emotion as Invariant** preserves and **R4 · Scale the Invariance** scales — the single test the whole framework resolves to.

The invariant is the page's visual anchor: it appears as the closing mark of the [banner](#), returns as the anchor of Plate 06 below, and is the mark every verdict resolves against (see [the verdict table](#the-verdict-table)).

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset=".github/assets/divider.svg">
    <img src=".github/assets/divider-light.svg" alt="" width="700">
  </picture>
</p>

<a name="plate-05" id="plate-05"></a>

## Plate 05 — Architecture

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset=".github/assets/plate-05.svg">
    <img src=".github/assets/plate-05-light.svg" alt="Plate 05 — Architecture. Four layers of packaging, each doing a distinct job." width="100%">
  </picture>
</p>

The plugin has four layers, and each does a distinct job — plus a packaging split that keeps it portable. This is also a plugin-authoring reference: it is a complete worked example of an Agent Plugins 1.0.0 package with client namespaces cooperating in one repository.

### Portability — the packaging split

Two kinds of content live side by side, per the Agent Plugins 1.0.0 standard (§8, client extensions):

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset=".github/assets/art-architecture.svg">
    <img src=".github/assets/art-architecture-light.svg" alt="The packaging split: portable content and client-namespaced content, side by side." width="100%">
  </picture>
</p>

- **Portable** — [`skills/`](skills) and the root [`plugin.json`](plugin.json). Every Agent Plugins 1.0.0 client reads these; they reference nothing client-specific.
- **Client-namespaced** — [`com.anthropic.claude/`](com.anthropic.claude) (commands, subagents, hooks, hook scripts) and [`com.github.copilot/`](com.github.copilot) (the same components in Copilot's documented formats, with a [porting note](com.github.copilot/README.md)). Clients that don't implement a namespace ignore it, which is what keeps the package portable.

  Claude Code's manifest at [`.claude-plugin/plugin.json`](.claude-plugin/plugin.json) declares the namespace paths for its commands, agents, and hooks.

Per-agent adapters live in [`.codex-plugin/plugin.json`](.codex-plugin/plugin.json) (Codex compatibility fallback) and [`.cursor-plugin/plugin.json`](.cursor-plugin/plugin.json) (Cursor manifest pointing at the portable skills and the Claude-namespace commands and agents).

### Commands — the public entry points

Five flat command files in [`com.anthropic.claude/commands/`](com.anthropic.claude/commands) — `decide.md`, `diagnose.md`, `map.md`, `teach.md`, `lexicon.md`. Commands are thin: an argument hint, a one-line description, and dispatch instructions. Depth lives below them. Copilot users get the same five doors as command wrappers under [`com.github.copilot/commands/`](com.github.copilot/commands).

### Skills — the operative content

Four skills in [`skills/`](skills), each a `SKILL.md` carrying the compact canon it needs:

| Skill              | Carries                                                              |
| ------------------ | -------------------------------------------------------------------- |
| `decision-engine`  | Principles, loop, and the structured output format (backs `/decide`)  |
| `diagnostic`       | The audit process: where an existing work loses the invariant (backs `/diagnose`) |
| `tutor`            | The canon plus a teaching structure and level-adaptation rules (backs `/teach`) |
| `lexicon`          | The canon plus the full glossary (backs `/lexicon`)                   |

Every skill carries the invariant.

### Subagents — the specialists

Three subagents in [`com.anthropic.claude/agents/`](com.anthropic.claude/agents), all `model: sonnet`, all with `disallowedTools: Write, Edit` — they evaluate, they do not modify.

| Agent                  | Job                                            | Effort | Turns |
| ---------------------- | ---------------------------------------------- | ------ | ----- |
| `gregorian-decision`   | The full framework run → structured verdict    | medium | 15    |
| `invariant-checker`    | The fast narrow pass → `Preserved` / `Lost`    | low    | 8     |
| `ten-position-mapper`  | Structural cartography → map plus gaps         | medium | 12    |

The division of labor is clean: `gregorian-decision` is the full operation, `invariant-checker` is the scalpel, `ten-position-mapper` does the cartography.

Copilot users get the same three specialists as `.agent.md` custom agents under [`com.github.copilot/agents/`](com.github.copilot/agents); the no-write guardrail travels in the prompt body there, since `.agent.md` frontmatter does not carry `disallowedTools`.

### Hooks — the ambient reminders

Two hooks in [`com.anthropic.claude/hooks/hooks.json`](com.anthropic.claude/hooks/hooks.json), both non-blocking:

- **SessionStart** runs [`com.anthropic.claude/scripts/welcome.sh`](com.anthropic.claude/scripts/welcome.sh), which greets you and lists the commands.
- **PreToolUse** on `Write|Edit` runs [`com.anthropic.claude/scripts/design-reminder.sh`](com.anthropic.claude/scripts/design-reminder.sh), which fires only when the file being touched matches `*.design.md` and reminds you to check the invariant (R2) and scale (R4). It exits 0 — it reminds, it does not gate.

The hook commands reference `${CLAUDE_PLUGIN_ROOT}` — the plugin root — so the scripts resolve through the namespace path (`com.anthropic.claude/scripts/`) and nothing escapes the plugin directory.

Hooks are Claude-namespace components; agents without a hook mechanism simply run without them.

### Canon and synchronization

> [!WARNING]
> **Edit the canon in [CLAUDE.md](CLAUDE.md) first, then reconcile every skill in [`skills/`](skills) against it.**

[`CLAUDE.md`](CLAUDE.md) at the plugin root is the human-readable single source of truth for the framework — and, as the file states explicitly, it is *not* auto-loaded into the host agent's context.

The operative content is carried into context by the skills, each of which restates only the compact canon it needs. This is a deliberate synchronization burden accepted in exchange for skills that work standalone.

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset=".github/assets/divider.svg">
    <img src=".github/assets/divider-light.svg" alt="" width="700">
  </picture>
</p>

<a name="plate-06" id="plate-06"></a>

## Plate 06 — Colophon

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset=".github/assets/plate-06.svg">
    <img src=".github/assets/plate-06-light.svg" alt="Plate 06 — Colophon. Maintainers, contributing, license — the framework is meant to be passed on." width="100%">
  </picture>
</p>

### Maintainers

- [@AlastairZeved](https://github.com/AlastairZeved) — author and maintainer.

### Contributing

Questions and framework discussion: [open an issue](https://github.com/AlastairZeved/With-Love-Math/issues). Pull requests are welcome for corrections and for keeping the several copies in sync; proposals that change the framework itself should be opened as issues first, since the framework is the content of the plugin.

| The one non-negotiable | The reason |
|---|---|
| **Edit the canon in [CLAUDE.md](CLAUDE.md) first, then reconcile every skill in [`skills/`](skills) against it.** | The skills each carry their own copy of the canon by design; a change that updates one copy but not the others breaks the synchronization rule the plugin runs on. Subagents under [`com.anthropic.claude/agents/`](com.anthropic.claude/agents) must keep `Write` and `Edit` disallowed — they evaluate, they do not modify. |

When you add a piece that only one client understands, put it in that client's own namespace (`com.anthropic.claude/` for Claude Code, `com.github.copilot/` for Copilot), declare it in that client's manifest where the client supports it, and keep the portable `skills/` directory free of anything client-specific.

Per-agent adapters live in [`.codex-plugin/plugin.json`](.codex-plugin/plugin.json) (Codex compatibility fallback) and [`.cursor-plugin/plugin.json`](.cursor-plugin/plugin.json) (Cursor) — update them whenever the portable files they point at change.

### License

[MIT](LICENSE) © AlastairZeved

## Design notes

This page is one continuous object: seven numbered plates on a single ground, the invariant as the recurring anchor.

- **The ground.** One seamless motif carries the whole page — warm graph paper (a 24-unit minor grid, a 120-unit major grid, a punch-holed margin rule) over a faint field of EB Garamond italics: ampersands and the digits of the ten positions. "Love letter meets mathematics" as a texture, not a decoration. The motif is defined once per theme in `.github/assets/textures/` (`ground-dark.svg`, `ground-light.svg`) and inherited by every chapter plate and diagram; it extends the banner's Deep Surfaces aesthetic (near-black field, faint glyph field, gold rules) down the page instead of restarting the design at section one.
- **Chapter system.** Seven plates, numbered 00–06, all on the one continuous ground — no section restarts the design. Each plate: a ghost chapter numeral, a `PLATE` label with rule, a serif display title in EB Garamond, an italic keyline restating the chapter's thesis, and a ribbon icon at the right edge, so a mid-page reader re-orients from the plate number and icon alone.
- **The icon family.** One system: 48-unit grid, 2.4-unit stroke, round caps and joins, gold on near-black. Every visual cue on the page comes from it — the inventory with the design rules lives in [docs/icons.md](docs/icons.md).
- **Diagrams, not prose.** The WHY→WHO→FEEL→EVOKE loop is a cycle diagram (`art-loop`), the ten positions are a two-axis map (`art-map`), R1–R4 are four parallel callouts (`art-pillars`), the drift of a decision from its origin is drawn (`art-drift`), and the install routes are a hallway of doors (`art-doors`). Tables remain as accessible fallbacks inside collapsible sections.
- **The spatial test.** Each plate is a room: the showcase is a screening room, the install section a hallway of doors, the framework a gallery with the four principles as framed callouts, the map a two-axis chart, the WONDER plate a lantern-lit inner chamber at the center of the house, and the colophon the door left open behind you. The question — *would this exist in a physical version of this space?* — was applied to every section; anything that could not be answered with a spatial object was reworked into one.
- **Constraints.** Static SVG/CSS only; zero new runtime dependencies; presentation restyle only — meaning is frozen.

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset=".github/assets/divider.svg">
    <img src=".github/assets/divider-light.svg" alt="" width="700">
  </picture>
</p>

<p align="center">
  <sub><strong>github.com/alastairzeved/with-love-math</strong> — *With Love, Math.*<br>
  <em>The framework is meant to be passed on.</em></sub>
</p>
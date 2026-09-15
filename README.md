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
[![math-approved](https://img.shields.io/badge/math--approved-WONDER_preserved-f0d878?style=flat-square&labelColor=0d0d10)](#the-invariant-wonder)

An [Agent Plugins 1.0.0](https://agent-plugins.org/specification) plugin that turns deliberation into a verdict. It is a folder of written instructions an agent reads when it starts. Nothing to compile, nothing to run. Hand it a decision, or a project already underway, and it runs the whole thing through one fixed set of questions: four principles, one loop, one invariant — the one thing that must not change. What comes back is a verdict, **Aligned** or **Needs Revision**, and when the answer is Needs Revision it names exactly which principle failed and the single first move to fix it.

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset=".github/assets/pillars.svg">
    <img src=".github/assets/pillars-light.svg" alt="One body of work, three pillars: Gregorian Mode interrogates design choices; Editorial Loop interrogates text; With Love, Math interrogates decisions — the broadest and most personal." width="100%">
  </picture>
</p>


> [!IMPORTANT]
> **It is not a cover generator, not a website builder, and not a chat partner for endless deliberation.** Those three all produce something — a cover, a site, more conversation. This one produces a judgement. It is a discipline for running a decision and getting a verdict: an **Aligned / Needs Revision** verdict that names any failing principle.

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset=".github/assets/divider.svg">
    <img src=".github/assets/divider-light.svg" alt="" width="700">
  </picture>
</p>

<a name="plate-00" id="plate-00"></a>

## 00 — Watch the Showcase

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset=".github/assets/plate-00.svg">
    <img src=".github/assets/plate-00-light.svg" alt="Plate 00 — Watch the Showcase. The four principles, the loop, and the invariant in motion." width="100%">
  </picture>
</p>

## Contents

<a name="contents" id="contents"></a>

| | | |
|---|---|---|
| [**00 — Watch the showcase**](#plate-00) · *1½ min* | [**01 — Background**](#plate-01) | [**Plate 02 — Install**](#plate-02) |
| [**3 — Usage**](#plate-03) — commands · example · output | [**04 — The Framework**](#plate-04) — principles · loop · map · layers · WONDER | [**05 — Architecture**](#plate-05) — packaging · skills · subagents · hooks |
| [**06 — Colophon**](#plate-06) — maintainers · contributing · license | | |

<a name="plate-01" id="plate-01"></a>

## 01 — Background

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset=".github/assets/plate-01.svg">
    <img src=".github/assets/plate-01-light.svg" alt="Plate 01 — Background. Most work starts with a reason and a feeling, and then loses both." width="100%">
  </picture>
</p>

With Love, Math is a framework for not losing the feeling or the reason mid-build. Put simply, it's a framework for maintaining intention when designing with an agent. If you're looking for something to vibe code harder, look elsewhere. **R1 · Recursive Grounding** traces every choice back to where it started; **R2 · Emotion as Invariant** names the feeling before you begin and holds it steady through every change.

<a name="plate-02" id="plate-02"></a>

## 02 — Install

### Per-agent instructions

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

## 03 — Usage

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

<a name="plate-04" id="plate-04"></a>

## 04 — The Framework

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset=".github/assets/plate-04.svg">
    <img src=".github/assets/plate-04-light.svg" alt="Plate 04 — The Framework. Four principles, one loop, one map, four layers, one invariant." width="100%">
  </picture>
</p>

### The four principles (R1–R4)

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset=".github/assets/art-pillars.svg">
    <img src=".github/assets/art-pillars-light.svg" alt="The four principles: R1 Recursive Grounding — Why am I doing this?; R2 Emotion as Invariant — What feeling must I preserve?; R3 Distinction Within Unity — How do these parts make one whole?; R4 Scale the Invariance — Does this work at every size?" width="100%">
  </picture>
</p>

<details open>
<summary><strong>As a table</strong></summary>

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

### The ten-position map

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

Position 10 — **Find the Math** — is where the map ends: name the pattern, ratio, symmetry, or structure underneath the decision. If none exists, that absence is itself a finding. Most decision frameworks stop before this point. The claim here is that good decisions have an underlying form, and that naming it makes them easier to see and easier to fix.

### The invariant: WONDER

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset=".github/assets/art-wonder.svg">
    <img src=".github/assets/art-wonder-light.svg" alt="The invariant: WONDER. If a decision, design, or project does not evoke wonder, it has not yet passed." width="100%">
  </picture>
</p>

> [!TIP]
> **WONDER.** If a decision, design, or project does not evoke wonder, it has not passed. This is what **R2 · Emotion as Invariant** preserves and **R4 · Scale the Invariance** scales — the single test the whole framework resolves to.

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset=".github/assets/divider.svg">
    <img src=".github/assets/divider-light.svg" alt="" width="700">
  </picture>
</p>

<a name="plate-05" id="plate-05"></a>

## 05 — Architecture

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset=".github/assets/plate-05.svg">
    <img src=".github/assets/plate-05-light.svg" alt="Plate 05 — Architecture. Four layers of packaging, each doing a distinct job." width="100%">
  </picture>
</p>

The plugin has four layers, and each does a distinct job — plus a packaging split that keeps it portable.

### Commands

Five flat command files in [`com.anthropic.claude/commands/`](com.anthropic.claude/commands) — `decide.md`, `diagnose.md`, `map.md`, `teach.md`, `lexicon.md`.Copilot users get the same five doors as command wrappers under [`com.github.copilot/commands/`](com.github.copilot/commands).

### Skills

Four skills in [`skills/`](skills), each a `SKILL.md`:

| Skill              | Carries                                                              |
| ------------------ | -------------------------------------------------------------------- |
| `decision-engine`  | Principles, loop, and the structured output format (backs `/decide`)  |
| `diagnostic`       | The audit process: where an existing work loses the invariant (backs `/diagnose`) |
| `tutor`            | The canon plus a teaching structure and level-adaptation rules (backs `/teach`) |
| `lexicon`          | The canon plus the full glossary (backs `/lexicon`)                   |

### Subagents

Three subagents in [`com.anthropic.claude/agents/`](com.anthropic.claude/agents), all with `disallowedTools: Write, Edit` — they evaluate, they do not modify.

| Agent                  | Job                                            | Effort | Turns |
| ---------------------- | ---------------------------------------------- | ------ | ----- |
| `gregorian-decision`   | The full framework run → structured verdict    | medium | 15    |
| `invariant-checker`    | The fast narrow pass → `Preserved` / `Lost`    | low    | 8     |
| `ten-position-mapper`  | Structural cartography → map plus gaps         | medium | 12    |

The division of labor is clean: `gregorian-decision` is the full operation, `invariant-checker` is the scalpel, `ten-position-mapper` does the cartography.

Copilot users get the same three as `.agent.md` custom agents under [`com.github.copilot/agents/`](com.github.copilot/agents); the no-write guardrail travels in the prompt body there, since `.agent.md` frontmatter does not carry `disallowedTools`.

### Hooks

Two hooks in [`com.anthropic.claude/hooks/hooks.json`](com.anthropic.claude/hooks/hooks.json), both non-blocking:

- **SessionStart** runs [`com.anthropic.claude/scripts/welcome.sh`](com.anthropic.claude/scripts/welcome.sh), which greets you and lists the commands.
- **PreToolUse** on `Write|Edit` runs [`com.anthropic.claude/scripts/design-reminder.sh`](com.anthropic.claude/scripts/design-reminder.sh), which fires only when the file being touched matches `*.design.md` and reminds you to check the invariant (R2) and scale (R4). It exits 0 — it reminds, it does not gate.

The hook commands reference `${CLAUDE_PLUGIN_ROOT}` — the plugin root — so the scripts resolve through the namespace path (`com.anthropic.claude/scripts/`) and nothing escapes the plugin directory.

Hooks are Claude-namespace components; agents without a hook mechanism simply run without them.

## 06 — Colophon

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

### License

[MIT](LICENSE) © AlastairZeved

  <picture>
    <source media="(prefers-color-scheme: dark)" srcset=".github/assets/divider.svg">
    <img src=".github/assets/divider-light.svg" alt="" width="700">
  </picture>
</p>

<p align="center">
  <sub><strong>github.com/alastairzeved/with-love-math</strong> — *With Love, Math.*<br>
  <em>The framework is meant to be passed on.</em></sub>
</p>

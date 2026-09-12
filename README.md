# With Love, Math _(With-Love-Math)_

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-1.0.0-green.svg)](plugin.json)
[![Agent Plugins 1.0.0](https://img.shields.io/badge/Agent_Plugins-1.0.0-blue.svg)](https://agent-plugins.org/specification)
[![Standard Readme](https://img.shields.io/badge/standard--readme-follower-brightgreen.svg)](https://github.com/richardlitt/standard-readme)

Runs any decision through a WHY/WHO/FEEL/EVOKE loop, four principles, a ten-position map, one invariant: WONDER.

With Love, Math is a decisioning framework packaged as an [Agent Plugins 1.0.0](https://agent-plugins.org/specification) plugin — the portable package installs into any conformant agent, and client-namespaced components extend the agents that support more. It is not a cover generator, not a website builder, and not a chat partner for endless deliberation: it is a discipline for running a decision and getting a verdict — a binary **Aligned / Needs Revision** naming any failing principle.

The name carries a comma the repository does not — the repo is `With-Love-Math`, the framework is *With Love, Math* (the sign-off, the breath, the point). This is the third pillar in the same body of work as Gregorian Mode and Editorial Loop. Where Gregorian Mode interrogates design choices and Editorial Loop interrogates text, this plugin interrogates decisions — any decision. It is the broadest of the three, and in some ways the most personal.

The plugin *is* the framework. It applies its own principles to itself: R1 by always returning to Why, R2 by checking every decision against the invariant, R3 by keeping each principle distinct yet unified, R4 by working at any scale — one decision or a whole project.

## Table of Contents

- [Background](#background)
- [Install](#install)
  - [Dependencies](#dependencies)
  - [What loads where](#what-loads-where)
  - [Per-agent instructions](#per-agent-instructions)
- [Usage](#usage)
  - [Commands](#commands)
  - [Example](#example)
  - [Output format](#output-format)
- [The Framework](#the-framework)
  - [The four principles (R1–R4)](#the-four-principles-r1r4)
  - [The decisioning loop](#the-decisioning-loop)
  - [The ten-position map](#the-ten-position-map)
  - [The four layers](#the-four-layers)
  - [The invariant: WONDER](#the-invariant-wonder)
- [Architecture](#architecture)
  - [Portability — the packaging split](#portability--the-packaging-split)
  - [Commands — the public entry points](#commands--the-public-entry-points)
  - [Skills — the operative content](#skills--the-operative-content)
  - [Subagents — the specialists](#subagents--the-specialists)
  - [Hooks — the ambient reminders](#hooks--the-ambient-reminders)
  - [Canon and synchronization](#canon-and-synchronization)
- [Maintainers](#maintainers)
- [Contributing](#contributing)
- [License](#license)

## Background

Most work starts with a reason and a feeling, and then loses both. Iterations accumulate, constraints arrive, other people's opinions land on top, and by the end the decision no longer resembles the one you set out to make. With Love, Math is a framework for not losing them: R1 traces every choice back to its origin; R2 names the feeling before you start and holds it constant through every change.

"Gregorian" is the term the author reuses from Gregorian Mode, where it was defined as *a standard strangers adopt and never stop running* — hence `gregorian-decision`, the name of the full-framework subagent. Here the standard is a four-principle decisioning framework whose single invariant is WONDER. The framework is meant to be passed on, not just used privately: the `/teach` command and `tutor` skill exist precisely so others can adopt and run it.

Every element of the framework reads at four depths simultaneously — Design Philosophy (physical), Self-Help / Self-Love (emotional), Math in Nature (structural), Esotericism (spiritual). A good decision holds at all four. This is the framework's most unusual claim: a layout decision, a life decision, a structural pattern, and a spiritual question are the same object viewed from different altitudes.

Its brand personality is **Friendly · Quirky · Bold · Sophisticated** — warm enough to invite, strange enough to be memorable, confident enough to commit, refined enough to trust.

## Install

No build step, no package manager, no runtime dependencies — the plugin is plain markdown that a compatible agent discovers on load. Clone once; every install path below starts from that clone or reads the repository directly.

```bash
git clone https://github.com/AlastairZeved/With-Love-Math.git
```

The root [`plugin.json`](plugin.json) is the [Agent Plugins 1.0.0](https://agent-plugins.org/specification) manifest — the portable source of truth every conformant client reads. Client-specific adapters live in their own namespaces and are ignored by clients that do not implement them, which is what keeps the package portable.

### Dependencies

None. Markdown only. (Git, to clone the repository.)

### What loads where

| Agent | Install route | Skills | Commands | Subagents | Hooks |
|---|---|---|---|---|---|
| **Claude Code** | [`claude --plugin-dir`](#claude-code) | ✓ | ✓ 5 | ✓ 3 | ✓ 2 |
| **Hermes Agent** | [`hermes plugins install`](#hermes-agent) | ✓ 4 | via skills | — | — |
| **Codex** (CLI / ChatGPT app) | [`/plugins` browser + marketplace](#codex) | ✓ | — | — | — |
| **Cursor** | [Customize page or `~/.cursor/plugins/local`](#cursor) | ✓ | ✓* | ✓* | — |
| **GitHub Copilot** | [`copilot plugin install` / VS Code](#github-copilot) | ✓ | ✓ 5 | ✓ 3 | — |
| **Pi Agent** | [clone into `~/.pi/agent/skills/`](#pi-agent) | ✓ 4 | — | — | — |
| **Any SKILL.md agent** | [copy a `skills/` folder](#any-skillmd-agent) | ✓ | — | — | — |

\* Cursor reads the Claude-namespace `commands/` and `agents/` through its [`.cursor-plugin/plugin.json`](.cursor-plugin/plugin.json) manifest where a Claude-style command or agent is understood.

In agents that register no slash commands, the same procedures are reachable in words — "Run the decision engine on `<decision>`" reaches the identical skill. The commands are doors, not the house.

### Per-agent instructions

<a name="claude-code" id="claude-code"></a>
<details>
<summary><strong>Claude Code</strong> · <code>claude --plugin-dir ./With-Love-Math</code></summary>

Requires [Claude Code](https://code.claude.com/docs).

```bash
git clone https://github.com/AlastairZeved/With-Love-Math.git
claude --plugin-dir ./With-Love-Math
```

The `--plugin-dir` flag loads the plugin directly without marketplace installation. There is no `marketplace.json` in this repository, so `/plugin marketplace add AlastairZeved/With-Love-Math` will not work; `--plugin-dir` is the documented direct-load path. The five commands, three subagents, and both hooks live under the [`com.anthropic.claude/`](com.anthropic.claude) client namespace, declared in [`.claude-plugin/plugin.json`](.claude-plugin/plugin.json). `claude plugin validate .` passes on this repository as shipped.

To install permanently, copy the plugin into your personal skills directory:

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

Portable Agent Plugins packages install disabled by default; enable explicitly and restart the gateway for the skills to take effect. The four portable skills are discovered from the root manifest; `hermes plugins validate <repo-dir>` and `hermes plugins show with-love-math` verify the install, and `hermes plugins remove with-love-math` removes it.

</details>

<a name="codex" id="codex"></a>
<details>
<summary><strong>Codex</strong> · CLI plugin browser or ChatGPT desktop app</summary>

Requires [Codex](https://developers.openai.com/codex). Codex reads the portable root [`plugin.json`](plugin.json) — which declares the Agent Plugins schema and carries OpenAI's presentation data under `extensions["com.openai"]` (display name "With Love, Math", category "decision-making") — and OpenAI documents the `.codex-plugin/plugin.json` manifest as a supported compatibility fallback for existing `.codex-plugin/` packages.

In **Codex CLI**, open the plugin browser and install from a configured marketplace:

```text
/plugins
```

To make the plugin installable from this repository, add the repo as a marketplace source:

```bash
codex plugin marketplace add AlastairZeved/With-Love-Math
```

For **local testing**, OpenAI's packaging documentation routes local plugins through a marketplace file — either a repo-scoped `.agents/plugins/marketplace.json` (with the plugin folder under `$REPO_ROOT/plugins/`) or a personal one at `~/.agents/plugins/marketplace.json` — then install from the marketplace in the CLI browser or the ChatGPT desktop app and start a new session. Bundled skills become available in the new session. The `.codex-plugin/plugin.json` fallback manifest ships for environments that expect the legacy layout.

The three subagents stay in the Claude namespace — Codex subagents use TOML definitions, which this repo does not ship.

</details>

<a name="cursor" id="cursor"></a>
<details>
<summary><strong>Cursor</strong> · Customize page or <code>~/.cursor/plugins/local</code></summary>

Requires [Cursor](https://cursor.com/docs/plugins). Cursor supports the Agent Plugins open standard: a package with a root `plugin.json` loads in Cursor without changes, and Cursor-specific components keep working through the [`.cursor-plugin/plugin.json`](.cursor-plugin/plugin.json) manifest, which points at the portable `skills/` directory and at the Claude-namespace `commands/` and `agents/`.

Install from a marketplace: open **Customize** in the sidebar, find the plugin, and select **Install** with a project or user scope.

Develop locally without a marketplace:

```bash
ln -s /path/to/With-Love-Math ~/.cursor/plugins/local/With-Love-Math
```

then restart Cursor (or run **Developer: Reload Window**) and confirm the skills and components under **Customize**. Cursor discovers plugins in that folder when local plugin imports are allowed (on Teams and Enterprise, an admin setting controls this).

</details>

<a name="github-copilot" id="github-copilot"></a>
<details>
<summary><strong>GitHub Copilot</strong> · <code>copilot plugin install</code> or VS Code "Install Plugin From Source"</summary>

Requires Copilot in VS Code, the Copilot CLI, or the app. Copilot supports Agent Plugins 1.0.0: it reads the portable `skills/` directory and the root `plugin.json`, then reads Copilot-specific components from the [`com.github.copilot/`](com.github.copilot) client namespace — the three specialists as `.agent.md` custom agents and the five command procedures as command wrappers — so Copilot users get the full plugin, not only the portable skills.

From the Copilot CLI, installing straight from the repository is a documented path:

```bash
copilot plugin install AlastairZeved/With-Love-Math
```

The `install` command accepts an `OWNER/REPO` root, a Git URL, or a local directory. From **VS Code**, run **Chat: Install Plugin From Source** from the Command Palette (or **Install Plugin from Source** on the Plugins page of the Agent Customizations editor) and enter the repository URL:

```text
https://github.com/AlastairZeved/With-Love-Math
```

Support for agent plugins can be toggled with the `chat.plugins.enabled` VS Code setting. Skills appear in the **Configure Skills** menu; the specialist agents appear alongside custom agents.

</details>

<a name="pi-agent" id="pi-agent"></a>
<details>
<summary><strong>Pi Agent</strong> · clone into <code>~/.pi/agent/skills/</code></summary>

Pi discovers skills in its config directory, recursively finding any directory that contains a `SKILL.md`. Clone the repository into its global skills directory and the four portable skills are found automatically — no manifest needed.

```bash
git clone https://github.com/AlastairZeved/With-Love-Math.git ~/.pi/agent/skills/with-love-math
```

(Project-scoped alternative: clone into `.pi/skills/` in a trusted project.)

</details>

<a name="any-skillmd-agent" id="any-skillmd-agent"></a>
<details>
<summary><strong>Any other SKILL.md-compatible agent</strong> · copy a skill folder</summary>

Copy any folder under `skills/` into the agent's skills directory. Each skill is a self-contained `SKILL.md` with YAML frontmatter (`name`, `description`); nothing else is required.

```bash
git clone https://github.com/AlastairZeved/With-Love-Math.git
mkdir -p ~/.your-agent/skills
cp -r With-Love-Math/skills/* ~/.your-agent/skills/
```

</details>

## Usage

Once the plugin is loaded, the session-start hook greets you and lists the commands — in agents that ship the hook. Five commands, stable and minimal; each dispatches to a skill or subagent beneath it. In agents that do not register slash commands, invoke the same procedures in words — "Run the decision engine on `<decision>`" reaches the identical skill.

### Commands

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

The decision engine returns a structured verdict, in this fixed format:

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

The verdict is binary at the top level; failures are named by principle, and the framework never softens a Fail into a Weak to reach Aligned. If you want a verdict instead of a discussion, this is the point.

## The Framework

The framework is the content; the plugin is its encoding. It has five components — four principles, one loop, one map, four layers, one invariant.

### The four principles (R1–R4)

| Principle                     | Question                             | What it enforces                                    |
| ----------------------------- | ------------------------------------ | --------------------------------------------------- |
| **R1 · Recursive Grounding**  | "Why am I doing this?"               | Every decision traces back to its origin.           |
| **R2 · Emotion as Invariant** | "What feeling must I preserve?"      | A chosen feeling survives every iteration unchanged.|
| **R3 · Distinction Within Unity** | "How do these parts make one whole?" | Parts stay individually legible while cohering — "distinct colors, one shape." |
| **R4 · Scale the Invariance** | "Does this work at every size?"      | Integrity holds from 2-inch icon to 10-foot mural.  |

### The decisioning loop

```
WHY → WHO → FEEL → EVOKE → (return to WHY)
```

- **WHY** — the reason this exists
- **WHO** — who it is for, who receives it
- **FEEL** — the feeling that must be preserved
- **EVOKE** — how that feeling is produced

The loop is infinite; it always returns to the beginning. This is R1 in motion — no decision is ever fully grounded, only re-grounded each time you run the loop.

### The ten-position map

A second lens on the same structure. The loop is the sequence you run; the map is the shape it makes.

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

Position 10 — **Find the Math** — is the terminal move: name the pattern, ratio, symmetry, or structure underneath the decision. If none exists, that absence is itself a finding. This is the move most decision frameworks do not have; it is the claim that good decisions have an underlying form, and that naming it makes a decision more legible and more transferable.

### The four layers

1. **Design Philosophy** — physical, practical
2. **Self-Help / Self-Love** — emotional, psychological
3. **Math in Nature** — intellectual, structural
4. **Esotericism** — spiritual, transcendent

Any element can be read at any layer; a good decision holds at all four. (See [Background](#background).)

### The invariant: WONDER

**WONDER.** If a decision, design, or project does not evoke wonder, it has not passed. This is what R2 preserves and R4 scales — the single test the whole framework resolves to.

## Architecture

The plugin has four layers, and each does a distinct job — plus a packaging split that keeps it portable. This is also a plugin-authoring reference: it is a complete worked example of an Agent Plugins 1.0.0 package with client namespaces cooperating in one repository.

### Portability — the packaging split

Two kinds of content live side by side, per the Agent Plugins 1.0.0 standard (§8, client extensions):

- **Portable** — [`skills/`](skills) and the root [`plugin.json`](plugin.json). Every Agent Plugins 1.0.0 client reads these; they reference nothing client-specific.
- **Client-namespaced** — [`com.anthropic.claude/`](com.anthropic.claude) (commands, subagents, hooks, hook scripts) and [`com.github.copilot/`](com.github.copilot) (the same components in Copilot's documented formats, with a [porting note](com.github.copilot/README.md)). Clients that don't implement a namespace ignore it, which is what keeps the package portable. Claude Code's manifest at [`.claude-plugin/plugin.json`](.claude-plugin/plugin.json) declares the namespace paths for its commands, agents, and hooks.

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

The division of labor is clean: `gregorian-decision` is the full operation, `invariant-checker` is the scalpel, `ten-position-mapper` does the cartography. Copilot users get the same three specialists as `.agent.md` custom agents under [`com.github.copilot/agents/`](com.github.copilot/agents); the no-write guardrail travels in the prompt body there, since `.agent.md` frontmatter does not carry `disallowedTools`.

### Hooks — the ambient reminders

Two hooks in [`com.anthropic.claude/hooks/hooks.json`](com.anthropic.claude/hooks/hooks.json), both non-blocking:

- **SessionStart** runs [`com.anthropic.claude/scripts/welcome.sh`](com.anthropic.claude/scripts/welcome.sh), which greets you and lists the commands.
- **PreToolUse** on `Write|Edit` runs [`com.anthropic.claude/scripts/design-reminder.sh`](com.anthropic.claude/scripts/design-reminder.sh), which fires only when the file being touched matches `*.design.md` and reminds you to check the invariant (R2) and scale (R4). It exits 0 — it reminds, it does not gate.

The hook commands reference `${CLAUDE_PLUGIN_ROOT}` — the plugin root — so the scripts resolve through the namespace path (`com.anthropic.claude/scripts/`) and nothing escapes the plugin directory. Hooks are Claude-namespace components; agents without a hook mechanism simply run without them.

### Canon and synchronization

[`CLAUDE.md`](CLAUDE.md) at the plugin root is the human-readable single source of truth for the framework — and, as the file states explicitly, it is *not* auto-loaded into the host agent's context. The operative content is carried into context by the skills, each of which restates only the compact canon it needs. This is a deliberate synchronization burden accepted in exchange for skills that work standalone; the maintenance rule is: **edit the canon in CLAUDE.md first, then reconcile the skills against it.**

## Maintainers

- [@AlastairZeved](https://github.com/AlastairZeved) — author and maintainer.

## Contributing

Questions and framework discussion: [open an issue](https://github.com/AlastairZeved/With-Love-Math/issues). Pull requests are welcome for corrections and reconciliations; proposals that change the framework itself should be opened as issues first, since the framework is the content of the plugin.

The non-negotiable for any PR: **edit the canon in [CLAUDE.md](CLAUDE.md) first, then reconcile every skill in [`skills/`](skills) against it.** The skills each carry their own copy of the canon by design; a change that updates one copy but not the others breaks the synchronization rule the plugin runs on. Subagents under [`com.anthropic.claude/agents/`](com.anthropic.claude/agents) must keep `Write` and `Edit` disallowed — they evaluate, they do not modify.

When adding a client-namespaced component, add it to the owning namespace (`com.anthropic.claude/` for Claude Code, `com.github.copilot/` for Copilot), declare it in that client's manifest where the client supports it, and keep the portable `skills/` directory client-agnostic. Per-agent adapters live in [`.codex-plugin/plugin.json`](.codex-plugin/plugin.json) (Codex compatibility fallback) and [`.cursor-plugin/plugin.json`](.cursor-plugin/plugin.json) (Cursor) — update them when the portable surface they reference changes.

## License

[MIT](LICENSE) © AlastairZeved

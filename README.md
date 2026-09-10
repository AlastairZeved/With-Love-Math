# With Love, Math _(With-Love-Math)_

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-1.0.0-green.svg)](.claude-plugin/plugin.json)
[![Standard Readme](https://img.shields.io/badge/standard--readme-follower-brightgreen.svg)](https://github.com/richardlitt/standard-readme)

A decisioning framework packaged as a Claude Code plugin — four principles, a ten-position map, one invariant: WONDER.

With Love, Math runs any decision, project, or creative challenge through four recursive principles (R1–R4), a WHY/WHO/FEEL/EVOKE loop, a ten-position map, and a single emotional invariant — WONDER — then returns a binary verdict naming any failing principle. It is not a cover generator, not a website builder, and not a chat partner for endless deliberation: it is a discipline for running a decision and getting a verdict.

The name carries a comma the repository does not — the repo is `With-Love-Math`, the framework is *With Love, Math* (the sign-off, the breath, the point). This is the third pillar in the same body of work as Gregorian Mode and Editorial Loop. Where Gregorian Mode interrogates design choices and Editorial Loop interrogates text, this plugin interrogates decisions — any decision. It is the broadest of the three, and in some ways the most personal.

The plugin *is* the framework. It applies its own principles to itself: R1 by always returning to Why, R2 by checking every decision against the invariant, R3 by keeping each principle distinct yet unified, R4 by working at any scale — one decision or a whole project.

## Table of Contents

- [Background](#background)
- [Install](#install)
  - [Dependencies](#dependencies)
  - [Try it for one session](#try-it-for-one-session)
  - [Install it permanently](#install-it-permanently)
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

With Love, Math is a Claude Code plugin. Install it once and the commands, skills, subagents, and hooks load automatically at the start of every session.

### Dependencies

- [Claude Code](https://code.claude.com/docs), installed and working — `claude --version` should return a version
- Git, to clone the repository

### Try it for one session

Clone the repo, then point Claude Code at it:

```bash
git clone https://github.com/AlastairZeved/With-Love-Math.git
cd With-Love-Math
claude --plugin-dir .
```

Nothing is written to your system; the plugin loads for this session only. This is the fastest way to confirm it works before committing to an install. Run `/reload-plugins` to pick up local edits to the plugin without restarting.

### Install it permanently

Copy the plugin folder into your personal skills directory:

```bash
cp -r ./With-Love-Math ~/.claude/skills/with-love-math
```

Claude Code auto-discovers plugins in `~/.claude/skills/` that carry a `.claude-plugin/plugin.json` manifest — this repo has one — so it loads on the next session with no further install step, appearing as `with-love-math@skills-dir`.

Manage it afterward with:

```bash
# Disable
claude plugin disable with-love-math@skills-dir

# Re-enable
claude plugin enable with-love-math@skills-dir

# Uninstall (removes the folder)
rm -rf ~/.claude/skills/with-love-math
```

## Usage

Once the plugin is loaded, the session-start hook greets you and lists the commands. Five commands, stable and minimal; each dispatches to a skill or subagent beneath it.

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

The plugin has four layers, and each does a distinct job. This is also a Claude Code plugin-authoring reference: it is a complete worked example of commands, skills, subagents, and hooks cooperating in one package.

### Commands — the public entry points

Five flat command files in [`commands/`](commands) — `decide.md`, `diagnose.md`, `map.md`, `teach.md`, `lexicon.md`. Commands are thin: an argument hint, a one-line description, and dispatch instructions. Depth lives below them.

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

Three subagents in [`agents/`](agents), all `model: sonnet`, all with `disallowedTools: Write, Edit` — they evaluate, they do not modify.

| Agent                  | Job                                            | Effort | Turns |
| ---------------------- | ---------------------------------------------- | ------ | ----- |
| `gregorian-decision`   | The full framework run → structured verdict    | medium | 15    |
| `invariant-checker`    | The fast narrow pass → `Preserved` / `Lost`    | low    | 8     |
| `ten-position-mapper`  | Structural cartography → map plus gaps         | medium | 12    |

The division of labor is clean: `gregorian-decision` is the full operation, `invariant-checker` is the scalpel, `ten-position-mapper` does the cartography.

### Hooks — the ambient reminders

Two hooks in [`hooks/hooks.json`](hooks/hooks.json), both non-blocking:

- **SessionStart** runs [`scripts/welcome.sh`](scripts/welcome.sh), which greets you and lists the commands.
- **PreToolUse** on `Write|Edit` runs [`scripts/design-reminder.sh`](scripts/design-reminder.sh), which fires only when the file being touched matches `*.design.md` and reminds you to check the invariant (R2) and scale (R4). It exits 0 — it reminds, it does not gate.

### Canon and synchronization

[`CLAUDE.md`](CLAUDE.md) at the plugin root is the human-readable single source of truth for the framework — and, as the file states explicitly, it is *not* auto-loaded into the host agent's context. The operative content is carried into context by the skills, each of which restates only the compact canon it needs. This is a deliberate synchronization burden accepted in exchange for skills that work standalone; the maintenance rule is: **edit the canon in CLAUDE.md first, then reconcile the skills against it.**

## Maintainers

- [@AlastairZeved](https://github.com/AlastairZeved) — author and maintainer.

## Contributing

Questions and framework discussion: [open an issue](https://github.com/AlastairZeved/With-Love-Math/issues). Pull requests are welcome for corrections and reconciliations; proposals that change the framework itself should be opened as issues first, since the framework is the content of the plugin.

The non-negotiable for any PR: **edit the canon in [CLAUDE.md](CLAUDE.md) first, then reconcile every skill in [`skills/`](skills) against it.** The skills each carry their own copy of the canon by design; a change that updates one copy but not the others breaks the synchronization rule the plugin runs on. Subagents under [`agents/`](agents) must keep `Write` and `Edit` disallowed — they evaluate, they do not modify.

## License

[MIT](LICENSE) © AlastairZeved

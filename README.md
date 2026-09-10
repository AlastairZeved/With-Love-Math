# With-Love-Math
With Love, Math is a decisioning framework packaged as a Claude Code plugin. It runs any decision through four recursive principles (R1–R4), a WHY/WHO/FEEL/EVOKE loop, a ten-position map, and a single emotional invariant — WONDER — and returns a binary verdict naming any failing principle.

With Love, Math — what it is, how it runs, why you'd use it

This is the third pillar in the same body of work as Gregorian Mode and Editorial Loop. Where Gregorian Mode interrogates design choices and Editorial Loop interrogates text, this plugin interrogates decisions — any decision, project, or creative challenge. It is the broadest of the three, and in some ways the most personal.

The name in the subagent gives it away: gregorian-decision. The author is reusing the term from Gregorian Mode, where "Gregorian" was defined as "a standard strangers adopt and never stop running." Here that standard is a four-principle decisioning framework whose single invariant is WONDER.

# 1. What it's for

It is not a cover generator, a website builder, or a design system. It is a decisioning framework — a lens you run things through. The plugin is the framework, encoded as commands, skills, and subagents. As CLAUDE.md states it directly:

    A decisioning framework — not a cover generator, not a website builder. It runs any problem, project, or creative challenge through four recursive principles, maps it onto the ten-position map, and checks it against a single emotional invariant: WONDER. Every decision, design, and project must evoke it.

The plugin applies its own framework to itself. R1 by always returning to Why. R2 by checking every decision against the invariant. R3 by keeping each principle distinct yet unified. R4 by working at any scale — one decision or a whole project.

Its job: stop decisions from drifting. Most work starts with a reason and a feeling, and then loses both as it accumulates iterations, constraints, and other people's opinions. This framework is a discipline for not losing them.

# 2. The framework content
The four principles
Principle	Question	What it enforces
R1 · Recursive Grounding	"Why am I doing this?"	Every decision traces back to its origin. The elastic that snaps the loop to its start.
R2 · Emotion as Invariant	"What feeling must I preserve?"	A chosen feeling survives every iteration unchanged.
R3 · Distinction Within Unity	"How do these parts make one whole?"	Parts stay individually legible while cohering. "Distinct colors, one shape."
R4 · Scale the Invariance	"Does this work at every size?"	Integrity holds from 2-inch icon to 10-foot mural.
The loop

WHY → WHO → FEEL → EVOKE → return to WHY.

    WHY — the reason this exists

    WHO — who it is for, who receives it

    FEEL — the feeling that must be preserved

    EVOKE — how that feeling is produced

The loop is infinite. It always returns to the beginning. This is R1 in motion — no decision is ever fully grounded; it is re-grounded each time you run the loop.
The ten-position map

A second lens on the same structure. The loop is the sequence you run; the map is the shape it makes.
Position	Element
1	State the Goal (< 5 words)
2	WHY
3	WHO
4	FEEL
5	EVOKE
6	R1 · Recursive Grounding
7	R2 · Emotion as Invariant
8	R3 · Distinction Within Unity
9	R4 · Scale the Invariance
10	Find the Math

Position 10 — "Find the Math" — is the terminal move: name the pattern, ratio, symmetry, or structure underneath the decision. If none exists, that absence is itself a finding.
The four layers

Every element can be read at four depths simultaneously:

    Design Philosophy — physical, practical

    Self-Help / Self-Love — emotional, psychological

    Math in Nature — intellectual, structural

    Esotericism — spiritual, transcendent

A good decision holds at all four. This is the most unusual part of the framework: it claims that a layout decision, a life decision, a structural pattern, and a spiritual question are the same object viewed from different altitudes.
The invariant

WONDER. If a decision, design, or project does not evoke wonder, it has not passed. This is what R2 preserves and R4 scales. It is the single test the whole framework resolves to.
Brand personality

Friendly · Quirky · Bold · Sophisticated. Warm enough to invite, strange enough to be memorable, confident enough to commit, refined enough to trust.

# 3. How it works mechanically

The plugin has four layers, and each does a distinct job.
Commands — the public entry points

Five commands, stable and minimal. Each takes the user's argument and dispatches to a skill or subagent.
Command	Does
/decide	Run a decision through the full framework → Aligned / Needs Revision verdict
/diagnose	Audit an existing project against R1–R4 → prescription with first step
/map	Map a project onto the ten-position map → filled table plus gaps
/teach	Teach the framework, adapted to the learner
/lexicon	Define the framework's terms

Commands are thin. They contain the argument hint, a one-line description, and instructions to dispatch to a skill or agent. Depth lives below them.
Skills — the operative content

Four skills: decision-engine, diagnostic, lexicon, tutor.

Here is the key mechanical detail, and it is a sophisticated piece of plugin authoring. The CLAUDE.md at the plugin root is not auto-loaded into the host agent's context — the file says so explicitly:

    A CLAUDE.md at a plugin root is not auto-loaded into the host agent's context. This file is the human-readable single source of truth for the framework. The operative content is carried into context by the skills in skills/ (each restates only the compact canon it needs). Edit the canon here first, then reconcile the skills against it.

So the author maintains a single source of truth (CLAUDE.md) and then duplicates the compact canon into each skill that needs it. This is a deliberate synchronization burden accepted in exchange for skills that work standalone. The instruction "Edit the canon here first, then reconcile the skills against it" tells you the author knows this is a maintenance cost and has a process for it.

Each skill restates only the canon it needs. The decision-engine skill carries the four principles, the loop, and the output format. The tutor skill carries the same canon plus a teaching structure and adaptation rules. The lexicon skill carries the canon plus the full glossary. Every skill carries the invariant.
Agents — the specialists

Three subagents, all model: sonnet, all with disallowedTools: Write, Edit — they evaluate, they do not modify.

    gregorian-decision — the full framework run. Medium effort, 15 turns. States the goal, runs the loop, checks R1–R4 each as Pass/Weak/Fail with one line of evidence, finds the math, issues the verdict. Its closing instruction: "Never soften a Fail to reach Aligned."

    invariant-checker — the fast narrow pass. Low effort, 8 turns. Identifies the invariant, checks evidence for and against, analyzes where it leaks, returns Preserved/Lost. "This is a scalpel, not the whole operation."

    ten-position-mapper — maps a project onto all ten positions, checks that they connect, surfaces gaps. Medium effort, 12 turns.

The division of labor is clean. gregorian-decision is the full operation. invariant-checker is the quick check. ten-position-mapper does structural cartography.
Hooks — the ambient reminders

Two hooks, both non-blocking, both narrow.

SessionStart runs welcome.sh, which prints:
text

✨ With Love, Math — the framework is loaded.
Commands:
  /decide   <choice>    Run a decision through R1–R4 + the WONDER check
  /diagnose <project>   Audit a project and prescribe the first fix
  /map      <project>   Map it onto the ten-position map
  /teach    [audience]  Learn or teach the framework
  /lexicon  [term]      Define the framework's language
Invariant: WONDER. If it doesn't evoke wonder, it hasn't passed.

PreToolUse on Write|Edit runs design-reminder.sh, which greps the tool input for .design.md. If found, it prints:
text

🌿 Editing a design file — check the emotional invariant (R2): does this still evoke WONDER, and does it hold at every scale (R4)?

This is a well-scoped hook. It fires only when a file matching *.design.md is being written or edited, so it does not nag on ordinary edits. And it exits 0 — non-blocking. It reminds, it does not gate.
The output format

The decision-engine skill defines a strict output format:
text

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

The verdict is binary at the top level. Failures are named by principle. And the instruction is explicit: "never soften a Fail into a Weak to reach Aligned."

# 4. Why someone would use it
To keep a decision from drifting

The framework's premise is that decisions start with a reason and a feeling, and then lose both. R1 traces back to the reason. R2 names the feeling and holds it constant. Running the loop is a way to re-ground a decision that has wandered.
To get a verdict instead of a discussion

Most AI assistants will discuss a decision with you indefinitely. This one runs a process and returns Aligned or Needs Revision, with the failing principle named. That is a different product. It is for someone who wants to be told, not to be agreed with.
To check a project at every scale

R4 is a stress test most design processes skip. A logo, an icon, a billboard, and a mural are the same decision at different zoom levels. The framework forces you to ask whether the integrity survives the scaling. This is useful for anyone shipping work that will be seen at multiple sizes — brand systems, type, illustration, product UI.
To hold an emotional invariant across iterations

R2 is the discipline of naming a feeling before you start and checking it after every change. This is hard to do without a framework because the feeling is invisible once you are deep in execution. The plugin makes it a named, checkable thing — and the invariant-checker subagent exists specifically to verify it quickly.
To teach the framework

The tutor skill exists because this framework is meant to be passed on. It has adaptation rules for beginners, practitioners, and teachers-in-training. The teaching structure moves from Why → four principles → loop → optional map → one real practice decision. This is a framework designed to be adopted by others, not just used privately. That is exactly what "Gregorian" meant in the other plugin.
To get a structural read of a project

/map fills all ten positions from a project description and shows which positions are empty, thin, or overloaded. This is a fast way to see whether a project has a stated goal, a clear why, a defined audience, a named feeling, and an underlying pattern — or whether some of those are missing.
To find the math

Position 10 — "Find the Math" — is the move most decision frameworks do not have. It asks you to name the pattern, ratio, symmetry, or structure underneath the decision. This is not decoration. It is the claim that good decisions have an underlying form, and that naming it makes the decision more legible and more transferable.

# In One Paragraph

With Love, Math is a decisioning framework packaged as a Claude Code plugin. It runs any decision through four recursive principles (R1–R4), a WHY/WHO/FEEL/EVOKE loop, a ten-position map, and a single emotional invariant — WONDER — and returns a binary verdict naming any failing principle. It is invoked through five commands, executed by four skills and three read-only subagents, and supported by two non-blocking hooks that greet you and remind you to check the invariant when editing design files. You would use it to keep a decision from drifting from its reason and its feeling, to get a verdict rather than a discussion, to stress-test work at every scale, and to have a framework you can teach to others.

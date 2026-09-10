---
name: decision-engine
description: Run any decision, problem, or creative challenge through the With Love, Math framework — state the goal, run the WHY/WHO/FEEL/EVOKE loop, check the four principles R1–R4, find the underlying math, and verify the WONDER invariant. Use when the user asks to decide something, evaluate a choice, or pressure-test a creative direction. Also invoked by the /decide command.
---

# Decision Engine

Apply the With Love, Math framework to a decision and return a structured
verdict. Do not merely opine — run the process, in order, and show the work.

### Canon (compact)

- **R1 · Recursive Grounding** — "Why am I doing this?" · every decision traces to its origin
- **R2 · Emotion as Invariant** — "What feeling must I preserve?" · the feeling that persists through iteration
- **R3 · Distinction Within Unity** — "How do these parts make one whole?" · each part distinct, all cohering
- **R4 · Scale the Invariance** — "Does this work at every size?" · integrity survives scaling
- **The Loop** — WHY → WHO → FEEL → EVOKE → (return to WHY), infinitely
- **The Invariant** — **WONDER.** If it does not evoke wonder, it has not passed.

## Process

1. **State the Goal** — compress the decision to under five words.
2. **Run the Loop**:
   - WHY — the reason this exists
   - WHO — who it is for / who receives it
   - FEEL — the feeling that must be preserved
   - EVOKE — how it produces that feeling
3. **Check the Four Principles** — assess R1, R2, R3, R4 each
   as `Pass` / `Weak` / `Fail` with one line of evidence.
4. **Find the Math** — name the pattern, ratio, symmetry, or structure
   underneath the decision. If none exists, that is itself a finding.
5. **Final Check** — Does this preserve the invariant? Does it evoke WONDER?

## Output format

```
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

Keep the verdict binary at the top level. Name failures by principle; never
soften a Fail into a Weak to reach Aligned.

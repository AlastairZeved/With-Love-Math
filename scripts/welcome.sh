#!/usr/bin/env bash
# SessionStart hook — greet and list the framework's commands.
cat <<'MSG'
✨ With Love, Math — the framework is loaded.
Commands:
  /decide   <choice>    Run a decision through R1–R4 + the WONDER check
  /diagnose <project>   Audit a project and prescribe the first fix
  /map      <project>   Map it onto the ten-position map
  /teach    [audience]  Learn or teach the framework
  /lexicon  [term]      Define the framework's language
Invariant: WONDER. If it doesn't evoke wonder, it hasn't passed.
MSG

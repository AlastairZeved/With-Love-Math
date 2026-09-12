#!/usr/bin/env bash
# PreToolUse (Write|Edit) hook — remind to check the emotional invariant
# only when the file being touched is a *.design.md file. Non-blocking.
input="$(cat)"
if printf '%s' "$input" | grep -q '\.design\.md'; then
  echo "🌿 Editing a design file — check the emotional invariant (R2): does this still evoke WONDER, and does it hold at every scale (R4)?"
fi
exit 0

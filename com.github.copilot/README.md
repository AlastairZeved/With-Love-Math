# com.github.copilot

GitHub Copilot's client-extension namespace under the [Agent Plugins 1.0.0](https://agent-plugins.org/specification) standard (§8: client extensions). Copilot in VS Code, the Copilot CLI, and the GitHub Copilot app read the portable `skills/` directory and the root `plugin.json` from the repository root, then read Copilot-specific components from this directory — `agents/` (`.agent.md` custom agents), `commands/` (`.command.md` wrappers), `rules/`, and `hooks/hooks.json`. Other clients ignore this namespace, so the package stays portable.

## What ships here

| Component | File | Role |
|---|---|---|
| Gregorian Decision | [`agents/gregorian-decision.agent.md`](agents/gregorian-decision.agent.md) | Custom agent (`.agent.md`) — the full framework run → structured verdict |
| Invariant Checker | [`agents/invariant-checker.agent.md`](agents/invariant-checker.agent.md) | Custom agent — the fast narrow pass → `Preserved` / `Lost` |
| Ten-Position Mapper | [`agents/ten-position-mapper.agent.md`](agents/ten-position-mapper.agent.md) | Custom agent — structural cartography → map plus gaps |
| Decide procedure | [`commands/decide.command.md`](commands/decide.command.md) | Thin wrapper: loads and follows the `decision-engine` skill |
| Diagnose procedure | [`commands/diagnose.command.md`](commands/diagnose.command.md) | Thin wrapper: loads and follows the `diagnostic` skill |
| Map procedure | [`commands/map.command.md`](commands/map.command.md) | Thin wrapper: dispatches the ten-position mapping |
| Teach procedure | [`commands/teach.command.md`](commands/teach.command.md) | Thin wrapper: loads and follows the `tutor` skill |
| Lexicon procedure | [`commands/lexicon.command.md`](commands/lexicon.command.md) | Thin wrapper: loads and follows the `lexicon` skill |

The four portable skills need nothing here — they are discovered from `skills/` by every Agent Plugins client, Copilot included. The eight files above exist so Copilot users get the full plugin (the three specialist agents and the five command doors) rather than the skills alone.

## Porting note

All eight files port the components under [`com.anthropic.claude/`](../com.anthropic.claude/) (the Claude Code namespace, issue #1's packaging split) into Copilot's documented formats: each subagent becomes an `.agent.md` custom agent and each slash command keeps its Claude-style frontmatter as a `.command.md` wrapper. Discovery of the command files follows the namespace layout the VS Code agent-plugins documentation shows; if a given Copilot surface does not surface them, the portable path still works — ask for the procedure in words ("Run the decision engine on `<decision>`"), which is the documented universal door in the root [README](../README.md#usage).

The three agents keep their guardrail (`they evaluate, they do not modify`) in the prompt body — `.agent.md` frontmatter carries `description`, and the `disallowedTools` restriction stays enforced by the instruction rather than the manifest.
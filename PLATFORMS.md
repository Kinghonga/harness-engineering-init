# Platform Triggers & Capability Ceilings

The harness loop logic (in SKILL.md) works on any agent that can read/write
files. This file is about making it **fire automatically** instead of
relying on the agent remembering. Triggers are platform-specific and their
**capability ceilings are not equal** — never promise uniform behavior.

## The portability vs determinism tradeoff

You cannot have both full portability and full determinism. Pick a point on
the spectrum per project:

| Trigger type | Portability | Determinism | Needs |
|---|---|---|---|
| AGENTS.md tells agent to run the loop | max | low (prompt-based) | nothing |
| Platform-native hook calls the logic | medium | medium-high | per-platform adapter |
| File-watcher daemon calls the logic | medium | high | a running process |
| Git hook (if git present) | low (git-only) | high | git repo |

## Per-platform recipes

### Claude Code — highest ceiling

Claude Code exposes lifecycle hooks in `settings.json`:
`PreToolUse`, `PostToolUse`, `Stop`, `SubagentStop`, `SessionStart`.

- **Stop hook with exit code 2** can force the agent to resume — the only
  mainstream platform that can auto-force the Critic loop mid-session. Wire
  it to run the Critic when the agent tries to stop with unanalyzed traces.
- `SubagentStop` can trigger a review subagent after a coding subagent
  finishes (cross-review pattern).
- `PreToolUse` on edit/write can run a preflight check before a structural
  edit, blocking dependency-direction violations before they land.

### opencode — medium ceiling (detection hard, analysis soft)

opencode exposes plugin events: `session.created`, `session.idle`,
`file.changed`, `tool.execute.before`, `tool.execute.after`.

- **`file.changed`** is the best fit: when a file under `.harness/trace/`
  changes, fire an action. This makes trace→Critic-bookkeeping deterministic
  **without a separate daemon**.
- **`session.idle` is fire-and-forget** — a plugin/hook **cannot force the
  agent to resume**. So the LLM Critic analysis cannot be auto-forced; it
  must run in the next session (the hook writes a "critic pending" marker,
  and AGENTS.md tells the agent to clear it on start).
- `SubagentStop` is **not supported** — the cross-review auto-trigger does
  not map directly.

Honest ceiling: opencode can harden *detection* and *bookkeeping*, but the
*analysis* stays a soft agent action. Do not claim otherwise.

### Trae / Cursor / Continue.dev — low ceiling

These expose rules/prompt files but limited or undocumented lifecycle hooks.
Treat them as **AGENTS.md-driven soft triggers**: the rules file instructs
the agent to run the harness phases. Determinism lives only in execution,
not in the trigger.

### Git (optional, when present)

If the project uses git (not all do — do not assume it):
- `pre-commit` → preflight (block new violations)
- `post-commit` → health snapshot

Git is one event source among several, not a requirement.

### No hooks / manual

The agent follows AGENTS.md and runs the phases on demand, or the human
triggers them by hand. This is the graceful default — the loop still works,
it just isn't auto-forced.

## Wiring order recommendation

1. First get the loop to close **manually once** (run the Critic by hand,
   produce the first `memory/failures/` entry). Prove value before
   automating.
2. Add the health check as a habit (read-only, cheap) so silent failure
   stays visible.
3. Only then wire the platform-native trigger — and document the ceiling
   honestly in the project's AGENTS.md.

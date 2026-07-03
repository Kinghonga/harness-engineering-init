# Harness Templates

Use these verbatim. Consistent structure is what lets the Critic find
patterns across records later. Date format is `YYYYMMDD`.

## Checkpoint (`.harness/tasks/{name}-{YYYYMMDD}.md`)

```markdown
# {Task name} - checkpoint

**date**: {YYYYMMDD}
**status**: {in-progress | done | blocked}

## Architecture decisions
- {key decision 1}
- {key decision 2}

## Files touched
### {added | modified}
| layer | file |
|---|---|
| {layer} | {path} |

## Verification result
- [ ] {lint/typecheck/test/build command}: {pass | fail}
- [ ] failure trace: {.harness/trace/... or none}

## Next step
{what to do next}
```

## Failure trace (`.harness/trace/failure-{type}-{YYYYMMDD}.md`)

```markdown
# {Short title}

**date**: {YYYYMMDD}
**type**: {compile | lint | test | dependency-direction | other}

## Failing command
{exact command(s)}

## Error summary
{paste the real error output, trimmed to the relevant lines}

## Fix attempts
1. {what was tried}
2. {what was tried}

## Root cause
{why it actually failed, beneath the symptom}

## Fix applied
{final fix}

## Current verification status
- {command}: {pass | fail}
```

## Failure pattern (`.harness/memory/failures/{pattern}.md`) — written by the Critic

```markdown
# Pattern: {pattern name}

- occurrence count: {N}
- first seen: {YYYYMMDD}
- last seen: {YYYYMMDD}

## Typical scenario
{when this failure tends to happen}

## Root cause
{the deep cause, shared across the occurrences}

## Prevention
{concrete check or rule that would have stopped it}

## Rule update
- target file: {AGENTS.md | harness-rules | lint config}
- proposed addition: {exact text}
- status: {proposed | applied | not project-specific}
```

## Episodic memory (`.harness/memory/episodic/{topic}-{YYYYMMDD}.md`)

```markdown
# {Short description}

- date: {YYYYMMDD}
- scenario: {when it happened}
- lesson: {what was learned}
- rule update: {yes -> where | no}
```

## Procedural memory (`.harness/memory/procedural/{flow}-{YYYYMMDD}.md`)

```markdown
# Flow: {task type}

- applies when: {when to use this procedure}
- success count: {N}

## Steps
1. {step}
2. {step}

## Verification
{command(s) to confirm success}

## Compiled to script?
- {no | yes -> path}
```

## Baseline (`.harness/baseline.json`)

```json
{
  "captured": "YYYYMMDD",
  "lint": { "errors": N, "warnings": N },
  "typecheck": { "errors": N },
  "test": { "fail": N, "pass": N },
  "note": "Pre-existing debt snapshot. Only deltas from here are signal."
}
```

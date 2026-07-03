---
name: harness-engineering-init
description: Initialize and operate a project's AI-agent harness-engineering loop so it actually runs, not just gets scaffolded. Scaffolds the .harness/ structure, checks whether the loop is alive, drives task checkpoints, failure-trace recording, and the Critic analysis that converts traces into failure-pattern memory and rule updates. Use when the user says "harness", asks to set up / check / run harness engineering, mentions .harness/ or AGENTS.md discipline, wants an AI coding agent's loop to self-improve, or when checkpoints/traces/memory are not being maintained. Makes silent harness failure visible and closes the trace-to-Critic-to-failures loop that usually dies.
---

# Harness Engineering

A harness that doesn't run is just documentation. This skill operates the
AI-agent harness loop — scaffold, check health, checkpoint, record traces,
run the Critic, evolve rules — and makes silent failure visible.

Most harnesses die the same way: structure gets scaffolded, the "recording
half" (checkpoints + traces) limps along manually, and the "evolution half"
(trace → Critic → failure-patterns → rule updates) never runs once. This
skill treats the evolution half as the point, not an afterthought.

## Core principle

**Logic is portable; triggers are not.** The phases below work on any agent
that can read/write files. Making them fire automatically depends on the
platform — see [PLATFORMS.md](PLATFORMS.md). **Never confuse "I scaffolded
`.harness/`" with "the harness runs."** Init is five minutes; keeping the
loop alive is the job.

## Phase 0 — Health check first (read-only)

Before any harness action, check whether the loop is alive, using your own
file tools (list / read / stat). This touches nothing — run it freely.

1. If `.harness/` is absent → not initialized; go to Phase 1.
2. If present, list content files in each dir (exclude `README.md`,
   `.gitkeep`):
   - `tasks/` → checkpoint count + newest date
   - `trace/` → trace count
   - `memory/failures/` → failure-pattern count
   - `memory/episodic/`, `memory/procedural/` → counts
3. Find the newest checkpoint date. Records are named `{name}-{YYYYMMDD}.md`,
   so parse the date from filenames (fall back to file mtime only if a name
   has no date). Compute days since that date.
4. Verdict (evaluate in order):
   - `failures/` empty **and** traces > 0 → **BROKEN**: traces are waiting,
     the Critic has never run. Say this out loud.
   - no checkpoints at all → **EMPTY**: structure exists but nothing recorded yet.
   - newest checkpoint > 14 days → **DORMANT**.
   - newest checkpoint > 7 days → **STALE**.
   - otherwise → **HEALTHY** (active; if traces exist, also run Phase 4 to
     confirm none are unanalyzed).

Do not proceed to scaffold or checkpoint as if all is well — a dead loop is
the normal state and the thing to fix.

## Phase 1 — Init (only if `.harness/` is absent)

Scaffold the standard structure:

```
.harness/
  tasks/        README.md   (checkpoint template + rules)
  trace/        README.md   (failure-record template + rules)
  memory/
    episodic/   .gitkeep
    failures/   .gitkeep    <- THE file that proves the loop ever ran
    procedural/ .gitkeep
    README.md   (three-memory model + self-evolution loop)
```

Each README carries its template and rules (see [TEMPLATES.md](TEMPLATES.md)).
Do NOT create empty READMEs with no template — a scaffold with no
instructions is how harnesses die silently.

Then add a one-line pointer to the project's `AGENTS.md` (create one if
absent): `> Harness loop lives in .harness/ — run the harness skill's health
check to see if it's alive.`

If `.harness/` already exists, **do not re-scaffold** — go to Phase 0.

## Phase 2 — Checkpoint (task starts)

When a medium-or-larger task begins, write
`.harness/tasks/{name}-{YYYYMMDD}.md` from the checkpoint template.
Required fields: stage, status, architecture decisions, files touched,
verification result, next step.

This is the "recording half." It usually works because it's a low-friction
write. Its only purpose is to feed the evolution half later.

## Phase 3 — Verify + trace + baseline

Run the project's own verification (lint / typecheck / test / build). When
it fails past one retry, record
`.harness/trace/failure-{type}-{YYYYMMDD}.md` from the trace template:
error, attempts, root cause, fix.

**Baseline rule (critical):** the first time you verify a project, record
the current violation count as the baseline (in `.harness/baseline.json` —
see [TEMPLATES.md](TEMPLATES.md)). Thereafter treat only the **delta** as
signal. Pre-existing debt is noise; without a baseline the agent learns to
ignore verification entirely, and the loop can never converge. Never silently
bypass full-repo verification — if it is red from pre-existing debt, record
the baseline and report the delta explicitly.

## Phase 4 — Critic (the part that usually dies) ★

If you do nothing else from this skill, do this. This is the core.

When traces exist and `memory/failures/` is empty (or a trace has no
matching failure-pattern), analyze the traces and write a failure pattern.
A trace is **covered** if its date stamp (YYYYMMDD from its filename)
appears in any failures/ file, or its topic is named in a pattern's
"typical scenario". Uncovered traces are pending — analyze those.
**This is reasoning work — do it yourself, do not skip it.** For each
cluster of related traces:

1. Read the trace(s).
2. Name the failure pattern (e.g. `st-render-after-async-data`).
3. Find the root cause beneath the symptom, not just the symptom.
4. Write `.harness/memory/failures/{pattern}.md` from the failure template:
   pattern name, occurrence count, typical scenario, root cause, prevention,
   rule update.
5. If the prevention maps to a concrete rule, propose the rule update to the
   project's harness-rules / `AGENTS.md` and **ask the user before writing**.

A trace with no corresponding failure-pattern entry means the loop is open.
Close it. Phase 0 exists to make an open loop visible; this phase exists to
close it. Re-run the Phase 0 health check afterward to confirm `failures/`
is no longer empty.

## Phase 5 — Evolve (compile, don't just remember)

When the same task type succeeds 3+ times with near-identical steps, compile
the procedural memory into a deterministic script or checklist (a
"trajectory"). Record it in `memory/procedural/`. The goal is to stop
re-asking the LLM for mechanical, repeatable work.

This is the terminal state of a mature harness: common operations become
scripts; the LLM handles only the genuinely novel.

## Platform triggers (optional — makes it automatic)

The phases above work on any agent that can read/write files. To make them
fire automatically instead of relying on the agent remembering, wire a
trigger for your platform. **Capability ceilings differ**: Claude Code can
force-resume via Stop hooks; opencode can detect file changes but cannot
force-resume; hookless tools rely on the agent or a human. See
[PLATFORMS.md](PLATFORMS.md) for per-platform recipes.

Do not promise the user "automatic harness" without checking what their
platform can actually enforce.

## Templates

Checkpoint, trace, failure-pattern, memory, and baseline templates live in
[TEMPLATES.md](TEMPLATES.md). Use them verbatim — consistent structure is
what lets the Critic find patterns across records later.

## Guardrails

- Never modify project source code from this skill, except adding the
  one-line harness pointer to `AGENTS.md`.
- Phase 0 (health check) is read-only. Run it freely; it touches nothing.
- Ask before writing rule updates (Phase 4 step 5) — rules are owned by the
  human.
- Do not scaffold a second `.harness/` if one exists; run the health check
  instead.
- If the user has uncommitted work in progress, do not touch those files —
  harness records are metadata, not code changes.

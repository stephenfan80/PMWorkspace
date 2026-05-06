---
name: pm-handoff
description: |
  PMWorkspace handoff generator. Use when an aligned brief, chosen prototype direction,
  PRD notes, Zoon doc, or product decision record should become PRD-ready, design-ready,
  experiment-ready, or engineering handoff material with goals, scope, non-goals,
  acceptance criteria, metrics, risks, open decisions, and reusable next steps.
---

# PM Handoff

Turn the chosen product direction into a reusable delivery artifact without pretending every unknown is solved.

## Preamble

Run platform checks and usage logging:

```bash
_PMW_BIN=""
for _CANDIDATE in "$PWD/bin" "$PWD/pmworkspace-shared/bin" "$HOME/.codex/skills/pmworkspace-shared/bin"; do
  if [ -x "$_CANDIDATE/pmw-log" ]; then _PMW_BIN="$_CANDIDATE"; break; fi
done
[ -n "$_PMW_BIN" ] && "$_PMW_BIN/pmw-update-check" 2>/dev/null || true
[ -n "$_PMW_BIN" ] && "$_PMW_BIN/pmw-log" usage pm-handoff >/dev/null 2>&1 || true
```

## Workflow

1. Read the latest aligned brief, strategy decisions, and prototype manifest if available.
2. Choose handoff type: PRD-ready, design-ready, experiment-ready, or engineering-ready.
3. Include goal, target user, problem, scenario, chosen direction, scope, non-goals, acceptance criteria, metrics, risks, dependencies, and open decisions.
4. Keep unsupported capabilities under `不可虚构 / Not invented`.
5. Log final delivery decisions when platform scripts are available.

## Output Shape

```markdown
# PMWorkspace Handoff: <feature>

## Summary

## Goal And Metrics

## User / Job / Scenario

## Chosen Direction

## Scope

## Non-Goals

## Acceptance Criteria

## Experiment Or Rollout Notes

## Risks And Open Decisions

## Not Invented
```

---
name: pm-strategy-review
description: |
  PMWorkspace strategy review. Use when a product direction, brief, PRD, prototype
  concept, or scope decision needs challenge before design or delivery. Reviews ambition,
  scope, positioning, value exchange, trust, counter-metrics, feasibility, risks,
  what to remove, what to expand, and what must be decided by the PM.
---

# PM Strategy Review

Challenge the product direction before prototype or handoff. The goal is a stronger product strategy, not more features by default.

## Preamble

Run update and usage checks when platform scripts are available:

```bash
_PMW_BIN=""
for _CANDIDATE in "$PWD/bin" "$PWD/pmworkspace-shared/bin" "$HOME/.codex/skills/pmworkspace-shared/bin"; do
  if [ -x "$_CANDIDATE/pmw-log" ]; then _PMW_BIN="$_CANDIDATE"; break; fi
done
[ -n "$_PMW_BIN" ] && "$_PMW_BIN/pmw-update-check" 2>/dev/null || true
[ -n "$_PMW_BIN" ] && "$_PMW_BIN/pmw-log" usage pm-strategy-review >/dev/null 2>&1 || true
```

## Workflow

1. Read the current brief or PM Jobs alignment if available.
2. Read `../pmworkspace-shared/references/adversarial-review.md`.
3. Select 3-5 challenge lenses relevant to the scenario.
4. Present concrete strategy choices. Do not silently change scope.
5. Log accepted strategy decisions when platform scripts are available.

## Review Lenses

- Problem reality and evidence.
- Status quo competition.
- Scope expansion versus scope reduction.
- Value before friction or costly action.
- Trust, privacy, and data credibility.
- Business conflict or metric gaming.
- Feasibility and unsupported promises.
- Edge cases and failure states.
- Design-system fit.

## Output

```text
PM Strategy Review:
- Strongest premise:
- Weakest assumption:
- Recommended posture: expand / hold / reduce / pivot
- Strategy choices:
- Not in scope:
- Prototype implications:
- PM decisions required:
- Recommended next skill:
```

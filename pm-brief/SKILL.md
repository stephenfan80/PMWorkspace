---
name: pm-brief
description: |
  PMWorkspace brief generator. Use when product alignment, PM Jobs output, strategy
  review, PRD notes, Zoon docs, screenshots, or customer insights need to become a
  reusable Quick, Standard, or Deep product brief with version, source of truth,
  assumptions, decisions, constraints, and Aligned status before image-2 prototypes.
---

# PM Brief

Create the product contract that later prototype, handoff, and experiment steps must read.

## Preamble

Run platform checks and usage logging when possible:

```bash
_PMW_BIN=""
for _CANDIDATE in "$PWD/bin" "$PWD/pmworkspace-shared/bin" "$HOME/.codex/skills/pmworkspace-shared/bin"; do
  if [ -x "$_CANDIDATE/pmw-log" ]; then _PMW_BIN="$_CANDIDATE"; break; fi
done
[ -n "$_PMW_BIN" ] && "$_PMW_BIN/pmw-update-check" 2>/dev/null || true
[ -n "$_PMW_BIN" ] && "$_PMW_BIN/pmw-log" usage pm-brief >/dev/null 2>&1 || true
```

## Workflow

1. Read `../pmworkspace-shared/references/product-plan-handoff.md`.
2. Choose Quick, Standard, or Deep Brief based on ambiguity and risk.
3. Include source of truth, version, confirmation status, scenario route, user job, goal, counter-metric, constraints, not-invented items, and PM decision items.
4. If Zoon is provided, read `../pmworkspace-shared/references/zoon-workflow.md` and treat the latest approved Zoon snapshot as source of truth.
5. Save the brief with `pmw-log brief <name>` when platform scripts are available.

## Alignment Rule

Only `Aligned` briefs can feed image prompts. If the user has not confirmed, mark `Ready for PM confirmation` and stop before prototype generation.

## Output

Return the smallest useful brief and end with:

```text
Brief status:
- Version:
- Confirmation status:
- Source of truth:
- Saved asset:
- Next skill:
```

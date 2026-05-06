---
name: pm-workspace
description: |
  PMWorkspace main entry for product managers and designers. Use when product ideas,
  PRDs, Zoon docs, screenshots, customer insights, or prototype requests need routing
  into product problem definition, strategy review, brief creation, mobile-first
  image-2 prototype exploration, or handoff. Runs first-use guidance, update checks,
  local usage logging, and routes to pm-jobs, pm-strategy-review, pm-brief,
  pm-prototype-shotgun, or pm-handoff. Also use when the user has just installed
  PMWorkspace and needs a welcome guide, onboarding, starter prompts, or help
  choosing what to do first.
---

# PMWorkspace

PMWorkspace is a product workbench for turning raw product context into reusable product assets: decisions, briefs, prototype prompts, image-2 screens, and handoff notes.

## Platform Preamble

Run this before the workflow when shell access is available:

```bash
_PMW_BIN=""
for _CANDIDATE in "$PWD/bin" "$PWD/pmworkspace-shared/bin" "$HOME/.codex/skills/pmworkspace-shared/bin"; do
  if [ -x "$_CANDIDATE/pmw-update-check" ]; then _PMW_BIN="$_CANDIDATE"; break; fi
done
if [ -n "$_PMW_BIN" ]; then
  _UPD=$("$_PMW_BIN/pmw-update-check" 2>/dev/null || true)
  [ -n "$_UPD" ] && echo "$_UPD"
  "$_PMW_BIN/pmw-log" usage pm-workspace >/dev/null 2>&1 || true
fi
```

If output contains `UPGRADE_AVAILABLE old new`, tell the user PMWorkspace has an update and offer to run `pmw-upgrade`. If `auto_upgrade` is `true`, upgrade automatically and say what changed only after upgrade succeeds.

## Workbench Routing

Route by the user's actual job:

- Raw idea, vague product request, "help me think", problem definition -> use `$pm-jobs`.
- Scope, ambition, strategic tradeoff, "think bigger", "is this worth doing" -> use `$pm-strategy-review`.
- Need an editable product brief, Zoon alignment, or decision record -> use `$pm-brief`.
- Need prototype directions, image-2 mockups, multiple schemes, screenshot revision -> use `$pm-prototype-shotgun`.
- Need PRD-ready, design-ready, experiment-ready, or engineering handoff -> use `$pm-handoff`.

When unsure, start with `$pm-jobs`; product clarity comes before prototype output.

## Welcome And First Run

If the user invokes `$pm-workspace` with no concrete product task, asks what PMWorkspace does, or has just installed it, read `../pmworkspace-shared/references/welcome-guide.md` and give the welcome message plus the first choice menu.

Do not make the user guess the command set. The first response should feel like an app onboarding screen: short orientation, clear paths, and one recommended next step.

If the user provides a product task in the same message, skip the welcome menu and route directly.

## Operating Rules

- Product brief alignment is required before any image prompt or image generation.
- Default prototype canvas is mobile-first: iPhone 17 portrait `402 x 874`.
- Use desktop only when the user explicitly asks, or when dashboard/internal-tool work clearly needs a large workspace.
- One scheme plus one screen equals one image output. Do not create comparison collages unless the user asks for a presentation board.
- Save durable assets when a platform script is available: usage logs, decisions, brief markdown, prototype manifests, and taste feedback.
- Never save real tokens, private customer data, internal recordings, sensitive screenshots, or unredacted Zoon content in local assets.

## First-Use Message

For a new user or new project, briefly explain:

```text
PMWorkspace works like a product team before design: pm-jobs defines the real problem, strategy review challenges the direction, pm-brief records the product contract, prototype-shotgun explores mobile-first image-2 schemes, and pm-handoff turns the chosen path into a reusable delivery artifact.
```

Then route to the smallest useful next skill.

## Shared References

Use `../pmworkspace-shared/references/` for:

- `welcome-guide.md` for install success and first-run onboarding.
- `routing.md` for route selection.
- `state-and-telemetry.md` for durable asset rules.
- `update-workflow.md` for update prompts.
- Existing product references for gates, methods, prompt templates, AutoDesign, Zoon, and QA.

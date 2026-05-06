---
name: pm-prototype-shotgun
description: |
  PMWorkspace mobile-first prototype exploration. Use when the user wants image-2 UI
  mockups, multiple product directions, screenshot revision, design schemes, mobile
  app prototypes, forms, result pages, dashboards, internal tools, transaction flows,
  content/community screens, or prototype QA. Requires an Aligned brief and outputs
  one separate image per scheme and screen.
---

# PM Prototype Shotgun

Generate prototype schemes only after product alignment. This is product strategy made visible, not visual skin exploration.

## Preamble

Run platform checks and log usage:

```bash
_PMW_BIN=""
for _CANDIDATE in "$PWD/bin" "$PWD/pmworkspace-shared/bin" "$HOME/.codex/skills/pmworkspace-shared/bin"; do
  if [ -x "$_CANDIDATE/pmw-log" ]; then _PMW_BIN="$_CANDIDATE"; break; fi
done
[ -n "$_PMW_BIN" ] && "$_PMW_BIN/pmw-update-check" 2>/dev/null || true
[ -n "$_PMW_BIN" ] && "$_PMW_BIN/pmw-log" usage pm-prototype-shotgun >/dev/null 2>&1 || true
```

## Hard Gates

- Read `../pmworkspace-shared/references/image-prompts.md`.
- Do not write prompts or generate images unless the brief is `Aligned`.
- Existing-feature iterations require current screenshots or equivalent visual baseline.
- Confirm concept directions before multi-scheme generation unless the user explicitly approved defaults.
- Default to mobile-first iPhone 17 portrait `402 x 874`.
- Use desktop only when explicitly requested or when dashboard/internal-tool density requires it.

## Multi-Scheme Rules

- Directions must differ by product strategy, information architecture, interaction model, or trust model.
- One scheme plus one screen equals one image output.
- `3 directions x 2 screens` means six independent images.
- Do not create collages or comparison boards unless the user asks for presentation material.

## Workflow

1. Read aligned brief and scenario route.
2. Read `design-system-workflow.md`, `design-heuristics.md`, and `adversarial-review.md` as needed.
3. Propose concept directions with names and tradeoffs.
4. For each image output unit, declare scheme, screen, canvas, and brief dependency.
5. Generate with image-2 / image generation.
6. Run `prototype-quality-review.md`.
7. Save a prototype manifest with `pmw-log prototype <batch>` when platform scripts are available.
8. Record approved/rejected design feedback with `pmw-log taste`.

## Output

```text
Prototype plan / handoff:
- Brief:
- Scenario:
- Canvas:
- Images produced or planned:
- QA status:
- Saved manifest:
- Taste feedback:
- Next skill:
```

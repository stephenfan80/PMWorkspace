# Prototype Quality Review

Use this after each image generation batch and before the final response. The goal is to catch beautiful but unusable prototype output.

## Review The Image Against The Brief

Check:

- Does the screen match the aligned product brief and scenario route?
- Does it honor the mobile-first canvas decision, or clearly justify desktop?
- Does it solve the stated user task?
- Does it optimize the primary goal without violating the counter-metric?
- Does it preserve required elements from the current baseline for existing-feature iteration?
- Does it avoid unsupported functions, fake data, fake buttons, or impossible promises?
- Does it make estimates, uncertainty, eligibility, or human follow-up honest?

## Review The Image Against AutoDesign

AutoDesign is the default production baseline. Check:

- Primary blue, commercial orange, text colors, dividers, and background are plausible.
- Typography uses production-like Chinese UI hierarchy.
- Layout uses 8-point structure and 4-point detail rhythm.
- Buttons, forms, NavBar, cards, tags, result modules, and bottom bars look shippable.
- There is one dominant primary action unless comparison is the point.
- No excessive gradients, over-rounded cards, heavy shadows, decorative filler, or marketing-poster layout.
- No overlapping text, cramped rows, broken alignment, distorted assets, or unreadable numbers.

## Review Multi-Scheme Work

- Schemes must differ by product strategy or information architecture, not only color.
- Each scheme should have a clear name and tradeoff.
- Each scheme/screen must be delivered as its own image, not merged into a collage or comparison board.
- Form/result pairs must share data, tone, and visual system.
- If a scheme repeats another with minor cosmetic changes, revise the weaker concept.

## If The Prototype Fails

If a failure is material:

1. Name the failure briefly.
2. Revise the prompt using the aligned brief.
3. Regenerate the affected screen only.
4. Do not ask the user to accept a prototype that violates feasibility, trust, or design-system quality.

## Handoff Manifest

After acceptable images are produced, keep the final note compact:

```text
Prototype handoff:
- Brief source:
- Brief version/status:
- Scenario route:
- Screens produced:
- Concept direction:
- QA status:
- Key assumptions:
- Not invented:
- PM decisions remaining:
```

Keep the handoff focused on what another PM, designer, or agent needs to continue the work. Do not include long rationale unless the user asks for it.

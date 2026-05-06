# Design System Workflow

Use this reference before generating prototype images. AutoDesign is the default production-quality visual baseline for PMWorkspace. A user-provided design system, Figma, screenshot, or brand rule can supersede specific visual details, but the output should still feel production-ready.

## Detect The Design System

Load a design-system profile when:

- The task reaches prototype generation; default to AutoDesign production baseline.
- The user names a brand or system, such as AutoDesign, 汽车之家, 之家, or Autohome.
- The user asks for production-ready, design-system-compliant, or component-aligned prototypes.
- The user provides design-system URLs, screenshots, Figma links, or existing product screenshots.

Read `autohome-auto-design.md` by default for production baseline tokens, spacing, components, and anti-patterns. For non-Autohome products, use AutoDesign as a quality baseline, not as brand copy or domain content.

## Acquire Context

Use the most reliable available source:

1. User-provided screenshot or design file.
2. Accessible design-system page via browser inspection.
3. Local AutoDesign reference profile.
4. User-provided verbal rules.

If a page is accessible only in the user's browser session, inspect it with browser tools and summarize only the reusable rules. Do not paste full internal docs into generated open-source artifacts.

## Build A Design Constraint Summary

Before writing an image prompt, create a compact constraint summary:

```text
Design system: <name>
Baseline role: <default production baseline / explicit brand system / screenshot source of truth>
Canvas/device: <size>
Colors: <primary, accent, text, background, border>
Typography: <font family, size scale, weight rules>
Grid/spacing: <grid and common spacing>
Components: <NavBar, Button, Form, ToolBar, cards, result modules>
Do not: <known anti-patterns>
```

For image prompts, paste the constraint summary into the `Visual requirements` section.

Default canvas is mobile-first iPhone 17 portrait `402 x 874`. Choose desktop only when the user explicitly asks or the scenario is a dashboard/internal tool that would be materially worse on mobile.

## Production Design Review

Run this review before final image generation:

- Does the design use the named system's tokens rather than invented colors?
- If AutoDesign is only a quality baseline, does the screen avoid pretending to be an Autohome domain product unless the product is Autohome?
- Are components named and shaped like the system's components?
- Are text sizes plausible for the target device?
- Are labels, buttons, and warnings short enough for production UI?
- Is there one dominant primary action?
- Are optional inputs moved out of the first step when conversion is the goal?
- Are result pages fulfilling value rather than repeating the form?
- Is there any decorative filler that would not ship?
- Are there overlapping text, cramped rows, or distorted assets?

## Scheme Design

When producing multiple schemes, vary the product strategy, not just visual styling:

- Scheme A: preview-first value before input.
- Scheme B: input-first but ultra-light conversion.
- Scheme C: comparison/report/result-driven structure.

Keep the same design-system tokens across schemes unless the user asks for visual exploration.

## Iteration Rules

When the user annotates a screenshot:

- Red boxes usually mean remove, reduce, or move away from the current page.
- Green boxes usually mean preserve, simplify, or strengthen.
- Keep the accepted visual system intact.
- Only redesign unrelated sections when the requested change would otherwise break hierarchy or fit.

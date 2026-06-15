---
name: product-agent-prototype
description: Use when the user needs mobile-first image-2 prototype directions, multiple product schemes, or screenshot-based prototype revisions after a product brief is aligned.
---

# product-agent-prototype

Plan prototype directions from an aligned brief.

## Read first

1. `../product-agent-shared/references/language-and-localization.md`
2. `../product-agent-shared/references/product-agent-readiness.md`
3. `../product-agent-shared/references/product-agent-gotchas.md`
4. `../product-agent-shared/references/artifact-flow.md`

## Inputs

- Aligned `product_brief`.
- Visual baseline or explicit non-applicable baseline.
- Desired scheme count and screen task.

## Outputs

- One output unit per scheme and screen.
- Scheme name, screen task, goal, counter-metric, non-fiction boundary.
- Image-2 prompt only after readiness passes.

## Gotchas

- No aligned brief, no prompt.
- If image-2 is unavailable, do not fall back to HTML.
- Multiple schemes must differ by product logic, not visual style only.
- One image equals one scheme and one screen task.

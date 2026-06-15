# product_agent readiness

Readiness checks prevent premature generation and delivery.

## Prototype readiness

Prototype work is allowed only when:

- `product_brief` is aligned for the current input.
- Visual baseline is available or explicitly not applicable.
- Scheme differences are product-level, not visual-only.
- Non-fiction boundaries and counter-metrics are known.
- The requested output is image-2, unless the user explicitly asks for HTML or frontend implementation.

If any item fails, return the first blocker in product language.

## Handoff readiness

Handoff work is allowed only when:

- The brief is aligned.
- Prototype-dependent handoff has a passed or explicitly accepted review.
- Scope-changing decisions are captured.
- Unknown interface, data, tracking, or experiment items stay blank as `待补充`.

If readiness fails, do not write a PRD that implies false certainty.

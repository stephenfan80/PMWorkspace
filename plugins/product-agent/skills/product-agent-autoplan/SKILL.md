---
name: product-agent-autoplan
description: Use when the user asks product_agent to automatically run the recommended product review, move from rough idea toward brief/prototype/handoff, or proceed by recommendation while stopping for direction-changing decisions.
---

# product-agent-autoplan

Drive the product-agent chain while stopping at the first real gate.

## Read first

1. `../product-agent-shared/references/language-and-localization.md`
2. `../product-agent-shared/references/product-agent-routing.md`
3. `../product-agent-shared/references/product-agent-readiness.md`
4. `../product-agent-shared/references/product-agent-gotchas.md`

## Behavior

- Start from the earliest missing gate.
- Recommend the next capability.
- Ask only for decisions that materially change direction, scope, promise, or delivery.

## Output

- 自动评审结论
- 当前最早门槛
- 建议下一步
- 当前 Q 或 D

## Gotchas

- Autoplan is not permission to skip gates.
- If brief readiness fails, stop before prototype.
- If handoff readiness fails, stop before PRD or delivery claims.

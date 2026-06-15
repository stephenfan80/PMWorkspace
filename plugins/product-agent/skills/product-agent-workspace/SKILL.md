---
name: product-agent-workspace
description: Use when the user has product material but is not sure where to start, asks how to move a product idea forward, provides mixed screenshots/PRD/feedback, or needs product_agent to route the task before brief, prototype, review, or handoff work.
---

# product-agent-workspace

Main entry and routing skill.

## Read first

1. `../product-agent-shared/references/language-and-localization.md`
2. `../product-agent-shared/references/product-agent-routing.md`
3. `../product-agent-shared/references/product-agent-gotchas.md`
4. `../product-agent-shared/references/artifact-flow.md`

## Use this when

- The user is unsure whether they need problem definition, brief, prototype, review, or handoff.
- The input mixes ideas, screenshots, PRD notes, feedback, or business goals.
- A downstream request may be premature and needs a readiness check.

## Do not use this when

- The user explicitly asks to edit code, docs, packaging, or evals in this repository.
- A specific product-agent skill is already clearly requested and its gate is satisfied.

## Output

Give a short work card:

- 当前动作
- 当前判断
- 当前最早门槛
- 需要用户补什么
- 补齐后解锁
- 下一 skill

## Gotchas

- Do not direct prototype or handoff work before brief alignment.
- Do not treat screenshots as permission to generate a full solution.
- If intent is unclear, route to the earliest useful capability, not the most impressive output.

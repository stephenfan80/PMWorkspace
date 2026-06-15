# AGENTS

This file is for agents working in this repository. Keep it short: use it to decide what context to load, what not to touch, and where product_agent guidance lives.

## Repository Context

- This repository maintains the `product_agent` skill suite.
- The public product is `product_agent`; do not introduce legacy product names or legacy command prefixes.
- Do not infer that every task needs the full product workflow. For simple docs, script, eval, packaging, or cleanup tasks, inspect only the relevant files.

## What To Read

- For user-facing behavior, read [docs/product-agent-usage.md](docs/product-agent-usage.md).
- For routing or capability boundaries, read [docs/product-agent-capability-map.md](docs/product-agent-capability-map.md) and [product-agent-shared/references/product-agent-routing.md](product-agent-shared/references/product-agent-routing.md).
- For a specific skill change, read that skill's `SKILL.md` first, then only the directly referenced shared files needed for the change.
- For eval changes, read [product-agent-shared/references/product-agent-eval-system.md](product-agent-shared/references/product-agent-eval-system.md), then the target fixture or suite.
- For packaging changes, read [docs/codex-plugin-submission.md](docs/codex-plugin-submission.md) and `bin/product-agent-build-plugin`.

## Working Rules

- Default to Chinese for user-facing product explanations and project docs unless the surrounding file is clearly English.
- Explain product-impacting bugs in product language: name the product bias, user misunderstanding, review risk, or delivery risk.
- Keep changes surgical. Do not broaden the workflow or add stages unless the user explicitly asks.
- Do not write real tokens, private screenshots, internal recordings, customer data, or unredacted collaboration-doc content into the repository.
- Keep skill entry files compact. Put heavy references, cases, templates, schemas, assets, scripts, and eval fixtures in their dedicated folders.
- If user intent conflicts with current docs, follow the latest explicit user instruction and update the relevant docs.

## Verification

- For docs-only changes, reread edited sections and check for contradictory routing.
- For skill behavior changes, add or update focused eval fixtures.
- For script changes, run the narrowest relevant command before reporting completion.

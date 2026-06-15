# product_agent

[中文文档](README.zh-CN.md)

`product_agent` is a product capability skill suite. It turns product ideas, screenshots, PRDs, interviews, support notes, and domain knowledge into aligned product briefs, mobile-first prototype directions, prototype reviews, and compact handoff assets.

The workflow is intentionally simple:

```text
Align -> Prototype -> Review -> Deliver
```

`product_agent` is not a prompt pack or a prototype generator. It packages product judgment, workflow, tools, templates, and failure boundaries into reusable agent capabilities.

## Start

Use the main entry skill:

```text
Use product-agent-workspace to help me move this product idea forward: <idea / screenshot / PRD / feedback>
```

If the task is already specific, call the matching capability:

| Need | Skill |
|---|---|
| Not sure where to start | `product-agent-workspace` |
| Clarify whether an idea is worth doing | `product-agent-problem` |
| Let the agent drive the whole review but stop for key decisions | `product-agent-autoplan` |
| Challenge scope, risk, and value exchange | `product-agent-strategy-review` |
| Create or update the product brief | `product-agent-brief` |
| Generate mobile-first image-2 prototype directions | `product-agent-prototype` |
| Review generated prototype images | `product-agent-prototype-review` |
| Produce a compact PRD or handoff asset | `product-agent-handoff` |

## Core Gates

- An aligned `product_brief` is required before image prompts, image generation, or delivery.
- A direction choice does not equal brief alignment.
- Screenshots and online references update evidence only; they do not automatically authorize a full plan or prototype.
- Existing-feature iteration needs a current screenshot, URL, design file, or equivalent visual baseline before prototype work.
- HTML is allowed only when the user explicitly requests an interactive web or frontend prototype.
- Multi-scheme prototype work must differ by product strategy, information architecture, interaction model, trust model, or task path, not just visual style.

## Install From This Repository

```bash
bin/product-agent-build-plugin
bin/product-agent-upgrade --host codex
```

The installer writes skills to the configured Codex skills directory and uses `~/.product_agent/` for local state.

## Maintainer Commands

```bash
bin/product-agent-operation-router classify --text "<user request>"
bin/product-agent-controller next --json
bin/product-agent-dashboard status
bin/product-agent-eval run --suite smoke
bin/product-agent-gen-skill-docs check
bin/product-agent-build-plugin
```

More usage guidance lives in [docs/product-agent-usage.md](docs/product-agent-usage.md), and the internal capability map lives in [docs/product-agent-capability-map.md](docs/product-agent-capability-map.md).

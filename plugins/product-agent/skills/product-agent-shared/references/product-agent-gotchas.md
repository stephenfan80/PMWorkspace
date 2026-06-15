# product_agent gotchas

These are high-value failure boundaries. They come from repeated product-agent mistakes and should be encoded in skills and evals.

- Direction choice is not brief alignment. “按 A 继续” only selects a direction.
- Screenshots and online references update evidence only. They do not automatically authorize a full plan, HTML, prompt, or image.
- A locked, aligned `product_brief` is required before image prompts, image generation, or delivery.
- If image-2 is unavailable, do not silently fall back to HTML.
- Multiple prototype schemes must differ by product strategy, information architecture, interaction model, trust model, or task path, not color only.
- Prototype images must not show unconfirmed product capabilities as if they already exist.
- Handoff docs must not invent interfaces, tracking events, data sources, experiment standards, acceptance criteria, or legal/compliance decisions.
- Memory, preference, or prior examples cannot override current user facts, screenshots, brief, counter-metrics, or non-fiction boundaries.
- If new evidence changes scope, promise, target user, or data truth, return to brief alignment.

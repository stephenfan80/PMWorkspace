# product_agent artifact flow

`product_agent` persists product assets under `~/.product_agent/`.

Core asset kinds:

- `product_brief`
- `visual_baseline`
- `prototype_manifest`
- `prototype_review`
- `handoff`

Use `bin/product-agent-artifact add --kind <kind> --title <title> --summary <summary>` to record a simple asset. Use `bin/product-agent-artifact list` to inspect assets.

Do not store secrets, private screenshots, raw recordings, customer data, or unredacted collaboration content.

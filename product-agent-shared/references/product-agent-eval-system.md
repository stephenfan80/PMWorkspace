# product_agent eval system

Evals are lightweight JSON fixtures for the deterministic product_agent classifier. They guard routing, operation type, and shallow boundary signals; they are not a full replacement for LLM or human eval.

Suites:

- `smoke`: fastest public flow checks.
- `core`: routing, readiness, gotcha, and delivery checks.
- `full`: all fixtures.

Fixture shape:

```json
{
  "id": "fixture-id",
  "category": "routing|forbidden-load|gotcha",
  "prompt": "user request",
  "expected": {
    "route": "product-agent-brief",
    "operation_type": "brief_request",
    "must_not_route": ["product-agent-handoff"],
    "must_include_signals": ["needs_brief_alignment"],
    "must_exclude_signals": ["local_edit_only"],
    "must_not": ["legacy-token"]
  }
}
```

Run with:

```bash
bin/product-agent-eval run --suite smoke
bin/product-agent-eval run --fixture brief-alignment-before-prototype
bin/product-agent-eval sync
```

## Current Limits

- The harness validates deterministic keyword output from `classify_text`, not live agent tool selection.
- Signals such as `no_fake_interfaces` prove the boundary is detected, not that a future generated PRD contains no invented interface, tracking, or data-source detail.
- Deep gotchas need LLM eval, human review, or artifact inspection before release-grade claims.
- Route-only fixtures are intentionally weak regression checks; strengthen them with operation or signal assertions when a reliable deterministic signal exists.

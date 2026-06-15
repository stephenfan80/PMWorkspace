# product_agent evals

Run:

```bash
bin/product-agent-eval run --suite smoke
bin/product-agent-eval run --suite core
bin/product-agent-eval run --suite full
bin/product-agent-eval sync
```

Fixtures are deterministic classifier checks. They verify route choice, operation type, and shallow boundary signals such as `needs_brief_alignment`, `no_html_fallback`, `no_fake_interfaces`, and `needs_visual_baseline`.

Weak route-only fixtures still exist for broad regression coverage, for example the multi-scheme fixture that reminds maintainers that方案差异不能只靠换配色. Deep behavior such as whether a generated PRD truly avoids fake interfaces still needs LLM or human review.

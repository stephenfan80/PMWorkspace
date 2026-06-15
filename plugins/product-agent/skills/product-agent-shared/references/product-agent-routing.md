# product_agent routing

Route to the earliest useful capability. Do not jump downstream because the user asked for a final artifact.

## Public Actions

| Action | User intent | Default skill |
|---|---|---|
| 对齐 | Turn rough material into product judgment | `product-agent-workspace` or `product-agent-problem` |
| 原型 | Create image-2 prototype directions | `product-agent-prototype` |
| 复审 | Review prototype images | `product-agent-prototype-review` |
| 交付 | Produce product design docs or compact PRDs | `product-agent-handoff` |

## Operation Types

| Operation | Typical input | Route |
|---|---|---|
| `new_product_workflow` | “帮我做方案/原型/PRD” | `product-agent-workspace` |
| `answer_pending_gate` | “我选 A / 按这个假设继续” | current gate, no new intake |
| `attach_evidence` | “补一张截图 / URL / 数据” | update evidence, then earliest gate |
| `modify_brief` | “目标/范围/承诺改了” | `product-agent-brief` |
| `prototype_revision` | “基于这张图改这里” | `product-agent-prototype` with edit scope |
| `prototype_review` | “这张图能不能交付” | `product-agent-prototype-review` |
| `handoff_continue` | “整理成 PRD / 交付稿” | `product-agent-handoff` |

## Routing Rules

- If the problem is unclear, route to `product-agent-problem`.
- If the user wants the agent to drive the whole chain, route to `product-agent-autoplan`.
- If scope, risk, business promise, or value exchange is unstable, route to `product-agent-strategy-review`.
- If there is no aligned product brief, route to `product-agent-brief`.
- If prototype readiness fails, return to the first blocking gate.
- If handoff readiness fails, return to brief, review, or decision capture.
- For industry-specific work, load the matching file under `references/industries/` only when needed. Industry packs are references, not skills, and never create a separate default route.

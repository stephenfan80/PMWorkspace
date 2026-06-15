# product_agent 公开工具箱

普通用户只需要使用 8 个 skill。

| Skill | 用途 |
|---|---|
| `product-agent-workspace` | 主入口和路由 |
| `product-agent-problem` | 问题定义与价值判断 |
| `product-agent-autoplan` | 自动推进产品评审 |
| `product-agent-strategy-review` | 策略、范围和风险审查 |
| `product-agent-brief` | 产品简报 |
| `product-agent-prototype` | 多方案原型 |
| `product-agent-prototype-review` | 原型复审 |
| `product-agent-handoff` | 产品交付 |

维护者命令位于 `bin/product-agent-*`。常用命令：

```bash
bin/product-agent-operation-router classify --text "<用户请求>"
bin/product-agent-dashboard status
bin/product-agent-eval run --suite smoke
bin/product-agent-gen-skill-docs check
bin/product-agent-build-plugin
```

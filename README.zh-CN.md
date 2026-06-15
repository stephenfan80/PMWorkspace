# product_agent

`product_agent` 是产品能力 Skill 套件。它把产品想法、业务材料、截图、PRD、访谈 / 支持反馈和行业经验，推进为产品判断、产品简报、移动端优先原型方向、原型复审结论和交付文档。

核心链路：

```text
对齐 -> 原型 -> 复审 -> 交付
```

`product_agent` 不是提示词集合，也不是单纯原型生成器。它封装的是产品专家的判断、取舍、工作流、模板、工具和失败边界。

## 第一次使用

从主入口开始：

```text
使用 product-agent-workspace 帮我判断这个产品想法应该怎么推进：<一句话想法 / 截图 / PRD / 反馈>
```

如果意图已经很明确，可以直接使用对应能力：

| 你想做什么 | 使用哪个 skill |
|---|---|
| 不确定从哪里开始 | `product-agent-workspace` |
| 判断想法是否值得做 / 问题是否成立 | `product-agent-problem` |
| 希望 Agent 自动推进完整评审，但关键点让我拍板 | `product-agent-autoplan` |
| 挑战策略、范围、风险和价值交换 | `product-agent-strategy-review` |
| 生成或更新产品简报 | `product-agent-brief` |
| 做多方案 image-2 原型 | `product-agent-prototype` |
| 复审已生成原型图 | `product-agent-prototype-review` |
| 生成产品设计文档 / 精简 PRD / 交付稿 | `product-agent-handoff` |

## 关键门槛

- 产品简报未“已对齐”时，不写 image-2 提示词，不生成图片，不生成 HTML，不输出交付稿。
- 用户选择方案 A/B/C 或确认“按 A 继续”，只代表方向选择，不能替代产品简报对齐。
- 用户提供截图或线上参考时，只更新视觉基线和参考状态，不自动产出完整方案、HTML 或原型图。
- 已上线功能迭代必须先拿到当前生产截图、关键节点截图、线上页面 URL、Figma / 设计稿或等价视觉基线。
- HTML 只在用户明确要求“HTML / 可交互网页 / 前端实现 / 本地网页原型”时允许。
- 多方案必须在产品策略、信息架构、交互模型、信任模型或关键任务路径上有差异，不能只是换配色。

## 本地安装

```bash
bin/product-agent-build-plugin
bin/product-agent-upgrade --host codex
```

本地状态保存在 `~/.product_agent/`。不会自动读取或迁移旧状态。

## 维护者命令

```bash
bin/product-agent-operation-router classify --text "<用户请求>"
bin/product-agent-controller next --json
bin/product-agent-dashboard status
bin/product-agent-eval run --suite smoke
bin/product-agent-gen-skill-docs check
bin/product-agent-build-plugin
```

使用指南见 [docs/product-agent-usage.md](docs/product-agent-usage.md)，能力地图见 [docs/product-agent-capability-map.md](docs/product-agent-capability-map.md)。

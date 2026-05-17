# PMW 资产样例库

这些样例展示 PMWorkspace 如何把一个产品任务沉淀成连续的产品资产流：`product_brief` -> `visual_baseline` -> `prototype_manifest` -> `prototype_review` -> `handoff`。

样例不是运行协议，也不是模板生成器，更不是“原子库”。它们的作用是让用户和维护者快速看懂：PMW 为什么先对齐、怎样保留视觉基线、如何登记多方案原型、复审怎么影响重出或交付、最终 PRD 应该读取哪些上游事实。

长期最有价值的样例是真实匿名 / 脱敏资产：真实项目里的 `product_brief`、`visual_baseline`、`prototype_review` 和 `handoff`。当前公开仓库使用真实匿名风格的虚构脱敏内容做安全占位：字段、取舍、缺口和证据边界尽量接近真实产品工作流，但不包含真实客户、真实截图或内部数据。

## 完整资产流样例

| 样例 | 适合场景 | 重点资产 |
|---|---|---|
| [`asset-flows/01-new-idea/`](asset-flows/01-new-idea/) | 从一句新想法进入产品判断和多方案原型。 | 无生产截图时如何保留 `visual_baseline` 资产位，并说明参考基线不适用。 |
| [`asset-flows/02-existing-feature/`](asset-flows/02-existing-feature/) | 优化已上线页面或流程。 | 生产截图如何约束局部改动、合规入口和交付验收。 |
| [`asset-flows/03-screenshot-iteration/`](asset-flows/03-screenshot-iteration/) | 根据标注截图修改已生成或生产原型。 | 标注范围、局部重出、少于 3 方案豁免和产品承诺边界。 |
| [`asset-flows/04-prd-handoff/`](asset-flows/04-prd-handoff/) | 把已确认方向整理成精简 PRD / 研发交付稿。 | brief、baseline、manifest、review 如何被 PRD 逐条读取。 |

## 轻量场景配方

以下旧示例保留为“怎么开口 / 怎么描述场景”的配方，完整资产链路请优先看上面的 `asset-flows/`：

| 配方 | 适合场景 |
|---|---|
| [`new-feature-exploration.md`](new-feature-exploration.md) | UI 设计前验证新想法。 |
| [`existing-feature-iteration.md`](existing-feature-iteration.md) | 优化已上线屏幕或流程。 |
| [`conversion-flow.md`](conversion-flow.md) | 注册、留资、预约、付款或授权流程。 |
| [`dashboard.md`](dashboard.md) | 帮助角色监控、对比和决策。 |
| [`screenshot-feedback-iteration.md`](screenshot-feedback-iteration.md) | 修改已生成或生产截图。 |
| [`prompt-recipes.md`](prompt-recipes.md) | 用户不知道怎么发起任务时的可复制话术。 |

## 生成规则

- 默认移动端优先。
- 无线上截图时画布为 iPhone 17 竖屏 `402 x 874`。
- 有生产截图 / `visual_baseline` 时，以截图物理像素长板或截图编辑模式为准。
- 一个方案 + 一个屏幕 = 一张 image-2 图。
- 多方案任务输出多张图，不合成一张比较板。
- 产品简报未达到 `已对齐` 时，不写 image-2 提示词，不生成图片，不输出交付稿。

# Product Artifact Flow

PMWorkspace 产物流动层让每一步产物都能被下游技能读取，而不是只存在于对话里。产品简述 / 产品简报、原型清单、复审结论、最终产品设计文档和交付稿必须登记为下游可读产物。浏览器证据也以 `browser_evidence` 产物进入同一条 Product Artifact Flow。浏览器证据和视觉基线也进入同一条 Product Artifact Flow：`browser_evidence` 说明线上参考在哪里，`visual_baseline` 说明参考图如何转成可执行的尺寸、字号、间距和密度约束。

## 目标

- 把 `$pm-brief`、`$pm-prototype-shotgun`、`$pm-prototype-review`、`$pm-handoff` 的输出串成一条可追溯链路。
- 让下游技能先读取最近的上游产物，再决定是否继续、退回门槛或补证据。
- 让 `pmw-dashboard status --details` 展示准备度和产物流动；默认状态摘要只给业务结论，避免用户被零散文件路径和内部链路打扰。

## 产物链路

| 上游技能 | 登记产物 | 下游读取 | 用途 |
|---|---|---|---|
| `$pm-jobs` / `$pm-strategy-review` | `decision`、`strategy_review` | `$pm-brief` | 把事实、范围、策略取舍、PM 判断摘要、产品判断对抗校验和产品作业写进产品契约。 |
| `$pm-brief` | `product_brief` | `$pm-prototype-shotgun`、`$pm-handoff` | 作为出图前短版产品简述 / 产品简报真源，并保留真实问题、证据边界、PM 判断摘要、产品判断对抗校验和下一步产品作业。 |
| 浏览器 / 截图 / Zoon 检查 | `browser_evidence` | `$pm-brief`、`$pm-prototype-shotgun`、`$pm-prototype-review`、`$pm-handoff` | 记录线上流程截图、状态页、竞品参考、设计启发或 Zoon 漂移证据，支撑线上参考和设计规范目标门槛。 |
| 视觉基线 | `visual_baseline` | `$pm-brief`、`$pm-prototype-shotgun`、`$pm-prototype-review`、`$pm-handoff` | 记录参考图路径、像素尺寸、逻辑宽度推断、目标输出像素、核心字号层级、页面边距、模块间距、底部栏高度和参考优先级。 |
| `$pm-prototype-shotgun` | `prototype_manifest` | `$pm-prototype-review` | 绑定三条产品路径、方案、屏幕、主目标、反指标、不可虚构项和 brief 版本。 |
| `$pm-prototype-review` | `prototype_review`、`repair_brief` | `$pm-prototype-shotgun`、`$pm-handoff` | 决定可通过、需要重出、需要 PM 拍板或补参考，并保留原型可信度对抗复审结论。 |
| `$pm-handoff` | `product_design_doc` | `$pm-handoff`、后续评审、研发交付 | 汇总产品简述、产品判断对抗校验、三条产品路径、原型设计完整度、原型可信度对抗复审、信息架构思考、产品判断演进、推荐方案、风险和下一步，作为最终产品设计文档。 |
| `$pm-handoff` | `handoff`、`acceptance_seed`、`release_doc_seed` | `document-release`、`ship`、`qa` | 让文档同步、发布准备和 QA 不重新猜验收口径。 |

## 命令

```bash
pmw-artifact add \
  --kind product_brief \
  --title "<产物标题>" \
  --status "已对齐" \
  --source-skill pm-brief \
  --path "<本地文件>" \
  --url "<Zoon URL>" \
  --pm-judgment-summary "<真实问题、最大不确定性、最该验证和推荐推进>" \
  --product-homework "<访谈、补截图、拉数据、找竞品或确认不可承诺项>" \
  --upstream "decision,strategy_review" \
  --next-skill "pm-prototype-shotgun,pm-handoff"

pmw-artifact latest --kind product_brief
pmw-artifact latest --kind product_design_doc
pmw-artifact latest --kind browser_evidence
pmw-artifact latest --kind visual_baseline
pmw-artifact flow
pmw-artifact flow --details
pmw-dashboard status
pmw-dashboard status --details
```

`visual_baseline` 的最小摘要包含：参考图路径、参考像素尺寸、逻辑宽度推断、目标输出像素、核心字号层级、页面边距、模块间距、底部栏高度、参考优先级和不可压缩项。有线上截图时，视觉基线优先级高于泛化 AutoDesign token；缺视觉基线时，现有功能迭代不能写 image-2 prompt。

设计启发不新增 artifact 类型：Dribbble、Pinterest、公开参考页、平台模式或用户自有截图的启发统一登记为 `browser_evidence`，摘要必须写清 `设计启发`、可复用模式、不可照搬项和版权边界。它只能帮助确定设计规范目标和 prompt 约束，不能覆盖产品简报、线上截图、反指标或不可虚构项。

`PM 判断摘要`、`产品作业`、`产品判断对抗校验` 和 `原型可信度对抗复审` 不新增独立 artifact 类型：它们写入 `decision`、`strategy_review`、`product_brief`、`prototype_manifest`、`prototype_review` 或 `product_design_doc` 的摘要字段和本地审计；其中 `PM 判断摘要` / `产品作业` 继续使用 `pm_judgment_summary` / `product_homework` 结构化字段。`pmw-artifact add` 支持 `--pm-judgment-summary` 和 `--product-homework`；`pmw-log brief` / `pmw-log handoff` 会优先使用显式参数，缺省时从 Markdown 的对应章节提取。禁止新增独立“产品方案文档”或“产品思考账本”作为核心产物，避免产物流膨胀。

`prototype_manifest` 的每个方案单元必须能说明它代表的产品路径：相信什么用户行为、要赢过哪个现状替代、解决什么当前损失、主动删除 / 牺牲 / 后置什么、验证信号、失败信号、保护哪个反指标、哪些内容不可虚构。三条路径比较的目标是帮助 PM 做产品取舍，不是比较视觉皮肤。

可用 `pmw-image-audit baseline --reference <截图路径> --register` 从参考图生成并登记视觉基线；出图后用 `pmw-image-audit audit --image <生成图> --reference <参考图>` 做尺寸 / 长板复审。

`pmw-log brief`、`pmw-log prototype` 和 `pmw-log handoff` 会自动写入 `artifact-flow.jsonl`；手动命令只用于额外产物、修复 brief、验收种子或文档同步种子。

## 技能要求

- 每个下游技能开始时，优先读取 `pmw-artifact flow --details` 或 `pmw-artifact latest --kind <产物类型>`。
- `上游产物`、`本轮产物`、`下游可读`、`产物流动` 和 `下一技能` 是内部审计 / 交接字段，必须写入本地状态并供下游读取，但默认不输出给用户。
- 用户可见输出只在需要时说明“已保存 / 已同步 / 可继续”，用户明确要求“看状态 / 看审计 / 展开产物流动”时才展示完整表格。
- 当最新上游产物缺失、过期、未通过准备度或与 Zoon 漂移冲突时，不能假装可以继续下游交付；必须退回最早能修复的技能。
- 产物流动只登记元数据、路径、Zoon URL、状态和摘要；不要把完整私密 brief、客户资料、token、ownerSecret、Authorization header、API key、cookie、未脱敏截图内容或内部 PRD 正文写进公开仓库。

## 状态

- `未记录`：没有 `artifact-flow.jsonl` 或没有当前类型产物。
- `已记录`：产物有本地路径或 URL，但尚未声明下游。
- `下游可读`：产物有来源技能、状态、位置和下一技能。
- `有断点`：缺上游产物、产物状态失败、Zoon 有实质漂移，或下游所需字段不完整。

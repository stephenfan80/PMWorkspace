# Product Artifact Flow

PMWorkspace 产物流动层让每一步产物都能被下游技能读取，而不是只存在于对话里。产品简述 / 产品简报、原型清单、复审结论、最终产品设计文档和交付稿必须登记为下游可读产物。浏览器证据也以 `browser_evidence` 产物进入同一条 Product Artifact Flow。浏览器证据和视觉基线也进入同一条 Product Artifact Flow：`browser_evidence` 说明线上参考在哪里，`visual_baseline` 说明参考图如何转成可执行的尺寸、字号、间距和密度约束。

## 目标

- 把 `$pm-brief`、`$pm-prototype-shotgun`、`$pm-prototype-review`、`$pm-handoff` 的输出串成一条可追溯链路。
- 让下游技能先读取最近的上游产物，再决定是否继续、退回门槛或补证据。
- 让 `pmw-dashboard status --details` 展示准备度和产物流动；默认状态摘要只给业务结论，避免用户被零散文件路径和内部链路打扰。

## 产物链路

| 上游技能 | 登记产物 | 下游读取 | 用途 |
|---|---|---|---|
| `$pm-jobs` / `$pm-strategy-review` | `decision`、`strategy_review` | `$pm-brief` | 把事实、范围、策略取舍写进产品契约。 |
| `$pm-brief` | `product_brief` | `$pm-prototype-shotgun`、`$pm-handoff` | 作为出图前短版产品简述 / 产品简报真源。 |
| 浏览器 / 截图 / Zoon 检查 | `browser_evidence` | `$pm-brief`、`$pm-prototype-shotgun`、`$pm-prototype-review`、`$pm-handoff` | 记录线上流程截图、状态页、竞品参考或 Zoon 漂移证据，支撑线上参考门槛。 |
| 视觉基线 | `visual_baseline` | `$pm-brief`、`$pm-prototype-shotgun`、`$pm-prototype-review`、`$pm-handoff` | 记录参考图路径、像素尺寸、逻辑宽度推断、目标输出像素、核心字号层级、页面边距、模块间距、底部栏高度和参考优先级。 |
| `$pm-prototype-shotgun` | `prototype_manifest` | `$pm-prototype-review` | 绑定方案、屏幕、主目标、反指标、不可虚构项和 brief 版本。 |
| `$pm-prototype-review` | `prototype_review`、`repair_brief` | `$pm-prototype-shotgun`、`$pm-handoff` | 决定可通过、需要重出、需要 PM 拍板或补参考。 |
| `$pm-handoff` | `product_design_doc` | `$pm-handoff`、后续评审、研发交付 | 汇总产品简述、三方案原型、信息架构思考、推荐方案、风险和下一步，作为最终产品设计文档。 |
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

# Product Artifact Flow

PMWorkspace 产物流动层让每一步产物都能被下游技能读取，而不是只存在于对话里。产品简报、原型清单、复审结论和交付稿必须登记为下游可读产物。浏览器证据也以 `browser_evidence` 产物进入同一条 Product Artifact Flow。

## 目标

- 把 `$pm-brief`、`$pm-prototype-shotgun`、`$pm-prototype-review`、`$pm-handoff` 的输出串成一条可追溯链路。
- 让下游技能先读取最近的上游产物，再决定是否继续、退回门槛或补证据。
- 让 `pmw-dashboard status` 同时展示准备度和产物流动，避免用户只看到零散文件路径。

## 产物链路

| 上游技能 | 登记产物 | 下游读取 | 用途 |
|---|---|---|---|
| `$pm-jobs` / `$pm-strategy-review` | `decision`、`strategy_review` | `$pm-brief` | 把事实、范围、策略取舍写进产品契约。 |
| `$pm-brief` | `product_brief` | `$pm-prototype-shotgun`、`$pm-handoff` | 作为原型、复审和交付的产品真源。 |
| 浏览器 / 截图 / Zoon 检查 | `browser_evidence` | `$pm-brief`、`$pm-prototype-shotgun`、`$pm-prototype-review`、`$pm-handoff` | 记录线上流程截图、状态页、竞品参考或 Zoon 漂移证据，支撑线上参考门槛。 |
| `$pm-prototype-shotgun` | `prototype_manifest` | `$pm-prototype-review` | 绑定方案、屏幕、主目标、反指标、不可虚构项和 brief 版本。 |
| `$pm-prototype-review` | `prototype_review`、`repair_brief` | `$pm-prototype-shotgun`、`$pm-handoff` | 决定可通过、需要重出、需要 PM 拍板或补参考。 |
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
pmw-artifact latest --kind browser_evidence
pmw-artifact flow
pmw-dashboard status
```

`pmw-log brief`、`pmw-log prototype` 和 `pmw-log handoff` 会自动写入 `artifact-flow.jsonl`；手动命令只用于额外产物、修复 brief、验收种子或文档同步种子。

## 技能要求

- 每个下游技能开始时，优先读取 `pmw-artifact flow` 或 `pmw-artifact latest --kind <产物类型>`。
- 用户可见输出必须包含 `上游产物`、`本轮产物`、`下游可读`、`产物流动` 和 `下一技能`。
- 当最新上游产物缺失、过期、未通过准备度或与 Zoon 漂移冲突时，不能假装可以继续下游交付；必须退回最早能修复的技能。
- 产物流动只登记元数据、路径、Zoon URL、状态和摘要；不要把完整私密 brief、客户资料、token、ownerSecret、Authorization header、API key、cookie、未脱敏截图内容或内部 PRD 正文写进公开仓库。

## 状态

- `未记录`：没有 `artifact-flow.jsonl` 或没有当前类型产物。
- `已记录`：产物有本地路径或 URL，但尚未声明下游。
- `下游可读`：产物有来源技能、状态、位置和下一技能。
- `有断点`：缺上游产物、产物状态失败、Zoon 有实质漂移，或下游所需字段不完整。

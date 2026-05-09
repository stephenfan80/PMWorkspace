# Product Readiness Dashboard

Product Readiness Dashboard 是 PMWorkspace 的出图 / 交付前总控面板。它借鉴 gstack Review Readiness Dashboard 的做法：不是把证据散列成清单，而是用 `Required`、`状态`、`证据`、`行动` 和 `Verdict` 统一判断现在能不能继续。

## 使用时机

- `$pm-autoplan` 推进到原型准备度或交付准备度时。
- `$pm-prototype-shotgun` 写 image-2 提示词或调用 image-2 前。
- `$pm-handoff` 输出 PRD、设计交付、实验方案或研发验收前。
- `$pm-brief` 准备把下一技能指向 `$pm-prototype-shotgun` 或 `$pm-handoff` 时。

平台脚本可用时优先运行：

```bash
pmw-dashboard readiness --target prototype
pmw-dashboard readiness --target handoff
pmw-dashboard status
```

`pmw-dashboard status` 默认输出简洁状态摘要，`pmw-dashboard status --details` 才内嵌完整 `PMWorkspace 产品准备度仪表盘`，避免用户只看到后台证据表。

## 固定门槛

仪表盘至少展示以下门槛：

| 门槛 | 出图前 | 交付前 | 判断 |
|---|---|---|---|
| 产品简报 | Required | Required | 必须是 `已对齐`，且没有缺失门槛或实质漂移。 |
| 产品简报确认 | Required | Required | 当前 run 必须记录用户确认产品简报或关键前提；不能只凭 Markdown 中出现 `已对齐` 放行。 |
| Zoon | Conditional | Conditional | 未启用时使用本地已对齐 Markdown，不阻断出图 / 交付；已启用、已有 URL 或用户选择在线协作时，必须已同步且无实质漂移。 |
| 线上参考 | Required | Required | 已提供线上参考、已确认无线上参考，或明确不适用；未判断时不继续。优先读取最新 `browser_evidence` 产物，没有时回退到 run evidence / gate 事件。 |
| 视觉基线 | Conditional | Conditional | 已采集线上截图或生产视觉参考时必须登记 `visual_baseline`，包含参考尺寸和目标输出像素；缺视觉基线或缺目标像素时不写 image-2 prompt。新概念页且用户确认无参考时显示不适用。 |
| 输出单元绑定 | Conditional | Conditional | 已登记 prototype-board 输出单元时，`brief_path` 和 `brief_version` 必须等于当前 latest brief；旧 brief 版本的输出单元不能放行出图。 |
| 输出画布 | Conditional | Conditional | 有 `visual_baseline` 时，当前 run 的 prototype-board 输出单元必须写 `canvas_mode=physical_longboard` 和 `target_output_pixels`，且不得含 `H874` / `标准首屏` 锚点。 |
| 方案差异 | Required | Required | 多方案必须在页面结构、信息架构、交互路径、信任表达或关键任务上不同；单方案也要标注不适用或已登记。 |
| 方案方向确认 | Required | Required | 当前 run 必须记录用户已确认或批准默认方案方向；未确认时不写 image-2 prompt。 |
| 不可虚构项 | Required | Required | 必须明确不能展示的能力、数据、承诺或动作。 |
| 数据佐证 | no | no | 有数据时登记 `data_evidence`；没有数据时不阻断，但必须提示 `未提供，存在未验证风险`，并把风险写入 brief 与原型不可虚构项。 |
| 原型图片审计 | Conditional | Conditional | 出图后若 `pmw-prototype-board image` 或 `pmw-image-audit` 返回 `需要重出`，该图不能作为交付结果展示，必须重出。 |
| 复审状态 | no | Required | 出图前展示但不阻断；交付前必须是 `可通过`，不能有需要重出、PM 拍板或补参考项。 |

可以追加 `待决策项`、`设计系统`、`交付资产` 等行，但不能省略以上固定行。

## Verdict 规则

- `READY_FOR_PROTOTYPE / 可出图`：产品简报、产品简报确认、线上参考、必要的视觉基线、方案差异、方案方向确认和不可虚构项都通过；Zoon 未启用时使用本地简报，已启用时必须同步且无漂移；数据佐证缺失只提示未验证风险；复审状态仅展示，不阻断出图。
- `READY_FOR_HANDOFF / 可交付`：出图前门槛全部通过，且原型复审为 `可通过`，关键 D 已拍板，交付缺口不会改变承诺或验收。
- `NOT_READY / 不可出图 / 不可交付`：任一 required 行未通过。输出必须给出第一条阻断行的行动建议，并路由到能补齐它的最早技能。

## 默认输出契约

默认用户可见输出只给结论和下一步，不展示完整门槛表：

```text
产品准备度：
- 目标：<出图前 / 交付前>
- 结论：<可出图 / 不可出图 / 可交付 / 不可交付>
- 原因：<关键门槛已通过 / 第一条阻断门槛的人话原因>
- 下一步：<继续 / 补截图 / 回到产品简报 / 先复审>
```

完整门槛表属于内部审计输出。用户明确要求“看状态 / 看审计 / 调试 / 展开证据”时，或开发者运行 `pmw-dashboard readiness --details` 时才展示。

## 详细输出契约

详细输出使用中文字段：

```text
PMWorkspace 产品准备度仪表盘：
- 目标：<出图前 / 交付前>
- 当前 run：
- Verdict：<可出图 / 不可出图 / 可交付 / 不可交付>
- 下一步：

| 门槛 | Required | 状态 | 证据 | 行动 |
|---|---|---|---|---|
| 产品简报 | YES | ... | ... | ... |
| 产品简报确认 | YES | ... | ... | ... |
| Zoon | YES/no | ... | ... | ... |
| 线上参考 | YES | ... | ... | ... |
| 视觉基线 | YES/no | ... | ... | ... |
| 输出单元绑定 | YES/no | ... | ... | ... |
| 输出画布 | YES/no | ... | ... | ... |
| 方案差异 | YES | ... | ... | ... |
| 方案方向确认 | YES | ... | ... | ... |
| 不可虚构项 | YES | ... | ... | ... |
| 数据佐证 | no | ... | ... | ... |
| 原型图片审计 | YES/no | ... | ... | ... |
| 复审状态 | YES/no | ... | ... | ... |
```

如果仪表盘显示缺口，不要用图片、PRD 或“后续补充”绕过。默认输出只说第一条阻断原因和下一步；内部审计记录完整表格。把缺口转成一个 `Q`、一个 `D`，或退回 `$pm-brief`、`$pm-prototype-shotgun`、`$pm-prototype-review`、`$pm-handoff` 中最早能修复的技能。

仪表盘可以展示 Zoon URL 的存在和同步状态，但不得暴露 `token`、`ownerSecret`、Authorization header 或 API 原始响应内部信息。

## 与 Evidence Dashboard 的关系

Evidence Dashboard 回答“现在有哪些证据”；Product Readiness Dashboard 回答“基于这些证据，现在能不能出图或交付”。前者是证据页，后者是 gate verdict。两者可以同屏展示，但 Product Readiness Dashboard 必须放在出图 / 交付判断之前。

浏览器证据属于 Product Artifact Flow 的轻量产物：用 `pmw-artifact add --kind browser_evidence` 登记线上流程截图、状态页、竞品参考或 Zoon 漂移证据。仪表盘只读取它的状态、URL / 路径和摘要，不引入新的证据库或浏览器自动化命令。

视觉基线属于出图控制产物：用 `pmw-artifact add --kind visual_baseline` 或 `pmw-image-audit baseline --reference <截图路径> --register` 登记参考图尺寸、目标输出像素、字号层级、页面边距、模块间距、底部栏高度和参考优先级。汽车之家 / AutoDesign 生产页中，线上截图基线高于泛化 AutoDesign token；生成后还要用 `pmw-image-audit audit` 做尺寸 / 长板审计。

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

`pmw-dashboard status` 必须内嵌 `PMWorkspace 产品准备度仪表盘`，避免用户只看到零散证据状态。

## 固定门槛

仪表盘至少展示以下门槛：

| 门槛 | 出图前 | 交付前 | 判断 |
|---|---|---|---|
| 产品简报 | Required | Required | 必须是 `已对齐`，且没有缺失门槛或实质漂移。 |
| Zoon | Required | Required | 必须已同步，且出图 / 交付前无实质漂移。 |
| 线上参考 | Required | Required | 已提供线上参考、已确认无线上参考，或明确不适用；未判断时不继续。优先读取最新 `browser_evidence` 产物，没有时回退到 run evidence / gate 事件。 |
| 方案差异 | Required | Required | 多方案必须在页面结构、信息架构、交互路径、信任表达或关键任务上不同；单方案也要标注不适用或已登记。 |
| 不可虚构项 | Required | Required | 必须明确不能展示的能力、数据、承诺或动作。 |
| 复审状态 | no | Required | 出图前展示但不阻断；交付前必须是 `可通过`，不能有需要重出、PM 拍板或补参考项。 |

可以追加 `待决策项`、`设计系统`、`交付资产` 等行，但不能省略以上六行。

## Verdict 规则

- `READY_FOR_PROTOTYPE / 可出图`：产品简报、Zoon、线上参考、方案差异和不可虚构项都通过；复审状态仅展示，不阻断出图。
- `READY_FOR_HANDOFF / 可交付`：出图前门槛全部通过，且原型复审为 `可通过`，关键 D 已拍板，交付缺口不会改变承诺或验收。
- `NOT_READY / 不可出图 / 不可交付`：任一 required 行未通过。输出必须给出第一条阻断行的行动建议，并路由到能补齐它的最早技能。

## 输出契约

用户可见输出使用中文字段：

```text
PMWorkspace 产品准备度仪表盘：
- 目标：<出图前 / 交付前>
- 当前 run：
- Verdict：<可出图 / 不可出图 / 可交付 / 不可交付>
- 下一步：

| 门槛 | Required | 状态 | 证据 | 行动 |
|---|---|---|---|---|
| 产品简报 | YES | ... | ... | ... |
| Zoon | YES | ... | ... | ... |
| 线上参考 | YES | ... | ... | ... |
| 方案差异 | YES | ... | ... | ... |
| 不可虚构项 | YES | ... | ... | ... |
| 复审状态 | YES/no | ... | ... | ... |
```

如果仪表盘显示缺口，不要用图片、PRD 或“后续补充”绕过。把缺口转成一个 `Q`、一个 `D`，或退回 `$pm-brief`、`$pm-prototype-shotgun`、`$pm-prototype-review`、`$pm-handoff` 中最早能修复的技能。

仪表盘可以展示 Zoon URL 的存在和同步状态，但不得暴露 `token`、`ownerSecret`、Authorization header 或 API 原始响应内部信息。

## 与 Evidence Dashboard 的关系

Evidence Dashboard 回答“现在有哪些证据”；Product Readiness Dashboard 回答“基于这些证据，现在能不能出图或交付”。前者是证据页，后者是 gate verdict。两者可以同屏展示，但 Product Readiness Dashboard 必须放在出图 / 交付判断之前。

浏览器证据属于 Product Artifact Flow 的轻量产物：用 `pmw-artifact add --kind browser_evidence` 登记线上流程截图、状态页、竞品参考或 Zoon 漂移证据。仪表盘只读取它的状态、URL / 路径和摘要，不引入新的证据库或浏览器自动化命令。

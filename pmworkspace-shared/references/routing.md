# PMWorkspace 路由

决定下一步由哪个 PMWorkspace 专家负责时使用本文件。

For Chinese users, use Chinese names in explanations and keep skill ids unchanged.

## 主入口协议

`$pm-workspace` 只读取本文件作为路由唯一真源；不要在 `$pm-workspace/SKILL.md` 里维护第二份路由表。

路由前同时读取 `pm-workbench-map.md`。本文件决定“下一技能是什么”，`pm-workbench-map.md` 决定“当前链路阶段、共享状态字段和 eval 分类怎么对齐”。

路由前先完成 D0 工作方式判定。默认使用内部评分，不向用户暴露评分细节；只有模式不清、风险信号冲突或输入材料不足以判断时，才展开一个 `D0 工作方式` 选择题并等待用户回答。

## D0 工作方式判定

| 判定维度 | 快速成型信号 | 深度交付信号 |
|---|---|---|
| 输出目标 | 想先拿出去讨论、看 2-3 个方案、10 分钟轻量包、产品简报 + 方案方向 + 原型图 | PRD、设计评审、研发交付、实验验证、Zoon 对齐、生产交付资产 |
| 输入材料 | 一句话 idea、拍脑袋方向、没有 PRD/截图/线上流程 | PRD、Zoon、访谈、支持洞察、线上截图、录屏、生产视觉基线 |
| 风险等级 | 低风险探索，不涉及真实承诺、交易、线索、隐私或数据真实性 | 涉及用户承诺、数据真实性、交易、线索、隐私、合规、业务指标或高风险流程 |
| 是否生产流程 | 新概念、新页面概念稿、非线上承接流程 | 现有功能迭代、线上流程承接、结果页/状态页、生产样式继承 |
| 是否要交付 | 只需要讨论材料或方向探索 | 需要给设计、研发、业务、实验或评审继续使用 |

内部评分默认：

- 快速成型信号每项记 1 分；“10 分钟轻量包 / 先给几个方案 / 简报 + 方案方向 + 原型图”记 2 分。
- 深度交付信号每项记 2 分；高风险等级、生产流程、真实交付要求各额外记 1 分。
- 深度交付分数高于快速成型分数时，默认深度交付；快速成型分数高于深度交付分数且没有高风险信号时，默认快速成型。
- 分数接近、用户目标和输入材料冲突、或缺少输出目标时，必须问 `D0 工作方式`。

`D0 工作方式` 的用户可见选择题只保留两个选项：

```text
D0 工作方式
A. 快速成型：先做可讨论轻量包，确认假设后再出方案和原型图。
B. 深度交付：先补齐产品事实、风险、Zoon/截图/简报门槛，再进入原型或交付。
```

## 路由表

| 用户意图 | 路由 |
|---|---|
| 快速成型、10 分钟轻量包、先给几个方案、产品简报 + 方案方向 + 原型图 | `$pm-autoplan` 快速成型模式 |
| 原始想法、模糊请求、“帮我想想”、“是否值得做” | `$pm-jobs` |
| 一次自动跑完整产品评审、按推荐推进但关键点拍板、深度交付 | `$pm-autoplan` 深度交付模式 |
| 策略、范围、野心、风险、价值交换、“想大一点” | `$pm-strategy-review` |
| 需要可沉淀的产品简报或 Zoon 对齐资产 | `$pm-brief` |
| 需要 image-2 原型图、多方案、截图修改 | `$pm-prototype-shotgun` |
| 已生成原型图，需要复审、重出判断、偏好沉淀 | `$pm-prototype-review` |
| 需要适合 PRD、设计、实验验证或研发使用的交付稿 | `$pm-handoff` |

多个路由都适用时，先判断模式，再从最早缺失的资产开始：

1. 新 idea 且用户要“先拿出去讨论” -> `$pm-autoplan` 快速成型模式。
2. 产品问题不清楚且没有要求轻量包 -> `$pm-jobs`。
3. 问题清楚，但策略/范围有争议 -> `$pm-strategy-review`。
4. 策略清楚，但没有已对齐的产品简报 -> `$pm-brief`。
5. 产品简报已对齐，并且用户要原型 -> `$pm-prototype-shotgun`。
6. 原型已生成，但需要验收、复审或重出判断 -> `$pm-prototype-review`。
7. 方向已选定，下一团队需要接手 -> `$pm-handoff`。

## 路由输出契约

每次 `$pm-workspace` 完成路由后，默认只给用户一个短业务摘要：

```text
业务判断：
当前需要确认：
下一步：
```

完整路由字段必须写入本地审计；用户明确要求“看状态 / 看审计 / 调试 / 展开证据”时才输出：

```text
当前模式：
当前门槛：
下一技能：
为什么：
run_id：
证据状态：
```

- `当前模式`：快速成型 / 深度交付 / 维护检查。
- `当前门槛`：当前必须停住或即将处理的最早门槛，例如 D0 工作方式、假设确认、产品简报未已对齐、线上参考缺失、原型复审、交付确认。
- `下一技能`：写 skill id，例如 `$pm-autoplan`。
- `为什么`：用一句话说明路由依据，只引用用户输入、已对齐产品简报、最新 Zoon、截图/线上参考或当前 run 证据，不用历史偏好替代事实。
- `run_id`：平台脚本可用时由 `$pm-workspace` 创建；脚本不可用时写 `未启用`。
- `证据状态`：至少说明产品简报、Zoon、线上参考、原型清单、待决策项和 Product Readiness Dashboard 的当前状态；未知项写 `未提供`、`未运行` 或 `待检查`。

## Run 衔接

`$pm-workspace` 是路由型会话的 run owner：完成 D0 和路由判定后先创建 run，并记录当前门槛、证据状态和下一技能。被路由到的子 skill 必须复用当前 run；只有用户直接调用子 skill 且没有当前 run 时，子 skill 才创建自己的 run。

## 端到端地图衔接

路由结果必须落在 `pm-workbench-map.md` 的一个链路阶段上：

- 欢迎与 D0 路由 -> `$pm-workspace`
- 自动产品评审 -> `$pm-autoplan`
- 产品追问 -> `$pm-jobs`
- 策略审查 -> `$pm-strategy-review`
- 产品简报 -> `$pm-brief`
- 原型方案 -> `$pm-prototype-shotgun`
- 原型复审 -> `$pm-prototype-review`
- 产品交付 -> `$pm-handoff`

如果某个门槛失败，下一技能必须指向最早能补齐该门槛的阶段；不要跳到下游产物。

## 快速成型工作流

```text
pm-workspace
-> pm-autoplan quick shaping
-> 2-3 critical Qs
-> assumption confirmation
-> light brief + solution directions
-> pm-prototype-shotgun for separate image-2 screens
-> next upgrade: PRD / prototype review / handoff
```

轻量包状态是 `基于假设，可讨论`。它可以用于组内讨论、领导评审或方案探索，但不能包装成最终 PRD 或已验证产品事实。

## 深度交付工作流

```text
pm-workspace
-> pm-jobs
-> pm-strategy-review when strategy risk is material
-> decision questions when PM tradeoffs remain
-> pm-brief + Zoon online doc
-> pm-prototype-shotgun reads latest Zoon brief
-> pm-prototype-review checks generated images
-> pm-handoff
```

深度交付生成图片前，不能跳过已对齐的产品简报。快速成型生成图片前，必须先让用户确认“按这些假设继续”。

# PMWorkspace 路由

决定下一步由哪个 PMWorkspace 专家负责时使用本文件。

For Chinese users, use Chinese names in explanations and keep skill ids unchanged.

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

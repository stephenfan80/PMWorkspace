# PMWorkspace 路由

Use this when deciding which PMWorkspace expert should own the next step.

For Chinese users, use Chinese names in explanations and keep skill ids unchanged.

## 路由表

| 用户意图 | 路由 |
|---|---|
| 原始想法、模糊请求、“帮我想想”、“是否值得做” | `$pm-jobs` |
| 策略、范围、野心、风险、价值交换、“想大一点” | `$pm-strategy-review` |
| 需要可沉淀的产品简报或 Zoon 对齐资产 | `$pm-brief` |
| 需要 image-2 原型图、多方案、截图修改 | `$pm-prototype-shotgun` |
| 需要适合 PRD、设计、实验验证或研发使用的交付稿 | `$pm-handoff` |

When multiple routes fit, start with the earliest missing asset:

1. 产品问题不清楚 -> `$pm-jobs`。
2. 问题清楚，但策略/范围有争议 -> `$pm-strategy-review`。
3. 策略清楚，但没有已对齐的产品简报 -> `$pm-brief`。
4. 产品简报已对齐，并且用户要原型 -> `$pm-prototype-shotgun`。
5. 方向已选定，下一团队需要接手 -> `$pm-handoff`。

## 默认工作流

```text
pm-workspace
-> pm-jobs
-> pm-strategy-review when strategy risk is material
-> pm-brief
-> pm-prototype-shotgun
-> pm-handoff
```

生成图片前，不能跳过已对齐的产品简报。

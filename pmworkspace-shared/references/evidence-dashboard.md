# Evidence Dashboard

Evidence Dashboard 是 PMWorkspace 的证据状态页，用来避免产品事实、Zoon 版本、线上参考、原型清单和复审结论散落在对话里。

如果要判断能不能出图或交付，必须同时读取 `product-readiness-dashboard.md`。Evidence Dashboard 回答“证据在哪里”，Product Readiness Dashboard 回答“现在能不能继续”。

## 使用时机

- `$pm-autoplan` 结束一个门槛判断后。
- `$pm-prototype-shotgun` 出图前和批量出图后。
- `$pm-prototype-review` 完成复审后。
- `$pm-handoff` 生成交付稿前。

平台脚本可用时运行：

```bash
pmw-dashboard status
pmw-dashboard status --run <run_id>
pmw-dashboard readiness --target prototype
pmw-dashboard readiness --target handoff
```

## 状态页必须覆盖

- 产品简报版本和状态。
- Zoon URL、最近同步时间和漂移状态。
- 线上参考状态。
- 主目标、反指标、关键假设和不可虚构项。
- `D` 决策和当前待拍板项。
- 原型图片清单和方案比较板。
- 原型复审结论。
- 问题偏好摘要。
- 用户全局记忆摘要：个人偏好、产品认知、交付事实和 PMWorkspace 进化候选。
- 本地交付资产：接口、数据来源、埋点事件、实验标准和指标口径的摘要与适用范围。
- GitHub 回流待审稿状态：无 / 已生成本地草稿 / 待用户确认 / 已回流。

如果 dashboard 显示证据缺口，不要用漂亮原型掩盖缺口。把缺口转成一个 `Q`、一个 `D`，或明确标注为快速成型假设。

用户全局记忆只能作为推荐来源。若它影响建议，输出必须明示“基于过往偏好”、“基于本地产品认知”或“基于本地交付资产”，不能覆盖当前产品简报、最新 Zoon、反指标、不可虚构项或线上参考门槛。

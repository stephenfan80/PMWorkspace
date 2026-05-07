# Evidence Dashboard

Evidence Dashboard 是 PMWorkspace 的证据状态页，用来避免产品事实、Zoon 版本、线上参考、原型清单和复审结论散落在对话里。

## 使用时机

- `$pm-autoplan` 结束一个门槛判断后。
- `$pm-prototype-shotgun` 出图前和批量出图后。
- `$pm-prototype-review` 完成复审后。
- `$pm-handoff` 生成交付稿前。

平台脚本可用时运行：

```bash
pmw-dashboard status
pmw-dashboard status --run <run_id>
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

如果 dashboard 显示证据缺口，不要用漂亮原型掩盖缺口。把缺口转成一个 `Q`、一个 `D`，或明确标注为快速成型假设。


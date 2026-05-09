# Question Tuning for PM

Question Tuning 记录用户对 PMWorkspace 追问方式的偏好，让系统越用越贴近用户，但不能覆盖当前产品事实。

## 策略

- `always_ask`：这类问题永远问清楚。
- `high_risk_only`：只有涉及高风险业务、线上流程、数据承诺或交付时才问。
- `default_recommend`：默认采用推荐项，只在用户质疑或风险升高时展开。
- `avoid_unless_blocking`：除非不问会阻断产品方向，否则避免追问。

## 使用方式

开始 `$pm-jobs` 或 `$pm-autoplan` 时读取：

```bash
pmw-question-tuning summary
```

用户表达“这个以后别总问”“这类问题一定要问我”“这种默认你决定”时记录：

```bash
pmw-question-tuning add \
  --dimension "<问题维度>" \
  --policy <always_ask|high_risk_only|default_recommend|avoid_unless_blocking> \
  --reason "<脱敏原因>"
```

## 约束

- 问题偏好只影响提问方式和默认追问力度。
- 偏好不能覆盖主目标、反指标、不可虚构项、Zoon 最新内容或用户本轮明确决策。
- 如果偏好导致少问问题，必须在简报中标注采用的默认假设。


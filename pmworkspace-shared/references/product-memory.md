# 产品记忆与偏好复利

PMWorkspace 的记忆只保存脱敏后的产品资产和偏好摘要。目标是让后续产品简报和原型方向更贴近用户，而不是保存原始敏感材料。

## 使用时机

- 新一轮 `$pm-jobs` 或 `$pm-autoplan` 开始时，读取项目记忆摘要。
- 多方案原型前，读取偏好摘要，避免重复生成用户已经拒绝的方向。
- 原型复审或用户反馈后，记录批准/拒绝原因。
- 用户反复纠正同类问题时，沉淀为 learning。
- 用户明确表达某类 Q/D 的追问偏好时，使用 `question-tuning.md` 记录，不要只写成普通 taste。

## 工具

平台脚本可用时：

```bash
pmw-memory summary
pmw-memory taste-summary
pmw-memory search "<关键词>"
pmw-memory add-learning "<脱敏学习>"
```

偏好反馈仍通过：

```bash
pmw-log taste approved "<用户喜欢的方向>"
pmw-log taste rejected "<用户拒绝的方向>"
pmw-log taste rejected "<脱敏原因>" --scenario "转化流程" --target "表单摩擦" --scope "同类场景可复用" --source "用户反馈" --confidence 0.6
```

问题偏好使用：

```bash
pmw-question-tuning summary
pmw-question-tuning add --dimension "<问题维度>" --policy <always_ask|high_risk_only|default_recommend|avoid_unless_blocking> --reason "<脱敏原因>"
```

## 保存什么

- 用户确认过的产品判断。
- 原型方案的批准/拒绝原因。
- 用户常用反指标。
- 常见不可虚构边界。
- 设计偏好，例如信息密度、信任表达、表单摩擦、结果页结构。

## 原型反馈记忆字段

第一阶段优先复用 `taste-profile.jsonl`、`prototype-board.jsonl` 和 `learnings.jsonl`。记录原型反馈时，尽量沉淀为这些脱敏字段：

- `action`：`approved` 或 `rejected`。
- `note`：短原因，不保存原始敏感材料。
- `scenario`：转化流程、结果页、看板、内部工具等。
- `target`：方案方向、信息架构、信任表达、文案、视觉密度、表单摩擦或数据承诺。
- `scope`：仅本项目、同类场景可复用、高风险时不复用。
- `source`：用户反馈、原型复审或 D 拍板。
- `confidence`：新反馈默认较低，重复出现后再提高。

## 不保存什么

- 原始客户资料、录音、敏感截图、完整私密 PRD。
- token、API key、cookie、Zoon ownerSecret。
- 未脱敏 Zoon 正文。

## 应用规则

- 记忆是建议，不是事实来源；如果和当前 brief 冲突，以当前已对齐 brief 或最新 Zoon 为准。
- 偏好只能影响方案方向和表达方式，不能覆盖主目标、反指标或不可虚构项。
- 原型复审中的事实错误、反指标风险、不可虚构违规、线上参考缺失或未决用户承诺不能保存成普通偏好；它们必须保留为门槛、重出原因或 `D` 拍板。
- 原型复审沉淀偏好时，必须写明 `source: 原型复审` 或 `source: 用户反馈`，并标注 `scope`，避免下一轮把局部审美意见当成全局规则。
- 问题偏好只能影响追问力度，不能覆盖本轮明确事实或高风险门槛。
- 如果记忆改变了推荐方案，需要明说“基于过往偏好，我建议……”。

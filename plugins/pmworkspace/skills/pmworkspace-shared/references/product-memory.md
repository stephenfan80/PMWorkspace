# 产品记忆与偏好复利

PMWorkspace 的记忆只保存脱敏后的产品资产和偏好摘要。目标是让后续产品简报和原型方向更贴近用户，而不是保存原始敏感材料。

记忆默认分为两层：

- `个人全局记忆`：单个用户独有，保存在本地 `~/.pmworkspace/user/`，跨项目复用。
- `项目局部记忆`：保存在 `~/.pmworkspace/projects/<slug>/`，只服务当前项目证据和局部偏好。

个人全局记忆是推荐来源，不是事实来源；当前已对齐产品简报 / 最新 Zoon / 本轮明确输入永远优先。

## 使用时机

- 新一轮 `$pm-jobs`、`$pm-brief`、`$pm-prototype-shotgun` 或 `$pm-handoff` 开始时，优先读取 `pmw-memory user-summary`，再读取项目记忆摘要。
- 进入 `$pm-handoff` 时，额外读取 `pmw-memory delivery-summary`，复用接口、数据、埋点和实验口径；必须明示 `基于本地交付资产...`，且不能覆盖当前 brief、Zoon、反指标或不可虚构项。
- 多方案原型前，读取偏好摘要，避免重复生成用户已经拒绝的方向。
- 原型复审或用户反馈后，记录批准/拒绝原因。
- 用户反复纠正同类问题时，沉淀为 learning。
- 用户明确表达某类 Q/D 的追问偏好时，使用 `question-tuning.md` 记录，不要只写成普通 taste。

## 工具

平台脚本可用时：

```bash
pmw-memory summary
pmw-memory user-summary
pmw-memory taste-summary
pmw-memory search "<关键词>"
pmw-memory add-learning "<脱敏学习>"
pmw-memory add-feedback --type preference --note "<脱敏偏好>" --scenario "<场景>" --target "<对象>" --scope "个人全局偏好" --source "用户反馈" --confidence 0.4
pmw-memory add-feedback --type product-cognition --note "<脱敏产品认知>" --scenario "<场景>" --target "<认知对象>" --scope "同类场景可复用" --source "原型复审" --confidence 0.4
pmw-memory add-feedback --type pmworkspace-improvement --note "<脱敏产品化建议>" --target "$pm-prototype-review" --scope "PMWorkspace 进化候选" --source "用户反馈" --confidence 0.4
pmw-memory draft-github-feedback --title "<标题>" --observation "<脱敏观察>" --affected-skill "$pm-prototype-review" --suggested-rule "<建议规则>" --suggested-eval "<建议 eval>"
pmw-memory delivery-summary
pmw-memory add-delivery-fact --fact-type tracking --note "<脱敏埋点事件或指标口径>" --scenario "<场景>" --target "<对象>" --scope "本项目" --source "产品交付" --confidence 0.5
pmw-memory add-delivery-fact --fact-type interface --note "<脱敏接口能力或来源>" --scenario "<场景>" --target "<接口对象>" --scope "本项目" --source "用户输入" --confidence 0.5
pmw-memory add-delivery-fact --fact-type data-source --note "<脱敏数据来源或字段口径>" --scenario "<场景>" --target "<数据对象>" --scope "同类场景可复用" --source "产品交付" --confidence 0.5
pmw-memory add-delivery-fact --fact-type experiment --note "<脱敏实验标准>" --scenario "<场景>" --target "<实验对象>" --scope "同类场景可复用" --source "产品交付" --confidence 0.5
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
- 交付资产，例如接口能力、数据来源、字段口径、埋点事件、实验标准、指标定义和数据可用性判断。

## 全局用户资产

默认本地结构：

```text
~/.pmworkspace/user/
  taste-profile.jsonl
  product-cognition.jsonl
  delivery-facts.jsonl
  pmworkspace-improvements.jsonl
  pmworkspace-feedback-drafts/
```

保存边界：

- `taste-profile.jsonl`：跨项目个人偏好，例如信息密度、信任表达、视觉风格、表单摩擦、结果页结构。
- `product-cognition.jsonl`：脱敏产品认知，例如常用反指标、不可虚构边界、场景机制经验。
- `delivery-facts.jsonl`：脱敏交付事实，例如接口、数据来源、埋点事件、实验标准和指标口径。
- `pmworkspace-improvements.jsonl`：PMWorkspace 进化候选，记录值得产品化的技能规则、eval、输出结构或门槛判断。
- `pmworkspace-feedback-drafts/`：准备回流 GitHub 的脱敏 Markdown 待审稿。

每条反馈资产必须包含 `scenario`、`target`、`scope`、`source` 和 `confidence`，并区分 `本项目`、`同类场景可复用`、`个人全局偏好`、`PMWorkspace 进化候选`。

## 反馈资产化分类

原型复审或用户反馈后，把反馈分成：

- `个人偏好`：用户对信息密度、信任表达、视觉风格、表单摩擦、结果页结构等表达方式的稳定偏好。
- `产品认知`：可复用的产品判断、反指标、不可虚构边界、场景机制经验。
- `PMWorkspace 进化建议`：技能规则、eval、输出结构、门槛判断中值得产品化的改进。
- `不应保存`：事实错误、反指标风险、不可虚构违规、线上参考缺失、未决用户承诺、数据真实性、隐私或合规边界。

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
- 真实项目名、内部 URL、截图内容、客户信息或未脱敏 PRD 到 GitHub 回流草稿。

## 交付资产字段

`pmw-memory add-delivery-fact` 用于保存用户在 PRD、接口、埋点、实验或数据沟通中补充的可复用交付事实。每条记录至少包含：

- `fact_type`：`interface`、`data-source`、`tracking`、`experiment` 或 `metric-definition`。
- `note`：脱敏后的短摘要，不保存原始私密文档。
- `scenario`：转化流程、社区、直播、产品库、看板、交易等使用场景。
- `target`：接口、数据表、事件、指标、实验对象或功能模块。
- `scope`：`本项目`、`同类场景可复用` 或其他明确范围。
- `source`：用户输入、产品交付、现成文档、Zoon、原型复审等。
- `confidence`：新记录默认较低，重复被确认后再提高。

交付资产可以帮助下一次 PRD 少问重复问题，但它只作为参考来源；如果和当前 brief、最新 Zoon、本轮输入、反指标、不可虚构项或线上参考冲突，以当前事实为准。

## GitHub 回流边界

- 默认只生成本地脱敏待审稿，不自动提交 GitHub、issue 或 PR。
- 草稿包含：反馈来源、脱敏观察、影响的技能、建议规则、建议 eval、隐私检查。
- 只有用户明确要求“提交 GitHub / 部署上线”时，才把待审稿转成仓库变更、issue 或 PR。
- GitHub 回流草稿不得包含真实项目名、Zoon 正文、截图内容、客户信息、token、内部 URL 或未脱敏 PRD。

## 应用规则

- 记忆是建议，不是事实来源；如果和当前 brief 冲突，以当前已对齐 brief 或最新 Zoon 为准。
- 偏好只能影响方案方向和表达方式，不能覆盖主目标、反指标或不可虚构项。
- 应用个人记忆时必须明示“基于过往偏好”或“基于本地产品认知”，并说明来源和适用范围。
- 应用交付事实时必须明示“基于本地交付资产”，并说明来源和适用范围。
- 原型复审中的事实错误、反指标风险、不可虚构违规、线上参考缺失或未决用户承诺不能保存成普通偏好；它们必须保留为门槛、重出原因或 `D` 拍板。
- 原型复审沉淀偏好时，必须写明 `source: 原型复审` 或 `source: 用户反馈`，并标注 `scope`，避免下一轮把局部审美意见当成全局规则。
- 问题偏好只能影响追问力度，不能覆盖本轮明确事实或高风险门槛。
- 如果记忆改变了推荐方案，需要明说“基于过往偏好，我建议……”。

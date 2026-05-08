# 状态与遥测

PMWorkspace 默认在本地保存可沉淀产品资产。它应该帮助用户积累产品判断和可复用交付材料，同时避免泄露敏感源材料。

## 本地状态根目录

默认根目录：

```text
~/.pmworkspace/
```

预期结构：

```text
config.yaml
analytics/usage.jsonl
user/taste-profile.jsonl
user/product-cognition.jsonl
user/delivery-facts.jsonl
user/pmworkspace-improvements.jsonl
user/pmworkspace-feedback-drafts/
projects/<slug>/briefs/
projects/<slug>/decisions.jsonl
projects/<slug>/questions.jsonl
projects/<slug>/project.json
projects/<slug>/runs/
projects/<slug>/prototype-board.jsonl
projects/<slug>/question-tuning.jsonl
projects/<slug>/prototypes/
projects/<slug>/handoffs/
projects/<slug>/delivery-facts.jsonl
projects/<slug>/taste-profile.jsonl
projects/<slug>/learnings.jsonl
```

## 保存什么

- 使用事件：技能名、时间戳、项目标识。
- 决策：用户确认过的简短产品或设计决策。
- 拍板问题：问题标题、推荐项、用户选择和最终决策摘要。
- 产品简报：已对齐或待确认的 Markdown 产品简报。
- 交付稿：PRD、设计交付、实验验证或研发交付的 Markdown 资产。
- 项目元数据：中文展示名、技术 slug、最新产品简报路径和 Zoon 文档链接。
- 运行审计：run id、模式、门槛、证据、决策、产物、复审和下一步。
- 原型清单：方案、屏幕、画布、产品简报依赖和提示词摘要。
- 原型方案比较板：方案、屏幕、主目标、反指标、不可虚构项、brief 版本、评分和评论。
- 问题偏好：用户对 Q/D 追问方式的脱敏偏好。
- 偏好反馈：批准/拒绝的方向、脱敏原因、场景、反馈对象、来源、适用边界和置信度。
- 产品学习：脱敏后的复用判断、常见边界和后续偏好。
- 个人全局偏好：单个用户独有、跨项目可复用的偏好资产。
- 产品认知：脱敏后的产品判断、反指标、不可虚构边界和场景机制经验。
- 交付事实：接口、数据来源、字段口径、埋点事件、实验标准、指标定义和数据可用性判断的脱敏摘要。
- PMWorkspace 进化候选：用户反馈中可产品化为技能规则、eval、输出结构或门槛判断的建议。
- GitHub 回流待审稿：只保存在本地的脱敏 Markdown 草稿，用户确认后才提交。

## 不保存什么

- 真实 token、owner secret、API key、cookie、鉴权头。
- 私密客户数据、原始通话记录、内部录音。
- 敏感截图或未脱敏 Zoon 内容。
- 完整私密 PRD，除非用户明确要求本地保存。
- Zoon ownerSecret 或 API 原始响应。
- 真实项目名、内部 URL、截图内容、客户信息或未脱敏 PRD 到 `user/pmworkspace-feedback-drafts/`。

## 遥测默认值

- `telemetry: local` 表示只写本地日志。
- 远程遥测必须由用户明确开启。
- 匿名远程遥测实现后，最多包含技能名、耗时、结果、版本和粗略系统信息。
- 不发送项目名、文件路径、提示词文本、截图、产品简报内容或客户数据。

## 用户全局记忆

`~/.pmworkspace/user/` 是单个用户独有的本地资产目录。它可以让 PMWorkspace 跨项目理解用户偏好，但它不是事实来源。

- 使用时必须明示来源，例如“基于过往偏好，我建议……”。
- 使用交付事实时必须明示来源，例如“基于本地交付资产，我建议……”。
- 不得覆盖当前 brief、Zoon、反指标、不可虚构项或线上参考门槛。
- 远程回流默认关闭；GitHub 回流只能从脱敏待审稿开始。

使用 `bin/pmw-config list` 查看当前设置。

## 中文项目名

技术 slug 只用于本地目录稳定性，不作为用户可见项目名。面向用户输出时，优先展示 `pmw-project get-name` 的中文项目名，例如“通用券站外召回方案”。如果项目还没有展示名，先从产品简报标题、产品想法或功能名中提炼 6-14 个中文字符，再运行：

```bash
pmw-project set-name "<中文项目名>"
```

不要向用户展示技术 slug 或裸 hash，除非用户正在调试本地目录。

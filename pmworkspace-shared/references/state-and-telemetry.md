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
projects/<slug>/briefs/
projects/<slug>/decisions.jsonl
projects/<slug>/questions.jsonl
projects/<slug>/project.json
projects/<slug>/prototypes/
projects/<slug>/taste-profile.jsonl
```

## 保存什么

- 使用事件：技能名、时间戳、项目标识。
- 决策：用户确认过的简短产品或设计决策。
- 拍板问题：问题标题、推荐项、用户选择和最终决策摘要。
- 产品简报：已对齐或待确认的 Markdown 产品简报。
- 项目元数据：中文展示名、技术 slug、最新产品简报路径和 Zoon 文档链接。
- 原型清单：方案、屏幕、画布、产品简报依赖和提示词摘要。
- 偏好反馈：批准/拒绝的方向，以及用户原因。

## 不保存什么

- 真实 token、owner secret、API key、cookie、鉴权头。
- 私密客户数据、原始通话记录、内部录音。
- 敏感截图或未脱敏 Zoon 内容。
- 完整私密 PRD，除非用户明确要求本地保存。
- Zoon ownerSecret 或 API 原始响应。

## 遥测默认值

- `telemetry: local` 表示只写本地日志。
- 远程遥测必须由用户明确开启。
- 匿名远程遥测实现后，最多包含技能名、耗时、结果、版本和粗略系统信息。
- 不发送项目名、文件路径、提示词文本、截图、产品简报内容或客户数据。

使用 `bin/pmw-config list` 查看当前设置。

## 中文项目名

技术 slug 只用于本地目录稳定性，不作为用户可见项目名。面向用户输出时，优先展示 `pmw-project get-name` 的中文项目名，例如“通用券站外召回方案”。如果项目还没有展示名，先从产品简报标题、产品想法或功能名中提炼 6-14 个中文字符，再运行：

```bash
pmw-project set-name "<中文项目名>"
```

不要向用户展示技术 slug 或裸 hash，除非用户正在调试本地目录。

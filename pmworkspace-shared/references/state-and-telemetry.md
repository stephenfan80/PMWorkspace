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
projects/<slug>/prototypes/
projects/<slug>/taste-profile.jsonl
```

## 保存什么

- 使用事件：技能名、时间戳、项目标识。
- 决策：用户确认过的简短产品或设计决策。
- 产品简报：已对齐或待确认的 Markdown 产品简报。
- 原型清单：方案、屏幕、画布、产品简报依赖和提示词摘要。
- 偏好反馈：批准/拒绝的方向，以及用户原因。

## 不保存什么

- 真实 token、owner secret、API key、cookie、鉴权头。
- 私密客户数据、原始通话记录、内部录音。
- 敏感截图或未脱敏 Zoon 内容。
- 完整私密 PRD，除非用户明确要求本地保存。

## 遥测默认值

- `telemetry: local` 表示只写本地日志。
- 远程遥测必须由用户明确开启。
- 匿名远程遥测实现后，最多包含技能名、耗时、结果、版本和粗略系统信息。
- 不发送项目名、文件路径、提示词文本、截图、产品简报内容或客户数据。

使用 `bin/pmw-config list` 查看当前设置。

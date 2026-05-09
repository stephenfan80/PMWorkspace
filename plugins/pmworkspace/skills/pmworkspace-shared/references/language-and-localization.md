# 语言与本地化

生成面向用户的 PMWorkspace 输出前，先读取本文件。

## 语言判断

- 如果用户当前消息主要是中文，默认输出简体中文。
- 如果用户明确要求中文，输出简体中文。
- 如果用户使用英文，除非用户另有要求，否则输出英文。
- 如果对话中中英文混用，跟随用户最新消息的语言。

## 中文输出标准

面向中文用户时，输出应尽可能保持纯中文：

- 使用中文标题、标签、字段名、说明、示例数据和建议。
- 避免使用英文策略标题、英文输出标题或英文交付标题。
- 优先使用中文状态标签：`需要补充`、`待确认`、`已对齐`、`已记录`、`下一步`。
- 优先使用中文产品术语：`产品简报`、`交付稿`、`原型方案`、`范围外`、`验收标准`、`风险与待决策`。
- 只有精确技术或产品术语才保留英文：`token`、`API`、`URL`、`PRD`、`Zoon`、`GitHub`、`Codex`、`image-2`、`$pm-workspace` 这类技能 id、文件路径、命令、模型名和代码标识符。
- 必须保留英文术语时，不要让整句话变成英文。示例：`不要把 token、API key 或未脱敏截图写入资产文件。`

## 避免中英文混杂

避免像这样混用英文标签：

```text
English label: ...
English recommendation: ...
English section title
English output title
```

改成：

```text
最强前提：...
建议姿态：扩大方向，但分阶段推进。
策略选择
原型计划
```

## 技能名称

Keep skill ids unchanged:

- `$pm-workspace`
- `$pm-jobs`
- `$pm-strategy-review`
- `$pm-brief`
- `$pm-prototype-shotgun`
- `$pm-prototype-review`
- `$pm-autoplan`
- `$pm-handoff`

When explaining them to Chinese users, add a Chinese role name:

- `$pm-jobs`：产品追问
- `$pm-strategy-review`：策略审查
- `$pm-brief`：产品简报
- `$pm-prototype-shotgun`：原型方案
- `$pm-prototype-review`：原型复审
- `$pm-autoplan`：自动产品评审
- `$pm-handoff`：交付稿

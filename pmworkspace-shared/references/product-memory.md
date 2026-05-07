# 产品记忆与偏好复利

PMWorkspace 的记忆只保存脱敏后的产品资产和偏好摘要。目标是让后续产品简报和原型方向更贴近用户，而不是保存原始敏感材料。

## 使用时机

- 新一轮 `$pm-jobs` 或 `$pm-autoplan` 开始时，读取项目记忆摘要。
- 多方案原型前，读取偏好摘要，避免重复生成用户已经拒绝的方向。
- 原型复审或用户反馈后，记录批准/拒绝原因。
- 用户反复纠正同类问题时，沉淀为 learning。

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
```

## 保存什么

- 用户确认过的产品判断。
- 原型方案的批准/拒绝原因。
- 用户常用反指标。
- 常见不可虚构边界。
- 设计偏好，例如信息密度、信任表达、表单摩擦、结果页结构。

## 不保存什么

- 原始客户资料、录音、敏感截图、完整私密 PRD。
- token、API key、cookie、Zoon ownerSecret。
- 未脱敏 Zoon 正文。

## 应用规则

- 记忆是建议，不是事实来源；如果和当前 brief 冲突，以当前已对齐 brief 或最新 Zoon 为准。
- 偏好只能影响方案方向和表达方式，不能覆盖主目标、反指标或不可虚构项。
- 如果记忆改变了推荐方案，需要明说“基于过往偏好，我建议……”。

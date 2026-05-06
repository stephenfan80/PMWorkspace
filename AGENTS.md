# AGENTS

本项目维护 `PMWorkspace` Codex skill 套件，用于把产品想法、PRD、截图、访谈/支持洞察转成对齐后的产品 brief、移动端优先 image-2 UI 原型图和可交付产品资产。

本地工作规则：

- 做原型前先完成产品对齐：确认场景、用户问题、目标、反指标、约束、数据可用性和 brief 状态。
- 只有 brief 达到 `Aligned`，才写 image prompt 或生成原型图。
- 默认原型输出移动端优先，使用 iPhone 17 portrait `402 x 874`；只有用户明确要求或 dashboard/internal tool 确实需要大屏时才用桌面端。
- 要求输出设计原型方案时，使用 image-2 / image generation 输出方案图片。
- 不要把多个方案合成在同一张图里；每个方案、每个屏幕都单独输出一张图。
- 可以批量生成多张，但每张图必须对应一个明确的方案名和屏幕任务。
- 多方案必须在产品策略、信息架构、交互模型或信任模型上有差异，不能只是换配色。
- 已上线功能迭代必须先拿到当前生产截图、录屏或等价视觉基线。
- 平台状态资产默认保存在 `~/.pmworkspace/`，只保存 brief、决策、原型 manifest、偏好反馈和本地 usage log。
- 不要把真实 token、内部录音、私密截图、客户资料或未脱敏 Zoon 内容写进公开仓库。

## Skill routing

- 产品想法 / 问题定义 / 是否值得做 -> `$pm-jobs`
- 策略、范围、价值交换、风险挑战 -> `$pm-strategy-review`
- 生成或更新产品 brief -> `$pm-brief`
- 多方案原型、image-2 出图、截图修改 -> `$pm-prototype-shotgun`
- PRD / 设计 / 实验 / 研发交付 -> `$pm-handoff`
- 不确定从哪里开始 -> `$pm-workspace`

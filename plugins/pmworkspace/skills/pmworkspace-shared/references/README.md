# PMWorkspace References Index

`pmworkspace-shared/references/` is PMWorkspace's shared reference layer. It is not a random file pile. Read it as two mental models:

- **方法库**：PMW 如何做产品判断、写产品简报、设计原型、复审方案和交付 PRD。
- **运行协议**：PMW 如何路由、记录 run、管理资产流、检查准备度、同步 Zoon、评估和升级。

普通用户不需要逐个阅读这些文件。第一次使用 PMW 时，先看仓库根目录的 `README.zh-CN.md`，再从 `$pm-workspace` 开始。Skill 作者、维护者和需要调试状态的人，再按本索引进入具体文件。

## 阅读顺序

| 你是谁 | 先读什么 | 什么时候继续读 |
|---|---|---|
| 普通 PM / 创始人 / 业务同学 | 根目录 `README.zh-CN.md` | 只在想理解 PMW 为什么追问、为什么不能直接出图时读方法库。 |
| Skill 作者 | 本索引 + 当前阶段的方法文件 | 写或改 `SKILL.md`、输出字段、门槛判断、下游资产读取时继续读运行协议。 |
| 维护者 | 本索引 + 运行协议 | 改路由、状态、eval、打包、Zoon、隐私或升级链路时继续读对应协议。 |

## 方法库

方法库解释 PMW 的产品工作方法。它们更接近“为什么这么做”和“产物应该长什么样”。

| 分组 | 文件 | 用途 |
|---|---|---|
| 产品发现 / 对齐 | `product-office-hours.md`、`product-discovery-gate.md`、`scenario-routing.md`、`internet-best-practice-research.md`、`decision-question-mode.md`、`pm-decision-principles.md` | 判断真实问题、当前替代、当前损失、目标、反指标、路径和关键 PM 拍板。 |
| 产品简报 | `product-manager-brief.md`、`product-plan-handoff.md` | 把产品判断压缩成出图、复审和交付都能读取的产品契约。 |
| 原型生成 | `image-prompts.md`、`design-system-workflow.md`、`prototype-shotgun-board.md`、`production-reference-gate.md`、`autohome-auto-design.md`、`design-heuristics.md`、`scenario-experts.md` | 约束 image-2 单方案单屏出图、多方案差异、截图基线、设计系统和场景专家。 |
| 原型复审 | `prototype-quality-review.md`、`pm-review-army.md`、`adversarial-review.md` | 检查原型是否忠实表达 brief、是否违反不可虚构项、是否需要重出或追加专家复审。 |
| 产品交付 | `delivery-handoff.md` | 把已对齐 brief、原型选择和复审结论整理成产品设计文档、精简 PRD 或交付稿。 |
| 语言与首次使用 | `language-and-localization.md`、`welcome-guide.md`、`first-use-onboarding.md` | 约束中文表达、欢迎引导和第一次使用的心智入口。 |
| 附录方法 | `appendix/product-methodology.md`、`appendix/product-office-hours-examples.md`、`appendix/prompt-recipes.md` | 存放可复用方法背景、示例和提示词配方。 |

## 运行协议

运行协议解释 PMW 如何保持“先对齐，再出图，最后交付”的秩序。它们更接近“系统如何不跳步、不丢状态、不泄露隐私”。

| 分组 | 文件 | 用途 |
|---|---|---|
| 路由 / 工作台地图 | `routing.md`、`pm-workbench-map.md`、`autoplan-workflow.md` | 决定入口职责边界、当前动作、下一技能、端到端阶段、共享状态字段和自动推进边界。 |
| 运行状态 / 准备度 | `runtime-kernel.md`、`artifact-flow.md`、`product-readiness-dashboard.md`、`evidence-dashboard.md`、`state-and-telemetry.md`、`browser-evidence.md` | 管理 run、Product Artifact Flow、Product Readiness Dashboard、证据登记、本地状态和隐私边界。 |
| 记忆 / 偏好 | `product-memory.md`、`question-tuning.md` | 管理可复用产品学习和 Q/D 追问偏好，但不能覆盖本轮事实。 |
| Zoon 协作 | `zoon-workflow.md`、`zoon-drift-check.md` | 管理在线协作文档的创建、加入、同步和漂移检查。 |
| 版本 / eval / 生成 | `update-workflow.md`、`pm-eval-system.md`、`skill-doc-template-system.md` | 管理更新、评估、skill 文档生成区块和 plugin 打包校验。 |

## 边界

- 根目录 README 负责回答“PMW 是什么、怎么开始、怎么安装更新、四个动作怎么走”。
- 本索引负责回答“references 里每个文件属于方法库还是运行协议、应该什么时候读”。
- 具体业务规则以对应 reference 文件为真源，不在 README 里复制完整状态机。
- 新增 reference 文件时，先判断它是方法库还是运行协议，再补到本索引，避免 references 重新变成杂项目录。

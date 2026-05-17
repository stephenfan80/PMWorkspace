# PMWorkspace

**PMWorkspace 是 AI 产品工作站：把一句想法、截图反馈、PRD 或用户洞察，推进成可讨论、可出图、可交付的产品方案。**

> Codex 插件展示名：**AI 产品工作站**。`PMWorkspace` 是 GitHub 仓库名、技术包名和 `$pm-workspace` 技能入口。当前版本：`0.1.29`。

最快开始：

```text
使用 $pm-workspace 帮我判断这个产品想法应该怎么推进。请先告诉我当前判断、还缺什么、不补会有什么偏差，以及补齐后能产出什么。
```

PMWorkspace 的用户心智只有四个动作：**对齐、出图、复审、交付**。它不会把一句“帮我做个原型”直接变成图片，而是先确认真实问题、目标用户、当前替代、主目标、反指标、不可虚构项和必要证据；产品简报对齐后，再生成移动端优先的 image-2 原型图；原型复审通过后，再整理成产品设计文档、精简 PRD 或交付稿。

简单说：**先用最少材料拿到可讨论方案；需要交付时，再把事实、截图、风险和复审补齐**，产出能评审、能交给设计 / 研发继续推进的文档。

## 四个动作

| 动作 | 你得到什么 | 什么时候用 |
|---|---|---|
| **对齐** | 工作方式卡片、产品作业卡、产品简报或可讨论方向。 | 有新想法、截图反馈、PRD、用户洞察，但还不知道真实问题、范围或下一步。 |
| **出图** | 每个方案 / 每个屏幕单独生成一张 image-2 原型图。 | 产品简报已对齐，需要至少 3 条有差异的移动端优先原型方向。 |
| **复审** | 检查图片是否符合 brief、反指标、不可虚构项、线上参考和设计系统。 | 已有原型图，要判断可通过、重出、补参考还是需要 PM 拍板。 |
| **交付** | 产品设计文档、精简 PRD、实验或研发交付材料。 | 方向和原型已确认，需要交给设计、研发、业务评审或后续协作。 |

你可以只说想做哪一步，PMWorkspace 会自动判断当前最早门槛：如果还没对齐，就先对齐；如果可出图，就进入 image-2；如果图已生成，就先复审；如果复审通过，就进入交付。

## 适合谁

- 产品经理：把想法、反馈、数据和截图整理成可评审方案。
- 设计师：在出图前拿到目标用户、边界、反指标和产品判断。
- 研究、运营、业务团队：把访谈、客服记录、运营诉求转成产品机会。
- 创业者和负责人：快速得到可讨论的产品方向、假设和下一步验证。
- 需要交付的团队：把已对齐 brief、原型和复审结论整理成 PRD 或设计交付。

## 如何安装 PMWorkspace

### 方式一：Codex 插件安装

适合普通用户。

1. 打开 Codex 的 `Plugins`。
2. 搜索并安装 **AI 产品工作站**。
3. 安装后从 `$pm-workspace` 开始。

### 方式二：GitHub 本地插件 / 团队测试

适合公开上架前试用、团队测试或从 GitHub 仓库安装。

```bash
codex plugin marketplace add stephenfan80/PMWorkspace
```

如果之前添加过旧版本或本地路径：

```bash
codex plugin marketplace remove pmworkspace
codex plugin marketplace add stephenfan80/PMWorkspace
```

然后重启 Codex，在 `Plugins` 中把筛选切到 `All`，搜索 **AI 产品工作站** 或 `PMWorkspace`，安装 / 启用后使用 `$pm-workspace`。

### 方式三：开发者本地仓库

适合维护者和本地开发。

```bash
git clone https://github.com/stephenfan80/PMWorkspace.git
cd PMWorkspace
bin/pmw-upgrade --host codex-plugin
```

## 如何更新 PMWorkspace

### 公开 Codex 插件用户

在 Codex `Plugins` 里更新 **AI 产品工作站**。这是公开插件用户的默认更新方式。

### GitHub 本地插件用户

先检查版本：

```bash
bin/pmw-version --check
bin/pmw-update-check --quick
```

如果检查输出 `UPGRADE_AVAILABLE` 和 `UPGRADE_COMMAND`，运行输出里的升级命令。常见命令是：

```bash
bin/pmw-upgrade --host codex-plugin
```

升级会替换 PMWorkspace 插件包，不会删除 `~/.pmworkspace/` 里的项目状态、产品简报、原型、交付稿或审计记录。

### 开发者本地仓库

```bash
git pull
bin/pmw-build-plugin
bin/pmw-upgrade --host codex-plugin
bin/pmw-version --json
```

详细升级契约见 `pmworkspace-shared/references/update-workflow.md` 和 `docs/codex-plugin-submission.md`。

## 快速开始

先选一个动作即可：**对齐、出图、复审、交付**。如果你不确定，就从 `$pm-workspace` 开始，它会把请求路由到当前最早该处理的门槛。

### 新想法

```text
使用 $pm-workspace 处理一个新想法。请先判断它是否值得继续，再帮我整理成可讨论的产品说明和至少 3 个方案方向。

产品想法：<一句话描述>
目标用户：<谁在什么场景最需要>
当前替代：<用户现在怎么解决>
已知约束：<业务 / 数据 / 设计 / 上线范围>
参考材料：<竞品 / 截图 / PRD / 协作文档，可为空>
我想要的结果：<讨论稿 / 原型 / PRD / 交付稿>
```

### 优化已有功能

```text
使用 $pm-workspace 帮我优化一个已有功能。请先基于截图、线上参考或现有反馈判断问题区域，再告诉我应该怎么改。

当前页面或流程：<页面 / 功能 / 链路>
线上材料：<截图 / 关键节点截图 / URL / Figma>
核心问题：<用户或业务现在卡在哪里>
目标：<希望提升的行为或指标>
约束：<数据 / 业务 / 法务 / 设计系统 / 上线范围>
我想要的结果：<讨论稿 / 原型 / PRD / 交付稿>
```

已有功能迭代需要生产截图、关键节点截图、线上 URL、Figma / 设计稿或等价视觉基线。缺少基线时，PMWorkspace 会先说明为什么这会影响问题区域、保留项、可改项和原型可信度，而不是直接生成三套图。

如果你要原型或 PRD，也可以直接写在“我想要的结果”里。PMWorkspace 会先确认产品说明、线上参考、方案差异和不能虚构的内容，再继续出图或交付。

## 工具箱

### 四个用户动作

| 用户说法 | PMWorkspace 会做什么 | 常用入口 |
|---|---|---|
| “帮我想清楚 / 整理成方案 / 看是否值得做” | **对齐**：判断全新功能或已有功能迭代，补齐真实问题、当前替代、目标、反指标和产品简报。 | `$pm-workspace`、`$pm-autoplan`、`$pm-jobs`、`$pm-brief` |
| “我要原型图 / 多个方向 / 每个方案单独出图” | **出图**：先检查产品简报和 Product Readiness Dashboard，再用 image-2 单方案单屏出图。 | `$pm-prototype-shotgun` |
| “帮我看看这几张图能不能用 / 需不需要重出” | **复审**：用四个可插拔专家检查策略、信任 / 风险、设计系统和数据可行性。 | `$pm-prototype-review` |
| “整理成 PRD / 交给研发 / 做评审材料” | **交付**：把已对齐 brief、原型和复审结论整理成产品设计文档或精简 PRD。 | `$pm-handoff` |

### 底层技能

| 工具 | 它做什么 | 什么时候用 |
|---|---|---|
| `$pm-workspace` | 主入口。判断全新功能 / 已有功能迭代，建立工作方式卡片，并路由到最早门槛。 | 不确定从哪里开始，或刚安装后想启动 PMWorkspace。 |
| `$pm-autoplan` | 自动产品评审。按推荐链路推进，但只在会改变方向的关键点让你拍板。 | 想“一次跑完整产品评审”，或想从想法推进到 brief / 原型前。 |
| `$pm-jobs` | 产品方向审查内核。审前提、找现状替代、推演不做损失、整理路径对比。 | 只有想法、反馈或截图，还不知道真实问题是否成立。 |
| `$pm-strategy-review` | 产品方向审查。挑战范围、价值交换、风险和本周期验证。 | 方向、范围、承诺或策略取舍不稳时。 |
| `$pm-brief` | 产品简报生成器。把已确认判断写成出图 / 交付前的产品契约。 | 需要一份可沉淀、可复用、可指导原型的产品简报。 |
| `$pm-prototype-shotgun` | image-2 原型出图导演。把已对齐 brief 拆成多条产品路径和单图输出。 | 产品简报已对齐，需要多方案原型图。 |
| `$pm-prototype-review` | 原型复审。检查图片是否符合 brief、反指标、不可虚构项和设计系统。 | image-2 原型图生成后，进入评审或交付前。 |
| `$pm-handoff` | 产品交付。生成产品设计文档、精简 PRD 或交付稿。 | 方向和原型已确认，需要交给设计、研发或评审会。 |

### 维护 / 审计命令

| 命令 | 用途 |
|---|---|
| `bin/pmw-version --json` | 查看本地 PMWorkspace 版本和 revision。 |
| `bin/pmw-update-check --quick` | 快速检查是否有更新。 |
| `bin/pmw-dashboard status` | 查看当前项目的简洁状态。 |
| `bin/pmw-dashboard readiness --target prototype` | 出图前检查产品简报、线上参考、方案差异和不可虚构项；默认只输出一句人话 verdict。 |
| `bin/pmw-dashboard readiness --target handoff` | 交付前检查 brief、复审和交付门槛；默认只输出一句人话 verdict。 |
| `bin/pmw-artifact flow` | 查看产品资产流。 |
| `bin/pmw-artifact latest --kind product_brief` | 读取最新产品简报资产。 |
| `bin/pmw-prototype-board list` | 查看多方案原型比较板。 |
| `bin/pmw-zoon drift --url "<Zoon URL>"` | 检查在线协作文档是否和本地 brief 漂移。 |
| `bin/pmw-eval run` | 运行行为契约测试。 |
| `bin/pmw-gen-skill-docs check` | 检查 skill 共享契约是否和 manifest 一致。 |

## 工具路径图

从用户视角看，PMWorkspace 只有四段主线：

```text
对齐 -> 出图 -> 复审 -> 交付
```

### 1. 新想法到可讨论方案

```text
对齐：一句想法
-> $pm-workspace 判断产品路径
-> $pm-jobs 审查真实问题、当前替代和损失
-> $pm-strategy-review 挑战范围和本周期验证
-> $pm-brief 生成待确认 / 已对齐产品简报
-> 可讨论方案 / 三条产品路径
```

### 2. 新想法到 image-2 原型

```text
对齐：产品想法
-> 产品方向审查
-> 产品简报确认：已对齐
出图：
-> Product Readiness Dashboard：可出图
-> $pm-prototype-shotgun 逐张生成 image-2 原型图
复审：
-> $pm-prototype-review 复审
```

### 3. 已有功能迭代到原型

```text
对齐：线上页面 / 反馈 / 数据
-> 补生产截图、关键节点截图、URL、Figma 或视觉基线
-> 线上基线拆解：保留项 / 可改项 / 问题区域
-> $pm-brief 写入最新证据并确认
出图：
-> physical_longboard 或截图编辑模式出图
复审：
-> 原型复审
```

### 4. 已确认方向到交付

```text
对齐：已对齐产品简报
出图：
-> 已选原型方向
复审：
-> 原型复审：可通过
交付：
-> $pm-handoff 生成产品设计文档 / 精简 PRD
-> 可选同步到 Zoon 在线协作文档
```

README 只保留用户能理解的路径图。完整端到端工作台地图、阶段索引和状态字段由 `pmworkspace-shared/references/pm-workbench-map.md` 维护。

## 知识库 / 方法库 / 运行协议

`pmworkspace-shared/references/` 是 PMWorkspace 的方法库和运行协议层。它不是让普通用户逐个阅读的杂项文件；普通用户只需要从本 README 和 `$pm-workspace` 开始。需要理解内部文件时，先看 `pmworkspace-shared/references/README.md`，它已经把 references 拆成两层：

- **方法库**：解释 PMW 如何做产品判断、写产品简报、设计原型、复审方案和交付 PRD。
- **运行协议**：解释 PMW 如何路由、记录 run、管理资产流、检查准备度、同步 Zoon、评估和升级。

### 方法库：PMW 怎么做产品判断和产出

| 分类 | 代表文件 | 解决什么问题 |
|---|---|---|
| 产品发现 / 对齐 | `product-office-hours.md`、`product-discovery-gate.md`、`scenario-routing.md` | 判断真实问题、当前替代、当前损失、目标和反指标是否足够。 |
| 产品简报 | `product-manager-brief.md`、`product-plan-handoff.md` | 把产品判断压缩成出图 / 交付前的产品契约。 |
| 原型生成 | `image-prompts.md`、`design-system-workflow.md`、`prototype-shotgun-board.md`、`production-reference-gate.md` | 约束 image-2 单图生成、多方案差异、设计系统和视觉基线。 |
| 原型复审 | `prototype-quality-review.md`、`pm-review-army.md` | 检查原型是否忠实表达产品判断，是否违反不可虚构项。 |
| 产品交付 | `delivery-handoff.md` | 把已对齐 brief 和复审结论整理成产品设计文档或精简 PRD。 |
| 语言与首次使用 | `language-and-localization.md`、`welcome-guide.md`、`first-use-onboarding.md` | 统一中文表达、欢迎引导和第一次使用的心智入口。 |

### 运行协议：PMW 如何不跳步、不丢状态、不泄露隐私

| 分类 | 代表文件 | 解决什么问题 |
|---|---|---|
| 路由 / 工作台地图 | `routing.md`、`pm-workbench-map.md`、`autoplan-workflow.md` | 决定当前动作、下一技能、端到端阶段、共享状态字段和自动推进边界。 |
| 运行状态 / 准备度 | `runtime-kernel.md`、`artifact-flow.md`、`product-readiness-dashboard.md`、`evidence-dashboard.md`、`state-and-telemetry.md` | 管理 run、Product Artifact Flow、Product Readiness Dashboard、本地状态和隐私边界。 |
| 证据 / 线上参考 | `browser-evidence.md`、`production-reference-gate.md` | 登记线上页面、截图、竞品或公开参考，避免已有功能迭代脱离真实视觉基线。 |
| 记忆 / 偏好 | `product-memory.md`、`question-tuning.md` | 沉淀可复用产品学习和 Q/D 追问偏好，但不能覆盖本轮事实。 |
| 协作 / 更新 / eval | `zoon-workflow.md`、`zoon-drift-check.md`、`update-workflow.md`、`pm-eval-system.md`、`skill-doc-template-system.md` | 管理 Zoon 在线协作、漂移检查、版本升级、评估和 skill 文档生成。 |

## PMW 的产品资产流

dbskill 有“原子库”的概念；PMWorkspace 更适合叫 **产品资产流**。PMW 的最小可复用单元不是孤立知识点，而是一条能被下游 skill 读取的 Product Artifact Flow。

普通用户只需要记住 5 个核心资产：

| 公开资产 | 你可以怎么理解 | 什么时候出现 |
|---|---|---|
| `product_brief` | 已对齐产品简报，是出图、复审和交付的事实源。 | 对齐完成后。 |
| `visual_baseline` | 线上截图 / 视觉参考基线，约束尺寸、字号、间距、密度和保留区域。 | 已有功能迭代、截图编辑或需要贴近生产样式时。 |
| `prototype_manifest` | 原型清单，记录每张图属于哪个方案、屏幕、目标和不可虚构边界。 | 出图前后。 |
| `prototype_review` | 原型复审结论，判断可通过、重出、补参考或需要 PM 拍板。 | 图片生成后、交付前。 |
| `handoff` | 交付资产，包含产品设计文档、精简 PRD、实验或研发交付材料。 | 复审通过或方向确认后。 |

其他内部资产是辅助证据或维护记录，不作为用户第一层心智：`browser_evidence` 用来记录线上页面、竞品、Zoon 或公开参考；`repair_brief` 用来指导重出图；`product_design_doc`、`acceptance_seed` 和 `release_doc_seed` 是交付阶段的细分登记类型。它们仍在 Product Artifact Flow 里，但默认只出现在审计、调试或维护说明中。

常用查看命令：

```bash
bin/pmw-artifact flow
bin/pmw-artifact flow --details
bin/pmw-artifact latest --kind product_brief
bin/pmw-artifact latest --kind prototype_review
```

维护者或证据采集场景可以手动登记辅助证据：

```bash
bin/pmw-artifact add --kind browser_evidence --title "线上参考：结果页" --status "已采集" --source-skill pm-brief --path "<screenshot>" --url "<URL>" --summary "页面任务、视觉基线、交互模式、必须保留、可以挑战"
```

## 原型输出规则

- 默认移动端优先。
- 一个方案 + 一个屏幕 = 一张图。
- 默认至少 3 个方案；少于 3 个必须有明确豁免原因。
- 多方案必须在产品策略、信息架构、交互模型、信任模型或关键任务路径上不同，不能只是换配色。
- 产品简报没有 `已对齐` 前，不写 image-2 提示词，不生成图片，不输出交付稿。
- 设计原型默认使用 image-2 / 图像生成。HTML 只在你明确要求“HTML / 可交互网页 / 前端实现 / 本地网页原型”时使用。
- 用户提供截图或线上参考时，只更新视觉基线和参考状态，不自动产出完整方案、HTML 或原型图。
- 已有生产截图 / `visual_baseline` 时，默认使用物理像素长板或截图编辑模式，不能随意重画整页。

## 你会拿到什么

- **工作方式卡片：** 产品路径、对齐深度、当前任务、缺口和下一步。
- **产品作业卡：** 已知事实、暂定判断、证据边界、用户作业和补齐后解锁。
- **产品简报：** 出图和交付前的短版产品契约。
- **多方案方向：** 至少 3 条有本质差异的产品路径。
- **移动端原型图：** 一个方案 / 一个屏幕 / 一张 image-2 图片。
- **原型复审：** 策略、信任 / 风险、设计系统、数据可行性四个可插拔专家的复审结论；深度交付、高风险、批量交付、研发交付或多角色 review 时，追加 CEO、Eng、Design、DX、安全、QA、发布工程师短结论。
- **交付稿：** 产品设计文档、精简 PRD、实验或研发交付材料。

## Zoon 在线协作

PMWorkspace 默认本地优先。产品简报、原型清单、复审和交付稿会先保存在本地 `~/.pmworkspace/`。Zoon 是可选的在线协作层，适合多人评审、团队在线修改和后续防漂移。

常用命令：

```bash
bin/pmw-zoon join --url "<协作文档 URL>"
bin/pmw-zoon drift --url "<协作文档 URL>"
bin/pmw-zoon read --url "<协作文档 URL>"
```

PMWorkspace 不会在产品简报未对齐时自动创建 Zoon 文档；只有用户选择同步、提供现有 Zoon URL，或任务明确需要多人在线协作时才会创建或更新。

## 本地状态和隐私

PMWorkspace 默认把资产保存在本地 `~/.pmworkspace/`，包括业务简报、本地审计副本、用户确认过的决策、协作文档链接、产物流动记录、复审专家短结论、原型清单、交付稿、脱敏交付事实、偏好反馈和本地使用日志。

不会保存 token、owner secret、API key、cookie、原始客户资料、内部材料、会议记录、敏感截图、未脱敏协作文档内容或 API 原始响应。默认遥测是本地优先，只写入 `~/.pmworkspace/analytics/usage.jsonl`；远程匿名汇总必须由用户明确开启。

## 维护者说明

### 维护命令

```bash
bin/pmw-eval list
bin/pmw-eval run
bin/pmw-build-plugin
bin/pmw-gen-skill-docs write
bin/pmw-gen-skill-docs check
```

### 维护规则

- 改 PMW 的用户心智、默认输出或产物命名时，先稳定 README / references 的产品表达，再更新生成契约，最后补 eval；不要先改 eval 反向牵着产品表达走。
- 共享契约区块由 `bin/pmw-gen-skill-docs write` 从 manifest 生成，不要手写生成区块。
- 改动 source skill、`pmworkspace-shared/references`、`bin`、`evals`、README 或插件 assets 后，运行 `bin/pmw-build-plugin`，并把插件副本变化一起提交。
- README 只讲用户入口、工具箱、路径图、方法库和资产流；完整路由和阶段字段由 `pmworkspace-shared/references/` 维护。
- 发布、插件打包、旧版 skill 迁移和提交说明见 `docs/codex-plugin-submission.md`。

## 许可证

MIT

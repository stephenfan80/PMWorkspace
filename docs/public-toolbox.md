# PMW 公开工具目录

这份目录只解决一个问题：**我应该用哪个入口？**

- 普通用户入口是 `$pm-*`：在 Codex 对话里调用，用来完成产品工作。
- 维护者 / 审计入口是 `bin/pmw-*`：在仓库或本机终端运行，用来检查状态、维护插件、验证契约。

普通用户不需要先学命令行。你只要从 `$pm-workspace` 开始，PMWorkspace 会判断当前应该先对齐、出图、复审还是交付。

## 普通用户入口：$pm-*

| 入口 | 一句话用途 | 什么时候用 | 常见下一步 |
|---|---|---|---|
| `$pm-workspace` | 主入口，判断任务类型并路由到最早门槛。 | 不确定从哪里开始；刚安装后第一次使用；有想法、截图、PRD 或反馈。 | `$pm-autoplan`、`$pm-jobs`、`$pm-brief` |
| `$pm-autoplan` | 自动产品评审，只把关键取舍交给用户拍板。 | 想让 PMW 主动推进完整链路，但不希望它替你决定方向。 | `$pm-jobs`、`$pm-strategy-review`、`$pm-brief` |
| `$pm-jobs` | 产品方向审查内核，判断真实问题、当前替代和现状损失。 | 想法还模糊，或者只知道“想做一个功能”。 | `$pm-strategy-review`、`$pm-brief` |
| `$pm-strategy-review` | 审范围、价值交换、风险、承诺和本周期验证。 | 方向大致有了，但范围、策略或承诺边界不稳。 | `$pm-brief` |
| `$pm-brief` | 生成或更新产品简报，作为出图和交付的事实源。 | 已有产品判断，需要沉淀成可确认、可复用的 brief。 | `$pm-prototype-shotgun`、`$pm-handoff` |
| `$pm-prototype-shotgun` | 基于已对齐 brief，用 image-2 逐张生成原型图。 | 产品简报已对齐，需要至少 3 个移动端方案方向。 | `$pm-prototype-review` |
| `$pm-prototype-review` | 复审原型是否符合 brief、反指标、不可虚构项和设计系统。 | 原型图已经生成，准备决定通过、重出、补参考或拍板。 | `$pm-handoff`、重新出图 |
| `$pm-handoff` | 输出产品设计文档、精简 PRD、实验或研发交付稿。 | brief、原型方向和复审结论已经能支持交付。 | 设计 / 研发 / 业务评审 |

## 普通用户怎么选

| 你现在的状态 | 直接用 |
|---|---|
| “我只有一句产品想法。” | `$pm-workspace` |
| “我想让 PMW 自动推进，但关键点问我。” | `$pm-autoplan` |
| “我不知道这个需求到底值不值得做。” | `$pm-jobs` |
| “我已经有方向，但怕范围或承诺不对。” | `$pm-strategy-review` |
| “我需要一份可确认的产品简报。” | `$pm-brief` |
| “我想要 3 个移动端原型方向，每个方案单独出图。” | `$pm-prototype-shotgun` |
| “我已经有原型图，想判断能不能交付。” | `$pm-prototype-review` |
| “我要 PRD / 设计交付 / 研发交付。” | `$pm-handoff` |

## 维护者 / 审计入口：bin/pmw-*

下面这些命令主要给维护者、审计流程和高级排障使用。普通产品工作不需要先运行它们。

### 安装、更新和版本

| 命令 | 用途 |
|---|---|
| `bin/pmw-version --json` | 查看本地 PMWorkspace 的 `VERSION@REVISION` 身份。 |
| `bin/pmw-version --check` | 检查版本身份是否完整。 |
| `bin/pmw-update-check --quick` | 快速检查远端是否有更新。 |
| `bin/pmw-upgrade --host codex-plugin` | 升级本机 Codex plugin 安装。 |
| `bin/pmw-upgrade --host codex` | 升级本机 Codex skills 安装。 |
| `bin/pmw-build-plugin` | 从源码刷新 `plugins/pmworkspace` 插件包。 |
| `bin/pmw-revision` | 计算应该写入插件包的 source revision。 |
| `bin/pmw-snooze-update` | 临时延后更新提醒。 |

### 项目状态、准备度和产品资产流

| 命令 | 用途 |
|---|---|
| `bin/pmw-dashboard status` | 查看当前项目的简洁状态。 |
| `bin/pmw-dashboard readiness --target prototype` | 出图前准备度检查，默认只输出一句人话 verdict。 |
| `bin/pmw-dashboard readiness --target handoff` | 交付前准备度检查，默认只输出一句人话 verdict。 |
| `bin/pmw-dashboard readiness --target prototype --details` | 展开证据表，用于审计或调试。 |
| `bin/pmw-artifact flow` | 查看 Product Artifact Flow。 |
| `bin/pmw-artifact flow --details` | 展开资产流详情。 |
| `bin/pmw-artifact latest --kind product_brief` | 读取最新产品简报资产。 |
| `bin/pmw-artifact latest --kind prototype_review` | 读取最新原型复审资产。 |
| `bin/pmw-artifact add --kind browser_evidence ...` | 手动登记线上截图、竞品参考或浏览器证据。 |
| `bin/pmw-prototype-board list` | 查看多方案原型输出单元。 |

### 运行内核和本地记录

| 命令 | 用途 |
|---|---|
| `bin/pmw-controller intake` | 建立任务 revision、产品路径和 controller 状态。 |
| `bin/pmw-controller next` | 读取下一步门槛和推荐路由。 |
| `bin/pmw-run start` | 创建本轮运行记录。 |
| `bin/pmw-run gate` | 记录门槛状态。 |
| `bin/pmw-run decision` | 记录 Q / D 拍板结果。 |
| `bin/pmw-run artifact` | 记录本轮产物。 |
| `bin/pmw-run finish` | 标记运行结束。 |
| `bin/pmw-log brief` | 保存产品简报并登记产品资产流。 |
| `bin/pmw-log handoff` | 保存交付稿并登记产品资产流。 |
| `bin/pmw-project` | 查看或维护当前项目指针。 |
| `bin/pmw-config` | 查看或维护 PMW 本地配置。 |
| `bin/pmw-slug` | 把项目名转成安全 slug。 |
| `bin/pmw-welcome` | 输出安装后的欢迎和启动提示。 |

### 出图、截图和复审审计

| 命令 | 用途 |
|---|---|
| `bin/pmw-discovery-gate check` | 检查产品发现 / brief 是否满足目标门槛。 |
| `bin/pmw-image-preflight check` | 出图前检查 brief、方案数量、输出单元和图片绑定。 |
| `bin/pmw-image-audit baseline` | 登记或检查视觉基线。 |
| `bin/pmw-prototype-prompt-check` | 检查 image-2 prompt 是否符合单图、单方案和不可虚构契约。 |
| `bin/pmw-review-specialist` | 运行可插拔复审专家短结论。 |
| `bin/pmw-memory` | 管理脱敏的产品偏好和项目学习。 |
| `bin/pmw-question-tuning` | 沉淀用户对 Q / D 追问方式的偏好。 |

### Zoon 协作

| 命令 | 用途 |
|---|---|
| `bin/pmw-zoon join --url "<Zoon URL>"` | 绑定已有 Zoon 协作文档。 |
| `bin/pmw-zoon read --url "<Zoon URL>"` | 读取 Zoon 内容用于对齐或审计。 |
| `bin/pmw-zoon drift --url "<Zoon URL>"` | 检查 Zoon 与本地 brief 是否发生实质漂移。 |

### 质量、生成契约和发布

| 命令 | 用途 |
|---|---|
| `bin/pmw-eval list` | 查看全部行为契约 fixtures。 |
| `bin/pmw-eval run --suite smoke` | 日常小改先跑，确认主链路没断。 |
| `bin/pmw-eval run --suite core` | 改 skill、references、readiness 或资产流时跑。 |
| `bin/pmw-eval run --suite full` | 发布 GitHub / plugin 前跑全量。 |
| `bin/pmw-gen-skill-docs write` | 从 manifest 生成 SKILL.md 共享契约区块。 |
| `bin/pmw-gen-skill-docs check` | 检查 SKILL.md 生成区块是否漂移。 |

## 边界

- `$pm-*` 是用户入口，负责完成产品工作。
- `bin/pmw-*` 是维护 / 审计入口，负责让 PMW 可追踪、可检查、可发布。
- README 只保留最短启动路径；这份目录保留完整工具索引。
- 运行协议真源仍在 `pmworkspace-shared/references/`，这里不复制内部状态机。

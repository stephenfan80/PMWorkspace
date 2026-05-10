# PMWorkspace 运行逻辑与瘦身审计 - PPT 讲稿

面向对象：PMWorkspace 维护者 / 开发者

讲解目标：讲清楚 PMWorkspace 的运行逻辑、硬门槛、产物流动、插件发布链路，以及本轮瘦身已经完成的修复和后续需要守护的漂移风险。

## 1. 封面

标题：PMWorkspace 运行逻辑与瘦身审计

讲稿：
这份讲解不是用户侧宣传稿，而是维护者视角的系统地图。PMWorkspace 的定位已经从“帮我出一张原型图”升级成“产品方案工作台”：它要先把产品价值判断、事实边界和关键取舍跑通，再把这些判断交给 image-2 原型、复审和交付链路。今天重点看三件事：主链路如何跑、哪些脚本负责挡错、哪些文档正在制造噪声或漂移。

## 2. 一句话系统定位

标题：不是原型捷径，而是产品判断流水线

讲稿：
PMWorkspace 的核心约束是“快速成型，深度交付”。快速成型允许基于假设出轻量包，但要标明假设和反指标；深度交付则必须先完成产品发现、简报确认、准备度检查，再进入图片或 PRD。这个定位决定了系统里很多看似啰嗦的门槛其实不是装饰，而是为了防止直接把功能愿望画成可信方案。

## 3. 端到端链路

标题：8 个阶段，只有最早门槛能继续

讲稿：
主链路来自 `pm-workbench-map.md`：入口路由、自动评审、产品价值澄清、策略审查、产品简报、原型方案、原型复审、产品交付，再加一层运行 / 产物流动 / 记忆。关键不是把 8 个阶段一次跑完，而是每次只推进到“当前最早可靠门槛”。这能避免用户刚给一个截图，系统就直接写简报、出图、交付，最后看起来很完整但事实不成立。

## 4. 入口与路由

标题：D0 决定工作方式，不决定最终答案

讲稿：
`$pm-workspace` 只负责判断快速成型还是深度交付，并创建或复用 runtime run。它不是第二份业务规则表。具体路由真源在 `routing.md`，阶段真源在 `pm-workbench-map.md`。入口输出必须让用户看到当前模式、为什么这么判定、当前一步和下一步，而不是把模式只藏在审计里。

## 5. 自动评审

标题：$pm-autoplan 是总控，不是跳关器

讲稿：
`$pm-autoplan` 的职责是把推荐链路串起来，但只推进到最早门槛。快速成型遇到生产流程、高风险承诺、真实数据、线索 / 交易 / 隐私或研发交付信号，要升级到深度交付。深度交付的顺序是工作目标、产品价值判断、多轮 Q、多轮 D、前提确认、产品经理简报、本地保存、Zoon A/B 推荐、原型或交付准备度。

## 6. 产品发现硬门槛

标题：一次只问一个，不等于总共只问一个

讲稿：
`pmw-discovery-gate` 是前期两个失败案例的关键修复点。它要求深度交付或线上功能优化在进入简报前覆盖 5 个维度：产品定位与链路角色、目标用户与触发时刻、用户现状与当前替代、真实痛点与当前损失、主目标与反指标。Q 用来补事实，D 用来拍取舍。一个 Q 加一个 D 不能代表产品发现完成。

## 7. 产品经理简报

标题：简报是 PM brief，不是 8 行摘要

讲稿：
当前源头规则已经把 `$pm-brief` 定义成 1-2 页产品经理简报。它要先给核心价值判断，再写背景与现状、目标用户、痛点与当前替代、竞品 / 行业做法、解决思路、范围方向、指标和约束。内部审计继续记录 run、路径、门槛和证据状态，但这些不应挤进业务正文。

## 8. Zoon 工作流

标题：本地事实源优先，Zoon 是协作增强

讲稿：
Zoon 的正确模型是 local-first、Zoon-optional。本地 Markdown 保存成功后，系统必须推荐 Zoon 的协作价值：多人协作、事实源统一、后续 image-2 原型 / PRD 防漂移。但不能自动同步，必须让用户选 A/B。未启用 Zoon 时，Product Readiness Dashboard 应显示“未启用，使用本地简报”，不阻断出图或交付。

## 9. 原型出图链路

标题：readiness -> output unit -> prompt check -> image -> audit

讲稿：
`$pm-prototype-shotgun` 现在是 image-2 出图导演，而不是产品判断补写器。它必须先确认产品简报已对齐，方案方向已确认，输出单元已登记，并运行 Product Readiness Dashboard。每个输出单元等于一张图：一个方案、一个屏幕任务、一个主目标、一个反指标和明确不可虚构项。批量只是顺序执行多个单图任务。

## 10. 物理长板规则

标题：有生产截图时，402 x 874 不能进 prompt

讲稿：
长板失败的根因是 prompt 里仍残留 `402 x 874 / H874 / 标准首屏` 这类短画布锚点。现在规则要求：无线上截图时才能用标准移动端首屏；只要有生产截图或 `visual_baseline`，就必须走 `physical_longboard`，写参考图物理尺寸和目标输出像素。`pmw-prototype-prompt-check` 负责在出图前挡掉旧锚点，`pmw-image-audit` 负责在出图后挡掉尺寸不合格的图。

## 11. 原型复审与交付

标题：好看不能覆盖事实错误

讲稿：
`$pm-prototype-review` 先检查输出单元绑定，再用策略、信任 / 风险、设计系统、数据可行性四个专家给短结论。深度交付和高风险场景再追加 CEO、Eng、Design、DX、安全、QA、发布工程师视角。任何违反 brief、反指标、不可虚构项、线上参考或长板尺寸的图，都要标记需要重出。`$pm-handoff` 只在 brief 已对齐、复审可通过、关键 D 已拍板后生成精简 PRD。

## 12. 运行时内核

标题：脚本把“应该”变成“不能越过”

讲稿：
这一套系统真正可靠的地方不在 skill 文案，而在运行时脚本：`pmw-run` 管 run，`pmw-log` 记 discovery / brief / prototype / handoff，`pmw-artifact` 管产物流动，`pmw-dashboard` 做准备度，`pmw-prototype-board` 绑定输出单元，`pmw-prototype-prompt-check` 和 `pmw-image-audit` 管长板出图。文案可以提示模型，脚本才是硬门槛。

## 13. 回归与插件发布

标题：manifest 生成 skill，eval 防行为退化

讲稿：
共享契约不是手写在每个 SKILL.md 里，而是由 `pmworkspace-shared/skill-docs/skill-docs.manifest.json` 生成，再用 `pmw-gen-skill-docs check` 检查。行为回归靠 `pmw-eval` 的 fixtures。发布链路是：改 source skill / references / bin / eval，检查生成契约，运行 eval，再用 `pmw-build-plugin` 同步到插件副本。这个链路要继续保持，否则本地 source 和 Codex plugin 会漂。

## 14. 已完成的瘦身修复

标题：修规则，更要修真源

讲稿：
本轮已经处理完 D1-D17：README 的产品简报和 Zoon 口径改成 PM brief + local-first；长板出图真源收敛到 `image-prompts.md` 和 `prototype-shotgun-board.md`；`pm-eval-system.md` 回到测试契约；`product-office-hours.md` 拆出案例附录；孤岛 reference 已合并、移位或保留；`SKILL.md` 共享门槛由 manifest / generator 压缩输出。最新补强是把 image-2 画布模板拆成互斥模式，避免把 `402 x 874` 和物理长板写进同一个 prompt 字段。

## 15. 后续守护点

标题：不要让旧锚点回来

讲稿：
后续不是继续沿 D1-D17 往下拆，而是重新审计 D18+。优先守住四件事：第一，产品发现必须靠 `pmw-discovery-gate`，不能退回一个 Q/D 后写已对齐简报；第二，有视觉基线时 final prompt 不能出现短画布锚点；第三，artifact-only commit 不需要刷新插件 REVISION，只有 source skill、references、bin 或 eval 影响插件包时才 build；第四，PPTX、讲稿和审计报告既然是交付物，就要纳入版本控制，不能长期漂在未跟踪状态。

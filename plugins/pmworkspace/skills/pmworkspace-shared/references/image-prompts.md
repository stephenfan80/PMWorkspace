# 图片提示词模板

仅在产品简报已对齐、产品路径已确认，并且当前任务通过 `pmw-controller preflight --target prototype` 与 `pmw-image-preflight check` 后，才把这些模板用于 `imagegen` / 内置图像生成。`$pm-prototype-shotgun` 是 image-2 原型出图导演：每个提示词只对应一个屏幕，每张图只对应一个产品路径。

```text
一次 image-2 调用 = 一张图 = 一个产品路径 + 一个屏幕任务
```

批量生成只是顺序执行多个单图任务，不是一次生成多图。每次 image-2 调用必须独立提示、独立产物、独立记录状态。

For Chinese users, keep planning notes, output contracts, final summaries, and generated UI copy in Simplified Chinese. The prompt may keep precise technical terms such as `image-2`, `UI`, `token`, `API`, device names, colors, and component names when useful for image quality.

## 原型方案控制器

`$pm-prototype-shotgun` 写图片提示词或调用 image-2 前，先建立原型方案控制器。控制器至少记录：

- `产品简报来源`：已对齐产品简报版本、Zoon URL / 快照状态、最新漂移检查结论。
- `Controller Preflight`：用 `pmw-controller preflight --target prototype --json` 确认当前 run / `task_digest` / `input_revision` 可进入出图准备；返回 STOP gate 时停止。
- `Product Readiness Dashboard`：用 `pmw-dashboard readiness --target prototype` 统一检查产品简报、Zoon、线上参考、方案差异、不可虚构项和复审状态；verdict 不是 `可出图` 时停止。默认只展示短 verdict 和第一阻断原因，完整表格只在审计 / 调试时展开。
- `图片生成前门槛`：产品简报已对齐、Zoon 无实质漂移、线上参考门槛通过、设计系统已载入、image-2 可用。
- `视觉基线`：当用户提供线上截图或生产视觉参考时，必须登记 `visual_baseline`，记录参考图路径、像素尺寸、逻辑宽度推断、目标输出像素、核心字号层级、页面边距、模块间距、底部栏高度和参考优先级。
- `生产基线改动证明`：当存在 `visual_baseline` 时，每个输出单元必须说明当前线上问题、改动区域、为什么优于当前线上、保留 / 删除边界。证明不成立时，不写 image-2 prompt。
- `生成模式`：视觉还原优先、现有生产截图或截图修改任务默认使用 `screenshot_edit`；不得从零重绘整页。若产品探索或大幅重构确实需要 `redraw`，先回到 `$pm-brief` / `$pm-strategy-review` 让用户显式确认重构范围，再作为新的产品简报版本推进。
- `方案差异质量`：默认最少 3 条产品路径；每条路径差异来自产品策略、信息架构、交互模型、信任模型或关键任务路径；如果只是配色、圆角、插画、卡片皮肤不同，停止并重拟方向。少于 3 条路径必须有明确豁免原因。
- `产品路径 / 原型思考`：每条路径必须写明它相信什么用户行为、要赢过哪个现状替代、解决什么当前损失、主动删除 / 牺牲 / 后置什么、验证信号、失败信号、为什么这样设计、信息架构如何组织、如何帮助用户解决问题、解决哪个反指标风险，以及哪些内容不可虚构。
- `原型设计完整度`：每条产品路径在写 image-2 prompt 前必须给出 0-10 评分、为什么是这个分数、距离 10/10 的最大设计差距、10/10 原型标准、本轮 prompt 如何补齐、反 AI 模板味约束、状态覆盖策略和第一眼 / 第二眼 / 第三眼信息层级。快速成型可以低分继续，但必须标记 `基于假设，可讨论`，不能包装成设计已完成。
- `设计规范目标`：每个输出单元必须声明目标来自用户提供规范、AutoDesign、平台模式库或 PMW 默认假设，并写清平台模式、灵感来源摘要、不可照搬项和版权边界。Dribbble / Pinterest / 平台参考只能转成抽象设计原则，不能复制图片、文案、品牌素材或专有 UI。
- `方案方向确认`：用户已确认方向，或明确批准使用默认方向；未确认时只输出方向和取舍，不写图片提示词。
- `输出单元清单`：把每个 `方案 + 屏幕任务` 拆成一张独立图片，并绑定当前 run、`task_digest`、`input_revision`、主目标、反指标、不可虚构项、产品简报版本、线上参考状态、设计系统、image-2 状态和画布。
- `方案比较板写入`：生成前用 `pmw-prototype-board add` 登记计划单元，生成后补充图片路径或 URL；脚本不可用时在输出中标记原因。
- `生成后复审`：每批图片后运行 `prototype-quality-review.md`，实质问题交给 `$pm-prototype-review`。
- `证据状态`：产品简报、Zoon、线上参考、设计系统、方案方向、输出单元、方案比较板和图片资产的状态。

如果任一图片生成前门槛未通过，停止在对应门槛，不写 image-2 提示词，不生成图片，不用 HTML、Markdown 线框、拼贴图或比较板替代。

## 单图生成协议

- 一次 image-2 调用只能对应一张图、一个产品路径和一个屏幕任务。
- `3 条产品路径` 必须拆成 3 个输出单元并连续执行 3 次 image-2。
- `3 条产品路径 x 2 个屏幕` 必须拆成 6 个输出单元并连续执行 6 次 image-2。
- 每个输出单元单独写 prompt，不能把多个方案或多个屏幕合成一个 prompt。
- 每次 prompt 必须写明：只生成一张独立移动端产品界面，禁止拼图、三联图、并排比较、一图多屏、一图多方案和故事板。
- 每张图独立记录状态：`计划生成`、`已生成`、`生成失败`、`待重试` 或 `需要重出`；批量成功不能掩盖单张失败。
- 单张失败时只重试或重出受影响输出单元，不能把其他已生成图片合并成替代物。

## 提示词前置门槛

以下条件全部成立前，不要写图片提示词：

- `$pm-jobs` 已产出产品意图摘要。
- 工作目标模式、Q 诊断、前提确认和必要 D 拍板已经完成。
- 变化类型已判断为新功能或现有功能迭代。
- 现有功能迭代已包含当前生产截图或等价基线证据。
- 已提供线上截图或生产视觉参考时，已登记 `visual_baseline`，且其中包含目标输出像素；缺视觉基线或缺目标像素时，不写 image-2 prompt。
- 已提供线上截图或生产视觉参考时，已完成 `线上基线接收` 和 `生产基线改动证明`；截图上传只代表有参考，不代表新方案已经比线上更好。
- 已读取 `production-reference-gate.md`，并判断新页面是否承接线上流程、结果状态或生产样式。
- 如果新页面需要线上参考，用户已提供参考，或已明确确认没有线上参考并批准按概念稿推进。
- 对话或 Zoon 中已有快速版、标准版或深度版产品简报。
- 产品简报已通过用户确认、最新 Zoon 编辑确认，或明确批准假设而达到“已对齐”。
- 产品简报、用户确认、visual_baseline、prototype-board 输出单元都匹配当前 run / `task_digest` / `input_revision`；旧产物只能参考，不能放行本轮。
- 多方案任务已有至少 3 条命名产品路径，并得到用户确认或批准作为默认方向；少于 3 条路径时已记录豁免原因。
- 输出计划已经把每个方案/屏幕映射为一张独立图片，不把多个方案合成一张比较图。
- 每张图片已经绑定方案名、屏幕任务、主目标、反指标、不可虚构项、产品简报版本、线上参考状态、设计系统和 image-2 状态。
- 每条路径已经写入 `产品路径`、`用户行为假设`、`要赢过的现状替代`、`当前损失`、`删除 / 牺牲 / 后置项`、`验证信号`、`失败信号`、`原型思考`、`信息架构设计思考`、`用户问题解决逻辑`、`反指标保护` 和 `不可虚构边界`。
- 每条路径已经写入 `设计完整度评分`、`主要设计差距`、`10/10 原型标准`、`prompt 设计修正方向`、`反 AI 模板味约束`、`状态覆盖` 和 `第一眼 / 第二眼 / 第三眼信息层级`；如果缺失，先补原型设计完整度，不写 image-2 prompt。
- 每个输出单元已经写入 `设计规范目标`、`设计系统 / 平台模式`、`灵感来源摘要` 和 `禁止照搬项`；如果设计规范不明确，先给用户设计规范目标卡，或得到用户确认后按 PMW 默认假设继续。
- 每个输出单元已经登记到 Prototype Shotgun Board，或已说明脚本不可用的原因。
- 画布决策遵循移动端优先但必须二选一：无线上截图时使用 `standard_first_screen` 模板；有线上截图 / `visual_baseline` 时使用 `physical_longboard` 模板。最终 image-2 prompt 只写当前模式的正向画布字段，不复制另一种模式的短画布锚点。
- 汽车之家 / AutoDesign 生产页必须声明 `参考截图尺寸`、截图倍率和 `目标输出画布`；线上截图基线覆盖泛化 token。目标默认使用参考截图原始物理像素长板，例如 `1179 x 2556 = 393pt @3x`；字体、间距、卡片和底部栏按参考物理像素比例等比执行。只有显式 override 目标宽度时才允许改宽，并必须同步等比缩放字号、间距和组件。
- 视觉还原优先的线上截图任务必须使用 `screenshot_edit`：以参考截图为底，只修改目标区域，保留状态栏、顶部导航、车系头图、车型切换、tab 和底部吸底 CTA；不得从零重绘整页。
- 视觉基线下的每个输出单元必须写清：当前线上问题、改动区域、为什么优于当前线上、保留 / 删除边界。不能只写“更现代、更清爽、更高级”，也不能把线上已经更好的方案替换成 Agent 自己想象的重设计。
- 已通过 `design-system-workflow.md` 确定并确认设计规范目标。
- 产品方向审查中的实质改动已写回产品简报。
- 已运行 Product Readiness Dashboard，且出图前 required 行的 verdict 是 `可出图`。
- 已运行 `pmw-image-preflight check --json`，且返回 `ALLOW_IMAGE_PROMPT`。PMW 无法拦截宿主级 `imagegen` 工具，但绕过 preflight 的图片不能登记为 prototype artifact、不能复审、不能交付。

## 媒介锁

PMWorkspace 的设计原型默认使用 `image-2` / 图像生成。不要用 HTML、Markdown 线框、拼贴图或比较板替代原型图，除非用户明确要求“HTML”“可交互网页”“前端实现”或“本地网页原型”。

如果当前环境不能生成 image-2 图片，停止并说明无法出图；不要改用 HTML 来制造交付感。

## 方案方向确认

Before generating multiple schemes, present concise product-path directions:

```text
方案方向：
A. <名称> - <产品路径；相信的用户行为；要赢过的现状替代；解决的当前损失；删除 / 牺牲 / 后置项；验证信号；失败信号；信息架构依据；用户问题解决逻辑>
B. <名称> - <产品路径；相信的用户行为；要赢过的现状替代；解决的当前损失；删除 / 牺牲 / 后置项；验证信号；失败信号；信息架构依据；用户问题解决逻辑>
C. <名称> - <产品路径；相信的用户行为；要赢过的现状替代；解决的当前损失；删除 / 牺牲 / 后置项；验证信号；失败信号；信息架构依据；用户问题解决逻辑>
```

Directions must include at least 3 product paths by default and differ by product strategy, information architecture, interaction model, trust model, or key task path. Do not offer three visual skins of the same idea. After confirmation, generate each direction/screen as a separate image, even when several images are generated in one batch.

Each direction must also be a different design judgment. At least one of these must differ materially: information hierarchy, interaction model, trust model, state strategy, or subtraction / de-noising strategy. Do not treat three color palettes, three illustration styles, or three card treatments as three directions.

The scheme quality rule is business-agnostic: it applies to lead forms, community, live streaming, product libraries, transaction flows, content screens, tools, and dashboards. Visual style is only the expression inside an approved scheme; it is not the scheme itself.

方案差异质量不通过时，不要降级成“先出几张看看”。先重拟方向，直到差异能映射到产品判断；视觉风格只能作为已确认方案内的表达，不是方案本身。

## 图片输出契约

For every image generation request, declare the output unit before prompting:

```text
图片输出单元：
- 方案：<A/B/C 或方案名>
- 屏幕任务：<屏幕名 + 这个屏幕要帮用户完成什么>
- 产品路径：<这个方案相信什么产品判断会成立>
- 用户行为假设：<它相信什么用户行为会发生>
- 要赢过的现状替代：<用户当前靠什么完成任务，这条路径要比它强在哪里>
- 当前损失：<它主要解决什么损失>
- 删除 / 牺牲 / 后置项：<它主动不做、后置或弱化什么>
- 验证信号：<本周期看到什么说明路径可能成立>
- 失败信号：<看到什么说明路径需要收缩、转向或停止>
- 原型思考：<为什么这样设计>
- 信息架构设计思考：<信息如何组织，优先级如何排序>
- 用户问题解决逻辑：<如何帮助用户解决当前替代/损失>
- 反指标保护：<保护哪个信任、质量或体验风险>
- 生产基线问题：<有 visual_baseline 时必填；当前线上具体哪里影响理解、信任、转化或反指标>
- 改动区域：<有 visual_baseline 时必填；只改哪些模块 / 字段 / 层级>
- 为什么优于当前线上：<有 visual_baseline 时必填；基于截图、数据、用户反馈或 PM 判断说明，不得只写审美词>
- 保留 / 删除边界：<有 visual_baseline 时必填；哪些线上结构必须保留，哪些降级、删除或后置>
- 设计完整度评分：<0-10，并说明为什么是这个分数>
- 主要设计差距：<距离 10/10 最大的 1-2 个设计缺口>
- 10/10 原型标准：<这张图做到什么才算设计完整>
- 本轮 prompt 设计修正：<prompt 将如何补齐信息架构、状态、旅程或信任表达>
- 状态覆盖：<默认 / 加载 / 空态 / 错误 / 成功 / 部分结果如何表达；不适用也要说明>
- 第一眼 / 第二眼 / 第三眼：<用户扫描时分别看到什么>
- 反 AI 模板味约束：<禁止泛卡片、紫蓝渐变、装饰性图标、模板 hero 等具体模式>
- 设计规范目标：<用户提供 / AutoDesign / 平台模式库 / PMW 默认假设>
- 设计系统 / 平台模式：<具体系统或平台模式；不适用时写 PMW 默认移动端产品 UI 基线>
- 灵感来源摘要：<Dribbble / Pinterest / 公开页面 / 用户截图 / 未使用；只写可复用模式>
- 禁止照搬项：<具体图片 / 品牌素材 / 文案 / 专有 UI / 未授权资产>
- 版权边界：<仅抽象启发 / 用户自有规范 / 已授权 / 未授权不可复制>
- 画布模式：<standard_first_screen 或 physical_longboard，只能二选一>
- 画布：<按下方互斥模板填写，不要把两种模式写在同一行>
- 主目标：<这个屏幕服务的指标或行为>
- 反指标：<这个屏幕不能伤害的信任、质量或体验指标>
- 不可虚构项：<不能画进屏幕的未支持数据、能力、承诺或动作>
- 线上参考状态：<已提供线上参考 / 无线上参考已确认 / 缺失待补充 / 不适用>
- 视觉基线状态：<已登记，参考尺寸 / 目标输出像素 / 缺失待补充 / 不适用>
- 目标输出像素：<例如 1179 x 自适应长板；若有参考截图，写参考尺寸、截图倍率和目标宽高>
- 生成模式：<screenshot_edit / redraw；有线上截图且视觉还原优先默认 screenshot_edit>
- base_image：<screenshot_edit 时写当前 visual_baseline 的参考截图路径>
- edit_scope：<screenshot_edit 时写本次只修改的目标区域 / 目标模块>
- preserve_regions：<screenshot_edit 时默认保留：状态栏、顶部导航、车系头图、车型切换、tab、底部吸底 CTA>
- 设计系统：<用户提供设计系统 / AutoDesign / 截图基线 / 平台模式库 / PMW 默认移动端产品 UI 基线>
- 设计规范目标：<用户提供 / AutoDesign / 平台模式库 / PMW 默认假设>
- 平台模式：<Instagram / YouTube / TikTok / 抖音 / 大众点评 / 美团 / 不适用>
- 灵感来源摘要：<可复用布局、信息层级、交互结构、状态表达和信任提示；不可写成复制来源>
- 禁止照搬项：<图片、品牌素材、文案、专有 UI、未授权资产>
- 版权边界：<仅抽象启发 / 用户自有规范 / 已授权 / 未授权不可复制>
- image-2 状态：<计划生成 / 已生成 / 生成失败 / 待重试 / 需要重出>
- 依赖：<产品简报版本和来源>
```

image-2 prompt 必须是设计修正指令，不是界面氛围描述。禁止只写 `现代`、`简洁`、`高级`、`清爽`、`卡片式`、`科技感` 这类泛化词；如果需要表达这些方向，必须替换成具体决策：信息优先级、组件密度、状态呈现、主 CTA 数量、降噪项、字体层级、间距节奏和信任提示。每个 prompt 都要写清哪些内容必须删除或降级，而不只是新增元素。

默认反 AI 模板味约束：

```text
不要生成泛 SaaS 卡片堆叠、紫蓝渐变、装饰性图标圆圈、三栏模板、居中大字空泛 hero、无意义插画、统一大圆角、重阴影、漂浮装饰图形或拼贴感界面。若界面是工具 / 看板 / 交易 / 表单 / 结果页，优先使用任务驱动的信息层级，而不是营销海报式布局。
```

无线上截图时追加当前模板：

```text
画布补充：
- 画布模式：standard_first_screen
- 画布：标准移动端首屏
- 输出像素：iPhone 17 402 x 874
```

有线上截图 / `visual_baseline` 时追加当前模板：

```text
画布补充：
- 画布模式：physical_longboard
- 画布：线上截图物理长板
- 参考截图尺寸：<w x h>
- 截图倍率：<例如 393pt @3x>
- 目标输出画布：<目标宽度>px 宽，内容自适应长图，高度不得低于 <参考或换算高度>px，可随内容增长；字体、间距和组件按参考物理像素等比绘制
- 生成模式：screenshot_edit
- base_image：<当前 visual_baseline 参考截图路径>
- edit_scope：<只修改的目标区域 / 目标模块>
- preserve_regions：状态栏、顶部导航、车系头图、车型切换、tab、底部吸底 CTA
```

Rules:

- 一个输出单元等于一张图片；一次 image-2 调用只服务当前一个输出单元。
- 无线上截图的短内容输出单元使用上方 `standard_first_screen` 模板。
- 有线上截图 / `visual_baseline` 的输出单元必须写 `画布模式：physical_longboard`，并写 `目标输出画布：<目标宽度>px 宽，内容自适应长图，高度不得低于 <参考或换算高度>px，可随内容增长`。
- `standard_first_screen` 和 `physical_longboard` 模板互斥；不要在同一个最终 prompt 字段里同时出现短画布锚点和物理长板字段。
- 线上截图物理长板必须是一张连续移动端界面；不要为了塞进短画布缩小字体、压缩间距、裁切内容、遮挡底部操作区，或拆成多图 / 拼图 / 多屏故事板。
- 有线上截图时，图片输出契约必须同时保留内部逻辑宽度和物理像素输出：逻辑宽度只写在审计或视觉基线摘要里，不能进入最终 image-2 prompt 的画布字段。汽车之家生产页默认写 `参考截图尺寸：<w x h>`、`识别为 <逻辑宽度>pt @<scale>x`、`目标输出画布：默认使用参考截图物理像素长板，高度不得低于参考图高度，可随内容增长；字体、间距和组件按参考物理像素等比绘制`。
- `screenshot_edit` prompt 必须写：以参考截图为底、只修改 `edit_scope`、保留 `preserve_regions`、不得从零重绘整页。若 prompt 出现“从零 / 重新设计整页 / 重绘整页 / 改写所有模块”，必须显式写 `generation_mode=redraw`，否则检查失败。
- 视觉基线下不要默认 `redraw`。如果用户只说“使用方案 A”或“参考这些截图”，仍然停在产品简报 / 基线改动证明，不进入最终 prompt。
- 桌面端输出单元必须说明为什么移动端不合适。
- 除非用户明确要展示板，否则不要创建拼贴图、三联图、并排比较图、一图多屏、一图多方案或多屏故事板。
- 如果用户要 `3 个方向`，确认方向后生成三张独立图片。
- 如果用户要 `3 个方向 x 2 个屏幕`，生成六张独立图片；按方案或按屏幕排序，取决于用户的评审方式。
- 相关图片之间要保持产品事实、示例数据、字体层级和设计系统一致。
- 每个输出单元必须能追溯到已对齐产品简报中的产品判断；如果追溯不到，先回到产品对齐。
- 每个输出单元必须能追溯到自己的 10/10 原型标准；生成后复审会按该标准判断是否达标。若生成图明显出现模板味，即使产品逻辑正确，也不得直接通过。
- 每个输出单元必须能追溯到自己的设计规范目标；设计灵感只能提升布局、状态、层级和信任表达，不能替代产品路径，也不能复制外部页面。

## 设计启发 Prompt Block

Use this block whenever Dribbble, Pinterest, platform references, or user-provided visual inspiration are used. Keep it abstract and safe:

```text
Design inspiration constraints:
- Design-spec target: <用户提供 / AutoDesign / 平台模式库 / PMW 默认假设>.
- Platform pattern: <Instagram / YouTube / TikTok / 抖音 / 大众点评 / 美团 / 不适用>.
- Inspiration summary: only reuse layout logic, information hierarchy, interaction structure, component density, visual rhythm, state expression, trust cues, and de-noising strategy.
- Do not copy any specific screenshot, image, illustration, logo, brand asset, proprietary UI, exact copywriting, creator content, or unlicensed visual material.
- If the reference is Dribbble or Pinterest, treat it as mood / structure evidence only; convert it into concrete product UI decisions for the current brief.
- If the reference is an external platform pattern, do not claim official compliance; write it as a PMW platform-pattern profile.
```

## 基础 UI 原型模板

```text
用途：UI 原型
资产类型：移动端优先的应用原型屏幕
主要请求：为 <产品/功能> 生成 <屏幕名>。使用当前输出单元指定的唯一画布模式；如果是线上截图物理长板，写参考截图尺寸和目标输出画布。字体、间距、颜色和组件密度匹配提供的参考截图。
单图约束：只生成一张独立产品界面；禁止拼图、三联图、并排比较、一图多屏、一图多方案和故事板。

上下文：
- 产品意图：
  - 产品简报版本/状态：<vN / 已对齐>
  - 工作目标模式：<验证价值 / 优化线上指标 / 业务评审 / 设计评审 / 研发交付>
  - 场景路由：<主场景>
  - 方案方向：<名称和策略>
  - 产品路径：<它相信什么用户行为、要赢过哪个现状替代、解决什么损失、主动删除 / 牺牲 / 后置什么>
  - 设计完整度目标：<当前评分、主要差距、10/10 原型标准、本轮 prompt 修正方向>
  - 设计规范目标：<用户提供 / AutoDesign / 平台模式库 / PMW 默认假设>
  - 平台模式：<Instagram / YouTube / TikTok / 抖音 / 大众点评 / 美团 / 不适用>
  - 灵感来源摘要：<可复用模式，不复制来源>
  - 禁止照搬项：<图片、品牌素材、文案、专有 UI、未授权资产>
  - 版权边界：<仅抽象启发 / 用户自有规范 / 已授权 / 未授权不可复制>
  - 信息层级：<第一眼 / 第二眼 / 第三眼>
  - 状态策略：<默认 / 加载 / 空态 / 错误 / 成功 / 部分结果>
  - 反 AI 模板味约束：<禁止的模板模式和必须删除 / 降级的装饰项>
  - 原型思考：<为什么这个方案成立>
  - 信息架构设计思考：<信息组织与优先级>
  - 用户问题解决逻辑：<如何解决当前替代/损失>
  - 已确认前提：<2-4 条会影响原型的前提>
  - 变化类型：<新功能 / 现有功能迭代>
  - 现状基线：<已提供截图/参考；当前页面目的和需要保留的元素>
  - 页面类型：<新页面 / 现有页面迭代 / 不明确>
  - 线上参考需求：<需要 / 不需要 / 待判断>
  - 线上参考状态：<已提供线上参考 / 无线上参考已确认 / 缺失待补充 / 不适用>
  - 视觉基线：<参考图路径、参考尺寸、目标输出像素、优先级>
  - 承接页面：<上一步页面、入口或来源>
  - 相似线上模式：<相似结果页、状态页、活动页、表单页>
  - 核心问题：<具体问题和当前损失>
  - 用户任务：<用户现在想完成什么>
  - 原型内容重点：<必须展示、重点突出、可后置、不可虚构>
  - 主目标：<指标或行为>
  - 反指标：<信任 / 质量 / 投诉 / 留存 / 完成率等>
  - 当前阻力：<问题或证据>
  - 硬约束：<业务 / 法务 / 数据 / 运营 / 组件>
  - 可用数据：<现在能展示什么；什么是估算或需要确认>
- 产品方向审查决策：
  - 优先展示：<最高价值信息>
  - 删除或弱化：<未赚取的复杂度>
  - 后置：<可选精度或后续跟进>
  - 标注不确定：<估算或假设>
  - 不可虚构：<无法上线的功能/数据/动作>
- 决策门槛：
  - 已通过：<变化类型、问题真实性、价值交换、数据可行性、产品简报对齐、设计系统>
  - PM 待决策：<无或列表>

屏幕内容：
- 顶部：<标题、导航、品牌元素>
- 主要价值区：<钩子 / 预览 / 汇总>
- 输入或动作区：<最少必填字段和主要按钮>
- 结果/价值详情：<仅结果页需要>
- 信任说明：<隐私、跟进、不确定性、资格判断>

视觉要求：
- 平台/设备：<只写当前模式对应平台，不要列条件分支>
- 输出像素：<只写当前模式对应的输出像素；两种画布不能同场出现>
- 字体：<品牌字体或参考风格>
- 色彩：<品牌/参考色>
- 布局密度：<紧凑 / 标准 / 宽松>
- 设计系统约束：<适用时粘贴 design-system-workflow.md 的简短摘要>
- 设计规范目标：<适用时粘贴 design-system-workflow.md 的设计规范目标卡摘要>
- 设计启发约束：<若使用 Dribbble / Pinterest / 平台模式库，只写可复用模式和不可照搬项>
- 设计规范目标约束：按已确认的用户规范、AutoDesign、平台模式库或 PMW 默认假设执行。汽车之家产品 UI 中，线上截图的字号层级、间距节奏、组件密度和长板尺寸优先于泛化 AutoDesign token；品牌 VI 色和字体包只作为品牌露出、活动视觉或特殊场景参考，不能覆盖产品 UI token，也不能写成字体已授权可生产。
- 避免：不要红色标注框、不要水印、不要外部说明、不要文字重叠。
```

## AutoDesign Prompt Block

Use this block when the design-spec target is AutoDesign / Autohome, or when the user explicitly chooses AutoDesign for a non-Autohome concept. If the product is not Autohome, use only the visual discipline without adding Autohome-specific brand copy or domain content. Keep screenshot facts above generic tokens whenever reference screenshots are provided.

```text
AutoDesign production constraints:
- Make it look like a real Autohome mobile app screen, not a marketing poster or abstract concept.
- Visual baseline first: if a production screenshot is provided, match its typography hierarchy, spacing rhythm, component density, bottom bar height, and long-board proportions before applying generic AutoDesign tokens.
- Generation mode: for visual-fidelity iterations on a production screenshot, use `screenshot_edit`; use the screenshot as the base image, modify only the target module, preserve the status bar, top navigation, car-series hero, model switcher, tabs, and sticky bottom CTA. Use `redraw` only when the product brief explicitly asks for broad restructuring.
- Canvas mode: use the standard mobile first-screen template only when there is no screenshot baseline. If a production screenshot is provided, use physical long-board mode; do not put short-canvas anchors in the final image-2 prompt canvas field.
- Pixel output: for Autohome production-page prototypes with screenshot reference, generate a 3x physical-pixel mobile long board. Write the reference screenshot size and scale, for example `参考截图尺寸：1179 x 2556；识别为 393pt @3x`; write target output from the visual baseline, for example `目标输出画布：1179px 宽，内容自适应长图，高度不得低于 2556px，可随内容增长；字体、间距和组件按参考物理像素等比绘制`. Do not output a narrow 851px image when the reference is 1179px wide.
- Colors: primary blue #0088FF, blue gradient #0099FF -> #0088FF, commercial orange #FF6600 only for price/deal/subsidy emphasis, cyan #25C9FF only for IM-like emphasis, primary text #111E36, secondary text #464E64, weak text #828CA0, divider #E6E9F0, page background #F8F9FC, white cards.
- Typography: system Chinese font; prominent numbers can use HarmonyOS Sans SC; use production-like sizes from 12/14/16/18/20/24/28/32px with clear hierarchy.
- Layout: 8-point grid for structure and 4-point grid for details; use spacing 4/8/12/16/24/32px; align cards, fields, and CTAs to consistent margins.
- Do not shrink Chinese typography, chart axis labels, cards, tags, CTA text, or bottom toolbar just to fit more modules in a shorter canvas. If the screen includes first screen + explanation module + sample list + bottom CTA, use a longer board.
- Radius and depth: small tags/buttons 2px, cards/images 3px, dialogs/toasts/bottom sheets 6px, large bottom sheets 8px; use subtle shadow only where hierarchy needs it.
- Components: use AutoDesign-like NavBar, Button, Form, ToolBar, Tag, card, and result modules.
- Buttons: one dominant primary action per screen; bottom primary button height 48px, blue gradient, concise verb-object copy.
- Forms: short field labels, low input burden, phone number visible and editable in first screen for lead forms, privacy agreement near submit.
- Lead forms: clearly explain dealer/service follow-up when calls are part of the product reality.
- Brand VI boundary: do not replace product UI tokens with the brand VI colors #0055ff or #ff8800 unless the task is explicitly a brand/marketing visual; custom font packages require authorization confirmation and must not be presented as production-ready by default.
- Avoid: decorative orbs, oversized hero marketing layout, excessive gradients, over-rounded cards, heavy shadows, stacked CTAs, fake functions, cramped rows, and overlapping text.
```

## Form Page Prompt Checklist

Include:

- One clear hook above the form.
- One dominant CTA.
- Only required-looking fields.
- Optional refinements hidden, secondary, or moved after submit.
- Privacy/confidence copy short enough to not compete with the CTA.
- For Autohome lead forms: phone number visible and editable on the first screen; submit button visible on the first screen; privacy agreement close to submit.

Avoid:

- Long explanatory modules below the form.
- Multiple equally strong CTAs.
- Heavy conditions before phone/email/signup.
- Phone/email/signup fields when the product is not a lead, account, contact, or saved-result flow.
- Result-level detail on the form page unless it is a teaser.
- AutoDesign violations: arbitrary colors, excessive rounded corners, too many shadows, marketing-poster hero sections, and button stacks.

## Result Page Prompt Checklist

Include:

- "Report generated" or equivalent state.
- Integrated top summary.
- Detailed modules that fulfill the form promise.
- Optional refinements or condition-entry modules if they improve accuracy.
- Clear explanation of human follow-up when applicable.
- No bottom CTA if the real product has no such action.
- For Autohome result pages: use production-like cards, concise status tags, clear value hierarchy, and no invented bottom action.

Avoid:

- Repeating the same form CTA.
- Making the result page feel like another lead form.
- Hiding uncertainty; label what is estimated, confirmed, or needs follow-up.
- Filler text, decorative widgets, or visual modules that do not answer the user's task.

## Iteration Prompt Template

```text
Use case: ui-mockup
Asset type: revised mobile app prototype screen
Primary request: Revise the previous <screen name> according to annotated feedback.

Keep:
- <accepted style / layout / modules>

Change:
- Remove <red-boxed or specified module>.
- Simplify <green-boxed or specified area> to <new content>.
- Move <removed complexity> to <result page / detail layer> if requested.

Constraints:
- Preserve device size <width x height>.
- Preserve font and visual style from the reference.
- Preserve the active design-system profile, such as AutoDesign tokens and components.
- Do not add new functions unless explicitly requested.
- No annotation boxes, no watermark, no overlapping text.
```

## 生产检查清单

发送图片提示词前，确认：

- 产品简报状态为“已对齐”。
- 多方案任务已确认概念方向。
- 新页面已完成线上参考判断；需要参考时，不能在 `缺失待补充` 状态下出图。
- 产品意图块足够具体，可以指导信息层级。
- 产品方向审查决策已反映在屏幕内容中。
- 适用时已命名设计系统。
- 已采集线上截图时，提示词已写入 `视觉基线状态`、`参考截图尺寸` 和 `目标输出像素`；缺任一项时停止。
- 已采集线上截图时，最终 prompt 已通过 `pmw-prototype-prompt-check`；只要出现脚本定义的短画布锚点，就必须重写 prompt。
- 提示词包含具体颜色、字体、间距、圆角和组件约束。
- 提示词明确声明一次 image-2 调用只生成一张图、一个产品路径和一个屏幕任务。
- 除非用户明确要求比较动作，否则屏幕只有一个主要动作。
- 表单提交前只索取必要信息。
- 结果页在要求更多动作前先兑现承诺价值。
- 提示词明确禁止标注框、水印、文字重叠和假功能。

## 生成后质量检查

After generation, use `prototype-quality-review.md`:

- 对照已对齐的产品简报、场景路由、方案方向、可行性边界和当前设计规范目标检查图片。
- 有参考图时先运行 `pmw-image-audit audit --image <生成图> --reference <参考图>`；宽度低于参考截图 95%、长板高度低于参考截图 95%、底部栏遮挡或内容裁切时，结论至少是 `需要重出`。
- 如果某个屏幕有实质问题，只修改对应提示词/屏幕。
- 最终回答包含简短交付清单，不写长篇理由。

## 多屏顺序

When the user asks for many screens:

1. 先生成最重要的表单/输入页。
2. 再生成对应结果页。
3. 之后按方案继续生成。
4. 每张生成图都绑定一个产品路径和一个屏幕。
5. 同一组屏幕保持产品名、数据、字体和视觉系统一致。

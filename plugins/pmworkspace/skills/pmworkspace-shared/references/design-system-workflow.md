# 设计系统工作流

生成原型图片前使用本参考。PMWorkspace 的设计系统判断不是单纯套皮，而是先确定 `设计规范目标`：当前原型应该服从哪个品牌 / 平台 / 截图 / 概念基线。用户提供的设计系统、Figma、截图或品牌规则优先；命中汽车之家时使用 AutoDesign；非汽车之家产品可使用平台模式库或 PMW 默认移动端产品 UI 基线。用户提供当前线上截图时，截图基线优先于泛化 token，并且必须登记为 `visual_baseline`。

当用户、brief、Zoon、截图或参考材料命中汽车之家、AutoDesign、之家或 Autohome 时，产品 UI 优先使用 AutoDesign token。品牌 VI 和字体包只作为品牌露出、活动视觉或特殊场景参考；字体授权必须保留边界，不能写成生产可用承诺。

## 设计规范选择顺序

写 image-2 prompt 前，按以下顺序确定唯一 `设计规范目标`：

1. 用户提供的设计规范、Figma、截图、品牌规则或明确的组件说明。
2. 用户、brief、Zoon、截图或参考材料命中汽车之家、AutoDesign、之家或 Autohome 时，使用 AutoDesign；平台灵感只能辅助，不得覆盖 AutoDesign 产品 UI token。
3. 非汽车之家产品按用户指定或产品形态选择 PMW 内置平台模式库：Instagram（Ins）、YouTube、TikTok、抖音、大众点评、美团等。平台模式库是参考型设计规范，不是官方合规声明。
4. 如果没有可用规范，使用 PMW 默认移动端产品 UI 基线，并标记 `设计规范目标：PMW 默认假设，可讨论`。

设计规范目标必须写入设计约束摘要、图片输出单元和 Prototype Shotgun Board。缺设计规范目标时，先给用户一份可编辑的 `设计规范目标卡`，或让用户确认采用 PMW 默认假设后再写 image-2 prompt；平台脚本可用时用当前 run 的 `设计规范目标确认` gate / decision 记录用户确认，未确认时 Product Readiness Dashboard 不放行出图。

## 设计启发采集

当原型方向不清、缺视觉基线、用户要求更强设计感、设计完整度不足，或需要补足反 AI 模板味约束时，`$pm-prototype-shotgun` 可以使用 Browser / Computer Use 访问 Dribbble、Pinterest 等公开页面获取设计启发。采集结果只提炼可复用模式：

- 布局结构、信息层级、交互结构和关键任务路径。
- 组件密度、视觉节奏、状态表达、信任提示和降噪方式。
- 可借鉴原则、不可照搬项、版权边界和对当前原型的影响。

不要复制具体图片、品牌素材、文案、专有 UI 或未授权资产。设计启发只作为 `browser_evidence` 登记，标题或摘要中标明 `设计启发`，不新增 `design_inspiration` artifact。页面登录、不可访问或版权边界不清时，标记 `灵感证据不足`，退回用户提供链接 / 截图，或使用平台模式库 / PMW 默认假设继续。

推荐登记方式：

```bash
pmw-artifact add --kind browser_evidence \
  --title "设计启发：<来源 / 平台>" \
  --status "已采集" \
  --source-skill pm-prototype-shotgun \
  --url "<公开 URL>" \
  --summary "<布局 / 信息层级 / 交互结构 / 状态表达 / 不可照搬 / 对原型影响>"
```

## 平台模式库

平台模式库只服务信息架构、交互模型和视觉表达的启发，不得把外部平台内容、品牌资产、文案或专有 UI 写成可复制素材。

- Instagram（Ins）：内容流、视觉优先、轻互动、头像 / 关系 / 媒体比例、低解释文本。
- YouTube：视频消费、频道信任、播放 / 推荐 / 订阅路径、封面标题层级、连续观看。
- TikTok / 抖音：沉浸式短视频、强单屏任务、手势路径、轻量转化、创作者信任。
- 大众点评：本地生活决策、评分 / 距离 / 价格 / 排队 / 团购 / 评价证据。
- 美团：交易效率、优惠 / 库存 / 履约状态、商家信任、下单路径和售后状态。
- PMW 默认移动端产品 UI 基线：任务驱动、清晰层级、真实状态、克制装饰、可交付组件密度。

## 设计规范目标卡

当设计规范不明确，或用户可能有自有规范时，先发给用户一份可编辑的目标卡。用户修改后提交，或确认默认方案，才进入 image-2 prompt。

```text
设计规范目标卡：
- 目标品牌 / 平台：
- 设计基线来源：<用户提供 / AutoDesign / 平台模式库 / PMW 默认假设>
- 可借鉴对象：
- 禁止借鉴 / 不可照搬：
- 颜色：
- 字体：
- 栅格 / 间距：
- 组件风格：
- 信息密度：
- 状态覆盖：
- 图标 / 影像：
- 不可虚构项：
- 版权边界：
- 用户确认状态：<已确认 / 待修改 / 按默认假设继续>
```

## Detect The Design System

Load a design-system profile when:

- The task reaches prototype generation; default to the design-spec selection order above.
- The user names a brand or system, such as AutoDesign, 汽车之家, 之家, or Autohome.
- The user asks for production-ready, design-system-compliant, or component-aligned prototypes.
- The user provides design-system URLs, screenshots, Figma links, or existing product screenshots.
- 新页面仍需要匹配现有线上流程、结果状态、平台模式或生产样式。

Read `autohome-auto-design.md` when the product is Autohome or the user explicitly asks for AutoDesign. For non-Autohome products, use platform pattern profiles or PMW default mobile UI discipline; do not add Autohome-specific brand copy or domain content.

If the user provides Autohome brand VI material or local font packages, treat them as secondary visual references. They do not replace AutoDesign product UI tokens unless the task is explicitly a brand/marketing visual rather than product UI.

## Acquire Context

Use the most reliable available source:

1. User-provided screenshot or design file.
2. Accessible design-system page via browser inspection.
3. Local AutoDesign reference profile when Autohome / AutoDesign is detected.
4. PMW platform pattern profile.
5. User-provided verbal rules.

新页面回退到任一设计规范目标前，先读取 `production-reference-gate.md`。如果页面需要线上参考且状态是 `缺失待补充`，停止并索取截图，或让用户明确确认没有线上参考。

已提供线上截图时，先用 `pmw-image-audit baseline --reference <截图路径> --register` 或等价 `pmw-artifact add --kind visual_baseline` 记录参考尺寸和目标输出像素。没有 `visual_baseline` 时，设计系统不能被视为出图可执行约束。

If a page is accessible only in the user's browser session, inspect it with browser tools and summarize only the reusable rules. Do not paste full internal docs into generated open-source artifacts.

## 生成设计约束摘要

写图片提示词前，创建简短设计约束摘要：

```text
设计系统：<名称>
设计规范目标：<用户提供 / AutoDesign / 平台模式库 / PMW 默认假设>
平台模式：<Instagram / YouTube / TikTok / 抖音 / 大众点评 / 美团 / 不适用>
灵感来源摘要：<Dribbble / Pinterest / 公开页面 / 用户截图 / 未使用；只写可复用模式>
禁止照搬项：<具体图片 / 品牌素材 / 文案 / 专有 UI / 未授权资产>
版权边界：<仅抽象启发 / 用户自有规范 / 已授权 / 未授权不可复制>
基线角色：<PMW 默认移动端产品 UI 基线 / 明确品牌系统 / 截图事实来源>
线上参考状态：<已提供线上参考 / 无线上参考已确认 / 缺失待补充 / 不适用>
视觉基线状态：<已登记 / 缺目标输出像素 / 缺失待补充 / 不适用>
画布模式：<standard_first_screen / physical_longboard>
画布/设备：<按画布模式填写当前唯一模板：standard_first_screen 或 physical_longboard>
目标输出像素：<有线上截图时写参考尺寸、截图倍率与目标输出画布；汽车之家生产页默认使用参考截图物理像素 3x 长板，显式 override 时字体、间距和组件必须等比缩放>
颜色：<主色、强调色、文字、背景、边框>
字体：<字体族、字号层级、字重规则>
栅格/间距：<栅格和常用间距>
组件：<NavBar、Button、Form、ToolBar、卡片、结果模块>
不要：<已知反模式>
```

用于图片提示词时，把约束摘要放进 `视觉要求` 部分。

画布规则只保留摘要：无线上截图时可用移动端首屏；有线上截图 / `visual_baseline` 时必须使用截图物理像素长板。详细画布禁词、目标像素写法和出图前检查以 `image-prompts.md` 为真源，输出单元字段以 `prototype-shotgun-board.md` 为真源；本文只负责设计系统约束。

## Production Design Review

Run this review before final image generation:

- Does the design use the named system's tokens rather than invented colors?
- If AutoDesign is only a quality baseline, does the screen avoid pretending to be an Autohome domain product unless the product is Autohome?
- Is the design-spec target explicitly declared as user-provided, AutoDesign, platform pattern profile, or PMW default hypothesis?
- If Dribbble, Pinterest, or platform references were used, are they summarized as reusable patterns instead of copied UI, copy, images, or brand assets?
- Are components named and shaped like the system's components?
- For Autohome product UI, are AutoDesign tokens used instead of replacing them with brand VI colors or unverified font packages?
- Are text sizes plausible for the target device?
- If a screenshot baseline exists, are generated dimensions, type hierarchy, spacing rhythm, and bottom toolbar height close to the reference instead of compressed?
- Are labels, buttons, and warnings short enough for production UI?
- Is there one dominant primary action?
- Are optional inputs moved out of the first step when conversion is the goal?
- Are result pages fulfilling value rather than repeating the form?
- Is there any decorative filler that would not ship?
- Are there overlapping text, cramped rows, or distorted assets?

## Scheme Design

When producing multiple schemes, vary page structure, information architecture, interaction path, trust expression, or key task, not just visual styling:

- Scheme A: preview-first value before input.
- Scheme B: input-first but ultra-light conversion.
- Scheme C: comparison/report/result-driven structure.

Keep the same design-system target across schemes unless the user asks for visual exploration. Design inspiration may improve expression inside a product path, but it cannot turn three visual skins into three product paths.
This rule is business-agnostic: it applies equally to lead forms, community, live streaming, product libraries, transaction flows, content screens, tools, and dashboards.

## Iteration Rules

When the user annotates a screenshot:

- Red boxes usually mean remove, reduce, or move away from the current page.
- Green boxes usually mean preserve, simplify, or strengthen.
- Keep the accepted visual system intact.
- Only redesign unrelated sections when the requested change would otherwise break hierarchy or fit.

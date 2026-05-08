# 设计系统工作流

生成原型图片前使用本参考。AutoDesign 是 PMWorkspace 默认的生产级视觉基线。用户提供的设计系统、Figma、截图或品牌规则可以覆盖具体视觉细节，但输出仍应保持生产可用感。

当用户、brief、Zoon、截图或参考材料命中汽车之家、AutoDesign、之家或 Autohome 时，产品 UI 优先使用 AutoDesign token。品牌 VI 和字体包只作为品牌露出、活动视觉或特殊场景参考；字体授权必须保留边界，不能写成生产可用承诺。

## Detect The Design System

Load a design-system profile when:

- The task reaches prototype generation; default to AutoDesign production baseline.
- The user names a brand or system, such as AutoDesign, 汽车之家, 之家, or Autohome.
- The user asks for production-ready, design-system-compliant, or component-aligned prototypes.
- The user provides design-system URLs, screenshots, Figma links, or existing product screenshots.
- 新页面仍需要匹配现有线上流程、结果状态或生产样式。

Read `autohome-auto-design.md` by default for production baseline tokens, spacing, components, and anti-patterns. For non-Autohome products, use AutoDesign as a quality baseline, not as brand copy or domain content.

If the user provides Autohome brand VI material or local font packages, treat them as secondary visual references. They do not replace AutoDesign product UI tokens unless the task is explicitly a brand/marketing visual rather than product UI.

## Acquire Context

Use the most reliable available source:

1. User-provided screenshot or design file.
2. Accessible design-system page via browser inspection.
3. Local AutoDesign reference profile.
4. User-provided verbal rules.

新页面回退到 AutoDesign 前，先读取 `production-reference-gate.md`。如果页面需要线上参考且状态是 `缺失待补充`，停止并索取截图，或让用户明确确认没有线上参考。

If a page is accessible only in the user's browser session, inspect it with browser tools and summarize only the reusable rules. Do not paste full internal docs into generated open-source artifacts.

## 生成设计约束摘要

写图片提示词前，创建简短设计约束摘要：

```text
设计系统：<名称>
基线角色：<默认生产基线 / 明确品牌系统 / 截图事实来源>
线上参考状态：<已提供线上参考 / 无线上参考已确认 / 缺失待补充 / 不适用>
画布/设备：<尺寸>
颜色：<主色、强调色、文字、背景、边框>
字体：<字体族、字号层级、字重规则>
栅格/间距：<栅格和常用间距>
组件：<NavBar、Button、Form、ToolBar、卡片、结果模块>
不要：<已知反模式>
```

用于图片提示词时，把约束摘要放进 `视觉要求` 部分。

默认画布是移动端优先：iPhone 17 竖屏 `402 x 874`。只有用户明确要求，或看板/内部工具在移动端会明显变差时，才选择桌面端。

## Production Design Review

Run this review before final image generation:

- Does the design use the named system's tokens rather than invented colors?
- If AutoDesign is only a quality baseline, does the screen avoid pretending to be an Autohome domain product unless the product is Autohome?
- Are components named and shaped like the system's components?
- For Autohome product UI, are AutoDesign tokens used instead of replacing them with brand VI colors or unverified font packages?
- Are text sizes plausible for the target device?
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

Keep the same design-system tokens across schemes unless the user asks for visual exploration.
This rule is business-agnostic: it applies equally to lead forms, community, live streaming, product libraries, transaction flows, content screens, tools, and dashboards.

## Iteration Rules

When the user annotates a screenshot:

- Red boxes usually mean remove, reduce, or move away from the current page.
- Green boxes usually mean preserve, simplify, or strengthen.
- Keep the accepted visual system intact.
- Only redesign unrelated sections when the requested change would otherwise break hierarchy or fit.

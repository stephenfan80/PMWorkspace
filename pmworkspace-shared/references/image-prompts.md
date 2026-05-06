# 图片提示词模板

仅在产品简报已对齐、方案方向已确认后，才把这些模板用于 `imagegen` / 内置图像生成。每个提示词只对应一个屏幕，每张图只对应一个方案。

For Chinese users, keep planning notes, output contracts, final summaries, and generated UI copy in Simplified Chinese. The prompt may keep precise technical terms such as `image-2`, `UI`, `token`, `API`, device names, colors, and component names when useful for image quality.

## 提示词前置门槛

以下条件全部成立前，不要写图片提示词：

- `$pm-jobs` 已产出产品意图摘要。
- 工作目标模式、Q 诊断、前提确认和必要 D 拍板已经完成。
- 变化类型已判断为新功能或现有功能迭代。
- 现有功能迭代已包含当前生产截图或等价基线证据。
- 已读取 `production-reference-gate.md`，并判断新页面是否承接线上流程、结果状态或生产样式。
- 如果新页面需要线上参考，用户已提供参考，或已明确确认没有线上参考并批准按概念稿推进。
- 对话或 Zoon 中已有快速版、标准版或深度版产品简报。
- 产品简报已通过用户确认、最新 Zoon 编辑确认，或明确批准假设而达到“已对齐”。
- 多方案任务已有命名方案方向，并得到用户确认或批准作为默认方向。
- 输出计划已经把每个方案/屏幕映射为一张独立图片，不把多个方案合成一张比较图。
- 每张图片已经绑定方案名、屏幕任务、主目标、反指标、不可虚构项和产品简报版本。
- 画布决策遵循移动端优先：iPhone 17 竖屏 `402 x 874`；除非用户明确要求桌面端，或看板/内部工具确实需要大屏密度。
- 已通过 `design-system-workflow.md` 载入 AutoDesign 生产基线。
- 对抗审查中的实质改动已写回产品简报。

## 媒介锁

PMWorkspace 的设计原型默认使用 `image-2` / 图像生成。不要用 HTML、Markdown 线框、拼贴图或比较板替代原型图，除非用户明确要求“HTML”“可交互网页”“前端实现”或“本地网页原型”。

如果当前环境不能生成 image-2 图片，停止并说明无法出图；不要改用 HTML 来制造交付感。

## 方案方向确认

Before generating multiple schemes, present concise directions:

```text
方案方向：
A. <名称> - <产品策略和取舍>
B. <名称> - <产品策略和取舍>
C. <名称> - <产品策略和取舍>
```

Directions must differ by product strategy, information architecture, interaction model, or trust model. Do not offer three visual skins of the same idea. After confirmation, generate each direction/screen as a separate image, even when several images are generated in one batch.

## 图片输出契约

For every image generation request, declare the output unit before prompting:

```text
图片输出单元：
- 方案：<A/B/C 或方案名>
- 屏幕任务：<屏幕名 + 这个屏幕要帮用户完成什么>
- 画布：<设备和尺寸>
- 主目标：<这个屏幕服务的指标或行为>
- 反指标：<这个屏幕不能伤害的信任、质量或体验指标>
- 不可虚构项：<不能画进屏幕的未支持数据、能力、承诺或动作>
- 依赖：<产品简报版本和来源>
```

Rules:

- 一个输出单元等于一张图片。
- 默认输出单元画布是 iPhone 17 竖屏 `402 x 874`。
- 桌面端输出单元必须说明为什么移动端不合适。
- 除非用户明确要展示板，否则不要创建拼贴图、并排比较图或多屏故事板。
- 如果用户要 `3 个方向`，确认方向后生成三张独立图片。
- 如果用户要 `3 个方向 x 2 个屏幕`，生成六张独立图片；按方案或按屏幕排序，取决于用户的评审方式。
- 相关图片之间要保持产品事实、示例数据、字体层级和设计系统一致。
- 每个输出单元必须能追溯到已对齐产品简报中的产品判断；如果追溯不到，先回到产品对齐。

## 基础 UI 原型模板

```text
用途：UI 原型
资产类型：移动端优先的应用原型屏幕
主要请求：为 <产品/功能> 生成 <屏幕名>。尺寸严格为 <设备宽度 x 高度>。字体、间距、颜色和组件密度匹配提供的参考截图。

上下文：
- 产品意图：
  - 产品简报版本/状态：<vN / 已对齐>
  - 工作目标模式：<验证价值 / 优化线上指标 / 业务评审 / 设计评审 / 研发交付>
  - 场景路由：<主场景>
  - 方案方向：<名称和策略>
  - 已确认前提：<2-4 条会影响原型的前提>
  - 变化类型：<新功能 / 现有功能迭代>
  - 现状基线：<已提供截图/参考；当前页面目的和需要保留的元素>
  - 页面类型：<新页面 / 现有页面迭代 / 不明确>
  - 线上参考需求：<需要 / 不需要 / 待判断>
  - 线上参考状态：<已提供线上参考 / 无线上参考已确认 / 缺失待补充 / 不适用>
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
- 对抗审查决策：
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
- 平台/设备：<默认 iPhone 17 W402 x H874；只有明确要求或确有必要时用桌面端>
- 字体：<品牌字体或参考风格>
- 色彩：<品牌/参考色>
- 布局密度：<紧凑 / 标准 / 宽松>
- 设计系统约束：<适用时粘贴 design-system-workflow.md 的简短摘要>
- AutoDesign 基线：除非用户提供的设计系统明确覆盖，使用接近生产的 AutoDesign token、间距、组件和反模式约束。
- 避免：不要红色标注框、不要水印、不要外部说明、不要文字重叠。
```

## AutoDesign Prompt Block

Use this block by default as the production-quality visual baseline. If the product is not Autohome, use the visual discipline without adding Autohome-specific brand copy or domain content. Keep it in the prompt even when reference screenshots are provided, unless the screenshots clearly supersede a specific value.

```text
AutoDesign production constraints:
- Make it look like a real Autohome mobile app screen, not a marketing poster or abstract concept.
- Canvas: iPhone 17 portrait W402 x H874 unless the user specifies otherwise; preserve AutoDesign's 375px mobile canvas logic.
- Colors: primary blue #0088FF, blue gradient #0099FF -> #0088FF, commercial orange #FF6600 only for price/deal/subsidy emphasis, cyan #25C9FF only for IM-like emphasis, primary text #111E36, secondary text #464E64, weak text #828CA0, divider #E6E9F0, page background #F8F9FC, white cards.
- Typography: system Chinese font; prominent numbers can use HarmonyOS Sans SC; use production-like sizes from 12/14/16/18/20/24/28/32px with clear hierarchy.
- Layout: 8-point grid for structure and 4-point grid for details; use spacing 4/8/12/16/24/32px; align cards, fields, and CTAs to consistent margins.
- Radius and depth: small tags/buttons 2px, cards/images 3px, dialogs/toasts/bottom sheets 6px, large bottom sheets 8px; use subtle shadow only where hierarchy needs it.
- Components: use AutoDesign-like NavBar, Button, Form, ToolBar, Tag, card, and result modules.
- Buttons: one dominant primary action per screen; bottom primary button height 48px, blue gradient, concise verb-object copy.
- Forms: short field labels, low input burden, phone number visible and editable in first screen for lead forms, privacy agreement near submit.
- Lead forms: clearly explain dealer/service follow-up when calls are part of the product reality.
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
- 对抗审查决策已反映在屏幕内容中。
- 适用时已命名设计系统。
- 提示词包含具体颜色、字体、间距、圆角和组件约束。
- 除非用户明确要求比较动作，否则屏幕只有一个主要动作。
- 表单提交前只索取必要信息。
- 结果页在要求更多动作前先兑现承诺价值。
- 提示词明确禁止标注框、水印、文字重叠和假功能。

## 生成后质量检查

After generation, use `prototype-quality-review.md`:

- 对照已对齐的产品简报、场景路由、方案方向、可行性边界和 AutoDesign 基线检查图片。
- 如果某个屏幕有实质问题，只修改对应提示词/屏幕。
- 最终回答包含简短交付清单，不写长篇理由。

## 多屏顺序

When the user asks for many screens:

1. 先生成最重要的表单/输入页。
2. 再生成对应结果页。
3. 之后按方案继续生成。
4. 每张生成图都绑定一个方案和一个屏幕。
5. 同一组屏幕保持产品名、数据、字体和视觉系统一致。

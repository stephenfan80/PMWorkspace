---
name: pm-prototype-shotgun
description: |
  PMWorkspace 移动端优先的原型探索。用于用户需要 image-2 UI 原型图、多产品方向、
  截图修改、设计方案、移动应用原型、表单、结果页、看板、内部工具、交易流程、
  内容/社区屏幕或原型质量检查。要求产品简报已对齐，并且每个方案、每个屏幕
  单独输出一张图。
---

# 原型方案

`$pm-prototype-shotgun` 是 image-2 原型出图导演。它不重新做 `$pm-jobs` 的产品方向审查、不替 `$pm-strategy-review` 拍策略取舍、也不替 `$pm-brief` 补写产品契约；它只把已对齐产品简述 / 产品简报里的产品判断拆成可生成、可比较、可复审的单张设计稿。多方案不是三种视觉风格，而是三条产品路径。

核心规则：

```text
一次 image-2 调用 = 一张图 = 一个产品路径 + 一个屏幕任务
```

批量生成只是自动连续执行多个单图任务。`3 条产品路径` 表示连续执行 3 次 image-2；`3 条产品路径 x 2 个屏幕` 表示连续执行 6 次 image-2。每次调用都必须独立提示、独立产物、独立记录状态，不允许拼图、三联图、并排比较、一图多方案或多屏故事板。

默认最少 3 条产品路径；少于 3 条必须写明确豁免原因。每条路径都要先写清：相信什么用户行为、要赢过哪个现状替代、解决什么当前损失、主动删除 / 牺牲 / 后置什么、验证信号、失败信号、反指标保护和不可虚构边界。

出图前增加 `原型设计完整度内核`：每条产品路径必须先判断当前设计完整度 0-10，说明为什么不是 10/10，定义本屏的 10/10 原型标准，再把 image-2 prompt 写成设计修正指令。PMW 不接受只写“现代、简洁、高级”的氛围 prompt；必须把设计判断落到信息层级、状态覆盖、用户旅程、反 AI 模板味、设计系统 / 线上基线、移动端可用性和未决设计选择。

出图前还要确定 `设计规范目标`：优先使用用户提供的设计规范 / Figma / 截图 / 品牌规则；命中汽车之家、AutoDesign、之家或 Autohome 时使用 AutoDesign；非汽车之家产品可按 Instagram（Ins）、YouTube、TikTok、抖音、大众点评、美团等平台模式库建立参考型规范；都没有时使用 PMW 默认移动端产品 UI 基线并标记 `基于假设，可讨论`。Dribbble、Pinterest 或平台参考只能作为设计启发，提炼布局、层级、交互、状态和信任模式，不能复制图片、文案、品牌素材或专有 UI。

<!-- PMW-GENERATED-CONTRACT:START -->
## PMWorkspace 生成契约

> 本区块由 `bin/pmw-gen-skill-docs` 根据 `pmworkspace-shared/skill-docs/skill-docs.manifest.json` 生成；不要手写修改。更新共享门槛、前置检查或输出字段后，运行 `bin/pmw-gen-skill-docs write`，再运行 `bin/pmw-gen-skill-docs check`。

- skill：`pm-prototype-shotgun`
- 契约版本：`2`
- 阶段：原型方案
- 定位：基于已对齐 brief 默认规划最少 3 条产品路径，逐张生成 image-2 原型图，并把每个方案 / 屏幕写入方案比较板。

### 统一前置检查

- `_PMW_BIN`
- `pmw-update-check`
- `usage`
- `usage pm-prototype-shotgun`
- `pmw-dashboard`
- `readiness --target prototype`
- `pmw-prototype-board`

### 必读共享协议

- `../pmworkspace-shared/references/pm-eval-system.md`
- `../pmworkspace-shared/references/runtime-kernel.md`
- `../pmworkspace-shared/references/pm-workbench-map.md`
- `../pmworkspace-shared/references/artifact-flow.md`
- `../pmworkspace-shared/references/product-plan-handoff.md`
- `../pmworkspace-shared/references/product-readiness-dashboard.md`
- `../pmworkspace-shared/references/image-prompts.md`
- `../pmworkspace-shared/references/prototype-shotgun-board.md`
- `../pmworkspace-shared/references/design-system-workflow.md`
- `../pmworkspace-shared/references/browser-evidence.md`

### 共享门槛

- 真源：`pmworkspace-shared/skill-docs/skill-docs.manifest.json` 的 `shared_gates`。
- 快速更新：每个 skill 运行前用 `pmw-update-check --quick`；如果输出 `UPGRADE_AVAILABLE`，先询问用户是否执行 `UPGRADE_COMMAND`，除非 `auto_upgrade` 为 `true`。
- 摘要：中文本地化、复用 `current_run_id`、记忆不覆盖本轮事实、等待 Q/D/证据/确认时停住、禁止泄露 token/ownerSecret/私密资料。

### 默认用户可见输出字段

- `原型出图判断`
- `产品信息对齐状态`
- `方案方向`
- `产品路径`
- `原型设计完整度`
- `设计规范目标`
- `原型思考`
- `输出单元清单`
- `image-2 状态`
- `生成后复审`
- `下一步`

### 内部审计字段（默认不展示）

- `产品准备度仪表盘`
- `产品信息对齐包`
- `图片生成前门槛`
- `方案差异质量`
- `三条路径数量检查`
- `产品路径`
- `原型设计完整度`
- `设计规范目标`
- `设计启发`
- `平台模式`
- `禁止照搬项`
- `10/10 原型标准`
- `反 AI 模板味约束`
- `原型思考`
- `方案比较板`
- `证据状态`
<!-- PMW-GENERATED-CONTRACT:END -->

Before user-facing output, read `../pmworkspace-shared/references/language-and-localization.md`. For Chinese users, use Chinese labels for schemes, screens, QA status, and next steps; keep `image-2` as the model/product term.

## Preamble

Run platform checks and log usage:

```bash
_PMW_BIN=""
for _CANDIDATE in "$PWD/bin" "$PWD/pmworkspace-shared/bin" "$HOME/.codex/skills/pmworkspace-shared/bin" "$HOME/.agents/plugins/plugins/pmworkspace/skills/pmworkspace-shared/bin" $(find "$HOME/.codex/plugins/cache" -path "*/pmworkspace/*/skills/pmworkspace-shared/bin" -type d 2>/dev/null | sort -r); do
  if [ -x "$_CANDIDATE/pmw-log" ]; then _PMW_BIN="$_CANDIDATE"; break; fi
done
if [ -n "$_PMW_BIN" ]; then
  _UPD=$("$_PMW_BIN/pmw-update-check" --quick 2>/dev/null || true)
  [ -n "$_UPD" ] && echo "$_UPD"
fi
[ -n "$_PMW_BIN" ] && "$_PMW_BIN/pmw-log" usage pm-prototype-shotgun >/dev/null 2>&1 || true
[ -n "$_PMW_BIN" ] && [ -x "$_PMW_BIN/pmw-memory" ] && "$_PMW_BIN/pmw-memory" user-summary 2>/dev/null || true
[ -n "$_PMW_BIN" ] && [ -x "$_PMW_BIN/pmw-dashboard" ] && "$_PMW_BIN/pmw-dashboard" status 2>/dev/null || true
[ -n "$_PMW_BIN" ] && [ -x "$_PMW_BIN/pmw-dashboard" ] && "$_PMW_BIN/pmw-dashboard" readiness --target prototype 2>/dev/null || true
[ -n "$_PMW_BIN" ] && [ -x "$_PMW_BIN/pmw-artifact" ] && "$_PMW_BIN/pmw-artifact" latest --kind product_brief 2>/dev/null || true
[ -n "$_PMW_BIN" ] && [ -x "$_PMW_BIN/pmw-artifact" ] && "$_PMW_BIN/pmw-artifact" latest --kind visual_baseline 2>/dev/null || true
```

## Hard Gates

- Read `../pmworkspace-shared/references/image-prompts.md`.
- Read `../pmworkspace-shared/references/product-plan-handoff.md` and require the latest product contract to be `已对齐`.
- Read `../pmworkspace-shared/references/production-reference-gate.md`.
- Read `../pmworkspace-shared/references/zoon-drift-check.md`.
- Read `../pmworkspace-shared/references/product-memory.md`.
- Read `../pmworkspace-shared/references/pm-decision-principles.md`.
- Read `../pmworkspace-shared/references/pm-eval-system.md`.
- Read `../pmworkspace-shared/references/runtime-kernel.md`.
- Read `../pmworkspace-shared/references/pm-workbench-map.md` and use its 原型方案 stage fields.
- Read `../pmworkspace-shared/references/artifact-flow.md` and read the latest `product_brief` artifact before planning images.
- Read `../pmworkspace-shared/references/evidence-dashboard.md`.
- Read `../pmworkspace-shared/references/product-readiness-dashboard.md`.
- Read `../pmworkspace-shared/references/prototype-shotgun-board.md`.
- Read `../pmworkspace-shared/references/design-system-workflow.md`.
- Read `../pmworkspace-shared/references/prototype-quality-review.md`.
- Follow `runtime-kernel.md` Run Owner 协议：如果 `pmw-project show` 已有 `current_run_id`，复用当前 run；如果用户直接调用 `$pm-prototype-shotgun` 且没有当前 run，再创建 runtime run.
- 原型方案阶段必须先读取统一 `产品信息对齐包`：脚本可用时用 `pmw-dashboard status` 的产品信息对齐和当前产品缺口；脚本不可用时从最新 brief / artifact-flow / run 手动整理。若对齐包显示核心事实维度缺失、最新截图/数据未写回 brief、或产品判断对抗校验缺失，退回 `$pm-jobs` / `$pm-brief`，不能只靠当前对话继续写 prompt。
- 原型出图前必须先输出 `原型出图判断`，说明我建议出哪些图、暂时不出哪些图、为什么，以及图片生成前门槛；不能直接写 image-2 prompt。
- 原型出图前必须运行 Product Readiness Dashboard；`产品简报`、`产品简报确认`、`Zoon`、`线上参考`、必要的 `视觉基线`、`方案差异`、`方案方向确认`、`不可虚构项` 未通过时，停止在第一条阻断门槛，不写 image-2 prompt。默认只向用户展示短 verdict 和第一条阻断原因，完整表格只在审计 / 调试输出中展示。`数据佐证` 和 `复审状态` 出图前展示但不阻断，出图后再进入复审。
- 原型出图前必须有 `设计规范目标`：用户提供、AutoDesign、平台模式库或 PMW 默认假设。设计规范不明确时，先给用户可编辑的设计规范目标卡，或取得“按默认假设继续”的确认；未声明设计规范目标时不写 image-2 prompt。
- 产品简报未“已对齐”时，不写提示词，不生成图片，不生成 HTML，不输出交付稿。
- 用户选择一个方案方向、回复“使用方案 A”，或上传线上截图，都不能替代 `产品简报确认：已对齐`。如果截图是在方向选择之后才提供，必须先退回 `$pm-brief` 把新证据写入 brief 并重新确认；不得把对话里的口头方向直接当作 image-2 输入。
- 现有功能迭代必须有当前截图或等价视觉基线；只登记线上参考不够，还必须把截图转成 `visual_baseline`，包含参考图尺寸、目标输出像素、字号层级、间距节奏、组件密度和底部栏约束。
- 有 `visual_baseline` 的已有功能迭代，必须先完成 `生产基线改动证明`：当前线上问题、改动区域、为什么优于当前线上、保留 / 删除边界。证明不成立时，建议保留 / 微调当前线上方案，不写 image-2 prompt。
- 新页面如果承接线上流程、结果页、状态页或生产样式，必须先拿到线上参考，或得到用户明确确认“没有线上参考，按新页面概念稿推进”。
- 多方案生成前先确认概念方向，除非用户明确批准使用默认方向。
- 默认最少 3 条产品路径；少于 3 条路径必须记录 `少于 3 条路径豁免原因`，否则不能写 image-2 prompt。
- 每个方案必须包含 `产品路径`、`用户行为假设`、`要赢过的现状替代`、`当前损失`、`删除 / 牺牲 / 后置项`、`验证信号`、`失败信号`、`原型思考`、`信息架构设计思考`、`用户问题解决逻辑`、`反指标保护` 和 `不可虚构边界`。
- 每个方案必须包含 `设计完整度评分`、`为什么是这个分数`、`主要设计差距`、`10/10 原型标准`、`本轮 prompt 设计修正`、`反 AI 模板味约束`、`状态覆盖`、`第一眼 / 第二眼 / 第三眼信息层级` 和 `未决设计选择`。
- 三条产品路径也必须是三种设计判断，至少在信息架构、交互模型、信任模型、状态策略或降噪策略上有实质差异；不能只换配色、圆角、插画、卡片密度或文案语气。
- 设计启发可以使用 Browser / Computer Use 访问 Dribbble、Pinterest 或公开参考页，但只登记为 `browser_evidence`，只提炼可复用模式和不可照搬项；页面不可访问、需要登录或版权边界不清时，标记 `灵感证据不足`，不要假装已采集。
- 设计原型默认只能使用 image-2 / 图像生成输出方案图片；HTML 只在用户明确要求“HTML”“可交互网页”“前端实现”或“本地网页原型”时允许。
- 如果当前环境无法生成 image-2 图片，停止并说明无法出图；不要用 HTML、Markdown 线框或拼图替代设计原型。
- 默认移动端优先分两种互斥模式：无线上截图时使用 `standard_first_screen` 模板；有生产截图 / `visual_baseline` 时使用 `physical_longboard` 模板，必须以参考图物理像素和目标输出像素为 image-2 画布。
- 线上截图物理长板模式中，逻辑宽度只允许写入审计或视觉基线摘要，不能进入 image-2 prompt 的画布字段；prompt 不得出现 `pmw-prototype-prompt-check` 定义的短画布锚点。
- 汽车之家 / AutoDesign 生产页必须额外声明目标输出画布：默认使用参考截图原始物理像素长板，例如 `1179 x 2556 = 393pt @3x`；字体、间距、卡片和底部栏按参考物理像素比例等比执行。只有显式 override 目标宽度时才允许改宽，并必须同步等比缩放字号、间距和组件。缺视觉基线或缺目标输出像素时不写 image-2 prompt。
- 视觉还原优先、现有生产截图或截图修改任务默认使用 `screenshot_edit`：以线上截图作为底图，只修改目标区域，保留状态栏、顶部导航、车系头图、车型切换、tab 和底部吸底 CTA。只有产品探索或大幅重构时才显式使用 `redraw`。
- 只有用户明确要求，或看板/内部工具密度确实需要时，才使用桌面端。

## Multi-Scheme Rules

- 方向必须先在产品策略、信息架构、交互模型、信任模型或关键任务路径上不同，再讨论视觉差异。
- 默认最少 3 条产品路径；少于 3 条路径必须有明确豁免原因。
- 方案差异必须来自产品策略、信息架构、交互模型、信任模型或关键任务路径之一；默认多方案必须是三条产品路径。
- 不要把配色、插画、圆角、卡片样式或风格皮肤包装成多方案。
- 规则不局限留资业务；社区、直播、产品库、交易、内容、工具、看板等场景也必须用同一套方案质量标准。
- 一个产品路径 + 一个屏幕 = 一张图片。
- 一次 image-2 调用只能生成一张独立图片。
- `3 个方向 x 2 个屏幕` 表示六张独立图片。
- 除非用户要求演示材料，否则不要创建拼图、三联图、并排比较图或多屏故事板。
- 每次 prompt 都必须明确禁止拼图、并排比较、一图多屏和一图多方案。
- 每张图独立记录状态：`计划生成`、`已生成`、`生成失败`、`待重试` 或 `需要重出`；批量成功不能掩盖单张失败。
- 每个方案都必须输出产品路径思考：相信什么用户行为、要赢过哪个现状替代、解决什么当前损失、主动删除 / 牺牲 / 后置什么、验证信号、失败信号、为什么这样设计、信息架构如何组织、如何解决用户问题、解决哪个反指标风险、哪些内容不可虚构。

## Workflow

1. 建立原型方案控制器，记录 `产品简报来源`、`Product Readiness Dashboard`、`图片生成前门槛`、`方案差异质量`、`设计规范目标`、`设计启发`、`方案方向确认`、`输出单元清单`、`方案比较板写入`、`上游产物`、`本轮产物`、`下游可读`、`产物流动`、`生成后复审` 和 `证据状态`。
2. Read aligned brief and scenario route, then read `pmw-artifact latest --kind product_brief` when available. If the brief is missing, `待确认`, `草稿`, or has unresolved `缺失门槛`, route back to `$pm-brief` and stop before writing image-2 prompts. If the product brief artifact is missing or stale, also route back to `$pm-brief` instead of guessing from conversation memory.
3. If `pmw-project show` contains a Zoon URL, run `pmw-zoon drift --url <url>` when available, then read the latest document with `pmw-zoon read --url <url>` and treat it as the product source of truth. If drift changes goal, anti-metric, non-fiction boundary, scope, user promise, or scheme direction, route back to `$pm-brief` / `$pm-strategy-review` and stop.
4. 对每个请求的屏幕运行线上参考门槛；如果必要参考是 `缺失待补充`，先停下来问，不写图片提示词。
5. Read `design-heuristics.md`, `scenario-experts.md`, and `adversarial-review.md` as needed, but do not change scope or promise without writing the decision back to the product brief.
6. Use `pmw-memory user-summary` plus `pmw-memory taste-summary` when available so rejected directions are not repeated as “new”方案 and local product cognition can improve recommendations; if memory changes the recommendation, explicitly say `基于过往偏好，我建议...` or `基于本地产品认知...`, and never let memory override the current brief, Zoon, anti-metric, non-fiction boundary, design system, or reference gate.
7. 输出 `原型出图判断`：先说明我建议这轮出哪些单图、暂时不出哪些屏、为什么这些图能帮助 PM 做产品选择，以及图片生成前门槛。必须展示 `产品简报确认`、`方案方向确认`、`数据佐证`、`视觉基线状态`、`目标输出像素` 和 `设计规范目标`；数据缺失时写明 `数据佐证：未提供，本方案存在未验证风险`。
8. Propose concept directions with names and tradeoffs. 默认最少 3 条产品路径；少于 3 条路径必须记录豁免原因。方案差异必须通过 `方案差异质量`：至少说明每个方向在产品策略、信息架构、交互模型、信任模型或关键任务路径上的不同；如果只是视觉皮肤差异，停止并重拟方向。每个方案必须输出 `产品路径`、`用户行为假设`、`要赢过的现状替代`、`当前损失`、`删除 / 牺牲 / 后置项`、`验证信号`、`失败信号`、`原型思考`、`信息架构设计思考` 和 `用户问题解决逻辑`。
9. 对每条产品路径运行 `原型设计完整度内核`：给出 0-10 评分，说明当前差距，定义本屏 10/10 原型标准，并判断是否存在 AI 模板味风险。检查维度包括信息架构、状态覆盖、用户旅程、反 AI 模板味、设计系统 / 线上基线、移动端可用性和未决设计选择。快速成型可以低分继续，但用户可见状态必须写 `基于假设，可讨论`；深度交付中缺 10/10 标准或反模板味约束时不写 image-2 prompt。
10. 确定并确认 `设计规范目标`：用户提供规范优先；命中汽车之家、AutoDesign、之家或 Autohome 时默认载入 AutoDesign 约束，产品 UI 优先使用 AutoDesign token；非汽车之家产品按用户指定或产品形态选择 Instagram（Ins）、YouTube、TikTok、抖音、大众点评、美团等平台模式库；都没有时使用 PMW 默认移动端产品 UI 基线并标记 `基于假设，可讨论`。如果设计规范不明确，先输出设计规范目标卡并等待用户修改 / 确认，或得到按默认假设继续的批准；平台脚本可用时记录 `设计规范目标确认` gate / decision。
11. 如果使用 Dribbble、Pinterest、公开页面、平台模式库或用户截图做设计启发，登记为 `browser_evidence`，摘要必须写清可复用布局、信息层级、交互结构、状态表达、信任提示、不可照搬项和版权边界。不得把外部参考写成可复制图片、品牌素材、文案、专有 UI 或官方规范合规承诺。
12. 若用户提供线上截图或等价视觉基线，截图基线优先于泛化设计 token，并且必须用 `visual_baseline` 锁定参考尺寸与目标输出像素；品牌 VI 和字体包只作为品牌露出、活动视觉或特殊场景参考，字体授权必须保留边界，不能写成生产可用承诺。
13. 多方案生成前确认方案方向；如果用户已经明确批准默认方向，记录 `方案方向确认：默认方向已批准`，否则停在方向确认，不写 image-2 提示词。注意：方案方向确认不是产品简报确认；已有功能迭代在方向确认后如果新增截图 / 数据 / 线上参考，必须重新进入 `$pm-brief` 确认最新 brief。
14. For each image output unit, declare scheme, screen task, prototype thinking, information architecture rationale, user problem fit, anti-metric protection, canvas mode, canvas, main goal, anti-metric, non-fiction boundary, plus design completeness score, design gap, 10/10 prototype standard, prompt design fix, state coverage, first/second/third hierarchy, anti-AI-slop constraints, design spec target, design system profile, platform pattern, inspiration sources, inspiration patterns, no-copy boundary, product path, behavior assumption, current substitute to beat, current loss, tradeoff, validation signal, and failure signal. Also declare target output pixels, 线上参考状态, 视觉基线状态, design system, image-2 status, and brief dependency. 一个输出单元等于一张图片，不能把多个方案或多个屏幕合成拼图。
    - 无线上截图时，`画布模式` 写 `standard_first_screen`，并使用 `image-prompts.md` 的对应模板。
    - 有线上截图 / `visual_baseline` 时，`画布模式` 必须写 `physical_longboard`，`画布` 必须写 `线上截图物理长板`；`目标输出像素` 必须写明确宽高或宽度 + 最小高度，例如 `参考截图尺寸：1179 x 2556；识别为 393pt @3x；目标输出画布：1179px 宽，内容自适应长图，高度不得低于 2556px，可随内容增长；字体、间距和组件按参考物理像素等比绘制`。
    - 有线上截图且目标是视觉还原时，`生成模式` 必须写 `screenshot_edit`，`base_image` 绑定当前 `visual_baseline` 参考图，`edit_scope` 写清只改哪个模块，`preserve_regions` 默认写 `状态栏、顶部导航、车系头图、车型切换、tab、底部吸底 CTA`。
    - 有线上截图时，还必须写 `生产基线问题`、`改动区域`、`为什么优于当前线上`、`保留 / 删除边界`；这些不能只写“更现代 / 更清爽 / 更好看”。
    - 有线上截图时，最终 image-2 prompt 不得包含短画布锚点；以 `pmw-prototype-prompt-check` 为准。
    - 移动长板仍是一张连续移动端界面，不得拆成多张图、拼图、多屏故事板或桌面端。
15. 把批量请求拆成顺序单图队列：`3 条产品路径` -> 3 个输出单元，`3 条产品路径 x 2 个屏幕` -> 6 个输出单元。每个输出单元单独调用一次 image-2；不要把多个单元合成一个 prompt。
16. 平台脚本可用时，先用 `pmw-prototype-board add` 登记每个方案/屏幕单元；`--product-path`、`--behavior-assumption`、`--current-loss` 和 `--tradeoff` 是必填字段；有 `visual_baseline` 时还必须写入 `--baseline-problem`、`--changed-regions`、`--why-better-than-current` 和 `--baseline-preservation`；新输出必须同时写入 `--design-score`、`--design-gap`、`--ten-out-of-ten-standard`、`--prompt-design-fix`、`--anti-ai-slop-constraints`、`--state-coverage`、`--first-second-third-hierarchy`、`--design-spec-target`、`--design-system-profile`、`--platform-pattern`、`--inspiration-sources`、`--inspiration-patterns` 和 `--no-copy-boundary`。如果写入失败，输出 `方案比较板：未写入（原因）`，不能假装已记录。
17. 平台脚本可用时运行 `pmw-dashboard readiness --target prototype`；用户可见输出只包含短 verdict / 第一阻断原因。如果 verdict 是 `不可出图`，根据第一条阻断行退回 `$pm-brief`、线上参考门槛、设计规范目标卡、方案方向确认或不可虚构项补齐，不写 image-2 prompt。只有用户要求看审计时才展示 `pmw-dashboard readiness --details`。
18. 数据佐证缺失时不阻断出图，但必须把 `未验证风险` 写入用户可见输出和每个 image-2 prompt 的不可虚构项：不得展示确定性承诺、真实验证过的数值、已核验结果或无法兑现的数据能力，只能使用示例、区间、占位或明确标注假设。
19. 在每个输出单元的图片生成前门槛通过后，先把最终 prompt 交给 `pmw-prototype-prompt-check`；有视觉基线时检查失败必须重写 prompt，不得调用 image-2。检查通过后逐个 Generate with image-2 / image generation。每次生成只服务当前一个输出单元，并在 prompt 中写明 10/10 原型标准、设计规范目标、平台模式、灵感来源摘要、禁止照搬项、第一眼 / 第二眼 / 第三眼信息层级、必须出现的状态、必须删除 / 降级的内容、反 AI 模板味约束，以及禁止拼图、并排比较、一图多屏、一图多方案。 如果当前环境无法生成 image-2，停止并说明，不用 HTML、Markdown 线框或方案比较板替代。
20. 每张图出图后用 `pmw-prototype-board image` 补充图片路径或 URL；当当前 run 有 `visual_baseline` 且输出单元是 `physical_longboard` 时，脚本会自动调用 `pmw-image-audit`。如果返回 `需要重出` 或命令非 0，必须把该图标为 `需要重出`，不能展示为交付结果，也不能把批次写成全成功。
21. Run `prototype-quality-review.md`; if a reference screenshot exists, first trust the `pmw-prototype-board image` audit result or run `pmw-image-audit audit --image <生成图> --reference <参考图>` again for复核，并 expose `视觉审计：通过 / 需要重出`. Then route substantial post-image review to `$pm-prototype-review`.
22. 平台脚本可用时，用 `pmw-log prototype <batch>` 保存原型清单，它会登记 `prototype_manifest` 到 Product Artifact Flow；再用 `pmw-run event --type artifact` 记录产物。
23. Record approved/rejected design feedback with `pmw-log taste`, including scenario, feedback target, source, scope, and confidence when available.
24. 批量输出后运行 `pmw-dashboard status`，最终说明只给每张图的业务状态和下一步；方案比较板、产物流动和证据状态默认留在审计中。
25. 出图后必须给出结构化反馈入口，不要停在“已生成图片”。至少提供：选定一个方案继续、保留某个信息架构、保留某种信任表达、删除某个模板化视觉元素、指出要重出的区域 / 字段、继续探索新方案、补充截图 / 数据参考、进入 `$pm-handoff` 生成精简 PRD / 交付稿。若用户反馈只影响单屏视觉、信息层级或表单字段，可重出受影响单图；若反馈改变用户承诺、范围、数据真实性或交付责任，先回到 `$pm-brief` 更新产品简报并确认。

## 输出

```text
原型出图判断：
- 我建议：
- 这轮先出：
- 暂时不出：
- 为什么：
- 准备度：<可出图 / 不可出图>，<第一阻断原因或关键门槛已通过>
- 数据佐证：<已佐证 / 未提供，本方案存在未验证风险 / 不适用>
- 视觉基线：<已登记 / 缺目标输出像素 / 缺失待补充 / 不适用>
- 目标输出像素：<例如 1179 x 自适应长板；无参考时说明不适用>
- 设计规范目标：<用户提供 / AutoDesign / 平台模式库 / PMW 默认假设>
- 灵感来源：<已采集 / 未使用 / 灵感证据不足>
- 生成模式：<screenshot_edit / redraw；有线上截图且视觉还原优先默认 screenshot_edit>
- 编辑范围：<screenshot_edit 时只改哪个模块；无参考时说明不适用>
- 保留区域：<screenshot_edit 时必须保留的原截图区域>
- 下一步：

原型设计完整度：
- 当前评分：
- 为什么是这个分数：
- 主要差距：
- 10/10 原型标准：
- 本轮出图修正：
- 状态覆盖：
- 第一眼 / 第二眼 / 第三眼：
- 反 AI 模板味约束：
- 设计规范目标：
- 设计系统 / 平台模式：
- 灵感来源摘要：
- 禁止照搬项：
- 版权边界：
- 需要 PM 拍板：

方案方向：
- 方案 A：
  - 产品路径：
  - 用户行为假设：
  - 要赢过的现状替代：
  - 当前损失：
  - 删除 / 牺牲 / 后置项：
  - 验证信号：
  - 失败信号：
  - 产品判断：
  - 原型思考：
  - 信息架构设计思考：
  - 用户问题解决逻辑：
  - 反指标保护：
  - 不可虚构边界：
  - 设计完整度评分：
  - 主要设计差距：
  - 10/10 原型标准：
  - 本轮 prompt 设计修正：
  - 状态覆盖：
  - 第一眼 / 第二眼 / 第三眼：
  - 反 AI 模板味约束：
  - 未决设计选择：
  - 设计规范目标：
  - 设计系统 / 平台模式：
  - 灵感来源摘要：
  - 禁止照搬项：
  - 版权边界：
  - 最大风险：

图片输出单元：
- 方案名：
- 屏幕任务：
- 产品路径：
- 用户行为假设：
- 要赢过的现状替代：
- 当前损失：
- 删除 / 牺牲 / 后置项：
- 验证信号：
- 失败信号：
- 原型思考：
- 信息架构设计思考：
- 用户问题解决逻辑：
- 反指标保护：
- 设计完整度评分：
- 主要设计差距：
- 10/10 原型标准：
- 本轮 prompt 设计修正：
- 状态覆盖：
- 第一眼 / 第二眼 / 第三眼：
- 反 AI 模板味约束：
- 未决设计选择：
- 设计规范目标：
- 设计系统 / 平台模式：
- 灵感来源摘要：
- 禁止照搬项：
- 版权边界：
- 画布模式：
- 画布：
- 主目标：
- 反指标：
- 不可虚构项：
- 产品简报版本：
- 线上参考状态：
- 视觉基线状态：
- 目标输出像素：
- 生成模式：
- base_image：
- edit_scope：
- preserve_regions：
- 设计系统：
- image-2 状态：

内部原型计划（默认不展示，写入审计）：
- 产品简报：
- run_id：
- Zoon 事实来源：
- Zoon 漂移检查：
- 产品准备度仪表盘：
- 上游产物：
- 本轮产物：
- 下游可读：
- 产物流动：
- 图片生成前门槛：
- 场景：
- 线上参考：
- 视觉基线：
- 目标输出像素：
- 设计系统：
- 设计规范目标：
- 设计启发：
- 平台模式：
- 禁止照搬项：
- 方案差异质量：
- 方案方向确认：
- 画布：
- prompt 检查：
- 输出单元清单：
- 每张图绑定：方案名 / 屏幕任务 / 主目标 / 反指标 / 不可虚构项 / 产品简报版本 / 画布模式 / 目标输出像素 / 设计系统 / 设计规范目标 / 灵感来源摘要 / 禁止照搬项 / 线上参考状态 / image-2 状态
- 每个方案思考：产品路径 / 用户行为假设 / 要赢过的现状替代 / 当前损失 / 删除、牺牲或后置项 / 验证信号 / 失败信号 / 原型思考 / 信息架构设计思考 / 用户问题解决逻辑 / 反指标保护 / 不可虚构边界
- 单图生成协议：一次 image-2 调用 = 一张图 = 一个产品路径 + 一个屏幕任务
- image-2 状态：
- 已生成 / 计划生成的图片：
- 质量检查：
- 视觉审计：
- 已保存清单：
- 方案比较板：
- 证据状态：
- 偏好反馈：
- 原型复审：
- 生成后复审：
  - 是否符合 brief：
  - 是否符合设计系统：
  - 是否违反反指标：
  - 是否需要重出：
- 建议下一步：
  - 我建议：
  - 你可以直接回复：
    - 选定某个方案继续
    - 指出要改的区域 / 字段
    - 继续探索新方案
    - 补充截图 / 数据参考
    - 进入 `$pm-handoff` 生成精简 PRD / 交付稿
```

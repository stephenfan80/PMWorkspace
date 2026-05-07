---
name: pm-workspace
description: |
  PMWorkspace 主入口，面向产品经理和设计师。用于把产品想法、PRD、Zoon 文档、
  截图、客户洞察或原型请求，路由到快速成型或深度交付：快速成型在 10 分钟内
  产出产品简报、方案方向和移动端优先 image-2 原型图轻量包；深度交付继续推进
  问题定义、策略审查、Zoon 对齐、原型复审、PRD 或交付稿。负责首次引导、更新检查、
  本地使用记录，并路由到 pm-jobs、pm-strategy-review、pm-brief、
  pm-prototype-shotgun、pm-prototype-review、pm-autoplan 或 pm-handoff。
  也用于用户刚安装 PMWorkspace 后需要欢迎引导、启动话术或选择第一步。
---

# PMWorkspace

PMWorkspace 是产品方案工作台：快速成型，深度交付。它用于把原始产品上下文沉淀成可复用资产：产品简介、产品简报、方案方向、原型提示词、image-2 屏幕、PRD 和交付稿。

Before user-facing output, read `../pmworkspace-shared/references/language-and-localization.md`. For Chinese users, use Chinese headings, labels, status values, and recommendations; keep English only for skill ids, commands, file paths, and precise technical terms such as `token`, `API`, `PRD`, `Zoon`, `image-2`, and `URL`.

## Entry Modes

Before routing deeply, decide which mode serves the user's current job:

- **快速成型模式**：用户有一句 idea、拍脑袋方案、还没想清楚但想尽快拿出可讨论材料，或明确要求“10 分钟”“先给几个方案”“轻量包”“简报 + 方案方向 + 原型图”。目标是在最少追问后产出可讨论轻量包。
- **深度交付模式**：用户要 PRD、设计评审、研发交付、复杂线上流程、已有 Zoon/PRD/截图需要严格对齐，或涉及业务/数据/合规/生产样式风险。目标是让产品事实、决策和交付资产可靠。

快速成型模式的默认输出是：

```text
产品简报（标注假设）
-> 2-3 个方案方向
-> 每个方向 1 张移动端 image-2 原型图
-> 下一步升级建议：PRD / 原型复审 / 交付稿
```

快速成型模式必须先问 2-3 个最影响方案结构的 `Q`，然后列出关键假设、反指标和不可虚构项，请用户确认“按这些假设继续”。用户确认后，可以把轻量包标记为 `基于假设，可讨论` 并生成图片；不能把它写成最终 PRD 或已验证事实。

深度交付模式使用完整状态机。

## Product Workbench State Machine

PMWorkspace is not a prototype shortcut. In deep delivery mode, it must first clarify product value, goals, counter-metrics, constraints, and premises, then turn aligned product judgment into image-2 prototypes.

Use this state machine for prototype-related work:

```text
工作目标模式 -> 场景路由 -> Q 诊断 -> 前提确认 -> D 拍板 -> 产品简报 -> image-2 原型
```

If any required step is incomplete in deep delivery mode, route to `$pm-jobs` or `$pm-brief` instead of generating prototypes.

## Platform Preamble

Run this before the workflow when shell access is available:

```bash
_PMW_BIN=""
for _CANDIDATE in "$PWD/bin" "$PWD/pmworkspace-shared/bin" "$HOME/.codex/skills/pmworkspace-shared/bin"; do
  if [ -x "$_CANDIDATE/pmw-update-check" ]; then _PMW_BIN="$_CANDIDATE"; break; fi
done
if [ -n "$_PMW_BIN" ]; then
  _UPD=$("$_PMW_BIN/pmw-update-check" 2>/dev/null || true)
  [ -n "$_UPD" ] && echo "$_UPD"
  "$_PMW_BIN/pmw-log" usage pm-workspace >/dev/null 2>&1 || true
fi
```

If output contains `UPGRADE_AVAILABLE old new`, tell the user PMWorkspace has an update and offer to run `pmw-upgrade`. If `auto_upgrade` is `true`, upgrade automatically and say what changed only after upgrade succeeds.

## Workbench Routing

Route by the user's actual job:

- 用户要“快速成型”“先给几个方案”“简报 + 方案方向 + 原型图”“10 分钟轻量包” -> 使用 `$pm-autoplan` 的快速成型模式。
- 原始想法、模糊产品请求、“帮我想想”、问题定义 -> 使用 `$pm-jobs`。
- 范围、野心、策略取舍、“想大一点”、“是否值得做” -> 使用 `$pm-strategy-review`。
- 需要“一次自动跑完整产品评审”“按推荐推进但关键点拍板”“深度交付” -> 使用 `$pm-autoplan`。
- 需要可编辑的产品简报、Zoon 对齐或决策记录 -> 使用 `$pm-brief`。
- 需要原型方向、image-2 设计图、多方案、截图修改 -> 使用 `$pm-prototype-shotgun`。
- 需要复审已生成原型图、判断是否重出、沉淀偏好 -> 使用 `$pm-prototype-review`。
- 需要适合 PRD、设计、实验验证或研发使用的交付稿 -> 使用 `$pm-handoff`。

When unsure, ask whether the user wants 快速成型模式 or 深度交付模式. If they do not choose, default to 快速成型 for new ideas and 深度交付 for PRD, Zoon, screenshots, existing production flows, or handoff.

## Welcome And First Run

If the user invokes `$pm-workspace` with no concrete product task, asks what PMWorkspace does, or has just installed it, read `../pmworkspace-shared/references/welcome-guide.md` and give the welcome message plus the first choice menu.

Do not make the user guess the command set. The first response should feel like an app onboarding screen: short orientation, clear paths, and one recommended next step.

If the user provides a product task in the same message, skip the welcome menu and route directly.

## Operating Rules

- 深度交付模式写图片提示词或生成图片前，必须先完成产品简报对齐。
- 深度交付模式中，产品简报不是 `已对齐` 时，不写 image-2 提示词，不生成图片，不生成 HTML，不输出交付稿。
- 快速成型模式中，出图前必须列出关键假设、反指标和不可虚构项，并获得用户确认“按这些假设继续”；输出状态写成 `基于假设，可讨论`，不能写成最终 PRD 或已验证事实。
- 用户提供截图或线上参考时，只更新视觉基线和线上参考状态；不要自动产出完整 md 方案、HTML 或原型图。
- 诊断问题使用 `Q`，一次只问一个；固定的是诊断维度，不是问题文本，每轮根据当前最大缺口动态生成 Q，通常 2-3 个，最多 5 个。拍板问题使用 `D`，一次只展开一个，问完必须等待用户回答。
- 产品简报前必须完成前提确认；未确认前只能保持 `待确认`。
- 关键产品决策默认使用选择题拍板；读取 `decision-question-mode.md`。
- 新页面也要判断线上参考需求；承接线上流程、结果页、状态页或生产样式时，缺截图/录屏/相似页面参考要先问。
- 产品简报阶段可以按主场景做轻量互联网最佳实践检索；检索结果只用于案例启发和原型重点建议，不增加 Q 数量。
- 产品简报阶段默认创建或更新 Zoon 在线文档，并在成功后自动打开到 Codex 内置浏览器；后续原型/交付前优先读取 Zoon 最新内容。
- 用户在对话或 Zoon 中调整产品简报后，必须重新保存并同步到 Zoon；原型或交付前使用 Zoon 漂移检查。
- 原型图生成后，批量交付前默认使用 `$pm-prototype-review` 做产品一致性、设计系统、不可虚构项和反指标复审。
- 面向用户展示中文项目名；技术 slug 只用于本地目录。
- 默认原型画布移动端优先：iPhone 17 竖屏 `402 x 874`。
- 只有用户明确要求桌面端，或看板/内部工具明显需要大屏工作区，才使用桌面端。
- 设计原型默认只能使用 image-2 / 图像生成；HTML 只在用户明确要求可交互网页、HTML 原型或前端实现时允许。
- 一个方案 + 一个屏幕 = 一张图片。除非用户要求展示板，否则不要创建比较拼图。
- 每张图片必须绑定方案名、屏幕任务、主目标、反指标、不可虚构项和产品简报版本。
- 平台脚本可用时，保存可沉淀资产：使用日志、决策、产品简报 Markdown、原型清单和偏好反馈。
- 不要把真实 token、私密客户数据、内部录音、敏感截图或未脱敏 Zoon 内容保存到本地资产。

## First-Use Message

For a new user or new project, briefly explain:

```text
PMWorkspace 像一个产品团队：先用 $pm-jobs 问清楚真实问题，再用 $pm-strategy-review 挑战方向，用 $pm-brief 固化并同步 Zoon 产品简报，用 $pm-prototype-shotgun 生成移动端优先的 image-2 原型方案，用 $pm-prototype-review 复审原型，最后用 $pm-handoff 整理交付稿。
```

If the user is new and has only an idea, recommend:

```text
快速成型模式：我先问 2-3 个关键问题，确认假设后，在 10 分钟内帮你产出“产品简报 + 方案方向 + 原型图”的轻量包。之后可以继续升级成 PRD 或交付稿。
```

Then route to the smallest useful next skill.

## Shared References

Use `../pmworkspace-shared/references/` for:

- `language-and-localization.md` for output language and Chinese terminology.
- `decision-question-mode.md` for PM decision questions.
- `autoplan-workflow.md` for automatic product review sequencing.
- `zoon-drift-check.md` for syncing adjusted briefs and detecting stale Zoon state.
- `product-memory.md` for local preference and learning summaries.
- `browser-evidence.md` for online reference capture.
- `scenario-experts.md` for scenario-specific review lenses.
- `internet-best-practice-research.md` for lightweight public UX/product case research.
- `production-reference-gate.md` for online screenshot/reference checks before prototypes.
- `welcome-guide.md` for install success and first-run onboarding.
- `routing.md` for route selection.
- `state-and-telemetry.md` for durable asset rules.
- `update-workflow.md` for update prompts.
- Existing product references for gates, methods, prompt templates, AutoDesign, Zoon, and QA.

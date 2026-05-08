---
name: pm-workspace
description: |
  PMWorkspace 主入口，面向产品经理和设计师。用于把产品想法、PRD、Zoon 文档、
  截图、客户洞察或原型请求，路由到快速成型或深度交付：快速成型在 10 分钟内
  产出产品简报、方案方向和移动端优先 image-2 原型图轻量包；深度交付继续推进
  问题定义、策略审查、Zoon 对齐、原型复审、PRD 或交付稿。负责首次引导、更新检查、
  本地使用记录，并路由到 pm-jobs、pm-strategy-review、pm-brief、
  pm-prototype-shotgun、pm-prototype-review、pm-autoplan 或 pm-handoff。
  也用于用户刚安装 PMWorkspace 后需要欢迎引导、启动话术或选择第一步。v0.2 起
  负责启动 PMWorkspace runtime run，并把证据、决策、产物和下一步写入本地审计轨迹。
---

# PMWorkspace

PMWorkspace 是产品方案工作台：快速成型，深度交付。它用于把原始产品上下文沉淀成可复用资产：产品简介、产品简报、方案方向、原型提示词、image-2 屏幕、PRD 和交付稿。

Before user-facing output, read `../pmworkspace-shared/references/language-and-localization.md`. For Chinese users, use Chinese headings, labels, status values, and recommendations; keep English only for skill ids, commands, file paths, and precise technical terms such as `token`, `API`, `PRD`, `Zoon`, `image-2`, and `URL`.

## Frontloaded Protocol

`$pm-workspace` 是入口协议，不是第二份业务规则表。用户有具体产品任务时，跳过欢迎菜单，先读取这些共享协议再路由：

1. Read `../pmworkspace-shared/references/runtime-kernel.md`.
2. Read `../pmworkspace-shared/references/pm-workbench-map.md` for the end-to-end stage map, shared state fields, and eval category alignment.
3. Read `../pmworkspace-shared/references/pm-decision-principles.md`.
4. Read `../pmworkspace-shared/references/pm-eval-system.md` and keep its contracts as maintenance guardrails.
5. Read `../pmworkspace-shared/references/routing.md` as the only source for D0 工作方式判定、路由表、run 衔接和路由输出契约。
6. Read `../pmworkspace-shared/references/welcome-guide.md` only when the user has no concrete product task, asks what PMWorkspace can do, or needs first-run onboarding.

## Product Workbench State Machine

PMWorkspace is not a prototype shortcut. In deep delivery mode, it must first clarify product value, goals, counter-metrics, constraints, and premises, then turn aligned product judgment into image-2 prototypes.

Use this state machine for prototype-related work:

```text
工作目标模式 -> 场景路由 -> Q 诊断 -> 前提确认 -> D 拍板 -> 产品简报 -> image-2 原型 -> 原型复审 -> 产品交付
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

After D0 and routing choose 快速成型模式 or 深度交付模式, `$pm-workspace` creates the runtime run for routed sessions when scripts are available:

```bash
"$_PMW_BIN/pmw-run" start --skill pm-workspace --mode <quick|deep> --goal "<本轮产品目标>"
```

Use `pmw-run event` for the D0 result, current gate, evidence state, and next skill. If a child skill continues the workflow, do not finish the run in `$pm-workspace`; the child skill must reuse `current_run_id` and finish only at a terminal readiness state. If scripts are unavailable, mark `运行审计：未启用`.

## Routing Source

Read `../pmworkspace-shared/references/routing.md`; it is the only route table and D0 source of truth.

After routing, always output the routing contract from `routing.md`: `当前模式`、`当前门槛`、`下一技能`、`为什么`、`run_id`、`证据状态`.

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
- 平台脚本可用时，使用 `pmw-dashboard status` 汇总当前证据状态；不要让 Zoon、线上参考、原型清单和待决策项散落在对话里。
- 不要把真实 token、私密客户数据、内部录音、敏感截图或未脱敏 Zoon 内容保存到本地资产。

## Shared References

Use `../pmworkspace-shared/references/` for:

- `language-and-localization.md` for output language and Chinese terminology.
- `runtime-kernel.md` for run ids, shared statuses, audit events, and final run state.
- `pm-workbench-map.md` for the end-to-end PMWorkspace map, shared state fields, and eval category alignment.
- `pm-decision-principles.md` for automatic decision priorities, stop gates, and memory boundaries.
- `pm-eval-system.md` for maintenance eval fixtures and PMWorkspace behavior contracts.
- `evidence-dashboard.md` for evidence status pages.
- `decision-question-mode.md` for PM decision questions.
- `autoplan-workflow.md` for automatic product review sequencing.
- `zoon-drift-check.md` for syncing adjusted briefs and detecting stale Zoon state.
- `product-memory.md` for local preference and learning summaries.
- `question-tuning.md` for user-specific Q/D questioning preferences.
- `browser-evidence.md` for online reference capture.
- `scenario-experts.md` for scenario-specific review lenses.
- `internet-best-practice-research.md` for lightweight public UX/product case research.
- `production-reference-gate.md` for online screenshot/reference checks before prototypes.
- `prototype-shotgun-board.md` for multi-scheme comparison without merging images.
- `pm-review-army.md` for structured multi-lens review.
- `welcome-guide.md` for install success and first-run onboarding.
- `routing.md` for route selection.
- `state-and-telemetry.md` for durable asset rules.
- `update-workflow.md` for update prompts.
- Existing product references for gates, methods, prompt templates, AutoDesign, Zoon, and QA.

---
name: pm-workspace
description: |
  PMWorkspace 主入口，面向产品经理和设计师。用于把产品想法、PRD、Zoon 文档、
  截图、客户洞察或原型请求，先路由到全新功能或已有功能迭代，再由 Agent 判定
  快速成型或深度交付：快速成型在 10 分钟内产出产品简述、至少 3 个方案方向和
  移动端优先 image-2 原型图轻量包；深度交付继续推进产品方向审查内核、策略审查、
  Zoon 对齐、原型复审、产品设计文档、PRD 或交付稿。负责首次引导、更新检查、
  本地使用记录，并路由到 pm-jobs、pm-strategy-review、pm-brief、
  pm-prototype-shotgun、pm-prototype-review、pm-autoplan 或 pm-handoff。
  也用于用户刚安装 PMWorkspace 后需要欢迎引导、启动话术或选择第一步。v0.2 起
  负责启动 PMWorkspace runtime run，并把证据、决策、产物和下一步写入本地审计轨迹。
---

# PMWorkspace

PMWorkspace 是产品方案工作台：快速成型，深度交付。它用于把原始产品上下文沉淀成可复用资产：产品简述、方案方向、原型提示词、image-2 屏幕、产品设计文档、PRD 和交付稿。

<!-- PMW-GENERATED-CONTRACT:START -->
## PMWorkspace 生成契约

> 本区块由 `bin/pmw-gen-skill-docs` 根据 `pmworkspace-shared/skill-docs/skill-docs.manifest.json` 生成；不要手写修改。更新共享门槛、前置检查或输出字段后，运行 `bin/pmw-gen-skill-docs write`，再运行 `bin/pmw-gen-skill-docs check`。

- skill：`pm-workspace`
- 契约版本：`2`
- 阶段：主入口路由
- 定位：先判断全新功能 / 已有功能迭代，再由 Agent 判定执行深度，创建或衔接 run，并路由到最小可用的下一技能。

### 统一前置检查

- `_PMW_BIN`
- `pmw-update-check`
- `usage`
- `usage pm-workspace`
- `pmw-artifact`

### 必读共享协议

- `../pmworkspace-shared/references/runtime-kernel.md`
- `../pmworkspace-shared/references/pm-workbench-map.md`
- `../pmworkspace-shared/references/artifact-flow.md`
- `../pmworkspace-shared/references/pm-eval-system.md`
- `../pmworkspace-shared/references/routing.md`

### 共享门槛

- 真源：`pmworkspace-shared/skill-docs/skill-docs.manifest.json` 的 `shared_gates`。
- 摘要：中文本地化、复用 `current_run_id`、记忆不覆盖本轮事实、等待 Q/D/证据/确认时停住、禁止泄露 token/ownerSecret/私密资料。

### 默认用户可见输出字段

- `工作方式`
- `本轮价值时刻`
- `产品信息对齐`
- `产品路径`
- `业务判断`
- `当前需要确认`
- `补齐后解锁`
- `下一步`

### 内部审计字段（默认不展示）

- `当前模式`
- `产品路径`
- `产品信息对齐包`
- `执行深度`
- `当前门槛`
- `下一技能`
- `为什么`
- `run_id`
- `证据状态`
- `产物流动`
<!-- PMW-GENERATED-CONTRACT:END -->

Before user-facing output, read `../pmworkspace-shared/references/language-and-localization.md`. For Chinese users, use Chinese headings, labels, status values, and recommendations; keep English only for skill ids, commands, file paths, and precise technical terms such as `token`, `API`, `PRD`, `Zoon`, `image-2`, and `URL`.

## Frontloaded Protocol

`$pm-workspace` 是入口协议，不是第二份业务规则表。用户有具体产品任务时，跳过欢迎菜单，先读取这些共享协议再路由：

1. Read `../pmworkspace-shared/references/runtime-kernel.md`.
2. Read `../pmworkspace-shared/references/pm-workbench-map.md` for the end-to-end stage map, shared state fields, and eval category alignment.
3. Read `../pmworkspace-shared/references/artifact-flow.md` so routed skills preserve upstream artifacts and downstream-readable handoffs.
4. Read `../pmworkspace-shared/references/pm-decision-principles.md`.
5. Read `../pmworkspace-shared/references/pm-eval-system.md` and keep its contracts as maintenance guardrails.
6. Read `../pmworkspace-shared/references/routing.md` as the only source for D0 工作方式判定、路由表、run 衔接和路由输出契约。
7. Read `../pmworkspace-shared/references/welcome-guide.md` only when the user has no concrete product task, asks what PMWorkspace can do, or needs first-run onboarding.

## Product Workbench State Machine

PMWorkspace is not a prototype shortcut. In deep delivery mode, it must first clarify product value, goals, counter-metrics, constraints, and premises, then turn aligned product judgment into image-2 prototypes.

Use this state machine for prototype-related work:

```text
产品路径 -> 工作目标模式 -> 产品方向审查内核 -> 前提确认 -> 必要 Q/D -> 产品简述 / 产品简报 -> 三条产品路径 image-2 原型 -> 原型复审 -> 产品设计文档 / 产品交付
```

If any required step is incomplete in deep delivery mode, route to `$pm-jobs` or `$pm-brief` instead of generating prototypes.

## Platform Preamble

Run this before the workflow when shell access is available:

```bash
_PMW_BIN=""
for _CANDIDATE in "$PWD/bin" "$PWD/pmworkspace-shared/bin" "$HOME/.codex/skills/pmworkspace-shared/bin" "$HOME/.agents/plugins/plugins/pmworkspace/skills/pmworkspace-shared/bin" $(find "$HOME/.codex/plugins/cache" -path "*/pmworkspace/*/skills/pmworkspace-shared/bin" -type d 2>/dev/null | sort -r); do
  if [ -x "$_CANDIDATE/pmw-update-check" ]; then _PMW_BIN="$_CANDIDATE"; break; fi
done
if [ -n "$_PMW_BIN" ]; then
  _UPD=$("$_PMW_BIN/pmw-update-check" 2>/dev/null || true)
  [ -n "$_UPD" ] && echo "$_UPD"
  "$_PMW_BIN/pmw-log" usage pm-workspace >/dev/null 2>&1 || true
  [ -x "$_PMW_BIN/pmw-dashboard" ] && "$_PMW_BIN/pmw-dashboard" status 2>/dev/null || true
  [ -x "$_PMW_BIN/pmw-artifact" ] && "$_PMW_BIN/pmw-artifact" flow 2>/dev/null || true
fi
```

If output contains `UPGRADE_AVAILABLE old new`, tell the user PMWorkspace has an update. If output also contains `UPGRADE_COMMAND <command>`, offer that exact command; otherwise offer `pmw-upgrade --host codex`. If `auto_upgrade` is `true`, upgrade automatically with the detected command and say what changed only after upgrade succeeds.

After D0 and routing choose 快速成型模式 or 深度交付模式, `$pm-workspace` creates the runtime run for routed sessions when scripts are available:

```bash
"$_PMW_BIN/pmw-run" start --skill pm-workspace --mode <quick|deep> --goal "<本轮产品目标>"
```

Use `pmw-run event` for the D0 result, current gate, evidence state, and next skill. If a child skill continues the workflow, do not finish the run in `$pm-workspace`; the child skill must reuse `current_run_id` and finish only at a terminal readiness state. If scripts are unavailable, mark `运行审计：未启用`.

## Routing Source

Read `../pmworkspace-shared/references/routing.md`; it is the only route table and D0 source of truth.

After routing, record the full routing contract from `routing.md` in local audit: `当前模式`、`当前门槛`、`下一技能`、`为什么`、`run_id`、`证据状态`. Default user-facing output should show a short `工作方式` card plus `业务判断`、`当前需要确认` and `下一步`; it must now also include `本轮价值时刻` and `补齐后解锁`, so users can see whether they are in 10min 快速成型 or 深度交付, what product judgment PMW is helping them obtain now, and what single action is expected now.

If platform scripts are available, read `pmw-artifact flow --details` for routing context, but do not include the flow table in default user output. A routed child skill should know the latest `上游产物`, expected `本轮产物`, and `下游可读` target from local audit instead of relying only on conversation memory.

Before routing to any downstream skill, establish the `产品信息对齐包` from `pm-workbench-map.md`. If `pmw-dashboard status` is available, treat its `产品信息对齐` and `当前产品缺口` lines as the compact project context. If it says core product facts are missing, route to `$pm-jobs` / evidence intake instead of proposing方案方向 or prototypes.

## Welcome And First Run

If the user invokes `$pm-workspace` with no concrete product task, asks what PMWorkspace does, or has just installed it, read `../pmworkspace-shared/references/welcome-guide.md` and give the welcome message plus the first choice menu.

Do not make the user guess the command set. The first response should feel like an app onboarding screen: short orientation, clear paths, and one recommended next step.

If the user provides a product task in the same message, skip the welcome menu and route directly.

## Operating Rules

- 深度交付模式写图片提示词或生成图片前，必须先完成产品简报对齐。
- 深度交付模式中，产品简报不是 `已对齐` 时，不写 image-2 提示词，不生成图片，不生成 HTML，不输出交付稿。
- 快速成型模式中，出图前必须列出关键假设、反指标和不可虚构项，并获得用户确认“按这些假设继续”；输出状态写成 `基于假设，可讨论`，不能写成最终 PRD 或已验证事实。
- 每次进入产品任务，先输出或内部建立 `产品信息对齐包`：已知事实、暂定判断、证据边界、当前最大缺口、用户只需补什么、补齐后解锁什么。不能只凭最后一句话继续下游。
- 用户提供截图或线上参考时，只更新视觉基线和线上参考状态；不要自动产出完整 md 方案、HTML 或原型图。
- 已有功能迭代缺线上截图 / 录屏 / 等价视觉基线时，不输出 `方案 A / 方案 B / 方案 C` 或三条产品路径；只输出产品信息对齐卡、证据请求、Agent 拿到材料后会如何拆解和补齐后解锁的下一步。
- 用户选择某个方案方向后再上传截图时，只代表“方向选择 + 新证据输入”，不代表产品简报已对齐。必须先做线上基线接收：拆解当前线上优势、问题区域、必须保留、可以改、暂不应改、为什么新方案会优于当前线上；之后回到 `$pm-brief` 做产品简报确认，不能直接进入 `$pm-prototype-shotgun`。
- 已有功能迭代默认先保护线上体验。若当前线上方案明显比 Agent 新方案更简洁、更符合信息密度或更可信，PMW 必须建议保留 / 微调线上方案，而不是为了出图重画。
- `Q` / `D` 只作为关键卡点的交互方式，不是完整产品发现流程；Agent 可以先协助整理材料、拆解截图、生成访谈提纲、梳理数据口径、检索最佳实践和归纳路径机会。拍板问题使用 `D`，一次只展开一个，问完必须等待用户回答。
- 产品简报前必须完成前提确认；未确认前只能保持 `待确认`。
- 关键产品决策默认使用选择题拍板；读取 `decision-question-mode.md`。
- 新页面也要判断线上参考需求；承接线上流程、结果页、状态页或生产样式时，缺截图/录屏/相似页面参考要先问。
- 产品简报阶段可以按主场景做轻量互联网最佳实践检索；检索结果只用于案例启发和原型重点建议，不增加 Q 数量。
- 产品简报阶段默认先保存本地 Markdown 业务简报和本地审计副本；不要自动创建或更新 Zoon 在线文档。
- 在产品简报保存后，用一个轻量选择询问是否同步到在线协作文档（Zoon）。只有用户选择同步、提供现有 Zoon URL 或任务明确需要多人在线协作时，才创建/更新 Zoon，并在成功后自动打开到 Codex 内置浏览器。
- 用户在对话中调整产品简报后，必须重新保存本地简报；只有已启用 Zoon 时才重新同步到 Zoon，并在原型或交付前使用 Zoon 漂移检查。
- 未启用 Zoon 时，后续原型/交付优先读取本地已对齐产品简报，Product Readiness Dashboard 不应把 Zoon 当作阻断门槛。
- 原型图生成后，批量交付前默认使用 `$pm-prototype-review` 做产品一致性、设计系统、不可虚构项和反指标复审。
- 面向用户展示中文项目名；技术 slug 只用于本地目录。
- 默认原型画布移动端优先：无线上截图时用 iPhone 17 竖屏 `402 x 874`；有生产截图 / `visual_baseline` 时用截图物理像素长板。
- 只有用户明确要求桌面端，或看板/内部工具明显需要大屏工作区，才使用桌面端。
- 设计原型默认只能使用 image-2 / 图像生成；HTML 只在用户明确要求可交互网页、HTML 原型或前端实现时允许。
- 一个方案 + 一个屏幕 = 一张图片。除非用户要求展示板，否则不要创建比较拼图。
- 默认最少 3 个方案；少于 3 个必须有明确豁免原因。
- 每个方案必须包含原型思考、信息架构设计思考、用户问题解决逻辑、反指标保护和不可虚构边界。
- 每张图片必须绑定方案名、屏幕任务、主目标、反指标、不可虚构项和产品简报版本。
- 平台脚本可用时，保存可沉淀资产：使用日志、决策、产品简报 Markdown、原型清单和偏好反馈。
- 平台脚本可用时，使用 `pmw-dashboard status` / `pmw-dashboard readiness --target prototype|handoff` 获取简洁 verdict；需要完整审计时才运行或展示 `--details` 表格。
- 平台脚本可用时，使用 `pmw-artifact flow --details` 汇总产物流动给下游技能；默认用户输出不说明 `上游产物`、`本轮产物`、`下游可读` 和 `产物流动`。
- 不要把真实 token、私密客户数据、内部录音、敏感截图或未脱敏 Zoon 内容保存到本地资产。

## Shared References

Use `../pmworkspace-shared/references/` for:

- `language-and-localization.md` for output language and Chinese terminology.
- `runtime-kernel.md` for run ids, shared statuses, audit events, and final run state.
- `pm-workbench-map.md` for the end-to-end PMWorkspace map, shared state fields, and eval category alignment.
- `artifact-flow.md` for Product Artifact Flow, upstream artifacts, downstream-readable outputs, and `pmw-artifact`.
- `pm-decision-principles.md` for automatic decision priorities, stop gates, and memory boundaries.
- `pm-eval-system.md` for maintenance eval fixtures and PMWorkspace behavior contracts.
- `evidence-dashboard.md` for evidence status pages.
- `product-readiness-dashboard.md` for the pre-image and pre-handoff readiness verdict.
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

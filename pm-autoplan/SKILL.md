---
name: pm-autoplan
description: |
  PMWorkspace 自动产品评审流水线。用于用户希望“一次跑完整产品评审”“自动把
  产品方向梳理到可出原型前”“按推荐推进但关键点让我拍板”，或希望快速产出
  “产品简报 + 方案方向 + 原型图”轻量包时。支持快速成型模式和深度交付模式。
  快速成型模式用最少追问确认假设后产出可讨论轻量包；深度交付模式顺序串联
  pm-jobs、pm-strategy-review、pm-brief、本地简报保存、可选 Zoon 同步、Zoon 漂移检查和原型
  准备度检查，只把会改变方向的 D 选择题交给用户确认。
---

# 自动产品评审

`$pm-autoplan` 是 PMWorkspace 的一键推进模式：把零散想法推进成可讨论轻量包，或推进到可确认的产品简报与交付资产。它不是跳过产品判断直接出图。

<!-- PMW-GENERATED-CONTRACT:START -->
## PMWorkspace 生成契约

> 本区块由 `bin/pmw-gen-skill-docs` 根据 `pmworkspace-shared/skill-docs/skill-docs.manifest.json` 生成；不要手写修改。更新共享门槛、前置检查或输出字段后，运行 `bin/pmw-gen-skill-docs write`，再运行 `bin/pmw-gen-skill-docs check`。

- skill：`pm-autoplan`
- 契约版本：`1`
- 阶段：自动产品评审
- 定位：作为靠谱产品负责人，总控快速成型或深度交付，只推进到当前最早门槛。

### 统一前置检查

- `_PMW_BIN`
- `pmw-update-check`
- `usage`
- `usage pm-autoplan`
- `pmw-dashboard`
- `pmw-artifact`

### 必读共享协议

- `../pmworkspace-shared/references/autoplan-workflow.md`
- `../pmworkspace-shared/references/runtime-kernel.md`
- `../pmworkspace-shared/references/pm-workbench-map.md`
- `../pmworkspace-shared/references/product-readiness-dashboard.md`
- `../pmworkspace-shared/references/artifact-flow.md`
- `../pmworkspace-shared/references/pm-eval-system.md`
- `../pmworkspace-shared/references/routing.md`

### 共享门槛

- 先读语言与本地化协议，中文用户默认使用中文字段、中文状态和中文建议。
- 复用 runtime run：子 skill 发现已有 current_run_id 时不得重新创建 run。
- 历史偏好、记忆和默认规则不能覆盖本轮事实、brief、Zoon、反指标、不可虚构项或证据门槛。
- 等待 Q、D、证据或用户确认时必须停住；不能假装已对齐、可出图或可交付。
- 不得把真实 token、ownerSecret、私密客户资料、内部录音、未脱敏截图或未脱敏 Zoon 内容写进公开仓库。

### 默认用户可见输出字段

- `工作方式`
- `自动评审结论`
- `我建议`
- `理由`
- `当前需要确认`
- `下一步`

### 内部审计字段（默认不展示）

- `模式来源`
- `推进阶段`
- `最早门槛`
- `门槛等级`
- `停止原因`
- `下一技能`
- `交接上下文`
- `产品准备度仪表盘`
- `证据状态`
<!-- PMW-GENERATED-CONTRACT:END -->

Before user-facing output, read `../pmworkspace-shared/references/language-and-localization.md`. 面向中文用户时，输出中文标题、状态和建议；只保留 `$pm-*`、Zoon、PRD、image-2、URL 等必要术语。

## Preamble

可用时运行平台检查和记忆摘要：

```bash
_PMW_BIN=""
for _CANDIDATE in "$PWD/bin" "$PWD/pmworkspace-shared/bin" "$HOME/.codex/skills/pmworkspace-shared/bin"; do
  if [ -x "$_CANDIDATE/pmw-log" ]; then _PMW_BIN="$_CANDIDATE"; break; fi
done
[ -n "$_PMW_BIN" ] && "$_PMW_BIN/pmw-update-check" 2>/dev/null || true
[ -n "$_PMW_BIN" ] && "$_PMW_BIN/pmw-log" usage pm-autoplan >/dev/null 2>&1 || true
[ -n "$_PMW_BIN" ] && [ -x "$_PMW_BIN/pmw-memory" ] && "$_PMW_BIN/pmw-memory" summary 2>/dev/null || true
[ -n "$_PMW_BIN" ] && [ -x "$_PMW_BIN/pmw-question-tuning" ] && "$_PMW_BIN/pmw-question-tuning" summary 2>/dev/null || true
[ -n "$_PMW_BIN" ] && [ -x "$_PMW_BIN/pmw-artifact" ] && "$_PMW_BIN/pmw-artifact" flow 2>/dev/null || true
```

## Workflow

1. Read `../pmworkspace-shared/references/autoplan-workflow.md`.
2. Read `../pmworkspace-shared/references/runtime-kernel.md`.
3. Read `../pmworkspace-shared/references/pm-workbench-map.md` and use its 自动产品评审 stage fields.
4. Read `../pmworkspace-shared/references/evidence-dashboard.md`.
5. Read `../pmworkspace-shared/references/product-readiness-dashboard.md`.
6. Read `../pmworkspace-shared/references/artifact-flow.md` and include Product Artifact Flow in the control panel when routing between skills.
7. Read `../pmworkspace-shared/references/pm-decision-principles.md`.
8. Read `../pmworkspace-shared/references/pm-eval-system.md` and treat its contracts as maintenance guardrails for PMWorkspace behavior.
9. Read `../pmworkspace-shared/references/routing.md`; if `$pm-autoplan` was entered from `$pm-workspace`, inherit its mode and run. If called directly, use routing D0 to choose mode.
10. Read `../pmworkspace-shared/references/question-tuning.md`.
11. Read `../pmworkspace-shared/references/product-office-hours.md`.
12. Read `../pmworkspace-shared/references/adversarial-review.md`.
13. Read `../pmworkspace-shared/references/product-plan-handoff.md`.
14. Read `../pmworkspace-shared/references/zoon-workflow.md` and `../pmworkspace-shared/references/zoon-drift-check.md`.
15. Follow `runtime-kernel.md` Run Owner 协议：如果 `pmw-project show` 已有 `current_run_id`，复用当前 run，不要重新 `pmw-run start`；如果用户直接调用 `$pm-autoplan` 且没有当前 run，再 start `pmw-run start --skill pm-autoplan --mode <quick|deep> --goal "<本轮目标>"`.
16. Build the automatic review control panel from `autoplan-workflow.md`: 靠谱产品负责人姿态、模式来源、事实来源优先级、当前阶段、最早阻塞门槛、门槛等级、门槛来源、可自动采用项、必须 PM 拍板项、下一技能和交接上下文.
17. 快速成型模式：先做生产/高风险升级检查；如果出现生产流程、高风险承诺、真实数据、线索/交易/隐私或研发交付信号，升级到深度交付门槛，不要继续轻量包。
18. 快速成型模式：按最早门槛顺序只检测会影响轻量包结构的缺口：核心用户/场景、核心问题、主目标/反指标、不可虚构项、原型屏幕范围、方案差异、假设确认。默认最多问 2-3 个 `Q`。
19. 快速成型模式：列出关键假设、方案方向和每张图的不可虚构项，请用户确认“按这些假设继续”。确认前不生成图片，并用 `pmw-run event --type gate` 记录当前门槛。
20. 快速成型模式：确认后输出轻量包：标注假设的产品简报、2-3 个方案方向、每个方案 1 张移动端 image-2 原型图计划，并把状态写成 `基于假设，可讨论`。
21. 深度交付模式：按最早门槛顺序推进：工作目标模式、场景路由、Q 诊断、前提确认、必要 D、策略审查、产品简报、本地简报保存、可选 Zoon 同步、已启用 Zoon 的漂移检查、线上参考和设计系统基线、Product Readiness Dashboard 的原型准备度或交付准备度。
22. 深度交付模式：Use `pm-decision-principles.md` to auto-decide only low-risk defaults that do not change product direction; surface any direction-changing item as a single `D` choice question and stop.
23. Give the user a conclusion-first review: first output `自动评审结论` with `我建议` and `理由`, include a short `工作方式` / progress card, then write the full `评审控制面板` to audit.
24. For the earliest gate, always declare `门槛等级` as `阻断`、`高风险`、`可自动采用` or `可延后`, and declare `门槛来源`.
25. Every item in `已自动采用` must include source and why no PM decision is needed, for example `默认移动端优先。来源：PMWorkspace 默认规则。原因：不改变产品方向或用户承诺。`
26. When enough information exists, create the smallest useful product brief and save it with `pmw-log brief <name>`. This saves the local business brief and audit copy, registers `product_brief` in Product Artifact Flow, and syncs to Zoon only when `PMW_ZOON_SYNC_ON_BRIEF=true` / `zoon_sync_on_brief: true` or the user has explicitly chosen online collaboration.
27. If a Zoon URL exists before prototype preparation, run `pmw-zoon drift --url <url>` when available. If it returns `DRIFT`, read the latest Zoon snapshot and update the product brief version before continuing.
28. Before routing to `$pm-prototype-shotgun` or `$pm-handoff`, run `pmw-dashboard readiness --target prototype` or `pmw-dashboard readiness --target handoff` when available and use the short verdict in the user-facing conclusion. If the verdict is `不可出图` or `不可交付`, route to the first blocking gate instead of continuing. Only show `--details` when the user asks for audit/debug output.
29. Map the earliest blocking gate to one next skill: `$pm-jobs`, `$pm-strategy-review`, `$pm-brief`, `$pm-prototype-shotgun`, `$pm-prototype-review`, or `$pm-handoff`. Do not pretend all downstream skills have completed when only the next gate is ready.
30. `下一技能` cannot be only a skill id in audit; record `交接上下文` with 来源门槛、已确认事实、未决 Q/D、证据状态 and 交给它的原因. 交接上下文还必须追加上游产物、本轮产物、下游可读和产物流动，但默认不展示给用户。
31. At each gate, record evidence, decisions, artifacts, or reviews with `pmw-run event`; before final output, run `pmw-dashboard status` when available and only surface its short business summary.
32. End with a readiness state: `需要补充`、`待确认`、`基于假设，可讨论`、`已对齐`、`可进入原型复审`、or `可交付`. Call `pmw-run finish` only when the current run reaches a terminal readiness state; if waiting for Q/D/证据 or handing off to a child skill, keep the current run open for reuse.

## Auto-Decide Rules

自动决策必须遵守 `pm-decision-principles.md` 的事实优先级：已对齐产品简报或最新 Zoon 快照 > 用户本轮明确输入 > 当前已确认 Q / D / 前提 > 运行审计和复审结论 > 历史偏好。

自动接受：

- 用户已经明说或文档中明确写出的事实。输出时说明来源：用户本轮明确输入 / 已对齐产品简报 / 最新 Zoon。
- 默认移动端优先画布。输出时说明来源：PMWorkspace 默认规则；原因：不改变产品方向或用户承诺。
- 不影响方向的格式、标题、状态字段。输出时说明来源：PMWorkspace 输出协议；原因：不改变范围、承诺或验收。
- 已有 Zoon URL 时优先 append，不新建文档。输出时说明来源：Zoon 协议；原因：保持在线事实来源连续。
- 未启用 Zoon 时使用本地已对齐产品简报。输出时说明来源：PMWorkspace 默认规则；原因：减少在线协作卡点，不改变产品事实。
- 快速成型模式中，不影响方案结构的轻量包格式和默认输出数量。输出时说明来源：快速成型协议；原因：不改变产品事实。

必须提问：

- 目标人群、主目标、反指标、不可虚构项仍会改变原型结构。
- 多方案方向没有本质差异。
- 线上参考需要但缺失。
- Zoon 最新内容和本地产品简报冲突。
- 用户承诺、数据真实性、线索/交易/隐私口径需要 PM 拍板。
- 快速成型模式出图前，用户尚未确认“按这些假设继续”。
- 快速成型输入出现生产流程、高风险承诺、真实数据、线索/交易/隐私或研发交付信号，需要升级到深度交付门槛。
- 深度交付的最早门槛尚未通过，但用户要求跳到原型、HTML、交付稿或完整 PRD。

## 输出

```text
自动评审结果：

工作方式：
- 当前模式：
- 当前一步：
- 已完成：
- 下一步：
- 你只需要：

自动评审结论：
- 我建议：
- 理由：
- 当前需要确认：
- 下一步：

内部评审控制面板（默认不展示，写入审计）：
- 状态：
- run_id：
- 模式：<快速成型 / 深度交付>
- 模式来源：
- 推进阶段：
- 当前门槛：
- 最早门槛：
- 门槛等级：
- 门槛来源：
- 停止原因：
- 下一技能：
- 交接上下文：
- 已自动采用：
- 需要 PM 拍板：
- 证据状态：
- 证据状态页：
- 产品准备度仪表盘：
- 产物流动：
- 上游产物：
- 本轮产物：
- 下游可读：
- 产品简报：
- 方案方向：
- 轻量包图片计划：
- Zoon 同步：
- Zoon 漂移检查：
- 原型准备度：
- 可升级到：
- 建议下一步：
```

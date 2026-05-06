---
name: pm-workspace
description: |
  PMWorkspace 主入口，面向产品经理和设计师。用于把产品想法、PRD、Zoon 文档、
  截图、客户洞察或原型请求，路由到问题定义、策略审查、产品简报、移动端优先
  image-2 原型探索或交付稿。负责首次引导、更新检查、本地使用记录，并路由到
  pm-jobs、pm-strategy-review、pm-brief、pm-prototype-shotgun 或 pm-handoff。
  也用于用户刚安装 PMWorkspace 后需要欢迎引导、启动话术或选择第一步。
---

# PMWorkspace

PMWorkspace 是产品工作台，用于把原始产品上下文沉淀成可复用资产：决策、产品简报、原型提示词、image-2 屏幕和交付稿。

Before user-facing output, read `../pmworkspace-shared/references/language-and-localization.md`. For Chinese users, use Chinese headings, labels, status values, and recommendations; keep English only for skill ids, commands, file paths, and precise technical terms such as `token`, `API`, `PRD`, `Zoon`, `image-2`, and `URL`.

## Product Workbench State Machine

PMWorkspace is not a prototype shortcut. It must first clarify product value, goals, counter-metrics, constraints, and premises, then turn aligned product judgment into image-2 prototypes.

Use this state machine for prototype-related work:

```text
工作目标模式 -> 场景路由 -> Q 诊断 -> 前提确认 -> D 拍板 -> 产品简报 -> image-2 原型
```

If any required step is incomplete, route to `$pm-jobs` or `$pm-brief` instead of generating prototypes.

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

- 原始想法、模糊产品请求、“帮我想想”、问题定义 -> 使用 `$pm-jobs`。
- 范围、野心、策略取舍、“想大一点”、“是否值得做” -> 使用 `$pm-strategy-review`。
- 需要可编辑的产品简报、Zoon 对齐或决策记录 -> 使用 `$pm-brief`。
- 需要原型方向、image-2 设计图、多方案、截图修改 -> 使用 `$pm-prototype-shotgun`。
- 需要适合 PRD、设计、实验验证或研发使用的交付稿 -> 使用 `$pm-handoff`。

When unsure, start with `$pm-jobs`; product clarity comes before prototype output.

## Welcome And First Run

If the user invokes `$pm-workspace` with no concrete product task, asks what PMWorkspace does, or has just installed it, read `../pmworkspace-shared/references/welcome-guide.md` and give the welcome message plus the first choice menu.

Do not make the user guess the command set. The first response should feel like an app onboarding screen: short orientation, clear paths, and one recommended next step.

If the user provides a product task in the same message, skip the welcome menu and route directly.

## Operating Rules

- 写图片提示词或生成图片前，必须先完成产品简报对齐。
- 产品简报不是 `已对齐` 时，不写 image-2 提示词，不生成图片，不生成 HTML，不输出交付稿。
- 用户提供截图或线上参考时，只更新视觉基线和线上参考状态；不要自动产出完整 md 方案、HTML 或原型图。
- 诊断问题使用 `Q`，一次只问一个；默认 3 个核心 Q，只有原型重点或约束边界仍不清楚时最多追加到 5 个。拍板问题使用 `D`，一次只展开一个，问完必须等待用户回答。
- 产品简报前必须完成前提确认；未确认前只能保持 `待确认`。
- 关键产品决策默认使用选择题拍板；读取 `decision-question-mode.md`。
- 新页面也要判断线上参考需求；承接线上流程、结果页、状态页或生产样式时，缺截图/录屏/相似页面参考要先问。
- 产品简报阶段可以按主场景做轻量互联网最佳实践检索；检索结果只用于案例启发和原型重点建议，不增加 Q 数量。
- 产品简报阶段默认创建或更新 Zoon 在线文档，并在成功后自动打开到 Codex 内置浏览器；后续原型/交付前优先读取 Zoon 最新内容。
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
PMWorkspace 像一个产品团队：先用 $pm-jobs 问清楚真实问题，再用 $pm-strategy-review 挑战方向，用 $pm-brief 固化产品简报，用 $pm-prototype-shotgun 生成移动端优先的 image-2 原型方案，最后用 $pm-handoff 整理交付稿。
```

Then route to the smallest useful next skill.

## Shared References

Use `../pmworkspace-shared/references/` for:

- `language-and-localization.md` for output language and Chinese terminology.
- `decision-question-mode.md` for PM decision questions.
- `internet-best-practice-research.md` for lightweight public UX/product case research.
- `production-reference-gate.md` for online screenshot/reference checks before prototypes.
- `welcome-guide.md` for install success and first-run onboarding.
- `routing.md` for route selection.
- `state-and-telemetry.md` for durable asset rules.
- `update-workflow.md` for update prompts.
- Existing product references for gates, methods, prompt templates, AutoDesign, Zoon, and QA.

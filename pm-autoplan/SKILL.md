---
name: pm-autoplan
description: |
  PMWorkspace 自动产品评审流水线。用于用户希望“一次跑完整产品评审”“自动把
  产品方向梳理到可出原型前”“按推荐推进但关键点让我拍板”，或希望快速产出
  “产品简报 + 方案方向 + 原型图”轻量包时。支持快速成型模式和深度交付模式。
  快速成型模式用最少追问确认假设后产出可讨论轻量包；深度交付模式顺序串联
  pm-jobs、pm-strategy-review、pm-brief、Zoon 同步、Zoon 漂移检查和原型
  准备度检查，只把会改变方向的 D 选择题交给用户确认。
---

# 自动产品评审

`$pm-autoplan` 是 PMWorkspace 的一键推进模式：把零散想法推进成可讨论轻量包，或推进到可确认的产品简报与交付资产。它不是跳过产品判断直接出图。

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
```

## Workflow

1. Read `../pmworkspace-shared/references/autoplan-workflow.md`.
2. Read `../pmworkspace-shared/references/runtime-kernel.md`.
3. Read `../pmworkspace-shared/references/evidence-dashboard.md`.
4. Read `../pmworkspace-shared/references/question-tuning.md`.
5. Read `../pmworkspace-shared/references/product-office-hours.md`.
6. Read `../pmworkspace-shared/references/adversarial-review.md`.
7. Read `../pmworkspace-shared/references/product-plan-handoff.md`.
8. Read `../pmworkspace-shared/references/zoon-workflow.md` and `../pmworkspace-shared/references/zoon-drift-check.md`.
9. Choose mode:
   - 快速成型模式：用户要求轻量包、先看方案、快速出可讨论材料，或是新 idea 且没有明确 PRD/交付要求。
   - 深度交付模式：用户要求 PRD、Zoon 对齐、已有线上截图/生产流程、设计/研发交付、或高风险业务流程。
10. After mode is chosen, start `pmw-run start --skill pm-autoplan --mode <quick|deep> --goal "<本轮目标>"` when available.
11. 快速成型模式：只检测最早会影响轻量包的缺口：核心用户/场景、核心问题、主目标/反指标、不可虚构项、原型屏幕范围。默认最多问 2-3 个 `Q`。
12. 快速成型模式：列出关键假设、方案方向和每张图的不可虚构项，请用户确认“按这些假设继续”。确认前不生成图片，并用 `pmw-run event --type gate` 记录当前门槛。
13. 快速成型模式：确认后输出轻量包：标注假设的产品简报、2-3 个方案方向、每个方案 1 张移动端 image-2 原型图计划，并把状态写成 `基于假设，可讨论`。
14. 深度交付模式：Detect the earliest missing gate in this order: 工作目标模式、场景路由、Q 诊断、前提确认、必要 D、产品简报、Zoon 同步、原型准备度。
15. 深度交付模式：Auto-decide only low-risk defaults that do not change product direction; surface any direction-changing item as a single `D` choice question and stop.
16. When enough information exists, create the smallest useful product brief and save it with `pmw-log brief <name>`. Because `pmw-log brief` auto-syncs, this should create or append to Zoon when enabled.
17. If a Zoon URL exists before prototype preparation, run `pmw-zoon drift --url <url>` when available. If it returns `DRIFT`, read the latest Zoon snapshot and update the product brief version before continuing.
18. At each gate, record evidence, decisions, artifacts, or reviews with `pmw-run event`; before final output, run `pmw-dashboard status` when available.
19. End with a readiness state: `需要补充`、`待确认`、`基于假设，可讨论`、`已对齐`、`可进入原型复审`、or `可交付`, and call `pmw-run finish`.

## Auto-Decide Rules

自动接受：

- 用户已经明说或文档中明确写出的事实。
- 默认移动端优先画布。
- 不影响方向的格式、标题、状态字段。
- 已有 Zoon URL 时优先 append，不新建文档。
- 快速成型模式中，不影响方案结构的轻量包格式和默认输出数量。

必须提问：

- 目标人群、主目标、反指标、不可虚构项仍会改变原型结构。
- 多方案方向没有本质差异。
- 线上参考需要但缺失。
- Zoon 最新内容和本地产品简报冲突。
- 用户承诺、数据真实性、线索/交易/隐私口径需要 PM 拍板。
- 快速成型模式出图前，用户尚未确认“按这些假设继续”。

## 输出

```text
自动评审结果：
- 状态：
- run_id：
- 模式：<快速成型 / 深度交付>
- 当前门槛：
- 已自动采用：
- 需要 PM 拍板：
- 证据状态页：
- 产品简报：
- 方案方向：
- 轻量包图片计划：
- Zoon 同步：
- Zoon 漂移检查：
- 原型准备度：
- 可升级到：
- 建议下一步：
```

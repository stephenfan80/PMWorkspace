---
name: pm-autoplan
description: |
  PMWorkspace 自动产品评审流水线。用于用户希望“一次跑完整产品评审”“自动把
  产品方向梳理到可出原型前”“按推荐推进但关键点让我拍板”时。顺序串联
  pm-jobs、pm-strategy-review、pm-brief、Zoon 同步、Zoon 漂移检查和原型
  准备度检查，只把会改变方向的 D 选择题交给用户确认。
---

# 自动产品评审

`$pm-autoplan` 是 PMWorkspace 的一键评审模式：把零散想法推进到可确认的产品简报，而不是跳过产品判断直接出图。

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
```

## Workflow

1. Read `../pmworkspace-shared/references/autoplan-workflow.md`.
2. Read `../pmworkspace-shared/references/product-office-hours.md`.
3. Read `../pmworkspace-shared/references/adversarial-review.md`.
4. Read `../pmworkspace-shared/references/product-plan-handoff.md`.
5. Read `../pmworkspace-shared/references/zoon-workflow.md` and `../pmworkspace-shared/references/zoon-drift-check.md`.
6. Detect the earliest missing gate in this order: 工作目标模式、场景路由、Q 诊断、前提确认、必要 D、产品简报、Zoon 同步、原型准备度。
7. Auto-decide only low-risk defaults that do not change product direction; surface any direction-changing item as a single `D` choice question and stop.
8. When enough information exists, create the smallest useful product brief and save it with `pmw-log brief <name>`. Because `pmw-log brief` auto-syncs, this should create or append to Zoon when enabled.
9. If a Zoon URL exists before prototype preparation, run `pmw-zoon drift --url <url>` when available. If it returns `DRIFT`, read the latest Zoon snapshot and update the product brief version before continuing.
10. End with a readiness state: `需要补充`、`待确认`、`已对齐`、或 `可进入原型复审`.

## Auto-Decide Rules

自动接受：

- 用户已经明说或文档中明确写出的事实。
- 默认移动端优先画布。
- 不影响方向的格式、标题、状态字段。
- 已有 Zoon URL 时优先 append，不新建文档。

必须提问：

- 目标人群、主目标、反指标、不可虚构项仍会改变原型结构。
- 多方案方向没有本质差异。
- 线上参考需要但缺失。
- Zoon 最新内容和本地产品简报冲突。
- 用户承诺、数据真实性、线索/交易/隐私口径需要 PM 拍板。

## 输出

```text
自动评审结果：
- 状态：
- 当前门槛：
- 已自动采用：
- 需要 PM 拍板：
- 产品简报：
- Zoon 同步：
- Zoon 漂移检查：
- 原型准备度：
- 建议下一步：
```

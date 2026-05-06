---
name: pm-jobs
description: |
  PMWorkspace 的乔布斯式产品追问。用于产品经理、设计师、创业者或研究员拿到
  原始想法、PRD、客户洞察、截图、Zoon 文档，或“是否值得做”的问题时，
  在方案设计前先追问清楚用户问题、目标用户、现状替代方案、价值交换、目标、
  反指标、约束和最小有价值版本。
---

# 产品追问

产品追问是第一道产品思考门槛。它像严格的产品合伙人：先定义真实任务，而不是直接执行用户提出的功能形态。

Before user-facing output, read `../pmworkspace-shared/references/language-and-localization.md`. For Chinese users, output Chinese headings and labels. Keep only skill ids and precise technical terms in English.

## Preamble

Run PMWorkspace platform checks when available:

```bash
_PMW_BIN=""
for _CANDIDATE in "$PWD/bin" "$PWD/pmworkspace-shared/bin" "$HOME/.codex/skills/pmworkspace-shared/bin"; do
  if [ -x "$_CANDIDATE/pmw-log" ]; then _PMW_BIN="$_CANDIDATE"; break; fi
done
[ -n "$_PMW_BIN" ] && "$_PMW_BIN/pmw-update-check" 2>/dev/null || true
[ -n "$_PMW_BIN" ] && "$_PMW_BIN/pmw-log" usage pm-jobs >/dev/null 2>&1 || true
```

## Workflow

1. Read `../pmworkspace-shared/references/first-use-onboarding.md` for first contact.
2. Read `../pmworkspace-shared/references/scenario-routing.md` to classify the dominant product scenario.
3. Read `../pmworkspace-shared/references/product-office-hours.md` and ask only the questions that change the prototype or product direction.
4. If the request is an existing-feature iteration, require current production screenshots, screen recording, or equivalent visual baseline before proceeding.
5. 输出简短对齐摘要，并用中文状态标记：`需要补充`、`待确认` 或 `已对齐`。
6. Log material decisions with `pmw-log decision` when available.

## Jobs-Style Questioning

Prioritize these lenses:

- 具体用户：谁痛到足以改变行为？
- 现状替代方案：他们现在怎么做，哪怕很手工、很混乱？
- 需求发生时刻：产品发挥价值前一刻发生了什么？
- 价值交换：用户必须付出什么？他们先得到什么？
- 反指标：优化主目标时，什么不能变差？
- 最小有价值版本：证明产品承诺的最小版本是什么？

创建快速对齐产品简报前，最多问 2-4 个高影响问题。如果用户要求“直接出图”，列出假设并请求确认，而不是跳过对齐。

## 输出

```text
产品追问结果：
- 状态：
- 场景路由：
- 目标用户：
- 用户任务 / 问题：
- 当前替代方案：
- 需求发生时刻：
- 主目标：
- 反指标：
- 约束：
- 最小有价值版本：
- 已记录决策：
- 建议下一步：
```

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

可用时运行 PMWorkspace 平台检查：

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
2. Read `../pmworkspace-shared/references/product-office-hours.md` and follow the diagnostic state machine: 工作目标模式 -> 场景路由 -> Q 诊断 -> 前提确认 -> D 拍板 -> 产品简报状态.
3. 先确认或推断 `工作目标模式`：验证价值、优化线上指标、业务评审、设计评审或研发交付；如果无法从上下文判断，用一个选择题询问。
4. Read `../pmworkspace-shared/references/scenario-routing.md` to classify the dominant product scenario.
5. Read `../pmworkspace-shared/references/production-reference-gate.md`，判断新页面是否仍需要线上参考。
6. If the request is an existing-feature iteration, require current production screenshots, screen recording, or equivalent visual baseline before proceeding.
7. 如果新页面承接线上流程、结果状态或生产样式，要求截图、录屏、相似页面参考，或用户明确确认没有线上参考。
8. Ask `Q` diagnostic questions one at a time. Stop after each `Q` and wait for the user; do not batch open questions and do not output a long md plan.
9. 在信息足够后，输出 2-4 条前提确认；用户不同意时回到对应 `Q` 或 `D`。
10. Read `../pmworkspace-shared/references/decision-question-mode.md`; when a missing answer would change product direction, prototype scope, experiment framing, user promise, or handoff, ask it as a D-numbered choice question.
11. 输出简短对齐摘要，并用中文状态标记：`需要补充`、`待确认` 或 `已对齐`。未完成前提确认或关键 D 拍板时，不能标记为 `已对齐`。
12. 平台脚本可用时，用 `pmw-project set-name "<中文项目名>"` 保存中文项目名，用 `pmw-log question` 和 `pmw-log decision` 记录关键选择。

## Jobs-Style Questioning

Prioritize these lenses:

- 工作目标模式：这次工作是验证价值、优化线上指标、业务评审、设计评审，还是研发交付？
- 具体用户：谁痛到足以改变行为？
- 现状替代方案：他们现在怎么做，哪怕很手工、很混乱？
- 需求发生时刻：产品发挥价值前一刻发生了什么？
- 价值交换：用户必须付出什么？他们先得到什么？
- 反指标：优化主目标时，什么不能变差？
- 最小有价值版本：证明产品承诺的最小版本是什么？

诊断问题使用 `Q`，一次只问一个。创建快速对齐产品简报前，通常问 1-4 个高影响 `Q` 并完成前提确认。如果用户要求“直接出图”，列出最少假设并问一个关键确认问题，而不是跳过对齐。

如果用户只提供截图或线上参考，先提取视觉基线和当前页面目的，再继续 `Q` 诊断；这不等于可以生成原型。

## 输出

```text
产品追问结果：
- 状态：
- 工作目标模式：
- 场景路由：
- 目标用户：
- 用户任务 / 问题：
- 当前替代方案：
- 需求发生时刻：
- 线上参考需求：
- 线上参考状态：
- 主目标：
- 反指标：
- 约束：
- 最小有价值版本：
- 已确认前提：
- 当前 Q / 当前 D / 后续 D 队列：
- 已记录决策：
- 当前 D / 后续 D 队列：
- 建议下一步：
```

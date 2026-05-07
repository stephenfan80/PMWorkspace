---
name: pm-jobs
description: |
  PMWorkspace 的乔布斯式产品追问。用于产品经理、设计师、创业者或研究员拿到
  原始想法、PRD、客户洞察、截图、Zoon 文档，或“是否值得做”的问题时，
  在方案设计前用 3-5 个核心 Q 帮产品经理梳理目标人群、核心问题、
  当前损失、目标指标、原型重点和约束边界。
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
[ -n "$_PMW_BIN" ] && [ -x "$_PMW_BIN/pmw-question-tuning" ] && "$_PMW_BIN/pmw-question-tuning" summary 2>/dev/null || true
```

## Workflow

1. Read `../pmworkspace-shared/references/first-use-onboarding.md` for first contact.
2. Read `../pmworkspace-shared/references/product-office-hours.md` and follow the diagnostic state machine: 工作目标模式 -> 场景路由 -> Q 诊断 -> 前提确认 -> D 拍板 -> 产品简报状态.
3. Read `../pmworkspace-shared/references/product-memory.md` and use `pmw-memory summary` when available to avoid repeating known preferences or resolved decisions.
4. Read `../pmworkspace-shared/references/question-tuning.md` and apply saved Q/D preferences without overriding current facts or high-risk gates.
5. Read `../pmworkspace-shared/references/pm-decision-principles.md` and apply its fact priority before using memory or defaults.
6. Read `../pmworkspace-shared/references/pm-eval-system.md` so diagnostic output preserves PMWorkspace gate contracts.
7. Read `../pmworkspace-shared/references/pm-workbench-map.md` and use its 产品追问 stage fields.
8. Read `../pmworkspace-shared/references/runtime-kernel.md`; follow its Run Owner 协议：如果 `pmw-project show` 已有 `current_run_id`，复用当前 run；如果用户直接调用 `$pm-jobs` 且没有当前 run，再创建 runtime run.
9. Build the 产品追问控制器 from `product-office-hours.md`: 模式来源、已知事实、证据状态、已覆盖诊断维度、当前最大缺口、Q 预算、当前动作.
10. 如果来自 `$pm-autoplan`，只解决自动评审交给 `$pm-jobs` 的最早门槛：工作目标、场景、Q 诊断或前提确认；不要假装后续产品简报、原型或交付已完成。
11. 先确认或推断 `工作目标模式`：验证价值、优化线上指标、业务评审、设计评审或研发交付；如果无法从上下文判断，用一个选择题询问。
12. Read `../pmworkspace-shared/references/scenario-routing.md` to classify the dominant product scenario.
13. Read `../pmworkspace-shared/references/scenario-experts.md` and select only the dominant expert lens.
14. Read `../pmworkspace-shared/references/browser-evidence.md` when the user provides URL、线上页面、竞品或 Zoon 参考。
15. Read `../pmworkspace-shared/references/production-reference-gate.md`，判断新页面是否仍需要线上参考。
16. If the request is an existing-feature iteration, require current production screenshots, screen recording, or equivalent visual baseline before proceeding.
17. 如果新页面承接线上流程、结果状态或生产样式，要求截图、录屏、相似页面参考，或用户明确确认没有线上参考。
18. Ask `Q` diagnostic questions one at a time. 默认最多问 3 个动态 Q；只有信息不足以生成有价值原型时，最多追加到 5 个。Stop after each `Q` and wait for the user; do not batch open questions and do not output a long md plan.
19. If the current最大缺口 is evidence, stop with one evidence request; do not continue with product questions.
20. If the missing item is a fact, ask one `Q`; if facts are enough but a tradeoff changes direction, scope, promise, experiment framing, or handoff, ask one `D`.
21. 在信息足够后，输出 2-4 条前提确认；用户不同意时回到对应 `Q` 或 `D`。
22. Read `../pmworkspace-shared/references/decision-question-mode.md`; when a missing answer would change product direction, prototype scope, experiment framing, user promise, or handoff, ask it as a D-numbered choice question.
23. 输出简短对齐摘要，并用中文状态标记：`需要补充`、`待确认` 或 `已对齐`。未完成前提确认或关键 D 拍板时，不能标记为 `已对齐`。
24. 平台脚本可用时，用 `pmw-project set-name "<中文项目名>"` 保存中文项目名，用 `pmw-log question`、`pmw-log decision` 和 `pmw-run event` 记录关键选择。

## Jobs-Style Questioning

Prioritize a dynamic question from the diagnosis dimension pool. The dimensions are fixed; the user-facing question text and title are not fixed.

- 目标人群与使用场景
- 核心问题与当前损失
- 本次目标与反指标
- 原型内容重点
- 约束边界与不可虚构项

诊断问题使用 `Q`，一次只问一个。每轮根据用户输入、场景路由、线上参考状态和当前信息缺口，选择一个最会影响产品简报或原型结构的维度来动态生成问题；如果用户已经回答了某个维度，就跳过该维度。Q 标题使用中文短标题，格式为 `Qn <当前意图>`，例如 `Q1 转化对象`、`Q2 首屏价值`、`Q3 数据承诺边界`。创建快速对齐产品简报前，通常覆盖 2-3 个关键诊断维度并完成前提确认；只有原型内容或约束边界仍不清楚时，才追加到 5 个 Q。用户回答模糊时，在当前 Q 内追问一次把答案压实，不新增一串问题。如果用户要求“直接出图”，列出最少假设并问一个最关键 Q，而不是跳过对齐。

如果用户只提供截图或线上参考，先提取视觉基线和当前页面目的，再继续 `Q` 诊断；这不等于可以生成原型。

## 输出

```text
产品追问结果：
- 状态：
- run_id：
- 模式来源：
- 诊断阶段：
- 当前最大缺口：
- Q 预算：
- 停止原因：
- 下一技能：
- 证据状态：
- 工作目标模式：
- 场景路由：
- 目标人群：
- 核心问题梳理：
- 用户任务 / 问题：
- 当前替代方案：
- 需求发生时刻：
- 线上参考需求：
- 线上参考状态：
- 主目标：
- 反指标：
- 约束：
- 最小有价值版本：
- 原型内容重点：
- 已确认前提：
- 当前 Q：
- 当前 D：
- 后续 D 队列：
- 已记录决策：
- 建议下一步：
```

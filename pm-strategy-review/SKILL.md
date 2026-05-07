---
name: pm-strategy-review
description: |
  PMWorkspace 策略审查。用于产品方向、产品简报、PRD、原型概念或范围决策，
  在设计或交付前需要被挑战时。审查野心、范围、定位、价值交换、信任、
  反指标、可行性、风险、应该删除什么、应该扩大什么，以及哪些必须由 PM 拍板。
---

# 策略审查

在原型或交付前挑战产品方向。目标是更强的产品策略，而不是默认堆更多功能。

Before user-facing output, read `../pmworkspace-shared/references/language-and-localization.md`. For Chinese users, avoid English labels; use Chinese headings, status values, and recommendations.

## Preamble

Run update and usage checks when platform scripts are available:

```bash
_PMW_BIN=""
for _CANDIDATE in "$PWD/bin" "$PWD/pmworkspace-shared/bin" "$HOME/.codex/skills/pmworkspace-shared/bin"; do
  if [ -x "$_CANDIDATE/pmw-log" ]; then _PMW_BIN="$_CANDIDATE"; break; fi
done
[ -n "$_PMW_BIN" ] && "$_PMW_BIN/pmw-update-check" 2>/dev/null || true
[ -n "$_PMW_BIN" ] && "$_PMW_BIN/pmw-log" usage pm-strategy-review >/dev/null 2>&1 || true
```

## Workflow

1. 读取当前产品简报或 `$pm-jobs` 对齐结果。
2. Read `../pmworkspace-shared/references/adversarial-review.md`.
3. Read `../pmworkspace-shared/references/decision-question-mode.md`.
4. Read `../pmworkspace-shared/references/scenario-experts.md` and use the dominant scenario lens.
5. Read `../pmworkspace-shared/references/product-memory.md`; use memory only as preference signal, not as fact source.
6. Read `../pmworkspace-shared/references/pm-workbench-map.md` and use its 策略审查 stage fields.
7. Read `../pmworkspace-shared/references/runtime-kernel.md`; follow its Run Owner 协议：如果 `pmw-project show` 已有 `current_run_id`，复用当前 run；如果用户直接调用 `$pm-strategy-review` 且没有当前 run，再创建 runtime run.
8. Build the 策略取舍控制器 from `adversarial-review.md`: 来源门槛、已确认事实、策略风险类型、3-5 个审查视角、建议姿态、策略取舍、当前 D / 后续 D 队列、下一技能.
9. 如果来自 `$pm-jobs`，只接住产品追问交出的策略门槛：范围、价值交换、信任/风险、反指标、可行性、定位或业务冲突；不要重新展开 Q 诊断全流程。
10. If basic facts such as user, problem, main goal, anti-metric, or non-fiction boundary are missing, route back to `$pm-jobs` with one focused `Q`; do not use strategy review to invent missing facts.
11. Select 3-5 challenge lenses relevant to the strategy risk type and scenario.
12. Present concrete strategy choices. Do not silently change scope, add promises, move anti-metrics, or include unsupported capabilities.
13. 把“需要 PM 拍板”的点转成选择题；每轮只展开一个完整 `D`，其余只提示后续标题队列。
14. If strategy review resolves the tradeoff, route next to `$pm-brief` by default so the decision becomes part of the product contract. If the brief is already aligned and only direction review was requested, route next to `$pm-prototype-shotgun` or `$pm-handoff`.
15. Log accepted strategy decisions with `pmw-log question` and `pmw-log decision` when platform scripts are available.

## Review Lenses

- 问题真实性和证据。
- 现状替代方案。
- 扩大范围还是收缩范围。
- 高摩擦或高成本动作前，是否先给价值。
- 信任、隐私和数据可信度。
- 业务冲突或指标游戏。
- 可行性和无法支持的承诺。
- 边界情况和失败状态。
- 设计系统匹配度。

## 输出

```text
策略审查结果：
- run_id：
- 来源门槛：
- 策略风险类型：
- 使用视角：
- 证据状态：
- 最强前提：
- 最弱假设：
- 建议姿态：扩大 / 保持 / 收缩 / 转向
- 策略取舍：
- 范围外：
- 对原型的影响：
- 当前 D：
- 后续 D 队列：
- 下一技能：
- 建议下一步：
```

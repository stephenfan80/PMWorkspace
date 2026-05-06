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
4. Select 3-5 challenge lenses relevant to the scenario.
5. Present concrete strategy choices. Do not silently change scope.
6. 把“需要 PM 拍板”的点转成选择题；一次最多 3 个，超过 3 个分批问。
7. Log accepted strategy decisions with `pmw-log question` and `pmw-log decision` when platform scripts are available.

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
- 最强前提：
- 最弱假设：
- 建议姿态：扩大 / 保持 / 收缩 / 转向
- 策略选择：
- 范围外：
- 对原型的影响：
- 需要 PM 拍板的选择题：
- 建议下一步：
```

---
name: pm-handoff
description: |
  PMWorkspace 交付稿生成器。用于把已对齐的产品简报、选定原型方向、PRD 笔记、
  Zoon 文档或产品决策记录，整理成适合 PRD、设计、实验验证或研发使用的交付稿，
  包含目标、范围、不做什么、验收标准、指标、风险、待决策项和可复用下一步。
---

# 产品交付稿

把选定产品方向整理成可复用交付稿，同时明确保留未解决的问题。

Before user-facing output, read `../pmworkspace-shared/references/language-and-localization.md`. For Chinese users, call the artifact `交付稿` and use Chinese headings. Keep `PRD` when referring to the document type.

## Preamble

运行平台检查和使用记录：

```bash
_PMW_BIN=""
for _CANDIDATE in "$PWD/bin" "$PWD/pmworkspace-shared/bin" "$HOME/.codex/skills/pmworkspace-shared/bin"; do
  if [ -x "$_CANDIDATE/pmw-log" ]; then _PMW_BIN="$_CANDIDATE"; break; fi
done
[ -n "$_PMW_BIN" ] && "$_PMW_BIN/pmw-update-check" 2>/dev/null || true
[ -n "$_PMW_BIN" ] && "$_PMW_BIN/pmw-log" usage pm-handoff >/dev/null 2>&1 || true
[ -n "$_PMW_BIN" ] && [ -x "$_PMW_BIN/pmw-dashboard" ] && "$_PMW_BIN/pmw-dashboard" status 2>/dev/null || true
```

## Workflow

1. Read `../pmworkspace-shared/references/delivery-handoff.md`.
2. Read `../pmworkspace-shared/references/product-plan-handoff.md`; require the latest product brief to be `已对齐`.
3. Read `../pmworkspace-shared/references/prototype-quality-review.md` and require prototype-dependent delivery to have `原型复审状态：可通过`.
4. Read `../pmworkspace-shared/references/pm-review-army.md`; unresolved review findings must not be hidden in delivery notes.
5. Read `../pmworkspace-shared/references/pm-decision-principles.md`; unresolved user promise, data truth, scope, experiment, lead, transaction, privacy, compliance, or acceptance boundary issues must become `需要 PM 拍板`.
6. Read `../pmworkspace-shared/references/decision-question-mode.md`; 每轮只展开一个当前 `D`，不要批量写多个验收相关决策。
7. Read `../pmworkspace-shared/references/runtime-kernel.md`.
8. Read `../pmworkspace-shared/references/evidence-dashboard.md` and run `pmw-dashboard status` when available.
9. Read `../pmworkspace-shared/references/prototype-shotgun-board.md`; if a selected prototype direction exists, include the board result instead of relying on memory.
10. Read `../pmworkspace-shared/references/zoon-drift-check.md`.
11. Read `../pmworkspace-shared/references/pm-workbench-map.md` and use its 产品交付 stage fields.
12. Read `../pmworkspace-shared/references/pm-eval-system.md` and preserve delivery contracts.
13. Follow `runtime-kernel.md` Run Owner 协议：如果 `pmw-project show` 已有 `current_run_id`，复用当前 run；如果用户直接调用 `$pm-handoff` 且没有当前 run，再创建 runtime run.
14. 建立交付控制器，记录 `交付目标`、`事实来源`、`交付前门槛`、`原型复审状态`、`未决拍板`、`交付类型`、`验收写入边界`、`范围外`、`下一技能` 和 `证据状态`。
15. 如果 `pmw-project show` 中有 Zoon URL，先运行 `pmw-zoon drift`；若存在实质漂移，读取最新文档，作为交付事实来源，并退回 `$pm-brief` 或 `$pm-strategy-review`，不要沿用旧交付口径。
16. 如果产品简报不是 `已对齐`，退回 `$pm-brief`；如果交付依赖原型但复审不是 `可通过`，退回 `$pm-prototype-review`、`$pm-prototype-shotgun` 或当前 `D`。
17. 如果仍有会改变范围、用户承诺、实验口径、数据真实性、线索/交易/隐私/合规边界或验收标准的未决 D，停止在 `需要 PM 拍板`，只输出一个当前 `D`，不写研发验收标准。
18. 选择交付类型：PRD、设计交付、实验验证、研发交付，或组合；只输出当前需要的深度。
19. 包含目标、目标用户、问题、场景、选定方向、范围、范围外、验收标准、指标、风险、依赖和待决策项。
20. Keep unsupported capabilities under `不可虚构`; unsupported capabilities, unverified data, unresolved commitments, and future ideas must not appear as acceptance criteria.
21. 平台脚本可用时，用 `pmw-log handoff <name>` 保存交付稿，记录 `pmw-run event --type artifact`，并且只有交付前门槛全部通过时才 `pmw-run finish --status "可交付"`。

## 输出结构

```markdown
# PMWorkspace 交付稿：<功能名>

## 证据状态

- run_id：
- 交付目标：
- 事实来源：
- 交付前门槛：
- 原型复审状态：
- 未决拍板：
- 交付类型：
- 验收写入边界：
- 下一技能：
- 已保存资产：

## 摘要

## 目标与指标

## 用户 / 任务 / 场景

## 选定方向

## 范围

## 不做什么

## 验收标准

## 实验或上线说明

## 风险与待决策

## 不可虚构
```

---
name: pm-handoff
description: |
  PMWorkspace 精简 PRD 交付官。用于把已对齐的产品简报、选定原型方向、PRD 笔记、
  Zoon 文档或产品决策记录，压缩成可执行的最小交付契约；默认 PRD 只保留需求背景、
  需求价值、需求方案、需求功能及描述、接口以及数据来源、埋点信息和实验标准。
---

# 产品交付

把选定产品方向整理成精简 PRD 和可复用交付资产，同时明确保留未解决的问题。`$pm-handoff` 是精简 PRD 交付官，不是项目管理计划、测试计划或开发周期排期工具。

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
[ -n "$_PMW_BIN" ] && [ -x "$_PMW_BIN/pmw-memory" ] && "$_PMW_BIN/pmw-memory" user-summary 2>/dev/null || true
[ -n "$_PMW_BIN" ] && [ -x "$_PMW_BIN/pmw-memory" ] && "$_PMW_BIN/pmw-memory" delivery-summary 2>/dev/null || true
[ -n "$_PMW_BIN" ] && [ -x "$_PMW_BIN/pmw-dashboard" ] && "$_PMW_BIN/pmw-dashboard" status 2>/dev/null || true
[ -n "$_PMW_BIN" ] && [ -x "$_PMW_BIN/pmw-dashboard" ] && "$_PMW_BIN/pmw-dashboard" readiness --target handoff 2>/dev/null || true
[ -n "$_PMW_BIN" ] && [ -x "$_PMW_BIN/pmw-artifact" ] && "$_PMW_BIN/pmw-artifact" flow 2>/dev/null || true
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
9. Read `../pmworkspace-shared/references/product-readiness-dashboard.md` and run `pmw-dashboard readiness --target handoff` when available.
10. Read `../pmworkspace-shared/references/prototype-shotgun-board.md`; if a selected prototype direction exists, include the board result instead of relying on memory.
11. Read `../pmworkspace-shared/references/zoon-drift-check.md`.
12. Read `../pmworkspace-shared/references/product-memory.md`; use `pmw-memory user-summary` and `pmw-memory delivery-summary` when available. If delivery assets affect wording, explicitly say `基于本地交付资产...`; memory cannot override the current brief, Zoon, 反指标, 不可虚构项, 线上参考门槛 or 本轮输入。
13. Read `../pmworkspace-shared/references/pm-workbench-map.md` and use its 产品交付 stage fields.
14. Read `../pmworkspace-shared/references/artifact-flow.md` and read latest `product_brief` / `prototype_review` artifacts before writing delivery assets.
15. Read `../pmworkspace-shared/references/pm-eval-system.md` and preserve delivery contracts.
16. Follow `runtime-kernel.md` Run Owner 协议：如果 `pmw-project show` 已有 `current_run_id`，复用当前 run；如果用户直接调用 `$pm-handoff` 且没有当前 run，再创建 runtime run.
17. 如果用户要 PRD、研发交付、实验标准、埋点或接口梳理，先提示：`如果你有现成 PRD、接口文档、埋点方案、实验方案、Zoon 或截图，可以上传给我参考；没有的话，我会基于当前已对齐 brief 生成精简 PRD，并把缺失项留空待补充。`
18. 建立交付控制器，记录 `交付目标`、`事实来源`、`Product Readiness Dashboard`、`交付前门槛`、`原型复审状态`、`未决拍板`、`交付类型`、`PRD 缺口处理`、`验收写入边界`、`交付资产沉淀`、`上游产物`、`本轮产物`、`下游可读`、`产物流动`、`下一技能` 和 `证据状态`。
18. 如果 `pmw-project show` 中有 Zoon URL，先运行 `pmw-zoon drift`；若存在实质漂移，读取最新文档，作为交付事实来源，并退回 `$pm-brief` 或 `$pm-strategy-review`，不要沿用旧交付口径。
19. 如果产品简报不是 `已对齐`，退回 `$pm-brief`；如果交付依赖原型但复审不是 `可通过`，退回 `$pm-prototype-review`、`$pm-prototype-shotgun` 或当前 `D`。
20. 交付稿输出前必须展示 Product Readiness Dashboard；如果 verdict 是 `不可交付`，根据第一条阻断行退回 `$pm-brief`、线上参考门槛、`$pm-prototype-shotgun`、`$pm-prototype-review` 或当前 `D`，不写 PRD、实验口径或验收标准。
21. 如果仍有会改变范围、用户承诺、实验口径、数据真实性、线索/交易/隐私/合规边界或验收标准的未决 D，停止在 `需要 PM 拍板`，只输出一个当前 `D`，不写研发验收标准、实验口径或对外承诺。
22. 默认选择 `精简 PRD`；只有用户明确要求设计交付、实验验证或研发交付时，才追加对应补充，不把所有模板硬塞进一份文档。
23. 精简 PRD 核心只保留：需求背景、需求价值、需求方案、需求功能及描述、接口以及数据来源、埋点信息、实验标准。测试计划、开发周期、排期、人力、会议纪要和长风险清单默认不写。
24. 缺接口、数据字段、埋点属性或实验细节但不改变承诺时，保留空值并写入 `待补充项`；不能虚构字段、口径、事件名、接口可用性或实验阈值。
25. Keep unsupported capabilities under `不可虚构`; unsupported capabilities, unverified data, unresolved commitments, and future ideas must not appear as acceptance criteria.
26. 从用户输入中提取可复用交付资产：接口、数据来源、指标口径、埋点事件、实验标准和数据可用性判断；平台脚本可用时，用 `pmw-memory add-delivery-fact` 写入本地脱敏资产，并标明 `scenario`、`target`、`scope`、`source`、`confidence` 和 `fact-type`。
27. 平台脚本可用时，用 `pmw-log handoff <name>` 保存交付稿，它会登记 `handoff` 到 Product Artifact Flow；需要给 QA、发布或文档同步接力时，额外用 `pmw-artifact add --kind acceptance_seed` 或 `--kind release_doc_seed` 记录下游可读摘要。记录 `pmw-run event --type artifact`，并且只有交付前门槛全部通过时才 `pmw-run finish --status "可交付"`。

## 输出结构

```markdown
# PRD：<需求名>

## PRD 生成判断

- run_id：
- 交付目标：
- 事实来源：
- 现成文档参考：
- 产品准备度仪表盘：
- 交付前门槛：
- 原型复审状态：
- 未决拍板：
- 交付类型：
- PRD 缺口处理：
- 验收写入边界：
- 交付资产沉淀：
- 上游产物：
- 本轮产物：
- 下游可读：
- 产物流动：
- 下一技能：
- 证据状态：
- 已保存资产：

## 需求背景

## 需求价值

## 需求方案

## 需求功能及描述

| 功能模块 | 功能描述 | 规则 / 状态 | 异常 / 空态 | 待补充 |
|---|---|---|---|---|

## 接口以及数据来源

| 数据 / 接口 | 来源 | 字段 / 口径 | 状态 | 待补充 |
|---|---|---|---|---|

## 埋点信息

| 事件名 | 触发时机 | 属性 | 指标用途 | 状态 | 待补充 |
|---|---|---|---|---|

## 实验标准

| 实验假设 | 实验人群 | 主指标 | 反指标 | 判断标准 | 待补充 |
|---|---|---|---|---|

## 待补充项

## 不可虚构

## 已保存资产
```

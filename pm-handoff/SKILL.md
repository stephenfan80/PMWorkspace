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
```

## Workflow

1. 读取最新已对齐的产品简报、策略决策，以及可用的原型清单。
2. Read `../pmworkspace-shared/references/zoon-drift-check.md`.
3. 如果 `pmw-project show` 中有 Zoon URL，先运行 `pmw-zoon drift`；若存在漂移，读取最新文档，作为交付事实来源，并更新产品简报版本。
4. 选择交付类型：适合 PRD、适合设计、适合实验验证或适合研发。
5. 包含目标、目标用户、问题、场景、选定方向、范围、不做什么、验收标准、指标、风险、依赖和待决策项。
6. Keep unsupported capabilities under `不可虚构`.
7. 未决交付取舍继续使用 `decision-question-mode.md` 的选择题结构。
8. Log final delivery decisions when platform scripts are available.

## 输出结构

```markdown
# PMWorkspace 交付稿：<功能名>

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

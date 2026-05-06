---
name: pm-brief
description: |
  PMWorkspace 产品简报生成器。用于把产品对齐、产品追问输出、策略审查、
  PRD 笔记、Zoon 文档、截图或客户洞察，整理成可复用的快速版、标准版或
  深度版产品简报，包含版本、事实来源、假设、决策、约束和“已对齐”状态，
  作为 image-2 原型前的产品契约。
---

# 产品简报

创建后续原型、交付稿和实验步骤都必须读取的产品契约。

Before user-facing output, read `../pmworkspace-shared/references/language-and-localization.md`. For Chinese users, call the artifact `产品简报`; keep `brief` only when referring to a technical file or existing English source.

## Preamble

可用时运行平台检查和使用记录：

```bash
_PMW_BIN=""
for _CANDIDATE in "$PWD/bin" "$PWD/pmworkspace-shared/bin" "$HOME/.codex/skills/pmworkspace-shared/bin"; do
  if [ -x "$_CANDIDATE/pmw-log" ]; then _PMW_BIN="$_CANDIDATE"; break; fi
done
[ -n "$_PMW_BIN" ] && "$_PMW_BIN/pmw-update-check" 2>/dev/null || true
[ -n "$_PMW_BIN" ] && "$_PMW_BIN/pmw-log" usage pm-brief >/dev/null 2>&1 || true
```

## Workflow

1. Read `../pmworkspace-shared/references/product-plan-handoff.md`.
2. Read `../pmworkspace-shared/references/production-reference-gate.md`，并写入页面类型和线上参考状态。
3. Read `../pmworkspace-shared/references/decision-question-mode.md` and turn PM decision items into choice questions.
4. Read `../pmworkspace-shared/references/zoon-workflow.md`.
5. 根据模糊程度和风险选择快速版、标准版或深度版产品简报。
6. 包含事实来源、版本、确认状态、场景路由、页面类型、线上参考需求、线上参考状态、用户任务、目标、反指标、约束、不可虚构项和 PM 决策项。
7. 从功能名或产品简报标题提炼中文项目名，并用 `pmw-project set-name "<中文项目名>"` 保存。
8. Save the brief with `pmw-log brief <name>` when platform scripts are available.
9. If a Zoon URL is already available, append the brief with `pmw-zoon append --url <url>`; otherwise, when `zoon_auto_create` is true, create one with `pmw-zoon create --title "产品设计简报：<功能名>"`.

## Alignment Rule

只有“已对齐”的产品简报才能进入图片提示词。用户未确认时，标记为“待确认”，并在生成原型前停止。如果页面需要线上参考但状态是“缺失待补充”，确认状态不能写成“已对齐”。

## 输出

Return the smallest useful brief and end with:

```text
产品简报状态：
- 版本：
- 确认状态：
- 信息来源：
- 线上参考状态：
- 已保存资产：
- Zoon 在线简报：
- 项目名称：
- 待拍板选择题：
- 建议下一步：
```

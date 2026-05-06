---
name: pm-prototype-shotgun
description: |
  PMWorkspace 移动端优先的原型探索。用于用户需要 image-2 UI 原型图、多产品方向、
  截图修改、设计方案、移动应用原型、表单、结果页、看板、内部工具、交易流程、
  内容/社区屏幕或原型质量检查。要求产品简报已对齐，并且每个方案、每个屏幕
  单独输出一张图。
---

# 原型方案

只在产品对齐后生成原型方案。这里要把产品策略可视化，而不是只探索视觉皮肤。

Before user-facing output, read `../pmworkspace-shared/references/language-and-localization.md`. For Chinese users, use Chinese labels for schemes, screens, QA status, and next steps; keep `image-2` as the model/product term.

## Preamble

Run platform checks and log usage:

```bash
_PMW_BIN=""
for _CANDIDATE in "$PWD/bin" "$PWD/pmworkspace-shared/bin" "$HOME/.codex/skills/pmworkspace-shared/bin"; do
  if [ -x "$_CANDIDATE/pmw-log" ]; then _PMW_BIN="$_CANDIDATE"; break; fi
done
[ -n "$_PMW_BIN" ] && "$_PMW_BIN/pmw-update-check" 2>/dev/null || true
[ -n "$_PMW_BIN" ] && "$_PMW_BIN/pmw-log" usage pm-prototype-shotgun >/dev/null 2>&1 || true
```

## Hard Gates

- Read `../pmworkspace-shared/references/image-prompts.md`.
- 产品简报未“已对齐”时，不写提示词，也不生成图片。
- 现有功能迭代必须有当前截图或等价视觉基线。
- 多方案生成前先确认概念方向，除非用户明确批准使用默认方向。
- 默认移动端优先：iPhone 17 竖屏 `402 x 874`。
- 只有用户明确要求，或看板/内部工具密度确实需要时，才使用桌面端。

## Multi-Scheme Rules

- 方向必须在产品策略、信息架构、交互模型或信任模型上不同。
- 一个方案 + 一个屏幕 = 一张图片。
- `3 个方向 x 2 个屏幕` 表示六张独立图片。
- 除非用户要求演示材料，否则不要创建拼图或比较板。

## Workflow

1. Read aligned brief and scenario route.
2. If `pmw-project show` contains a Zoon URL, read the latest document with `pmw-zoon read --url <url>` and treat it as the product source of truth.
3. Read `design-system-workflow.md`, `design-heuristics.md`, and `adversarial-review.md` as needed.
4. Propose concept directions with names and tradeoffs.
5. For each image output unit, declare scheme, screen, canvas, and brief dependency.
6. Generate with image-2 / image generation.
7. Run `prototype-quality-review.md`.
8. 平台脚本可用时，用 `pmw-log prototype <batch>` 保存原型清单。
9. Record approved/rejected design feedback with `pmw-log taste`.

## 输出

```text
原型计划：
- 产品简报：
- Zoon 事实来源：
- 场景：
- 画布：
- 已生成 / 计划生成的图片：
- 质量检查：
- 已保存清单：
- 偏好反馈：
- 建议下一步：
```

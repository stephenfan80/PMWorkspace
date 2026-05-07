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
[ -n "$_PMW_BIN" ] && [ -x "$_PMW_BIN/pmw-dashboard" ] && "$_PMW_BIN/pmw-dashboard" status 2>/dev/null || true
```

## Hard Gates

- Read `../pmworkspace-shared/references/image-prompts.md`.
- Read `../pmworkspace-shared/references/product-plan-handoff.md` and require the latest product contract to be `已对齐`.
- Read `../pmworkspace-shared/references/production-reference-gate.md`.
- Read `../pmworkspace-shared/references/zoon-drift-check.md`.
- Read `../pmworkspace-shared/references/product-memory.md`.
- Read `../pmworkspace-shared/references/pm-decision-principles.md`.
- Read `../pmworkspace-shared/references/pm-eval-system.md`.
- Read `../pmworkspace-shared/references/runtime-kernel.md`.
- Read `../pmworkspace-shared/references/pm-workbench-map.md` and use its 原型方案 stage fields.
- Read `../pmworkspace-shared/references/evidence-dashboard.md`.
- Read `../pmworkspace-shared/references/prototype-shotgun-board.md`.
- Read `../pmworkspace-shared/references/design-system-workflow.md`.
- Read `../pmworkspace-shared/references/prototype-quality-review.md`.
- Follow `runtime-kernel.md` Run Owner 协议：如果 `pmw-project show` 已有 `current_run_id`，复用当前 run；如果用户直接调用 `$pm-prototype-shotgun` 且没有当前 run，再创建 runtime run.
- 产品简报未“已对齐”时，不写提示词，不生成图片，不生成 HTML，不输出交付稿。
- 现有功能迭代必须有当前截图或等价视觉基线。
- 新页面如果承接线上流程、结果页、状态页或生产样式，必须先拿到线上参考，或得到用户明确确认“没有线上参考，按新页面概念稿推进”。
- 多方案生成前先确认概念方向，除非用户明确批准使用默认方向。
- 设计原型默认只能使用 image-2 / 图像生成输出方案图片；HTML 只在用户明确要求“HTML”“可交互网页”“前端实现”或“本地网页原型”时允许。
- 如果当前环境无法生成 image-2 图片，停止并说明无法出图；不要用 HTML、Markdown 线框或拼图替代设计原型。
- 默认移动端优先：iPhone 17 竖屏 `402 x 874`。
- 只有用户明确要求，或看板/内部工具密度确实需要时，才使用桌面端。

## Multi-Scheme Rules

- 方向必须先在产品策略、信息架构、交互模型或信任模型上不同，再讨论视觉差异。
- 不要把配色、插画、圆角、风格皮肤包装成多方案。
- 一个方案 + 一个屏幕 = 一张图片。
- `3 个方向 x 2 个屏幕` 表示六张独立图片。
- 除非用户要求演示材料，否则不要创建拼图或比较板。

## Workflow

1. 建立原型方案控制器，记录 `产品简报来源`、`图片生成前门槛`、`方案差异质量`、`方案方向确认`、`输出单元清单`、`方案比较板写入`、`生成后复审` 和 `证据状态`。
2. Read aligned brief and scenario route. If the brief is missing, `待确认`, `草稿`, or has unresolved `缺失门槛`, route back to `$pm-brief` and stop before writing image-2 prompts.
3. If `pmw-project show` contains a Zoon URL, run `pmw-zoon drift --url <url>` when available, then read the latest document with `pmw-zoon read --url <url>` and treat it as the product source of truth. If drift changes goal, anti-metric, non-fiction boundary, scope, user promise, or scheme direction, route back to `$pm-brief` / `$pm-strategy-review` and stop.
4. 对每个请求的屏幕运行线上参考门槛；如果必要参考是 `缺失待补充`，先停下来问，不写图片提示词。
5. Read `design-heuristics.md`, `scenario-experts.md`, and `adversarial-review.md` as needed, but do not change scope or promise without writing the decision back to the product brief.
6. Use `pmw-memory taste-summary` when available so rejected directions are not repeated as “new”方案; if memory changes the recommendation, explicitly say `基于过往偏好，我建议...`, and never let preference override the current brief, anti-metric, non-fiction boundary, or reference gate.
7. Propose concept directions with names and tradeoffs. 方案差异必须通过 `方案差异质量`：至少说明每个方向在产品策略、信息架构、交互模型或信任模型上的不同；如果只是视觉皮肤差异，停止并重拟方向。
8. 多方案生成前确认方案方向；如果用户已经明确批准默认方向，记录 `方案方向确认：默认方向已批准`，否则停在方向确认，不写 image-2 提示词。
9. For each image output unit, declare scheme, screen task, canvas, main goal, anti-metric, non-fiction boundary, 线上参考状态, and brief dependency. 一个输出单元等于一张图片，不能把多个方案或多个屏幕合成拼图。
10. 平台脚本可用时，先用 `pmw-prototype-board add` 登记每个方案/屏幕单元；如果写入失败，输出 `方案比较板：未写入（原因）`，不能假装已记录。
11. 在所有图片生成前门槛通过后，Generate with image-2 / image generation. 如果当前环境无法生成 image-2，停止并说明，不用 HTML、Markdown 线框或方案比较板替代。
12. 出图后用 `pmw-prototype-board image` 补充图片路径或 URL；用户反馈后用 `pmw-prototype-board score` 记录评分。
13. Run `prototype-quality-review.md`, then route substantial post-image review to `$pm-prototype-review`.
14. 平台脚本可用时，用 `pmw-log prototype <batch>` 保存原型清单，并用 `pmw-run event --type artifact` 记录产物。
15. Record approved/rejected design feedback with `pmw-log taste`, including scenario, feedback target, source, scope, and confidence when available.
16. 批量输出后运行 `pmw-dashboard status`，在最终说明中给出方案比较板状态。

## 输出

```text
原型计划：
- 产品简报：
- run_id：
- Zoon 事实来源：
- Zoon 漂移检查：
- 图片生成前门槛：
- 场景：
- 线上参考：
- 设计系统：
- 方案差异质量：
- 方案方向确认：
- 画布：
- 输出单元清单：
- 每张图绑定：方案名 / 屏幕任务 / 主目标 / 反指标 / 不可虚构项 / 产品简报版本
- image-2 状态：
- 已生成 / 计划生成的图片：
- 质量检查：
- 已保存清单：
- 方案比较板：
- 证据状态：
- 偏好反馈：
- 原型复审：
- 建议下一步：
```

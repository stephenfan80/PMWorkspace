---
name: pm-prototype-shotgun
description: |
  PMWorkspace 移动端优先的原型探索。用于用户需要 image-2 UI 原型图、多产品方向、
  截图修改、设计方案、移动应用原型、表单、结果页、看板、内部工具、交易流程、
  内容/社区屏幕或原型质量检查。要求产品简报已对齐，并且每个方案、每个屏幕
  单独输出一张图。
---

# 原型方案

`$pm-prototype-shotgun` 是 image-2 原型出图导演。它不重新做 `$pm-jobs` 的价值澄清、不替 `$pm-strategy-review` 拍策略取舍、也不替 `$pm-brief` 补写产品契约；它只把已对齐产品简报里的产品判断拆成可生成、可比较、可复审的单张设计稿。

核心规则：

```text
一次 image-2 调用 = 一张图 = 一个方案 + 一个屏幕任务
```

批量生成只是自动连续执行多个单图任务。`3 个方案` 表示连续执行 3 次 image-2；`3 个方案 x 2 个屏幕` 表示连续执行 6 次 image-2。每次调用都必须独立提示、独立产物、独立记录状态，不允许拼图、三联图、并排比较、一图多方案或多屏故事板。

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
- 原型出图前必须先输出 `原型出图判断`，说明我建议出哪些图、暂时不出哪些图、为什么，以及图片生成前门槛；不能直接写 image-2 prompt。
- 产品简报未“已对齐”时，不写提示词，不生成图片，不生成 HTML，不输出交付稿。
- 现有功能迭代必须有当前截图或等价视觉基线。
- 新页面如果承接线上流程、结果页、状态页或生产样式，必须先拿到线上参考，或得到用户明确确认“没有线上参考，按新页面概念稿推进”。
- 多方案生成前先确认概念方向，除非用户明确批准使用默认方向。
- 设计原型默认只能使用 image-2 / 图像生成输出方案图片；HTML 只在用户明确要求“HTML”“可交互网页”“前端实现”或“本地网页原型”时允许。
- 如果当前环境无法生成 image-2 图片，停止并说明无法出图；不要用 HTML、Markdown 线框或拼图替代设计原型。
- 默认移动端优先：iPhone 17 竖屏 `402 x 874`。
- 只有用户明确要求，或看板/内部工具密度确实需要时，才使用桌面端。

## Multi-Scheme Rules

- 方向必须先在页面结构、信息架构、交互路径、信任表达或关键任务上不同，再讨论视觉差异。
- 不要把配色、插画、圆角、卡片样式或风格皮肤包装成多方案。
- 规则不局限留资业务；社区、直播、产品库、交易、内容、工具、看板等场景也必须用同一套方案质量标准。
- 一个方案 + 一个屏幕 = 一张图片。
- 一次 image-2 调用只能生成一张独立图片。
- `3 个方向 x 2 个屏幕` 表示六张独立图片。
- 除非用户要求演示材料，否则不要创建拼图、三联图、并排比较图或多屏故事板。
- 每次 prompt 都必须明确禁止拼图、并排比较、一图多屏和一图多方案。
- 每张图独立记录状态：`计划生成`、`已生成`、`生成失败`、`待重试` 或 `需要重出`；批量成功不能掩盖单张失败。

## Workflow

1. 建立原型方案控制器，记录 `产品简报来源`、`图片生成前门槛`、`方案差异质量`、`方案方向确认`、`输出单元清单`、`方案比较板写入`、`生成后复审` 和 `证据状态`。
2. Read aligned brief and scenario route. If the brief is missing, `待确认`, `草稿`, or has unresolved `缺失门槛`, route back to `$pm-brief` and stop before writing image-2 prompts.
3. If `pmw-project show` contains a Zoon URL, run `pmw-zoon drift --url <url>` when available, then read the latest document with `pmw-zoon read --url <url>` and treat it as the product source of truth. If drift changes goal, anti-metric, non-fiction boundary, scope, user promise, or scheme direction, route back to `$pm-brief` / `$pm-strategy-review` and stop.
4. 对每个请求的屏幕运行线上参考门槛；如果必要参考是 `缺失待补充`，先停下来问，不写图片提示词。
5. Read `design-heuristics.md`, `scenario-experts.md`, and `adversarial-review.md` as needed, but do not change scope or promise without writing the decision back to the product brief.
6. Use `pmw-memory taste-summary` when available so rejected directions are not repeated as “new”方案; if memory changes the recommendation, explicitly say `基于过往偏好，我建议...`, and never let preference override the current brief, anti-metric, non-fiction boundary, or reference gate.
7. 输出 `原型出图判断`：先说明我建议这轮出哪些单图、暂时不出哪些屏、为什么这些图能帮助 PM 做产品选择，以及图片生成前门槛。
8. Propose concept directions with names and tradeoffs. 方案差异必须通过 `方案差异质量`：至少说明每个方向在页面结构、信息架构、交互路径、信任表达或关键任务上的不同；如果只是视觉皮肤差异，停止并重拟方向。
9. 如果用户、brief、Zoon、截图或参考材料命中汽车之家、AutoDesign、之家或 Autohome，默认载入 AutoDesign 约束。产品 UI 优先使用 AutoDesign token；品牌 VI 和字体包只作为品牌露出、活动视觉或特殊场景参考，字体授权必须保留边界，不能写成生产可用承诺。
10. 多方案生成前确认方案方向；如果用户已经明确批准默认方向，记录 `方案方向确认：默认方向已批准`，否则停在方向确认，不写 image-2 提示词。
11. For each image output unit, declare scheme, screen task, canvas, main goal, anti-metric, non-fiction boundary, 线上参考状态, design system, image-2 status, and brief dependency. 一个输出单元等于一张图片，不能把多个方案或多个屏幕合成拼图。
12. 把批量请求拆成顺序单图队列：`3 个方案` -> 3 个输出单元，`3 个方案 x 2 个屏幕` -> 6 个输出单元。每个输出单元单独调用一次 image-2；不要把多个单元合成一个 prompt。
13. 平台脚本可用时，先用 `pmw-prototype-board add` 登记每个方案/屏幕单元；如果写入失败，输出 `方案比较板：未写入（原因）`，不能假装已记录。
14. 在每个输出单元的图片生成前门槛通过后，逐个 Generate with image-2 / image generation。每次生成只服务当前一个输出单元，并在 prompt 中写明禁止拼图、并排比较、一图多屏、一图多方案。 如果当前环境无法生成 image-2，停止并说明，不用 HTML、Markdown 线框或方案比较板替代。
15. 每张图出图后用 `pmw-prototype-board image` 补充图片路径或 URL；单张失败时记录 `生成失败` 或 `待重试`，不能把批次写成全成功。用户反馈后用 `pmw-prototype-board score` 记录评分。
16. Run `prototype-quality-review.md`, then route substantial post-image review to `$pm-prototype-review`.
17. 平台脚本可用时，用 `pmw-log prototype <batch>` 保存原型清单，并用 `pmw-run event --type artifact` 记录产物。
18. Record approved/rejected design feedback with `pmw-log taste`, including scenario, feedback target, source, scope, and confidence when available.
19. 批量输出后运行 `pmw-dashboard status`，在最终说明中给出每张图的单独状态和方案比较板状态。

## 输出

```text
原型出图判断：
- 我建议：
- 这轮先出：
- 暂时不出：
- 为什么：
- 图片生成前门槛：

方案方向：
- 方案 A：
  - 产品判断：
  - 页面结构：
  - 适合场景：
  - 最大风险：

图片输出单元：
- 方案名：
- 屏幕任务：
- 画布：
- 主目标：
- 反指标：
- 不可虚构项：
- 产品简报版本：
- 线上参考状态：
- 设计系统：
- image-2 状态：

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
- 每张图绑定：方案名 / 屏幕任务 / 主目标 / 反指标 / 不可虚构项 / 产品简报版本 / 设计系统 / 线上参考状态 / image-2 状态
- 单图生成协议：一次 image-2 调用 = 一张图 = 一个方案 + 一个屏幕任务
- image-2 状态：
- 已生成 / 计划生成的图片：
- 质量检查：
- 已保存清单：
- 方案比较板：
- 证据状态：
- 偏好反馈：
- 原型复审：
- 生成后复审：
  - 是否符合 brief：
  - 是否符合设计系统：
  - 是否违反反指标：
  - 是否需要重出：
- 建议下一步：
```

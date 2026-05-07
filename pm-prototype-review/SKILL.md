---
name: pm-prototype-review
description: |
  PMWorkspace 原型复审。用于 image-2 原型图生成后，按已对齐产品简报、Zoon 最新
  内容、线上参考、设计系统、主目标、反指标和不可虚构项做质量复审；发现实质问题时，
  输出需要重出的屏幕和修正后的图片提示词方向。也用于批量原型交付前的验收。
---

# 原型复审

原型复审的目标不是评价“好不好看”，而是判断图片是否忠实表达已对齐的产品判断，是否值得进入评审、交付或下一轮 image-2。

Before user-facing output, read `../pmworkspace-shared/references/language-and-localization.md`. 面向中文用户时使用中文字段和状态。

## Preamble

运行平台检查和偏好摘要：

```bash
_PMW_BIN=""
for _CANDIDATE in "$PWD/bin" "$PWD/pmworkspace-shared/bin" "$HOME/.codex/skills/pmworkspace-shared/bin"; do
  if [ -x "$_CANDIDATE/pmw-log" ]; then _PMW_BIN="$_CANDIDATE"; break; fi
done
[ -n "$_PMW_BIN" ] && "$_PMW_BIN/pmw-update-check" 2>/dev/null || true
[ -n "$_PMW_BIN" ] && "$_PMW_BIN/pmw-log" usage pm-prototype-review >/dev/null 2>&1 || true
[ -n "$_PMW_BIN" ] && [ -x "$_PMW_BIN/pmw-memory" ] && "$_PMW_BIN/pmw-memory" taste-summary 2>/dev/null || true
[ -n "$_PMW_BIN" ] && [ -x "$_PMW_BIN/pmw-dashboard" ] && "$_PMW_BIN/pmw-dashboard" status 2>/dev/null || true
```

## Workflow

1. Read `../pmworkspace-shared/references/prototype-quality-review.md`.
2. Read `../pmworkspace-shared/references/image-prompts.md`.
3. Read `../pmworkspace-shared/references/design-system-workflow.md`.
4. Read `../pmworkspace-shared/references/zoon-drift-check.md`.
5. Read `../pmworkspace-shared/references/pm-review-army.md`.
6. Read `../pmworkspace-shared/references/prototype-shotgun-board.md`.
7. Read `../pmworkspace-shared/references/evidence-dashboard.md`.
8. Read `../pmworkspace-shared/references/pm-workbench-map.md` and use its 原型复审 stage fields.
9. Read `../pmworkspace-shared/references/runtime-kernel.md`; follow its Run Owner 协议：如果 `pmw-project show` 已有 `current_run_id`，复用当前 run；如果用户直接调用 `$pm-prototype-review` 且没有当前 run，再创建 runtime run.
10. Read `../pmworkspace-shared/references/pm-decision-principles.md`; unresolved user promise, data truth, scope, experiment, lead, transaction, privacy, or compliance issues must become `需要 PM 拍板`, not visual fixes.
11. Read `../pmworkspace-shared/references/pm-eval-system.md` and preserve prototype review contracts.
12. 建立原型复审控制器，记录 `复审输入`、`输出单元绑定`、`复审视角`、`判定原因`、`行动结论`、`修正方向`、`PM 拍板`、`偏好沉淀` 和 `证据状态`。
13. If `pmw-project show` contains a Zoon URL, run `pmw-zoon drift` when available. If drift exists, read the latest Zoon snapshot before judging the image. If drift changes product facts, route back to `$pm-brief` or `$pm-strategy-review` before accepting the image.
14. For every image, check the bound output unit: 方案名、屏幕任务、主目标、反指标、不可虚构项、产品简报版本. If an image is not bound to one output unit or prototype-board item, mark `需要补充参考` and do not pass it by visual impression.
15. Score each screen on five dimensions: 产品一致性、任务完成、信任与反指标、设计系统、可交付性. Scores are diagnostic only; any hard violation overrides the average.
16. Use PM Review Army lenses for strategy, trust/risk, design system, and data feasibility; merge into `可通过`、`需要重出`、`需要 PM 拍板`, or `需要补充参考`.
17. If a screen violates the product brief, anti-metric, non-fiction boundary, online reference, or design system, mark `需要重出` and produce a concise repair brief for `$pm-prototype-shotgun`; do not accept a pretty but misleading image.
18. If the issue is unresolved user promise, data truth, scope, experiment, lead, transaction, privacy, or compliance boundary, mark `需要 PM 拍板`, output one current D, and do not create repair prompts until the D is resolved.
19. Log approved/rejected preferences with `pmw-log taste` only for user feedback or review-confirmed preferences; include scenario, feedback target, source, scope, and confidence. Do not save fact violations, anti-metric risks, non-fiction failures, missing references, or unresolved promises as taste.
20. Log scheme scores with `pmw-prototype-board score --screen <屏幕任务>` when applicable.
21. If repeated preferences emerge, save a learning with `pmw-memory add-learning`, but keep it脱敏 and scoped.
22. 复审结束时用 `pmw-run event --type review` 记录结论，并运行 `pmw-dashboard status`。

## 复审标准

- `已通过`：没有实质偏离，只有轻微文字或审美调整。
- `需要重出`：违反产品简报、反指标、不可虚构项、线上参考或设计系统。
- `需要 PM 拍板`：问题来自产品取舍未决，不应靠改图解决。
- `需要补充参考`：图的问题来自缺少线上截图、设计系统或真实数据边界。
- `可通过` 只能用于不影响产品判断或交付使用的问题；轻微审美偏好可以记录 taste，但不能覆盖当前 brief、Zoon、反指标或不可虚构项。

## 输出

```text
原型复审结果：
- 产品简报 / Zoon 来源：
- run_id：
- Zoon 漂移检查：
- 复审输入：
- 输出单元绑定：
- 证据状态：
- PM Review Army：
- 已检查图片：
- 五维评分：
- 逐屏结论：
- 需要重出的屏幕：
- 修正方向：
- 需要 PM 拍板：
- 当前 D：
- 偏好记忆更新：
- 方案比较板评分：
- 建议下一步：
```

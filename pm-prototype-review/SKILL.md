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
8. If `pmw-project show` contains a Zoon URL, run `pmw-zoon drift` when available. If drift exists, read the latest Zoon snapshot before judging the image.
9. For every image, check the bound output unit: 方案名、屏幕任务、主目标、反指标、不可虚构项、产品简报版本。
10. Score each screen on five dimensions: 产品一致性、任务完成、信任与反指标、设计系统、可交付性.
11. Use PM Review Army lenses for strategy, trust/risk, design system, and data feasibility; merge into `可通过`、`需要重出`、or `需要 PM 拍板`.
12. If a screen has material failure, mark `需要重出` and produce a concise repair brief for `$pm-prototype-shotgun`; do not accept a pretty but misleading image.
13. Log approved/rejected preferences with `pmw-log taste` when the user gives feedback; log scheme scores with `pmw-prototype-board score` when applicable.
14. If repeated preferences emerge, save a learning with `pmw-memory add-learning`.
15. 复审结束时用 `pmw-run event --type review` 记录结论，并运行 `pmw-dashboard status`。

## 复审标准

- `已通过`：没有实质偏离，只有轻微文字或审美调整。
- `需要重出`：违反产品简报、反指标、不可虚构项、线上参考或设计系统。
- `需要 PM 拍板`：问题来自产品取舍未决，不应靠改图解决。
- `需要补充参考`：图的问题来自缺少线上截图、设计系统或真实数据边界。

## 输出

```text
原型复审结果：
- 产品简报 / Zoon 来源：
- run_id：
- Zoon 漂移检查：
- PM Review Army：
- 已检查图片：
- 逐屏结论：
- 需要重出的屏幕：
- 修正方向：
- 偏好记忆更新：
- 建议下一步：
```

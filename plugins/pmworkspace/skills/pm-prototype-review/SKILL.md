---
name: pm-prototype-review
description: |
  PMWorkspace 原型复审。用于 image-2 原型图生成后，按已对齐产品简报、Zoon 最新
  内容、线上参考、设计系统、主目标、反指标和不可虚构项做质量复审；先用策略、
  信任 / 风险、设计系统、数据可行性四个可插拔专家各自产出短结论，再由原型复审
  合并；高风险时追加 Product Review Squad 的 CEO、Eng、Design、DX、安全、QA、
  发布工程师角色短结论。发现实质问题时，输出需要重出的屏幕、PM 拍板项或修正后的
  图片提示词方向。也用于批量原型交付前的验收。
---

# 原型复审

原型复审的目标不是评价“好不好看”，而是判断图片是否忠实表达已对齐的产品判断和对应产品路径，是否值得进入评审、交付或下一轮 image-2。复审必须先做原型可信度对抗复审：检查图片是否把未经验证的产品判断视觉化，是否放大理解偏差，是否让用户误以为产品已经具备未确认能力。

<!-- PMW-GENERATED-CONTRACT:START -->
## PMWorkspace 生成契约

> 本区块由 `bin/pmw-gen-skill-docs` 根据 `pmworkspace-shared/skill-docs/skill-docs.manifest.json` 生成；不要手写修改。更新共享门槛、前置检查或输出字段后，运行 `bin/pmw-gen-skill-docs write`，再运行 `bin/pmw-gen-skill-docs check`。

- skill：`pm-prototype-review`
- 契约版本：`2`
- 阶段：原型复审
- 定位：围绕产品路径、brief、反指标和不可虚构项，用四个可插拔专家和必要的 Product Review Squad 合并判断原型是否可通过、重出或拍板。

### 统一前置检查

- `_PMW_BIN`
- `pmw-update-check`
- `pmw-controller`
- `usage`
- `usage pm-prototype-review`
- `pmw-dashboard`
- `pmw-artifact`
- `pmw-review-specialist`

### 必读共享协议

- `../pmworkspace-shared/references/prototype-quality-review.md`
- `../pmworkspace-shared/references/pm-review-army.md`
- `../pmworkspace-shared/references/pm-workbench-map.md`
- `../pmworkspace-shared/references/artifact-flow.md`
- `../pmworkspace-shared/references/runtime-kernel.md`
- `../pmworkspace-shared/references/pm-decision-principles.md`
- `../pmworkspace-shared/references/pm-eval-system.md`

### 共享门槛

- 真源：`pmworkspace-shared/skill-docs/skill-docs.manifest.json` 的 `shared_gates`。
- 快速更新：每个 skill 运行前用 `pmw-update-check --quick`；如果输出 `UPGRADE_AVAILABLE`，先询问用户是否执行 `UPGRADE_COMMAND`，除非 `auto_upgrade` 为 `true`。
- 运行时入口：每个 PMW 产品任务先过 `pmw-controller intake`，由 controller 判定是否继承或新建 run，并写入 `task_digest` / `input_revision`。
- STOP gate：`pmw-controller next` 返回 `ASK_CONFIRMATION`、`NEEDS_BASELINE`、`BRIEF_PENDING`、`D_REQUIRED` 或 `BLOCKED` 时必须停住，不能进入下游产物。
- 当前任务绑定：brief、visual baseline、prototype-board、review、handoff 和用户确认必须匹配当前 run、`task_digest` 与 `input_revision`；旧产物只能参考，不能放行。
- 摘要：中文本地化、记忆不覆盖本轮事实、出图前必须通过 prototype preflight、禁止泄露 token/ownerSecret/私密资料。

### 默认用户可见输出字段

- `复审结论`
- `产品信息对齐状态`
- `逐屏结论`
- `设计完整度复审`
- `原型可信度对抗复审`
- `需要重出的屏幕`
- `需要 PM 拍板`
- `下一步`

### 内部审计字段（默认不展示）

- `复审输入`
- `产品信息对齐包`
- `输出单元绑定`
- `产品路径`
- `设计完整度复审`
- `原型可信度对抗复审`
- `PM Review Army`
- `可插拔专家`
- `专家合并结论`
- `反馈资产化`
- `证据状态`
<!-- PMW-GENERATED-CONTRACT:END -->

Before user-facing output, read `../pmworkspace-shared/references/language-and-localization.md`. 面向中文用户时使用中文字段和状态。

## Preamble

运行平台检查和偏好摘要：

```bash
_PMW_BIN=""
for _CANDIDATE in "$PWD/bin" "$PWD/pmworkspace-shared/bin" "$HOME/.codex/skills/pmworkspace-shared/bin" "$HOME/.agents/plugins/plugins/pmworkspace/skills/pmworkspace-shared/bin" $(find "$HOME/.codex/plugins/cache" -path "*/pmworkspace/*/skills/pmworkspace-shared/bin" -type d 2>/dev/null | sort -r); do
  if [ -x "$_CANDIDATE/pmw-log" ]; then _PMW_BIN="$_CANDIDATE"; break; fi
done
if [ -n "$_PMW_BIN" ]; then
  _UPD=$("$_PMW_BIN/pmw-update-check" --quick 2>/dev/null || true)
  [ -n "$_UPD" ] && echo "$_UPD"
fi
[ -n "$_PMW_BIN" ] && "$_PMW_BIN/pmw-log" usage pm-prototype-review >/dev/null 2>&1 || true
[ -n "$_PMW_BIN" ] && [ -x "$_PMW_BIN/pmw-dashboard" ] && "$_PMW_BIN/pmw-dashboard" status 2>/dev/null || true
[ -n "$_PMW_BIN" ] && [ -x "$_PMW_BIN/pmw-memory" ] && "$_PMW_BIN/pmw-memory" user-summary 2>/dev/null || true
[ -n "$_PMW_BIN" ] && [ -x "$_PMW_BIN/pmw-memory" ] && "$_PMW_BIN/pmw-memory" taste-summary 2>/dev/null || true
[ -n "$_PMW_BIN" ] && [ -x "$_PMW_BIN/pmw-dashboard" ] && "$_PMW_BIN/pmw-dashboard" status 2>/dev/null || true
[ -n "$_PMW_BIN" ] && [ -x "$_PMW_BIN/pmw-artifact" ] && "$_PMW_BIN/pmw-artifact" latest --kind prototype_manifest 2>/dev/null || true
[ -n "$_PMW_BIN" ] && [ -x "$_PMW_BIN/pmw-artifact" ] && "$_PMW_BIN/pmw-artifact" latest --kind visual_baseline 2>/dev/null || true
[ -n "$_PMW_BIN" ] && [ -x "$_PMW_BIN/pmw-review-specialist" ] && "$_PMW_BIN/pmw-review-specialist" summary 2>/dev/null || true
```

## Workflow

1. Read `../pmworkspace-shared/references/prototype-quality-review.md`.
2. Read `../pmworkspace-shared/references/image-prompts.md`.
3. Read `../pmworkspace-shared/references/design-system-workflow.md`.
4. Read `../pmworkspace-shared/references/zoon-drift-check.md`.
5. Read `../pmworkspace-shared/references/pm-review-army.md`.
6. Read `../pmworkspace-shared/references/prototype-shotgun-board.md`.
7. Read `../pmworkspace-shared/references/evidence-dashboard.md`.
8. Read `../pmworkspace-shared/references/product-memory.md` and use `pmw-memory user-summary` when available. If memory changes the recommendation, explicitly say `基于过往偏好...` or `基于本地产品认知...`; memory cannot override the current brief, Zoon, anti-metric, non-fiction boundary, or reference gate.
9. Read `../pmworkspace-shared/references/pm-workbench-map.md` and use its 原型复审 stage fields.
10. Read `../pmworkspace-shared/references/artifact-flow.md` and read the latest `prototype_manifest` artifact before judging generated images.
11. Read `../pmworkspace-shared/references/runtime-kernel.md`; follow its Run Owner 协议：如果 `pmw-project show` 已有 `current_run_id`，复用当前 run；如果用户直接调用 `$pm-prototype-review` 且没有当前 run，再创建 runtime run.
12. Read `../pmworkspace-shared/references/pm-decision-principles.md`; unresolved user promise, data truth, scope, experiment, lead, transaction, privacy, or compliance issues must become `需要 PM 拍板`, not visual fixes.
13. Read `../pmworkspace-shared/references/pm-eval-system.md` and preserve prototype review contracts.
14. 先读取统一 `产品信息对齐包`，再建立原型复审控制器，记录 `复审输入`、`输出单元绑定`、`产品信息对齐状态`、`设计完整度复审`、`原型可信度对抗复审`、`可插拔专家`、`专家合并结论`、`Product Review Squad`、`角色短结论`、`判定原因`、`行动结论`、`修正方向`、`PM 拍板`、`偏好沉淀`、`反馈资产化`、`上游产物`、`本轮产物`、`下游可读`、`产物流动` 和 `证据状态`；这些默认写入审计，用户可见输出只保留复审结论、逐屏结论、需要调整和下一步。
15. If `pmw-project show` contains a Zoon URL, run `pmw-zoon drift` when available. If drift exists, read the latest Zoon snapshot before judging the image. If drift changes product facts, route back to `$pm-brief` or `$pm-strategy-review` before accepting the image.
16. For every image, check the bound output unit: 方案名、屏幕任务、产品路径、用户行为假设、要赢过的现状替代、当前损失、删除 / 牺牲 / 后置项、验证信号、失败信号、主目标、反指标、不可虚构项、产品简报版本、线上参考状态、视觉基线状态、目标输出像素、设计完整度评分、10/10 原型标准、prompt 设计修正、状态覆盖、第一眼 / 第二眼 / 第三眼、反 AI 模板味约束、设计规范目标、设计系统 / 平台模式、灵感来源摘要和禁止照搬项. If an image is not bound to one output unit or prototype-board item, mark `需要补充参考` and do not pass it by visual impression.
17. If a reference screenshot and generated image path exist, run `pmw-image-audit audit --image <生成图> --reference <参考图>` before expert review. If it returns `需要重出`, the merged conclusion is at least `需要重出`; do not override a failed width / long-board audit with subjective visual approval.
18. Score each screen on seven dimensions: 产品路径一致性、产品一致性、任务完成、信任与反指标、设计系统、设计完整度、可交付性. Scores are diagnostic only; any hard violation overrides the average. `设计完整度` 必须对照 prototype-board 中的 10/10 原型标准，检查信息层级、状态覆盖、移动端可用性和反 AI 模板味是否达标。
19. 对每张图执行 `原型可信度对抗复审`：检查真实问题一致性、假设视觉化风险、反指标冲突、不可虚构违规、理解偏差风险和用户能力误解。发现假设被画成事实，至少标为 `需要 PM 拍板`；发现明确承诺无法兑现的能力、不可虚构项被画入、反指标冲突或偏离真实问题，不能 `可通过`。
20. Run PM Review Army as pluggable specialists first: `strategy`、`trust-risk`、`design-system`、`data-feasibility` must each output an independent short conclusion with status, severity, evidence, one-sentence judgment, and action. When platform scripts are available, record each with `pmw-review-specialist add`, then run `pmw-review-specialist summary`; `$pm-prototype-review` merges the four specialist outputs into `可通过`、`需要重出`、`需要 PM 拍板`, or `需要补充参考`.
21. For deep delivery, high-risk, batch handoff, engineering handoff, production flow, or explicit multi-role review requests, also run Product Review Squad roles: CEO, Eng, Design, DX, 安全, QA, 发布工程师. Each role must output a short conclusion with status, severity, evidence, one-sentence judgment, and action; merge role outputs after the pluggable specialist merge.
22. If a screen violates the product path, product brief, anti-metric, non-fiction boundary, online reference, visual baseline, target output pixels, design system, 10/10 原型标准, 原型可信度对抗复审, or anti-AI-slop constraints, mark `需要重出` and produce a concise repair brief for `$pm-prototype-shotgun`; do not accept a pretty but misleading image. 明显泛 SaaS 卡片堆叠、紫蓝渐变、装饰性图标圆圈、无意义 hero、拼贴感界面、占位式空态或不可读状态，也不能因为“看起来好看”而通过。
23. If the issue is unresolved user promise, data truth, scope, experiment, lead, transaction, privacy, or compliance boundary, mark `需要 PM 拍板`, output one current D, and do not create repair prompts until the D is resolved.
24. Log approved/rejected preferences with `pmw-log taste` only for user feedback or review-confirmed preferences; include scenario, feedback target, source, scope, and confidence. Do not save fact violations, anti-metric risks, non-fiction failures, missing references, or unresolved promises as taste. Failed image audits also cannot be saved as taste.
25. 将复审和用户反馈做 `反馈资产化`：分类为 `个人偏好`、`产品认知`、`PMWorkspace 进化建议` 或 `不应保存`。个人偏好用 `pmw-memory add-feedback --type preference`，产品认知用 `pmw-memory add-feedback --type product-cognition`，进化建议用 `pmw-memory add-feedback --type pmworkspace-improvement`；需要回流 GitHub 时只生成本地脱敏待审稿 `pmw-memory draft-github-feedback`，不自动提交。
26. Log scheme scores with `pmw-prototype-board score --screen <屏幕任务>` when applicable.
27. If repeated preferences emerge, save a learning with `pmw-memory add-learning`, but keep it脱敏 and scoped.
28. 复审结束时用 `pmw-run event --type review` 记录结论；如果输出修复 brief 或可交付复审结论，使用 `pmw-artifact add --kind prototype_review` 或 `--kind repair_brief` 登记到 Product Artifact Flow，并运行 `pmw-dashboard status` 获取短摘要；完整状态只在审计 / 调试时展开。
29. 复审结束必须给出明确下一步引导。`可通过` 时引导用户选择：选定方案进入 `$pm-handoff` 生成产品设计文档、继续改某一张图、继续探索新方案、补充截图/数据参考；`需要重出` 时只让用户确认修复方向或直接重出受影响单图；`需要 PM 拍板` 时只展开一个当前 `D`。

## 复审标准

- `已通过`：没有实质偏离，只有轻微文字或审美调整。
- `需要重出`：违反产品简报、反指标、不可虚构项、线上参考或设计系统。
- `需要 PM 拍板`：问题来自产品取舍未决，不应靠改图解决。
- `需要补充参考`：图的问题来自缺少线上截图、设计系统、设计规范目标或真实数据边界。
- `可通过` 只能用于不影响产品判断或交付使用的问题；轻微审美偏好可以记录 taste，但不能覆盖当前 brief、Zoon、反指标或不可虚构项。

## 输出

```text
原型复审结果：
- 复审结论：
- 逐屏结论：
- 设计完整度复审：
  - 评分：
  - 是否达到 10/10 原型标准：
  - 是否出现 AI 模板味：
  - 信息层级是否符合第一眼 / 第二眼 / 第三眼：
  - 状态覆盖是否缺失：
  - 重出 prompt 修正方向：
- 原型可信度对抗复审：
  - 真实问题一致性：
  - 假设视觉化风险：
  - 反指标冲突：
  - 不可虚构违规：
  - 理解偏差风险：
  - 用户能力误解：
  - 处理动作：
- 需要重出的屏幕：
- 需要 PM 拍板：
- 当前 D：
- 下一步：
  - 我建议：
  - 你可以直接回复：选定方案生成产品设计文档 / 修改某区域 / 继续探索 / 补充参考 / 进入交付稿

内部复审审计（默认不展示）：
- 产品简报 / Zoon 来源：
- run_id：
- Zoon 漂移检查：
- 复审输入：
- 输出单元绑定：
  - 产品路径：
  - 用户行为假设：
  - 当前损失：
  - 牺牲项 / 后置项：
- 设计完整度复审：
  - 原始设计评分：
  - 10/10 原型标准：
  - 生成图评分：
  - 反 AI 模板味检查：
  - 状态覆盖：
  - 第一眼 / 第二眼 / 第三眼：
- 原型可信度对抗复审：
  - 真实问题一致性：
  - 假设视觉化风险：
  - 反指标冲突：
  - 不可虚构违规：
  - 理解偏差风险：
  - 用户能力误解：
  - 处理动作：
- 视觉审计：
  - visual_baseline：
  - 参考图 / 目标输出像素：
  - pmw-image-audit 结果：
- PM Review Army：
  - 可插拔专家：
  - 专家合并结论：
  - Product Review Squad：
  - 角色短结论：
- 偏好记忆更新：
- 反馈资产化：
  - 可沉淀为个人偏好：
  - 可沉淀为产品认知：
  - 可回流 PMWorkspace：
  - 不应保存：
  - 已保存到：
- 上游产物：
- 本轮产物：
- 下游可读：
- 产物流动：
- 证据状态：
- 方案比较板评分：
```

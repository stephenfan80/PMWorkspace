---
name: pm-autoplan
description: |
  PMWorkspace 自动产品评审流水线。用于用户希望“一次跑完整产品评审”“自动把
  产品方向梳理到可出原型前”“按推荐推进但关键点让我拍板”，或希望产出
  “产品简述 + 至少 3 个方案方向 + 原型图”时。所有任务统一进入深度产品对齐，
  顺序串联
  pm-jobs、pm-strategy-review、pm-brief、本地简报保存、可选 Zoon 同步、Zoon 漂移检查和原型
  准备度检查，只把会改变方向的 D 选择题交给用户确认。
---

# 自动产品评审

`$pm-autoplan` 是 PMWorkspace 的一键推进模式：把零散想法推进到可确认的产品简报、方案方向与交付资产。它不是跳过产品判断直接出图。

<!-- PMW-GENERATED-CONTRACT:START -->
## PMWorkspace 生成契约

> 本区块由 `bin/pmw-gen-skill-docs` 根据 `pmworkspace-shared/skill-docs/skill-docs.manifest.json` 生成；不要手写修改。更新共享门槛、前置检查或输出字段后，运行 `bin/pmw-gen-skill-docs write`，再运行 `bin/pmw-gen-skill-docs check`。

- skill：`pm-autoplan`
- 契约版本：`3`
- 阶段：自动产品评审
- 定位：作为靠谱产品负责人，总控全新功能或已有功能迭代的深度产品对齐，只推进到当前最早门槛。

### 统一前置检查

- `_PMW_BIN`
- `pmw-update-check`
- `pmw-controller`
- `usage`
- `usage pm-autoplan`
- `pmw-dashboard`
- `pmw-artifact`
- `pmw-discovery-gate`

### 必读共享协议

- `../pmworkspace-shared/references/autoplan-workflow.md`
- `../pmworkspace-shared/references/product-discovery-gate.md`
- `../pmworkspace-shared/references/product-manager-brief.md`
- `../pmworkspace-shared/references/runtime-kernel.md`
- `../pmworkspace-shared/references/pm-workbench-map.md`
- `../pmworkspace-shared/references/product-readiness-dashboard.md`
- `../pmworkspace-shared/references/artifact-flow.md`
- `../pmworkspace-shared/references/pm-eval-system.md`
- `../pmworkspace-shared/references/routing.md`

### 产品表达真源顺序

- 先稳定用户可见产品表达：根 README、routing.md、welcome-guide.md 或对应方法 reference 说明 PMW 对外心智、默认输出和产物命名。
- 再同步 skill 正文和 manifest：生成契约只承接已稳定表达需要共享的阶段、定位、前置检查、必读协议、输出字段和审计字段。
- 然后运行 pmw-gen-skill-docs write/check：让 SKILL.md 生成区块镜像 manifest，防止手写漂移。
- 最后补 eval fixture：把已经稳定的表达锁成防回退断言；不要先写 eval 反向牵引产品表达。

### 共享门槛

- 真源：`pmworkspace-shared/skill-docs/skill-docs.manifest.json` 的 `shared_gates`。
- 快速更新：每个 skill 运行前用 `pmw-update-check --quick`；如果输出 `UPGRADE_AVAILABLE`，先询问用户是否执行 `UPGRADE_COMMAND`，除非 `auto_upgrade` 为 `true`。
- 运行时入口：每个 PMW 产品任务先过 `pmw-controller intake`，由 controller 判定是否继承或新建 run，并写入 `task_digest` / `input_revision`。
- STOP gate：`pmw-controller next` 返回 `ASK_CONFIRMATION`、`NEEDS_BASELINE`、`WRITE_PENDING_BRIEF`、`BRIEF_PENDING`、`D_REQUIRED` 或 `BLOCKED` 时必须停住，不能进入下游产物；`WRITE_PENDING_BRIEF` 只能路由到产品简报。
- 当前任务绑定：brief、visual baseline、prototype-board、review、handoff 和用户确认必须匹配当前 run、`task_digest` 与 `input_revision`；旧产物只能参考，不能放行。
- 摘要：中文本地化、记忆不覆盖本轮事实、只有 `ALLOW_IMAGE_PROMPT` 才能写 image-2 prompt，方向选择不能替代产品简报确认，禁止泄露 token/ownerSecret/私密资料。

### 默认用户可见输出字段

- `工作方式`
- `本轮价值时刻`
- `产品信息对齐`
- `产品作业卡`
- `关键缺口队列`
- `自动评审结论`
- `我建议`
- `理由`
- `当前需要确认`
- `补齐后解锁`
- `下一步`

### 内部审计字段（默认不展示）

- `模式来源`
- `推进阶段`
- `产品信息对齐包`
- `最早门槛`
- `门槛等级`
- `停止原因`
- `下一技能`
- `交接上下文`
- `产品准备度仪表盘`
- `证据状态`
<!-- PMW-GENERATED-CONTRACT:END -->

Before user-facing output, read `../pmworkspace-shared/references/language-and-localization.md`. 面向中文用户时，输出中文标题、状态和建议；只保留 `$pm-*`、Zoon、PRD、image-2、URL 等必要术语。

## Preamble

可用时运行平台检查和记忆摘要：

```bash
_PMW_BIN=""
for _CANDIDATE in "$PWD/bin" "$PWD/pmworkspace-shared/bin" "$HOME/.codex/skills/pmworkspace-shared/bin" "$HOME/.agents/plugins/plugins/pmworkspace/skills/pmworkspace-shared/bin" $(find "$HOME/.codex/plugins/cache" -path "*/pmworkspace/*/skills/pmworkspace-shared/bin" -type d 2>/dev/null | sort -r); do
  if [ -x "$_CANDIDATE/pmw-log" ]; then _PMW_BIN="$_CANDIDATE"; break; fi
done
if [ -n "$_PMW_BIN" ]; then
  _UPD=$("$_PMW_BIN/pmw-update-check" --quick 2>/dev/null || true)
  [ -n "$_UPD" ] && echo "$_UPD"
fi
[ -n "$_PMW_BIN" ] && "$_PMW_BIN/pmw-log" usage pm-autoplan >/dev/null 2>&1 || true
[ -n "$_PMW_BIN" ] && [ -x "$_PMW_BIN/pmw-controller" ] && "$_PMW_BIN/pmw-controller" next --json 2>/dev/null || true
[ -n "$_PMW_BIN" ] && [ -x "$_PMW_BIN/pmw-dashboard" ] && "$_PMW_BIN/pmw-dashboard" status 2>/dev/null || true
[ -n "$_PMW_BIN" ] && [ -x "$_PMW_BIN/pmw-memory" ] && "$_PMW_BIN/pmw-memory" summary 2>/dev/null || true
[ -n "$_PMW_BIN" ] && [ -x "$_PMW_BIN/pmw-question-tuning" ] && "$_PMW_BIN/pmw-question-tuning" summary 2>/dev/null || true
[ -n "$_PMW_BIN" ] && [ -x "$_PMW_BIN/pmw-artifact" ] && "$_PMW_BIN/pmw-artifact" flow 2>/dev/null || true
[ -n "$_PMW_BIN" ] && [ -x "$_PMW_BIN/pmw-discovery-gate" ] && "$_PMW_BIN/pmw-discovery-gate" check --target alignment 2>/dev/null || true
```

## Workflow

1. Read `../pmworkspace-shared/references/autoplan-workflow.md`.
2. Read `../pmworkspace-shared/references/runtime-kernel.md`.
3. Read `../pmworkspace-shared/references/pm-workbench-map.md` and use its 自动产品评审 stage fields.
4. Read `../pmworkspace-shared/references/evidence-dashboard.md`.
5. Read `../pmworkspace-shared/references/product-readiness-dashboard.md`.
6. Read `../pmworkspace-shared/references/artifact-flow.md` and include Product Artifact Flow in the control panel when routing between skills.
7. Read `../pmworkspace-shared/references/pm-decision-principles.md`.
8. Read `../pmworkspace-shared/references/pm-eval-system.md` and treat its contracts as maintenance guardrails for PMWorkspace behavior.
9. Read `../pmworkspace-shared/references/routing.md`; if `$pm-autoplan` was entered from `$pm-workspace`, inherit its product path and run. If called directly, use routing D0 to choose product path; execution depth is always deep alignment.
10. Read `../pmworkspace-shared/references/question-tuning.md`.
11. Read `../pmworkspace-shared/references/product-office-hours.md`.
12. Read `../pmworkspace-shared/references/product-discovery-gate.md`.
13. Read `../pmworkspace-shared/references/product-manager-brief.md`.
14. Read `../pmworkspace-shared/references/adversarial-review.md`.
15. Read `../pmworkspace-shared/references/product-plan-handoff.md`.
16. Read `../pmworkspace-shared/references/zoon-workflow.md` and `../pmworkspace-shared/references/zoon-drift-check.md`.
15. Follow `runtime-kernel.md` Run Owner 协议 through `pmw-controller`: if `$pm-autoplan` was entered from `$pm-workspace`, read the current controller run/revision and inherit it only when `task_digest` matches the current user materials；匹配时复用当前 run，不要重新 `pmw-run start`。If called directly, run `pmw-controller intake --goal "<本轮目标>" --materials "<本轮用户材料摘要>" --skill pm-autoplan --product-path "<全新功能|已有功能迭代>" --depth "deep" --stage autoplan`, then run `pmw-controller next --json`.
    - If controller creates a new `input_revision`, old brief/board/review artifacts are only reference material until re-stamped or regenerated.
    - If `pmw-controller next` returns `ASK_CONFIRMATION`、`NEEDS_BASELINE`、`WRITE_PENDING_BRIEF`、`BRIEF_PENDING`、`D_REQUIRED` or `BLOCKED`, stop at that earliest gate and do not write downstream artifacts.
16. 先建立 `产品信息对齐包` 和 `产品作业卡`，再 Build the automatic review control panel from `autoplan-workflow.md`: 靠谱产品负责人姿态、产品路径、事实来源优先级、当前阶段、产品信息对齐状态、当前主阻断、关键缺口队列、PMW 产品建议、PMW 信息架构建议、最早阻塞门槛、门槛等级、门槛来源、可自动采用项、必须 PM 拍板项、下一技能和交接上下文.
17. 按统一深度产品对齐门槛顺序推进：工作目标模式、产品路径、产品方向审查内核（含线上/竞品基线识别）、证据收集、用户需求澄清、数据/现状佐证、路径机会判断、必要 Q/D、前提确认、策略审查、产品简述 / 产品简报、待确认问题卡、本地简报保存、产品简报确认、已对齐后 Zoon A/B 推荐、已启用 Zoon 的漂移检查、线上参考和设计系统基线、Product Readiness Dashboard 的原型准备度或交付准备度。
18. 用户说“先看方案”“直接出图”“快速给我”也不能绕过产品简报。只有当前 `input_revision` 的产品简报已对齐，并且 `pmw-controller preflight --target prototype` 与 `pmw-image-preflight check` 返回 `ALLOW_IMAGE_PROMPT`，才允许交给 `$pm-prototype-shotgun`。
19. Use `pm-decision-principles.md` to auto-decide only low-risk defaults that do not change product direction; surface any direction-changing item as a single `D` choice question and stop.
23. Give the user a conclusion-first review: first output `自动评审结论` with `我建议` and `理由`, include a short `工作方式` / progress card, and include `本轮价值时刻` plus `补齐后解锁`; then write the full `评审控制面板` to audit.
24. For the earliest gate, always declare `门槛等级` as `阻断`、`高风险`、`可自动采用` or `可延后`, and declare `门槛来源`.
25. Every item in `已自动采用` must include source and why no PM decision is needed, for example `默认移动端优先。来源：PMWorkspace 默认规则。原因：不改变产品方向或用户承诺。`
26. When enough information exists, create the smallest useful product brief and save it with `pmw-log brief <name>`. This saves the local business brief and audit copy, registers `product_brief` in Product Artifact Flow, and syncs to Zoon only when `PMW_ZOON_SYNC_ON_BRIEF=true` / `zoon_sync_on_brief: true` or the user has explicitly chosen online collaboration.
    - `enough information` 必须先通过 `pmw-discovery-gate check --target brief`：深度交付或现有线上功能优化必须覆盖产品定位与链路角色、目标用户与触发时刻、用户现状与当前替代、真实痛点与当前损失、主目标与反指标，并且最终确认产品简报前通常至少完成 2 个方向性 `D`。一个 `Q` 加一个 `D` 不能代表产品发现完成。
    - 如果产品发现深度不足，最早门槛是 `产品发现深度不足`，下一技能必须是 `$pm-jobs`，回到证据收集、需求澄清、数据/现状佐证或产品作业卡里的当前主阻断；不要直接写产品简报或进入原型。
    - 如果产品简报仍有待确认信息，自动评审的用户可见 `下一步` 必须先让用户补齐或确认偏差风险，不能推荐 Zoon，也不能只提示“确认后进入原型 / 交付”。
    - 产品简报确认状态已对齐并且本地 Markdown 保存成功后，自动评审的用户可见 `下一步` 必须走 `$pm-brief` 同一段 Zoon 推荐选择。
    - 固定推荐文案：`Zoon 协作建议：这次已对齐简报适合多人评审 / 后续原型或 PRD 复用，建议同步到 Zoon；不同步也不影响继续使用本地 Markdown。`
    - 推荐必须说明 Zoon 的好处：多人协作、事实源统一、后续 image-2 原型 / PRD 防漂移；同时说明 `不自动同步，不作为出图或交付阻断`。
    - 必须让用户用一个轻量 `D` 选择：`D：是否同步到在线协作文档（Zoon）？A. 先不需要，使用本地 Markdown 继续；B. 需要，同步到 Zoon 供团队在线修改。`
27. If a Zoon URL exists before prototype preparation, run `pmw-zoon drift --url <url>` when available. If it returns `DRIFT`, read the latest Zoon snapshot and update the product brief version before continuing.
28. Before routing to `$pm-prototype-shotgun` or `$pm-handoff`, run `pmw-dashboard readiness --target prototype` or `pmw-dashboard readiness --target handoff` when available and use the short verdict in the user-facing conclusion, including its `阻断影响` and `解锁动作`. If the verdict is `不可出图` or `不可交付`, route to the first blocking gate instead of continuing. Only show `--details` when the user asks for audit/debug output.
29. Map the earliest blocking gate to one next skill: `$pm-jobs`, `$pm-strategy-review`, `$pm-brief`, `$pm-prototype-shotgun`, `$pm-prototype-review`, or `$pm-handoff`. Do not pretend all downstream skills have completed when only the next gate is ready.
30. `下一技能` cannot be only a skill id in audit; record `交接上下文` with 来源门槛、已确认事实、未决 Q/D、证据状态 and 交给它的原因. 交接上下文还必须追加上游产物、本轮产物、下游可读和产物流动，但默认不展示给用户。
31. At each gate, record evidence, decisions, artifacts, or reviews with `pmw-run event`; before final output, run `pmw-dashboard status` when available and only surface its short business summary.
32. End with a readiness state: `需要补充`、`待确认`、`已对齐`、`可进入原型复审`、or `可交付`. Call `pmw-run finish` only when the current run reaches a terminal readiness state; if waiting for Q/D/证据 or handing off to a child skill, keep the current run open for reuse.

## Auto-Decide Rules

自动决策必须遵守 `pm-decision-principles.md` 的事实优先级：已对齐产品简报或最新 Zoon 快照 > 用户本轮明确输入 > 当前已确认 Q / D / 前提 > 运行审计和复审结论 > 历史偏好。

自动接受：

- 用户已经明说或文档中明确写出的事实。输出时说明来源：用户本轮明确输入 / 已对齐产品简报 / 最新 Zoon。
- 默认移动端优先画布。输出时说明来源：PMWorkspace 默认规则；原因：不改变产品方向或用户承诺。
- 不影响方向的格式、标题、状态字段。输出时说明来源：PMWorkspace 输出协议；原因：不改变范围、承诺或验收。
- 已有 Zoon URL 时优先 append，不新建文档。输出时说明来源：Zoon 协议；原因：保持在线事实来源连续。
- 未启用 Zoon 时使用本地已对齐产品简报。输出时说明来源：PMWorkspace 默认规则；原因：减少在线协作卡点，不改变产品事实。

必须提问：

- 目标人群、主目标、反指标、不可虚构项仍会改变原型结构。
- 多方案方向没有本质差异。
- 线上参考需要但缺失。
- Zoon 最新内容和本地产品简报冲突。
- 用户承诺、数据真实性、线索/交易/隐私口径需要 PM 拍板。
- 当前 `input_revision` 的产品简报尚未达到 `已对齐`，但用户要求跳到原型、HTML、交付稿或完整 PRD。

## 输出

```text
自动评审结果：

工作方式：
- 当前模式：
- 本轮价值时刻：
- 当前一步：
- 已完成：
- 下一步：
- 产品作业卡：

自动评审结论：
- 我建议：
- 理由：
- 当前需要确认：
- 补齐后解锁：
- 下一步：

内部评审控制面板（默认不展示，写入审计）：
- 状态：
- run_id：
- 对齐深度：深度产品对齐
- 路径来源：
- 产品路径：<全新功能 / 已有功能迭代>
- 当前任务流阶段：
- 推进阶段：
- 当前门槛：
- 最早门槛：
- 门槛等级：
- 门槛来源：
- 停止原因：
- 下一技能：
- 交接上下文：
- 已自动采用：
- 需要 PM 拍板：
- 证据状态：
- 证据状态页：
- 产品准备度仪表盘：
- 产物流动：
- 上游产物：
- 本轮产物：
- 下游可读：
- 产品简报：
- 产品设计文档：
- 方案方向：
- 原型图片计划：
- Zoon 同步：
- Zoon 漂移检查：
- 原型准备度：
- 可升级到：
- 建议下一步：
```

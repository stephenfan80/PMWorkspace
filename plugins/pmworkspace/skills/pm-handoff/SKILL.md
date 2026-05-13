---
name: pm-handoff
description: |
  PMWorkspace 精简 PRD 交付官。用于把已对齐的产品简报、选定原型方向、PRD 笔记、
  Zoon 文档或产品决策记录，压缩成可执行的最小交付契约；默认 PRD 只保留需求背景、
  需求价值、需求方案、需求功能及描述、接口以及数据来源、埋点信息和实验标准。
---

# 产品交付

把选定产品方向整理成精简 PRD 和可复用交付资产，同时明确保留未解决的问题。`$pm-handoff` 是精简 PRD 交付官，不是项目管理计划、测试计划或开发周期排期工具。生成产品设计文档时，它读取产品评估和原型复审中的对抗结论，记录哪些判断仍是假设、哪些原型表达需要防误解；这不是新增交付 gate。

<!-- PMW-GENERATED-CONTRACT:START -->
## PMWorkspace 生成契约

> 本区块由 `bin/pmw-gen-skill-docs` 根据 `pmworkspace-shared/skill-docs/skill-docs.manifest.json` 生成；不要手写修改。更新共享门槛、前置检查或输出字段后，运行 `bin/pmw-gen-skill-docs write`，再运行 `bin/pmw-gen-skill-docs check`。

- skill：`pm-handoff`
- 契约版本：`2`
- 阶段：产品交付
- 定位：把已对齐 brief、已通过复审的原型、产品路径和产品判断演进整理成产品设计文档或精简 PRD / 交付稿，并沉淀脱敏交付资产。

### 统一前置检查

- `_PMW_BIN`
- `pmw-update-check`
- `usage`
- `usage pm-handoff`
- `pmw-dashboard`
- `readiness --target handoff`
- `pmw-artifact`

### 必读共享协议

- `../pmworkspace-shared/references/delivery-handoff.md`
- `../pmworkspace-shared/references/product-plan-handoff.md`
- `../pmworkspace-shared/references/prototype-quality-review.md`
- `../pmworkspace-shared/references/pm-review-army.md`
- `../pmworkspace-shared/references/runtime-kernel.md`
- `../pmworkspace-shared/references/product-readiness-dashboard.md`
- `../pmworkspace-shared/references/pm-workbench-map.md`
- `../pmworkspace-shared/references/artifact-flow.md`
- `../pmworkspace-shared/references/pm-eval-system.md`

### 共享门槛

- 真源：`pmworkspace-shared/skill-docs/skill-docs.manifest.json` 的 `shared_gates`。
- 快速更新：每个 skill 运行前用 `pmw-update-check --quick`；如果输出 `UPGRADE_AVAILABLE`，先询问用户是否执行 `UPGRADE_COMMAND`，除非 `auto_upgrade` 为 `true`。
- 摘要：中文本地化、复用 `current_run_id`、记忆不覆盖本轮事实、等待 Q/D/证据/确认时停住、禁止泄露 token/ownerSecret/私密资料。

### 默认用户可见输出字段

- `交付结论`
- `交付目标`
- `产品设计文档`
- `产品判断演进`
- `产品评估与原型可信度复审结论`
- `原型设计完整度`
- `精简 PRD`
- `功能能力与研发依赖`
- `待补充项`
- `Zoon 协作建议`
- `在线协作选择`
- `下一步`

### 内部审计字段（默认不展示）

- `事实来源`
- `产品判断对抗校验`
- `原型可信度对抗复审`
- `产品准备度仪表盘`
- `交付前门槛`
- `原型复审状态`
- `prototype-board 设计完整度`
- `研发可行性反问`
- `验收写入边界`
- `交付资产沉淀`
- `下一技能`
- `证据状态`
<!-- PMW-GENERATED-CONTRACT:END -->

Before user-facing output, read `../pmworkspace-shared/references/language-and-localization.md`. For Chinese users, call the artifact `交付稿` and use Chinese headings. Keep `PRD` when referring to the document type.

## Preamble

运行平台检查和使用记录：

```bash
_PMW_BIN=""
for _CANDIDATE in "$PWD/bin" "$PWD/pmworkspace-shared/bin" "$HOME/.codex/skills/pmworkspace-shared/bin" "$HOME/.agents/plugins/plugins/pmworkspace/skills/pmworkspace-shared/bin" $(find "$HOME/.codex/plugins/cache" -path "*/pmworkspace/*/skills/pmworkspace-shared/bin" -type d 2>/dev/null | sort -r); do
  if [ -x "$_CANDIDATE/pmw-log" ]; then _PMW_BIN="$_CANDIDATE"; break; fi
done
if [ -n "$_PMW_BIN" ]; then
  _UPD=$("$_PMW_BIN/pmw-update-check" --quick 2>/dev/null || true)
  [ -n "$_UPD" ] && echo "$_UPD"
fi
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
6. Read `../pmworkspace-shared/references/decision-question-mode.md`; 交付中如果仍有会改变范围、承诺、实验口径、验收或产品设计文档结论的取舍，一次只展开一个当前 `D`，不要批量写多个验收相关决策。
7. Read `../pmworkspace-shared/references/runtime-kernel.md`.
8. Read `../pmworkspace-shared/references/evidence-dashboard.md` and run `pmw-dashboard status` when available for a short summary; use `--details` only for audit/debug output.
9. Read `../pmworkspace-shared/references/product-readiness-dashboard.md` and run `pmw-dashboard readiness --target handoff` when available for the verdict.
10. Read `../pmworkspace-shared/references/prototype-shotgun-board.md`; if a selected prototype direction exists, include the board result instead of relying on memory.
11. Read `../pmworkspace-shared/references/zoon-drift-check.md`.
12. Read `../pmworkspace-shared/references/product-memory.md`; use `pmw-memory user-summary` and `pmw-memory delivery-summary` when available. If delivery assets affect wording, explicitly say `基于本地交付资产...`; memory cannot override the current brief, Zoon, 反指标, 不可虚构项, 线上参考门槛 or 本轮输入。
13. Read `../pmworkspace-shared/references/pm-workbench-map.md` and use its 产品交付 stage fields.
14. Read `../pmworkspace-shared/references/artifact-flow.md` and read latest `product_brief` / `prototype_review` artifacts before writing delivery assets.
15. Read `../pmworkspace-shared/references/pm-eval-system.md` and preserve delivery contracts.
16. Follow `runtime-kernel.md` Run Owner 协议：如果 `pmw-project show` 已有 `current_run_id`，复用当前 run；如果用户直接调用 `$pm-handoff` 且没有当前 run，再创建 runtime run.
17. 如果用户要 PRD、研发交付、实验标准、埋点或接口梳理，先提示：`如果你有现成 PRD、接口文档、埋点方案、实验方案、Zoon 或截图，可以上传给我参考；没有的话，我会基于当前已对齐 brief 生成精简 PRD，并把缺失项留空待补充。`
18. 建立交付控制器，记录 `交付目标`、`事实来源`、`Product Readiness Dashboard`、`交付前门槛`、`原型复审状态`、`未决拍板`、`交付类型`、`产品设计文档来源`、`产品判断对抗校验`、`原型可信度对抗复审`、`研发可行性反问`、`功能能力与研发依赖`、`PRD 缺口处理`、`验收写入边界`、`交付资产沉淀`、`上游产物`、`本轮产物`、`下游可读`、`产物流动`、`下一技能` 和 `证据状态`；这些默认写入审计，不能进入 PRD 正文。用户可见输出只保留交付结论、产品设计文档或精简 PRD、功能能力与研发依赖、待补充项、Zoon 协作建议、在线协作选择和下一步，不输出 `PRD 生成判断`。
19. 如果 `pmw-project show` 中有 Zoon URL，先运行 `pmw-zoon drift`；若存在实质漂移，读取最新文档，作为交付事实来源，并退回 `$pm-brief` 或 `$pm-strategy-review`，不要沿用旧交付口径。
20. 如果产品简报不是 `已对齐`，退回 `$pm-brief`；如果交付依赖原型但复审不是 `可通过`，退回 `$pm-prototype-review`、`$pm-prototype-shotgun` 或当前 `D`。
21. 交付稿输出前执行 `研发可行性反问`：逐项审查功能承诺背后的数据来源、接口能力、算法 / 推荐能力、规则口径、权限、后台配置、运营支持、埋点日志、异常 / 空态和合规边界；把结果落入 `产品需补齐`、`研发需评估`、`可留待补充` 或 `不可写入验收`。
22. 如果研发可行性反问发现选中路径的成本、能力或数据前提不成立，退回 `$pm-strategy-review`，用收缩、转向或选择性扩大重新拍板；不能静默改方案。
23. 完成研发可行性反问后，平台脚本可用时用 `pmw-run event --type gate --status "已完成" --title "研发可行性反问" --summary "<功能能力与研发依赖审查结果>"` 记录现有 run；不新增 artifact。
24. 交付稿输出前必须运行 Product Readiness Dashboard；如果 verdict 是 `不可交付`，根据第一条阻断行退回 `$pm-brief`、线上参考门槛、`$pm-prototype-shotgun`、`$pm-prototype-review`、研发可行性反问或当前 `D`，不写 PRD、实验口径或验收标准。默认只展示短 verdict 和第一阻断原因。
25. 如果仍有会改变范围、用户承诺、实验口径、数据真实性、算法能力、线索/交易/隐私/合规边界或验收标准的未决 D，停止在 `需要 PM 拍板`，只输出一个当前 `D`，不写研发验收标准、实验口径或对外承诺。
26. 如果用户要求产品设计文档，或上游已经完成三条产品路径 image-2 原型图与复审，默认优先生成 `产品设计文档`；否则默认选择 `精简 PRD`。只有用户明确要求设计交付、实验验证或研发交付时，才追加对应补充，不把所有模板硬塞进一份文档。
27. 产品设计文档必须读取 `product_brief` 中的产品判断对抗校验、`prototype_review` 中的原型可信度对抗复审，以及 prototype-board 中每个方案的产品路径、用户行为假设、要赢过的现状替代、当前损失、删除 / 牺牲 / 后置项、验证信号、失败信号、原型思考、信息架构设计思考、用户问题解决逻辑、反指标保护、不可虚构边界、设计完整度评分、10/10 原型标准、prompt 设计修正、状态覆盖、第一眼 / 第二眼 / 第三眼和反 AI 模板味约束，生成 `背景与现状 / 用户需求与证据 / 数据或访谈或截图或竞品启发 / 产品简述 / 三条产品路径对比 / 每个方案原型图 / 原型设计完整度与重出依据 / 产品评估与原型可信度复审结论 / 信息架构设计思考 / 产品判断演进 / 推荐方案 / 风险与待验证 / 下一步产品作业 / 下一步`。
28. 精简 PRD 核心只保留本周期承诺。单功能默认使用 `1-2 周` 交付 / 验证口径；只有跨模块、大功能或产品线规划才使用 `1-3 个月`，并且只能进入阶段规划或下一步，不能写成本周期验收。PRD 默认只写：需求背景、需求价值、需求方案、需求功能及描述、功能能力与研发依赖、接口以及数据来源、埋点信息、实验标准。测试计划、开发周期、排期、人力、会议纪要和长风险清单默认不写。
29. 缺接口、数据字段、埋点属性或实验细节但不改变承诺时，保留空值并写入 `待补充项`；每项状态使用 `待补充`、`已跳过` 或 `已补充`，用户可回复 `跳过某项` 或 `全部先跳过`，普通缺口不阻断当前 PRD。不能虚构字段、口径、事件名、接口可用性、算法能力或实验阈值。
30. Keep unsupported capabilities under `不可虚构`; unsupported capabilities, unverified data, unresolved commitments, and future ideas must not appear as acceptance criteria.
31. 从用户输入中提取可复用交付资产：接口、数据来源、指标口径、埋点事件、实验标准、功能能力依赖和数据可用性判断；平台脚本可用时，用 `pmw-memory add-delivery-fact` 写入本地脱敏资产，并标明 `scenario`、`target`、`scope`、`source`、`confidence` 和 `fact-type`。
32. 平台脚本可用时，用 `pmw-log handoff <name>` 保存交付稿，它会登记 `handoff` 到 Product Artifact Flow；产品设计文档用 `pmw-log handoff <name> --artifact-kind product_design_doc` 保存并登记 `product_design_doc`，同时把 `PM 判断摘要` / `产品判断演进` 和 `下一步产品作业` 写入结构化字段。需要给 QA、发布或文档同步接力时，额外用 `pmw-artifact add --kind acceptance_seed` 或 `--kind release_doc_seed` 记录下游可读摘要。记录 `pmw-run event --type artifact`，并且只有交付前门槛全部通过时才 `pmw-run finish --status "可交付"`。
33. 交付稿 / PRD / 产品设计文档保存后必须输出 `Zoon 协作建议` 和 `在线协作选择`，把本地 Markdown 定位为已完成交付稿，把 Zoon 定位为团队继续修改、评审和研发对齐的协作起点。推荐文案必须说明：同步后 PMWorkspace agent 会自动加入文档继续协助修改；不自动同步、不阻断本地 Markdown 继续使用。每次让用户选择：`A. 暂不需要，继续使用本地 Markdown`；`B. 同步到已有 Zoon 文档（提供 URL 或使用项目已记录 URL）`；`C. 新建一个 Zoon 交付文档`。
34. 用户选择 B/C 后才调用 `pmw-zoon append|create|sync`。创建或追加成功后，默认由 `pmw-zoon` 自动执行 `join` / presence，让 `pmworkspace` agent 加入协作态，并优先打开 Codex 内置浏览器。若自动加入失败或服务不支持，输出：`已创建/已同步，但 agent 自动加入失败/不支持，请在文档编辑页手动邀请或继续用本地 Markdown`；不要把手动邀请作为默认流程。

## 输出结构

产品设计文档输出结构：

```markdown
# 产品设计文档：<功能名>

## 交付结论

- 结论：
- 交付目标：
- 准备度：
- 来源：
- 下一步：

## 背景与现状

## 用户需求与证据

## 数据 / 访谈 / 截图 / 竞品启发

## 产品简述

## 三条产品路径对比

| 方案 | 产品路径 | 用户行为假设 | 要赢过的现状替代 | 当前损失 | 删除 / 牺牲 / 后置项 | 验证信号 | 失败信号 | 信息架构设计思考 | 用户问题解决逻辑 | 反指标保护 | 风险 |
|---|---|---|---|---|---|---|---|---|---|---|---|

## 每个方案原型图

| 方案 | 屏幕任务 | image-2 原型图 | 产品路径 | 原型思考 | 不可虚构项 |
|---|---|---|---|---|---|

## 原型设计完整度与重出依据

| 方案 | 屏幕任务 | 设计评分 | 10/10 原型标准 | 主要差距 | 状态覆盖 | 第一眼 / 第二眼 / 第三眼 | 反 AI 模板味约束 | 复审结论 / 重出依据 |
|---|---|---|---|---|---|---|---|---|

## 产品评估与原型可信度复审结论

| 来源 | 想当然 / 理解偏差 / 证据不足 / 假设视觉化风险 | 处理动作 | 对推荐方案的影响 |
|---|---|---|---|

## 推荐方案

## 产品判断演进

| 判断项 | 保留 / 放弃 / 调整 | 原因 | 证据状态 | 对后续的影响 |
|---|---|---|---|---|

## 风险与待验证

## 下一步产品作业

## 下一步
```

精简 PRD 输出结构：

```markdown
# PRD：<需求名>

## 交付结论

- 结论：
- 交付目标：
- 准备度：
- 待补充项数量 / 状态：
- 下一步：

## 需求背景

## 需求价值

## 需求方案

## 需求功能及描述

| 功能模块 | 功能描述 | 规则 / 状态 | 异常 / 空态 | 待补充 |
|---|---|---|---|---|

## 功能能力与研发依赖

| 功能承诺 | 所需能力 | 当前状态 | 事实来源 | 责任归属 | 是否阻断 | 处理动作 |
|---|---|---|---|---|---|---|

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

| 待补充项 | 为什么需要 | 状态 | 用户可选动作 |
|---|---|---|---|

## 下一步：待补充决策清单

- 可回复 `补充 <待补充项>` 继续完善。
- 可回复 `跳过 <待补充项>` 或 `全部先跳过`；普通缺口不阻断当前 PRD。
- 如果补充内容改变范围、承诺、实验口径、数据真实性、合规或验收标准，先进入一个当前 `D`。

## 不可虚构

```

## Zoon 协作建议

交付稿已保存为本地 Markdown。建议同步到 Zoon，让团队在线修改 PRD / 产品设计文档，并让 PMWorkspace agent 加入文档继续协助完善接口、埋点、实验标准和待补充项。不同步也不影响继续使用本地 Markdown。

在线协作选择：
- A. 暂不需要，继续使用本地 Markdown。
- B. 同步到已有 Zoon 文档（提供 URL 或使用项目已记录 URL）。
- C. 新建一个 Zoon 交付文档。

内部交付审计继续记录交付前门槛、原型复审状态、未决拍板、产物流动和已保存资产；默认不展示给用户，也不写入 PRD 正文。

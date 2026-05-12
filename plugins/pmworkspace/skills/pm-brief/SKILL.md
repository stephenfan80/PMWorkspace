---
name: pm-brief
description: |
  PMWorkspace 产品简述 / 产品简报生成器。用于把产品方向审查、关键 Q/D、策略审查、
  PRD 笔记、Zoon 文档、截图 / 关键节点截图 / 数据、竞品或客户洞察，写成能指导三条产品路径原型、
  复审和最终产品设计文档的短版产品简述 / 产品简报，并保留版本、事实来源、门槛和“已对齐”状态。
---

# 产品简述 / 产品简报

创建后续三条产品路径原型、复审、产品设计文档、交付稿和实验步骤都必须读取的产品简述 / 产品简报。它不是会议纪要，也不是最终产品设计文档；它要接收产品方向审查结论，讲清真实问题、证据状态、目标用户、当前替代 / 损失、选中路径、范围模式、本周期验证、主目标、反指标、不可虚构项、PM 判断摘要、产品判断对抗校验、原型范围、产品作业和待验证项，再进入方案和原型。

<!-- PMW-GENERATED-CONTRACT:START -->
## PMWorkspace 生成契约

> 本区块由 `bin/pmw-gen-skill-docs` 根据 `pmworkspace-shared/skill-docs/skill-docs.manifest.json` 生成；不要手写修改。更新共享门槛、前置检查或输出字段后，运行 `bin/pmw-gen-skill-docs write`，再运行 `bin/pmw-gen-skill-docs check`。

- skill：`pm-brief`
- 契约版本：`2`
- 阶段：产品简报
- 定位：把已完成的产品方向审查、价值判断、PM 判断摘要、产品作业和策略取舍写成出图前短版产品简述 / 产品简报，默认本地保存，并按用户选择同步到 Zoon。

### 统一前置检查

- `_PMW_BIN`
- `pmw-update-check`
- `usage`
- `usage pm-brief`
- `pmw-memory`
- `pmw-artifact`
- `pmw-discovery-gate`

### 必读共享协议

- `../pmworkspace-shared/references/product-discovery-gate.md`
- `../pmworkspace-shared/references/product-manager-brief.md`
- `../pmworkspace-shared/references/product-plan-handoff.md`
- `../pmworkspace-shared/references/production-reference-gate.md`
- `../pmworkspace-shared/references/pm-decision-principles.md`
- `../pmworkspace-shared/references/pm-eval-system.md`
- `../pmworkspace-shared/references/pm-workbench-map.md`
- `../pmworkspace-shared/references/artifact-flow.md`
- `../pmworkspace-shared/references/runtime-kernel.md`
- `../pmworkspace-shared/references/zoon-workflow.md`
- `../pmworkspace-shared/references/zoon-drift-check.md`
- `../pmworkspace-shared/references/product-readiness-dashboard.md`

### 共享门槛

- 真源：`pmworkspace-shared/skill-docs/skill-docs.manifest.json` 的 `shared_gates`。
- 摘要：中文本地化、复用 `current_run_id`、记忆不覆盖本轮事实、等待 Q/D/证据/确认时停住、禁止泄露 token/ownerSecret/私密资料。

### 默认用户可见输出字段

- `产品简述 / 产品简报`
- `产品作业卡`
- `核心价值判断`
- `PM 判断摘要`
- `产品判断对抗校验`
- `确认状态`
- `当前需要确认`
- `下一步`

### 内部审计字段（默认不展示）

- `产品简报门槛`
- `产品信息对齐包`
- `支持信息`
- `缺失门槛`
- `事实/假设边界`
- `PM 判断摘要`
- `产品判断对抗校验`
- `产品作业`
- `Zoon 同步状态`
- `Zoon 漂移检查`
- `产品准备度仪表盘`
- `下一技能`
- `证据状态`
<!-- PMW-GENERATED-CONTRACT:END -->

Before user-facing output, read `../pmworkspace-shared/references/language-and-localization.md`. For Chinese users, call the artifact `产品简报`; keep `brief` only when referring to a technical file or existing English source.

## Preamble

可用时运行平台检查和使用记录：

```bash
_PMW_BIN=""
for _CANDIDATE in "$PWD/bin" "$PWD/pmworkspace-shared/bin" "$HOME/.codex/skills/pmworkspace-shared/bin" "$HOME/.agents/plugins/plugins/pmworkspace/skills/pmworkspace-shared/bin" $(find "$HOME/.codex/plugins/cache" -path "*/pmworkspace/*/skills/pmworkspace-shared/bin" -type d 2>/dev/null | sort -r); do
  if [ -x "$_CANDIDATE/pmw-log" ]; then _PMW_BIN="$_CANDIDATE"; break; fi
done
[ -n "$_PMW_BIN" ] && "$_PMW_BIN/pmw-update-check" 2>/dev/null || true
[ -n "$_PMW_BIN" ] && "$_PMW_BIN/pmw-log" usage pm-brief >/dev/null 2>&1 || true
[ -n "$_PMW_BIN" ] && [ -x "$_PMW_BIN/pmw-dashboard" ] && "$_PMW_BIN/pmw-dashboard" status 2>/dev/null || true
[ -n "$_PMW_BIN" ] && [ -x "$_PMW_BIN/pmw-memory" ] && "$_PMW_BIN/pmw-memory" user-summary 2>/dev/null || true
[ -n "$_PMW_BIN" ] && [ -x "$_PMW_BIN/pmw-artifact" ] && "$_PMW_BIN/pmw-artifact" flow 2>/dev/null || true
[ -n "$_PMW_BIN" ] && [ -x "$_PMW_BIN/pmw-discovery-gate" ] && "$_PMW_BIN/pmw-discovery-gate" check --target brief 2>/dev/null || true
```

## Workflow

1. Read `../pmworkspace-shared/references/product-discovery-gate.md`; product brief confirmation requires this gate.
2. Read `../pmworkspace-shared/references/product-manager-brief.md`; use its business brief structure by default.
3. Read `../pmworkspace-shared/references/product-plan-handoff.md`.
4. Read `../pmworkspace-shared/references/production-reference-gate.md`，并写入页面类型和线上参考状态。
3. Read `../pmworkspace-shared/references/pm-decision-principles.md` before deciding whether to write a brief, ask a D, or apply memory.
4. Read `../pmworkspace-shared/references/pm-eval-system.md` and preserve the brief gate contracts it lists.
5. Read `../pmworkspace-shared/references/pm-workbench-map.md` and use its 产品简报 stage fields.
6. Read `../pmworkspace-shared/references/artifact-flow.md`; `$pm-brief` must turn upstream Q/D and strategy decisions into a downstream-readable `product_brief`.
7. Read `../pmworkspace-shared/references/runtime-kernel.md`; follow its Run Owner 协议：如果 `pmw-project show` 已有 `current_run_id`，复用当前 run；如果用户直接调用 `$pm-brief` 且没有当前 run，再创建 runtime run.
8. Read `../pmworkspace-shared/references/decision-question-mode.md` and turn PM decision items into choice questions.
9. Read `../pmworkspace-shared/references/internet-best-practice-research.md` and run lightweight internet best-practice research for the dominant scenario when tools are available.
10. Read `../pmworkspace-shared/references/zoon-workflow.md`; Zoon is optional by default. Save the local brief first, then ask whether to sync to Zoon unless the user already provided a Zoon URL or explicitly requested online collaboration.
11. Read `../pmworkspace-shared/references/zoon-drift-check.md`.
12. Read `../pmworkspace-shared/references/product-readiness-dashboard.md`; if the next skill will be `$pm-prototype-shotgun` or `$pm-handoff`, run `pmw-dashboard readiness --target prototype|handoff` when available, use the verdict for gating, and only show the short verdict / first blocker by default.
13. Read `../pmworkspace-shared/references/product-memory.md` and use `pmw-memory user-summary` plus `pmw-memory summary` when available. If memory changes phrasing or recommendation, explicitly say `基于过往偏好...` or `基于本地产品认知...`; memory cannot override the current brief, Zoon, anti-metric, non-fiction boundary, online reference gate, or missing gate.
14. 先建立 `产品信息对齐包` 和 `产品作业卡`，再进入产品简述控制器。控制器要求：先建立产品简述控制器，记录 `来源门槛`、`已完成门槛`、`缺失门槛`、`事实/假设边界`、`PM 判断摘要`、`产品判断对抗校验`、`产品作业`、`策略决策写入`、`5 个核心事实维度`、`当前主阻断`、`关键缺口队列`、`PMW 产品建议`、`PMW 信息架构建议`、`产品发现深度`、`简报深度`、`上游产物`、`本轮产物`、`下游可读`、`产物流动`、`下一技能` 和 `证据状态`；再写业务简述，避免把审计日志堆成正文。
14. 如果来自 `$pm-jobs` 或 `$pm-strategy-review`，先接收上游输出的前提挑战、现状替代、不做推演、路径对比、范围模式、选中路径、本周期验证、风险、范围、价值交换、信任/风险、反指标、可行性、定位、业务冲突、产品判断对抗校验和待决策队列。
15. 如果基础事实仍缺失，退回 `$pm-jobs`，只展开一个当前 Q，不写完整产品简报；如果 `pmw-discovery-gate check --target brief` 阻断，也退回 `$pm-jobs` 补齐产品发现维度。基础事实包括产品定位与链路角色、目标人群、触发时刻、用户现状、当前替代方案、真实问题与当前损失、主目标、反指标、约束、数据可用性和不可虚构项。如果策略取舍仍未拍板，退回 `$pm-strategy-review`，只展开一个当前 D。
16. 确认已完成工作目标模式、多轮 Q 诊断、产品发现深度门槛、至少 2 个方向性 D（或记录 D 豁免原因）、前提确认和必要策略拍板；如果缺失，只输出短对齐摘要、缺失门槛和下一技能，不写完整产品简报。一个 `Q` 加一个 `D` 不能代表产品发现完成；`D` 不能替代事实诊断。
    - 用户选择 `方案 A / 方案 B / 方案 C` 只能写成 `选中路径 / 方案方向确认`，不能写成 `产品简报确认：已对齐`。如果选择方向后又上传了线上截图，必须把截图中的线上事实、当前优势、问题区域、保留项、可改项和生产基线改动证明写入候选 brief，并重新等待用户确认。
    - 已有功能迭代的 brief 必须说明新方案为什么优于当前线上。如果说不清，只能建议保留 / 微调线上方案或继续补证据，不能把 Agent 生成的新结构写成推荐方案。
17. 如果已有 Zoon URL，先运行 `pmw-zoon drift` 或读取最新 Zoon 快照；Zoon 漂移如果改变目标、反指标、不可虚构项、范围、用户承诺或方案方向，确认状态退回 `待确认`，并回到 `$pm-jobs` 或 `$pm-strategy-review`。
18. 根据模糊程度、风险等级和证据状态选择快速版、标准版或深度版产品简述 / 产品简报。简报深度不等于内容长度；深度只代表证据和风险处理深度，不代表把审计日志写进正文。
19. 用户可见输出必须先给业务版 `产品简述 / 产品简报`，默认包含 `产品作业卡`、`真实问题`、`PM 判断摘要`、`产品判断对抗校验`、`证据状态`、`目标用户`、`当前替代 / 损失`、`选中路径`、`范围模式`、`本周期验证`、`主目标`、`反指标`、`不可虚构项`、`原型范围`、`待验证项与产品作业`。这些业务内容不能默认藏进 `支持信息`；本地路径、run、Zoon 状态表、产物流动和完整证据边界仍进入内部审计。
    - Zoon、线上参考、检索来源、已保存资产和证据边界默认进入内部审计；业务正文只保留会影响产品判断的现状、竞品、痛点、替代方案和解决思路。
20. `产品核心信息` 可以作为简报摘要保留，但不能替代产品简述正文；产品简述必须讲清真实问题、证据状态、用户痛点、当前替代/损失、选中路径、范围模式、本周期验证和待验证项。
21. 互联网案例启发只保留 `可借鉴原则`、`不可照搬` 和 `对原型影响`；参考来源放入内部审计。最佳实践不能覆盖当前 brief、Zoon、线上截图、反指标或不可虚构项。
22. 把已拍板的范围模式、选中路径和策略取舍写入产品方向审查后的设计取舍、方案方向、范围外、决策记录、本周期验证和对原型的影响；未拍板的范围变化或策略取舍只能放进当前 D 或后续 D 队列。
    - 把 `$pm-jobs` 的 `PM 判断摘要` 写入简报正文；如果上游没有提供，`$pm-brief` 必须基于已知事实补出暂定摘要，并清楚标注证据边界、建议范围模式和不可承诺项。
    - 把 `$pm-jobs` 或 `$pm-strategy-review` 的 `产品判断对抗校验` 写入事实/假设边界、风险 / 待验证和内部审计；如果缺失，`$pm-brief` 只能基于已知事实补出暂定校验，并标注为 `假设驱动`。
    - 把本阶段 `产品作业` 写入待验证问题与下一步；作业必须是现实动作，不能写成“继续沟通”。
23. 已对齐且用户要原型时，下一技能是 `$pm-prototype-shotgun`；已对齐且用户要交付时，下一技能是 `$pm-handoff`；未对齐时停在 `$pm-brief` 或回到上游缺失门槛。
24. 从功能名或产品简报标题提炼中文项目名，并用 `pmw-project set-name "<中文项目名>"` 保存。
25. 产品简报生成后必须先停在 `产品简报确认`：把 2-4 条关键前提、方案方向、反指标、不可虚构项和 `风险 / 待验证` 展示给用户。已有功能迭代还必须展示线上基线判断：当前线上优势、问题区域、必须保留、可以改、暂不应改、为什么新方案优于当前线上。只有用户明确确认产品简报或关键前提后，当前 run 才能记录 `产品简报确认：已对齐`，并且产品简报确认状态才能写成 `已对齐`；未确认时保存为 `待确认`，不能把下一技能指向 `$pm-prototype-shotgun`。
26. Save the brief with `pmw-log brief <name>` when platform scripts are available. It uses local-first, Zoon-optional publishing: save the business brief as latest brief, save the full input as a local audit copy, and automatically register `product_brief` in Product Artifact Flow. 完整审计副本保存在本地. It syncs to Zoon only when `PMW_ZOON_SYNC_ON_BRIEF=true` / `zoon_sync_on_brief: true` or the user explicitly chose online collaboration. 如果输入简报声明 `确认状态：已对齐`，但当前 run 没有 `产品简报确认 / 前提确认：已对齐` 记录，或 `pmw-discovery-gate check --target brief` 未通过，平台脚本会拒绝保存为已对齐。`pmw-log brief` 会把 `PM 判断摘要` 和 `产品作业` 写入 artifact-flow 的结构化字段；显式传入 `--pm-judgment-summary` / `--product-homework` 时优先使用参数，否则从 Markdown 章节提取。
    - 本地 Markdown 保存成功后，用户可见 `下一步` 必须默认推荐 Zoon，但不能自动同步：`Zoon 协作建议：这次简报适合多人评审 / 后续原型或 PRD 复用，建议同步到 Zoon；不同步也不影响继续使用本地 Markdown。`
    - 推荐必须说明 Zoon 的好处：多人协作、事实源统一、后续 image-2 原型 / PRD 防漂移；同时说明 `不自动同步，不作为出图或交付阻断`。
    - 推荐后必须让用户用一个轻量 `D` 选择：`D：是否同步到在线协作文档（Zoon）？A. 先不需要，使用本地 Markdown 继续；B. 需要，同步到 Zoon 供团队在线修改。`
27. Ask before creating or updating a Zoon online brief:
    - If a Zoon URL is already available, ask whether to append this brief to that document before calling `pmw-zoon sync` / `pmw-zoon append --url <url>`.
    - If no Zoon URL exists, do not auto-create one. Ask `是否同步到在线协作文档（Zoon）？A. 先不需要，使用本地 Markdown 继续；B. 需要，同步到 Zoon 供团队在线修改。`
    - If the user chooses B, use `PMW_ZOON_SYNC_ON_BRIEF=true PMW_ZOON_AUTO_CREATE=true pmw-log brief <name>` or `pmw-zoon create --title "产品设计简报：<功能名>"`, then store the local audit copy and Zoon URL.
    - After create or append succeeds, `pmw-zoon` must automatically join the Zoon document as `pmworkspace` via the agent presence API before opening the editable URL or marking the online source ready.
    - After a create or append succeeds, automatically open the editable Zoon URL in the Codex built-in browser when browser tools are available. Do not use HTML, local files, or a macOS default-browser fallback as a substitute for the Zoon online brief.
    - If browser opening fails, still return the editable URL and mark the open status as `打开失败，可手动打开`.
    - Do not leave the Zoon field as a passive uncreated state. If Zoon is disabled or creation fails, write `未启用（原因）` or `创建失败（原因）`.

## Alignment Rule

只有“已对齐”的产品简报才能进入图片提示词。用户未确认时，标记为“待确认”，并在生成原型前停止。未完成前提确认或关键 D 拍板时，确认状态不能写成“已对齐”。如果页面需要线上参考但状态是“缺失待补充”，确认状态不能写成“已对齐”。

如果产品简述控制器显示 `缺失门槛`、`策略决策写入：未完成`、`Zoon 漂移检查：有实质变化` 或 `事实/假设边界` 不清，确认状态不能写成“已对齐”，也不能进入 `$pm-prototype-shotgun` 或 `$pm-handoff`。

产品简报不是“已对齐”时，不写 image-2 提示词，不生成图片，不生成 HTML，不输出交付稿。

数据佐证不是绝对阻断，但必须检查并写入边界。有数据时登记 `data_evidence`；没有数据时产品简报要写 `数据佐证：未提供，本方案存在未验证风险`，并在 `风险 / 待验证` 与不可虚构项中禁止确定性承诺、真实验证过的数值或无法兑现的数据能力。

用户在沟通过程中调整产品简报后，必须重新运行 `pmw-log brief <name>` 更新本地业务简报和完整审计副本；只有已启用 Zoon 或用户再次选择同步时，才把业务简报版同步到 Zoon。不能只在对话中更新口径。

## 输出

Return the smallest useful product-manager brief. 用户可见第一屏只放业务简报，不放工作流字段、仪表盘表格、产物流动或本地路径；默认输出 `产品简报`、`当前需要确认` 和必要的 `下一步`，不得输出 `产品简报门槛`、`支持信息`、run_id、Zoon 状态、产物流动或已保存资产：

```text
产品简述 / 产品简报：
- 产品作业卡：
  - 已知事实：
  - 暂定判断：
  - 证据边界：
  - 当前主阻断：
  - 关键缺口队列：
  - PMW 产品建议：
  - PMW 信息架构建议：
  - 用户作业：
  - 补齐后解锁：
- 真实问题：
- PM 判断摘要：
- 产品判断对抗校验：
  - 我担心的想当然：
  - 可能的理解偏差：
  - 证据不足处：
  - 需要降级为假设的判断：
  - 处理动作：
- 证据状态：
- 目标用户：
- 当前替代 / 损失：
- 选中路径：
- 范围模式：
- 本周期验证：
- 主目标：
- 反指标：
- 不可虚构项：
- 原型范围：
- 待验证项与产品作业：

当前需要确认：
- 无 / Q：... / D：...
```

内部审计必须继续记录产品简报门槛、事实/假设边界、Zoon 同步、漂移检查、准备度 verdict、产物流动和已保存资产；只有用户要求看状态或调试时才展开。

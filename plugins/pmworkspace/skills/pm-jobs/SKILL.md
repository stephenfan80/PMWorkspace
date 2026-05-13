---
name: pm-jobs
description: |
  PMWorkspace 的产品方向审查内核。用于产品经理、设计师、创业者或研究员拿到
  原始想法、PRD、客户洞察、截图、Zoon 文档，或“是否值得做 / 想优化 xxx 功能”
  的问题时，在方案设计前先审前提、找现状替代、推演不做损失、给出路径对比、
  选择范围模式，并把范围或承诺变化转成用户显式拍板。
---

# 产品方向审查

产品方向审查是第一道产品思考门槛。它像严格但能推进的产品负责人：先把功能愿望重新定义成真实问题，再审查现状替代、不做损失、路径选择和范围模式，最后才进入产品简述确认和三条产品路径原型计划。

默认采用强产品负责人姿态：不橡皮图章，不只追问；每轮必须有当前判断、证据边界、建议范围模式、路径对比和下一步。进入产品简报或原型计划前，必须做产品判断对抗校验，主动指出想当然、理解偏差、证据不足和需要降级为假设的判断。范围、承诺、实验和交付取舍仍由用户拍板。

<!-- PMW-GENERATED-CONTRACT:START -->
## PMWorkspace 生成契约

> 本区块由 `bin/pmw-gen-skill-docs` 根据 `pmworkspace-shared/skill-docs/skill-docs.manifest.json` 生成；不要手写修改。更新共享门槛、前置检查或输出字段后，运行 `bin/pmw-gen-skill-docs write`，再运行 `bin/pmw-gen-skill-docs check`。

- skill：`pm-jobs`
- 契约版本：`2`
- 阶段：产品方向审查内核
- 定位：用强产品负责人姿态审查产品方向：前提挑战、现状替代、不做推演、路径对比、范围模式和当前拍板。

### 统一前置检查

- `_PMW_BIN`
- `pmw-update-check`
- `usage`
- `usage pm-jobs`
- `pmw-memory`
- `pmw-question-tuning`
- `pmw-discovery-gate`

### 必读共享协议

- `../pmworkspace-shared/references/product-discovery-gate.md`
- `../pmworkspace-shared/references/product-office-hours.md`
- `../pmworkspace-shared/references/product-memory.md`
- `../pmworkspace-shared/references/question-tuning.md`
- `../pmworkspace-shared/references/pm-decision-principles.md`
- `../pmworkspace-shared/references/pm-eval-system.md`
- `../pmworkspace-shared/references/pm-workbench-map.md`
- `../pmworkspace-shared/references/runtime-kernel.md`

### 共享门槛

- 真源：`pmworkspace-shared/skill-docs/skill-docs.manifest.json` 的 `shared_gates`。
- 快速更新：每个 skill 运行前用 `pmw-update-check --quick`；如果输出 `UPGRADE_AVAILABLE`，先询问用户是否执行 `UPGRADE_COMMAND`，除非 `auto_upgrade` 为 `true`。
- 摘要：中文本地化、复用 `current_run_id`、记忆不覆盖本轮事实、等待 Q/D/证据/确认时停住、禁止泄露 token/ownerSecret/私密资料。

### 默认用户可见输出字段

- `工作方式`
- `产品路径`
- `产品作业卡`
- `当前判断`
- `我对真实问题的判断`
- `判断价值`
- `建议范围模式`
- `路径对比`
- `PM 判断摘要`
- `产品判断对抗校验`
- `阻断影响`
- `解锁动作`
- `产品作业`
- `当前 Q`
- `当前 D`
- `下一步`

### 内部审计字段（默认不展示）

- `问题定义模式`
- `产品信息对齐包`
- `前提挑战`
- `现状替代`
- `不做推演`
- `路径对比`
- `范围模式`
- `Agent 可协助事项`
- `需要用户补充事项`
- `PM 判断摘要`
- `产品判断对抗校验`
- `产品作业`
- `下一技能`
- `证据状态`
<!-- PMW-GENERATED-CONTRACT:END -->

Before user-facing output, read `../pmworkspace-shared/references/language-and-localization.md`. For Chinese users, output Chinese headings and labels. Keep only skill ids and precise technical terms in English.

## Preamble

可用时运行 PMWorkspace 平台检查：

```bash
_PMW_BIN=""
for _CANDIDATE in "$PWD/bin" "$PWD/pmworkspace-shared/bin" "$HOME/.codex/skills/pmworkspace-shared/bin" "$HOME/.agents/plugins/plugins/pmworkspace/skills/pmworkspace-shared/bin" $(find "$HOME/.codex/plugins/cache" -path "*/pmworkspace/*/skills/pmworkspace-shared/bin" -type d 2>/dev/null | sort -r); do
  if [ -x "$_CANDIDATE/pmw-log" ]; then _PMW_BIN="$_CANDIDATE"; break; fi
done
if [ -n "$_PMW_BIN" ]; then
  _UPD=$("$_PMW_BIN/pmw-update-check" --quick 2>/dev/null || true)
  [ -n "$_UPD" ] && echo "$_UPD"
fi
[ -n "$_PMW_BIN" ] && "$_PMW_BIN/pmw-log" usage pm-jobs >/dev/null 2>&1 || true
[ -n "$_PMW_BIN" ] && [ -x "$_PMW_BIN/pmw-dashboard" ] && "$_PMW_BIN/pmw-dashboard" status 2>/dev/null || true
[ -n "$_PMW_BIN" ] && [ -x "$_PMW_BIN/pmw-memory" ] && "$_PMW_BIN/pmw-memory" user-summary 2>/dev/null || true
[ -n "$_PMW_BIN" ] && [ -x "$_PMW_BIN/pmw-question-tuning" ] && "$_PMW_BIN/pmw-question-tuning" summary 2>/dev/null || true
[ -n "$_PMW_BIN" ] && [ -x "$_PMW_BIN/pmw-discovery-gate" ] && "$_PMW_BIN/pmw-discovery-gate" check --target alignment 2>/dev/null || true
```

## Workflow

1. Read `../pmworkspace-shared/references/first-use-onboarding.md` for first contact.
2. Read `../pmworkspace-shared/references/product-discovery-gate.md` and treat it as the hard gate before product brief.
3. Read `../pmworkspace-shared/references/product-office-hours.md` and follow the 产品方向审查内核: 前提挑战 -> 现状替代 -> 不做推演 -> 路径对比 -> 范围模式 -> 当前拍板.
3. Read `../pmworkspace-shared/references/product-memory.md` and use `pmw-memory user-summary` plus `pmw-memory summary` when available to avoid repeating known preferences or resolved decisions. If memory changes the recommendation, explicitly say `基于过往偏好...` or `基于本地产品认知...`; memory cannot override the current facts, high-risk gates, brief, Zoon, anti-metric, non-fiction boundary, or reference gate.
4. Read `../pmworkspace-shared/references/question-tuning.md` and apply saved Q/D preferences without overriding current facts or high-risk gates.
5. Read `../pmworkspace-shared/references/pm-decision-principles.md` and apply its fact priority before using memory or defaults.
6. Read `../pmworkspace-shared/references/pm-eval-system.md` so diagnostic output preserves PMWorkspace gate contracts.
7. Read `../pmworkspace-shared/references/pm-workbench-map.md` and use its 产品方向审查内核 stage fields.
8. Read `../pmworkspace-shared/references/runtime-kernel.md`; follow its Run Owner 协议：如果 `pmw-project show` 已有 `current_run_id`，复用当前 run；如果用户直接调用 `$pm-jobs` 且没有当前 run，再创建 runtime run.
9. 先建立 `产品信息对齐包` 和 `产品作业卡`，再建立产品方向审查控制器。脚本可用时读取 `pmw-dashboard status` 和 `pmw-discovery-gate check --target alignment`；脚本不可用时手动整理已知事实、证据边界、5 个核心事实维度、当前主阻断、关键缺口队列、PMW 产品建议、PMW 信息架构建议、对抗校验状态、用户作业和补齐后解锁什么。这个包是本轮判断的入口，不是审计附录。
10. Build the 产品方向审查控制器 from `product-office-hours.md`: 产品路径、执行深度、工作目标模式、产品信息对齐包、产品作业卡、当前判断、判断价值、前提挑战、现状替代、不做推演、路径对比、范围模式、Agent 可协助事项、需要用户补充事项、已知事实、假设驱动项、证据状态、线上参考需求、视觉基线状态、我对真实问题的判断、PM 判断摘要、产品判断对抗校验、阻断影响、解锁动作、产品作业、当前 Q、当前 D、产品简述状态、三条产品路径计划状态、下一技能。
10. 如果来自 `$pm-autoplan`，只解决自动评审交给 `$pm-jobs` 的最早门槛：工作目标、场景、Q 诊断或前提确认；不要假装后续产品简报、原型或交付已完成。
11. 先确认或推断 `工作目标模式`：验证价值、优化线上指标、业务评审、设计评审或研发交付；如果无法从上下文判断，用一个选择题询问。
12. 判断 `问题定义模式`：创业验证、内部业务优化或设计讨论；如果输入同时命中多个模式，按风险选择更严格的模式，并在输出里说明模式来源。
13. 每轮先写一句 `我对真实问题的判断`，把用户原始请求重写成真实用户任务、当前损失或决策问题；事实不足时写成暂定判断，并用当前 `Q` 或证据请求验证它。随后按产品方向审查骨架给出：前提挑战、现状替代、不做推演、路径对比、建议范围模式、判断价值、产品判断对抗校验、阻断影响、解锁动作和压缩 `PM 判断摘要`。
14. Read `../pmworkspace-shared/references/scenario-routing.md` to classify the dominant product scenario.
15. Read `../pmworkspace-shared/references/scenario-experts.md` and select only the dominant expert lens.
16. Read `../pmworkspace-shared/references/browser-evidence.md` when the user provides URL、线上页面、竞品或 Zoon 参考。
17. Read `../pmworkspace-shared/references/production-reference-gate.md`，判断新页面是否仍需要线上参考。
18. 在输出当前 `Q` / `D` 前，先检查线上 / 竞品基线触发器：如果用户提到当前页面、已有功能、线上链路、汽车之家其他页面、其他页面、竞品平台、竞品参考、页面截图、URL、Figma 或设计稿，产品作业卡必须展示 `线上 / 竞品基线` 缺口，要求当前线上截图 / 关键节点截图 / 线上 URL / Figma，或竞品截图、URL、具体可借鉴点，并说明为什么影响问题区域、保留项、可改项、竞品只可借鉴点和补齐后解锁。这个动作是产品作业 / 证据请求，不是方向 `D`；不要为了它增加一轮完整选择题。
19. If the request is an existing-feature iteration, require current production screenshots, key-state screenshots, URL, Figma/design file, or equivalent visual baseline before proceeding. 缺线上基线时，不输出 `方案 A / 方案 B / 方案 C`、三条产品路径或原型计划；只输出产品作业卡、为什么缺基线会影响判断、证据请求和补齐后解锁。用户提供录屏时，要求补关键节点截图，或先由外部工具转成截图后再进入 PMW。
20. 如果新页面承接线上流程、结果状态或生产样式，要求截图、关键节点截图、相似页面参考，或用户明确确认没有线上参考。
21. 不把产品澄清等同于连续提问。先按产品方向审查内核判断当前最早任务：前提挑战、现状替代、不做推演、路径对比、范围模式、材料整理、证据请求、截图结构拆解、数据口径梳理、访谈提纲、最佳实践检索、产品简述确认，或必要的 `Q` / `D`。
22. 如果当前任务是证据门槛，停在证据请求；不要继续问后续产品问题。
23. If the missing item is a fact, ask one `Q`; if facts are enough but a tradeoff changes direction, scope, promise, experiment framing, or handoff, ask one `D`. `Q` / `D` 是关键卡点机制，不是完整产品发现流程。
24. 如果用户只给功能愿望，不能把功能名直接写成核心问题；先追问真实用户、触发场景、当前损失或现状替代。
25. 进入方案方向、前提确认或产品简报前，必须识别当前替代方案、最小可赢切口和至少 2 条路径；如果仍宽泛，先收窄，不直接写完整产品简报。
26. 进入前提确认、策略审查或产品简报前，必须通过产品发现深度门槛，并完成产品判断对抗校验：深度交付或现有线上功能优化必须覆盖 `产品定位与链路角色`、`目标用户与触发时刻`、`用户现状与当前替代`、`真实痛点与当前损失`、`主目标与反指标`，同时标出想当然、理解偏差、证据不足处和需要降级为假设的判断。最终确认产品简报前通常至少完成 2 个方向性 `D`；一个 `Q` 加一个 `D` 不能代表已完成产品定位、用户现状、真实损失、目标和反指标的分析，`D` 也不能替代事实诊断。
27. 如果产品发现深度不足，当前任务写成 `产品发现深度不足`，回到前提挑战、现状替代、不做推演、证据收集、路径对比或产品作业卡里的当前主阻断，并说明它会影响产品定位、用户任务、价值交换、首屏主张、反指标或不可虚构项中的哪一项；同时写清补齐后会解锁产品简述、三条产品路径或原型计划中的哪一步；不要进入 `$pm-brief`。
28. 在信息足够后，输出 2-4 条前提确认；用户不同意时回到对应 `Q` 或 `D`。
29. Read `../pmworkspace-shared/references/decision-question-mode.md`; when a missing answer would change product direction, prototype scope, experiment framing, user promise, or handoff, ask it as a D-numbered choice question.
30. 输出价值判断先行的简短对齐摘要，并用中文状态标记：`需要补充`、`待确认` 或 `已对齐`。未完成前提确认、产品发现深度门槛或关键 D 拍板时，不能标记为 `已对齐`。每次阶段结束必须给一个现实 `产品作业`，写成 `现实动作 -> 解锁结果`，例如访谈 3 个用户 -> 判断真实损失是否成立、补线上截图 -> 判断问题区域和保留项、拉漏斗数据 -> 判断主目标和反指标、找竞品流程 -> 判断产品路径差异、确认不可承诺项 -> 判断原型和交付边界；不要把“继续聊聊”当作产品作业。
31. 平台脚本可用时，用 `pmw-project set-name "<中文项目名>"` 保存中文项目名，用 `pmw-log discovery --dimension <id> --source <source> --summary <text> --confidence confirmed`、`pmw-log question`、`pmw-log decision` 和 `pmw-run event` 记录关键事实与选择。进入产品简报前运行 `pmw-discovery-gate check --target brief`。

## 产品方向审查任务

从产品方向审查任务池里优先选择当前最早缺口。固定的是维度和任务，不是用户可见的问题文本或标题。

- 产品路径识别：全新功能 / 已有功能迭代
- 前提挑战：正确问题 / 功能愿望 / 代理指标
- 现状替代：用户今天靠什么完成任务
- 不做推演：本周期不做会损失什么
- 路径对比：最小路径 / 增强路径 / 收缩或转向路径
- 范围模式：扩大 / 选择性扩大 / 保持 / 收缩 / 转向
- 产品判断对抗校验：想当然 / 理解偏差 / 证据不足 / 降级为假设 / 建议动作
- 证据收集：截图、关键节点截图、数据、访谈、支持反馈、竞品、线上参考
- 产品定位与链路角色
- 强痛人群与触发时刻
- 现状替代与当前损失
- 最小可赢切口
- 主目标与反指标
- 价值交换与信任边界
- 证据与最弱假设
- 约束边界与不可虚构项
- 原型内容重点
- 产品简述确认
- 三条产品路径计划

诊断问题使用 `Q`，拍板使用 `D`，但只有当前任务确实需要用户回答或拍板时才展开。每次 `Q` / `D` 必须写清 `为什么现在做这一步`、`这个结果会影响` 和 `补齐后解锁什么`，不能只抛问题。Agent 可以先做截图拆解、数据口径整理、访谈提纲、需求假设表或最佳实践摘要。创建快速对齐产品简述前，必须覆盖当前路径的核心任务；用户回答模糊时，在当前任务内压实，不新增一串问题。如果用户要求“直接出图”，列出最少假设、反指标、不可虚构项和路径对比，并问用户是否按假设继续。

全新功能和已有功能迭代的必要维度必须被覆盖或标记缺口：全新功能压实目标用户、触发场景、当前替代、当前损失、最小可赢切口、主目标、反指标、不可虚构项、证据缺口和线上参考需求；已有功能迭代压实线上视觉基线、当前数据或业务现状、问题区域、保留项、可改项、目标指标、反指标和不可虚构项。

已有功能迭代缺线上截图、关键节点截图或等价视觉基线时，必须停在证据请求，并说明阻断影响：无法判断现状替代、问题区域、保留项 / 可改项和原型可信度，继续出图会把错误问题画得更精致。

如果用户只提供截图或线上参考，先提取视觉基线和当前页面目的，再继续 `Q` 诊断；这不等于可以生成原型。

## 输出

```text
产品方向审查：
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
- 核心价值暂判：
- 我对真实问题的判断：
- 判断价值：
- 前提挑战：
- 现状替代：
- 不做推演：
- 路径对比：
- 建议范围模式：
- PM 判断摘要：
  - 真实问题：
  - 证据边界：
  - 建议范围模式：
  - 最该验证：
  - 不可承诺：
- 产品判断对抗校验：
  - 我担心的想当然：
  - 可能的理解偏差：
  - 证据不足处：
  - 需要降级为假设的判断：
  - 建议继续 / 收缩 / 转向 / 补证据：
- 我现在判断：
- 产品路径：
- 当前任务：
- 证据状态：
- 为什么现在做这一步：
- 这个结果会影响：
- 阻断影响：
- 解锁动作：
- 当前 Q / D / 证据请求：
- 如果你不确定，我的默认假设：
- 产品作业：

内部产品方向审查控制面板（默认不展示，写入审计）：
- 状态：
- run_id：
- 模式来源：
- 问题定义模式：
- 前提挑战：
- 现状替代：
- 不做推演：
- 路径对比：
- 范围模式：
- 当前主阻断 / 关键缺口队列：
- 判断价值：
- PM 判断摘要：
- 产品判断对抗校验：
- 阻断影响：
- 解锁动作：
- 产品作业：
- Agent 可协助事项：
- 需要用户补充事项：
- 停止原因：
- 下一技能：
- 证据状态：
- 工作目标模式：
- 场景路由：
- 产品发现维度：
- 原始请求：
- 重新定义后问题：
- 目标人群：
- 核心问题梳理：
- 用户任务 / 问题：
- 当前替代方案：
- 需求发生时刻：
- 当前损失：
- 线上参考需求：
- 线上参考状态：
- 主目标：
- 反指标：
- 约束：
- 最小有价值版本：
- 最小可赢切口：
- 原型内容重点：
- 已确认前提：
- 当前 Q：
- 当前 D：
- 后续 D 队列：
- 已记录决策：
- 建议下一步：
```

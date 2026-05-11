# PMWorkspace 端到端工作台地图

本文件是 PMWorkspace 的全链路地图。它把 README 的产品叙事、`routing.md` 的下一技能选择、`pm-eval-system.md` 的 fixture 分类，以及各技能输出的状态字段统一到同一张表里。

使用优先级：

1. `routing.md` 仍是路由唯一真源。
2. 本文件是链路阶段、状态字段和 eval 分类真源。
3. 各技能自己的 controller 文档负责阶段内细节。

## 端到端链路

### 0. 欢迎与产品路径路由 — `$pm-workspace`

- 职责：先判断 `全新功能` 或 `已有功能迭代`，再由 Agent 根据风险、证据和交付目标判定快速成型或深度交付，并创建 / 复用 run。
- 输入：用户任务、输入材料、风险信号、当前 run。
- 硬门槛：产品路径不清、风险冲突或输入不足时必须停在路径/证据卡点；用户必须看见产品路径、执行深度、当前任务和只需完成的一步。
- 输出：路由结果，进入最早缺失技能。
- 代表 eval：`pm-workspace-entry`、`pm-workspace-routing`、`pm-workspace-runtime`。

### 1. 自动产品评审 — `$pm-autoplan`

- 职责：以靠谱产品负责人姿态串联推荐链路，但只推进到最早可靠门槛。
- 输入：D0 模式、用户目标、现有 brief / Zoon / run 证据。
- 硬门槛：快速成型遇到生产流程、高风险承诺、真实数据、线索 / 交易 / 隐私或交付信号时升级深度交付；每轮必须告诉用户当前一步和下一步。
- 输出：轻量包假设确认，或带交接上下文交给下一个技能。
- 代表 eval：`autoplan`、`quick-shaping`、`deep-delivery`。

### 2. 产品方向审查内核 — `$pm-jobs`

- 职责：用强产品负责人姿态推进产品方向审查内核：前提挑战、现状替代、不做推演、路径对比、范围模式和当前拍板；每轮必须有当前判断、证据边界、建议范围模式、路径对比、PM 判断摘要和产品作业。
- 输入：产品定位、用户、触发时刻、现状替代、当前损失、目标、反指标、价值交换、约束、线上参考状态。
- 硬门槛：全新功能必须补齐目标用户、触发场景、当前替代、当前损失、最小可赢切口、主目标、反指标、不可虚构项和线上参考需求；已有功能迭代缺截图/录屏或等价视觉基线时不能进入原型计划；不能用一个 Q + 一个 D 直接进入产品简述确认；范围变化必须进入一个当前 D。
- 输出：材料整理、证据请求、访谈/数据建议、PM 判断摘要、产品作业、路径对比、前提确认，或交给产品方向审查 / 产品简报。
- 代表 eval：`pm-jobs`。

### 3. 产品方向审查 — `$pm-strategy-review`

- 职责：先做前提挑战、现状替代、不做推演和路径对比，再用扩大、选择性扩大、保持、收缩或转向五种范围模式判断方向，并把 `最大策略矛盾` 转成 PM 取舍。
- 输入：`$pm-jobs` 交出的事实、风险门槛、反指标、不可虚构项。
- 硬门槛：基础事实缺失退回 `$pm-jobs`；进入范围模式前必须给 2-3 条路径；改变范围 / 承诺 / 实验 / 交付责任时只问一个 `D`；每个审查发现必须落成产品动作；不能省略范围模式。
- 输出：已拍板策略、选中路径、范围模式和本周期验证写入产品简报。
- 代表 eval：`pm-strategy-review`。

### 4. 产品简报 — `$pm-brief`

- 职责：写成短版产品简述 / 产品简报并固化出图前门槛，先讲清真实问题、PM 判断摘要、证据状态、目标用户、当前替代/损失、选中路径、范围模式、本周期验证、主目标、反指标、不可虚构项、原型范围、产品作业和待验证项。
- 输入：上游 Q/D、产品发现深度、已确认前提、策略决策、Zoon 最新内容、线上参考 / `browser_evidence`、轻量检索。
- 硬门槛：未完成产品发现深度、前提确认、关键 D、线上参考或 Zoon 漂移时不能标为 `已对齐`；缺事实不能用简报补写。
- 输出：`product_brief` 登记到产物流动，确认后进入三条产品路径原型或交付。
- 代表 eval：`pm-brief`、`artifact-flow`。

### 5. 原型方案 — `$pm-prototype-shotgun`

- 职责：作为 image-2 原型出图导演，基于已对齐 brief 默认规划最少 3 条产品路径，并逐张生成每个方案 / 屏幕独立设计稿。
- 输入：已对齐 brief、Zoon 快照、线上参考、视觉基线、设计系统、prototype-board、Product Readiness Dashboard、`product_brief` 产物流动。
- 硬门槛：readiness verdict 不是 `可出图`、brief 未已对齐、Zoon 实质漂移、线上参考缺失、视觉基线缺目标像素、线上截图下输出单元未锁定物理长板、产品路径少于 3 条且无豁免、方案只换皮、缺产品路径/原型思考、缺原型设计完整度判断或 image-2 不可用时，不能写提示词或替代出图；一次 image-2 调用只能生成一张图、一个产品路径和一个屏幕任务。
- 输出：`prototype_manifest` 登记到产物流动，状态 `可进入原型复审`。
- 代表 eval：`pm-prototype-shotgun`、`prototype-shotgun`、`prototype-output-contract`、`multi-scheme`、`production-reference`、`screenshot-feedback`、`artifact-flow`。

### 6. 原型复审 — `$pm-prototype-review`

- 职责：判断图片是否可通过、需要重出、需要 PM 拍板或补参考，并把用户反馈资产化。
- 输入：原型图片、输出单元绑定、brief、Zoon、线上参考、设计系统、PM Review Army / Product Review Squad、可插拔复审专家、用户全局记忆、`prototype_manifest` 产物流动。
- 硬门槛：缺绑定不能凭视觉通过；策略、信任 / 风险、设计系统、数据可行性四个专家必须独立输出短结论；违反 brief / 反指标 / 不可虚构 / 线上参考 / 设计系统 / 10/10 原型标准或出现明显 AI 模板味时必须重出；产品承诺未决必须拍板；深度交付、高风险、批量交付、研发交付或多角色 review 必须输出 CEO、Eng、Design、DX、安全、QA、发布工程师短结论。
- 输出：`prototype_review` 或 `repair_brief` 登记到产物流动；专家短结论写入本地 review-specialists 资产；个人偏好、产品认知或 PMWorkspace 进化候选写入本地资产。
- 代表 eval：`prototype-review`、`review-specialists`、`artifact-flow`。

### 7. 产品交付 — `$pm-handoff`

- 职责：作为产品设计文档 / 精简 PRD 交付官，把已通过复审的方向整理成最终产品设计文档或最小交付契约，并沉淀接口 / 数据 / 埋点 / 实验资产。
- 输入：已对齐 brief、已选原型、复审结论、D 决策、线上参考、Product Readiness Dashboard、现成 PRD / 接口 / 埋点 / 实验文档、本地交付资产、`product_brief` / `prototype_review` 产物流动。
- 硬门槛：readiness verdict 不是 `可交付`、未复审、研发可行性反问未完成、关键 D 未拍板时不交付；产品设计文档必须包含产品判断演进；单功能只写 1-2 周本周期承诺；不可虚构项和未验证数据不能写成验收；普通接口 / 数据 / 埋点 / 实验缺口可留空为待补充，不能虚构。
- 输出：`product_design_doc`、`handoff`、`acceptance_seed` 或 `release_doc_seed` 登记到产物流动，状态 `可交付`；功能能力与研发依赖、接口、数据、埋点和实验标准写入本地脱敏交付资产。
- 代表 eval：`pm-handoff`、`artifact-flow`。

### 8. 运行、产物流动与记忆 — 共享脚本

- 职责：保存可审计状态，复用偏好但不覆盖事实，并把上游产物交给下游技能。
- 输入：`pmw-run`、`pmw-dashboard`、`pmw-prototype-board`、`pmw-artifact`、`pmw-memory`、`pmw-log`。
- 硬门槛：历史偏好不能覆盖本轮 brief、Zoon、反指标、不可虚构项或当前门槛；下游不能绕过缺失的上游产物。
- 输出：本地审计轨迹、产物流动清单、偏好、学习和 eval 结果。
- 代表 eval：`memory`、`decision-principles`、`eval-system`、`artifact-flow`。

## 共享状态字段

这些字段是内部审计和下游交接字段，默认写入 `pmw-run`、`pmw-dashboard --details`、`pmw-artifact` 或本地审计副本；不要默认展示给用户。默认用户可见输出只保留业务判断、当前需要确认、已生成产物和下一步。阶段字段可以追加，但不能省掉当前阶段的门槛与证据记录：

```text
- run_id：
- 模式 / 当前模式：
- 状态：
- 当前门槛 / 最早门槛：
- 产品路径：
- 执行深度：
- 前提挑战：
- 现状替代：
- 不做推演：
- 路径对比：
- 范围模式：
- 当前价值缺口 / 当前最大缺口：
- 下一技能：
- 证据状态：
- 当前 Q：
- 当前 D：
- 已记录决策：
- PM 判断摘要：
- 产品作业：
- 产物清单 / 已保存资产：
- 产物流动：
- 上游产物：
- 本轮产物：
- 下游可读：
- 建议下一步：
```

证据状态至少说明：

- 产品简报：未创建 / 草稿 / 待确认 / 已对齐 / 有漂移。
- Zoon：未启用 / 无 URL / 已同步 / 同步失败 / 有漂移 / 读取失败。未启用时使用本地已对齐产品简报，不阻断出图或交付。
- 线上参考：已提供线上参考 / 无线上参考已确认 / 缺失待补充 / 不适用。
- 浏览器证据：无 / 已采集 / 读取失败 / 待补充；作为 `browser_evidence` 产物进入 Product Artifact Flow。
- 原型清单：未生成 / 已登记 / 已生成 / 已复审 / 需重出。
- 用户全局记忆：暂无 / 已读取 / 已应用并明示来源 / 有 GitHub 回流待审稿。
- 本地交付资产：暂无 / 已读取 / 已应用并明示来源 / 已新增。
- 待决策项：无 / 当前 Q / 当前 D / 后续 D 队列。
- 不可虚构项：未定义 / 已定义 / 有违规。
- 交付资产：未生成 / 已保存 handoff / 已保存交付事实 / 不适用。
- 产品准备度仪表盘：未运行 / 不可出图 / 可出图 / 不可交付 / 可交付。
- 产物流动：未记录 / 已记录 / 下游可读 / 有断点。

## 状态值地图

统一状态来自 `runtime-kernel.md`，各阶段可以在行动结论里使用更细状态：

- `需要补充`：缺少会改变方向或交付质量的事实、参考或证据。
- `待确认`：已有假设、前提或推荐，需要用户确认。
- `需要 PM 拍板`：存在会改变承诺、范围、数据真实性、实验口径、线索/交易/隐私/合规或验收的取舍。
- `基于假设，可讨论`：快速成型轻量包可讨论，但不是最终 PRD 或已验证事实。
- `已对齐`：产品简报、关键前提或最新 Zoon 已确认。
- `可进入原型复审`：已生成独立原型图片，需要复审。
- `需要补充参考`：缺少线上截图、设计系统、输出单元绑定或真实数据边界。
- `需要重出`：图片违反 brief、反指标、不可虚构项、线上参考或设计系统。
- `可通过`：原型复审通过，可进入交付。
- `可交付`：交付前门槛全部通过，交付稿可以保存并交给下一团队。

## Eval 分类地图

`pmw-eval` 的 fixture `category` 必须能映射回链路阶段：

| Eval 分类 | 对应阶段 | 主要守住什么 |
|---|---|---|
| `pm-workspace-entry`、`pm-workspace-routing`、`pm-workspace-runtime` | 欢迎与 D0 路由 | 欢迎页、D0、路由输出契约、run owner |
| `autoplan`、`quick-shaping`、`deep-delivery` | 自动产品评审 | 自动推进、风险升级、最早门槛、终态 finish |
| `pm-jobs` | 产品方向审查内核 | 前提挑战、现状替代、不做推演、路径对比、范围模式、PM 判断摘要、产品作业、上游门槛接力 |
| `pm-strategy-review` | 产品方向审查 | 策略结论先行、路径对比、范围模式、最大策略矛盾、产品动作、缺事实退回、一个策略 D |
| `pm-brief` | 产品简报 | 产品简述 / 产品简报、真实问题、证据状态、目标用户、当前替代/损失、选中路径、范围模式、本周期验证、待验证项、Zoon 漂移、已对齐门槛、进入原型/交付 |
| `pm-prototype-shotgun`、`prototype-shotgun`、`prototype-output-contract`、`multi-scheme`、`production-reference`、`screenshot-feedback` | 原型方案 | image-2 前门槛、单图生成协议、默认最少 3 条产品路径、方案差异质量、原型思考、输出单元、线上参考、设计系统 |
| `prototype-review` | 原型复审 | 复审控制器、重出、PM 拍板、偏好边界 |
| `review-specialists` | 原型复审 | 四个可插拔专家独立短结论、最高严重度合并、`pmw-review-specialist` 可追踪 |
| `pm-handoff` | 产品交付 | 产品设计文档、精简 PRD 核心字段、现成文档入口、未复审不交付、未拍板不写验收、缺口留空、保存 handoff / product_design_doc 和交付事实 |
| `readiness-dashboard` | 原型方案 / 产品交付 / 运行与记忆 | 出图 / 交付前 Product Readiness Dashboard 和 verdict |
| `artifact-flow` | 产品简报 / 原型方案 / 原型复审 / 产品交付 / 运行与记忆 | 上游产物可被下游读取，brief、prototype manifest、review、product_design_doc、handoff 和 `browser_evidence` 不在对话中断流 |
| `skill-doc-generator` | 运行与记忆 | `pmw-gen-skill-docs` 用 manifest 生成并检查 SKILL.md 共享契约，防止 preamble、输出字段和共享门槛漂移 |
| `memory`、`decision-principles`、`eval-system` | 运行与记忆 | 偏好不覆盖事实、eval runner 可用、维护契约 |

新增 fixture 时，先把它放入上表已有分类；如果确实出现新阶段，必须同步更新本文件、`pm-eval-system.md` 和 `evals/README.md`。

## 链路收口规则

- README 只讲产品体验和入口，不维护第二套路由表；它应链接或摘录本地图。
- `routing.md` 只决定下一技能和 D0，不重复展开每个技能的完整 controller。
- `pm-eval-system.md` 只维护测试分层、fixture 结构和分类地图，不复制技能全文。
- 技能 `SKILL.md` 必须读取本文件，并在输出中保留本阶段要求的状态字段。
- 技能 `SKILL.md` 的共享契约区块由 `pmw-gen-skill-docs` 生成；修改共享 preamble、必读协议、输出字段或共享门槛时，先改 manifest，再重新生成和检查。
- 如果某个门槛失败，下一技能必须指向最早能补齐该门槛的技能；不要把下游产物伪装成已完成。

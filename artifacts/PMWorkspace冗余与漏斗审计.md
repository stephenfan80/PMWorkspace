# PMWorkspace 冗余与漏斗审计

审计日期：2026-05-09

审计口径：两阶段稳妥。第一阶段只识别明显矛盾、重复规则、低价值噪声和运行时漏斗；不直接删除 skill 或 references。第二阶段等删减决策表拍板后再执行。

执行状态更新：本审计列出的 D1-D17 已完成第一轮保守瘦身。已修正文案冲突、收敛长板 / 简报 / eval / office-hours 真源、归档孤岛 reference，并通过 generator 收敛 `SKILL.md` 共享门槛重复。后续继续瘦身时，应重新审计 D18+，不要沿用本报告里的“待执行”旧状态。

## 总体结论

PMWorkspace 的核心运行逻辑已经形成闭环：`$pm-workspace` 路由，`$pm-autoplan` 总控，`$pm-jobs` 做产品价值判断，`$pm-brief` 生成产品经理简报，`$pm-prototype-shotgun` 负责 image-2 单图出图，`$pm-prototype-review` 复审，`$pm-handoff` 交付。真正能挡错的是运行时脚本和 eval，而不是单纯靠 skill 长文案。

当前主要风险不是“规则缺失”，而是“规则散落 + 旧文案残留 + 重复解释过多”。这会让执行模型在长上下文中优先记住旧锚点或入口摘要，出现用户指出的两类问题：产品发现只问一个 Q/D 就进入简报，或者有生产截图时仍被短画布锚定。

## A. 明显矛盾

| 编号 | 位置 | 问题 | 风险 | 建议动作 | 是否需拍板 |
|---|---|---|---|---|---|
| C1 | `README.zh-CN.md:66` | README 仍写“产品简报默认输出 12-18 行左右的业务简报”。 | 与当前 `product-plan-handoff.md:11-18` 和 `$pm-brief` 的 1-2 页 PM brief 结构冲突，用户理解会停留在短摘要。 | 改成“默认输出 1-2 页产品经理简报；快速版可压缩但必须保留核心价值、现状、用户、痛点、替代、指标和不可虚构项”。 | 是 |
| C2 | `README.zh-CN.md:110` | README 仍写“产品简报阶段默认优先创建或追加到 AI 协作文档”。 | 与 `zoon-workflow.md:1-5`、`zoon-workflow.md:49-60` 的 local-first / Zoon-optional 冲突，容易导致自动同步。 | 改成“本地 Markdown 先保存，保存后推荐 Zoon A/B，同步需用户选择”。 | 是 |

## A2. 入口措辞歧义 / 中风险

| 编号 | 位置 | 问题 | 风险 | 建议动作 | 是否需拍板 |
|---|---|---|---|---|---|
| C3 | `README.zh-CN.md:203` | “协作文档转原型：先同步最新产品简报”在 Zoon 文档场景下是合理动作，但入口文案没有说清“仅已启用 / 已提供 Zoon 时”。 | 中风险：可能被误读为所有产品简报都要先同步 Zoon，而不是 local-first。 | 改成“若已提供或已启用 Zoon，先读取最新快照并检查漂移；未启用时使用本地已对齐简报”。 | 是 |

## B. 重复规则

| 编号 | 位置 | 问题 | 风险 | 建议动作 | 是否需拍板 |
|---|---|---|---|---|---|
| R1 | `402 x 874` 出现在 12 个文件；`H874` 出现在 8 个文件 | 长板规则散落在 `pm-prototype-shotgun/SKILL.md`、`image-prompts.md`、`design-system-workflow.md`、`autohome-auto-design.md`、`pm-eval-system.md` 等处。 | 任一处出现旧写法或上下文不清，image-2 prompt 可能重新被短画布锚定。 | 保留 `image-prompts.md` 为 prompt 真源，`prototype-shotgun-board.md` 为 output unit 真源；只删重复解释，不删 `$pm-prototype-shotgun` 硬门槛、Product Readiness Dashboard 门槛、output unit 契约和 `pm-eval-system.md` 测试断言。 | 是 |
| R2 | `product-plan-handoff.md`、`product-manager-brief.md`、`pm-brief/SKILL.md`、`pm-eval-system.md` | 产品经理简报结构被重复描述。 | 维护时容易一处改成 PM brief，另一处仍像短摘要或审计合同。 | 保留 `product-manager-brief.md` 为模板真源，`product-plan-handoff.md` 只写门槛和交接，`pm-brief/SKILL.md` 只写执行流程。 | 是 |
| R3 | `product-office-hours.md`、`product-discovery-gate.md`、`pm-jobs/SKILL.md` | 产品发现维度和 Q/D 规则多处重复。 | 执行时容易把“一次只问一个”误读成“总共只问一个”。 | 保留 `product-discovery-gate.md` 为硬门槛真源；`product-office-hours.md` 主文档只保留产品发现状态机，案例、反例、口吻示例后续迁到 appendix/examples。 | 是 |
| R4 | `README.zh-CN.md`、`README.md`、`update-workflow.md` | 安装与升级命令重复出现。 | 文档维护成本高，版本更新时容易漏改。 | README 只保留快速安装和开发安装各一条，其余迁到 `docs/codex-plugin-submission.md` 或 `update-workflow.md`。 | 是 |

## C. 低价值噪声

| 编号 | 位置 | 问题 | 风险 | 建议动作 | 是否需拍板 |
|---|---|---|---|---|---|
| N1 | `pm-workbench-map.md:13-23` | 端到端链路表单行过长，单行承载目标、字段、门槛、产物、eval。 | 对模型和维护者都不友好；容易只扫到前半段，忽略不可越过门槛。 | 改成阶段卡片式结构：每阶段保留“职责 / 输入 / 硬门槛 / 输出 / eval”。 | 是 |
| N2 | `pm-eval-system.md` | 规则密度最高，关键字扫描 237 次。 | 容易变成第二套业务协议，稀释 source references 的优先级。 | 收敛为 eval 合同：保留 fixture 分类、禁止项、验收断言和失败条件；只移除重复业务长解释，不能压缩成纯链接。 | 是 |
| N3 | 各 `SKILL.md` preamble / 共享门槛 | `_PMW_BIN` 查找脚本仍在每个 skill 中重复；共享门槛长文此前也重复。 | preamble 是生成契约的一部分，不能手删；共享门槛重复会增加阅读噪声。 | 已通过 manifest / generator v2 收敛共享门槛输出，只保留真源和摘要；preamble 暂保留，不手删。 | 否，已完成低风险收敛 |
| N4 | `product-office-hours.md` | 439 行，是最长 reference，且和 discovery gate / jobs skill 有重叠。 | 对执行模型来说噪声大，重要门槛容易被案例稀释。 | 拆成“产品发现状态机主文档”和“案例 / 反例 / 口吻示例 appendix”。 | 是 |

## D. 运行时漏斗

| 编号 | 位置 | 问题 | 风险 | 建议动作 | 是否需拍板 |
|---|---|---|---|---|---|
| L1 | `$pm-jobs` 到 `$pm-brief` | 文案要求多轮 Q/D，但如果不依赖 `pmw-discovery-gate`，模型仍可能提前写简报。 | 回到“一个 Q + 一个 D 后已对齐”的失败路径。 | 已验证 `pmw-log brief` 在声明已对齐时会检查 run 确认和 `pmw-discovery-gate check --target brief`，见 `bin/pmw-log:131-147`；保持该脚本门槛。 | 否，保持现有脚本门槛 |
| L2 | `$pm-prototype-shotgun` prompt 前 | 长板规则如果只靠 prompt 文案，会被旧画布锚点稀释。 | 有截图仍生成短画布或低分辨率图。 | 保持 `pmw-prototype-prompt-check` 为出图前硬门槛；失败时不能调用 image-2。 | 否，保持现有脚本门槛 |
| L3 | 出图后展示 | 如果 image audit 失败但助手仍展示图片，用户会误认为交付成功。 | 不合格图继续流入评审或 PRD。 | 保持 `pmw-prototype-board image` 自动审计，失败写 `需要重出` 并阻断展示。 | 否，保持现有脚本门槛 |
| L4 | source skill 与 plugin 副本 | 修改 source 后如果不运行 `pmw-build-plugin`，Codex plugin 仍使用旧规则。 | 本地测试通过但线上 plugin 继续漂移。 | 把 `pmw-build-plugin` 放进发布验收 checklist，并在 PPT 中明确。 | 否，流程要求 |

## E. 可保留但应移位

| 编号 | 位置 | 当前价值 | 移位建议 | 是否需拍板 |
|---|---|---|---|---|
| M1 | `pm-eval-system.md` | 维护 eval 契约和 fixture 分类。 | 不删除；瘦身为 eval 合同，不重复展开每个业务规则。 | 是 |
| M2 | `product-office-hours.md` | 有助于产品专家式追问。 | 主文档只保留产品发现状态机，案例、反例、口吻示例移到 appendix/examples。 | 是 |
| M3 | `autohome-auto-design.md` | 汽车之家场景有用，尤其 AutoDesign 约束。 | 只保留领域差异和 token，不再重复通用长板规则。 | 是 |
| M4 | `README.zh-CN.md` | 用户入口文档。 | 保留体验叙事，删掉会变成第二套协议的细节。 | 是 |

## F. 疑似孤岛 reference

审计依据：`rg` 未发现下列文件被 source skill、README、AGENTS 或 `pmworkspace-shared/skill-docs/skill-docs.manifest.json` 明确引用。该结论只说明“入口不明确”，不等于可以删除。

执行状态更新：D13 `decision-gates.md` 和 D14 `intake.md` 已在合并有效内容后移除；D15 `product-methodology.md` 和 D16 `prompt-recipes.md` 已移到 appendix / examples；D17 `skill-doc-template-system.md` 已确认保留，因为 eval 直接断言该生成体系说明。

| 编号 | 位置 | 原始发现 | 原始风险 | 最终动作 | 当前状态 |
|---|---|---|---|---|---|
| O1 | `pmworkspace-shared/references/decision-gates.md` | 疑似未被显式引用，内容可能和 discovery / readiness 门槛重叠。 | 继续漂移会形成第三套决策门槛。 | 有效门槛语言已并入 `product-discovery-gate.md` / 相关真源，孤岛文件已移除。 | 已处理 |
| O2 | `pmworkspace-shared/references/intake.md` | 疑似未被显式引用，可能和 `$pm-workspace`、`$pm-autoplan` 的入口诊断重叠。 | 入口信息若不统一，会让“先问什么”继续分叉。 | 最小上下文字段已并入 `first-use-onboarding.md`，孤岛文件已移除。 | 已处理 |
| O3 | `pmworkspace-shared/references/product-methodology.md` | 疑似未被显式引用，可能和 `product-office-hours.md`、`product-discovery-gate.md` 重叠。 | 产品方法论解释可能稀释运行时硬门槛。 | 已移到 `pmworkspace-shared/references/appendix/product-methodology.md`，不进入运行时必读。 | 已处理 |
| O4 | `pmworkspace-shared/references/prompt-recipes.md` | 疑似未被显式引用，可能只作为历史 prompt 示例存在。 | 旧 prompt 可能重新带回过时画布或简报口径。 | 已移到 appendix / examples，并新增 `examples/prompt-recipes.md` 入口。 | 已处理 |
| O5 | `pmworkspace-shared/references/skill-doc-template-system.md` | 疑似未被显式引用，但名称显示可能与 skill-doc generator 设计有关。 | 直接删除可能误伤生成契约维护依据。 | 已确认 eval 依赖，继续保留为生成体系说明和测试契约锚点。 | 保留 |

## 执行结果

1. C1 / C2 / C3 已修正：产品简报、Zoon local-first 和协作文档入口口径已对齐。
2. 长板出图真源已收敛：`image-prompts.md` 负责 prompt 真源，`prototype-shotgun-board.md` 负责 output unit 真源，脚本 / eval 继续做硬门槛。
3. 产品简报真源已收敛：模板归 `product-manager-brief.md`，门槛归 `product-plan-handoff.md`，执行归 `$pm-brief`。
4. `pm-eval-system.md` 已收敛为测试契约，保留 fixture 分类、禁止项、验收断言和失败条件。
5. README 安装重复、`pm-workbench-map.md` 长表格、AutoDesign 长板重复和英文 README 口径已处理。
6. O1-O5 已完成归属确认和处理；继续瘦身时从新的 D18+ 审计开始。

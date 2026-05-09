# PMWorkspace 删减决策表

使用方式：每一行选择 `保留 / 合并 / 移到 reference / 删除 / 暂缓`。默认建议偏保守，先修冲突和重复真源，再做大规模瘦身。

| 编号 | 对象 | 当前问题 | 推荐选择 | 可选动作 | 影响 |
|---|---|---|---|---|---|
| D1 | `README.zh-CN.md:66` 产品简报 12-18 行口径 | 与 1-2 页 PM brief 规则冲突。 | 合并 | 改成 PM brief 入口摘要，保留快速版可压缩说明。 | 低风险，建议立即修。 |
| D2 | `README.zh-CN.md:110` Zoon 默认优先同步口径 | 与 local-first / Zoon-optional 冲突。 | 合并 | 改成“本地保存后推荐 Zoon A/B”。 | 低风险，建议立即修。 |
| D3 | `README.zh-CN.md:203` 协作文档转原型描述 | Zoon 文档场景下读取最新快照合理，但入口文案容易误导为每次都要先同步 Zoon。 | 合并 | 改成“已提供或已启用 Zoon 时读取最新快照并检查漂移；未启用用本地简报”。 | 中风险措辞澄清，不按明显矛盾处理。 |
| D4 | README 安装 / 升级命令重复 | 中英文 README 和 update reference 都有安装命令。 | 合并 | README 保留快速安装 + 开发安装；详细升级迁到 `update-workflow.md`。 | 中低风险，需确认对外文档口径。 |
| D5 | 长板规则在 12 个文件重复 | 规则正确但分散，旧锚点容易残留。 | 合并 | `image-prompts.md` 做 prompt 真源；`prototype-shotgun-board.md` 做 output unit 真源；只删重复解释，不删 `$pm-prototype-shotgun` 硬门槛、Product Readiness Dashboard 门槛、output unit 契约和 `pm-eval-system.md` 测试断言。 | 中风险，需配合 eval，避免误伤运行契约。 |
| D6 | `pm-eval-system.md` 规则密度过高 | 像第二份业务协议。 | 合并 | 保留 fixture 分类、禁止项、验收断言和失败条件；只移除重复业务长解释，不能压缩成纯链接。 | 中风险，需跑全量 eval，避免误伤测试契约。 |
| D7 | `product-office-hours.md` 过长 | 已在 references 中，问题不是“移到 reference”，而是与 discovery gate / jobs skill 重叠。 | 拆分 / 合并 | 主体保留产品发现状态机；案例、反例、口吻示例后续迁到 appendix/examples 或合并到专门示例文档。 | 中风险，需确认追问体验不变。 |
| D8 | 产品简报模板重复 | `product-manager-brief.md`、`product-plan-handoff.md`、`pm-brief/SKILL.md` 都写结构。 | 合并 | 模板真源归 `product-manager-brief.md`；交接门槛归 `product-plan-handoff.md`；skill 只写执行。 | 中风险，需更新 manifest / eval。 |
| D9 | `pm-workbench-map.md` 长表格 | 单行过长，维护者和模型都难扫。 | 合并 | 改成 8 个阶段卡片，每卡只保留职责、输入、硬门槛、输出、eval。 | 中低风险，主要是文档结构调整。 |
| D10 | 各 `SKILL.md` 生成契约重复 | preamble 和共享门槛多处重复。 | 暂缓 | 不手删；如要收敛必须先改 manifest / generator。 | 高风险，本轮不建议动。 |
| D11 | AutoDesign 与通用长板规则重复 | `autohome-auto-design.md` 既写领域 token，也重复通用画布禁令。 | 合并 | AutoDesign 只保留领域 token / 组件 / 反模式，通用长板规则引用 `image-prompts.md`。 | 中风险，需保留汽车之家特例。 |
| D12 | `README.md` 与 `README.zh-CN.md` 结构差异 | 中英文入口文档维护不完全同步。 | 暂缓 | 先修中文 README；英文 README 后续按同口径补齐。 | 低风险，可分批。 |
| D13 | `decision-gates.md` 疑似孤岛 reference | 当前未被 source skill、README、AGENTS 或 manifest 明确引用，且可能与 discovery / readiness 门槛重叠。 | 暂缓 | 执行前先确认没有插件副本、文档入口或未来 generator 依赖；确认后再合并有效内容或归档。 | 中风险，不能直接删除。 |
| D14 | `intake.md` 疑似孤岛 reference | 当前未被显式引用，可能和路由 / 入口诊断重叠。 | 暂缓 | 先确认依赖；若无依赖，把有价值的最小 intake 字段合并到入口路由文档，其余归档。 | 中风险，需防止入口诊断信息丢失。 |
| D15 | `product-methodology.md` 疑似孤岛 reference | 当前未被显式引用，可能和产品发现方法文档重叠。 | 合并 | 先确认依赖；把仍有效的方法原则合并到 discovery reference，其余归档。 | 中风险，避免方法论漂移成第二套流程。 |
| D16 | `prompt-recipes.md` 疑似孤岛 reference | 当前未被显式引用，可能保留旧 prompt 示例。 | 暂缓 | 先确认依赖并筛掉过时锚点；可复用示例迁到 appendix/examples，其余归档。 | 中风险，避免旧画布或旧简报口径回流。 |
| D17 | `skill-doc-template-system.md` 疑似孤岛 reference | 当前未被显式引用，但可能是 generator 设计依据。 | 暂缓 | 先确认 generator、manifest、插件副本和未来文档入口都无依赖，再决定合并或归档。 | 高风险，不建议直接删除。 |

## 推荐执行顺序

1. 先执行 D1-D2：修高确定性冲突，低风险高收益。
2. 同步澄清 D3：按入口措辞歧义处理，避免把 Zoon 文档场景下的快照读取误判为错误。
3. 再执行 D5-D8：收敛长板、简报、discovery、eval 的真源，但只删重复解释，不删硬门槛、运行契约或测试断言。
4. 然后执行 D4、D9、D11、D12：改善可维护性和对外文档一致性。
5. D13-D17 先做依赖确认；确认无插件副本、文档入口或未来 generator 依赖后，再决定合并或归档。
6. D10 本轮暂缓，除非决定重构 skill-doc generator。

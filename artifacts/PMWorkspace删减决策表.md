# PMWorkspace 删减决策表

使用方式：每一行选择 `保留 / 合并 / 移到 reference / 删除 / 暂缓`。默认建议偏保守，先修冲突和重复真源，再做大规模瘦身。

执行状态更新：截至 commit `9880bcd`，D1-D17 已按保守瘦身路线处理完毕；D17 明确保留，D10 已通过 manifest / generator 收敛，未手工删除生成区块。

| 编号 | 对象 | 当前问题 | 推荐选择 | 可选动作 | 影响 |
|---|---|---|---|---|---|
| D1 | `README.zh-CN.md:66` 产品简报 12-18 行口径 | 与 1-2 页 PM brief 规则冲突。 | 已合并 | 已改成 PM brief 入口摘要，保留快速版可压缩说明。 | 已修，commit `b0975ef`。 |
| D2 | `README.zh-CN.md:110` Zoon 默认优先同步口径 | 与 local-first / Zoon-optional 冲突。 | 已合并 | 已改成“本地保存后推荐 Zoon A/B”。 | 已修，commit `b0975ef`。 |
| D3 | `README.zh-CN.md:203` 协作文档转原型描述 | Zoon 文档场景下读取最新快照合理，但入口文案容易误导为每次都要先同步 Zoon。 | 已合并 | 已改成“已提供或已启用 Zoon 时读取最新快照并检查漂移；未启用用本地简报”。 | 已修，commit `b0975ef`。 |
| D4 | README 安装 / 升级命令重复 | 中英文 README 和 update reference 都有安装命令。 | 已合并 | README 保留公开插件、本地 GitHub plugin、开发安装三条主路径；详细升级迁到 `update-workflow.md`。 | 已修，commit `6dd77b6`。 |
| D5 | 长板规则在 12 个文件重复 | 规则正确但分散，旧锚点容易残留。 | 已合并 | `image-prompts.md` 做 prompt 真源；`prototype-shotgun-board.md` 做 output unit 真源；硬门槛和 eval 断言保留。 | 已修，commit `268935f`。 |
| D6 | `pm-eval-system.md` 规则密度过高 | 像第二份业务协议。 | 已合并 | 保留 fixture 分类、禁止项、验收断言和失败条件；移除重复业务长解释。 | 已修，commit `268935f`。 |
| D7 | `product-office-hours.md` 过长 | 已在 references 中，问题不是“移到 reference”，而是与 discovery gate / jobs skill 重叠。 | 已拆分 / 合并 | 主体保留产品发现状态机；案例、反例、口吻示例迁到 appendix/examples。 | 已修，commit `268935f`。 |
| D8 | 产品简报模板重复 | `product-manager-brief.md`、`product-plan-handoff.md`、`pm-brief/SKILL.md` 都写结构。 | 已合并 | 模板真源归 `product-manager-brief.md`；交接门槛归 `product-plan-handoff.md`；skill 只写执行。 | 已修，commit `268935f`。 |
| D9 | `pm-workbench-map.md` 长表格 | 单行过长，维护者和模型都难扫。 | 已合并 | 已改成 8 个阶段卡片，每卡只保留职责、输入、硬门槛、输出、eval。 | 已修，commit `6dd77b6`。 |
| D10 | 各 `SKILL.md` 生成契约重复 | preamble 和共享门槛多处重复。 | 已合并 | 已通过 manifest / generator v2 压缩 `shared_gates` 输出；完整真源仍在 manifest；新增 compact gates eval。 | 已修，commit `8328be4`，未手删生成区块。 |
| D11 | AutoDesign 与通用长板规则重复 | `autohome-auto-design.md` 既写领域 token，也重复通用画布禁令。 | 已合并 | AutoDesign 只保留领域 token / 组件 / 反模式，通用长板规则引用 `image-prompts.md`。 | 已修，commit `6dd77b6`。 |
| D12 | `README.md` 与 `README.zh-CN.md` 结构差异 | 中英文入口文档维护不完全同步。 | 已合并 | 英文 README 已按中文 README 同口径补齐产品简报、Zoon、长板和安装路径。 | 已修，commit `6dd77b6`。 |
| D13 | `decision-gates.md` 疑似孤岛 reference | 当前未被 source skill、README、AGENTS 或 manifest 明确引用，且可能与 discovery / readiness 门槛重叠。 | 已合并 / 归档 | 有效门槛语言并入 `product-discovery-gate.md` / 相关真源；孤岛文件已移除。 | 已修，commit `6ec70c1`。 |
| D14 | `intake.md` 疑似孤岛 reference | 当前未被显式引用，可能和路由 / 入口诊断重叠。 | 已合并 / 归档 | 最小 intake 字段并入 `first-use-onboarding.md`，孤岛文件已移除。 | 已修，commit `6ec70c1`。 |
| D15 | `product-methodology.md` 疑似孤岛 reference | 当前未被显式引用，可能和产品发现方法文档重叠。 | 已移位 | 已移到 `pmworkspace-shared/references/appendix/product-methodology.md`。 | 已修，commit `6ec70c1`。 |
| D16 | `prompt-recipes.md` 疑似孤岛 reference | 当前未被显式引用，可能保留旧 prompt 示例。 | 已移位 | 已移到 appendix/examples，并补充 `examples/prompt-recipes.md` 入口。 | 已修，commit `6ec70c1`。 |
| D17 | `skill-doc-template-system.md` 疑似孤岛 reference | 当前未被显式引用，但可能是 generator 设计依据。 | 已保留 | 已确认 eval 依赖，继续作为生成体系测试契约文档；若未来移动必须同步 eval。 | 已确认，commit `0c8ef0a` / `8328be4`。 |

## 推荐执行顺序

1. 已完成 D1-D3：修正产品简报、Zoon local-first 和协作文档入口文案。
2. 已完成 D5-D8：收敛长板、eval、product-office-hours 和产品简报真源。
3. 已完成 D4、D9、D11、D12：收敛安装文档、工作台地图、AutoDesign 和英文 README。
4. 已完成 D13-D17：依赖确认后归档 / 移位孤岛 reference，D17 保留。
5. 已完成 D10：通过 manifest / generator 收敛共享门槛重复，并新增 eval 防回退。
6. 后续不再按 D1-D17 继续拆；若继续瘦身，应先重新审计新的高噪声项，再小步制定 D18+。

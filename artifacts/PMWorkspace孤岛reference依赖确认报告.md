# PMWorkspace 疑似孤岛 reference 依赖确认报告

本报告最初只做依赖确认，不删除文件、不修改 skill、不改变生成契约。后续已按本报告的保守建议执行归档 / 移位；插件副本只视为 `bin/pmw-build-plugin` 的镜像，不作为独立真源。

## 复查范围

- Source skill：`pm-workspace`、`pm-autoplan`、`pm-jobs`、`pm-strategy-review`、`pm-brief`、`pm-prototype-shotgun`、`pm-prototype-review`、`pm-handoff`
- 文档入口：`README.md`、`README.zh-CN.md`、`docs/`、`evals/README.md`
- 生成系统：`pmworkspace-shared/skill-docs/skill-docs.manifest.json`、`bin/pmw-gen-skill-docs`
- 测试契约：`evals/fixtures`
- 插件副本：`plugins/pmworkspace/skills/pmworkspace-shared`

复查命令摘要：

```bash
rg -l --glob '!artifacts/**' '<reference-file-name>' .
rg -n '<reference-stem>' pmworkspace-shared/skill-docs bin docs README*.md pm-* evals/fixtures
git ls-files pmworkspace-shared/references/<file> plugins/pmworkspace/skills/pmworkspace-shared/references/<file>
```

## 结论摘要

执行状态更新：D13 `decision-gates.md` 与 D14 `intake.md` 已在职责合并后移除；D15 `product-methodology.md` 与 D16 `prompt-recipes.md` 已移到 appendix / examples；D17 `skill-doc-template-system.md` 保留，并在 D10 generator 收敛后继续承担生成体系说明和 eval 锚点。

| 文件 | 当前引用结论 | 风险级别 | 建议动作 | 是否可直接删除 |
|---|---|---:|---|---|
| `decision-gates.md` | 未发现 source skill、README、manifest、generator 或 eval 直接读取该文件；`decision-gates` 只作为 `pmw-config question_mode` 枚举值出现，不等于文档依赖。 | 中 | 已合并有效门槛语言并移除孤岛文件。 | 已处理 |
| `intake.md` | 未发现显式引用；内容与 `first-use-onboarding.md`、`production-reference-gate.md`、`routing.md` 的首次输入 / 线上参考判断重叠。 | 中 | 已把最小上下文字段迁入首次引导 / onboarding 相关文档，并移除孤岛文件。 | 已处理 |
| `product-methodology.md` | 未发现显式引用；内容是通用产品方法，和 `product-discovery-gate.md`、`product-office-hours.md`、`pm-decision-principles.md` 有方法论重叠。 | 低-中 | 已移到 `pmworkspace-shared/references/appendix/product-methodology.md`，不进入运行时必读。 | 已处理 |
| `prompt-recipes.md` | 未发现显式引用；内容是启动话术示例，和 README 示例、`welcome-guide.md`、`first-use-onboarding.md` 有重叠。 | 低 | 已移到 appendix / examples，并补充示例入口。 | 已处理 |
| `skill-doc-template-system.md` | 有 eval 直接断言：`skill-doc-generator-required` 和 compact gates eval 检查该文件；未发现 skill/manifest/generator 运行时读取。 | 高 | 保留：它是生成体系的测试契约文档。若改名或移动，必须同步 eval 和插件副本。 | 保留 |

## 逐项依据

### D13 `decision-gates.md`

- 文件存在于 source 与插件副本，说明当前构建会复制它。
- 未发现 `decision-gates.md` 文件名被 source skill、README、manifest、generator 或 eval 直接引用。
- `decision-gates` 字符串只出现在 `bin/pmw-config` / 插件副本的 `question_mode` 默认值注释中，语义是配置枚举，不是读取该 Markdown。
- 内容仍包含变化类型、问题真实性、价值交换、数据可行性、产品简报对齐、线上参考等门槛，和当前硬门槛体系重叠。

建议：不要直接删除。先把仍有价值的简洁门槛语言合并到 `product-discovery-gate.md` 或 `pm-decision-principles.md`，再做单独归档提交。

### D14 `intake.md`

- 未发现显式引用。
- 内容主要是首次输入字段、快速问题候选、默认假设和输入摘要模板。
- 当前运行链路已由 `$pm-workspace` + `routing.md` + `first-use-onboarding.md` + `production-reference-gate.md` 承担首次路由、线上参考判断和最小输入确认。

建议：作为合并候选。若要瘦身，优先保留“最小上下文”和“输入摘要模板”中仍未被覆盖的字段，迁入 onboarding 附录。

### D15 `product-methodology.md`

- 未发现显式引用。
- 内容是通用产品判断方法，价值在培训和维护者理解，不在运行时硬门槛。
- 与产品发现 gate、office-hours 状态机、PM 决策原则存在明显重叠。

建议：不进入运行时必读；可压缩为 appendix 或从审计材料中保留“方法论来源”，后续再决定是否归档。

### D16 `prompt-recipes.md`

- 未发现显式引用。
- 内容是用户可复制启动话术，适合作为示例，不适合作为运行时协议。
- 与 README 的快速成型 / 深度交付示例和 `welcome-guide.md` 存在重叠。

建议：移到 examples 或 README 链接区；若暂时没有入口需求，可归档但不要直接删除。

### D17 `skill-doc-template-system.md`

- `evals/fixtures/skill-doc-generator-required.json` 直接检查此文件。
- 插件副本中同名 eval 也保留该检查。
- 未发现 `bin/pmw-gen-skill-docs` 或 manifest 运行时读取该文档，但它承担生成体系说明和 eval 契约锚点。

建议：保留。若未来要瘦身，只能把内容合并到更正式的生成器维护文档，并同步修改 eval；不能按“未被 skill 读取”直接删除。

## 最终处理

| 决策项 | 最终动作 | 结果 |
|---|---|---|
| D13 `decision-gates.md` | 合并后归档 | 有效门槛语言已承接，源文件和插件副本已移除。 |
| D14 `intake.md` | 合并到 onboarding | 最小输入字段已承接，源文件和插件副本已移除。 |
| D15 `product-methodology.md` | 移到 appendix | 已移到 `pmworkspace-shared/references/appendix/product-methodology.md`。 |
| D16 `prompt-recipes.md` | 移到 examples / appendix | 已移到 appendix，并新增 `examples/prompt-recipes.md` 入口。 |
| D17 `skill-doc-template-system.md` | 保留 | eval 仍依赖该文档，D10 后继续作为生成体系说明。 |

## 下一步边界

- 本轮孤岛 reference 已处理完毕，D17 保留。
- 若继续做下一批删减，先重新审计新的 D18+；不要把本报告中的旧“候选”状态当作未执行计划。
- 执行任何新删除前必须再次新增或更新 eval，明确“删除后谁接住原职责”，并运行 `bin/pmw-eval run`、`bin/pmw-gen-skill-docs check`、`bin/pmw-build-plugin` 和 `git diff --check`。

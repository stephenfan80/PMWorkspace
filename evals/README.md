# PMWorkspace evals

第一阶段 eval 是无依赖维护工具，用来守住 PMWorkspace 的产品门槛和输出契约，不运行真实 image-2，也不调用 LLM-as-judge。

```bash
bin/pmw-eval list
bin/pmw-eval run
bin/pmw-eval run --fixture quick-assumption-confirmation-required
bin/pmw-eval run --json
```

fixture 放在 `evals/fixtures/`，每个 JSON 代表一个必须被 PMWorkspace 规则兜住的场景。

## 分类地图

eval 分类必须能映射回 `pmworkspace-shared/references/pm-workbench-map.md` 的端到端链路：

| 分类 | 链路阶段 |
|---|---|
| `pm-workspace-entry`、`pm-workspace-routing`、`pm-workspace-runtime` | 欢迎与 D0 路由 |
| `autoplan`、`quick-shaping`、`deep-delivery` | 自动产品评审 |
| `pm-jobs` | 产品价值澄清 |
| `pm-strategy-review` | 策略审查 |
| `pm-brief` | 产品简报 / 核心信息契约 |
| `pm-prototype-shotgun`、`prototype-shotgun`、`prototype-output-contract`、`multi-scheme`、`production-reference`、`screenshot-feedback` | 原型方案：image-2 前门槛、单图协议、方案差异质量、输出单元、线上参考、设计系统 |
| `prototype-review` | 原型复审 |
| `review-specialists` | 原型复审：四个可插拔专家独立短结论、最高严重度合并、专家汇总 |
| `pm-handoff` | 产品交付：精简 PRD、现成文档入口、未复审不交付、未拍板不写验收、交付资产沉淀 |
| `readiness-dashboard` | 出图 / 交付前 Product Readiness Dashboard 和 verdict |
| `artifact-flow` | Product Artifact Flow：产品简报、原型清单、复审结论和交付稿必须成为下游可读产物 |
| `skill-doc-generator` | Skill 文档生成：manifest、`pmw-gen-skill-docs`、生成契约区块和防漂移检查 |
| `memory`、`decision-principles`、`eval-system` | 运行与记忆：偏好边界、个人全局记忆、GitHub 待审稿、自动决策、eval runner |

新增分类时，必须同时更新 `pm-workbench-map.md` 和 `pm-eval-system.md`。

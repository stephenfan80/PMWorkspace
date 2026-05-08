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
| `pm-handoff` | 产品交付 |
| `memory`、`decision-principles`、`eval-system` | 运行与记忆 |

新增分类时，必须同时更新 `pm-workbench-map.md` 和 `pm-eval-system.md`。

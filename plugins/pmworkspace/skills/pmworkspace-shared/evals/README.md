# PMWorkspace evals

第一阶段 eval 是无依赖维护工具，用来守住 PMWorkspace 的产品门槛和输出契约，不运行真实 image-2，也不调用 LLM-as-judge。

```bash
bin/pmw-eval list
bin/pmw-eval run --suite smoke
bin/pmw-eval run --suite core
bin/pmw-eval run --suite full
bin/pmw-eval run --fixture brief-alignment-required-before-image
bin/pmw-eval run --json
```

fixture 放在 `evals/fixtures/`，每个 JSON 代表一个必须被 PMWorkspace 规则兜住的场景。

## 三层检查

PMW 的 eval 不少，维护时不要一上来就被全量吓住。先按改动风险选一层：

| 层级 | 人话意思 | 什么时候跑 |
|---|---|---|
| `smoke` | 主链路有没有断。 | 改 README、examples、入口文案、小范围规则说明时。 |
| `core` | 对齐、出图、复审、交付四个动作是否还稳。 | 改 skill、references、readiness、artifact flow、controller、打包脚本时。 |
| `full` | 全量 eval。 | 发布 GitHub / plugin 前必须跑。 |

`bin/pmw-eval run` 仍然等于 `bin/pmw-eval run --suite full`，避免老脚本悄悄降低检查强度。`smoke` 和 `core` 的清单在 `evals/suites/`，只放 fixture id，不复制 fixture 内容。

## 维护顺序

eval 是后置防回退工具，不是产品表达的起点。改 PMW 行为或用户心智时，先稳定 README、`routing.md`、`welcome-guide.md` 或对应方法 reference 中的产品表达；再同步 skill 正文和 `pmw-gen-skill-docs` 生成契约；最后新增或修改 fixture，把已经稳定的表达锁住。

不要为了先让测试通过而反向修改产品表达，也不要只改 fixture 掩盖 reference、skill 或本地脚本的真实漂移。

## 分类地图

eval 分类必须能映射回 `pmworkspace-shared/references/pm-workbench-map.md` 的端到端链路：

| 分类 | 链路阶段 |
|---|---|
| `pm-workspace-entry`、`pm-workspace-routing`、`pm-workspace-runtime` | 欢迎与产品路径路由 |
| `autoplan` | 自动产品评审 |
| `pm-jobs` | 产品方向审查内核 |
| `pm-strategy-review` | 策略审查 |
| `pm-brief` | 产品简述 / 产品简报契约 |
| `pm-prototype-shotgun`、`prototype-output-contract`、`production-reference`、`screenshot-feedback` | 原型方案：image-2 前门槛、单图协议、`brief_lock.image_output_mode` 出图数量、页面实验差异质量、原型思考、输出单元、线上参考、设计系统 |
| `prototype-review` | 原型复审 |
| `review-specialists` | 原型复审：四个可插拔专家独立短结论、最高严重度合并、专家汇总 |
| `pm-handoff` | 产品交付：产品设计文档、精简 PRD、现成文档入口、未复审不交付、未拍板不写验收、交付资产沉淀 |
| `readiness-dashboard` | 出图 / 交付前 Product Readiness Dashboard 和 verdict |
| `artifact-flow` | Product Artifact Flow：产品简报、浏览器证据、原型清单、复审结论、产品设计文档和交付稿必须成为下游可读产物 |
| `skill-doc-generator` | Skill 文档生成：manifest、`pmw-gen-skill-docs`、生成契约区块和防漂移检查 |
| `memory`、`eval-system`、`release-maintenance` | 运行与记忆：偏好边界、个人全局记忆、GitHub 待审稿、eval runner、版本 / 升级 / 插件打包 |

新增分类时，必须同时更新 `pm-workbench-map.md` 和 `pm-eval-system.md`。

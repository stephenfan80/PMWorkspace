# PMWorkspace

PMWorkspace 是一个面向产品经理、设计师、研究员、运营和创业者的产品方案工作台：**快速成型，深度交付**。它把产品想法、PRD、截图、访谈洞察或 Zoon 文档，沉淀成可复用的产品资产：产品简介 / 产品简报、方案方向、移动端优先的 image-2 原型图、PRD、设计反馈和交付稿。

PMWorkspace 来自原来的 `product-prototype-designer` 技能。旧名称已废弃，后续请使用 `$pm-workspace` 和 PMWorkspace 技能套件。

## 它解决什么问题

很多产品方案失败不是因为图不好看，而是用户、场景、问题、目标、约束和解决方案没有被想清楚。PMWorkspace 先把拍脑袋的 idea 变成可以讨论、评审和交付的产品资产，再进入原型或 PRD。

PMWorkspace 有两个入口：

- **快速成型模式：** 10 分钟内把一句 idea 推进成“产品简报 + 方案方向 + 原型图”的轻量包，适合拿去组内、领导或设计讨论。
- **深度交付模式：** 用更完整的 Q 诊断、D 拍板、Zoon 对齐、原型复审和交付稿，把选定方向升级成 PRD、设计或研发交付资产。

深度交付模式遵循完整状态机：

```text
工作目标模式
-> 场景路由
-> Q 诊断
-> 前提确认
-> D 拍板
-> 产品简报
-> image-2 原型
-> 原型复审
-> 交付资产
```

## 端到端工作台地图

PMWorkspace 的全链路地图由 `pmworkspace-shared/references/pm-workbench-map.md` 维护，README、routing、eval 和各技能状态字段都以它为同一张地图：

```text
$pm-workspace
-> $pm-autoplan
-> $pm-jobs
-> $pm-strategy-review
-> $pm-brief
-> $pm-prototype-shotgun
-> $pm-prototype-review
-> $pm-handoff
```

每一环都必须说明：当前模式 / 状态、当前门槛或最早门槛、下一技能、run_id、证据状态、当前 Q / D、产物清单和建议下一步。这样用户不会在“已经出图了吗”“能交付了吗”“缺什么证据”之间来回猜。

## 技能套件

| 技能 | 什么时候用 |
|---|---|
| `$pm-workspace` | 主入口，负责路由、首次引导、更新检查和状态记录。 |
| `$pm-autoplan` | 自动串联产品追问、策略审查、产品简报、Zoon 同步和原型准备度检查。 |
| `$pm-jobs` | 产品价值澄清器：强痛用户是谁、何时触发、现在怎么替代、损失是什么、先赢哪一小块。 |
| `$pm-strategy-review` | 策略取舍裁判：判断该扩大、保持、收缩还是转向，并把最大策略矛盾转成 PM 拍板。 |
| `$pm-brief` | 产品核心信息契约：把已对齐事实、策略取舍和参考门槛压缩成可出图、复审和交付的核心判断。 |
| `$pm-prototype-shotgun` | 基于已对齐的产品简报生成多方案 image-2 原型图。 |
| `$pm-prototype-review` | 复审已生成原型图，判断是否需要重出并沉淀偏好。 |
| `$pm-handoff` | 输出精简 PRD / 交付稿，并把接口、数据、埋点、实验标准沉淀为本地交付资产。 |

## 快速开始

### 10 分钟轻量包

```text
使用 $pm-workspace 快速成型这个产品想法，输出一套轻量包：产品简报、2-3 个方案方向、每个方向 1 张移动端原型图。
产品想法：<一句话描述>
已知背景：<可选，用户 / 场景 / 约束 / 参考>
要求：可以先基于明确标注的假设推进；出图前请先让我确认这些假设。
```

轻量包默认包含：

- 标注假设的产品简报。
- 2-3 个在产品策略、信息架构、交互模型或信任模型上不同的方案方向。
- 每个方案按“一个方案 + 一个屏幕 = 一张图”生成独立 image-2 原型图。
- 下一步升级建议：继续补齐 PRD、进入原型复审，或整理成研发交付稿。

### 深度交付

```text
使用 $pm-workspace 帮我梳理这个产品想法，并在确认后生成原型方案。
产品想法：<一句话描述>
目标人群：<谁在什么场景最需要>
核心问题：<他们现在卡在哪里>
目标：<希望提升的行为或指标>
约束：<数据 / 业务 / 法务 / 设计系统 / 上线范围>
输出：<只要产品简报 / 1 个屏幕 / 2 个屏幕 / 3 个方案 / 交付稿>
要求：每个方案和屏幕单独生成一张图，不要合成在同一张图里。
```

## 默认工作流

1. `$pm-workspace` 先判断入口：快速成型模式，还是深度交付模式。
2. 快速成型模式只问 2-3 个最影响方案结构的问题，列出关键假设，并请用户确认“按这些假设继续”。
3. 用户确认后，输出轻量包：产品简报、方案方向、独立 image-2 原型图和下一步升级建议。
4. 深度交付模式先确认工作目标模式：验证价值、优化线上指标、业务评审、设计评审或研发交付。
5. `$pm-jobs` 先判断问题定义模式：创业验证、内部业务优化或设计讨论；每轮先给一句“我对真实问题的判断”，把功能愿望重新定义成用户问题、当前损失或决策任务。
6. `$pm-jobs` 再用 `Q` 一次一个问题澄清强痛人群、触发时刻、现状替代、当前损失和最小可赢切口；问题根据用户输入和当前价值缺口动态生成，通常 2-3 个，必要时最多 5 个。
7. 输出 2-4 条关键前提让 PM 确认；不同意就回到对应追问。
8. 关键 PM 决策用 `D` 选择题拍板，一次只展开一个完整问题；多个待拍板只提示后续标题队列。
9. 新页面如果承接线上流程或生产样式，先完成线上参考检查。
10. `$pm-brief` 按主场景做轻量互联网最佳实践检索，但不增加 Q 数量，只保留可借鉴原则、不可照搬和对原型影响。
11. `$pm-brief` 先输出产品核心信息，再固化门槛和支持信息；`pmw-log brief` 会自动创建或追加 Zoon 在线文档。
12. 用户在对话或 Zoon 中调整 brief 后，重新保存并同步 Zoon；原型前运行 Zoon 漂移检查。
13. 产品简报达到“已对齐”后，`$pm-prototype-shotgun` 先读取 Zoon 最新内容，再生成 image-2 原型图。
14. `$pm-prototype-review` 复审原型是否符合 brief、线上参考、反指标和不可虚构项。
15. `$pm-handoff` 把选定方向转成 PRD、设计、实验验证或研发交付文档。

## 原型输出规则

- 默认移动端优先：iPhone 17 竖屏 `402 x 874`。
- 只有用户明确要求桌面端，或看板 / 内部工具确实需要大屏密度，才使用桌面端。
- 深度交付模式中，产品简报没有“已对齐”前，不写图片提示词，不生成图片，不生成 HTML，不输出交付稿。
- 快速成型模式中，出图前必须列出关键假设和不可虚构项，并获得用户确认“按这些假设继续”；轻量包要标注“基于假设，可讨论，不等于最终 PRD”。
- HTML 只在用户明确要求“HTML / 可交互网页 / 前端实现 / 本地网页原型”时允许；不能作为 image-2 不可用时的替代品。
- 新页面也要先判断是否需要线上参考；如果它承接线上流程、结果页、状态页或生产样式，必须先提供截图/录屏/相似页面，或明确确认“没有线上参考，按新页面概念稿推进”。
- 用户提供截图或线上参考时，只更新视觉基线和参考状态，不自动产出完整 md 方案、HTML 或原型图。
- 多方案必须在产品策略、信息架构、交互模型或信任模型上不同，不能只是换颜色。
- 一个方案 + 一个屏幕 = 一张图。
- 每张图必须绑定方案名、屏幕任务、主目标、反指标、不可虚构项和产品简报版本。
- `3 个方案 x 2 个屏幕` = 6 张独立图片。
- 禁止把多个方案合成在一张比较图里，除非用户明确要展示板。

## 使用环境

最佳体验是 **Codex**。

PMWorkspace 的完整体验包含移动端优先的 image-2 原型图输出，依赖宿主环境提供图像生成能力。Codex 环境可以同时完成产品追问、产品简报、方案方向、image-2 原型图和交付稿，因此推荐使用：

```bash
./setup --host codex
```

其他支持 Codex skill 的环境也可以使用 PMWorkspace 的产品追问、产品简报、PRD 和交付稿能力；如果宿主没有 image-2 / 图像生成能力，原型图输出会受限，不能用 HTML 或 Markdown 线框替代 image-2 原型图，除非用户明确要求 HTML / 可交互网页 / 前端实现。

## 产品运行层

PMWorkspace v0.2 把技能套件升级成本地产品运行系统：

- **Runtime Kernel：** `pmw-run` 为每次工作生成 `run_id`，记录模式、门槛、决策、证据、产物、复审和下一步。
- **Workbench Map：** `pm-workbench-map.md` 统一 README、路由、eval 分类和技能间状态字段。
- **Evidence Dashboard：** `pmw-dashboard status` 输出中文证据状态页，汇总产品简报版本、Zoon 状态、线上参考、假设、不可虚构项、原型清单、复审结论和问题偏好。
- **Prototype Shotgun Board：** `pmw-prototype-board` 登记每个独立 image-2 图片单元，并用表格比较方案；不把多张图合成一张图。
- **PM Review Army：** 原型复审使用策略、信任 / 风险、设计系统和数据可行性四个视角，最终合并为可通过、需要重出或需要 PM 拍板。
- **Question Tuning：** `pmw-question-tuning` 记录用户对 Q/D 的偏好，例如永远问、高风险才问、默认采用推荐或除非阻塞否则少问。
- **PM Eval：** `pmw-eval` 用无依赖 fixture 检查核心门槛和输出契约，防止 skill 规则退化。
- **自动决策原则：** 统一事实优先级和停止门槛，明确低风险默认项可以自动采用，用户承诺、数据真实性、范围、实验口径、线索 / 交易 / 隐私边界必须 PM 拍板。

## 安装

```bash
git clone https://github.com/stephenfan80/PMWorkspace.git
cd PMWorkspace
./setup --host codex
```

如果已经在本仓库目录里：

```bash
./setup --host codex
```

然后使用：

```text
使用 $pm-workspace 显示欢迎引导，并帮我选择合适的产品工作流。
```

安装后不要让用户自己猜命令。重启 Codex 后先用 `$pm-workspace`，它会像第一次打开应用一样说明 PMWorkspace 能做什么，并给出新想法、PRD/Zoon、原型方向、截图优化、交付稿这几条入口。

## 本地状态资产

PMWorkspace 默认把资产保存在本地：

```text
~/.pmworkspace/
  config.yaml
  analytics/usage.jsonl
  user/taste-profile.jsonl
  user/product-cognition.jsonl
  user/delivery-facts.jsonl
  user/pmworkspace-improvements.jsonl
  user/pmworkspace-feedback-drafts/
  projects/<slug>/briefs/
  projects/<slug>/decisions.jsonl
  projects/<slug>/questions.jsonl
  projects/<slug>/project.json
  projects/<slug>/runs/
  projects/<slug>/prototype-board.jsonl
  projects/<slug>/question-tuning.jsonl
  projects/<slug>/prototypes/
  projects/<slug>/handoffs/
  projects/<slug>/delivery-facts.jsonl
  projects/<slug>/taste-profile.jsonl
  projects/<slug>/learnings.jsonl
```

会保存：

- 技能使用记录。
- 中文项目名和 Zoon 在线简报链接。
- 用户确认过的产品/设计决策。
- 选择题拍板记录。
- 每次运行的本地审计轨迹。
- 产品简报 Markdown。
- 原型批次清单。
- PRD / 设计 / 实验 / 研发交付稿。
- 接口、数据来源、埋点和实验标准等脱敏交付事实。
- 方案比较板。
- Q/D 问题偏好。
- 用户批准或拒绝的设计偏好。
- 脱敏后的产品学习和复用判断。
- 单个用户独有的全局偏好。
- 脱敏后的产品认知。
- PMWorkspace 进化候选和本地 GitHub 回流待审稿。

不会保存：

- token、owner secret、API key、cookie。
- 原始客户资料、内部录音、敏感截图。
- 未脱敏 Zoon 内容。
- Zoon ownerSecret 或 API 原始响应。
- 用户没有明确要求保存的私密 PRD 原文。
- 未经用户确认，不会把 GitHub 回流待审稿提交到远端。

查看配置：

```bash
bin/pmw-config list
```

项目记录：

```bash
bin/pmw-project get-name
bin/pmw-project set-name "通用券站外召回方案"
bin/pmw-project show
```

运行层工具：

```bash
bin/pmw-run start --skill pm-autoplan --mode quick --goal "10 分钟轻量包"
bin/pmw-run event --type gate --status "待确认" --title "假设确认" --summary "等待 PM 确认"
bin/pmw-run finish --status "基于假设，可讨论" --next "进入 image-2 原型"
bin/pmw-dashboard status
bin/pmw-prototype-board add --scheme "方案 A" --screen "首页" --brief-version "v1"
bin/pmw-prototype-board list
bin/pmw-question-tuning add --dimension "反指标" --policy high_risk_only --reason "低风险轻量包默认采用推荐"
bin/pmw-question-tuning summary
bin/pmw-eval list
bin/pmw-eval run
```

Eval fixture 保存在仓库的 `evals/fixtures/`，安装时会复制到 shared skill bundle，供维护检查使用。

Zoon 在线简报：

```bash
bin/pmw-zoon protocol --host "https://zoon.up.railway.app"
cat brief.md | bin/pmw-zoon create --title "产品设计简报：通用券站外召回方案"
cat brief.md | bin/pmw-zoon append --url "<Zoon URL>"
cat brief.md | bin/pmw-zoon sync --title "产品设计简报：通用券站外召回方案"
bin/pmw-zoon drift --url "<Zoon URL>"
bin/pmw-zoon read --url "<Zoon URL>"
```

`protocol` 会动态读取 Zoon 的 `/skill` 和 `/agent-docs`，并缓存协议摘要，默认 TTL 为 300 秒；Zoon 升级时优先跟随远端协议说明。

## 选择题拍板

PMWorkspace 不应只输出“还需要你拍板 5 个问题”，也不应一次展开多个完整选择题。凡是会改变产品方向、原型范围、实验口径、用户承诺或交付稿的关键点，都要变成 `D` 选择题，并且每轮只展开一个：

```text
D1 - “全品牌可用”的对外口径
为什么重要：口径过大容易形成无条件承诺，用户发现部分品牌不可领时会损害信任。
推荐选择：A，因为它既能表达覆盖面，又保留真实业务边界。

选项 A：参与品牌可领取
选项 B：全品牌可参与查询
选项 C：全品牌都有机会领

取舍：增长吸引力 vs 承诺真实性。
默认假设：如果你不改，我会按 A 继续。

后续待拍板：D2 至高金额展示方式、D3 多车提交后的线索生成。
```

## 更新提醒

每个 skill 使用前都会检查 GitHub：同时比较 `VERSION` 和 `main` 分支最新提交。因此即使没有正式升版本号，只要 GitHub 上的技能规则或文档有新提交，也会提示：

```text
UPGRADE_AVAILABLE <local> <remote>
```

升级：

```bash
bin/pmw-upgrade --host codex
```

暂缓某个版本：

```bash
bin/pmw-snooze-update <remote-version-or-commit>
```

关闭更新检查：

```bash
bin/pmw-config set update_check false
```

## 迁移旧名称

如果之前安装过旧的 `product-prototype-designer`：

```bash
rm -rf ~/.codex/skills/product-prototype-designer
./setup --host codex
```

之后使用 `$pm-workspace`。

## 隐私

默认遥测是本地优先，只写入 `~/.pmworkspace/analytics/usage.jsonl`。远程匿名汇总必须由用户明确开启。PMWorkspace 不应上报项目名、文件路径、提示词内容、截图、产品简报正文或客户数据。

## 许可证

MIT

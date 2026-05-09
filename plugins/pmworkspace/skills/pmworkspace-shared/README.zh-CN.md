# PMWorkspace

**把模糊想法推进到可评审、可出图、可交付。**

> Codex 插件展示名：**AI 产品工作站**。`PMWorkspace` 仍是 GitHub 仓库名、技术包名和 `$pm-workspace` 技能入口。

## Codex Plugin Beta 安装

公开插件库上架前，`Plugins` 默认市场里搜不到它；先把 GitHub 仓库作为本地 marketplace 加进去。

最快方式：

```bash
codex plugin marketplace add stephenfan80/PMWorkspace
```

如果你之前添加过旧版本或本地路径，先移除再添加：

```bash
codex plugin marketplace remove pmworkspace
codex plugin marketplace add stephenfan80/PMWorkspace
```

然后：

1. 完全退出并重启 Codex。
2. 打开 `Plugins`。
3. 把筛选从 `Built by OpenAI` 切到 `全部`。
4. 搜索 **AI 产品工作站** 或 `PMWorkspace`。
5. 点击安装 / 启用，之后从 `$pm-workspace` 开始。

本地开发或团队测试也可以从仓库运行升级脚本：

```bash
git clone https://github.com/stephenfan80/PMWorkspace.git
cd PMWorkspace
bin/pmw-upgrade --host codex-plugin
```

PMWorkspace 是一个产品方案工作台。它不是只帮你生成一张好看的原型图，而是把真实问题、产品简报（brief）、AI 协作文档（Zoon）、截图证据、方案差异、复审结论和交付稿串成一条连续的产品工作流。

你可以把一句想法、一段 PRD、一张线上截图、一份用户反馈或一个协作文档丢进来。PMWorkspace 会先帮你判断真正要解决的问题，再把它推进成能讨论、能评审、能出图、能交付的产品资产。

核心定位很简单：

```text
快速成型，深度交付。
```

## 你是不是也遇到这些情况

- 老板或业务方只给了一句话，但希望你明天就拿出方案。
- 用户反馈、运营诉求、客服记录和截图都在，但产品判断还没站稳。
- 设计需要马上出图，可你担心问题定义、目标人群和业务边界还没对齐。
- PRD、协作文档、截图和对话记录散在不同地方，每次交付都要重新讲一遍上下文。
- 原型越做越快，结果越容易变成“看起来完整，但不知道为什么这么做”。
- 线上功能要优化，却没有当前流程截图、状态页、竞品参考或视觉基线。
- 评审时只有一个 PM 视角，缺策略、风险、设计系统、数据可行性和研发交付视角。

PMWorkspace 接住的就是这种混乱时刻：不是替你跳过思考，而是把思考压缩成一条能往前走的路径。

## PMWorkspace 帮你推进成什么

你给它原始材料，它帮你形成一组可继续流动的产品资产：

- **产品简报：** 默认输出 12-18 行左右的业务简报，只保留产品判断、范围、反指标、不可虚构项和下一步；完整 Q/D、来源、准备度、产物流动和路径进入本地审计。
- **方案方向：** 不只是换配色，而是在产品策略、信息架构、交互模型或信任模型上给出不同解法。
- **移动端优先原型图：** 无线上截图时默认按 iPhone 17 竖屏 `402 x 874` 生成；有生产截图 / `visual_baseline` 时必须按截图物理像素长板生成。一个方案、一个屏幕、单独一张图。
- **线上证据记录：** 把线上流程截图、状态页、竞品参考和协作文档漂移证据纳入同一条产品链路。
- **产品准备度判断：** 在出图或交付前统一检查产品简报、协作文档、线上参考、方案差异、不可虚构项和复审状态；默认只给结论和第一条阻断原因，完整表格用 `--details` 展开。
- **多角色复审结论：** 从策略、信任 / 风险、设计系统、数据可行性等角度指出能不能通过、要不要重出、哪里需要拍板。
- **交付稿：** 把通过复审的方向整理成精简 PRD、设计交付、实验验证或研发交付材料。

## 两种工作方式

### 快速成型

适合新想法、拍脑袋方案、组内讨论、领导预览或创业验证。

PMWorkspace 会用 2-3 个关键澄清补齐最大缺口，列出关键假设、反指标和不可虚构项。你确认“按这些假设继续”后，它会输出一套轻量包：

- 产品简报。
- 2-3 个方案方向。
- 每个方向 1 张移动端 image-2 原型图。
- 下一步建议：继续验证、进入复审，或升级为交付稿。

这类产物会明确标注“基于假设，可讨论”，不会包装成已经验证过的最终结论。

### 深度交付

适合 PRD、设计评审、研发交付、生产流程优化、高风险业务或需要协作文档同步的项目。

PMWorkspace 会先判断工作目标，再做关键澄清和拍板选择题。只有产品简报达到“已对齐”，才进入 image-2 原型或交付稿。这样做的目的不是拖慢速度，而是避免在错误问题上快速出图。

深度交付更适合这些任务：

- 把现有 PRD 或协作文档转成可出图的产品简报。
- 基于生产截图优化线上页面。
- 为设计评审准备多方案原型。
- 为研发交付整理精简 PRD。
- 在出图前确认线上参考、不可虚构项和复审状态。

## 它如何工作

PMWorkspace 的工作方式更像一支小型产品小队，而不是单个问答工具：

1. **先判断真实问题。** 每一轮都会先说清楚“我对真实问题的判断”，避免直接把功能愿望当成解决方案。
2. **再做关键澄清。** 它不会一次甩出长问卷，而是每次只问最影响方案结构的问题。
3. **用拍板选择题减少反复。** 遇到会改变范围、承诺、实验口径或交付边界的地方，会给出推荐选项和取舍说明。
4. **把产品简报同步到 AI 协作文档。** 产品简报阶段默认优先创建或追加到 AI 协作文档，后续出图和交付前会检查是否发生漂移。
5. **用线上证据建立事实基础。** 线上流程截图、状态页、竞品参考和协作文档漂移证据会作为轻量产物进入同一条工作流。
6. **出图或交付前做准备度检查。** 缺产品简报、缺线上参考、缺复审或方案差异不够时，会先指出阻断点。
7. **用多角色复审补齐盲区。** 策略、风险、设计系统、数据可行性等视角各自产出短结论，再合并成最终判断。

## 核心优势

- **快，但不莽。** 快速成型可以 10 分钟起步，但必须带着假设、反指标和不可虚构项。
- **能把散乱材料收束成共识。** 想法、PRD、截图、协作文档和用户洞察会被压缩成一份能继续流动的产品简报。
- **出图前有证据。** 线上参考、视觉基线、状态页和竞品流程不再只是口头描述。
- **评审不只靠一个 PM 视角。** 原型复审默认有策略、信任 / 风险、设计系统、数据可行性四个视角，高风险场景还能追加更多角色。
- **产物会往下游流动。** 产品简报、原型清单、复审结论和交付稿会被登记为下游可读产物，减少重复解释。
- **有记忆，但不越界。** 它可以沉淀 taste、偏好和历史决策，但不会用偏好覆盖本轮事实、风险或用户确认。
- **移动端原型更克制。** 默认一个方案、一个屏幕、一张图，避免把多个方向糊成一张无法判断的拼图。
- **隐私边界清楚。** token、cookie、客户资料、内部录音、私密截图和未脱敏协作文档内容不写入公开材料。

## 第一次怎么用

公开插件用户：

- 在 Codex 的 `Plugins` 里安装 `AI 产品工作站`。
- 后续公开版本更新也优先从 Codex 插件页更新。
- 注意：公开上架审批前，它不会出现在默认插件市场搜索结果里。

GitHub 本地 plugin 试用：

推荐直接添加 GitHub marketplace：

```bash
codex plugin marketplace add stephenfan80/PMWorkspace
```

如果已经添加过旧版本：

```bash
codex plugin marketplace remove pmworkspace
codex plugin marketplace add stephenfan80/PMWorkspace
```

重启 Codex 后，在 `Plugins` 页面把 `Built by OpenAI` 筛选切到 `全部`，搜索 `AI 产品工作站` 或 `PMWorkspace`。

开发者也可以从本地仓库安装：

```bash
git clone https://github.com/stephenfan80/PMWorkspace.git
cd PMWorkspace
bin/pmw-upgrade --host codex-plugin
```

旧版 skill 安装：

```bash
git clone https://github.com/stephenfan80/PMWorkspace.git
cd PMWorkspace
./setup --host codex
```

已经在本目录里时：

```bash
./setup --host codex
```

重启 Codex 后，从 `$pm-workspace` 开始：

```text
使用 $pm-workspace 显示欢迎引导，并帮我选择合适的产品工作流。
```

也可以直接说清楚你要哪种结果：

```text
使用 $pm-workspace 快速成型这个产品想法，输出产品简报、2-3 个方案方向和每个方向 1 张移动端原型图。

产品想法：<一句话描述>
已知背景：<用户 / 场景 / 约束 / 参考>
要求：可以先基于明确标注的假设推进；出图前请先让我确认这些假设。
```

```text
使用 $pm-workspace 帮我把这份 PRD / AI 协作文档 / 截图反馈整理成可出图的产品简报。

目标人群：<谁在什么场景最需要>
核心问题：<他们现在卡在哪里>
目标：<希望提升的行为或指标>
约束：<数据 / 业务 / 法务 / 设计系统 / 上线范围>
输出：<只要产品简报 / 1 个屏幕 / 3 个方案 / 交付稿>
```

## 常见场景

- **新想法验证：** 从一句 idea 生成轻量产品简报、方案方向和讨论用原型图。
- **现有页面优化：** 先读取当前截图或线上参考，再判断哪些信息、状态和承诺不能乱改。
- **协作文档转原型：** 先同步最新产品简报，再检查是否和对话中的方向发生漂移。
- **多方案设计讨论：** 每个方案独立成图，并进入方案比较板，方便做取舍。
- **原型复审：** 检查原型是否符合产品简报、线上参考、反指标和不可虚构项。
- **交付 PRD：** 把已通过复审的方向压缩成精简 PRD，保留接口、数据、埋点、实验标准和待补充项。

更多示例见 `examples/`。

## 原型输出规则

- 默认移动端优先：无线上截图时用 iPhone 17 竖屏 `402 x 874`；有生产截图 / `visual_baseline` 时用截图物理像素长板。
- 只有用户明确要求桌面端，或看板 / 内部工具确实需要大屏密度，才使用桌面端。
- 深度交付中，产品简报没有“已对齐”前，不写图片提示词，不生成图片，不生成 HTML，不输出交付稿。
- 快速成型中，出图前必须列出关键假设和不可虚构项，并获得用户确认“按这些假设继续”。
- HTML 只在用户明确要求“HTML / 可交互网页 / 前端实现 / 本地网页原型”时允许；不能作为 image-2 不可用时的替代品。
- 新页面如果承接线上流程、结果页、状态页或生产样式，必须先提供截图 / 录屏 / 相似页面，或明确确认“没有线上参考，按新页面概念稿推进”。
- 用户提供截图或线上参考时，只更新视觉基线和参考状态，不自动产出完整 md 方案、HTML 或原型图。
- 多方案必须在产品策略、信息架构、交互模型或信任模型上不同，不能只是换颜色。
- 一个方案 + 一个屏幕 = 一张图。
- `3 个方案 x 2 个屏幕` = 6 张独立图片。
- 禁止把多个方案合成在一张比较图里，除非用户明确要展示板。

## 高级能力与维护入口

这一节给已经开始深用 PMWorkspace 的用户和维护者。第一次阅读时，可以先跳过。

### 端到端工作台地图

PMWorkspace 的端到端工作台地图由 `pmworkspace-shared/references/pm-workbench-map.md` 维护。README 只讲产品体验和入口，不维护第二套路由表。

核心链路是：

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

### 技能套件

| 技能 | 用户能获得什么 |
|---|---|
| `$pm-workspace` | 选择工作方式，进入欢迎引导，记录本轮状态。 |
| `$pm-autoplan` | 自动串联问题澄清、策略审查、本地产品简报、可选协作文档同步和准备度检查。 |
| `$pm-jobs` | 把功能愿望重新定义成用户问题、当前损失和最小可赢切口。 |
| `$pm-strategy-review` | 用扩大、保持、收缩、转向四种范围模式判断策略取舍。 |
| `$pm-brief` | 生成产品简报，让原型、复审和交付有同一份事实来源。 |
| `$pm-prototype-shotgun` | 基于已对齐的产品简报生成多方案 image-2 原型图。 |
| `$pm-prototype-review` | 复审原型是否符合产品简报、线上参考、反指标和不可虚构项。 |
| `$pm-handoff` | 输出精简 PRD / 交付稿，并沉淀接口、数据、埋点和实验事实。 |

### 产品运行层

- **Product Readiness Dashboard：** `pmw-dashboard readiness --target prototype|handoff` 在出图 / 交付前统一给出准备度判断，覆盖产品简报、可选 AI 协作文档、线上参考、方案差异、不可虚构项和复审状态；默认是简洁 verdict，完整门槛表用 `--details`。
- **Product Artifact Flow：** `pmw-artifact` 记录下游可读产物，让产品简报、原型清单、复审结论和交付稿能流向下一个技能，而不是靠对话记忆重新推断；默认只给摘要，完整链路用 `pmw-artifact flow --details`。
- **Browser Evidence Lite：** 线上流程截图、状态页、竞品参考和协作文档漂移证据统一登记为 `browser_evidence` 产物，复用 `pmw-artifact`，不新增浏览器证据子系统。
- **Evidence Dashboard：** `pmw-dashboard status` 默认输出中文状态摘要；`pmw-dashboard status --details` 才展开产品简报版本、协作文档状态、线上参考、假设、不可虚构项、原型清单、复审结论和问题偏好。
- **Prototype Shotgun Board：** `pmw-prototype-board` 登记每个独立 image-2 图片单元，并用表格比较方案。
- **PM Review Army / Product Review Squad：** 原型复审先运行策略、信任 / 风险、设计系统、数据可行性四个可插拔专家独立检查；高风险或深度交付时，可追加 CEO、Eng、Design、DX、安全、QA、发布工程师短结论。
- **Skill Doc Generator：** `pmw-gen-skill-docs` 从 manifest 生成并检查 SKILL.md 共享契约区块，统一 preamble、共享门槛、必读协议和输出字段。

### 常用命令

```bash
bin/pmw-run start --skill pm-autoplan --mode quick --goal "10 分钟轻量包"
bin/pmw-run event --type gate --status "待确认" --title "假设确认" --summary "等待 PM 确认"
bin/pmw-run finish --status "基于假设，可讨论" --next "进入 image-2 原型"
bin/pmw-dashboard status
bin/pmw-dashboard status --details
bin/pmw-dashboard readiness --target prototype
bin/pmw-dashboard readiness --target handoff
bin/pmw-dashboard readiness --target prototype --details
bin/pmw-artifact add --kind browser_evidence --title "线上参考：结果页" --status "已采集" --source-skill pm-brief --path "<截图路径>" --url "<URL>" --summary "页面任务、视觉基线、交互模式、必须保留、可以挑战"
bin/pmw-artifact flow
bin/pmw-artifact flow --details
bin/pmw-artifact latest --kind product_brief
bin/pmw-review-specialist list
bin/pmw-review-specialist summary
bin/pmw-prototype-board add --scheme "方案 A" --screen "首页" --brief-version "v1"
bin/pmw-prototype-board list
bin/pmw-question-tuning add --dimension "反指标" --policy high_risk_only --reason "低风险轻量包默认采用推荐"
bin/pmw-question-tuning summary
bin/pmw-eval list
bin/pmw-eval run
bin/pmw-gen-skill-docs write
bin/pmw-gen-skill-docs check
```

协作文档命令：

```bash
bin/pmw-zoon protocol --host "https://zoon.up.railway.app"
bin/pmw-zoon join --url "<协作文档 URL>"
cat brief.md | bin/pmw-zoon create --title "产品设计简报：通用券站外召回方案"
cat brief.md | bin/pmw-zoon append --url "<协作文档 URL>"
cat brief.md | bin/pmw-zoon sync --title "产品设计简报：通用券站外召回方案"
bin/pmw-zoon drift --url "<协作文档 URL>"
bin/pmw-zoon read --url "<协作文档 URL>"
```

`protocol` 会动态读取协作服务的 `/skill` 和 `/agent-docs`，并缓存协议摘要，默认 TTL 为 300 秒；服务升级时优先跟随远端协议说明。

### 本地状态资产

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
  projects/<slug>/briefs/audit/
  projects/<slug>/decisions.jsonl
  projects/<slug>/questions.jsonl
  projects/<slug>/project.json
  projects/<slug>/runs/
  projects/<slug>/artifact-flow.jsonl
  projects/<slug>/review-specialists.jsonl
  projects/<slug>/prototype-board.jsonl
  projects/<slug>/question-tuning.jsonl
  projects/<slug>/prototypes/
  projects/<slug>/handoffs/
  projects/<slug>/delivery-facts.jsonl
  projects/<slug>/taste-profile.jsonl
  projects/<slug>/learnings.jsonl
```

会保存项目名、业务简报、完整本地审计副本、用户确认过的决策、协作文档链接、产物流动记录、复审专家短结论、原型清单、交付稿、脱敏交付事实、偏好反馈和本地使用日志。默认用户输出和 `pmw-project show`、dashboard、artifact-flow 都会脱敏 token、ownerSecret、Authorization 等敏感字段；本机调试确需原始项目 JSON 时使用 `pmw-project show --raw`。

不会保存 token、owner secret、API key、cookie、原始客户资料、内部录音、敏感截图、未脱敏协作文档内容或 API 原始响应。

### 更新

每个 skill 使用前都会检查 GitHub：同时比较 `VERSION` 和 `main` 分支最新提交。因此即使没有正式升版本号，只要技能规则或文档有新提交，也会提示：

```text
UPGRADE_AVAILABLE <local> <remote> <host>
UPGRADE_COMMAND pmw-upgrade --host <codex|codex-plugin>
```

升级时优先使用提示里的 `UPGRADE_COMMAND`。

从 GitHub 本地安装 plugin 的用户：

```bash
bin/pmw-upgrade --host codex-plugin
```

旧版 `~/.codex/skills` 用户：

```bash
bin/pmw-upgrade --host codex
```

从 Codex 插件库安装的用户：打开 Codex 的 `Plugins`，找到 `AI 产品工作站`，点击更新；如果没有更新按钮，就卸载后重新安装。

暂缓某个版本：

```bash
bin/pmw-snooze-update <remote-version-or-commit>
```

关闭更新检查：

```bash
bin/pmw-config set update_check false
```

### 发布新版本

发布时让 AI 按这个清单处理：

```text
请发布 PMWorkspace vX.Y.Z。

要求：
1. 更新 VERSION。
2. 同步更新 Codex plugin 的 plugin.json version。
3. 重新构建 plugins/pmworkspace 包。
4. 检查 skill 契约和 eval。
5. 更新 README 中的安装与更新说明。
6. 不要修改用户本地状态目录，不要提交 token、私密截图或客户资料。
7. 最后给我列出 Codex plugin 用户和旧版 skill 用户分别如何更新。
```

### 迁移旧名称

如果之前安装过旧的 `product-prototype-designer`：

```bash
rm -rf ~/.codex/skills/product-prototype-designer
./setup --host codex
```

之后使用 `$pm-workspace`。

## 隐私

默认遥测是本地优先，只写入 `~/.pmworkspace/analytics/usage.jsonl`。远程匿名汇总必须由用户明确开启。PMWorkspace 不上报项目名、文件路径、提示词内容、截图、产品简报正文或客户数据。

## 许可证

MIT

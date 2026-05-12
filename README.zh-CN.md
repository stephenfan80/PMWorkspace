# PMWorkspace

**把一句想法、截图反馈或 PRD，变成能讨论、能出图、能交付的产品方案。**

> Codex 插件展示名：**AI 产品工作站**。`PMWorkspace` 仍是 GitHub 仓库名、技术包名和 `$pm-workspace` 技能入口。

PMWorkspace 适合你想把一个产品想法、线上截图、用户反馈或 PRD 快速推进成方案时使用。

它不会一上来就替你画图，而是先帮你看清楚：这个问题值不值得做、现在证据够不够、哪些地方不能靠猜。然后再产出能拿去讨论、评审、出图或交给设计 / 研发继续推进的材料。

简单说：**先用最少材料拿到可讨论方案；需要交付时，再把事实、截图、风险和复审补齐，产出能评审、能交给设计 / 研发的文档。**

## 你可能正卡在这些事

- 只有一句想法，但明天就要拿去和老板、组内或投资人讨论。
- 有用户反馈、运营诉求、客服记录和截图，但不知道真正该改哪里。
- 设计同学想出图，但你担心问题、目标用户和边界还没说清。
- PRD、截图、协作文档和聊天记录散在不同地方，每次评审都要重新解释。
- 方案看起来越来越完整，但其实很多结论是猜的。
- 线上功能要改，却缺当前页面截图、关键状态页或视觉基线。

## PMWorkspace 会帮你做什么

- **先判断问题靠不靠谱。** 它会追问目标用户、触发场景、当前替代、真实损失和风险边界，避免把“感觉可以做”直接写成方案。
- **告诉你现在缺什么。** 它会用一张轻量对齐卡告诉你：当前判断是什么、还缺哪些信息、不补会偏到哪里、下一步补什么。
- **把散乱材料变成一份短产品说明。** 这份说明会成为后续出图、复审和交付的共同依据。
- **给出多条可比较的方案方向。** 方案差异不只是换颜色，而是信息结构、任务路径、信任方式或产品取舍不同。
- **在出图前守住边界。** 如果截图、数据、约束或关键前提不足，它会先标注假设和风险，而不是把不确定内容画成确定事实。
- **把确认后的方案继续整理成交付材料。** 需要给设计、研发或评审会时，它可以继续整理成产品设计文档、精简 PRD 或交付稿。

## 两种开始方式

### 1. 我有一个新想法

适合一句 idea、新能力、MVP、创业验证、组内讨论或领导预览。

你可以先给：

- 产品想法
- 谁会在什么场景用
- 用户现在怎么解决
- 你希望它带来什么变化
- 约束、参考或竞品

PMWorkspace 会先判断这个机会是否成立、最小切口是什么、哪些信息可以先假设、哪些信息必须补齐。

### 2. 我要优化已有功能

适合线上页面优化、已有流程改版、数据下降、用户反馈集中、截图反馈或生产样式继承。

你可以先给：

- 生产截图或关键节点截图
- 线上 URL、Figma / 设计稿或等价视觉基线
- 当前数据、业务现状或用户反馈
- 你希望优化的目标

PMWorkspace 会先判断问题区域、必须保留的线上结构、可以挑战的地方，以及为什么新方案会比当前方案更好。

如果缺截图或等价视觉基线，它不会直接给三套方案。它会先说明为什么缺基线会影响判断，以及你补齐后能解锁什么。

## 你会拿到什么结果

- **讨论稿：** 适合先拿去开会、和老板对齐、和组内讨论。它会明确标注哪些是事实、哪些是假设。
- **产品简报：** 适合出原型前统一口径，包含目标用户、真实问题、关键路径、主目标、风险和待确认信息。
- **3 个以上方案方向：** 适合比较不同取舍，而不是只看一个“像完成稿”的答案。
- **移动端原型图：** 默认一个方案一个屏幕单独出图，便于逐张评审和修改。
- **交付稿：** 适合继续给设计、研发、评审或实验验证使用。

## 复制这段开始

安装 **AI 产品工作站** 后，从 `$pm-workspace` 开始。

如果你不确定怎么描述，直接发这句：

```text
使用 $pm-workspace 帮我判断这个产品想法应该怎么推进。请先告诉我当前判断、还缺什么、不补会有什么偏差，以及补齐后能产出什么。
```

也可以按场景复制：

### 新想法

```text
使用 $pm-workspace 处理一个新想法。请先判断它是否值得继续，再帮我整理成可讨论的产品说明和至少 3 个方案方向。

产品想法：<一句话描述>
目标用户：<谁在什么场景最需要>
当前替代：<用户现在怎么解决>
已知约束：<业务 / 数据 / 设计 / 上线范围>
参考材料：<竞品 / 截图 / PRD / 协作文档，可为空>
我想要的结果：<讨论稿 / 原型 / PRD / 交付稿>
```

### 优化已有功能

```text
使用 $pm-workspace 帮我优化一个已有功能。请先基于截图、线上参考或现有反馈判断问题区域，再告诉我应该怎么改。

当前页面或流程：<页面 / 功能 / 链路>
线上材料：<截图 / 关键节点截图 / URL / Figma>
核心问题：<用户或业务现在卡在哪里>
目标：<希望提升的行为或指标>
约束：<数据 / 业务 / 法务 / 设计系统 / 上线范围>
我想要的结果：<讨论稿 / 原型 / PRD / 交付稿>
```

如果你要原型或 PRD，也可以直接写在“我想要的结果”里。PMWorkspace 会先确认产品说明、线上参考、方案差异和不能虚构的内容，再继续出图或交付。

## 安装和维护

<details>
<summary>展开安装、命令、更新和维护者信息</summary>

### 安装

公开插件用户：在 Codex `Plugins` 中安装 **AI 产品工作站**。

GitHub 本地 plugin / 团队测试：

```bash
codex plugin marketplace add stephenfan80/PMWorkspace
```

如果之前添加过旧版本或本地路径：

```bash
codex plugin marketplace remove pmworkspace
codex plugin marketplace add stephenfan80/PMWorkspace
```

开发者本地仓库：

```bash
git clone https://github.com/stephenfan80/PMWorkspace.git
cd PMWorkspace
bin/pmw-upgrade --host codex-plugin
```

详细升级、旧版 skill、发布提交说明统一看 `docs/codex-plugin-submission.md` 和 `pmworkspace-shared/references/update-workflow.md`。

### 工作台地图

PMWorkspace 的端到端工作台地图由 `pmworkspace-shared/references/pm-workbench-map.md` 维护。README 只讲产品体验和入口，不维护第二套路由表。

核心链路：

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

### 常用命令

```bash
bin/pmw-dashboard status
bin/pmw-dashboard status --details
bin/pmw-dashboard readiness --target prototype
bin/pmw-dashboard readiness --target handoff
bin/pmw-artifact flow
bin/pmw-artifact latest --kind product_brief
bin/pmw-prototype-board list
bin/pmw-version --json
bin/pmw-update-check --quick
```

### 维护索引

- **Product Readiness Dashboard：** 出图 / 交付前总控面板，使用 `bin/pmw-dashboard readiness --target prototype|handoff` 检查产品简报、可选协作文档（Zoon）、线上参考、方案差异、设计规范目标、不可虚构项和复审状态。
- **Product Artifact Flow：** 产品简报、原型清单、复审结论和交付稿会登记为下游可读产物；浏览器证据用 `bin/pmw-artifact add --kind browser_evidence` 进入同一条产物流。
- **PM Review Army / Product Review Squad：** 原型复审先运行策略、信任 / 风险、设计系统、数据可行性四个可插拔专家；深度交付、高风险、批量交付、研发交付或多角色 review 时，追加 CEO、Eng、Design、DX、安全、QA、发布工程师短结论。
- **Zoon 协作：** 已启用在线协作文档时，可用 `bin/pmw-zoon join --url <Zoon URL>` 加入协作态，再做同步和漂移检查。
- **Skill Doc Generator：** 共享契约由 `bin/pmw-gen-skill-docs write` 生成，用 `bin/pmw-gen-skill-docs check` 检查。

### 原型输出规则

- 默认移动端优先。
- 一个方案 + 一个屏幕 = 一张图。
- 默认至少 3 个方案，少于 3 个必须说明原因。
- HTML 只在你明确要求“HTML / 可交互网页 / 前端实现 / 本地网页原型”时使用。
- 深度交付中，产品简报没有“已对齐”前，不写 image-2 提示词，不生成图片，不输出交付稿。
- 用户提供截图或线上参考时，只更新视觉基线和参考状态，不自动产出完整方案、HTML 或原型图。

### 协作文档命令

```bash
bin/pmw-zoon join --url "<协作文档 URL>"
bin/pmw-zoon drift --url "<协作文档 URL>"
bin/pmw-zoon read --url "<协作文档 URL>"
```

### 维护者命令

```bash
bin/pmw-eval list
bin/pmw-eval run
bin/pmw-build-plugin
bin/pmw-gen-skill-docs write
bin/pmw-gen-skill-docs check
```

### 更新

每个 skill 使用前都会执行快速更新检查：`pmw-update-check --quick` 会优先复用短缓存，并用短超时比较 `VERSION` 和远端插件包 `REVISION`。

如果快速检查输出 `UPGRADE_AVAILABLE`，Agent 会先询问是否现在更新；只有用户确认，或本地配置 `auto_upgrade=true`，才会执行升级命令。

执行 `pmw-upgrade` 时，会先删除所选安装目标里的 PMWorkspace 旧版本目录，再写入最新版本；不会删除 `~/.pmworkspace` 中的项目状态、产品简报、原型、交付稿或审计记录。

### 本地状态和隐私

PMWorkspace 默认把资产保存在本地 `~/.pmworkspace/`，包括业务简报、本地审计副本、用户确认过的决策、协作文档链接、产物流动记录、复审专家短结论、原型清单、交付稿、脱敏交付事实、偏好反馈和本地使用日志。

不会保存 token、owner secret、API key、cookie、原始客户资料、内部材料、会议记录、敏感截图、未脱敏协作文档内容或 API 原始响应。默认遥测是本地优先，只写入 `~/.pmworkspace/analytics/usage.jsonl`；远程匿名汇总必须由用户明确开启。

改动 source skill、`pmworkspace-shared/references`、`bin`、`evals`、README 或插件 assets 后，必须运行 `bin/pmw-build-plugin`，并把插件副本变化一起提交。

</details>

## 许可证

MIT

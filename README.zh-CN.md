# PMWorkspace

PMWorkspace 是一个面向产品经理、设计师、研究员、运营和创业者的产品工作台。它把产品想法、PRD、截图、访谈洞察或 Zoon 文档，沉淀成可复用的产品资产：产品决策、对齐后的产品简报、移动端优先的 image-2 原型图、设计反馈和交付稿。

PMWorkspace 来自原来的 `product-prototype-designer` 技能。旧名称已废弃，后续请使用 `$pm-workspace` 和 PMWorkspace 技能套件。

## 它解决什么问题

很多原型失败不是因为图不好看，而是问题没有定义清楚。PMWorkspace 的原则是：

```text
先定义问题
-> 再挑战策略
-> 再固化产品简报
-> 再生成移动端优先的原型图
-> 最后沉淀可交付资产
```

## 技能套件

| 技能 | 什么时候用 |
|---|---|
| `$pm-workspace` | 主入口，负责路由、首次引导、更新检查和状态记录。 |
| `$pm-jobs` | 乔布斯式产品追问：用户是谁、痛点是什么、现在怎么解决、为什么值得做。 |
| `$pm-strategy-review` | 挑战策略、范围、价值交换、风险、反指标和取舍。 |
| `$pm-brief` | 生成快速版、标准版或深度版产品简报。 |
| `$pm-prototype-shotgun` | 基于已对齐的产品简报生成多方案 image-2 原型图。 |
| `$pm-handoff` | 输出适合 PRD、设计、实验验证或研发使用的交付稿。 |

## 快速开始

```text
使用 $pm-workspace 帮我梳理这个产品想法，并在确认后生成原型方案。
产品想法：<一句话描述>
目标用户：<谁>
用户问题：<他们现在卡在哪里>
目标：<希望提升的行为或指标>
约束：<数据 / 业务 / 法务 / 设计系统 / 上线范围>
输出：<只要产品简报 / 1 个屏幕 / 2 个屏幕 / 3 个方案 / 交付稿>
要求：每个方案和屏幕单独生成一张图，不要合成在同一张图里。
```

## 默认工作流

1. `$pm-workspace` 判断任务类型并路由。
2. `$pm-jobs` 先问清楚产品问题和最小有价值版本。
3. `$pm-strategy-review` 在高风险或范围不清时挑战方向。
4. 关键 PM 决策用选择题拍板，一次最多 3 个问题。
5. `$pm-brief` 写出可确认、可复用的产品简报，并默认创建 Zoon 在线文档。
6. 产品简报达到“已对齐”后，`$pm-prototype-shotgun` 先读取 Zoon 最新内容，再生成 image-2 原型图。
7. `$pm-handoff` 把选定方向转成可交付文档。

## 原型输出规则

- 默认移动端优先：iPhone 17 竖屏 `402 x 874`。
- 只有用户明确要求桌面端，或看板 / 内部工具确实需要大屏密度，才使用桌面端。
- 产品简报没有“已对齐”前，不写图片提示词，也不生成图片。
- 多方案必须在产品策略、信息架构、交互模型或信任模型上不同，不能只是换颜色。
- 一个方案 + 一个屏幕 = 一张图。
- `3 个方案 x 2 个屏幕` = 6 张独立图片。
- 禁止把多个方案合成在一张比较图里，除非用户明确要展示板。

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
  projects/<slug>/briefs/
  projects/<slug>/decisions.jsonl
  projects/<slug>/questions.jsonl
  projects/<slug>/project.json
  projects/<slug>/prototypes/
  projects/<slug>/taste-profile.jsonl
```

会保存：

- 技能使用记录。
- 中文项目名和 Zoon 在线简报链接。
- 用户确认过的产品/设计决策。
- 选择题拍板记录。
- 产品简报 Markdown。
- 原型批次清单。
- 用户批准或拒绝的设计偏好。

不会保存：

- token、owner secret、API key、cookie。
- 原始客户资料、内部录音、敏感截图。
- 未脱敏 Zoon 内容。
- Zoon ownerSecret 或 API 原始响应。
- 用户没有明确要求保存的私密 PRD 原文。

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

Zoon 在线简报：

```bash
cat brief.md | bin/pmw-zoon create --title "产品设计简报：通用券站外召回方案"
cat brief.md | bin/pmw-zoon append --url "<Zoon URL>"
bin/pmw-zoon read --url "<Zoon URL>"
```

## 选择题拍板

PMWorkspace 不应只输出“还需要你拍板 5 个问题”。凡是会改变产品方向、原型范围、实验口径、用户承诺或交付稿的关键点，都要变成选择题：

```text
D1 - “全品牌可用”的对外口径
为什么重要：口径过大容易形成无条件承诺，用户发现部分品牌不可领时会损害信任。
推荐选择：A，因为它既能表达覆盖面，又保留真实业务边界。

选项 A：参与品牌可领取
选项 B：全品牌可参与查询
选项 C：全品牌都有机会领

取舍：增长吸引力 vs 承诺真实性。
默认假设：如果你不改，我会按 A 继续。
```

## 更新提醒

每个 skill 使用前会尝试检查 `VERSION`。如果 GitHub 上有新版本，会提示：

```text
UPGRADE_AVAILABLE <local> <remote>
```

升级：

```bash
bin/pmw-upgrade --host codex
```

暂缓某个版本：

```bash
bin/pmw-snooze-update <remote-version>
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

# AI 产品工作站 Codex Plugin 上架提交材料

本文档用于准备 **AI 产品工作站**（powered by PMWorkspace）进入 Codex 插件库 / 插件目录时的提交材料。提交前先运行：

```bash
bin/pmw-build-plugin
bin/pmw-gen-skill-docs check
bin/pmw-eval run
```

## 插件基础信息

- Plugin name: `pmworkspace`
- Display name: `AI 产品工作站`
- Category: `Productivity`
- Developer: `Stephen Fan`
- Repository: `https://github.com/stephenfan80/PMWorkspace`
- Homepage: `https://github.com/stephenfan80/PMWorkspace`
- License: `MIT`
- Version source: 根目录 `VERSION` 与 `plugins/pmworkspace/.codex-plugin/plugin.json` 保持一致
- Package path: `plugins/pmworkspace`

## 一句话介绍

AI 产品工作站 helps product managers turn ideas, PRDs, screenshots, and feedback into aligned product briefs, image-2 prototype directions, reviews, and compact handoff assets.

## Short Description

Product briefs, image-2 prototypes, reviews, and PRDs

## Long Description

AI 产品工作站, powered by PMWorkspace, is a product workbench for product managers. It turns fuzzy ideas, PRDs, screenshots, customer insight, or prototype requests into quick shaping or deep delivery workflows. It captures assumptions, goals, counter-metrics, constraints, and non-fiction boundaries; produces aligned product briefs; supports mobile-first image-2 prototype directions; reviews prototypes against product intent; and prepares compact PRD or design handoff assets.

## 默认 Prompt

```text
用 AI 产品工作站把这个产品想法快速成型为产品简报、方案方向和移动端原型图。
用 AI 产品工作站把这份 PRD 或截图反馈整理成可出图产品简报。
用 AI 产品工作站复审这批原型，并整理成精简 PRD 交付稿。
```

## 搜索关键词

```text
pmworkspace
ai-product-workstation
ai-product-workbench
product-manager
product-manager-workflow
product-management
product-discovery
product-strategy
product-requirements
prd
requirements
prototype
ui-prototype
mobile-prototype
product-brief
brief
image-2
screenshot-feedback
ux-review
prototype-review
user-feedback
design-handoff
handoff
AI 产品工作站
AI产品工作站
产品经理
产品简报
产品原型
原型图
截图反馈
设计评审
精简PRD
```

## 截图素材

提交包会生成这些 PNG：

- `plugins/pmworkspace/assets/screenshot-onboarding.png`：展示工作方式选择和可见 workflow card。
- `plugins/pmworkspace/assets/screenshot-brief.png`：展示从 idea / PRD / screenshot feedback 到产品简报。
- `plugins/pmworkspace/assets/screenshot-prototype.png`：展示 image-2 原型单元、复审门槛和 PRD handoff。

图标素材：

- `plugins/pmworkspace/assets/icon.png`
- `plugins/pmworkspace/assets/logo.png`

## 目标用户

第一目标用户是产品经理，尤其是这些场景：

- 一句话产品想法需要快速变成可讨论方案。
- PRD、截图反馈、用户洞察散落在不同地方，需要先压缩成产品简报。
- 设计要出移动端原型图，但目标、反指标、边界和事实来源还没对齐。
- 原型已经有了，需要用产品、风险、设计系统和数据可行性视角复审。
- 需要把已选方向整理成精简 PRD 或设计 / 研发交付稿。

## 用户可见安装与触发方式

公开插件库用户：

```text
Codex -> Plugins -> Search "AI 产品工作站" or "PMWorkspace" -> Install
```

公开上架审批前，它不会出现在默认插件市场搜索结果里。Beta / 团队测试用户先运行：

```bash
codex plugin marketplace add stephenfan80/PMWorkspace
```

或从本地仓库运行：

```bash
bin/pmw-upgrade --host codex-plugin
```

然后重启 Codex，在 `Plugins` 中把筛选从 `Built by OpenAI` 切到 `全部`，再搜索 `AI 产品工作站` 或 `PMWorkspace`。

安装后推荐触发：

```text
使用 $pm-workspace 把这个产品想法快速成型为产品简报、方案方向和移动端原型图。
```

也可以搜索：

```text
AI 产品工作站
PMWorkspace
product brief
PRD
prototype
product manager
image-2
产品经理
产品简报
原型图
截图反馈
```

## 隐私与数据说明

- PMWorkspace 默认只把运行状态、产品简报、决策、原型清单、复审结论和交付稿保存在用户本机 `~/.pmworkspace/`。
- 默认不上传项目名、文件路径、提示词正文、截图内容、产品简报正文或客户数据。
- 不应保存真实 token、ownerSecret、API key、cookie、内部录音、客户资料、私密截图或未脱敏 Zoon 内容。
- 远程匿名汇总必须由用户明确开启。

## 审核前检查清单

- `plugins/pmworkspace/.codex-plugin/plugin.json` 存在且 JSON 合法。
- `plugin.json` 的 `version` 与根目录 `VERSION` 一致。
- `plugin.json` 包含 `skills: "./skills/"`。
- 8 个核心 skill 和 `pmworkspace-shared` 都已复制到 `plugins/pmworkspace/skills/`。
- `assets/` 下存在 icon、logo 和 3 张 PNG screenshot。
- `bin/pmw-gen-skill-docs check` 通过。
- `bin/pmw-eval run` 通过。
- README 中公开插件、本地 plugin、旧版 skill 三种安装 / 更新路径一致。

## 插件 REVISION 策略

- `plugins/pmworkspace/skills/pmworkspace-shared/REVISION` 记录最近一次影响插件打包内容的 source commit，用来判断插件副本对应哪一次 source skill / references / bin / eval / README / 插件 listing assets 内容。
- `bin/pmw-revision` 会按插件打包输入路径计算 REVISION，`bin/pmw-build-plugin`、`setup` 和 `bin/pmw-upgrade` 必须复用它，不直接使用当前 `HEAD`；因此 artifact-only、审计报告、PPTX、讲稿、release note 或 revision-only 提交不会让插件 REVISION 追上维护性 HEAD。
- `bin/pmw-upgrade` 不允许使用浅克隆；浅克隆看不到路径历史，会把维护性 HEAD 误判成最近一次打包内容提交。
- 改动 source skill、`pmworkspace-shared/references`、`bin`、`evals`、README 或插件 assets 时，必须运行 `bin/pmw-build-plugin`，并把插件副本变化一起提交。
- 只修改本地交付 artifact、审计报告、PPTX、讲稿、release note 或不进入插件包的维护材料时，不刷新插件 REVISION，也不需要为了让 REVISION 追上 HEAD 单独提交。
- 若先提交 source 变化再刷新插件包，可以允许一个 revision-only commit；该 commit 只更新插件打包元数据，REVISION 仍应指向上一条真正影响插件内容的 source commit。

## 发布与更新说明

发布新版本时，让 AI 执行：

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

用户更新路径：

- 公开 Codex plugin 用户：从 Codex `Plugins` 页面更新 `AI 产品工作站`。
- GitHub 本地 plugin 用户：运行 `pmw-upgrade --host codex-plugin`。
- 旧版 `~/.codex/skills` 用户：运行 `pmw-upgrade --host codex`。

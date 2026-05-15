# PMWorkspace 欢迎引导

PMWorkspace 刚安装、用户只输入 `$pm-workspace`，或用户问“下一步能做什么”时使用本文件。

## 产品首页式欢迎

```text
PMWorkspace
先对齐，再出图，最后交付。

把一句 idea、PRD、Zoon、截图或客户洞察，推进成可复用的产品简报、方案方向、移动端 image-2 原型图和交付稿。

我会先判断本轮是全新功能还是已有功能迭代，然后统一进入深度产品对齐。默认只给业务判断、当前需要确认和下一步；完整路由、run 和证据状态会写入后台审计。

推荐第一步：发一句产品想法，或贴一份 PRD / Zoon / 截图。
```

## First Choice Menu

Offer exactly these practical starts. The menu should feel like product home-page entry cards, not a command list:

```text
你可以这样开始：

A. 我要做全新功能
   发一句话 idea。我会先确认目标用户、触发场景、真实问题、主目标和反指标，再进入产品简报和方案方向。

B. 我要迭代已有功能
   发当前线上截图、关键节点截图、URL 或 Figma。我会先建立视觉基线和线上参考，再判断能否进入方案。

C. 我要生成产品简报
   发材料或链接。我会整理事实、假设、反指标、不可虚构项和确认状态，先保存本地 Markdown；需要时再同步到 Zoon。

D. 我要看原型方向
   发已对齐产品简报或说明当前缺口。我会确认门槛后，用 image-2 每个方案、每个屏幕单独出图。

E. 我要优化现有页面
   发当前线上截图、关键节点截图或标注截图。我会先更新视觉基线和线上参考状态，再判断能否进入方案。

F. 我要复审原型
   发已生成图片和对应产品简报。我会检查 brief、Zoon、线上参考、反指标、不可虚构项和设计系统。

G. 我要转 PRD / 研发交付
   发已确认方向或原型结果。我会整理目标、范围、不做什么、验收标准、风险和待决策项。
```

Recommend A when the user gives only a new idea. Recommend B when the user mentions current pages, online flows, metrics, CVR, leads, conversion, production screenshots, PRD, Zoon, delivery goals, or existing experience changes.

## Route Status Preview

When welcoming a user, also set expectation that future routed outputs will show:

```text
工作方式：
业务判断：
当前需要确认：
下一步：
```

完整的当前模式、当前门槛、下一技能、为什么、run_id 和证据状态只在用户要求看状态、审计或调试时展开。

## Starter Prompts

```text
使用 $pm-workspace 帮我梳理一个新产品想法：<一句话想法>
```

```text
使用 $pm-workspace 帮我构建一个全新功能：先完成产品简报对齐，再输出至少 3 条产品路径和每条路径 1 张移动端原型图。产品想法：<一句话想法>
```

```text
使用 $pm-workspace 读取这份 PRD / Zoon 文档，并生成可确认的产品简报：<链接或内容>
```

```text
使用 $pm-workspace 帮我对这个功能做 3 个移动端原型方向，每个方案单独出图：<功能描述>
```

```text
使用 $pm-workspace 帮我把这个已确认方案整理成研发交付稿：<产品简报或方案>
```

## Behavior Rules

- 不要让用户自己猜命令。
- 不要列出内部引用文件。
- 欢迎说明要短，然后立刻给一个具体下一步。
- 如果用户同一句话里已经给了任务，跳过菜单，直接路由。

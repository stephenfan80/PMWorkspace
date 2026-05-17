# PMWorkspace 欢迎引导

PMWorkspace 刚安装、用户只输入 `$pm-workspace`，或用户问“下一步能做什么”时使用本文件。

## 产品首页式欢迎

```text
PMWorkspace
对齐、出图、复审、交付。
先对齐，再出图，最后交付。

把一句 idea、PRD、Zoon、截图或客户洞察，推进成可复用的产品简报、移动端 image-2 原型图、原型复审结论和交付稿。

你只要告诉我现在想做哪一步：对齐、出图、复审或交付。我会先判断本轮是全新功能还是已有功能迭代，然后停在当前最早门槛。默认只给业务判断、当前需要确认和下一步；完整路由、run 和证据状态会写入后台审计。

推荐第一步：如果不确定，就选“对齐”，发一句产品想法，或贴一份 PRD / Zoon / 截图。
```

## First Choice Menu

Offer exactly these four action cards. The menu should feel like product home-page entry cards, not a command list:

```text
你可以这样开始：

A. 我要对齐
   发一句话 idea、PRD、Zoon、截图或客户洞察。我会先判断全新功能 / 已有功能迭代，再确认真实问题、目标用户、当前替代、主目标、反指标和产品简报状态。
   常见说法：我要做全新功能 / 我要迭代已有功能 / 我要生成产品简报。兼容旧入口：A. 我要做全新功能。

B. 我要出图
   发已对齐产品简报，或说明当前缺口。我会先跑出图前准备度，确认 brief、线上参考、方案差异和不可虚构项，再用 image-2 每个方案、每个屏幕单独出图。
   常见说法：我要看原型方向 / 我要优化现有页面 / 我要 3 个移动端方案。

C. 我要复审
   发已生成图片和对应产品简报。我会检查 brief、Zoon、线上参考、反指标、不可虚构项和设计系统，判断可通过、需要重出、需要补参考还是需要 PM 拍板。
   常见说法：我要复审原型 / 看看这张图能不能交付。

D. 我要交付
   发已确认方向或原型结果。我会整理目标、范围、不做什么、验收标准、风险和待决策项。
   常见说法：我要转 PRD / 研发交付 / 设计评审材料。
```

Recommend A when the user gives only a new idea or unclear materials. Recommend A first when the user mentions current pages, online flows, metrics, CVR, leads, conversion, production screenshots, PRD, Zoon, delivery goals, or existing experience changes but no aligned brief exists. Recommend B only when the aligned brief and needed references are ready. Recommend C after images exist. Recommend D after review passes or the user asks for delivery based on confirmed direction.

## Route Status Preview

When welcoming a user, also set expectation that future routed outputs will show:

```text
工作方式：
当前动作：
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
使用 $pm-workspace 帮我先对齐这个全新功能：先判断是否值得做，再整理产品简报和至少 3 条产品路径。产品想法：<一句话想法>
```

```text
使用 $pm-workspace 读取这份 PRD / Zoon 文档，并先对齐成可确认的产品简报：<链接或内容>
```

```text
使用 $pm-workspace 帮我对这个已对齐 brief 出 3 个移动端原型方向，每个方案单独出图：<brief 或功能描述>
```

```text
使用 $pm-workspace 复审这些原型图，并判断哪些可以继续交付：<图片和产品简报>
```

```text
使用 $pm-workspace 帮我把这个已确认方案整理成研发交付稿：<产品简报、复审结论或方案>
```

## Behavior Rules

- 不要让用户自己猜命令。
- 不要列出内部引用文件。
- 欢迎说明要短，然后立刻给一个具体下一步。
- 如果用户同一句话里已经给了任务，跳过菜单，直接路由。

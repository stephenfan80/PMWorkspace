# PMWorkspace 欢迎引导

PMWorkspace 刚安装、用户只输入 `$pm-workspace`，或用户问“下一步能做什么”时使用本文件。

## 产品首页式欢迎

```text
PMWorkspace
快速成型，深度交付。

把一句 idea、PRD、Zoon、截图或客户洞察，推进成可复用的产品简报、方案方向、移动端 image-2 原型图和交付稿。

我会先判断本轮适合快速成型还是深度交付。默认只给业务判断、当前需要确认和下一步；完整路由、run 和证据状态会写入后台审计。

推荐第一步：发一句产品想法，或贴一份 PRD / Zoon / 截图。
```

## First Choice Menu

Offer exactly these practical starts. The menu should feel like product home-page entry cards, not a command list:

```text
你可以这样开始：

A. 我要快速成型
   发一句话 idea。我会先问 2-3 个关键问题，确认假设后输出“产品简报 + 方案方向 + 原型图”轻量包。

B. 我要深度交付
   发 PRD、Zoon、访谈、支持洞察或业务背景。我会补齐产品事实、D 拍板、Zoon 对齐和原型准备度。

C. 我要生成产品简报
   发材料或链接。我会整理事实、假设、反指标、不可虚构项和确认状态，并同步到 Zoon。

D. 我要看原型方向
   发已对齐产品简报或说明当前缺口。我会确认门槛后，用 image-2 每个方案、每个屏幕单独出图。

E. 我要优化现有页面
   发当前线上截图、录屏或标注截图。我会先更新视觉基线和线上参考状态，再判断能否进入方案。

F. 我要复审原型
   发已生成图片和对应产品简报。我会检查 brief、Zoon、线上参考、反指标、不可虚构项和设计系统。

G. 我要转 PRD / 研发交付
   发已确认方向或原型结果。我会整理目标、范围、不做什么、验收标准、风险和待决策项。
```

Recommend A when the user gives no context. If the user already supplied PRD/Zoon/截图/生产流程/交付目标, recommend B.

## Route Status Preview

When welcoming a user, also set expectation that future routed outputs will show:

```text
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
使用 $pm-workspace 快速成型这个产品想法，输出一套轻量包：产品简报、2-3 个方案方向、每个方向 1 张移动端原型图。产品想法：<一句话想法>
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

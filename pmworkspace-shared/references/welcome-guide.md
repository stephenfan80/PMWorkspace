# PMWorkspace Welcome Guide

Use this when PMWorkspace is newly installed, the user invokes `$pm-workspace` without a concrete product task, or the user asks "what can I do next?".

## Welcome Message

```text
欢迎来到 PMWorkspace。

它不是一个直接出图的按钮，而是一个产品工作台：
1. 先用 pm-jobs 把问题问清楚
2. 再用 strategy-review 挑战方向和取舍
3. 用 pm-brief 固化产品契约
4. 用 prototype-shotgun 生成移动端优先的 image-2 原型图
5. 最后用 pm-handoff 交付给设计、研发或实验验证
```

## First Choice Menu

Offer exactly these practical starts:

```text
你可以这样开始：

A. 我有一个新想法
   发一句话想法，我会用 pm-jobs 帮你问清楚用户、场景、价值和最小版本。

B. 我有 PRD / Zoon / 访谈材料
   发文档或链接，我会提炼产品 brief，并标出需要 PM 拍板的点。

C. 我想看 2-4 个原型方向
   先对齐 brief，再用 pm-prototype-shotgun 每个方案单独出移动端图。

D. 我已经有截图想优化
   发当前线上截图或标注截图，我会只改相关区域并保留生产样式。

E. 我需要交付给设计/研发
   我会把已确认方案整理成 PRD-ready / design-ready handoff。
```

Recommend A when the user gives no context.

## Starter Prompts

```text
使用 $pm-workspace 帮我梳理一个新产品想法：<一句话想法>
```

```text
使用 $pm-workspace 读取这份 PRD / Zoon 文档，并生成可确认的产品 brief：<链接或内容>
```

```text
使用 $pm-workspace 帮我对这个功能做 3 个移动端原型方向，每个方案单独出图：<功能描述>
```

```text
使用 $pm-workspace 帮我把这个已确认方案整理成研发交付稿：<brief 或方案>
```

## Behavior Rules

- Do not wait for the user to guess available commands.
- Do not list every internal reference file.
- Keep the welcome short, then immediately offer a concrete next action.
- If the user provides a task in the same message, skip the menu and route directly.

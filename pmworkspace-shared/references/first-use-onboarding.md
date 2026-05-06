# 首次使用引导

Use this when the user first invokes PMWorkspace in a thread, starts a new product topic, or provides only a rough product idea. The goal is to route the work and gather the minimum context needed for a useful product brief.

For Chinese users, make the first response feel like a Chinese product app onboarding screen: short orientation, Chinese labels, one recommended next step, and no English section names unless they are product terms such as `PRD`, `Zoon`, or `image-2`.

## 需要识别的信息

- **用户角色：** 产品经理、设计师、研究员、运营、创业者或其他产品协作者。
- **输入来源：** Zoon 文档、PRD、截图、研究/通话记录、指标、Figma/设计系统，或一句产品想法。
- **变化类型：** 新功能、现有功能迭代，或暂不明确。
- **协作方式：** 使用现有 Zoon 文档、新建/更新 Zoon 产品简报，或把产品简报留在对话里。
- **期望输出：** 只要产品简报、一个移动端原型屏、两个关联屏、多方案原型、交付稿，或截图修改。
- **设计基线：** 默认使用 AutoDesign 生产基线；如果用户提供更强的设计系统，则以用户提供的为准。

## 首轮问题

Ask only the questions that are not answered by the user's prompt or attached materials.

Use these in order:

1. 这是新功能，还是现有线上功能迭代？
2. 如果是现有功能迭代，当前线上截图或录屏在哪里？
3. 这个原型要服务哪个用户问题和主产品目标？
4. 你希望交付什么：产品简报、一个移动端屏幕、两个关联屏、多方案原型、交付稿，还是截图修改？

If the user provides a Zoon URL, follow `zoon-workflow.md`, announce presence, and read the doc only after the task requires it.

## 开始前输出

Before creating the brief, summarize:

```text
开始前确认：
- 用户角色：
- 输入来源：
- 变化类型：
- 现状基线：
- 场景路由：
- 期望输出：
- 设计基线：
- 阻塞项：
```

如果“阻塞项”不为空，先停下来向用户索取缺失项。对现有功能迭代来说，缺少当前线上截图就是阻塞项。

## 默认规则

- 默认输出是已对齐的产品简报，然后再进入 image-2 原型图或交付稿。
- 默认原型设备是移动端优先：iPhone 17 竖屏 `402 x 874`。
- 只有用户明确要求桌面端，或场景是看板/内部工具且确实需要大屏密度时，才使用桌面端。
- 默认视觉系统是 AutoDesign 生产基线。
- 如果用户提供 Zoon 文档，默认把 Zoon 作为协作事实来源。
- 不要默认加入手机号、留资、付款、登录或其他高成本动作，除非产品上下文确实需要。

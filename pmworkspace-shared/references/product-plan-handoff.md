# Product Plan Handoff

Use this after first-use onboarding, scenario routing, decision gates, and the PM Jobs pass. The brief must be aligned before prototype generation.

The handoff is an adaptive product design brief, not a fixed PRD. Its job is to make product intent editable, confirmable, reusable by later agents, and safe to hand off to design or product partners. It is the alignment gate between product thinking and image generation.

## Always Create Or Update A Brief

Create or update a brief for every prototype request. Include version and confirmation status. Choose the smallest useful format:

- **Quick Brief:** screenshot iteration, narrow page change, or a single product/design decision.
- **Standard Brief:** most product prototype requests where intent and constraints should persist.
- **Deep Brief:** new feature, high-risk flow, cross-team collaboration, unclear evidence, or sensitive data/operations.

Do not skip the brief because the user wants speed. A speed-oriented request should become a Fast Alignment Brief with explicit assumptions and a confirmation step.

If the user already provided a complete Zoon product document, create a short alignment summary that points to the latest Zoon snapshot as the source of truth.

## Version And Status

Every brief should carry:

- `Brief version`: start at `v1`; increment when the user changes product direction.
- `Confirmation status`: `Draft`, `Ready for PM confirmation`, or `Aligned`.
- `Source of truth`: chat, existing Zoon doc, new Zoon doc, screenshot set, or user-provided PRD.
- `Last decision`: the latest user-confirmed product/design decision.

## Brief Depth

Choose the smallest useful depth.

### Quick Brief

Use for screenshot iterations and narrow changes.

Include:

- Current understanding
- Requested change or goal
- Constraints
- Prototype strategy
- PM supplement or approval items

### Standard Brief

Use for most product prototype work.

Include:

- Current understanding
- Goals and tasks
- Constraints
- Available data
- Adversarial design tradeoffs
- Prototype strategy
- PM supplement or approval items

### Deep Brief

Use for new features, high-risk product choices, cross-team work, sensitive data, transaction/service flows, or unclear evidence.

Include everything in Standard Brief plus:

- Evidence and current behavior
- Alternatives considered
- Design decision record
- Open questions

## Alignment Gate

Before writing image prompts or generating prototype images, the brief must be aligned by one of these signals:

- The user confirms the brief in chat.
- The user edits or approves the Zoon brief and asks the agent to use the latest version.
- The user explicitly says to use the assumptions listed in the brief.

If none of these signals exists, stop after sharing the brief or Zoon link and ask the user to confirm or edit it.

For iterative screenshot changes, a Quick Brief can be as short as:

```markdown
## Quick Alignment Update
- Product intent unchanged:
- Change requested:
- Keep unchanged:
- Constraint:
- 请确认：按以上范围只改这些区域后再出图。
```

## Core Shape

Do not force every section to be filled. Prefer readable prose with short bullets. Mark uncertainty explicitly.

```markdown
# 产品设计 Brief：{功能名}

## Brief 状态
- Brief version：v1
- Confirmation status：Draft / Ready for PM confirmation / Aligned
- Source of truth：{Chat / Zoon / PRD / Screenshot set}
- Last decision：

## 当前理解
{用 3-5 句话说明用户问题、业务目标、当前约束}

## 功能类型与现状基线
- 功能类型：{全新功能 / 现有功能迭代}
- 现有线上截图：{已提供 / 缺失 / 不适用}
- 场景路由：{新功能 / 现有迭代 / 转化 / 结果报告 / Dashboard / 内部工具 / 交易服务 / 内容社区 / 截图迭代}
- 现状问题：
- 需要保留：

## 目标与任务
- 用户任务：
- 主目标：
- 反指标：
- 不应牺牲：

## 当前约束
- 业务约束：
- 数据约束：
- 设计/组件约束：
- 不可新增能力：

## 对抗审查后的设计取舍
- 应优先展示：
- 应删除/弱化：
- 应后置：
- 需要标注不确定：
- 不能虚构：

## 方案方向
- 选定方向：
- 备选方向：
- 放弃方向：
- 原因：

## 原型策略
{页面结构、首屏重点、主要动作、结果页如何兑现价值}

## 决策记录
- 选定方向：
- 放弃方向：
- 原因：
- 对原型的影响：

## 请 PM 补充或拍板
- [ ] 若为现有功能迭代，请补充线上功能截图或确认已有截图就是当前线上版本
- [ ] {问题 1}
- [ ] {问题 2}
```

## Scenario Modules

Add only the modules that fit the product. Do not include all modules by default.

### Conversion Flow

- Value exchange before costly action.
- Required versus optional input.
- Trust, complaint, or opt-out risk.
- Counter-metric to prevent low-quality conversion.

### Result Or Report Page

- Promise made before the result.
- Data credibility and freshness.
- Estimated versus confirmed values.
- Next step and uncertainty handling.

### Internal Tool

- Repeated task and expected speed gain.
- Error recovery and audit trail.
- Permissions and role boundaries.
- Empty, partial, stale, and failed states.

### Transaction Or Service

- Eligibility and required materials.
- Fulfillment status.
- Exception paths and recovery.
- Human or partner dependency.

### Content Or Community

- Creation or consumption motivation.
- Quality signal.
- Participation loop.
- Moderation or abuse risk.

### Dashboard Or Analytics

- Decision the user should make.
- Data freshness.
- Comparison baseline.
- Alert threshold or action trigger.

## Markers For Collaboration

Use these markers so the PM knows where to edit:

- `当前假设：` when the agent inferred something.
- `请补充：` when missing context would improve the prototype.
- `请拍板：` when a product tradeoff needs a decision.
- `不可虚构：` when the design must not show unsupported data or functions.

## Zoon Handoff

If the user gave an existing Zoon doc:

- Append the brief to that doc unless the user asks for a new doc.
- Use the Zoon workflow and append operations.
- Tell the user the existing doc is now the source of truth for the next prototype step.
- Ask the user to confirm in chat or edit the Zoon brief before image generation.
- If the user changes direction in Zoon, increment `Brief version` and re-run relevant decision gates.

If there is no existing Zoon doc and the user wants online collaboration:

- Create a new Zoon document using the public document creation endpoint from the active Zoon host.
- If no host is provided, default to `https://zoon.up.railway.app`.
- Send only the returned editable `url` to the user.
- Do not expose `ownerSecret`, raw tokens, or API response internals.

If Zoon creation fails:

- Provide the brief markdown in chat.
- State the failure briefly and offer to retry when Zoon is reachable.

## Before Prototype Generation

When an editable Zoon brief exists and the user has confirmed it:

1. Re-read the latest Zoon snapshot before generating images.
2. Treat the latest markdown as the product source of truth.
3. Use PM edits to update product intent, constraints, and prompt content.
4. Do not rely only on stale chat history.

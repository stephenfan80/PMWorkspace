# 自适应对抗审查

决定原型策略前使用。目标是暴露薄弱前提，并把它们转成更好的设计选择。不要跑固定清单，要选择适合当前产品的审查视角。中文用户场景下，输出标题和字段全部使用中文。

## 审查结构

1. 说出当前方向隐含的三个最强前提。
2. 从下面的问题库中选择 3-5 个审查视角。
3. 每个视角用一句话说明风险。
4. 把审查结果转成原型决策。

使用这个格式：

```text
对抗审查：
- 前提 1：
- 前提 2：
- 前提 3：
- 使用视角：
- 原型决策：
  - 优先展示：
  - 删除或弱化：
  - 后置：
  - 标注为估算/不确定：
  - 不可虚构：
```

## Challenge Lens Library

### Problem Reality

Use when the feature is new or the problem sounds abstract.

- Is this a real user pain or a team-invented desire?
- What observed behavior proves the pain exists?
- What happens if the product does nothing?

### Specific User

Use when the audience is broad.

- Who exactly needs this most?
- What situation makes the problem urgent?
- What consequence does this user face if the task fails?

### Status Quo Competition

Use when the proposed flow assumes users will adopt it.

- What workaround already solves this well enough?
- What must the design beat: speed, trust, completeness, price, social proof, habit?
- Where does the current workaround fail?

### Value Exchange

Use for signup, phone, payment, permission, location, install, or other user-costly actions.

- Is the requested user effort proportional to the value shown?
- What useful value can be shown before the costly action?
- What becomes more specific or more reliable after the action?

### Free Information Boundary

Use when the flow gates information.

- Is this basic information the product should provide for free?
- Would gating it reduce trust or create complaint risk?
- What should be a preview, and what should require personalization or confirmation?

### Friction Cost

Use for forms, filters, onboarding, setup, and multi-step flows.

- Which field, step, or choice is not required before the primary action?
- Does every input improve the result enough to earn its place?
- Can optional precision move to a result page, drawer, or second step?

### Trust And Privacy

Use when the user gives personal data, money, location, identity, or sensitive context.

- Does the UI explain why the data is needed?
- Does the page make follow-up, storage, or sharing expectations clear?
- What copy reduces surprise without adding fear?

### Data Credibility

Use for estimates, rankings, scores, AI output, reports, prices, or recommendations.

- What data is fresh, estimated, inferred, or user-provided?
- What caveat must be visible for the result to feel honest?
- What would a skeptical user challenge?

### Feasibility And Delivery

Use when the design suggests new data, automation, fulfillment, or human operations.

- Can the product actually deliver what the screen promises today?
- What requires manual confirmation, partner inventory, policy lookup, or backend work?
- Which proposed function should not appear until it exists?

### Business Conflict

Use when business goals may fight user goals.

- Where does the business objective push against user trust?
- What design makes the exchange feel fair?
- What complaint, support ticket, churn, or regulatory risk could this create?

### Metric Gaming

Use when optimizing conversion, engagement, retention, or revenue.

- Could this design improve the metric while harming real user outcomes?
- What counter-metric should protect trust or quality?
- What behavior would look successful in analytics but bad in reality?

### Edge Cases

Use when results depend on availability, eligibility, permissions, data quality, or unusual users.

- What happens with missing, empty, stale, or contradictory data?
- What if the user is ineligible, not ready, already completed the task, or changes their mind?
- How should uncertainty and recovery appear?

### Design System Fit

Use when a design system or production constraint is named.

- Does the UI reuse known components instead of inventing new shapes?
- Are colors, typography, spacing, and interaction patterns plausible for production?
- Does the screen avoid decorative filler that would not ship?

## 产品类型默认审查视角

Use these as starting points, then adjust.

- **转化：** 价值交换、摩擦成本、信任/隐私、指标游戏。
- **结果/报告：** 数据可信度、免费信息边界、边界情况、下一步清晰度。
- **内部工具：** 现状替代方案、重复任务效率、错误恢复、权限边界。
- **交易/服务：** 可行性、资格判断、履约状态、异常处理。
- **内容/社区：** 具体用户、动机循环、质量信号、治理风险。
- **看板/数据分析：** 决策有用性、数据新鲜度、对比基线、提醒疲劳。
- **留资：** 价值交换、免费信息边界、摩擦成本、信任/隐私、业务冲突。

## 转成设计选择

The review is useful only if it changes the prototype. Convert findings into choices:

- 把最强用户价值放到第一个高成本动作之前。
- 删除不影响第一结果的字段。
- 把可选精度放到结果页、抽屉、筛选器或后续步骤。
- 在信任敏感处标注估算和假设。
- 只有真实存在人工跟进时，才解释人工跟进。
- 不添加产品无法支持的按钮、功能、数据或承诺。

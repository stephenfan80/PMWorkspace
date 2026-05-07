# 自适应对抗审查

决定原型策略前使用。目标是暴露薄弱前提，并把它们转成更好的设计选择。不要跑固定清单，要选择适合当前产品的审查视角。中文用户场景下，输出标题和字段全部使用中文。

## 审查结构

1. 说出当前方向隐含的三个最强前提。
2. 从下面的问题库中选择 3-5 个审查视角。
3. 每个视角用一句话说明风险。
4. 把审查结果转成原型决策。

## 策略取舍控制器

`$pm-strategy-review` 接住 `$pm-jobs` 或 `$pm-autoplan` 交出的策略门槛：范围、价值交换、信任/风险、反指标、可行性、定位或业务冲突。它不是重新做 Q 诊断，也不是直接写产品简报。

```text
来源门槛
-> 已确认事实
-> 策略风险类型
-> 3-5 个审查视角
-> 建议姿态：扩大 / 保持 / 收缩 / 转向
-> 策略取舍
-> 当前 D / 后续 D 队列
-> 下一技能
```

控制器规则：

- 如果缺少用户、问题、主目标、反指标或不可虚构项等基础事实，退回 `$pm-jobs` 问一个 `Q`，不要用策略审查替代事实诊断。
- 如果事实足够，但不同选择会改变范围、价值交换、用户承诺、实验口径、信任风险、可行性边界或交付责任，展开一个完整 `D` 并停止。
- 每轮只处理一个最重要的策略取舍；如果还有后续取舍，只输出 `后续 D 队列` 标题，不展开选项。
- 不要静默扩大范围、增加承诺、挪动反指标或把不可交付能力写进方案。
- 策略审查完成后，默认下一技能是 `$pm-brief`；如果仍缺事实，下一技能是 `$pm-jobs`；如果产品简报已对齐且只是复审方案方向，下一技能可以是 `$pm-prototype-shotgun` 或 `$pm-handoff`。
- 每次输出必须包含 `来源门槛`、`策略风险类型`、`使用视角`、`建议姿态`、`策略取舍`、`当前 D`、`下一技能` 和 `证据状态`。

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

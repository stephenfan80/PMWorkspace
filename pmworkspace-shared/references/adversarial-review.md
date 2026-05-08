# 策略取舍裁判

决定原型策略前使用。目标是暴露薄弱前提，把它们转成明确产品取舍，并让 PM 知道当前方向应该扩大、保持、收缩还是转向。不要跑固定清单，要选择适合当前产品的审查视角。中文用户场景下，输出标题和字段全部使用中文。

## 审查结构

1. 说出当前方向隐含的三个最强前提。
2. 指出一个最大策略矛盾。
3. 从下面的问题库中选择 3-5 个审查视角。
4. 每个视角用一句话说明风险，并转成一个产品动作。
5. 把审查结果转成 PM 可拍板的策略取舍。

## 策略取舍裁判

`$pm-strategy-review` 是 PMWorkspace 的策略取舍裁判：在 `$pm-jobs` 已经澄清产品价值后，判断方向应该扩大、保持、收缩还是转向，并把最大策略矛盾转成一个 PM 可拍板的取舍。

边界：

- 不重新做 `$pm-jobs` 的事实诊断。
- 不替 `$pm-brief` 写产品契约。
- 只负责识别最大策略矛盾，并转成明确取舍。
- 缺用户、问题、主目标、反指标、不可虚构项时，退回 `$pm-jobs` 问一个 `Q`。
- 策略审查后不能直接写 image-2 提示词，必须把已拍板策略交给 `$pm-brief` 写入产品契约。

## 范围模式

策略审查必须显式选择一个范围模式。范围模式不是口号，而是控制本轮审查如何处理野心、范围、风险和后续产品简报写法。

- **扩大模式：** 当前方向太小，无法解决真实损失或无法形成足够价值交换。默认动作是提出 1-2 个能显著提高价值的范围扩展，但每个扩展都必须标注前提、风险、反指标和不可虚构边界。不能静默增加承诺或把未来能力画进原型。
- **保持模式：** 当前方向基本正确，问题在表达、顺序、信任或局部取舍。默认动作是保留核心范围，只调整信息层级、价值交换、风险标注或优先级。不能借保持模式绕过最大策略矛盾。
- **收缩模式：** 当前范围过宽、用户任务不聚焦、第一版交付风险过高或反指标容易被破坏。默认动作是删除、后置或实验验证非关键范围，保留最小可赢切口。不能把收缩写成“体验缩水”，必须说明保住了哪个核心价值。
- **转向模式：** 当前方向和真实问题、目标用户、现状替代或可交付能力不匹配。默认动作是提出新的主问题或主路径，并说明旧方向为什么不应继续进入产品简报。不能在证据不足时强行转向；缺事实先退回 `$pm-jobs`。

选择规则：

- 如果最大策略矛盾来自价值不足或需求被低估，优先考虑 `扩大模式`。
- 如果最大策略矛盾来自范围蔓延、交付不可控、反指标风险或第一版不可验证，优先考虑 `收缩模式`。
- 如果最大策略矛盾来自错误用户、错误任务、错误价值交换或错误业务目标，优先考虑 `转向模式`。
- 如果当前方向能解决真实问题，且风险主要来自呈现顺序、边界标注或局部取舍，优先考虑 `保持模式`。
- 范围模式会改变范围、承诺、实验口径或交付责任时，必须转成一个策略 `D`，不能自动采用。

## 策略取舍控制器

`$pm-strategy-review` 接住 `$pm-jobs` 或 `$pm-autoplan` 交出的策略门槛：范围、价值交换、信任/风险、反指标、可行性、定位或业务冲突。它不是重新做 Q 诊断，也不是直接写产品简报。

```text
来源门槛
-> 已确认事实
-> 策略风险类型
-> 3-5 个审查视角
-> 最大策略矛盾
-> 范围模式：扩大模式 / 保持模式 / 收缩模式 / 转向模式
-> 建议姿态：扩大 / 保持 / 收缩 / 转向
-> 产品动作：删除 / 前置 / 后置 / 标注 / 禁止 / 实验验证
-> 策略取舍
-> 当前 D / 后续 D 队列
-> 下一技能
```

控制器规则：

- 如果缺少用户、问题、主目标、反指标或不可虚构项等基础事实，退回 `$pm-jobs` 问一个 `Q`，不要用策略审查替代事实诊断。
- 每轮必须指出一个最大策略矛盾，例如价值交换不成立、范围过宽、承诺不可交付、反指标被破坏、业务目标损害用户信任。
- 如果事实足够，但不同选择会改变范围、价值交换、用户承诺、实验口径、信任风险、可行性边界或交付责任，展开一个完整 `D` 并停止。
- 每轮只处理一个最重要的策略取舍；如果还有后续取舍，只输出 `后续 D 队列` 标题，不展开选项。
- 不要静默扩大范围、增加承诺、挪动反指标或把不可交付能力写进方案。
- 每轮必须输出一个 `范围模式`，并说明该模式如何处理范围、价值交换、反指标和不可虚构边界。
- `建议姿态` 必须说明理由，不能只写扩大、保持、收缩或转向标签。
- 每个审查视角必须落成一个产品动作：删除、前置、后置、标注、禁止或实验验证。
- 策略 `D` 必须包含推荐项、选项、风险、会影响什么、进入产品简报的写法。
- 策略审查完成后，默认下一技能是 `$pm-brief`；如果仍缺事实，下一技能是 `$pm-jobs`；如果产品简报已对齐且只是复审方案方向，下一技能可以是 `$pm-prototype-shotgun` 或 `$pm-handoff`。
- 交给 `$pm-brief` 时必须带上策略决策、最大策略矛盾、范围外、用户承诺边界、反指标保护和对原型的影响。
- 交给 `$pm-brief` 时必须带上 `范围模式` 和它进入产品简报的写法：扩大项、保留项、删除/后置项或转向后的新主问题。
- 每次输出必须先给 `策略审查结论`，再给 `策略取舍控制面板`；控制面板必须包含 `来源门槛`、`策略风险类型`、`使用视角`、`最大策略矛盾`、`范围模式`、`建议姿态`、`策略取舍`、`当前 D`、`下一技能` 和 `证据状态`。

使用这个格式：

```text
策略审查结论：
- 我建议：
- 最大策略矛盾：
- 范围模式：扩大模式 / 保持模式 / 收缩模式 / 转向模式
- 建议姿态：扩大 / 保持 / 收缩 / 转向
- 为什么：
- 当前必须拍板：
- 进入产品简报的写法：

策略取舍控制面板：
- 来源门槛：
- 策略风险类型：
- 证据状态：
- 范围模式：
- 前提 1：
- 前提 2：
- 前提 3：
- 使用视角：
- 产品动作：
- 策略取舍：
- 范围外：
- 用户承诺边界：
- 反指标保护：
- 对原型的影响：
- 当前 D：
- 后续 D 队列：
- 下一技能：
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

产品动作只能使用以下类型，必要时一条视角可映射多个动作，但用户可见输出要简洁：

- `删除`：从第一版范围移除，或从原型中删除。
- `前置`：放到高成本动作、留资、支付或权限请求之前。
- `后置`：移到结果页、二级页、抽屉、后续步骤或实验后。
- `标注`：标注估算、不确定、人工确认、数据新鲜度或适用范围。
- `禁止`：不可虚构、不可承诺、不可写入验收或不可出现在原型里。
- `实验验证`：不进入稳定承诺，只进入实验假设、观察指标或后续验证。

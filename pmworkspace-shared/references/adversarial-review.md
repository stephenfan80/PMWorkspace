# Adaptive Adversarial Review

Use this before deciding the prototype strategy. The goal is to expose weak premises and convert them into better design choices. Do not run a fixed checklist. Choose the lenses that fit the product.

## Review Shape

1. State the three strongest premises implied by the current direction.
2. Select 3-5 challenge lenses from the library below.
3. For each lens, name the risk in one sentence.
4. Convert the review into prototype decisions.

Use this format:

```text
Adversarial review:
- Premise 1:
- Premise 2:
- Premise 3:
- Lenses used:
- Prototype decisions:
  - Show first:
  - Remove or reduce:
  - Move later:
  - Label as estimated/uncertain:
  - Do not invent:
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

## Product-Type Defaults

Use these as starting points, then adjust.

- **Conversion:** value exchange, friction cost, trust/privacy, metric gaming.
- **Result/report:** data credibility, free information boundary, edge cases, next-step clarity.
- **Internal tool:** status quo competition, repeated task speed, error recovery, permission boundaries.
- **Transaction/service:** feasibility, eligibility, fulfillment state, exception handling.
- **Content/community:** specific user, motivation loop, quality signal, moderation risk.
- **Dashboard/analytics:** decision usefulness, data freshness, comparison baseline, alert fatigue.
- **Lead capture:** value exchange, free information boundary, friction cost, trust/privacy, business conflict.

## Design Translation

The review is useful only if it changes the prototype. Convert findings into choices:

- Put the strongest user value before the first costly action.
- Remove fields that do not affect the first result.
- Move optional precision to result pages, drawers, filters, or follow-up steps.
- Label estimates and assumptions where trust matters.
- Explain human follow-up only when it is real.
- Do not add buttons, functions, data, or promises that the product cannot support.

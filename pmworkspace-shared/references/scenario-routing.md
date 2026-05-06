# Scenario Routing

Use this after first-use onboarding and before PM Jobs questioning. Route the request to the dominant product scenario. A product can have secondary scenarios, but choose one primary route so the brief and prototype stay focused.

## Routing Output

```text
Scenario route:
- Primary scenario:
- Secondary scenario:
- Required inputs:
- Core forcing questions:
- Prototype shape:
- Decision gates:
```

## New Feature Exploration

- **Use when:** there is no current production flow.
- **Required inputs:** user problem, target user, current workaround, primary goal, usable data, constraints.
- **Core questions:** Is the problem real? Who needs it most? What is the smallest useful version? What data can be shown honestly?
- **Prototype shape:** concept screen, MVP flow, or screen pair that proves the value.
- **Gate:** problem reality and MVP scope must be aligned before image generation.

## Existing Feature Iteration

- **Use when:** improving an online page, flow, module, or shipped concept.
- **Required inputs:** current screenshots or screen recording, current goal, known friction, metric or feedback, constraints.
- **Core questions:** What is broken now? What must stay? What should change? What evidence supports the change?
- **Prototype shape:** revised screen, before/after strategy, or corresponding result/detail page.
- **Gate:** production baseline screenshots are mandatory.

## Conversion Flow

- **Use when:** the user is asked for signup, phone, email, payment, permission, install, booking, quote, trial, or another costly action.
- **Required inputs:** primary conversion metric, counter-metric, required input, value shown before action, value unlocked after action.
- **Core questions:** Is the value exchange fair? Which inputs can move later? What reduces distrust without adding fear?
- **Prototype shape:** input page plus result/confirmation page when the action promises a result.
- **Gate:** value exchange and input cost must be explicit.

## Result Or Report Page

- **Use when:** the product promises a generated result, recommendation, score, quote, eligibility, summary, report, or comparison.
- **Required inputs:** promise made before the result, available data, data freshness, uncertainty, next step.
- **Core questions:** Does the page fulfill the promise? What is estimated versus confirmed? What should the user do next?
- **Prototype shape:** integrated result summary plus detailed modules.
- **Gate:** data credibility and uncertainty labeling must be clear.

## Dashboard Or Analytics

- **Use when:** the user needs to monitor, compare, diagnose, or make a decision from data.
- **Required inputs:** decision to support, audience, metric hierarchy, data freshness, comparison baseline, action path.
- **Core questions:** What decision changes after seeing this? What is stale or missing? What alert/action prevents passive reporting?
- **Prototype shape:** decision-first dashboard, status overview, drilldown, or alert page.
- **Gate:** every chart or number must support a decision.

## Internal Tool

- **Use when:** the product improves an operational workflow, admin task, support process, review queue, or team tool.
- **Required inputs:** repeated task, roles/permissions, current workflow, failure modes, speed or accuracy goal.
- **Core questions:** What task is repeated? What slows users down? How do users recover from error? What state must be visible?
- **Prototype shape:** dense workflow UI, queue, detail panel, editor, or status console.
- **Gate:** task efficiency and error recovery must be designed.

## Transaction Or Service Flow

- **Use when:** eligibility, booking, fulfillment, refund, delivery, verification, application, or partner service is involved.
- **Required inputs:** eligibility rules, required materials, status states, human/partner dependency, exception paths.
- **Core questions:** What is confirmed? What is pending? What can fail? How does the user recover?
- **Prototype shape:** service application flow, status page, checklist, or exception state.
- **Gate:** fulfillment and exception states must not be invented.

## Content Or Community

- **Use when:** creation, discovery, publishing, discussion, collection, moderation, or participation loop matters.
- **Required inputs:** user motivation, content object, quality signal, participation loop, abuse/moderation risk.
- **Core questions:** Why contribute or consume now? What signals quality? What loop brings the user back?
- **Prototype shape:** feed, detail page, composer, moderation flow, or contribution prompt.
- **Gate:** motivation and quality signal must be explicit.

## Screenshot Revision

- **Use when:** the user marks red/green boxes or gives targeted UI feedback.
- **Required inputs:** annotated screenshot, accepted style, exact requested change.
- **Core questions:** What changes? What stays? Does the product intent change?
- **Prototype shape:** revised screen only, plus corresponding result/detail screen if requested.
- **Gate:** do not redesign unrelated areas.

# Product Office Hours

Use this before every prototype generation request after first-use onboarding and scenario routing. In PMWorkspace, this is usually owned by `$pm-jobs`. It is a mandatory alignment gate that helps the product manager or designer clarify what the design must accomplish before any image prompt is written.

## Operating Rules

- Always create an alignment moment before design work.
- First classify the change type: `new feature`, `existing feature iteration`, or `unclear`.
- If the change type is `existing feature iteration`, require current production screenshots or equivalent visual evidence before moving past alignment.
- Use `scenario-routing.md` to select questions by product scenario; do not ask a fixed checklist.
- Ask only questions that change the prototype.
- Ask at most 2-4 questions before creating or updating the brief.
- Smart-skip duplicate questions already answered by docs, screenshots, Zoon content, or the user's prompt, but never skip the alignment stage itself.
- If the user says "直接做", "skip", "先出图", or gives a fully formed request, create a Fast Alignment Brief with explicit assumptions and ask the user to confirm or edit it.
- Default prototype strategy is mobile-first unless the user explicitly requests desktop or the scenario truly requires large-screen density.
- Do not generate image prompts while the alignment status is `Needs clarification` or `Ready for PM confirmation`.
- Push for concrete evidence and specific user tasks, not abstract goals.
- Do not praise vague answers; translate them into sharper assumptions or ask one harder follow-up.

## Work Type Routing

First identify the change type:

- **New feature:** no existing production flow is being changed; clarify the user problem, smallest useful version, constraints, and design references.
- **Existing feature iteration:** an existing production page, flow, or module is being improved; require online screenshots and baseline behavior before prototype strategy.
- **Unclear:** ask whether this is new or existing before asking other questions.

Then identify the dominant work type:

- **New feature exploration:** purpose, target user, evidence, smallest useful version.
- **Existing-flow optimization:** current friction, target metric, drop-off point, constraints.
- **Conversion flow:** value exchange, input cost, trust risk, primary action.
- **Result/report page:** promised value, data credibility, uncertainty, next step.
- **Internal tool:** repeated task, speed/accuracy goal, failure handling, permission boundaries.
- **Content/community:** creation or consumption job, quality signal, participation loop.
- **Transaction/service:** eligibility, fulfillment, status, exception handling.
- **Dashboard/analytics:** decision to support, data freshness, comparison baseline, alert threshold.

Use the dominant work type to choose questions. The user always controls final tradeoffs; the agent should recommend a direction, explain why, and wait at decision gates.

## Existing Feature Iteration Gate

If the request is an existing-feature iteration, do not proceed to brief alignment until the user provides at least one of:

- Current online screenshots of the affected page or flow.
- A screen recording or annotated screenshot showing the current behavior.
- A Zoon/product document that includes the current screen state and enough visual detail to preserve production style.

Use the current screenshots to extract:

- Current page purpose and primary action.
- Current information hierarchy and modules.
- Current input burden, friction, or trust problem.
- Existing design system, typography, color, spacing, component density, and button patterns.
- Elements that must be preserved versus areas open to change.

If screenshots are missing, ask in one concise sentence:

```text
这是现有功能迭代的话，请先补充线上功能截图或当前页面录屏；我会基于现状问题和生产样式再做产品 Brief 对齐。
```

## Forcing Question Library

Pick only the questions that matter for the current task.

### User Problem

- What specific user problem should this screen solve?
- What is the user doing immediately before they arrive here?
- What would make the user say this screen helped them decide or act?

### Status Quo

- What is the user doing today instead, even if it is manual or messy?
- What cost does the current workaround create: time, money, risk, confusion, support, churn?
- If the user ignores this feature, what happens?

### Goal And Metric

- What is the primary behavior or metric this design must improve?
- What counter-metric protects the team from cheating the goal?
- What should not get worse while improving the primary metric?

### User Task

- What is the smallest task the user must complete on this screen?
- What information must be visible before the user can trust the next action?
- What can be moved after the primary action without hurting the task?

### Evidence

- What evidence shows this is a real problem: call transcripts, complaints, drop-off data, repeated support tickets, observed behavior?
- What user quote or behavior should shape the copy and hierarchy?
- What assumption is currently weakest?

### Constraints

- What business, compliance, data, operational, or technical constraint cannot change?
- What existing component, design system, or production pattern must be reused?
- What function must not appear because it cannot be delivered?

### Data

- What data can be shown immediately?
- What data requires personalization, freshness, inventory, eligibility, or human confirmation?
- What data is estimated, and how should uncertainty be labeled?

### Concept Direction

- What product strategy should lead the prototype: lower friction, stronger trust, better comparison, clearer status, richer report, faster task completion, or sharper delight?
- What direction should be deliberately avoided because it is off-brand, not feasible, or optimizes the wrong metric?
- For multi-scheme work, which 2-4 directions are meaningfully different enough to compare?

## Alignment Status

Use one of these statuses before moving forward:

- `Needs clarification`: one or more product decisions would materially change the prototype; ask focused questions.
- `Ready for PM confirmation`: enough context exists; summarize the plan and ask the user to confirm, edit, or approve assumptions.
- `Aligned`: the user confirmed the plan in chat, edited/approved the Zoon brief, or explicitly said to use the stated assumptions.

Only `Aligned` can move to design-system review, adversarial review, image prompts, or image generation.

## Compact Output

Before creating a brief, summarize the answers as:

```text
Alignment status:
Product intent:
- Change type: <new feature / existing feature iteration / unclear>
- Existing baseline: <screenshots provided / missing / not applicable>
- Scenario route:
- User problem:
- User task:
- Primary goal:
- Counter-metric:
- Current friction:
- Hard constraints:
- Usable data:
- Concept direction:
- Design implication:
```

Use this summary in the product brief. After the brief is aligned, use it in the image prompt's product intent block.

## Product Plan Handoff

After PM Jobs alignment, create or update an editable product brief:

- **Quick Brief:** small screenshot iteration, narrow page change, or a single decision.
- **Standard Brief:** most prototype requests where product intent and constraints should persist.
- **Deep Brief:** new feature, high-risk flow, cross-team collaboration, unclear evidence, or sensitive data/operations.

Do not treat the brief as a required PRD template. It is a collaboration artifact that captures current understanding, assumptions, and PM decision points. The brief is the product contract for the next prototype step.

Mark uncertain areas clearly:

- `当前假设：` for inferred facts.
- `请补充：` for missing information.
- `请拍板：` for tradeoffs.
- `不可虚构：` for unsupported capabilities or data.

See `product-plan-handoff.md` for the adaptive brief structure and Zoon handoff rules.

# Intake

Use this when first-use onboarding and PM Jobs show that the user gave a rough idea without enough context to design safely. Ask the fewest questions needed; do not turn prototype work into a long workshop.

## Minimum Context To Extract

- Product or feature name
- Change type: new feature or existing feature iteration
- Current production screenshots or screen recording when iterating an existing feature
- Scenario route and expected output shape
- Target user and moment of use
- Primary goal or metric
- Counter-metric or guardrail
- Current problem or evidence
- Required screens and count
- Device size and platform
- Design baseline: AutoDesign by default, or user-provided stronger design system
- Data that can realistically be shown
- Operational constraints: human follow-up, fulfillment, support, compliance

## Fast Question Set

Ask at most three questions in one turn:

1. Is this a new feature or an iteration on an existing online feature?
2. If it is an existing-feature iteration, can you provide the current production screenshots or screen recording?
3. What is the primary metric this prototype should improve, and what must not get worse?

If the user does not answer, create a Fast Alignment Brief with explicit assumptions and ask the user to approve those assumptions before image generation.

## Default Assumptions

- Mobile-first screen unless the user says otherwise.
- One dominant action per screen.
- Show a useful preview before asking for sensitive input.
- Put complex personalization, confirmations, and human follow-up on the result page.
- Prefer realistic product UI over marketing-style presentation.

## Input Summary Template

Summarize the task before product-plan alignment:

```text
Alignment status: <Needs clarification / Ready for PM confirmation / Aligned>
Change type: <new feature / existing feature iteration / unclear>
Existing baseline: <screenshots provided / missing / not applicable>
Scenario route: <new feature / existing iteration / conversion / result-report / dashboard / internal tool / transaction-service / content-community / screenshot revision>
Goal: <metric / behavior>
Counter-metric: <trust / quality / complaint / retention / completion / cost / compliance>
Audience: <user segment>
Current friction: <problem>
Hook: <why the user would continue>
Free value: <shown before input>
Gated value: <shown after input>
Constraints: <business / data / legal / operational>
Screens: <list>
Visual reference: <screenshot / brand style>
```

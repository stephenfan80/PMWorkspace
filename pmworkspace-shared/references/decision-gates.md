# Decision Gates

Use these gates to prevent vague product thinking from becoming polished but weak prototypes. Gates should be lightweight, explicit, and owned by the user. Stop only when a missing decision would materially change the prototype.

## Gate Status

- `Blocked`: required input or decision is missing; stop and ask.
- `Ready for confirmation`: the agent has a recommendation; user must confirm or edit.
- `Aligned`: the user confirmed, approved assumptions, or updated the Zoon brief.

## Required Gates

### 1. Change Type Gate

- Decide whether the work is a new feature or an existing-feature iteration.
- If unclear, ask before any product strategy.
- Existing-feature iteration requires current production screenshots, recording, or equivalent visual baseline.

### 2. Problem Reality Gate

- Name the user problem, current workaround, and evidence.
- If evidence is weak, mark it as `当前假设` and shape the prototype as a learning artifact rather than a production claim.

### 3. Goal And Counter-Metric Gate

- Define the primary behavior or metric.
- Define what must not get worse: trust, quality, complaint rate, retention, task success, cost, or compliance.

### 4. Value Exchange Gate

- Use for any costly action: personal data, signup, phone, payment, permission, install, booking, or long setup.
- Decide what value is shown before the action and what becomes better after it.
- If the exchange is not fair, redesign around free value or lower friction.

### 5. Data And Feasibility Gate

- Separate available, estimated, inferred, user-provided, manual, partner, and unavailable data.
- Mark what cannot be invented.
- Do not show functions, buttons, scores, automations, or guarantees that cannot be delivered.

### 6. Scenario Strategy Gate

- Confirm the primary scenario route and prototype shape.
- For multi-scheme work, confirm distinct concept directions before generating images.

### 7. Product Brief Alignment Gate

- Create or update Quick, Standard, or Deep Brief.
- Stop until the user confirms the brief, approves assumptions, or updates the Zoon source of truth.

### 8. Design System Gate

- Use AutoDesign production baseline by default.
- If a stronger user-provided design system exists, follow it while preserving production-grade spacing, typography, component realism, and no-fake-function discipline.

### 9. Prototype QA Gate

- After image generation, review whether the prototype matches the brief, scenario, design system, and feasibility boundaries.
- If it fails materially, revise the prompt or generate a corrected image rather than presenting a weak artifact as final.

## Decision Brief Format

When a gate needs user confirmation:

```text
Decision:
- Recommendation:
- Why it matters:
- Tradeoff:
- Default if approved:
```

Keep the decision brief short. The user decides; the agent should recommend clearly.

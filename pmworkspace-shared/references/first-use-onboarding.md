# First-Use Onboarding

Use this when the user first invokes PMWorkspace in a thread, starts a new product topic, or provides only a rough product idea. The goal is to route the work and gather the minimum context needed for a useful product brief.

## What To Identify

- **User role:** PM, designer, researcher, operator, founder, or other product partner.
- **Input source:** Zoon doc, PRD, screenshots, research/call notes, metrics, Figma/design system, or plain idea.
- **Change type:** new feature, existing feature iteration, or unclear.
- **Collaboration mode:** use existing Zoon doc, create/update a Zoon brief, or keep the brief in chat.
- **Expected output:** product brief only, one mobile prototype screen, screen pair, multi-scheme prototype set, handoff, or screenshot revision.
- **Design baseline:** AutoDesign production baseline by default; use explicit user-provided design systems when they supersede it.

## First Questions

Ask only the questions that are not answered by the user's prompt or attached materials.

Use these in order:

1. Is this a new feature or an iteration on an existing online feature?
2. If it is an existing-feature iteration, where are the current production screenshots or screen recording?
3. What user problem and primary product goal should the prototype serve?
4. What should the deliverable be: brief, one mobile screen, screen pair, multi-scheme prototype set, handoff, or revision?

If the user provides a Zoon URL, follow `zoon-workflow.md`, announce presence, and read the doc only after the task requires it.

## Start-Here Output

Before creating the brief, summarize:

```text
Start here:
- Role:
- Input source:
- Change type:
- Existing baseline:
- Scenario route:
- Expected output:
- Design baseline:
- Missing blocker:
```

If `Missing blocker` is non-empty, stop and ask for that item. For existing-feature iteration, missing production screenshots are a blocker.

## Defaults

- Default output is an aligned product brief followed by image-2 prototype screens or a handoff.
- Default prototype device is mobile-first iPhone 17 portrait, `402 x 874`.
- Use desktop only when the user explicitly asks or the scenario is a dashboard/internal tool that truly needs large-screen density.
- Default visual system is AutoDesign production baseline.
- Default collaboration source of truth is Zoon when a Zoon doc is provided.
- Do not assume phone, lead capture, payment, login, or other costly user action unless the product context requires it.

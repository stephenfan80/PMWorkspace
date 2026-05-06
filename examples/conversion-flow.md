# Example: Conversion Flow

This is a fictional public example.

## User Prompt

```text
Use $pm-prototype-shotgun to create 3 mobile-first directions for a course trial signup flow.
Scenario: conversion flow
User problem: learners want to know whether a course fits their level before leaving contact info.
Goal: increase trial booking completion.
Counter-metric: avoid low-intent bookings and complaint risk.
Known data: course level, lesson outline, teacher availability, sample lesson clip.
Output: signup page and booking result page.
```

## Expected Skill Behavior

- Route to `Conversion Flow`.
- Apply Value Exchange Gate before form design.
- Show useful free value before contact input.
- Keep required fields minimal and move optional precision later.
- Explain what happens after booking only if that follow-up is real.

## Example Concept Directions

- **Preview First:** show sample lesson and level fit before signup.
- **Time First:** expose available slots first, then collect info.
- **Fit Check:** ask one lightweight level question before recommending a trial.

## Example Handoff

```text
Prototype handoff:
- Brief source: Chat / v1 / Aligned
- Scenario route: Conversion Flow
- Screens produced: Trial signup page, booking result page
- Key assumptions: sample lesson clip is available
- Not invented: no guaranteed teacher match, no instant certificate, no payment
- PM decisions remaining: choose whether level check is required or optional
```

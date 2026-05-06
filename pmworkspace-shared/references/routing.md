# PMWorkspace Routing

Use this when deciding which PMWorkspace expert should own the next step.

## Route Table

| User intent | Route |
|---|---|
| Raw idea, vague request, "help me think", "is this worth building" | `$pm-jobs` |
| Strategy, scope, ambition, risk, value exchange, "think bigger" | `$pm-strategy-review` |
| Need a durable product brief or Zoon alignment artifact | `$pm-brief` |
| Need image-2 prototype screens, multiple schemes, screenshot revision | `$pm-prototype-shotgun` |
| Need PRD-ready, design-ready, experiment-ready, or engineering handoff | `$pm-handoff` |

When multiple routes fit, start with the earliest missing asset:

1. No clear product problem -> `$pm-jobs`.
2. Problem clear but strategy/scope disputed -> `$pm-strategy-review`.
3. Strategy clear but no aligned brief -> `$pm-brief`.
4. Brief aligned and prototype requested -> `$pm-prototype-shotgun`.
5. Direction chosen and next team needs it -> `$pm-handoff`.

## Default Workbench Flow

```text
pm-workspace
-> pm-jobs
-> pm-strategy-review when strategy risk is material
-> pm-brief
-> pm-prototype-shotgun
-> pm-handoff
```

Never skip the aligned brief before image generation.

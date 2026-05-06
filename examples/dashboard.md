# Example: Dashboard Or Analytics

This is a fictional public example.

## User Prompt

```text
Use $pm-jobs to define a dashboard prototype brief, then use $pm-prototype-shotgun after alignment.
Decision this dashboard supports: content operators need to decide which article clusters need intervention today.
Audience: content operations lead.
Metrics available: traffic, completion rate, complaint count, freshness, and moderation status.
Action after seeing data: open cluster detail, assign owner, or suppress recommendation.
Output: dashboard + drilldown screen.
```

## Expected Skill Behavior

- Route to `Dashboard Or Analytics`.
- Start from the decision, not chart variety.
- Require data freshness and comparison baseline.
- Avoid charts that do not change an action.
- Design stale, empty, and alert states if relevant.

## Example Concept Directions

- **Action Queue:** prioritized clusters with owner assignment.
- **Risk Map:** traffic versus complaint risk, optimized for triage.
- **Freshness Monitor:** stale content and moderation status first.

## Example Handoff

```text
Prototype handoff:
- Brief source: Chat / v1 / Aligned
- Scenario route: Dashboard Or Analytics
- Screens produced: Dashboard, cluster drilldown
- Key assumptions: operator can assign owners from this screen
- Not invented: no automated suppression unless existing system supports it
- PM decisions remaining: confirm alert threshold and data freshness SLA
```

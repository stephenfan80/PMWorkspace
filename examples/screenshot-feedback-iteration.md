# Example: Screenshot Feedback Iteration

This is a fictional public example.

## User Prompt

```text
Use $pm-prototype-shotgun to revise this prototype from my annotated screenshot.
Red boxes mean remove the explanatory modules from the form page.
Green boxes mean keep only phone number and primary CTA.
Product intent changed: no.
Output: revised form page plus corresponding result page.
```

## Expected Skill Behavior

- Route to `Screenshot Revision`.
- Create a Quick Alignment Update.
- Change only specified areas.
- Move removed form-page complexity to the result page only if it supports result value.
- Preserve accepted visual style and AutoDesign baseline.

## Example Handoff

```text
Prototype handoff:
- Brief source: Annotated screenshot / v1 / Aligned
- Scenario route: Screenshot Revision
- Screens produced: Revised form page, corresponding result page
- Key assumptions: product intent and primary CTA are unchanged
- Not invented: no new backend capability, no new secondary CTA
- PM decisions remaining: confirm result-page detail priority
```

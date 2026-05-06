# Example: Existing Feature Iteration

This is a fictional public example.

## User Prompt

```text
Use $pm-jobs to iterate an existing online feature, then use $pm-prototype-shotgun after the brief is aligned.
I will provide current production screenshots of the subscription cancellation page.
Current problem: users do not understand the difference between pause and cancel.
Goal: reduce accidental cancellations while keeping cancellation easy to find.
Do not change: account navigation and legal cancellation access.
Output: revised screen plus confirmation result page.
```

## Expected Skill Behavior

- Require current production screenshots before alignment.
- Route to `Existing Feature Iteration` with secondary `Transaction Or Service Flow`.
- Extract current hierarchy, primary actions, copy, and visual density.
- Create a Quick or Standard Brief naming what changes and what stays.
- Preserve production style outside the requested areas.

## Example Decision Gates

- Change Type Gate: existing feature iteration, screenshots required.
- Goal And Counter-Metric Gate: reduce accidental cancellation; do not hide cancellation.
- Data And Feasibility Gate: no unsupported retention offer if backend does not support it.

## Example Handoff

```text
Prototype handoff:
- Brief source: Screenshot set / v1 / Aligned
- Scenario route: Existing Feature Iteration + Transaction Or Service Flow
- Screens produced: Revised cancellation page, confirmation result page
- Key assumptions: pause is available today
- Not invented: no discount offer, no human callback, no new billing policy
- PM decisions remaining: confirm exact pause duration choices
```

# Example: New Feature Exploration

This is a fictional public example.

## User Prompt

```text
Use $pm-jobs to clarify a new feature idea before design.
Feature: Habit Match
User problem: users want to build exercise habits but do not know which plan fits their schedule.
Goal: increase first-week plan activation.
Known constraints: only schedule, goal, and historical check-in data are available.
Output: 3 prototype directions for the first screen and result screen.
```

## Expected Skill Behavior

- Run first-use onboarding.
- Route to `New Feature Exploration` with a secondary `Result Or Report Page`.
- Ask only for missing high-impact context, such as target user and counter-metric.
- Create a Standard Brief with current assumptions.
- Propose distinct concept directions before image generation.

## Example Concept Directions

- **Fast Fit:** shortest path to a recommended plan, optimized for activation.
- **Confidence Report:** show why the recommendation fits, optimized for trust.
- **Schedule First:** start from weekly availability, optimized for realism.

## Example Handoff

```text
Prototype handoff:
- Brief source: Chat / v1 / Aligned
- Scenario route: New Feature Exploration + Result Or Report Page
- Screens produced: Form/input screen, recommendation result screen
- Key assumptions: users value schedule fit more than coaching personality
- Not invented: no wearable sync, no AI coach chat, no guaranteed health result
- PM decisions remaining: choose whether historical check-ins are required or optional
```

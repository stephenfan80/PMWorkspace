# Prompt Recipes

Use these recipes when the user asks how to start, when the input is vague, or when the agent needs to suggest a compact next prompt. These are user-facing starters, not rigid templates.

## New Feature

```text
Use $pm-jobs to clarify this new feature idea before design.
Feature: <name>
User problem: <who has what problem>
Goal: <primary metric or behavior>
Known constraints: <data / policy / operations / design system>
Output: <brief only / one screen / screen pair / 3 directions>
```

## Existing Feature Iteration

```text
Use $pm-jobs to iterate an existing online feature, then use $pm-prototype-shotgun after the brief is aligned.
I will provide current production screenshots.
Current problem: <what is not working>
Goal: <metric or user behavior>
Do not change: <parts that must stay>
Output: <revised screen / screen pair / 3 options>
```

## Zoon Product Doc

```text
Use $pm-workspace with this Zoon doc.
First align the product brief in Zoon, then generate image-2 prototypes after I confirm.
Doc: <Zoon URL>
Output: <screen list or scheme count>
```

## Multi-Scheme Prototype

```text
Use $pm-prototype-shotgun to create multiple prototype directions from an Aligned PMWorkspace brief.
Scenario: <conversion / result report / dashboard / internal tool / service flow / content community>
Goal: <primary metric>
Counter-metric: <what must not get worse>
Please confirm concept directions before image-2 generation.
Output: <number of directions x screen list>; generate each scheme/screen as a separate image.
```

## Chinese Quick Start

```text
使用 $pm-workspace 帮我把这个想法路由到 PMWorkspace 工作台：先用 $pm-jobs 梳理产品 brief，并在我确认后用 $pm-prototype-shotgun 生成 image-2 原型图。
产品想法：<一句话描述>
目标用户：<谁>
用户问题：<他们现在卡在哪里>
目标：<希望提升的行为或指标>
约束：<数据 / 业务 / 法务 / 设计系统 / 上线范围>
输出：<brief only / 1 个屏幕 / 2 个屏幕 / 3 个方案>
要求：每个方案和屏幕单独生成一张图，不要合成在同一张图里。
```

## Screenshot Feedback

```text
Use $pm-prototype-shotgun to revise this prototype from my annotated screenshot.
Red boxes mean: <remove / reduce / move / revise>
Green boxes mean: <keep / simplify / strengthen>
Product intent changed: <yes / no>
Output: <revised screen only / plus corresponding result page>
```

## Dashboard Or Analytics

```text
Use $pm-jobs to define a dashboard prototype brief, then use $pm-prototype-shotgun after alignment.
Decision this dashboard supports: <decision>
Audience: <role>
Metrics available: <metrics and freshness>
Action after seeing data: <what user should do>
Output: <one dashboard / dashboard + drilldown>
```

## Internal Tool

```text
Use $pm-jobs to define this internal tool workflow, then use $pm-prototype-shotgun after alignment.
Repeated task: <task>
Role: <operator / support / reviewer / admin>
Current workflow: <current workaround>
Failure modes: <empty / stale / error / permission / conflict>
Output: <workflow screen / queue + detail / status console>
```

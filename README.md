# PMWorkspace

[中文说明](README.zh-CN.md)

PMWorkspace is a product workbench for PMs, designers, researchers, operators, and founders. It turns raw product context into durable product assets: product decisions, aligned briefs, mobile-first image-2 prototype screens, design feedback, and handoff documents.

PMWorkspace evolved from the former `product-prototype-designer` skill. The old name is intentionally retired; use `$pm-workspace` and the PMWorkspace skill suite going forward.

## What It Does

PMWorkspace follows a gstack-inspired workbench model:

```text
Update check + state logging
-> Work goal mode
-> Scenario routing
-> Q diagnostics, one question at a time
-> Premise confirmation
-> D decision questions for PM tradeoffs
-> Online reference gate for new pages that continue production flows
-> Aligned product brief
-> Zoon online brief for human edits
-> Mobile-first image-2 prototype exploration
-> Prototype QA
-> PRD/design/experiment handoff
```

The core rule is simple: define the product problem, goals, counter-metrics, constraints, and premises before generating prototype images.

## Skill Suite

| Skill | Use When |
|---|---|
| `$pm-workspace` | Start here; route product work and run PMWorkspace platform checks. |
| `$pm-jobs` | Interrogate a raw idea like a demanding product partner before solution design. |
| `$pm-strategy-review` | Challenge scope, value exchange, ambition, risks, and tradeoffs. |
| `$pm-brief` | Create a reusable Quick, Standard, or Deep product brief. |
| `$pm-prototype-shotgun` | Generate mobile-first image-2 prototype schemes from an Aligned brief. |
| `$pm-handoff` | Create PRD-ready, design-ready, experiment-ready, or engineering-ready handoff. |

## Quick Start

```text
Use $pm-workspace to clarify this product idea before prototype design.
Idea: <one sentence>
Target user: <who>
User problem: <what is hard today>
Goal: <behavior or metric>
Constraints: <data / business / policy / design system>
Output: <brief only / one screen / screen pair / 3 directions / handoff>
```

For prototype work, PMWorkspace defaults to mobile-first iPhone 17 portrait `402 x 874`. Desktop is used only when the user asks for it or when a dashboard/internal tool truly needs large-screen density.

Prototype work is locked to image-2 / image generation unless the user explicitly asks for HTML, an interactive web prototype, or frontend implementation. If the product brief is not `Aligned`, PMWorkspace should ask the next diagnostic or decision question instead of producing images, HTML, or a long plan.

## Install

```bash
git clone https://github.com/stephenfan80/PMWorkspace.git
cd PMWorkspace
./setup --host codex
```

Manual install from this folder:

```bash
./setup --host codex
```

Then invoke:

```text
Use $pm-workspace to show the welcome guide and help me choose the right PM workflow.
```

After installation, PMWorkspace should feel like opening a product app for the first time: start with `$pm-workspace`, read the welcome guide, choose a path, then provide your idea, PRD, screenshot, or handoff goal.

## Platform State

PMWorkspace stores durable assets locally by default:

```text
~/.pmworkspace/
  config.yaml
  analytics/usage.jsonl
  projects/<slug>/briefs/
  projects/<slug>/decisions.jsonl
  projects/<slug>/questions.jsonl
  projects/<slug>/project.json
  projects/<slug>/prototypes/
  projects/<slug>/taste-profile.jsonl
```

Defaults:

- Telemetry is local-first: usage logs stay on your machine.
- Remote anonymous telemetry requires explicit opt-in.
- Stored assets should include project display names, briefs, decision questions, decisions, Zoon URLs, prototype manifests, and taste feedback.
- Do not store raw private customer data, tokens, internal recordings, or sensitive screenshots.

Project helpers:

```bash
bin/pmw-project get-name
bin/pmw-project set-name "通用券站外召回方案"
bin/pmw-project show
```

Zoon helpers:

```bash
cat brief.md | bin/pmw-zoon create --title "产品设计简报：通用券站外召回方案"
cat brief.md | bin/pmw-zoon append --url "<Zoon URL>"
bin/pmw-zoon read --url "<Zoon URL>"
```

Inspect settings:

```bash
bin/pmw-config list
```

## Updates

Each skill checks `VERSION` before use when platform scripts are available. If a newer GitHub version exists, PMWorkspace reports:

```text
UPGRADE_AVAILABLE <local> <remote>
```

Upgrade:

```bash
bin/pmw-upgrade --host codex
```

Snooze one version:

```bash
bin/pmw-snooze-update <remote-version>
```

The default remote version URL is:

```text
https://raw.githubusercontent.com/stephenfan80/PMWorkspace/main/VERSION
```

Override with `PMW_REMOTE_VERSION_URL` or `bin/pmw-config set remote_version_url <url>`.

## Prototype Rules

- The brief must be `Aligned` before image prompts or image generation.
- New pages still need an online-reference check. If a screen continues an existing flow, result state, or production style, provide screenshots/recordings/similar pages or explicitly confirm there is no online reference before image generation.
- Multi-scheme concepts must differ by product strategy, information architecture, interaction model, or trust model.
- One scheme plus one screen equals one image.
- `3 directions x 2 screens` means six separate image outputs.
- Do not create collages, side-by-side comparison boards, or multi-screen storyboards unless the user explicitly asks for presentation material.
- Use image-2 / image generation for prototype images.

## Repository Layout

```text
pm-workspace/
pm-jobs/
pm-strategy-review/
pm-brief/
pm-prototype-shotgun/
pm-handoff/
pmworkspace-shared/
  references/
bin/
examples/
```

## Migration From Old Name

If you previously installed `product-prototype-designer`, remove the old skill folder and install PMWorkspace:

```bash
rm -rf ~/.codex/skills/product-prototype-designer
./setup --host codex
```

Use `$pm-workspace` instead of the old long skill name.

## Safety

This repository intentionally contains no real Zoon tokens, user recordings, internal screenshots, or private product data.

## License

MIT

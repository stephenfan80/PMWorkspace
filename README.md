# PMWorkspace

[中文说明](README.zh-CN.md)

PMWorkspace is a product solution workbench for PMs, designers, researchers, operators, and founders: **shape fast, deliver deep**. It turns raw product context into durable product assets: product intros / briefs, solution directions, mobile-first image-2 prototype screens, PRDs, design feedback, and handoff documents.

PMWorkspace evolved from the former `product-prototype-designer` skill. The old name is intentionally retired; use `$pm-workspace` and the PMWorkspace skill suite going forward.

## What It Does

PMWorkspace helps PMs turn an idea that still feels vague into product assets that can be discussed, reviewed, and handed off. It has two entry modes:

- **Quick shaping mode:** produce a 10-minute light package: product brief, 2-3 solution directions, and prototype images. This is for team discussion, leadership review, or early product exploration.
- **Deep delivery mode:** use the full diagnostic workflow, Zoon alignment, prototype review, and handoff flow to upgrade the chosen direction into PRD, design, experiment, or engineering delivery assets.

Deep delivery follows a product runtime workbench model:

```text
Update check + state logging
-> Work goal mode
-> Problem-definition mode: startup validation, internal business optimization, or design discussion
-> Scenario routing
-> Real problem reframe, stated as one sentence before each Q/D
-> Dynamic Q diagnostics, one question at a time, usually 2-3 and at most 5
-> Premise confirmation
-> D decision questions for PM tradeoffs, one at a time
-> Online reference gate for new pages that continue production flows
-> Lightweight internet best-practice research without adding Qs
-> Aligned product brief
-> Zoon online brief for human edits, auto-opened in the Codex built-in browser
-> Mobile-first image-2 prototype exploration
-> Prototype QA
-> PRD/design/experiment handoff
```

The core rule is simple: reframe the user's feature request into the real product problem, then define goals, counter-metrics, constraints, and premises before generating prototype images.

## End-to-End Workbench Map

The canonical end-to-end map lives in `pmworkspace-shared/references/pm-workbench-map.md`. README, routing, eval categories, and skill-to-skill state fields should all point back to that single map:

```text
$pm-workspace
-> $pm-autoplan
-> $pm-jobs
-> $pm-strategy-review
-> $pm-brief
-> $pm-prototype-shotgun
-> $pm-prototype-review
-> $pm-handoff
```

Every handoff between skills should preserve the current mode/status, current or earliest gate, next skill, run_id, evidence state, current Q/D, artifact list, and recommended next step.

## Skill Suite

| Skill | Use When |
|---|---|
| `$pm-workspace` | Start here; route product work and run PMWorkspace platform checks. |
| `$pm-autoplan` | Run the automatic product review pipeline through brief readiness and Zoon sync. |
| `$pm-jobs` | Clarify product value before solution design: painful user, trigger, substitute, loss, and narrow wedge. |
| `$pm-strategy-review` | Judge strategic tradeoffs through four scope modes: expand, hold, shrink, or pivot, then turn the core contradiction into a PM decision. |
| `$pm-brief` | Create a compact product core contract that turns aligned facts, strategy choices, and reference gates into decisions for prototype, review, and handoff. |
| `$pm-prototype-shotgun` | Generate mobile-first image-2 prototype schemes from an Aligned brief. |
| `$pm-prototype-review` | Review generated prototype screens against the brief, Zoon, and non-fiction boundaries. |
| `$pm-handoff` | Create compact PRDs and handoff assets, preserving API, data, tracking, and experiment facts locally. |

## Quick Start

### 10-Minute Light Package

```text
Use $pm-workspace to quickly shape this product idea into a light package: product brief, 2-3 solution directions, and one mobile prototype image per direction.
Idea: <one sentence>
Known context: <optional user / scenario / constraints / references>
Requirement: You may proceed with clearly marked assumptions, but ask me to approve those assumptions before image generation.
```

The light package includes:

- A product brief with assumptions clearly marked.
- 2-3 solution directions that differ by product strategy, information architecture, interaction model, or trust model.
- Separate image-2 prototype screens, following one direction plus one screen equals one image.
- Suggested next step: deepen into PRD, run prototype review, or produce handoff.

### Deep Delivery

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

Prototype work is locked to image-2 / image generation unless the user explicitly asks for HTML, an interactive web prototype, or frontend implementation. In deep delivery mode, if the product brief is not `Aligned`, PMWorkspace should ask the next diagnostic or decision question instead of producing images, HTML, or a long plan. In quick shaping mode, PMWorkspace may generate the light package after the user approves clearly marked assumptions; the package must be labeled as discussion-ready, not final PRD truth.

Briefs start with compact product core information, then gate status and supporting evidence. Briefs published through `pmw-log brief` use Zoon-first, local-backed sync: PMWorkspace first appends or creates the Zoon online brief, then stores the same Markdown as the local audit copy. Before prototype or handoff work, PMWorkspace checks for Zoon drift so edits made in the conversation or in Zoon do not fall out of sync.

## Runtime

PMWorkspace works best in **Codex**.

The full experience includes mobile-first image-2 prototype generation, so the host environment needs image generation capability. Codex can run the product diagnostics, product briefs, solution directions, image-2 prototype screens, and handoff workflow together, so the recommended setup is:

```bash
./setup --host codex
```

Other Codex skill-compatible hosts can still use PMWorkspace for product questioning, briefs, PRDs, and handoff documents. If the host does not provide image-2 / image generation, prototype image output is limited. Do not replace image-2 prototypes with HTML or Markdown wireframes unless the user explicitly asks for HTML, an interactive web prototype, or frontend implementation.

## Product Runtime

PMWorkspace v0.2 turns the skill suite into a local product runtime:

- **Runtime Kernel:** `pmw-run` gives each workflow a `run_id`, mode, gate events, decisions, evidence, artifacts, reviews, and next step.
- **Workbench Map:** `pm-workbench-map.md` aligns README, routing, eval categories, and shared state fields across skills.
- **Evidence Dashboard:** `pmw-dashboard status` renders a Chinese Markdown status page with brief version, Zoon state, references, assumptions, non-fiction boundaries, prototype list, reviews, and question preferences.
- **Prototype Shotgun Board:** `pmw-prototype-board` registers each independent image-2 unit and compares schemes without merging multiple screens into one image.
- **PM Review Army / Product Review Squad:** prototype review keeps the strategy, trust/risk, design system, and data feasibility lenses, then adds CEO, Eng, Design, DX, security, QA, and release-engineering short conclusions before merging findings into pass, regenerate, PM decision, or missing evidence.
- **Question Tuning:** `pmw-question-tuning` records whether a Q/D dimension should always be asked, asked only at high risk, defaulted to the recommendation, or avoided unless blocking.
- **PM Eval:** `pmw-eval` uses dependency-free fixtures to check core gates and output contracts, so skill rules do not silently regress.
- **Auto-Decision Principles:** shared fact priority and stop gates clarify which low-risk defaults can be auto-accepted and which user promises, data-truth, scope, experiment, lead, transaction, or privacy choices require PM decision.

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
  user/taste-profile.jsonl
  user/product-cognition.jsonl
  user/delivery-facts.jsonl
  user/pmworkspace-improvements.jsonl
  user/pmworkspace-feedback-drafts/
  projects/<slug>/briefs/
  projects/<slug>/decisions.jsonl
  projects/<slug>/questions.jsonl
  projects/<slug>/project.json
  projects/<slug>/runs/
  projects/<slug>/prototype-board.jsonl
  projects/<slug>/question-tuning.jsonl
  projects/<slug>/prototypes/
  projects/<slug>/handoffs/
  projects/<slug>/delivery-facts.jsonl
  projects/<slug>/taste-profile.jsonl
  projects/<slug>/learnings.jsonl
```

Defaults:

- Telemetry is local-first: usage logs stay on your machine.
- Remote anonymous telemetry requires explicit opt-in.
- Stored assets should include project display names, briefs, decision questions, decisions, Zoon URLs, prototype manifests, project taste feedback, user-level preferences, sanitized product cognition, delivery facts, local GitHub feedback drafts, and product learnings.
- Runtime assets include local run audit trails, evidence dashboard inputs, prototype board entries, and question tuning preferences.
- Handoff assets include compact PRD-ready, design-ready, experiment-ready, and engineering-ready documents under `handoffs/`; reusable API, data, tracking, and experiment facts are stored in `delivery-facts.jsonl`.
- Do not store raw private customer data, tokens, internal recordings, or sensitive screenshots.
- GitHub feedback drafts stay local and sanitized until the user explicitly asks to submit them.

Project helpers:

```bash
bin/pmw-project get-name
bin/pmw-project set-name "通用券站外召回方案"
bin/pmw-project show
```

Runtime helpers:

```bash
bin/pmw-run start --skill pm-autoplan --mode quick --goal "10 分钟轻量包"
bin/pmw-run event --type gate --status "待确认" --title "假设确认" --summary "等待 PM 确认"
bin/pmw-run finish --status "基于假设，可讨论" --next "进入 image-2 原型"
bin/pmw-dashboard status
bin/pmw-prototype-board add --scheme "方案 A" --screen "首页" --brief-version "v1"
bin/pmw-prototype-board list
bin/pmw-question-tuning add --dimension "反指标" --policy high_risk_only --reason "低风险轻量包默认采用推荐"
bin/pmw-question-tuning summary
bin/pmw-eval list
bin/pmw-eval run
```

Eval fixtures live in the repository at `evals/fixtures/`, and are copied into the installed shared skill bundle for maintenance checks.

Zoon helpers:

```bash
bin/pmw-zoon protocol --host "https://zoon.up.railway.app"
cat brief.md | bin/pmw-zoon create --title "产品设计简报：通用券站外召回方案"
cat brief.md | bin/pmw-zoon append --url "<Zoon URL>"
cat brief.md | bin/pmw-zoon sync --title "产品设计简报：通用券站外召回方案"
bin/pmw-zoon drift --url "<Zoon URL>"
bin/pmw-zoon read --url "<Zoon URL>"
```

`protocol` dynamically reads Zoon's `/skill` and `/agent-docs` and caches a protocol summary for 300 seconds by default, so PMWorkspace can follow Zoon upgrades instead of relying only on built-in routes.

Inspect settings:

```bash
bin/pmw-config list
```

## Updates

Each skill checks GitHub before use when platform scripts are available. It compares both `VERSION` and the latest `main` branch commit, so same-version skill-rule updates are detected too. If a newer GitHub version or commit exists, PMWorkspace reports:

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

The default repository URL is:

```text
https://github.com/stephenfan80/PMWorkspace.git
```

Override with `PMW_REMOTE_VERSION_URL`, `PMW_REPO_URL`, `bin/pmw-config set remote_version_url <url>`, or `bin/pmw-config set repo_url <url>`.

## Prototype Rules

- Deep delivery: the brief must be `Aligned` before image prompts or image generation.
- Quick shaping: image generation requires explicit approval to proceed with listed assumptions, plus non-fiction boundaries for every image.
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
pm-prototype-review/
pm-handoff/
pmworkspace-shared/
  references/
bin/
evals/
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

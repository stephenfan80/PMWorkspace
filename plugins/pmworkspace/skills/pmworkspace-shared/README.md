# PMWorkspace

[中文主文档](README.zh-CN.md)

**PMWorkspace is AI 产品工作站: a product solution workbench that turns an idea, screenshot, PRD, or customer signal into an aligned product brief, image-2 prototype directions, review conclusions, and delivery assets.**

Codex plugin display name: **AI 产品工作站**. `PMWorkspace` is the GitHub repository name, package name, and `$pm-workspace` skill entrypoint. Current version: `0.1.29`.

```text
Align first. Prototype next. Deliver with evidence.
```

Start after installation:

```text
Use $pm-workspace to show the welcome guide and help me choose the right PM workflow.
```

## Install

### Public Codex Plugin

Install **AI 产品工作站** from Codex `Plugins`, then start with `$pm-workspace`.

### Local GitHub Plugin / Team Testing

```bash
codex plugin marketplace add stephenfan80/PMWorkspace
```

If you previously added an older local path:

```bash
codex plugin marketplace remove pmworkspace
codex plugin marketplace add stephenfan80/PMWorkspace
```

Then restart Codex, open `Plugins`, switch the filter to `All`, search **AI 产品工作站** or `PMWorkspace`, and enable it.

### Developer Clone

```bash
git clone https://github.com/stephenfan80/PMWorkspace.git
cd PMWorkspace
bin/pmw-upgrade --host codex-plugin
```

## Update

Public Codex plugin users should update from the Codex `Plugins` UI.

Local GitHub plugin users can check and upgrade with:

```bash
bin/pmw-version --check
bin/pmw-update-check --quick
bin/pmw-upgrade --host codex-plugin
```

Developer clone workflow:

```bash
git pull
bin/pmw-build-plugin
bin/pmw-upgrade --host codex-plugin
bin/pmw-version --json
```

`pmw-upgrade` replaces the PMWorkspace install package, but does not delete project state, briefs, prototypes, handoff assets, or audit logs under `~/.pmworkspace/`.

Detailed release, upgrade, and legacy skill notes live in `docs/codex-plugin-submission.md` and `pmworkspace-shared/references/update-workflow.md`.

## Toolbox

### User Skills

| Tool | What it does | When to use it |
|---|---|---|
| `$pm-workspace` | Main entrypoint. Chooses new feature vs existing feature iteration and routes to the earliest useful gate. | You are not sure where to start. |
| `$pm-autoplan` | Automatic product review. Moves through the recommended workflow while stopping for direction-changing decisions. | You want PMWorkspace to drive the review. |
| `$pm-jobs` | Product direction discovery. Challenges the premise, current substitute, loss, and path options. | The problem is still fuzzy. |
| `$pm-strategy-review` | Strategy and scope review. Tests range, value exchange, risk, and this-cycle validation. | Scope or promise needs a hard look. |
| `$pm-brief` | Product brief generator. Creates the aligned source of truth before prototypes or handoff. | You need a reusable product contract. |
| `$pm-prototype-shotgun` | image-2 prototype director. Generates one image per scheme and screen from an aligned brief. | The brief is aligned and you need prototype images. |
| `$pm-prototype-review` | Prototype review. Checks product, risk, design-system, and data feasibility fit. | Images are generated and need review. |
| `$pm-handoff` | Delivery writer. Produces product design docs, compact PRDs, and handoff assets. | The direction is ready for design, engineering, or review. |

### Runtime Commands

| Command | Purpose |
|---|---|
| `bin/pmw-version --json` | Show local PMWorkspace version identity. |
| `bin/pmw-update-check --quick` | Check for updates quickly. |
| `bin/pmw-dashboard status` | Show concise project state. |
| `bin/pmw-dashboard readiness --target prototype` | Check prototype readiness. |
| `bin/pmw-dashboard readiness --target handoff` | Check handoff readiness. |
| `bin/pmw-artifact flow` | Show the Product Artifact Flow. |
| `bin/pmw-prototype-board list` | Show registered prototype scheme units. |
| `bin/pmw-eval run` | Run behavior contract evals. |
| `bin/pmw-gen-skill-docs check` | Check generated skill contract blocks. |

## Workflow Map

New idea to discussion package:

```text
Idea
-> $pm-workspace
-> $pm-jobs
-> $pm-strategy-review when scope risk matters
-> $pm-brief
-> Discussion-ready product directions
```

New idea to image-2 prototypes:

```text
Idea
-> Product direction review
-> Aligned product brief
-> Product Readiness Dashboard: prototype-ready
-> $pm-prototype-shotgun
-> $pm-prototype-review
```

Existing feature iteration:

```text
Current flow / screenshot / data
-> Production screenshot, URL, Figma, or visual baseline
-> Baseline analysis
-> Updated and aligned product brief
-> image-2 physical longboard or screenshot-edit prototype
-> Prototype review
```

Delivery:

```text
Aligned brief
-> Selected prototype direction
-> Prototype review: pass
-> $pm-handoff
-> Product design doc / compact PRD
```

The complete internal stage map lives in `pmworkspace-shared/references/pm-workbench-map.md`. The README keeps only the user-facing path.

## Method Library

`pmworkspace-shared/references/` is PMWorkspace's method library. It contains the product discovery gates, brief structure, image prompt rules, design-system workflow, prototype review rules, handoff rules, runtime state contracts, and update workflow used by the skills.

Useful anchors:

- Product discovery: `product-office-hours.md`, `product-discovery-gate.md`
- Product brief: `product-manager-brief.md`, `product-plan-handoff.md`
- Prototype generation: `image-prompts.md`, `design-system-workflow.md`, `prototype-shotgun-board.md`
- Prototype review: `prototype-quality-review.md`, `pm-review-army.md`
- Delivery: `delivery-handoff.md`
- Runtime: `runtime-kernel.md`, `artifact-flow.md`, `product-readiness-dashboard.md`
- Collaboration and updates: `zoon-workflow.md`, `zoon-drift-check.md`, `update-workflow.md`

## Product Artifact Flow

PMWorkspace's reusable units are product artifacts rather than isolated notes. Downstream skills read these artifacts instead of guessing from chat memory.

| Artifact | Producer | Used by |
|---|---|---|
| `product_brief` | `$pm-brief` | Prototype, review, handoff |
| `visual_baseline` | Screenshot / reference intake | Prototype canvas and layout constraints |
| `browser_evidence` | Online reference capture | Brief, prototype, review |
| `prototype_manifest` | `$pm-prototype-shotgun` | Prototype review |
| `prototype_review` | `$pm-prototype-review` | Handoff |
| `repair_brief` | `$pm-prototype-review` | Prototype regeneration |
| `product_design_doc` | `$pm-handoff` | Product/design/engineering review |
| `handoff` | `$pm-handoff` | Compact PRD and delivery follow-up |

Inspect the flow:

```bash
bin/pmw-artifact flow
bin/pmw-artifact flow --details
bin/pmw-artifact latest --kind product_brief
```

## Prototype Rules

- An aligned product brief is required before image prompts or image generation.
- One scheme plus one screen equals one image.
- Default output is mobile-first image-2.
- Default exploration uses at least three product paths unless there is an explicit exception.
- Multi-scheme directions must differ by product strategy, information architecture, interaction model, trust model, or key task path, not only visual styling.
- Existing feature iteration requires a production screenshot, URL, Figma, or equivalent visual baseline before image generation.
- HTML is only used when the user explicitly asks for HTML, an interactive web prototype, frontend implementation, or a local web prototype.

## Privacy

PMWorkspace keeps project assets local by default under `~/.pmworkspace/`: briefs, audit copies, decisions, Zoon links, artifact flow metadata, prototype manifests, review conclusions, handoff docs, sanitized delivery facts, preferences, and usage logs.

It should not store tokens, owner secrets, API keys, cookies, raw customer data, internal recordings, sensitive screenshots, unsanitized collaboration-doc content, or raw API responses in shared materials.

## Maintainers

```bash
bin/pmw-eval list
bin/pmw-eval run
bin/pmw-build-plugin
bin/pmw-gen-skill-docs write
bin/pmw-gen-skill-docs check
```

Generated contract blocks in `SKILL.md` files are produced by `bin/pmw-gen-skill-docs write`; do not edit generated blocks by hand. After changing source skills, shared references, `bin`, `evals`, README, or plugin assets, run `bin/pmw-build-plugin` and include the plugin package changes in the commit.

## License

MIT

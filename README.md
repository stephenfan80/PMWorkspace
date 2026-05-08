# PMWorkspace

[中文说明](README.zh-CN.md)

**Turn a fuzzy product idea into something reviewable, visual, and ready to hand off.**

PMWorkspace is a product solution workbench for PMs, designers, researchers, operators, and founders. It does more than produce attractive prototype images: it connects the real problem, product summary (brief), AI collaboration document (Zoon), screenshot evidence, scheme differences, review conclusions, and delivery assets into one product workflow.

Use it when you have an idea, PRD, screenshot, user feedback, or collaboration doc that is not yet ready for design or engineering. PMWorkspace helps reframe the problem, align the core product judgment, generate mobile-first image-2 prototype screens, review the result, and produce compact delivery material.

```text
Shape fast. Deliver deep.
```

## Who It Helps

- Product managers turning vague requests into aligned product direction.
- Designers who need evidence, boundaries, and product intent before visual exploration.
- Researchers, operators, and business teams turning insights or support signals into a product plan.
- Founders and product leads who need a discussion-ready package quickly.
- Cross-functional teams that need reviewable artifacts instead of scattered context.

## The Pain It Solves

- A stakeholder gives one sentence, but expects a convincing solution tomorrow.
- Feedback, screenshots, PRDs, and collaboration docs are scattered across tools.
- Prototype work moves fast, but the underlying problem is still unstable.
- Existing flows need improvement, yet there is no production screenshot or visual baseline.
- Reviews depend on one PM perspective and miss risk, design-system, data, or engineering concerns.
- Handoff restarts from scratch because prior product decisions were never captured as durable assets.

## What PMWorkspace Produces

- **Product summary:** target user, core problem, current loss, goal, counter-metric, constraints, and non-fiction boundaries.
- **Solution directions:** options that differ by product strategy, information architecture, interaction model, or trust model.
- **Mobile-first prototype images:** one direction plus one screen equals one image-2 output, defaulting to iPhone 17 portrait `402 x 874`.
- **Evidence records:** online screenshots, status pages, competitor references, and collaboration-doc drift evidence.
- **Readiness verdicts:** a pre-image or pre-handoff check across summary, collaboration doc, online reference, scheme difference, boundaries, and review status.
- **Review conclusions:** strategy, trust/risk, design-system, and data-feasibility perspectives before final prototype review.
- **Delivery assets:** compact PRD, design handoff, experiment seed, or engineering handoff.

## Two Working Modes

**Quick shaping** is for early ideas and discussion packages. PMWorkspace asks only the few clarifications that affect the shape of the solution, lists assumptions and non-fiction boundaries, and then creates a light package after approval.

**Deep delivery** is for PRDs, design reviews, engineering handoff, production-flow work, high-risk business promises, or AI collaboration document sync. PMWorkspace aligns the product summary before image generation or delivery writing, so the team does not move quickly in the wrong direction.

## How It Works

1. Reframe the real product problem before jumping into a solution.
2. Ask focused clarifying questions instead of long generic questionnaires.
3. Use decision choices when scope, promise, experiment language, or delivery boundaries need a clear owner.
4. Publish and sync the product summary through the AI collaboration document when available.
5. Record online evidence through the existing artifact flow.
6. Run a readiness check before image generation or handoff.
7. Use multi-role review to catch strategy, risk, design-system, and data gaps.

## Start

Install:

```bash
git clone https://github.com/stephenfan80/PMWorkspace.git
cd PMWorkspace
./setup --host codex
```

Then start with:

```text
Use $pm-workspace to show the welcome guide and help me choose the right PM workflow.
```

Quick shaping prompt:

```text
Use $pm-workspace to quickly shape this product idea into a product summary, 2-3 solution directions, and one mobile prototype image per direction.

Idea: <one sentence>
Known context: <user / scenario / constraints / references>
Requirement: proceed with clearly marked assumptions, but ask me to approve them before image generation.
```

Deep delivery prompt:

```text
Use $pm-workspace to turn this PRD / AI collaboration document / screenshot feedback into a product summary that is ready for prototype design.

Target user: <who>
Core problem: <what is hard today>
Goal: <behavior or metric>
Constraints: <data / business / policy / design system / scope>
Output: <summary only / one screen / three directions / handoff>
```

## Advanced Runtime

The Chinese README is the primary user guide. This section keeps the runtime anchors for deeper usage and maintenance.

- **End-to-end workbench map:** the canonical map lives in `pmworkspace-shared/references/pm-workbench-map.md`; README should not maintain a second route table.
- **Product Readiness Dashboard:** `pmw-dashboard readiness --target prototype|handoff` gives a verdict before image generation or handoff.
- **Product Artifact Flow:** `pmw-artifact` makes product summaries, prototype manifests, review results, handoff docs, and browser evidence readable by downstream skills.
- **Browser Evidence Lite:** online screenshots, status pages, competitor references, and collaboration-doc drift evidence are recorded as `browser_evidence` artifacts through `pmw-artifact`.
- **PM Review Army / Product Review Squad:** strategy, trust/risk, design-system, and data-feasibility specialists review first; high-risk delivery can add CEO, Eng, Design, DX, security, QA, and release-engineering roles.
- **Skill Doc Generator:** `pmw-gen-skill-docs` generates and checks shared SKILL.md contract blocks.

Useful commands:

```bash
bin/pmw-dashboard status
bin/pmw-dashboard readiness --target prototype
bin/pmw-dashboard readiness --target handoff
bin/pmw-artifact add --kind browser_evidence --title "线上参考：结果页" --status "已采集" --source-skill pm-brief --path "<screenshot>" --url "<URL>" --summary "页面任务、视觉基线、交互模式、必须保留、可以挑战"
bin/pmw-artifact flow
bin/pmw-review-specialist summary
bin/pmw-prototype-board list
bin/pmw-eval run
bin/pmw-gen-skill-docs write
bin/pmw-gen-skill-docs check
```

AI collaboration document helpers:

```bash
bin/pmw-zoon protocol --host "https://zoon.up.railway.app"
cat brief.md | bin/pmw-zoon create --title "产品设计简报：通用券站外召回方案"
cat brief.md | bin/pmw-zoon append --url "<document URL>"
cat brief.md | bin/pmw-zoon sync --title "产品设计简报：通用券站外召回方案"
bin/pmw-zoon drift --url "<document URL>"
bin/pmw-zoon read --url "<document URL>"
```

## Prototype Rules

- Deep delivery requires an aligned product summary before image prompts or image generation.
- Quick shaping requires explicit approval to proceed with listed assumptions.
- New pages that continue existing flows, result states, or production styles need online reference checks.
- Multi-scheme concepts must differ by product strategy, information architecture, interaction model, or trust model.
- One scheme plus one screen equals one image.
- Do not create collages, side-by-side comparison boards, or multi-screen storyboards unless the user asks for presentation material.
- Use image-2 / image generation for prototype images.

## Privacy

PMWorkspace keeps telemetry local by default. It should not report project names, file paths, prompt contents, screenshots, product-summary text, or customer data. Do not store raw private customer data, tokens, internal recordings, or sensitive screenshots in shared materials.

## License

MIT

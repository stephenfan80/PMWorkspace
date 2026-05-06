# Image Prompt Templates

Use these templates with `imagegen` / built-in image generation only after the product brief is aligned and concept directions are confirmed. Keep one screen per prompt and one scheme per image output.

## Pre-Prompt Gate

Do not write an image prompt until all are true:

- PM Jobs has produced a product intent summary.
- Change type is classified as new feature or existing feature iteration.
- Existing-feature iterations include current production screenshots or equivalent baseline evidence.
- A Quick, Standard, or Deep Brief exists in chat or Zoon.
- The brief is aligned by user confirmation, latest approved Zoon edits, or explicit approval of assumptions.
- Multi-scheme work has named concept directions confirmed by the user or approved as defaults.
- The output plan maps each requested scheme/screen to a separate image. Do not compose several schemes into one comparison board image.
- The canvas decision follows mobile-first defaults: iPhone 17 portrait `402 x 874`, unless the user explicitly requests desktop or the screen is a dashboard/internal tool that needs large-screen density.
- AutoDesign production baseline has been loaded through `design-system-workflow.md`.
- Any material adversarial-review changes have been reflected back into the brief.

## Concept Direction Confirmation

Before generating multiple schemes, present concise directions:

```text
Concept directions:
A. <name> - <product strategy and tradeoff>
B. <name> - <product strategy and tradeoff>
C. <name> - <product strategy and tradeoff>
```

Directions must differ by product strategy, information architecture, interaction model, or trust model. Do not offer three visual skins of the same idea. After confirmation, generate each direction/screen as a separate image, even when several images are generated in one batch.

## Image Output Contract

For every image generation request, declare the output unit before prompting:

```text
Image output unit:
- Scheme: <A/B/C or concept name>
- Screen: <screen name>
- Canvas: <device and size>
- Depends on: <brief version and source>
```

Rules:

- One output unit equals one image.
- Default output unit canvas is mobile iPhone 17 portrait `402 x 874`.
- Desktop output units must state why mobile is not appropriate.
- Do not create collage boards, side-by-side comparisons, or multi-screen storyboards unless the user explicitly asks for a presentation board instead of prototype images.
- If the user asks for `3 directions`, generate three separate images after direction confirmation.
- If the user asks for `3 directions x 2 screens`, generate six separate images, ordered by scheme or by screen depending on the user's review workflow.
- Keep product facts, sample data, typography, and design-system profile consistent across related images.

## Base UI Mockup Template

```text
Use case: ui-mockup
Asset type: mobile-first app prototype screen
Primary request: Generate <screen name> for <product/feature>. Size strictly <device width x height>. Match the provided reference screenshots for typography, spacing, color, and component density.

Context:
- Product intent:
  - Brief version/status: <vN / Aligned>
  - Scenario route: <primary scenario>
  - Concept direction: <name and strategy>
  - Change type: <new feature / existing feature iteration>
  - Existing baseline: <screenshots/reference provided; current page purpose and preserved elements>
  - User problem: <specific problem>
  - User task: <what the user is trying to do now>
  - Primary goal: <metric or behavior>
  - Counter-metric: <trust, quality, complaint, retention, completion, etc.>
  - Current friction: <problem or evidence>
  - Hard constraints: <business / legal / data / operations / components>
  - Usable data: <what can be shown now; what is estimated or requires confirmation>
- Adversarial review decisions:
  - Show first: <highest-value information>
  - Remove or reduce: <unearned complexity>
  - Move later: <optional precision or follow-up>
  - Label as uncertain: <estimates or assumptions>
  - Do not invent: <functions/data/actions that cannot ship>
- Decision gates:
  - Gates passed: <change type, problem reality, value exchange, data feasibility, brief alignment, design system>
  - Open PM decisions: <none or list>

Screen content:
- Header: <title, nav, brand elements>
- Main value area: <hook / preview / summary>
- Input or action area: <minimum required fields and CTA>
- Result/value details: <only if this is a result page>
- Trust/explanation: <privacy, follow-up, uncertainty, eligibility>

Visual requirements:
- Platform/device: <iPhone 17 W402 x H874 by default; desktop only if explicitly requested or necessary>
- Typography: <brand font or reference style>
- Palette: <brand/reference palette>
- Layout density: <compact / standard / spacious>
- Design system constraints: <paste the compact summary from design-system-workflow.md when applicable>
- AutoDesign baseline: apply production-like AutoDesign tokens, spacing, components, and anti-patterns unless a stronger provided design system overrides specifics.
- Avoid: no red annotation boxes, no watermarks, no external notes, no overlapping text.
```

## AutoDesign Prompt Block

Use this block by default as the production-quality visual baseline. If the product is not Autohome, use the visual discipline without adding Autohome-specific brand copy or domain content. Keep it in the prompt even when reference screenshots are provided, unless the screenshots clearly supersede a specific value.

```text
AutoDesign production constraints:
- Make it look like a real Autohome mobile app screen, not a marketing poster or abstract concept.
- Canvas: iPhone 17 portrait W402 x H874 unless the user specifies otherwise; preserve AutoDesign's 375px mobile canvas logic.
- Colors: primary blue #0088FF, blue gradient #0099FF -> #0088FF, commercial orange #FF6600 only for price/deal/subsidy emphasis, cyan #25C9FF only for IM-like emphasis, primary text #111E36, secondary text #464E64, weak text #828CA0, divider #E6E9F0, page background #F8F9FC, white cards.
- Typography: system Chinese font; prominent numbers can use HarmonyOS Sans SC; use production-like sizes from 12/14/16/18/20/24/28/32px with clear hierarchy.
- Layout: 8-point grid for structure and 4-point grid for details; use spacing 4/8/12/16/24/32px; align cards, fields, and CTAs to consistent margins.
- Radius and depth: small tags/buttons 2px, cards/images 3px, dialogs/toasts/bottom sheets 6px, large bottom sheets 8px; use subtle shadow only where hierarchy needs it.
- Components: use AutoDesign-like NavBar, Button, Form, ToolBar, Tag, card, and result modules.
- Buttons: one dominant primary action per screen; bottom primary button height 48px, blue gradient, concise verb-object copy.
- Forms: short field labels, low input burden, phone number visible and editable in first screen for lead forms, privacy agreement near submit.
- Lead forms: clearly explain dealer/service follow-up when calls are part of the product reality.
- Avoid: decorative orbs, oversized hero marketing layout, excessive gradients, over-rounded cards, heavy shadows, stacked CTAs, fake functions, cramped rows, and overlapping text.
```

## Form Page Prompt Checklist

Include:

- One clear hook above the form.
- One dominant CTA.
- Only required-looking fields.
- Optional refinements hidden, secondary, or moved after submit.
- Privacy/confidence copy short enough to not compete with the CTA.
- For Autohome lead forms: phone number visible and editable on the first screen; submit button visible on the first screen; privacy agreement close to submit.

Avoid:

- Long explanatory modules below the form.
- Multiple equally strong CTAs.
- Heavy conditions before phone/email/signup.
- Phone/email/signup fields when the product is not a lead, account, contact, or saved-result flow.
- Result-level detail on the form page unless it is a teaser.
- AutoDesign violations: arbitrary colors, excessive rounded corners, too many shadows, marketing-poster hero sections, and button stacks.

## Result Page Prompt Checklist

Include:

- "Report generated" or equivalent state.
- Integrated top summary.
- Detailed modules that fulfill the form promise.
- Optional refinements or condition-entry modules if they improve accuracy.
- Clear explanation of human follow-up when applicable.
- No bottom CTA if the real product has no such action.
- For Autohome result pages: use production-like cards, concise status tags, clear value hierarchy, and no invented bottom action.

Avoid:

- Repeating the same form CTA.
- Making the result page feel like another lead form.
- Hiding uncertainty; label what is estimated, confirmed, or needs follow-up.
- Filler text, decorative widgets, or visual modules that do not answer the user's task.

## Iteration Prompt Template

```text
Use case: ui-mockup
Asset type: revised mobile app prototype screen
Primary request: Revise the previous <screen name> according to annotated feedback.

Keep:
- <accepted style / layout / modules>

Change:
- Remove <red-boxed or specified module>.
- Simplify <green-boxed or specified area> to <new content>.
- Move <removed complexity> to <result page / detail layer> if requested.

Constraints:
- Preserve device size <width x height>.
- Preserve font and visual style from the reference.
- Preserve the active design-system profile, such as AutoDesign tokens and components.
- Do not add new functions unless explicitly requested.
- No annotation boxes, no watermark, no overlapping text.
```

## Production Review Checklist

Before sending an image prompt, verify:

- The product brief has alignment status `Aligned`.
- Concept directions are confirmed for multi-scheme work.
- The product intent block is concrete enough to guide hierarchy.
- The adversarial review decisions are reflected in screen content.
- The design system is named when applicable.
- The prompt includes concrete color, type, spacing, radius, and component constraints.
- The screen has one primary action unless the user explicitly asks for comparison actions.
- The form asks only what is needed before submission.
- The result page fulfills the promised value before asking for more.
- The prompt explicitly forbids annotation boxes, watermarks, overlapping text, and fake functions.

## Post-Generation QA

After generation, use `prototype-quality-review.md`:

- Check the image against the aligned brief, scenario route, concept direction, feasibility boundary, and AutoDesign baseline.
- If a screen materially fails, revise only that prompt/screen.
- Final response should include a compact handoff manifest, not long rationale.

## Multi-Screen Sequencing

When the user asks for many screens:

1. Generate the most important form/input page first.
2. Generate its corresponding result page second.
3. Continue scheme by scheme.
4. Keep each generated image tied to one scheme and one screen.
5. Use consistent product name, data, typography, and visual system across a pair.

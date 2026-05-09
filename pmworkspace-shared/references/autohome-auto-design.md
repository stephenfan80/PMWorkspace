# Autohome AutoDesign Profile

Use this profile when the user mentions Autohome, 汽车之家, 之家, AutoDesign, or production design requirements for Autohome products.

This file is a reusable summary, not a copy of the internal design site. If the user provides newer AutoDesign pages or screenshots, inspect those and prefer the latest source.

## Design System Intent

- AutoDesign is a shared design and component system maintained by Autohome technical and UED teams.
- The goal is consistent product experience, reusable components, and production-friendly design-to-development handoff.
- Prototypes should feel like realistic Autohome app screens, not marketing posters or decorative concept art.
- Product UI uses AutoDesign as the primary source of visual truth. Brand VI material is secondary and should not override product UI tokens unless the task is explicitly a brand/marketing visual.
- When the user provides a current Autohome production screenshot, that screenshot becomes the highest visual baseline for the current prototype. Its pixel size, typography hierarchy, spacing rhythm, component density, and bottom bar behavior override generic AutoDesign guidance.

## Color Tokens

Primary and semantic colors:

- Main blue: `Blue_1 #0088FF`, `Blue_2 #33A0FF`, `Blue_3 #99CFFF`, `Blue_4 #E5F3FF`
- Orange: `Orange_1 #FF6600`, `Orange_2 #FF8533`, `Orange_3 #FFC299`, `Orange_4 #FFEFE5`
- Cyan: `Cyan_1 #25C9FF`, `Cyan_2 #51D4FF`, `Cyan_3 #A8E9FF`, `Cyan_4 #E9F9FF`
- Success green: `Green_1 #1CCD99`, `Green_2 #49D7AD`, `Green_3 #A4EBD6`, `Green_4 #E8FAF4`
- Error/warning red: `Red_1 #FF4434`, `Red_2 #FF695D`, `Red_3 #FFB4AE`, `Red_4 #FFECEA`

Neutral colors:

- Primary text: `Gray_1 #111E36`
- Secondary text: `Gray_2 #464E64`
- Tertiary text: `Gray_3 #828CA0`
- Disabled/weak text: `Gray_4 #BFC5D2`
- Divider/border: `Gray_5 #E6E9F0`
- Background block: `Gray_6 #E6EBF5`
- Page background: `Gray_7 #F8F9FC`
- White: `#FFFFFF`

Gradient tokens:

- Blue gradient: `#0099FF -> #0088FF`
- Orange gradient: `#FF8C3B -> #FF6600`
- Cyan gradient: `#40D0FF -> #00C0FF`

Usage:

- Use blue for primary actions and Autohome brand emphasis.
- Use orange for price, deal, subsidy, or strong commercial emphasis.
- Use cyan for IM/chat-like scenarios.
- Avoid large areas of orange or cyan.
- Keep the color ratio restrained; avoid noisy red/green/orange combinations.

## Typography

- Prefer the platform/system default font.
- Use `HarmonyOS Sans SC` for prominent numbers when appropriate.
- Common font sizes: `8, 9, 10, 11, 12, 13, 14, 16, 17, 18, 20, 24, 28, 30, 32, 36px`.
- Chinese text usually uses Regular/Medium weights; Android maps these to Normal/Bold.
- Prominent numbers can use Medium/Bold.
- Maintain clear hierarchy with few type levels.
- Ensure primary text contrast is production-readable; do not use faint text for important values.
- Local or brand font packages require authorization confirmation. Do not present custom fonts as production-ready defaults in generated product UI.
- For production screenshot reproduction, keep visual hierarchy close to the reference: nav titles and vehicle/model titles should remain prominent, price numbers should stay the dominant numeric layer, CTA text should remain readable, and chart labels / tags / helper text must not be compressed to tiny sizes to fit more content.

## Brand VI And Font Boundary

- Brand VI colors such as `#0055ff` and `#ff8800` are brand/marketing references, not default product UI replacements.
- For product screens, use AutoDesign product tokens such as `Blue_1 #0088FF` and `Orange_1 #FF6600` unless the latest design-system source explicitly says otherwise.
- Brand logos, slogans, auxiliary graphics, and decorative VI assets should only appear when the brief requires brand exposure; do not turn functional product screens into posters.
- Font packages can inform special brand or campaign visuals only after authorization is confirmed; otherwise use system Chinese font and HarmonyOS Sans SC for prominent numbers.

## Layout

- Standard design canvas reference: 375px mobile width.
- For generated prototypes, use the user's requested canvas, commonly iPhone 17 `402 x 874`, while preserving AutoDesign spacing logic.
- For Autohome production-page prototypes with a screenshot reference, also lock the pixel output. Default target is a 3x mobile long board: width no lower than the reference screenshot's 95%, preferably `1179-1206px` when the reference is a modern iPhone screenshot. Height should grow with content; do not squeeze first screen, explanation modules, sample lists, and bottom CTA into a shorter canvas.
- Use an 8-point grid for page structure and a 4-point grid for fine adjustment.
- Spacing scale: `4, 8, 12, 16, 24, 32, 48, 64px`.
- Use closer spacing for strongly related information and larger spacing for separate modules.
- Align content to consistent page margins and card gutters.

## Radius And Shadow

Radius:

- `2px`: small tags, small operation buttons, text labels.
- `3px`: images and cards.
- `6px`: feedback containers, dialogs, toast, bottom sheets.
- `8px`: large page-level bottom sheets.

Shadow:

- Base elevation: color `#111E36`, opacity `8%`, offset `0 5`, blur `20`.
- Use shadow sparingly; prefer clean grouping and backgrounds over heavy depth.

## Component Rules

### NavBar

- Place it at the top and use it to explain the current page.
- Title should be short and easy to understand.
- Include back/close actions when the flow is modal or nested.
- Right-side function icons should not exceed three.

### Button

- Buttons should communicate clear actions such as search, submit, inquire, or view.
- A screen should usually have one highest-priority primary button.
- Primary button: blue gradient by default.
- Orange button only for price/deal/strong commercial emphasis.
- Bottom floating primary button height: `48px`, radius `2px`, text size around `16px`.
- Common button heights: `48, 40, 32, 28, 24px`.
- Button text should be concise and action-oriented, usually verb-object copy.
- Avoid vague button copy such as "OK" or "Next" when the outcome can be named.

### Form

- Use forms to collect user demand and return a system response.
- Keep form structure clear, accurate, and low cost.
- Field title should be short, ideally within six Chinese characters.
- Basic elements: title, required marker when needed, input area, optional helper icon, error message.
- Minimize required-looking fields before the primary CTA.

### ToolBar

- Bottom toolbar appears at the bottom and stays visible while the page scrolls.
- It can contain auxiliary information and a primary operation.
- Types include heavy-button bottom bar, auxiliary-info bottom bar, fixed-width button bottom bar, and primary-secondary button bottom bar.
- Do not create bottom buttons on result pages if the real product has no action there.

### CluesForm

Use these rules for lead forms:

- Applicable to vehicle price, deal, service, dealer, or commercial lead collection scenarios.
- Vehicle basic information is required: image, brand/series/model; model switching can be omitted in simplified forms.
- Phone number is required, must appear in the first screen, must be clear, and must be editable.
- Submit button is required and should appear in the first screen.
- Privacy and personal information agreements are required and must be close to submission.
- If dealer follow-up will happen, clearly tell the user they may receive dealer or service calls.
- Optional items such as city, dealer, payment method, finance, trade-in, store visit time, or service configuration should not overload the first screen unless essential.

## Prompt Block

生成汽车之家原型时，在图片提示词中加入这个区块：

```text
AutoDesign production constraints:
- Use Autohome mobile app style, not a marketing poster.
- Screenshot baseline: if a production screenshot is provided, follow its pixel size, typography hierarchy, spacing rhythm, card density, chart density, bottom toolbar height, and long-board proportions before applying generic tokens.
- Pixel output: for a reference such as `1179 x 2556`, target a 3x mobile long board with width no lower than 1179px and preferably 1206px. Height is adaptive and may exceed the reference when content is longer.
- Colors: primary blue #0088FF, blue gradient #0099FF -> #0088FF, commercial orange #FF6600, primary text #111E36, secondary text #464E64, weak text #828CA0, divider #E6E9F0, page background #F8F9FC, white cards.
- Typography: system Chinese font, prominent numbers may use HarmonyOS Sans SC; clear hierarchy using 12/14/16/18/20/24/28/32px sizes.
- Layout: 8-point grid for structure, 4-point grid for details; spacing 4/8/12/16/24/32; consistent margins and gutters.
- Do not shrink Chinese text, chart axis labels, cards, tags, or bottom CTA to force more modules into the image.
- Radius: small buttons/tags 2px, cards/images 3px, dialogs/toasts/bottom sheets 6px, large bottom sheets 8px.
- Buttons: one primary action per screen; bottom primary button height 48px, blue gradient, concise verb-object text.
- Forms: short labels, phone number visible and editable on the first screen for lead forms, required agreement near submit.
- Brand VI boundary: do not replace AutoDesign product UI tokens with VI colors #0055ff or #ff8800 unless this is explicitly a brand/marketing visual; custom font packages require authorization confirmation.
- Avoid decorative gradients/orbs, oversized hero marketing layout, excessive shadows, over-rounded cards, stacked CTAs, and overlapping text.
```

## Production Review Checklist

Before generating or finalizing an Autohome prototype, check:

- Does the screen use AutoDesign colors instead of arbitrary blues/oranges?
- Does the screen avoid replacing AutoDesign product tokens with brand VI colors unless the task is explicitly brand/marketing?
- If custom font packages are requested, is authorization marked as confirmed or still pending?
- Is the main CTA singular and action-oriented?
- Is the form short enough for the conversion goal?
- Is the phone number visible and editable on lead forms?
- Are privacy agreements near the submit action?
- If calls are expected, is the reason and scope clearly explained?
- Are spacing, radius, and typography aligned to the profile?
- If a production screenshot is provided, does the generated image pass size / long-board audit against the reference, and does it avoid visibly smaller fonts or tighter spacing?
- Does the result page fulfill the user's promised value before asking for more action?

---
name: aaa-design
description: Produce top-tier ("AAA") UI/UX and visual design in code — landing pages, dashboards, app screens, mobile flows, onboarding, portfolios, brand/identity pages, design systems and components — with a committed token system, all interaction states, accessibility and a measured self-critique loop. Use this whenever the user asks to design, build, redesign, restyle, polish or "make beautiful" any web page, UI, screen, component, prototype or brand page in HTML/CSS/Tailwind/React, or asks for a design system, theme, style guide or visual direction — even if they don't say "design" explicitly (e.g. "build me a pricing page", "make this dashboard look premium", "create an onboarding flow").
---

# AAA Design

This skill turns a brief into an interface that holds up next to the best current showcase work and fixes what that work usually gets wrong.

It is distilled from a study of 348 reference examples: 287 Inspora shots and motion pieces, and 61 real brand-guideline documents and sites. Most of those references are beautiful in a screenshot and fail where nobody looks:

- **Contrast:** 90% contain text below WCAG AA.
- **States:** only 4 of 348 show an empty, error or 404 state.
- **Reduced motion:** none demonstrate a reduced-motion variant.

You win by matching their craft and then doing the unglamorous parts properly.

Work through the six steps in order. Steps 3 and 6 are where quality is decided, so don't skip them.

```
1 Read the brief  →  2 Choose a direction  →  3 Commit tokens  →  4 Lay out & type
→  5 Build components with every state  →  6 Render, audit, critique, iterate (≤3 loops)
```

Reference files live in `references/` and load only what you need:

| When you are… | Read |
|---|---|
| choosing a direction | `references/style-recipes.md` |
| writing tokens | `references/token-presets.md` (4 contrast-verified presets) |
| picking fonts and a scale | `references/typography.md` |
| building a palette or dark mode | `references/color.md` |
| adding motion | `references/motion.md` |
| building controls, cards, nav, forms, states | `references/components.md` |
| making a brand or identity page | `references/brand-system-template.md` |
| doing the final pass | `references/craft-checklist.md`, `references/anti-patterns.md` |
| scoring your output | `rubric.md` |

Working references in `examples/` show the bar. Open one that matches your direction before you start, and skim it in 30 seconds; don't copy it.

---

## 1. Read the brief

Before any code, write a short design brief for yourself, either in your reply or as a comment at the top of the file:

```
Product / subject:   what it is, in one line
Audience & job:      who uses it and the single most important thing they must do or feel
Content inventory:   the real sections, data, actions (list them; invent realistic specifics if the user gave none)
Tone (3 words):      e.g. "precise, calm, expensive" — pick words that exclude something
Constraints:         framework, brand colours/fonts given, platforms, must-have sections
Signature moment:    ONE place where this design will be memorable (see step 2)
```

Why: the best references all had one idea that does a job. Examples:

- A stamp prints the chosen date.
- A search field morphs into the selected country.
- A loader shares the grid of the image it reveals.

Weak work has either no idea or five decorations. Deciding the signature moment up front keeps everything else quiet.

If the user supplied brand assets, they override the presets. Derive tokens from them, then still run the contrast gate. Real brands often ship failing pairs, such as white on a light brand green, so fix them with an "ink" shade instead of changing the brand colour.

## 2. Choose a direction: one base plus one expressive layer

Pick **exactly one structural base** and **at most one expressive layer**. The top-rated references follow this rule. The lowest-rated stacked glass, aurora glow and gradient mesh on the same screen.

| Brief signal | Base | One expressive layer | Avoid |
|---|---|---|---|
| B2B SaaS, analytics, dev tools | neutral-swiss *or* dark-premium | hairline/technical detail, or one shader/orb object | glass behind data |
| AI assistant / agent | dark-premium or neutral-swiss | orb or shape-morph for **state**, mono metadata | decorative loops that mean nothing |
| Fintech / payments / commerce | neutral-swiss | a physical metaphor (card, receipt, stamp, ticket) | white text on bright brand colour |
| Consumer / playful / education | playful-soft | soft-3D or meaningful colour-coding | pastel fills with white labels |
| Portfolio / studio / culture | editorial-warm *or* hairline | one physical or pixel signature | more than one gimmick |
| Brand / identity page | editorial-warm or swiss-poster | the brand's own device used as texture | template look |
| Mobile flow | neutral-swiss or playful-soft | one illustration or material per screen | hover-only affordances |

**Restraint is not blandness.** In blind tests, builds that were correct but used Inter for everything with no bespoke art lost on direction and typography to riskier designs. Every design needs both of these:

1. **A characterful display voice.** Pick it from the display list in `references/typography.md`: an editorial serif (Instrument Serif, Fraunces, Newsreader, Gloock), a grotesk with personality (Bricolage Grotesque, Familjen Grotesk, Schibsted Grotesk, Space Grotesk, Unbounded), or a rounded face for playful briefs. Pair it with a quiet text face. Inter or system-ui alone is acceptable only for dense app chrome, and even then give headings or numbers a second voice (a mono or a display cut).
2. **At least one piece of bespoke art in the first viewport.** This can be:
   - an inline-SVG illustration or mascot;
   - a product mock built in HTML and CSS with real-looking data;
   - a typographic composition (oversized, cropped or overlapping type);
   - the signature object (receipt, ticket, orb).

   Stock-looking icon grids don't count. The art should *be* or *stage* the signature moment, and it must be visible in the hero, not below the fold.

Write one sentence stating the direction. For example: *"Neutral-swiss base, dark hero band, one physical layer: the invoice prints out of the CTA when you click it."*

`references/style-recipes.md` gives the exact parameters and CSS for each base and layer.

## 3. Commit the token system before writing any component

Start from the closest preset in `references/token-presets.md` and copy its `:root` block. Every preset's text pairs are pre-verified for contrast. Then adapt it, keeping its structure:

- **Colour:**
  - **Canvas and surfaces:** canvas, surface-1, surface-2 and surface-3, stepped by lightness.
  - **Borders:** a decorative hairline and a control border, which must be ≥ 3:1.
  - **Text:** text-1 ≥ 12:1, text-2 ≥ 7:1 and text-3 ≥ 4.5:1, all measured on the surfaces they will actually sit on.
  - **Accent:** one accent plus a darker accent-ink for text, which must be ≥ 4.5:1.
  - **Semantic colours:** success, warning, danger and info, each as a fill plus an ink.
  - **Neutrals:** use a tinted near-black and a warm or cool off-white, not #000 and #fff. Tinted neutrals appeared in 75 of the studied examples.
- **Type:** two families at most, plus one mono if the product has data. Use a modular scale of 6–8 named steps:
  - ratio 1.2 for apps, 1.25–1.333 for marketing;
  - body 16px;
  - display ÷ body of 3.5–5× on landing pages, 2–2.5× in apps;
  - tracking per step: −0.02 to −0.03em at display sizes, +0.06 to +0.1em on small caps.
- **Space:** a 4px base; scale 4 8 12 16 24 32 48 64 96 128.
- **Radius:** pick 2–3 values plus `9999px`, and nest them as inner = outer − padding. Use 0 only for things that should feel like paper.
- **Elevation:**
  - light themes: a soft two-layer shadow and an inset top highlight;
  - dark themes: tint steps instead of shadows;
  - glows: hue-matched to their object.
- **Motion:** `--dur-1 120ms`, `--dur-2 200ms`, `--dur-3 320ms`, `--dur-4 560ms`; `--ease-out: cubic-bezier(.2,.8,.2,1)`; a `prefers-reduced-motion` block that collapses movement to opacity.

**Verify before moving on.** Run the contrast script on every text/background pair you defined:

```bash
python3 <skill>/scripts/contrast.py '#6b6b72' '#ffffff' '#a1a1aa' '#0b0b0d' ...
python3 <skill>/scripts/contrast.py --fix '#16a34a' '#f2f2f2'   # nearest passing shade
```

Why this step comes first: tokens decided after components drift. The live sites studied used a median of 9 distinct font sizes and up to 21, and the weakest guideline documents contradicted their own hex values between pages. A small, verified token set is what makes work look intentional.

Components must use tokens only. No raw hex or px values inside component styles, except one-off art.

## 4. Layout and type rules

**Grid and layout:**
- Use a 12-column desktop grid with 24px gutters.
- Margins: 16px at 390, 32px at 768, 48–104px at ≥1280. Max content width is 1200–1320px; prose stays at 60–72ch.
- One focal point per viewport. Keep 30–45% of a hero empty. Put the eye path in order: headline → proof → action.
- Section rhythm on landing pages is 96–160px. App density uses rows of 40–56px.

**Type and colour:**
- Hierarchy comes from size and colour before weight, with no more than 2 weights per family on a screen.
- Display line-height is 0.95–1.1 and body 1.5.
- Use sentence case. All-caps only for labels of ≤ 3 words, tracked +0.08em.
- Numbers use `font-variant-numeric: tabular-nums` and right-align in columns. Dim units and currency symbols one step.
- One accent per view. Colour-code only when categories exist, then thread each category's hue through every layer (badge, bar, dot, citation).
- Text never sits directly on moving or busy imagery. Use a solid zone, or a scrim sampled from the image, and check its contrast.

**Responsive and copy:**
- Responsive means redesigned, not shrunk:
  - fluid type with `clamp()`;
  - sidebars collapse;
  - touch targets ≥ 44px;
  - no horizontal scroll at 390px.
- Write real, specific copy, with numbers, units, names and plausible data. Placeholder text and typos were the most avoidable craft loss in the study (20 examples).

`references/typography.md` has pairings and ready-made scales.

## 5. Build components with every state

Every interactive component ships all of these states, styled from tokens:

`default · hover · focus-visible · active/pressed · disabled · loading · error · empty/success`

The non-negotiable UX coverage:

- **Keyboard:**
  - every control is reachable by Tab in a logical order;
  - focus is a visible 2px ring in the accent-ink with a 2–3px offset (`:focus-visible`), never `outline: none` without a replacement;
  - Esc closes overlays, and arrow keys move inside tabs, menus and radio groups;
  - focus is trapped in modals and returned when they close.
- **Semantics:** use real `<button>`, `<a>`, `<label for>` and landmarks (`header`, `nav`, `main`, `footer`), one `<h1>` and no heading skips. Every image has `alt` (empty `alt=""` if it's decorative) and every icon-only button has an `aria-label`. Use `aria-live` for async status.
- **State is never colour-only:** pair colour with an icon, a word or a shape. For example, the verb changes tense: Create → Creating → Created.
- **Feedback timing:**
  - press feedback in ≤ 100ms;
  - optimistic UI with **Undo** instead of confirm dialogs for reversible actions;
  - progress shown in two synchronised ways for long tasks.
- **Empty, error and loading** get designed layouts, not afterthoughts. An empty state names what will appear, gives one action, and uses the page's signature device. Errors say what happened and what to do. A skeleton shares the result's geometry, so nothing shifts.
- **Reduced motion:** `@media (prefers-reduced-motion: reduce)` removes transforms, parallax and auto-play, and keeps short opacity fades of ≤ 150ms.
- **Scroll reveals are progressive enhancement.** Content must be fully visible with JS off, for crawlers and print, and in full-page screenshots.
  - Hide elements only behind a class that JS adds to `<html>`, e.g. `.js .reveal{opacity:0}`.
  - Reveal once, never re-hide.
  - Keep the reveal ≤ 400ms, with a ≤ 12px translate.
  - Under reduced motion, show everything immediately.
- **Motion choreography** (measured median 0.33s across 1,368 reference transitions):
  - use ease-out for entries and ease-in only for exits and things falling;
  - open 1.5–3× slower than you close;
  - content inside a morphing container arrives about 80ms after the container, going from blur(6px) and opacity 0 to rest;
  - every animation must signal state.

  See `references/motion.md`.

`references/components.md` has recipes for buttons, inputs, segmented controls, cards, tray-plus-card nesting, nav, tables, toasts, empty states and more.

## 6. Render, audit, critique, iterate

You haven't finished until you have looked at the rendered result. Code that "should" look right usually doesn't: spacing collapses, a font fails to load, a grey disappears on a tinted card.

Run this loop at most 3 times:

1. **Render and measure:**
   ```bash
   node <skill>/scripts/audit.mjs path/to/page.html ./audit
   ```
   It saves full-page screenshots at 390, 768 and 1440px plus a reduced-motion shot. It also checks the hard gates: AA text contrast, no overflow at 390, visible keyboard focus, reduced motion respected, text ≥ 12px, alt text and accessible names. It warns about touch targets, heading order, more than 3 font families, more than 4 radii and more than 1 accent hue.

   Playwright is required. If it's missing, install it (`npm i -D playwright`), or use any headless browser to screenshot, and run `contrast.py` on your token pairs manually.

   For React or Tailwind projects, build or serve the page first and pass its URL.
2. **Look at the screenshots yourself.** Open `shot-1440.png` and `shot-390.png` with your image viewer. Check them against the brief: is the signature moment visible? Is there one focal point? Does anything look generic?

   **Template test:** if this could pass as a stock UI-kit template with the logo swapped, it fails Direction. Push one of these and re-render:
   - a more characterful display face;
   - bespoke art in the hero;
   - one bold composition move (oversized or cropped type, an asymmetric 7/5 split, overlap between art and type, a full-bleed colour band);
   - a stronger signature interaction.

   **Blank-section test:** if any section looks empty or faded in the full-page shot, your reveal animation is hiding content. Fix it (see step 5).
3. **Score** with `rubric.md`: 8 axes scored 1–10 plus the hard gates. Write the scores and the three biggest problems.
4. **Fix the three biggest problems first.** Usually that means hierarchy, spacing rhythm, contrast or a missing state, not new decoration. Then re-run.

**Stop when:**
- all hard gates pass, and
- every axis scores ≥ 7 with a total ≥ 64/80, or
- you have done 3 loops (report what's left).

Scoring below the bar after the first loop is normal, not a reason to stop. Loop 2 is where the design gets good: fix the weakest axis, re-render and look again. Also view at least one non-default state, such as an open menu, an error, a later step or a hover, through a quick Playwright script or by reading the screenshot of it. The audit only renders the initial state.

## Final craft pass (two minutes, before you hand over)

Check the top 15 from `references/craft-checklist.md`, which has 86 items:

1. Display tracking is negative and set per size; small caps are tracked positive.
2. Every text pair is computed; there's no grey under 4.5:1 and no white on a light brand colour.
3. One accent; tinted neutrals; a second font voice (mono or serif) is used for a reason.
4. Radii: 2–3 values plus pill, nested correctly.
5. Hairlines at 6–12% ink are used for structure, not as the only carrier of information.
6. Raised surfaces have a 1px inner top highlight; shadows are soft, layered and hue-tinted.
7. Numbers are tabular, with units dimmed.
8. The layout doesn't shift between states; loaders share the result's geometry.
9. The signature moment does a job: it confirms, explains or guides.
10. Every animation maps to a state change, with ease-out by default and close faster than open.
11. Focus rings are visible, hover and focus are distinct, and Esc closes overlays.
12. Empty, error and loading states are designed.
13. 390px works: no overflow, 44px targets, and a collapsed nav.
14. Copy is real, specific and proofread, with no lorem ipsum.
15. `prefers-reduced-motion` and `prefers-color-scheme` (if you ship dark mode) are handled.

Then tell the user:
- the direction you chose and why;
- the token summary;
- the audit result: gates and scores;
- anything you would do with more time.

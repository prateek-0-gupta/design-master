---
id: bg-instacart
source: brandguidelines
category: guideline
status: analyzed
title: "Instacart Brand Guide"
creator: "In-house"
styles: [playful-rounded, maximalist-color, flat-illustration, photo-led]
patterns: [index-as-oversized-list-with-rules, yellow-on-kale-hero-statement, half-circle-colour-chips, colour-groups-by-purpose-primary-secondary-exclusive-neutral, aa-aaa-badges-per-swatch, sticky-dark-header, giant-wordmark-footer, type-demo-in-lime-card]
mode: mixed
palette: ["#003d28", "#faf1e5", "#f9fb93", "#ff7009", "#0aad0a", "#c5ff96", "#ffbb6e", "#3a682f"]
type_families: ["Instacart Sans (custom; Regular 400 and Semibold 600; display 600 at 60 px / -1.2 px)", "Inter (swatch data labels)"]
type_class: [grotesk, rounded-sans]
radius_px: [16, 23]
motion: {durations_s: [0.2], easing: [ease, "cubic-bezier(0.56,0.86,0.59,1)"], loop: false}
scores: {aesthetics: 9, originality: 8, usability: 8, craft: 8}
craft_signals: [kale-and-cashew-as-ink-and-paper, butter-yellow-statement-headlines, half-circle-swatch-motif-from-the-carrot, contrast-badges-AA-AAA-on-swatches, hex-rgb-pantone-cmyk-per-colour, exclusive-palette-with-do-not-repurpose-rule, margin-spec-1x-and-0.5x-in-layout, tight-tracking-on-60px-display]
anti_patterns: [orange-carrot-on-cream-fails-contrast, sticky-header-covers-content-in-tall-captures, tiny-swatch-data-text, tight-line-height-on-body-copy]
---
# Instacart Brand Guide — In-house

## 1. Snapshot
- **Subject:** `heyitsinstacart.com`, the 2026 Instacart brand guide (footer says 2026). The request was `/` and the final URL was `/layout/`. The site has an index plus 8 chapters: Brand Element, Logo, Carrot, Big Green Bag, Colors, Typography, Photography and Layout. Subpages were captured for Brand Element, Logo, Colors, Typography, Photography and Layout; Carrot and Big Green Bag were not captured. No archive.
- **Why it's remarkable:** a food-fresh palette built on two "ink and paper" colours (Kale #003d28 and Cashew #faf1e5), shown as half-circle chips that echo the carrot logo. Each colour group has a defined purpose, and the accessibility ratings are printed on the swatches.

Viewed: home t01 and t02; d01 t01 (Brand Element); d02 t01 (Logo); d03 t01 and t05 (Colors); d04 t01 (Typography); d05 t01 (Photography); d06 t01 (Layout); mobile sheet 1.

## 2. Composition & layout
- **Index (home):** a Cashew page with eight chapter names as huge Instacart Sans Semibold lines (about 60 px, -1.2 px tracking) separated by 1 px kale rules on a 146 px row pitch, 40 px page margins. Below it a Kale footer block holds a giant cream wordmark (about 1350 px wide) with the colour carrot, then a 3-column text index and "2026".
- **Sticky header:** a Kale bar, 47 px tall, with a small logo at x=40 and "Login" at the right. In tall captures it repeats and overlaps content; this is a capture artifact, not a design bug.
- **Sub-page template:**
  1. A Kale hero (about 340–600 px tall) with a centred statement in Butter yellow (#f9fb93) at about 60 px, e.g. "The Instacart logo is our most recognizable brand asset."
  2. A white content area with sections that start with a 36 px heading (Inter-like, regular) and a 17/17 px body (tight leading).
  3. Cards in a 3-column grid (about 350 px wide, 16–24 px radius), with a title and a one-line description under each.
  4. 1 px kale rules between sections; content width about 1125 px (x 155–1285).
- **Mobile:** the index collapses to a single column of chapter names, then the wordmark fills the width.

## 3. Typography
- **Instacart Sans** is the custom face (loaded as custom_72625, weights 400 and 600). Census: 60/58 at 600 with -1.2 px tracking (index and hero lines), 36/32 and 24/29 at 400 (section titles, card titles, nav).
- Body copy is 17 px with a very tight leading, about 1.0–1.1 (e.g. 17 px / 17 px). This is visible in the dense two-line captions.
- **Inter** at 12.9/14, 15.5/17, 20.7/21, 31/34 and 40/44 px is used inside the swatch data labels. The type page itself demonstrates "In titles, we use Instacart Sans" in large kale-on-lime cards, with heading, subheading and body proportions.
- The face has a distinctive single-storey "y" with a straight tail, and chunky rounded terminals.

## 4. Colour
Primary (HEX per page):
| hex | name | role | share |
|---|---|---|---|
| #003d28 | Kale | ink, dark ground, header | ~20% on home, 90% on hero bands |
| #faf1e5 | Cashew | paper ground | 64% of index |
| #ff7009 | Carrot | logo base, accent | small |
| #0aad0a | Lime | logo leaves, accent | small |
| #c5ff96 | Honeydew | type-demo cards | panels |
| #ffbb6e | Cantaloupe | logo ground, panels | panels |
| #3a682f | Spinach | logo ground | panels |

Secondary: Matcha #85cc3e, Granny Smith #dbef77, Butter #f9fb93 (hero statement colour), Mushroom #edc9a2, Tangerine #ffa323. Exclusive: Banana #ffe200, Watermelon #ff8e67, Mint #c6f0cb. Neutrals: Dark Chocolate #442202, Cashew 80 #32302e, Cashew 60 #716c67, then Cashew 30/20/10/050/025/00 (#e1d9ce, #efe1cf, #faf1e5, #fdf8f2, #fefbf9, #ffffff). Each swatch lists HEX, RGB, Pantone and CMYK (neutrals list HEX and RGB only).

Rules from the page:
- The palette is organised into groups, each with a defined purpose.
- **Exclusive** colours are reserved for sub-brand differentiation, affordability (Banana for deals, savings and price drops) and seasonal campaigns (Watermelon and Mint for Mother's Day and summer). "Any new applications outside these guidelines require approval."
- Each swatch carries AA/AAA badges with small dots showing which text colours pass (e.g. Banana: AAA with Kale and Dark Chocolate; Watermelon and Mint: AA).

Contrast (contrast.py):
- Kale on Cashew: **11.06:1**.
- Butter on Kale: **11.33:1**.
- Kale on Banana: **9.5:1**.
- Kale on Honeydew: **10.67:1**.
- Cashew on Spinach: **5.87:1**.
- Carrot on Kale: **4.46:1** (large text only).
- Lime on Kale: **4.12:1** (large text only).
- Carrot on Cashew: **2.48:1**, which fails. Never use it for text.

## 5. Depth & material
Flat, with no shadows (census). Depth comes from watercolour illustration (a child sliding down a celery stalk into a pool of peas, a watermelon half) and from candid photography. Rounded tiles (16–24 px radius) and half-circle chips are the structural motif. Shapes echo the logo, a carrot whose top is a green arrow and whose base is an orange half-circle.

## 6. Components & patterns
- Cards: a rounded visual on top, a 24 px label and a 14–15 px one-line description.
- Half-circle swatch chips with Inter data in a 4-line block.
- Pill CTA: "View Image Library" in Kale on Butter, about 390×78 px, fully rounded.
- Logo grid: four tiles (Cashew, Kale, Cantaloupe, Spinach) each with the right logo version (colour carrot on light and dark; white on mid-tones).
- Layout rules shown with orange dashed overlays and "1X / 0.5X" spec labels around a phone-card.

## 7. Motion
The site uses `opacity 0.2s ease` for the nav and links (122 uses on the colour page) and a custom `cubic-bezier(0.56,0.86,0.59,1)` easing. The brand's Motion element appears on the Brand Element page (a "1 2 3 Days to eat" counter animation), but no timings are published in the frames I saw.

## 8. Brand system
- **Chapters:** Brand Element (Colour: "Care with Flavor"; Typography: "Care as Voice"; Illustration: "Care through Expression"; Motion; Carrot; Photography), Logo (Hero, Logo Color), Carrot, Big Green Bag, Colors, Typography, Photography, Layout.
- **Logo:** the full-colour dark logo is the primary ("should be used wherever possible"). Four ground versions: Cashew, Kale, Cantaloupe and Spinach.
- **Colour system:** four named groups (Primary, Secondary, Exclusive, Neutrals), all food-named.
- **Typography:** one custom sans with proportional heading/subheading/body relations.
- **Photography:** a "candid, human lens". Three categories: Brand Forward (warm everyday moments), Splash Screen (bold produce macro with negative space so the three-colour logo reads) and Functional (CPG packshots).
- **Layout:** characteristics are "intentional asymmetry" (imagery bleeding off a centre axis) and "consistent margins and spacing" (0.5X top, 1X sides and bottom around a card). Three type alignments (left, centred and a playful staggered one) set different tones.
- **Voice cue:** "Care" is the thread in every element's tagline.
- **Token decisions worth stealing:** ink-and-paper pairing (Kale/Cashew), a purpose-labelled palette, AA/AAA badges on swatches, a logo-derived chip shape.

## 9. UX
Fast index-to-chapter navigation, a sticky header and strong hero statements. The swatch data is small (about 6–7 px in the capture) and the body leading is tight. The mobile index is excellent.

## 10. Craft signals
- The half-circle chip echoes the carrot's base.
- Every hero line is in the same Butter on Kale combination at a fixed size, which gives a strong rhythm.
- Neutrals are a named tint scale (Cashew 80 to 00) that shares the paper colour's name.
- Exclusive-palette governance with explicit "when not to use".
- A single 60 px display style with -1.2 px tracking.

## 11. Reproduction recipe
```css
:root{--kale:#003d28;--cashew:#faf1e5;--butter:#f9fb93;--carrot:#ff7009;--lime:#0aad0a;
  --honeydew:#c5ff96;--cantaloupe:#ffbb6e;--spinach:#3a682f;--banana:#ffe200}
body{background:var(--cashew);color:var(--kale);font:400 17px/1.1 "Instacart Sans",system-ui,sans-serif}
.hero{background:var(--kale);color:var(--butter);text-align:center;padding:110px 40px}
.hero h1{font:600 60px/58px "Instacart Sans";letter-spacing:-1.2px}
.index a{display:block;font:600 60px/58px "Instacart Sans";letter-spacing:-1.2px;padding:44px 0;border-top:1px solid var(--kale);transition:opacity .2s ease}
.card{border-radius:20px;background:var(--cashew);overflow:hidden}
.chip{width:152px;height:76px;border-radius:152px 152px 0 0}
.btn-pill{background:var(--butter);color:var(--kale);font:600 32px "Instacart Sans";border-radius:999px;padding:20px 48px}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 9 | Warm and fresh: the Kale, Cashew and Butter triad, watercolour and candid photography feel instantly food-first. |
| Originality | 8 | Index-as-giant-type and half-circle chips tied to the logo are fresh. |
| Usability | 8 | Purpose-labelled colour groups, AA/AAA badges and layout margin specs are actionable. |
| Craft | 8 | Consistent hero template and tokens; small swatch text and tight body leading. |

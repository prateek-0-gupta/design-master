---
id: bg-odido
source: brandguidelines
category: guideline
status: analyzed
title: "Odido Brand Guidelines (Merk)"
creator: "Odido (formerly T-Mobile Netherlands)"
styles: [gradient-mesh, playful-rounded, minimal-swiss, photo-led]
patterns: [glow-gradient-palette, pill-swatch-with-tint-ladder, three-identity-levels-entry-participation-functional, mirror-layout-system, bespoke-typeface-headline-and-text, logo-versions-tabbed, photo-carousel-hero, left-rail-nav-with-grey-inactive-items]
mode: light
palette: ["#2c72ff", "#2f9a92", "#ffac24", "#ff7621", "#ff808c", "#7066ff", "#000000", "#ececec"]
type_families: ["Otypical Headline 500 (bespoke)", "Otypical Text 400 (bespoke)"]
type_class: [geometric-sans, humanist-sans]
radius_px: [40, 9999]
motion: {durations_s: [0.1, 0.15, 0.2, 0.5], easing: ["cubic-bezier(0.4,0,0.2,1)"], loop: false}
scores: {aesthetics: 9, originality: 8, usability: 7, craft: 8}
craft_signals: [bespoke-typeface-with-headline-and-text-cuts, six-hue-five-tint-ladders, pill-radius-9999-on-swatches, glows-as-named-gradients, logo-readable-both-ways, small-size-logo-variant, tracking-0.32px-on-16px-body, minimum-margin-1-12-of-short-side]
anti_patterns: [inactive-nav-bbbbbb-1.9-contrast, tab-labels-light-grey, palette-values-only-on-hover, text-in-mockups-unreadable-small]
---
# Odido Brand Guidelines (Merk) — Odido

## 1. Snapshot
- **Subject:** Odido's live brand portal ("Merk" = brand in Dutch) at `merk.odido.nl/en`. `site_meta.json`: requested `/en`, ended on `/en/photography` after crawling six subpages (Brand foundation, Logo, Colour, Typography, Layout, Photography). No archive. Home is a long single page of seven tiles; chapters are listed in the nav as Introduction, Brand foundation, Logo, Colour, Typography, Layout, Shapes, Photography, Illustration, Iconography, Motion, Sonic, Tone of Voice, Digital, Resources, Support.
- **Why it's remarkable:** A telco identity built from five geometric letter-shapes (circle, half-circle, rectangle, half-circle, circle) that spell Odido and read both ways. The colour system is "Glows": four soft multi-hue gradients over six hues with five tints each. Brand expression is split into three levels (Entry black and premium; Participation colourful; Functional editorial).

## 2. Composition & layout
- Fixed left rail about 340 px wide: logo mark at top (120×32 at x≈64), a vertical nav in 14 px grey with the current page in black and sub-items indented 16 px, and account/search icons beneath.
- Content column starts at x≈437 and runs to x≈1312 (875 px). Image carousels bleed past the column to the right edge (x 340→1440), with a 4-dot pager (active dot a 24×8 pill).
- Large chapter titles at 104 px with 100 px leading. Section titles are 64/64, sub-sections 42/48. Vertical space between sections is about 150–200 px.
- Mobile (390 px): rail collapses to a menu icon, one 390-wide column, image cards with 40 px radius, and body at 16 px.
- Application examples sit in a rounded 2-up photo grid (radius 40 px) with a staggered third image.

## 3. Typography
Two bespoke cuts, both loaded as fonts, drawn from `census_home.json`.

| Style | Spec |
|---|---|
| Chapter H1 | Otypical Headline 500, 104 / 100 |
| Section H2 | Otypical Headline 500, 64 / 64 |
| Sub H3 | Otypical Headline 500, 42 / 48 |
| Lead | Otypical Text 400, 24 / 32 |
| Body | Otypical Text 400, 16 / 24, tracking +0.32px (2%) |
| Caption / nav | Otypical Text 400, 12 / 16, tracking +0.24px |

The typography chapter describes Headline as the "show-stealer" and Text as a toned-down cut for small sizes. It is "geometrical and human". Type setting rules shown in the nav include sentence case, tracking, kerning, headline and body leading, quotes, and "smart headline features". Display specimens appear at 160 and 200 px with 160 and 180 leading (negative leading above 1:1 rule of thumb). Headline colours in examples include Tech blue and gradient fills on rotated type.

## 4. Colour
| Hex | Role | Approx share |
|---|---|---|
| #ffffff | page | 60–75% |
| #000000 | text, entry-level fields, logo | 5–15% |
| #ececec | panels, tab fields | 8–30% on sub-tiles |
| #2c72ff Tech blue | secondary hue | swatch |
| #2f9a92 Charm teal | secondary hue | swatch |
| #ffac24 Solar yellow | secondary hue | swatch |
| #ff7621 Dutch orange | secondary hue | swatch |
| #ff808c Warm pink | secondary hue | swatch |
| #7066ff Lively purple | secondary hue | swatch |
| #bbbbbb | inactive nav and tab text | UI |

Core palette: Black, White and four Glows (gradients combining the secondary hues). Each secondary hue has a five-step tint ladder, for example blue #2c72ff, #578fff, #82acff, #adc8ff, #c3d7ff, #eef3ff. Swatches are 136 px pills (radius 9999 px, top-rounded or bottom-rounded for the ladder). Hex values appear on hover.

Contrast: black on #2c72ff **4.96:1**; black on #ff7621 **7.87:1**; black on #2f9a92 **6.16:1**; black on #ececec high. The inactive nav grey #bbbbbb on white is **1.92:1** (fails AA, a real weakness for the primary navigation).

## 5. Depth & material
No shadows (`shadow {}` in every census). Depth is photographic: mockups on textured white walls with hard daylight shadows, a black 3D sign box with a gradient logo, trams wrapped in the Glow gradient. Graphics are flat or gradient; there are no blurs in UI.

## 6. Components & patterns
- Pill-shaped swatches and a donut diagram of the three identity levels (Entry outer ring, Participation middle, Functional white core).
- Segmented text tabs (Colour logo / Solid logo / Outlined logo / Masked logo) in 12–14 px with grey inactive states.
- Chat-bubble shapes (white and black, radius about 40 px) in the Shapes chapter ("Wij zijn Odido." / "Welkom bij Odido.").
- Photo cards with 40 px radius; buttons are pills (9999 px).
- "Back to top" with an arrow at the page end.

## 7. Motion
UI transitions are Tailwind defaults: `all 0.15s cubic-bezier(0.4,0,0.2,1)`, `0.1s` for hover, `0.2s` for the Typography page and one `0.5s` colour fade. Brand motion is a separate chapter I did not capture; a motion thumbnail shows a 5G illustration with a rocket.

## 8. Brand system
- **Positioning:** "premium for everyone"; a balance of maturity, outspokenness, playfulness and a down-to-earth approach. Mission: make technology enjoyable for all; "the joy of taking part".
- **Name:** stays the same however you read it; the letters are "open, playful and unique characters" that form a unity.
- **Logo (Logo chapter):** blends mark and wordmark; designed to be read both ways. Versions: Colour (entry level), Solid (participation and functional), each in standard and small sizes. Outlined and masked versions are special-use and not allowed at small sizes. Sub-pages: Versions, Minimum sizes, Clearspace, Placement, Colour options, Logo on image, Brand architecture, Don'ts, Application, Resources.
- **Identity levels:** Entry (black, premium, clean, with the colour logo; "an invitation to open the door"), Participation (colourful, warm, playful), Functional (editorial, for service and information).
- **Colour:** guided by "the Glow", the energy of human connection as a spectrum. Chapter includes Colour palettes, Colour combinations (Glows, "The Glow contrast", secondary combos), Applying colours (proportions across levels) and Don'ts.
- **Layout:** the "Mirror" system echoes the logotype's symmetry; adaptive to all ratios. Participation grid: columns are a multiple of 4; minimum margins 1/12 of the shortest side; a second "Functional" grid is for editorial work.
- **Chapters:** see §1. Photography shows people with real emotion in outdoor Dutch settings.

## 9. UX
Left rail with in-page sub-anchors; hover reveals hex values; tabs for logo versions. Each page opens with a swipeable photo carousel that sets mood before rules. Weaknesses: grey-on-white nav; colour codes hidden until hover; the chapter page is very long (13 tiles for Logo).

## 10. Craft signals
- Own typeface with display and text optical cuts and 2% tracking on small sizes.
- Six hues with tint ladders in a single repeating 136 px column grid.
- Corner radius system of two values only: 40 px for cards and 9999 px for controls.
- Margin rule tied to format (1/12 of the shortest side).
- Application photos use the same weather: hard sun and white walls.
- The logo's five forms are reused as the shape vocabulary for layout (the Mirror).

## 11. Reproduction recipe
```css
:root{--black:#000;--tech-blue:#2c72ff;--charm-teal:#2f9a92;--solar-yellow:#ffac24;
  --dutch-orange:#ff7621;--warm-pink:#ff808c;--lively-purple:#7066ff;--panel:#ececec;
  --glow-1:linear-gradient(160deg,#ffb4bb 10%,#8fb8b6 50%,#ff9451 95%);
  --glow-2:linear-gradient(170deg,#adc8ff,#ffce7d 45%,#c7c4ff 90%);}
body{font:400 16px/24px "Otypical Text",system-ui;letter-spacing:.02em}
h1{font:500 104px/100px "Otypical Headline"} h2{font:500 64px/64px "Otypical Headline"}
h3{font:500 42px/48px "Otypical Headline"}
.swatch{width:136px;border-radius:9999px 9999px 0 0}
.card{border-radius:40px;overflow:hidden}
.btn{border-radius:9999px;transition:all .15s cubic-bezier(.4,0,.2,1)}
.margin{padding:calc(min(100vw,100vh)/12)}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 9 | Soft Glow gradients, bespoke type and consistent daylight photography feel premium and friendly. |
| Originality | 8 | A letter-shape logo that reads both ways, three-level identity and the Mirror layout are all distinctive. |
| Usability | 7 | Deep, well-structured chapters; grey nav and hover-only hex values slow use. |
| Craft | 8 | Two radii, tint ladders, margin rule tied to ratio; small flaws in nav contrast. |

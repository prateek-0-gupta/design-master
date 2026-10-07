---
id: bg-canva
source: brandguidelines
category: guideline
status: analyzed
title: "Canva Brand Hub - Brand Pillars"
creator: "In-house (Canva)"
styles: [corporate-clean, playful-rounded, photo-led, maximalist-color]
patterns: [sticky-left-section-nav, purple-hero-banner-per-page, core-vs-playground-model, example-tile-with-caption-labels, prev-next-colour-cards, out-of-date-banner, three-col-philosophy-grid, gradient-endframe]
mode: light
palette: ["#7236e6", "#00c4cc", "#c2ff3c", "#272727", "#ffffff", "#000000", "#e986e9", "#f2f3f5"]
type_families: ["Canva Sans (self-hosted, 400/700 loaded)", "Canva Sans heavier cut (tight tracking, headline; hashed font name in census)", "Canva wordmark script (logo only)"]
type_class: [geometric-sans, humanist-sans]
radius_px: [4, 1000]
motion: {durations_s: [0.3, 0.2, 0.25], easing: [ease, ease-in-out], loop: false}
scores: {aesthetics: 7, originality: 6, usability: 7, craft: 6}
craft_signals: [negative-tracking-on-display, consistent-image-radius, labelled-example-tiles, two-circle-diagram-core-playground, banner-pointing-to-new-hub]
anti_patterns: [low-res-blurred-example-media, unlabelled-loading-spinners-in-capture, text-light-pillar-body-small, banner-says-page-outdated]
---
# Canva Brand Hub - Brand Pillars — In-house (Canva)

## 1. Snapshot
- **Subject:** The "Brand Pillars" page of Canva's public brand hub (public.canva.site/brand-pillars). **Wayback Machine snapshot dated 2025-12-10 09:50:29** (`captured_from` = web.archive.org/web/20251210095029if_/...). The live URL was not used. A lime banner on the page itself says it is "a little out of date" and points to a redesigned Brand Hub, so this is Canva's superseded guideline site.
- **Coverage:** one subpage only (the home capture is this page). 4 desktop tiles (1440 px wide, ~1800 px each) and 1 mobile sheet viewed; all 4 desktop tiles seen. The 14 sibling pages in the left nav (Tone of Voice, Logo, Color, Typography, Brand System, Showing UI, Choosing Templates, Photography & Film, Illustration, Motion, Sonic, Accessibility, Localisation) were NOT captured, so nothing is known about their content. Several example tiles show loading spinners and blurred placeholders (capture timing), so media detail is unreliable.
- **Why it's remarkable:** It states the brand as six short pillars plus a "core and playground" model that separates globally fixed elements (logo, gradient, typeface) from locally flexible ones (photography, film).

## 2. Composition & layout
- Page frame: a 1440 px canvas with a 36 px inset white card. Top: lime banner (y 0-66), then a light-grey nav bar (y 66-142) with "Canva Brand" lockup at left and three links at right (Our Brand, Guidelines in purple, Our Agency Partners).
- Hero band: full-width purple #7236e6, about 225 px tall (y 142-368), with a darker purple hand-drawn scribble and pale sparkle stars; title "Brand Pillars" in white right-aligned.
- Body is a two-column grid: sticky left nav about 205 px wide (x 68-273, active item shown as light-grey pill with purple text) and a content column starting at x≈408 that runs to about x≈1352 (~945 px).
- Rhythm: H2 at ~48 px, an intro paragraph at ~26 px, then three-step blocks ("We are human / empowering / inspiring") each with a 16-20 px body paragraph (max ~520 px wide) and a staggered image collage with 24 px rounded corners.
- Philosophy grid: 3 columns × 2 rows (columns ~313 px each, gutter ~12 px).
- Footer: previous/next cards (teal #00c4cc and magenta #e986e9, each ~460×160 px; census radius 4 px), a feedback box (light grey, radius estimated ~16 px), repeated lime banner, link footer, and a black "Designed with Canva" bar.

## 3. Typography
- Census shows self-hosted fonts under hashed names; only "Canva Sans 400 700" is named. Four weight/size cuts dominate. Wordmark is a script and appears only in the logo.
- Scale from census (px / line-height / tracking): 64/89 (hero) · 48 · 37.4/52/-0.93 · 34.2/37/-0.86 · 26.3/31/-0.66 · 21.4/32/-0.53 · 17.95/44 (nav, 14 uses) · 14.7/25 (bold labels, -0.15) · 12/normal (500-600).
- Tracking is negative and proportional to size (about -2.5% on display), which gives the tight look on "Our guiding principles". Weights present: 400 (68), 700 (19), 600 (3). Only two uppercase runs (PREVIOUS / NEXT with +2.2 px spacing).

## 4. Colour
| hex | role | approx share |
|---|---|---|
| #ffffff | page ground | 60-70% of tiles |
| #7236e6 | hero band, active nav, primary brand purple | ~10% of tile 1 |
| #00c4cc | teal: previous card, Core/Playground diagrams | up to 6% |
| #c2ff3c | lime banner | ~3% of tile 1 |
| #272727 | dark example cards | ~5% of tile 3 |
| #000000 | all body text (71 of 88 text runs) | - |
| #e986e9 (sampled) | magenta next-card | small |
| #f2f3f5 | grey chip/nav/feedback panels | small |

- CSS variables (hash-named) also expose #8b3dff, #3d8bff, #db142c, #096d11, #36a137 for UI states.
- Contrast (contrast.py): black on lime #c2ff3c **17.66:1**; black on teal #00c4cc **9.77:1**; white on purple #7236e6 **6.2:1**; white on teal **2.15:1 (fail)**. The page wisely uses black on teal.

## 5. Depth & material
- Almost flat: census records no box-shadow. Depth comes from the photographic collages, soft rounded media crops and the cyan-to-violet gradient tiles (the "endframe" card runs teal at lower-left to violet #7a2be7 at upper-right).

## 6. Components & patterns
- Sticky left TOC with an active pill; hero banner per page; example tiles with bold-lead captions ("Our opening line:", "Our tagline:", "Our endframe:", "Our USP:"); core/playground two-circle diagram; prev/next colour cards; "How can we make this page better?" feedback box with a form link; banner CTA ("View the new Brand Hub", white pill on lime).

## 7. Motion
- Census transitions: `transform .3s ease` (49 uses, mostly the media tiles), `opacity .3s ease-in-out`, `background-color .2s ease`, `opacity .25s ease`. No custom cubic-beziers. Spinners in the capture show lazy-loaded video tiles. Nothing about motion rules was captured, since the Motion page is not in the capture.

## 8. Brand system
- **Pillars:** We are human · We are empowering · We are inspiring, each with three example images. **Creative platforms:** four message slots, each tagged by function (opening line = "inspiring provocation", tagline = "empowering proclamation", endframe = "breadth of product", USP = foundation for communication; the tagline text shown is "With Canva, you can…" and the USP "With Canva, it's easy to design anything…").
- **Philosophies:** Democratise design; Make design personal; Celebrate our community; "Design anything"; Keep it simple; Do the most good we can.
- **Core and Playground:** Core is "Global. Consistent. Familiar." (logo, gradient, Canva Sans, brand-colour square, UI shots); Playground is "Local. Flexible. Surprising." (photography and film that evolve with culture). Drawn as a small solid circle inside a ring vs a thick ring with a hole.
- **Not covered:** logo clearspace, minimum size, palette specs, voice rules - those live on pages not captured. Document structure of the hub: Brand Pillars, Tone of Voice, Logo, Color, Typography, Brand System, Showing UI, Choosing Templates, Photography & Film, Illustration, Motion, Sonic, Accessibility, Localisation (14 pages; only the first captured).

## 9. UX
- Strength: persistent left nav of 14 pages, previous/next cards, and a feedback form. Weakness: the page describes itself as outdated; the example media are small and some are low-resolution; pillar body text (~16 px, grey-black on white) is small relative to the 48 px headings.

## 10. Craft signals
- Display headings use progressively tighter tracking by size (-0.53 px at 21 px to -0.93 px at 37 px).
- All photo crops share the same ~24 px radius; collages stagger tile heights on a common top edge.
- Teal/magenta nav cards carry black text for contrast instead of white.
- Caption convention (bold lead + plain explanation) is applied to all four creative-platform tiles.

## 11. Reproduction recipe
```css
:root{--purple:#7236e6;--teal:#00c4cc;--lime:#c2ff3c;--ink:#000;--panel:#f2f3f5;--dark:#272727}
h1{font:700 64px/1.1 "Canva Sans",system-ui,sans-serif;letter-spacing:-.025em}
h2{font:700 37px/52px "Canva Sans";letter-spacing:-.93px}
.lead{font:400 26px/31px "Canva Sans";letter-spacing:-.66px}
p{font:400 18px/25px "Canva Sans"}
.hero{background:var(--purple);color:#fff;height:225px}
.card{border-radius:24px;overflow:hidden}
.nav-pill[aria-current]{background:var(--panel);color:var(--purple);border-radius:8px}
.next{background:#e986e9;color:#000;border-radius:4px}
.tile{transition:transform .3s ease}
.endframe{background:linear-gradient(45deg,#00c4cc,#7a2be7)}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 7 | Confident purple/teal/lime accents on white, good photo collages; otherwise standard doc page. |
| Originality | 6 | Core-vs-playground model is a useful idea; layout is a familiar docs template. |
| Usability | 7 | Clear nav, short blocks; limited by outdated banner and small body text. |
| Craft | 6 | Consistent radii and tracking; capture shows blurry/loading media (partly snapshot artefact). |

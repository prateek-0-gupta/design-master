---
id: bg-super-com
source: brandguidelines
category: guideline
status: analyzed
title: "Super.com brand portal"
creator: "In-house (hosted on Frontify)"
styles: [playful-rounded, flat-illustration, maximalist-color, corporate-clean]
patterns: [full-width-magenta-nav-bar, thumbnail-card-index-of-chapters, mascot-as-brand-device, pill-cta, icon-set-tile, mini-illustration-system, ai-in-creative-production-section, print-and-copy-link-floating-toolbar]
mode: light
palette: ["#ff0099", "#ffffff", "#000000", "#260d55", "#0c0c62", "#2b2b9c", "#ffbb00", "#87d2f8"]
type_families: ["Montserrat (Black 900 headline, 700, 600, 400)", "Poppins 500 (button)", "Diatype (portal chrome, Frontify default)"]
type_class: [geometric-sans, rounded-sans]
radius_px: [4, 8, 12, 30]
motion: {durations_s: [0.075, 0.15], easing: ["cubic-bezier(0.4,0,0.2,1)"], loop: false}
scores: {aesthetics: 7, originality: 6, usability: 6, craft: 6}
craft_signals: [single-saturated-brand-colour-full-bleed-nav, 12px-card-radius, 3-column-equal-card-index, art-led-cards-without-captions-overlay, last-modified-stamp]
anti_patterns: [index-page-only-captured, white-on-magenta-fails-aa-small, mobile-heading-breaks-mid-word, sticky-bar-repeats-in-stitched-capture]
---
# Super.com brand portal — In-house (Frontify)

## 1. Snapshot
- **Subject:** the Super.com brand portal at brand.super.com, hosted on Frontify. `site_meta.json` shows a redirect to `/document/1#/-/homepage-1`. Only one page was captured, the portal homepage; the "subpage" tiles d01 are identical to the home tiles. The page is 900 px high in the census, with the tiles stitched from scroll captures. The pink nav bar repeats in the screenshot at y≈900 and y≈1183 because it is sticky, and that repetition is a capture artefact, not a design.
- **Why it's remarkable:** the whole portal is an index: nine large art cards (Logo, Colors, Spottie mascot, Illustrations, Typography, Photography, Mini illustrations, Writing, Motion design) stand for the brand itself. A pink bar and a heavy black headline show the colour and the type in the first 2 seconds.
- **Limit:** inner chapters were not captured, so rules (clearspace, hex values, voice) cannot be reported. Only what is visible on the index is analysed.

## 2. Composition & layout
- **Header (1440 px):** a 90 px full-width #ff0099 bar. A search icon is at x≈70, then the items "Brand guidelines" (bold), "Core brand assets", "AI in creative production" and "Press kits" in 14 px white, then the white italic lightning-bolt "Super.com" logo flush right at x≈1230-1380.
- **Hero:** a 70 px / 70 px Montserrat Black headline in two lines, left at x=72, 540 px wide. Beneath, a 20 px / 26 px lead (about 600 px wide) and a magenta pill "Get Started" button (144×45 px, 22-30 px radius).
- **Card grid:** 3 equal columns about 393 px wide at x=80, 523, 967 with a gutter of about 50 px; each card is 393 px square with a 12 px radius. A 1 px light grey border is used for the white cards (Logo, Mini illustrations). The caption is 20 px Montserrat Bold below the card, 8-16 px under. Three rows seen, with a 90-px row gap (about 98 px from caption to next card).
- **Footer:** "Last modified on August 18, 2026 at 8:11 PM" at 12 px grey (#676763) and a floating print/copy-link toolbar, 98×60 px white with a soft shadow, centred.
- **Mobile 390 px:** header 90 px with logo, search and hamburger. The heading wraps at 390 px with "Super.co / m brand" breaking mid-word at 70 px, so the heading does not scale down. The lead reflows at 20 px and the button follows. The first card is narrower than the gutter (230 px wide) and is centred.

## 3. Typography
Census: Montserrat is the main face (weights 900, 700, 600, 400). Sizes: 70 px (1), 20 px (10), 14 px (5), 16 px, 12 px.

| Role | Spec |
|---|---|
| H1 | Montserrat 900, 70 px / 70 px (line-height 1.0), letter-spacing normal |
| Card title (H3) | Montserrat 700, 20 px / 26 px |
| Lead | Montserrat 400, 20 px / 26 px |
| Nav | Montserrat 600 / 400, 14 px / 16.8 px |
| Button | Poppins 500, 16 px / 20.8 px |
| Meta | Montserrat 400, 12 px / 18 px |

The portal CSS also declares Diatype/Geist fallbacks (Frontify theme). Tracking is `normal` everywhere (19 of 19 samples): no optical tuning. The "Aa" card for Typography shows a 200 px or larger specimen in white on magenta; the specimen is clipped by the sticky bar in the capture.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #ffffff | page and card ground | ~49-78% |
| #ff0099 | brand magenta (nav, CTA, Typography tile, mascot) | 21.5% of tile 1 |
| #000000 | headline text | |
| #260d55 | deep violet (illustration dark) | 4% |
| #0c0c62 | deep navy, Motion tile | 6% |
| #2b2b9c / #87d2f8 / #3399d6 | blues in the swatch card | accents |
| #ffbb00 | yellow in the swatch card, coins, icons | accent |
| #ffdcec / #ff9fd2 | pink tints in the swatch card | accents |
| #f5ccff | portal highlight (CSS variable) | UI only |
| #676763 | meta text | |

The swatch card is a 3×3 grid: row 1 magenta, light pink, pale pink; row 2 navy, indigo, sky; row 3 yellow, white, blue. This shows the palette as a tonal grid of pink, blue, yellow plus white.

WCAG: black on #ff0099 is **5.71:1**; white on #ff0099 is only **3.68:1**, which fails AA at 14 px (nav items) and passes only for large text. White on #0c0c62 is **16.87:1**. #676763 on white is **5.68:1**. #e00087 on white is **4.65:1**. The nav uses white 14 px on magenta, so it fails AA for small text.

## 5. Depth & material
Mostly flat. The one shadow in the census is the toolbar's `0 4px 24px rgba(17,17,16,.2)`. Radii are 12 px (cards, 9 uses), 30 px (pill), 8 px and 4 px. The mascot "Spottie" (a magenta sphere with hand and foot outlines and a small ground shadow) gives volume through a darker magenta crescent. Photography cards carry a coloured arc overlay (magenta, indigo) crossing the photo.

## 6. Components & patterns
- Sticky 90 px magenta nav with dropdown chevrons.
- Pill CTA.
- Art-led index card: image, then bold caption, no description text.
- Mini illustration icon grid (3×3: hotel, treasure chest, power bolt, plane, piggy bank, gauge, basket, suitcase, wallet) in a flat-with-highlight style.
- Photography is warm, candid, smiling or hands-on (laptop, phone), overlaid with arcs.
- A motion card on #0c0c62 shows icons in white circles orbiting along thin ellipses with dashed paths.
- Floating print / copy-link toolbar.

## 7. Motion
CSS: transitions of 0.15 s `cubic-bezier(0.4,0,0.2,1)` for colour and transforms and 0.075 s opacity. A "Motion design" chapter exists (orbiting coins) but its rules are not visible.

## 8. Brand system
(Promoted index page; short.) Chapters visible: Logo, Colors, Spottie (mascot), Illustrations, Typography, Photography, Mini illustrations (marketing icons), Writing, Motion design. The nav adds "Core brand assets", "AI in creative production" and "Press kits". The italic lightning-bolt wordmark with a bolt shows speed; magenta is used as a signature field. Useful decisions: a mascot as a first-class chapter; an explicit AI-in-creative-production section; the use of a tonal 3×3 palette card.

## 9. UX
It is quick to scan: 9 cards, 3 per row, each a clear label. Weaknesses: card art does not say what is inside; nav text fails AA on magenta; the mobile headline breaks mid-word; nothing in the capture shows the rules.

## 10. Craft signals
- Single saturated #ff0099 used for the full-bleed bar, CTA and the Typography card, so the brand is recognisable at thumbnail size.
- All cards are 393 px squares with 12 px radius and consistent caption spacing.
- Black Montserrat 900 with 1.0 line-height gives tight, poster-like headlines.
- Palette presented as one cell grid card.
- "Last modified" timestamp builds trust.

## 11. Reproduction recipe
```css
:root{--magenta:#ff0099;--ink:#000;--navy:#0c0c62;--violet:#260d55;--yellow:#ffbb00;--sky:#87d2f8;--ease:cubic-bezier(.4,0,.2,1)}
.nav{height:90px;background:var(--magenta);color:#fff;font:600 14px/16.8px Montserrat,sans-serif}
h1{font:900 70px/70px Montserrat,sans-serif;max-width:540px}
.lead{font:400 20px/26px Montserrat,sans-serif;max-width:600px}
.cta{background:var(--magenta);color:#fff;font:500 16px/20.8px Poppins,sans-serif;padding:12px 26px;border-radius:30px;transition:all .15s var(--ease)}
.grid{display:grid;grid-template-columns:repeat(3,393px);gap:50px 50px;padding-left:80px}
.card{aspect-ratio:1;border-radius:12px;overflow:hidden;border:1px solid #e2e2dd}
.card+h3{font:700 20px/26px Montserrat,sans-serif;margin-top:8px}
.toolbar{box-shadow:0 4px 24px rgba(17,17,16,.2);border-radius:8px}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 7 | Confident pink and navy, warm mascot art, strong headline. |
| Originality | 6 | Mascot and AI-production chapters add character; the Frontify format is standard. |
| Usability | 6 | Clear index, but inner content unseen, white-on-pink small text and a mobile heading that breaks. |
| Craft | 6 | Even card grid and tokens; no tracking tuning, brittle mobile heading. |

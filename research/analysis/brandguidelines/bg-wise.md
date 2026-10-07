---
id: bg-wise
source: brandguidelines
category: guideline
status: analyzed
title: "Wise Design (wise.design root)"
creator: "Wise (in-house)"
styles: [corporate-clean, playful-rounded, photo-led, minimal-swiss]
patterns: [pill-shaped-image-carousel, circle-to-rounded-card-expansion, segmented-pill-tab-switch, play-pause-ambient-carousel, rotating-localised-footer-credit, scroll-progress-bar, lazy-placeholder-grey-pills, docs-link-with-lock]
mode: light
palette: ["#9fe870", "#163300", "#223d0d", "#e2f6d5", "#f0f0f0", "#ffffff", "#000000"]
type_families: ["Inter (Regular, Semi Bold; Tailwind default sans stack)"]
type_class: [neo-grotesk]
radius_px: [64, 50, 999]
motion: {durations_s: [0.6], easing: [ease-out, "cubic-bezier(0.4,0,0.2,1)", "cubic-bezier(0,0,0.2,1)"], loop: true}
scores: {aesthetics: 7, originality: 8, usability: 5, craft: 7}
craft_signals: [forest-green-and-lime-pair-from-brand, pill-geometry-everywhere, real-photo-thumbnails-in-pill-shapes, soft-0.04-alpha-shadows, localised-credit-line-cycle]
anti_patterns: [captured-in-loading-state, foundations-page-404, content-hidden-behind-js-carousel, 12px-captions]
---
# Wise Design (wise.design root) — Wise (in-house)

## 1. Snapshot
- **Subject:** The home of wise.design, Wise's design-team showcase. **Captured from the live root `https://wise.design/`** (`captured_from`), not from Wayback, because the requested `/foundations` URL now returns 404 (`requested` = wise.design/foundations, `final` = wise.design/). The site's own nav lists only Inspiration and Direction; Docs is shown behind a lock icon on mobile.
- **Coverage (explicit):** 17 viewport frames `d00_home_w01-w17` (1440×900, smooth-scroll/animated site, so they are screenshots of one animated screen, not a tiled page). I viewed 7 (w01, w03, w05, w08, w11, w14, w17) and mobile sheet 1. Frames w05 onward are visually identical: the carousel is stuck in a lazy-loading state (grey placeholders where images belong) and only the footer credit line changes language between frames (e.g. Spanish, Cyrillic, Korean, Vietnamese, Filipino). So only the Inspiration tab was seen, and only one project card ("Prompts and critical banners") with its text. The Direction tab and foundations content (colour, type, logo rules) were NOT captured.
- **Why it's remarkable:** The whole page is one horizontal carousel of pill-shaped photo cards that expand into a large rounded card with a title, description and tags - a gallery of the brand in the world (cards, trams, stands, ads) rather than a rulebook.

## 2. Composition & layout
- Header (y 30-78): a 40 px rounded logo tile (Wise "flag" in lime on a green-teal painted texture) at x=32; a centred 252×48 segmented control (Inspiration active in dark green with lime text, Direction in light-green tint); a 44 px circular play/pause button at right (x≈1386).
- Stage: a horizontal row of 120 px-tall pill/circle thumbnails (y 390-510) with 160 px photo thumbnails for loaded images; widths vary (120, 160, 212 px) producing a bead-on-string rhythm. The active item expands to a ~480×480 px rounded card (radius ≈64 px) placed to the right (x 852-1332, y 210-690), with a 12-13 px bold title at the left (868 px), a 12 px grey description (~360 px wide) and 12 px tag chips ("Design Systems", "Product Discovery", "Event Design").
- Footer strip: bottom-left credit "Designed by Wise" (cycles through locales with a vertical text swap), centred scroll-progress track 160×9 px (dark navy thumb on light grey), bottom-right "Instagram" / "Careers" links.
- Mobile (390 px): carousel turns vertical: stacked pills of 124 px width down the page, a pill nav with globe and filter icons, and a "Docs" button with lock icon. Footer text overlaps pills slightly (visible overlap of "Wise Platform at Sibos 2025" label).

## 3. Typography
- Inter only, with named instances "Inter:Regular" and "Inter:Semi Bold" (Figma-export naming). Census: 12/18 400 (labels, tag text), 16/24 600 with -0.176 px tracking (nav "Inspiration"/"Direction"), 12 normal. Everything is small; no heading level exists (census `headings` empty). Scale effectively 12 / 16. Tracking -1.1% on 16 px nav.

## 4. Colour
| hex | role | approx share |
|---|---|---|
| #ffffff | page ground | 62-86% of frame |
| #f0f0f0 | loading placeholders, card well | up to 34% of w03 |
| #163300 | forest green: active tab, text | small |
| #9fe870 | Wise lime: active tab label, logo | small |
| #223d0d | dark green tab fill / hover | small |
| #e2f6d5 (60%) | segmented control track | small |
| #000000 | body text | small |

- Contrast: #163300 on #9fe870 **9.45:1**; lime #9fe870 on #223d0d **8.18:1**; black on #f0f0f0 **18.43:1**. The grey placeholder gives about 1.1:1 against white (decorative).
- Photo content is dominated by green (cards, trams, screens), reinforcing the palette.

## 5. Depth & material
- Shadow in census: `0 10px 15px -3px oklab(0 0 0 / .04), 0 4px 6px -4px oklab(0 0 0 / .04)` on all 30 thumbnails (Tailwind shadow-lg at 4% opacity). Radii: 64 px (30 uses, pills and card), 294 px (3), 999 px, 6.7 px (chips), 50 px. Otherwise flat.

## 6. Components & patterns
- Segmented tab pill; play/pause toggle (icon swaps pause→play); bead carousel with progress scrub bar; expanding card; tag chips; rotating locale credit; footer links. Likely Tailwind v4 (`--tw-*` variables, `--spacing .25rem`) plus Figma-exported fonts; page height variables use `100dvh` and a 48 px/40 px banner offset.

## 7. Motion
- Census: `opacity .6s ease-out` (fade-in of images). CSS also holds Tailwind eases `cubic-bezier(.4,0,.2,1)` and `cubic-bezier(0,0,.2,1)`. The carousel auto-advances (hence a pause button) and the footer credit cycles locale every frame in the sequence; the stuck grey pills show how the lazy-loaded media looked at capture time. Exact carousel speed cannot be measured from stills.

## 8. Brand system
- Visible: lime-on-forest-green pairing, the Wise flag logo as a square tile with painted gradient, rounded/pill geometry, Inter. The content is a gallery of brand applications: cards on grass, event stages, tram livery, packaging, out-of-home ad boards, a trade-show stand ("Wise Platform at Sibos 2025", "Art Meets Science 2026", "Prompts and critical banners"), categorised by tags such as Design Systems, Event Design and Product Discovery. Logo clearspace, minimum size, voice, and token rules are not shown here and were not captured.
- Structure: Inspiration, Direction (not captured), Docs (locked on mobile).

## 9. UX
- Playful, but discoverability is low: all content is in a JS carousel, there is no text headline, 12 px captions are small, and without images (loading state) the page is empty grey. The pause button respects motion preferences; locales show care for global audience. `/foundations` returning 404 means the guideline body is not reachable through this entry.

## 10. Craft signals
- One radius (64 px) shared by pills and the expanded card; thumbnails uniformly 120 px tall.
- Very low-alpha shadows (4%) so pills float without a visible edge.
- Credit line localised in many languages.
- Brand pair #163300/#9fe870 used for the only coloured UI element.

## 11. Reproduction recipe
```css
:root{--forest:#163300;--lime:#9fe870;--forest-2:#223d0d;--mint:#e2f6d5;--well:#f0f0f0}
.tabs{display:inline-flex;padding:4px;border-radius:999px;background:rgb(226 246 213 / .6)}
.tab{font:600 16px/24px Inter;letter-spacing:-.176px;padding:8px 22px;border-radius:999px;color:var(--forest)}
.tab[aria-selected=true]{background:var(--forest-2);color:var(--lime)}
.pill{height:120px;border-radius:64px;overflow:hidden;background:var(--well);
  box-shadow:0 10px 15px -3px rgb(0 0 0 / .04),0 4px 6px -4px rgb(0 0 0 / .04)}
.card{width:480px;height:480px;border-radius:64px;background:var(--well)}
.pill img{opacity:0;transition:opacity .6s ease-out} .pill img.loaded{opacity:1}
.meta{font:400 12px/18px Inter;color:#666}
.chip{font:400 12px/18px Inter;border-radius:999px;background:var(--well);padding:2px 10px}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 7 | Clean white stage, bead-shaped photo pills and a disciplined green palette. |
| Originality | 8 | A carousel of pills that morph into a card is an unusual way to present a brand system. |
| Usability | 5 | Content is small, motion-dependent, loading-state fragile; guidelines themselves are not on this page. |
| Craft | 7 | Consistent geometry, soft shadows, localisation; capture shows stalled media and a few overlaps on mobile. |

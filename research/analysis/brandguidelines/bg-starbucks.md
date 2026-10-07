---
id: bg-starbucks
source: brandguidelines
category: guideline
status: analyzed
title: "Starbucks Creative Expression"
creator: "In-house"
styles: [organic-blob, editorial-serif, corporate-clean]
patterns: [off-canvas-contents-panel, organic-blob-hero, vertical-section-label, half-width-text-column-on-tint, hairline-grid-menu, uppercase-tracked-eyebrow, light-weight-large-body-copy, philosophy-opener]
mode: light
palette: ["#1e3932", "#016241", "#d4e9e2", "#f2f0eb", "#22292f", "#ffffff"]
type_families: ["SODO Sans 300/400/600"]
type_class: [geometric-sans, humanist-sans]
radius_px: []
motion: {durations_s: [0.15, 0.3, 1], easing: [ease], loop: false}
scores: {aesthetics: 7, originality: 7, usability: 5, craft: 6}
craft_signals: [light-300-at-large-size, 49px-leading-on-29px-text, vertical-eyebrow-label, green-tint-ladder, hairline-menu-rows]
anti_patterns: [menu-overlay-captured-over-hero, home-only-coverage, half-page-empty-right-column]
---
# Starbucks Creative Expression — In-house

## 1. Snapshot
- **Subject:** creative.starbucks.com, the "Creative Expression" guide. Wayback Machine capture dated 2026-01-03 20:20:31 UTC (`captured_from` .../web/20260103202031if_/https://creative.starbucks.com/). The live site is not reliably reachable.
- **Coverage:** home only: two tiles (2333 px page) and one mobile sheet. The sections Theory, Case Studies, Logos, Color, Voice, Typography, Illustration and Photography are known only as menu labels.
- **Capture caveat:** the contents menu is rendered open on top of the hero, so the menu items (dark green text, hairlines) collide with the headline. That is a capture artefact, and the right 570 px of the page is empty off-canvas panel. Judge the hero from its design, not the overlap.
- **Why it's remarkable:** a calm, large, light-weight reading experience built from a single organic green blob and a tint ladder.

## 2. Composition & layout
- The viewport is split at about x=870: the left 870 px holds content; the right is a #f1f0eb panel that is the off-canvas menu, with a close "X" at x≈1410.
- Hero: 900 px tall dark green (#1e3932) with a large irregular blob (#016241) spanning x=44–870. Siren logo (about 64 px) plus "Starbucks Creative Expression" 15 px at top-left, x=62.
- Headline "Our new expression." at 72/80 px, weight 400, in white at x=444; intro 15 px/19.5.
- Philosophy section: tint #d4e9e2 field with a rotated 12 px uppercase eyebrow ("OUR PHILOSOPHY") at x≈113 and a hand-drawn Siren, then body at x=230 and about 550 px wide.
- Menu rows are 90 px high separated by 1 px hairlines (#22292f), with an uppercase "CORE ELEMENTS" group label.

## 3. Typography
SODO Sans only (300, 400, 600):
- Display 72/79.9 px, 400, tracking 0.72 px (+1%).
- Body 29/49 px, **weight 300** (leading 1.69), about 38 characters per line. Set large and light as editorial reading text.
- UI 15/19.5 px, 400, tracking 0.375 px; eyebrow 14/18 px, **600**, uppercase, tracking 2.45 px (0.175em); small 12/21 px 300.
- No serif despite the editorial feel.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #f1f0eb | page ground, menu panel | 39% |
| #d4e9e2 | philosophy tint | 25–50% |
| #016241 | blob (Starbucks green, rich) | 21% |
| #1e3932 | hero ground (House Green) | 7% |
| #22292f | text, hairlines | — |
| #aabdb9, #c1d5cf | intermediate tints | few % |

Contrast: #22292f on #d4e9e2 **11.61:1**; on #f2f0eb **12.93:1**; white on #1e3932 **12.45:1**; white on #016241 **7.43:1**. The tint ladder passes AAA comfortably.

## 5. Depth & material
Flat. No shadows or radii. Shape is a single freeform blob overlapping the ground; no photography on the captured portion.

## 6. Components & patterns
Off-canvas contents panel; vertical rotated eyebrow; blob hero; hairline menu list; uppercase tracked group label.

## 7. Motion
Transitions: `transform 0.15 s ease` (9 nodes, menu rows), `opacity/transform 0.3 s` and `1 s` (reveal), `width 0.3 s`, `left 0.3 s` (panel slide), `opacity, margin, letter-spacing 0.3 s` (menu hover widening tracking). Single `ease` curve throughout.

## 8. Brand system
Home-page evidence only.
- **Philosophy:** evolve a design system that keeps the core (Siren logo, an expanded palette of greens rooted in the apron, a constrained family of typefaces) while putting customer experience first; "optimistic, joyful and recognizably Starbucks"; coffee and art as connectors.
- **Chapters (from nav):** Theory; Case Studies; Core Elements: Logos, Color, Voice, Typography, Illustration, Photography.
- **Tokens worth stealing:** a green ladder (#1e3932 → #016241 → #d4e9e2 → #f2f0eb); 300-weight 29 px body with 49 px leading; 0.175em tracked 600 eyebrows.
- **Unknown:** logo clearspace, min size, any numeric rules.

## 9. UX
Reading comfort is excellent (line length, leading, contrast). Navigation is hidden behind "Contents", and the empty half-width panel looks broken when captured.

## 10. Craft signals
- Light weight scaled up rather than a heavier size-down.
- Vertical eyebrow anchors each section without a heading.
- Tinted fields change per section, giving rhythm with one hue.
- Hairlines in text colour, not grey.

## 11. Reproduction recipe
```css
:root{--house:#1e3932;--green:#016241;--tint:#d4e9e2;--paper:#f2f0eb;--ink:#22292f}
body{font:400 15px/19.5px "SODO Sans",system-ui,sans-serif;letter-spacing:.375px;color:var(--ink);background:var(--paper)}
.hero h1{font:400 72px/80px "SODO Sans";letter-spacing:.72px;color:#fff}
.lede{font:300 29px/49px "SODO Sans";max-width:550px;background:var(--tint)}
.eyebrow{font:600 14px/18px "SODO Sans";letter-spacing:2.45px;text-transform:uppercase;writing-mode:vertical-rl;transform:rotate(180deg)}
.menu li{height:90px;border-top:1px solid var(--ink);transition:transform .15s ease}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 7 | Calm green ladder and generous reading type. |
| Originality | 7 | Blob hero and vertical eyebrow are distinctive. |
| Usability | 5 | High contrast, but hidden nav and little verifiable depth. |
| Craft | 6 | Strong type decisions; capture shows overlay collision. |

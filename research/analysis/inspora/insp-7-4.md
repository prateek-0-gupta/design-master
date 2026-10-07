---
id: insp-7-4
source: inspora
category: Motion
status: analyzed
title: "Carousel animation"
creator: "@YousufSoomroDev"
styles: [minimal-swiss, organic-blob, photo-led, kinetic-type]
patterns: [vertical-project-carousel, gooey-metaball-bridge, scroll-velocity-skew, index-list-active-highlight, four-column-meta-row, hover-view-pill]
mode: light
palette: ["#f8f8f8", "#000000", "#bdbdbd", "#e5e6e6", "#7d655a", "#4e342d"]
type_families: ["Jost / Futura-style geometric sans (likely)"]
type_class: [geometric-sans]
radius_px: [36, 9999]
motion: {durations_s: [1.97, 1.87, 1.13, 1.17, 0.33], easing: [ease-in-out, ease-out], loop: false}
scores: {aesthetics: 9, originality: 9, usability: 6, craft: 8}
craft_signals: [liquid-neck-samples-neighbour-colours, cards-deform-with-velocity, meta-row-on-card-centreline, active-index-in-black-rest-in-grey, text-scramble-on-change, single-near-white-canvas]
anti_patterns: [index-list-1.8-to-1-contrast, long-motion-may-cause-vestibular-issues]
---
# Carousel animation — @YousufSoomroDev

## 1. Snapshot
- **Subject:** A 44.6 s, 2560×1626 at 60 fps screen recording of a portfolio index. Project cards travel vertically through the centre of a near-white page, and neighbouring cards are joined by a stretching liquid "neck", like viscous droplets.
- **Why it's remarkable:** The connective tissue between cards is a gooey metaball bridge that takes its colour from the images it joins. A plain vertical list becomes something physical and memorable without breaking a minimal typographic frame.

## 2. Composition & layout
- **Stage:** a single near-white canvas (#f8f8f8, 83% of pixels).
- **Active card:** centred at about 740×500 px (real px), a 1.48 landscape ratio, with corner radius about 36 px.
- **Neighbour cards:** peek in from the top and bottom edges, skewed and squashed into wedges.
- **Meta row:** sits on the card's horizontal centreline (y≈815 real) as four fixed columns: index "11" at x≈130, title "Iris" at x≈265, discipline "Photography" right-aligned to x≈2270 and year "2023" at x≈2440. The row spans the full width so the card floats in the middle.
- **Index list:** 18 project names stacked top-right at x≈2105, y 50→610, with leading of about 33 px. It doubles as a minimap.

## 3. Typography
- **Typeface:** A geometric sans with a round "o", a single-storey "a" and a straight-legged "y", closest to Jost or a Futura derivative.
- **Meta row:** set at two sizes. The title and discipline are about 46 px Regular; the index and year are about 30 px.
- **Index list:** about 24 px.
- **Weight:** a single weight (400) throughout, with no bold. Hierarchy comes from size and black/grey value.
- **Text change:** When the active project changes, the meta-row text glitches or scrambles (37.13 s frame: "Favor" and "E-commerce" rendered as broken glyph fragments) before resolving. This is a text-scramble transition.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #f8f8f8 | canvas | 83% |
| #000000 | active text, black "J" card | 9% |
| #bdbdbd (est.) | inactive index names | <1% |
| #e5e6e6 | soft edges / shadows of deformed cards | 1% |
| #7d655a / #4e342d / #71433b | skin and coffee tones of neighbouring imagery | 3% |

WCAG checks:
- Black on #f8f8f8 is 19.77:1.
- Inactive index items, about #bdbdbd on #f8f8f8, are **1.77:1 (fail)**. They are legible as texture only.

Colour beyond black and white comes entirely from the project imagery: red (MVN), purple, blue (Favor) and red/black (Freshweb).

## 5. Depth & material
- **Flat 2D page;** depth comes from deformation, not shadow.
- **Cards:** skew and taper as they leave the centre. The off-screen ones become trapezoids or wedges, as if bent around a cylinder.
- **Liquid bridge:** a narrow neck, about 20–70 px wide, joins card edges. It is filled with a vertical gradient of the two images' edge colours (black → skin tone in the key frame, blue → purple at 12.38 s). It thins into a 1–2 px thread as cards separate, then snaps.

## 6. Components & patterns
- **Vertical project carousel:** one active card plus partial neighbours.
- **Meta row:** a four-column rhythm (No. / Name / Category / Year), a classic agency index.
- **Index list:** the active item is black and the rest grey; it updates as the carousel moves (Proba → Iris → PM24 → Favor → Freshweb).
- **Hover pill:** a "↗ View" pill (about 90×28 px, radius 9999) appears next to the cursor at 42 s, as a contextual CTA.
- The 2.48 s frame shows an intro state: a tiny thumbnail that grows into the carousel.

## 7. Motion
Measured (m0_motion.json, 60 fps source, 44.56 s, motion_fraction 0.15, not loop-seamless). Six segments:
- **6.00–7.97 s (1.97 s, peak 0.50):** symmetric ease-in-out, a long scroll between projects.
- **14.80–14.93 s (0.13 s, peak 0.12):** a brief ease-out flick.
- **15.37–17.23 s (1.87 s, peak 0.56):** ease-in-out.
- **26.40–27.53 s (1.13 s, peak 0.13):** ease-out. A fast start then a long settle, consistent with inertial or spring scroll.
- **36.67–37.00 s (0.33 s):** coincides with the text scramble.
- **43.13–44.30 s (1.17 s, peak 0.39).**

The median segment is 1.15 s, which is slow and luxurious. Between segments the page sits still while the user dwells. Neck stretching is tied to velocity: frames mid-move (17.33 s, 22.28 s) show the thread thinning as distance grows, so this is likely a shader or SVG goo filter driven by scroll delta.

## 8. Brand system
n/a — this is a portfolio interface, not a brand system. Identity cues: the liquid bridge is effectively the studio's signature, and the strict Swiss meta row signals "agency".

## 9. UX
- **Strengths:**
  - The index list gives orientation (position 11 of 18).
  - The meta row always shows the current project.
  - The hover pill makes the click target explicit.
- **Risks:**
  - The grey list fails contrast.
  - Long 1–2 s transitions and heavy deformation can be uncomfortable and need a reduced-motion path.
  - The neighbour cards are unreadable while warped, so browsing is sequential only.
  - Text scramble briefly makes labels illegible.

## 10. Craft signals
- The bridge takes its colour by blending from the image pixels at each edge. It never uses a flat grey.
- The meta row is locked to the active card's centreline across every frame.
- The active index item is the only black entry in the list, a single-variable state change.
- Cards keep their about 36 px radius even while skewed. The deformation is applied post-shape (mesh), not by CSS skew.
- One typeface and one weight are used for the whole UI.

## 11. Reproduction recipe
```css
:root{--bg:#f8f8f8;--ink:#000;--ink-muted:#bdbdbd;--r-card:36px;--font:"Jost","Futura",system-ui}
.meta{position:fixed;inset:50% 0 auto;transform:translateY(-50%);display:grid;
  grid-template-columns:80px 1fr auto 100px;padding:0 100px;font:400 36px/1 var(--font)}
.meta .n,.meta .y{font-size:24px}
.index li{font:400 18px/1.4 var(--font);color:var(--ink-muted)}
.index li[aria-current]{color:var(--ink)}
.track{filter:url(#goo)}   /* SVG: feGaussianBlur stdDeviation=18 → feColorMatrix alpha 0 0 0 22 -9 */
.card{border-radius:var(--r-card);width:min(40vw,580px);aspect-ratio:1.48;
  transition:transform 1.15s cubic-bezier(.65,0,.35,1)}
@media (prefers-reduced-motion:reduce){.track{filter:none}.card{transition:none}}
```
A faithful bridge needs WebGL: render cards as a vertex-displaced mesh, with an SDF smooth-union (`smin(k≈60px)`) between neighbouring card rectangles, sampling texture colour at the union.

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 9 | Swiss restraint plus one outrageous physical idea; imagery supplies all colour. |
| Originality | 9 | Liquid metaball necks between carousel items are genuinely new. |
| Usability | 6 | Good orientation aids; failing grey index, slow transitions, illegible neighbours. |
| Craft | 8 | Colour-sampled bridge, centreline-locked meta, consistent radius under deformation. |

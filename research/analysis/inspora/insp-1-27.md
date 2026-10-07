---
id: insp-1-27
source: inspora
category: Motion
status: analyzed
title: "Smooth scroll with lens refraction."
creator: "@colton__tollett"
styles: [editorial-serif, physical-material, minimal-swiss, photo-led]
patterns: [vertical-snap-gallery, lens-warp-at-viewport-edges, centred-active-item-caption, chromatic-aberration-edges, pastel-backdrop-product-cards]
mode: light
palette: ["#f2eee5", "#e6dfd5", "#cacaca", "#a5c2b0", "#f7c0a1", "#b9cada", "#529277", "#48443b"]
type_families: ["Ogg / Canela-style high-contrast display serif (likely)", "Inter / Söhne-style sans for labels (likely)"]
type_class: [editorial-serif, neo-grotesk]
radius_px: [16]
motion: {durations_s: [1.8, 2.07, 2.23, 2.93, 1.63], easing: [ease-out, ease-in-out], loop: false}
scores: {aesthetics: 9, originality: 8, usability: 7, craft: 9}
craft_signals: [barrel-distortion-only-at-edges, rgb-fringe-on-warped-items, title-colour-matches-card-bg, active-card-slightly-larger, tracked-caps-label-with-year, cream-canvas-not-white]
anti_patterns: [year-text-very-low-contrast, title-colour-contrast-borderline]
---
# Smooth scroll with lens refraction. — @colton__tollett

## 1. Snapshot
- **Subject:** A 2600×2160, 28.3 s, 60 fps recording of a vertical gallery of vintage computers (Apple II, BBC Micro, Olivetti P101, Macintosh-era machines). Each is photographed on a pastel backdrop in a rounded square card. Scrolling snaps one item to the centre with "MODEL / year" on the left and the model name in serif on the right. Items entering or leaving the viewport edges are warped by a fisheye lens with RGB fringing.
- **Why it's remarkable:** A fisheye-lens edge distortion makes a flat list feel like it is rolling over a glass cylinder, and the centre stays undistorted for reading.

## 2. Composition & layout
- **Canvas:** cream #f2eee5, 2600×2160 (shown 2000 px wide in the key frame).
- **Column:** a single centred column. Cards are about 377×338 px (display 290×260) with gaps of about 57 px. The active card is slightly larger (about 386×356) with a soft shadow.
- **Caption row:** aligned to the active card's vertical centre.
  - Left: "MODEL", tracked caps, right-aligned at about 145 px from the card. Below it the year ("1977").
  - Right: "Apple II" in serif, left-aligned at about 75 px from the card.
- **Edge zones:** at the top and bottom (about 15% each), cards stretch into trapezoids. They are wider at the viewport edge (up to about 640 px) and pinch toward the centre, with bowed sides, which is classic barrel distortion. Their content is blurred and RGB-split.

## 3. Typography
- **Model name:** a high-contrast display serif (Ogg- or Canela-like) at about 52 px (display 40 px), regular. It is coloured to match the active card's backdrop: green #529277 for the Apple II on mint, red-brown for the BBC Micro on peach, plum for the Olivetti on lavender.
- **Label:** "MODEL" in sans caps at about 20 px, tracking about +0.15 em, colour #48443b. The year "1977" is at about 18 px in a very light grey (about #b6b2a9).

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #f2eee5 | canvas | 82% |
| #e6dfd5 / #cacaca | warped edge zones, photo greys | about 15% |
| #a5c2b0 | mint card backdrop (Apple II) | — |
| #f7c0a1 | peach card backdrop (BBC Micro) | — |
| #b9cada | blue card backdrop (Mac) | — |
| #529277 | active title (green variant) | — |
| #48443b | "MODEL" label | — |

WCAG checks:
- "MODEL" #48443b on #f2eee5: 8.38:1.
- Green title #529277 on #f2eee5: **3.16:1**, which passes only as large text. It is about 52 px, so it is acceptable.
- Year #b6b2a9 on #f2eee5: **1.83:1** (fails).

## 5. Depth & material
- **Cards:** photographic product shots with soft studio shadows, radius about 16 px. The active card has a soft drop shadow (about 0 12px 30px rgba(0,0,0,.12)).
- **Lens:** a refraction or barrel warp at the viewport edges, chromatic aberration of about 6–10 px (red, yellow, cyan fringes around the machines), slight blur and a bloom-like brightening. The effect reads as looking through a thick glass edge.

## 6. Components & patterns
- A vertical snap carousel with a centred active item.
- A split caption: metadata left, name right, flanking the image.
- Thematic colour coupling between the caption and the card backdrop.

## 7. Motion
- **Measured:** 28.28 s at 60 fps, `motion_fraction` 0.61, 14 segments, median 0.96 s.
  - Slow scroll glides: 0.93–2.73 s (1.80 s, symmetric) and 8.07–11.00 s (2.93 s, symmetric).
  - Flick-and-settle: 2.93 s (2.07 s, `peak_at` 0.02) and 5.33 s (2.23 s, `peak_at` 0.13), both ease-out.
  - Quick nudges of 0.20–0.47 s.
  - 14.93–18.63 s (3.70 s, ease-in): a slow wind-up.
- **Reading:** a smooth-scroll (Lenis-like) with long decelerating tails of about 2 s. The snap brings the nearest item to centre. The title text swaps per item (frames at t=11.0–14.14 s show "Apple II" holding while the cards shift slightly).

## 8. Brand system
n/a — not a brand system. Identity cues: a museum-catalogue tone (cream paper, serif names, tracked caps metadata) and pastel per-object backdrops.

## 9. UX
- The centre is crisp and readable while the edges communicate "more above/below", a good use of distortion as a scroll affordance.
- The year is nearly invisible (1.83:1).
- Long scroll inertia (about 2 s) can feel floaty for precise browsing.

## 10. Craft signals
- Distortion is confined to the outer about 15% of the viewport, and the centre item is geometrically true.
- Chromatic aberration appears only on warped items, linking the effect to the lens.
- The title colour is sampled from the active card's backdrop, so the caption visually belongs to the image.
- The active card scales by about 2–5% and gains a shadow; neighbours do not.
- The cream canvas (#f2eee5) is warmer than the photo whites, so the cards pop without borders.

## 11. Reproduction recipe
```css
:root{--canvas:#f2eee5;--label:#48443b;--muted:#8e897f;--r:16px}
body{background:var(--canvas)}
.item{width:290px;aspect-ratio:29/26;border-radius:var(--r);overflow:hidden;scroll-snap-align:center;transition:transform .4s,box-shadow .4s}
.item.active{transform:scale(1.03);box-shadow:0 12px 30px rgba(0,0,0,.12)}
.caption .k{font:500 15px/1 Inter;letter-spacing:.15em;text-transform:uppercase;color:var(--label)}
.caption .year{font:400 13px Inter;color:var(--muted)} /* darker than source for AA */
.caption .name{font:400 40px/1 "Canela","Ogg",Georgia,serif;color:var(--accent)} /* = card bg darkened */
```
```glsl
// post-pass: barrel warp + RGB split near top/bottom
float e=smoothstep(.7,1.,abs(uv.y-.5)*2.);          // 0 in centre, 1 at edges
vec2 c=uv-.5; vec2 w=c*(1.-e*.35*(1.-c.x*c.x*4.));  // pinch toward centre column
col=vec3(tex(w+.5+vec2(e*.006,0)).r, tex(w+.5).g, tex(w+.5-vec2(e*.006,0)).b);
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 9 | A refined museum palette; pastel cards on cream with a serif accent. |
| Originality | 8 | The lens-warp scroll edge is a fresh affordance. |
| Usability | 7 | Clear centre focus, but the faint year and long inertia hurt it. |
| Craft | 9 | Distortion is localised, colour coupling is precise, and the snapping is smooth. |

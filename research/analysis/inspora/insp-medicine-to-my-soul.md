---
id: insp-medicine-to-my-soul
source: inspora
category: Illustration
status: analyzed
title: "medicine to my soul"
creator: "cem hasimi"
styles: [generative-particle, dark-premium, x-flow-field-narrative]
patterns: [flow-field-dashes, tiny-figure-vast-field, particle-plume-emotion, two-temperature-palette, short-loop-series, perspective-floor-from-dashes]
mode: dark
palette: ["#03233c", "#180030", "#ffffff", "#e8655a", "#ff2b2b", "#ff9a2a", "#b9b3d9", "#7fb4c8"]
type_families: []
type_class: []
radius_px: []
motion: {durations_s: [0.8, 0.92, 0.92, 0.8], easing: [ease-in-out, ease-out, ease-in], loop: true}
scores: {aesthetics: 9, originality: 9, usability: 5, craft: 8}
craft_signals: [figure-under-1-percent-of-frame, warm-vs-cool-particle-semantics, dash-orientation-encodes-flow, perspective-from-dash-spacing, consistent-series-system, outline-figure-inside-particles]
anti_patterns: [loops-under-1s-visible-jump, figure-too-small-on-mobile]
---
# medicine to my soul — cem hasimi

## 1. Snapshot
- **Subject:** Four very short (0.88–1.0 s, 1280×1280, 25 fps) particle-art loops from a series about grief after losing a pet:
  1. a tiny coral figure alone in a field of blue-white flow dashes beside a bright "shore";
  2. a seated, hunched figure whose head releases a red funnel of particles;
  3. a red particle burst erupting from a point on a horizon;
  4. an outlined figure lying under a vertical column of falling red/orange particles.
- **Why it's remarkable:** Emotion is encoded entirely in particle behaviour: direction, density and temperature. The human is reduced to a few dozen pixels. One visual grammar (short dashes on a flat dark ground) carries four distinct emotional states.

## 2. Composition & layout
- **m0:** The coral figure (~40×45 px, 0.1% of frame) sits at about (350, 540), a left-third/centre-height point. A diagonal "shoreline" of dense white dashes splits the frame at x≈650–850, so the figure faces a wall of light across ~300 px of empty sea.
- **m1:** The figure (~110 px) sits at about (460, 1050), in the bottom third and left of centre. A red plume rises from it, widening from ~40 px to the full frame width at the top. The composition is a V or funnel, with the dash field curving around the figure like a whirlpool.
- **m2:** The burst origin is at the exact centre-x and y≈740 (58%). The horizon is implied at y≈600–740 by the border between dense red above and sparse white below, a one-point-perspective floor.
- **m3:** A vertical red column ~520 px wide, centred, falls onto a lying figure outline (~480 px long) at y≈990. Vertical white dashes on the sides curve into a floor at y≈900, forming a box-room perspective.

## 3. Typography
None.

## 4. Colour
| Hex | Role | Clip |
|---|---|---|
| #03233c | deep sea-navy ground | m0 (77%) |
| #180030 / #1d0131 | ink-violet ground | m1–m3 (65–79%) |
| #ffffff / #b9b3d9 | cool flow dashes (environment) | all |
| #7fb4c8 | faint teal dashes (far field) | m0 |
| #e8655a | coral figure | m0 |
| #ff2b2b / #7f052f | red emotion particles | m1–m3 |
| #ff9a2a | orange highlight particles | m1–m3 |

The semantics are consistent: **cool = world, warm = feeling.** The figure or the emotion is always the only warm element.

Contrast on ground:
- Coral on navy is 4.92:1.
- White dashes on navy are 16.04:1.
- Red particles on violet are 5.21:1.
- Orange is 9.16:1.
- Lavender dashes are 9.72:1.

Orange particles read as "nearer/hotter" than red because of their higher luminance.

## 5. Depth & material
- **Depth from dash spacing:** Dash length and spacing shrink toward vanishing points. m2's floor dashes radiate from the burst origin, and m3's side walls bend into the floor, so 3D rooms are built without any surfaces.
- **Size gradient:** Particles get larger toward the camera (m2 top particles ~12×4 px vs ~4×2 px near the origin).
- **No glow or blur:** Everything is flat, which keeps a print-like, risograph honesty.

## 6. Components & patterns
- Flow-field rendering: each dash is oriented along a vector field (whirlpool in m1, radial in m2, vertical in m3).
- A tiny figure in a vast field for scale and loneliness.
- Outline-only figure (m3), filled with particles of the same red, so the body and the emotion share one material.
- A series system: same dash grammar, same ground darkness, warm/cool split, square 1:1 format.

## 7. Motion
Measured values (`m{N}_motion.json`). Each is one continuous segment, with no seamless loop detected:

| Clip | Duration | Motion fraction | Peak at | Shape |
|---|---|---|---|---|
| m0 | 0.80 s | 1.0 | 0.38 | symmetric ease-in-out (CV 0.09, very steady drift) |
| m1 | 0.92 s | 0.96 | 0.28 | ease-out (fast start); the plume surges then settles |
| m2 | 0.92 s | 1.0 | 0.72 | ease-in (slow start); the burst builds |
| m3 | 0.80 s | 1.0 | 0.57 | ease-in-out |

The first/last diffs are 14.5, 5.7, 7.9 and 11.6, so every clip will jump on repeat. They are GIF-like micro-loops (about 20–23 frames). Visually the figures stay fixed and only the particles advance along their field. Estimated travel is about 20–40 px per frame for red particles and 5–10 px for white dashes, so the emotion moves faster than the world.

## 8. Brand system
n/a — this is not a brand system. The artist's recurring signature (shared with "I want to run again") is a single small figure as anchor in a dense particle world.

## 9. UX
Not interactive. As editorial illustration it communicates instantly, since the warm element is always the subject. On mobile a 1280 px square shown at ~360 px shrinks the m0 figure to ~11 px, nearly lost. The sub-second loops with visible seams would feel jittery as ambient backgrounds; they work better as short social posts.

## 10. Craft signals
- The warm/cool temperature split is maintained across all four clips.
- In m0 the figure is under 0.2% of the frame area yet is the first fixation (the only warm hue).
- The dash orientation field differs per clip (whirlpool, radial, vertical), matching each emotional verb (spiral, explode, pour).
- Room perspective is built from dash-direction bends alone (m3).
- The outline figure in m3 is drawn with a 1.5 px white line, the only line element, echoing the series' line-figure motif.

## 11. Reproduction recipe
```css
:root{--ground-sea:#03233c;--ground-ink:#180030;--dash:#ffffff;--dash-dim:#b9b3d9;--self:#e8655a;--feel:#ff2b2b;--feel-hot:#ff9a2a}
.canvas{aspect-ratio:1;background:var(--ground-ink)}
```
```js
// p5.js sketch: flow-field dashes + warm emotional plume
function draw(){ background('#180030');
  for (const p of field){ const a = angleAt(p.x,p.y);              // whirl / radial / vertical per scene
    stroke(p.warm ? random(['#ff2b2b','#ff9a2a']) : '#b9b3d9');
    strokeWeight(p.warm ? map(p.z,0,1,2,5) : 1.2);
    line(p.x,p.y,p.x+cos(a)*p.len,p.y+sin(a)*p.len);
    p.x += cos(a)*(p.warm?30:8); p.y += sin(a)*(p.warm?30:8); wrap(p); }
  drawFigure();                                                    // tiny outline or filled #e8655a
}
```
To get seamless loops, use a periodic noise offset (`noise(x, y, cos(t*TAU), sin(t*TAU))`) over a 1–4 s period.

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 9 | Two-temperature palette and dash fields are poetic and cohesive across the series. |
| Originality | 9 | Emotion expressed purely as particle physics around a tiny figure is a distinctive authored language. |
| Usability | 5 | Seamed sub-second loops; the figure disappears at small sizes. |
| Craft | 8 | Consistent system and perspective-from-dashes; the loops are not closed. |

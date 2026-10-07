---
id: insp-1-40
source: inspora
category: Web
status: analyzed
title: "A bento card"
creator: "Maxim Kuznetsov"
styles: [dither-halftone, retro-pixel, dark-premium, technical-wireframe]
patterns: [bento-feature-card, dithered-3d-object, pixel-field-backdrop, two-tone-sentence-emphasis, dashed-layout-guides, crosshair-corner-marker]
mode: dark
palette: ["#000000", "#191919", "#393939", "#757575", "#a6a6a6", "#c8c8c8", "#f2f2f2"]
type_families: ["Haffer / Neue Haas-style grotesk with ink-trap feel (likely)"]
type_class: [neo-grotesk]
radius_px: [0]
motion: {durations_s: [4.63], easing: [ease-in-out], loop: true}
scores: {aesthetics: 9, originality: 8, usability: 7, craft: 9}
craft_signals: [ordered-dither-on-rotating-3d, two-dither-scales-object-vs-field, sentence-split-white-then-grey, crosshair-at-card-corner, dashed-guides-at-low-alpha, hairline-card-border-1px]
anti_patterns: [backdrop-noise-competes-with-card, motion-heavy-for-a-card]
---
# A bento card — Maxim Kuznetsov

## 1. Snapshot
- **Subject:** A 4.67 s, 2056×1894 (about 2× retina) clip of a single dark bento card for a cross-chain protocol, "Closed-Loop Consensus". A rotating 3D loop-arrow ring is rendered as 1-bit ordered dither and floats over a backdrop of large blocky dither "clouds" that drift past.
- **Why it's remarkable:** It is a fully 1-bit aesthetic in motion. Two dither scales separate foreground from background: fine dots (about 8 px) for the object and coarse squares (about 16 px) for the field. Depth comes from pixel density alone, with no blur or colour.

## 2. Composition & layout
- **Card:** about 855×1095 px in the capture (about 428×548 CSS px), x 570→1425, y 452→1545. Square corners, a 1 px #393939-ish border and a solid #000 fill that masks the field behind it.
- **Inside the card (about 76 px padding):**
  - the dithered ring at y≈600–940 (about 680 px wide);
  - an eyebrow "Closed-Loop Consensus" at y≈1070;
  - a 4-line statement at y≈1140–1460.
- **Backdrop:** a layout grid of dashed 1 px lines at about 15% grey (verticals at x≈155/668/1327/1836, horizontals at y≈552/1443) plus a faint dot grid. A crosshair "+" sits exactly on the card's bottom-right corner.
- The dither clouds enter from the top-left and bottom-right diagonals, framing the card.

## 3. Typography
- One grotesk with slightly squarish curves and open apertures, reading like Haffer or Neue Haas Unica.
- **Statement:** about 60 px in the capture (about 30 CSS px), medium (500), leading about 1.42, tracking about −0.01 em.
- **Two-tone sentence:** "Every block reinforces the next," is in near-white #f2f2f2, and the remainder "enabling safer, faster cross-chain transfers." is in #757575. The tint carries the emphasis instead of weight.
- **Eyebrow:** about 32 px capture (16 CSS), regular, #a6a6a6.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #000000 | canvas and card fill | 78% |
| #191919 / #2c2c2c | dot grid, dashed guides | 5% |
| #393939 | card border | 2% |
| #4a4a4a–#8b8b8b | dither mid-tones, secondary text #757575 | 6% |
| #a6a6a6 / #c8c8c8 | eyebrow, dither highlights | 4% |
| #f2f2f2 | primary text, dither pixels | — |

WCAG checks:
- Primary #f2f2f2 on #000 is 18.8:1.
- Secondary #757575 on #000 is 4.56:1 (just passes AA).
- Eyebrow #a6a6a6 is 8.63:1.
- The border #393939 is 1.82:1, decorative only.

## 5. Depth & material
- **Object:** a glossy 3D torus with two arrows, converted to an ordered/Bayer-like dither. Specular highlights become solid pixel clusters, which preserves the sense of material through dot density.
- **Field:** a coarse dither cloud (bigger squares) behind the card's solid black, giving a clear z-order of field → card → object.
- There is no blur, glow or shadow anywhere. Depth uses halftone scale only.

## 6. Components & patterns
- A bento cell with an illustration slot, eyebrow and statement, and no CTA.
- A two-tone statement pattern: the first clause bright, the continuation grey.
- **Wireframe furniture:** dashed guides and a "+" registration marker, giving a design-spec/blueprint vibe.

## 7. Motion
- **Measured:** 4.67 s at 55 fps. motion_fraction is 0.75 (motion almost the whole time) and there is one continuous segment of 4.63 s with peak_at 0.46, i.e. symmetric ease-in-out. The detector says it is not a seamless loop (first/last diff 7.35), but the frames show the ring returning to its t=0.26 s pose at t=4.41 s, so it is effectively a loop of about 4.6 s.
- **Ring:** rotates through about 360° on a tilted axis. Mid-cycle (t=2.34–3.38 s) it is seen edge-on and the arrows almost disappear, then re-emerge.
- **Backdrop clouds:** translate diagonally (top-left → bottom-right, an estimated 150–250 px per cycle) with per-cell flicker as the dither threshold re-evaluates.

## 8. Brand system
n/a — not a brand system. Identity cues:
- a 1-bit dither visual language;
- blueprint guides;
- monochrome with emphasis by grey value.

These suit a crypto-infrastructure brand.

## 9. UX
- As a marketing card it reads instantly: the eyebrow names the feature, the sentence explains it, and the visual shows a loop.
- **Risks:**
  - The large animated backdrop competes for attention.
  - There is no `prefers-reduced-motion` evidence.
  - The secondary grey sits exactly at the AA threshold.

## 10. Craft signals
- Two distinct dither pitches: about 8 px cells in the object vs about 16 px squares in the field, which keeps the layers legible.
- The card's solid #000 fill knocks out the field, so the text never sits on dither.
- The crosshair "+" is centred precisely on the card's bottom-right corner.
- The dashed guides align with the card's top and bottom edges (y≈552 is the card top + 100, y≈1443 is near the card bottom − 100).
- Emphasis is a colour split within a single sentence, not a separate headline.
- The palette is pure greyscale: 7 steps from #000 to #f2f2f2, with no hue.

## 11. Reproduction recipe
```css
:root{--bg:#000;--line:#393939;--guide:#2c2c2c;--text:#f2f2f2;--text-2:#757575;--eyebrow:#a6a6a6}
.stage{background:
  radial-gradient(circle,#191919 1px,transparent 1.5px) 0 0/28px 28px,var(--bg)}
.card{position:relative;width:428px;padding:38px;background:var(--bg);border:1px solid var(--line);border-radius:0}
.card::after{content:"+";position:absolute;right:-7px;bottom:-11px;color:#666;font:300 20px/1 monospace}
.card .eyebrow{font:400 16px/1.3 "Haffer",Inter,sans-serif;color:var(--eyebrow)}
.card p{font:500 30px/1.42 "Haffer",Inter,sans-serif;letter-spacing:-.01em;color:var(--text-2)}
.card p strong{color:var(--text);font-weight:inherit}
.guide{border-left:1px dashed var(--guide)}
```
```glsl
// fragment: ordered dither of a lit torus
float bayer4(vec2 p){ /* 4x4 Bayer threshold */ }
gl_FragColor = vec4(vec3(step(bayer4(floor(gl_FragCoord.xy/4.0)), lum)),1.0);
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 9 | A rigorous 1-bit world with striking motion and calm type. |
| Originality | 8 | Dithered 3D in a bento cell, with two halftone scales for depth, is a fresh combination. |
| Usability | 7 | Clear message and contrast. The busy animated backdrop may distract. |
| Craft | 9 | Precise corner marker, guide alignment and layer knock-out. |

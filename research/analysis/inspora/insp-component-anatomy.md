---
id: insp-component-anatomy
source: inspora
category: Motion
status: analyzed
title: "Component Anatomy"
creator: "@MSchwaibold"
styles: [isometric, technical-wireframe, hairline-ui, soft-3d]
patterns: [exploded-layer-stack, component-anatomy-diagram, layer-reorder-by-drag, glass-orb-cursor, wireframe-skeleton-layer, grid-baseline-layer, music-player-card]
mode: light
palette: ["#ffffff", "#fbeef8", "#e5ddee", "#e6edfb", "#1c1c1c", "#8a8a8a", "#927588", "#5a63f0"]
type_families: ["Inter (likely)"]
type_class: [neo-grotesk]
radius_px: [64, 24, 9999]
motion: {durations_s: [0.6, 0.43, 0.5, 0.57, 0.6, 0.33], easing: [ease-out, ease-in-out], loop: true}
scores: {aesthetics: 8, originality: 8, usability: 6, craft: 8}
craft_signals: [four-semantic-layers-same-footprint, pastel-coding-per-layer, live-progress-keeps-ticking-while-exploded, glass-sphere-cursor-refracts-grid, hairline-skeleton-labels-title-body-cap, soft-contact-shadows-under-each-plane]
anti_patterns: [secondary-grey-below-aa, low-contrast-layer-labels]
---
# Component Anatomy — @MSchwaibold

## 1. Snapshot
- **Subject:** A 10.9 s, 1996×2160 loop in which a flat music-player card ("The Visit — Agar Agar") tilts into isometric space and explodes into four stacked planes — content, skeleton, layout blocks, grid — that a glass-ball cursor reorders before they collapse back.
- **Why it's remarkable:** It teaches design-system anatomy (content sits on structure sits on layout sits on grid) as a physical object, and the player keeps playing (3:48 → 3:57) throughout, proving it is one live component.

## 2. Composition & layout
- Flat state: card ≈1070×600 px centred on pure white, artwork 290 px square at left, title/artist and transport to the right, full-width progress bar below.
- Exploded state: planes rotated ≈30° about X and ≈−15° about Z (isometric-ish), vertical spacing ≈330 px, each plane the same footprint so edges align as a column.
- Layers top-to-bottom in the key frame: layout blocks (lavender/blue rectangles on a pink-gridded frame), skeleton ("Title / Body / Cap." with grey placeholders), content card, and 8 px graph-paper grid.
- Negative space ≥35% on every side; the stack occupies the middle 60% of the frame.

## 3. Typography
- Inter-like neo-grotesk. Title "The Visit" ≈44 px regular #1c1c1c; artist ≈34 px #8a8a8a; time stamps ≈30 px #6e6e6e with tabular numerals ("3:48 / −0:22").
- Skeleton layer reuses the same type positions as labels — "Title", "Body", "Cap." — in grey hairline style, an annotation voice.
- No bold anywhere: hierarchy is size + grey.

## 4. Colour
| Hex | Role | Share (key frame) |
|---|---|---|
| #ffffff | canvas, card surface | 83% |
| #fbeef8 | pink grid/frame (layout layer) | 13% |
| #e5ddee | lavender layout blocks | 2.5% |
| #e6edfb | pale blue layout blocks | — |
| #1c1c1c | title, play button | — |
| #8a8a8a | artist, icons | — |
| #927588 | mauve grid lines | 1% |
| #5a63f0 | artwork blue (content only) | — |

WCAG (contrast.py):
- Title #1c1c1c on #fff: 17.04:1; white pause glyph on #1c1c1c: 17.04:1.
- Time stamps #6e6e6e: 5.1:1 (pass).
- Artist #8a8a8a: **3.45:1** (fails AA body).
- Skeleton labels ≈#9a9a9a: 2.81:1 — acceptable as diagram annotation, not as UI.

Strategy: pastel, low-chroma colour encodes *layer type* (pink = grid/frame, lavender/blue = layout regions, grey = skeleton); full saturation is only in the album art.

## 5. Depth & material
- Every plane casts a soft, wide contact shadow (≈60 px blur, ≈6% black) offset downward — paper floating above white.
- The cursor is a translucent glass sphere (≈120 px) that magnifies/refracts the grid beneath it.
- Grid layer is semi-transparent so lower planes show through — implies stacking order in depth without darkening.

## 6. Components & patterns
- **Music player card**: 290 px artwork with ≈24 px radius, prev / play-pause (≈110 px black circle) / next, progress bar with elapsed and remaining.
- **Exploded anatomy**: same-footprint planes for grid, layout, skeleton, content.
- **Reorder by drag**: between 3.0 s and 6.7 s the cursor drags planes so the content card moves from top to middle to bottom and the grid rises to the top.
- **Collapse**: at ≈9 s all planes snap back to a single flat card.

## 7. Motion
Measured (m0_motion.json): 10.9 s at 60 fps, motion_fraction 0.28, seamless_loop_likely true, 6 segments, median 0.53 s.
- 1.63–2.23 s (0.60 s, peak 0.36, ease-in-out): tilt into 3D and first separation.
- 3.40–3.83 s, 4.73–5.23 s, 5.57–6.13 s (0.43 / 0.50 / 0.57 s, peaks 0.04–0.09): layer swaps — sharply front-loaded ease-out, like a spring release after drag.
- 6.43–7.03 s (0.60 s, peak 0.47, symmetric) and 7.83–8.17 s (0.33 s, ease-out): restack and collapse to flat.
The 3D transitions are slower (≈0.6 s, symmetric) than the reorder snaps (≈0.45–0.55 s, ease-out) — big spatial moves get gentler curves.

## 8. Brand system
n/a — not a brand system. Identity cues: pastel layer-coding and the glass-ball cursor form a recognisable explainer style.

## 9. UX
- As an explainer it is very effective: each layer's role is legible from its colour and contents alone.
- Live progress during the explosion reinforces that the layers are the same component.
- As UI, the card's grey secondary text misses AA; the explode interaction would need labels for non-designers.

## 10. Craft signals
- All four planes share an identical footprint and corner radius (≈64 px), so the stack reads as a column.
- Skeleton labels sit exactly where the real text sits on the content layer.
- Progress timer advances 3:48 → 3:57 across the clip (≈9 s real time).
- Each layer type has its own pastel; no layer uses two hues.
- Glass-sphere cursor refracts the grid it passes over.

## 11. Reproduction recipe
```css
:root{--ink:#1c1c1c;--muted:#6e6e6e;--grid:#fbeef8;--grid-line:#e7c9de;--lav:#e5ddee;--blue:#e6edfb;--r:64px}
.stack{perspective:2400px}
.stack .plane{position:absolute;inset:0;border-radius:var(--r);transform-style:preserve-3d;
  transition:transform .55s cubic-bezier(.16,1,.3,1);box-shadow:0 40px 60px -20px rgba(0,0,0,.08)}
.stack.exploded{transform:rotateX(55deg) rotateZ(-15deg)}
.stack.exploded .plane:nth-child(1){transform:translateZ(330px)}
.stack.exploded .plane:nth-child(2){transform:translateZ(110px)}
.stack.exploded .plane:nth-child(3){transform:translateZ(-110px)}
.stack.exploded .plane:nth-child(4){transform:translateZ(-330px)}
.plane.grid{background:#fff;background-image:linear-gradient(var(--grid-line) 1px,transparent 1px),linear-gradient(90deg,var(--grid-line) 1px,transparent 1px);background-size:24px 24px;opacity:.85}
.plane.layout .block{background:var(--lav)} .plane.layout .block.alt{background:var(--blue)}
.plane.skeleton{background:#fff;border:1px solid #e3e3e3}
.time{font-variant-numeric:tabular-nums;color:var(--muted)}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Airy white stage with pastel layer-coding; artwork is the only loud colour. |
| Originality | 8 | Exploded-view anatomy is known, but drag-reordering live layers is a fresh teaching device. |
| Usability | 6 | Great as an explainer; the card's secondary text fails AA. |
| Craft | 8 | Aligned footprints, consistent radius, live timer, refractive cursor. |

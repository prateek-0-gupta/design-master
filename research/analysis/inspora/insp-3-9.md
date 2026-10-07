---
id: insp-3-9
source: inspora
category: Motion
status: analyzed
title: "A brick button"
creator: "@Designownow_"
styles: [x-voxel-brick, soft-3d, micro-interaction]
patterns: [extruding-hover-button, split-arrow-block, pixel-chevron, blurred-color-shadow, toy-brick-nub]
mode: light
palette: ["#f2f2f2", "#6fa9e8", "#6292e4", "#4d81e4", "#f9d172", "#f5a84c", "#8a8a8a"]
type_families: ["Figtree / Gilroy-style geometric sans (likely)"]
type_class: [geometric-sans]
radius_px: [0]
motion: {durations_s: [0.3, 0.23, 0.2, 0.1], easing: [ease-out, ease-in], loop: true}
scores: {aesthetics: 7, originality: 8, usability: 5, craft: 7}
craft_signals: [side-face-darker-than-top, arrow-block-detaches-on-hover, connector-nub-like-lego, pixel-art-chevron, blurred-duplicate-as-shadow]
anti_patterns: [white-label-on-light-blue-fails-contrast, hover-target-splits-into-two-objects]
---
# A brick button — @Designownow_

## 1. Snapshot
- **Subject:** A 16.4 s, 1920×1054 recording of a "Build legacy" CTA built like a toy brick: a long blue block plus a square yellow arrow block with a connector nub. On hover it extrudes into 3D, and the two blocks pull apart.
- **Why it's remarkable:** It turns a split button (label plus arrow) into a construction metaphor that matches the "build" copy.

## 2. Composition & layout
- **Context:** The button sits in a landing-page section under a grey 3-line paragraph (about 30 px text, leading about 42 px) and a 1 px hairline divider at y≈303.
- **Rest state:** The button is about 836×148 px in total.
  - Blue label block: 687×148.
  - Yellow arrow block: 147×148, a true square.
  - Nub: about 33×79 px, protruding right and vertically centred.
- **Shadow:** A blurred, colour-matched duplicate of the button sits about 120 px below and offset about 200 px right, acting as a coloured cast shadow.

## 3. Typography
- **Label:** "Build legacy" in a geometric sans with a double-storey "a" and an open "g". It is close to Figtree or Gilroy, Medium weight, about 56 px, white.
- **Body:** The paragraph is the same family, Light, at about 30 px in #8a8a8a.

## 4. Colour
| Hex | Role |
|---|---|
| #f2f2f2 | canvas |
| #6fa9e8 → #6292e4 | blue block top face (vertical gradient light→mid) |
| #4d81e4 | blue side face (revealed on hover) |
| #f9d172 / #f8e7b1 | yellow block top face |
| #f5a84c | yellow side face |
| #8a8a8a | body copy |

WCAG:
- White label on #6fa9e8 is **2.47:1** and on #6292e4 is 3.11:1. The label only passes as large text in the darker region.
- The white pixel chevron on #f9d172 is **1.46:1** (fails badly).
- Body text #8a8a8a on #f2f2f2 is 3.08:1 (fails AA normal).

## 5. Depth & material
- **Rest:** A flat face with a subtle top-to-bottom gradient and a faint top highlight.
- **Hover:** A darker side face (about 68 px tall) appears beneath each block, giving an isometric-ish extrusion. The top face lifts by the same amount.
- **Shadow:** The cast shadow is the button itself, Gaussian-blurred (about 30 px) at reduced opacity. It is coloured blue and yellow rather than grey, which keeps the toy feel.

## 6. Components & patterns
- Split CTA: a label block plus an arrow block joined by a stud or nub.
- The chevron is drawn from 5 pixel squares (a pixel-art "›").
- In the hover state the arrow block separates by about 130 px to the right while the blue block extrudes. The nub stays attached to the blue block and becomes a small blue tab.

## 7. Motion
- **Measured:** 16 segments across 16.43 s, median 0.23 s (range 0.10–0.30 s). motion_fraction is 0.18 and `seamless_loop_likely: true`.
- **Shape:** Segments pair up as hover-in and hover-out:
  - Entry moves peak early: at 1.00 s (0.30 s, peak_at 0.06) and 6.27 s (0.30 s, peak 0.06), i.e. ease-out.
  - Exits peak late: at 2.13 s (0.17 s, peak 0.90) and 7.37 s (0.20 s, peak 0.75), i.e. ease-in.
  - Several 0.27 s symmetric segments (9.70 s, 10.73 s, 12.27 s, peak about 0.44) are the separation and rejoin of the arrow block.
- **Read:** A snappy 200–300 ms system with fast-out entry and accelerating exit, the right feel for a physical "pop".

## 8. Brand system
n/a — not a brand system. Identity cues: the toy-brick metaphor, pixel glyph, and blue/yellow primaries all echo construction toys.

## 9. UX
- Hover feedback is unmistakable and playful.
- **Risk:** On hover, the arrow block moves away from the cursor. If a user aims for the arrow, the target relocates by about 130 px, which is a classic "fleeing target" problem.
- Label and chevron contrast are weak.
- Touch devices get none of the payoff.

## 10. Craft signals
- The side faces are darker hue-shifted versions of each block (#4d81e4 under blue, #f5a84c under yellow), not black overlays.
- The arrow block is an exact square (147×148) matching the button height.
- The nub sits at the vertical centre and is 53% of the button height.
- The cast shadow is a blurred coloured duplicate rather than a grey box-shadow.
- The pixel chevron is aligned to a 5-cell grid.

## 11. Reproduction recipe
```css
.brick{display:flex;align-items:stretch;gap:0;transition:gap .25s cubic-bezier(.2,.8,.2,1)}
.brick__label,.brick__arrow{position:relative;height:148px;transition:transform .3s cubic-bezier(.2,.8,.2,1),box-shadow .3s}
.brick__label{width:687px;background:linear-gradient(#7fb6ee,#6292e4);color:#fff;font:500 56px/148px Figtree,sans-serif;padding-left:50px}
.brick__arrow{width:148px;background:linear-gradient(#fbe08e,#f9d172)}
.brick__arrow::after{content:"";position:absolute;right:-33px;top:34px;width:33px;height:79px;background:#f9d172}
.brick:hover{gap:130px}
.brick:hover .brick__label{transform:translateY(-12px);box-shadow:0 68px 0 #4d81e4}
.brick:hover .brick__arrow{transform:translateY(-12px);box-shadow:0 68px 0 #f5a84c}
.brick::before{content:"";position:absolute;inset:0;transform:translate(200px,120px);filter:blur(30px);opacity:.25;
  background:linear-gradient(90deg,#6292e4 82%,#f9d172 82%);z-index:-1}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 7 | Cheerful primaries and clean geometry, though the pastel blue is a bit washed. |
| Originality | 8 | The brick metaphor plus the separating arrow block is a fresh button idea. |
| Usability | 5 | Fails contrast, and the arrow target moves on hover. |
| Craft | 7 | Hue-shifted side faces and a coloured shadow are considered; the snap timing is good. |

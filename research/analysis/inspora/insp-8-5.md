---
id: insp-8-5
source: inspora
category: Motion
status: analyzed
title: "Liquid glass buttons"
creator: "@tranmautritam"
styles: [glassmorphism, physical-material, soft-3d, monochrome]
patterns: [liquid-glass-circle-button, refractive-caustic-drift, primitive-shape-glyphs, button-trio-specimen, dispersion-rim]
mode: light
palette: ["#d3d8db", "#c8cccf", "#b3b8bc", "#4f5252", "#a4a8ab", "#f4f4f4"]
type_families: []
type_class: []
radius_px: [9999, 8]
motion: {durations_s: [24.02], easing: [linear], loop: true}
scores: {aesthetics: 8, originality: 6, usability: 6, craft: 8}
craft_signals: [chromatic-dispersion-on-rim, inner-caustic-bands-drift, white-rim-thicker-at-bottom, glyphs-softly-rounded-primitives, contact-shadow-offset-down-right, equal-245px-pitch]
anti_patterns: [no-label-meaning-ambiguous-glyphs, white-rim-1.4-to-1-on-canvas]
---
# Liquid glass buttons — @tranmautritam

## 1. Snapshot
- **Subject:** A 24 s, 960×720 seamless loop of three circular "liquid glass" buttons in a row. Each holds a white primitive glyph (rounded square, hexagon, triangle). Refracted dark caustic bands slide slowly inside the lenses.
- **Why it's remarkable:** It is a convincing recreation of thick, refractive glass, with dispersion fringes on the rim and shifting internal reflections. It is done with almost no colour, and the "liquid" quality is carried purely by slow internal motion.

## 2. Composition & layout
- **Row:** three buttons, each about 162 px in diameter, with centres at x≈235 / 480 / 725 (an equal 245 px pitch, gaps about 83 px) and the row vertically centred at y≈360.
- **Glyphs:** about 50 px, optically centred. The triangle is nudged down about 3 px so its centroid sits at the circle centre.
- **Backdrop:** a diagonal grey gradient from top-left (#d3d8db) to bottom-right (#b3b8bc) gives the glass something to refract.
- The row occupies about 68% of the width.

## 3. Typography
None. Glyphs are geometric primitives with about 8 px corner rounding: square, hexagon (pointy-top) and triangle. They read like PlayStation-style symbolic buttons.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #d3d8db | backdrop light | 50% |
| #c8cccf | backdrop mid | 21% |
| #b3b8bc | backdrop shade (bottom-right) | 22% |
| #4f5252 | lens interior (dark refraction) | 5.6% |
| #a4a8ab | caustic mid-tones | 2% |
| #f4f4f4 (est.) | glyphs, rim highlight | <1% |
| dispersion (cyan/orange/violet fringes) | rim edges | <0.5% |

WCAG checks:
- Glyph #f4f4f4 on the lens (#4f5252) is 7.17:1.
- The lens body on the backdrop is 5.49:1, which is good for target perception.
- The white rim on the backdrop is only 1.44:1, but it is decorative because the dark lens defines the edge.

## 5. Depth & material
- **Rim:** a thick bright glass rim (6–10 px), thicker and brighter at the bottom-left and bottom where light pools. It shows thin rainbow dispersion lines (cyan, orange, violet) along its inner edge.
- **Interior:** darker than the background, as though the lens is a thick dome inverting and compressing the surroundings. Lighter curved caustic bands sweep through it.
- **Drop shadow:** soft, offset down and right by about 6 px, with about 14 px blur, consistent with top-left light.
- **Glyphs:** flat white, with a very faint shadow so they sit just above the glass surface.

## 6. Components & patterns
- **Icon-only circular button set:** a material study, not a full component. No pressed or hover state is shown in the clip (the only measured segment is 0.10 s).
- It suits media controls (stop / shape / play) or game-pad affordances.

## 7. Motion
Measured (m0_motion.json, 60 fps, 24.02 s, motion_fraction 0.01, mean energy 0.15, seamless_loop_likely true, first/last diff 0.26):
- Practically continuous sub-threshold motion. The only detected segment is 7.37–7.47 s (0.10 s, symmetric), a brief glint.
- From frames 2.67 s apart (estimates):
  - The dark caustic bands inside each lens rotate and slide slowly. Each button is out of phase with the others (at 9.34 s the left lens shows a horizontal band while the right one shows a diagonal band).
  - The dispersion highlights travel around the rim.
  - The full cycle matches the 24 s loop.
- The pace is linear and very slow (roughly 15° of band rotation per second). It reads as an environment reflection moving, not as the button animating.

## 8. Brand system
n/a — this is a material study, not a brand system. Identity cues: monochrome "liquid glass" aligned with the current OS-level glass trend.

## 9. UX
- The dark lens with a white glyph gives a clear target and a legible icon (7.2:1).
- **Risks:**
  - The abstract glyphs carry no inherent meaning without labels or tooltips.
  - The continuous internal motion is distracting if repeated across a UI, and needs a reduced-motion fallback.
  - It is not shown how pressed or disabled states would differ.

## 10. Craft signals
- Dispersion fringes appear only at the rim's inner edge, where real thick glass would split light.
- The rim is brighter and thicker along the bottom (light pooling) than the top.
- The three lenses animate with phase offsets, so they never mirror each other.
- The triangle is optically centred (shifted down) rather than box-centred.
- The pitch is exactly equal (245 px), and the shadow direction is consistent with the backdrop gradient.
- The loop is seamless over 24 s.

## 11. Reproduction recipe
```css
:root{--bg1:#d3d8db;--bg2:#b3b8bc;--lens:#4f5252;--glyph:#f4f4f4}
body{background:linear-gradient(120deg,var(--bg1),#c8cccf 55%,var(--bg2))}
.glass{--a:0deg;width:81px;aspect-ratio:1;border-radius:50%;display:grid;place-items:center;position:relative;
  background:
    conic-gradient(from var(--a),transparent 0 20%,rgba(255,255,255,.25) 25%,transparent 32% 60%,rgba(0,0,0,.35) 66%,transparent 74%),
    radial-gradient(circle at 50% 45%,#6b6f70,var(--lens) 70%);
  box-shadow:inset 0 0 0 4px rgba(255,255,255,.85),inset 0 -6px 10px rgba(255,255,255,.5),
    inset 2px 0 0 5px rgba(120,200,255,.25),inset -2px 0 0 5px rgba(255,170,90,.2),
    3px 4px 10px rgba(40,50,60,.25);
  animation:caustic 24s linear infinite}
.glass:nth-child(2){animation-delay:-8s}.glass:nth-child(3){animation-delay:-16s}
@property --a{syntax:"<angle>";inherits:false;initial-value:0deg}
@keyframes caustic{to{--a:360deg}}
.glass svg{width:25px;fill:var(--glyph);filter:drop-shadow(0 1px 1px rgba(0,0,0,.2))}
@media (prefers-reduced-motion:reduce){.glass{animation:none}}
```
For true refraction, use an SVG `feDisplacementMap` on a `backdrop-filter`, or a WebGL lens shader.

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Convincing glass, calm palette, perfect spacing. |
| Originality | 6 | Liquid-glass buttons are a widespread 2025–26 trend; execution rather than idea. |
| Usability | 6 | High-contrast targets, but meaningless glyphs and no state changes shown. |
| Craft | 8 | Dispersion placement, bottom-weighted rim, phase-offset caustics, optical centring. |

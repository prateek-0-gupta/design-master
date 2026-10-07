---
id: insp-liquid-metal
source: inspora
category: Illustration
status: analyzed
title: "Liquid metal"
creator: "@basit_designs"
styles: [y2k-chrome, physical-material, monochrome, micro-interaction]
patterns: [chrome-rim-icon-button, nested-pill-containers, extruded-label-text, spec-caption-corners, shader-animated-icon, tile-grid-backdrop]
mode: light
palette: ["#e3e3e3", "#cfcfcf", "#bebebe", "#fafafa", "#efefef", "#a4a4a4", "#3c3c3c"]
type_families: ["Inter / SF Pro Display Medium (likely)", "Geist Mono / IBM Plex Mono (captions, likely)"]
type_class: [neo-grotesk, mono]
radius_px: [400, 9999]
motion: {durations_s: [10.95], easing: [linear], loop: true}
scores: {aesthetics: 8, originality: 6, usability: 6, craft: 8}
craft_signals: [chromatic-fringe-on-rim, concentric-pill-radii, label-drop-shadow-as-extrusion, metal-only-on-interactive-parts, mono-spec-captions-four-corners, backdrop-tile-grid-hairlines]
anti_patterns: [cropped-label, white-on-white-container-1-2-to-1, decorative-motion-not-feedback]
---
# Liquid metal — @basit_designs

## 1. Snapshot
- **Subject:** A 10.95 s, 2104×1834, 60 fps close-up of a white "Upload fi…" upload control: a circular "+" button with a liquid-chrome rim and a liquid-metal plus glyph, inside nested white pills, on a pale tiled backdrop. The corner captions credit "Paper Design" and "Chroma Glass / Liquid Metallic".
- **Why it's remarkable:** All the chrome is confined to two tiny elements, a ~6 px ring and the plus glyph. The surrounding white-on-white plastic makes those reflections feel like jewellery. It shows how a shader material can upgrade a mundane CTA.

## 2. Composition & layout
- **Crop:** an extreme macro. The control is cropped at the right edge mid-word ("Upload fi"), so the frame is about the button, not the action.
- **Three nested containers:**
  1. an outer slab with a ≈400 px corner radius, running off-frame;
  2. a pill track about 790 px tall with a 1.5 px silver hairline;
  3. inside it, the ≈462 px circle button and a white label pill about 450 px tall.
- **Rhythm:** The gaps between circle and pill (~60 px) and between pill and track (~170 px) are generous and symmetrical vertically.
- **Captions:** four corner caption blocks (two lines each) at a ~330 px inset, aligned to a backdrop tile grid of ~840 px squares with 4 px grooves.

## 3. Typography
- **Label:** "Upload fi…" is a neo-grotesk Medium, close to Inter Display or SF Pro. Cap height is about 160 px in source and tracking is about −0.02 em. It is filled with a vertical grey gradient (#5a5a5a → #2a2a2a) and carries a soft drop shadow (~6 px y, 12 px blur), so it reads as raised or debossed lettering.
- **Captions:** a monospace at about 23 px source, uppercase, tracking about +0.12 em, set in pairs (label / value: "DESIGN / EXPERIMENT", "YEAR / 2025", "TOOL / PAPER DESIGN").

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #e3e3e3 | backdrop tiles, outer slab | 64% |
| #cfcfcf / #bebebe | cast shadow gradient, tile grooves | 27% |
| #fafafa / #efefef | label pill, button face highlights | 7% |
| #a4a4a4 | silver hairline rims | 2% |
| #3c3c3c | label ink, caption ink | — |
| iridescent fringe | rim and plus glyph only (cyan/orange/violet specks) | ≪1% |

WCAG checks:
- The label (#3c3c3c on #fafafa) is 10.57:1.
- The captions (#6a6a6a on #e3e3e3) are **4.21:1**, slightly under AA for ~11 px CSS text.
- The container edges rely on #cfcfcf against #e3e3e3, which is 1.21:1. Boundaries are carried only by the shadow and the silver rim (#a4a4a4 on #efefef is 2.17:1, below the 3:1 non-text minimum).

## 5. Depth & material
- **Lighting:** a single top-left key light. The outer slab casts a long soft shadow down-right (~200 px spread, ending at ~#bebebe).
- **Track and pill:** inset/outset by 1.5 px metallic rims with a bright top edge and a darker bottom edge.
- **Button rim:** a ~6 px toroidal chrome ring with environment-map reflections and a **chromatic aberration fringe** (rainbow specks at 10 and 4 o'clock).
- **Plus glyph:** a liquid-metal blob, thicker at the centre junction, with a specular streak. The ends are rounded and slightly bulbous like mercury.

## 6. Components & patterns
- Icon button plus label pill combined into one upload control.
- A spec-sheet frame (four mono caption corners) used as presentation.
- Shader-driven material (consistent with Paper's "liquid metal" shader) applied to an SVG icon and stroke.

## 7. Motion
Measured values (`m0_motion.json`):
- Motion fraction is 0.00, with mean energy 0.03 and no segments. `seamless_loop_likely` is true (first/last diff 0.47).
- Layout and camera are static. The only change is the reflection pattern inside the rim and plus glyph, which drifts slowly. Compare the glyph across 0.61 s, 4.26 s and 7.91 s: the dark and bright sections migrate around the stroke, and the rim fringe moves from the left side to the bottom.
- Estimated as a continuous linear environment rotation looping over about 10–11 s. It is ambient, not tied to hover or press.

## 8. Brand system
n/a — this is not a brand system. It is a showcase "design experiment" with tool credit; the caption frame is the author's presentation signature.

## 9. UX
- **Strengths:** A large hit area (the circle alone is ≈462 px source, ~120 pt) and a clear "+" plus "Upload" labelling.
- **Risks:**
  - The low-contrast white containers fail non-text contrast.
  - Perpetual shimmer is decoration rather than state. It should respond to hover or drag-over (e.g. faster flow while a file hovers) and stop under `prefers-reduced-motion`.
  - The text is cropped in the presentation.

## 10. Craft signals
- The chromatic fringe sits only on the rim's curvature extremes, which mimics real dispersion.
- The container radii are concentric: each inner pill's radius equals the outer radius minus the gap, so the curves stay parallel.
- The label uses a vertical gradient fill plus a drop shadow, an embossed-type effect without bevel kitsch.
- Metal appears only on interactive parts (button rim, icon, track rim). Static surfaces are matte.
- The captions sit on the backdrop tile grid's columns (x≈330 and x≈1860).

## 11. Reproduction recipe
```css
:root{--bg:#e3e3e3;--slab:#ededed;--face:#fafafa;--rim:#a4a4a4;--ink:#3c3c3c;--cap:#6a6a6a;
  --chrome:conic-gradient(from 200deg,#fff,#8a8a8a 12%,#f4f4f4 22%,#4a4a4a 35%,#e8e8e8 50%,#9ad7ff 53%,#ffc59a 55%,#7a7a7a 62%,#fff 80%,#5a5a5a 92%,#fff)}
.track{border-radius:9999px;background:var(--slab);padding:40px;display:flex;gap:16px;
  box-shadow:inset 0 0 0 1.5px var(--rim),0 40px 80px -30px rgba(0,0,0,.25)}
.plus-btn{width:120px;aspect-ratio:1;border-radius:50%;position:relative;background:radial-gradient(circle at 40% 30%,#fff,#e9e9e9)}
.plus-btn::before{content:"";position:absolute;inset:0;border-radius:50%;padding:3px;background:var(--chrome);
  -webkit-mask:linear-gradient(#000 0 0) content-box exclude,linear-gradient(#000 0 0);animation:env 11s linear infinite}
@property --a{syntax:"<angle>";inherits:false;initial-value:0deg}
@keyframes env{to{filter:hue-rotate(0deg);transform:rotate(360deg)}}
.label{font:500 40px/1 Inter,system-ui;letter-spacing:-.02em;background:linear-gradient(#5a5a5a,#2a2a2a);
  -webkit-background-clip:text;color:transparent;filter:drop-shadow(0 3px 4px rgba(0,0,0,.25))}
.cap{font:400 11px/1.35 "Geist Mono",ui-monospace;letter-spacing:.12em;text-transform:uppercase;color:var(--cap)}
@media (prefers-reduced-motion:reduce){.plus-btn::before{animation:none}}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Elegant restraint: chrome jewellery on white plastic, with the spec captions framing it. |
| Originality | 6 | Liquid-metal shader UI is a current trend; the restraint is the differentiator. |
| Usability | 6 | Big target, but container edges fail non-text contrast and the shimmer is not state-linked. |
| Craft | 8 | Concentric radii, dispersion on the rim and an embossed label are very carefully tuned. |

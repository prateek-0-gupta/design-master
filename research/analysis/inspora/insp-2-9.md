---
id: insp-2-9
source: inspora
category: Motion
status: analyzed
title: "Jelly Switch"
creator: "@iwoplaza"
styles: [claymorphism, soft-3d, physical-material, micro-interaction]
patterns: [jelly-toggle-thumb, recessed-slot-track, emissive-on-state, environment-tint-from-glow, squash-and-wobble, hue-variant-cycling]
mode: mixed
palette: ["#e5e5e5", "#c4c9c7", "#4a6b8a", "#83f1da", "#cee3dc", "#3fb8ff", "#d91cf0", "#4a4a4c"]
type_families: []
type_class: []
radius_px: [9999, 28]
motion: {durations_s: [0.27, 0.33, 0.37, 0.17, 0.2], easing: [ease-out, ease-in-out, ease-in], loop: false}
scores: {aesthetics: 8, originality: 8, usability: 6, craft: 8}
craft_signals: [subsurface-scatter-in-jelly, glow-tints-whole-backdrop, track-recessed-with-inner-shadow, top-face-wobbles-after-travel, off-state-desaturated-and-dim, on-state-emissive-bloom]
anti_patterns: [state-by-colour-and-position-only, mint-on-state-low-contrast-on-light-bg, no-label]
---
# Jelly Switch — @iwoplaza

## 1. Snapshot
- **Subject:** A 16.2 s, 1080×1080 real-time 3D (likely WebGPU/TypeGPU, given the creator) toggle. A translucent jelly cube rides in a recessed pill slot.
  - Off: it sits left as a dim, desaturated blue.
  - On: it slides right, lights up from within (blue, then mint, then magenta across cycles), and tints the whole surface around it.
  - The last third repeats the same on a dark backdrop.
- **Why it's remarkable:** The thumb is a soft-body material that squashes, wobbles and emits light. "On" is communicated by glow and environmental colour spill, not just position.

## 2. Composition & layout
- **Switch:** a single, centred-left object about 230 px wide overall (cube ≈130×120 px plus the slot extending ≈110 px) on a 1080 canvas. More than 90% of the frame is the studio surface.
- **Slot:** a capsule groove about 110×22 px, cut into the surface.
- **Cube positions:**
  - Off: the cube covers the slot's left end, with the slot visible to the right (0.90 s).
  - On: the cube covers the right end, with the slot visible to the left (6.30 s).
- **Camera:** top-down at about 30° tilt, with a soft gradient light from top-left.

## 3. Typography
None. The piece has no labels or text, which is a limitation if used as UI (see §9).

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #e5e5e5 / #c4c9c7 | light studio surface (gradient) | ~80% |
| #4a6b8a (approx) | off-state jelly (cool slate blue) | ~2% |
| #3fb8ff (approx) | on-state blue glow | variant |
| #83f1da / #cee3dc | on-state mint jelly / mint-tinted surface | 4% / 14% |
| #d91cf0 (approx) | on-state magenta | variant |
| #4a4a4c (approx) | dark surface (11.7 s onward) | late |

Contrast, as non-text UI graphics against a 3:1 target:
- Off cube on light surface: 4.43:1 (pass).
- Mint on-cube on #e5e5e5: **1.07:1**, and on the tinted #c4c9c7 it is 1.24:1. The on state is visible only through glow and saturation, not luminance.
- Magenta on the dark surface: 2.51:1.
- Off purple on dark: 1.16:1.

Luminance contrast is weak; the state relies on emission and hue.

## 5. Depth & material
- **Jelly:** translucent with subsurface scattering. There is a lighter "skin" with a darker inner core, a wobbling top face (two soft bumps on the top edge, visible in every frame), and about a 28 px rounded-box radius.
- **Emission:** the on state emits light, with a bloom of about 80 px around the cube. The surrounding surface takes on the hue (mint wash in the key frame, violet wash at 13.5 s), which is ambient colour bleed.
- **Track:** a recessed groove with an inner shadow along its top edge and a light lip at the bottom.
- **Shadows:** a soft contact shadow under the cube. The off state shows a slightly darker, cooler shadow.

## 6. Components & patterns
- **Toggle:** a jelly thumb in a slot track.
- **States:** off (dim, desaturated, left) and on (emissive, saturated, right). Each on-cycle uses a new hue (blue → mint → magenta), as a variant showcase.
- **Themes:** the light environment (0–10 s) and the dark environment (11.7–16 s) are shown with the same component.

## 7. Motion
Measured: 16.2 s at 30 fps, 14 segments, motion fraction 0.19, median 0.20 s, not a loop.
- **Toggle travel:**
  - 0.83–1.10 s (0.27 s, symmetric) is a toggle.
  - 1.97–2.30 s (0.33 s, peak 0.15 → ease-out) is the return.
  - 3.87–4.23 s (0.37 s, ease-out) is another.
  - Toggles take about 0.27–0.37 s, ease-out dominant, so the cube leaves quickly and settles.
- **Wobble after-shocks:** pairs like 12.00–12.17 s (ease-in) followed by 12.53–12.70 s (ease-out) and 12.83–13.03 s are 0.17–0.20 s secondary motions. This is the jelly overshoot and wobble after travel, a spring with low damping.
- **Glow:** the glow ramps with the travel. Hue and environment tint change over the same window (estimated ≤0.3 s).

## 8. Brand system
n/a — not a brand system. Identity cues: a soft-body "candy" material language and neon-on-neutral emission; the creator's GPU-shader showcase aesthetic.

## 9. UX
- **Strengths:** The state change is delightful and very visible in the moment (glow plus colour spill). Its physicality makes the affordance obvious.
- **Risks:**
  - No label.
  - The state is encoded only by position and hue/glow, so on the light theme the mint on state has almost no luminance contrast with the surface.
  - It needs `role="switch"`, `aria-checked`, a text label, and reduced-motion handling for the wobble.

## 10. Craft signals
- The jelly top face deforms (two-bump wobble) after each travel, which is secondary motion.
- The emissive glow tints the entire backdrop in the state hue (mint at 8.1 s, violet at 13.5 s).
- The off state is desaturated and dimmer, not just a different hue.
- The slot is a true recessed groove with an inner shadow on the far edge.
- The same component reads in both light and dark environments.
- The contact shadow stays under the cube throughout travel.

## 11. Reproduction recipe
```css
:root{--surface:#e5e5e5;--off:#4a6b8a;--on:#83f1da;}
.switch{position:relative;width:240px;height:130px}
.switch .slot{position:absolute;left:55px;top:55px;width:130px;height:22px;border-radius:9999px;background:var(--surface);
  box-shadow:inset 0 3px 4px rgba(0,0,0,.25),inset 0 -1px 0 rgba(255,255,255,.8)}
.switch .jelly{position:absolute;left:0;top:0;width:130px;height:120px;border-radius:28px;
  background:radial-gradient(70% 60% at 50% 60%,color-mix(in oklab,var(--c),#fff 15%),var(--c));
  box-shadow:inset 0 6px 10px rgba(255,255,255,.5),inset 0 -10px 16px rgba(0,0,0,.18),0 10px 18px rgba(0,0,0,.18);
  --c:var(--off);filter:saturate(.6) brightness(.85);
  transition:transform .3s cubic-bezier(.16,1,.3,1),filter .3s,background .3s}
.switch[aria-checked=true] .jelly{--c:var(--on);transform:translateX(110px);filter:none;
  box-shadow:inset 0 6px 10px rgba(255,255,255,.6),0 0 80px 10px color-mix(in srgb,var(--on) 60%,transparent);
  animation:wobble .5s .3s}
@keyframes wobble{25%{transform:translateX(110px) scale(1.05,.95)}55%{transform:translateX(110px) scale(.97,1.03)}80%{transform:translateX(110px) scale(1.01,.99)}}
.stage:has([aria-checked=true]){background:radial-gradient(40% 40% at 55% 50%,color-mix(in srgb,var(--on) 25%,var(--surface)),var(--surface))}
@media (prefers-reduced-motion:reduce){.switch .jelly{animation:none;transition-duration:.01s}}
```
For real subsurface and deformation, use a WebGPU/Three.js SDF rounded box with a vertex wobble driven by a damped spring (k≈300, c≈10).

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Lovely candy material and glow, with good restraint on a neutral studio surface. |
| Originality | 8 | An emissive soft-body thumb with environment colour spill is a fresh toggle idea. |
| Usability | 6 | The physical affordance and state flash are clear, but there is no label and low luminance contrast in the light theme. |
| Craft | 8 | Secondary wobble, recessed slot and ambient tint are all physically coherent. |

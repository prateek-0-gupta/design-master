---
id: insp-handmade-icons
source: inspora
category: Branding
status: analyzed
title: "Handmade icons"
creator: "Alex Socoloff"
styles: [soft-3d, physical-material, grain-noise, hairline-ui]
patterns: [app-icon-series-carousel, keycap-in-squircle, pixel-heatmap-tile, hardware-mixer-icon, radar-sweep-icon, crop-mark-artboard-frame, sticker-peel-transition]
mode: light
palette: ["#fdfdfd", "#eaecef", "#d5ecfe", "#b8cbfc", "#9cb1fb", "#f0623a", "#b5b5b5", "#3a3a3a"]
type_families: ["SF Pro Display / Inter-style neo-grotesk (likely, keycap 'A')"]
type_class: [neo-grotesk]
radius_px: [70, 48]
motion: {durations_s: [0.37, 0.33, 0.43, 1.0], easing: [ease-out], loop: false}
scores: {aesthetics: 8, originality: 7, usability: 6, craft: 8}
craft_signals: [fine-grain-noise-on-surfaces, coloured-cast-shadow-under-keycap, crop-marks-and-hairline-artboard, glyph-inner-glow, knob-slot-orientations-vary, single-red-led-accent, consistent-squircle-size-across-set]
anti_patterns: [white-glyph-on-pale-blue-low-contrast, icons-dissolve-into-white-canvas]
---
# Handmade icons — Alex Socoloff

## 1. Snapshot
- **Subject:** A 4.5 s, 1080×1080 reel cycling through four tactile 3D app icons on a white artboard with print crop marks:
  - a warm orange pixel-grid "heat" tile;
  - a frosted blue keycap "A";
  - a grey audio mixer with three knobs and an LED column;
  - a grey radar with a cyan sweep.
- **Why it's remarkable:** Each icon is a miniature physical object (keycap, mixer, radar screen) with grain, cast colour and real light. The series stays coherent through one squircle size, one light direction and one grain texture.

## 2. Composition & layout
- **Artboard:** hairline guides (#eaecef, 1–2 px) inset about 78 px on all sides, with "+" crop marks at the top-left and bottom-right corners. It reads as a designer's working file.
- **Icon:** centred, about 400×400 px (37% of the frame) with a corner radius of about 70 px (17.5%, close to the iOS continuous corner).
- **Keycap:** an inner plate of about 300 px with a radius of about 48 px, offset about 12 px upward from the base, so there is a visible "skirt" along the bottom.
- **Mixer:** three knobs (about 75 px) on a diagonal from top-left to bottom-left. A vertical column of five 22 px holes sits on the right, the top one a red LED.

## 3. Typography
Only the "A" keycap carries type: a neo-grotesk capital (SF Pro / Inter-like) at about 150 px cap height, medium weight, white with a soft white outer glow of about 6 px. There are no other labels.

## 4. Colour
| Hex | Role | Share (key frame) |
|---|---|---|
| #fdfdfd | artboard | 86% |
| #eaecef | hairline guides / crop marks | 1% |
| #d5ecfe / #e8fefe | keycap base (top, icy cyan) | 7% |
| #b8cbfc / #9cb1fb | keycap face → base shadow (periwinkle) | 5% |
| #f0623a (est.) | heat tile core / mixer orange knob / LED | — |
| #b5b5b5 / #3a3a3a (est.) | mixer and radar aluminium / holes | — |

WCAG / non-text checks:
- The white "A" on the keycap face is **1.62–2.08:1**, so it relies on glow and size.
- The icon edge against the canvas (#b8cbfc on #fdfdfd) is 1.59:1. These pastel icons dissolve on white wallpapers.
- The mixer's holes (#3a3a3a) on aluminium are 5.55:1, the strongest contrast in the set.

Strategy: each icon has one base hue (warm orange, cool periwinkle, neutral grey). Orange recurs as the accent across three of the four (heat core, knob, LED), which ties the series together.

## 5. Depth & material
- **Grain:** fine monochrome noise of about 1 px over every surface (visible on the keycap and the aluminium). This gives the "handmade" or printed feel.
- **Keycap:**
  - a frosted translucent plate with a 1 px light rim;
  - the base glows icy cyan at the top and saturated periwinkle (#7f8cff-ish) underneath;
  - the shadow below is coloured, not grey.
- **Pixel tile:** rounded voxel squares in a 5×5 grid. Some cells are raised (heat cells cast shadows), with a radial orange→yellow hotspot and white frosted edge cells.
- **Mixer:** bead-blasted aluminium. The knobs are convex discs with grip slots at varying angles (0°, 45°, 0°).
- **Radar:** concentric hairline rings in cyan, with a translucent glass sweep wedge and blip dots.

## 6. Components & patterns
- The icons share one silhouette (an about 400 px squircle) and a light source at about 11 o'clock.
- **Metaphors:** pixels/heat-map (analytics or design), keycap (typing or fonts), mixer (audio), radar (discovery).
- **Transition state at 1.26 s:** the keycap appears as a sticker with a peeling top-right corner, a playful mid-morph frame.

## 7. Motion
These figures are measured: 4.53 s, motion_fraction 0.45, 4 segments, all ease-out (peak_at 0.02–0.05).

| Segment | Time | Duration | What happens |
|---|---|---|---|
| 1 | 0.00–0.37 s | 0.37 s | pixel cells pop up and down |
| 2 | 1.13–1.47 s | 0.33 s | heat tile → keycap (with the sticker peel) |
| 3 | 2.30–2.73 s | 0.43 s | keycap → mixer |
| 4 | 3.50–4.50 s | 1.00 s | mixer → radar, then the sweep rotates |

The cadence is about 1.15 s per icon (holds of about 0.75 s plus about 0.4 s transitions). All moves are fast-start decelerations, which reads as snappy and tactile. It is not a seamless loop (first-to-last difference 5.95).

## 8. Brand system
n/a — not a brand system. Identity cues: a recurring orange accent, universal fine grain, and one squircle spec for the series.

## 9. UX
- The metaphors are clear and distinct at 400 px.
- At 60 px, the white "A" (about 1.6:1) and the pastel edges (1.59:1 to the canvas) risk washing out. A darker rim or drop shadow would be needed on light home screens.
- The mixer and radar have the best small-size read thanks to their dark holes and rings.

## 10. Craft signals
- The same about 70 px corner radius and about 400 px size are kept across all four icons.
- The cast shadow under the keycap is tinted periwinkle, matching the object colour.
- The knob slots are rotated differently (vertical, 45°, horizontal) to suggest real settings.
- A single red LED sits at the top of a column of four dark holes (state indication).
- 1 px grain noise is applied uniformly, so all four look like the same material family.
- Crop marks and a #eaecef guide frame present the work as a production artboard.

## 11. Reproduction recipe
```css
:root{--board:#fdfdfd;--guide:#eaecef;--ice:#d5ecfe;--peri:#b8cbfc;--peri-2:#9cb1fb;--ember:#f0623a;--alu:#b5b5b5;--hole:#3a3a3a;
  --r-icon:70px;--r-cap:48px}
.artboard{background:var(--board);outline:1px solid var(--guide);outline-offset:-78px}
.icon{width:400px;aspect-ratio:1;border-radius:var(--r-icon);position:relative;
  background:linear-gradient(180deg,var(--ice),var(--peri) 70%,#8f9dff);
  box-shadow:0 24px 40px -12px rgba(110,125,255,.45),inset 0 1px 0 #fff}
.icon::after{content:"";position:absolute;inset:0;border-radius:inherit;opacity:.18;mix-blend-mode:multiply;
  background:url("data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' width='120' height='120'><filter id='n'><feTurbulence baseFrequency='.9'/></filter><rect width='100%' height='100%' filter='url(%23n)'/></svg>")}
.cap{position:absolute;inset:48px 48px 60px;border-radius:var(--r-cap);background:linear-gradient(160deg,#cfe2ff,#a9b9fb);
  box-shadow:inset 0 0 0 1.5px rgba(255,255,255,.7),0 12px 0 #7f8cff;display:grid;place-items:center;
  font:500 150px/1 "SF Pro Display","Inter",sans-serif;color:#fff;text-shadow:0 0 6px #fff}
.swap{animation:pop .4s cubic-bezier(.05,.7,.1,1)}
@keyframes pop{from{transform:scale(.92);opacity:0}}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Soft, grainy, tactile set with a coherent light and an orange accent thread. |
| Originality | 7 | The hardware-metaphor icons (mixer, radar) are fresh; keycap icons are common. |
| Usability | 6 | Strong metaphors, but the pastel edges and white glyph have low contrast for small sizes. |
| Craft | 8 | Consistent radii, tinted shadows, varied knob slots and a production-artboard framing. |

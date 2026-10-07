---
id: insp-1-14
source: inspora
category: Motion
status: analyzed
title: "Shader Stamps"
creator: "@raul_dronca"
styles: [grain-noise, physical-material, gradient-mesh, editorial-serif]
patterns: [postage-stamp-cards, focus-zoom-with-depth-blur, perforated-edge-mask, collection-carousel, mono-metadata-labels]
mode: light
palette: ["#d3ccbc", "#e1decb", "#688449", "#a1684b", "#5f7078", "#39372a", "#707d52", "#7a765e"]
type_families: ["JetBrains Mono / Space Mono-style monospace (likely)"]
type_class: [mono]
radius_px: [12]
motion: {durations_s: [0.33, 0.27, 0.3], easing: [ease-out, ease-in-out], loop: false}
scores: {aesthetics: 9, originality: 8, usability: 7, craft: 9}
craft_signals: [perforation-scallops-consistent, slight-random-rotation, grain-on-shader-gradients, background-blur-on-neighbours, mono-caps-tracked-labels, paper-tone-border]
anti_patterns: [tiny-label-low-contrast]
---
# Shader Stamps — @raul_dronca

## 1. Snapshot
- **Subject:** A 3840×2156, 24.6 s, 60 fps screen recording of four "postage stamps", each holding an animated grainy shader gradient. They are named MEADOW POST (green), COPPER PRESS (copper), HARBOR MAIL (blue) and NIGHT COURIER (charcoal), dated 01/2025–04/2025.
- **Why it's remarkable:** Generative shader art is framed as collectible physical stamps. Clicking one zooms it to centre while its neighbours blur into depth of field.

## 2. Composition & layout
- **Overview state (key frame):**
  - Four stamps in a row centred on the canvas, spanning x≈800→3030 of 3840 (58% of the width).
  - Each stamp is about 490×610 px with a 1:1.25 portrait ratio, separated by about 90 px gaps.
  - Each is rotated slightly (about −1° to +3°) and vertically offset by up to about 80 px, which gives a casually laid-out feel.
- **Stamp anatomy:**
  - an off-white paper border of about 40 px with scalloped perforations (about 16 scallops per long side, each about 32 px);
  - an inner art window with about 12 px radius;
  - a two-line label top-left ("MEADOW / POST");
  - a date bottom-right ("01/2025").
- **Focus state:** the selected stamp scales to about 2.2× (about 350×450 at the 1952 sheet scale, around 1100 px tall at full res) and centres. Its neighbours shift to the sides, shrink and blur at about 12 px.

## 3. Typography
- One monospace typeface in uppercase for labels (JetBrains Mono or Space Mono-like): about 17 px at overview and about 30 px when focused. Tracking is about +0.1 em, with two stacked words.
- **Date:** the same mono with slashed zero (01/2025).
- **Colour:** the label takes a darker tint of the stamp's own hue (#707d52 on green) rather than black. On NIGHT COURIER it inverts to a light grey (#b5b3a4).

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #d3ccbc | canvas (warm putty) | 89.5% |
| #e1decb | stamp paper border | about 4% |
| #688449 | Meadow green | — |
| #a1684b | Copper | — |
| #5f7078 | Harbor blue-grey | — |
| #39372a | Night charcoal-olive | — |
| #707d52 / #7a765e | tinted labels | — |

WCAG checks:
- Meadow label #707d52 on its light area (#e1decb): 3.27:1, which passes large text only. The labels are tiny, so this is a real weakness.
- Night label #b5b3a4 on #39372a: 5.67:1.

Every hue is desaturated toward the putty background, so the set reads as one print run.

## 5. Depth & material
- **Paper:** the stamp border has a slight paper texture and a soft drop shadow (about 0 8px 24px rgba(60,50,30,.15)).
- **Art:** each art window is a smooth gradient blob (a swirl or fold) overlaid with heavy film grain, about 2 px noise at roughly 15% opacity.
- **Focus:** non-focused stamps get Gaussian blur and lower contrast. This is depth of field as a focus indicator.

## 6. Components & patterns
- A collection or gallery of cards styled as stamps.
- Click to focus, with zoom and background blur.
- Metadata in mono caps (series name and date) as a "philatelic" label system.

## 7. Motion
- **Measured:** 24.55 s, `motion_fraction` 0.10 (mostly holds), 8 segments of 0.27–0.33 s (median 0.32 s). They alternate between:
  - ease-out (`peak_at` 0.19–0.25: 6.87 s, 11.77 s, 17.70 s, 23.53 s);
  - symmetric (`peak_at` 0.45–0.50: 2.33 s, 8.17 s, 13.67 s, 19.10 s).
- **Reading:** The pairs are open/close or switch. Zooming into focus is fast-start and decelerating (ease-out, about 0.3 s). Moving between stamps or returning is symmetric (about 0.3 s).
- The shader gradients inside barely move in the 9 frames (slow drift), so the energy comes from layout transitions.

## 8. Brand system
n/a — not a brand system. Identity cues: a series naming system ("Post", "Press", "Mail", "Courier") with monthly dating, which works as a collectible-drop format.

## 9. UX
- Focus and zoom are clear, and the blurred neighbours signal "more items, left and right".
- No visible close or navigation affordance appears in the frames; the cursor clicks empty space to return.
- The labels are very small at overview (about 17 px on a 4K canvas, under 9 px at 1080p).

## 10. Craft signals
- Perforation scallops are evenly spaced, and corners land on a full scallop.
- Each stamp has a unique small rotation and y-offset, avoiding a rigid row.
- Grain sits on top of the gradients (and on the paper), unifying the digital art with print.
- Label colour is derived from each stamp's hue, not a global black.
- Blur, not opacity, is used for the unfocused state.

## 11. Reproduction recipe
```css
:root{--canvas:#d3ccbc;--paper:#ece8d8;--r-art:12px;--perf:16px}
.stamp{width:245px;aspect-ratio:4/5;padding:20px;background:var(--paper);
  -webkit-mask:radial-gradient(circle var(--perf) at var(--perf) var(--perf),#0000 98%,#000) calc(-1*var(--perf)) calc(-1*var(--perf))/calc(2*var(--perf)) calc(2*var(--perf));
  filter:drop-shadow(0 6px 14px rgba(60,50,30,.15));transform:rotate(var(--tilt,-1deg));
  transition:transform .32s cubic-bezier(.16,1,.3,1),filter .32s}
.stamp .art{border-radius:var(--r-art);height:100%;position:relative;overflow:hidden}
.stamp .art::after{content:"";position:absolute;inset:0;background:url(noise.png);opacity:.18;mix-blend-mode:overlay}
.stamp .lbl{font:500 9px/1.4 "JetBrains Mono",monospace;letter-spacing:.1em;text-transform:uppercase;color:color-mix(in oklab,var(--hue) 60%,#000)}
.gallery.has-focus .stamp:not(.focus){filter:blur(12px);transform:scale(.8)}
.stamp.focus{transform:scale(2.2) rotate(0)}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 9 | A muted, cohesive print palette; tactile paper and grain. |
| Originality | 8 | Shader gradients as stamps is a clever framing device. |
| Usability | 7 | Clear focus model, but tiny low-contrast labels and no explicit navigation. |
| Craft | 9 | Clean perforations, hue-derived labels, and crisp 0.3 s transitions. |

---
id: insp-1-29
source: inspora
category: Motion
status: analyzed
title: "Speed Slider"
creator: "@raul_dronca"
styles: [micro-interaction, minimal-swiss, soft-3d]
patterns: [range-slider, value-tooltip-bubble, endpoint-icon-buttons, threshold-state-swap, gradient-progress-fill, animated-pictogram]
mode: light
palette: ["#ffffff", "#2a54d6", "#4469d1", "#e4edfe", "#e8e7e9", "#bbc4da", "#111111"]
type_families: ["SF Pro Rounded / SF Pro Display (likely)"]
type_class: [neo-grotesk]
radius_px: [9999]
motion: {durations_s: [20.23], easing: [ease-out], loop: true}
scores: {aesthetics: 7, originality: 7, usability: 8, craft: 8}
craft_signals: [endpoint-active-swaps-at-midpoint, fill-gradient-darkens-toward-origin, inset-thumb-dish, tooltip-tracks-thumb-center, pictogram-gait-changes-with-value, single-accent-hue]
anti_patterns: [inactive-icon-low-contrast, no-unit-on-value]
---
# Speed Slider — @raul_dronca

## 1. Snapshot
- **Subject:** A 3024×2160 (1512×1080 @2x), 20.2 s, 60 fps screen capture of a horizontal "speed" range slider. A walking pictogram button sits at the left end and a running pictogram at the right. A floating numeric bubble rides above the thumb.
- **Why it's remarkable:** The end icons do semantic work. Whichever end the value is closer to becomes the "active" endpoint: a pale-blue disc with a blue icon. The pictogram's gait pose also shifts as you drag, so the slider says *walk ↔ run* without any text.

## 2. Composition & layout
- **Placement:** A single centred row on pure white. In the key frame (scale 1.51) the row spans x≈280→2745 real px, about 82% of the width, and sits at y≈1075 (exactly 50% vertical).
- **End buttons:** circles of ≈264 px real (≈132 CSS px @2x).
- **Track:** ≈1715 px long and ≈33 px tall (≈16 CSS px), with fully rounded caps.
- **Gaps:** ≈110 px between button and track on both sides, so the row is symmetric.
- **Thumb:** ≈151 px circle (≈75 CSS px).
- **Value bubble:** ≈242×174 px, floating ≈60 px above the thumb's top edge. It is horizontally centred on the thumb in every frame (values 16, 43, 92, 46, 25, 60, 49).
- **Pointer:** A small ghost circle (≈50 px) below the track is the recorded touch/pointer indicator, not UI.

## 3. Typography
- **Value:** the only text, a bold rounded-grotesk numeral ≈75 px real (≈36 CSS px), close to SF Pro Display Semibold/Bold.
- **Figures:** tabular-looking digits. The bubble width stays constant between "16" and "92", so the bubble is a fixed-width pill rather than hugging the text.
- There is no unit or label. Meaning comes entirely from the icons.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #ffffff | canvas, bubble, thumb rim | 97.6% |
| #2a54d6 → #4469d1 | track fill (gradient, darker at origin) and active icon stroke | 0.4% |
| #e4edfe | active endpoint disc | 0.9% |
| #e8e7e9 | unfilled track, thumb dish | 0.9% |
| #bbc4da | soft shadow tint under thumb/bubble | 0.2% |
| #111111 | value numeral | <0.1% |

WCAG checks:
- Numeral #111 on white: **18.88:1**.
- Active icon #4469d1 on #e4edfe: **4.26:1** (passes 3:1 for graphical objects).
- Inactive grey icon ≈#8e8e93 on white: **3.26:1**, borderline for a non-text glyph.
- Fill #2a54d6 against the empty track #e8e7e9: 5.1:1, so the progress edge is unambiguous.

## 5. Depth & material
- **Thumb:** a white ring around a concave light-grey dish (#e8e7e9 centre). It reads as a pressed button cap, with a ≈20 px soft drop shadow tinted cool grey.
- **Bubble:** the same diffuse shadow, which gives it a hovering-card feel.
- **End buttons:** the inactive button is white with a 2 px #ebebeb ring; the active one loses the ring and gains the tint fill.
- **Track:** completely flat. Depth lives only on the elements you can touch.

## 6. Components & patterns
- **Range slider:** a continuous slider with a value tooltip that is always visible while interacting. It disappears at rest (t=1.12 s and 16.86 s show no bubble).
- **Endpoint buttons:** they double as "jump to min/max" affordances and as state indicators.
- **Threshold swap:** the value 49 lights the walker and 60 lights the runner, so the switch sits at about 50.
- **Fill:** a linear gradient, with the darker #2a54d6 at the left origin and lighter at the thumb, giving a "speed builds up" direction cue.

## 7. Motion
- **Measured:** 20.23 s at 60 fps. motion_fraction **0.0** and mean energy 0.07, so every change is small in pixel area (a thumb and a bubble on a vast white field). No segment crosses the 0.35 threshold. seamless_loop_likely **true** (first/last diff 0.06).
- **From frames (estimates):**
  - The thumb follows the finger directly with no lag.
  - The bubble appears with a scale-up from the thumb when a drag starts and fades when it ends: present at 3.37–14.61 s, absent at 1.12 and 16.86 s.
  - The endpoint tint cross-fades in about 0.2 s when the value crosses ~50.
  - The pictogram's limb pose differs between frames at 3.37/5.62/19.11 s, which implies a frame-by-frame gait animation driven by the value.

## 8. Brand system
n/a — not a brand system. The identity cues are a single cobalt accent and iOS-style rounded geometry.

## 9. UX
- **Clarity:** The endpoints make the scale's meaning self-evident. The bubble keeps the numeric value readable above the finger, so it is never occluded.
- **Target size:** a 75 CSS px thumb and 132 CSS px end buttons, both well above 44 px.
- **Risks:**
  - The numbers have no unit (km/h? %?).
  - The inactive icon is faint.
  - The midpoint state swap may be read as a mode toggle rather than as proximity.

## 10. Craft signals
- The active endpoint swaps exactly at the midpoint: 49 lights the walker, 60 the runner.
- The track gradient darkens toward the origin (#2a54d6) rather than toward the thumb.
- The thumb has a concave grey dish inside a white ring, not a flat disc.
- The bubble's centre x equals the thumb's centre x in all 7 bubble frames.
- The active button drops its 2 px ring and gains the #e4edfe fill. There is one state change per element, no double signalling.
- The whole composition uses one hue (cobalt) and greys.

## 11. Reproduction recipe
```css
:root{--accent:#2a54d6;--accent-2:#4469d1;--accent-tint:#e4edfe;--track:#e8e7e9;--ink:#111;}
.speed{display:flex;align-items:center;gap:56px}
.end{width:132px;aspect-ratio:1;border-radius:50%;background:#fff;box-shadow:inset 0 0 0 2px #ebebeb;color:#8e8e93;transition:background .2s,box-shadow .2s,color .2s}
.end[data-active]{background:var(--accent-tint);box-shadow:none;color:var(--accent-2)}
input[type=range]{flex:1;height:16px;border-radius:9999px;appearance:none;
  background:linear-gradient(90deg,var(--accent),var(--accent-2)) 0/var(--p) 100% no-repeat,var(--track)}
input[type=range]::-webkit-slider-thumb{appearance:none;width:75px;height:75px;border-radius:50%;
  background:radial-gradient(circle,#e8e7e9 55%,#fff 58%);box-shadow:0 6px 20px rgba(60,70,100,.18)}
.bubble{position:absolute;translate:-50% 0;bottom:calc(100% + 30px);width:120px;height:86px;border-radius:9999px;
  background:#fff;box-shadow:0 6px 20px rgba(60,70,100,.15);font:700 36px/86px "SF Pro Display",system-ui;text-align:center;
  font-variant-numeric:tabular-nums;scale:.6;opacity:0;transition:scale .25s cubic-bezier(.2,.9,.3,1.2),opacity .15s}
.dragging .bubble{scale:1;opacity:1}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 7 | Calm, single-accent, iOS-grade polish, though visually conventional. |
| Originality | 7 | Endpoint icons that change state and gait turn a standard slider into a semantic one. |
| Usability | 8 | Large targets, unoccluded value, self-explaining ends. It lacks a unit. |
| Craft | 8 | Consistent radius, centred bubble, considered thumb material. |

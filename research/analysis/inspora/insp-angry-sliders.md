---
id: insp-angry-sliders
source: inspora
category: Motion
status: analyzed
title: "angry sliders"
creator: "@ggsimm"
styles: [dark-premium, micro-interaction, hairline-ui, minimal-swiss]
patterns: [slingshot-slider, trajectory-preview-arc, rubber-band-tether, landing-marker-with-value, labelled-slider-stack, mono-value-readout]
mode: dark
palette: ["#1a191e", "#353439", "#e9e8ed", "#9a99a0", "#6052ed", "#6b6a6f"]
type_families: ["Inter (likely) for labels", "JetBrains Mono / SF Mono (likely) for values"]
type_class: [neo-grotesk, mono]
radius_px: [9999]
motion: {durations_s: [], easing: [spring], loop: true}
scores: {aesthetics: 8, originality: 9, usability: 5, craft: 8}
craft_signals: [dotted-ballistic-preview, twin-tether-lines, predicted-value-tick-on-track, accent-only-during-interaction, value-label-tinted-while-dragging, mono-for-values-sans-for-labels]
anti_patterns: [accent-text-below-aa, imprecise-input-by-design]
---
# angry sliders — @ggsimm

## 1. Snapshot
- **Subject:** A 17.5 s, 1466×1588 (120 fps) demo of four render-settings sliders (Exposure, Bloom, Field of view, Samples). You set a value by pulling the knob *off* the track like an Angry Birds slingshot and releasing it. It then flies along a previewed arc and lands at the new value.
- **Why it's remarkable:** It reinvents a slider as a projectile mechanic with honest feedback. A dotted ballistic arc and a violet landing tick with a value label show the outcome *before* release.

## 2. Composition & layout
- A single centred column about 785 px wide (track x 345→1117) on an empty #1a191e canvas. About 30% of the canvas is empty above and below, and that space is used as the slingshot pull zone.
- Four rows at a 156 px pitch. Each has a label (top-left) and value (top-right) on one line, with the track about 55 px below.
- **Track:** 3 px tall, unfilled #353439 and filled #e9e8ed. Knob about 24 px white.

## 3. Typography
- **Labels:** "Exposure", "Bloom" and so on are in a neo-grotesk (Inter-like) at about 24 px Regular in #9a99a0.
- **Values:** "+0.4 EV", "68%", "103°" and "64" are in a monospace at about 22 px in #e6e6ea, right-aligned to the track end.
- Mono for numbers and sans for names is a precise two-voice split.
- **During drag:** the active slider's value turns violet, and a second, smaller mono label (about 20 px, violet) floats above the landing tick showing the predicted value ("-2.8 EV", "217", "17%").

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #1a191e | canvas (slightly violet-black) | 98% |
| #353439 | empty track, aim dots | <1% |
| #e9e8ed | filled track, knob, values | <1% |
| #9a99a0 | labels | <1% |
| #6052ed | active knob, tethers, landing tick, active value | <1% |

WCAG:
- Values #e6e6ea on the canvas are 14.04:1, and labels #9a99a0 are 6.19:1.
- Violet value text #6052ed is **3.27:1 (fails AA for normal text)**. It is shown only while dragging, but the predicted value is the most important number at that moment.
- Aim dots #6b6a6f are 3.26:1, which is decorative.

## 5. Depth & material
Completely flat vector work, with hairline weights: track 3 px, tethers 2 px, aim dots about 5 px. There are no shadows or glows. The only depth cue is the pulled knob leaving the track plane.

## 6. Components & patterns
- **Slingshot slider:**
  - Grab the knob (cursor becomes a grab hand) and drag it away from the track.
  - Two violet tether lines stretch from two anchor points on the track to the knob (a rubber band).
  - A dotted parabolic arc shows the flight path, and a violet tick with a value label marks the landing spot.
  - Pull direction and length set the distance: pull down-right to fly left (8.76 s, Exposure flung to -2.8 EV).
- **Landing:** the knob lands with an outlined ring state (white fill, violet 2 px outline, f3 and f8) before settling.
- **Misfire (14.6 s):** the knob is mid-air below Field of view while Samples' track has emptied. The value is in flux, which shows the state between launch and landing.

## 7. Motion
The motion is measured: 17.51 s at 120 fps, but the profiler reports **motion_fraction 0.0 and no segments** (mean energy 0.04). The moving parts are a 24 px knob and 2 px lines on a 1466×1588 canvas, so frame-difference energy stays under the 0.35 threshold. The loop is seamless (first/last diff 0.9).

Timings from the frames (estimates):
- one launch about every 2 s;
- drags last about 1–1.5 s;
- the flight takes about 0.3–0.5 s, with landing between consecutive frames (f6 to f7 is 1.95 s apart and covers a full launch).

The arc preview implies a constant-gravity parabola, and tether stretch implies spring physics on release.

## 8. Brand system
n/a — not a brand system. Cues: a violet-black canvas plus a single electric-violet accent that appears only during interaction.

## 9. UX
- **Pro:** wonderfully legible feedback. The predicted value is shown before commit, the active control is the only coloured element, and labels and values are aligned.
- **Con:**
  - It is deliberately imprecise and slow for real settings work.
  - It is unusable by keyboard or screen reader unless standard arrow-key input is preserved.
  - Predicted-value text fails contrast.

It is a delight concept, not a production control.

## 10. Craft signals
- The dotted arc spacing compresses at the apex, the way a real projectile sampled at equal time steps does (key frame, y≈505).
- There are two tether lines from two anchors, not one, which reads as a slingshot band.
- The landing tick (2×24 px violet) is drawn on the track with its own value label.
- The accent colour is used only for the element in interaction. The other sliders stay greyscale.
- Mono values are right-aligned flush to the track's end cap (x≈1130).
- The violet-tinted near-black (#1a191e) canvas harmonises with the violet accent.

## 11. Reproduction recipe
```css
:root{--bg:#1a191e;--track:#353439;--fill:#e9e8ed;--label:#9a99a0;--accent:#6052ed;--accent-text:#8a80ff}
.row{display:grid;grid-template-columns:1fr auto;row-gap:22px;width:785px}
.label{font:400 24px Inter;color:var(--label)}
.value{font:400 22px "JetBrains Mono";color:var(--fill);font-variant-numeric:tabular-nums}
.row.is-aiming .value{color:var(--accent-text)} /* 5.0:1 — fixes the AA miss */
.track{grid-column:1/-1;height:3px;border-radius:9999px;background:linear-gradient(to right,var(--fill) var(--p),var(--track) 0)}
.knob{width:24px;height:24px;border-radius:50%;background:var(--fill)}
.knob.flying{background:var(--accent)} .knob.landed{box-shadow:0 0 0 2px var(--accent)}
.aim-dot{width:5px;height:5px;border-radius:50%;background:#6b6a6f}
```
```js
// preview: sample projectile at dt steps; v0 = k * (anchor - knob)
for(let t=0;t<T;t+=0.04){x=x0+vx*t; y=y0+vy*t+0.5*g*t*t; drawDot(x,y)}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Austere hairline layout with a single accent, very tidy. |
| Originality | 9 | Slingshot-to-set-value with trajectory preview is a genuinely new slider idea. |
| Usability | 5 | Excellent feedback, but imprecise and a11y-hostile as a real control, and the accent text fails AA. |
| Craft | 8 | Physically plausible arc spacing, twin tethers and a consistent two-font system. |

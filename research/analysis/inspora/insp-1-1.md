---
id: insp-1-1
source: inspora
category: Motion
status: analyzed
title: "Brightness & volume controller"
creator: "@staromlynski"
styles: [dark-premium, skeuomorphic, soft-3d, micro-interaction]
patterns: [pill-control-panel, mode-switch-icon-buttons, rotary-knob-input, gradient-fill-slider, value-readout-with-dim-unit, inactive-fill-dimming]
mode: dark
palette: ["#171717", "#222222", "#151515", "#95ffea", "#4bb0f6", "#ffd27a", "#f39a4a", "#fefefe"]
type_families: ["Satoshi / General Sans-style geometric grotesk (likely)"]
type_class: [geometric-sans]
radius_px: [9999, 31]
motion: {durations_s: [10.1], easing: [ease-in-out], loop: true}
scores: {aesthetics: 8, originality: 6, usability: 7, craft: 8}
craft_signals: [unit-symbol-dimmed, fill-colour-encodes-mode, knurled-knob-edge, inset-track-in-raised-panel, active-icon-button-filled, faint-background-grid]
anti_patterns: [white-on-light-fill-low-contrast, value-hidden-during-transition]
---
# Brightness & volume controller — @staromlynski

## 1. Snapshot
- **Subject:** A 960×720 10.1 s loop of a dark, pill-shaped hardware-like control panel. It has a gradient fill slider, two round mode buttons (sun = brightness, speaker = volume) and a knurled rotary knob that drives the value.
- **Why it's remarkable:** The fill colour is the mode. Brightness is a warm yellow→orange gradient and volume is a mint→sky-blue gradient. Switching mode cross-fades the fill hue while a knob turn drives the length.

## 2. Composition & layout
- **Panel:** centred, x≈160→792 (632 px) by y≈268→446 (178 px), so the radius is fully round (about 89 px). It sits on a #171717 canvas with a faint 1 px grid at about 160 px spacing (visible lines at x≈147, 807 and y≈253, 461, framing the panel).
- **Internal grid (left to right):**
  - Slider column, x≈213→540: the "Volume" label at y≈300 and the track at y≈328→392 (64 px tall, fully rounded).
  - Two stacked 58 px icon buttons at x≈560→618, centres y≈322 and y≈392.
  - Knob, about 128 px in diameter, centred at (698,357).
- **Padding:** about 53 px left, and about 30 px between the track and the buttons.

## 3. Typography
- **Family:** a geometric grotesk with round "o" and "e", close to Satoshi or General Sans.
- **Label:** "Volume" / "Brightness", about 19 px regular in #fefefe.
- **Value:** "72%", about 19 px. The "%" sign is rendered in a dimmer grey (about #888) than the digits (#fefefe), so only the number reads as the value.
- During a mode switch the number fades and is replaced (the frame at t=2.81 s shows "5" partially faded).

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #171717 | canvas | 87% (with panel) |
| #222222 | panel surface | 10.5% |
| #151515 | inset track / button wells | — |
| #95ffea → #4bb0f6 | volume fill gradient (left→right) | 2.4% |
| about #ffd27a → #f39a4a | brightness fill gradient | (other frames) |
| #fefefe | labels, active icon | — |

WCAG checks:
- Label #fefefe on panel #222: 15.78:1.
- Value #fefefe on track #151515: 18.1:1.
- Dim "%" (#888) on #151515: 5.15:1.
- **Weak point:** when the fill reaches the value text (about 90%), white on #4bb0f6 is only 2.38:1.

## 5. Depth & material
- **Panel:** raised with a broad soft drop shadow (about 0 20px 40px rgba(0,0,0,.5)) and a subtle top highlight edge.
- **Track:** inset (darker #151515 well with an inner shadow).
- **Fill:** glossy, with a lighter top edge and a soft coloured glow onto the track (about 6 px blur).
- **Knob:** two-tier. An outer knurled ring with about 40 radial ticks, an inner cap, and a recessed centre dot of about 36 px. Shading comes from the top-left.
- **Icon buttons:** the active one is filled black (#111) with a white icon. The inactive one is #222 with a grey icon. Their depth is inset.

## 6. Components & patterns
- A segmented mode switch made of two circular icon buttons stacked vertically.
- A rotary knob as the primary input (implied by the knob's tick ring rotating between frames).
- A fill slider whose length mirrors the knob angle.
- An inactive state: at t=0.56 s the brightness fill is desaturated (#8a6a40-ish) while the panel waits for input. At t=9.54 s the volume fill dims to about #2a4a50 with the value hidden, which reads as mute or idle.

## 7. Motion
- **Measured:** 10.1 s at 30 fps, `motion_fraction` 0.01, mean energy 0.05, and no segments above threshold. The moving area is small: fill length and knob ticks. `seamless_loop_likely: true` (first/last difference 0.41).
- **Estimated from frames:**
  - Brightness dims then lights (0.56→1.68 s).
  - The mode switches to Volume: the fill hue cross-fades and the value fades from 52 to 53 (about 2.8 s).
  - Volume ramps from 53% to 72% (3.9→5.1 s, about 1.1 s).
  - It holds, then drops to 14% (about 7.3 s).
  - It dims to idle (9.5 s).
- Changes are smooth with an ease-in-out feel. Number changes cross-fade rather than tick.

## 8. Brand system
n/a — not a brand system. Identity cues: an audio-hardware or Teenage-Engineering-adjacent tactility in dark mode.

## 9. UX
- The mode is communicated three times: label, filled icon button, and fill hue.
- The knob gives fine control, but on touch a rotary input is less discoverable than dragging the bar.
- The value overlaps the fill end at high values, which hurts contrast.
- Hiding the value during transitions briefly removes feedback.

## 10. Craft signals
- The "%" is dimmer than the digits, a typographic hierarchy inside a single token.
- Fill gradients run light to saturated in the direction of increase (mint→blue, cream→orange).
- The panel radius is exactly half its height (89 px), and the track radius is half its 64 px height. Every rounded element is a true pill.
- The knurled ring has evenly spaced ticks, and they move between frames (the rotation is real, not a static texture).
- A 1 px background grid frames the panel edges and aligns with them, a quiet stage for the object.

## 11. Reproduction recipe
```css
:root{--bg:#171717;--panel:#222;--well:#151515;--text:#fefefe;--muted:#888;
  --vol:linear-gradient(90deg,#95ffea,#4bb0f6);--bri:linear-gradient(90deg,#ffe08a,#f39a4a)}
.panel{display:grid;grid-template-columns:1fr 58px 128px;gap:20px;align-items:center;
  width:632px;height:178px;padding:0 30px 0 53px;border-radius:9999px;background:var(--panel);
  box-shadow:0 24px 48px rgba(0,0,0,.55), inset 0 1px 0 rgba(255,255,255,.06)}
.track{height:64px;border-radius:32px;background:var(--well);box-shadow:inset 0 2px 6px rgba(0,0,0,.6);position:relative}
.fill{height:100%;border-radius:inherit;background:var(--vol);width:72%;
  box-shadow:0 0 12px rgba(75,176,246,.35);transition:width .45s cubic-bezier(.65,0,.35,1),background .4s}
.panel[data-mode=brightness] .fill{background:var(--bri)}
.value .unit{color:var(--muted)}
.icon-btn{width:58px;height:58px;border-radius:50%;background:var(--panel)}
.icon-btn[aria-pressed=true]{background:#0f0f0f;color:#fff}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Cohesive dark hardware look; two clean gradient moods. |
| Originality | 6 | Skeuomorphic knob plus slider is a familiar Dribbble pattern. |
| Usability | 7 | Triple-coded mode, but contrast at high values and the knob are questionable on touch. |
| Craft | 8 | True pill geometry, a dimmed unit, and a real knob rotation. |

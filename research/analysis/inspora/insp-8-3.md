---
id: insp-8-3
source: inspora
category: Motion
status: analyzed
title: "Weather scrubber"
creator: "@nihalnova"
styles: [aurora-glow, micro-interaction, photo-led, corporate-clean]
patterns: [time-scrubber-tick-ruler, sky-gradient-follows-time, floating-time-pill, live-value-ticker, reset-to-now-button, dark-mode-at-night]
mode: mixed
palette: ["#08090e", "#2c1410", "#172d38", "#e8d9b0", "#f1e8e0", "#d9764a", "#6a9fd8"]
type_families: ["SF Pro Display / SF Pro Text (likely)"]
type_class: [neo-grotesk]
radius_px: [9999, 48]
motion: {durations_s: [8.13, 2.67, 0.5], easing: [linear, ease-in], loop: false}
scores: {aesthetics: 8, originality: 8, usability: 7, craft: 8}
craft_signals: [red-playhead-ticks, sun-position-tracks-hour, numeral-tints-warm-at-night, tom-prefix-for-next-day, metadata-row-updates-live, thumb-offset-label-above-finger]
anti_patterns: [secondary-metadata-2.5-to-1, label-hidden-under-thumb-on-edges]
---
# Weather scrubber — @nihalnova

## 1. Snapshot
- **Subject:** An 11.6 s, 3170×2160 handheld phone recording of a weather app prototype running on a real iPhone. The thumb drags a horizontal tick-ruler scrubber, and the whole screen's sky (gradient, sun disc, light/dark mode), temperature and conditions update continuously for the selected hour.
- **Why it's remarkable:** The entire UI is a function of one scrubbed time value. Dragging moves through midday blue, sunset orange and night black, and on into tomorrow morning. It feels like scrubbing a video of the sky.

## 2. Composition & layout
- **Filming:** close-up and handheld at an oblique angle; the phone screen fills about 60% of the frame. Dimensions below are estimated in screen points.
- **Temperature:** a large numeral, about 72 pt, at the left of the upper-middle, with a circular → arrow pill button (about 60×36 pt) on the right.
- **Condition row:** location arrow, "Gurugram · Partly Cloudy".
- **Metadata row:** H/L, humidity, UV/rain, at about 12 pt in grey.
- **Scrubber row:** a reset/"now" circular button (about 28 pt) at the left, then a ruler of about 60 ticks (about 1 pt wide at a ~4 pt pitch) spanning the rest of the width. A floating dark pill shows the selected hour ("2 PM", "Tom 5 AM") above the playhead.
- **Tab bar:** a pill tab bar at the bottom (Nearby, Cities, Rankings, More).

## 3. Typography
- **Typeface:** SF Pro, recognisable from the iOS system digits and the "R" in "Rankings".
- **Temperature:** about 72 pt Regular/Light with a degree symbol. It is #111 on day themes and switches to warm cream (#e8d9b0) at night.
- **Condition line:** about 15 pt Medium.
- **Metadata:** about 12 pt Regular in about #9a948e.
- **Time pill:** about 15 pt Semibold, white on #111 in daytime, inverted to dark on light at night.
- **"Tom" prefix:** "Tom 3 AM" is a compact abbreviation for tomorrow.

## 4. Colour
| Hex | Role | Share (key, night) |
|---|---|---|
| #08090e | night sky / screen | 35% |
| #2c1410 / #523830 | skin, warm shadows (filming) | 20% |
| #172d38 | dusk blue | 7% |
| #e8d9b0 | night temperature numeral | <1% |
| #f1e8e0 (est.) | day lower sky (cream) | — |
| #6a9fd8 (est.) | day upper sky | — |
| #d9764a (est.) | sunset sky | — |
| #e53935 (est.) | playhead ticks | <0.5% |

WCAG checks:
- The temperature (#111) on cream (#f1e8e0) is 15.61:1.
- The night numeral #e8d9b0 on #08090e is 14.19:1.
- The time pill, white on #111, is 18.88:1.
- Dark text on the sunset orange (#e07a50) is 6.36:1.
- Grey metadata on cream is **2.48:1 (fail)**.

## 5. Depth & material
- **Sky:** full-bleed vertical gradients, with a blurred sun disc (about 120 pt, soft-edged, warm cream-orange) whose position moves with the hour. It is high at noon and lower and redder at 6 PM (1.93 s vs 4.51 s frames). There is a faint halo ring at midday.
- **UI chrome:** floats on the sky. The arrow button and tab bar are frosted pills whose tint adapts (white-ish by day, black-ish at night).
- **Time pill:** a solid dark capsule with a soft shadow.

## 6. Components & patterns
- **Tick-ruler scrubber:** ticks are grey. The current position is marked by 2–3 red ticks forming a playhead, which shows a motion trail when dragging fast (key frame: doubled red ticks and a ghosted pill).
- **Reset button:** a "now" button with a circular-arrow icon.
- **Live metadata:** humidity, rain % and UV update per hour.
- **Theme switch:** the theme flips to dark when the scrub crosses into night (5.80 s) and back to light at dawn.

## 7. Motion
Measured (m0_motion.json, 30 fps, 11.60 s, motion_fraction 0.92). Because this is a handheld camera recording, energy includes camera shake and finger movement:
- **0.00–8.13 s (8.13 s, peak 0.74):** one long ease-in segment, a continuous scrub from 2 PM to tomorrow morning.
- **8.27–10.93 s (2.67 s, peak 0.79).**
- **11.07–11.57 s (0.50 s).**

The UI responds 1:1 to the finger, with no easing between hours. Sky colours interpolate continuously, as frames show intermediate states. The time pill appears ghosted or doubled in the key frame, which suggests a short cross-fade (about 100–150 ms, estimate) as labels change. The theme flip near midnight is also a cross-fade, not a cut.

## 8. Brand system
n/a — this is a product prototype, not a brand system. Identity cues: the sky-as-UI, the red playhead and the "Tom" shorthand.

## 9. UX
- **Strengths:** A direct-manipulation forecast replaces scrolling an hourly list. Feedback is immediate and multi-channel (number, sky, sun, label), and a reset-to-now button is provided.
- **Risks:**
  - Grey metadata is unreadable on the cream sky.
  - The thumb covers the playhead. The floating label above it mitigates this, but at the right edge the label is clipped ("Tom 12 P" at 10.95 s).
  - It is unclear how the scrubber is reached with assistive tech; it needs `role=slider` and step announcements.

## 10. Craft signals
- The playhead is a cluster of red ticks rather than a separate handle, so the ruler itself is the control.
- The sun disc position and colour track the time of day.
- The temperature numeral shifts to warm cream at night instead of pure white, so it does not glare.
- Frosted button tints invert with the theme.
- The label sits above the thumb with about a 30 pt offset.
- "Tom" disambiguates next-day hours in a 4-character prefix.

## 11. Reproduction recipe
```css
:root{--day-top:#6a9fd8;--day-bot:#f1e8e0;--dusk-top:#d9764a;--dusk-bot:#f3d9c8;--night:#08090e;--ink:#111;--night-ink:#e8d9b0;--tick:#9a948e;--play:#e53935}
.sky{background:linear-gradient(180deg,var(--top) 0%,var(--bot) 70%);transition:none} /* JS sets --top/--bot by hour */
.temp{font:300 72px/1 -apple-system,"SF Pro Display",system-ui;color:var(--ink)}
.night .temp{color:var(--night-ink)}
.ruler{display:flex;gap:3px;height:28px;align-items:center;touch-action:pan-y}
.ruler i{width:1px;height:16px;background:var(--tick);opacity:.6}
.ruler i.on{background:var(--play);height:22px;opacity:1}
.timepill{position:absolute;transform:translate(-50%,-44px);padding:6px 12px;border-radius:9999px;
  background:#111;color:#fff;font:600 15px/1 -apple-system,system-ui;transition:opacity .12s}
.night .timepill{background:#f1f1f1;color:#111}
.sun{width:120px;aspect-ratio:1;border-radius:50%;background:radial-gradient(#f6d59a,#f0b071 60%,transparent 70%);filter:blur(6px)}
```
JS: map x → hour (0–36 h), then interpolate a sky LUT, sun (x, y), temp and metadata.

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Beautiful sky gradients and restrained iOS chrome; mode shift at night is dramatic. |
| Originality | 8 | Whole-screen time scrubbing with a ruler is a fresh forecast interaction. |
| Usability | 7 | Direct and informative; low-contrast metadata and edge clipping of the label. |
| Craft | 8 | Sun tracking, warm night numerals, red-tick playhead, theme-aware frosted pills. |

---
id: insp-1-16
source: inspora
category: Illustration
status: analyzed
title: "Dark mode toggle"
creator: "@Designownow_"
styles: [soft-3d, physical-material, micro-interaction, glassmorphism]
patterns: [curved-track-toggle, theme-switch, groove-inset-track, glowing-trail-fill, corner-hugging-control, frosted-pill-thumb]
mode: mixed
palette: ["#dedede", "#d7d7d7", "#c7c7c7", "#39405a", "#30384b", "#242a37", "#5f3f68", "#d6a596"]
type_families: []
type_class: []
radius_px: [9999, 260]
motion: {durations_s: [0.43, 0.40, 0.47, 0.37], easing: [ease-in-out, ease-out], loop: true}
scores: {aesthetics: 8, originality: 9, usability: 5, craft: 8}
craft_signals: [track-concentric-with-card-corner, thumb-reorients-along-arc, specular-flare-on-rim, colour-coded-glow-per-mode, cast-shadow-follows-thumb, whole-scene-retints]
anti_patterns: [no-label-or-state-text, near-zero-surface-contrast, novelty-over-convention]
---
# Dark mode toggle — @Designownow_

## 1. Snapshot
- **Subject:** A 12.2 s, 1118×1080 clip of a theme switch whose track is a curved groove wrapping the rounded corner of a card. The thumb slides a quarter-circle from the top edge (light) to the right edge (dark), and the whole scene retints.
- **Why it's remarkable:** The toggle's path is derived from the layout. The groove runs concentric with the card's ~260 px corner radius, so the control looks carved into the object it configures.

## 2. Composition & layout
- A large card fills the lower-left (top edge at y≈365, right edge at x≈722 in the key frame), with its top-right corner rounded at about 260 px.
- The groove sits ~50 px outside that corner, ~45 px wide, sweeping 90° from horizontal (top, starting x≈400) to vertical (ending y≈700).
- **Thumb:** a horizontal pill ~175×130 px at the top end, which rotates to vertical (~130×175 px) at the bottom end. Its inner disc is ~85 px.
- Everything else is empty, so the control is the only object in roughly 1.2 Mpx of canvas.

## 3. Typography
None. The only glyph is an 8-tick "activity" spinner (~40 px) in the thumb disc: black on light, white on dark. There is no on/off text.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #dedede / #d7d7d7 | light-mode canvas and card | ~90% (light frames) |
| #c7c7c7 | light-mode shaded right gutter | ~8% |
| #39405a | dark-mode card / canvas (navy-slate) | 72% (key) |
| #30384b / #242a37 | dark background and shaded gutter | 21% / 6% |
| #5f3f68 | magenta-violet trail glow inside groove (dark) | <1% |
| #d6a596 | peach glow behind thumb disc (light) | <1% |

WCAG (surface separation, not text):
- #dedede vs #d7d7d7 is 1.07:1.
- #d7d7d7 vs #c7c7c7 is 1.17:1.
- The dark rim #4a4f66 vs #39405a is 1.27:1.

The card and groove are defined almost only by shadow and a 1 px highlight. Each mode gets one warm accent: peach for light (sun) and magenta for dark (night).

## 5. Depth & material
- **Groove:** an inset channel with a soft inner shadow and a 1 px light lip on its outer edge.
- **Thumb:** frosted, translucent glass. It has a bright specular flare at its top-left rim (a 4-point star glint) and a soft drop shadow (~40 px blur, offset down-right) that moves with it.
- **Inner disc:** a convex white button with its own small shadow.
- **Card:** a 1 px highlight on its top edge, plus a shaded gutter on its right (#c7c7c7 / #242a37) that suggests the card is raised.
- **Trail:** in dark mode a blurred magenta streak fills the groove behind the thumb, like a light trail.

## 6. Components & patterns
- **Binary switch on a curved track:** the end positions are top (light) and side (dark).
- **Thumb orientation:** the thumb stays tangent to the arc, so its long axis turns 90°.
- **State fill:** the trail fills the traversed path in dark mode, the way a progress track does.
- **Scene retint:** the toggle recolours the canvas, the card and itself together, which shows the result rather than a label.

## 7. Motion
Measured: 60 fps, duration 12.18 s, motion_fraction 0.12, seamless_loop_likely true. There are four segments:

| Segment (s) | Duration | Shape | Event |
|---|---|---|---|
| 0.97–1.40 | 0.43 s | ease-in-out (peak 0.42) | light → dark |
| 6.30–6.70 | 0.40 s | ease-in-out | dark → light |
| 8.00–8.47 | 0.47 s | ease-out (peak 0.32) | light → dark |
| 9.37–9.73 | 0.37 s | ease-in-out | dark → light |

The median is 0.42 s. From the frames (estimate), the background retint and the thumb travel share one timeline, and the thumb finishes without visible overshoot. Long holds of 1–5 s between clicks let the end states read.

## 8. Brand system
n/a — not a brand system. The peach-for-day, magenta-for-night accent pair could become an identity cue.

## 9. UX
- **Strengths:** The large hit area (~175 px) is good, and the immediate full-scene feedback makes the state unmistakable after the click.
- **Risks:**
  - Before the click nothing says what the control does.
  - The spinner icon reads as "loading", not "theme".
  - A curved track is unconventional for drag or keyboard input (what does an arrow key do?).
  - Surface contrast of about 1.1:1 hides the groove for low-vision users.

## 10. Craft signals
- The groove centre-line is offset by a constant ~50 px from the card corner arc (concentric radii).
- The thumb rotates exactly 90° between endpoints and stays tangent to the path.
- The specular star glint sits on the upper-left rim in both modes, so the light source is consistent.
- The drop shadow translates with the thumb and lengthens down-right in both positions.
- The accent glow changes hue per mode: peach (#d6a596) and magenta (#5f3f68).
- The trail fill appears only along the traversed arc.

## 11. Reproduction recipe
```css
:root{--bg:#dedede;--card:#d7d7d7;--gutter:#c7c7c7;--glow:#f2a58a;--r-card:260px;--t:.42s cubic-bezier(.45,0,.25,1)}
[data-theme=dark]{--bg:#30384b;--card:#39405a;--gutter:#242a37;--glow:#b0409a}
body{background:var(--bg);transition:background var(--t)}
.card{border-top-right-radius:var(--r-card);background:var(--card);box-shadow:inset 0 1px 0 rgba(255,255,255,.35),40px 0 60px -20px var(--gutter)}
.track{position:absolute;width:45px;border:45px solid transparent;border-top-color:rgba(0,0,0,.04);border-right-color:rgba(0,0,0,.04);
  border-top-right-radius:310px;box-shadow:inset 2px 2px 6px rgba(0,0,0,.12)}
.thumb{offset-path:path('M0,0 A310,310 0 0 1 310,310');offset-rotate:auto;offset-distance:0%;
  width:175px;height:130px;border-radius:9999px;backdrop-filter:blur(12px);
  background:radial-gradient(circle at 70% 50%,var(--glow) 0,transparent 45%),rgba(255,255,255,.35);
  box-shadow:inset 0 1px 0 rgba(255,255,255,.8),20px 30px 40px rgba(0,0,0,.18);transition:offset-distance var(--t)}
[data-theme=dark] .thumb{offset-distance:100%}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Calm two-mode palette, believable glass and shadow, one accent per mode. |
| Originality | 9 | Deriving the toggle path from the container's corner radius is a genuinely new idea. |
| Usability | 5 | Clear feedback, but there is no label, the spinner icon is misleading, and the groove contrast is about 1.1:1. |
| Craft | 8 | Concentric geometry, a tangent thumb and a consistent light source. The cursor overlay is slightly rough. |

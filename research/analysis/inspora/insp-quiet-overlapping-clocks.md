---
id: insp-quiet-overlapping-clocks
source: inspora
category: Product
status: analyzed
title: "Quiet overlapping clocks"
creator: "Lokki"
styles: [soft-3d, skeuomorphic, hairline-ui, physical-material]
patterns: [home-screen-widget, cropped-dial-quadrant, light-dark-widget-pair, digital-readout-pill, am-pm-badge, overlapping-cards]
mode: mixed
palette: ["#d7d3d9", "#e5e6e7", "#1e1e1e", "#cacacd", "#51514e", "#6ac23a", "#ff9500"]
type_families: ["SF Mono / JetBrains Mono-style monospace (likely)", "SF Pro (badges, likely)"]
type_class: [mono, neo-grotesk]
radius_px: [150, 9999]
motion: null
scores: {aesthetics: 9, originality: 8, usability: 6, craft: 9}
craft_signals: [off-centre-pivot-crops-dial, hairline-radial-guides, luminous-green-hour-ticks, dim-hour-digit-bright-minute, rotated-numerals-follow-dial, inner-rim-highlight, light-dark-pairing-overlap]
anti_patterns: [green-ticks-low-contrast-on-light, partial-dial-hard-to-read-hour]
---
# Quiet overlapping clocks — Lokki

## 1. Snapshot
- **Subject:** One 1500×1875 still of two square home-screen clock widgets, one light and one black, overlapping diagonally on a lilac-grey backdrop. They show 04:45 AM and 01:32 PM.
- **Why it's remarkable:** The dial's pivot is pushed into the **top-left corner** of the widget, so only one quadrant of the clock face is visible. The hand sweeps across a big arc of ticks, which turns a 2×2 widget into a dramatic close-up of a watch dial while a digital readout pill keeps it legible.

## 2. Composition & layout
- **Light widget:** about 720×720 px (x≈275→995, y≈460→1180).
- **Dark widget:** the same size, offset about +230 px x and +230 px y (x≈505→1230, y≈690→1415).
- The overlap of about 490×490 px forms a stepped diagonal. The pair sits slightly above centre, and a small credit line sits at y≈1730.
- **Widget anatomy:**
  - pivot at about (230, 230) px from the widget's top-left;
  - digital pill top-left, about 275×95 px;
  - AM/PM badge as a 95 px circle top-right;
  - ticks along an arc of radius about 400 px;
  - hour numerals placed outside the ticks.
- The dark widget **mirrors** the composition: its pivot is near the top edge (dial from 2 to 3 visible) and the readout and badge sit at the bottom.

## 3. Typography
- **Readout:** monospace (SF Mono / JetBrains Mono feel) at about 58 px. The hour digits ("04", "01") are grey #8a8a8a and the minute digits ("45", "32") are black or white. Dimming the hour reads as "time since the hour" emphasis.
- **Dial numerals:** about 40 px light mono, **rotated to follow the dial** (the "3", "4" and "5" tilt with the radius), in grey.
- **AM/PM badge:** a single capital "A" or "P", about 46 px Regular sans.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #d7d3d9 | backdrop (lilac-grey) | 77% |
| #e5e6e7 | light widget face | 10.5% |
| #1e1e1e | dark widget face | 9% |
| #cacacd | shadows, ticks | 2% |
| #51514e | credit text, dim marks | 1% |
| ~#6ac23a (estimated, too small to sample) | hour ticks, hand inlay | — |
| ~#ff9500 (estimated) | status dot in readout | — |

WCAG checks:
- #1e1e1e on #e5e6e7: 13.3:1.
- The grey hour digit #8a8a8a on its #ececec pill is **2.92:1**. This is intentional dimming but fails.
- Grey numerals (~#7a7a7a) on #1e1e1e: 3.88:1.
- **Green ticks on the light face: 1.79:1** vs 7.45:1 on the dark face. The green only really sings on black.
- Credit #51514e on the backdrop: 5.39:1.

## 5. Depth & material
- The widgets are thick, soft slabs. The light one has a gradient face (#efefef top-left → #dcdcde bottom-right), a 2 px inner rim highlight and a wide soft shadow (about 0 40 80 rgba(60,50,70,.18)) that tints the backdrop under the stack.
- The dark one has a subtle top-edge sheen.
- **Readout pill:** inset, slightly lighter (light widget) or lighter grey (dark widget), with an inner shadow.
- **Hands:** white with a green luminous inlay and a small round cap at the pivot.
- **Ticks:** the green hour ticks are raised with a soft glow; the minute ticks are short grey dashes.
- **Faint radial hairlines** (about 1 px, roughly 8% opacity) fan out from the pivot like a sundial, and a few blurred green streaks suggest motion trails or reflections.

## 6. Components & patterns
- **Widget:** analog quadrant, digital pill and AM/PM badge, a redundant encoding of time.
- **Status dot:** an orange dot inside the readout, probably signalling an alarm or live state.
- **Light/dark pair:** shows both appearances, and possibly two time zones (04:45 A vs 01:32 P).

## 7. Motion
Still image; no motion observed. The widget implies a continuous sweep of the hand across the visible arc. Home-screen widgets update once a minute, so the realistic behaviour is a 0.3–0.5 s ease-out tick per minute.

## 8. Brand system
n/a — not a brand system. Identity cues:
- luminous green inlay with an orange status dot, a watch-dial vocabulary (Braun / Apple Watch "Utility" lineage);
- mono numerals.

## 9. UX
- **Strengths:**
  - The digital readout guarantees legibility.
  - The A/P badge solves 12-hour ambiguity compactly.
  - Light and dark variants are designed together.
- **Risks:**
  - The analog quadrant shows only about 3 hours of the dial, so the hour is unreadable from the hands alone once the time leaves the visible arc.
  - The green ticks disappear on the light face.
  - The dim hour digits fail contrast.

## 10. Craft signals
- The pivot sits at about 32% of the widget's width and height, not centred, so the dial's arc is about 1.7× the widget.
- Dial numerals rotate tangentially (the "4" is tilted about 60°).
- Hour ticks are about 3× the length of minute ticks, coloured green with a white edge.
- The readout splits hour (grey) from minute (ink) inside the same mono string.
- The radius is a continuous squircle (about 150 px on 720 px, roughly 21%), matching iOS widget geometry.
- The dark widget mirrors the light widget's layout (readout bottom-left, badge bottom-right) rather than copying it.

## 11. Reproduction recipe
```css
:root{--bg:#d7d3d9;--face-light:#e5e6e7;--face-dark:#1e1e1e;--tick:#cacacd;--lume:#6ac23a;--dot:#ff9500;
  --r-widget:21%;--mono:"SF Mono","JetBrains Mono",ui-monospace,monospace}
.widget{width:360px;aspect-ratio:1;border-radius:var(--r-widget);position:relative;overflow:hidden;
  background:linear-gradient(135deg,#f1f1f2,var(--face-light) 60%,#dadadd);
  box-shadow:inset 0 0 0 2px rgba(255,255,255,.7),0 30px 60px rgba(60,50,70,.18)}
.widget.dark{background:linear-gradient(160deg,#2a2a2a,var(--face-dark) 40%);box-shadow:inset 0 1px 0 rgba(255,255,255,.08),0 30px 60px rgba(0,0,0,.25)}
.dial{position:absolute;left:32%;top:32%;width:0;height:0}          /* pivot */
.tick{position:absolute;width:3px;height:14px;background:var(--tick);transform-origin:0 0;
  transform:rotate(var(--a)) translateY(200px)}
.tick.hour{height:42px;width:6px;border-radius:3px;background:var(--lume);box-shadow:0 0 0 1px #fff,0 0 8px rgba(106,194,58,.4)}
.readout{font:400 29px/1 var(--mono);border-radius:9999px;padding:10px 18px;background:rgba(255,255,255,.55)}
.readout .h{color:#6f6f6f}.readout::after{content:"";width:10px;height:10px;border-radius:50%;background:var(--dot);display:inline-block;margin-left:12px}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 9 | A quiet, tactile pair with an exquisite lume accent and a strong diagonal composition. |
| Originality | 8 | The off-centre, cropped dial is a fresh take on clock widgets. |
| Usability | 6 | The digital pill rescues legibility, but the analog quadrant and green-on-light are weak. |
| Craft | 9 | Tangential numerals, hairline guides, mirrored layouts and squircle radii are all careful. |

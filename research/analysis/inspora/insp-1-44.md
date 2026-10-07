---
id: insp-1-44
source: inspora
category: Product
status: analyzed
title: "Meeting Finder"
creator: "@jeetnirnejak"
styles: [micro-interaction, data-dense, corporate-clean]
patterns: [timezone-overlap-grid, draggable-time-scrubber, per-row-colour-coding, working-hours-heat-cells, live-status-summary, find-best-time-cta, mono-time-readouts, nested-card-in-tray]
mode: light
palette: ["#ffffff", "#f2f2f2", "#2f6ff0", "#8a2cf0", "#e8064f", "#f08a00", "#111111", "#16a34a"]
type_families: ["Inter (likely)", "JetBrains Mono / Geist Mono (likely)"]
type_class: [neo-grotesk, mono]
radius_px: [40, 28, 6, 9999]
motion: {durations_s: [0.2, 0.1, 0.17], easing: [ease-in, ease-in-out, ease-out], loop: true}
scores: {aesthetics: 8, originality: 8, usability: 8, craft: 9}
craft_signals: [shoulder-hours-pale-tint, local-time-coloured-when-in-hours, scrubber-capsule-spans-all-rows, utc-chip-mono-slashed-zero, minus-one-day-suffix, success-state-turns-scrubber-green]
anti_patterns: [orange-time-text-low-contrast, colour-carries-in-hours-state]
---
# Meeting Finder — @jeetnirnejak

## 1. Snapshot
- **Subject:** A 14.7 s, 1924×1518 capture of a timezone overlap widget. Four cities (San Francisco UTC−7, New York UTC−4, São Paulo UTC−3, London UTC+1) are shown as 24-cell hour strips with a draggable vertical scrubber, a UTC chip, local-time readouts, a status line and a "Find best time" button.
- **Why it's remarkable:** A scheduling problem becomes a single glanceable chart. A vertical cut through the colour bars shows who is in working hours. On "Find best time", the scrubber snaps to 16:00 UTC and turns green: "Works for everyone".

## 2. Composition & layout
- **Container:** the same tray-plus-card system as the creator's Date Range Picker (insp-1-30).
  - Grey tray #f2f2f2, about 1082×640 px (x 422→1504, y 441→1080), radius about 40 px.
  - Inner white card inset about 21 px, radius about 28 px.
- **Header:** "Meeting Finder" (≈30 px Semibold) and a "20:00 UTC" mono chip.
- **Grid:**
  - A label column of about 215 px: dot, city ≈24 px, UTC offset ≈18 px mono grey.
  - 24 hour cells per row, each about 22×60 px with a 4 px gap and radius ≈6 px, spanning x 687→1307.
  - Hour ticks "00 06 12 18 UTC" at the top in mono.
  - A right column of local times at x≈1340.
- **Rows:** on a 76 px pitch.
- **Footer:** a status dot with text on the left, and a dark pill CTA (≈244×64 px) on the right.

## 3. Typography
- **Sans:** Inter-like; Semibold for the title, Regular for city names.
- **Mono:** used for all times, offsets and ticks ("13:00", "UTC−7"), with a slashed zero in "20:00" and "00". This separates data from labels.
- **Tense of status copy:** short and evaluative, e.g. "Off hours everywhere", "1 of 4 in working hours", "3 of 4, early in San Francisco", "3 of 4, late in London", "Works for everyone".

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #ffffff | stage, inner card | 85% |
| #f2f2f2 | tray, empty hour cells | 10% |
| #2f6ff0 | San Francisco hours | — |
| #8a2cf0 | New York | — |
| #e8064f | São Paulo | — |
| #f08a00 | London | — |
| pale tints (#bcd4fb, #dccbfb, #f8c1d0, #f8e07a) | shoulder hours (≈1 h each side) | — |
| #111111 | CTA, scrubber stroke | — |
| #16a34a | success scrubber / status | — |

WCAG checks:
- Coloured local times: blue 4.51:1, violet 5.68:1, red 4.6:1 (all pass).
- **Orange #f08a00: 2.52:1 (fails).**
- Out-of-hours grey times (#9a9a9a): 2.81:1, a deliberate de-emphasis but below AA.
- Status grey on tray: 5.7:1.
- CTA: 18.88:1.
- Green status text on mint: about 2.96:1.

## 5. Depth & material
- The tray has a soft shadow (≈0 30px 60px rgba(0,0,0,.08)). Everything inside is flat.
- **Scrubber:** a 2.5 px black outline capsule (≈32 px wide) spanning all four rows, with a black "handle" bar (≈34×8 px) above the tick row and ◀▶ arrows on the cursor. It is the only stroked element, so it reads as an overlay tool.

## 6. Components & patterns
- **Heat strip per city:**
  - full-saturation cells for core working hours (about 9 h);
  - pale cells for shoulder hours;
  - #f2f2f2 cells otherwise.
- **Local-time readout:** coloured in the city's hue when inside working hours and grey when outside. A "−1d"/"+1d" suffix appears in small grey when the day rolls over (frames at 0.82 s and 8.99 s).
- **UTC chip** updates live with drag.
- **Find best time:** at 13.90 s the scrubber is green-outlined at 16:00 UTC, the handle is green, and the status is "• Works for everyone" on a mint pill.

## 7. Motion
Measured: duration 14.72 s at 60 fps, motion_fraction 0.03, seamless_loop_likely true. Three segments, all in the last third:
- 9.17–9.37 s (0.20 s, peak_at 0.75, ease-in);
- 11.37–11.47 s (0.10 s, symmetric);
- 13.10–13.27 s (0.17 s, peak_at 0.30, ease-out). This is the snap to the best time.

The earlier drag (0.8–9 s) is continuous cursor-following that falls below the energy threshold, so it is direct manipulation with no easing. Programmatic moves get a short ease-out of about 170 ms.

## 8. Brand system
n/a — this is a product UI component, not a brand system. It shares tokens with insp-1-30 (tray #f2f2f2, 40/28 px radii, dark CTA), which suggests a personal component system.

## 9. UX
- **Strengths:**
  - The overlap is visible before the user reads anything.
  - The status sentence names *who* is the problem ("late in London").
  - The one-click best time.
  - The day-rollover suffix prevents date mistakes.
- **Weaknesses:**
  - Hue alone distinguishes cities: the label dots help, but red/orange are close for some users.
  - The orange readout fails contrast.
  - The hour cells are 22 px wide, which is a small touch target if tappable.

## 10. Craft signals
- Shoulder hours use a 25–30% tint of the city hue, giving soft edges to the working day.
- Local times switch from grey to the city colour only when inside working hours.
- The scrubber capsule has the same corner radius as the cells and spans exactly from the top row to the bottom row.
- All numerals are mono with slashed zeros, and the "UTC" tick label aligns with the 24th cell.
- The success state recolours the scrubber and handle green rather than adding a new element.

## 11. Reproduction recipe
```css
:root{--tray:#f2f2f2;--card:#fff;--empty:#f2f2f2;--ink:#111;--ok:#16a34a;
  --sf:#2f6ff0;--ny:#8a2cf0;--sp:#e8064f;--ldn:#f08a00;--mono:"JetBrains Mono",ui-monospace}
.finder{background:var(--tray);border-radius:40px;padding:21px;box-shadow:0 30px 60px rgb(0 0 0/.08)}
.grid{background:var(--card);border-radius:28px;padding:28px;display:grid;grid-template-columns:215px 1fr 90px;row-gap:16px}
.hours{display:grid;grid-template-columns:repeat(24,1fr);gap:4px}
.hours i{height:60px;border-radius:6px;background:var(--empty)}
.hours i.work{background:var(--c)} .hours i.shoulder{background:color-mix(in srgb,var(--c) 30%,#fff)}
.local{font:400 24px var(--mono);font-feature-settings:"zero";color:#9a9a9a}
.local.in-hours{color:var(--c)}
.scrubber{position:absolute;width:32px;inset-block:0;border:2.5px solid var(--ink);border-radius:10px;transition:left .17s cubic-bezier(.2,.8,.2,1)}
.scrubber.ok{border-color:var(--ok)}
.utc-chip{font:400 20px var(--mono);background:#e8e8e8;border-radius:9999px;padding:6px 18px}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Clean tray system. Four saturated strips give it energy. |
| Originality | 8 | Combining a scrubber, status sentence and auto-solve in one widget is a fresh take on the timezone grid. |
| Usability | 8 | Instantly legible overlap and helpful copy. The orange contrast and hue-only coding are weak points. |
| Craft | 9 | Tinted shoulders, conditional colouring, rollover suffixes, consistent tokens. |

---
id: insp-dynamic-island-streak
source: inspora
category: Motion
status: analyzed
title: "Dynamic Island Streak"
creator: "@calebwu_"
styles: [micro-interaction, minimal-swiss, high-contrast-bw]
patterns: [dynamic-island-expand, streak-counter, weekday-dot-tracker, flame-ember-burst, rolling-day-labels, icon-button-tooltip, number-tick-increment]
mode: light
palette: ["#fefefe", "#000000", "#1d1a19", "#ffffff", "#8a8a8a", "#f26a1b", "#e2e2e2", "#c8c8c8"]
type_families: ["SF Pro Display / Text (likely)"]
type_class: [neo-grotesk]
radius_px: [9999, 10]
motion: {durations_s: [0.27, 0.1, 0.1, 0.1, 0.27], easing: [ease-out, ease-in-out], loop: true}
scores: {aesthetics: 8, originality: 7, usability: 8, craft: 8}
craft_signals: [dashed-ring-for-future-days, flame-only-colour-in-ui, leading-zero-streak-count, week-window-slides-on-increment, ember-particles-on-flame, tooltip-dark-chip-under-control]
anti_patterns: [control-rims-1-66-on-white]
---
# Dynamic Island Streak — @calebwu_

## 1. Snapshot
- **Subject:** A 13.3 s, 1144×720 prototype on a white canvas: a black Dynamic-Island pill expands into an "08 Day Streak" Live Activity with a flame and a 4-day dot tracker; pressing "+" (tooltip "Add streak") bumps it to 09 and rolls the week forward, then it collapses.
- **Why it's remarkable:** Streak state is encoded with three tiny, legible devices — a leading-zero count, filled vs. dashed day dots, and a flame that bursts into embers — all inside a 515×132 px pill.

## 2. Composition & layout
- Expanded pill ≈515×132 px, centred at (580, 295), fully rounded (66 px).
- Internal layout: flame icon ≈50×70 at x≈375–425; "08" ≈36 px semibold over "Day Streak" ≈18 px at x≈457; day columns (letter over dot) at x≈683/719/755/791, i.e. a 36 px pitch, right-aligned with ≈46 px end padding.
- Compact pill states: ≈345×88 px (start) and ≈175×48 px (end) — island resting sizes.
- Control row 240 px below the pill: three 62 px outlined circles (add, reset, swap/compare), 16 px gaps; tooltip chip ≈105×48 px, 10 px radius, 26 px below the hovered button.

## 3. Typography
- SF Pro: streak number "08" ≈36 px semibold white, tabular with leading zero; "Day Streak" ≈18 px regular grey.
- Day initials ≈18 px medium: white for completed days, grey for upcoming.
- Tooltip "Add streak" ≈15 px white on near-black.

## 4. Colour
| Hex | Role | Share (key frame) |
|---|---|---|
| #fefefe | canvas | 90% |
| #000000 | island pill | 7% |
| #ffffff | number, completed dots | — |
| #8a8a8a | secondary label, upcoming days | — |
| #f26a1b → #e8401c | flame gradient (only colour) | <1% |
| #1d1a19 | tooltip chip | 1% |
| #e2e2e2 / #c8c8c8 | control rims / disabled icon | 1% |

WCAG (contrast.py):
- "Day Streak" #8a8a8a on #000: 6.08:1 (pass).
- Upcoming day letters ≈#6c6c6c on #000: 4.0:1 (large-only).
- Tooltip white on #1d1a19: 17.3:1.
- Control rims #c8c8c8 on white: **1.66:1** — below the 3:1 non-text guideline.

## 5. Depth & material
- Fully flat: black pill on white, no shadow — honest to the hardware island.
- The flame is the only rendered object: an orange-to-red gradient with a pale inner tongue and a single spark dot above.
- Controls are hairline (1 px) outlined circles; hovered one gets a light grey fill.

## 6. Components & patterns
- **Weekday tracker:** filled 12 px white dot = done, dashed 12 px ring = upcoming. The 4-day window slides (T F S S → F S S M) when the streak increments, keeping "today" in a fixed column.
- **Streak counter** with leading zero, so 08 → 09 doesn't change width.
- **Flame burst:** at ≈3.7 s the flame dissolves into ≈6 orange shards/embers before re-forming — reward feedback.
- **Icon toolbar with tooltip** for prototype controls.

## 7. Motion
Measured (m0_motion.json): 13.33 s at 60 fps, motion_fraction 0.07 (very sparse), seamless_loop_likely true, 5 segments, median 0.10 s.
- 0.67–0.93 s (0.27 s, peak 0.31, ease-out): compact pill expands into the Live Activity.
- 1.03–1.13 s (0.10 s, ease-out): content settles/fades in.
- 3.00–3.10 s and 3.57–3.67 s (0.10 s each, symmetric): flame ember burst ticks.
- 10.57–10.83 s (0.27 s, peak 0.19, ease-out): collapse to the small pill.
The number tick and week roll (≈7–8 s) fall below the motion threshold — they are small, crisp swaps rather than big moves. Expand and collapse share an identical 0.27 s ease-out — symmetric timing tokens.

## 8. Brand system
n/a — not a brand system. Identity cues: flame mark as the streak symbol, black/white only plus one orange.

## 9. UX
- Very glanceable: count, progress and upcoming days in one line.
- Leading zero and fixed day columns prevent layout shift.
- Dashed rings clearly read as "not yet" rather than "missed" — kind design.
- Risks: no distinct state for a missed day; prototype control outlines are faint.

## 10. Craft signals
- Upcoming days use a dashed ring, not a dim dot.
- Orange appears only in the flame.
- "08"/"09" keep a fixed two-digit width.
- The week window shifts by one column on increment, keeping today's slot stable.
- Expand and collapse both measured at 0.27 s.
- Tooltip is a 10 px-radius dark chip centred under its button.

## 11. Reproduction recipe
```css
:root{--bg:#fefefe;--island:#000;--fg:#fff;--fg-2:#8a8a8a;--flame-a:#ff8a2a;--flame-b:#e8401c;--t:.27s;--ease:cubic-bezier(.2,.8,.2,1)}
.island{background:var(--island);color:var(--fg);border-radius:9999px;height:132px;width:515px;
  display:grid;grid-template-columns:auto 1fr auto;align-items:center;padding:0 46px 0 50px;gap:30px;
  transition:width var(--t) var(--ease),height var(--t) var(--ease)}
.island.compact{width:175px;height:48px}
.count{font:600 36px/1 system-ui;font-variant-numeric:tabular-nums}
.days{display:grid;grid-auto-flow:column;grid-auto-columns:36px;text-align:center;font:500 18px system-ui}
.dot{width:12px;height:12px;border-radius:50%;margin:10px auto 0}
.dot.done{background:#fff} .dot.todo{border:1.5px dashed #6c6c6c}
.flame{background:linear-gradient(180deg,var(--flame-a),var(--flame-b));clip-path:path('M25 0 L50 55 Q25 75 0 55 Z')}
.tip{background:#1d1a19;color:#fff;border-radius:10px;padding:12px 14px;font:15px system-ui}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Pure black/white with one flame of colour; perfectly balanced pill. |
| Originality | 7 | Streak Live Activity is expected, but the rolling week window and ember burst are nice. |
| Usability | 8 | Highly glanceable; no layout shift; missed-day state absent. |
| Craft | 8 | Consistent 36 px day pitch, tabular count, symmetric 0.27 s expand/collapse. |

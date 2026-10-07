---
id: insp-progress-bar-animation
source: inspora
category: Motion
status: analyzed
title: "progress bar animation"
creator: "Petar Cirkovic (@kippe07)"
styles: [micro-interaction, maximalist-color, minimal-swiss]
patterns: [full-bleed-progress-fill, squiggle-pause-state, colour-swap-on-state, pause-resume-toggle, percent-counter, wobble-on-resume]
mode: dark
palette: ["#2d47f2", "#3b54f6", "#ffffff", "#b5bef7", "#f39e30", "#e6952e", "#1e140c"]
type_families: ["SF Pro Display / Inter (likely)"]
type_class: [neo-grotesk]
radius_px: [9999]
motion: {durations_s: [0.23, 0.27, 0.27, 0.23, 5.44], easing: [ease-out, ease-in-out], loop: false}
scores: {aesthetics: 7, originality: 8, usability: 7, craft: 8}
craft_signals: [line-compresses-into-squiggle-on-pause, ink-inverts-with-background, dimmed-percent-sign, tint-shift-marks-filled-area, wobble-settle-on-resume, round-line-caps]
anti_patterns: [filled-vs-unfilled-only-1.15-to-1, state-change-relies-on-hue-swap]
---
# progress bar animation — Petar Cirkovic

## 1. Snapshot
- **Subject:** A 5.44 s, 1912×1432 @120 fps demo of a full-screen progress indicator: a white line grows left-to-right with a percent counter; tapping pause turns the screen orange and the line's leading end "squeezes" into a squiggle; resume returns to blue with a wobble.
- **Why it's remarkable:** Pause is shown as physical compression — the line bunches up like a spring at its head — so "paused, holding tension" is felt rather than labelled.

## 2. Composition & layout
- Full-bleed colour field. The fill area (left of the line's head) is a slightly lighter tint of the background, so the whole screen is the progress bar.
- The line (≈ 14 px stroke, round caps) sits at y ≈ 50% (≈ 718 px of 1432); the percent counter is centred at y ≈ 30%; a 140 px circular control is centred at y ≈ 71%.
- A strict vertical centre axis for counter and button; only the line runs edge-anchored from x=0.

## 3. Typography
- Neo-grotesk numerals ≈ 105 px regular (SF Pro Display / Inter), tabular-looking; "%" at the same size but ≈ 60% opacity (#b5bef7 on blue) so the number dominates.
- No other text; icons do the rest (pause = two bars in a 6 px ring, resume = circular-arrows refresh glyph).

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #2d47f2 | running background (unfilled) | — |
| #3b54f6 | running filled region | up to 98% |
| #ffffff | line, numerals, icon (running) | 1% |
| #b5bef7 | dimmed "%" | 0.6% |
| #f39e30 | paused background (unfilled) | — |
| #e6952e | paused filled region | — |
| #1e140c | line, numerals, icon (paused) | — |

WCAG checks:
- White on blue fill #3b54f6: 5.55:1.
- Dim "%" #b5bef7 on #3b54f6: 3.08:1 (AA-large only — acceptable at 105 px).
- Near-black #1e140c on orange #e6952e: 7.5:1 — the ink flips to dark on orange, correctly (white on orange would be 2.16:1).
- Filled vs unfilled tint: **1.15:1 blue, 1.12:1 orange** — the area boundary is almost invisible; the line does the work.

## 5. Depth & material
Completely flat. The only "material" is the line's behaviour: it behaves like an elastic cord (it compresses into an S-curve kink at its head when paused and ripples as a low-amplitude sine wave right after resuming — visible at 0.91 s, 2.12 s and 5.14 s).

## 6. Components & patterns
- Full-screen determinate progress with a large percentage readout.
- Pause/resume toggle; the background hue encodes state (blue = running, orange = paused).
- Squiggle "compression" glyph at the line head during pause (≈ 80 px tall S-shaped kink).
- The cursor in the capture shows it was a clickable prototype (Rive / Framer-style).

## 7. Motion
Measured (m0_motion.json): 5.44 s at 120 fps, motion_fraction 0.19, 4 short segments (median 0.25 s), not a loop. Segments track the full-screen colour swaps:
- 0.93–1.17 s (0.23 s), peak_at 0.21 → ease-out — blue→orange on pause;
- 1.87–2.13 s (0.27 s), peak_at 0.31 → ease-out — orange→blue on resume;
- 3.43–3.70 s (0.27 s), peak_at 0.44 → symmetric — second pause;
- 4.73–4.97 s (0.23 s), peak_at 0.36 → symmetric — second resume.
State swaps take ≈ 0.25 s — snappy and responsive. Progress itself advances at ≈ 33%/s while running (11% at 0.30 s → 31% at 0.91 s; 36% at 2.12 s → 78% at 3.33 s), estimated from frames. After resume, the line ripples for ≈ 0.3–0.5 s and then straightens (2.12 s frame wavy, 2.72 s straight).

## 8. Brand system
n/a — not a brand system. A complementary blue/orange pair is used as the state code.

## 9. UX
- Pause state is unmistakable: hue flip, icon change (pause → refresh/resume) and the squiggle — three redundant cues.
- Large, centred percent is readable at a distance.
- **Risks:** blue↔orange relies partly on hue (fine for most colour-vision deficiencies because the luminance also changes and the ink inverts); the "resume" icon is a refresh glyph, which reads as "restart" — ambiguous; full-screen colour flashes may be heavy for a minor action.

## 10. Craft signals
- Ink colour inverts (white → #1e140c) with the background so contrast stays ≥ 5.5:1 in both states.
- "%" dimmed to ≈ 60% opacity next to full-white digits.
- The squiggle forms at the line's head only; the rest of the line stays straight.
- Round line caps match the round control ring.
- Captured at 120 fps — the wobble is smooth, not stepped.

## 11. Reproduction recipe
```css
:root{--run-bg:#2d47f2;--run-fill:#3b54f6;--pause-bg:#f39e30;--pause-fill:#e6952e;--ink:#fff}
.progress{--p:0;background:linear-gradient(90deg,var(--run-fill) calc(var(--p)*1%),var(--run-bg) 0);
  transition:background-color .25s cubic-bezier(.2,.8,.2,1)}
.progress[data-paused]{--run-fill:var(--pause-fill);--run-bg:var(--pause-bg);--ink:#1e140c}
.count{font:400 52px/1 "SF Pro Display",Inter,sans-serif;color:var(--ink);font-variant-numeric:tabular-nums}
.count .pct{opacity:.6}
.line path{stroke:var(--ink);stroke-width:7;stroke-linecap:round;fill:none}
/* SVG path d morphs between a straight head and an S-kink */
.line[data-paused] .head{d:path("M0 0 H-40 C-30 0 -30 -20 -20 -20 S-10 20 0 20 H10");transition:d .25s ease-out}
.line.resumed{animation:wobble .45s ease-out}
@keyframes wobble{25%{transform:translateY(-3px)}50%{transform:translateY(2px)}75%{transform:translateY(-1px)}}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 7 | Bold, graphic, but the flat full-screen fields are blunt. |
| Originality | 8 | "Squeeze when paused" is a fresh physical metaphor for a common control. |
| Usability | 7 | Triple-coded state; ambiguous resume icon; invisible fill boundary. |
| Craft | 8 | Ink inversion, round caps and smooth wobble at 120 fps. |

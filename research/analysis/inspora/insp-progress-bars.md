---
id: insp-progress-bars
source: inspora
category: Motion
status: analyzed
title: "progress bars"
creator: "@ozzyxs1a"
styles: [retro-pixel, playful-rounded, micro-interaction]
patterns: [narrative-loading-bar, segmented-block-progress, state-coloured-label, retry-state, success-state, characters-standing-on-bar]
mode: light
palette: ["#ffffff", "#6c8a98", "#ced5d8", "#dddee2", "#c0506a", "#5f9a72", "#282a31", "#9d867d"]
type_families: ["custom pixel font (5×7 bitmap, Press Start / Silkscreen-like)"]
type_class: [pixel]
radius_px: []
motion: {durations_s: [0.13, 0.2, 0.33, 19.67], easing: [steps], loop: false}
scores: {aesthetics: 7, originality: 8, usability: 6, craft: 8}
craft_signals: [label-and-fill-share-state-colour, bar-resets-after-retry, sprite-poses-sync-to-progress, 1px-bevel-on-bar-frame, percent-right-label-left-baseline-aligned, three-state-palette-blue-red-green]
anti_patterns: [licensed-ip-characters, label-contrast-below-aa]
---
# progress bars — @ozzyxs1a

## 1. Snapshot
- **Subject:** A 19.7 s, 2214×1232 @30 fps pixel-art loading bar on which two lightsaber duellists fight; the outcome of the duel mirrors the loading state: LOADING (blue-grey), RETRYING (red, when the robed fighter is knocked down) and SUCCESS (green at 100%).
- **Why it's remarkable:** A progress bar with a plot — failure and retry are dramatised by the characters, and every state is redundantly coded by label text, fill colour and the sprites' poses.

## 2. Composition & layout
- A white stage; the bar is centred horizontally at y≈57% (≈ 970 px wide original, x≈570→1645), ≈ 60 px tall, with ≈ 22 discrete block cells ≈ 40×30 px and 4 px gutters.
- Two sprites ≈ 200 px tall stand directly on the bar's top edge near its centre — the bar is literally their floor.
- Label "LOADING" left-aligned under the bar's left edge and "50%" right-aligned under its right edge, both ≈ 40 px cap height; the gap bar→label is ≈ 45 px.
- Generous empty margins (≈ 50% of the frame is white).

## 3. Typography
- A bitmap pixel font (5×7-ish grid, Silkscreen / Press Start-like) in caps; letterforms are drawn with 1-pixel steps scaled ≈ 6×. The "%" glyph is a compact pixel slash.
- One size only; state is conveyed by colour + word.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #ffffff | stage | 95% |
| #6c8a98 | loading fill blocks + label | 0.4% |
| #ced5d8 / #dddee2 | empty cells, bar frame | 2% |
| #b0bec4 / #c5c9cb | frame bevel, shadow edge | 0.8% |
| #c0506a (est.) | retry state fill + label, red saber | <0.5% |
| #5f9a72 (est.) | success fill + label | <0.5% (at end) |
| #282a31 | dark duellist | 0.4% |
| #9d867d / #704f54 | robe browns | 0.6% |

WCAG checks:
- "LOADING" #6c8a98 on white: **3.67:1** (AA-large only; the pixel text is large, so this is borderline acceptable).
- "RETRYING" #c0506a on white: 4.57:1.
- "SUCCESS" #5f9a72 on white: **3.31:1**.
- Filled block #6c8a98 vs empty cell #dddee2: 2.73:1 — readable but soft.

## 5. Depth & material
- A flat pixel-art bar with a 1 px-scaled bevel (lighter top edge, darker #b0bec4 bottom lip ≈ 6 px) — a classic 16-bit UI frame.
- Filled cells have a lighter top row of pixels, a tiny inner highlight.
- Sprites carry 3–4 tone shading per material (robe tan/brown, black armour with grey highlights, saber blades with a white core and coloured edges).

## 6. Components & patterns
- Segmented block progress (discrete cells, not a smooth fill) — matches the pixel aesthetic and quantises progress.
- State label + percent pair.
- Error/retry state: the robed fighter falls (3.28 s), the fill and label turn red, and then progress restarts from a low value (25% → 8% at 5.46 s).
- Success state: green fill and label at 100% as the robed fighter lands the final strike (18.57 s).
- The characters are recognisable licensed film characters — fine as a fan piece, not usable commercially.

## 7. Motion
Measured (m0_motion.json): 19.67 s at 30 fps, motion_fraction 0.18, **23 micro-segments with median 0.13 s** (4 frames at 30 fps), not a loop. The motion is sprite-frame animation: short bursts of 0.10–0.33 s (sword swings, the fall), each either ease-out (peak 0.06–0.12) or ease-in (peak 0.83–0.88) — characteristic of stepped, held-pose animation rather than tweening. Longer beats of 0.33 s at 9.70 and 15.63 s (peak 0.65) are the big clashes.
- Progress pacing (estimated from frames): 12% at 1.09 s → 25% (retry) at 3.28 s → reset to 8% at 5.46 s → 30% at 7.65 s → 50% at 9.83 s → 67% at 12.02 s → 82% at 14.20 s → 93% at 16.39 s → 100% at 18.57 s ≈ 7.5% per second after the retry.
- Cells fill one at a time (stepped), consistent with `steps()` timing.

## 8. Brand system
n/a — not a brand system. It borrows a film franchise's iconography (fan art).

## 9. UX
- Makes waiting entertaining and, crucially, makes the retry legible: the user sees that something failed and restarted, not a frozen bar.
- State is coded three ways (word, colour, character pose) — robust for colour-blind users.
- **Risks:** the narrative may imply false progress semantics (does losing the duel cause the failure?); label contrast sits below AA for normal text; the 20 s demo pacing is long for real loads; IP issues.

## 10. Craft signals
- Label colour and fill colour switch together on each state (blue-grey → red → blue-grey → green).
- Sprites stand exactly on the bar's top bevel; feet pixels touch the frame line.
- "LOADING" left edge and "%" right edge align with the bar's outer frame.
- Block gutters are consistent (≈ 4 px) across all ~22 cells.
- After the retry, the bar visibly resets rather than continuing — honest feedback.

## 11. Reproduction recipe
```css
:root{--load:#6c8a98;--retry:#c0506a;--ok:#5f9a72;--cell:#dddee2;--frame:#ced5d8;--bevel:#b0bec4}
.pbar{--state:var(--load);--n:22;--p:0;display:grid;grid-template-columns:repeat(var(--n),1fr);gap:4px;
  padding:6px;background:#ebeef0;box-shadow:0 0 0 4px var(--frame),0 8px 0 0 var(--bevel);image-rendering:pixelated}
.pbar[data-state=retry]{--state:var(--retry)} .pbar[data-state=ok]{--state:var(--ok)}
.cell{height:30px;background:var(--cell)} .cell.on{background:var(--state);box-shadow:inset 0 3px 0 rgba(255,255,255,.2)}
.label{font:24px/1 "Silkscreen","Press Start 2P",monospace;color:var(--state);text-transform:uppercase;display:flex;justify-content:space-between}
.sprite{animation:swing .4s steps(4) infinite}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 7 | Charming, clean pixel art on white; deliberately low-fi. |
| Originality | 8 | A loading bar that dramatises retry and success is a clever idea. |
| Usability | 6 | Triple-coded states; soft contrast and long pacing. |
| Craft | 8 | Pixel-consistent sprites, aligned labels, synced state colours. |

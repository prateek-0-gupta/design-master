---
id: insp-1-39
source: inspora
category: Motion
status: analyzed
title: "Watch face"
creator: "@itshassco"
styles: [micro-interaction, minimal-swiss, playful-rounded]
patterns: [physics-rope-hands, draggable-hands-spring-back, settings-sidebar-pills, segmented-control, colour-theme-swatches, floating-pill-buttons]
mode: light
palette: ["#ebebeb", "#ffffff", "#111111", "#d71e2c", "#646464", "#979797", "#ddf5c5", "#c3d9ee"]
type_families: ["Inter / SF Pro Text (likely)", "wide squared display numerals (Eurostile Extended / Michroma-like, likely)"]
type_class: [neo-grotesk, display]
radius_px: [9999]
motion: {durations_s: [0.4, 0.63, 0.4, 0.3, 0.33, 0.43, 0.63], easing: [ease-in-out, ease-out], loop: true}
scores: {aesthetics: 7, originality: 9, usability: 5, craft: 8}
craft_signals: [hands-as-verlet-ropes, spring-return-to-true-time, red-seconds-only-accent, two-tier-tick-marks, ghost-ring-shows-anchor, pill-only-chrome]
anti_patterns: [numerals-low-contrast, joke-interaction-obscures-time]
---
# Watch face — @itshassco

## 1. Snapshot
- **Subject:** A 3452×2160, 17.1 s, 60 fps capture of "CO'WATCH!", a browser clock whose hands are **strings**: soft ropes pinned at the centre. You can grab a hand's tip, swing it, tangle it, and let it fall back to the correct time.
- **Why it's remarkable:** It replaces rigid clock hands with rope physics. Reading the time is still possible at rest, but every drag produces a believable catenary sag, overshoot and settle. A "mode" selector ("Strings +") implies other physical hand models.

## 2. Composition & layout
- **Dial:** centred at about x≈1725, y≈1075 real (key scale 1.73), diameter ≈1660 px. It fills ≈77% of the viewport height.
- **Left settings column:** ≈80 px from the left edge, ≈620 px wide, stacked as:
  - a palette icon button;
  - "SYSTEM PREFERENCES": a MODE pill and 5 colour swatches;
  - "SOUND": a Mute / System / Watch segmented control and a 100% volume bar;
  - "SUPPORT": a "Buy me a coffee" pill;
  - the "CO'WATCH!" wordmark and credit.
- **Corners:** top-right holds X (share) and fullscreen circular buttons; bottom-right holds the date pill "Sun, 23 Aug".
- **Feel:** the clock floats in empty space with all chrome pushed to the edges, like a desktop widget.

## 3. Typography
- **UI text:** Inter / SF-like. Section labels are uppercase, ≈30 px real, semibold, grey #646464, tracked ≈+0.04em. Control text is ≈34 px regular.
- **Dial numerals:** 12 / 3 / 6 / 9 in a wide, squarish display face (Eurostile Extended / Michroma-like), ≈95 px cap height in mid-grey #979797. This is an engineered retro-instrument voice.
- **Wordmark:** "CO'WATCH!" is a bold grotesk in light grey with a smaller credit line below it.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #ebebeb | page / dial background | 94% |
| #ffffff | pill controls, swatch rings | 2.3% |
| #111111 | hour and minute rope hands, pivot, primary text | <1% |
| #d71e2c | seconds rope (sole accent) | <1% |
| #646464 | section labels | <1% |
| #979797 / #737373 | numerals, major ticks | ~1% |
| #ddf5c5 / #fefe8e / #c3d9ee | theme swatches (mint, lemon, sky) | <0.5% |

WCAG checks:
- Black UI text on the white pills: 18.88:1.
- Hands #111 on #ebebeb: **15.84:1**.
- Section labels #646464 on #ebebeb: 4.96:1.
- Red seconds #d71e2c: 4.28:1, which is fine for a graphic.
- **Dial numerals #979797 on #ebebeb: 2.45:1**, so they are decorative rather than legible.

## 5. Depth & material
- **Chrome:** pills are white with a very soft shadow (≈0 4px 12px rgba(0,0,0,.06)). The volume bar sits in a recessed grey track.
- **Dial:** fully flat. The 60 minor ticks are ≈2 px and light; the 12 major ticks are ≈10×40 px and darker grey.
- **Rope hands:** ≈8 px black strokes with round caps and a filled pivot dot of ≈40 px. The red seconds rope has a ≈20 px red bob at its end. Hollow ≈40 px rings mark where a displaced tip's true anchor is (8.53 s: hollow rings at the 10 and 2 positions while the ropes hang loose).

## 6. Components & patterns
- **Draggable physics hands:** each is a rope with a fixed root at the centre and a tip pinned to the time position. Dragging detaches the tip; releasing springs it back to its anchor ring.
- **Segmented control:** "Watch" is selected with a white pill on a grey track.
- **Theme swatches:** five circles of 64 px real; the selected one has a white ring.
- **Floating pill buttons:** share, fullscreen and date.
- **Sound:** the "Watch" sound mode suggests ticking audio tied to the physics.

## 7. Motion
- **Measured:** 17.07 s at 60 fps. motion_fraction 0.20. 10 segments, median **0.36 s**. Most are symmetric (peaks 0.39–0.65): for example 1.03–1.43 s (0.40 s), 1.63–2.27 s (0.63 s), 13.47–13.90 s (0.43 s), 14.70–15.33 s (0.63 s). Two ease-out segments sit at 2.73 s (0.40 s, peak 0.12) and 12.83 s (0.17 s, peak 0.10).
- seamless_loop_likely **true** (first/last diff 0.92).
- **Interpretation:**
  - The symmetric 0.4–0.6 s segments are drags and pendulum swings.
  - The fast-start ease-out segments are releases, where the rope snaps back and decelerates.
  - Between them, ropes hang still (catenary sag at 4.74 s and 8.53 s) because gravity, not time, drives the shape until the user lets go.
  - At 2.84 s the minute and hour ropes show S-curves from a fast swing, which is visible secondary motion and good evidence of a verlet or spring simulation.

## 8. Brand system
n/a — not a brand system. A small personal product identity: "CO'WATCH!" wordmark, a red-seconds accent and an all-pill control language.

## 9. UX
- **Strengths:**
  - A delightful toy with full-bleed focus.
  - The settings are compact and readable.
  - The true time is restored automatically, so play never breaks the function.
- **Risks:**
  - Numerals at 2.45:1 and the floppy hands make it hard to tell the time at a glance during or after interaction.
  - Grabbing a thin 8 px rope tip needs a generous hit area.
  - The creator calls it "the most useless watch face"; it is a delight piece, not a utility.

## 10. Craft signals
- Rope hands sag with gravity and show S-curve secondary motion after fast swings.
- Hollow anchor rings appear only while a hand is displaced, showing where it will return.
- Red is reserved exclusively for the seconds rope and its bob.
- Ticks come in two tiers: 60 thin minor ticks and 12 heavy major ticks.
- Every control (mode, swatches, segmented control, volume, buttons, date) is a full pill, with no other radius in use.
- The numerals are tucked inside the major ticks, and the 12 overlaps the hand pivot path.

## 11. Reproduction recipe
```css
:root{--bg:#ebebeb;--surface:#fff;--ink:#111;--accent:#d71e2c;--muted:#646464;--dial:#979797;
  --font:"Inter",system-ui;--dial-font:"Michroma","Eurostile Extended",sans-serif}
body{background:var(--bg);font:400 17px/1.2 var(--font)}
.pill{background:var(--surface);border-radius:9999px;padding:10px 14px;box-shadow:0 4px 12px rgba(0,0,0,.06)}
.label{font:600 13px/1 var(--font);letter-spacing:.04em;text-transform:uppercase;color:var(--muted)}
.seg{background:#dedede;border-radius:9999px;padding:4px;display:flex}
.seg [aria-pressed=true]{background:#fff;border-radius:9999px}
.numeral{font:400 48px/1 var(--dial-font);color:var(--dial)}
.rope{fill:none;stroke:var(--ink);stroke-width:4;stroke-linecap:round}
.rope--sec{stroke:var(--accent)}
```
```js
// Verlet rope: N=16 points, root pinned at centre, tip pinned to the time angle unless dragged
for (const p of pts){const vx=(p.x-p.px)*0.98, vy=(p.y-p.py)*0.98+GRAVITY; p.px=p.x;p.py=p.y;p.x+=vx;p.y+=vy;}
for (let k=0;k<20;k++) constrain(pts, SEG_LEN); // distance constraints
if(!dragging) tip.x += (anchor.x-tip.x)*0.18, tip.y += (anchor.y-tip.y)*0.18; // spring back
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 7 | Clean, quiet chrome; the dial numerals are pale and the layout widget-like. |
| Originality | 9 | Rope-physics clock hands are a genuinely new take on a watch face. |
| Usability | 5 | A toy by intent: time is ambiguous mid-play and numerals are low contrast. |
| Craft | 8 | Convincing physics, anchor rings and a consistent pill system. |

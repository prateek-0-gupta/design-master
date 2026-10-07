---
id: insp-ticket-stub
source: inspora
category: Motion
status: analyzed
title: "ticket stub"
creator: "@darel023"
styles: [technical-wireframe, terminal-mono, physical-material, micro-interaction]
patterns: [spring-tilt-card, cursor-follow-light-source, blueprint-annotation-overlay, collectible-stub-reward, live-physics-readout, dimension-callouts, perforated-tear-line]
mode: mixed
palette: ["#3160f8", "#436ef5", "#869ec4", "#e7e9e6", "#ffffff", "#1a2238"]
type_families: ["JetBrains Mono / Geist Mono-style monospace (likely)", "Geist / Inter-style sans (likely)", "handwritten script (Caveat-like)"]
type_class: [mono, neo-grotesk, script]
radius_px: [12, 6, 4]
motion: {durations_s: [0.4, 0.5, 0.17, 0.33, 0.7], easing: [spring-underdamped, ease-out, ease-in-out], loop: false}
scores: {aesthetics: 9, originality: 9, usability: 7, craft: 10}
craft_signals: [spring-constants-printed-on-page, light-icon-orbits-card, dimension-lines-236x292, perforation-dots-at-tear, vertical-issuer-microtext, scanline-texture-on-blue, ordinal-personalised-handwriting]
anti_patterns: [annotation-text-below-contrast, decorative-math-noise-for-lay-users]
---
# ticket stub — @darel023

## 1. Snapshot
- **Subject:** A 42 s, 2778×2012 capture at 120 fps of a personal site's end-of-page reward. A watercolour "ADMIT ONE · CEBU → LONDON" stub, numbered "No. 9,302", tilts on an underdamped spring toward the cursor while a sun icon acts as a moving light source. The stub sits inside a blueprint diagram that prints the physics live.
- **Why it's remarkable:** The page documents its own motion system. Spring constants (k = 237.6, ζ = 7.5, ω = 13.47 rad/s), light timings and live θX/θY readouts are typeset around the object, so the demo is also the spec.

## 2. Composition & layout
- **Full-bleed blue field:** A footer separated by a hairline at y≈1280 (shown) carries "imdaryl.com", "London", Email and X. A row of progress squares runs along the bottom edge.
- **Centre stage:** a dashed bounding box ~860×960 shown (≈1195×1335 source) with crosshair axes labelled −1.8 / +1.8 and "REACH · 120 PX · LET GO BEYOND" above it.
- **The stub:** ~440×510 shown (≈610×710 source). Dimension callouts read "236" (width) and "292" (height), the CSS px size of the stub.
- **Columns:** A left column (x≈63) holds the equations in mono, and a right column (x≈1445) holds live telemetry (θX −16.12°, θY −6.97°, AIM, X, Ẋ, LIGHT 90% 2%, LIT 1.00, "held").
- **Below the stub:** an uppercase mono message in three centred lines, then a white "Claim stub" button (~245×66 shown) and the counter "128 STUBS CLAIMED SO FAR".

## 3. Typography
- **Monospace:** All annotation is uppercase mono with wide tracking (~+0.12 em) at ~16 px shown (≈22 px source). The face is a geometric mono close to JetBrains Mono or Geist Mono, with a slashed or dotted zero visible in "0.70".
- **Stub:**
  - "No." small mono;
  - "9,302" ~48 px bold sans with tight tracking;
  - FROM / ON / AT labels in grey mono, values in black mono;
  - a personal line in a handwritten script ("Back for the 223rd time. Thanks."), ~22 px, Caveat-like;
  - "ISSUED BY IMDARYL.COM" set vertically at the right edge in ~10 px mono.
- **Button:** "Claim stub" in ~26 px medium sans (Geist / Inter-like), in brand blue with a ticket glyph.

## 4. Colour
| Hex | Role | Approx share |
|---|---|---|
| #3160f8 | page field (electric cobalt) | 87% |
| #436ef5 | scanline stripes, dashed rules | 5% |
| #869ec4 | dimmed annotation text and lines | 3% |
| #e7e9e6 / #ffffff | stub paper, button, primary labels | 5% |
| #1a2238 | stub ink | <1% |
| watercolour teal, ochre and pink | illustration only | — |

WCAG checks:
- White on #3160f8: 5.05:1 (pass).
- Light labels #e7e9e6 on blue: 4.13:1 (AA-large only).
- **Dim annotation ≈#9db3fb on blue: 2.47:1 (fails)**, acceptable only as decorative telemetry.
- Button text #3160f8 on white: 5.05:1.
- Stub ink #1a2238 on paper #f7f7f5: 14.72:1.
- Grey field labels ≈#8a8f99 on paper: 3.03:1.

## 5. Depth & material
- **Stub:** a paper card with ~6 px radius, rotated in 3D (perspective visible: the top edge is wider than the bottom when θX is negative). The highlight sweeps across the paper based on the sun icon position (LIGHT 90%).
- **Tear line:** a dotted line between the illustration and the stub half, with two small blue punch circles at the perforation ends.
- **Shadows:** a soft drop shadow shifts opposite to the light, plus a dotted ghost outline of the resting position behind the card.
- **Background:** fine horizontal scanlines (≈4 px period, #436ef5 on #3160f8) give a blueprint or CRT texture.

## 6. Components & patterns
- **Spring tilt:** the cursor within reach (120 px past the stage edge) aims the card, and θ = 10°·x with |x| ≤ 1.8, so the tilt is capped at about 18°.
- **Light source:** a ☼ icon orbits a dotted circle around the stub and follows the cursor. The light is critically damped (T = 0.4 s held, 0.8 s home; lit τ = 0.18 s in, 0.26 s out).
- **Reward mechanic:** "Claim stub" with a social-proof counter ("128 stubs claimed").
- **Personalisation:** the stub number, timestamp ("19:52 · 15 SEPT 2026"), device ("MAC") and visit count ("223rd time") appear to be generated per visitor.

## 7. Motion
Measured profile: 42.07 s at 120 fps, `motion_fraction` 0.25, 29 short segments with a median of 0.33 s. Not a loop.
- **Segment lengths:** Most cluster at 0.17–0.7 s, with a mix of ease-out (peaks 0.04–0.3, e.g. 0.77 s for 0.40 s, peak 0.04) and ease-in (peaks 0.68–0.93). This is consistent with spring release (fast start, oscillating decay) and cursor-led approaches (ramping in).
- **Stated parameters:** On-page constants give ω = 13.47 rad/s, a natural period of about 0.47 s. That matches the measured 0.4–0.5 s segments, the decay of one tilt overshoot.
- **Energy:** Low mean energy (0.25) because only the card and the light icon move on a static field.
- **Settling:** Light settles in 0.8 s "home" after release (stated). The frames show the sun returning to the top right of the circle between 21 s and 25.7 s.
- **Fade-out:** At 39.73 s the annotations fade to about 30% opacity (an idle or dim state) while the card stays fully opaque.

## 8. Brand system
n/a — not a brand system. Identity cues:
- a cobalt blueprint field;
- mono engineering annotation;
- watercolour travel imagery (Cebu to London, the author's journey);
- the "imdaryl.com" signature on the stub.

## 9. UX
- **Strengths:**
  - A delightful, low-stakes reward at the end of reading.
  - The tilt is capped (±18°), so text stays legible.
  - A single clear CTA with social proof.
- **Risks:**
  - The physics overlay is noise for non-designers.
  - Much of the annotation fails contrast.
  - A touch-device fallback for cursor reach is not shown.

## 10. Craft signals
- The real spring constants are printed and match the measured ~0.47 s oscillation period.
- Dimension lines report the true stub size (236 × 292).
- The light position drives both the highlight and the shadow offset.
- Perforation dots and two punch circles sit at the tear line.
- Vertical "ISSUED BY IMDARYL.COM" microtext runs along the stub edge.
- A dotted ghost of the rest position stays behind the tilted card.
- A 4 px scanline texture adds grain to a flat blue.
- A handwritten line uses the visitor's ordinal count.

## 11. Reproduction recipe
```css
:root{--field:#3160f8;--rule:#436ef5;--dim:#869ec4;--paper:#f7f7f5;--ink:#1a2238;
  --mono:"Geist Mono","JetBrains Mono",ui-monospace,monospace;--sans:"Geist","Inter",sans-serif}
body{background:var(--field) repeating-linear-gradient(0deg,transparent 0 3px,rgba(255,255,255,.04) 3px 4px)}
.note{font:500 11px/1.6 var(--mono);letter-spacing:.12em;text-transform:uppercase;color:var(--dim)}
.stage{border:1px dashed rgba(255,255,255,.5);perspective:900px}
.stub{width:236px;height:292px;border-radius:6px;background:var(--paper);color:var(--ink);
  transform:rotateX(var(--tx)) rotateY(var(--ty));box-shadow:calc(var(--lx)*-12px) 18px 30px rgba(10,20,80,.35)}
.tear{border-top:1px dotted #b9c0cc}
.cta{background:#fff;color:var(--field);border-radius:12px;padding:12px 22px;font:500 16px var(--sans)}
```
```js
// Underdamped spring: x'' = -k x - 2ζ x', k=237.6, ζ=7.5 → ω≈13.47 rad/s
const k=237.6, z=7.5; let x=0, v=0;
function step(dt, target){ const a = -k*(x-target) - 2*z*v; v += a*dt; x += v*dt; el.style.setProperty('--ty', (10*x)+'deg'); }
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 9 | The cobalt blueprint against a watercolour paper stub is a striking, cohesive contrast. |
| Originality | 9 | A self-documenting physics demo combined with a collectible reward is a new idea. |
| Usability | 7 | The CTA is clear and the tilt capped. The annotations fail contrast and touch behaviour is unclear. |
| Craft | 10 | Stated constants match the measured timing. Perforation, microtext and the light-linked shadow are exemplary. |

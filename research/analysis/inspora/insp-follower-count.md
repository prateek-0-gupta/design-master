---
id: insp-follower-count
source: inspora
category: Motion
status: analyzed
title: "Follower Count"
creator: "@AdityaSur11"
styles: [photo-led, micro-interaction, minimal-swiss, x-data-as-crowd]
patterns: [tick-ruler-scrubber, value-bubble-above-handle, quantity-visualised-as-people, crowd-forms-heart-shape, tabular-mono-counter, grab-cursor-drag]
mode: light
palette: ["#fefefe", "#1c1c1c", "#d9d9d9", "#7c5cff", "#c5b4a5", "#373030", "#5b463b", "#414142"]
type_families: ["JetBrains Mono / SF Mono-style monospace (likely)"]
type_class: [mono]
radius_px: [9999]
motion: {durations_s: [0.37, 0.2, 0.33, 0.47, 0.4, 0.53, 1.47], easing: [ease-out, ease-in-out, ease-in], loop: false}
scores: {aesthetics: 7, originality: 8, usability: 6, craft: 7}
craft_signals: [ticks-fade-toward-ends, bubble-scales-with-value-magnitude, mono-thousands-separator, crowd-depth-sorted-by-y, heart-silhouette-at-max, accent-tick-at-handle]
anti_patterns: [scrubber-ticks-near-invisible, non-linear-value-mapping-unexplained, ai-crowd-repetition]
---
# Follower Count — @AdityaSur11

## 1. Snapshot
- **Subject:** An 18.9 s, 60 fps, 2160×2160 clip of a horizontal tick-ruler slider. Dragging it changes a counter bubble (0 → 1 → 2 → 4 → 970 → 5,000), and above it a crowd of cut-out photoreal people appears in the matching number. Small values show individuals. At 5,000 the crowd arranges itself into a giant heart.
- **Why it's remarkable:** It makes an abstract metric (followers) tangible as bodies. The crowd's silhouette changes meaning at the top of the range (heart = love/fame), so the visualisation carries emotion as well as quantity.

## 2. Composition & layout
- Everything is centred on a white field.
- **Slider:** a ruler of about 9 vertical ticks (about 3×55 px at 2160 scale, roughly 50 px pitch) centred at y≈1240.
- **Counter:** a black pill (about 170×55 px) about 70 px above the handle, which follows it.
- **Crowd:** sits above the slider. It grows from a single 270 px-tall figure (1 person) to a heart about 1700 px wide spanning about 80% of the canvas at 5,000. At 970 it forms a lozenge or isometric plaza (about 1000 px wide).
- **Scale behaviour:** the whole UI zooms. At 3.15 s, with 2 people, the slider and counter are rendered about 1.6× larger than at 1.05 s, so the camera is closer for small numbers and pulls back as the crowd grows.

## 3. Typography
- One typeface: a monospace (SF Mono or JetBrains Mono-like) in the counter, about 32 px at capture (about 13–15 px at 1×), white on black, with thousands separators ("5,000"). Mono keeps the bubble width stable as digits change.
- There is no other text, no labels or units. The crowd is the label.

## 4. Colour
| Hex | Role | Approx share (key frame) |
|---|---|---|
| #fefefe | field | 76% |
| #1c1c1c | counter pill | <0.5% |
| #d9d9d9 | ruler ticks | <0.5% |
| #7c5cff | active tick at handle (thin violet line, visible at 17.87 s) | <0.1% |
| #c5b4a5 / #afa599 | beige coats (crowd) | 3.4% |
| #373030 / #414142 | navy/charcoal jackets, hair | 3.4% |
| #5b463b | brown trousers | 1.5% |

The crowd's palette is a muted earthy set (sage green, navy, beige, brown), so thousands of figures form a calm texture rather than noise.

WCAG checks:
- Counter #f2f2f2 on #1c1c1c is 15.22:1.
- Ruler ticks #d9d9d9 on white are **1.4:1**, too faint for a non-text UI control (WCAG 1.4.11 asks for 3:1).
- The violet active tick is 4.31:1.

## 5. Depth & material
- The crowd is made of photoreal cut-out figures (AI or stock renders) with no shadows on the white field. They are layered by y-position: lower figures are drawn larger and in front, which gives a convincing 3/4 isometric crowd with front rows at full size and back rows smaller.
- The UI is flat: a solid pill and hairline ticks.

## 6. Components & patterns
- **Tick-ruler slider:** ticks fade toward both ends (opacity falls off about 3 ticks from the handle), implying infinite scroll. The handle is shown by a grab-hand cursor and a violet tick.
- **Value bubble:** a pill tooltip that tracks the handle.
- **Quantity-as-figures:** the count maps to visible people. It is clearly non-linear at the top: "5,000" shows only around 1,000–1,500 figures, so it is sampled or capped.
- **Shape morph:** the crowd is a cluster for small numbers, a diamond plaza at 970 and a heart at 5,000.

## 7. Motion
- **Measured:** 18.92 s, motion fraction 0.26, with 15 short segments (median **0.27 s**) that correspond to drag steps and crowd spawns. Representative segments:
  - 1.67–2.03 s (0.37 s, ease-out): the first figure appears.
  - 3.73–4.07 s (0.33 s, ease-out): people are removed.
  - 8.73–9.20 s (**0.47 s**, symmetric, highest variance, CV 1.45): the jump to 5,000. The heart crowd floods in.
  - 9.33–9.73 s (0.40 s, symmetric): the crowd settles.
  - 13.63–14.17 s (0.53 s, ease-out): back down to 1.
  - 14.70–16.17 s (**1.47 s**, ease-in, peak 0.72): the long build back to the full heart.
- `seamless_loop_likely: false` (diff 41.51).
- **From frames (estimate):** figures pop in with a quick fade and scale-up (about 0.2 s). The camera zoom between small and large counts eases smoothly over about 0.4–0.5 s. The counter updates per frame while dragging.

## 8. Brand system
n/a — not a brand system. The identity cue is "people, not numbers": a human-scale data metaphor for a social or creator platform.

## 9. UX
- **Strength:** an instantly emotional understanding of scale (1 vs 970 vs 5,000), useful for creator onboarding or goal-setting.
- **Problems:**
  - The ruler is nearly invisible (1.4:1).
  - The numeric mapping between ticks is not shown (ticks have no labels, and the step from 4 to 970 to 5,000 suggests a logarithmic scale).
  - The visual count does not literally equal the number.
  - On mobile, rendering thousands of photo sprites is costly.
- The bubble is the only precise readout. The mono figures help here.

## 10. Craft signals
- Ruler ticks fade in opacity with distance from the handle, an endless-dial cue.
- The counter pill's width stays steady because digits are monospaced. A comma separator appears from 1,000 upward.
- Crowd figures are depth-sorted by y and scaled, with the front row larger, giving a consistent isometric perspective.
- The camera zoom ties to magnitude: small numbers get a close-up, large numbers a wide shot.
- The heart shape appears only at the maximum, an emotional "reward state".
- The active tick is a single violet line, the only chromatic UI accent.

## 11. Reproduction recipe
```css
:root{--bg:#fefefe;--pill:#1c1c1c;--tick:#d9d9d9;--accent:#7c5cff;--mono:"JetBrains Mono",ui-monospace,monospace}
.ruler{display:flex;gap:22px;align-items:end;height:28px;
  -webkit-mask:linear-gradient(90deg,transparent,#000 30%,#000 70%,transparent)}
.ruler i{width:1.5px;height:24px;background:var(--tick);border-radius:1px}
.ruler i.active{background:var(--accent);height:28px}
.bubble{font:500 14px/1 var(--mono);font-variant-numeric:tabular-nums;color:#f2f2f2;background:var(--pill);
  padding:6px 12px;border-radius:9999px;transform:translateX(var(--x));transition:transform .12s ease-out}
.person{position:absolute;left:var(--px);top:var(--py);height:calc(120px * var(--s));z-index:var(--py-int);
  animation:spawn .22s cubic-bezier(.2,.8,.2,1) both}
@keyframes spawn{from{opacity:0;transform:translateY(6px) scale(.9)}}
.stage{transition:transform .45s cubic-bezier(.65,0,.35,1);transform:scale(var(--zoom))} /* zoom = f(log10(count)) */
```
```js
// map slider to followers logarithmically; sample sprites; place on heart curve at max
const count = Math.round(10 ** (t * Math.log10(5000)));
const visible = Math.min(count, 1200);
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 7 | Clean white stage and a striking heart crowd, though the repeated AI figures look samey up close. |
| Originality | 8 | Followers rendered as an actual crowd that forms a heart is a memorable, novel data metaphor. |
| Usability | 6 | Emotional clarity is high, but the ruler is nearly invisible and the scale mapping unclear. |
| Craft | 7 | Depth sorting, mono counter and magnitude-linked zoom work well. Figure count does not equal the value. |

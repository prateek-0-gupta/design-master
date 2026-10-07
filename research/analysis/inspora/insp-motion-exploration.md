---
id: insp-motion-exploration
source: inspora
category: Branding
status: analyzed
title: "Personal brand — motion exploration"
creator: "@iamnotsrc"
styles: [kinetic-type, photo-led, grain-noise, minimal-swiss]
patterns: [rotating-drum-logo-reel, portfolio-marks-as-faces, motion-blur-transitions, shrink-to-wordmark-resolve, image-filled-squircle]
mode: light
palette: ["#ffffff", "#111111", "#a395f1", "#f17c8b", "#da6096", "#5fb7c0", "#6e8a3a"]
type_families: ["Neue Haas Grotesk Display / Inter Display-style neo-grotesk (likely)"]
type_class: [neo-grotesk]
radius_px: [90]
motion: {durations_s: [3.28, 0.6], easing: [ease-out, ease-in], loop: true}
scores: {aesthetics: 8, originality: 8, usability: 6, craft: 7}
craft_signals: [barrel-distortion-sells-cylinder-rotation, per-face-photo-background, grain-overlay-on-faces, monotone-white-marks-unify-portfolio, progressive-scale-down-before-resolve, all-lowercase-tight-wordmark]
anti_patterns: [white-marks-on-light-faces-low-contrast, blur-frames-hide-marks]
---
# Personal brand — motion exploration — @iamnotsrc

## 1. Snapshot
- **Subject:** A 6.1 s, 1920×1080 (25 fps) logo reel for a designer's personal brand.
  - A squircle tile spins like a rotating drum or prism.
  - Each face shows a different client mark (white) over a full-bleed scenic image: green hills, mossy rock, a steel bridge, purple-to-coral canyon, blue sky.
  - It shrinks as it spins, then resolves to the wordmark "iamnotsrc".
- **Why it's remarkable:** A portfolio of logos becomes a single object. The drum metaphor presents many marks as faces of one identity, ending on the designer's name.

## 2. Composition & layout
- Everything is dead centre on #ffffff.
- **Tile size:** about 750 px wide at 0.34 s, about 510 px at 3.05 s and about 450 px at 3.73 s. That is a steady shrink of about 40% over 3.4 s.
- **Shape:** the tile is taller than wide (about 0.9:1 at the key frame, 500×560 px) with a radius of about 90 px. The side edges bulge (barrel distortion) as faces rotate past, which sells the cylinder.
- **Marks:** each sits centred at about 40% of the tile width.
- **Wordmark:** "iamnotsrc", about 390 px wide, sits on the frame's centre line and is held for the last about 1.8 s.

## 3. Typography
- The wordmark is all lowercase, in a neo-grotesk (Neue Haas Display or Inter Display-like) at about 80 px, weight about 500–600, with tight tracking (about −0.04 em). The "m" and "n" nearly touch.
- No other type appears. The client marks are geometric line icons with consistent stroke (about 22 px at a 500 px tile), rounded caps, and white fill.

## 4. Colour
| Hex | Role | Share (key frame) |
|---|---|---|
| #ffffff | canvas; all marks | 87% |
| #111111 | wordmark | — |
| #a395f1 / #9288ea | lavender sky face | 4% |
| #f17c8b / #da6096 / #b264ac | coral/magenta canyon rocks | 3% |
| #5fb7c0 (est., 0.34 s) | teal sky face | — |
| #6e8a3a (est., 0.34 s) | hill green | — |

WCAG / non-text checks:
- The white sun mark on lavender (#a395f1) is 2.58:1, and on coral (#f17c8b) it is 2.63:1. Both are below 3:1, so the mark's legibility depends on its stroke weight and the darker earth/rock faces.
- The wordmark #111111 on white is 18.88:1.

Strategy: a neutral white world. All colour lives inside the spinning photo faces and then drains away for the black-on-white resolve.

## 5. Depth & material
- **The drum:**
  - a 3D cylinder with photographic textures;
  - soft vertical shading and a slight highlight at the side curvature;
  - a faint soft reflection or ground glow below (about 20 px blurred band at the bottom edge).
- A fine film grain is visible on the lavender face (about 1 px noise).
- Mid-spin frames (1.02 s, 1.69 s, 3.73 s) show strong vertical motion blur, which reads as fast rotation.

## 6. Components & patterns
- **Faces seen, in order:**
  1. cloud/spade mark on hills;
  2. shield/crest mark on rock;
  3. interlocked-S mark on forest;
  4. brace/hex mark on a bridge;
  5. sun mark on a canyon;
  6. door/columns mark on sky.
- The marks are white-only with no colour, so the portfolio reads as one family.
- The resolve swaps the object for type with no morph: a cut or fade to the wordmark.

## 7. Motion
These figures are measured: 6.10 s at 25 fps, motion_fraction 0.60, 2 segments, `seamless_loop_likely: true` (first-to-last difference 1.22).
- **Segment 1:** 0.20–3.48 s (3.28 s), peak_at 0.01, so a hard ease-out. The drum starts at top speed and decelerates through about six faces while shrinking.
- **Segment 2:** 3.64–4.24 s (0.60 s), peak_at 0.97, so an ease-in. The final whip accelerates into the exit, and the tile disappears into the wordmark.
- **Hold:** about 4.3–6.1 s on the static wordmark (about 1.8 s).

Estimated face dwell is about 0.55–0.7 s each, getting longer as the spin slows.

## 8. Brand system
n/a — not a full brand system; it is a personal-brand sting. Identity cues: the lowercase tight wordmark, "many faces, one person" (the drum), and a photo-plus-white-mark treatment for portfolio pieces.

## 9. UX
- As a sting it is clear: show the work, then the name.
- The marks are hard to identify during blur frames, and three of the six faces are mostly motion blur in sampled frames. Each face gets under 0.7 s.
- The loop is seamless (it starts and ends on white), so it works as an autoplaying header.

## 10. Craft signals
- The side edges bulge as faces rotate (barrel distortion), a physically correct cylinder cue.
- Every client mark is recoloured pure white at the same optical size (about 40% of tile width).
- Each face has its own scenic photograph matched to the mark (hills/cloud, sky/door).
- The tile scale decreases continuously (about 750 → 450 px) as speed decays, so the energy drops together.
- Grain on the faces prevents banding in the lavender gradient.

## 11. Reproduction recipe
```css
:root{--bg:#fff;--ink:#111;--r-tile:90px}
.stage{display:grid;place-items:center;height:100vh;background:var(--bg);perspective:1400px}
.drum{width:500px;height:560px;transform-style:preserve-3d;
  animation:spin 3.28s cubic-bezier(.05,.75,.25,1) .2s both, shrink 3.28s cubic-bezier(.05,.75,.25,1) .2s both}
.face{position:absolute;inset:0;border-radius:var(--r-tile);background-size:cover;display:grid;place-items:center;backface-visibility:hidden}
.face:nth-child(n){transform:rotateY(calc(var(--i)*60deg)) translateZ(433px)}  /* 6 faces */
.face svg{width:40%;fill:none;stroke:#fff;stroke-width:22;stroke-linecap:round}
@keyframes spin{from{transform:rotateY(0)}to{transform:rotateY(-1800deg)}}
@keyframes shrink{from{scale:1.5}to{scale:.9}}
.exit{animation:whip .6s cubic-bezier(.7,0,.95,.4) 3.64s forwards}
@keyframes whip{to{transform:rotateY(-2160deg) scale(.2);opacity:0}}
.wordmark{font:550 80px/1 "Neue Haas Grotesk Display","Inter Display",sans-serif;letter-spacing:-.04em;color:var(--ink)}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Lush photo faces against pure white, and a crisp wordmark resolve. |
| Originality | 8 | A logo-portfolio-as-spinning-drum is a memorable, fitting metaphor. |
| Usability | 6 | Marks fly by in under 0.7 s and some white marks sit on light faces at about 2.6:1. |
| Craft | 7 | Convincing cylinder distortion and measured easing; the transition into type is abrupt. |

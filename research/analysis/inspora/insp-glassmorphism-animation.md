---
id: insp-glassmorphism-animation
source: inspora
category: Web
status: analyzed
title: "glassmorphism animation"
creator: "@DesignGabor"
styles: [glassmorphism, aurora-glow, minimal-swiss, micro-interaction]
patterns: [cursor-following-colour-blob, frosted-tile-grid-reveal, white-on-light-low-key-hero, colour-cycling-spotlight, blocky-logomark-shape]
mode: light
palette: ["#d3d3d3", "#ffffff", "#da852c", "#e4af31", "#e6d768", "#d7b69a", "#e9e8e8"]
type_families: ["Inter / SF Pro (likely)"]
type_class: [neo-grotesk]
radius_px: [22, 40]
motion: {durations_s: [0.77, 0.7, 1.03, 0.67, 0.8, 0.9], easing: [ease-in-out, ease-out, linear], loop: true}
scores: {aesthetics: 8, originality: 7, usability: 3, craft: 6}
craft_signals: [tile-grid-only-visible-where-lit, hue-shifts-orange-to-lime-over-time, lagged-follow-of-cursor, tiles-tinted-by-blur-not-fill, white-shape-sits-above-glass]
anti_patterns: [white-text-on-light-grey-illegible, recording-watermark-in-shot, hidden-content-until-hover]
---
# glassmorphism animation — @DesignGabor

## 1. Snapshot
- **Subject:** A 13.26 s, 1280×720 screen recording of a minimal light-grey hero (#d3d3d3) with a white "R" logo top-left, a large white blocky logomark shape on the right, and a small white paragraph. A glowing orange/yellow/lime colour blob trails the cursor, seen through a hidden grid of frosted glass tiles that become visible only where the light passes.
- **Why it's remarkable:** The glass grid is invisible until lit. The cursor acts as a flashlight behind frosted glass, so the interface reveals its material only through interaction.

## 2. Composition & layout
- **Canvas:** an empty #d3d3d3 field covering about 75% of the frame.
- **Brand elements:**
  - logo "R" (about 24 px bold white) at x≈120, y≈90 in sheet scale (about x≈240, y≈170 in the key frame, where it is overlapped by the grid);
  - a "CapCut" watermark at the bottom-left (a recording artefact);
  - the white blocky shape on the right, about 450×430 px, built from rounded rectangles (radius about 40 px), like an "S" or tetromino;
  - a four-line paragraph at about 13 px below it (x≈843, y≈620).
- **Grid:** square tiles of about 130 px with a ~4 px gap and ~22 px radius, covering the whole viewport. Typically only a 3×3 to 4×4 neighbourhood is visible around the cursor.

## 3. Typography
- A neo-grotesk (Inter / SF Pro). The "R" mark is bold. The body is regular at about 13 px with leading of about 1.25, in white.
- The type is nearly invisible on the grey, an aesthetic choice that fails as content.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #d3d3d3 | canvas | 75% |
| #ffffff | logomark shape, text | 9% |
| #da852c | orange blob core | 4% |
| #e4af31 / #e6d768 | yellow halo | 4.5% |
| #d7b69a / #d8cdaa | tinted glass edges | 5.6% |
| lime (~#9ccc1a, frames 8.10–11.05 s) | later hue phase | — |

WCAG checks:
- White text on #d3d3d3 is **1.5:1**.
- White "R" on the orange #da852c is 2.85:1, and on yellow #e4af31 it is 2.0:1.

All body text is unreadable; this is a mood piece, not usable copy.

## 5. Depth & material
- **Tiles:** frosted glass, each with a heavy backdrop blur (about 30 px) over a coloured radial blob. Each tile shows a lighter inner rim (about 1 px white at 40%) and a darker edge where the colour pools, so tiles read as thick, rounded glass bricks.
- **Spatial cues:**
  - The colour saturates at the blob centre (deep orange) and fades through peach to clear at the edges, making tiles disappear into the canvas.
  - The white logomark sits above the glass plane: it occludes the tiles cleanly (frame 5.16 s) and has a soft grey shadow.

## 6. Components & patterns
- A cursor-reactive spotlight under a glass grid.
- An oversized brand shape as the hero object.
- A minimal top-left mark plus a supporting paragraph (a portfolio/agency hero pattern).

## 7. Motion
Measured: 13.26 s at 30 fps, 9 segments, motion fraction 0.43, `seamless_loop_likely: true`, median segment 0.7 s.

| Segment | Duration | Shape (peak_at) |
|---|---|---|
| 2.23–3.00 s | 0.77 s | symmetric (0.46) |
| 3.43–4.13 s | 0.7 s | ease-out (0.21) |
| 4.57–5.60 s | 1.03 s | continuous/linear |
| 5.97–6.63 s | 0.67 s | symmetric |
| 6.87–7.67 s | 0.8 s | symmetric |
| 9.40–10.30 s | 0.9 s | ease-out (0.24) |

The blob follows the cursor with a noticeable lag. In frame 0.74 s the cursor is at the grid's left edge while the colour mass is centred about 1 tile away, which implies a spring or lerp follow (about 0.1–0.15 per frame).

The hue drifts over time: orange/yellow (0–6.6 s), yellow-olive (5.16–9.58 s), lime/green (8.10–11.05 s), then back to yellow (12.52 s). That is a slow hue cycle of about 10–12 s.

## 8. Brand system
n/a — not a brand system. Identity cues: the white "R" monogram and a chunky rounded-block logomark, with warm citrus light as the brand energy.

## 9. UX
- **Strengths:** Delightful discovery and a strong sense of material; the cursor feedback is immediate.
- **Risks:**
  - The content (paragraph, logo) is illegible.
  - Nothing is visible without a pointer, which leaves touch devices with a blank grey page.
  - There is no reduced-motion fallback.
  - The CapCut watermark shows this is a recording, not a shipped piece.

## 10. Craft signals
- Tiles are not drawn at all outside the lit zone; their edges are revealed only by the blurred colour behind them.
- Each tile has a lighter rim and darker pooling at its lower edges (thick-glass refraction cue).
- The colour blob lags the cursor (smoothed follow), not pinned to it.
- The hue cycles slowly from orange through yellow to lime over about 10 s, independent of the cursor.
- The white logomark occludes the glass grid with a soft shadow, establishing z-order.

## 11. Reproduction recipe
```html
<div class="stage"><div class="blob"></div><div class="grid"><!-- 10x6 .tile --></div></div>
```
```css
:root{--bg:#d3d3d3;--tile:130px;--gap:4px;--r:22px}
.stage{position:relative;background:var(--bg);overflow:hidden;height:100vh}
.blob{position:absolute;width:520px;height:520px;border-radius:50%;translate:-50% -50%;
  left:var(--x);top:var(--y);background:radial-gradient(circle,#da852c 0%,#e4af31 35%,#e6d768 55%,transparent 70%);
  animation:hue 11s linear infinite}
@keyframes hue{50%{filter:hue-rotate(40deg)}}
.grid{position:absolute;inset:0;display:grid;grid-template-columns:repeat(auto-fill,var(--tile));gap:var(--gap)}
.tile{aspect-ratio:1;border-radius:var(--r);backdrop-filter:blur(30px) saturate(160%);
  background:rgba(211,211,211,.35);box-shadow:inset 0 1px 0 rgba(255,255,255,.4),inset 0 -6px 12px rgba(0,0,0,.06)}
@media (prefers-reduced-motion:reduce){.blob{animation:none}}
```
```js
let x=0,y=0,tx=0,ty=0;addEventListener('pointermove',e=>{tx=e.clientX;ty=e.clientY});
(function f(){x+=(tx-x)*.12;y+=(ty-y)*.12;stage.style.setProperty('--x',x+'px');stage.style.setProperty('--y',y+'px');requestAnimationFrame(f)})();
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Beautiful glowing citrus glass against calm grey. |
| Originality | 7 | Cursor spotlight under a glass grid is a known trick, done with a nice hue cycle and invisible tiles. |
| Usability | 3 | Text is illegible (1.5:1) and the page is empty without a pointer. |
| Craft | 6 | Convincing glass rendering and smooth lag; the watermark and type neglect lower it. |

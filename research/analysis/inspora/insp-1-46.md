---
id: insp-1-46
source: inspora
category: Motion
status: analyzed
title: "Grid Reveal animation"
creator: "@SwamiMalode"
styles: [dark-premium, micro-interaction, minimal-swiss]
patterns: [ai-generation-loading-state, tile-grid-skeleton, staged-status-labels, mosaic-reveal, shimmer-text, disabled-button-during-task]
mode: dark
palette: ["#101010", "#1b1b1b", "#252525", "#2b2b2b", "#ef5a2c", "#f49d7c", "#fadacd", "#844d3d"]
type_families: ["Inter (likely)"]
type_class: [neo-grotesk]
radius_px: [16, 9999, 6]
motion: {durations_s: [0.33, 0.43, 0.4, 0.37], easing: [ease-out, ease-in-out, ease-in], loop: false}
scores: {aesthetics: 7, originality: 7, usability: 8, craft: 8}
craft_signals: [two-stage-grid-2x2-then-8x8, random-tile-luminance-flicker, tile-wise-image-reveal, shimmer-highlight-in-status-text, button-label-mirrors-state, status-chip-inside-frame]
anti_patterns: [disabled-label-low-contrast, no-progress-estimate]
---
# Grid Reveal animation — @SwamiMalode

## 1. Snapshot
- **Subject:** A 1254×806, 13.8 s, 30 fps capture of an AI image-generation card. Pressing "Generate" collapses the current image into a dark 2×2 grid ("Starting to generate"). The grid then subdivides into an 8×8 mosaic of flickering grey tiles ("Creating image"), and the new orange-sky image resolves tile by tile. The cycle runs twice.
- **Why it's remarkable:** The skeleton is spatially honest. The tiles are the same grid the image will appear through, so the loading state *previews the reveal mechanism* and gives a sense of "rendering in blocks" that matches how users imagine diffusion working.

## 2. Composition & layout
- **Layout:** a single centred stack on #101010.
- **Image frame:** ≈383×383 px (x≈436–819, y≈183–566), radius ≈16 px.
- **Generate button:** a pill ≈156×52 px centred ≈30 px below the frame.
- **Status chip:** sits inside the frame, bottom-left, ≈18 px inset ("Creating image").
- **Mosaic:** 8×8 tiles of ≈46 px with ≈2 px gutters. The starting state is a 2×2 split with hairline cross gutters (2.29 s).

## 3. Typography
- **Typeface:** Inter-like neo-grotesk.
- **Button:** ≈19 px medium. Light grey #c8c8c8 for "Generate"; dimmed ≈#6a6a6a for "Generating" while busy.
- **Status chip:** ≈16 px in light grey on a near-black pill. It has a **shimmer**: a brighter band sweeps across the letters (the frame at 3.82 s shows "im" brighter than the surrounding text).
- **Copy:** progresses "Starting to generate" → "Creating image". Two staged messages give the impression of a pipeline.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #101010 | page | 84% |
| #1b1b1b / #252525 | button and chip fills, darkest tiles | ~1% |
| #2b2b2b–#333 | tile luminance range (random) | during load |
| #ef5a2c / #ef6d44 | generated sky, saturated top | 6% |
| #f49d7c / #f7af94 / #fadacd | sky gradient to haze | 6% |
| #844d3d | tile-seam shadows during reveal | 0.6% |

WCAG checks:
- Status text ≈#d4d4d4 on chip #1b1b1b: **11.62:1**.
- "Generate" #c8c8c8 on #262626: 9.05:1.
- "Generating" (disabled) ≈#6a6a6a on #232323: **2.91:1**. This is acceptable for a disabled control, but the label also carries status.

The UI is achromatic, so all colour arrives with the generated content.

## 5. Depth & material
- **Surfaces:** flat. The frame and button are subtle lifts (#1b1b1b–#262626 on #101010) with no shadows.
- **Tiles:** have their own small radius (≈4–6 px) and step in luminance. The texture reads like a low-res noise field, a nod to latent-space noise.
- **Reveal:** tile seams are briefly visible as faint banding in the key frame, which emphasises the block-wise rendering.

## 6. Components & patterns
- **Generation card:** frame, in-frame status chip and primary pill button.
- **Skeleton:** a mosaic loader whose tiles vary in luminance over time (a Perlin-like flicker) rather than a single sweeping shimmer gradient.
- **Busy state:** the button relabels to "Generating" and is disabled (the cursor shows a ⊘ not-allowed badge at 2.29 s and 8.41 s).
- **Reveal:** content fades in per tile with staggered delays.

## 7. Motion
- **Measured:** 13.77 s at 30 fps. motion_fraction 0.11. Four segments:
  - 0.40–0.73 s (**0.33 s**, peak 0.25, ease-out): the image collapsing into the dark 2×2 grid after the click;
  - 5.63–6.07 s (**0.43 s**, symmetric): the first mosaic reveal;
  - 11.70–12.10 s (**0.40 s**, peak 0.71, ease-in);
  - 13.37–13.73 s (0.37 s, ease-in): the second cycle's reveal and settle.
- **Ambient flicker:** the tile flicker between segments is below the 0.35 threshold, so it is a gentle shimmer, not busy noise.
- seamless_loop_likely false (first/last diff 21.4).
- **From frames (estimates):**
  - Generation takes ≈5.5 s per cycle (click ≈0.5 s → image ≈6.0 s; click ≈7.0 s → image ≈12.0 s).
  - About 1.5 s is spent in the 2×2 "Starting" stage and about 4 s in the 8×8 "Creating" stage.

## 8. Brand system
n/a — not a brand system.

## 9. UX
- **Strengths:**
  - Clear three-state feedback: idle, busy (with staged copy) and done.
  - The disabled button prevents double submission.
  - The loader occupies the exact frame of the result, so there is no layout shift.
- **Risks:**
  - There is no progress estimate or cancel option.
  - The disabled label's contrast is low.
  - A 64-tile flicker may need a reduced-motion alternative.
  - The previous image is discarded immediately; keeping it dimmed until the new one arrives would aid comparison.

## 10. Craft signals
- The loader has two resolutions: a 2×2 grid at "Starting to generate", subdividing to 8×8 at "Creating image".
- Tile luminance varies randomly within #252525–#333 and changes over time.
- The final image is revealed through the same 8×8 grid, with seams visible mid-reveal.
- A shimmer highlight travels through the status chip's letters.
- The button text changes "Generate" → "Generating" and greys out, with a not-allowed cursor.
- The status chip sits inside the frame, so loader and result share one footprint.

## 11. Reproduction recipe
```css
:root{--page:#101010;--surface:#1b1b1b;--tile-a:#252525;--tile-b:#333;--text:#d4d4d4}
.frame{position:relative;width:384px;aspect-ratio:1;border-radius:16px;overflow:hidden;
  display:grid;grid-template-columns:repeat(var(--n,8),1fr);gap:2px;background:var(--page)}
.tile{border-radius:5px;background:var(--tile-a);animation:flick 1.6s ease-in-out infinite;animation-delay:calc(var(--r)*-1.6s)}
@keyframes flick{50%{background:var(--tile-b)}}
.frame.revealing .tile{background-image:var(--img);background-size:384px 384px;
  background-position:calc(var(--x)*-48px) calc(var(--y)*-48px);
  animation:show .4s cubic-bezier(.2,.8,.2,1) both;animation-delay:calc(var(--r)*.4s)}
@keyframes show{from{opacity:0;filter:brightness(.4)}to{opacity:1}}
.chip{position:absolute;left:18px;bottom:18px;padding:6px 12px;border-radius:9999px;background:#1b1b1b;
  font:400 14px Inter;color:transparent;background-clip:text;-webkit-background-clip:text;
  background-image:linear-gradient(90deg,#8a8a8a 40%,#fff 50%,#8a8a8a 60%);background-size:200% 100%;
  animation:shine 1.8s linear infinite}
@keyframes shine{to{background-position:-200% 0}}
button[disabled]{color:#6a6a6a;cursor:not-allowed}
```
(Set `--r` to a random 0–1 per tile and `--x`/`--y` to the tile's column and row; start with `--n:2`, then switch to `--n:8`.)

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 7 | Tidy dark shell; the orange result pops; tiles are subtle. |
| Originality | 7 | A mosaic skeleton that is also the reveal grid is a clever twist on standard shimmer loaders. |
| Usability | 8 | Clear staged states, no layout shift, double-submit prevention; no progress or cancel. |
| Craft | 8 | Two-stage grid, shimmer text and consistent radii are carefully considered. |

---
id: insp-run-to-the-hills
source: inspora
category: Illustration
status: analyzed
title: "run to the hills"
creator: "cem hasimi"
styles: [generative-particle, maximalist-color, playful-rounded, x-pointillist-landscape]
patterns: [outline-figure-over-texture, foreground-scale-pass, dotted-terrain-bands, black-sky-negative-space, leap-exit-beat, dot-size-depth-cue]
mode: dark
palette: ["#000113", "#2a9350", "#bf6891", "#206486", "#866975", "#19364c", "#ffffff"]
type_families: []
type_class: []
radius_px: []
motion: {durations_s: [4.84], easing: [ease-in], loop: false}
scores: {aesthetics: 8, originality: 7, usability: 5, craft: 7}
craft_signals: [figure-stroke-scales-with-proximity, dot-size-gradient-1-to-40px, flowers-only-in-foreground, black-river-as-path, hill-bands-by-hue, leap-silhouette-against-black-sky]
anti_patterns: [figure-crosses-yellow-dots-1-6-to-1, loop-seam-jump]
---
# run to the hills — cem hasimi

## 1. Snapshot
- **Subject:** A 5.0 s, 1000×562 (16:9), 25 fps generative-art clip. A thick white outline figure runs past the camera into a pointillist flower meadow, grows to fill the lower frame, then leaps into the black sky and disappears.
- **Why it's remarkable:** It is a single-shot storytelling beat (approach, pass, leap, gone) done with a dot field and one hand-drawn outline. Dot size alone does all the depth work, from ~2 px far hills to ~40 px foreground blossoms.

## 2. Composition & layout
- **Sky:** pure near-black (#000113), about the top 30% (y 0–150). A black void separates sky from land.
- **Hills:** two hill masses converge to a V at about x 560, y 240. Hue bands (pink/magenta, yellow, green, blue) run along the contours in strips ~25–40 px thick.
- **River:** a black, dot-free channel sweeps from the left edge into the V, a leading line pointing at the horizon where the figure leaps.
- **Meadow:** the foreground meadow rises diagonally from bottom-left to the right edge, so the frame divides along a ~25° diagonal.
- **Figure scale:** it enters at the bottom-centre (~70 px tall at 0.83 s), grows to ~320 px at 3.06 s (exceeding the frame) and appears ~95 px wide mid-air at 4.17 s, centred over the horizon V.

## 3. Typography
None.

## 4. Colour
| Hex | Role | Share (key) |
|---|---|---|
| #000113 / #0d142c | sky, river, gaps between dots | ~54% |
| #2a9350 | green dots/leaves | 4% |
| #bf6891 / #866975 | pink and mauve hill bands | 7% |
| #206486 / #19364c | blue dots (far and near) | 9% |
| (est.) #f2c81e, #f04a1e | yellow centres, orange-red poppies | — |
| #ffffff | figure stroke, daisy petals | <2% |

Figure legibility:
- On black, white is 20.72:1.
- On green dots it is 3.9:1, and on blue 5.73:1.
- On yellow dots it is **1.61:1**. When the stroke crosses yellow flowers (frame 2.50 s), short segments vanish. The stroke's thickness (~8 px at near scale) compensates.

## 5. Depth & material
- **Depth by size:** far-hill dots are about 2–3 px, mid-meadow 8–12 px, near flowers 30–45 px with drawn petals. That is a 15–20× size ramp with no blur or atmospheric fade.
- **Stroke weight:** the figure's stroke weight also scales (≈3 px when far, ≈9 px when near), keeping it in the same projected space.
- **Black as space:** the black is not empty. It reads as night-sky depth and as the river channel, making the coloured surfaces float.

## 6. Components & patterns
- Outline character over a point-cloud landscape (same artist grammar as "I want to run again").
- Foreground scale pass: the figure comes closest mid-clip to create a moment of intimacy.
- **Exit beat:** the leap silhouette against the empty sky (the only time the figure is fully on black) acts as the punchline.

## 7. Motion
Measured values (`m0_motion.json`):
- One continuous segment from 0.08 to 4.92 s (4.84 s) with peak_at 0.67, shape "ease-in (slow start)" and energy CV 1.12.
- Motion fraction is 0.48, with p95 energy 28.4 against a mean of 9.8. Most energy sits in the second half, when the giant figure sweeps through frame and leaps.
- `seamless_loop_likely` is false (first/last diff 14.6).

From the frames (estimate):
- The camera drifts slowly forward the whole time, as the near dots grow between 0.28 s and 1.94 s.
- The figure approaches from 0.83 to 3.06 s, accelerating in on-screen size.
- The jump peaks around 4.17 s, and the figure is gone by 4.72 s, leaving the opening composition to almost restart the scene.

## 8. Brand system
n/a — this is not a brand system. The creator's recurring signature is a white-outline protagonist in a dotted colour world.

## 9. UX
Not interactive. It would work as a short storytelling header with a headline on the black sky band (white on #000113, 20.7:1). The motion is energetic and full-frame in the second half, so it needs a reduced-motion poster fallback (frame 0.28 s is a good still).

## 10. Craft signals
- The figure's stroke width scales with distance rather than staying constant like a UI icon.
- Flowers with petals and centres appear only in the near field; the far field is plain dots, a level-of-detail choice.
- Hill hues are organised in contour bands, not random, so the hills read as terraced fields.
- The dot-free black river acts as a compositional leading line to the leap point.
- The leap happens over the empty sky so the silhouette has maximum contrast at the climax.

## 11. Reproduction recipe
```css
:root{--night:#000113;--green:#2a9350;--pink:#bf6891;--blue:#206486;--yellow:#f2c81e;--poppy:#f04a1e;--line:#fff}
.scene{aspect-ratio:16/9;background:var(--night);overflow:hidden;position:relative}
.runner path{fill:none;stroke:var(--line);stroke-linecap:round;stroke-linejoin:round;
  stroke-width:calc(2px + 7px * var(--near,0))}  /* --near 0..1 driven by depth */
@keyframes approach{0%{transform:translate(-50%,40%) scale(.2)}62%{transform:translate(-40%,20%) scale(1.6);--near:1}
  84%{transform:translate(-50%,-140%) scale(.35)}100%{transform:translate(-50%,-260%) scale(.1);opacity:0}}
.runner{animation:approach 5s cubic-bezier(.55,0,.75,.4) forwards}
```
Terrain (p5/three): scatter points over layered height-fields with band colour by `floor(height*6)`. Point radius is `lerp(1,22,1-depth)`. Points with `depth<.2` are drawn as 5-petal flowers.

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Joyful, naive palette on black; the flower foreground is lush. |
| Originality | 7 | Strong authored style, but close kin to the same artist's other runner piece. |
| Usability | 5 | No loop and an intense full-frame pass; the stroke drops out over yellow dots. |
| Craft | 7 | Thoughtful LOD and stroke scaling; compression artefacts and an unresolved loop. |

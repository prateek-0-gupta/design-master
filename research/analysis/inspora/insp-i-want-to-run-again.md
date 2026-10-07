---
id: insp-i-want-to-run-again
source: inspora
category: Illustration
status: analyzed
title: "I want to run again"
creator: "cem hasimi"
styles: [generative-particle, maximalist-color, x-pointillist-landscape]
patterns: [particle-landscape, outline-figure-over-texture, camera-dolly-through-scene, flat-chroma-sky, foreground-parallax-blooms]
mode: mixed
palette: ["#0407c9", "#000000", "#151a34", "#a3488d", "#22954a", "#879655", "#61514f", "#ffffff"]
type_families: []
type_class: []
radius_px: []
motion: {durations_s: [4.84], easing: [ease-in-out], loop: false}
scores: {aesthetics: 8, originality: 8, usability: 5, craft: 7}
craft_signals: [single-white-outline-figure-as-anchor, sky-particle-fade-band, density-by-depth, black-mass-hills-as-negative-space, saturated-blue-not-gradient]
anti_patterns: [loop-seam-jump, figure-lost-on-light-hills, video-compression-mush]
---
# I want to run again — cem hasimi

## 1. Snapshot
- **Subject:** A 5.0 s, 900×506 (16:9), 25 fps generative clip. A white single-stroke outline of a running figure crosses hills built from thousands of coloured particle dots under a flat electric-blue sky.
- **Why it's remarkable:** It mixes a pointillist, almost Seurat or Yayoi-Kusama surface with a line-drawn character. The only line element in a world of dots is the protagonist, so it is found instantly despite maximal colour noise.

## 2. Composition & layout
- **Horizon:** The horizon sits on the upper third (y≈150 of 506, about 30%). The sky band above is solid #0407c9.
- **Transition band:** Between y≈130 and 190 a band of scattered yellow and white specks dissolves sky into land, acting as atmospheric perspective done with particle density.
- **Hero mountain:** A large black-bodied mountain occupies the centre (x≈130–640 in the key frame). Its silhouette is defined by the colour of the dots on its surface, not by an edge.
- **Figure:** The runner is small, about 45–60 px tall, roughly 10% of frame height. It stays near the horizontal centre third throughout the nine frames (x≈0.35–0.55 W) while the landscape moves past it, a tracking-shot composition.
- **Foreground:** Big blooms (white flower about 110 px at t=4.17 s, red and pink clusters) enter at the bottom edge for a three-layer depth stack: foreground blooms, mid hills, far mountain.

## 3. Typography
None. The piece is purely illustrative.

## 4. Colour
| Hex | Role | Share (key) |
|---|---|---|
| #0407c9 / #1519af | sky (flat ultramarine) | 31% |
| #000000 / #151a34 | hill bodies (negative mass) | ~12% |
| #a3488d / #755263 | magenta/mauve dot fields | 9% |
| #22954a | green meadow dots | 4% |
| #879655 | olive-yellow hill | 7% |
| #61514f / #8b7870 | brown-pink mid-tones (blended dots) | 13% |
| #ffffff | figure stroke, white blooms, specks | <3% |

The hues are fully saturated primaries and secondaries with no intermediate tints, so mixing happens optically, as in pointillism.

Figure-stroke legibility:
- White on sky #0407c9 is 11.18:1.
- On dark hill #151a34 it is 17.08:1.
- On the olive hill #879655 it is only **3.22:1**, and on #8b7870 it is 4.18:1. In frames 1.39–1.94 s the figure crosses the yellow hill and visibly loses presence.

## 5. Depth & material
- **Depth without shading:** Depth is carried by dot size and density. Far dots are about 1–2 px and sparse, near blooms are 8–15 px blobs.
- **Hill bodies:** These are unlit black, so lighting is implied only by where dots sit, mostly on crests. The result reads like a point-cloud render with no surface shading.
- **No blur:** There is no depth-of-field blur; everything is equally crisp, which keeps the flat-poster quality.

## 6. Components & patterns
- Particle/point-cloud terrain.
- An outline character as narrative anchor.
- A continuous camera move (dolly plus slight rise) rather than an animated character on a static background.
- Atmospheric speck band at the horizon.

## 7. Motion
These values are measured from `m0_motion.json`:
- There is one continuous segment from 0.08 to 4.92 s (4.84 s, peak_at 0.36, energy CV 1.02).
- Motion fraction is 0.48.
- `seamless_loop_likely` is false, with a first/last diff of 23.1, which is high. The clip is not a clean loop and the restart will visibly jump.

From the frames (estimate):
- The camera travels forward and to the right continuously. Terrain re-forms almost entirely every ~0.55 s frame step.
- The figure's limb pose changes every sampled frame, suggesting a run cycle of about 0.4–0.6 s.
- Particle energy is high and flickery (CV 1.02), consistent with per-frame point resampling as well as camera motion.

## 8. Brand system
n/a — this is not a brand system. The artist-signature cue is a saturated flat-blue sky plus a white-line character.

## 9. UX
Not interactive. As a visual for a hero or loading background it is very busy, so any overlaid text would need a solid plate. The sky band (top 30%) is the only calm area safe for a headline (white on #0407c9 is 11.18:1). The loop jump would be noticeable as an ambient background.

## 10. Craft signals
- The protagonist is the only line-based element; everything else is dots. This difference in rendering mode makes it the focal point.
- The horizon transition is a ~60 px band of decreasing-density specks rather than a gradient.
- The sky is one flat hex (#0407c9), with no gradient or vignette.
- Hill masses are pure black, so the dot colour does all the form work.
- Foreground blooms are 5–10× the size of the far dots, a deliberate scale contrast for depth.

## 11. Reproduction recipe
```css
:root{--sky:#0407c9;--mass:#000;--magenta:#a3488d;--green:#22954a;--olive:#879655;--bloom:#ffffff}
.scene{aspect-ratio:16/9;background:linear-gradient(var(--sky) 0 28%,transparent 28%),var(--mass);position:relative;overflow:hidden}
.horizon-specks{position:absolute;inset:26% 0 auto;height:12%;
  background:radial-gradient(1.5px 1.5px at 20% 40%,#e9e36a 99%,transparent),radial-gradient(1px 1px at 60% 70%,#fff 99%,transparent);
  background-size:7px 5px,11px 9px;mask:linear-gradient(transparent,#000 40%,transparent)}
.runner{stroke:#fff;stroke-width:2.5;fill:none;stroke-linejoin:round}
```
Generative version (p5/three): sample N points on layered height-fields. Colour each layer from `[magenta, green, olive, red, blue]`. Point size is `lerp(1.5,12,depth)`, the camera z advances 1 unit/s, and the outline runner is an SVG sprite sequence with 8 poses at 60 ms each.

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Joyful, dense and coherent; the flat blue sky disciplines the chaos. |
| Originality | 8 | Line-figure-in-point-cloud is a distinctive pairing. |
| Usability | 5 | Not loopable and too noisy for UI backgrounds; the figure drops below 3.5:1 on light hills. |
| Craft | 7 | Strong depth-by-density, but compression smears dots and the loop seam is unresolved. |

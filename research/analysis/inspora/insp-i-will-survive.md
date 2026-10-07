---
id: insp-i-will-survive
source: inspora
category: Illustration
status: analyzed
title: "I will survive"
creator: "YUDHO"
styles: [dither-halftone, retro-pixel, duotone, high-contrast-bw]
patterns: [one-bit-dither-render, diagonal-rain-particles, flicker-loop, monochrome-red-on-black]
mode: dark
palette: ["#000000", "#dc0408", "#b2060a", "#7d070b", "#3a0507", "#250305"]
type_families: []
type_class: []
radius_px: []
motion: {durations_s: [0.42, 0.5], easing: [ease-in], loop: true}
scores: {aesthetics: 7, originality: 7, usability: 5, craft: 6}
craft_signals: [ordered-dither-texture, single-ink-duotone, rain-as-dotted-streaks, vertical-sword-axis-composition]
anti_patterns: [non-seamless-loop, caption-not-present-in-capture, subject-legibility-low]
---
# I will survive — YUDHO

## 1. Snapshot
- **Subject:** A 1280×1280, 0.5 s looping clip in one red ink on pure black. It shows a vertical sword planted into a dithered mass of rubble, with a skull-like block with two dark sockets to the right of the blade. A shape on the left flaps from frame to frame. Diagonal rain crosses everything.
- **Why it's remarkable:** Everything is rendered as a 1-bit dot field (ordered or noise dither), so the image reads like a thermal print or an old LCD in red. The rain is made of dotted dashes that share the same pixel grid.
- **Caption:** The description mentions a gothic caption, "I will survive", but no type appears in any of the 9 frames or the key frame. It may live only in the source post, so it is not analysed here.

## 2. Composition & layout
- **Axis:** A strong central vertical. The sword runs from y≈60 to ≈1040 at x≈600, slightly left of centre (47%).
- **Masses:** The upper 50% is almost pure black with rain only. The masses sit in the lower half:
  - the skull block at x≈650→990, y≈630→1180;
  - the flapping shape at x≈200→600, y≈890→1280.
- **Rain:** Streaks run at about −20° (rising to the right), each about 40–120 px long, built from dots about 5 px apart. The art grid is therefore about 5 px per pixel, an effective resolution of about 256×256 upscaled 5×.
- The crop is tight: the subject touches the bottom edge, with no breathing room.

## 3. Typography
None visible in the captured media. The site description names a gothic blackletter caption, but it is not seen in the frames, so no claim is made.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #000000 | ground | 69% |
| #dc0408 | full-intensity ink dots | 2.6% |
| #b2060a / #93070a / #7d070b | anti-aliased / compressed ink | about 11% |
| #250305 / #3a0507 | compression bleed in dense dither areas | about 13% |

The intermediate reds are artefacts of video compression on a strictly 2-colour source.

WCAG checks (graphic contrast, not text):
- Brightest red #dc0408 on black: 4.06:1.
- Mid red #b2060a: 2.92:1.

The red-on-black pairing is intentionally low-luminance and moody, but anything thin (rain, sword edge) drops below 3:1 once it is compressed.

## 5. Depth & material
- Depth comes only from dot density. The near masses are dense (about 50% fill). The sword is a 30–50 px wide column of medium density. The background rain is sparse.
- No gradients and no blur. The dither pattern itself encodes tone, and the dot structure gives a printed or thermal texture.

## 6. Components & patterns
- 1-bit dither render of a 3D or photographic source (the flapping shape has believable cloth or fire shading converted to dots).
- Particle rain as dotted line segments aligned to the pixel grid.
- Single-ink duotone (red #dc0408 / black).

## 7. Motion
- **Measured:** 0.5 s at 23.98 fps, so about 12 frames. There is one segment from 0.00 to 0.42 s (duration 0.42 s) with `peak_at` 0.95, classified ease-in (energy keeps rising to the end). `motion_fraction` 1.0, mean energy 5.54. `seamless_loop_likely: false` (first/last difference 7.05).
- **Observed:**
  - Rain streaks shift position every frame (about 2 frames per streak lifetime).
  - The left shape changes silhouette dramatically between frames, from a horizontal slab at t=0.14–0.36 s to a tall diagonal sail at t=0.42 s. This reads as a flag or flame whipped by wind.
  - The sword and skull stay static, apart from dither shimmer.
- **Loop:** At 0.5 s the cut is visible: the frame 0.42 s shape pops back to the slab. As a GIF this reads as a stutter rather than a clean cycle.

## 8. Brand system
n/a — not a brand system. Identity cues: the creator works in pixel or dither gothic aesthetics, using one ink and survival or memento-mori imagery.

## 9. UX
Not a UI. As an avatar or post loop it is high-impact at thumbnail size thanks to the saturated red, but the subject (sword, skull) is hard to parse. The dither destroys edges, and the skull is recognisable mainly by its two dark sockets at about (700,720) and (810,1075).

## 10. Craft signals
- The rain dots lie on the same about 5 px grid as the subject dither, with no sub-pixel mismatch.
- A strict one-ink palette: no second hue was introduced, even for highlights.
- A vertical blade splits the frame into a "sky" half (sparse) and a "ground" half (dense). The composition relies on density alone.
- Rain angle and dash length vary (40–120 px), which avoids a mechanical pattern.

## 11. Reproduction recipe
```css
/* duotone dither look on any image/video */
.dither{image-rendering:pixelated;width:1280px;height:1280px;background:#000}
.dither canvas{filter:none} /* do the dithering in JS (Bayer 4x4 on a 256x256 downsample) */
:root{--ink:#dc0408;--ground:#000}
```
```js
// 256px Bayer dither → scale ×5
const B=[[0,8,2,10],[12,4,14,6],[3,11,1,9],[15,7,13,5]];
for(let y=0;y<256;y++)for(let x=0;x<256;x++){
  const l=lum(src,x,y)/255, t=(B[y%4][x%4]+.5)/16;
  ctx.fillStyle = l>t ? '#dc0408' : '#000'; ctx.fillRect(x*5,y*5,5,5);
}
// rain: dotted segments at -20°, length 8-24 grid cells, respawn every 2 frames
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 7 | A striking one-ink red and the dither texture create mood. |
| Originality | 7 | Dither rain plus gothic memento mori is a fresh combination. |
| Usability | 5 | The subject is hard to read; the caption is absent from the capture. |
| Craft | 6 | Consistent grid, but the 0.5 s loop has a visible pop. |

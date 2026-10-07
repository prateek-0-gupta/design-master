---
id: insp-folder-icon-timeline
source: inspora
category: Motion
status: analyzed
title: "macOS Folder Icon Timeline"
creator: "@raul_dronca"
styles: [minimal-swiss, retro-pixel, skeuomorphic, micro-interaction]
patterns: [scrubbable-timeline, tick-ruler-slider, gaussian-tick-falloff, version-history-viewer, hover-chip-on-label, centered-hero-object]
mode: light
palette: ["#ffffff", "#222222", "#777777", "#d0d0d0", "#8fc7ef", "#a0d5f4", "#859fb3"]
type_families: ["SF Pro Text (likely)"]
type_class: [neo-grotesk]
radius_px: [10]
motion: {durations_s: [1.0, 1.0, 0.5, 0.4, 1.13, 0.87, 0.67], easing: [ease-in-out, ease-out], loop: false}
scores: {aesthetics: 8, originality: 7, usability: 8, craft: 8}
craft_signals: [bell-curve-tick-heights, selected-year-bold-not-colored, tabular-year-labels, pixel-art-kept-crisp-at-scale, hover-chip-f4f4f4, icon-swap-without-chrome]
anti_patterns: [unselected-labels-just-below-aa, no-label-for-current-era-name]
---
# macOS Folder Icon Timeline — @raul_dronca

## 1. Snapshot
- **Subject:** A 32.3 s, 2876×2160 (retina, about 1438×1080 CSS) recording of a single folder icon above a tick-ruler timeline. Scrubbing or clicking a year (1984, 1994, 1997, 2001, 2007, 2012, 2014, 2020, 2025) swaps the icon through four decades of Mac folder designs.
- **Why it's remarkable:** The ruler's tick heights form a bell curve centred on the playhead, so the control itself visualises "where you are" in time. The UI is otherwise invisible, which lets the icons carry the whole story.

## 2. Composition & layout
- Pure white canvas. The icon is centred horizontally at about 648 px wide (≈324 CSS) and occupies y≈520–1160 px.
- The ruler sits about 140 px below the icon: 49 ticks spaced about 29 px apart across about 1380 px (x≈750→2130).
- Year labels sit about 110 px below the ticks, spaced about 172 px apart. Each label aligns under every sixth tick.
- The vertical stack (icon, ruler, labels) sits just above optical centre, leaving about 40% white below. It is a single-object stage with no title or chrome.

## 3. Typography
- One sans, SF Pro Text-like, at about 29 px real (≈14.5 CSS) with letter-spacing of about +0.04 em, which is generous for numerals.
- **Selected year:** semibold #222. **Others:** regular #777. Hierarchy is weight plus value, with no colour accent.
- The years appear to use tabular figures, since every label's width matches.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #ffffff | canvas | 94% |
| #222222 | playhead tick, selected year | <1% |
| #777777 | unselected years | <1% |
| #d0d0d0 | inactive ticks | ~1% |
| #8fc7ef / #a0d5f4 | modern folder blues (2007/2020/2025) | ~2% |
| #859fb3 | 2012 slate-blue folder | <1% |

The only chroma comes from the artefact on display. In early eras that is lavender pixel fills (≈#d9d4f5) and violet 3D pixels for 1997.

WCAG checks:
- Selected #222 on white is 15.91:1.
- Unselected #777 on white is **4.48:1**, which just misses AA for 14.5 px text.
- On the #f4f4f4 hover chip, the same grey drops to 4.07:1.
- Inactive ticks #d0d0d0 are 1.54:1. That is fine for decoration, but the playhead tick must carry the state.

## 5. Depth & material
- The UI is completely flat, with no shadows. The depth lives in the icons themselves:
  - 1-bit outline (1984);
  - dithered lavender fill (1994);
  - isometric pixel 3D (1997);
  - Aqua pinstripe glass with a black keyline (2001);
  - glossy gradients (2007/2020);
  - matte slate (2012).
- Pixel-art eras are scaled with nearest-neighbour, so the edges stay hard at about 18 px per source pixel.

## 6. Components & patterns
- **Tick-ruler slider:** a 2 px dark playhead tick about 170 px tall. Neighbouring ticks fall off in height and lightness along a Gaussian curve: about 170 px at the playhead down to about 50 px at a distance of 10 ticks.
- **Year labels as snap targets:** hovering shows a #f4f4f4 rounded chip (radius ≈10 px, about 170×120 px) behind the label, and the pointer is a hand cursor.
- The icon is a plain swap with no captions, which keeps the comparison pure.

## 7. Motion
Measured: 60 fps, 32.3 s, `motion_fraction` 0.17, 12 segments with a median of **0.53 s**.
- **Long scrubs** (playhead travelling across many ticks) take 1.0 s with a symmetric ease-in-out: 2.33–3.33 s and 8.07–9.07 s.
- **Short snaps** take 0.4–0.5 s and are ease-out, peaking at 0.04–0.17 of the segment: 12.87–13.37 s and 14.6–15.0 s.
- **The late sequence (26.2–30.8 s)** is a fast back-and-forth drag of 0.57 / 1.13 / 0.87 / 0.67 s. It alternates ease-in and ease-out, which is the signature of a hand-driven scrub.

The bell curve travels with the playhead in real time. The icon appears to crossfade or snap rather than morph, and no in-between frames were seen in the 9-frame sample (estimate).

## 8. Brand system
n/a — not a brand system. It is a design-history piece. Identity cues: the Apple folder lineage; the presentation itself is brand-neutral.

## 9. UX
- **Strengths:**
  - Direct manipulation with two input paths (drag the ruler, or click a year).
  - The bell curve makes the current position legible even without reading labels.
  - The labels are discrete snap points.
- **Risks:**
  - Unselected label contrast is about 4.5:1.
  - There is no OS name (e.g. "Mac OS X 10.0") to say why each year matters.
  - The labels are unevenly spaced in time but evenly spaced on screen, which visually compresses the 1984–1994 gap.

## 10. Craft signals
- Tick heights follow a smooth falloff of about 3.4× (170 → 50 px) from the playhead, and tick lightness falls off too.
- The selected state uses weight and value (#222 semibold) with no accent colour.
- The hover chip is a quiet #f4f4f4 at radius ≈10 px.
- Pixel-era icons render with hard edges; there is no bilinear blur at 18× scale.
- The icon's footprint stays at about 648 px across eras, so the swaps do not jump in size.
- Tick pitch (about 29 px) divides the label pitch (about 172 px) evenly, at six ticks per year.

## 11. Reproduction recipe
```css
:root{--bg:#fff;--ink:#222;--ink-2:#777;--tick:#d0d0d0;--chip:#f4f4f4;--font:-apple-system,"SF Pro Text","Inter",sans-serif}
.ruler{display:flex;gap:12.5px;align-items:flex-end;height:86px}
.tick{width:1px;background:var(--tick);
  height:calc(25px + 60px * exp(-1 * pow(var(--d), 2) / 32)); /* --d = distance from playhead in ticks */
  transition:height .5s cubic-bezier(.2,.8,.2,1)}
.tick.is-head{width:2px;background:var(--ink);height:86px}
.years{display:flex;justify-content:space-between;font:400 14.5px/1 var(--font);letter-spacing:.04em;font-variant-numeric:tabular-nums;color:var(--ink-2)}
.years button{padding:20px 22px;border-radius:10px}
.years button:hover{background:var(--chip)}
.years [aria-current]{color:var(--ink);font-weight:600}
.icon img{image-rendering:pixelated;width:324px}
```
(`pow`/`exp` are CSS math functions in modern browsers; otherwise compute the height in JS.)

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Calm white stage. The ruler is beautiful, and the icons provide all the colour. |
| Originality | 7 | The tick ruler with a Gaussian focus is a fresh take on a common slider. |
| Usability | 8 | Two input paths, clear state and snap labels. Grey labels are marginal on contrast. |
| Craft | 8 | Consistent pitch, crisp pixel art and restrained states. |

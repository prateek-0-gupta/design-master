---
id: insp-4-1
source: inspora
category: Motion
status: analyzed
title: "Age Progression slider"
creator: "@AdityaSur11"
styles: [minimal-swiss, monochrome, photo-led]
patterns: [tick-ruler-slider, bell-curve-tick-heights, floating-value-pill, segmented-mono-color-toggle, image-scrub-morph]
mode: light
palette: ["#ffffff", "#010101", "#ebebeb", "#cacaca", "#ba8a73", "#261f1d"]
type_families: ["Inter / SF Pro Text (likely)"]
type_class: [neo-grotesk]
radius_px: [9999]
motion: {durations_s: [0.1, 0.13, 0.2, 0.3, 0.53], easing: [ease-out, ease-in], loop: true}
scores: {aesthetics: 8, originality: 7, usability: 6, craft: 6}
craft_signals: [tick-heights-form-bell-curve-around-thumb, black-thumb-line-only-saturated-mark, value-pill-tracks-thumb, mono-toggle-desaturates-photo, cutout-face-no-background]
anti_patterns: [age-label-and-image-out-of-sync, invisible-inactive-ticks, inactive-toggle-label-low-contrast]
---
# Age Progression slider — @AdityaSur11

## 1. Snapshot
- **Subject:** A 29.8 s, 2180×2160 demo of a slider that scrubs a cut-out face from age 5 to about 64. It has a "Mono / Color" segmented toggle in the top-right corner.
- **Why it's remarkable:** The slider is a ruler of fading ticks whose heights swell into a bell curve around the thumb. It works like a magnifier on the timeline, with no track or knob.

## 2. Composition & layout
- **Overall:** Everything is centred on pure white.
- **Face:** About 410×550 px, roughly y 600→1150.
- **Value pill:** "Age: N", about 156×59 px, sitting about 100 px below the chin.
- **Ruler:**
  - 23 ticks spaced about 46 px apart, spanning about 1000 px (x≈555→1575).
  - The active tick is a black bar about 4×160 px.
  - Neighbouring ticks shrink stepwise (about 150 → 20 px tall) and fade toward the ends.
- **Toggle:** About 220×60 px, anchored about 20 px from the top-right corner.
- **Whitespace:** More than 70% of the canvas is white. The face is the only mass.

## 3. Typography
- One neo-grotesk (Inter/SF-like) used at a single size: about 26 px Medium, white on black inside the value pill and the toggle.
- The inactive toggle label is #cacaca-ish regular.
- No headings. The UI is entirely label-level.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #ffffff | canvas | 95% |
| #010101 | thumb tick, value pill, active toggle | 1% |
| #ebebeb | inactive ticks | <1% |
| #cacaca | inactive toggle text | <1% |
| #ba8a73 / #9c7562 | skin tones in Color mode | 2% |
| #261f1d | hair | 1% |

WCAG:
- White on #010101 (pill) is 20.87:1.
- Inactive "Mono" #cacaca on white is **1.64:1**, which fails. It is only discoverable because it sits inside the toggle.
- The far ticks are near-invisible (#ebebeb on #fff is about 1.2:1), which is acceptable because they are decorative.

## 5. Depth & material
- Totally flat. The only depth comes from the photographic face, which is cut out with a soft edge and no shadow.
- The toggle has a 1 px #e5e5e5 outline with a black inner pill for the active segment.

## 6. Components & patterns
- **Tick-ruler slider:** No track. The magnitude of each tick encodes its distance from the current value (a fisheye bell curve).
- **Floating value pill:** It follows the thumb horizontally (x shifts from 323 to 969 to 1605 across the frames) and stays at a fixed y.
- **Mono/Color toggle:** It swaps a greyscale filter on the image. Frames 0–3 are Mono and frames 4–7 are Color.

## 7. Motion
- **Measured:** 14 segments across 29.79 s, median 0.18 s, durations 0.10–0.53 s. motion_fraction is 0.11 and `seamless_loop_likely: true`.
- **Shape:** Most segments are short scrub bursts, with drag starts peaking early and settles peaking late:
  - 7.73 s: 0.20 s, peak 0.08 (ease-out).
  - 15.5 s: 0.30 s, peak 0.06 (ease-out).
  - 6.57 s: 0.20 s, peak 0.92 (ease-in).
  - 25.80 s: 0.53 s, peak 0.78 (ease-in).
  - The longest symmetric move is 24.8 s (0.40 s, peak 0.38), likely the face crossfade between age keyframes.
- **Frames:** The bell curve of ticks re-centres continuously as the thumb moves. The face appears to crossfade between a small number of discrete age images rather than morphing per year.

## 8. Brand system
n/a — not a brand system.

## 9. UX
- Scrubbing is direct and the value pill gives precise feedback.
- **Bug-like inconsistency:** At t≈8.3 s the label reads "Age: 21" over the 5-year-old face, and in the key frame "Age: 24" also shows the child. The image buckets lag the label, which breaks trust.
- No min/max labels.
- The ticks don't show the scale (years per tick unknown).

## 10. Craft signals
- Tick heights form a smooth symmetric falloff (about 9 steps each side) centred on the thumb, re-computed live.
- Black (#010101) is reserved for the single "now" element: thumb, pill and active toggle.
- The value pill is horizontally locked to the thumb x within ±5 px.
- The face is cut out with no backdrop, so the Mono/Color switch is a clean filter swap.

## 11. Reproduction recipe
```css
:root{--ink:#010101;--tick:#e6e6e6;--bg:#fff}
.ruler{display:flex;gap:42px;align-items:flex-end;height:160px}
.tick{width:4px;border-radius:2px;background:var(--tick);
  height:calc(160px * max(.12, 1 - var(--d) * .1));   /* --d = |i - value| set from JS */
  transition:height .18s cubic-bezier(.2,.8,.2,1)}
.tick[aria-current]{background:var(--ink)}
.pill{background:var(--ink);color:#fff;font:500 26px/1 Inter;padding:16px 26px;border-radius:9999px;
  transform:translateX(var(--x));transition:transform .18s cubic-bezier(.2,.8,.2,1)}
.face{transition:filter .3s ease}.mono .face{filter:grayscale(1)}
.seg{border:1px solid #e5e5e5;border-radius:9999px;padding:4px}.seg [aria-pressed=true]{background:var(--ink);color:#fff}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Severe, gallery-like restraint with one photo and one black accent. |
| Originality | 7 | The bell-curve tick ruler is a fresh slider idiom. |
| Usability | 6 | Direct scrubbing, but the label/image mismatch, no scale and a low-contrast toggle hurt it. |
| Craft | 6 | The ruler is beautifully tuned, but the age buckets are visibly out of sync. |

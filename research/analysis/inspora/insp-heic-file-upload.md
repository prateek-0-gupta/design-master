---
id: insp-heic-file-upload
source: inspora
category: Motion
status: analyzed
title: "HEIC File Upload"
creator: "@yanhladchenko"
styles: [corporate-clean, soft-3d, aurora-glow, micro-interaction]
patterns: [drop-zone-empty-state, fanned-file-cards-illustration, thumbnail-grid-with-format-badge, ticked-quality-slider, live-size-estimate, success-toast-with-action, before-after-file-size]
mode: light
palette: ["#fefefe", "#ecf3f0", "#f3effa", "#555555", "#111111", "#183d7a", "#e07a3a", "#b7aaa7"]
type_families: ["SF Pro Text (likely)"]
type_class: [neo-grotesk]
radius_px: [48, 24, 9999]
motion: {durations_s: [0.27, 0.37, 0.37, 0.77, 0.1], easing: [ease-out, ease-in-out], loop: false}
scores: {aesthetics: 8, originality: 6, usability: 8, craft: 8}
craft_signals: [badge-flips-heic-to-jpg, size-delta-arrow-per-file, savings-summary-in-toast, ticked-slider-track, pastel-mesh-window-tint, approx-sign-on-estimate]
anti_patterns: [quality-label-2-6-to-1, size-estimate-lags-slider]
---
# HEIC File Upload — @yanhladchenko

## 1. Snapshot
- **Subject:** A 16.1 s, 2432×2160 recording of a small macOS utility that converts HEIC to JPG.
- **Flow:**
  - an empty drop state with fanned "1.9 MB / JPG" cards;
  - four photos appear as HEIC-badged thumbnails;
  - a zoomed close-up of a ticked "Quality" slider (50% → 18% → 80% → 51%);
  - Convert, after which the badges flip to JPG with "6.5 MB → 5.4 MB" deltas;
  - a toast: "4 photos converted · Saved 2.7 MB · 14% smaller".
- **Why it's remarkable:** Every step reports the consequence in file-size terms. The slider shows "≈ 17 MB", each tile shows before → after, and the toast shows the total saving. The tool explains its value without any copy.

## 2. Composition & layout
- **Window:** about 2250×2000 px with large corners (radius ≈48 px real), floating on a blurred orange/blue macOS wallpaper, with traffic lights top-left.
- **Empty state:** the stacked-card illustration (about 580 px wide) sits at y≈30% of the window. Below it: the headline, a one-line hint and an "Add Files…" pill, all centred.
- **Loaded state:**
  - toolbar row with "4 photos", grid/list toggle, and the "Add Files…" and "Clear" pills;
  - a 4-up grid of about 500×620 px thumbnails at about 50 px gutters;
  - a footer bar separated by a hairline: "Quality", a slider about 60% of the width, "50% ≈ 17 MB", and a black "Convert" pill bottom-right.
- **Toast:** centred above the footer, about 1100×150 px, holding a check icon, two lines of text and a "Show in Finder" pill.

## 3. Typography
- SF Pro Text.
- **Headline:** "Drop your HEIC photos", about 70 px semibold #111.
- **Hint:** about 36 px regular grey.
- **Tile captions:** filename about 32 px medium, with size about 30 px grey below.
- **Slider values:** "18% ≈ 17 MB" at about 64 px regular #555 in the zoom shot. They appear to use tabular figures and the ≈ sign.
- The "Quality" label is lighter grey (≈#9a9a9a).
- **Badges** ("HEIC", "JPG") are about 26 px semibold in small translucent pills.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #fefefe | window surface | 80% |
| #ecf3f0 / #f3effa | mint (bottom-right) and lavender (top-left) mesh tints inside the window | 11% |
| #555555 | values, secondary text | — |
| #111111 | headline, Convert button | <1% |
| #183d7a / #e07a3a | wallpaper blue / orange (context) | 6% |
| #b7aaa7 | slider track ticks | 3% |

WCAG checks:
- Values #555 on #f6f7f6 are 6.94:1.
- The "Quality" label at #9a9a9a is **2.62:1, a fail**.
- Size subtext (≈#8a8a8a on white) is 3.45:1.
- The Convert pill (white on #111) is 18.88:1.
- Buttons ("Add Files…", #222 on #e6e6e6) are 12.75:1.

## 5. Depth & material
- **Window:** a soft drop shadow, and an interior pastel mesh gradient: lavender top-left, peach top-right, mint bottom. It reads as frosted glass catching wallpaper colour.
- **Empty-state cards:** three rotated, fanned cards (green, lavender, peach to rose) with drop shadows and white pill labels.
- **Slider:** an inset grey pill track with about 45 vertical tick marks. The white thumb is a capsule with a shadow.
- **Thumbnails:** radius ≈24 px. On hover a small circular "×" remove button appears top-right (t≈13.39 s).

## 6. Components & patterns
- A drop zone with an illustration, headline, hint and secondary button.
- Grid/list view toggle.
- Thumbnail tiles: format badge bottom-left, then filename and size.
- **Quality slider with live output estimate:** the "≈ 17 MB" readout is the key affordance.
- Primary action as a black pill anchored bottom-right.
- **Success toast:** a summary metric plus a follow-up action ("Show in Finder").

## 7. Motion
Measured: 60 fps, 16.1 s, `motion_fraction` 0.12, 5 segments, median **0.37 s**:
- 2.77–3.03 s (0.27 s, ease-out, peak at 0.06): photos dropped in, empty state to grid;
- 3.57–3.93 s and 5.43–5.80 s (0.37 s each, ease-out): the grid settling, then the cut or zoom to the slider;
- 11.53–12.30 s (0.77 s, symmetric): the motion-blurred camera pull-back from the slider (t≈11.6 s frame is heavily blurred);
- 13.33–13.43 s (0.10 s): Convert press feedback.

All UI transitions start fast and settle (peaks at 0.05–0.14). The 18% frame still shows "≈ 17 MB" and the 80% frame shows no size, so the estimate recomputes with a lag (observed).

## 8. Brand system
n/a — not a brand system. It inherits macOS conventions (traffic lights, SF, pill buttons). The pastel window mesh is its only identity cue.

## 9. UX
- **Strengths:**
  - The empty state teaches the input (drag photos or a folder).
  - Format badges show state before and after.
  - Per-file and total savings.
  - Clear and Add are always reachable.
  - The toast offers the obvious next step.
- **Risks:**
  - The "Quality" label is low contrast.
  - The size estimate lags behind the slider, which momentarily misleads.
  - Quality is shown only as a percentage with no preview of the visual impact.

## 10. Craft signals
- The badge text swaps HEIC → JPG in place, in the same pill and position.
- Each tile shows "6.5 MB → 5.4 MB" with an arrow glyph, not a hyphen.
- The toast quantifies the result ("Saved 2.7 MB · 14% smaller") with a middle-dot separator.
- The estimate uses "≈", which is honest about approximation.
- The slider track has about 45 evenly spaced ticks for fine-grain feedback.
- The window's interior mesh tints echo the wallpaper hues (peach, lavender, mint).
- Exactly one black (primary) button per screen state.

## 11. Reproduction recipe
```css
:root{--surface:#fefefe;--mint:#ecf3f0;--lav:#f3effa;--ink:#111;--ink-2:#555;--ink-3:#767676;--track:#e4e4e4;--r-win:24px;--r-tile:12px}
.window{border-radius:var(--r-win);background:
  radial-gradient(50% 40% at 15% 10%,var(--lav),transparent),radial-gradient(60% 50% at 85% 100%,var(--mint),transparent),var(--surface);
  box-shadow:0 30px 80px rgb(0 0 0/.25)}
.tile img{border-radius:var(--r-tile);aspect-ratio:4/5;object-fit:cover}
.badge{position:absolute;left:8px;bottom:8px;padding:2px 7px;border-radius:9999px;background:rgb(255 255 255/.7);backdrop-filter:blur(6px);font:600 11px -apple-system}
.slider{appearance:none;height:28px;border-radius:9999px;
  background:repeating-linear-gradient(90deg,transparent 0 6px,#b7aaa7 6px 7px) center/calc(100% - 16px) 12px no-repeat,var(--track)}
.slider::-webkit-slider-thumb{appearance:none;width:18px;height:24px;border-radius:9999px;background:#fff;box-shadow:0 1px 4px rgb(0 0 0/.25)}
.estimate{font-variant-numeric:tabular-nums;color:var(--ink-2)}
.btn-primary{background:var(--ink);color:#fff;border-radius:9999px;padding:8px 16px;font-weight:600}
.toast{animation:toast .35s cubic-bezier(.2,.8,.2,1)} @keyframes toast{from{opacity:0;translate:0 12px}}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | A clean native-feeling window with a subtle pastel mesh and nice fanned-card illustration. |
| Originality | 6 | A standard converter flow, elevated by the size-centric feedback. |
| Usability | 8 | Outcome-oriented feedback at every step. The label contrast and estimate lag are minor issues. |
| Craft | 8 | Consistent pills, in-place badge swaps and honest "≈" numbers. |

---
id: insp-shader-dial
source: inspora
category: Motion
status: analyzed
title: "Shader Dial"
creator: "@raul_dronca"
styles: [hairline-ui, gradient-mesh, grain-noise, corporate-clean]
patterns: [preset-list-with-swatches, fill-slider-rows, label-inside-slider, live-shader-preview, reset-appears-on-dirty, three-panel-tool-layout]
mode: light
palette: ["#fafafa", "#ffffff", "#dddce0", "#efeff1", "#1c1c1e", "#55555a", "#60646f", "#b8b9bd"]
type_families: ["Inter (likely)"]
type_class: [neo-grotesk]
radius_px: [100, 24, 16, 10]
motion: {durations_s: [0.13, 0.2, 0.27, 38.52], easing: [ease-out], loop: false}
scores: {aesthetics: 9, originality: 7, usability: 8, craft: 9}
craft_signals: [slider-is-the-row, label-and-value-inside-track, preset-swatch-is-mini-render, reset-only-when-modified, thin-thumb-bar-4px, squircle-preview-matches-swatches, panel-hairline-borders]
anti_patterns: [slider-fill-vs-track-low-contrast, value-only-percent-no-units]
---
# Shader Dial — @raul_dronca

## 1. Snapshot
- **Subject:** A 38.5 s, 2880×2160 screen recording of a mesh-gradient shader tool: a preset list (Greenwood, Sandstone, Harbor, Heather, Rosewater, Slate) on the left, a large grainy squircle preview in the centre, and a "Settings" panel with four fill-style sliders (Distortion, Swirl, Grain mixer, Grain overlay) on the right.
- **Why it's remarkable:** The sliders are the rows themselves: label left, value right, the darker fill and a 4 px thumb bar sitting behind the text, so a 4-parameter control panel stays as calm as a list.

## 2. Composition & layout
- Stage #fafafa; three elements on a shared horizontal band, vertically centred around y≈750 (of 2160 original ≈ 50%):
  - preset panel ≈ 475×790 px (original), 6 rows ≈ 130 px pitch;
  - preview squircle ≈ 925 px square (radius ≈ 100 px, a continuous-curvature corner);
  - settings panel ≈ 700×660 px, header row + 4 slider rows ≈ 112 px tall with ≈ 16 px gaps.
- Gaps between panels ≈ 60 px; the preview is the visual anchor, ≈ 2× the side panels' width.

## 3. Typography
- Inter-like neo-grotesk: row labels ≈ 36 px (≈ 13 px at 1×) regular/medium #1c1c1e; values "35%" right-aligned, same size, #55555a; header "Settings" ≈ 36 px medium, "Reset" ≈ 30 px regular grey.
- Tabular percent values; sentence case everywhere; no bold.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #fafafa | stage | 83% |
| #ffffff | panels | — |
| #efeff1 | slider track | — |
| #dddce0 | slider fill, selected preset row | 3.3% |
| #1c1c1e | labels | — |
| #55555a | values, secondary | — |
| #60646f → #b8b9bd | "Slate" shader greys | ~10% |
| preset hues | Greenwood sage/forest, Sandstone peach, Harbor steel blue, Heather lilac/aubergine, Rosewater pink | swatches |

WCAG checks:
- Label #1c1c1e on slider fill #dddce0: 12.47:1.
- Value #55555a on track #efeff1: 6.45:1.
- Preset label ≈#3a3a3c on white: 11.35:1.
- Fill #dddce0 vs track #efeff1 ≈ 1.2:1 — the slider position reads only via a subtle tint plus the white 4 px thumb.

## 5. Depth & material
- UI is flat: white panels with a 1–2 px #e5e5e8 hairline border and an extremely soft shadow; selected preset row = #efeff1 pill.
- All material richness lives in the preview: a domain-warped two/three-tone gradient with real film grain (visible at "Grain overlay 50%"), soft-shadowed folds that read as satin or brushed metal.
- Preset swatches (≈ 60 px, 12 px radius) are miniature renders of each shader with the same diagonal light, not flat colour chips.

## 6. Components & patterns
- Preset list with mini-render swatches + names; the selected row is highlighted.
- Fill slider rows (label-in-track): the full row is draggable, a darker fill = value, a 4×28 px white thumb bar at the fill's edge, the value at the right.
- "Reset" link appears in the header only after a parameter has been changed (absent at 2.14–14.98 s, present from 19.26 s).
- Live preview updates continuously as sliders move.

## 7. Motion
Measured (m0_motion.json): 38.52 s, 60 fps, motion_fraction 0.03 (the UI is mostly still), six short segments all **ease-out (peak_at 0.08–0.25)**: 3.30 s (0.13 s), 6.30 s (0.20 s), 8.87 s (0.27 s), 10.83 s (0.17 s), 12.77 s (0.23 s), 25.63 s (0.20 s). These match preset switches (Greenwood → Rosewater/Harbor → Heather → Slate → Greenwood), each re-rendering the preview with a fast 0.13–0.27 s ease-out crossfade. Slider drags and the shader's slow internal drift stay below the energy threshold. Not a loop (first/last diff 8.24).

## 8. Brand system
n/a — not a brand system. Preset naming (natural-material names: Greenwood, Sandstone, Harbor, Heather, Rosewater, Slate) gives the tool a calm, crafted personality.

## 9. UX
- Low cognitive load: 6 presets plus 4 named, bounded (0–100%) parameters; tweaks are reversible via Reset.
- Full-row sliders give large hit areas (≈ 112 px tall at 2×, ≈ 40 px at 1×).
- **Risks:** the fill-vs-track difference is subtle (≈ 1.2:1), so the slider value relies on the numeric label; no keyboard/drag affordance is visible until hover; values have no precision input or units beyond %.

## 10. Craft signals
- Label text sits on top of the fill without colour change — it stays legible at both fill and track (12.5:1 / ≈ 14:1).
- The thumb is a 4 px rounded white bar, not a knob — it doesn't cover the label.
- Swatches use the same squircle shape and lighting as the preview.
- "Reset" appears only once state is dirty.
- Panel heights differ but are centred on the preview's vertical midline.
- Grain is visible only inside the preview, never on UI chrome.

## 11. Reproduction recipe
```css
:root{--stage:#fafafa;--panel:#fff;--track:#efeff1;--fill:#dddce0;--ink:#1c1c1e;--ink-2:#55555a;--hair:#e5e5e8}
.panel{background:var(--panel);border:1px solid var(--hair);border-radius:16px;padding:8px;box-shadow:0 1px 2px rgba(0,0,0,.03)}
.slider{--v:35%;position:relative;height:40px;border-radius:10px;
  background:linear-gradient(90deg,var(--fill) var(--v),var(--track) 0);display:flex;align-items:center;
  justify-content:space-between;padding:0 12px;font:500 13px/1 Inter,system-ui;color:var(--ink);cursor:ew-resize}
.slider::after{content:"";position:absolute;left:calc(var(--v) - 10px);top:10px;width:4px;height:20px;border-radius:2px;background:#fff}
.slider output{color:var(--ink-2);font-variant-numeric:tabular-nums}
.preset[aria-selected=true]{background:var(--track);border-radius:10px}
.swatch{width:22px;height:22px;border-radius:6px}
.preview{width:320px;aspect-ratio:1;border-radius:22%;transition:opacity .2s cubic-bezier(.16,1,.3,1)}
```
Shader: domain-warped noise (`uv += distortion * fbm(uv + swirl*rot(t))`), three-stop palette per preset, plus a hash-based grain `mix(col, vec3(hash(uv*res)), grainOverlay*0.15)`.

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 9 | Quiet, Apple-grade chrome framing a lush preview. |
| Originality | 7 | Label-in-track sliders exist (Figma, Linear), executed exceptionally. |
| Usability | 8 | Big targets, clear values, Reset-on-dirty; subtle fill contrast. |
| Craft | 9 | Consistent radii, shape echoing, thin thumb, contextual Reset. |

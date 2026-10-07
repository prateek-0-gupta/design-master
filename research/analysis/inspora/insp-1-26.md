---
id: insp-1-26
source: inspora
category: 3D
status: analyzed
title: "Wave thinking animations"
creator: "@AdityaSur11"
styles: [isometric, monochrome, technical-wireframe, minimal-swiss]
patterns: [isometric-heightfield-loader, rotating-status-copy, shimmer-text-sweep, blur-in-text-swap, ai-thinking-indicator]
mode: light
palette: ["#f9f9f9", "#ffffff", "#e8e8e8", "#dddddd", "#c3c2c5", "#5c5c63", "#9a9aa0"]
type_families: ["Inter (likely)"]
type_class: [neo-grotesk]
radius_px: []
motion: {durations_s: [16.5, 1.8], easing: [continuous-linear, ease-in-out], loop: true}
scores: {aesthetics: 8, originality: 7, usability: 7, craft: 8}
craft_signals: [hairline-edge-per-cube, three-tone-face-shading, shimmer-gradient-on-label, blur-dissolve-copy-change, centred-optical-axis, single-hue-greys]
anti_patterns: [shimmer-trough-below-aa, low-figure-ground-separation]
---
# Wave thinking animations — @AdityaSur11

## 1. Snapshot
- **Subject:** A 16.5 s, 1920×1328 loop of an AI "thinking" state. It shows a 5×5 isometric field of white cubes whose heights ripple in waves (diagonal ramps, pyramids, terraces). Below it, a status line cycles through "Recalling previous context…", "Processing…" and "Searching memories…".
- **Why it's remarkable:** The loader is a heightfield, so each status gets a different wave shape. It feels computational without using a single colour.

## 2. Composition & layout
- **Placement:** Everything is on the vertical axis.
  - The cube field is about 560×300 px, centred at roughly (960, 665), so it sits slightly below the frame centre.
  - The label baseline is at y≈980, a gap of about 165 px under the field's lowest vertex.
- **Negative space:** About 90% of the frame is empty #f9f9f9, so the object reads like a product empty state.
- **Geometry:** A 2:1 isometric projection (30° edges). Each cube is about 56 px on its top-face diagonal, and the base plate is about 6 px thick.

## 3. Typography
- **Typeface:** Inter or a similar neo-grotesk, about 34 px in the 1920 frame (about 17 px at @2x), medium weight, sentence case with a trailing ellipsis.
- **Colour:** The ink is a cool grey (#5c5c63). A lighter band (#9a9aa0) sweeps across the word left to right. On the key frame "P" is light while "rocessing" is dark, so the sweep is caught mid-pass.
- **Copy changes:** The leading characters blur out and in. Frame f1 (2.75 s) shows "Re" Gaussian-blurred, about 6 px radius, while "calling…" is sharp.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #f9f9f9 | canvas | 97% |
| #ffffff | cube top faces | — |
| #e8e8e8 / #dddddd | left / right cube faces | 2.7% |
| #c3c2c5 | 1 px edges | 0.1% |
| #5c5c63 | label ink | <0.5% |
| #9a9aa0 | shimmer highlight | — |

WCAG checks:
- Label #5c5c63 on #f9f9f9: 6.3:1 (pass).
- Shimmer trough #9a9aa0: **2.66:1** (fails while the sweep passes over a letter).
- Cube edges #c3c2c5: 1.68:1, which is decorative only.
- Side faces #e8e8e8 on canvas: 1.16:1, so the object barely separates from the ground. That is intentionally whisper-quiet.

## 5. Depth & material
- Flat-shaded with three tones and no cast shadows or gradients. Light comes from the top-left, giving a top of #fff, a left face of #e8e8e8 and a right face of #dddddd.
- Every cube carries a 1 px #c3c2c5 outline, which reads as a vector/CAD illustration rather than a render.
- Some faces show dotted edges where cubes are coplanar (key frame), a subtle construction-line detail.

## 6. Components & patterns
- **Thinking indicator:** a visual object plus a rotating status string. Three messages were seen across 16.5 s.
- **Heightfield states:** checkerboard (0.92 s), radial pyramid (4.58 s), single-axis terraces (6.42 s, 10.08 s), and a diagonal ramp (key frame). Each looks like a different "thought".
- **Text transition:** a blur dissolve per glyph from the left plus a continuous shimmer gradient.

## 7. Motion
Measured profile:
- 16.5 s at 30 fps.
- `motion_fraction` **0.0** and mean energy 0.09: the motion never crossed the detector threshold (0.35).
- `seamless_loop_likely: true`, but first_last_diff is 0.68.

So the cube motion is slow, small and continuous: a constant ripple rather than discrete pops. That suits "thinking" because nothing ever snaps.

Estimated from the 9 frames (about 1.83 s apart):
- The wave shape fully changes between every sampled frame, so each formation lasts at most about 1.8 s.
- Labels persist for roughly 3.5–5.5 s ("Recalling" at 6.42 s and "Processing" at 8.25 s).
- At 10.08 s the label is a blurred fragment ("Se…"), so the text swap takes an estimated 0.3–0.5 s with ease-in-out blur.

## 8. Brand system
n/a — not a brand system. Identity cues: a monochrome CAD aesthetic and lowercase-calm status copy, a "memory" vocabulary (recall, search memories) suited to an AI assistant.

## 9. UX
- **Strengths:** Changing labels tell the user what stage the agent is in, which is better than a generic spinner. The calm motion reduces perceived wait.
- **Risks:**
  - The shimmer dips below AA.
  - With 1.16:1 faces, the object nearly disappears on lower-quality displays.
  - There is no progress estimate, and messages appear to cycle rather than reflect real state.

## 10. Craft signals
- Three-tone face shading (#fff / #e8e8e8 / #dddddd) is consistent across every cube, so the light direction never changes.
- A 1 px hairline on all cube edges, with dotted lines on hidden coplanar seams.
- The label shimmer is a moving gradient, not an opacity pulse.
- The copy change blurs only the changing leading glyphs.
- The cube field and label share one centre line, with about a 165 px fixed gap.

## 11. Reproduction recipe
```css
:root{--bg:#f9f9f9;--top:#fff;--left:#e8e8e8;--right:#ddd;--edge:#c3c2c5;--ink:#5c5c63;--ink-hi:#9a9aa0}
.cube{transform-style:preserve-3d;animation:wave 1.8s ease-in-out infinite alternate;animation-delay:calc((var(--x) + var(--y)) * -120ms)}
.cube .face{outline:1px solid var(--edge)}
@keyframes wave{from{transform:translateZ(0)}to{transform:translateZ(calc(var(--h) * 28px))}}
.status{font:500 17px/1.3 "Inter",system-ui;letter-spacing:-.005em;
  background:linear-gradient(90deg,var(--ink) 0 40%,var(--ink-hi) 50%,var(--ink) 60% 100%);
  background-size:250% 100%;-webkit-background-clip:text;color:transparent;animation:shimmer 2.2s linear infinite}
@keyframes shimmer{from{background-position:100% 0}to{background-position:-150% 0}}
.status.swap{animation:blurIn .4s cubic-bezier(.45,0,.55,1)}
@keyframes blurIn{from{filter:blur(6px);opacity:0}to{filter:blur(0);opacity:1}}
```
An SVG or Three.js grid with `h = sin(x*k + y*k2 + t)` per cell reproduces the ripple. Change `k`/`k2` per status for the different formations.

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Restrained monochrome isometric object with exact hairlines. |
| Originality | 7 | Fresh take on the AI "thinking" shimmer, with a heightfield in place of dots. |
| Usability | 7 | Staged copy informs, but the shimmer contrast and faint object are weak. |
| Craft | 8 | Consistent lighting, a blur-in swap and calm continuous motion. |

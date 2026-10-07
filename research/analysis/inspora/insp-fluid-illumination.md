---
id: insp-fluid-illumination
source: inspora
category: Motion
status: analyzed
title: "fluid illumination"
creator: "sasha birukoff"
styles: [aurora-glow, gradient-mesh, micro-interaction]
patterns: [morphing-container, loading-indicator, inner-glow-edge, dot-ring-spinner, label-fade-on-collapse, aspect-ratio-morph-sequence]
mode: light
palette: ["#f7f7f7", "#1c1e5a", "#3e37ae", "#605ad7", "#7a68e4", "#a797f4", "#e2d1f6", "#ffffff"]
type_families: ["Inter / SF Pro Text (likely)"]
type_class: [neo-grotesk]
radius_px: [120, 50]
motion: {durations_s: [0.53, 0.33, 0.17, 0.47], easing: [ease-in-out], loop: true}
scores: {aesthetics: 9, originality: 7, usability: 6, craft: 8}
craft_signals: [dark-core-bright-feathered-edge, pink-white-rim-1-to-2px, gradient-centre-tracks-shape, spinner-stays-centred-through-morphs, label-fades-before-shrink, symmetric-easing-every-segment]
anti_patterns: [white-label-near-pale-edge-2-51, low-edge-definition-1-33]
---
# fluid illumination — sasha birukoff

## 1. Snapshot
- **Subject:** A 6.95 s, 2560×1702 loop of a single glowing indigo-violet card that morphs from a wide pill-ish banner ("Autonomous demos" + dot spinner) to a small square, a tall portrait card, a larger square and back to the banner.
- **Why it's remarkable:** The fill behaves like light inside frosted glass — a dark navy core with edges that bloom to lavender and pink-white — and the glow re-centres continuously as the container changes aspect ratio, so the shape seems to contain living fluid.

## 2. Composition & layout
- Container always centred on a #f7f7f7 field.
- States (from sheet; ×4 scale): wide banner ≈1940×1030 px with ≈120 px radius; small square ≈590×590 (key frame) with ≈50 px radius; portrait ≈860×1200; mid square ≈1170×1160.
- Banner content: spinner at ≈160 px from the left edge, vertically centred; label "Autonomous demos" right-aligned ≈130 px from the right edge.
- In compact states the spinner moves to the exact centre and the label is hidden.

## 3. Typography
- Single label in a neo-grotesk (Inter / SF-like), ≈60 px regular white, sentence case.
- No other type — the motion carries the message.

## 4. Colour
| Hex | Role | Share (key frame) |
|---|---|---|
| #f7f7f7 | page | 92% |
| #1c1e5a / #3e37ae | dark core of the glow | 1% |
| #605ad7 / #4742bb | mid indigo | 2.5% |
| #7a68e4 / #8c81f0 | violet transition | 1.6% |
| #a797f4 / #b8a2f6 | lavender edge | 2% |
| #e2d1f6 / #ccbbf7 | pink-white rim bloom | 1% |
| #ffffff | spinner dots, label, rim stroke | — |

WCAG (contrast.py):
- White on core #1c1e5a: 15.19:1; on mid #605ad7: 5.33:1.
- White near the lavender edge #a797f4: **2.51:1** — in the banner the label sits close to the right edge where the glow lightens, which weakens it.
- Rim #e2d1f6 vs. page #f7f7f7: **1.33:1** — the container boundary is defined by the inner colour, not the edge.

## 5. Depth & material
- Inverted vignette: darkest in the centre, brightest at the edges — the opposite of a typical shadowed card, which reads as back-lit glass or a lightbox.
- A crisp 1–2 px white/pale-pink rim inside the edge, then ≈60–80 px of feathered lavender before the core.
- Gradient is not concentric: a bluer lobe sits upper-left and a violet lobe lower-right, and they drift between states.
- No drop shadow; glow does not spill outside the shape.

## 6. Components & patterns
- **Morphing container** for an agent/demo loading state (banner → compact → portrait → banner).
- **Dot-ring spinner:** 8 white dots (≈20 px) in a ≈100 px ring with two gaps, implying rotation.
- **Label collapse:** "Autonomous demos" fades out as the banner shrinks and fades back as it re-expands (at 6.56 s it is mid-fade).

## 7. Motion
Measured (m0_motion.json): 6.95 s at 60 fps, motion_fraction 0.22, seamless_loop_likely true, 4 segments, median 0.40 s.
- 2.13–2.67 s (0.53 s, peak 0.53): banner collapses to the small square.
- 3.63–3.97 s (0.33 s, peak 0.45): square grows to portrait.
- 5.03–5.20 s (0.17 s, peak 0.50): portrait reflows to the mid square.
- 6.23–6.70 s (0.47 s, peak 0.46): expands back to the banner.
All four segments are symmetric ease-in-out (peaks 0.45–0.53) — morphs feel fluid rather than springy. Holds between morphs (≈1.0–1.5 s) let the inner gradient drift slowly below the motion threshold.

## 8. Brand system
n/a — not a brand system. Identity cues: indigo-to-lavender "illumination" palette as an AI/agent signature.

## 9. UX
- Communicates "working, adapting" well; the shape change could map to different agent tasks.
- Spinner remains centred during compact states, so the loading signal persists.
- Risks: on a light page the edge has almost no contrast with the background; the label near the bright edge drops to 2.51:1; the morph alone does not say what changed.

## 10. Craft signals
- Darkest value in the centre, lightest at the edge.
- A thin bright rim sits inside a feathered glow band.
- The gradient re-centres with every aspect change rather than stretching.
- The label fades out before the container shrinks below its width, and back in after it expands.
- Corner radius scales with container size (≈50 px small, ≈120 px large) instead of staying fixed.
- All morphs use symmetric easing with durations from 0.17 to 0.53 s.

## 11. Reproduction recipe
```css
:root{--page:#f7f7f7;--core:#1c1e5a;--mid:#605ad7;--violet:#7a68e4;--edge:#b8a2f6;--rim:#f4e9fb;
  --ease:cubic-bezier(.65,0,.35,1)}
.illum{position:relative;border-radius:clamp(48px,6vw,120px);overflow:hidden;
  background:
    radial-gradient(60% 55% at 45% 45%,var(--core) 0,transparent 70%),
    radial-gradient(50% 50% at 25% 25%,#4a6cf0 0,transparent 70%),
    radial-gradient(55% 55% at 75% 80%,var(--violet) 0,transparent 70%),
    var(--mid);
  box-shadow:inset 0 0 0 1.5px var(--rim),inset 0 0 70px 30px var(--edge);
  transition:width .5s var(--ease),height .5s var(--ease),border-radius .5s var(--ease)}
.illum[data-state=banner]{width:970px;height:515px}
.illum[data-state=compact]{width:295px;height:295px}
.illum[data-state=portrait]{width:430px;height:600px}
.illum .label{color:#fff;transition:opacity .2s ease}
.illum[data-state=compact] .label,.illum[data-state=portrait] .label{opacity:0}
.spinner{width:50px;height:50px;background:radial-gradient(circle,#fff 4px,transparent 5px) 0 0/16px 16px;animation:spin 1.2s steps(8) infinite}
@keyframes spin{to{transform:rotate(1turn)}}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 9 | Lush inverted-vignette glow with a delicate rim; very refined. |
| Originality | 7 | Morphing glowing containers are trending; the backlit-edge treatment is the distinct part. |
| Usability | 6 | Clear loading signal, but weak edge definition and label contrast near the rim. |
| Craft | 8 | Gradient re-centres per shape, radius scales, consistent symmetric timing. |

---
id: insp-holographic-card
source: inspora
category: Illustration
status: analyzed
title: "holographic card"
creator: "@matiNotFound"
styles: [dark-premium, generative-particle, micro-interaction, x-holographic-foil]
patterns: [cursor-tilt-card, pointer-reveal-shader, collectible-edition-card, contour-line-foil, fractal-hero-glyph, hint-microcopy]
mode: dark
palette: ["#07080a", "#151518", "#231e26", "#3d2d40", "#425766", "#e4e4e7"]
type_families: ["Inter / Geist-style neo-grotesk (likely)", "spaced monospace caption (likely Geist Mono / JetBrains Mono)"]
type_class: [neo-grotesk, mono]
radius_px: [30]
motion: {durations_s: [0.7, 0.93, 0.63], easing: [ease-in-out, ease-out], loop: true}
scores: {aesthetics: 9, originality: 7, usability: 6, craft: 9}
craft_signals: [foil-hidden-until-pointer, contour-lines-not-flat-gradient, sierpinski-depth-in-foil-only, hairline-card-rim, corner-crosshair-registration-marks, mono-metadata-row, tilt-returns-to-rest]
anti_patterns: [hint-text-below-3-to-1, foil-washes-footer-label, hover-only-reveal]
---
# holographic card — @matiNotFound

## 1. Snapshot
- **Subject:** A 6.16 s screen capture (2490×1716, 120 fps) of a WebGPU trading-card object, "vgpu / Holographic / Light, computed.", that tilts toward the cursor. A rainbow contour-line foil blooms under the pointer.
- **Why it's remarkable:** At rest the card is almost entirely achromatic, with a faint triangle outline (frames t=0.34 s and t=5.82 s). All colour and the Sierpinski detail exist only where the light hits, so the interaction *is* the reveal.

## 2. Composition & layout
- **Card:** The card is centred and spans about x 800→1690 and y 212→1490 in source px, so it is roughly 885×1275 px. The ratio is about 0.69, close to a 63×88 mm trading-card proportion. The surrounding black is about 32% of width on each side.
- **Internal grid:** The inset is about 70 px. The wordmark sits top-left (~42 px cap height in source) with a "+" glyph top-right. The triangle glyph is centred at about 40% of card height and is ~545 px wide. The title block is anchored lower-left at ~74% height. A footer metadata row ("EDITION 001" left, "WEBGPU" right) sits about 75 px from the bottom.
- **Registration marks:** Four tiny "+" crosshairs sit at the corners of the art zone, like print marks.
- **Hint:** "MOVE TO REVEAL" is centred about 200 px below the card.

## 3. Typography
- **Wordmark and title:** a neo-grotesk close to Inter Display or Geist. "Holographic" is about 52 px source, Regular/Medium, tracking about −0.01 em. "vgpu" is about 48 px Medium, all lowercase.
- **Subline:** "Light, computed." is about 24 px Regular in grey.
- **Metadata:** a monospace face at about 17 px, uppercase, tracking about +0.2 em. The same style is used for "MOVE TO REVEAL". Mono is reserved for system and meta text, sans for names.
- **Scale:** 52 / 24 / 17, with a wide 2.2× jump from title to subline that keeps a poster feel.

## 4. Colour
| Hex | Role | Share (key frame) |
|---|---|---|
| #07080a | page void | 74% |
| #151518 | card surface | 17% |
| #231e26 / #3d2d40 | foil in magenta-violet shadow tones | 6% |
| #425766 | foil in teal/cyan tones | 3% |
| #e4e4e7 (est.) | title and wordmark | <1% |

The foil hue runs a full spectrum (magenta → violet → blue → cyan → green → amber) across concentric contours. It is not a fixed palette; hue is a function of the angle to the pointer.

WCAG checks:
- Title #e4e4e7 on #151518 is 14.36:1.
- Subline #8b8b90 on #151518 is 5.37:1.
- Mono meta #a1a1a6 is 7.08:1.
- "MOVE TO REVEAL" (~#4a4b50 on #07080a) is **2.3:1 (fails)**.
- The resting triangle stroke (~#2e2f33 on the card) is 1.36:1. That is deliberate but invisible on poor displays.

## 5. Depth & material
- **Tilt:** The card has a real 3D tilt of roughly ±6–8° on both axes, visible as trapezoidal edges in frames 1.03 s and 3.76 s.
- **Shadow and rim:** A soft ambient shadow falls below the card (about 40 px blur, offset downward). A 1 px lighter rim (~#2a2a2e) defines the edge against the void.
- **Foil:** Thin iso-lines (≈1.5 px, ~6 px pitch) warp around the pointer like a fingerprint or interference pattern, which reads as diffraction foil rather than a flat CSS rainbow.
- **Fractal detail:** The Sierpinski subdivisions appear only inside lit areas, so the "print" seems embossed under a clear varnish.

## 6. Components & patterns
- Collectible or edition card (title, tagline, edition number, tech badge).
- Cursor-tracked tilt plus a specular/iridescent reveal mask.
- Instructional microcopy below the hero.
- Plus button affordance top-right (unexplained; likely flips or expands the card).

## 7. Motion
These values are measured from `m0_motion.json`:
- Duration is 6.16 s at 120 fps. Motion fraction is 0.36, and `seamless_loop_likely` is true (first/last diff 0.10).
- There are three motion bursts, each matching a cursor sweep:
  - 1.17–1.87 s (0.70 s, peak 0.50, symmetric ease-in-out);
  - 3.00–3.93 s (0.93 s, peak 0.34, ease-out);
  - 4.70–5.33 s (0.63 s, peak 0.45, ease-in-out).
- The median segment is 0.70 s.

Between bursts the card holds still, so the tilt is damped (spring/lerp) toward the pointer rather than continuously animated. When the pointer leaves (t≈5.8 s) the foil fades fully and the card settles flat. My estimate is that the foil fade lags the tilt by about 0.1–0.2 s.

## 8. Brand system
n/a — this is not a brand system. Identity cues are the lowercase "vgpu" wordmark, the "Edition 001" numbering that implies a series, and the tagline voice "Light, computed."

## 9. UX
- **Affordance:** The pointer-reveal is self-explaining once touched, and "Move to reveal" primes it.
- **Risks:**
  - Touch and keyboard users get no hover. The design needs a gyro or auto-sweep fallback.
  - The hint text fails contrast.
  - The foil passes over the "WEBGPU" label, dropping it to near illegibility in the key frame.
  - `prefers-reduced-motion` should freeze the tilt and keep a static foil.

## 10. Craft signals
- The resting state is a 1-colour line drawing, and colour appears only within ~400 px of the pointer.
- The foil is built from contour iso-lines (~6 px pitch), not a smooth gradient.
- Fractal subdivision is visible only inside the lit mask, which gives two levels of detail.
- Four "+" registration marks sit at the art-zone corners, plus a "+" button that echoes them.
- The mono uppercase meta row is split left/right on the same baseline.
- The card returns to flat (frame 5.82 s) with no residual skew.

## 11. Reproduction recipe
```css
:root{--void:#07080a;--card:#151518;--rim:#2a2a2e;--ink:#e4e4e7;--ink-2:#8b8b90;--r:30px;--mx:50%;--my:50%;--rx:0deg;--ry:0deg}
.card{aspect-ratio:63/88;width:min(360px,80vw);border-radius:var(--r);background:var(--card);
  box-shadow:inset 0 0 0 1px var(--rim),0 30px 60px -20px #000;
  transform:perspective(1200px) rotateX(var(--rx)) rotateY(var(--ry));transition:transform .7s cubic-bezier(.22,1,.36,1);position:relative;overflow:hidden}
.card::after{content:"";position:absolute;inset:0;mix-blend-mode:color-dodge;opacity:var(--o,0);transition:opacity .4s ease-out;
  background:repeating-radial-gradient(circle at var(--mx) var(--my),transparent 0 5px,rgba(255,255,255,.18) 5px 6px),
    conic-gradient(from 0deg at var(--mx) var(--my),#ff3ea5,#7a5cff,#2fa8ff,#2fffc8,#d6ff5c,#ff3ea5);
  -webkit-mask:radial-gradient(420px circle at var(--mx) var(--my),#000,transparent 70%)}
.card:hover::after{--o:1}
.meta{font:500 11px/1 "Geist Mono",ui-monospace;letter-spacing:.2em;text-transform:uppercase;color:#a1a1a6}
@media (prefers-reduced-motion:reduce){.card{transform:none}}
```
JS: on `pointermove`, set `--mx/--my` from the local % position and `--ry=(x-.5)*14deg`, `--rx=(.5-y)*14deg`. Reset on `pointerleave`.

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 9 | Restrained black card where light is the only colour; contour foil is gorgeous. |
| Originality | 7 | Holo cards are a known trend; the contour-line foil and fractal-in-light reveal are the fresh parts. |
| Usability | 6 | Hover-only, the hint fails contrast, and the foil obscures a label. |
| Craft | 9 | Registration marks, mono meta, clean rest state and damped tilt are all precise. |

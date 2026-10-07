---
id: insp-2-5
source: inspora
category: Motion
status: analyzed
title: "Glowing particle burst"
creator: "@tojawuzik"
styles: [dark-premium, generative-particle, aurora-glow]
patterns: [particle-orb-loader, shimmer-text-sweep, loading-indicator, inset-device-corner, glow-spill-on-surface]
mode: dark
palette: ["#101012", "#16171b", "#22242a", "#727b8a", "#c9d3e8", "#ffffff"]
type_families: ["SF Pro Display / Inter Display Regular (likely)"]
type_class: [neo-grotesk]
radius_px: [80]
motion: {durations_s: [4.9, 1.68], easing: [linear], loop: true}
scores: {aesthetics: 8, originality: 6, usability: 6, craft: 8}
craft_signals: [orb-glow-lights-panel-surface, shimmer-hue-matches-orb, cool-blue-white-not-pure-white, double-bezel-corner, radial-streak-particles, seamless-loop]
anti_patterns: [resting-label-2-to-1, decorative-loader-without-progress]
---
# Glowing particle burst — @tojawuzik

## 1. Snapshot
- **Subject:** A 5.03 s, 1920×1920, 30 fps loop. A glowing blue-white particle sphere (~550 px) sits in the bottom-left corner of a dark rounded panel beside a large "Calculating." label whose letters are lit by a sweeping shimmer.
- **Why it's remarkable:** A "thinking" state as hero. The orb's light physically spills onto the panel surface (a lit radial area around it), and the text shimmer uses the orb's exact cool tint. The loader and the label read as one light source.

## 2. Composition & layout
- **Panel:** The panel corner is the frame: an inset rounded rectangle with radius ≈80 px, its left edge at x≈295 and bottom at y≈1640. A second outer bezel line sits ~30 px outside it, like a device edge. The top ~50% is empty dark panel.
- **Orb:** centred at about (655, 1255), diameter ≈550 px, about 360 px from the panel's left edge and about 110 px from its bottom.
- **Label:** "Calculating." starts at x≈1040 (≈110 px gap after the orb) and runs off the right edge. Its baseline is aligned to the orb's horizontal centre line (x-height centred on y≈1270).
- **Overall:** bottom-left weighted, with the big empty dark space above giving a cinematic, quiet frame.

## 3. Typography
- A neo-grotesk Regular (400), close to SF Pro Display or Inter Display. Cap height is about 140 px (font size ≈195 px) with tight tracking (~−0.02 em).
- The sentence-case word ends with a full stop instead of an ellipsis, which is calmer and more declarative.
- The colour is a gradient across the word: resting glyphs #4a4b50, and the shimmer band peaks at #c9d3e8.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #101012 | outer background | 84.5% |
| #16171b / #22242a | panel surface, lit spill area | 9.4% |
| #727b8a | glow halo mid-tone | 6.2% |
| #c9d3e8 | shimmer peak on text, particle tint | — |
| #ffffff | orb core | — |

WCAG checks:
- Resting label (#4a4b50 on #16171b) is **2.06:1**, and the lighter resting parts (#5a5c62) are 2.68:1. Both fail.
- The shimmer peak (#c9d3e8) is 11.91:1. The word is fully legible only under the sweep.
- The halo grey #727b8a is 4.45:1 on the background.

## 5. Depth & material
- **Orb:** volumetric particles. Hundreds of short radial streaks (2–6 px wide, 10–40 px long) on a sphere shell, with a hot white core about 180 px across. A soft halo (~150 px falloff) tints the panel blue-grey.
- **Panel:** a subtle top-to-bottom gradient. The lower area near the orb is lighter (#22242a) than the top (#121316), as if lit by the orb, with a 1–2 px edge highlight on the inner bezel.
- **Bezels:** two nested rounded rectangles (inner panel radius ≈80 px, outer ≈110 px) read as a device frame, implying a phone or watch UI.

## 6. Components & patterns
- Loading indicator plus status label, with a shimmer (skeleton-like "light sweep") on text.
- A particle sphere as an "AI is computing" metaphor.
- Glow spill as an ambient-light pattern.

## 7. Motion
Measured values (`m0_motion.json`):
- One continuous segment from 0.10 to 5.00 s (4.9 s) with shape "continuous/linear" and energy CV 0.21, so very steady.
- Motion fraction is 0.98, and `seamless_loop_likely` is true (first/last diff 1.05).
- The particles stream outward constantly at an even rate, with no pulses.

Shimmer (estimated from frames at 0.56 s spacing): the bright band sits on "lating." at 0.84 s, 2.52 s and 4.19 s and is off-word at 0.28, 1.96 and 3.64 s. That suggests a sweep period of about 1.68 s, so 3 sweeps per 5.03 s loop, which divides evenly and preserves the seamless loop. The band is roughly 4 letters (~450 px) wide and travels left to right.

## 8. Brand system
n/a — this is not a brand system.

## 9. UX
- **Strengths:** It communicates "busy, working" clearly; the steady linear motion is non-alarming.
- **Weaknesses:** It is indeterminate, with no progress or ETA. Long waits need stage labels.
- **Accessibility:**
  - The resting text is 2:1. Keep a minimum resting colour of about #8a8f99 (≥4.5:1) and let the shimmer add on top.
  - Provide `aria-live="polite"` status text.
  - Under reduced motion, stop the shimmer.

## 10. Craft signals
- The orb's light spill brightens the panel surface locally (#16171b → #22242a). It is not a separate drop shadow.
- The shimmer colour (#c9d3e8) matches the particles' cool tint rather than using neutral white.
- The shimmer period (~1.68 s) divides the 5.03 s loop 3× for a seamless repeat.
- The label's x-height is centred on the orb's centre line.
- The double bezel corner frames the UI as hardware.

## 11. Reproduction recipe
```css
:root{--bg:#101012;--panel:#16171b;--panel-lit:#22242a;--ink-rest:#5a5c62;--ink-peak:#c9d3e8;--r-panel:80px}
.panel{border-radius:var(--r-panel);background:radial-gradient(60% 50% at 20% 80%,var(--panel-lit),var(--panel) 70%);
  box-shadow:0 0 0 1px #1d1e22,0 0 0 30px #0d0d0f,0 0 0 31px #1a1b1f}
.orb{width:280px;aspect-ratio:1;border-radius:50%;
  background:radial-gradient(circle,#fff 0 12%,#cfe0ff 22%,rgba(160,185,230,.35) 48%,transparent 52%);
  filter:drop-shadow(0 0 40px rgba(170,195,240,.45))}  /* swap for a canvas particle shell in production */
.shimmer{font:400 96px/1 "Inter Display",system-ui;letter-spacing:-.02em;color:transparent;
  background:linear-gradient(90deg,var(--ink-rest) 0 40%,var(--ink-peak) 50%,var(--ink-rest) 60% 100%) 0 0/250% 100%;
  -webkit-background-clip:text;background-clip:text;animation:sweep 1.68s linear infinite}
@keyframes sweep{from{background-position:100% 0}to{background-position:-50% 0}}
@media (prefers-reduced-motion:reduce){.shimmer{animation:none;color:#8a8f99;background:none}}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Cinematic dark frame and a beautiful, cool particle light. |
| Originality | 6 | Orb loader plus shimmer label is a familiar AI-UI idiom; the light-spill is the nice touch. |
| Usability | 6 | Clear "busy" state, but the resting label fails contrast and there is no progress. |
| Craft | 8 | Hue-matched shimmer, seamless loop and surface lighting are carefully done. |

---
id: insp-dessn-welcome-envelope
source: inspora
category: Motion
status: analyzed
title: "DESSN welcome envelope"
creator: "@eminimnim"
styles: [cinematic-3d, physical-material, organic-blob]
patterns: [welcome-onboarding-film, wax-seal-reveal, layered-pour-concentric-rings, stamp-press-moment, macro-to-wide-pullback, logo-as-seal-shape, patterned-brand-backdrop]
mode: light
palette: ["#dbdad8", "#c0c0be", "#022220", "#07302d", "#41837c", "#e8952a", "#1fa04a", "#b6a995"]
type_families: ["geometric/neo-grotesk wordmark, close to Neue Haas Grotesk Display Medium (likely)"]
type_class: [neo-grotesk]
radius_px: [16]
motion: {durations_s: [1.03, 1.03, 0.6, 0.7, 0.5, 1.03, 0.97], easing: [ease-in-out, linear, ease-out, ease-in], loop: false}
scores: {aesthetics: 8, originality: 8, usability: 6, craft: 7}
craft_signals: [seal-colours-match-brand-palette, three-pour-layers-become-logo-rings, flower-seal-echoes-logomark, brass-stamp-specular-highlight, envelope-flap-line-continuous-across-shots, bookend-wide-shots]
anti_patterns: [low-resolution-768px-export, orange-on-teal-1-84]
---
# DESSN welcome envelope — @eminimnim

## 1. Snapshot
- **Subject:** A 17 s, 768×432 (30 fps) CG brand film: a "Welcome to DESSN" card slides into a white envelope on a green patterned table, then in macro, dark-green, teal and orange wax are poured in turn and pressed with a brass stamp into a flower-shaped seal.
- **Why it's remarkable:** The seal is not decoration — the three pours form concentric rings that become the brand's flower mark, so the onboarding moment literally manufactures the logo.

## 2. Composition & layout
- **Act 1 (0–3 s):** top-down shot; envelope ≈290×230 px centred-left on a saturated green (#1fa04a-ish) table printed with a teal outline flower pattern; card with "Welcome to" ≈14 px and the DESSN lockup ≈26 px, plus a thin red vertical rule at the card's left.
- **Act 2 (4.7–12.3 s):** macro low-angle on the flap: a thin grey flap line arcs across a #dbdad8 paper texture; the wax puddle sits on the line, centred, filling ≈50% of the width.
- **Act 3 (14–17 s):** pull back to top-down; the seal (≈50 px) sits on the flap point, with "DESSN" small bottom-left of the envelope.
- Shots share the flap line as a continuous visual thread.

## 3. Typography
- Wordmark "DESSN": uppercase neo-grotesk, medium weight, tight tracking (≈−0.01 em), in deep green; paired with a line-drawn four-petal/clover flower mark at cap height.
- "Welcome to" in a light-weight grotesk ≈55% of the wordmark's size, centred above it.
- Envelope corner lockup ≈9 px — small, quiet, stationery-like.
(The 768 px export prevents a confident font ID.)

## 4. Colour
| Hex | Role | Share (key frame) |
|---|---|---|
| #dbdad8 / #c0c0be / #cfcfcd | paper / envelope (lit and shadow) | 80% |
| #022220 / #07302d | outer wax ring, logo ink | 9% |
| #41837c | teal middle ring | 5% |
| #e8952a | orange inner flower | — |
| #1fa04a | green table backdrop | — (acts 1, 3) |
| #b6a995 | brass stamp | 3% |

WCAG (contrast.py):
- Logo ink #022220 on paper #dbdad8: 12.0:1; card text ≈#1f3b33 on #f2f2ef: 10.81:1.
- Teal ring vs. dark ring (#41837c on #07302d): 3.24:1 — readable as shape.
- Orange flower on teal (#e8952a on #41837c): **1.84:1** luminance contrast — the flower separates by hue, not lightness, so it would vanish in greyscale.

## 5. Depth & material
- Physically based wax: glossy specular streaks, viscous edge rolls and a soft contact shadow.
- Brass stamp: polished metal with environment reflections of the green set (≈10.4 s frame).
- Paper shows fine tooth texture and a scored flap line; macro depth of field blurs the far paper.
- The top-down shots use a vignette spotlight on the patterned table.

## 6. Components & patterns
- **Welcome kit** (card + envelope + seal) as an onboarding/brand ritual.
- **Concentric-ring seal:** dark green outer (wavy square), teal middle, orange five-petal flower, dark centre dot — the logo rebuilt as material.
- **Pour → pour → pour → press → reveal** sequence.
- Repeat pattern backdrop drawn from the same flower outline.

## 7. Motion
Measured (m0_motion.json): 17.0 s at 30 fps, motion_fraction 0.35, seamless_loop_likely false (first/last diff 69), 8 segments, median 0.83 s.
- 1.33–2.37 s (1.03 s, linear) and 2.90–3.93 s (1.03 s, symmetric): card slides in, flap folds/cut to macro.
- 5.10–5.20 s (0.1 s) and 5.67–6.27 s (0.60 s, symmetric): first pour start and spread.
- 9.67–10.37 s (0.70 s, peak 0.17, ease-out): stamp press — fast impact, slow settle.
- 11.60–12.10 s (0.50 s, peak 0.77, ease-in): stamp lifts away, accelerating.
- 12.90–13.93 s (1.03 s, linear) and 14.07–15.03 s (0.97 s, symmetric): camera pull-back to the wide reveal.
The pours themselves are slow and below threshold for long stretches — the film breathes between ≈1 s camera moves.

## 8. Brand system
n/a — not a brand guideline, but a strong identity piece:
- palette of deep green #022220, teal #41837c, orange #e8952a on warm paper;
- flower mark repeated as wordmark glyph, seal shape and table pattern;
- red hairline accent on the card;
- tone: crafted, ceremonial, tactile.

## 9. UX
- As onboarding content it sets expectations of care and craft; story is clear without words.
- Risks: 17 s is long for an in-product moment; at 768×432 the wordmark is soft; the colour layering relies on hue only.

## 10. Craft signals
- Each pour colour is a brand colour, and their order (dark → teal → orange) builds the logo's rings.
- Seal is placed exactly on the flap point in the wide shot.
- The flap line stays continuous across the macro and wide shots.
- Brass reflections carry the green of the set.
- Film is bookended by two top-down wides of the same envelope.

## 11. Reproduction recipe
```css
:root{--paper:#e6e5e2;--ink:#022220;--teal:#41837c;--orange:#e8952a;--table:#1fa04a}
.seal{width:120px;aspect-ratio:1;border-radius:38% 42% 40% 44%/44% 38% 42% 40%;
  background:
    radial-gradient(circle,var(--ink) 0 7%,transparent 7.5%),
    radial-gradient(circle,var(--orange) 0 26%,transparent 27%),
    radial-gradient(circle,var(--teal) 0 52%,transparent 53%),
    var(--ink);
  box-shadow:inset 0 4px 6px rgba(255,255,255,.25),inset 0 -6px 10px rgba(0,0,0,.35),0 6px 12px rgba(0,0,0,.25);
  animation:press .7s cubic-bezier(.2,.9,.3,1) both}
@keyframes press{0%{transform:scale(1.25);filter:blur(2px)}60%{transform:scale(.96)}100%{transform:scale(1);filter:none}}
.table{background:var(--table) url(flower-outline.svg) 0 0/220px}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Rich tactile materials and a confident three-colour brand palette. |
| Originality | 8 | Building the logo from layered wax pours is a memorable idea. |
| Usability | 6 | Communicates welcome well, but long and low-res for a product moment. |
| Craft | 7 | Convincing simulation and continuity; export resolution undercuts detail. |

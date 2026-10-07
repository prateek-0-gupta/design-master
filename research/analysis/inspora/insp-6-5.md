---
id: insp-6-5
source: inspora
category: Illustration
status: analyzed
title: "Liquid metal"
creator: "Brett (@BrettFromDJ)"
styles: [physical-material, minimal-swiss, micro-interaction, y2k-chrome]
patterns: [quantity-stepper, chrome-rim-primary-button, animated-env-reflection, recessed-segment-track, label-value-header, ghost-disabled-decrement]
mode: light
palette: ["#d9d9d9", "#f2f2f2", "#ebebeb", "#dadada", "#b7b7b7", "#97989a", "#000000"]
type_families: ["Neue Haas Grotesk / Helvetica Now Display (likely)"]
type_class: [neo-grotesk]
radius_px: [64, 40, 36]
motion: {durations_s: [4.0], easing: [linear], loop: true}
scores: {aesthetics: 8, originality: 7, usability: 6, craft: 8}
craft_signals: [rotating-specular-on-rim-only, chromatic-fringe-in-reflection, one-chromed-element-per-view, tight-negative-tracking-on-numerals, shared-track-tray, decrement-styled-as-unavailable]
anti_patterns: [label-contrast-1-8, glyph-on-chrome-low-contrast, motion-without-meaning]
---
# Liquid metal — @BrettFromDJ

## 1. Snapshot
- **Subject:** A 4.0 s, 1440×1024 looping clip of a minimal "Credits" stepper card (− / 2k / +) whose + button has a polished liquid-chrome bezel with a reflection that slowly orbits the rim.
- **Why it's remarkable:** All the motion is in one material detail. The environment reflection travels around the rounded-rectangle rim while geometry, layout and values stay still. The primary action is singled out by material, not colour.

## 2. Composition & layout
- **Card:** ~805×425 px (x≈317–1122, y≈300–723), radius ~64 px, #f2f2f2 on a #d9d9d9 canvas, centred.
- **Header row:** "Credits" left and "$30.00" right at y≈390, with ~56 px side padding.
- **Track:** a recessed tray (~690×200 px, radius ~48 px, #ebebeb) holding three equal ~205×175 px segments with a ~12 px gutter:
  - − button (raised, matte);
  - "2k" value cell (flat);
  - + button (chrome bezel).
- **Spacing:** card padding (~56 px) is about 4.5× the segment gutter (~12 px).

## 3. Typography
- A neo-grotesk with tight tracking, close to Neue Haas Grotesk Display or Helvetica Now:
  - "Credits" ~52 px Regular in light grey #b7b7b7;
  - "$30.00" ~52 px Regular black, tracking about −0.03 em (digits nearly touching);
  - "2k" ~48 px black.
- Glyphs: − and + are 4 px-stroke lines in #97989a (+) and #dadada (−, effectively disabled).

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #d9d9d9 | canvas | 81% |
| #f2f2f2 | card | 18% |
| #ebebeb | tray / value cell | <1% |
| #dadada | decrement glyph (disabled look) | — |
| #b7b7b7 | label "Credits" | — |
| #97989a | + glyph | — |
| #000000 | price and quantity | — |
| (chrome) | white → near-black, with faint blue/amber fringes | — |

WCAG:
- Black on #f2f2f2 is 18.76:1.
- "Credits" #b7b7b7 on #f2f2f2 is **1.79:1 (fails)**.
- The + glyph on chrome is **2.11:1**.
- The − glyph is 1.17:1, which suggests it is intentionally disabled.
- Card vs canvas is 1.26:1, so the card is defined by its value step alone.

This is a fully achromatic system. The only "colour" is the slight prismatic fringe in the chrome highlights.

## 5. Depth & material
- **− button:** matte, raised. A 1 px light border, a soft inner gradient and a ~10 px soft shadow.
- **Value cell:** flat, slightly darker than the card (recessed).
- **+ button:**
  - a thick (~10 px) polished chrome bezel with high-contrast streaks (white to #222) and tiny chromatic fringes;
  - a brushed-satin centre with a diagonal sheen;
  - a larger drop shadow (~30 px blur) that makes it the highest element.
- **Tray:** an inset with a 1 px inner shadow line.

## 6. Components & patterns
- **Quantity stepper** with a price header. The price "$30.00" presumably updates per 2k step (not shown).
- **Visual hierarchy by material:** chrome marks primary (+), matte marks secondary (−) and flat marks display (value).
- The decrement appears disabled (at minimum quantity), shown by a near-invisible glyph.

## 7. Motion
Measured: 30 fps, duration 4.0 s, motion_fraction 0.00 (no segment exceeds the 0.35 threshold), mean energy 0.06, first/last diff 0.04, so seamless_loop_likely is true.

The only motion is the environment reflection on the + bezel, which is too small in area to register as motion energy. Comparing frames f0/f2/f4/f6, the bright streaks migrate clockwise around the rim (top-right at 0.2 s, then right edge, then top-left, then bottom). That is about one full orbit per 4 s loop, at what looks like constant (linear) speed. The satin centre sheen shifts subtly. Nothing else moves.

## 8. Brand system
n/a — not a brand system. The tight-tracked grotesk on achromatic greys reads as a premium fintech or AI-credits product.

## 9. UX
- **Positives:** A clear primary action (+), a simple header pair (label/value), and generous targets (~205×175 px).
- **Negatives:**
  - The label at 1.79:1 and the + glyph at 2.11:1 are too faint.
  - The disabled state of − relies solely on a near-invisible glyph.
  - Looping shimmer on an idle control draws attention without conveying state. A reduced-motion fallback is needed.

## 10. Craft signals
- The reflection is confined to the bezel ring; the button face uses a separate, slower sheen.
- Chrome highlights carry subtle blue and amber fringes, imitating dispersion.
- Only one element in the view is chromed, which reserves the material for the primary action.
- Numerals are tightly tracked ("$30.00") and baseline-aligned with the label.
- All three segments share one recessed tray with a ~12 px uniform gutter.
- The corner radii nest: card ~64 > tray ~48 > buttons ~36 px.

## 11. Reproduction recipe
```css
:root{--canvas:#d9d9d9;--card:#f2f2f2;--tray:#ebebeb;--muted:#8a8a8a;/* raise label to 3.5:1 */}
.card{background:var(--card);border-radius:64px;padding:56px}
.tray{background:var(--tray);border-radius:48px;padding:12px;display:grid;grid-template-columns:repeat(3,1fr);gap:12px}
.seg{border-radius:36px;height:175px;display:grid;place-items:center;font:400 48px/1 "Neue Haas Grotesk Display",Inter;letter-spacing:-.03em}
.chrome{position:relative;background:linear-gradient(135deg,#dcdcdc,#f4f4f4 45%,#d2d2d2);box-shadow:0 20px 30px -10px rgb(0 0 0/.25)}
.chrome::before{content:"";position:absolute;inset:0;border-radius:inherit;padding:10px;
  background:conic-gradient(from var(--a),#fff 0 8%,#222 12%,#eee 20%,#9ab 26%,#fff 34%,#333 45%,#fff 55%,#ccd 70%,#111 80%,#fff 92%);
  -webkit-mask:linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);-webkit-mask-composite:xor;mask-composite:exclude;
  animation:orbit 4s linear infinite}
@property --a{syntax:"<angle>";inherits:false;initial-value:0deg}
@keyframes orbit{to{--a:360deg}}
@media (prefers-reduced-motion:reduce){.chrome::before{animation:none}}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Restrained greyscale with one jewel-like chrome detail. Very refined. |
| Originality | 7 | The liquid-chrome trend, used with unusual restraint (rim-only, single element). |
| Usability | 6 | Clear primary and big targets, but faint label and glyphs and decorative idle motion. |
| Craft | 8 | Nested radii, a seamless 4 s orbit and dispersion fringes. Contrast is neglected. |

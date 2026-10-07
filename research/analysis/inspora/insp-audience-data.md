---
id: insp-audience-data
source: inspora
category: Product
status: analyzed
title: "audience data"
creator: "@moguzbulbul"
styles: [minimal-swiss, corporate-clean, micro-interaction]
patterns: [sentiment-gradient-slider, kpi-three-up-footer, heatmap-tile-grid, delta-badge, staggered-card-reveal, skeleton-to-content-fade]
mode: light
palette: ["#eeeeee", "#ffffff", "#61c1fb", "#aae0ed", "#f07ca0", "#a6e8b4", "#111111", "#6b6b6b"]
type_families: ["Inter (likely)"]
type_class: [neo-grotesk]
radius_px: [20, 9999, 4]
motion: {durations_s: [0.2, 0.17, 3.0], easing: [ease-in-out, ease-out], loop: true}
scores: {aesthetics: 7, originality: 5, usability: 6, craft: 7}
craft_signals: [gradient-fades-to-white-at-neutral, hollow-thumb-on-gradient, hairline-cell-dividers, tile-by-tile-heatmap-build, micro-sparkline-per-kpi]
anti_patterns: [percent-sign-before-number, green-delta-badge-low-contrast, cards-nearly-invisible-on-grey]
---
# audience data — @moguzbulbul

## 1. Snapshot
- **Subject:** A 3.0 s, 1600×1200 looping reveal of two analytics cards on light grey. The "Audience" card shows "%48 Positive" with a Critical-to-Loved gradient slider and a 3-up Positive/Neutral/Negative footer. The "Moosehead" card shows "9 Comment" with a +160% badge and a blue tile heatmap that builds in.
- **Why it's remarkable:** The sentiment bar uses a pink-to-white-to-green gradient whose neutral middle literally fades to the card colour, so "neutral" reads as absence. That is a compact and honest way to encode a diverging scale.

## 2. Composition & layout
- **Two cards side by side:** each about 598×462 px (left) and 598×468 px (right), at x≈184 and x≈817, with a gap of about 34 px. Centred vertically (y≈366 to 830) on a 1600×1200 canvas.
- **Inner padding:** about 34 px. The left card stacks label (y≈428), big number (≈486), slider (≈590), end labels (≈641), and a full-bleed 3-column footer (y≈675–830) split by 1 px #eee dividers.
- **Right card:** header row with name left and meta right, then title with badge, then a 5-column tile grid (each tile ≈96×42 px with a 6–8 px gap) over 3 rows, followed by a "Less / More Positive" legend bar.
- **Grid discipline:** the left text edge at x≈218 is shared by every element.

## 3. Typography
- Neo-grotesk close to Inter, Regular 400 throughout (no bold).
- **Sizes (native px):** hero number "%48" at about 58 px; "9 Comment" at about 46 px; KPI values at about 28 px; labels at about 22 px; captions ("Critical", "Loved") at about 17 px.
- Labels are mid-grey and values near-black, so hierarchy is by value. Tracking is neutral. Numerals are proportional.

## 4. Colour
| Hex | Role | Approx share |
|---|---|---|
| #eeeeee | page background | 73% |
| #ffffff | card surfaces | 24% |
| #61c1fb / ≈#79c8fa / #aae0ed | heatmap tiles, 3 intensity steps | ~1.5% |
| ≈#f07ca0 | "Critical" pink end of slider | <1% |
| ≈#a6e8b4 / #d2f3df | "Loved" green end, delta-badge fill | <1% |
| #111111 | values | <1% |
| ≈#6b6b6b | labels | <1% |

WCAG checks (contrast.py):
- Values #111 on white: **18.88:1**.
- Labels ≈#6b6b6b: **5.33:1**. The lighter meta text (≈#7a7a7a) is **4.29:1 (fails normal AA)**.
- Delta badge green text ≈#4cc76f on #e8f8ec: **1.96:1 (fail)**.
- The white card on #eeeeee is 1.16:1. Cards are defined only by this tiny luminance step, with no border or shadow.

## 5. Depth & material
- Flat. The cards have no shadow or border. The slider track has a soft blurred glow (the gradient appears feathered, like a blur of about 6 px). The thumb is a hollow white circle about 32 px with a 2 px pale-pink stroke, giving a glassy bead.

## 6. Components & patterns
- **Diverging sentiment slider:** pink → white → green track, position thumb, and end captions.
- **KPI footer:** 3 equal cells with label, value and a tiny step-sparkline glyph (about 30×14 px).
- **Heatmap tile grid:** five columns, three blue intensities, with a gradient legend.
- **Delta badge:** a pill with an up-arrow and "160%".

## 7. Motion
- Measured: 3.0 s at 60 fps. `motion_fraction` 0.13. Two segments: **0.20 s symmetric (peak 0.58)** at 0.0 s, and **0.17 s ease-out (peak 0.30)** at 0.63 s. `seamless_loop_likely: true`.
- **From frames (estimates):**
  - 0.17 s: content fading out to ghosted opacity.
  - 0.50 s: empty white cards (skeleton state).
  - 0.83 s: left card content fully in while the right card shows only a faint header, so a stagger of about 0.3 s.
  - 1.17 s: right title and badge are in.
  - 1.50–1.83 s: heatmap tiles pop in tile by tile in reading order (about 7 tiles by 1.5 s, all 15 by 1.83 s).
  - 2.17 s: the legend bar appears.
- Overall: an approximately 2 s staggered build with fast 0.17–0.2 s fades, then a hold.

## 8. Brand system
n/a — not a brand system. "Moosehead" is subject data (a podcast or show), not branding.

## 9. UX
- Glanceable: one hero number, one diverging bar and three supporting numbers.
- **Risks:**
  - "%48" puts the percent sign before the number (a locale quirk that hurts scanning).
  - "9 Comment" is not pluralised.
  - The green badge fails contrast.
  - The heatmap has no axis labels, so tiles are uninterpretable without hover.
  - Cards nearly vanish on #eee for low-vision users.

## 10. Craft signals
- The gradient's neutral midpoint is pure white, matching the card, so the scale diverges from "nothing".
- The KPI footer is full-bleed with 1 px dividers, while the content above keeps the 34 px inset (an intentional change of grid).
- The heatmap uses exactly three tints of one blue, plus the legend.
- The reveal order follows reading order: left card, then right title, then tiles left to right, then legend.

## 11. Reproduction recipe
```css
:root{--page:#eee;--card:#fff;--ink:#111;--ink-2:#6b6b6b;--line:#eeeeee;
  --neg:#f07ca0;--pos:#7fdc96;--b1:#c6e9fd;--b2:#79c8fa;--b3:#3db2f8;--r:20px}
.card{background:var(--card);border-radius:var(--r);padding:34px;font-family:Inter,sans-serif}
.hero{font:400 58px/1 Inter;letter-spacing:-.01em;color:var(--ink)}
.track{height:32px;border-radius:9999px;filter:blur(.5px);
  background:linear-gradient(90deg,var(--neg) 0%,#fff 40%,#fff 55%,var(--pos) 100%)}
.thumb{width:32px;height:32px;border-radius:50%;border:2px solid #f6c6d4;background:#fff8}
.kpis{display:grid;grid-template-columns:repeat(3,1fr);margin:0 -34px -34px;border-top:1px solid var(--line)}
.kpis>*+*{border-left:1px solid var(--line)}
.tile{height:42px;border-radius:4px;opacity:0;transform:scale(.9);animation:pop .17s cubic-bezier(.16,1,.3,1) forwards;animation-delay:calc(var(--i)*40ms + 1s)}
@keyframes pop{to{opacity:1;transform:none}}
.badge{background:#e8f8ec;color:#1f8a43;border-radius:8px;padding:2px 8px}  /* darker green passes */
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 7 | Quiet, balanced cards; the gradient bar is the one lovely moment. |
| Originality | 5 | Standard analytics cards; the neutral-is-white bar is the only twist. |
| Usability | 6 | Glanceable, but the %-prefix, the unlabelled heatmap and the green badge hurt. |
| Craft | 7 | Consistent insets and a careful reveal order; copy and contrast slips. |

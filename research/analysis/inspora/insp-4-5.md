---
id: insp-4-5
source: inspora
category: Motion
status: analyzed
title: "Gooey liquid effect"
creator: "@Jakubantalik"
styles: [organic-blob, micro-interaction, soft-3d, minimal-swiss]
patterns: [gooey-metaball-merge, radial-fab-menu, draggable-avatar-into-pill, input-button-fusion, stretchy-slider-thumb, component-showcase-page]
mode: light
palette: ["#f6f6f6", "#ffffff", "#e9e9e9", "#d0d0d0", "#a0a0a0", "#1a1a1a"]
type_families: ["Inter (likely)"]
type_class: [neo-grotesk]
radius_px: [9999, 28]
motion: {durations_s: [0.9, 1.67, 0.6, 0.57, 1.13], easing: [ease-out, ease-in], loop: true}
scores: {aesthetics: 8, originality: 8, usability: 7, craft: 8}
craft_signals: [metaball-bridge-between-shapes, white-on-f6-with-shadow-only, consistent-circle-diameters, thumb-stretches-in-drag-direction, placeholder-grey-matches-subtitle]
anti_patterns: [placeholder-and-subtitle-below-aa]
---
# Gooey liquid effect — @Jakubantalik

## 1. Snapshot
- **Subject:** A 10.4 s, 1700×1280 showcase of a "Liquid gooey" React library with four demos:
  - a radial FAB menu that blobs out of a "+";
  - an avatar dragged into a "Share" pill;
  - an email field that absorbs its arrow button;
  - a slider whose thumb stretches like liquid.
- **Why it's remarkable:** One metaball (goo) filter is applied consistently to four everyday controls, so separate shapes visibly fuse and tear apart.

## 2. Composition & layout
- **Header block:** A 120×120 px squircle app icon (radius about 28) holding a two-lobed blob logo, the title "Liquid gooey" at about 34 px, and a grey subtitle at about 32 px. The block is centred near the top (y≈60→310).
- **Stage:** Demos are swapped in the centre with a horizontal blur-wipe at t≈4 s.
- **Sizes:**
  - Email field: 664×168 px pill.
  - Arrow button: 146 px circle, with a 60 px gap.
  - Slider: 715×26 px track.
  - FAB satellites: about 146 px circles arranged in a diamond with about 190 px offsets.
  - Share pill: about 610×195 px with 110 px overlapping avatars.

## 3. Typography
- Inter (likely) throughout.
- **Title:** About 34 px Regular in #1a1a1a.
- **Subtitle and placeholder:** About 32–40 px Regular in grey (about #9a9a9a).
- **"Share":** About 40 px Regular.
- No bold anywhere, so the restraint lets the shapes perform.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #f6f6f6 | canvas | 98% |
| #ffffff | all controls (pill, circle, thumb) | — |
| #e9e9e9 / #d0d0d0 | slider track, shadows, icon blob | 1% |
| #a0a0a0 | subtitle / placeholder | <1% |
| #1a1a1a | title, icons, arrow | <1% |

The only saturated colour is in the avatar photos (magenta, cyan).

WCAG:
- Placeholder or subtitle #9a9a9a on #fff is **2.81:1**, and on #f6f6f6 it is **2.60:1** (both fail).
- The title is about 16:1.

## 5. Depth & material
- White shapes on #f6f6f6, separated by a soft long shadow (about 0 10px 40px rgba(0,0,0,.06)) plus a faint 1 px edge.
- The goo filter makes surfaces feel viscous: when two shapes are within about 40 px, a smooth neck bridges them (visible between the avatar and the pill at t=0.58 s, and between the field and the arrow at t=6.38 s).

## 6. Components & patterns
- **Radial FAB:** "+" rotates to "×". Four satellites (image, file, folder, close) bud off the centre circle.
- **Drag-to-merge:** An avatar is dragged by its grab handle into the Share pill's avatar stack and then pinched off again.
- **Input/button fusion:** On focus the arrow circle is swallowed into the field, so the pill grows to the right. It re-emerges on blur.
- **Liquid slider thumb:** The thumb deforms into a teardrop opposite to the drag direction.

## 7. Motion
- **Measured:** 5 segments across 10.43 s, median 0.90 s. motion_fraction is 0.47 (busy), `seamless_loop_likely: true`.
  - 0.00–0.90 s: 0.9 s, peak 0.06 (ease-out). Avatar snapping into the pill.
  - 1.13–2.80 s: 1.67 s, peak 0.73 (ease-in). The FAB spreads, with a wind-up and then release.
  - 3.20–3.80 s and 3.93–4.50 s: about 0.6 s each, peak about 0.2 (ease-out). The blur-wipe scene change.
  - 9.10–10.23 s: 1.13 s, peak 0.25. The loop back to the FAB.
- **Read:** The goo reads as spring physics. Durations of 0.6–0.9 s are longer than typical UI because the stretching needs time to be seen.

## 8. Brand system
n/a — not a brand system. Identity cue: the logo itself is two metaballs mid-merge, so the mark demonstrates the product.

## 9. UX
- Merges communicate relationships well: "this avatar joins this share group" and "this button belongs to this field".
- The FAB satellites are a clear 4-way radial menu.
- **Risks:**
  - The stretchy slider may reduce perceived precision.
  - Placeholder contrast fails.
  - The goo should be disabled under reduced motion.

## 10. Craft signals
- Every control is pure #fff on #f6f6f6, with no borders heavier than 1 px.
- The arrow button and FAB satellites share the same about 146 px diameter.
- The metaball bridge appears only within a threshold distance, so it never smears static layouts.
- The icon set is a single 2 px-stroke line family (Lucide-like).
- The demo transitions use a horizontal motion blur, staying in the "liquid" vocabulary.

## 11. Reproduction recipe
```html
<svg width="0" height="0"><filter id="goo">
  <feGaussianBlur in="SourceGraphic" stdDeviation="10" result="b"/>
  <feColorMatrix in="b" mode="matrix" values="1 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 22 -9" result="g"/>
  <feComposite in="SourceGraphic" in2="g" operator="atop"/></filter></svg>
```
```css
:root{--bg:#f6f6f6;--surface:#fff;--ink:#1a1a1a;--muted:#8a8a8a}
.goo-layer{filter:url(#goo)}          /* shapes only; render text/icons above it */
.field{height:168px;border-radius:9999px;background:var(--surface);box-shadow:0 10px 40px rgba(0,0,0,.06)}
.fab{width:146px;aspect-ratio:1;border-radius:50%;background:var(--surface);
  transition:transform .9s cubic-bezier(.34,1.56,.64,1)}
.menu.open .fab:nth-child(1){transform:translate(0,-190px)}
.menu.open .fab:nth-child(2){transform:translate(-190px,-110px)}
.menu.open .fab:nth-child(3){transform:translate(190px,-110px)}
@media (prefers-reduced-motion:reduce){.goo-layer{filter:none}}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Pure white-on-grey restraint lets the liquid behaviour star. |
| Originality | 8 | The goo filter is old, but applying it systematically to forms, sliders and sharing is fresh. |
| Usability | 7 | Merges carry meaning, though contrast is weak and the timings are long. |
| Craft | 8 | Consistent sizes, a tuned bridge threshold, and a logo that demos the effect. |

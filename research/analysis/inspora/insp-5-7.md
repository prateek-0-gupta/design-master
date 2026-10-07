---
id: insp-5-7
source: inspora
category: Motion
status: analyzed
title: "Shader Slider"
creator: "@raul_dronca"
styles: [gradient-mesh, grain-noise, aurora-glow]
patterns: [shader-card-carousel, hue-matched-glow-shadow, blur-crossfade-text, pill-pagination-dots, ghost-chevron-arrows]
mode: light
palette: ["#f7f6f4", "#126645", "#3fd991", "#105739", "#487f58", "#414544"]
type_families: ["Inter Display / Geist-style neo-grotesk (likely)"]
type_class: [neo-grotesk]
radius_px: [20, 9999]
motion: {durations_s: [0.57, 0.7, 0.43, 0.5], easing: [ease-out, ease-in-out], loop: false}
scores: {aesthetics: 8, originality: 6, usability: 7, craft: 8}
craft_signals: [glow-shadow-takes-card-hue, film-grain-over-gradient, text-blurs-out-before-swap, active-dot-stretches-to-pill, dotted-radial-logomark]
anti_patterns: [white-text-on-light-gradient-zones, faint-prev-arrow]
---
# Shader Slider — @raul_dronca

## 1. Snapshot
- **Subject:** A 12.5 s, 1920×1442 carousel of five mood cards: Clarity (slate), Drift (violet), Stillness (green), Warmth (amber) and Depth (indigo). Each card is a grainy animated shader gradient with a white title and a one-line caption.
- **Why it's remarkable:** Each slide change morphs the shader colours rather than sliding the card, and the card's outer glow re-tints to match, so the whole page changes mood.

## 2. Composition & layout
- **Card:** About 1100×687 px (16:10), centred, with a radius of about 20.
- **Logomark:** At the top-left inset, about 85 px from the edges, a 56 px dotted radial mark.
- **Text:** Anchored bottom-left, about 85 px in. The title baseline sits at y≈890 and the caption about 80 px below.
- **Arrows:** Chevrons sit about 75 px outside the card's left and right edges, centred vertically.
- **Pagination:** At about 60 px below the card. The active indicator is a 50×16 px pill and the inactive ones are 16 px dots, with about 18 px gaps.

## 3. Typography
- Neo-grotesk (Inter Display or Geist-like).
- **Title:** About 60 px Bold with tight tracking of about −0.02 em.
- **Caption:** About 34 px Regular at about 80% white.
- Two levels only, one family.

## 4. Colour
| Hex | Role |
|---|---|
| #f7f6f4 | canvas (warm off-white) |
| #126645 / #105739 | Stillness deep greens (corners) |
| #3fd991 | Stillness highlight |
| #487f58 | mid-tone behind the caption |
| #414544 | active pagination pill |
| per slide | slate #5a6772, violet #6a2bd0, amber #d08a12 and indigo #4b3fc8 (seen in frames) |

WCAG:
- White on #126645 is 6.97:1.
- White on the #3fd991 highlight is **1.82:1**, though the text avoids that zone.
- The caption (about #d8e5dc) over #487f58 is 3.63:1, which passes only as large text.
- The shader's lightness varies, so contrast is not guaranteed per frame.

## 5. Depth & material
- **Card:** A fine film-grain or noise overlay sits on top of a soft multi-point gradient, giving a velvety, printed feel.
- **Shadow:** The card casts a large, low-opacity coloured glow (about 0 30px 120px of the card's hue at about 25%). It is greenish around Stillness, amber around Warmth and violet around Drift.
- **Chrome:** The canvas has no other ornament.

## 6. Components & patterns
- A carousel of five cards with prev/next chevrons and pill pagination.
- **On change:** the old title and caption blur out, the shader morphs to the new palette, then the new text sharpens in. In the frames at 2.09 s, 4.87 s and 7.66 s the text is caught mid-blur.
- **Logomark:** A dotted radial glyph, constant across slides.

## 7. Motion
- **Measured:** 4 segments across 12.53 s, median 0.53 s. `seamless_loop_likely: false`.
  - 1.90 s: 0.57 s, peak 0.09. 7.00 s: 0.43 s, peak 0.19. 9.03 s: 0.50 s, peak 0.17. All ease-out (fast start, gentle settle).
  - 4.73 s: 0.70 s, peak 0.40 (symmetric). A longer morph, likely violet to green, where the hue distance is largest.
- **Between clicks:** The shader keeps drifting below the motion threshold (an ambient loop).
- **Read:** About 0.5 s ease-out per slide, with text blur as a cross-dissolve mask.

## 8. Brand system
n/a — not a brand system. Cue: mood-word naming (Clarity, Drift, Stillness, Warmth, Depth) with one colour per mood.

## 9. UX
- Clear carousel affordances, and the pagination pill shows position.
- The prev arrow on the first slide is correctly faded.
- **Risks:**
  - Text legibility depends on the shader frame.
  - Grain plus a moving gradient may be heavy on low-end GPUs.
  - Reduced motion should freeze the shader.

## 10. Craft signals
- The glow shadow colour is derived from the active slide, not fixed grey.
- The grain is uniform and fine (about 1 px), and it is applied over the gradient but under the text.
- The text exits by blur rather than slide, so it never travels across the gradient.
- The active dot morphs into a 50 px pill, the same height as the dots.
- The canvas #f7f6f4 is warm and never pure white, so the coloured glows read softly.

## 11. Reproduction recipe
```css
:root{--bg:#f7f6f4;--hue-a:#126645;--hue-b:#3fd991;--hue-c:#105739}
.slide{width:1100px;aspect-ratio:16/10;border-radius:20px;position:relative;overflow:hidden;
  background:radial-gradient(60% 70% at 70% 15%,var(--hue-b),transparent 70%),
             radial-gradient(50% 60% at 15% 25%,var(--hue-c),transparent 70%),var(--hue-a);
  box-shadow:0 30px 120px color-mix(in srgb,var(--hue-b) 30%,transparent);
  transition:--hue-a .6s,--hue-b .6s,--hue-c .6s,box-shadow .6s cubic-bezier(.2,.8,.2,1)}
.slide::after{content:"";position:absolute;inset:0;opacity:.18;mix-blend-mode:overlay;
  background:url("data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' width='160' height='160'><filter id='n'><feTurbulence baseFrequency='.9'/></filter><rect width='100%' height='100%' filter='url(%23n)'/></svg>")}
.slide h2{font:700 60px/1 Inter;letter-spacing:-.02em;color:#fff;transition:filter .25s,opacity .25s}
.slide.is-leaving h2,.slide.is-leaving p{filter:blur(12px);opacity:0}
.dots i{width:16px;height:16px;border-radius:9999px;background:#d0d0ce;transition:width .3s}.dots i[aria-current]{width:50px;background:#414544}
@property --hue-a{syntax:"<color>";inherits:true;initial-value:#126645}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Rich grainy gradients with hue-matched glows on a quiet canvas. |
| Originality | 6 | Grainy gradient cards are common; the glow re-tinting and blur text swap lift it. |
| Usability | 7 | A standard, clear carousel, but text contrast varies with the shader. |
| Craft | 8 | Well-tuned ease-out timings, consistent insets and a careful grain layer. |

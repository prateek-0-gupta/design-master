---
id: insp-maple-research-cards
source: inspora
category: Branding
status: analyzed
title: "Maple Research cards"
creator: "@ayushsoni_io"
styles: [kinetic-type, generative-particle, terminal-mono, dark-premium]
patterns: [ascii-field-from-brand-word, metaball-mask-over-glyph-grid, paired-cards-inverse-layout, stacked-wordmark-with-descriptor, pixel-leaf-logomark, poster-card-pair]
mode: mixed
palette: ["#e5e5e5", "#000000", "#0847f6", "#ffffff", "#8ca6d6", "#3b61bd", "#1d1f2a"]
type_families: ["Neue Montreal / PP Mori-style grotesk (likely)", "Monospaced caps for ASCII field (likely Space Mono / Departure-like)"]
type_class: [neo-grotesk, mono]
radius_px: [33]
motion: {durations_s: [2.33, 2.37, 0.3, 3.63], easing: [ease-in, ease-out], loop: true}
scores: {aesthetics: 9, originality: 8, usability: 7, craft: 8}
craft_signals: [ascii-alphabet-drawn-from-word-research, two-tone-glyphs-in-field, inverse-layout-between-cards, same-mask-different-ground, wordmark-descriptor-tucked-under-baseline, field-edge-crops-at-card-radius]
anti_patterns: [ascii-texture-below-aa, motion-not-seamless]
---
# Maple Research cards — @ayushsoni_io

## 1. Snapshot
- **Subject:** A 10.8 s, 2200×2200, 60 fps loop of two portrait cards on #e5e5e5:
  - a black card with the "Maple Research" wordmark and the headline "Crossing the uncanny valley of conversational voice";
  - an electric-blue card with a pixel maple-leaf mark and "A research and engineering organization".
- Both carry a field of monospaced characters, drawn largely from the letters R-E-S-E-A-R-C-H plus punctuation, masked by slowly morphing metaball blobs.
- **Why it's remarkable:** The texture is literally made of the brand's name. The generative field turns the word "research" into a living material, and the inverted layout across the two cards makes them read as a pair.

## 2. Composition & layout
- **Cards:** Each is about 778×1386 px (about 9:16), with a radius of about 33 px and a gap of about 64 px. The pair is centred with about 250 px side margins.
- **Black card:** Text sits at the top: wordmark at an inset of about 62 px, headline below it at y≈+210. The ASCII field fills the lower about 65% of the card.
- **Blue card:** Inverted. The ASCII field fills the top about 78% and the logomark plus descriptor sit in the bottom about 20%.
- **Result:** Text-top/field-bottom against field-top/text-bottom, a mirrored diptych.
- **Field:** Glyphs are on an about 16 px horizontal and 16 px vertical pitch (in 2200 px), clipped by the card's rounded corners.

## 3. Typography
- **Wordmark:** "Maple" in a bold grotesk at about 75 px with tight tracking. "Research" is tucked under it at about 25 px, left-aligned with the M, hanging just below the baseline.
- **Headlines:** A grotesk close to Neue Montreal or PP Mori Medium.
  - About 58 px with leading of about 1.05 and tracking of about −0.02 em, in sentence case.
  - Black card: three lines, ragged right.
  - Blue card: two lines, bottom-aligned.
- **ASCII field:** monospaced uppercase characters at about 13 px, with letter-spacing that turns each glyph into a pixel.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #e5e5e5 | presentation board | 52% |
| #000000 | card 1 ground | 15% |
| #0847f6 / #1e56e7 | card 2 ground (electric blue) | 20% |
| #ffffff | wordmark, headlines, logomark | — |
| #8ca6d6 | ASCII glyphs on blue | 2% |
| #3b61bd / #1d1f2a | ASCII glyphs on black (blue and dim) | 4% |

WCAG checks:
- White on black: 21:1.
- White on blue #0847f6: 6.48:1 (passes AA for the 58 px headline and even for small text).
- ASCII on blue: 2.63:1.
- ASCII on black (#3b61bd): 3.63:1.
- The field is texture, not content, so the low contrast is acceptable and keeps it subordinate.
- Blue card on board: 5.14:1.

## 5. Depth & material
Flat: no shadows or gradients. Depth comes from the masking. On the black card the field mixes white and blue glyphs, which creates a two-depth shimmer. The blobs are large metaball shapes of about 300–500 px with soft, stair-stepped edges because they snap to the glyph grid.

## 6. Components & patterns
- **ASCII field masked by evolving blobs:** the blobs both reveal and hide the characters.
- **Card pair as a brand-system demo:** a primary ground (black) and an accent ground (blue) share one texture.
- **Pixel logomark:** a maple leaf built from squares with tiny numerals and dots around it, drawn from the same pixel language as the field.

## 7. Motion
Measured profile: 10.83 s at 60 fps, `motion_fraction` 0.64. Four segments:

| Window | Duration | peak_at | Shape |
|---|---|---|---|
| 0.03–2.37 s | 2.33 s | 0.79 | ease-in |
| 3.57–5.93 s | 2.37 s | 0.99 | ease-in |
| 6.03–6.33 s | 0.30 s | 0.06 | ease-out snap |
| 6.70–10.33 s | 3.63 s | 0.85 | ease-in |

- **Rhythm:** Each long segment builds slowly and peaks late, so the blobs drift and then accelerate into a re-form. A roughly 1.2 s calm separates the segments.
- **Type:** The text never moves; only the field animates. Characters likely re-randomise as the mask passes.
- **Loop:** `seamless_loop_likely: false` (first_last_diff 5.08), so there is a visible jump at the loop seam.

## 8. Brand system
Identity elements visible:
- Wordmark: "Maple" bold with a tucked "Research" descriptor.
- Pixel maple-leaf symbol.
- Two-ground palette: black and electric blue #0847f6, with white type.
- A generative ASCII texture built from the brand name.
- Grotesk headlines in sentence case.
- A voice that is research-forward and plain-spoken.

Transferable rule: derive the texture alphabet from the brand name so every pattern is "on brand" at the glyph level.

## 9. UX
- **Readability:** Headlines are isolated on solid ground and never overlap the field, so they stay legible.
- **Risks:**
  - The constant motion needs a reduced-motion state.
  - The loop seam is not seamless.

## 10. Craft signals
- The ASCII field alphabet is dominated by R, E, S, A, C and H (the letters of "research").
- The blob masks are quantised to the glyph grid, so their edges are stepped, not antialiased.
- The two cards invert text and field positions.
- The field is cropped by the card radius (glyphs disappear at the corner curve) rather than overflowing.
- The "Research" descriptor sits within the wordmark's x-height zone, hanging below "Maple".
- Only one accent hue (#0847f6) is used, and it also tints the glyphs on black.

## 11. Reproduction recipe
```css
:root{--board:#e5e5e5;--ink:#000;--blue:#0847f6;--fg:#fff;--glyph-on-blue:#8ca6d6;--glyph-on-ink:#3b61bd}
.card{width:360px;aspect-ratio:9/16;border-radius:15px;overflow:hidden;position:relative;color:var(--fg);padding:28px}
.card--ink{background:var(--ink)} .card--blue{background:var(--blue)}
.card h2{font:500 27px/1.05 "PP Mori","Neue Montreal",Inter,sans-serif;letter-spacing:-.02em}
.field{position:absolute;inset:auto 0 0 0;height:65%;font:700 6px/7.5px "Space Mono",monospace;letter-spacing:.9px;
  color:var(--glyph-on-ink);white-space:pre;
  -webkit-mask:url(#metaballs);mask:url(#metaballs)} /* or render on canvas: */
```
```js
// canvas: for each cell, n = noise3(x*.08, y*.08, t*.15); if (n > .1) draw "RESEARCH$?%+=#"[hash(x,y,floor(t*4)) % 15]
// t advanced with an ease-in pulse every ~2.4 s; respect prefers-reduced-motion by freezing t.
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 9 | A confident two-ground diptych where texture and type are perfectly balanced. |
| Originality | 8 | An ASCII field generated from the brand word is a clever, ownable twist on the trend. |
| Usability | 7 | Headlines are clean and AA-passing; constant motion and the seam are drawbacks. |
| Craft | 8 | Grid-quantised masks, mirrored layouts and a disciplined single accent. |

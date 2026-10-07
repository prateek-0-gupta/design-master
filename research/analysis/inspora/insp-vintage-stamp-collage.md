---
id: insp-vintage-stamp-collage
source: inspora
category: Print
status: analyzed
title: "Vintage stamp collage"
creator: "@jenny_wen"
styles: [physical-material, skeuomorphic, editorial-serif, photo-led]
patterns: [infinite-pan-canvas, draggable-stamp-cards, perforated-edge-frame, photo-to-engraving-treatment, lift-on-drag-shadow, scattered-collage-layout]
mode: light
palette: ["#e5e1d5", "#e6d6ba", "#d6c6aa", "#7a6a58", "#554236", "#838771", "#ad9179", "#b7af94"]
type_families: ["Clarendon / Century-style engraved serif in stamp art (likely)", "condensed grotesk on Türkiye stamps (likely)"]
type_class: [slab, transitional-serif, condensed]
radius_px: [0]
motion: {durations_s: [4.1, 1.63, 0.57, 0.27], easing: [linear, ease-in-out], loop: false}
scores: {aesthetics: 9, originality: 8, usability: 6, craft: 9}
craft_signals: [perforation-scallops-with-cream-margin, per-country-typographic-convention, monochrome-engraving-tint-per-stamp, faint-paper-grid-texture, lifted-stamp-larger-shadow, denomination-as-personal-date]
anti_patterns: [no-visible-navigation-or-affordance, ai-generated-art-uniformity]
---
# Vintage stamp collage — @jenny_wen

## 1. Snapshot
- **Subject:** A 15.5 s, 1660×1660 capture of an interactive canvas. Personal photos (a donkey, a Paris facade, an ultrasound, a Kadıköy ferry pier, a beach Polaroid) are re-rendered as vintage postage stamps from different countries and scattered on textured paper. The canvas pans, and stamps can be picked up and moved.
- **Why it's remarkable:** It turns a personal photo album into a philatelic collection. Each memory is assigned a country's stamp idiom (US "2 CENTS" engraving, "RÉPUBLIQUE FRANÇAISE 30 F", "INDIA POSTAGE 2 ANNAS", 中国人民邮政 8分, ΕΛΛΑΣ 2 ΔΡΧ), so the place and the feel of each photo are encoded in the stamp style.

## 2. Composition & layout
- **Canvas:** infinite, panned by drag. Stamps are scattered at irregular spacing with ~60–250 px gaps, occasionally overlapping (the donkey stamp sits on top of the French stamp in the key frame).
- **Stamp sizes (key, at 1660 px):**
  - landscape ~475×345 (India);
  - portrait ~330×460 (U.S. Polaroid);
  - French ~480×340.
- **Proportions:** close to real stamp ratios (≈1.38:1).
- **Orientation:** All stamps are axis-aligned (0° rotation). That is a deliberate tidy-collage choice rather than a messy scrapbook.
- **Negative space:** about 55–60% of the frame is bare paper, so the collage breathes.

## 3. Typography
Type lives inside the stamp art and follows each country's convention.
- **U.S. stamps:** bold Clarendon-like slab or engraved serif caps in ribbon banners ("U.S. POSTAGE", "2 CENTS", with numeral roundels).
- **French stamp:** a light, spaced Didone or transitional serif in small caps ("RÉPUBLIQUE FRANÇAISE"), denomination "30 F" between rules.
- **India stamp:** an engraved serif in a panel.
- **Türkiye stamps:** condensed sans caps ("TÜRKİYE CUMHURİYETİ POSTALARI").
- **Chinese stamp:** heavy Song-style hanzi with a red "8分".
- **No UI typography is visible.** The interface is the content.

## 4. Colour
| Hex | Role | Approx share |
|---|---|---|
| #e5e1d5 | paper ground | 59% |
| #e6d6ba / #d6c6aa | stamp cream margins and perforation paper | 11% |
| #554236 / #7a6a58 | sepia and brown engraving ink | 12% |
| #838771 / #b7af94 | olive-grey engraving (U.S. green, "2 cents") | 10% |
| #ad9179 / #d4b594 | warm photo tones | 9% |
| ≈#2f5a3a | India green ink | — |
| ≈#6e4a63 | U.S. purple ink | — |

WCAG checks:
- Sepia text #554236 on cream #e6d6ba: 6.62:1.
- India green ≈#2f5a3a on pale green: 5.99:1.

Each stamp is a near-monotone ink (green, purple, sepia, slate), while some stamps keep full colour (Paris, Türkiye). The tinting strategy unifies photos with very different sources.

## 5. Depth & material
- **Paper:** an off-white with visible fibre texture and a faint square grid (~60 px pitch), like ledger or album paper.
- **Stamps:**
  - perforated scalloped edges (~8 px teeth at ~14 px pitch) around a ~12 px cream margin;
  - a thin inner frame rule;
  - a small soft shadow (~2 px offset, 6 px blur).
- **Lift on drag:** A dragged stamp (9.49 s, 14.67 s) gets a larger, softer shadow (estimated 8 px offset, 20 px blur) and sits above its neighbours.
- **Engraving:** the stamp imagery is rendered with line-engraving or halftone texture, especially in the monotone stamps.

## 6. Components & patterns
- **Stamp card:** perforation, margin, frame, image, then a country banner and denomination. The denomination doubles as a cute value (e.g. 2 cents, 15¢).
- **Interactions:** canvas pan (hand cursor) and drag-to-rearrange stamps. There is no other chrome: no title, menu or captions.
- **Typographic travel log:** the country styling acts as the caption (e.g. the Kadıköy pier stamp reads "TÜRKİYE CUMHURİYETİ 100 KURUŞ").

## 7. Motion
Measured profile: 15.54 s at 56 fps, `motion_fraction` 0.43, five segments. Not a loop.
- **1.10–5.20 s (4.10 s, continuous/linear):** a long canvas pan. The whole field slides, with high mean energy (3.9) because every pixel moves.
- **5.50–7.13 s (1.63 s, peak 0.52, symmetric):** a second pan that eases in and out, an inertial drag release.
- **8.43–9.00 s (0.57 s, symmetric):** picking up the ultrasound stamp and moving it next to the French stamp (compare 7.77 s and 9.49 s).
- **11.10 s (0.27 s) and 13.80 s (0.27 s, ease-in):** short stamp drags. At 14.67 s the Greek stamp is placed onto the canvas.
- Movement is direct manipulation 1:1 with the cursor, with no spring or overshoot observed.

## 8. Brand system
n/a — not a brand system. Identity cues:
- a personal "life as a stamp album" concept;
- an analog warm palette;
- the country stamp idiom used as a visual language system.

## 9. UX
- **Strengths:**
  - Tactile and exploratory, with an immediately understood metaphor.
  - Drag affordance via the hand cursor.
- **Risks:**
  - No orientation: no minimap, no captions, no way to know how large the canvas is or which stamps were seen.
  - No keyboard path.
  - Stamp text inside images is not accessible text.
  - The consistent AI-render look flattens the authenticity a little.

## 10. Craft signals
- Perforation teeth are cut into a cream margin, not the image itself, as on real stamps.
- Each stamp follows its country's real typographic convention (banner caps, small-caps French, hanzi with a red denomination).
- Monotone ink tints per stamp unify varied photographs.
- The paper has both fibre texture and a faint grid.
- Shadow depth increases when a stamp is lifted.
- All stamps are axis-aligned, so the collage stays tidy while the positions vary.

## 11. Reproduction recipe
```css
:root{--paper:#e5e1d5;--stamp-margin:#efe4cc;--ink-sepia:#554236;--ink-olive:#838771}
body{background:var(--paper) url(fibre.png);background-image:
  linear-gradient(rgba(0,0,0,.025) 1px,transparent 1px),linear-gradient(90deg,rgba(0,0,0,.025) 1px,transparent 1px);
  background-size:60px 60px}
.stamp{position:absolute;padding:12px;background:var(--stamp-margin);
  /* perforation via radial mask */
  -webkit-mask:radial-gradient(circle at 7px 7px,transparent 4px,#000 4.5px) -7px -7px/14px 14px,
               linear-gradient(#000,#000) content-box;
  -webkit-mask-composite:source-over;
  filter:drop-shadow(0 2px 3px rgba(60,40,20,.18));transition:filter .2s ease-out}
.stamp.dragging{filter:drop-shadow(0 10px 14px rgba(60,40,20,.28));z-index:10;cursor:grabbing}
.stamp img{display:block;outline:1px solid var(--ink-sepia);outline-offset:-6px}
.stamp.mono img{filter:grayscale(1) sepia(.6) hue-rotate(60deg) contrast(1.15)}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 9 | A rich, warm analog collection with disciplined negative space. |
| Originality | 8 | Mapping memories onto country-specific stamp idioms is a lovely idea. |
| Usability | 6 | Delightful to explore, but there is no wayfinding or accessible captions. |
| Craft | 9 | Authentic perforation, typographic conventions and lift shadows. |

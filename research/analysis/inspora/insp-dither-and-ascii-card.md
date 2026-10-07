---
id: insp-dither-and-ascii-card
source: inspora
category: Motion
status: analyzed
title: "Dither and Ascii card"
creator: "Praveen Kumar"
styles: [dither-halftone, terminal-mono, editorial-serif, duotone]
patterns: [generative-card-header, dither-shader-image, ascii-binary-figure, info-panel-footer, avatar-stack-social-proof, ghost-and-solid-button-pair, colour-themed-card-variants]
mode: light
palette: ["#404040", "#ffffff", "#375f3c", "#4f8a42", "#92b8a1", "#cfd0e5", "#4b4fd6", "#e7ecee"]
type_families: ["light transitional/editorial serif for titles, close to Newsreader / Tiempos Headline Light (likely)", "Inter (likely)", "monospace glyphs in ASCII art"]
type_class: [editorial-serif, neo-grotesk, mono]
radius_px: [0, 8]
motion: {durations_s: [17.67], easing: [linear], loop: false}
scores: {aesthetics: 8, originality: 8, usability: 6, craft: 7}
craft_signals: [header-art-tinted-in-card-accent, two-render-modes-one-card-template, serif-title-against-pixel-art, panel-colour-matches-art-hue, avatar-stack-plus-count, square-cards-on-graphite]
anti_patterns: [muted-meta-text-below-aa, lavender-title-4-07, inconsistent-eyebrow-case]
---
# Dither and Ascii card — Praveen Kumar

## 1. Snapshot
- **Subject:** A 17.7 s, 1920×1440 clip of two portrait info cards — "NYC Exchange" (green, ordered-dither generative shape) and "Shanghai Stock Exchange" (lavender, figure drawn in animated 0/1 ASCII) — whose header art continuously shimmers.
- **Why it's remarkable:** One card template, two shader treatments: a Bayer-style dither and a binary-character ASCII render, each tinted in the card's own accent so image, panel and buttons form a single duotone.

## 2. Composition & layout
- Two cards ≈800×1232 px on #404040, 80 px apart, ≈120 px side margins, ≈100 px top margin.
- Each card: header art 800×790 (64%) above an info panel 800×445 (36%).
- Panel grid: ≈36 px inner padding; eyebrow + "Add Card" ghost button on one row (y≈958); title at y≈1045; 3-line description; location row; avatar stack + "Expand" CTA on the bottom row, CTA right-aligned to the same edge as "Add Card".
- Corners are square (0 px) on cards; buttons ≈8 px.

## 3. Typography
- **Title:** light editorial serif ≈44 px, tight tracking — "NYC Exchange" in white, "Shanghai Stock Exchange" in indigo.
- **UI:** Inter-like ≈20 px for eyebrow, body (leading ≈1.0 — notably tight), location and buttons.
- Eyebrow inconsistency: "Stock Card" (sentence case) vs. "MY CARD" (caps).
- ASCII art uses a monospace with "0", "1" and fragments, ≈14 px cells.

## 4. Colour
| Hex | Role | Share (key frame) |
|---|---|---|
| #404040 | stage | 27% |
| #ffffff | header art background, ghost buttons | 26% |
| #375f3c | green panel | 11% |
| #6a9777 / #92b8a1 / #b7cdc3 | dither tones (3-step green ramp) | 13% |
| #4f8a42 | green "Expand" CTA | — |
| #cfd0e5 | lavender panel | 16% |
| #4b4fd6 | indigo title, ASCII glyphs, CTA | — |

WCAG (contrast.py):
- White title on #375f3c: 7.33:1; body ≈#d6e2d8: 5.49:1.
- Meta "+30 more are watching" ≈#8fa894 on #375f3c: **2.86:1** (fail).
- White on green CTA #4f8a42: **4.16:1** (large-only).
- Indigo title #4b4fd6 on #cfd0e5: 4.07:1 (OK at 44 px, fails for "Shanghai, China" at 20 px).
- Body ≈#5d5d6e on lavender: 4.24:1; meta ≈#8a8aa0: **2.22:1**.
- White on indigo CTA: 6.2:1.

## 5. Depth & material
- Flat: no card shadows, square corners, graphite stage — print/poster sensibility.
- Only the "Expand" CTA has a soft ≈12 px shadow, marking it as the primary action.
- Texture comes entirely from the dither dot field and ASCII glyph density, which encode tone like halftone.

## 6. Components & patterns
- **Card header as shader canvas:** dither (density = luminance, 3 green levels) and ASCII (glyph opacity = luminance).
- **Ghost button** "Add Card" (white, 1 px border, copy icon) vs. **solid CTA** "Expand" (accent fill, expand icon).
- **Avatar stack** of three ≈36 px overlapping faces + "+30 more are watching".
- **Location row** with pin icon.

## 7. Motion
Measured (m0_motion.json): 17.75 s at 30 fps, motion_fraction 0.86, one continuous 17.67 s segment (peak_at 0.18, energy CV 0.49), seamless_loop_likely false.
- The UI is static; the energy is the header art boiling — the dither shape slowly rotates/morphs its chevron, and the ASCII figure's glyphs flicker and drift (the silhouette shifts from a hunched figure to an upright one across 1–17 s).
- Rate is steady and ambient, estimated ≈0.5–1 s per noticeable shape change; no eased UI transitions are shown.

## 8. Brand system
n/a — not a brand system. Identity cues: duotone per card (green / indigo) and generative-shader headers as a reusable "data card" language.

## 9. UX
- Clear hierarchy: art → serif title → description → social proof → CTA.
- Two buttons are well separated by style (ghost vs. solid).
- Risks: muted meta text fails contrast on both cards; body leading ≈1.0 is cramped; generative art carries no information about the exchange itself; mixed eyebrow casing.

## 10. Craft signals
- The dither ramp uses exactly the panel's hue family (three steps of green), and the ASCII uses the CTA's indigo.
- Both cards share identical geometry; only accent and shader change.
- "Add Card" and "Expand" share a right edge 26 px inside the card.
- Serif title is light weight, contrasting with the pixel-grain art above it.
- Square card corners suit the pixel-grid imagery.

## 11. Reproduction recipe
```css
:root{--stage:#404040;--g-panel:#375f3c;--g-cta:#3f7a34;--g-ink:#fff;--l-panel:#cfd0e5;--l-ink:#3f42c4;--l-cta:#4b4fd6}
.card{width:400px;display:grid;grid-template-rows:395px auto;background:#fff}
.card .art{image-rendering:pixelated}
.card .panel{padding:18px;display:grid;gap:12px}
.card.green .panel{background:var(--g-panel);color:var(--g-ink)}
.card.lav .panel{background:var(--l-panel);color:#4a4a5a}
.title{font:300 22px/1.1 "Newsreader","Tiempos Headline",Georgia,serif;letter-spacing:-.01em}
.btn-ghost{background:#fff;border:1px solid #e3e3e3;border-radius:4px;color:#111}
.btn-cta{border-radius:4px;color:#fff;box-shadow:0 6px 12px rgba(0,0,0,.15)}
.card.green .btn-cta{background:var(--g-cta)} .card.lav .btn-cta{background:var(--l-cta)}
.avatars img{width:18px;height:18px;border-radius:50%;margin-left:-6px;border:1px solid currentColor}
```
```glsl
// 4x4 Bayer dither for the header
float b=bayer4(gl_FragCoord.xy/2.0); vec3 c=mix(vec3(1.),vec3(.22,.37,.24),step(b,lum));
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Duotone cards with serif titles over grainy generative art feel editorial and fresh. |
| Originality | 8 | Pairing dither and binary-ASCII renderers in one card system is distinctive. |
| Usability | 6 | Clear CTA hierarchy; several meta lines fail contrast and body leading is tight. |
| Craft | 7 | Tight hue matching and shared geometry; small inconsistencies in casing and leading. |

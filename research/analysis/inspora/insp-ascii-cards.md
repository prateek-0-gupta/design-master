---
id: insp-ascii-cards
source: inspora
category: Motion
status: analyzed
title: "ASCII cards"
creator: "Praveen Kumar (@praveenisomer)"
styles: [x-ascii-art, minimal-swiss, editorial-serif, generative-particle]
patterns: [ascii-rendered-hero, morphing-glyph-shape, crop-mark-card-frame, segmented-range-control, share-action-pair, icon-corner-arrow, feature-card-pair]
mode: light
palette: ["#f6f6f6", "#ffffff", "#000000", "#111111", "#898989", "#4a46b5", "#634f84", "#e9e9e9"]
type_families: ["Tiempos / GT Sectra-style text serif (likely) for titles", "Inter (likely) for body/UI", "monospace (SF Mono / JetBrains-like) for ASCII glyphs"]
type_class: [transitional-serif, neo-grotesk, mono]
radius_px: [6, 4]
motion: {durations_s: [0.43, 0.73, 0.27, 0.23], easing: [ease-in, ease-in-out, ease-out], loop: true}
scores: {aesthetics: 8, originality: 7, usability: 6, craft: 7}
craft_signals: [crop-marks-outside-card, glyph-density-encodes-luminance, binary-vs-digit-charset-per-card, colour-to-mono-dissolve, serif-title-sans-body, primary-black-secondary-grey-buttons]
anti_patterns: [tiny-body-copy, low-contrast-body-grey, title-case-headline-inconsistency]
---
# ASCII cards — Praveen Kumar

## 1. Snapshot
- **Subject:** A 10.2 s, 1920×1386 loop of two marketing or feature cards for a market-analytics product. Each card's hero is a slowly morphing 3D-ish shape rendered entirely in monospaced characters: binary 0/1 on the left card, digits and symbols on the right.
- **Why it's remarkable:** It uses ASCII rendering as the brand's "data texture": the illustration is literally made of numbers. It is framed with print crop marks, so each card reads like a proof sheet.

## 2. Composition & layout
- Two cards on a #f6f6f6 field, each about 622×912 px (left x 235–857, right x 1050–1670), with a gap of about 193 px. Both are pure white with no border or shadow.
- **Crop marks:** L-shaped corners (about 14 px arms, 2 px black) sit *outside* each card at all four corners.
- **Card anatomy (top to bottom):**
  - ASCII hero, about 65% of the height;
  - title at y≈960;
  - 3-line body;
  - footer row about 140 px lower, with a "1D | 7D | 1M" segmented control left and a "Copy Link" grey button plus a "Share to X" black button right;
  - a 26 px black square ↗ icon button top-right of the text block.
- Inner padding is about 16 px left and right. The text block uses about 55% of the card width.

## 3. Typography
- **Titles:** "Turn Analysis Into Authority." and "Share The Narrative" are set in a text serif with moderate contrast and bracketed serifs (Tiempos-like) at about 26 px Regular, tracking about −0.01 em.
- **Body:** a neo-grotesk at about 10–11 px in grey #898989, line height about 1.1. This is very small for 1920-wide output.
- **UI labels:** about 11 px ("Copy Link", "Share to X", "1D").
- **ASCII:** a monospaced face at about 14 px on a 12×13 px grid.
  - Left card: `0`/`1` only.
  - Right card: a density ramp `^ / + 1 7 4 3 = 5 2 9 6 0 @`, with characters chosen by luminance, so denser glyphs mean darker areas.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #f6f6f6 | page | 89% |
| #ffffff | card | ~8% |
| #000000 / #111111 | titles, crop marks, primary button, mono glyphs | ~2% |
| #898989 | body copy | <1% |
| #4a46b5 | indigo glyph tint (left, colour phase) | ~1% |
| #634f84 / #c9a6f0 | violet glyph ramp + glow (right) | ~2% |
| #e9e9e9 | secondary button fill | <1% |

WCAG:
- Titles #111 on white are 18.88:1, and the primary button is white on black at 21:1.
- Body #898989 on white is about **3.45:1 at about 10 px (fails)**.
- Secondary button text #333 on #ececec is 10.69:1.
- Indigo glyphs are 7.41:1, but they are decorative.

## 5. Depth & material
- The UI is flat.
- **Hero depth:** the ASCII shape suggests depth through character density and a soft violet bloom behind the right card's digits (about 20 px blur, #f2def7 halo). The shape reads as a lit 3D blob or ribbon rendered to text, like a WebGL-to-ASCII shader.

## 6. Components & patterns
- **Range segmented control:** 3 options. The active option "1M" sits in a white pill with a 1 px #ddd border inside a #f3f3f3 track.
- **Button pair:** secondary grey with a copy icon, primary black with a share icon. Radius about 4 px (nearly square).
- **↗ icon button:** a black 26 px square with a 4 px radius.
- **Crop-mark frame:** a decorative print idiom that also groups the content.

## 7. Motion
The motion is measured: 10.18 s, 30 fps, motion_fraction 0.18 and seamless_loop_likely true (first/last diff 0.01).
- **Segments:**
  - 0.23 s (0.13 s, ease-in);
  - 0.83–1.27 s (0.43 s symmetric);
  - 2.37 s (0.23 s ease-out);
  - 2.97–3.70 s (0.73 s ease-in, peak 0.93);
  - 4.03 s (0.27 s ease-in);
  - 7.40 s (0.27 s ease-out).

The sheet shows the narrative (estimates):
- 0.6–2.8 s: the left shape morphs in indigo while the right blob stays violet;
- about 3.96 s: the left card empties to blank;
- 5.1–7.4 s: both re-form in **black**, so the colour has been stripped to monochrome;
- 8.5 s: the left returns to indigo;
- 9.6 s: both cards are blank, which is the loop point.

Characters appear to flicker per cell (the glyph changes as luminance changes) rather than translate, so the motion is a field re-sampling. The profiler segments are short because the change is spread thinly over many glyphs.

## 8. Brand system
n/a — not a brand system. Identity cues:
- numbers-as-imagery;
- serif headlines with grotesk UI;
- a single indigo/violet accent;
- crop marks as a "publish or print" metaphor, which fits "Share the narrative".

## 9. UX
- The share actions are clear and well prioritised (black primary, grey secondary), and the range control is familiar.
- **Problems:**
  - The body text is tiny and low contrast.
  - The decorative crop marks add noise around the clickable card.
  - The ASCII art is evocative but carries no actual data, despite the "inspect the data" copy.

## 10. Craft signals
- Crop marks sit outside the card bounds and align to its corners.
- Glyph density maps to brightness: the right card ramps from `^` and `/` at the edges to `6`, `9` and `@` in the core.
- Each card uses a different character set (binary vs decimal), which differentiates the two features.
- The colour phase and the black phase use the same geometry (f1 vs f5), so the colour is a uniform layer.
- Square 4 px radii on buttons match the editorial, print-sheet tone.

## 11. Reproduction recipe
```css
:root{--page:#f6f6f6;--card:#fff;--ink:#111;--muted:#6b6b6b;--accent:#4a46b5;--glow:#f2def7}
.card{position:relative;background:var(--card);width:622px;aspect-ratio:622/912;padding:16px;display:grid;grid-template-rows:1fr auto auto}
.card::before,.card::after{content:"";position:absolute;width:14px;height:14px;border:2px solid #000}
.card::before{top:-2px;left:-2px;border-right:0;border-bottom:0}.card::after{bottom:-2px;right:-2px;border-left:0;border-top:0}
h3{font:400 26px/1.15 "Tiempos Text",Georgia,serif;letter-spacing:-.01em}
p{font:400 13px/1.35 Inter;color:var(--muted)}  /* raise from 10px #898989 */
.ascii{font:500 14px/13px "JetBrains Mono",monospace;color:var(--accent);white-space:pre;text-shadow:0 0 20px var(--glow)}
.btn{border-radius:4px;padding:8px 10px;font:500 11px Inter}.btn--primary{background:#000;color:#fff}.btn--ghost{background:#e9e9e9}
```
```js
const RAMP=" ^/+174=3529608@"; // luminance → glyph
cell.textContent = RAMP[Math.min(RAMP.length-1, (lum*RAMP.length)|0)];
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | An editorial white-space system with a striking typographic hero. |
| Originality | 7 | ASCII shaders are trending, but the binary vs digits pairing and crop marks give it a distinct take. |
| Usability | 6 | Clear actions, but the body copy is tiny and fails contrast. |
| Craft | 7 | Thoughtful charset ramps and crop-mark alignment. Inconsistent title punctuation and casing between cards. |

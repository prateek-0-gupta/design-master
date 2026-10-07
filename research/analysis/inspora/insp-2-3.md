---
id: insp-2-3
source: inspora
category: Motion
status: analyzed
title: "Abstract gradient"
creator: "@its_sslvr"
styles: [aurora-glow, gradient-mesh, minimal-swiss, editorial-serif]
patterns: [animated-fluid-gradient-poster, poster-triptych, glyph-punctuation-motifs, two-tier-caption-blocks, light-to-dark-series, bottom-anchored-flame-field]
mode: mixed
palette: ["#efeef3", "#ffffff", "#151517", "#cff1fe", "#b2e8fd", "#fbc4c8", "#fbdcd8", "#a17f69"]
type_families: ["Inter (likely)"]
type_class: [neo-grotesk]
radius_px: [0]
motion: {durations_s: [0.53, 0.57, 1.0, 0.57, 0.9], easing: [ease-in-out, ease-in, ease-out], loop: false}
scores: {aesthetics: 9, originality: 7, usability: 7, craft: 8}
craft_signals: [shared-headline-baseline-across-triptych, plus-and-underscore-glyph-system, caps-microcopy-with-bold-lead-ins, gradient-confined-to-lower-third-on-white-poster, flames-rise-from-bottom-edge-on-dark, consistent-margins-29px]
anti_patterns: [microcopy-at-print-size-unreadable-on-screen]
---
# Abstract gradient — @its_sslvr

## 1. Snapshot
- **Subject:** A 13.7 s, 1920×1080 presentation of three A-ratio posters on a light grey board. Each poster carries a living fluid gradient: the first fills the page with pastel sky and blush, the second has a white page with colour rising only at the bottom edge, and the third is a black page with a flame-like emission.
- **Why it's remarkable:** One gradient engine, three densities (full, edge, emission on dark), which turns a common "mesh gradient" into a coherent print series with a strong typographic system.

## 2. Composition & layout
- **Posters:** three, each about 505×713 px (ratio 1:1.41, A-series), with about 70 px gutters, centred on a #efeef3 board. Tops align at y=182.
- **Shared grid:** every poster puts its headline at the same baseline (y≈230/257) with about a 29 px inset.
  - Poster 1 has the headline top-left.
  - Poster 2 sets the headline top-right (right-aligned) and pairs it with two caps-caption blocks top-left, plus a right-aligned paragraph at y≈365.
  - Poster 3 has the headline top-left, with caption blocks and a paragraph right-aligned in a two-column cluster at y≈345.
- **Gradient placement:** the field changes per poster: full-bleed on 1, the bottom 30% on 2, and the bottom 35% on 3.

## 3. Typography
- An Inter-like neo-grotesk throughout.
- **Headlines:** about 22 px regular, two lines, sentence case, with typographic "glyph punctuation": "Cosmic wind drop *", "Outer +____+ layers", "From the land +++", "Energy ingestion ____". The `+`, `*` and underscore rules act as a graphic language.
- **Captions:** about 8 px caps, with a bold lead line ending in an em dash ("GRAVITY IS SUBJECTIVE—") followed by grey caps lines.
- **Paragraph:** about 8 px sentence case, right-aligned, wrapped in "+++" markers.
- **Scale:** a dramatic 2.75:1 jump from caption to headline, with no intermediate sizes.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #efeef3 | presentation board | 52% |
| #ffffff | poster 2 page | 16% |
| #151517 | poster 3 page, all dark type | 13% |
| #cff1fe / #b2e8fd | sky-blue gradient stop | 6% |
| #fbc4c8 / #fbdcd8 | blush-pink stop | 5% |
| #a17f69 → amber/gold (approx #f5b443) | flame core on dark | 2% |

WCAG checks:
- Headline #151517 on white is 18.24:1.
- On the sky stop #cff1fe it is 15.34:1; on the pink stop #fbc4c8 it is 12.01:1, so type stays legible wherever the gradient drifts.
- White on #151517 is 18.24:1.
- Grey caption lines (≈#8a8a8a on #151517) are 5.28:1, and ≈#6b6b6b on white is 5.33:1.

## 5. Depth & material
- **Gradient:** a soft, high-blur fluid simulation with no hard edges. Streaks read like silk or aurora.
- **Dark poster:** the emission is additive. Colours bloom toward white at the hot core (yellow to white), with a faint violet and teal edge, which reads as light rather than paint.
- **Board:** posters sit flat with no shadow, as a clean presentation.

## 6. Components & patterns
- A poster triptych with a shared typographic grid but varied alignment (left / right / left).
- Glyph punctuation used as a visual motif rather than text.
- Caption blocks: bold caps lead-in, then grey caps lines.
- A light → white → dark progression across the series.

## 7. Motion
Measured: 13.73 s at 30 fps, 10 segments, motion fraction 0.41, mean energy 0.33 (very low), not a loop.
- The gradient flows continuously and slowly. The measured "segments" are just local energy swells of 0.40–1.00 s (e.g. 4.33–5.33 s, 1.00 s, ease-out; 10.50–11.40 s, 0.90 s, symmetric) on top of a near-constant drift.
- From the frames: poster 1 cycles from blush-dominant (0.76 s) to cyan (5.34 s) to magenta (9.92 s) over about 10 s. Poster 3's flame changes hue from green-lime to white to gold to teal-violet. The estimated colour cycle is about 3–4 s per hue shift.
- Type and layout are static, so all motion lives in the field.

## 8. Brand system
n/a — not a brand system, though the series behaves like one. Identity cues:
- cosmic and organic copy voice ("Darkness is alive—", "A new species has been discovered");
- `+++` and `____` as signature marks;
- three art-direction modes for one gradient.

## 9. UX
Poster and display context:
- **Strengths:** The headlines are legible over every gradient state (≥12:1). The hierarchy is instant.
- **Risks:** The microcopy at about 8 px on a 1080p presentation is decorative only. If adapted for screens as UI, it would need a minimum of 12 px.

## 10. Craft signals
- All three headlines share an identical cap height and top baseline across posters.
- Headline alignment alternates (L / R / L) to create rhythm while keeping the grid.
- `+` and `_` glyphs are used consistently as graphic punctuation in all headlines.
- Caption blocks always pair a bold lead line ending in an em dash with lighter lines.
- On the white poster the gradient is confined to the bottom about 30%, so the white space carries the type.
- The flame on black uses additive bloom to white at the core, not a saturated fill.

## 11. Reproduction recipe
```css
:root{--board:#efeef3;--ink:#151517;--sky:#b2e8fd;--blush:#fbc4c8;--peach:#fbdcd8;--ember:#f5b443;}
.poster{aspect-ratio:1/1.414;width:505px;padding:29px;position:relative;overflow:hidden;font-family:Inter,sans-serif;color:var(--ink)}
.poster h2{font:400 22px/1.2 Inter;letter-spacing:-.01em;margin:0}
.caption{font:500 8px/1.4 Inter;text-transform:uppercase;letter-spacing:.04em;color:#6b6b6b}
.caption b{color:var(--ink);font-weight:700}
.field{position:absolute;inset:0;filter:blur(40px) saturate(1.2);
  background:radial-gradient(60% 50% at 30% 30%,var(--sky),transparent 70%),
             radial-gradient(70% 50% at 60% 90%,var(--blush),transparent 70%),
             radial-gradient(50% 40% at 80% 60%,var(--peach),transparent 70%),#fff;
  animation:drift 12s ease-in-out infinite alternate}
.poster.edge .field{mask:linear-gradient(transparent 65%,#000 95%)}
.poster.dark{background:var(--ink);color:#fff}
.poster.dark .field{background:radial-gradient(40% 30% at 45% 100%,#fff,var(--ember) 30%,#5a3a7a 60%,transparent 75%);
  mix-blend-mode:screen;mask:linear-gradient(transparent 60%,#000)}
@keyframes drift{50%{background-position:20% -10%,-15% 10%,10% 20%;filter:blur(40px) hue-rotate(25deg)}}
```
For a true fluid look, use a WebGL noise-warped gradient (e.g. simplex domain warp, speed of about 0.05).

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 9 | Exquisite pastel and ember palettes with a confident Swiss-style type system. |
| Originality | 7 | Fluid gradients are a common trend; the three-density series and glyph language lift it. |
| Usability | 7 | Headlines stay readable on every state; the microcopy is decorative at screen size. |
| Craft | 8 | Shared baselines, alternating alignment and a consistent caption grammar. |

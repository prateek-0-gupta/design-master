---
id: insp-3-3
source: inspora
category: Web
status: analyzed
title: "Testimonials puzzle"
creator: "@ozzyxs1a"
styles: [playful-rounded, micro-interaction, maximalist-color, physical-material]
patterns: [jigsaw-testimonial-grid, drag-to-snap-piece, ghost-outline-slot, pastel-per-card-colour, quote-with-avatar-and-mono-role, progressive-reveal-on-completion]
mode: light
palette: ["#ffffff", "#fcd3c2", "#c2daf3", "#daf7bf", "#fbcbe5", "#dccafe", "#c2f2e2", "#222222"]
type_families: ["Inter / Geist (likely)", "Geist Mono / JetBrains Mono for role lines (likely)"]
type_class: [neo-grotesk, mono]
radius_px: [0]
motion: {durations_s: [0.2, 0.23, 0.2, 0.1], easing: [ease-out, ease-in-out], loop: false}
scores: {aesthetics: 8, originality: 9, usability: 6, craft: 8}
craft_signals: [darker-edge-strip-as-piece-thickness, ghost-outline-shows-target-slot, loose-pieces-tilted-and-unlabelled, text-only-appears-when-snapped, mono-caps-role-with-middot, one-pastel-per-testimonial]
anti_patterns: [content-hidden-until-solved, quote-marks-nearly-invisible, drag-only-interaction-risk]
---
# Testimonials puzzle — @ozzyxs1a

## 1. Snapshot
- **Subject:** A 12.1 s, 1920×1222 recording of a "What teams noticed." testimonials section built as a 3×2 jigsaw. Six pastel puzzle pieces start scattered and tilted, and each piece reveals its quote once it snaps into its slot. By t=11.4 s the board is complete.
- **Why it's remarkable:** It turns a passive testimonial grid into a tiny game. The jigsaw knobs are real interlocking geometry, and the "thickness" edge on each piece sells the cardboard.

## 2. Composition & layout
- **Header (centred):** an eyebrow "TESTIMONIALS" at about 13 px tracked caps (y≈195) and an H2 "What teams noticed." at about 34 px medium (y≈238).
- **Board:** about 1057×600 px (x 428→1485, y 322→920), with 3 columns of about 340/360/360 px and 2 rows of 300 px. Interlocking knobs (about 110 px wide, 45 px deep) sit on shared edges.
- **Empty slots:** shown as 1 px light-grey ghost outlines tracing each piece's knobs.
- **Loose pieces:** about 340 px, rotated −2° to +6°, offset up to about 130 px outside the board (e.g. the pink at x≈298 and the mint at up to x≈1668).
- **Inside a piece:** a quote mark at the top-left (y+55), a 3-line quote at about 15 px/1.5, and an avatar (40 px rounded square) with the name and a mono role line, all with about 55 px left padding.

## 3. Typography
- **Quote and name:** a neo-grotesk (Inter/Geist) in #222. Quotes are about 15 px/1.5 regular, names about 14 px medium.
- **Role and company:** "DESIGN ENGINEER · SLATE" in mono caps at about 11 px with tracking of about 0.08 em, #555, with a middot separator.
- **H2:** about 34 px with tracking of about −0.02 em. The eyebrow is about 12 px mono-ish tracked caps in #555.
- **Quote glyph:** "“" at about 20 px in a deeper tint of each piece's hue.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #ffffff | canvas | 70% |
| #fcd3c2 | piece 1 (peach) | 3.5% |
| #c2daf3 | piece 2 (sky) | 3.6% |
| #daf7bf | piece 3 (lime) | 4.1% |
| #fbcbe5 | piece 4 (pink) | 4.5% |
| #dccafe | piece 5 (lavender) | 5.5% |
| #c2f2e2 | piece 6 (mint) | 5.1% |
| #222222 / #555555 | text | — |
| #c3b1c4 / #e2e7e2 | piece-edge shadow, ghost outlines | 2% |

WCAG checks:
- #222 on peach is 11.5:1 and on sky 11.1:1.
- The role mono #555 on lavender is 4.94:1, on peach 5.41:1 and on lime 6.40:1. All pass.
- The H2 #111 on white is 18.9:1.
- The tinted quote marks (≈#e3a587 on #fcd3c2) are 1.52:1, decorative only.

## 5. Depth & material
- Each piece has a 6–8 px darker band of its own hue along the bottom edge and knob undersides (e.g. peach → #e3a587), plus a 4 px grey (#c3b1c4-ish) shadow strip below. It reads as cardboard thickness lit from above.
- Placed pieces are flat and flush, while loose pieces keep the thickness visible on their tilted edges.
- No blur shadows are used. The depth is graphic, almost isometric.

## 6. Components & patterns
- **Testimonial card:** quote, avatar, name, and role · company.
- **Puzzle mechanics:** drag a piece into its ghost slot, it snaps and the content fades in. Loose pieces are blank, so content is a reward.
- A centred section header with eyebrow and H2.

## 7. Motion
- **Measured:** 12.1 s at 30 fps. motion_fraction is 0.06, with 4 short segments:
  - 0.00–0.20 s (0.20 s, peak 0.08, ease-out);
  - 4.00–4.23 s (0.23 s, symmetric);
  - 6.00–6.20 s (0.20 s, symmetric);
  - 10.13–10.23 s (0.10 s, ease-out).
  It is not a loop (first/last diff 12.56: scattered → complete).
- **Interpretation:** the snaps are quick (about 0.1–0.23 s), and the drags between them are slow and low-energy. Pieces snap at about 2.0 s (sky), 4.0 s (lime), 6–7 s (pink), 8.7 s (lavender) and 11.4 s (mint), roughly one every 1.3–2.7 s.
- The quote text appears with the snap. No fade is longer than about 0.2 s.

## 8. Brand system
n/a — not a brand system. Identity cues:
- the pastel six-hue palette;
- mono role lines (a developer-tool tone: "pointercancel", "One file, one dependency");
- the puzzle as a metaphor for "the pieces fit".

## 9. UX
- Delightful as a showcase, but the content (social proof) is hidden until the user completes the puzzle, which most visitors won't do.
- It needs:
  - an auto-assemble on scroll, or a "solve" fallback;
  - keyboard support;
  - a way for screen readers to reach the quotes regardless of piece state.
- Text contrast inside the pieces is good.

## 10. Craft signals
- Each piece's thickness strip uses a darker shade of the same hue, not a generic grey.
- The ghost slot outlines are 1 px and trace the exact knob geometry, so the target is unambiguous.
- Knob positions alternate (tab/blank) across shared edges, so the pieces truly interlock.
- Text appears only on placed pieces, which keeps the loose pieces visually quiet.
- The role line is mono uppercase with a middot, a consistent micro-format across all six cards.
- Avatars are about 40 px rounded squares (about 8 px radius), aligned to the quote's left edge.

## 11. Reproduction recipe
```css
:root{--peach:#fcd3c2;--sky:#c2daf3;--lime:#daf7bf;--pink:#fbcbe5;--lav:#dccafe;--mint:#c2f2e2;--ink:#222;--ink-2:#555}
.board{display:grid;grid-template-columns:340px 360px 360px;grid-template-rows:300px 300px;position:relative}
.slot{outline:1px solid #e2e7e2;-webkit-mask:url(#piece-mask)}
.piece{background:var(--c);clip-path:url(#jigsaw-path);padding:55px;
  filter:drop-shadow(0 6px 0 color-mix(in srgb,var(--c),#000 18%)) drop-shadow(0 4px 0 #c3b1c4);
  transform:translate(var(--dx),var(--dy)) rotate(var(--rot));transition:transform .2s cubic-bezier(.2,.9,.3,1)}
.piece[data-placed]{--dx:0;--dy:0;--rot:0deg}
.piece:not([data-placed]) .quote{opacity:0}
.piece .quote{transition:opacity .2s ease-out;font:400 15px/1.5 Inter;color:var(--ink)}
.role{font:500 11px "Geist Mono",monospace;letter-spacing:.08em;text-transform:uppercase;color:var(--ink-2)}
@media (prefers-reduced-motion:reduce){.piece{--dx:0;--dy:0;--rot:0deg}.piece .quote{opacity:1}}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | A cheerful pastel system with tidy type. The cardboard edge adds charm. |
| Originality | 9 | A jigsaw that gates testimonials is a genuinely new take on a stale section type. |
| Usability | 6 | Social proof is hidden behind a game and drag-only interaction is risky. Good contrast once placed. |
| Craft | 8 | Precise interlocking geometry, hue-matched thickness and consistent micro-format. |

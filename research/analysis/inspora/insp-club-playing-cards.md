---
id: insp-club-playing-cards
source: inspora
category: Motion
status: analyzed
title: "club playing cards"
creator: "@MaelieLusson"
styles: [generative-particle, monochrome, high-contrast-bw, editorial-serif]
patterns: [card-sequence-flipbook, particle-starburst, rays-to-corner-index, invert-for-court-cards, mirrored-corner-indices]
mode: light
palette: ["#f5f5f5", "#ffffff", "#000000", "#7e7e7e"]
type_families: ["high-contrast transitional serif, Caslon / Times-like (likely) for indices"]
type_class: [transitional-serif]
radius_px: [24]
motion: {durations_s: [0.2], easing: [linear], loop: false}
scores: {aesthetics: 9, originality: 9, usability: 5, craft: 8}
craft_signals: [ray-anchored-to-corner-index, particle-density-gradient-to-hairline, rays-tighten-as-rank-rises, court-cards-invert-to-black, rotated-180-corner-index, consistent-card-geometry]
anti_patterns: [suit-pips-not-countable, too-fast-to-read]
---
# club playing cards — @MaelieLusson

## 1. Snapshot
- **Subject:** A 2.6 s, 1080×1350 (30 fps) flipbook through the club suit, from A to K. Each card face replaces the traditional pips with a stochastic black-particle starburst whose rays thin to hairlines and pierce the card edges. The Queen and King invert to black cards with white particles.
- **Why it's remarkable:** It re-imagines a deck as a generative system. The rank drives the shape (the cloud condenses and the rays sharpen as the value rises), and one ray always runs from the starburst into the corner index, tying the art to the typography.

  The post description mentions "3 then 8". The frames actually show A, 3, 4, 6, 7, 9, 10, Q and K, so it is a full-suit sequence. The description was checked against the frames and is inaccurate.

## 2. Composition & layout
- **Card:** about 604×917 px (x 238–842, y 216–1133), about 56% of the frame width. White with a corner radius of about 24 px, centred on a #f5f5f5 field with about 217 px top and bottom margins. The aspect is about 1:1.52, close to a poker card's 1:1.4.
- **Index:** top-left at about 28 px inset ("7♣", numeral about 75 px tall with a small club about 26 px placed superscript-right). It is repeated bottom-right rotated 180°, the classic double-ended layout.
- **Starburst:**
  - The centre sits off-axis (about x 640, y 550), right of centre, so rays reach the left edge and crop on the right edge.
  - It has 8 rays: up, down, left, up-left (ending at the index), down-left, and right-side rays cut by the card edge.
  - The vertical ray spans the full card height (y 245–1100), acting as an internal rule.

## 3. Typography
- **Indices:** a high-contrast transitional or old-style serif with a sharp diagonal "7", bracketed serifs and a calligraphic "Q" tail, close to Caslon or Times Ten. Weight is Regular.
- **Club glyph:** a solid trefoil at about 1/3 the numeral height, raised to cap-height like a superscript.
- No other text.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #f5f5f5 | page | 60% |
| #ffffff | card face (pip cards) | ~33% |
| #000000 | index, particles; card face for Q/K | ~4% (pip cards) |
| #7e7e7e | perceived mid-tone of dense particle cloud | — |

WCAG:
- The index is black on white (21:1), and on Q/K it is white on black (21:1).
- The card against the page is 1.09:1 (#fff on #f5f5f5). The card edge is defined only by this tiny shift, so it reads by shape, not border. This is a deliberate whisper.

## 5. Depth & material
- No shadows or gradients. Depth comes from **particle density**: the core is a dense stipple of 1 px dots that thins outward into rays, which taper to 1 px hairlines. The result reads like a sea urchin, a burst of ink spray or a star through a telescope, made only of black dots.
- On Q/K the inverted particles become white dust on black, a night-sky version that marks the court cards.

## 6. Components & patterns
- **Card system:** shared geometry across ranks. Only the burst parameters (core radius, ray sharpness, density) change.
- **Rank encoding through form (observed across frames):**
  - Ace: a near-uniform particle fog filling the card, with a void bottom-left.
  - 3–4: a broad, soft cloud with blurry thick rays.
  - 6–7: a defined 8-pointed star.
  - 9–10: a compact core with crisp needle rays.
  - Q/K: inverted, with the core smallest and the rays reduced to full-length 1 px lines.
- **Signature ray:** the up-left ray always terminates exactly at the corner club glyph.

## 7. Motion
The motion is measured: 2.6 s, 30 fps, motion_fraction 0.16, **0 detected segments**, and first/last diff 90.24 (A ≠ K, so not a loop).
- The profiler finds no segments because change is a hard cut at a near-constant rate (mean energy 1.44 with p95 1.65, a flat profile), not eased motion.
- **Timing:** the 9 evenly spaced frames (0.29 s apart) skip ranks (3 → 4 → 6 → 7 → 9 → 10 → Q → K). That implies about 13 cards in 2.6 s, so roughly **0.2 s per card (5 fps flipbook)**, with linear stepping. This is an estimate.
- Within a card the particles likely resettle per frame, giving a shimmering grain.
- The A → 3 jump (0.14 → 0.43 s) shows the cloud condensing from fog into rays, which reads as a dissolve or coalesce progression across the deck.

## 8. Brand system
n/a — not a brand system. It is an art deck concept: monochrome, particle-generative, serif indices and inverted court cards.

## 9. UX
- As a playing card, the rank is readable from the corner index (large, 21:1).
- **However:**
  - The suit count is no longer visible in the pips, so players lose the redundant cue.
  - The rapid 0.2 s cadence makes the reel hard to follow.
  - The off-white card on an off-white page has almost no edge definition.

## 10. Craft signals
- The up-left ray terminates on the corner club glyph on every card (A excepted).
- Ray tapering goes from a dense stipple to a 1 px hairline without aliasing (key frame, left horizontal ray at y≈550).
- The vertical ray spans the full card height, an implicit centre-right axis.
- The court cards invert the whole card face rather than adding ornament.
- The bottom index is a true 180° rotation, including the club glyph.
- Card geometry, index position and burst centre stay pixel-stable across all ranks.

## 11. Reproduction recipe
```css
:root{--page:#f5f5f5;--card:#fff;--ink:#000;--r:24px}
.card{width:604px;aspect-ratio:604/917;border-radius:var(--r);background:var(--card);position:relative;overflow:hidden}
.card.court{--card:#000;--ink:#fff}
.idx{position:absolute;top:28px;left:28px;font:400 92px/1 "Caslon","Times New Roman",serif;color:var(--ink)}
.idx sup{font-size:.34em;vertical-align:1.6em}
.idx.bottom{top:auto;left:auto;bottom:28px;right:28px;transform:rotate(180deg)}
```
```js
// canvas starburst: n rays, density falls with distance, rays taper with rank
function burst(ctx,cx,cy,rank){const core=220-rank*12, sharp=0.4+rank*0.06;
  for(let i=0;i<60000;i++){const a=Math.random()*Math.PI*2, k=8;
    const ray=Math.pow(Math.abs(Math.cos(a*k/2)),1/(1-sharp+.01));
    const r=core*Math.sqrt(Math.random())+ray*Math.random()*900*Math.random();
    ctx.fillRect(cx+Math.cos(a)*r,cy+Math.sin(a)*r,1,1);}}
// play: setInterval(nextCard,200)  // ≈0.2 s per card, hard cut
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 9 | Austere black-and-white particle art with elegant serif indices. Gallery-grade. |
| Originality | 9 | Rank expressed through starburst morphology, plus inverted court cards, is a new deck idea. |
| Usability | 5 | The index is legible, but the pip count is lost and the reel is too fast to read. |
| Craft | 8 | Consistent geometry and a clever corner-anchored ray. The near-invisible card edge on the page is a weak point. |

---
id: insp-quartr-meta
source: inspora
category: Print
status: analyzed
title: "Quartr x Meta Earnings"
creator: "haris_chc"
styles: [photo-led, duotone, grain-noise, swiss-grid-poster]
patterns: [poster-series-slideshow, sliced-portrait-collage, manifesto-text-as-texture, co-brand-lockup-header, fixed-info-block-template, pixel-square-overlay]
mode: mixed
palette: ["#181818", "#f4f4f4", "#3746bd", "#375ee9", "#3f6fec", "#6b9ff3", "#2a2a2a"]
type_families: ["Inter / Geist-style neo-grotesk with slashed zero (likely)", "handwritten script (manifesto layer)"]
type_class: [neo-grotesk, script]
radius_px: [0]
motion: {durations_s: [2.88, 0.32], easing: [hard-cut], loop: true}
scores: {aesthetics: 8, originality: 8, usability: 6, craft: 8}
craft_signals: [slashed-zero-in-time, info-block-reused-verbatim, strip-widths-vary-1-to-4, single-blue-plus-greyscale-photo, manifesto-copy-as-texture]
anti_patterns: [script-texture-unreadable, small-info-copy]
---
# Quartr x Meta Earnings — haris_chc

## 1. Snapshot
- **Subject:** A 2.88 s, 1280×1280 reel of nine poster variations announcing Meta's Q2 2026 earnings call on Quartr, cut on a #181818 stage.
- **Why it's remarkable:** It is a variation study. One greyscale portrait, one electric blue (#375ee9 family), one info block and one co-brand lockup are recombined nine ways: slices, halftone, blur glow, woven strips, pixel squares, a knotted net. The result shows how far a constrained kit stretches.

## 2. Composition & layout
- **Poster box:** about 732×938 px (x 274→1006, y 171→1109), a 0.78 / 4:5-ish portrait, identical in every cut.
- **Inner margin:** about 40 px. The lockup "QUARTR | ∞ Meta" sits at a top baseline of about y 219. The info block anchors bottom-left or bottom-right at about y 1030–1075.
- **Frame 0 (sliced):**
  - The portrait is cut into about 30 horizontal strips, each 8–20 px tall, offset ±60 px horizontally.
  - Twelve blue bars of about 12 px bleed off one edge.
  - The footer is a three-column grid: title (≈28 px) at x 315, then two 13 px columns at x 658 and x 822.
- **Key frame (1.44 s):** a full-bleed blue field with a blurred glowing face. The manifesto text fills the whole poster as about 11 px script lines, and the info block is right-aligned bottom at x≈965.
- **Other variants:**
  - the woven strip collage (1.12 s), with blue "label" cards;
  - a 40 px blue-square checker over a profile (1.76 s);
  - a 2D net of blue knotted rope (2.72 s), with text set in the net's cells.

## 3. Typography
- **Sans:** a neo-grotesk with single-storey-free, tight forms and a slashed zero ("Ø4:30 PM ET"), consistent with Inter (with `zero` feature) or Geist.
  - Title "Meta Platforms / Q2 2026 earnings call" is about 28 px Regular, leading about 1.2, tracking −0.02 em.
  - Info copy is about 13 px Medium, leading about 1.3.
- **Lockup:** "QUARTR" is a wide geometric caps wordmark at about 14 px. A 1 px vertical rule about 18 px tall separates it from the Meta logo.
- **Manifesto layer:** a casual handwritten script at about 11–12 px. It is used as texture (and once in magenta on the strip, "personal superintelligence to everyone").

## 4. Colour
| Hex | Role | Share (key) |
|---|---|---|
| #181818 | stage | 58% |
| #3746bd / #383d93 | deep blue field | 12% |
| #375ee9 / #3f6fec | electric accent (bars, squares, cards) | 6% |
| #6b9ff3 | glow highlight | 2.4% |
| #f4f4f4 | paper white (light variants) | — |
| #2a2a2a | ink | — |

WCAG checks:
- White info text on #3746bd: 7.57:1.
- White on #375ee9: 5.33:1.
- Ink on paper: 13.05:1.
- The manifesto script (≈#6b9ff3 on #3746bd) is 2.84:1, an intentional fail. It is texture, not content.

## 5. Depth & material
- Grain is visible across the blue fields (a risograph/photocopy noise feel), and the glow variant uses a 40–80 px gaussian bloom.
- Strip collages have subtle paper drop shadows (≈2 px) where strips overlap, as on the woven variant.
- Everything else is flat print.

## 6. Components & patterns
- **Lockup:** "QUARTR | Meta", placed in either top corner. On the pixel variant it sits in a blue tab (≈210×30 px).
- **Info block:** the same two-sentence copy in every frame, a reusable atom.
- **Recurring treatments:**
  - horizontal displacement slices;
  - text-as-texture;
  - pixel squares on a 40 px grid;
  - "label cards" (blue rectangles about 70×40 px with script captions) laid on a woven photo.

## 7. Motion
Measured: duration 2.88 s at 28.08 fps, motion_fraction 0.10, zero segments, mean energy 3.99 but p95 42.7. This is the signature of static holds broken by instantaneous cuts. The nine evenly spaced frames (0.16 → 2.72 s, 0.32 s apart) each show a different poster, so the dwell is about 0.32 s per poster (estimate) with no easing, which gives a strobing flip-book. seamless_loop_likely is false.

## 8. Brand system
n/a — not a brand system, but it behaves like a campaign kit: a fixed lockup, a fixed copy block, one accent hue, greyscale photography, and free image treatment. That split, with fixed rules and a free image layer, is the transferable idea.

## 9. UX
The date, time and venue are present in every variant at about 13 px, which is readable on a poster and tiny in a social square. The name "Meta" is carried by the logo only in most variants; only frame 0 has a headline.

## 10. Craft signals
- The slashed zero in "Ø4:30" avoids O/0 confusion in times.
- The info-block copy is identical across all nine variants.
- In frame 0, the blue bars alternate edges (left-bleed and right-bleed) rather than all running the same way.
- On the pixel variant, the squares sit on a strict 40 px lattice with deliberate gaps.
- The lockup is always about 40 px from the trim.

## 11. Reproduction recipe
```css
:root{--stage:#181818;--paper:#f4f4f4;--ink:#2a2a2a;--blue:#375ee9;--blue-deep:#3746bd;--glow:#6b9ff3;
  --sans:"Inter",system-ui,sans-serif;}
.poster{width:732px;aspect-ratio:732/938;background:var(--paper);padding:40px;display:grid;grid-template-rows:auto 1fr auto;
  font-family:var(--sans);font-feature-settings:"zero" 1, "tnum" 1}
.lockup{display:flex;gap:10px;align-items:center;font:600 14px/1 var(--sans);letter-spacing:.08em}
.lockup i{width:1px;height:18px;background:currentColor}
.footer{display:grid;grid-template-columns:2fr 1fr 1fr;gap:24px;font:500 13px/1.3 var(--sans)}
.footer h2{font:400 28px/1.2 var(--sans);letter-spacing:-.02em}
.slices img{clip-path:inset(0);mask:repeating-linear-gradient(#000 0 14px,transparent 14px 16px)}
.bar{height:12px;background:var(--blue)}
.glow{background:var(--blue-deep);filter:url(#grain)}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Cohesive blue/greyscale with tactile grain. |
| Originality | 8 | Nine distinct treatments from one kit. The manifesto-as-texture is a smart nod to the call content. |
| Usability | 6 | Key info is consistent but small. The script layer is purely decorative. |
| Craft | 8 | Consistent framing, lockup and copy. Careful numeral detail. |

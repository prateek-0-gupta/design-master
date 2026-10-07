---
id: insp-hairlines-v2
source: inspora
category: Illustration
status: analyzed
title: "hairlines v0.2"
creator: "Lucas (@lucasmarkes__)"
styles: [hairline-ui, technical-wireframe, isometric, editorial-serif]
patterns: [isometric-line-figure-library, live-signal-line-traversal, tick-ruler-progress, index-counter-header, catalogue-grid-overview, baseline-rule-type-reveal, npm-install-cta]
mode: light
palette: ["#efece7", "#1a1a1a", "#555350", "#8a8780", "#cac8c5", "#dbd9d6"]
type_families: ["Instrument Serif (likely, condensed high-contrast serif)", "Geist Mono / Berkeley Mono-style monospace with slashed zero (likely)"]
type_class: [editorial-serif, mono, condensed]
radius_px: []
motion: {durations_s: [0.43, 0.4, 2.33, 0.37, 0.33, 0.4, 0.67, 0.63, 0.27, 0.4], easing: [ease-out, ease-in, ease-in-out], loop: false}
scores: {aesthetics: 9, originality: 8, usability: 7, craft: 9}
craft_signals: [single-dark-line-among-grey-hairlines, tick-ruler-doubles-as-progress-bar, plus-grid-only-on-right-half, mono-labels-number-name-state, type-sits-on-drawn-baseline-rule, roman-plus-italic-in-one-headline, consistent-192px-margins]
anti_patterns: [figure-lines-1-4-to-1-on-paper, grey-meta-labels-at-3-to-1]
---
# hairlines v0.2 — Lucas (@lucasmarkes__)

## 1. Snapshot
- **Subject:** A 12 s, 3840×2160 (60 fps) launch film for "hairline v0.2.0", an npm library of isometric hairline illustrations (19 figures, 13 new: keyboard, elevator, phone, laptop, terminal, cabinet, branches, vault, lockers, padlock, patch, dish, router).
  - Each figure is drawn in pale grey hairlines while one dark "signal" line animates across it.
  - It ends on a catalogue grid and a "hairline v0.2.0 is available" title with the install command.
- **Why it's remarkable:** It is a masterclass in restraint. Hierarchy comes from line value alone: grey for objects, near-black for the one thing that moves.

## 2. Composition & layout
- **Frame grid:** margins of about 192 px on all sides.
  - Wordmark top-left, with "15 / 19" counter top-right in mono.
  - Bottom-left label "15 LOCKERS REST"; bottom-right "@lucasmarkes/hairline".
  - A tick ruler at y≈1880 spans the full width, with 19 ticks about 192 px apart.
- **Figures:** each is centred, about 1400–1900 px wide, in 30° isometric projection.
- **Background grid:** a field of faint "+" marks on about 160 px pitch, shown only on the right half of the frame (x > 1870). This is a subtle technical texture that never sits behind the label column.
- **Catalogue frame (8.67 s):** 13 figures in a loose 4/5/4 layout, each captioned with a mono index and name.
- **Final frame:** the title sits on a full-width 2 px baseline rule at y≈1200, with meta lines in mono below it.

## 3. Typography
- **Wordmark and title:** a condensed, high-contrast serif (Instrument Serif-like).
  - "hairline" is set at about 260 px x-height-to-ascender in the finale and about 80 px in the header.
  - "is available" switches to the **italic** of the same family, so one headline uses roman and italic.
- **Mono:** Geist Mono or Berkeley Mono-like with a slashed zero, used for:
  - version "v0.2.0";
  - counters "15 / 19";
  - labels "15 LOCKERS REST" (caps, about 40 px, tracking about +0.08 em);
  - "npm i @lucasmarkes/hairline".
- **Label grammar:** number (bold/dark) + NAME (dark) + STATE (grey), for example "13 BRANCHES MAIN · 7" and "09 PHONE GLASS".

## 4. Colour
| Hex | Role | Share (key frame) |
|---|---|---|
| #efece7 | warm paper | 94% |
| #dbd9d6 / #cac8c5 | figure hairlines, grid "+" marks | 6% |
| #1a1a1a (est.) | signal line, wordmark, active labels | <0.5% |
| #555350 (est.) | mid-grey version text | — |
| #8a8780 (est.) | state labels ("REST"), inactive ticks | — |

WCAG checks:
- Ink on paper is 14.77:1.
- Version grey #555350 is 6.51:1.
- State grey #8a8780 is 3.04:1, which fails AA-normal (passes large). The labels are about 40 px at 4K, roughly 20 px at 1080p.
- The figure hairlines (#cac8c5) are **1.42:1** and the grid (#dbd9d6) is 1.2:1. This is intentionally whisper-quiet, but the illustrations would vanish on lower-quality displays.

Strategy: a strict achromatic, warm-grey system with exactly one ink value for "active".

## 5. Depth & material
- There are no fills, shadows or colours. Depth is purely isometric linework.
- Some figures (lockers, terminal, phone "glass") use stacked offset hairlines (5–8 parallel copies about 4 px apart) to suggest thickness or translucency. This is the "glass" state.
- A very light paper grain is visible on the background.

## 6. Components & patterns
- **Signal line:** a single near-black path that traces through each object (a sine through the lockers, a branch curve through the switches, a cable through the phone). It is the motion's protagonist and the library's "live" element.
- **Tick ruler:** a progress indicator. Past ticks are dark and about 30 px tall, the current tick is taller (about 70 px), and future ticks are faint and short.
- **Index counter** "NN / 19" at the top-right.
- **Catalogue overview** with captions, then a title card with the CTA as a terminal command.

## 7. Motion
These figures are measured: 12.0 s at 60 fps, motion_fraction 0.49, 10 segments, median 0.40 s.

| Segment | Time | Duration | Shape |
|---|---|---|---|
| 1 | 0.03–0.47 s | 0.43 s | ease-out |
| 2 | 0.77–1.17 s | 0.40 s | ease-out |
| 3 | 1.57–3.90 s | 2.33 s | ease-in (peak_at 0.92) |
| 4 | 4.10–4.47 s | 0.37 s | ease-in-out |
| 5 | 4.67–5.00 s | 0.33 s | ease-out |
| 6 | 5.33–5.73 s | 0.40 s | ease-in-out |
| 7 | 5.93–6.60 s | 0.67 s | ease-out (peak 0.07) |
| 8 | 7.17–7.80 s | 0.63 s | ease-in-out |
| 9 | 8.97–9.23 s | 0.27 s | ease-in |
| 10 | 9.90–10.30 s | 0.40 s | ease-in-out |

- **Segment 3** is the longest move: an accelerating figure sequence (phone → terminal), where figure swaps speed up.
- **Segment 9** is the snap into the catalogue grid.
- **Segment 10** is the title rising from behind the baseline rule (at 10.00 s, "hairline 0.2.0" is masked, cut off by the rule).

Rhythm: short swaps of about 0.4 s separated by holds of about 0.2–0.6 s, which suits a figure every about 0.65 s. Not a loop (first-to-last difference 5.61).

## 8. Brand system
This is a library launch, not a full brand system. Cues:
- **Logotype:** lowercase condensed serif "hairline" plus the version in mono.
- **Tokens:** paper #efece7, ink #1a1a1a, two greys; 192 px margins; mono caps labels.
- **Naming convention:** NN NAME STATE (for example "09 PHONE GLASS", "15 LOCKERS REST"), so figures ship with states.
- **Voice:** developer-direct, with "npm i" as the CTA.

## 9. UX
- The counter, the tick ruler and the catalogue give excellent orientation within a 12 s piece.
- The CTA is literal and copy-pasteable.
- The figure lines (1.42:1) and state labels (3.04:1) are below comfortable contrast, an aesthetic choice that hurts reproduction at small or compressed sizes.

## 10. Craft signals
- Exactly one dark line per scene; everything else is #cac8c5–#dbd9d6.
- The tick ruler encodes past, current and future by height and value, and doubles as a progress bar.
- The "+" grid appears only in the right half, keeping the label column clean.
- The title sits exactly on a 2 px rule, and the reveal is masked by that same rule.
- The roman "hairline" pairs with the italic "is available" in one family.
- Every corner element sits on the same 192 px margin box.
- Mono labels use a strict "number / name / state" grammar with value-coded emphasis.

## 11. Reproduction recipe
```css
:root{--paper:#efece7;--ink:#1a1a1a;--ink-2:#555350;--ink-3:#8a8780;--line:#cac8c5;--grid:#dbd9d6;--m:192px;
  --serif:"Instrument Serif",Georgia,serif;--mono:"Geist Mono","Berkeley Mono",ui-monospace,monospace}
.frame{background:var(--paper);padding:var(--m);position:relative}
.frame::after{content:"";position:absolute;inset:0 0 0 50%;pointer-events:none;
  background:url("data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' width='160' height='160'><path d='M80 73v14M73 80h14' stroke='%23dbd9d6' stroke-width='2'/></svg>")}
.logo{font:400 80px/1 var(--serif);letter-spacing:-.01em}.logo small{font:500 32px var(--mono);color:var(--ink-2)}
.label{font:500 40px/1 var(--mono);letter-spacing:.08em;text-transform:uppercase;color:var(--ink)}.label .state{color:var(--ink-3)}
.figure path{stroke:var(--line);stroke-width:2;fill:none}.figure .signal{stroke:var(--ink);stroke-width:3;
  stroke-dasharray:1;stroke-dashoffset:1;pathLength:1;animation:trace .63s cubic-bezier(.45,0,.55,1) forwards}
@keyframes trace{to{stroke-dashoffset:0}}
.ticks i{width:2px;height:16px;background:var(--grid)}.ticks i.done{height:30px;background:var(--ink)}.ticks i.now{height:70px}
.title{font:400 260px/1 var(--serif);border-bottom:2px solid var(--ink);overflow:hidden}
.title em{font-style:italic}.title span{display:inline-block;animation:rise .4s cubic-bezier(.45,0,.55,1)}
@keyframes rise{from{transform:translateY(100%)}}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 9 | Calm paper and hairline world, beautiful serif/mono pairing and a single dark line as the hero. |
| Originality | 8 | The "signal line through grey objects" idea gives an illustration library a living identity. |
| Usability | 7 | Superb orientation devices; the hairlines and state labels are under-contrasted. |
| Craft | 9 | Exact margins, rule-masked type reveal, value-coded ticks and a disciplined label grammar. |

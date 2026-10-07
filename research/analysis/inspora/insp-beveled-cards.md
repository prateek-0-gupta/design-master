---
id: insp-beveled-cards
source: inspora
category: Web
status: analyzed
title: "beveled cards"
creator: "@RachitThakur146"
styles: [technical-wireframe, swiss-grid-poster, hairline-ui]
patterns: [chamfered-corner-cards, split-card-media-caption, line-diagram-illustrations, hover-redraw-illustration, numbered-card-index, dotted-rule-section-label, crop-mark-frames]
mode: dark
palette: ["#2b2b29", "#e04421", "#ebe3d6", "#e0d9c9", "#cfc8ba", "#1a1a1a", "#6e3426", "#8a8478"]
type_families: ["Inter Tight / Inter Display (likely)", "small monospace for indices (likely)"]
type_class: [neo-grotesk, mono]
radius_px: []
motion: {durations_s: [0.47, 0.13, 0.1], easing: [ease-out], loop: true}
scores: {aesthetics: 8, originality: 8, usability: 6, craft: 8}
craft_signals: [chamfered-6px-corners-not-radius, crop-marks-inside-media-well, dot-grid-texture-in-panels, card-split-into-two-tiles, 001-002-003-mono-indices, ruled-line-weight-consistent-1px]
anti_patterns: [black-text-on-orange-borderline, mono-index-near-invisible]
---
# beveled cards — @RachitThakur146

## 1. Snapshot
- **Subject:** A 16.9 s, 1280×720 recording of a "FEATURES" row of three AI-support feature cards ("Smart Actions", "Auto-Resolve", "Agent assist"). Each pairs a technical line drawing (concentric ±circles, a ruled triangle, a Venn diagram) with a short caption tile. Hovering redraws the drawing.
- **Why it's remarkable:** It reads as engineering drafting paper. Chamfered (beveled) corners instead of radii, crop marks, a dot grid, mono serial numbers and pure 1 px line art give an AI SaaS section a physical, blueprint-like identity.

## 2. Composition & layout
- **Section header:** "◇ FEATURES" in about 10 px tracked caps (#8a8478) followed by a dotted rule running to x≈1056, at y≈167.
- **Cards:**
  - three columns, each about 272 px wide, with an ~8 px gutter, spanning x≈223→1057 (about 834 px, 65% of the width), centred;
  - each card is two stacked tiles: an upper tile about 272×298 px (title row plus media well) and a lower caption tile about 272×70 px, with an ~6 px gap;
  - this "split card" gives a label/specimen feel.
- **Upper tile contents:** title 16 px bold at top-left (x+12), mono index ("001") at top-right, and a media well inset ~12 px with corner crop marks.
- **Background:** #2b2b29 with a faint ~40 px square grid (about 4% lighter lines), visible in the corners.

## 3. Typography
- **Titles:** a compact neo-grotesk (Inter Tight / Inter Display semibold) at about 16 px with −0.01 em tracking.
- **Captions:** the same family at about 11 px regular, wrapped at about 26 characters.
- **Indices:** "001 / 002 / 003" in a small mono (about 8 px), barely visible.
- **Section label:** "FEATURES" in about 10 px caps with +0.2 em tracking.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #2b2b29 | warm-charcoal canvas | 66% |
| #e04421 | signal orange (feature 1 / active) | 11% |
| #ebe3d6 / #e0d9c9 | cream paper tiles | 17% |
| #cfc8ba | dot grid on paper, shadows | 4% |
| #1a1a1a | line art + text | <1% |
| #6e3426 / #b4664d | dot grid on orange | 2% |
| #8a8478 | section label, index | <1% |

WCAG checks:
- Black text on cream #ebe3d6 is 13.67:1.
- Black on orange #e04421 is **4.16:1**, which fails AA for the 11 px caption and passes only for the 16 px bold title (large-bold threshold is 14 pt bold, so it still fails strictly).
- The label #8a8478 on the canvas is 3.82:1.
- A mono index at about #a09a8e on cream is 2.2:1.

## 5. Depth & material
- **Shape:** each tile is a flat polygon with 45° chamfered corners of about 6 px (via `clip-path`), with no shadow or border.
- **Texture:** a ~6 px dot grid at low contrast inside the tiles (darker dots on orange, grey on cream) gives a graph-paper feel.
- **Crop marks:** L-shaped 1 px corner ticks (~8 px) frame each media well, like printer registration marks.
- **Line art:** pure 1–1.25 px strokes in #1a1a1a. The Venn intersection is hatched at 45°, and the triangle has radiating ruled lines (a string-art fan).

## 6. Components & patterns
- A feature card made of a specimen tile plus a caption tile with a kebab "⋮" at the bottom-right of the caption.
- **Active/highlight card:** orange fill (first card); the others are cream. This is a one-hot emphasis.
- **Hover:** the card lifts about 3 px (the key frame shows the middle card at y≈181 vs 184) and its drawing redraws. At t=2.82 s the triangle has reset to an outline plus centre line, and by 4.69 s the fan lines have reappeared.

## 7. Motion
Measured: 16.9 s at 60 fps, motion fraction only 0.07, `seamless_loop_likely: true`. Segments:

| Start–end | Duration | Shape (peak_at) |
|---|---|---|
| 3.10–3.57 s | 0.47 s | ease-out (0.04) |
| 11.57–11.70 s | 0.13 s | symmetric |
| 11.90–12.00 s | 0.1 s | symmetric |
| 12.50–12.63 s | 0.13 s | ease-out (0.12) |
| 13.87–13.97 s | 0.1 s | ease-out (0.17) |

The 0.47 s segment is the main redraw: lines stroke in fast and settle, a very front-loaded energy. The 0.1–0.13 s blips are hover lifts and returns as the cursor crosses cards (around 10.33–14.08 s).

The motion is extremely economical: the page is still about 93% of the time.

## 8. Brand system
n/a — not a brand system. Identity cues: a technical-drawing language (chamfers, crop marks, dot grid, serials), one signal orange on warm neutrals, and geometric diagrams as feature metaphors (stacked ± for actions, a converging fan for resolution, overlap for assist).

## 9. UX
- **Strengths:** Three scannable cards with distinct pictograms; short captions; hover reward.
- **Risks:**
  - The orange card's caption contrast is borderline.
  - Indices and the kebab are near-invisible.
  - The reason the first card is orange is unclear (is it selected or just an accent?).
  - Abstract diagrams need the titles to carry meaning.

## 10. Craft signals
- The corners are 45° chamfers of about 6 px on every tile, with no border-radius anywhere.
- Crop marks sit inside the media well about 4 px from its corners, all at a 1 px line weight matching the diagrams.
- The dot grid changes tint per surface (rust dots on orange, sand dots on cream) rather than one overlay.
- Each card is split into two tiles with a 6 px gap matching the gutter rhythm (8 px between cards).
- Mono serials 001–003 are top-right-aligned with the title baseline.
- The section header's dotted rule ends flush with the last card's right edge.

## 11. Reproduction recipe
```css
:root{--bg:#2b2b29;--paper:#ebe3d6;--signal:#e04421;--ink:#1a1a1a;--mute:#8a8478;--cut:6px}
body{background:var(--bg);
  background-image:linear-gradient(#ffffff08 1px,transparent 1px),linear-gradient(90deg,#ffffff08 1px,transparent 1px);
  background-size:40px 40px}
.tile{background:var(--paper);color:var(--ink);
  clip-path:polygon(var(--cut) 0,calc(100% - var(--cut)) 0,100% var(--cut),100% calc(100% - var(--cut)),
    calc(100% - var(--cut)) 100%,var(--cut) 100%,0 calc(100% - var(--cut)),0 var(--cut));
  transition:transform .13s ease-out}
.card:hover .tile{transform:translateY(-3px)}
.tile.signal{background:var(--signal)}
.well{background-image:radial-gradient(#00000022 .6px,transparent .8px);background-size:6px 6px;position:relative}
.well::before{content:"";position:absolute;inset:4px;
  background:linear-gradient(var(--ink),var(--ink)) 0 0/8px 1px no-repeat, linear-gradient(var(--ink),var(--ink)) 0 0/1px 8px no-repeat}
.diagram path{stroke:var(--ink);stroke-width:1;fill:none;stroke-dasharray:var(--len);stroke-dashoffset:0}
.card:hover .diagram path{animation:redraw .47s cubic-bezier(.1,.8,.2,1) both}
@keyframes redraw{from{stroke-dashoffset:var(--len)}}
.index{font:400 8px "JetBrains Mono",monospace;color:var(--mute)}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Warm charcoal, cream and signal orange with drafting details is distinctive and cohesive. |
| Originality | 8 | Chamfered specimen cards with redrawing geometric diagrams avoid SaaS clichés. |
| Usability | 6 | Clear, but the small captions and indices are low contrast and the orange emphasis is ambiguous. |
| Craft | 8 | Consistent 1 px stroke system, chamfer size and gutter rhythm. |

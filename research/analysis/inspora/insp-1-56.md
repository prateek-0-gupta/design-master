---
id: insp-1-56
source: inspora
category: Branding
status: analyzed
title: "Spiderman icon"
creator: "@exteedesign"
styles: [skeuomorphic, soft-3d, physical-material]
patterns: [character-detail-crop-icon, squircle-icon-tile, ghost-neighbour-tiles, embossed-line-pattern, single-feature-icon]
mode: light
palette: ["#fdfdfd", "#e7e7e7", "#d60e18", "#e92132", "#a90913", "#211316", "#c9c9ca"]
type_families: []
type_class: []
radius_px: [210]
motion: null
scores: {aesthetics: 8, originality: 6, usability: 8, craft: 9}
craft_signals: [diagonal-micro-twill-texture, raised-web-ridges-with-shadow, bevelled-eye-frame, frosted-lens-gradient, ghost-grid-context, top-left-light-consistency, edge-darkening-on-tile]
anti_patterns: [licensed-character-fan-art, ghost-tiles-near-invisible]
---
# Spiderman icon — @exteedesign

## 1. Snapshot
- **Subject:** A single 2048×2048 render of an app icon showing an extreme close-up of a red suit with a raised white web and one black-framed white eye lens. It sits in a home-screen grid of blank ghost tiles.
- **Why it's remarkable:** Instead of drawing the whole mask, it crops to one eye plus the web. The detail is iconic enough to identify the character, and it fills the tile with a big, legible shape.

## 2. Composition & layout
- **Tile:** About 1220×1220 px (x≈385→1605, y≈385→1605 in the original), so about 60% of the canvas. The corner radius is about 210 px (17%), squircle-like.
- **Context:** Ghost neighbour tiles in #e7e7e7 peek in from all eight sides, cropped at the canvas edge. They hint at a home-screen grid with about 160 px gutters.
- **Eye:**
  - The black frame spans from about (535, 1690) at the bottom-left to (1360, 470) at the top-right of the tile area, so it runs at about 40° and covers roughly 55% of the tile area.
  - The tip breaks above the web at the top right but stays about 70 px inside the tile edge. Nothing bleeds out.
- **Web:** The white web radiates from an implied centre at the bottom-left (about 520, 900), so the composition reads as a crop of a larger face.

## 3. Typography
None.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #fdfdfd | canvas | 37% |
| #e7e7e7 / #c9c9ca | ghost tiles, lens shading | 34% |
| #d60e18 / #e92132 | suit red (base / twill highlight) | 13% |
| #a90913 | red shade at tile bottom & twill grooves | 7% |
| #211316 | eye frame (warm near-black) | 6% |
| #ffffff | web ridges, lens highlight | — |

WCAG checks (graphical):
- White web on red: 5.34:1.
- The tile against the canvas: 5.25:1 (red on #fdfdfd).
- Black frame on red: 3.37:1, which is enough for a 30–50 px stroke.
- Frame against the frosted lens (#e0e0e2): 13.62:1.
- Ghost tiles on canvas: **1.22:1** (intentionally faint).

## 5. Depth & material
- **Fabric:** The suit has a fine 45° twill stripe (about 6 px pitch) in two reds, a convincing woven texture. The tile darkens toward the bottom-right edge (#a90913) to round it.
- **Web lines:** About 22 px wide raised ridges with a soft shadow on the lower-right side, so they read as embossed piping.
- **Eye frame:**
  - A bevelled black rim about 55 px thick with a satin highlight on its upper edge and a crisp inner lip.
  - The lens is frosted white-to-grey with a vertical light streak, like a reflective mesh.
- **Shadow:** A large soft drop shadow (about 0 40 80 rgba(0,0,0,.15)) lifts the tile off the canvas.

## 6. Components & patterns
- **Single-feature icon:** reduce a character to its single most distinctive feature (the eye shape) on its signature surface (red + web).
- **Presentation:** ghost-grid neighbours give a sense of scale and an OS context without competing.

## 7. Motion
Still image, so no motion was observed. A natural extension would be a subtle lens "squint" (scaleY 1→0.85, 0.25 s ease-out) on tap.

## 8. Brand system
n/a — not a brand system. This is fan art of a licensed character. Identity cues: the red, the web and the eye lens are the franchise's own codes. The technique of "crop to signature feature + signature texture" is the transferable part.

## 9. UX
- **Strengths:**
  - Highly recognisable at 60 pt.
  - The big black/white shape survives downscaling.
  - The web lines thin out but the eye remains.
- **Risks:**
  - The twill texture will moiré or disappear below about 120 px.
  - Using IP without a licence makes it a portfolio-only piece.

## 10. Craft signals
- The twill stripe is 45° and runs perpendicular to the eye's long axis, so the textures don't fight.
- Web ridges carry a consistent lower-right shadow matching the top-left key light.
- The eye frame is warm near-black (#211316), not neutral, harmonising with the red.
- The lens gradient includes a vertical specular streak suggesting a curved surface.
- The tile has edge-darkening to #a90913 at the bottom for a domed read.
- Ghost tiles use the same radius and gutter as the hero tile.

## 11. Reproduction recipe
```css
:root{--red:#d60e18;--red-hi:#e92132;--red-lo:#a90913;--ink:#211316;--ghost:#e7e7e7;--canvas:#fdfdfd}
body{background:var(--canvas)}
.icon{width:1024px;aspect-ratio:1;border-radius:17.5%;
  background:
    repeating-linear-gradient(45deg,var(--red-hi) 0 3px,var(--red) 3px 6px),
    var(--red);
  box-shadow:inset 0 -40px 80px rgba(80,0,0,.35),inset 0 6px 10px rgba(255,255,255,.2),0 40px 80px rgba(0,0,0,.15)}
.web path{stroke:#fff;stroke-width:22;fill:none;stroke-linecap:round;filter:drop-shadow(4px 6px 4px rgba(90,0,0,.45))}
.eye-frame{fill:var(--ink);filter:drop-shadow(0 12px 18px rgba(0,0,0,.35))}
.eye-lens{fill:url(#lens)} /* linearGradient #f4f4f6 → #c9c9ca with a white vertical streak */
.ghost{background:var(--ghost);border-radius:17.5%}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Bold, tactile and instantly readable, with refined presentation. |
| Originality | 6 | The crop idea is smart, but the subject is borrowed IP and skeuomorphic hero icons are well trodden. |
| Usability | 8 | Strong silhouette at small sizes; the texture is lost at small sizes. |
| Craft | 9 | Texture, bevel, shadow direction and colour temperature are all controlled. |

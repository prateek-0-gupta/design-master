---
id: insp-4-2
source: inspora
category: Branding
status: analyzed
title: "A soft-UI app icon"
creator: "@luoyyisvic"
styles: [soft-3d, minimal-swiss, physical-material]
patterns: [swatch-dot-grid-icon, triangular-staircase-arrangement, plus-glyph-add-affordance, icon-in-dock-mockup, white-tile-icon]
mode: light
palette: ["#ebebeb", "#ffffff", "#ffd500", "#ffa69e", "#005e4a", "#577e8f", "#e8002a", "#8a5100", "#4b525c"]
type_families: []
type_class: []
radius_px: [290]
motion: null
scores: {aesthetics: 8, originality: 7, usability: 8, craft: 9}
craft_signals: [coloured-glow-shadow-per-dot, inner-rim-highlight-on-dots, extruded-plus-glyph, 3x3-grid-with-empty-cells, white-tile-subtle-gradient, in-context-dock-proof]
anti_patterns: [white-tile-on-light-bg-low-edge-contrast, yellow-and-pink-dots-low-contrast]
---
# A soft-UI app icon — @luoyyisvic

## 1. Snapshot
- **Subject:** Two 2160×2160 slides of an icon for a colour/palette app. A white squircle holds six glossy colour "buttons" stacked in a staircase (1/2/3 per row) on a 3×3 grid, plus a grey extruded "+" in the empty top-right cell. Slide 2 shows it in an iPhone dock beside Safari and Messages.
- **Why it's remarkable:** The arrangement is a diagram of "add a colour": the staircase leaves exactly one empty diagonal, and the "+" fills the top-right gap, so the composition implies the next action.

## 2. Composition & layout
- **Slide 1:** The tile is about 1155×1155 px (x≈465–1620 in the original), centred on #ebebeb. Its corner radius is about 290 px (25%), squircle-like.
- **Grid:** A 3×3 grid at a pitch of about 308 px. Each dot is about 270 px across, leaving a gap of about 38 px. The grid inset from the tile edge is about 135 px.
- **Placement:** Dots occupy cells (1,1), (2,1), (2,2), (3,1), (3,2) and (3,3), a lower-left triangle. The "+" sits at (1,3), about 270 px across with a stroke of about 40 px. Cells (1,2) and (2,3) are deliberately empty, giving a diagonal breathing channel.
- **Slide 2:** In the dock the icon renders at about 430 px in a 2160 frame. It is shown cropped at the device's bottom-left corner over a deep-blue wallpaper (#023a55 → #01134c).

## 3. Typography
None. The "+" is the only glyph, constructed as two round-capped bars.

## 4. Colour
| Hex (est. from pixels) | Role |
|---|---|
| #ebebeb | presentation background (79%) |
| #ffffff → #f2f2f2 | icon tile (subtle top-to-bottom gradient) |
| #ffd500 | yellow dot |
| #ffa69e | salmon-pink dot |
| #005e4a | bottle-green dot |
| #577e8f | slate-blue dot |
| #e8002a | signal red dot |
| #8a5100 | caramel-brown dot |
| #4b525c | "+" glyph |
| #023a55 / #01134c | wallpaper in slide 2 |

Contrast against the tile (#f7f7f7, graphical 3:1 target):

| Element | Ratio | Result |
|---|---|---|
| Green | 7.26 | pass |
| "+" | 7.37 | pass |
| Brown | 6.02 | pass |
| Red | 4.39 | pass |
| Slate | 4.1 | pass |
| **Yellow** | **1.33** | fail |
| **Pink** | **1.75** | fail |

The yellow and pink dots rely on hue and their coloured shadows to separate from the tile. The tile on the #ebebeb backdrop is only 1.19:1, which is why slide 2 proves it on a dark wallpaper.

The palette is a curated, slightly retro set: one warm primary (yellow), one cool primary (red), and earthy secondaries. It is not a rainbow.

## 5. Depth & material
- **Dots:** Each dot is a glossy acrylic disc with:
  - a thin lighter rim along the upper-left (inner bevel, about 6 px);
  - a flat face;
  - a tinted, coloured shadow below-right (yellow casts a yellow glow, red a pink one).
- **"+":** A rounded extruded bar with a top highlight and a soft grey drop shadow, matching the dots' lighting.
- **Tile:** Near-flat white with a faint vertical gradient and a 1–2 px lighter edge. It gets no heavy shadow, hence "soft UI".

## 6. Components & patterns
- **Swatch-grid icon:** for a palette, theme or colour app.
- **Staircase arrangement:** reads as a growing collection.
- **"+" in the next empty cell:** the create affordance is embedded in the icon.
- **In-context dock mockup:** validates the icon at real size next to system icons.

## 7. Motion
Still images, so no motion was observed. A natural extension is the dots popping in row by row (scale 0.6→1, 0.25 s, ease-out with about 40 ms stagger), with the "+" rotating 90° last.

## 8. Brand system
n/a — not a brand system. Identity cues: the six-swatch palette could become the app's theme set, and the "+" suggests a "make your own palette" proposition.

## 9. UX
- **At dock size (about 60 pt):** Six dots remain countable and distinct (slide 2 proves it), and the "+" remains readable.
- **Risks:**
  - On light wallpapers the white tile nearly disappears.
  - At 29 pt (Settings) the dots will merge into a confetti blur.

## 10. Craft signals
- Each dot's shadow is tinted with its own hue rather than black (visible pink under the red, ochre under the brown).
- The 3×3 grid is respected exactly, and the empty cells are intentional.
- The "+" has the same diameter as the dots, so it occupies its cell like a seventh button.
- The light source is consistent (top-left) across the dots, the "+" and the tile edge.
- The tile corner radius matches the iOS app-icon mask when placed in the dock (slide 2 aligns with Safari).

## 11. Reproduction recipe
```css
:root{--tile:#fff;--bg:#ebebeb;--y:#ffd500;--p:#ffa69e;--g:#005e4a;--s:#577e8f;--r:#e8002a;--b:#8a5100;--plus:#4b525c}
.icon{width:1024px;aspect-ratio:1;border-radius:25%;padding:12%;
  background:linear-gradient(#fff,#f2f2f2);display:grid;grid-template:repeat(3,1fr)/repeat(3,1fr);gap:3.3%;
  box-shadow:inset 0 2px 0 #fff,0 10px 30px rgba(0,0,0,.06)}
.dot{border-radius:50%;background:var(--c);
  box-shadow:inset 3px 4px 0 rgba(255,255,255,.35),inset -2px -3px 6px rgba(0,0,0,.12),
             6px 12px 20px color-mix(in srgb,var(--c) 45%,transparent)}
.plus{position:relative}
.plus::before,.plus::after{content:"";position:absolute;inset:44% 0;border-radius:9999px;background:var(--plus);
  box-shadow:inset 0 2px 0 rgba(255,255,255,.3),4px 8px 12px rgba(0,0,0,.18)}
.plus::after{inset:0 44%}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Calm white tile, an appealing curated palette, tactile dots. |
| Originality | 7 | A swatch grid is expected, but the staircase plus the embedded "+" add meaning. |
| Usability | 8 | Reads in the dock and implies the create action; weak on light wallpapers. |
| Craft | 9 | Hue-tinted shadows, an exact grid and lighting consistent across all elements. |

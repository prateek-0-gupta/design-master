---
id: insp-2-2
source: inspora
category: Illustration
status: analyzed
title: "MacOS"
creator: "@AndreaCopellino"
styles: [playful-rounded, soft-3d, grain-noise, x-object-mashup]
patterns: [window-traffic-lights-reskin, gamecube-button-cluster, size-encodes-priority, kidney-shaped-button, corner-hugging-control]
mode: mixed
palette: ["#5b60b1", "#4f539c", "#8e91c7", "#8587b8", "#42ad5d", "#e94f4a", "#eba337", "#215730"]
type_families: []
type_class: []
radius_px: [9999, 60]
motion: null
scores: {aesthetics: 8, originality: 9, usability: 5, craft: 8}
craft_signals: [same-hue-dark-glyphs, kidney-follows-window-corner, grain-on-every-surface, light-top-rim-on-buttons, gamecube-indigo-palette, hierarchy-by-size]
anti_patterns: [glyph-contrast-below-3, primary-action-swapped, unfamiliar-positions]
---
# MacOS — @AndreaCopellino

## 1. Snapshot
- **Subject:** A single 1629×1472 still: the macOS window controls (close, minimise, zoom) re-imagined as the Nintendo GameCube face buttons on a GameCube-indigo desktop.
- **Why it's remarkable:** It maps a famous button cluster onto another famous cluster almost one-to-one:
  - big green A becomes zoom/full-screen;
  - small red B becomes close;
  - the yellow C-stick-style kidney becomes minimise and wraps the window's corner.

## 2. Composition & layout
- A rounded window (corner radius ~60 px, left edge x≈257, top y≈257) fills the lower-right two-thirds on a darker indigo desktop.
- **Green "A" (zoom):** ~390 px diameter, centred at (592, 590), overlapping the window's top-left area.
- **Red "B" (close):** ~200 px, centred at (944, 590), on the same baseline as the green button. The ~60 px gap equals the window radius.
- **Yellow kidney (minimise):** ~300×200 px. It sits diagonally on the window corner, bridging the desktop and the window, with its curve parallel to the corner radius.
- The rest of the frame is empty texture, which keeps all attention on the cluster.

## 3. Typography
None. Glyphs are pictograms only:
- **Zoom:** a GameCube-like diagonal-split square, ~95 px.
- **Close:** a × with ~22 px rounded strokes.
- **Minimise:** a dash, ~90×22 px with rounded ends.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #5b60b1 / #4f539c | desktop (GameCube indigo) | 30% |
| #8e91c7 / #8587b8 | window surface (lavender-grey) | 61% |
| #42ad5d | zoom / "A" button | 5% |
| #e94f4a | close / "B" button | ~2% |
| #eba337 | minimise / kidney | ~2% |
| #215730 / #7b2927 / #7a551d | glyphs, darker shade of each button hue | <1% |

WCAG:
- Green glyph #1e5a2e on #42ad5d is **2.88:1**.
- Red glyph on red is 3.14:1.
- Yellow glyph on yellow is 4.21:1.
- Window vs desktop is 1.87:1, so the window edge relies on shadow and value.

The traffic-light hues are shifted toward the GameCube's softer, slightly desaturated red/green/yellow so they harmonise with the indigo.

## 5. Depth & material
- **Buttons:** convex plastic. Each has a 3–4 px lighter rim on the top edge, a slightly darker outline (~2 px, same hue), and a soft drop shadow (~12 px blur) onto the lavender window.
- **Kidney:** casts a shadow across both surfaces, which confirms it floats above the corner.
- **Grain:** a fine monochrome noise covers every surface (desktop, window, buttons), giving a moulded-plastic feel and avoiding banding.
- **Window:** a faint 1–2 px lighter top edge plus a soft shadow onto the desktop.

## 6. Components & patterns
- **Window chrome controls,** re-skinned. The functions are kept but size and shape are reassigned: zoom becomes the dominant target and close becomes secondary.
- **Corner-hugging control:** the kidney's inner curve follows the window corner radius, the same "path derived from container" idea seen in other corner controls.

## 7. Motion
None: still image. The shapes invite a press-depth animation (translateY 3–4 px with the shadow collapsing), but nothing is shown.

## 8. Brand system
n/a — not a brand system. It is a mash-up of two product identities: Nintendo's GameCube palette and button geometry, and Apple's traffic-light semantics.

## 9. UX
- **As a joke or concept it lands;** as UI it inverts the macOS conventions:
  - close is no longer leftmost or first;
  - zoom becomes the largest target, which invites accidental full-screen;
  - minimise is an odd shape that is hard to hit precisely at real size.
- Glyph contrast is low (2.9:1 on green).
- On the plus side, colour, size and shape all differ, so the three controls are distinguishable without colour vision.

## 10. Craft signals
- Each glyph is a darker shade of its own button hue (#215730 on #42ad5d), never black.
- The kidney's inner curve is concentric with the window corner (~60 px radius plus its offset).
- The gap between green and red (~60 px) equals the window corner radius.
- One consistent top-left light source: the rim highlight is on the upper edge and shadows fall down-right.
- Uniform noise grain is applied at the same scale on all layers.
- The green glyph reproduces the GameCube "A" diagonal motif rather than a generic expand arrow.

## 11. Reproduction recipe
```css
:root{--desk:#5b60b1;--win:#8e91c7;--a:#42ad5d;--b:#e94f4a;--c:#eba337;--r-win:60px}
body{background:var(--desk) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='120' height='120'%3E%3Cfilter id='n'%3E%3CfeTurbulence baseFrequency='.9'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='.08'/%3E%3C/svg%3E")}
.window{background:var(--win);border-radius:var(--r-win);box-shadow:0 20px 50px rgba(30,30,90,.35),inset 0 2px 0 rgb(255 255 255/.25)}
.btn{border-radius:50%;box-shadow:inset 0 3px 0 rgb(255 255 255/.25),inset 0 0 0 2px rgb(0 0 0/.08),0 8px 14px rgb(30 30 90/.25)}
.btn.zoom{width:390px;aspect-ratio:1;background:var(--a);color:#215730}
.btn.close{width:200px;aspect-ratio:1;background:var(--b);color:#7b2927}
.btn.min{width:300px;height:140px;border-radius:70px;background:var(--c);transform:rotate(-40deg);color:#7a551d}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Charming, harmonious palette, with the grain and plastic shading spot-on. |
| Originality | 9 | A witty and precise semantic mash-up. The kidney-on-corner is inspired. |
| Usability | 5 | Breaks macOS conventions and glyph contrast is weak. It is a concept, not a usable control set. |
| Craft | 8 | Consistent light, same-hue glyphs and geometric echoes of the window radius. |

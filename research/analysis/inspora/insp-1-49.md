---
id: insp-1-49
source: inspora
category: Branding
status: analyzed
title: "App icon concepts"
creator: "@dmiiiitrii"
styles: [soft-3d, playful-rounded, maximalist-color, claymorphism]
patterns: [app-icon-carousel, mascot-face-glyph, squircle-icon-tile, tinted-backdrop-per-icon, layered-card-glyph, glossy-blob-character]
mode: mixed
palette: ["#434cf4", "#43a6fb", "#e5e3fd", "#ffffff", "#3cc81a", "#2e0a8c", "#b84dff", "#ff7a1a"]
type_families: []
type_class: []
radius_px: [100]
motion: {durations_s: [9.6, 1.07], easing: [hard-cut], loop: false}
scores: {aesthetics: 8, originality: 6, usability: 8, craft: 8}
craft_signals: [two-dot-eyes-as-system, top-to-bottom-tile-gradient, backdrop-hue-keyed-to-icon, soft-floor-shadow-under-tile, white-rim-on-sticker-glyphs, consistent-icon-scale]
anti_patterns: [cute-mascot-sameness, light-tile-on-light-bg-low-edge-contrast]
---
# App icon concepts — @dmiiiitrii

## 1. Snapshot
- **Subject:** A 9.6 s, 1280×1066 slideshow of about nine app-icon concepts, each centred on its own coloured backdrop:
  - a green frog;
  - a rainbow starburst on black;
  - an indigo ghost in a rainbow tile;
  - a white spiky critter on lime;
  - stacked cards with a smile on blue (key frame);
  - a glossy holographic blob on deep purple;
  - a purple slime with a green status dot;
  - a black ink-drop "S" on cream;
  - an orange chick blob on white.
- **Why it's remarkable:** A coherent icon-design voice. Most glyphs are characters reduced to two oval eyes, so personality comes from a minimal face system rendered in very different materials.

## 2. Composition & layout
- **Frame:** Each icon is centred at an identical size, about 580×580 px in the 1280 px frame (45% of the width). The key frame tile spans x≈350–930, y≈242–822.
- **Shape:** The tile is an iOS-style continuous-corner squircle with a radius of about 100 px (about 17–22% of the side). One concept (the 2.67 s ghost) uses a thick white inset frame of about 12 px.
- **Glyph size:** The glyph occupies about 60–70% of the tile, with roughly 15% padding inside the corner curves, close to Apple's icon grid keylines.
- **Shadow:** A soft drop shadow sits below each tile, about 30 px offset and 60 px blur at around 10% black.

## 3. Typography
No text. The only letterform is the "S" built from two black liquid teardrops (8.00 s), a type-as-glyph concept.

## 4. Colour
Key-frame palette (stacked-cards icon):

| Hex | Role | Share |
|---|---|---|
| #ffffff | backdrop | 77% |
| #43a6fb → #434cf4 | tile vertical gradient (sky to indigo) | 11% |
| #e5e3fd / #f0eff2 | front card (white → lavender) | 7% |
| #3e6ff6 / #628df5 | rear card, translucent | 3% |

Other scenes:
- #3cc81a frog green on a #e8ffe0 mint gradient;
- #2e0a8c indigo field;
- #b84dff violet field;
- #ff7a1a orange blob;
- #2b6618 forest backdrop behind a #6af23a tile.

Contrast (glyph and tile edges, 3:1 non-text target):
- Smile #434cf4 on card #e5e3fd: 4.68:1.
- Tile bottom #434cf4 on white: 5.87:1.
- **Tile top #43a6fb on white: 2.6:1**, so the light edge of the tile softens on white home screens.
- Frog tile on mint: **2.09:1**.
- Lime tile on forest: 4.77:1.
- Black tile on grey: 7.9:1.

## 5. Depth & material
- **Light top, dark bottom:** Every tile carries a top-light gradient (a lighter top that deepens downward), the macOS Big Sur convention.
- **Glyph materials:**
  - glossy jelly (the frog, slime and orange blob, with specular hotspots top-left);
  - holographic iridescent (the purple ghost: pink/blue internal glow);
  - flat sticker with a black outline (lime spiky);
  - translucent stacked paper (blue cards at about 60% opacity, rotated about −12° and +35°);
  - liquid ink (the "S").
- **Sticker edges:** the glyphs get a 4–8 px white rim, like a sticker.

## 6. Components & patterns
- **Mascot-face system:** two vertical oval eyes, sometimes with a smile. It is shared across six or more concepts.
- **Status-dot badge:** a green dot with a white ring on the slime icon, mimicking an online indicator.
- **Backdrops:** each backdrop takes a hue from the icon (tint, shade or complement) as presentation framing.

## 7. Motion
Measured profile:
- 9.6 s at 20 fps.
- `motion_fraction` 0.08 with **0 segments**, while p95 energy (54.8) is 8× the mean (6.8). That is a hard-cut slideshow with near-static holds.
- `seamless_loop_likely: false`.

With 9 evenly spaced frames showing 9 distinct icons, the hold per icon is about 1.07 s (9.6/9). There are no tweens and no camera moves; the icon stays position-locked so cuts read as a contact sheet.

## 8. Brand system
n/a — not a brand system. Identity cues: these are concept icons for unnamed apps. The transferable rule is to reduce a brand mascot to "two eyes plus one material" so it survives 29–60 pt icon sizes.

## 9. UX
- **Strengths:** Icons are highly recognisable at small sizes because of one dominant silhouette per tile, high internal contrast and centred eyes.
- **Risks:**
  - The blue tile's light top edge and the frog's light green weaken on white or light wallpapers.
  - The cute-mascot convention makes several concepts interchangeable.

## 10. Craft signals
- All tiles share one size and corner radius across nine different scenes.
- The eye ovals are consistently vertical and spaced about one eye-width apart.
- The rear translucent card in the blue icon is rotated opposite the front card, creating a fan.
- Specular highlights on the jelly glyphs consistently come from the top-left.
- The drop shadow is softer and wider than the tile, with no hard edge.
- A white sticker rim (about 6 px) separates multicolour glyphs from busy tile fills (ghost and slime).

## 11. Reproduction recipe
```css
:root{--tile-top:#43a6fb;--tile-bot:#434cf4;--card:#fff;--card-2:#e5e3fd}
.icon{width:256px;aspect-ratio:1;border-radius:22.37%;  /* iOS-like; use squircle SVG mask for exact continuity */
  background:linear-gradient(180deg,var(--tile-top),var(--tile-bot));
  box-shadow:0 14px 28px -8px rgba(30,40,120,.18),inset 0 1px 0 rgba(255,255,255,.35)}
.card{position:absolute;inset:18% 20% 20% 22%;border-radius:18%;
  background:linear-gradient(180deg,var(--card),var(--card-2));transform:rotate(-12deg);
  box-shadow:0 6px 14px rgba(40,40,160,.25),inset 0 0 0 1px rgba(255,255,255,.8)}
.card.back{transform:rotate(35deg) translate(8%,4%);background:rgba(120,170,255,.55)}
.smile{stroke:var(--tile-bot);stroke-width:12;stroke-linecap:round;fill:none}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Saturated, polished and tactile, with each tile properly lit. |
| Originality | 6 | The mascot-with-two-eyes trope is popular; the ink "S" and stacked cards are the freshest. |
| Usability | 8 | Strong silhouettes that read at small sizes; light-edge risk on light wallpapers. |
| Craft | 8 | Consistent grid, light direction and shadow across very different materials. |

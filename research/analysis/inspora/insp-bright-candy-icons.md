---
id: insp-bright-candy-icons
source: inspora
category: Branding
status: analyzed
title: "bright candy icons"
creator: "@lucaisdesigning"
styles: [y2k-chrome, maximalist-color, soft-3d, playful-rounded]
patterns: [circular-glossy-icon-set, candy-sphere-container, specular-top-highlight, pastel-glyph-on-saturated-base, offset-brick-grid-layout]
mode: light
palette: ["#ffffff", "#8de82d", "#5be3de", "#fd17b9", "#fb9913", "#f876a0", "#7a7a7a", "#ebf9d2"]
type_families: ["Cooper Black / Chunky slab-grotesk display (likely, 'BOOK' label)"]
type_class: [display]
radius_px: [9999, 60]
motion: null
scores: {aesthetics: 7, originality: 6, usability: 5, craft: 6}
craft_signals: [crescent-specular-highlight-top-left, glyph-tinted-pale-version-of-base, darker-rim-at-sphere-edge, consistent-light-direction, inner-glyph-soft-bevel]
anti_patterns: [glyph-to-base-contrast-below-3-to-1, text-inside-icon, inconsistent-row-2-baseline, grey-camera-breaks-candy-palette]
---
# bright candy icons — @lucaisdesigning

## 1. Snapshot
- **Subject:** Seven glossy, sphere-like circular app icons on a 2560×1493 white canvas: camera (grey), chat smiley (lime), sparkle (pink), weather (cyan), video (lime), "BOOK" (orange) and flower (magenta).
- **Why it's remarkable:** A deliberate revival of Y2K/Aqua-era "lickable" candy gloss, applied to modern simplified glyphs. It shows that the gloss treatment unifies a set even when the hues are wildly different.

## 2. Composition & layout
- The icons sit in two rows (4 + 3), with the second row offset by half an icon (brick layout) so the set reads as a cluster.
- Each sphere is about 538 px in diameter (about 21% of the canvas width), with gaps of about 50 px between neighbours.
- Row 1 centres are at y≈475 and row 2 at y≈1015–1035 (real px). The rows nearly touch: about 5 px vertical clearance.
- Row 2 is not on one baseline: the orange and magenta icons sit about 15–25 px lower than the lime video icon.
- **Glyph size:**
  - wide glyphs (camera, chat, cloud) fill about 70% of the sphere width;
  - the sparkle and flower fill about 65%;
  - the book card is about 340×340 px, centred.

## 3. Typography
Only one icon has type: "BOOK" in a heavy, rounded, slightly condensed display face (Cooper Black or chunky-grotesk feel) at about 95 px, in brown #7a4a12 on a cream cover. The two horizontal bars below it suggest a subtitle and author. Text inside an icon is generally a weakness: it is not localisable and is illegible at 60 px.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #ffffff | canvas | 58% |
| #8de82d / #a9f334 | lime base (chat, video) | 7% |
| #5be3de | cyan base (weather) | 4% |
| #fd17b9 | magenta base (flower) | 4% |
| #fb9913 | orange base (book) | 3% |
| #f876a0 / #fca0bf | pink base (sparkle) | 4% |
| #7a7a7a (est.) | grey base (camera) | — |
| #ebf9d2 | pale glyph fill on lime | 2% |

WCAG / non-text checks:
- Glyphs are pale tints of their base: #ebf9d2 on #8de82d is **1.39:1**, white on lime is 1.53:1 and white on cyan is 1.56:1. All fail the 3:1 non-text threshold. Shading and the drop shadow carry the separation.
- White on magenta is 3.5:1, the best of the set.
- Face lines (#3f5a10 on #ebf9d2) are 7.09:1.
- "BOOK" (#7a4a12 on #fde9c8) is 6.27:1.

Strategy: fully saturated sRGB-edge hues with no shared palette logic beyond "candy". Grey camera is the odd one out.

## 5. Depth & material
- **Spheres:**
  - a bright crescent highlight across the top-left (about 15% of the area) with a soft white falloff;
  - a darker, more saturated rim at the bottom-right;
  - a subtle inner gradient from light to dark at roughly 135°.
- **Glyphs:**
  - each is a soft 3D bevel (pillowy), with its own small highlight and a slight drop shadow onto the sphere, about 6–10 px offset downward;
  - the sparkle is faceted (four-sided pyramids) for a gem effect;
  - the sun is a separate small sphere behind the cloud.
- The light direction is consistent (top-left) across all seven.

## 6. Components & patterns
- A circle container is used instead of the iOS squircle, so these read as badges or buttons rather than store icons.
- Glyph language: Apple-adjacent metaphors (FaceTime camera, Messages bubble, Weather cloud and sun, Books) re-skinned.
- Each glyph is a pale tint of its own base hue, not white. This gives tonal harmony at the cost of contrast.

## 7. Motion
Still image, so no motion was observed. The treatment invites a press-squash (scale 0.95, 120 ms) and highlight-shift hover.

## 8. Brand system
n/a — not a brand system. Identity cues: a Y2K candy-gloss icon theme; one hue per app; tinted-glyph-on-base rule.

## 9. UX
- **Recognisability:** high, because every metaphor is a standard one.
- **Small-size legibility:** weak. With glyph-to-base contrast of about 1.4–1.6:1 on lime and cyan, the shapes will merge at 40–60 px, especially on light wallpapers.
- Circles have less area than squircles at equal width (about 78.5%), so the glyphs read smaller.
- "BOOK" as text will not scale.

## 10. Craft signals
- The specular crescent is identical in shape and position on all seven spheres (top-left, about 15% of the area).
- Each glyph is tinted from its base hue (lime → #ebf9d2), not neutral white.
- A darker saturated rim along the lower-right edge gives the sphere a refractive depth.
- The sparkle's four facets catch light on the upper-left planes, matching the global light.
- Weak point: the row 2 icons are not vertically aligned (about 20 px drift).

## 11. Reproduction recipe
```css
:root{--lime:#8de82d;--cyan:#5be3de;--magenta:#fd17b9;--orange:#fb9913;--pink:#f876a0;--grey:#7a7a7a}
.candy{--c:var(--lime);width:538px;aspect-ratio:1;border-radius:50%;display:grid;place-items:center;
  background:
    radial-gradient(60% 35% at 35% 18%,rgba(255,255,255,.85),rgba(255,255,255,0) 70%),
    radial-gradient(100% 100% at 30% 25%,color-mix(in oklab,var(--c),#fff 25%),var(--c) 55%,color-mix(in oklab,var(--c),#000 18%) 100%);
  box-shadow:inset -10px -14px 30px color-mix(in oklab,var(--c),#000 25%),0 12px 30px rgba(0,0,0,.08)}
.candy .glyph{width:70%;color:color-mix(in oklab,var(--c),#fff 80%);
  filter:drop-shadow(0 8px 6px color-mix(in oklab,var(--c),#000 30%))}
/* accessibility fix: darken glyph outline */
.candy .glyph path{stroke:color-mix(in oklab,var(--c),#000 45%);stroke-width:6}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 7 | Joyful and cohesive gloss; the grey camera and orange book tilt the palette off-balance. |
| Originality | 6 | A faithful Y2K Aqua revival; the glyphs are close to Apple's originals. |
| Usability | 5 | Low glyph contrast on lime and cyan, text in an icon, and circles reduce glyph area. |
| Craft | 6 | Consistent light and highlights; row misalignment and uneven glyph scale. |

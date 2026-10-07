---
id: insp-7-2
source: inspora
category: Illustration
status: analyzed
title: "Sketch logo"
creator: "@raphaellopesph"
styles: [soft-3d, physical-material, glassmorphism, playful-rounded]
patterns: [app-icon-3d-object, building-block-metaphor, translucent-jelly-material, debossed-label-on-sleeve, isometric-hero-icon]
mode: light
palette: ["#f2f2f2", "#d6d8da", "#e3e5e4", "#acacac", "#fed45c", "#f9a71a", "#ec8809", "#e47307"]
type_families: ["Helvetica Now Display Black / Neue Haas Black (likely)"]
type_class: [neo-grotesk]
radius_px: [160, 90]
motion: null
scores: {aesthetics: 9, originality: 7, usability: 6, craft: 9}
craft_signals: [subsurface-glow-at-edges, embossed-mark-on-each-stud, sleeve-rim-catches-orange-bounce, type-follows-isometric-face, diamond-as-sticker-not-color, consistent-top-light]
anti_patterns: [debossed-label-1-8-contrast, block-reads-as-lego-trademark]
---
# Sketch logo — @raphaellopesph

## 1. Snapshot
- **Subject:** A single 2424×2048 render of a 2×2 translucent amber building brick seated in a white rounded sleeve.
  - The sleeve is debossed "AGENT PLUGINS" on its left face and carries a grey Sketch diamond on its right face.
  - Each stud is embossed with a small looping-line mark.
- **Why it's remarkable:** It condenses "plugins for an AI agent inside Sketch" into one tactile object: brick = modular plugin, sleeve = host app. The jelly material and the Sketch-amber family make it unmistakably Sketch without using the diamond's colours.

## 2. Composition & layout
- The object is centred and occupies about 55% of the width (x≈550–1890 px real) in a three-quarter isometric view, with ~25% margin above and ~20% below.
- **Brick:** a ~1200 px-wide top face with four studs of ~300 px diameter. The studs are arranged in a diamond because of the 45° rotation.
- **Sleeve:** ~250 px tall in projection. It covers the lower ~40% of the brick and has a ~90 px radius on its vertical edges and a top lip of ~25 px.
- The two sleeve faces each carry one element: type on the left and the diamond on the right, balancing the composition.

## 3. Typography
- "AGENT PLUGINS" is set in a black-weight neo-grotesk (Helvetica Now Display Black or Neue Haas Black) in all caps, two lines, tight leading (~0.9) and ~170 px cap height.
- The type is skewed onto the isometric left face and debossed (darker inner shadow) in grey #acacac.
- The stud marks are a monoline glyph (~110 px wide) embossed in a lighter amber.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #f2f2f2 | background | 80% |
| #d6d8da / #e3e5e4 | sleeve shaded / lit faces | ~5% |
| #acacac | debossed type, diamond | <1% |
| #fed45c | brick highlights / subsurface core | — |
| #f9a71a / #f4b93e | brick mid-tones | 8% |
| #ec8809 / #e47307 | brick shadow sides, stud walls | 6% |

WCAG:
- Debossed label #acacac on the sleeve (#e3e5e4) is **1.79:1**, and 1.59:1 on its shaded part.
- The brick's mid-tone vs the background is 1.77:1. As an icon its silhouette relies on value and shadow, not hue contrast.

The palette is a warm amber ramp from yellow to orange (Sketch's brand family) set against neutral cool greys.

## 5. Depth & material
- **Brick:** translucent jelly or resin. Light scatters inside, so the edges glow yellow (#fed45c) while the volume deepens to orange. The studs have soft specular rims and visible internal gradients. There is no hard specular glare.
- **Sleeve:** satin white plastic. Its inner rim takes an orange bounce light from the brick, and a cool grey shading (#d6d8da) wraps the lower sides.
- **Grounding:** a very soft, wide ground shadow, with the light from the top-left.

## 6. Components & patterns
- **3D app or feature icon:** the hero object for a product launch ("Agent Plugins").
- **Metaphor stack:**
  - the brick stands for an extensible module;
  - four studs stand for connectable points;
  - the sleeve with the host logo stands for the platform.
- **Labelling on the object surface,** in the manner of packaging: a type face and a logo face.

## 7. Motion
None: a still image. The object implies a natural launch animation (the brick drops into the sleeve with a squash-and-settle), but none is shown.

## 8. Brand system
n/a — not a brand system, though it is brand-adjacent:
- the Sketch diamond rendered monochrome as an embossed badge;
- the amber palette echoing Sketch's yellow-orange gem;
- the heavy all-caps grotesk for the feature name.

It shows how to extend a brand into a sub-feature identity (a colour family and a material) without reusing the full logo colours.

## 9. UX
As an icon it is legible at large sizes. The metaphor (plugins = blocks) is instantly understood. Risks:
- the debossed label vanishes at small sizes and is low contrast (1.8:1);
- at a 64 px favicon size the stud marks become noise;
- the brick-stud form strongly evokes LEGO, which raises trademark proximity.

## 10. Craft signals
- The subsurface glow is brightest at thin edges (stud rims, brick top edges) and darkest in the thick core, which is physically plausible.
- The same embossed mark appears on all four studs and is correctly foreshortened.
- The sleeve's inner lip picks up orange bounce light from the brick.
- The "AGENT PLUGINS" type is projected onto the isometric face, not just rotated.
- The Sketch diamond is greyscale, so the only chroma belongs to the new feature.
- There is one light source (top-left) for the specular rims, shading and ground shadow.

## 11. Reproduction recipe
```css
:root{--bg:#f2f2f2;--sleeve:#e3e5e4;--sleeve-shade:#d6d8da;--deboss:#acacac;--amber-1:#fed45c;--amber-2:#f9a71a;--amber-3:#ec8809;--amber-4:#e47307}
.brick{border-radius:160px;background:radial-gradient(120% 90% at 50% 30%,var(--amber-1) 0,var(--amber-2) 45%,var(--amber-3) 75%,var(--amber-4) 100%);
  box-shadow:inset 0 0 40px 10px rgb(255 220 120/.6),inset 0 -30px 60px rgb(200 80 0/.35)}
.stud{border-radius:50%;background:radial-gradient(circle at 50% 35%,#ffc44a,#f39a12 70%);box-shadow:inset 0 0 0 6px rgb(255 230 150/.55),0 18px 0 #e47307}
.sleeve{border-radius:90px;background:linear-gradient(180deg,#fff 0,var(--sleeve) 40%,var(--sleeve-shade));box-shadow:inset 0 8px 12px rgb(240 140 20/.25),0 60px 80px -30px rgb(0 0 0/.12)}
.deboss{font:900 170px/.9 "Helvetica Now Display",Inter,sans-serif;text-transform:uppercase;color:var(--deboss);
  text-shadow:0 2px 0 #fff,0 -1px 0 rgb(0 0 0/.15)}
```
For true 3D, model it in Blender or Spline with an SSS shader (Principled BSDF, subsurface 0.6, radius tinted orange).

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 9 | Gorgeous jelly material and calm composition, with the amber ramp perfectly controlled. |
| Originality | 7 | The block-as-plugin metaphor is familiar. The sleeve-as-host framing and the material lift it. |
| Usability | 6 | Strong large-size icon, but the label contrast and small-size legibility are weak. |
| Craft | 9 | Physically plausible subsurface glow, bounce light and projected type. |

---
id: insp-3-6
source: inspora
category: Product
status: analyzed
title: "Liquid glass"
creator: "@theatashka"
styles: [glassmorphism, monochrome, skeuomorphic, technical-wireframe]
patterns: [floating-tab-bar, recessed-track-with-raised-pill, expanding-active-tab, detached-fab, dashed-construction-grid, crop-zoom-presentation]
mode: dark
palette: ["#ba232e", "#ab1d26", "#77060e", "#911018", "#c3353d", "#c25d64", "#ffffff"]
type_families: ["Inter Display / SF Pro Display-style neo-grotesk (likely)"]
type_class: [neo-grotesk]
radius_px: [9999, 230]
motion: null
scores: {aesthetics: 8, originality: 6, usability: 7, craft: 8}
craft_signals: [single-hue-monochrome-depth, inner-rim-highlight-bottom-edge, recessed-track-top-inner-shadow, dashed-grid-aligned-to-device-edge, white-1-5px-outline-icons, glow-pooled-at-pill-base]
anti_patterns: [footer-caption-below-aa, liquid-glass-reads-as-plastic-without-backdrop]
---
# Liquid glass — @theatashka

## 1. Snapshot
- **Subject:** A 2160×1662 still, cropped close on the bottom-left corner of a red device screen, showing a liquid-glass tab bar (Search, Profile, active "Projects") plus a separate round "+" button.
- **Why it's remarkable:** It renders Apple-style liquid glass in a single hue. Every highlight, shadow and refraction is a different value of the same red, so the material reads as tinted glass rather than a grey overlay.

## 2. Composition & layout
- The device screen fills the top ~72% of the frame. Its rounded bottom-left corner (radius ≈230 px real) sits at about x≈200, y≈1190 real px. Construction space is outside it.
- **Tab bar track:** ≈1310×285 px real (x≈320–1635, y≈790–1075). The active pill inside is ≈620×215 px, inset ~30 px from the track edge.
- **"+" FAB:** ≈225 px diameter at x≈1765–1990, vertically centred with the track and separated by a ~140 px gap.
- **Below the device:** a dashed construction grid at a ~400 px pitch, with two footer captions bottom-left ("TOOL / MADE IN FIGMA") and bottom-right ("DONE BY / @theatashka") at y≈1400–1450 real.
- The heavy crop magnifies a ~1/4-scale mobile tab bar into a poster.

## 3. Typography
- "Projects" ≈97 px real (about 17 pt in device scale ×5.5), Medium weight, neo-grotesk close to SF Pro Display / Inter Display, with tight tracking (≈−0.01 em).
- Footer captions are ≈32 px uppercase Regular with a two-tone label/value pair: white label over a pink value.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #ba232e | screen base red | ~37% |
| #ab1d26 | mid red / track | ~28% |
| #77060e / #911018 | deep shadow, outside vignette | ~16% |
| #c3353d / #a93036 | lifted surfaces, track bottom glow | ~12% |
| #c25d64 | rim highlights, pink captions | ~3% |
| #ffffff | icons, label | <1% |

**WCAG:**
- White label on the active pill (≈#95282e) is **8.01:1**.
- White icons on the base red are **6.24:1**.
- The pink caption value (≈#e8a3a8 on #a93036) is **3.24:1**, so it fails AA for small text.

## 5. Depth & material
- **Track:** recessed. A dark inner shadow along its top edge (#77060e) and a lighter glow along its bottom edge (#c3353d) read as a channel carved into the surface.
- **Active pill:** raised glass. It has a 3–4 px pinkish rim highlight running around the lower edge, a darker translucent body, and a soft bright caustic pooled at its bottom centre, as if light passes through and focuses beneath it.
- **FAB:** a glass bead with the same bottom caustic, a rim highlight on its top-left, and a soft drop shadow down-right.
- **Screen edge:** a 2–3 px lighter bevel on the screen, and a large dark shadow cast onto the outer area (bottom-left corner darkening).

## 6. Components & patterns
- Floating tab bar. Inactive tabs are icon-only (≈90 px real outline icons, 1.5 px stroke at device scale). The active tab expands into an icon-plus-label pill.
- A separate primary-action FAB sits outside the tab track, the iOS 26 "detached accessory" arrangement.
- Presentation chrome: a dashed grid and spec captions in the style of a blueprint.

## 7. Motion
Still image, so no motion was observed. The expanding active pill implies a width/position morph between tabs (typically a 0.35–0.5 s spring), but none is shown.

## 8. Brand system
n/a — not a brand system. Identity cues: a single saturated red for everything, and blueprint captions as a signature presentation frame.

## 9. UX
- The active state is unmistakable: label, size and material all change.
- Inactive icons are clear and well-spaced (~235 px real between centres).
- **Risks:**
  - Icon-only inactive tabs depend on recognisable glyphs.
  - On real content the tinted glass would need a backdrop blur to remain legible. Here it sits on a flat colour, so the "liquid" quality is mostly highlights.

## 10. Craft signals
- Highlights sit at the bottom of the glass, not the top. That matches how light concentrates through a lens, the detail most liquid-glass knock-offs get wrong.
- The track's inner shadow is on the top and its glow is on the bottom, the inverse of the pill. This makes the concave/convex pairing read correctly.
- The dashed grid lines on the left align to the device's outer edge (x≈185 displayed).
- The icon stroke weight visually matches the "Projects" stem weight.

## 11. Reproduction recipe
```css
:root{--red:#ba232e;--red-mid:#ab1d26;--red-deep:#77060e;--red-lift:#c3353d;--rim:#e58a91;--ink:#fff;--r-pill:9999px;}
.screen{background:linear-gradient(160deg,#c3353d,#ab1d26 60%,#9c1a22);border-radius:230px 230px 230px 230px}
.track{display:flex;align-items:center;gap:48px;padding:30px;border-radius:var(--r-pill);
  background:linear-gradient(180deg,#a51c25,#c3353d);
  box-shadow:inset 0 10px 18px rgba(80,0,8,.55),inset 0 -6px 14px rgba(255,140,150,.25)}
.tab-active{display:flex;gap:40px;align-items:center;padding:0 60px;height:215px;border-radius:var(--r-pill);
  background:radial-gradient(60% 40% at 50% 100%,rgba(255,170,180,.45),transparent 70%),rgba(140,30,40,.55);
  box-shadow:inset 0 -3px 0 rgba(255,170,180,.7),inset 0 2px 0 rgba(255,255,255,.12),0 8px 24px rgba(60,0,6,.35);
  backdrop-filter:blur(18px) saturate(1.4);color:var(--ink);font:500 97px/1 "SF Pro Display","Inter",sans-serif}
.fab{width:225px;aspect-ratio:1;border-radius:50%;background:inherit;box-shadow:inherit}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Bold single-hue poster with a convincing material. |
| Originality | 6 | A Liquid Glass exploration, a heavily trending 2025–26 subject; the monochrome red is the twist. |
| Usability | 7 | Clear active state and solid icon contrast; untested over real content. |
| Craft | 8 | Correct concave/convex lighting, careful rims, and grid alignment. |

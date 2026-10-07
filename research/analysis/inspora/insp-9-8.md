---
id: insp-9-8
source: inspora
category: Web
status: analyzed
title: "html-in-canvas"
creator: "@rpavlini (Marijana Pavlinić)"
styles: [monochrome, glassmorphism, micro-interaction, x-sticker-collage]
patterns: [draggable-refractive-lens, sticker-pile-hero, coming-soon-page, floating-pill-nav, live-tweak-panel, theme-toggle-light-dark, chromatic-aberration-edge]
mode: mixed
palette: ["#f8f8f8", "#1e1e1f", "#dadcdb", "#bebfbd", "#56595b", "#323130", "#050505"]
type_families: ["Inter Display Light / Geist (likely)", "mixed sticker display faces: pixel, script, slab, grotesk"]
type_class: [neo-grotesk, display, pixel]
radius_px: [9999, 12, 8]
motion: {durations_s: [0.63, 0.73, 0.40, 1.30, 1.77, 0.80], easing: [ease-out, ease-in-out], loop: false}
scores: {aesthetics: 9, originality: 9, usability: 6, craft: 9}
craft_signals: [ior-1.52-glass-lens, rgb-split-at-lens-rim, lens-refracts-live-dom-text, monochrome-stickers-let-aberration-show, tweak-panel-exposes-shader-params, pill-nav-active-chip]
anti_patterns: [content-is-placeholder, interaction-not-discoverable-on-touch]
---
# html-in-canvas — @rpavlini

## 1. Snapshot
- **Subject:** A 2880×2160, 14.1 s, 60 fps recording of a "Shop — Coming soon" page for designer Marijana Pavlinić. A pile of black-and-white stickers sits under a draggable glass sphere that refracts both the stickers and the live HTML heading.
- **Why it's remarkable:** The lens refracts real DOM text (the "html-in-canvas" of the title). "Meanwhile" curls around the sphere's rim with RGB fringing. The final third reveals a "Shop Lens" tweak panel with physically based parameters: Radius 180, Magnification 1.75, IOR 1.520, Aberration 0.0100, Thickness 0.90, Bevel Start 0.900, Oblateness 0.47, Refraction Displacement 0.60.

## 2. Composition & layout
- **Page:** a 4:3 viewport inside a rounded presentation frame.
- **Header:** a hand-wave icon plus name top-left (~16 px), and theme/display icons plus avatar top-right.
- **Centre stack:**
  - "SHOP" eyebrow (~14 px caps)
  - "Coming soon" at ~64 px light
  - "Meanwhile, click, drag and explore ↓" at ~16 px
- **Sticker pile:** directly below, spanning ~55% of the width (x≈280–1160 in a 1600 frame). Postage-stamp, label and badge stickers overlap at ±15° rotations.
- **Nav:** a floating pill nav centred at the bottom (Work / About / Shop / Contact), with the active item in a filled chip.
- **Lens:** the glass sphere is ~330 px in diameter (Radius 180 in the panel, at about 1.0 scale), and is dragged over the pile and up onto the heading.

## 3. Typography
- **Heading:** "Coming soon" in a neo-grotesk at Light (300), ~64 px, tracking about −0.02 em, closest to Inter Display Light or Geist Light.
- **Body and nav:** ~16 px regular.
- **Sticker faces:** a deliberately eclectic display catalogue:
  - pixel bitmap ("1% BATTERY SURVIVORS CLUB")
  - a swash script ("Lorem ipsum")
  - a wide grotesk ("CASEMATES SQUARE", "1779")
  - a heavy condensed sans ("GIBRALTAR")
  - hand-lettering ("v60 and chill")

  The plain UI type lets the stickers be loud.
- **Panel:** labels are ~13 px sans, and values are in a mono (tabular) face aligned right.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #f8f8f8 | light canvas | 61% |
| #dadcdb / #ebebeb | sticker paper, lens body | 15% |
| #1e1e1f / #323130 | sticker ink, heading | 12% |
| #56595b / #807e7c / #9fa3a3 | mid-greys (shading, Chemex illustration) | 9% |
| #050505 | dark-theme canvas | — |
| RGB fringe (cyan, magenta, yellow) | only at the lens rim | <0.5% |

WCAG checks:
- The heading (~#3a3a3a) on #f8f8f8 is **10.71:1**.
- Sticker ink #1e1e1f on #f8f8f8 is **15.68:1**.
- Dark theme: #e8e8e8 on #050505 is **16.63:1**.
- Panel: labels #a0a0a0 on #2a2a2a are **5.49:1**, and values (#fff) are 14.35:1.

The whole piece is achromatic, so the only colour is the physically generated chromatic aberration, which makes the glass feel real.

## 5. Depth & material
- **Sphere:**
  - shows a strong inverted, magnified image through the centre;
  - has a bright white Fresnel rim (light theme) or a dark rim (dark theme);
  - gets RGB dispersion at grazing angles (aberration 0.01);
  - casts a soft drop shadow (~40 px blur) onto the page.
- **Oblateness:** at 0.47 the lens flattens into a lozenge or pebble at times (3.92 s), not a perfect ball.
- **Stickers:** a white die-cut border of ~6 px plus subtle shadows, so they read as physical paper.
- **Panel:** a dark glass card with radius ~12 px and 1 px inner strokes. Slider rows show their value as a lighter fill bar.

## 6. Components & patterns
- **Draggable lens:** cursor-follow with inertia.
- **Sticker collage:** acts as a hero and as a placeholder for upcoming merch.
- **Pill nav:** ~300×34 px with the active chip filled in #e6e6e6 (light) or #2e2e2e (dark).
- **Tweak panel ("Shop Lens"):**
  - a version dropdown;
  - an Off/On segmented toggle;
  - 8 slider-rows whose fill width encodes the value;
  - a copy-config icon.

  It is a DialKit/Leva-style designer tool exposed in the UI.
- **Light/dark toggle:** in the header (dark from ~9.5 s).

## 7. Motion
- **Measured:** 14.1 s at 60 fps, motion_fraction **0.34**, 6 segments with a median of **0.77 s**. **5 of 6 are ease-out** (peak 0.10–0.24), which fits a lens that is flicked and then glides to rest with inertia.
- **Segments:**

  | Time (s) | Duration (s) | Probable action |
  |---|---|---|
  | 0.63–1.27 | 0.63 | zoom-in from the framed overview |
  | 1.43–2.17 | 0.73 | symmetric drag |
  | 2.67–3.07 | 0.40 | drag |
  | 3.47–4.77 | 1.30 | drag to heading |
  | 5.20–6.97 | 1.77 | long drag |
  | 7.87–8.67 | 0.80 | zoom-out |

- **Other changes:** The theme switch (~9.5 s) and slider tweaks (10–13 s, oblateness scrubbed) fall below the threshold. Not a loop (first/last diff 137).

## 8. Brand system
n/a — not a brand system. Personal identity cues:
- a peace-hand icon with the name;
- a sticker-bombing aesthetic as a personality signal (coffee, travel, battery jokes);
- a strict monochrome palette that lets every piece of craft read.

## 9. UX
- **Strengths:**
  - "Click, drag and explore" sets expectations.
  - It is a delightful dead-end page that turns "not ready" into a toy.
  - The nav stays reachable at the bottom.
- **Weaknesses:**
  - No email capture or date for the shop.
  - The drag interaction on touch devices may conflict with scroll.
  - The panel is a dev artefact if left in production.
  - The lens over text momentarily makes the heading unreadable (by design).

## 10. Craft signals
- An IOR of 1.520 (crown glass) and aberration of 0.01 are physically plausible values, not arbitrary.
- RGB fringing appears only at the rim, never in the centre.
- The lens refracts live text, and the distortion matches the sticker refraction, so it is the same shader on DOM and canvas.
- An achromatic palette means the only colour on screen is optical.
- Slider rows show their value as a fill bar plus a right-aligned mono number.
- Sticker die-cut borders stay a consistent ~6 px white across all shapes.

## 11. Reproduction recipe
```css
:root{--bg:#f8f8f8;--ink:#1e1e1f;--paper:#ebebeb;--panel:#1c1c1c;--row:#2a2a2a;--row-fill:#3a3a3a;
  --font:"Inter Display","Geist",system-ui,sans-serif;--mono:"Geist Mono",ui-monospace,monospace}
[data-theme=dark]{--bg:#050505;--ink:#e8e8e8}
h1{font:300 64px/1 var(--font);letter-spacing:-.02em;color:var(--ink)}
.sticker{filter:drop-shadow(0 0 0 #fff) drop-shadow(0 6px 10px rgba(0,0,0,.12));outline:6px solid #fff;rotate:var(--r)}
.nav{position:fixed;bottom:24px;left:50%;translate:-50%;display:flex;gap:4px;padding:4px;border-radius:9999px;background:#fff;box-shadow:0 1px 0 #0000000f}
.nav a[aria-current]{background:#e6e6e6;border-radius:9999px}
.row{position:relative;height:32px;border-radius:8px;background:var(--row);display:flex;justify-content:space-between;padding:0 10px;font:13px var(--font)}
.row::before{content:"";position:absolute;inset:0 auto 0 0;width:var(--v);background:var(--row-fill);border-radius:inherit}
.row output{font-family:var(--mono);font-variant-numeric:tabular-nums}
```
```glsl
// lens fragment (sketch): refract DOM texture captured to canvas
vec2 n = normalize(uv - center) * pow(length(uv-center)/radius, 2.0);
float ior = 1.52, ab = 0.01;
vec2 offR = n * (1.0/ior - 1.0) * (1.0 + ab), offB = n * (1.0/ior - 1.0) * (1.0 - ab);
color = vec3(texture(page, uv/mag + offR).r, texture(page, uv/mag + n*(1.0/ior-1.0)).g, texture(page, uv/mag + offB).b);
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 9 | A strict monochrome collage plus one optical hero object; both themes look finished. |
| Originality | 9 | A refractive glass lens over live HTML, with exposed physical parameters, is a new idea for a coming-soon page. |
| Usability | 6 | Fun but low-utility: no capture, and touch-drag concerns. |
| Craft | 9 | Physically plausible shader values, clean rim dispersion and a meticulous tweak panel. |

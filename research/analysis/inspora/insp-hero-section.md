---
id: insp-hero-section
source: inspora
category: Web
status: analyzed
title: "Hero section"
creator: "@loseva_pro"
styles: [retro-pixel, monochrome, dither-halftone, terminal-mono]
patterns: [scanline-rendered-3d-mascot, pixel-display-headline, mono-body-copy, split-hero-text-left-art-right, solid-plus-text-cta-pair, looping-mascot-video]
mode: light
palette: ["#eff1ee", "#000000", "#373737", "#999998", "#b5b5b5", "#d2d2d2", "#e2e2e2"]
type_families: ["pixel display, Silkscreen / Pixelify Sans-style (likely)", "IBM Plex Mono (likely)"]
type_class: [pixel, mono]
radius_px: [0, 2]
motion: {durations_s: [1.0, 1.1, 1.47, 4.13], easing: [ease-out, ease-in, ease-in-out], loop: true}
scores: {aesthetics: 8, originality: 8, usability: 7, craft: 7}
craft_signals: [horizontal-line-shader-matches-pixel-type, mascot-bleeds-off-right-edge, pure-black-cta-on-offwhite, single-mono-family-for-ui, eyes-kept-solid-black-for-expression]
anti_patterns: [art-overlaps-headline-edge, nav-type-small-11px]
---
# Hero section — @loseva_pro

## 1. Snapshot
- **Subject:** A 1228×868, 8.6 s seamless loop of a hero for "MEOW AI AGENT". A 3D kitten mascot walks and turns, rendered entirely as **horizontal black scanlines** on a near-white field, beside a pixel-font headline and mono copy.
- **Why it's remarkable:** The illustration and type share one rendering logic. Both the cat (scanline-dithered) and the headline (bitmap pixels) are built from discrete horizontal strokes, so a cute 3D render reads as a 1-bit terminal graphic.

## 2. Composition & layout
- **Grid:** A two-zone split with a 30 px left margin.
- **Nav:** logomark top-left (28 px); five links top-right at y≈50, ~14 px mono, ~30 px apart.
- **Text column (x 30–530):**
  - "MEOW / AI AGENT" set over two lines from y≈200 to 372 (cap height ~78 px, line gap ~16 px)
  - a two-line subhead at y≈589–610
  - a CTA row at y≈697
- **Mascot zone (x≈520–1228):** the scanline field bleeds off the top-right and right edges. At times (4.31 s, 6.22 s) the cat's ears and outline overlap the "T" of "AGENT", which is intentional layering but slightly crowded.
- **Space:** A large vertical gap of ~215 px between headline and subhead gives the poster feel.

## 3. Typography
- **Headline:** a blocky bitmap face (Silkscreen- or Pixelify Sans-style) at ~96 px, all caps. Letters are built on a ~11 px pixel module, and tracking is the font's own.
- **Body, nav, buttons:** a monospace, IBM Plex Mono-like.
  - Subhead: ~17 px, about 1.25 leading.
  - Nav: ~14 px.
  - Buttons: ~14 px.
- **Contrast:** Pixel type for brand voice against a clean mono for reading, a good pairing because the mono keeps legibility while matching the "machine" tone.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #eff1ee | canvas (cool off-white) | 64% |
| #000000 | headline, CTA fill, cat eyes | ~6% |
| #373737 | scanlines (dense), body text | 4% |
| #999998 / #b5b5b5 / #c2c2c2 / #d2d2d2 / #e2e2e2 | scanline greys and ambient-occlusion haze | 31% |

WCAG checks:
- Black on #eff1ee is **18.49:1**.
- Body #373737 on #eff1ee is **10.48:1**.
- The CTA is white on #000 at 21:1.
- Light scanline greys (#999998) are 2.51:1, which is decorative only.

Strictly achromatic: the "AI" is conveyed by rendering style, not by colour.

## 5. Depth & material
- **Cat:** A 3D model with soft lighting is converted to 1–2 px horizontal lines with ~6 px spacing. Line density encodes shade, and lines break into dashes in highlights.
- **Fur:** Soft white bloom halos around the fur edges remain from the render, a mix of photographic softness and hard 1-bit lines.
- **Ground:** a horizontal scanline "floor" with a contact-shadow cluster under the paws.
- **UI:** flat; the CTA is a sharp rectangle (radius 0–2 px).

## 6. Components & patterns
- **Primary CTA:** "Get Started", solid black, ~138×39 px, white mono label.
- **Secondary CTA:** "See How It Works ›", a text link with a chevron, no border.
- **Logomark:** a 4-lobe pixel/quatrefoil glyph in black.
- **Nav:** text-only, with no active state shown.

## 7. Motion
- **Measured:** 8.62 s at 30 fps, motion_fraction **0.55**, 4 segments with a median of 1.29 s; **seamless_loop_likely = true** (first/last diff 0.48).
- **Segments:**

  | Time (s) | Duration (s) | Curve |
  |---|---|---|
  | 0.23–1.23 | 1.0 | ease-out, peak 0.02 (a sharp start as the loop resumes) |
  | 1.33–2.43 | 1.1 | ease-in |
  | 2.53–4.00 | 1.47 | ease-in-out |
  | 4.17–8.30 | 4.13 | ease-in-out |

- **Interpretation:** The cat walks toward the camera (2.39 s), turns its head (3.35 s), steps sideways, approaches closely (6.22–7.18 s, face filling ~45% of width) and retreats. These are character-animation beats, not UI transitions.
- **Shader:** The scanline treatment is applied per frame, so the lines stay horizontally locked while the form moves. That is the source of the CRT feel.
- **Text:** The UI text is static.

## 8. Brand system
n/a — not a brand system. Identity cues:
- a cat mascot as the AI persona;
- a 1-bit/scanline rendering as the visual language;
- pixel display type with mono text;
- strictly black on off-white.

## 9. UX
- **Strengths:** The value proposition is plain ("Your personal AI assistant…"), the CTA hierarchy is clear (solid vs text), and the high-contrast text is excellent.
- **Weaknesses:**
  - Nav links at ~14 px mono are fine, but at mobile sizes the pixel headline will need a step-down.
  - The mascot overlapping the headline edge can hurt the "T".
  - The animation is heavy (video), so it needs a poster frame and a reduced-motion still.

## 10. Craft signals
- The scanline pitch (~6 px) relates to the pixel-font module (~11 px), so the two read as one system.
- The cat's eyes are kept as solid black pixel blobs, preserving expression through the dithering.
- The canvas is #eff1ee (very slightly green-grey), not pure white, which softens the 1-bit harshness.
- The left edges of headline, subhead and CTA share x=30.
- The art bleeds off the top and right edges, so the scene feels bigger than the viewport.

## 11. Reproduction recipe
```css
:root{--bg:#eff1ee;--ink:#000;--text:#373737;--font-pixel:"Silkscreen","Pixelify Sans",monospace;--font-mono:"IBM Plex Mono",ui-monospace,monospace}
.hero{background:var(--bg);display:grid;grid-template-columns:minmax(0,520px) 1fr;min-height:100vh;padding:0 30px;overflow:hidden}
.hero h1{font:400 clamp(48px,7.8vw,96px)/1.0 var(--font-pixel);text-transform:uppercase;color:var(--ink);-webkit-font-smoothing:none}
.hero p{font:400 17px/1.25 var(--font-mono);color:var(--text);max-width:36ch}
.btn{font:400 14px var(--font-mono);background:var(--ink);color:#fff;padding:11px 24px;border-radius:2px}
.link{font:400 14px var(--font-mono);color:var(--ink)}.link::after{content:" ›"}
/* scanline treatment over a grayscale video */
.mascot{position:relative}
.mascot video{filter:grayscale(1) contrast(1.4) brightness(1.1)}
.mascot::after{content:"";position:absolute;inset:0;mix-blend-mode:screen;
  background:repeating-linear-gradient(0deg,transparent 0 2px,var(--bg) 2px 6px)}
@media (prefers-reduced-motion:reduce){.mascot video{display:none}.mascot{background:url(cat-poster.png) center/contain no-repeat}}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Cohesive 1-bit world; the scanline cat is charming and striking. |
| Originality | 8 | Rendering a 3D mascot as CRT scanlines that match pixel type is a fresh AI-brand idea. |
| Usability | 7 | Clear CTAs and high contrast; art overlap and video weight are concerns. |
| Craft | 7 | Shared module logic and alignment; slight headline/art collision. |

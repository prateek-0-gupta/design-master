---
id: insp-1-33
source: inspora
category: Web
status: analyzed
title: "Hero section"
creator: "@neropursue"
styles: [photo-led, editorial-serif, cinematic-3d, glassmorphism]
patterns: [split-hero-text-left-image-right, fluted-glass-overlay, cursor-reveal-layers, condensed-caps-headline, service-tile-trio, underline-active-nav]
mode: light
palette: ["#9da1aa", "#838790", "#a9acb3", "#686e77", "#32333b", "#271c21", "#513338", "#222222"]
type_families: ["condensed didone such as Bodoni Poster Compressed / Ogg Condensed (likely)", "Inter (likely)"]
type_class: [condensed, editorial-serif, neo-grotesk]
radius_px: [4, 0]
motion: {durations_s: [10.37], easing: [linear], loop: true}
scores: {aesthetics: 8, originality: 7, usability: 6, craft: 7}
craft_signals: [fluted-glass-slats-refract-image, cursor-lens-reveals-alt-layer, tile-captions-reuse-headline-face, em-dash-indent-second-line, grey-canvas-matches-statue-backdrop, square-cta-zero-radius]
anti_patterns: [ai-generated-imagery, tile-caption-legibility-on-busy-image, hover-only-reveal]
---
# Hero section — @neropursue

## 1. Snapshot
- **Subject:** A 10.4 s, 1920×1172 loop of an AI creative-studio hero. On the left is a condensed-caps headline, CTAs and three service tiles. On the right is a classical bust with a cosmic blindfold seen through a panel of vertical fluted-glass slats.
- **Why it's remarkable:** The glass slats are interactive lenses. As the cursor (a ring) moves over the face, alternate image layers (code-rain visor, ringed gold planet, red Mars) are revealed or swapped strip by strip, so the hero tells a "classical × digital" story through hover.

## 2. Composition & layout
- **Left column (x≈100→840):**
  - nav at y≈89, with an active underline under "Work" spanning about 86 px;
  - a two-line headline at y≈250–425;
  - a 2-line deck at y≈474–513;
  - CTA row at y≈580–625;
  - a trio of service tiles at y≈853–1113 (230/260/200 px wide, about 20 px gaps).
- **Right (x≈1135→1920):** a bust about 780 px wide bleeding off the bottom and right. The glass panel is about 715×665 px (x 1137→1850, y 123→790), divided into about 6 slats of about 120–145 px width with 1–2 px light edges.
- The second headline line is indented by a 46 px em-dash, which creates a stepped rag.

## 3. Typography
- **Headline:** a very condensed high-contrast serif in uppercase (Bodoni Poster Compressed or Ogg Condensed feel). Cap height is about 60 px (font-size about 88 px), leading about 1.15, tracking about −0.01 em, in black #1a1a1a.
- **Deck:** a neo-grotesk (Inter-like) at about 28 px/1.4 in near-black.
- **Nav, buttons and tile captions:**
  - Nav is about 22 px regular.
  - Buttons are about 22 px.
  - Tile captions reuse the condensed serif in white, about 34 px, two lines, right-, centre- or left-aligned per tile.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #9da1aa / #838790 / #a9acb3 | cool grey studio backdrop (page = photo background) | 65% |
| #686e77 / #4f5158 | shadows, tile backgrounds | 13% |
| #271c21 / #32333b | headline ink, cosmic darks | 13% |
| #513338 / #645b5d | maroon nebula tones | 7% |
| #222222 | primary CTA fill | <1% |
| orange-red / cobalt | nebula and Mars accents (image) | — |

WCAG checks:
- Headline #1a1a1a on #9da1aa is 6.72:1.
- Deck text on #a9acb3 is 6.23:1.
- White on the #222 CTA is 15.9:1.
- White tile captions on mid-grey #686e77 are 5.14:1, but where the image is lighter (#838790) only 3.6:1 (large text only). Legibility varies across the busy imagery.

## 5. Depth & material
- **Backdrop:** the page background is the photo's own seamless grey studio sweep, so there is no visible boundary between UI and image.
- **Glass slats:** each slat has a 1–2 px white edge highlight and refracts the face with a lateral offset of about 8–20 px (visible on the nose and lips). This is classic fluted/reeded glass.
- **Buttons and tiles:** flat. The tiles are square-cornered (radius about 4 px) and contain their own grey-backdrop renders that match the page.

## 6. Components & patterns
- Text nav with an underline active state.
- **CTAs:** a primary square black button "Book A Call" (about 170×46 px, radius 0) and a secondary text link "See Work →".
- **Service tiles:** image cards with overlaid serif captions ("CREATIVE AI SOLUTIONS", "DIGITAL BRAND SYSTEMS", "SCALABLE INNOVATION").
- **Cursor lens:** a ring cursor of about 60 px with a dot, signalling an interactive image.

## 7. Motion
- **Measured:** 10.37 s at 30 fps. motion_fraction is only 0.03 and mean energy 0.2, with one 0.17 s ease-in-out blip at 8.23 s. The clip is a likely seamless loop (first/last diff 1.6). The page layout never moves, and the change is confined to the bust.
- **Observed across 9 frames:** the content behind each slat changes as the cursor sweeps. At t=1.73 s a gold ringed planet and code visor show, at t=4.03 s a Mars sphere and right-side code, and at t=9.79 s the hair turns lighter and silver. Changes are per-strip, which suggests each slat masks a different image layer, cross-faded smoothly (low per-frame energy ⇒ slow linear blends, estimated at about 0.6–1 s).

## 8. Brand system
n/a — not a brand system. Identity cues:
- the classical-statue-meets-cosmos art direction;
- the condensed didone as the voice of "sovereign" authority;
- a cool grey studio world.

## 9. UX
- Clear primary and secondary actions above the fold, and the nav is simple.
- **Risks:**
  - The interactive reveal depends on hover, so touch users see a static image.
  - Tile captions sit on busy renders.
  - The heavy AI imagery dominates and may slow the page.
  - No hover affordance is visible on the tiles.

## 10. Craft signals
- The page background colour is sampled from the photo backdrop (#9da1aa), so the bust has no visible frame edge.
- The em-dash indent on line 2 aligns the "U" with the line-1 "C" optical column plus about 70 px, a deliberate editorial rag.
- Tile captions reuse the headline typeface, tying the tiles to the hero voice.
- The glass slats carry thin specular edges and per-strip displacement, which reads as real reeded glass.
- The CTA is square-cornered, matching the sharp classical tone (no pills anywhere).

## 11. Reproduction recipe
```css
:root{--studio:#9da1aa;--ink:#1a1a1a;--btn:#222;--serif-c:"Bodoni Poster Compressed","Ogg Condensed","Oswald",serif;--sans:Inter,system-ui}
body{background:radial-gradient(120% 90% at 70% 40%,#a9acb3,#838790)}
h1{font:400 88px/1.15 var(--serif-c);text-transform:uppercase;letter-spacing:-.01em;color:var(--ink)}
h1 .dash::before{content:"— ";}
.btn{background:var(--btn);color:#fff;border-radius:0;padding:10px 22px;font:400 22px var(--sans)}
.flutes{display:grid;grid-template-columns:repeat(6,1fr);width:715px;height:665px}
.flute{backdrop-filter:blur(1px);border-inline:1px solid rgba(255,255,255,.5);
  background:linear-gradient(90deg,rgba(255,255,255,.12),transparent 30%,transparent 70%,rgba(255,255,255,.18))}
.flute img{transform:translateX(calc(var(--i)*-6px)) scaleX(1.04);transition:opacity .8s linear}
.tile figcaption{position:absolute;bottom:16px;font:400 34px/1 var(--serif-c);color:#fff;text-transform:uppercase}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Strong art direction, and the condensed serif plus grey studio feel cohesive. |
| Originality | 7 | Fluted glass as a per-strip reveal lens is a fresh twist on a trendy effect. |
| Usability | 6 | Clear CTAs, but the hover-only storytelling and the busy caption backgrounds hurt it. |
| Craft | 7 | The seamless backdrop and tidy grid work. The AI-render imagery and the variable caption contrast are weaker. |

---
id: bg-mixcloud
source: brandguidelines
category: guideline
status: analyzed
title: "Mixcloud Brand Home"
creator: "Mixcloud (in-house, Webflow site)"
styles: [duotone, grain-noise, dither-halftone, maximalist-color, hand-drawn, photo-led, playful-rounded]
patterns: [duotone-photo-treatment, hand-drawn-scribble-overlays, smiley-sticker-mascot, wavy-display-wordmark-letters, pill-nav-over-hero, three-by-three-guideline-tiles, dark-manifesto-panel, yellow-icon-band, rounded-section-seams]
mode: mixed
palette: ["#5000ff", "#f45827", "#f69ae4", "#f3f810", "#171c2b", "#22293c", "#0cc281", "#ffffff"]
type_families: ["Sine Sans Medium (display, 170 px uppercase)", "DM Sans (body, 16-52 px)", "Karla (loaded, fallback)"]
type_class: [display, geometric-sans]
radius_px: [12, 20, 30, 45, 100]
motion: {durations_s: [0.2], easing: [ease], loop: false}
scores: {aesthetics: 9, originality: 8, usability: 6, craft: 8}
craft_signals: [tri-tone-photo-recolour, brush-circle-highlight-on-key-word, wavy-glyph-set-from-logo, 12px-card-radius, soft-0.05-alpha-card-shadow, white-sheet-with-rounded-top-over-dark]
anti_patterns: [subpages-not-linked-in-capture, low-contrast-grey-tile-labels, body-grey-61667a-small, strategy-section-locked]
---
# Mixcloud Brand Home — Mixcloud (in-house)

## 1. Snapshot
- **Subject:** The brand home / intro of Mixcloud's brand site (mixcloud.com/brand), a Webflow site. **Wayback Machine snapshot dated 2024-01-02 05:37:45** (`captured_from` www.mixcloud.com/brand). Live page not used (it is hidden/login-walled).
- **Coverage (explicit):** home page only: 7 desktop tiles (1440 px wide, scrollHeight 12,510 px so ~7 of the full ~7 tiles), all 7 viewed, and mobile sheet 1 of 2 viewed. The 9 guideline subpages (Colour, Logo, Illustration, Typography, Sub brands, Textures, Photography, Motion, Copywriting) plus Manifesto, Brand values, Strategy (padlocked) and Media kit were NOT captured; their contents are unknown. Everything about logo clearspace, exact palette roles and type use below comes from what is visible on the home.
- **Why it's remarkable:** A music-community brand expressed as hot-tri-tone (blue/orange/pink) recoloured photography, hand-drawn scribbles and smiley stickers over a wobbly custom display face - it looks like a gig-poster rather than a corporate guideline.

## 2. Composition & layout
- Hero (y 0-900): full-bleed duotone photograph of a DJ; floating pill nav (white, radius ~100 px, 14 px labels: Intro, Brand guidelines with dropdown, Manifesto, Brand values, Strategy with lock, Media kit); M-XCLOUD logo at x≈48; giant "OUR BRAND" uppercase in white, ~120 px cap height; sub-copy centred ~19 px; arrow glyph below. A white sheet with ~45 px rounded top corners slides over the hero at y≈900.
- Alternating editorial rows (text left/image right and mirror): headings at 52 px/52 px ("A brand evolution", "People powered music"), body at 17 px/28 px in grey #61667a, image cards ~470×680 px with rough hand-cut edges and black outline.
- "Explore guidelines": 3×3 grid of white tiles, each ~457×124 px, 12 px gap, centred labels at 16 px.
- Dark section (#161c2a): hero card "A brand built by connections" with a hand-drawn purple ring around the key word; then the same 9 tiles repeated in dark (#222a3d) as "Brand foundations".
- A light-grey (#f4f4f4) sheet shows the wavy glyph set (AN, MA, NN, NU, VU, ∞) at ~110 px, then two example images (phone mock, "On Rootation 2 Bossa Nova" sticker poster, "Share Your Mixcloud Live Moments" social tile) with 12 px radius and a soft shadow.
- Yellow #f3f810 band ~675 px tall with four monoline icons (person-play, send, heart, replay-30), then a halftone-dot photo banner "For every Scene, Genre and Sub-culture".
- Mobile: single column; tile grid collapses to 2 columns; hero "OUR BRAND" at ~54 px.

## 3. Typography
- **Sine Sans Medium**, 170 px / 160 px line-height, uppercase, weight 500 (66 census runs; this is the large decorative hero glyph set, each letter in its own element). **DM Sans** 400 for everything else: 17/28 (18 runs), 16/28, 20/32 (-0.3 px), 24/32 (-0.3 px), 42/52, 52/52.
- Scale observed: 16 · 17 · 20 · 24 · 42 · 52 · 170. Tracking normal except -0.3 px on 20-24 px. Display glyphs have wavy, stretched-stroke forms (also used as the "wave" illustration glyphs A N M U V).
- Headings sentence case; hero uppercase.

## 4. Colour
| hex | role | approx share |
|---|---|---|
| #ffffff | content sheet | 37-83% of light tiles |
| #5000ff | brand blue-violet (hero duotone shadows, highlight ring, links) | 14% of tile 1 |
| #f45827 / #c95816 | orange duotone highlight | ~5% of tile 1 |
| #f69ae4 / #c591b5 | pink duotone midtone, "connections" word | ~5% |
| #f3f810 | yellow icon band | large block |
| #171c2b / #22293c | dark navy sections | 62% of tile 3 |
| #0cc281 | green (secondary) | var only |
| #61667a / #919191 | body grey / mini-titles | small |

- Other CSS variables: --high-blue-tint #e2e3ff, --yellow-tint #f9fbb2, --violet-tint #fde1f7, --green-tint #e3faf0, --orange-medium #f45827, --pink-medium #d20442, --lines #c4c4c4, --bg #f2f2f2.
- Contrast: white on #5000ff **7.54:1**; navy #171c2b on yellow **14.74:1**; #61667a body on white **5.69:1**; mini-title grey #919191 on white **3.15:1 (fails AA body)**; #d2d3d7 on #22293c **9.68:1**.

## 5. Depth & material
- Photos are recoloured, posterised and dithered; stickers have black outlines; scribbles in white or pink are imposed on top. Cards use `0 0 12px 1px rgba(0,0,0,.05)` (9 uses) for a soft lift; a heavier `0 15px 35px 2px rgba(0,0,0,.35)` appears once on a hero image. Section seams use rounded 30/45 px corners (sheet over sheet).

## 6. Components & patterns
- Floating pill nav; text tile grid; paired image cards with hand-cut borders; smiley "sticker" mascot (pink disc with face, a stacked row of four); flower-person and runner doodles; brush ring around a keyword; icon set with 3 px strokes and rounded ends; halftone/dither photo banner; phone mock-up.

## 7. Motion
- Only `filter .2s ease` is in the census (18 uses, tile hover brightness). No motion guidance is visible on the home page; a Motion subpage exists but was not captured.

## 8. Brand system (home only)
- **Positioning copy:** "People powered music"; mission to help connect people through music; celebrates imperfection and individuality over algorithms.
- **Visual language:** tri-tone recolour (violet / orange / pink) for photography; black-and-white high-grain halftone for a second photo mode; teal accent on some posters; yellow as a punctuation band; dark navy as the calm backdrop.
- **Logo:** M-XCLOUD wordmark with a dash replacing the "I" and a stylised X; shown in white on busy photos. CSS holds `--logo-stack: 60px` and `--logo-horizontal: 30px`, hinting at stack/horizontal min heights, but no clearspace is visible.
- **Structure of the hub (from nav):** Intro · Brand guidelines (9 pages) · Manifesto · Brand values · Strategy (locked) · Media kit.

## 9. UX
- Highly legible hero and tiles; the sticky pill nav gives access to every sub-area. Weaknesses: tiles are label-only (no previews) at 16 px grey, and a locked Strategy section blocks external users. Home contains little concrete spec.

## 10. Craft signals
- Single three-colour grading used consistently across every hero photo and card.
- The brush ring is reused as a highlight device (hero scribbles, "connections", record circles).
- 12 px radius shared by all cards and example images; 45/30 px on section seams.
- Wavy glyph set reproduced as a graphic pattern.

## 11. Reproduction recipe
```css
:root{--blue:#5000ff;--orange:#f45827;--pink:#f69ae4;--yellow:#f3f810;--navy:#171c2b;--navy2:#22293c;--body:#61667a}
.hero{background:linear-gradient(#5000ff,#5000ff);mix-blend-mode:normal}
.hero img{filter:grayscale(1) contrast(1.4)}
.hero::after{content:"";position:absolute;inset:0;background:linear-gradient(#5000ff,#f45827);mix-blend-mode:screen}
.display{font:500 170px/160px "Sine Sans",sans-serif;text-transform:uppercase;color:#fff}
body{font:400 17px/28px "DM Sans",sans-serif;color:var(--body)}
.tile{border-radius:12px;box-shadow:0 0 12px 1px rgba(0,0,0,.05);transition:filter .2s ease}
.sheet{border-radius:45px 45px 0 0;background:#fff;margin-top:-45px}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 9 | Vivid tri-tone imagery, doodles and a quirky display face feel authentically club culture. |
| Originality | 8 | The duotone + sticker + wavy-letter system is distinctive within the music category. |
| Usability | 6 | Home is mostly mood; specs live in uncaptured subpages; tile labels are small and grey. |
| Craft | 8 | Consistent treatment, radii and shadows; lock icon on the Strategy item is a nice detail. |

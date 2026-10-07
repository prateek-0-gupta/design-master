---
id: insp-pick-your-plan
source: inspora
category: Product
status: analyzed
title: "Pick your Plan"
creator: "@basit_designs"
styles: [bento-grid, cinematic-3d, editorial-serif, maximalist-color]
patterns: [pricing-bento, segmented-plan-switcher, hero-plan-card, feature-tiles-with-3d-art, image-fade-into-surface, price-with-muted-period]
mode: light
palette: ["#f5f5f5", "#ffffff", "#111111", "#759ad3", "#9166bc", "#e2c4c8", "#e5fc9a", "#d8c6f6"]
type_families: ["serif display à la PP Editorial / Instrument Serif (likely)", "Inter (likely)"]
type_class: [editorial-serif, neo-grotesk]
radius_px: [48, 40, 9999]
motion: {durations_s: [], easing: [linear], loop: true}
scores: {aesthetics: 8, originality: 6, usability: 6, craft: 7}
craft_signals: [art-fades-into-tile-surface, serif-title-sans-ui, muted-per-month-suffix, hue-per-feature-tile, segmented-thumb-raised-white, condensed-serif-tracking]
anti_patterns: [no-cta-in-view, feature-tiles-not-actionable, art-carries-little-meaning]
---
# Pick your Plan — @basit_designs

## 1. Snapshot
- **Subject:** A 14.17 s, 1902×2304 loop of a mobile-sized pricing card. It has a serif "Pick your Plan" title, a three-way plan switcher, a hero "Upgrade to Pro $79/month" card and a 2×2 bento of feature tiles, each topped with a softly animated 3D render.
- **Why it's remarkable:** Each feature gets its own **material-hue 3D vignette** (pink silk, lilac droplet, lime folds, blue discs). The art **fades into the grey tile surface** above the caption, so the tiles feel like windows rather than stickers.

## 2. Composition & layout
- **Outer card:** about 970×1670 px in key-frame px (≈1115×1920 real), radius about 48 px, white, centred on #f5f5f5. Its padding is about 35 px.
- **Stack:**
  - The title is centred at y≈290.
  - The segmented switcher (about 560×80 px) sits at y≈415.
  - The hero card is full-width (about 900×475 px). Its text sits top-left and its features bottom-left. The 3D ribbon occupies the right 50% and bleeds off the top, right and bottom edges.
  - Below it is a 2×2 grid of tiles about 440×380 px with a gutter of about 22 px.
- Every tile is split roughly 65% art / 35% caption. Captions are centred two-liners.

## 3. Typography
- **Title:** a high-contrast transitional/editorial serif with tight tracking (about −0.03 em) at about 90 px. The narrow "y" and "k" suggest something like Instrument Serif or PP Editorial New. It is the only serif.
- **UI type:** Inter-like:
  - "Upgrade to Pro" is about 48 px Medium.
  - "$79" is 48 px Medium black, followed by "/month" at the same size in grey (#a8a8a8). This is a neat price-suffix trick.
  - Feature bullets are about 26 px Regular #5f5f5f, each with a small grey badge-check icon.
  - Tile captions are about 26 px Regular #5f5f5f, centred.
  - Switcher labels are about 26 px, with the active label in black Medium.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #f5f5f5 | page and tile surface | 80% |
| #ffffff | outer card, active segment | — |
| #111111 | title, price | — |
| #759ad3 / #9166bc | hero ribbon blue / violet | 6% |
| #e2c4c8 | pink silk tile | 3% |
| #d8c6f6 | lilac droplet tile | 3% |
| #e5fc9a | lime folds tile | 3% |

WCAG checks:
- #111 on white: 18.9:1.
- Captions #5f5f5f on #f2f2f2: 5.7:1.
- **"/month" #a8a8a8 on #f2f2f2: 2.12:1.** This is intentional de-emphasis, but it is part of the price, so it should be at least 4.5:1.
- Grey text over the faded lime: 5.69:1.

The chrome is neutral and every bit of hue lives in the renders. Each tile is assigned its own colour family.

## 5. Depth & material
- The renders are glossy 3D materials:
  - iridescent ribbon (hero);
  - translucent silk with lens flare;
  - glass bead on rippled liquid;
  - matte lime cloth;
  - frosted blue discs.
- Each render is masked with a vertical gradient to the tile colour at about 60% height.
- The UI is flat: no shadows except a hairline-plus-soft shadow on the active switcher thumb (white pill on #f0f0f0 track) and a faint 1 px border on the outer card.

## 6. Components & patterns
- **Segmented control:** a three-option pill track with a raised white thumb on the active option.
- **Hero plan card:** price-first, with two check-badge bullets.
- **Feature bento:** 2×2 equal tiles, art on top and caption below.
- **Missing:** no CTA button is visible in any frame; the card ends at the tiles.

## 7. Motion
Measured: 14.17 s at 30 fps, `motion_fraction` **0.00** and zero segments. Mean energy is 0.06 and `first_last_diff` is 2.07.
- All motion is slow, continuous drift inside the renders, below the detection threshold. The layout never moves.
- Frame comparison shows the pink silk's flare shifting and its colour moving from rose to coral (0.79 s → 11.81 s), the lilac ripple breathing, and the blue discs rotating slightly.
- This is ambient "living wallpaper" motion, estimated as a linear 10–15 s loop per tile.
- The plan switch is not demonstrated.

## 8. Brand system
n/a — not a brand system. Identity cues:
- a serif headline over a sans UI;
- a "one hue per feature" art direction reminiscent of Apple's iOS wallpapers.

## 9. UX
- **Strengths:**
  - The price is the second-largest element.
  - The switcher clearly shows three tiers.
  - Feature captions are short.
- **Risks:**
  - There is no purchase CTA.
  - The tiles look tappable but aren't explained.
  - "/month" contrast is low.
  - The decorative art takes about 60% of the area while conveying little feature meaning (e.g. a glass droplet for "roaming").
  - Switching plans may reflow the whole bento; not shown.

## 10. Craft signals
- Gradient masks fade each render into the exact tile colour (#f5f5f5), with no visible seam.
- The hero ribbon bleeds off three edges of its card and is clipped by the card radius.
- In the price "$79/month", the number is black and the period is grey at the same size and baseline.
- Each tile gets a distinct hue family: pink, lilac, lime, blue.
- Nested radii: the outer card is about 48 px and the tiles about 40 px.

## 11. Reproduction recipe
```css
:root{--page:#f5f5f5;--card:#fff;--tile:#f5f5f5;--ink:#111;--muted:#5f5f5f;--suffix:#767676;/* AA-safe */
  --r-outer:48px;--r-tile:40px;--serif:"Instrument Serif","PP Editorial New",serif;--sans:"Inter",sans-serif}
.title{font:400 clamp(40px,6vw,64px)/1 var(--serif);letter-spacing:-.03em;text-align:center}
.seg{display:inline-flex;background:#f0f0f0;border-radius:9999px;padding:4px}
.seg [aria-selected=true]{background:#fff;border-radius:9999px;box-shadow:0 1px 2px rgba(0,0,0,.08),0 0 0 1px rgba(0,0,0,.04);color:var(--ink);font-weight:500}
.bento{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.tile{background:var(--tile);border-radius:var(--r-tile);overflow:hidden;aspect-ratio:440/380;display:grid;grid-template-rows:65% 35%}
.tile video{object-fit:cover;mask-image:linear-gradient(#000 55%,transparent 100%)}
.price small{color:var(--suffix);font-size:inherit}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Lush 3D art held in a calm, neutral grid with an elegant serif title. |
| Originality | 6 | 3D-render bento pricing is a common Dribbble trend, though nicely executed here. |
| Usability | 6 | There is no CTA, the art outweighs information, and the price suffix has low contrast. |
| Craft | 7 | Seamless fades, consistent nested radii and a clear switcher thumb. |

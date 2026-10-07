---
id: bg-1042-studio-framer-components
source: brandguidelines
category: promoted
status: analyzed
title: "1042 Studio Store — Premium Components & Design Assets"
creator: "1042 Studio"
styles: [minimal-swiss, photo-led, monochrome]
patterns: [swiss-three-column-nav, full-bleed-product-hero, two-column-product-grid, price-chip-pill, filter-chips-all-figma-framer, browser-window-product-mockup, wordmark-nav-tens-forty-two]
mode: light
palette: ["#fcfcfc", "#fbfaf8", "#121212", "#8f8f8f"]
type_families: ["PP Neue Montreal Medium (body, census)", "Aspekta Variable 1000 (titles and display, census)"]
type_class: [neo-grotesk, grotesk]
radius_px: [16, 40, 8]
motion: null
scores: {aesthetics: 8, originality: 6, usability: 6, craft: 7}
craft_signals: [swiss-flush-left-grid, single-ink-on-off-white, product-thumbnails-as-brand, price-pill-alignment, 16px-body-with-20.8px-leading, display-tracking-minus-0-03em]
anti_patterns: [grey-meta-text-below-aa, no-visible-sort-or-search, long-undivided-grid]
---
# 1042 Studio Store — Premium Components & Design Assets — 1042 Studio

## 1. Snapshot
- **Subject:** The store page of 1042 Studio (`1042.studio/store`), a Framer-built shop for Framer and Figma components, remixes and kits. The capture redirected from `1042.studio/store` to `www.1042.studio/store` with no archive. Title: "1042 Studio Store | Premium Components & Design Assets".
- **Why it's remarkable:** A product list that is almost entirely a Swiss-style grid on an off-white ground. The products are shown as full-width framed screenshots, so the store works as a showroom with no marketing copy beyond one line.

## 2. Composition & layout
- **Header:** three wordmark items ("TEN", "FORTY", "TWO®") on a flush-left baseline at y≈32, with "Store" underlined at the right margin (x≈1392).
- **Title block:** a 78 px "Store" H1 at x=24, with a two-line deck at x≈378 (about 350 px from the title). The deck is about 20 px. A 32 px gutter separates the columns.
- **Product rows:** a full-width product hero (1392 px wide, about 783 px tall) for the first item. Below it, a filter row of pills ("All", "Figma", "Framer") and then a two-column grid. Each cell is about 684 px wide with a 24 px gutter.
- **Mobile (390 px):** the grid becomes one column with a 26 px margin. Titles and prices stay on one line.

## 3. Typography
- **Families (census):** PP Neue Montreal Medium carries body and labels (127 uses at 16 px, 400 weight). Aspekta Variable at weight 1000 carries display and product names (34 uses).
- **Scale (census):** 16 px (153 uses), 18 px (6), 20 px (1), 78 px (1). The body is essentially one size.
- **Line height:** 20.8 px (115 uses) for body text, which is 1.3, and 81.9 px for the 78 px H1 (about 1.05).
- **Tracking:** body text is `normal` (122 uses). Aspekta titles use `-0.16px` (38 uses) and the display uses `-2.34px` (about -0.03em at 78 px).
- **Weights:** 400 (125 uses), 1000 (34 uses) and 500 (2). The 1000 weight is the only heavy weight on the page.

## 4. Colour
| Hex | Role | Approx share (tile 1) |
|---|---|---|
| #fcfcfc | page ground (census `bg`) | ~37% |
| #fbfaf8 | token background (`--token-1c31…`) | not sampled in tiles |
| #121212 | ink: titles, prices, nav | ~24% of tile 1 (mostly the product black) |
| #8f8f8f | secondary text (census `textColor`, 81 uses) | text only |
| rgba(18,18,18,.04) | chip fill for filter pills | very low |

- **WCAG pairs (contrast.py):** #121212 on #fcfcfc **18.26:1**. #8f8f8f on #fcfcfc **3.15:1**, which fails AA-normal and passes only at large sizes.
- The sub-line "Framer Component" and "Framer Remix Component" is set in #8f8f8f at 16 px. That is the failing pair on the page.
- Product images carry the colour. The Spotify Mirrorball tile is a bright green (#1cbd55 sampled), and most other tiles use dark or saturated photos.

## 5. Depth & material
- No shadows (the census has none) and no borders. Depth comes from the product screenshots, which sit inside a browser window with three 6 px traffic-light dots and a translucent header.
- Filter chips use a 4% ink tint, so they read as flat tags.

## 6. Components & patterns
- **Product card:** a row with the name on the left and the price on the right, then a grey category line, then a full-width framed image. The price sits in a fully rounded pill.
- **Filter pills:** "All" (outlined when active), "Figma" and "Framer" as tinted chips.
- **Browser-window mockup:** every product is a framed screenshot in a 3-dot window, which keeps the catalogue visually consistent.
- **Price pill:** "Free", "$10", "$15", "$109" etc. The pill is the only element with a fill in the grid.
- **Footer:** four links stacked (Home, Store, Imprint, Terms) at the bottom-left.

## 7. Motion
- Not measurable. The census has no transitions, no shadows and no durations. Nothing is claimed.

## 8. Brand system
n/a — not a brand system. This is a store page. Identity cues: the spaced three-word wordmark (TEN / FORTY / TWO®), an ink-on-off-white palette, and a Swiss grid with flush-left text. The brand is shown through its own product screenshots.

## 9. UX
- The store is easy to scan: one product per row, consistent price placement and a clear category line.
- The filter set is minimal ("All / Figma / Framer"). There is no search, sort or price filter, and no visible way to find a remix versus an original apart from the category line.
- Weaknesses: the grey meta line fails AA (3.15:1), and the single long grid (9,523 px scroll height in the census) has no pagination in the capture.

## 10. Craft signals
- Flush-left alignment is held across the header, title, deck and grid.
- Body text sits at 16/20.8 px with normal tracking, so the page reads at one size.
- Display tracking is set in em-equivalent px (-2.34 px at 78 px).
- Product thumbnails are all framed in the same browser window, so the grid stays consistent when the photography varies.

## 11. Reproduction recipe
```css
:root{
  --paper:#fcfcfc; --paper-2:#fbfaf8; --ink:#121212; --ink-2:#8f8f8f;
  --chip:rgba(18,18,18,.04); --r-chip:16px; --r-pill:40px;
  --font-body:"PP Neue Montreal Medium",sans-serif;
  --font-disp:"Aspekta Variable",sans-serif;
}
body{background:var(--paper);color:var(--ink);font:400 16px/20.8px var(--font-body);}
h1{font:1000 78px/81.9px var(--font-disp);letter-spacing:-2.34px;}
.product-title{font:1000 16px/20px var(--font-disp);letter-spacing:-.16px;}
.meta{color:#6b6b6b;} /* #8f8f8f fails AA at 16px; use a darker grey for text */
.price{background:var(--chip);border-radius:var(--r-pill);padding:6px 14px;}
.filter{background:var(--chip);border-radius:var(--r-chip);padding:8px 14px;}
.grid{display:grid;grid-template-columns:1fr 1fr;column-gap:24px;row-gap:48px;}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | A disciplined Swiss grid, strong black-on-off-white type and image-led products. |
| Originality | 6 | Swiss storefronts are familiar, but the framed browser windows give the catalogue a clear identity. |
| Usability | 6 | Clean scanning and clear prices; minimal filters, no search and a grey meta line that fails AA. |
| Craft | 7 | Consistent alignment, one body size and tidy pill treatment; a few tokens are unsampled. |

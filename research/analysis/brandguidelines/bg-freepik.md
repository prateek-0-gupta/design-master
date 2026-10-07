---
id: bg-freepik
source: brandguidelines
category: guideline
status: analyzed
title: "Freepik / Magnific Press Resources"
creator: "Freepik Company (Magnific)"
styles: [corporate-clean, photo-led, dark-premium]
patterns: [press-kit-landing-page, spokesperson-card-grid, full-bleed-photo-hero-with-scrim, product-visual-tiles-with-dark-scrim, download-icon-per-card, cream-ground-with-oxblood-text, pink-accent-footer-headings]
mode: mixed
palette: ["#f4f3ef", "#2c0000", "#000000", "#101010", "#ff58ae", "#4f5fef", "#b3c9fd", "#665151"]
type_families: ["Klarheit (headings, weight 800)", "Geist (body 400/500/600)", "Geist Mono"]
type_class: [grotesk, neo-grotesk, mono]
radius_px: [8, 12, 24]
motion: {durations_s: [0.15, 0.3], easing: [cubic-bezier(0.4,0,0.2,1)], loop: false}
scores: {aesthetics: 7, originality: 5, usability: 7, craft: 6}
craft_signals: [oxblood-text-on-cream-instead-of-black, single-easing-token-367-uses, dark-scrim-on-product-tiles, consistent-12px-card-radius, tight-negative-tracking-on-display]
anti_patterns: [redirect-to-wrong-page, no-actual-logo-or-colour-rules-visible, mostly-people-cards, scrim-dims-product-visuals]
---
# Freepik / Magnific Press Resources — Freepik Company

## 1. Snapshot
- **Subject:** requested `freepik.design`; the captured final URL is `magnific.com/app/tools/image-to-360?...`. The home tiles actually show the **Magnific Press resources** page, and the page title is "Magnific: Press Resources and Brand Guidelines". The banner reads "Freepik is now Magnific". This is a **promoted press-kit landing page**, not a brand guideline, so §8 is kept short. The six subpages are Magnific AI product pages (Image Generator, Editor, Upscaler, Extender, Text to Speech, 3D 360). No Wayback archive.
- **Why it's remarkable:** a press page on a warm cream ground whose "black" is a deep oxblood (#2c0000), set against dark product tiles and a bright pink accent.

I viewed home t01, t02, t04, t06, subpages d01 t01 (Image Generator) and d03 t01 (Image Upscaler), and mobile sheet 1.

## 2. Composition & layout
- **Hero (0–1000 px):** a full-bleed photograph (a face and a globe) with a dark scrim, nav on top. The H1 "Magnific Press resources" sits at x=128, y≈497 in white at about 56 px, with a 20 px subline.
- **Body:** cream ground, content width 1280 px (x 80–1360). Sections stack with about 200 px vertical gaps: Brand overview (video card), Press guidelines (centred text), Spokespeople (one featured 628 px card plus a 4-up row), Product visuals (3-up plus a full-width tile), Enterprise use cases, Official Brand kit (white card with a dark button), Press & media inquiries.
- **Footer:** black, five columns, pink column headings.
- **Mobile:** the layout is a single column. The hero H1 drops to about 34 px. Spokesperson cards stack, centre-aligned, one per row. This makes about 15 cards long (the sheet shows 4 columns of the same scroll).

## 3. Typography
From census: **Klarheit 800** for headings and **Geist** for everything else.
- H1 56/56, letter-spacing -0.56 px.
- H2 44/52.8, -0.44 px (9 uses).
- Subhead 28/33.6, -0.56 px.
- Body 14/22.4 (48 uses), 16/25.6, 18/27, 20/30 (weight 500 for lead text).
- Micro label 10/10, 600, +0.2 px tracking.
The display face is heavy and tightly tracked; body Geist is neutral.

## 4. Colour
| hex | role | approx share |
|---|---|---|
| #f4f3ef | page ground | 70–74% of body tiles |
| #2c0000 | text on cream (rgb 44,0,0), 57 uses | text |
| #665151 | secondary body on cream | text |
| #000000 / #101010 | hero scrim, tile ground, footer | 13–26% |
| #ff58ae | pink accent: announcement bar, footer headings (rgb 255,88,174) | tiny |
| #4f5fef | "Generate" button on the product page | tiny |
| #b3c9fd | tag chip fill ("New") | tiny |
| #ffffff | cards, nav text | — |

Contrast:
- #2c0000 on #f4f3ef: **17.08:1**.
- #665151 on #f4f3ef: **6.61:1**.
- #ff58ae on #000: **7.26:1**.
- White on #4f5fef: **4.98:1**.
- White on #101010: **19.03:1**.

## 5. Depth & material
No box shadows (census: none). Depth comes from photography and from 50% black scrims over product screenshots, which makes the "Community / Spaces / Image Generator / All tools" tiles look dim and cinematic. Cards on cream use a 1 px light-brown outline and a 12 px radius.

## 6. Components & patterns
- Pill nav with a search field, a "Log in" link and a white "Sign up" button.
- Announcement bar in pink on black.
- Spokesperson cards: a portrait, a name at 20 px and a role at 14 px, with a download icon bottom right.
- Section header with a square outlined download button on the right.
- Product tiles with a bottom-left white label.
- On the product pages: a dark prompt box with a blue Generate button, a horizontally scrolling image strip, and a sticky "On this page" index with mono-style uppercase labels.

## 7. Motion
All transitions in the census use one easing, `cubic-bezier(0.4,0,0.2,1)` (367 uses in the CSS), at 0.15 s for colour and border, 0.1 s for quick states and 0.3 s for transform. A faster snap curve (0.16,1,0.3,1) appears 29 times. The press video card is an autoplaying text-reel (a scrolling list of tool names).

## 8. Brand system
This is a press kit. The visible brand rules are the "Press guidelines" paragraph (identify Magnific as an AI-powered creative platform; contact press@magnific.com) and a downloadable "Official Brand kit" (logos, colour palettes, typography and usage guidelines). The kit itself is not on the page, so the actual logo, colour and clearspace rules could not be analysed. The Magnific wordmark is a white "M" glyph plus a rounded sans wordmark.

## 9. UX
The page is easy to scan and each asset carries its own download icon. It is a long scroll with no in-page navigation. The dark scrim on product visuals hides the detail press people need. The mobile spokesperson list is very long.

## 10. Craft signals
- Oxblood #2c0000 instead of pure black on cream gives a warmer, more premium read.
- One easing token used across about 370 transitions.
- Consistent 12 px and 8 px radii.
- Negative tracking on display sizes (-0.44 / -0.56 px).
- Pink used only for the announcement bar and footer headings.

## 11. Reproduction recipe
```css
:root{--cream:#f4f3ef;--oxblood:#2c0000;--ink:#101010;--pink:#ff58ae;--cta:#4f5fef;--ease:cubic-bezier(.4,0,.2,1)}
body{background:var(--cream);color:var(--oxblood);font:400 16px/1.6 "Geist",sans-serif}
h1,h2{font:800 44px/1.2 "Klarheit","Helvetica Neue",sans-serif;letter-spacing:-.01em}
.card{border:1px solid #d5ccc8;border-radius:12px;padding:24px}
.tile{position:relative;border-radius:12px;overflow:hidden}
.tile::after{content:"";position:absolute;inset:0;background:rgb(0 0 0/.5)}
a,button{transition:color,background-color,border-color .15s var(--ease)}
footer h4{color:var(--pink)}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 7 | Warm cream and oxblood with dark product tiles is distinctive for an AI brand. |
| Originality | 5 | It is a standard press-kit layout. |
| Usability | 7 | Clear downloads and contacts; long mobile scroll. |
| Craft | 6 | Disciplined tokens, but the capture went to the wrong destination and the key brand content is missing. |

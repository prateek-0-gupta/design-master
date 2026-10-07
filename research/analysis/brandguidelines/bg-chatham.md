---
id: bg-chatham
source: brandguidelines
category: guideline
status: analyzed
title: "Chatham Identity Guidelines (partial: section 01 only)"
creator: "Chatham (in-house, hosted on Standards.site)"
styles: [editorial-serif, minimal-swiss, high-contrast-bw, corporate-clean]
patterns: [four-column-meta-header-per-block, huge-fading-section-index, two-up-logo-on-colour-squares, red-diagonal-strike-donts, scaling-stack-ladder, partner-lockup-stripes, icon-only-when-space-is-tight, next-section-footer-card]
mode: mixed
palette: ["#052e21", "#f2f6f6", "#000000", "#383b3b", "#c4cccc", "#ee3f22", "#ffffff"]
type_families: ["Custom slab-serif display (Chatham typeface, hashed webfont)", "Condensed grotesque for caps labels (hashed webfont, likely a News Gothic style)", "Text serif for body (hashed webfont)", "Söhne (Standards.site chrome only, on the 404)"]
type_class: [slab, condensed, transitional-serif]
radius_px: []
motion: {durations_s: [0.5], easing: [ease], loop: false}
scores: {aesthetics: 8, originality: 6, usability: 6, craft: 7}
craft_signals: [block-header-four-slot-grid, wordmark-sized-to-grid, caps-labels-tracked-1px, logo-scaling-ladder, strike-line-in-brand-red, dark-green-tonal-index]
anti_patterns: [only-one-section-captured, subpages-404, typos-parterships-patthens, no-clearspace-spec, low-contrast-white-on-grey-logo-tile]
---
# Chatham Identity Guidelines — Chatham

## 1. Snapshot
- **Subject:** the identity site for Chatham, a heritage woollen-blanket label ("since 1877"), built on Standards.site. `site_meta.json`: requested `live.standards.site/chatham`, final URL `/Photography`. The subpage captures (`d01–d03`, Typography, Color, Photography) are Standards.site "Page not found" screens (wrong slug paths), so they are not content. **Only the home page was captured, and it shows only section 01 "Wordmark & Icon"** (about 8 tiles; page index 00–06 is visible in the opening block). Typography, Color, Elements, Photography and Applications are known only from the nav.
- **Why it's remarkable:** a bold, American-sports-jersey slab wordmark treated as the entire brand, with a Swiss-style four-slot header repeated on every block and a deep-green index that fades its inactive entries.

## 2. Composition & layout
- **Index screen:** full-width #052e21 block (≈1055 px tall on a 1440 px tile). Seven entries stacked at 96 px pitch, 108 px type at line-height 98 px. The active entry ("01 Wordmark & Icon") is white, the others sit at 10% white (`rgba(255,255,255,.1)`). Eyebrow "CHATHAM IDENTITY GUIDELINES" 14 px caps centred at y≈125.
- **Block header (every block):** four slots on one baseline: "CHATHAM" at x=100, block title at x=310 (slab caps, 34/36 px), section name at x=835, "IDENTITY GUIDELINES" at x=1150. A narrow left column (x=100–270) holds 14 px serif notes.
- **Demo area:** x=310 to 1340, i.e. 1030 px wide. Two-up tiles are 505×505 with a 20 px gutter (310–815, 835–1340).
- **Vertical rhythm:** ≈200–250 px between blocks, no dividers, only whitespace.
- **Footer:** a "NEXT SECTION" card in the same green with the next index at 10%.
- **Mobile (390 px):** only the index screen was captured in `m00_home_sheet01`; it centres the same list and wraps "01 WORDMARK & ICON" onto two lines.

## 3. Typography
Census families are hashed, so identification is visual:
- **Display (family 95f6…):** a bold slab-serif, all caps, for the wordmark, index and block titles. 108/98 (index), 34/36 (block titles). The doc says the wordmark letterforms derive from Chatham's custom typeface.
- **Labels (faaf…):** 14 px / 19, uppercase, +1 px (0.998) tracking; a light condensed gothic.
- **Body (6c3e…):** 14 px / 19 text serif, 55 uses. Body is deliberately small and sits in the left margin as a caption.
- A fourth 30 px weight-600 face appears once (UI).

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #ffffff | content ground | ~45–55% |
| #052e21 | index/next-section green, logo-on-green | ~20% |
| #f2f6f6 | tile ground (light) | tiles |
| #000000 | text, single-colour logo | text |
| #383b3b | dark neutral tile | 1 tile |
| #c4cccc | grey tile | 1 tile |
| #ee3f22 | partner red ("× FLOYD" stripe) | accent |
| #cb3700 | unapproved-colour example (a "don't") | demo only |

Contrast: green on white 14.8:1; #f2f6f6 on green 13.59:1; black on #f2f6f6 19.29:1; white on #383b3b 11.31:1. **White wordmark on the #c4cccc tile is 1.63:1**, shown as an approved "logo on color" pairing even though the page says to ensure contrast. Inactive index text on green is ≈1.2:1 by design (a "ghost" state).

## 5. Depth & material
Entirely flat. No shadows, radii, gradients or borders. Photographic depth appears only in the icon-use examples: a phone on a wood desk and a green vest on grey.

## 6. Components & patterns
Section index; block header; logo tiles on colour; single-colour tiles (light / black); logo scaling ladder (six sizes, small to full-width); partnership stripes (`CHATHAM × Acne Studios / Rimowa / Floyd / Tom Ford`) with partner logos in one colour; secondary mark "CHATHAM BLANKET" in a thick black frame (blanket products only); icon "C" rules (full logo when space allows, never the icon when there is space; icon externally only with the name beside it); a six-up don'ts grid with a red hairline diagonal strike (tilt, wrong colour, stretch, outline, shadow, pattern).

## 7. Motion
The only measurable value is `opacity 0.5s ease` (19 uses), on index and link hover/active. The fading index suggests scroll-driven highlighting, but this was not captured as motion.

## 8. Brand system
**Captured chapters (01 Wordmark & Icon only):** Wordmark → Logo on color → Single color → Scaling → Partnerships → Secondary mark → Secondary mark in use → Icon use → Don'ts. **Not captured:** 02 Typography, 03 Color, 04 Elements, 05 Photography, 06 Applications (named in nav only).
- **Logo:** wordmark only, built from the custom slab. Icon = the slab "C".
- **Colour:** four approved logo grounds: light #f2f6f6, green #052e21, dark #383b3b, grey #c4cccc; single-colour black or off-white.
- **Scaling:** "as big as you like"; downward is by judgement ("if it is hard to read, it is too small"). **No minimum size or clearspace number** is given in what was captured.
- **Partnerships:** lock-up with × and the partner logo always in one colour.
- **Voice:** brief and heritage-led ("Art and tradition of American woolens since 1877", "The revival of the world-famous Chatham Blanket").

## 9. UX
Fast to scan: one idea per block, captions in a fixed margin, don'ts shown rather than described. Weaknesses: judgement-based sizing, unspecified clearspace, typos ("Parterships", "patthens"), and subpages that currently 404.

## 10. Craft signals
- The wordmark is stretched to exactly the 1030 px demo column on its hero block.
- The same 4-slot header on every block, with caps labels tracked at +1 px.
- Square tiles on a 505 px module with a constant 20 px gutter.
- Strike lines are 1 px in brand red (#cb3700 family), from corner to corner.
- Ghosted inactive index at 10% opacity of the foreground.
- Image captions at 14 px under each tile, left-aligned.

## 11. Reproduction recipe
```css
:root{--green:#052e21;--tile:#f2f6f6;--ink:#000;--slate:#383b3b;--fog:#c4cccc;--red:#cb3700;
 --display:"Rockwell Condensed","Roboto Slab",serif;--label:"News Gothic Condensed","Barlow Condensed",sans-serif;--text:Georgia,serif}
.index{background:var(--green);padding:120px 0;text-align:center}
.index li{font:400 108px/98px var(--display);text-transform:uppercase;color:rgba(255,255,255,.1);transition:opacity .5s ease}
.index li.on{color:#fff}
.block-head{display:grid;grid-template-columns:210px 525px 315px 1fr;font:400 14px/19px var(--label);letter-spacing:1px;text-transform:uppercase}
.block-head h2{font:400 34px/36px var(--display)}
.tile{aspect-ratio:1;background:var(--tile);display:grid;place-items:center}
.dont{position:relative}.dont::after{content:"";position:absolute;inset:0;background:linear-gradient(to top right,transparent calc(50% - .5px),var(--red) 50%,transparent calc(50% + .5px))}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Heavy slab wordmark and dark green give strong identity with almost no ornament. |
| Originality | 6 | Index-as-title is neat; the rest is standard logo-usage content. |
| Usability | 6 | Easy to read, but no min size or clearspace and incomplete capture. |
| Craft | 7 | Tight grid and consistent header; spelling errors and a failing grey tile. |

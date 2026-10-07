---
id: bg-dropbox
source: brandguidelines
category: guideline
status: analyzed
title: "Dropbox Design Standards"
creator: "In-house"
styles: [corporate-clean, photo-led, minimal-swiss]
patterns: [split-hero-dark-title-light-strapline, artwork-collage-with-file-chrome, four-pillar-index-cards, coloured-icon-chips, resources-two-up, dark-sitemap-footer, token-prefixed-css-variables, see-buy-use-framework]
mode: mixed
palette: ["#1e1919", "#f7f5f2", "#0061fe", "#b4dc19", "#b4c8e1", "#ff8c19", "#fa551e", "#161313"]
type_families: ["Sharp Grotesk DB Book 20/23 (display)", "Atlas Grotesk (text/UI)"]
type_class: [grotesk, neo-grotesk]
radius_px: []
motion: {durations_s: [0.25, 0.3], easing: [cubic-bezier(0.4,0,0.2,1)], loop: false}
scores: {aesthetics: 7, originality: 6, usability: 7, craft: 8}
craft_signals: [namespaced-design-tokens, 3px-focus-ring-token, tight-negative-tracking-on-display, warm-off-white-and-warm-black, file-browser-chrome-on-hero-art]
anti_patterns: [home-only-coverage, default-blue-underlined-links-on-warm-page]
---
# Dropbox Design Standards — In-house

## 1. Snapshot
- **Subject:** home of dropboxdesignstandards.com ("Welcome to the design standards"). Wayback Machine capture dated 2024-05-16 22:56:45 UTC (`captured_from` .../web/20240516225645if_/https://dropboxdesignstandards.com/); the live domain is no longer reliable.
- **Coverage:** home page only (two 1800 px tiles, 2454 px total) plus one mobile sheet. No subpage was captured, so logo, type, colour, layout and writing rules are known only by their titles in the footer sitemap.
- **Why it's remarkable:** the hero turns an art collage into a file-browser scene ("Creativity Explored > Digital Museum.png"), so the brand is demonstrated by its own product metaphor.

## 2. Composition & layout
- 64 px white top bar with a 64 px blue logo tile (#0061fe) and four text links (Strategy, Foundation, Systems, Writing).
- Hero is a 50/50 split at x=720, 726 px tall: left a warm black (#1e1919) field with the 72 px title, below it a warm off-white strip (#f7f5f2) with a 20 px strapline; right a #393836 panel with three paintings and a ceramic-figure photo overlapping at different offsets.
- Index: a 2×2 grid, left column at x=72 and right at x=744 (600 px columns, 72 px outer margin). Each cell is a 48 px square coloured icon chip, a 22 px title, a one-line description and an underlined link.
- "Resources" band: two 624 px cards with 16:9-ish previews (See-Buy-Use journey map; a Directory product-visual mock-up).
- Footer: #151412 with four columns (Strategy, Foundation, Systems, Writing) at 336 px pitch, a hairline and legal links. The sitemap lists Foundation as Customer Journey, Logo, Typography, Color, Layout and Planes, Visual Imagery, Shape; Systems as DIG and DWG.

## 3. Typography
- **Sharp Grotesk DB Book 23** at 72/79 px, weight 300, tracking −0.72 px (−1%) for the H1; **Book 20** at 28/36, 22/28 and 16/26 for section titles.
- **Atlas Grotesk** 400 for text: 14/18 (labels), 14/22 (body), 12/20, 20/30.
- Eight sizes, all weights 300 or 400: hierarchy is size and face, not boldness. Tokens expose `--type__title__large--fontsize: 28px`.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #ffffff | content area | 41% |
| #393836 | hero art panel | 15% |
| #1d1918 / #1e1919 | hero title field, glyph primary | 13% |
| #f6f5f1 / #f7f5f2 | warm off-white strip, inverse text | 9% |
| #0061fe | logo tile, links | small |
| #b4dc19, #b4c8e1, #ff8c19, #fa551e | icon chips (Strategy, Foundation, Systems, Writing) | small |
| #161313 | footer inverse background | — |

Contrast: #f7f5f2 on #1e1919 **15.97:1**; #0061fe on white **5.07:1**; #1e1919 on #b4dc19 **10.92:1**. Footer secondary text at 60% alpha is not computed here.

## 5. Depth & material
No radius and no shadows in the home census. Layering is photographic: overlapping artwork cards and a cut-out figurine. A `--boxshadow__focusring: 0 0 0 3px #428bff` token exists for keyboard focus.

## 6. Components & patterns
Square icon chips in four accent colours; text links with underline; pill "Digital Museum.png" file-chip in the hero; resource cards; dark sitemap footer.

## 7. Motion
`box-shadow 0.3s cubic-bezier(0.4,0,0.2,1)` and a 0.25 s material-style transition on background, shadow, border and colour (focus/hover). Token `--duration__1000` suggests a 1 s tier.

## 8. Brand system
Seen on this page only:
- **Structure:** four pillars: Strategy (design strategy), Foundation (customer journey, logo, typography, colour, layout and planes, visual imagery, shape), Systems (DIG, DWG: design and writing systems) and Writing. The See / Buy / Use customer-journey framework and three "product visual" types are previewed.
- **Voice:** "clear, simple, and magical".
- **Token architecture (worth stealing):** double-underscore names, e.g. `--color__glyph__primary`, `--color__inverse__standard__background`, `--type__body__xsmall--lineheight_paragraph`, with separate paragraph and label leading, plus status colours (`--color__success--dark #2d8000`, `--color__warning--dark #9a6500`, `--color__accent__gold #9b6400`).
- **Unknown:** logo clearspace, minimum size, any misuse rules.

## 9. UX
Four clear entry points, resource shortcuts, and a full sitemap in the footer. Links are default blue-underlined, which feels unfinished against the refined hero.

## 10. Craft signals
- Warm blacks and off-whites instead of #000/#fff.
- Tracking −1% only on the 72 px display.
- Hero art sits at deliberate offsets and overlaps, like pinned prints.
- Focus ring is a named token.

## 11. Reproduction recipe
```css
:root{--ink:#1e1919;--paper:#f7f5f2;--blue:#0061fe;--chip-lime:#b4dc19;--chip-sky:#b4c8e1;--chip-orange:#ff8c19;--chip-red:#fa551e}
.hero{display:grid;grid-template-columns:1fr 1fr;height:726px}
.hero h1{font:300 72px/79px "Sharp Grotesk DB Book 23",sans-serif;letter-spacing:-.72px;color:var(--paper)}
body{font:400 14px/22px "Atlas Grotesk",sans-serif;color:var(--ink)}
.chip{width:48px;height:48px;border-radius:0}
a:focus-visible{box-shadow:0 0 0 3px #428bff}
.btn{transition:background-color .25s cubic-bezier(.4,0,.2,1),box-shadow .25s cubic-bezier(.4,0,.2,1)}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 7 | Warm palette and art collage give personality. |
| Originality | 6 | File-chrome hero is a smart touch; layout otherwise standard. |
| Usability | 7 | Clear pillars and sitemap; contrast fine; unseen depth. |
| Craft | 8 | Namespaced tokens, tracking and focus ring discipline. |

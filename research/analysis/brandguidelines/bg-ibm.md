---
id: bg-ibm
source: brandguidelines
category: guideline
status: analyzed
title: "IBM Design Language"
creator: "IBM Design"
styles: [corporate-clean, minimal-swiss, technical-wireframe, flat-illustration, isometric]
patterns: [persistent-left-sidebar-nav, black-hero-band-with-page-title, hash-link-section-index, resource-tile-grid, hairline-tile-cards, colour-swatch-ramp-as-nav-tile, 2x-grid-divisions-of-two, illustration-style-taxonomy]
mode: light
palette: ["#161616", "#f4f4f4", "#ffffff", "#0f62fe", "#0430ad", "#525252", "#e6d5ff", "#ffd8d9"]
type_families: ["IBM Plex Sans Var (100-900, roman + italic)", "IBM Plex Mono (code and spec values)", "IBM Plex Serif (typeface showcase)"]
type_class: [neo-grotesk, mono, transitional-serif, variable]
radius_px: [2]
motion: {durations_s: [0.07, 0.11, 0.15, 0.5], easing: ["cubic-bezier(0.2,0,0.38,0.9)", "ease"], loop: false}
scores: {aesthetics: 8, originality: 6, usability: 9, craft: 9}
craft_signals: [carbon-motion-curve, 0.16px-tracking-on-14px, hairline-1px-tile-dividers, single-hero-band-per-page, per-section-tint-colour, sidebar-active-bar-2px-blue, plex-mono-for-spec-values, fixed-0.07-0.11s-micro-durations]
anti_patterns: [video-first-frames-look-empty, sidebar-height-ends-before-page, text-column-narrow-with-large-empty-right]
---
# IBM Design Language — IBM Design

## 1. Snapshot
- **Subject:** the live IBM Design Language site (ibm.com/design/language). The captured landing is the home page; `site_meta.json` shows the request redirected to the Illustration Overview as the final URL, but the home tiles are from `/design/language/`. Subpages captured: Accessibility (/able), Color, 2x Grid, Typeface, Photography Overview and Illustration Overview. Capture was taken October 2026 (footer: updated 1 Oct 2026).
- **Why it's remarkable:** a guidelines site built with the same system it documents (Carbon, Plex). Every page shares a black title band, a 256 px sidebar, a 14/20 px text rhythm and white tiles on #f4f4f4, so the document is both reference and proof.

## 2. Composition & layout
- **Frame (1440 px):** a 48 px #161616 top bar ("IBM **Design Language**", search and app-switcher icons). A white left sidebar of 256 px with a 1 px right border holds 12 top-level entries with chevrons. Its height stops at about 900 px, so it ends mid-page on long pages instead of sticking visually.
- **Home hero:** a 1184 px wide, 560 px tall black video panel split by two 1 px vertical rules into three zones. The left zone holds a teal smoky "n" letterform, the other two are labelled "Philosophy" and "Gallery". A pause button sits bottom-left.
- **Intro block:** two columns on a 12-col rhythm. The label "Think → Guide" is at x≈384, the lead statement starts at x≈736 in Plex Sans Light at about 30 px / 40 px.
- **Tile grid:** 352 px square tiles (about 1056 px in 3 columns) with no gutters. Colour fills (#fff, #ffd8d9, green ramp, #d9fbfb) separate them. Typeface, Philosophy, Color, Photography and Illustration tiles are all different artwork. A second grid of white 352×176 px resource cards has 1 px #e0e0e0 hairlines.
- **Subpages:** a black band 320 px high with a 67.5 px Plex Light title anchored at the bottom-left (x=384, bottom padding about 40 px). A 22 px lead paragraph and a two-column "↳" hash-link index follow, then 14 px body in a column about 660 px wide. Large media such as video or photo runs full content width, 1024 px.
- **Page end:** a #262626 "Next" band (e.g. "Philosophy: Point of view") then a #000 footer with link columns at x=384 and x=912.

## 3. Typography
Census (home / subpages): font-size counts are 14 px (41 on home, 375 on Color), 20 px, 16 px, 12 px, 21.88 px and 29.88 px (the fluid 22/30/54/67.5 px sizes). Weights are 400 (dominant), 600 (nav and labels) and one 300 for the lead.

| Role | Spec |
|---|---|
| Page title | Plex Sans Light, 67.5 px, white on black |
| Display statement | Plex Sans Light, 30.9 px / 39.9 px |
| Lead | Plex Sans 400, 21.9 px / 27.4 px |
| Section heading | Plex Sans 400, 29.9 px |
| Body | Plex Sans 400, 14 px / 20 px, letter-spacing 0.16 px |
| Label / nav | 14 px 600, 18 px leading, 0.16 px |
| Caption | 12 px / 16 px, 0.32 px |
| Spec values | Plex Mono 14 px / 20 px, 0.32 px (268 uses on Color) |

Plex Serif appears only in the Typeface page showcase (16 uses). Letter-spacing is positive on small sizes (0.16 to 0.32 px) and zero at large sizes. Rem-based fluid scaling gives the odd 21.88/29.88 px values.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #f4f4f4 | page ground (--cds layer) | ~40-45% of tiles |
| #ffffff | tiles, sidebar | ~15-25% |
| #000000 / #161616 | title bands, top bar, text | ~14% |
| #0f62fe | IBM Blue 60, active bar, link/"core" blue | accent |
| #0430ad | deep blue, "Blue at the core" left swatch | 9% on Color tile 1 |
| #525252 | secondary text, sidebar | text |
| #e6d5ff / #752fcd | purple of the Accessibility and Illustration pages | per-page tint |
| #ffd8d9 | pink Philosophy tile | home tile |

Each subsection gets its own tint: purple for Accessibility and Illustration, blue for Color, teal for 2x Grid.

WCAG (contrast.py): #161616 on #f4f4f4 is **16.45:1**. #525252 on #f4f4f4 is **7.10:1**. White on #0f62fe is **5.00:1**. White on #161616 is **18.1:1**. #c6c6c6 on #161616 is **10.59:1**. #0f62fe on #f4f4f4 is only **4.55:1** (passes AA normal but with little margin).

## 5. Depth & material
Flat. The single census shadow is a 0 2px 6px rgba(0,0,0,.3) on one control, radius is 2 px on one item and 50% on circles. Depth appears only in the artwork: isometric purple platforms with soft drop shadows (Accessibility), grey isometric factory (Illustration tile), smoke-lit letterform (hero).

## 6. Components & patterns
- **Sidebar:** 14 px / 600 items, #525252 text, chevron expand and a 3-4 px blue left bar plus #e0e0e0 fill on the active item. Child items are indented 16 px at 400 weight.
- **Resource tile:** white, 1 px hairline, title top-left at 14-20 px, icon (Figma, GitHub, ZIP, download arrow, external-link) bottom-left and arrow bottom-right.
- **Hash index:** "↳ label" items in two columns, 22 px.
- **"What's new" cards:** coloured art above, 14 px title, 12 px mono-like date.
- **Embedded video** with native controls for Typeface, 2x Grid and Illustration heroes.
- **Mobile (390 px):** a hamburger replaces the sidebar, tiles go single column at the full 390 px, and a second strip stacks the resource cards one per row at 196 px.

## 7. Motion
From the CSS census: micro-interactions are 0.07 s (background, opacity) and 0.11 s (colour, background-color, outline, transform) with `cubic-bezier(0.2, 0, 0.38, 0.9)` (Carbon's productive curve); 0.15 s for `all` transitions with the same curve; 0.5 s ease on opacity (image reveal). There is a pause control for the hero video. No scroll-jacking.

## 8. Brand system
- **Chapters (sidebar):** Philosophy, Gallery; Typography (Typeface, Type basics, Type scale), Color, 2x Grid, IBM logos, Iconography, Illustration (Overview, Tips, Line, Flat, Isometric, Hybrid UI, People), Photography (Overview, Tips), Data visualization, Infographics, Layout, Animation; Resources, What's new, Help.
- **Philosophy:** "Build Bonds", with "Think → Guide" as the framing tag; Photography is "great observers of the working world"; illustrations are "Engineered, Clear, Nimble, Diverse, Delightful".
- **Color:** "Blue at the core", palette families in green, teal, cyan and blue ramps in 4 x 4 steps, grays, gradients, UI colour, accessibility and a downloadable .ase/.clr.
- **2x Grid:** divisions of two (2, 4, 8, 16, 32, 64 columns), applied to UI, video, 3-D architecture; a base unit; spatial relationships.
- **Typeface:** Plex (Sans, Mono, Serif, Math, Chinese SC/TC etc.), open-source licensed, type tester, feature and language support pages.
- **Logo:** the 8-bar IBM and the Eye-Bee-M rebus are shown white on #0430ad and #0f62fe.
- **Photography:** reportage, portraiture and still-life as three typed categories.
- **Voice:** declarative, human ("great observers").
- **Token decisions worth stealing:** 0.16 px tracking at 14 px; 0.07/0.11/0.15 s durations; a mono face for every spec number; each sub-area's own tint on a neutral frame; a download tile for every asset.

## 9. UX
Strong wayfinding: a persistent sidebar, ↳ index on every page, and "Next" band. Spec-heavy pages put values in mono. Weaknesses: body column is only about 660 px of a 1184 px canvas, leaving a blank right half; videos show a black or paused first frame in static capture; the sidebar background stops about 900 px down.

## 10. Craft signals
- All interactive transitions use the same four durations and curve.
- Body text 14/20 with +0.16 px tracking; captions 12/16 with +0.32 px.
- Tiles abut with 1 px dividers, not margins.
- Title band is a fixed 320 px on every page; the sidebar active bar is blue.
- Tinted hero per section (purple #e6d5ff on Accessibility).
- Spec values set in Plex Mono at a distinct size.

## 11. Reproduction recipe
```css
:root{--ink:#161616;--sub:#525252;--ground:#f4f4f4;--tile:#fff;--rule:#e0e0e0;--blue:#0f62fe;--blue-deep:#0430ad;
 --ease:cubic-bezier(.2,0,.38,.9);--font:"IBM Plex Sans",Helvetica Neue,Arial,sans-serif}
body{background:var(--ground);color:var(--ink);font:400 14px/20px var(--font);letter-spacing:.16px}
.topbar{height:48px;background:#161616;color:#fff}
.sidebar{width:256px;background:#fff;border-right:1px solid var(--rule)}
.sidebar a{font-weight:600;color:var(--sub);padding:6px 16px}
.sidebar a[aria-current]{background:#e0e0e0;box-shadow:inset 3px 0 var(--blue);color:var(--ink)}
.band{height:320px;background:#000;color:#fff;display:flex;align-items:flex-end;padding:0 128px 40px}
.band h1{font:300 67.5px/1.1 var(--font)}
.lead{font:400 21.9px/27.4px var(--font);max-width:660px}
.tile{background:#fff;border:1px solid var(--rule);aspect-ratio:2/1;padding:16px;transition:background .07s var(--ease)}
.mono{font:400 14px/20px "IBM Plex Mono",monospace;letter-spacing:.32px}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Restrained neutral frame with strongly coloured artwork tiles; consistent black band. |
| Originality | 6 | Carbon-style documentation is well known; the colour-ramp tile and rebus logo add character. |
| Usability | 9 | Persistent nav, hash index, per-asset download tiles, spec values in mono, good contrast. |
| Craft | 9 | Token-level consistency of durations, tracking and leading throughout. |

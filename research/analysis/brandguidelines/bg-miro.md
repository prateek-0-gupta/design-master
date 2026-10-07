---
id: bg-miro
source: brandguidelines
category: guideline
status: analyzed
title: "Miro Brand Guidelines 2025"
creator: "Miro (in-house)"
styles: [maximalist-color, playful-rounded, corporate-clean, flat-illustration, kinetic-type]
patterns: [full-bleed-yellow-chapter-hero, heavy-italic-uppercase-headings, dot-grid-canvas-background, left-nav-with-app-icon, downloadable-asset-rows, minimum-size-chip-demo, product-ui-as-graphic-element, cursor-pills-as-brand-device]
mode: light
palette: ["#ffdd33", "#1c1c1e", "#ffffff", "#6edb8c", "#ce70fc", "#57d2f7", "#47d1c4", "#ff6683", "#ff9c57", "#f0f0f0"]
type_families: ["Roobert PRO (Regular, Heavy Italic, Bold, Light; SS1 + SS4 enabled)", "Rubik (portal fallback)", "Satoshi Bold (chrome)"]
type_class: [geometric-sans, grotesk, variable]
radius_px: [3, 6, 10]
motion: {durations_s: [0.2, 0.3, 0.35, 0.55], easing: [ease, ease-in-out], loop: false}
scores: {aesthetics: 8, originality: 7, usability: 8, craft: 8}
craft_signals: [single-hero-yellow-with-two-neutrals, dot-and-line-grid-as-brand-texture, px-min-size-demo-60-200-400, 2-to-1-buffer-zone-rule, secondary-palette-with-hex-on-tile, ink-not-pure-black-1c1c1e, product-ui-screenshot-in-guidelines, ss1-ss4-opentype-sets-specified]
anti_patterns: [light-grey-nav-text-low-contrast, white-text-on-pastel-fails, body-text-grey-6c7173-at-17px, archived-snapshot-sticky-nav-repeats]
---
# Miro Brand Guidelines 2025 — Miro

## 1. Snapshot
- **Subject:** the live Miro brand kit (brandkit.miro.com), "Corporate Visual Identity" 2025 refresh. Sections: Introduction, The Miro logo, Colors, Typography, Illustrations, Product Branding, Photography, Shapes, Application + Co-Branding, Motion Design. `site_meta.json` shows the requested URL was `/corporate-visual-identity/the-miro-logo`; the capture is flagged `archived: true`, `captured_from` the site root, and the final URL is Product Branding. The sticky sidebar (logo plus nav) repeats in tall tiles at about y=900, which is a capture artefact. Photography, Shapes, Application and Motion Design tiles were not fully reviewed (d05/d06 are the only ones beyond Illustrations that I opened, d06 = Product Branding).
- **Why it's remarkable:** a guideline that is one colour. Every chapter opens on a 320 px field of #ffdd33 with a huge black heavy-italic caps title, so the brand is felt before any rule is read. It then explains the rules over a canvas-dot-grid, the same texture as Miro's product.

## 2. Composition & layout
- **Frame (1440 px):** a 240 px white sidebar with the app icon (76 px rounded tile) at x=35,y=40, then "Corporate Visual Identity" and 10 nav items at about 32 px pitch (14 px, #6c7173; active #1c1c1e). Content is 1200 px wide, with an inner column 305-1375 (1070 px).
- **Home hero:** a 794 px high yellow field with the lockup (icon + "miro") and "BRAND GUIDELINES" in two lines at about 140 px heavy italic, plus a lilac "2025" pill (#ce70fc, 94×36 px) at the lower right. Below, two text columns of 17 px body (about 520 px each) and a grey "NEXT / Corporate Visual Identity / The Miro logo" footer bar 96 px high.
- **Chapter hero:** a 324 px yellow field with a 120 px / 132 px title centred; Product Branding uses 456 px with a two-line title.
- **Split sections:** two columns, copy at x=305 (about 335 px wide) and demo panel at x=672-1375. Panels are #f0f0f0 with dot or line grid and a 6 px radius. Alternate sections use a full-width grey band with the heading on the left and the demo on the right.
- **Download rows:** a yellow field with white 1070×113 px rows (filename left at 22 px, download icon right), 20 px gaps.
- **Mobile 390 px:** a 60 px header with a hamburger and centred app icon, the yellow hero (273 px) with the lockup scaled to about 290 px, and 17 px grey body in one column at 15 px gutter.

## 3. Typography
Roobert PRO is the brand face. Census: Regular (most text), Heavy Italic (headings, weight 200 slot in CSS naming), Bold, Light. Sizes: 120 px / 132 px (hero), 70 px / 77 px (section H1 caps), 67 px / 73.7 px, 30 px, 22 px / 30.8 px, 18 px, 17 px / 20.4 px (body), 14 px / 22.4 px (nav), 12 px. Letter-spacing is `normal`, except 0.3 px on the Heavy Italic headings (7 samples).

| Role | Spec |
|---|---|
| Chapter title | Roobert PRO Heavy Italic, 120/132 px, uppercase |
| Section H1 | Heavy Italic, 70/77 px, uppercase, tracking 0.3 px |
| Body | Roobert PRO Regular 17/20.4 px (line-height 1.2) |
| Nav | 14/22.4 px, #6c7173 |
| Spec labels | 14 px, #1c1c1e |

The guide says Roobert Pro is "a tweaked sans serif" that runs from heavy commanding to light refined, and that Stylistic Sets 1 and 4 must be enabled (the specimen compares default and alternate "a" and "tt").

## 4. Colour
| Hex | Name (guide) | Role | Share |
|---|---|---|---|
| #ffdd33 | Miro Hero Yellow | master brand colour, hero fields | 29-42% of hero tiles |
| #1c1c1e | Breakthrough Black | text, logo | |
| #ffffff | Workspace White | page | 37-62% |
| #f0f0f0 | canvas grey | grid panels | 23-42% |
| #6edb8c | Dark Green | secondary | |
| #ce70fc | Purple-Pink | secondary, "2025" pill | |
| #57d2f7 | Blue | secondary | |
| #47d1c4 | Cyan | secondary | |
| #ff6683 | Red | secondary | |
| #ff9c57 | Orange | secondary | |
| #6c7173 | body grey | nav, body | |

Rules: yellow is dominant ("should always be prominent"); the secondaries align with the product design language "Miro Aura"; darker shades are used for outlines and emphasised text; the guide has chapters for Extended Color Tones, Outline Color Combination and an AI colour palette. Two textures are specified as colour assets, Canvas Dot Grid and Canvas Line Grid.

WCAG (contrast.py): #1c1c1e on #ffdd33 is **12.67:1**; on white **17.01:1**; on #6edb8c **9.86:1**; on #ce70fc **5.95:1**; on #57d2f7 **9.7:1**; on #ff6683 **6.06:1**. Body grey #6c7173 on white is **4.94:1** (just AA). The light grey #969aa6 (18 uses in Colors, for labels) on white is only **2.81:1**, a fail, and white on #ce70fc is **2.86:1**. The guide does well to put only black on pastels.

## 5. Depth & material
Mostly flat. One real shadow is in the census (0 4px 20px rgba(0,0,0,.45) on a floating control). The illustrations carry soft-3D depth: a glossy blue globe with a heart, a glass-like green chart card, a lock shield, an orange folder, all with subtle gradients, on yellow, white and grey-grid grounds. The app icon is a flat black chevron mark on yellow, radius about 20 px (26%).

## 6. Components & patterns
- Left nav with icon, collapsible group and caps-lock headings in the content.
- Minimum-size demo with yellow chips labelled 400 px, 200 px and 60 px above scaled lockups.
- Swatch tile 345×345 px (primary) and 256×262 px (secondary), 6 px radius, hex printed at the tile's bottom centre.
- Download rows (white on yellow) for 5 logo SVGs: white, black, whiteyellow, blacknegative, blackyellow.
- Product-as-graphic chapter shows a real Miro board (spin wheel, sticky pills, name cursors).
- Cursor pills: dark and light versions in each of five colours and an AI cursor pill with a sparkle.

## 7. Motion
CSS: `all .2s ease` and `opacity .2s ease` (hover, nav), `.3s ease-in-out` (page), `.35s ease-in-out` on `height` (accordion in Colors), `.55s ease-in-out` on margin (nav collapse), `.4s ease`. A Motion Design chapter exists but was not captured.

## 8. Brand system
- **Chapters:** Introduction; The Miro logo (Logo guidelines, Space and scale, Vertical logo, Full colour, One colour, Co-branding); Colors (Primary, Secondary, Extended tones, Outline combination, AI palette); Typography (Roobert Pro, Stylistic sets); Illustrations (system, on backgrounds, people, in visuals); Product Branding (Brand x Product, Cursors); Photography; Shapes; Application + Co-Branding; Motion Design.
- **Logo:** two elements, the Miro icon and the wordmark; the full lockup is preferred, the icon alone for tight spaces (app icons, avatars, slides). Described as the brand's "most sacred asset". Clearspace: the layout keeps a 2:1 ratio with a buffer zone of 2x minimum around the logo. Minimum size: **60 px** digital, **2 cm** print; demo at 400/200/60 px. Vertical lockup for specific cases. Five SVG variants offered.
- **Colour:** yellow dominates; black and white are the other primaries; six secondaries.
- **Illustration:** appropriate for blog, website, social, product and presentations; on yellow, grey-grid or white; at small sizes use off-white tones and a single secondary colour.
- **Voice:** "empowering and accessible, sophisticated yet warmly human"; the refresh is framed as human ingenuity amplified by AI.
- **Token decisions worth stealing:** a yellow chapter hero at a fixed 324 px; ink #1c1c1e instead of pure black; opentype stylistic sets as brand rules; hex printed on the tile; the grid texture as a brand asset; product screenshots as graphic elements.

## 9. UX
Good: persistent nav, "NEXT" bar, SVG download rows, hex in each swatch. Weak: nav and label greys (#6c7173, #969aa6) are low contrast, many sections are text-heavy at small size, and the long descriptions run centred paragraphs of 100+ characters.

## 10. Craft signals
- All chapter titles share one 324 px yellow band and one heavy-italic caps style.
- Primary palette is exactly three tiles with hex values; the secondary rule says black text only.
- Minimum size is shown at three real sizes with chips.
- Illustration grounds are demonstrated in three variants for each piece (yellow, white, grey grid).
- Dot and line grids are rendered as true 1 px patterns on #f0f0f0.
- Stylistic Sets named explicitly.

## 11. Reproduction recipe
```css
:root{--yellow:#ffdd33;--ink:#1c1c1e;--paper:#fff;--canvas:#f0f0f0;--grey:#6c7173;
 --green:#6edb8c;--purple:#ce70fc;--blue:#57d2f7;--cyan:#47d1c4;--red:#ff6683;--orange:#ff9c57}
body{font:400 17px/20.4px "Roobert PRO","Rubik",sans-serif;color:var(--ink)}
.hero{background:var(--yellow);min-height:324px;display:grid;place-items:center}
.hero h1,.h1{font:800 italic 70px/77px "Roobert PRO",sans-serif;text-transform:uppercase;letter-spacing:.3px;font-feature-settings:"ss01","ss04"}
.hero h1{font-size:120px;line-height:132px}
.canvas{background:var(--canvas) radial-gradient(#d0d0d0 1px,transparent 1.5px) 0 0/20px 20px;border-radius:6px}
.swatch{width:345px;aspect-ratio:1;border-radius:6px;display:flex;align-items:flex-end;justify-content:center;padding:12px;font-size:17px}
.download{background:#fff;height:113px;padding:0 54px;display:flex;justify-content:space-between;align-items:center;font-size:22px}
.nav a{font:400 14px/22.4px "Roobert PRO";color:var(--grey);transition:all .2s ease}
.nav a[aria-current]{color:var(--ink)}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Confident yellow and black with soft canvas grids and bright secondaries. |
| Originality | 7 | Using the product canvas texture and cursors as brand devices is distinctive. |
| Usability | 8 | Clear rules, real px minimums, hex per swatch, SVG downloads; some grey text is weak. |
| Craft | 8 | Consistent hero band, type style and token values; OpenType sets specified. |

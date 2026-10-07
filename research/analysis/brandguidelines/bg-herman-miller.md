---
id: bg-herman-miller
source: brandguidelines
category: guideline
status: analyzed
title: "Herman Miller — Identity guidelines (brandstandards)"
creator: "Herman Miller (in-house; part of MillerKnoll)"
styles: [minimal-swiss, swiss-grid-poster, photo-led, hairline-ui, corporate-clean]
patterns: [fixed-left-rail-numbered-toc, full-bleed-hero-per-chapter, three-column-hairline-spec-rows, numbered-subsection-index, archival-history-first, swatch-card-with-all-four-colour-specs, download-all-outline-button, red-footer-block]
mode: light
palette: ["#ee3a24", "#000000", "#f7f7f6", "#ffffff", "#c3c3c8", "#0050b4", "#ffb805", "#009b3c", "#4b2355"]
type_families: ["Söhne Buch / Kräftig / Halbfett + Kursiv (Klim, licensed)", "Inter (alternate, in the CSS for fallback use)"]
type_class: [neo-grotesk]
radius_px: [5, 300]
motion: {durations_s: [0.5], easing: [ease], loop: false}
scores: {aesthetics: 9, originality: 7, usability: 7, craft: 8}
craft_signals: [one-red-one-neutral-chrome, negative-tracking-on-37px-headings, 1px-black-hairlines-as-only-structure, history-before-rules, extended-palette-14-with-cmyk-rgb-hex-pms, per-section-sub-numbering, hero-image-doubles-as-chapter-mood, request-fonts-split-internal-external]
anti_patterns: [mobile-not-responsive, grey-captions-fail-aa, white-text-on-red-3-99, white-on-light-extended-colours-fail, 21-chapter-sidebar-always-open]
---
# Herman Miller — Identity guidelines — Herman Miller (in-house)

## 1. Snapshot
- **Subject:** brandstandards.hermanmiller.com, a 21-chapter, single-scroll-per-chapter identity site. Capture covers Introduction, 8 Accessibility, 9 Identity, 10 Color, 11 Typography, 12 Photography, 13 Illustration (the site_meta "final" URL is `/illustration`, the last subpage visited). Footer says ©2025 Herman Miller, Inc., part of the MillerKnoll collective.
- **Why it's remarkable:** It reads as a Swiss-style print spec rendered on the web. The page uses almost no chrome besides a Söhne grotesque, black hairlines, an off-white ground (#f7f7f6) and one red (#ee3a24). The brand's archive posters and photography carry all the colour, and every chapter starts with a history section before the rules.

## 2. Composition & layout
- **Fixed left rail (0–275 px):** white, with the M-bird "Herman Miller symbol" in red (≈75×70 px at x=40, y=40) and a 21-item numbered index in 14–15 px Söhne Buch, 21 px line pitch. The active chapter turns red. In the tile capture the rail repeats every 900 px because the screenshot tiles a fixed element; it is one sticky rail in the real page.
- **Content canvas (275–1440 px):** a hero image full-bleed to the right edge, 1165×577 px (≈2:1), with the chapter number "9" at x=335 and the title at x=865 in white or black 37 px type. The two baselines set the page's two-column system: a **label column at x=335** and a **content column starting x=865** (or x=512 inside spec rows).
- **Spec rows:** each subsection is a 1 px black hairline from x=335 to x=1380, then a label ("10.2 Core palette") in the left column and 4–5 columns of content (≈160 px wide, 28 px gutter) to its right, with an outlined "Download" button at x=1218–1380. Vertical rhythm is airy: 80–150 px between rows.
- **Index block:** each chapter opens with a "Contents" row listing its numbered subsections (for example 9.0 History to 9.25 Additional don'ts, 25 items in 5 columns), so one chapter is a mini-document.
- **Footer:** a full-width red #ee3a24 block (≈135 px) with a white symbol and two small text columns.
- **Mobile (390 px sheet):** not responsive. The whole desktop layout (rail plus canvas) is scaled down to roughly 285 px of canvas with ~6 px rail text; body copy becomes ~8 px. This is the weakest part of the site.

## 3. Typography
Census (home): **Söhne**: `font-sohne-buch` 400 and a hashed Söhne Kräftig 500 (57 nodes); (colour sub) Söhne Halbfett 600 and Buch Kursiv 400 italic for captions; Inter is also loaded on the Typography page (for the fallback demonstrations).
- **Scale (measured):** 43/43 px (chapter titles, tracking −0.89px), 37/37 px (index list and headings, tracking −0.91px, line-height 1.0), 23/25 px (lead paragraphs), 16/21 px (body), 12/16 px (spec data, 458 nodes on the Colour page) and 10/18 px (swatch captions). Headings use leading = size, set solid and tight; body is 1.31.
- **Tracking:** −0.91 px on 37 px (≈ −0.025em), −0.89 px on 43 px (≈ −0.02em), −0.46/−0.47 px on the 15.8 px alternate settings, and −1 px for 45 px type. Body is `normal`.
- **Weights in use (rule 11.2):** Söhne Buch, Buch Kursiv, Kräftig, Kräftig Kursiv, so just two weights (400/500) and their italics. The site obeys it: 400 ×529, 500 ×92 and almost no 600/700.
- **Page structure of the Typography chapter:** 11.0 History (Ultra Bodoni → Helvetica → Meta → Söhne), 11.1 Primary typeface (a giant "Söhne AaBbCc &?!.0123" specimen at ≈330 px cap height), 11.2 Weights, then Leading, Tracking, Hierarchy, Scale and proportion, Capitalization, Punctuation, Whitespace, Line length, Margins, Principles, Grids, Application, Alternates, Additional languages. "Request Fonts" for external partners; internal staff install from a self-service app.

## 4. Colour
| Hex | Role | Approx share |
|---|---|---|
| #ee3a24 (RGB 238/58/36, PMS 485 C) | Herman Miller Red: symbol, active nav, footer, red hero | ≈19% of tile 2; 20% of Accessibility tile 3 |
| #000000 | text, hairlines | 409+ text nodes |
| #f7f7f6 (Gray 01, PMS 663 C) | page ground | 64–93% of content tiles |
| #ffffff | rail, cards | rail 275 px |
| #c3c3c8 (Light Gray, PMS 428 C) | quiet swatch, hairline captions | — |
| #0050b4 Blue / #51a5e1 Light Blue | extended | 6 and 5 uses |
| #ffb805 Yellow, #eb7300 Orange, #009b3c Green, #912896 Purple | extended | — |
| #4b2355 Deep Purple, #7d001e Maroon, #7d4b28 Brown, #505a00 Dark Green, #dcb98c Tan, #eb5078 Pink, #f978cd Light Pink | extended | — |

The core palette is five swatches (White, Gray 01, Light Gray, Black, Red). The extended palette is **14 more** (the census shows `#41bd41` ×68 as a swatch-hover tint). Every swatch is a card (≈160×160 px) carrying **Name / CMYK / RGB / HEX / PMS** in 10–12 px type, the most complete colour spec of the five sites in this batch. Black has "PMS: Not specified". Section 10.4 splits digital and print values into two lists because they are built in different blend spaces. A neutral ground (#f7f7f6) with a hero strip of 14 vertical colour bars is the chapter's signature.

**WCAG (contrast.py)**
- Black on #f7f7f6: 19.59:1. Black on red: 5.27:1. **White on red #ee3a24: 3.99:1** (fails AA for the small footer text, passes large; the 37 px titles over the red are fine).
- Grey #97999b on #f7f7f6: 2.67:1 and #b2b2b8: 1.97:1 (both fail; these are the muted/inactive captions).
- White on extended colours: green #41bd41 2.45:1, pink #f978cd 2.44:1, light blue #51a5e1 2.69:1 (fail). Black on yellow #ffb805 12.11:1; white on blue #0050b4 7.48:1. The swatch captions therefore flip between black and white text per card, with the white ones failing on the light colours (the doc has a "10.13 Accessibility and contrast" section for this).

## 5. Depth & material
Entirely flat: `shadow: {}` and radii almost absent (5 px on the Download buttons, 300 px on 208 nodes in the colour page: the pill indicators). Depth and materiality come from the photography (top-down shot of a red lounge chair on grey with a hard cast shadow, wood-panelled study) and scanned archival print (Irving Harper ads, Armin Hofmann poster 1962, 1964 catalogue) that is reproduced with paper grain left in.

## 6. Components & patterns
- **Numbered rail index:** number in a 25 px column, name after; current chapter in red.
- **Download button:** white fill, 1 px red border, 5 px radius, black 16 px label, 162×40 px. "Download all" at chapter level, "Download" per swatch group.
- **Image row with caption:** 12 px italic Söhne Kursiv credit ("Ad by Irving Harper", "Poster by Armin Hofmann, 1962").
- **Accessibility chapter:** a hairline row per WCAG principle (1 Perceivable, 2 Operable, ...), with a 2×2 grid of guidelines each linked "WCAG Guideline 1.1 ↗".
- **Colour swatch card, large type specimen, logo history gallery** (with 5 white tiles for the logo constructions).

## 7. Motion
The only transition is `opacity 0.5s ease` (156 uses on the Typography page, 188 on Colour, so media and swatches fade in on scroll). Chapter 17 "Motion" and 18 "Video" exist in the TOC but were not captured. No hover transforms.

## 8. Brand system
**Logo (Chapter 9, 25 subsections):** History (the M was drawn by Irving Harper, "cheapest logo campaign in advertising history"), Elements overview, Logo, Logo construction, Symbol, Symbol construction, Wordmark, Wordmark construction, Bug symbol and construction, Scaling principles, Scaling in composition, Scaling with type, Scaling limitations, Horizontal and Vertical alignment, Clearspace, Placement, Using together, Placing together, Identity and color, Application, Use cases, Co-branding, Authorship, Additional don'ts. The M symbol is the "most significant visual identifier"; wordmark is lowercase "herman miller".

**Chapter order (21):** 1 Introduction · 2 What we believe · 3 Who we are · 4 What we do · 5 How we show up · 6 Communication · 7 Why we matter · 8 Accessibility · 9 Identity · 10 Color · 11 Typography · 12 Photography · 13 Illustration · 14 Graphic elements · 15 Infographics · 16 Composition · 17 Motion · 18 Video · 19 Applications · 20 In use · 21 Resources. Strategy chapters (2–7) precede the visual ones, and accessibility is placed before identity.

**Colour rules:** 10.5 Use proportion; 10.6/10.7 pairing with neutrals and with values; do's and don'ts; 10.10 colour families. Only listed values may be used in branded material. Red is both brand and UI: the page itself uses it only for the symbol, active state, footer and hero.

**Photography (12):** categories, use proportion, composition, cropping, art direction. Settings are lived-in homes and studios (a records-and-books study, a fireplace with Eames lounge) with natural, warm light and objects in context.

**Illustration (13):** archival work by Girard, Massey, Frykholm and Mitchell: flat cut-paper shapes, saturated palette, bold forms (black seeds on pink, an eye, layered fruit). Illustration is allowed "when photography can't be used" or a stronger point of view is needed.

**Voice:** plain, first person plural ("we have the power and responsibility"), humble about the guide itself ("Always use your best judgment").

## 9. UX
- Deep numbering (10.4, 11.13) makes any rule citable; each chapter's own contents row jumps to it.
- Download buttons at section level supply the assets right where the rule lives.
- Weaknesses: the mobile layout is broken (scaled desktop), the 21-item rail is always open, captions in light grey fail AA, and white text on the red banner at 3.99:1.

## 10. Craft signals
- Headlines carry −0.025em tracking and 1.0 leading at 37 and 43 px.
- All structure is 1 px black rules; no boxes or cards apart from swatches.
- Two-column x-grid (335 / 865 or 512) is held across every chapter.
- Each swatch states CMYK, RGB, HEX and PMS, with digital and print values split.
- Credits are given for each archival piece (designer and year).
- A single red accent is held across rail, footer and active links.

## 11. Reproduction recipe
```css
:root{
  --hm-red:#ee3a24; --hm-black:#000; --hm-gray-01:#f7f7f6; --hm-light-gray:#c3c3c8; --hm-white:#fff;
  --font:"Söhne","Helvetica Neue",Inter,Arial,sans-serif;
  --rail:275px; --col-label:335px; --col-body:865px;
}
body{background:var(--hm-gray-01);font:400 16px/21px var(--font);color:#000;margin-left:var(--rail)}
.rail{position:fixed;inset:0 auto 0 0;width:var(--rail);background:#fff;padding:40px;font:400 14px/21.5px var(--font)}
.rail a.active{color:var(--hm-red)}
h1,.toc-item{font:500 37px/37px var(--font);letter-spacing:-.025em}
.chapter-title{font:500 43px/43px var(--font);letter-spacing:-.02em}
.lead{font:400 23px/25px var(--font)}
.spec-row{border-top:1px solid #000;display:grid;grid-template-columns:177px repeat(4,1fr) 162px;column-gap:28px;padding:12px 0 60px}
.spec-label{font:500 14px/21px var(--font)}
.caption{font:italic 400 12px/16px var(--font)}
.btn{border:1px solid var(--hm-red);background:#fff;border-radius:5px;height:40px;width:162px;font:500 16px var(--font)}
.swatch{width:162px;height:162px;padding:16px;font:400 10px/16px var(--font)}
.fade{transition:opacity .5s ease}
footer{background:var(--hm-red);color:#fff;min-height:135px}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 9 | A refined Swiss framework: tight Söhne, hairlines, one red and a gallery of mid-century archive material. |
| Originality | 7 | History-first chapters and full-bleed chapter heroes are distinctive, though the grid is a known Swiss pattern. |
| Usability | 7 | Numbered, downloadable and complete specs; mobile broken and low-contrast captions hurt. |
| Craft | 8 | Consistent tracked headings, two-column grid, full CMYK/RGB/HEX/PMS cards; small contrast and responsive faults. |

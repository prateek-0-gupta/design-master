---
id: bg-night-embassy
source: brandguidelines
category: guideline
status: analyzed
title: "Night Embassy Identity Guidelines (Jagermeister)"
creator: "Jagermeister / Night Embassy (in-house)"
styles: [maximalist-color, photo-led, kinetic-type, corporate-clean, swiss-grid-poster]
patterns: [fixed-left-sidebar-nav, full-bleed-photo-hero-per-chapter, hairline-rule-section-heads, mono-captions, click-to-copy-swatch, always-live-single-source-guide, update-log, downloadable-asset-button-per-section, city-identifier-logo-suffix]
mode: light
palette: ["#dd5a12", "#f88c29", "#282526", "#f7f3ed", "#092d17", "#0d4734", "#17b717", "#ffffff"]
type_families: ["Meister Bold / Regular (custom Jagermeister face, per guide)", "Sohne Mono (captions, per CSS)", "Sohne (CSS alias)"]
type_class: [geometric-sans, mono, display]
radius_px: [2]
motion: {durations_s: [0.5], easing: [ease], loop: false}
scores: {aesthetics: 8, originality: 7, usability: 8, craft: 7}
craft_signals: [uppercase-bold-section-heads-with-tight-tracking, hairline-1px-section-dividers, mono-caption-system, click-to-copy-hex, cmyk-rgb-hex-pms-in-each-swatch, approved-logo-on-colour-matrix, update-log-with-dates, active-nav-item-in-brand-orange]
anti_patterns: [orange-body-links-fail-contrast, typo-in-nav-DOCUMNETS, sidebar-logo-repeats-in-stitched-capture, best-viewed-on-desktop-only]
---
# Night Embassy Identity Guidelines — Jagermeister Night Embassy

## 1. Snapshot
- **Subject:** a live identity guideline site for Jagermeister's Night Embassy music programme (identity.night-embassy.com). `site_meta.json` shows the root redirected to `/logo?e=...`; the capture covers Introduction, Logo, Colour, Typography, Photography and Motion (six subpages). The sidebar and logo repeat down the tile because of the sticky nav, which is a stitching artefact. The footer reads (c) 2024.
- **Why it's remarkable:** a night-life brand shown through full-bleed, grainy, red-and-orange photography, huge clipped orange type on charcoal, and a quiet cream page that carries the rules. The guide says it replaces "endless pdf versions" with a single live reference and logs every change with a date.

## 2. Composition & layout
- **Frame (1440 px):** a 240 px white left sidebar. It has the Gateway Icon (about 80 px, with a starburst of fine hairlines) at the top and 14 uppercase items at 35 px pitch (15 px bold). The active item turns orange (#f88c29). The content area is cream #f7f3ed with a 960 px column from x=360 to x=1320.
- **Chapter hero:** a full-bleed photo or type hero 520-600 px high with a 12 px white caps kicker "JAGERMEISTER NIGHT EMBASSY" at x=360, y=44 and the chapter title in 23-27 px bold white below. "IDENTITY GUIDELINES" is flush right.
- **Lead:** 23 px / 24 px statement across the full 960 px, starting about 90 px below the hero.
- **Sections:** each opens with a 1 px black rule across 960 px, a 27 px bold uppercase heading with tracking about -0.9 px, and a 17 px / 19 px paragraph. An orange (#dd5a12) 143×40 px "Download" or "Assets" button sits top-right of the section.
- **Quick links grid (home):** uneven tiles (368×300, 552×300, 470×300 x2, then four 225×250) with 15 px mono captions below. Row gaps about 60 px.
- **Footer:** a #17b717 green "NEXT >" band 138 px high, then an #f88c29 orange footer with a Contact button (143×40 px, #282526) and "Back to Top".
- **Mobile 390 px:** the sidebar shrinks to a 95 px column holding 13 items at tiny size (about 6 px caps) and the content column is only 280 px wide. The nav is not collapsed, so the layout is cramped. The site itself says it is "best viewed on desktop".

## 3. Typography
Census sizes: 14, 15, 16, 17, 23, 27, 68 and 78 px. Weights 400 and 700 only.

| Role | Spec |
|---|---|
| Display (Typography page) | 68 px / 58 px bold (line-height 0.85), tracking about -1.2 px; 78 px / 59 px, tracking -5.5 to -6.2 px |
| Section head | 27 px / 24 px bold uppercase, tracking -0.91 px |
| Lead | 23 px / 24 px regular |
| Body | 17 px / 19 px regular |
| Swatch data | 14 px / 15 px |
| Nav | 16 px / 16 px bold uppercase |
| Caption | 15 px / 17 px mono |

Meister is the brand face (Bold for headlines, CTAs and subheadings and "always bold and UPPERCASE"; Regular for body). The CSS names the loaded fonts only as hashed ids and "sohne"/"sohne mono", so the site's UI faces are the Meister-like geometric sans plus Sohne Mono for captions and the update log. Line-heights are very tight: 24 px at 27 px, 58 px at 68 px (0.85).

## 4. Colour
| Hex | Name (guide) | Role | Share |
|---|---|---|---|
| #f7f3ed | Off White (PMS 9045 U) | page ground | 31-71% |
| #ffffff | | sidebar | 14% |
| #282526 | Twilight (PMS 6 C U) | text, dark fields | 5-16% |
| #dd5a12 | NE Orange (PMS 7578 C) | buttons, links, type heroes | 9% |
| #f88c29 | bright orange | active nav, footer | 6-25% |
| #092d17 | Dark Green | secondary field | |
| #0d4734 | Herbal Green | secondary field | |
| #17b717 | bright green | "Next" band, accents | 6-12% |

The guide gives CMYK, RGB, HEX and PMS for each primary (e.g. NE Orange 0/59/92/13, 221/90/18, #DD5A12). Click-to-copy on swatches.

WCAG: #282526 on #f7f3ed is **13.74:1**. #f7f3ed on #092d17 is **13.58:1**. #282526 on #f88c29 is **6.35:1**. #282526 on #17b717 is **5.66:1**. But orange link text #dd5a12 on cream is only **3.43:1** and the white Download label on #dd5a12 is **3.79:1** (both fail AA for small text); #282526 on #dd5a12 is 4.01:1. Orange #f88c29 on cream is **2.17:1** and is used for the active nav text on white: a fail.

## 5. Depth & material
No shadows (census empty), radius 2 px at most. All depth comes from photography (red-lit faces, neon, bokeh) and from poster mock-ups (hoardings, billboards, a theatre door). Type is clipped by the frame edge to make a texture (orange on charcoal, "OF THE ..." cropped).

## 6. Components & patterns
- Sidebar nav with brand orange as the active state.
- Section head with rule, a descriptive paragraph and an orange download button.
- Colour-on-logo matrix: icon in black and white on cream, charcoal, orange, dark green, herbal green, bright green, orange (pairs of 470×265 px cells).
- Swatch bars 960×200 px holding name, CMYK, RGB, HEX, PMS in 14 px.
- Typeface specimen: label left (mono), 68 px specimen right.
- Photo category grid with mono captions (Studio Portraits, Raw Portraits, etc.).
- Timeline diagram for motion: Intro, Main and Outro sections with chip tracks.
- Update log: date (DD-MM-YYYY) left and entry right, in mono, 27 px row pitch, 16 entries from 14-05-2024 to 28-09-2026.

## 7. Motion
CSS has only `opacity 0.5s ease`, which fades images and nav in. The Motion chapter itself prescribes content: long-form video (+20 s) has a clean first frame that makes an iconic thumbnail, then at least 10 frames before a logo animation, then an Outro with the Wordmark and the Jagermeister seal. Logo animations run only on Twilight or Off White. Short social loops are in the Social media chapter.

## 8. Brand system
- **Chapters in order:** Introduction, Logo, Colour, Typography, Photography, Design System, Motion, Social Media, Website, Posters & Billboards, Documents (spelled "Documnets" in the menu), Partnerships, Resources.
- **Logo:** two primary logos, the Gateway Icon with a city identifier ("G" for Global) and the Wordmark with identifier (the wordmark sets its "M" as the icon). Variants add the Jagermeister Gold Seal in off white and twilight black. A "city identifier" suffix is swapped per city (Madrid, Paris, Warsaw appear in the log). Construction diagram uses a thin circle with a labelled "Jagermeister Identifier". "On colour" shows approved combinations only.
- **Colour:** four new colours borrowed from the Jagermeister BVI were added to the primary palette.
- **Type:** Meister is compulsory except for markets with special characters; Bold is UPPERCASE for headlines, CTAs and subheadings; Regular for body.
- **Photography:** categories (studio portraits, raw portraits, performance, city night), plus a note to avoid centring the subject because the centre is reserved for the icon or wordmark.
- **Voice:** direct and inclusive ("genuinely magical moments").
- **Governance:** "no endless pdf versions"; templates need Illustrator, After Effects, InDesign and Creative Cloud; downloads need permission from the Jagermeister contact.
- **Token decisions worth stealing:** the centre-safe photography rule; an update log; one uppercase-bold voice for all headings; a CMYK/RGB/HEX/PMS block in every swatch.

## 9. UX
Fast to scan: persistent sidebar, a download button in every section, click-to-copy hex. Weaknesses: orange links and buttons fail AA; the active nav orange is low-contrast on white; mobile is not truly responsive; the nav has a typo.

## 10. Craft signals
- 1 px rules separate every section on the same 960 px column.
- Headline tracking is negative and increases with size (-0.9 px at 27 px, about -5.5 px at 78 px).
- Every swatch lists four colour systems.
- Captions in mono create a clear second voice.
- Logo matrix includes both black and white marks on every approved ground.
- A dated update log is on the home page.

## 11. Reproduction recipe
```css
:root{--orange:#dd5a12;--amber:#f88c29;--ink:#282526;--paper:#f7f3ed;--forest:#092d17;--herbal:#0d4734;--lime:#17b717}
body{background:var(--paper);color:var(--ink);font:400 17px/19px "Meister","Montserrat",sans-serif}
.side{position:fixed;width:240px;background:#fff;padding:20px}
.side a{font:700 15px/17px "Meister",sans-serif;text-transform:uppercase;display:block;padding:9px 0}
.side a.active{color:var(--amber)}
.section{border-top:1px solid #000;padding-top:16px}
.section h2{font:700 27px/24px "Meister",sans-serif;text-transform:uppercase;letter-spacing:-.91px}
.lead{font:400 23px/24px "Meister",sans-serif}
.cap{font:400 15px/17px "Sohne Mono",ui-monospace,monospace}
.btn{background:var(--orange);color:#fff;font:700 14px/1 "Meister",sans-serif;padding:13px 0;width:143px;text-align:center;border-radius:2px}
.next{background:var(--lime);height:138px;font:700 27px "Meister";text-transform:uppercase}
img{transition:opacity .5s ease}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Saturated red/orange photography and cropped type against calm cream. |
| Originality | 7 | Gateway icon with city identifier and photo rule about the centre are distinctive. |
| Usability | 8 | Live source of truth, change log, per-section downloads; weak AA on orange, poor mobile. |
| Craft | 7 | Consistent rules, tracking and swatch data; small typos and contrast misses. |

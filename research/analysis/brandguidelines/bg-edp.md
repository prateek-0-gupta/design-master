---
id: bg-edp
source: brandguidelines
category: guideline
status: analyzed
title: "EDP"
creator: "Pentagram"
styles: [maximalist-color, dark-premium, photo-led, corporate-clean]
patterns: [spiral-supergraphic-crop, logo-lockup-grid-units, blend-mode-image-overlay, accessible-text-on-colour-matrix, locale-number-formatting-rules, script-fallback-type-system, section-divider-flat-colour, file-naming-convention]
mode: dark
palette: ["#212E3E", "#28FF52", "#6D32FF", "#263CC8", "#0CD3F8", "#143F47", "#225E66", "#7C9599"]
type_families: ["FT Base (Light/Book/Regular/Medium/Semibold + italics, custom FTBaseEDP cut)", "Mulish (fallback Latin-extended/Cyrillic/Greek/Vietnamese)", "Noto Sans JP/SC/KR/Thai/Khmer/Tamil", "Arial (system fallback)"]
type_class: [neo-grotesk, geometric-sans]
radius_px: []
motion: {durations_s: [5, 3], easing: [], loop: false}
scores: {aesthetics: 9, originality: 7, usability: 9, craft: 9}
craft_signals: [margins-as-fraction-of-height, logo-size-in-grid-columns, spiral-55-percent-visible-rule, background-brightness-55-percent-logo-switch, blend-mode-recipes-per-output, pantone-ral-ncs-vinyl-codes-per-colour, tabular-figures-page, per-script-fallback-specimens]
anti_patterns: [electric-green-on-violet-below-aa, white-on-slate-grey-below-aa, unit-typo-mwh]
---
# EDP — Pentagram

## 1. Snapshot
- **Subject:** A 133-page, 1920×1080 pt landscape brand book (June 2022) for EDP, the Portuguese energy utility. The identity pairs a gradient spiral mark with a lowercase "edp" wordmark, an electric green/violet/ice-blue palette on a near-black Marine Blue, and FT Base throughout.
- **Why it's remarkable:** The spiral is controlled with numbers rather than adjectives. At least 55% of it must stay visible in a crop. Logo margins are height/40 and height/25. Lockup width is counted in grid columns. Photo overlays come with blend-mode and opacity recipes for RGB, Pantone and CMYK.

## 2. Composition & layout
- **Page system:** Pages are 1920×1080 pt (rendered at 1400×788 px). Every content page has a fixed left rail about 290 px wide at 1400 px (≈21%). The rail holds a two-line header: the chapter name in Electric Green (#28FF52, ~20 px) over the page title in white Light (~28 px). Below it sits 12–13 px explanatory copy. The right ~75% holds specimens inside 1 px slate hairline frames (e.g. the Minimum size / Clearance / Co-branding panels on p30). The footer reads "EDP · Brand Guidelines · June 2022" bottom-left, with the folio bottom-right at about y=762.
- **Dividers:** Each chapter opens with a full-bleed flat colour and a huge Light title of about 110 px at 1400 width ("Our logo" on green p26, "Colour" on ice blue p40, "Typography" on slate p63, "Imagery and Graphics" on cobalt p80). This gives a colour rhythm through the book.
- **Layout grid (p47–48):** Grids are "in multiples of 6": ISO A and square use 12 columns, Landscape HD 24, website/4:3 18, and tall display 6. Margins are top/bottom = height/40 and left/right = height/25. The lockup spans 4 columns in portrait and 5 in landscape. The standalone wordmark spans 2.5 and 3 columns.

## 3. Typography
- **Typeface:** **FT Base**, confirmed by pdffonts: FTBase Light, Book, Regular, Medium and Semibold, each with italics, plus a dedicated **FTBaseEDP-Book** cut. The specimen on p64 lists the 10 styles from Light to Semibold Italic.
- **Hierarchy (p65), stated as ratios:**
  - Title: Light, "at least 4× body size", 110% leading, 0 tracking.
  - Subheading: Semibold at 100% of body size, 120% leading.
  - Body: Book, 120% leading.
  - Caption: Book at 50% of body size, 140% leading.
  - The governing rule is "the larger the text the lighter it should be". Everything is set in sentence case, and ligatures are switched off.
- **Measured:** The display "Changing tomorrow now" is about 130 px at 1400 width (~178 pt on the 1920 page), and body is about 22 px. The ratio is ≈5.9×, which satisfies the 4× minimum.
- **Tabular figures (p66):** a dedicated page shows proportional and tabular figures side by side in financial tables.
- **Fallbacks (p67–79):**
  - Arial for email and Office.
  - **Mulish** for Polish, Czech, Greek, Cyrillic and Vietnamese.
  - **Noto Sans** JP, SC, KR, Khmer, Thai and Tamil. Each has its own specimen page with the tagline translated.
  - A weight-mapping table (p79) aligns FT Base Light/Book/Regular to the equivalent weight in each fallback. Manrope also appears embedded.
- **Class:** a neo-grotesk with geometric round bowls (the "e", "d" and "p" of the wordmark echo it).

## 4. Colour
Values are taken from the palette page (p42) and cross-checked against palette.json (p002 #29ff52 at 89%, p003 #212e3e at 89%, p005 #6d32ff at 96%, p008 #0bd3f7).

| Hex | Role | Approx share |
|---|---|---|
| #212E3E Marine Blue | preferred background, all body pages | ~55% |
| #28FF52 Electric Green | preferred highlight, chapter headers, stat tiles | ~12% |
| #6D32FF Violet Purple | highlight, dividers, spiral outer arc | ~6% |
| #263CC8 Cobalt Blue | highlight, divider | ~3% |
| #0CD3F8 Ice Blue | highlight, spiral core | ~4% |
| #143F47 Spruce Green / #225E66 Seaweed Green | muted natural backgrounds | ~6% |
| #7C9599 Slate Grey | muted background (illustration, motion pages) | ~8% |
| #3B4B5D | wordmark-only colour, explicitly outside the palette | <1% |

- Every colour is specified as RGB, HEX, CMYK, PMS coated/uncoated, RAL, NCS and 3M/Oracal vinyl numbers, which makes it signage-ready.
- **Web palette (p45):** each colour gets three tints (e.g. #6D32FF → #8351FF → #A784FF → #C5ADFF). It also adds warning colours outside the brand palette: Red #E32C2C / #EDD5D3 and Yellow #F2FF00 / #FFFFA2.

WCAG (contrast.py):
- White on #212E3E: **13.77:1**.
- #28FF52 on #212E3E: **10.17:1**.
- #0CD3F8 on #212E3E: 7.66:1.
- Black on #28FF52: 15.52:1.
- White on #6D32FF: 5.91:1.
- White on #263CC8: 8.19:1.
- #28FF52 on #263CC8: 6.05:1.
- **#28FF52 on #6D32FF: 4.37:1** (large text only). The book allows it for headlines on p43.
- **White on Slate #7C9599: 3.17:1.** This is large-text only, yet it is used for 12 px rail copy on p86–88 and p93.
- #225E66 on #0CD3F8: 4.09:1.

The text-on-colour page (p43) explicitly claims AA large (3:1) for headlines and "designer's discretion" for impact sizes. That is honest, but the body-size pairings on slate do not meet it.

## 5. Depth & material
- The pages themselves are flat, with no shadows and no radii.
- Depth lives only in the spiral, a ribbon with a hue gradient (violet → cobalt → ice → green) that overlaps itself like a coiled band.
- The image-overlay recipe (p59) creates luminous transparency:
  - **Digital:** spiral on Lighten at 40–60%, then Hard Light at 90–100%.
  - **Pantone print:** white spiral on Normal at 75%, blue on Multiply at 100%, then PMS green and purple on Normal.
  - **CMYK:** Colour Dodge at 100%, then Multiply at 80%.
- Applications (p100–131) use photoreal mockups for signage, a van, a hard hat and a debossed metal block.

## 6. Components & patterns
- Stat tiles: flat Electric Green rectangles with Light numerals (">50 GW", "100%") and a one-line label (p20).
- Icon set: 1.5 px line icons on a round-ended stroke, which can sit inside filled circles in palette colours (p89–90).
- Illustration: black outline figures with one flat highlight colour per illustration (green, violet, ice), built from three layers (highlight, optional person fill, outline). The book credits the illustrator as Nata Schepy (p86).
- Infographics: huge Light percentages in green and ice circles sized by value (p91, p127).
- Do/don't rows use a red circled-X icon with one-line captions.

## 7. Motion
The single motion page (p93) shows four storyboard frames: an arc drawing on, the spiral completing, the wordmark fading in from #3B4B5D-like grey to white, and the final lockup. The rules: the spiral may rotate, draw on and cycle colour, but must never be "broken" or distorted. The sonic logo exists in **5 s and 3 s** versions with fixed timing. No easing values are given.

## 8. Brand system
**Logo rules:**
- **Master logo:** spiral plus lowercase wordmark. The spiral reads as nature's circularity, turbines and the planet.
- **Minimum size:** regular 50 px / 14 mm. Below that a simplified "small size" logo is used, down to 25 px / 6 mm. The vertical logo's minimum is 85 px / 22 mm.
- **Clearance:** the spiral's x-height (marked X) on all sides. The wordmark alone gets the x-height of its "e" (shown as 1.5x on p36).
- **Co-branding:** the gap between logos is at least the spiral height, with partner logos centre-aligned (shown with NOS and Porto).
- **Variants:** tagline lockup, about 16 sector descriptor logos (Renewables, Innovation, Sãvida, etc., with the descriptor optically right of the spiral), vertical, standalone spiral, wordmark, greyscale (for black and white grounds) and a single-colour spiral.
- **Background switching (p57):** a background darker than 55% brightness takes the light-colour logo. "The darkest part of the spiral must not be darker than the background." On clashing brights (green, violet), a transparent greyscale logo is used.
- **Misuse (p39):** 9 don'ts, including no recolouring, no rotation, no outlined spiral and no translated descriptors.

**Graphic device:**
- The spiral is cropped as a supergraphic. At least **55%** of it must stay visible, and it must not be framed, left with odd gaps, used too small or cropped too much (p52).
- Messaging on the spiral must not cross its counters (p62).
- A centre crop with the wordmark is reserved for hero moments (p61).
- Web banners (300×250, 160×600, 300×50, etc.) get bespoke rules (p55).

**Voice:**
- Six voice attributes, each with a short definition: Language, Openness, Conscience, Proximity, Knowledge, Pragmatism (p21).
- Mechanical rules (p22–25):
  - PT vs EN thousand and decimal separators (1.362 vs 1,362).
  - Mixed numeral-word for large numbers ("16 million").
  - A space before units.
  - Currency symbol placement per currency.
  - Date and time formats (09h30 in PT).
  - "EDP" always in capitals in text, never the lowercase wordmark.
  - The tagline in sentence case.

**Imagery:** natural, candid photography in five buckets: Nature, People, Electricity, Technology, Staff (p81–85). It is colour-true, with no filters.

**Document structure (from the contents page and the dividers):**
1. Cover (p1)
2. Introduction / Why change (p2–4)
3. Our strategy: vision, purpose, people narrative, principles, brand strategy, architecture, tagline, commitments (p5–20)
4. Tone of voice: numbers, currency, time, writing (p21–25)
5. Our logo (p26–39)
6. Colour: palette, text on colour, web colour (p40–45)
7. Composition: margins, grid, graphic crops, wordmark and spiral, messaging, exceptional use, spiral and logo on colour or image, centre crop, misuse (p46–62)
8. Typography: typeface, hierarchy, tabular figures, fallback, world languages, overview (p63–79)
9. Imagery and graphics: nature, people, electricity, technology, staff, illustration, iconography, infographics (p80–91)
10. Motion and sound (p92–94)
11. Brand in use: campaign, OOH, signage, products, print, stationery, fleet, digital, presentation, video-call backgrounds (p95–131)
12. File naming (p132)
13. Back cover (p133)

**Token decisions worth stealing:**
- Margins expressed as fractions of format height (Y/40, Y/25).
- Logo width counted in grid columns.
- A 55% brightness threshold for switching logo versions.
- A tint ladder of exactly three steps per colour, for web only.
- A file-naming grammar: `EDP_Group_MasterLogo_RGB_Light_NEG_600px.png` = entity_division_asset_colourspace_variant_polarity_size (p132).

## 9. UX
For a designer this is close to exemplary. Every rule pairs a specimen with a number, the contents page has page numbers, and the left-rail header always says chapter › topic. Localisation (number and date formats and 9 script systems) is handled better than in most global brand books. Two weak points:
- Several rail paragraphs are set at about 12 px in white on slate (3.17:1).
- Some specimen labels in the logo pages are about 8 px at 1400 px wide and are hard to read on screen.

## 10. Craft signals
- Margins = Y/40 (top/bottom) and Y/25 (sides), drawn with green dimension marks on p47.
- Grid column counts are all multiples of 6 (6/12/18/24) across five formats.
- The wordmark colour #3B4B5D is quarantined from the palette and labelled "Wordmark only".
- Each of the 9 colours has 8 specification systems, from RGB to Oracal vinyl.
- The type hierarchy is specified as ratios of body (≥4×, 100%, 50%) rather than fixed pt.
- Blend-mode recipes are given per output (RGB/Pantone/CMYK) with exact opacities.
- Fallback specimens set the same tagline in 12 languages.

## 11. Reproduction recipe
```css
:root{
  --marine:#212E3E; --spruce:#143F47; --seaweed:#225E66; --slate:#7C9599;
  --green:#28FF52; --violet:#6D32FF; --cobalt:#263CC8; --ice:#0CD3F8; --white:#fff;
  --violet-2:#8351FF; --violet-3:#A784FF; --violet-4:#C5ADFF; /* web tints */
  --font:"FT Base","Mulish",Arial,sans-serif;
  --body:22px; --title:calc(var(--body)*4); --caption:calc(var(--body)*.5);
}
body{background:var(--marine);color:var(--white);font:400 var(--body)/1.2 var(--font);font-variant-ligatures:none}
h1{font-weight:300;font-size:var(--title);line-height:1.1;letter-spacing:0}
h3{font-weight:600;font-size:var(--body);line-height:1.2}
.caption{font-size:var(--caption);line-height:1.4;color:var(--green)}
.page{aspect-ratio:16/9;padding:calc(100% * 9/16 / 40) calc(100% * 9/16 / 25)} /* Y/40, Y/25 */
.rail-kicker{color:var(--green)} .rail-title{font-weight:300}
.spiral{background:conic-gradient(from 200deg,var(--violet),var(--cobalt),var(--ice),var(--green),var(--violet));
  -webkit-mask:radial-gradient(circle,transparent 38%,#000 39% 52%,transparent 53%);}
.on-photo .spiral{mix-blend-mode:hard-light;opacity:.95}
.stat{background:var(--green);color:#000;font-weight:300;font-size:64px}
.num{font-variant-numeric:tabular-nums}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 9 | The acid green and violet on deep marine is striking, and the spiral crops over photography are cinematic and coherent from cover to fleet. |
| Originality | 7 | A gradient ring/spiral mark is a known energy-sector trope. The value comes from the execution and the crop system, not the concept. |
| Usability | 9 | Numeric rules for nearly everything: margins, columns, minimum sizes, brightness thresholds, blend recipes, locale formatting, file names. |
| Craft | 9 | Consistent rail layout, exhaustive colour specs and fallback-script coverage. Minor slips: "Mwh" casing, a few sub-AA small-text pairings on slate. |

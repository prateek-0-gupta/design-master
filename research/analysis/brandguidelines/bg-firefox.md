---
id: bg-firefox
source: brandguidelines
category: guideline
status: analyzed
title: "Firefox Brand (mozilla.design/firefox)"
creator: "Mozilla (in-house)"
styles: [dark-premium, gradient-mesh, maximalist-color, corporate-clean]
patterns: [numbered-chapter-openers, deep-purple-ground, giant-trait-words, like-this-not-this-voice-table, logo-clearspace-by-letter-F, accessibility-contrast-grid, ten-step-colour-ramps, brand-platform-hierarchy, sticky-quick-links-nav]
mode: dark
palette: ["#21123b", "#ff4f5e", "#e41587", "#9059ff", "#ff7139", "#ffd567", "#b833e1", "#ffffff"]
type_families: ["Metropolis Bold (headings)", "Inter Regular (body)", "Zilla Slab (Mozilla parent, loaded not used on page)", "Sharp Sans Medium (product-logo modifier, per doc)"]
type_class: [geometric-sans, neo-grotesk]
radius_px: [3, 5]
motion: {durations_s: [0.5, 0.3, 0.4], easing: ["cubic-bezier(0.07,0.95,0,1)", ease, ease-in-out], loop: false}
scores: {aesthetics: 8, originality: 6, usability: 8, craft: 7}
craft_signals: [numbered-chapters-with-colour-coded-subtitles, clearspace-defined-by-F-height, ten-step-ramps-six-hues, in-page-aaa-fails-table, like-this-not-this-pairs, exponential-ease-out-hover]
anti_patterns: [purple-trait-words-below-aa-for-body, generous-empty-vertical-space, brand-centre-login-walled, long-single-page-scroll]
---
# Firefox Brand (mozilla.design/firefox) — Mozilla

## 1. Snapshot
- **Subject:** Mozilla's public Firefox brand microsite on mozilla.design. **Wayback Machine snapshot dated 2026-01-01 07:57:59** (`captured_from`). The live site now points to a newer Mozilla brand center, so this is the legacy Firefox guideline.
- **Coverage (explicit):** home page scroll-height 38,544 px captured in 15 desktop tiles (1440 px wide); I viewed 8 of 15 (t01, t03, t05, t07, t09, t11, t13, t15) plus mobile sheet 1 of 5. Between viewed tiles about 7 tiles (pp. 02, 04, 06, 08, 10, 12, 14 of the scroll) were not viewed, so parts of Visuals and Typography, and the exact type-scale values shown on the page, are not described here except from the census. Two extra capture "subpages" (d01, d02) turned out to be the newer Mozilla brand centre (brand.mozilla.com home - dark nav with Start Here / Voice & Message / Visual Elements and libraries; and its login page, `?referer=/foundation/`). They show the successor is login-walled; they are not Firefox guideline content.
- **Why it's remarkable:** A six-chapter dark-mode guideline whose own palette appears as ten-step ramps in six hues, with built-in accessibility results and a clearspace rule defined by the F in the wordmark.

## 2. Composition & layout
- Black 70 px header bar (site name "mozilla dot design", Firefox Brand, Mozilla Brand, Quick Links dropdown).
- Hero (y 70-1050): diagonal pink/orange/red gradient "flame" shapes over deep purple #21123b; "Firefox brand" in Metropolis Bold, ~200 px (line-height 168), semi-transparent white; chapter list at right (01 About, 02 Personality, 03 Logos & Usage, 04 Color, 05 Visuals, 06 Typography), 32 px.
- Chapters open the same way: grey two-digit number (≈64 px), white chapter name, then a colour-coded subtitle (About: violet #9059ff; Personality: yellow #ffd567; Logos: coral #ff4f5e; Visuals: orange #ff7139).
- Body: left-aligned at x=40; 18-24 px lines at 28 px leading, ~750 px measure; sub-sections indent to x≈472 for definitions (Brand Promise, Consumer Takeaway). 120 px+ vertical gaps between blocks.
- Mobile 390 px: single column, same dark ground, headings at ~36 px, hero shapes crop to the top 400 px.

## 3. Typography
- **Metropolis Bold** for all headings: 200/168, 150, 120, 64/72 (19 uses), 56/64, 48/56, 40/44, 32/36 (19), 24/28, 20/24, 16/20. **Inter Regular** for body: 18/28 (34), 16/24 (59), 14/22, 12/24 (82), 12/18.
- Weights are always "400" (weight is in the font file names). Tracking normal; no uppercase except two lowercase runs. Scale ratio is about 2× at the top (64 → 32), 1.33 inside body.
- Zilla Slab (Mozilla) is loaded in CSS but not used on this page; the page states product logo modifiers use Sharp Sans Medium.

## 4. Colour
| hex | role | approx share |
|---|---|---|
| #21123b | page ground (deep purple) | 92% of text tiles |
| #ff4f5e | coral: subtitles, logo chapter | in gradient 15% of t01 |
| #e41587 | magenta in hero | 13% of t01 |
| #9059ff | violet: About subtitle, "Radical" | accents |
| #b833e1 | orchid: "Kind" | accents |
| #ff7139 | orange: "Opinionated", Visuals | accents |
| #ffd567 | yellow: Personality | accents |
| #ffffff | text | all copy |
| #ededed (census bg) | light panels for logo tiles | panels |

- Ramps: ten steps each for violet, orchid, pink, red, orange, yellow, plus greens and blues, cyan-to-navy (the CSS bg list shows #e3fff3 → #083f37 for green and #acf1ff → #0a214d for blue), and three gradient chips (violet, blue-to-violet, red-to-orange).
- Contrast (contrast.py, on #21123b): white **17.29:1**; yellow #ffd567 **12.32:1**; orange #ff7139 **6.32:1**; coral #ff4f5e **5.38:1**; violet #9059ff **4.17:1** (large only); orchid #b833e1 **3.79:1** (large only). Violet and orchid headings are used large, so they pass AA-large only.
- The Accessibility block lists each swatch hex with an AAA/Fails label (e.g. #E3FFF3 AAA vs "Fails" on the other background).

## 5. Depth & material
- Flat with large gradient shapes. No shadows in census. Radii: 3 px (162 uses, swatches/chips/logo tiles) and 5 px. Logo tiles are light grey #ededed cards on the dark ground.

## 6. Components & patterns
- Numbered chapter opener; definition pairs (title + one line); like-this/not-this two-column voice examples with a bracketed reason; logo downloads as grey tiles with a download icon; ✓/✗ grid on a gradient strip showing 11 logo placements; swatch ramps; accessibility pair table.

## 7. Motion
- Census: `background .5s cubic-bezier(0.07,0.95,0,1)` (10 uses; swatch/hover), `transform .5s` with the same curve, `opacity .3s ease`, `all .4s ease-in-out`. The curve is a strong ease-out (starts almost instantly, settles over ~0.5 s). Mobile hero shows an animated scroll arrow. No dedicated Motion chapter was seen in the viewed tiles.

## 8. Brand system
- **Platform (01):** Positioning (dual purpose: better online life and a better internet), Purpose (people believe Firefox has their best interests at heart), Promise "Firefox fights for you", Takeaway "Firefox is on your side". Audience: Conscious Chooser, segments Adventurous Amplifiers and Caring Confidentials.
- **Personality (02):** four traits Opinionated, Open, Radical, Kind, each shown as a 150 px word in its own colour. Voice: four writing rules, with like-this/not-this pairs (e.g. warm and brief vs too chummy).
- **Logos & usage (03):** Parent brand logo = icon + wordmark lockup; browser logos (Browser, Developer Edition, Nightly, Beta, Reality, logomark). Clearspace: uppercase F of the wordmark = 40% of mark height as the margin; gap between mark and logotype = 20% of mark height. Full-colour logo only on very light or very dark backgrounds; strip of 11 placements shows which gradient positions fail (5 of 11 crossed). Product logos share the parent geometry; the modifying word is set in Sharp Sans Medium; "don't create your own colourway".
- **Color (04), Visuals (05), Typography (06):** palette ramps and gradients, accessibility pairs, a shape system derived from product-logo geometry ("background patterns, spot illustrations, motion graphics and pictograms"), and a type scale. Details of Visuals and Typography were only partly viewed.
- Minimum logo sizes were not seen in the viewed tiles.

## 9. UX
- A single long scroll with a sticky chapter list; the numbers and colour-coded subtitles make it scannable. The page is text-heavy on dark with large empty gaps; violet body-adjacent headings sit close to AA limits. The successor site is login-walled.

## 10. Craft signals
- Colour-coded subtitle per chapter, each ≥5.3:1 on the ground except violet (large).
- Clearspace given as multiples of a glyph in the logo itself (the F).
- Six-hue ramps with ten steps plus three official gradients.
- Strong ease-out curve `cubic-bezier(.07,.95,0,1)` applied consistently.

## 11. Reproduction recipe
```css
:root{--ground:#21123b;--coral:#ff4f5e;--magenta:#e41587;--violet:#9059ff;--orchid:#b833e1;--orange:#ff7139;--yellow:#ffd567}
body{background:var(--ground);color:#fff;font:400 16px/24px Inter,sans-serif}
h1,h2,h3{font-family:Metropolis,sans-serif;font-weight:700}
h1{font-size:64px;line-height:72px} h2{font-size:32px;line-height:36px}
.chapter-num{color:#cdcdd4;font-size:64px}
.chapter-sub{color:var(--violet)}
.swatch{border-radius:3px;transition:background .5s cubic-bezier(.07,.95,0,1)}
.hero{background:linear-gradient(135deg,#ff7139,#ff4f5e 40%,#e41587 70%,#21123b)}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Bold gradient hero and rich colour on deep purple; strong chapter rhythm. |
| Originality | 6 | Well-executed dark brand-site format; F-based clearspace and AAA table are nice touches. |
| Usability | 8 | Concrete rules, downloads, accessibility results, clear chapters. |
| Craft | 7 | Consistent tokens and ramps; sparse layout and tight contrast on violet. |

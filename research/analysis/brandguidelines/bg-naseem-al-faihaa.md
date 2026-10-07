---
id: bg-naseem-al-faihaa
source: brandguidelines
category: guideline
status: analyzed
title: "Naseem Al-Faihaa Brand Guidelines v1.0"
creator: "In-house"
styles: [corporate-clean, minimal-swiss]
patterns: [bilingual-mirrored-columns, symbol-derived-pattern, heritage-seal, tint-ramp-swatches, approved-vs-rejected-colour-grid, co-brand-percentage-scaling, download-link-per-chapter, mockup-application-showcase]
mode: light
palette: ["#78be43", "#1e4489", "#111921", "#bcbdc0", "#ffffff", "#f64740", "#f2af29", "#00a1e4"]
type_families: ["Factoria Demi (embedded)", "Acumin Pro Regular/Bold (embedded)", "Lama Sans Regular/Bold (embedded, Arabic)"]
type_class: [slab, humanist-sans, geometric-sans]
radius_px: []
motion: null
scores: {aesthetics: 6, originality: 5, usability: 6, craft: 5}
craft_signals: [english-arabic-parallel-text, symbol-built-from-letter-f, tint-steps-under-each-swatch, min-size-in-mm-and-px, co-brand-20-percent-rule, pattern-derivation-diagram, contents-page-with-page-numbers]
anti_patterns: [body-text-grey-2-1-contrast, approved-green-on-blue-4-1, no-voice-or-imagery-chapter, mockup-heavy-application-section, secondary-colours-unexplained]
---
# Naseem Al-Faihaa Brand Guidelines v1.0 — In-house

## 1. Snapshot
- **Subject:** A 39-page 16:9 deck (1920 × 1080 pt, rendered at 1400 × 787 px), ©2023, Version 1.0. It is the identity for a Baghdad tyre retailer that carries Dunlop, Michelin and Sumitomo, with fully bilingual English/Arabic text.
- **Why it's remarkable:**
  - The symbol is a ring of rotated "F" letterforms that reads as a wheel or tyre tread from a distance.
  - A single F becomes the repeat pattern.
  - The Latin slab wordmark (Factoria) and the Arabic lettering are modified to share stroke weight and horizontal stretch.

## 2. Composition & layout
- **Spec pages share a strict three-zone grid.**
  - Left title column at x = 88–400 px: Factoria Demi title in brand green, about 36 px cap height (≈50 pt), with the Arabic title in Lama Sans below it at ~18 px, and a "Download the …" link in navy with an icon.
  - English body column at x = 455–822 px.
  - Arabic body column at x = 945–1312 px, right-aligned.
  - Figures span 455–1312 px below y≈200.
  - Footer at y≈695 holds "Naseem Al-Faihaa | Brand Guidelines", a breadcrumb ("Brand Logo | Logo Clear Space") and a two-digit folio. The footer is about 8 px of light grey.
- **Margins:** 88 px left/right (≈120 pt). The page is about 93% white space on spec pages (p6 palette: #FFFFFF 93.5%).
- **Chapter dividers** (p5, 13, 17, 21, 24) are full-bleed green #78BE42 (98%) with a white Factoria title and an Arabic subtitle at the left, vertically centred.
- **Cover** (p1) is near-black #111A21 (96%), with an oversized outline of the symbol at about 4% opacity bleeding off the right edge and a green "Brand Guidelines" title of about 70 px. p2 is a dark tyre-and-hand photo with a slab headline ("Quality Tires, Unmatched Performance"), the third line struck through in grey.
- p25–38 are full-bleed photographic mock-ups without captions.

## 3. Typography
- **Embedded fonts (pdffonts):**
  - Factoria Demi: slab serif, used for headlines and the wordmark.
  - Acumin Pro Regular and Bold: sans, used for Latin body text.
  - Lama Sans Regular and Bold: Arabic.
  - Stolzl Book is also embedded (TrueType) but has no stated role. It is probably inside a mock-up.
- **Stated rules:**
  - p18: Factoria Demi for headlines and subheads, Acumin Pro Regular for body.
  - p19: Lama Sans Bold for Arabic headlines and subheads, Regular for body.
  - Each comes with a specimen line (A–Z, a–z, digits, symbols) under a hairline rule. The face name is in navy and the weight in grey.
- **Wordmark:** "The English and Arabic fonts have been modified to match each other" (p6). The Arabic is a flat, extended geometric drawing with long kashida joins.
- **Missing:** no size scale, leading or tracking is given anywhere. Observed on the slides: titles ≈50 pt, body ≈14 pt (≈10.5 px rendered) with generous leading of about 1.9.
- **Colour on type (p20):** text goes in white or dark grey on coloured backgrounds. The demo banner shows white Factoria and black Arabic on green, flanked by outline-only repeats of the name. That outline treatment is a nice secondary device, but it is never named.

## 4. Colour
| Hex (as published) | Name / role | Approx share |
|---|---|---|
| #78BE43 (sampled #78be42) | Primary green, "PANTONE P 154-8 C" | 98% of dividers; accents |
| #1E4489 | Primary navy, PANTONE 7687 C | links, secondary grounds (57% of p32) |
| #111921 | Primary near-black, PANTONE Black 6 C | cover, dark applications |
| #BCBDC0 | Cool Gray 4 C | neutral, logo-on-white demos |
| #FFFFFF | White | page ground (78–94%) |
| #F64740 / #F2AF29 / #05734E / #00A1E4 | Secondary: Vermilion, Xanthous, Dark Spring Green, Celestial Blue | only on p15 |

- Each primary swatch has a strip of **four tint steps** underneath it. Green and navy step towards white; black and cool grey run greyscale ramps. No values are given for the tints.
- The secondary colours "communicate different themes", but the themes are never named and none of the 14 application mock-ups uses them.

**WCAG checks:**
| Pair | Ratio | Result |
|---|---|---|
| Green on near-black #111921 | 7.8:1 | passes |
| Navy on white | 9.36:1 | passes |
| White on navy | 9.36:1 | passes |
| Near-black on white | 17.72:1 | passes |
| Navy on green | 4.12:1 | **fails AA-normal** |
| White on green | 2.27:1 | fails |
| Body copy grey (sampled ≈#B1B1B1) on white | 2.14:1 | fails |
| Xanthous on white | 1.92:1 | fails |

- Navy-on-green and green-on-navy are both *approved* for the symbol on p16, at 4.12:1.
- White on green is approved for the symbol (p16) and for headings (p20), even though it is the weakest pair.
- The deck's own body copy is set in light grey on white, so every English and Arabic paragraph is hard to read.

## 5. Depth & material
- The spec pages are flat: 1 px light-grey hairline frames around figures, no radii, no shadows.
- Depth appears only in the mock-ups (p25–38): signage in brushed metal, an embossed business card on wood, a curled pattern sheet, tape and a seal sticker.

## 6. Components & patterns
- **Logo set (p7):** four lock-ups, horizontal and vertical, each with English or Arabic leading. The horizontal lock-up is primary; the vertical one is for when space is limited.
- **Grid patterns (p22):**
  - "Tile Type: Grid": a single F blade extracted from the symbol (shown with a rotation diagram), alternating with small four-line "X" sparkles.
  - "Tile Type: Hex by Column": a rounded hexagon derived from the symbol's silhouette, with Y-shaped connectors.
  - Both are drawn as derivation diagrams, from symbol to extracted shape.
- **Fortified Seal (p23):** a double-ring roundel with the symbol in the centre, the name arched across the top in Factoria, "EST · 1959" on the horizontal axis, and the slogan "Unleash Your Drive" arched across the bottom. It appears as a sticker on p29.
- **Applications:** billboard, building sign, stationery set, notebooks, seal stickers, business card, envelope, Instagram profile, app icon (green rounded square), pattern sheets, packaging box, branded tape and mugs.

## 7. Motion
None documented.

## 8. Brand system
**Logo rules**
- **Structure (p6):**
  - Symbol: several "F" letters grouped in a circle to suggest a car wheel "especially if the logo is seen from afar".
  - Wordmark: Factoria slab, chosen for a "strong, dominant presence".
  - The symbol carries a ™.
- **Clearspace (p8):** a hatched margin of **2x** on all sides, where x is a small unit marked at the top-left. The figure is too light to read exactly what x measures. It looks like the height of one blade or the tagline cap height, but it is not legible enough to confirm. The rule applies to all four lock-ups.
- **Minimum size (p8):** horizontal lock-up 9.5 mm / 53 px height; vertical lock-up 16 mm / 100 px height.
- **Misuse (p9), six tiles with red ⊗ badges:**
  - Never change the colour (a purple example is shown).
  - Never fill with an image, pattern or gradient.
  - Never distort.
  - Never add drop shadows or effects.
  - Never add anything.
  - Never angle.
- **Positioning (p10):** top, bottom, centre or any of the four corners. It is shown as a 3×3 placement map on landscape and portrait formats.
- **Co-branding:**
  - Sponsors (p11): Naseem Al-Faihaa goes upper-left or lower-left and is **20% larger** than the other logos. A 100% / 80% / 80% scale strip with green spacing brackets illustrates this.
  - Partners (p12): partner logos are 20% smaller and follow the brand logo's alignment (centre, left or right), for single and multiple partners.
- **Colour backgrounds (p16):** 10 approved symbol/ground pairs (green, navy and black grounds with white, black or brand-colour symbols) and 4 rejected ones: grey symbol on green, navy on black, green on grey, navy on grey.

**Voice, tone, imagery**
- There is no voice chapter. The only copy cues are the slogan "Unleash Your Drive" (in the seal and the clearspace lock-up), the p2 headline "Quality Tires, Unmatched Performance", and a short introduction (p3) positioning the company as "Baghdad's tire authority".
- Photography is not codified. The images used are dark, moody workshop shots (mechanic, tyre, wheel) with cool grading.

**Document structure (39 pp)** (the contents page on p4 lists the same sections)
1. Cover, p1
2. Campaign headline, p2
3. Introduction, p3
4. Contents, p4
5. Brand Logo divider, p5
6. Logo Structure, p6
7. Logo Variations, p7
8. Logo Clear Space and minimum size, p8
9. Logo Misuses, p9
10. Logo Positioning, p10
11. Co-Branding (Sponsors), p11
12. Co-Branding (Partners), p12
13. Brand Colors divider, p13
14. Primary Colors, p14
15. Secondary Colors, p15
16. Logo with Colored Backgrounds, p16
17. Typography divider, p17
18. English Typeface, p18
19. Arabic Typeface, p19
20. Colour Usage for Typography, p20
21. Visual Elements divider, p21
22. Grid Patterns, p22
23. Fortified Seal, p23
24. Brand Applications divider, p24
25. Application mock-ups, pp25–38
26. Back cover (©2023), p39

**Token decisions worth stealing**
- The bilingual three-column spec layout (title | EN | AR) keeps both scripts equal without doubling the page count.
- Co-branding expressed as one number (±20%) rather than a drawing.
- Each pattern is shown as a derivation (symbol → extracted unit → tile), so the pattern's provenance is explicit.
- A "Download …" link sits on every spec page, next to the rule it serves.

## 9. UX
- **Easy to navigate:** a contents page, dividers, a breadcrumb in every footer, and download links next to each rule.
- **Weak as a working document:**
  - Low-contrast body text (2.1:1) makes the rules themselves hard to read.
  - No type scale.
  - Clearspace unit x is illegible.
  - Secondary colours have no usage.
  - No voice or photography guidance.
  - 14 of 39 pages are uncaptioned mock-ups.
- The "Logo with Colored Backgrounds" grid is the most practical page, but it approves two sub-AA pairings.

## 10. Craft signals
- The Arabic text is set with heavy tatweel (kashida) stretching to justify lines (visible on p6–p23). This produces uneven word gaps and is not typographically refined.
- Body text in both languages is rendered at about #B1B1B1 on #FFFFFF, a 2.14:1 ratio.
- The tint steps under each primary swatch (4 steps) are a useful idea but have no published values.
- Pantone "P 154-8 C" is a Pantone Plus-series chip code; the other swatches use standard names (7687 C, Cool Gray 4 C, Black 6 C).
- The cover's oversized symbol outline at about 4% contrast on #111A21 is a quiet, well-judged texture.
- Stolzl Book is embedded but never specified, a stray font in the file.
- Hairline figure frames (1 px, light grey) and red/green status badges are applied consistently across p9, p16 and p22.

## 11. Reproduction recipe
```css
:root{
  --naf-green:#78be43; --naf-navy:#1e4489; --naf-ink:#111921; --naf-grey:#bcbdc0; --naf-white:#fff;
  --naf-vermilion:#f64740; --naf-xanthous:#f2af29; --naf-spring:#05734e; --naf-celestial:#00a1e4;
  --font-head:"Factoria","Roboto Slab",serif;
  --font-body:"Acumin Pro","Inter",sans-serif;
  --font-ar:"Lama Sans","IBM Plex Sans Arabic",sans-serif;
  --body-ink:#5f6368; /* replace the doc's ~#b1b1b1 (2.14:1) with ≥4.5:1 */
}
.spec{display:grid;grid-template-columns:312px 1fr 1fr;column-gap:56px;padding:0 88px;background:var(--naf-white)}
.spec h2{font:600 50px/1.1 var(--font-head);color:var(--naf-green)}
.spec h2 + .ar{font:400 18px/1.4 var(--font-ar);direction:rtl;text-align:left;color:var(--naf-ink)}
.spec p{font:400 14px/1.9 var(--font-body);color:var(--body-ink)}
.spec p[lang=ar]{font-family:var(--font-ar);direction:rtl;text-align:right}
.divider{background:var(--naf-green);color:#fff;display:grid;align-content:center;padding-left:88px}
.pattern-f{background:var(--naf-green) url(f-blade.svg) 0 0/112px 112px repeat}
.cobrand-partner{height:calc(var(--logo-h)*.8)}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 6 | The green, navy and ink palette with a slab wordmark is solid and the F-wheel symbol is apt. The spec pages are pale and the mock-ups are stock-template. |
| Originality | 5 | The letter-built wheel symbol and the derived F pattern are clever. Otherwise it follows the standard template-deck format (dividers, misuse grid, mock-up parade). |
| Usability | 6 | Gives minimum sizes, co-branding percentages, approved and rejected backgrounds, bilingual text and download links. Missing: type scale, voice, imagery and secondary-colour usage, and the body text is barely legible. |
| Craft | 5 | The grid and footer system is consistent. The text has 2.1:1 contrast, the Arabic justification is kashida-stretched, the clearspace unit is illegible, an unexplained font is embedded and sub-AA pairings are approved. |

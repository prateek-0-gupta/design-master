---
id: bg-kia
source: brandguidelines
category: guideline
status: analyzed
title: "Kia Corporate Identity Guidelines (EN, Feb 2021)"
creator: "Blackspace"
styles: [corporate-clean, minimal-swiss, monochrome, technical-wireframe]
patterns: [rising-diagonal-line-motif, logo-derived-graphic-motif, ratio-based-type-scale, cap-height-unit-clearspace, logo-expansion-lockup, pictograms-from-logo-geometry, percentage-placement-rules, production-notes-per-item]
mode: light
palette: ["#05141f", "#ffffff", "#ea0029", "#6d6e71", "#939598", "#c7c8ca", "#f3c300", "#5d7d2b"]
type_families: ["Kia Signature (Light / Regular / Bold) — named in the text; the PDF's font programs were stripped, so pdffonts lists none"]
type_class: [neo-grotesk, humanist-sans]
radius_px: []
motion: null
scores: {aesthetics: 7, originality: 7, usability: 6, craft: 6}
craft_signals: [motif-thickness-scaled-by-paper-size, motif-corner-radius-0.1x, anchor-point-range-2-3a-to-a, dominant-colour-80-percent-rule, point-colour-max-50-percent, ratio-type-scale-60-50-20, cyan-construction-overlays, per-item-production-notes]
anti_patterns: [text-layer-fails-to-render, lorem-ipsum-in-type-specimen, yellow-on-white-1.66, rendered-black-drifts-from-spec]
---
# Kia Corporate Identity Guidelines — Blackspace

## 1. Snapshot
- **Subject:** a 123-page, 1280×720 pt landscape CI manual for the 2021 Kia rebrand: the new logotype, the "Movement that inspires" slogan, Kia Signature type, colour, a line motif, pictograms and icons, and about 65 pages of applications from ID cards and envelopes to fleet decals and hard hats.
- **Why it's remarkable:** almost everything is turned into a ratio. The logo-expansion type is set at a percentage of K height, the type scale is a percentage of the headline, motif line weights step with paper size, and motif corner radii are 0.1 × panel width. Only the logo's own clear space and minimum size are given in absolute units.

## 2. Composition & layout
- **Spread:** the landscape page splits into a left text column (about x = 38–410 pt, roughly the left 32%) and a right figure field that starts at x ≈ 410 pt (449 px on the 1400 px render) and runs to a right margin of about 92 px. Figures sit on very light grey #e6e6e6 panels or straight on white.
- **Grid:** the content stream includes a hidden 0.25 pt cyan guide layer. It defines **16 columns** of 68.125 pt with 10 pt gutters and 20 pt outer margins (guides at 88.1/98.1 … 1181.9/1191.9 pt). The figure field begins exactly at column 6 (410.6 pt), so the text column spans columns 1–5.
- **Chapter dividers** (p3, p5, p7, p57) use a 50 pt title. The cover and closing pages (p1, p123) are full Midnight Black with the motif: a 1 pt white line drops from the top-left, turns with a small radius and rises at about 30° to the top edge. The logo and slogan sit under the turn.
- **Rendering issue:** in the supplied rasters every live-text element is missing. Body copy, page headers and folios are all blank (pages 2, 3, 5, 8, 9, 22, 26 and others look empty). The PDF went through "3-Heights PDF Optimization Shell" and its CID font (`C0_0`, Adobe-Korea1) is no longer usable. I recovered the text by decoding the raw glyph IDs (CID + 0x1F = ASCII). The Korean strings could not be decoded and are not reported here.

## 3. Typography
- **Typeface:** Kia Signature in Light, Regular and Bold, named in the text (p34–37). pdffonts reports no fonts at all, and only outlined specimens are visible (p34–36, p38). Latin is a neo-grotesk with flat vertical stroke ends, a tall x-height and open K/W/y. The Korean companion has a humanist structure and is matched in weight to the Latin (p36). Coverage: Latin basic and extended, Greek and Coptic, Cyrillic (p38).
- **Hierarchy rule (p37):** headlines and subheads must be 12 pt (14 px) or larger, in Bold or Regular. Body and captions are below 12 pt (14 px), in Regular or Light.
- **Ratio scale (p39):** subhead = 60% of the headline size (Regular), body = 50% (Light), caption = 20% (Regular). Leading ratios exist per text type, but their values were only in the graphic and cannot be read.
- **The manual's own sizes** (from the decoded text matrices): divider titles 50 pt, cover 45 pt, page titles 20 pt, statement 32 pt, body 12 pt, notes 8 pt.
- **Notation:** write "Kia" with only the K capitalised. Full legal name "Kia Corporation", short form "Kia Corp."
- **Production specimens:** ID card name in Bold 8 pt with keywords in Bold 5.5 pt (p60). Email signature 7 pt throughout, with Bold for name and position and Light for address (p92). Banner headline in Light 260 pt on 320 pt leading, about 1.23 (p98).

## 4. Colour
Values taken from the colour pages (p13, p14, p30–32):

| Hex | Role | Approx share |
|---|---|---|
| #05141F Midnight Black (PMS 7547 C, C100 M58 Y21 K92) | primary, dominant surface | ≥80% when dominant |
| #FFFFFF Polar White | primary | ≥80% when dominant |
| #EA0029 Live Red (PMS 185 C) | point colour; never in the logo or motif | ≤50% |
| #6D6E71 / #939598 / #C7C8CA (K70/K50/K25) | dark / medium / light greys | support |
| #F3C300 Afternoon Yellow (P 7406 C) | secondary, image mood | small |
| #5D7D2B Forest Green (P 2279 C) | secondary | small |
| #9EA1A2 City Gray (P 422 C) | secondary | small |
| #85754E Gold (PMS 871) / #8C9091 Silver (PMS 877) | metallic logo only | special |

The p001 raster samples Midnight Black at **#141e28** in palette.json, not #05141F. The CMYK-built artwork renders lighter than the screen spec.

WCAG:
- #05141F on white: 18.65:1.
- White on #EA0029: 4.64:1 (AA pass).
- #EA0029 on #05141F: 4.02:1 (large text only).
- #939598 on white: 3.0:1 (large only).
- #6D6E71 on white: 5.1:1.
- #F3C300 on white: **1.66:1 (fail)**. #05141F on #F3C300: 11.2:1.
- White on #5D7D2B: 4.74:1.

## 5. Depth & material
The system is flat, with no shadows or gradients. The only material cues are the Gold and Silver metallic logos (p14), brushed-metal mock-ups of the badge, medal and plaque (p69–72), and the grayscale step chart (p15) that tells you when to switch from the black logo to the white one.

## 6. Components & patterns
- **Logo expansion** (p17–19). A service name follows the logo; the cap height of the name equals the logo height K, or 90% K for numerals and all-caps words; the gap is ¾ K; the vertical lockup uses 70% K margins. Example: "Kia 360", "Kia VIK", "Kia Members".
- **Co-branding** (p20): the partner logo is limited to a maximum height of 3K, with a hairline divider. **Hyundai + Kia** (p21): minimum size 50 mm, and Hyundai Blue #002C5F is specified.
- **Graphic motif types A, B and C** (p43–51), all derived from the logo's rising diagonal:
  - A: a vertical line turning into a diagonal;
  - B: a diagonal turning into a horizontal;
  - C: a long horizontal panel with a rounded corner.
  - Never let the lines descend.
- **25 pictograms** (p53–54), drawn on a grid with the logo's bevelled terminals and vertical cuts. **25 icon groups** (p55–56) whose stroke endings match Kia Signature.
- **Applications** each carry a "[Production Notes]" block: size, material, print method, colour build and font sizes. Examples: ID card 54×85.6 mm on 0.75 T PVC; banner 1800×600 mm on TP fabric or PET.

## 7. Motion
n/a, this is a static PDF. The motif is described as "ascending energy flow", but no animation rules are given.

## 8. Brand system
**Logo (p9–21).** The logotype rests on three ideas, Symmetry, Rhythm and Rising. The anatomy page (p11) labels:
1. bevelled stroke ends on K and A;
2. modulated stroke widths;
3. large counters;
4. narrow connections between letters.

The construction diagram marks angles of 31°/33°/45°. Clear space is the module **B**, the width of the "I" stem, on all sides (p12). Minimum size is **5 mm print / 15 px digital**. Logo colours are Midnight Black or Polar White only, K100 for mono print, and Gold or Silver metallics for special finishes. The p15 grayscale strip (10–100%) decides black versus white logo. There are **12 numbered misuses** (p16): recolour, outline, low-res, crop, skew, busy background, rotate (except watermark patterns), inside text, with the corporate name, mirror, vertical, and crop again.

**Slogan (p22–25).** "Movement that inspires" is English only and never translated. It may be set in any of the three weights. Its margin equals the cap height of "M", minimum size 3 mm. Two-line breaks go after "Movement"; three-line breaks go after each word. Logo + slogan lockups come vertical or horizontal with B clear space; the minimums are **8.5 mm / 24 px** and **6 mm / 18 px** (the two lockups on p25). The internal mission sentence must stay whole, in order, and at one size and colour.

**Colour (p26–32).** Three tiers: "Opposites United" (black/white), "Kianess" (red), "Modern Individuals' Lifestyle" (yellow, green, gray), each with a photo mood board (p27–30). Usage rules: one primary colour must cover **≥80%** of a surface; Live Red **≤50%** and never in the logo or motif. Pantone is the master; CMYK is "closest match, adjust by proof"; RGB/HEX is for screen.

**Graphic motif (p42–51), the most stealable section.**
- **Line weight by format:** 0.5 pt up to A6, 0.75 pt for A6–A4, 1 pt for A4–A3.
- **Anchor point:** the turn must sit between ⅔A and A.
- **Type A:** 5–10% from the left edge, height 30–50% on vertical formats; on horizontal formats it may also sit at 50–70%, height 30–80%.
- **Type B:** turn at 30–50% (vertical) or 50–70% (horizontal) from the top.
- **Type C:** horizontal formats only, 10% right margin, corner **R = 0.1X** (e.g. X 400 → R 40).
- **Logo with the motif:** max 50% of the format width (30% of the height for C), at least 1X from the motif, and always at the motif's left end, never top-left or right.

**Pictogram & icon (p52–56).** The pictograms' bevelled shoulder and the hip cut copy the K/A terminals, highlighted with cyan circles on p53.

**Voice.** Statements are short and declarative ("We believe movement inspires ideas"). A WHY / HOW / WHAT / TO WHOM brand-strategy diagram appears on p6. The stationery chapter tells you to choose eco-friendly suppliers (p76).

**Document structure (TOC p2, sub-TOCs p8, p9, p58):**
1. Cover, p1
2. Table of contents, p2
3. Introduction, p3–4
4. Brand Strategy, p5–6
5. Basic System, p7–56:
   - Logo, p9–21
   - Slogan, p22–25
   - Color, p26–32
   - Typeface, p33–41
   - Graphic System, p42–51
   - Pictogram & Icon, p52–56
6. Application System, p57–122:
   - General Affairs Form (ID cards, nameplates, flags, badge, medal, certificate), p59–75
   - Stationery (business card, letterhead, 10 envelopes, sales record, PPT template, email signature), p76–93
   - Promotional Items (placards, banners, shopping bags, tape, clock, mask), p94–105
   - Vehicle Decals (standard, test drive, partnership, company car), p106–116
   - Uniform Logo, p117–122
7. Back cover, p123

**Tokens worth stealing:** motif stroke weight keyed to format size; corner radius equal to 0.1 × panel width; red capped at 50% of a surface and one primary at 80% or more; ratio type scale 1 : 0.6 : 0.5 : 0.2.

## 9. UX
A designer can apply the measurable parts (clear space, lockups, motif placement, production notes) without asking. Three things work against them. The live-text failure means the PDF as shipped may show blank pages in some renderers. The type specimen (p40) is lorem ipsum. The leading ratios are not readable. The manual also hands photography and layout to a separate "Communication Style Guideline" (it cites "chapter 8. Graphic Style" repeatedly), so this document cannot stand alone.

## 10. Craft signals
- Clear-space module B = the I-stem width, drawn with cyan arrow-crosses at all four corners (p12).
- Motif weight table: 0.5 / 0.75 / 1 pt by A6 / A4 / A3.
- Type C corner radius R = 0.1X, with a worked example (X 400, R 40).
- Expansion cap height = K, or 90% K for numerals and all-caps; vertical lockup margins 70% K.
- A hidden 16-column guide layer (68.125 pt columns, 10 pt gutters, 20 pt margins) sits in every page's content stream.
- Every application page has a production-notes block with mm sizes, substrate, Pantone and pt sizes.
- Pictogram terminals copy the logo's bevel, with the matching points circled on p53.

## 11. Reproduction recipe
```css
:root{
  --kia-midnight:#05141f; --kia-polar:#ffffff; --kia-red:#ea0029;
  --kia-gray-70:#6d6e71; --kia-gray-50:#939598; --kia-gray-25:#c7c8ca;
  --kia-yellow:#f3c300; --kia-green:#5d7d2b; --kia-city:#9ea1a2;
  --font:"Kia Signature","Inter",system-ui,sans-serif;
  --h:clamp(2rem,4vw,3.5rem);         /* headline */
  --sub:calc(var(--h)*.6);            /* 60% Regular */
  --body:calc(var(--h)*.5);           /* 50% Light (keep >=14px on screen) */
  --cap:max(12px,calc(var(--h)*.2));  /* 20% Regular */
  --motif-w:1px;                      /* 0.5/0.75/1pt by format */
}
.kia-motif{position:relative;background:var(--kia-midnight);color:var(--kia-polar)}
.kia-motif::before{ /* Type A: vertical then rising diagonal (~30deg) */
  content:"";position:absolute;left:4%;top:0;width:1px;height:80%;
  background:currentColor}
.kia-motif::after{
  content:"";position:absolute;left:4%;top:80%;width:90%;height:var(--motif-w);
  background:currentColor;transform-origin:0 0;transform:rotate(-30deg)}
.kia-panel-c{border-top-right-radius:calc(var(--panel-w,400px)*.1)} /* R=0.1X */
.kia-point{background:var(--kia-red);max-inline-size:50%}            /* <=50% surface */
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 7 | A disciplined black/white system with one striking line motif. The application pages are tidy but read as line drawings. |
| Originality | 7 | Building the motif, pictograms and icons from the logotype's own diagonal and bevel is a fresh take on "graphic device from logo". |
| Usability | 6 | Excellent ratios and production notes. But the text layer does not render, the specimen is lorem ipsum, and imagery is deferred to another manual. |
| Craft | 6 | Precise construction drawings and a hidden grid. Against that: a broken font export, a rendered black that drifts from spec, and a yellow secondary that fails contrast on white. |

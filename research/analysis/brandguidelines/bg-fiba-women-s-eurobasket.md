---
id: bg-fiba-women-s-eurobasket
source: brandguidelines
category: guideline
status: analyzed
title: "FIBA Women's EuroBasket 2023 — Brand Manual (Logo & Brand assets guidelines)"
creator: "In-house"
styles: [maximalist-color, swiss-grid-poster, kinetic-type, dark-premium]
patterns: [op-art-stripe-court, quarter-circle-module-cluster, host-colour-coded-posters, word-height-clearspace, host-city-logo-variants, split-navy-rail-layout, download-tab-per-asset, cutout-athlete-over-pattern]
mode: mixed
palette: ["#000041", "#ffffff", "#5fd4c2", "#004995", "#960077", "#df4350", "#001659", "#a28542"]
type_families: ["Yeager (Light / Regular / Bold, embedded)", "Founders Grotesk (Light → Bold, embedded, undocumented body face)"]
type_class: [condensed, display, grotesk]
radius_px: []
motion: null
scores: {aesthetics: 8, originality: 7, usability: 6, craft: 6}
craft_signals: [clearspace-equals-word-height, print-and-digital-min-widths, darker-shade-per-host-colour, cluster-fades-to-edge, hostcolour-per-athlete-poster, colour-meaning-named]
anti_patterns: [black-swatch-rgb-255, five-vs-six-colours-contradiction, teal-text-on-white-1-8, no-type-hierarchy-spec, thin-photography-guidance]
---
# FIBA Women's EuroBasket 2023 Brand Manual — In-house

## 1. Snapshot
- **Subject:** A 61-page A4-landscape (841.89×595.28 pt) manual for the event identity of the 2023 tournament co-hosted by Israel and Slovenia. It covers concept, asset overview, the official logo and its host variants, misuse, brand assets (colour, type, graphic elements, photography) and mock-ups.
- **Why it's remarkable:** Two graphic languages do all the work. One is an op-art "abstract court" built from concentric white stripes. The other is a kit of quarter-circle basketball "building blocks" that cluster into Alps, waves and crowds. The palette names each colour for what it means (Slovenia, Israel, Mediterranean Sea, Unity, Passion), and each colour drives one athlete poster.

## 2. Composition & layout
Every content page uses a two-zone split.
- A left rail ~375/1400 px wide (27%), either Mediterranean Sea navy `#000041` (logo pages) or white (asset pages). It holds an uppercase section label in Yeager Bold (~18 px, "OFFICIAL LOGO"), a light Founders Grotesk page title (~28 px) underlined by a ~165 px grey rule, a short body column (~15 px), and a coral "DOWNLOAD" tab that bleeds off the left edge at y≈840.
- A right stage carrying the specimen. It has a two-line event lock-up as a running header at top-right ("FIBA WOMEN'S EUROBASKET / ISRAEL · SLOVENIA · 2023") and a light grey folio bottom-right.

Chapter dividers are full navy with a large grey numeral, a Yeager Bold title and a white underline (pp3, 5, 7, 35, 37, 51). Navy covers 92.6% of the cover (palette.json `#000040`). Application pages (pp52–61) place a single mock-up photo at ~1240×660 px on navy, with generous 38 px margins.

## 3. Typography
pdffonts lists **Yeager** (Light, Regular, Bold) and **Founders Grotesk** (Light, Regular, Medium, Bold). Times-Bold also appears but no visible use was found.
- **Yeager** is the only typeface documented (p40), as "strong character, energy and a modern feel". It is a narrow squared grotesque with angled terminals. The specimen shows Light, Regular and Bold, and the "DARE TO DREAM" slogan is set in Yeager Bold with heavy perspective skew. The "EUROBASKET" logotype is custom lettering in the same spirit.
- **Founders Grotesk** sets all the manual's titles (Light) and body copy (Regular/Light, ~15 px on 1400 px renders, ~1.45 leading). It is never named in the manual, so a designer would not know to use it.
- No hierarchy, sizes, leading or tracking are specified. p6 lists "Veager Regular / Veager Bold" as the overview items, and the asset-overview page spells the name with a V-like Y glyph, which may confuse readers.

## 4. Colour
From pp17, 26 and 39 (the document's own CMYK/RGB/Pantone). Palette.json for p39 matches within 1–2 values (`#df4350`, `#000040`, `#950076`, `#004a95`, `#5fd4c2`, `#000f5a`).

| hex | name / role | approx share |
|---|---|---|
| #000041 | Mediterranean Sea (PMS 2766 C), master background | 60–90% of dark pages |
| #ffffff | White, text on navy, stage ground | 30–70% of light pages |
| #5fd4c2 | Slovenia (PMS 3255 C), host colour | accent / poster ground |
| #004995 | Israel (PMS 2146 C), host colour | accent / poster ground |
| #960077 | Unity (PMS 241 C) | accent / poster ground |
| #df4350 | Passion (PMS 1785 C), also DOWNLOAD tabs | accent / poster ground |
| #001659 | Watermark (PMS 2757 C), background watermark lines | texture |
| #a28542 | FIBA Gold (PMS 4505 C), "used only for the logo" | <1% |

The darker shades on p17 are Slovenia `#30b0ac`, Israel `#00347b`, Unity `#7f0063` and Passion `#c3243d`, used inside the symbol's gradients.

**Errors in the document.** p17 lists the "BLACK" swatch as RGB 255/255/255 (white), confirmed in the extracted text. p17 says "five different colors" while p39 says "six".

WCAG (contrast.py):
- White on `#000041`: 19.51:1. `#004995` on white: 8.8:1. White on Unity: 8.19:1.
- `#5fd4c2` on navy: 10.85:1. `#df4350` on navy: 4.7:1.
- **`#5fd4c2` on white: 1.8:1**, yet "SLOVENIA" is set in that teal on white in the logo and in every white-page running header.
- White on Passion: 4.15:1, large only.
- **Unity on navy: 2.38:1**, which is what the dark-page running header uses for "ISRAEL" (pp40, 48).

## 5. Depth & material
The system is flat vector throughout, with no shadows except a faint drop shadow on the DOWNLOAD tab. Depth is optical: the abstract court (p43) is a perspective-skewed basketball court rendered as 10–14 concentric stripes per element, so it reads as a vortex. The symbol has the only gradients, soft radial shading on the quarter segments that make it read as a sphere. Cut-out athlete photos sit in front of the stripe field, often breaking out of it (pp4, 50, 54–55).

## 6. Components & patterns
- **Abstract court:** comes in mono (white stripes on navy), colour (navy stripes with teal, magenta and coral accents), and four single-colour "appearance" tiles (Israel, Passion, Unity, Slovenia), plus slogan and city variants ("DARE TO DREAM", "LJU", "TEL").
- **Building-block modules (pp44–47):** a circle quartered by basketball seams into coloured quarter- and half-discs. It produces "Basketball", "The Alps", "The Waves" and "The Fans" (dots as heads). Each has a "basic visual" and a "composite visual".
- **Composite cluster (pp48–49):** modules densest at the centre and smaller or fainter toward the edge, "to avoid sharp border… feel of a blur". The cluster is cropped by the format frame, never shown whole.
- **Background watermark (p42):** thin `#001659` court lines on `#000041`, about 1.2:1 tone-on-tone.
- **Athlete poster set (pp4, 50):** one cut-out player per host/brand colour on matching stripes, logo top-right.

## 7. Motion
None specified. The skewed type and stripe vortex imply motion, but no animation rules exist.

## 8. Brand system
**Logo rules.** The logo has three parts (p8): the *Symbol* (a sphere with ball seams, the trophy's handles, fans, the Mediterranean and the Alps, and "2023" hidden in the band), the *Permanent Competition Mark* (FIBA arc in gold, "WOMEN'S" in wide-spaced serif caps, the custom "EUROBASKET"), and the *Host Countries* line ("ISRAEL · SLOVENIA" in Israel blue and Slovenia teal).
- Versions: portrait and landscape, full colour positive and negative, flat colour, one-colour (navy, Israel blue, Slovenia teal) and monochrome black or white (pp9–14). Negative versions sit on four approved coloured grounds, Slovenia, Israel, Passion and Unity (pp11–12).
- **Clear area (p18):** E = the height of the word "EUROBASKET", on all sides, portrait and landscape.
- **Minimum widths (p19):** portrait 15 mm / 110 px, landscape 30 mm / 220 px, wordmark-only lock-up 20 mm / 165 px. Host-city and host-country versions repeat this (pp27–29).
- **Host variants (pp20–25, 32–34):** "SLOVENIA · 2023", "ISRAEL · 2023", "LJUBLJANA · SLOVENIA", "TEL AVIV · ISRAEL", each "Only for Limited Usage", e.g. city flags and host roll-ups. The competition wordmark (pp30–31) is a text-only two-line lock-up.
- **Partner lock-ups (pp15–16):** "Presented by" sits under the logo or to its right, and a partner composite sits under a hairline divider.
- **Misuse (p36), eight don'ts:** distort, recolour, delete parts, change font, unofficial background colour, holding shape, resize parts, complex photo background.

**Voice & tone.** There is no voice chapter. p4 gives the concept in one paragraph: the women's game is "fast, explosive and thrilling", and the identity must combine "the game and the lifestyle" and "highlight the hosts". The slogan "DARE TO DREAM" and the hashtag #EUROBASKETWOMEN are the only copy assets.

**Imagery.** There is a single page (p50): "cropped images of players can also be used together with the graphic elements". It sets no rules on photo style, crop, colour treatment or consent. The examples show cut-out action shots over stripes, one host colour per poster.

**Document structure (61 pp, from the TOC on p2):**
1. Cover, p1. Content, p2.
2. Brand Concept, pp3–4: the idea.
3. Brand Overview, pp5–6: asset overview.
4. Official Logo, pp7–34: overview, portrait, landscape, colour variants, one-colour, monochrome, presenting partner, partner composite, palette, clear area, minimum dimensions, host country/city logos positive and negative, their palette, clear area and minimums, competition and host wordmarks.
5. Unauthorized Usage, pp35–36.
6. Brand Assets, pp37–50: overview, colour palette, typography, graphic elements (complete palette, watermark, key abstract visual, basketball, Alps, waves, fans, composite cluster ×2), integrating photography.
7. Branding Examples, pp51–61: billboards, hoardings, posters, building wrap, apparel, champions banner, watch packaging, court-floor graphic.

**Token decisions worth stealing.** Name colours by their meaning (host nations, sea, unity, passion) so the colour-to-poster mapping explains itself. Give each brand colour a darker shade for depth inside the mark. Pair print mm with digital px minimums per lock-up. Use clear space equal to a named word's height. Fade generative clusters toward their edge so they never end in a hard border.

## 9. UX
It is easy to navigate: a numbered TOC, colour-coded rails, and a DOWNLOAD tab on every page whose asset is downloadable. The logo chapter (28 pages) is thorough. The guidance thins out after that. There is no type scale, no layout grid, almost no photography or copy guidance, and no colour-pairing rules, so a designer could easily put teal text on white, as the document itself does in its running headers.

## 10. Craft signals
- Clear space is drawn as grey "E" glyph blocks on every side of both orientations (p18).
- The minimum-width table gives 3 lock-ups × print mm and digital px (p19).
- Every host colour has a darker shade with its own Pantone (p17).
- The composite-cluster crop examples show the format frame cutting the cluster off-centre (p48).
- The running header changes host colours on dark pages (Unity, Passion) versus light pages (Israel, Slovenia).
- Flaws: black swatch listed as RGB 255/255/255 (p17), the five-vs-six colour count, "seames" typo (p8), and an undocumented body typeface.

## 11. Reproduction recipe
```css
:root{
  --med-sea:#000041; --watermark:#001659; --white:#fff;
  --slovenia:#5fd4c2; --slovenia-dk:#30b0ac;
  --israel:#004995;   --israel-dk:#00347b;
  --unity:#960077;    --unity-dk:#7f0063;
  --passion:#df4350;  --passion-dk:#c3243d;
  --fiba-gold:#a28542;
  --font-display:"Yeager","Barlow Condensed",sans-serif;
  --font-text:"Founders Grotesk","Inter",sans-serif;
}
.page{display:grid;grid-template-columns:27% 1fr;background:#fff}
.rail{background:var(--med-sea);color:#fff;padding:56px 24px 0 94px}
.rail h4{font:700 18px/1 var(--font-display);text-transform:uppercase}
.rail h2{font:300 28px/1.1 var(--font-text);padding-bottom:12px;border-bottom:3px solid #8a8a8a;display:inline-block}
.download{background:var(--passion);color:#fff;margin-left:-94px;padding:8px 0 8px 94px;border-radius:0 6px 6px 0;box-shadow:0 2px 4px rgba(0,0,0,.25)}
.slogan{font:700 clamp(48px,8vw,140px)/.85 var(--font-display);color:#fff;transform:skewY(-12deg) rotate(-8deg)}
/* op-art stripe field */
.court{background:repeating-linear-gradient(115deg,#fff 0 10px,var(--med-sea) 10px 20px)}
/* quarter-circle building block */
.block{width:80px;aspect-ratio:1;border-radius:50%;
  background:conic-gradient(var(--unity) 0 25%,var(--passion) 0 50%,var(--israel) 0 75%,var(--slovenia) 0)}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | The op-art stripe court and quarter-circle clusters on deep navy make striking, energetic event graphics. The mock-ups show the system scaling from watch boxes to court floors. |
| Originality | 7 | A fresh combination of op-art perspective and modular geometric "landscapes" tied to host geography, though both devices are familiar in sport branding. |
| Usability | 6 | Logo variants, clear space and minimums are exhaustive. Type hierarchy, layout grid, photo rules and contrast pairings are absent. |
| Craft | 6 | Clean, consistent page system, undermined by a white-RGB "black" swatch, a contradictory colour count, a 1.8:1 teal-on-white host line, and an undocumented body typeface. |

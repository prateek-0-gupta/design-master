---
id: bg-northalley
source: brandguidelines
category: guideline
status: analyzed
title: "NorthAlley"
creator: "Studio Fable"
styles: [corporate-clean, minimal-swiss, photo-led]
patterns: [crosshair-star-trail-device, running-header-rule-bar, rounded-swatch-pills, co-brand-x-separator, sentence-case-rule, highlight-word-in-accent, chapter-divider-crosshair]
mode: light
palette: ["#00403D", "#D9FF00", "#B3CFCD", "#E4E9E9", "#787664", "#8D8BDA", "#FF8048", "#D7ADDB"]
type_families: ["Degular (Medium/Semibold, Adobe Fonts)", "Manrope (Google Fonts)", "Poppins (embedded in mockups)", "Outfit (embedded, Thin)"]
type_class: [grotesk, geometric-sans]
radius_px: [20, 26, 12]
motion: null
scores: {aesthetics: 7, originality: 5, usability: 5, craft: 6}
craft_signals: [one-accent-hairline-crosshair, header-rule-bar-on-every-page, co-brand-gap-0-16x, icon-grid-1x-clearspace, highlight-colour-for-key-phrase, hex-and-cmyk-pantone-split-pages]
anti_patterns: [white-on-coral-fails-aa, fluorescent-on-light-invisible, thin-logo-rules, typos-in-spec, no-misuse-page, stock-photo-sourcing-advice]
---
# NorthAlley — Studio Fable

## 1. Snapshot
- **Subject:** A 39-page, 1152×648 pt (16:9) brand guideline for NorthAlley, a tech/software services firm. The identity is a four-point compass "star" plus a Degular wordmark, deep Pine green with a fluorescent yellow-green accent, and a "Star Trail" hairline crosshair device.
- **Why it's remarkable:** One small idea carries the whole identity. A 1 px fluorescent hairline cross with a star glint at the intersection divides photo and text panels. The page system is calm and consistent. As a rulebook, though, it is thin.

## 2. Composition & layout
- **Content pages (1400×787 px render):**
  - A header bar between two 1.5 px Pine rules at y≈53 and y≈107 holds "NorthAlley" (x=61), the section name (x=229) and the folio (x≈700), all about 22 px Manrope Medium. A ~55 px Pine star sits outside the rule on the right (x≈1310).
  - A left column with an H1 of about 56 px Degular (≈46 pt on the 1152 pt page) at y≈205, followed by about 16 px body at ~24 px line spacing.
  - On the right, a specimen card in Misty #B3CFCD with a radius of about 20 px, spanning x≈607–1281.
  - Margins are 61 px left, and the outer edge aligns at x=1281.
- **Dividers (p3, p7, p14, p18, p25):** full Pine with a white Degular title of about 64 px. Two 1 px fluorescent hairlines cross at an off-centre point (≈x 1090, y 463 on the cover), with a star glint at the crossing. This is the Star Trail in its purest form.
- **Applications:** posters and social posts are split into rectangles by the same crosshair, with a photo in one cell and a headline in another (p31–36).

## 3. Typography
- **Headlines: Degular** (embedded as Degular-Medium and Degular-Semibold). The book credits James Edmondson and Adobe Fonts. It has a quirky grotesk anatomy, with an angled "t" terminal and a narrow "y".
- **Body: Manrope.** pdffonts shows only a "Manrope-ExtraLight" subset name, almost certainly a variable-font naming artefact, since the rendered body is visibly Medium. The book says to use Medium mostly and Semibold for emphasis.
- Poppins (Regular, SemiBold, Light) and Outfit Thin are also embedded. They do not appear in any type specimen and likely come from mockup assets.
- **Hierarchy (p21):**
  - Headline: Degular Semibold, about 46 px in the card.
  - Subline: Degular Semibold, about 24 px.
  - Body: Manrope Medium, about 16 px at ~1.5 leading.
  - Button: Manrope Semibold, about 16 px, in a Pine pill (radius ~10 px) with fluorescent text.
  - No sizes, leading or tracking values are stated. The page only shows an example.
- **Rules:**
  - Sentence case everywhere. All caps is shown struck through (p24) because it "feels like shouting".
  - Highlight words go in the brighter accent, e.g. "the future." in #D9FF00 on Pine or Storm (p23).

## 4. Colour
Values are taken from the document's swatch pages p15 and p17. palette.json agrees: p001 #00413d at 94%, p015 #daff01 and #b2cfcd.

| Hex | Name / role | Approx share |
|---|---|---|
| #00403D | Pine: brand dark, dividers, type colour on light | ~35% |
| #E4E9E9 | Frosty: page background | ~45% |
| #B3CFCD | Misty: specimen cards, soft panels | ~10% |
| #D9FF00 | "Flourescent" (sic): accent lines, star glint, highlights | ~3% |
| #000000 / #FFFFFF | utility | — |
| #787664 Storm, #C2BCAF Foggy, #E6E4E1 Snow | secondary neutrals (poster panels) | ~4% |
| #D7ADDB Aurora, #8D8BDA Iris, #FF8048 Coral | secondary brights (social posts) | ~3% |

- p16 repeats the primaries with CMYK and gives the Pantone only for the accent (809 U).
- Secondaries are given only as HEX and RGB.

WCAG (contrast.py):
- Pine on Frosty: **9.51:1**.
- #D9FF00 on Pine: **10.14:1**.
- Pine on Misty: 7.07:1.
- White on Storm: 4.59:1, which passes, but #D9FF00 on Storm is 3.99:1 (large text only), and that pairing is used for the poster logo.
- White on Iris: **3.07:1** (large only).
- **White on Coral: 2.49:1**, which fails even AA large. Fluorescent on Coral is 2.16:1, and the p37 social post uses it.
- #D9FF00 on Frosty: **1.07:1**, which is effectively invisible. The book shows the fluorescent logo only on a Misty card (p8), with no warning against using it on light grounds.

## 5. Depth & material
- The system is flat. Cards have rounded corners (about 20 px on specimen cards, about 26 px on the tall colour swatch pills on p15) and no shadows.
- The only "light" effect is the four-point glint where the hairlines cross. It reads as a lens flare or star and carries the compass/north metaphor.
- Mockups (sign, USB sticks, jacket, bus shelter) are standard photoreal PSD composites.

## 6. Components & patterns
- **Star Trail (p27):** 1 px accent lines that may cross an image or text panel, with an optional glint at the crossing and a small white star in a corner. The book's stated purpose: recall, separating information, aesthetics. It must stay "supporting".
- **Tone cards (p6):** four Misty cards (Confident, Optimistic, Warm, Clear) in a 2×2 grid.
- **Type colour pairings (p22):** four horizontal bars (Pine on Misty, Frosty on Pine, Pine outline on Frosty, Pine on Foggy).
- **Brand extensions (p26):** star + NorthAlley + descriptor in Manrope Regular ("Solutions", "Development", "Strategy"). The descriptor's height must be slightly below the wordmark's.
- **Social templates:** a stat post ("87%" in Degular at about 40% of the tile width, in fluorescent), a quote post with the highlight phrase, and a bar chart in Storm/Snow/fluorescent.

## 7. Motion
None specified. The book mentions only that "animation and videos" should mix with static posts (p31). No durations or easing are given.

## 8. Brand system
**Logo rules:**
- **Construction:** horizontal lockup of the compass star and the Degular wordmark. Three colourways are shown: black on Misty, Pine, and fluorescent (p8).
- **Clear space (p9):** a 3×3 box grid around the logo. The module equals the logo height, but the book never states this in words. It only says "defined parameters".
- **Minimum size:** the lockup shows a "20 pt" label. The icon alone is "no smaller than 20px in height" with 1× clear space, where x = icon height (p12).
- **Co-branding (p11):** the partner logo is separated by **0.16x** with a "×" glyph between, and must not exceed the NorthAlley logo's height. Overhangs are allowed (the Taj example).
- **Brand extensions:** descriptor in Manrope beside the full logo, visually lower than the wordmark (p26).
- **Gaps:** there is no misuse/don'ts page for the logo, no greyscale or one-colour rule and no background-selection rule.

**Icon:** the compass star is used as the app and social avatar on Pine with a fluorescent glyph (p13), in "whatever shape is required" (circle or square).

**Voice (p6):** four attributes, each with a one-sentence gloss: Confident, Optimistic, Warm, Clear. There are no do/don't copy examples beyond the caps rule and the highlight rule.

**Imagery:** natural, well-lit, high-resolution photography of people at work, solar fields and AR. The book explicitly points to Unsplash, Freepik, Pexels and "Pexabay" (p35) as sources. That is practical, but it is a weak art-direction stance for a brand.

**Document structure:**
1. Cover (p1)
2. Contents (p2)
3. Brand Overview: Introduction, The Brand, Tone of Voice (p3–6)
4. Logo Overview: The Logo, Clearspace, Logo Usage, Co-branding, Our Icon, Icon in Use (p7–13)
5. Brand Palette: Primary Colours, Print Specs, Secondary Colours (p14–17)
6. Typography: Primary Type, Secondary Type, Type Hierarchy, Type Colour Use Cases, Highlights, Capitals (p18–24)
7. Brand Application: Brand Extensions, Brand Element, Exterior Usage, Stationery, Brand Communication (posters and socials), Merchandise (p25–38)
8. "Fin." back page with studio contact, © 2024 (p39)

**Token decisions worth stealing:**
- A single accent used only as 1 px lines and tiny glints, never as a fill. It stays precious, and #D9FF00 on #00403D gives 10:1.
- A running header between two rules with a fixed three-slot structure (brand / section / folio).
- The co-brand spacing ratio (0.16x) with a "×" glyph.

## 9. UX
Navigation is easy because the header bar always names the section and folio, and the contents page has page numbers. Applying the brand is harder:
- No type sizes, leading or tracking are given.
- No grid is defined.
- Clear space is shown but not defined in words.
- Secondary colours lack CMYK and Pantone.
- There is no misuse page.
- Several shown pairings fail WCAG (Coral, Iris).
- Text has typos: "Flourescent", "focu", "Pexabay".

A designer could copy the look from the examples but would have to invent the rules.

## 10. Craft signals
- Header rules sit at exactly the same y (≈53/107 px) on all 31 content pages, with a fixed 61 px left margin.
- The crosshair hairlines on the dividers stay at about 1 px, with the glint scaled to about 60 px.
- Specimen cards and colour pills share radius families (about 20 px cards, 26 px pills, 10 px buttons).
- The fluorescent accent is reserved for lines, glints, highlights and buttons.
- Co-brand spacing is given as a ratio (0.16x), not as an absolute value.

## 11. Reproduction recipe
```css
:root{
  --pine:#00403D; --frosty:#E4E9E9; --misty:#B3CFCD; --fluoro:#D9FF00;
  --storm:#787664; --foggy:#C2BCAF; --snow:#E6E4E1; --aurora:#D7ADDB; --iris:#8D8BDA; --coral:#FF8048;
  --font-display:"Degular","Manrope",system-ui,sans-serif; --font-body:"Manrope",system-ui,sans-serif;
  --r-card:20px; --r-pill:26px; --r-btn:10px;
}
body{background:var(--frosty);color:var(--pine);font:500 16px/1.5 var(--font-body)}
h1,h2{font-family:var(--font-display);font-weight:600;letter-spacing:-.01em;text-transform:none}
.header{display:grid;grid-template-columns:168px 1fr auto;border-block:1.5px solid var(--pine);padding:12px 0;font-size:22px}
.card{background:var(--misty);border-radius:var(--r-card);padding:40px 64px}
.btn{background:var(--pine);color:var(--fluoro);border-radius:var(--r-btn);padding:12px 28px;font-weight:600}
.highlight{color:var(--fluoro)}
/* Star Trail: hairline crosshair with glint */
.trail{position:relative}
.trail::before,.trail::after{content:"";position:absolute;background:var(--fluoro)}
.trail::before{left:var(--x,70%);top:0;bottom:0;width:1px}
.trail::after{top:var(--y,55%);left:0;right:0;height:1px}
.trail .glint{position:absolute;left:var(--x,70%);top:var(--y,55%);width:56px;aspect-ratio:1;translate:-50% -50%;
  background:var(--fluoro);clip-path:polygon(50% 0,56% 44%,100% 50%,56% 56%,50% 100%,44% 56%,0 50%,44% 44%)}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 7 | Pine plus a fluorescent hairline with generous Frosty space is cohesive and fresh-looking. Coral and Aurora social posts dilute it. |
| Originality | 5 | A compass star for a "north" name is literal. The crosshair-glint device is a nice, if familiar, touch. |
| Usability | 5 | Clear navigation, but few numeric rules, no grid, no misuse page and inaccessible secondary pairings. |
| Craft | 6 | The page template is consistent, but there are typos, unexplained embedded fonts and missing print specs for secondaries. |

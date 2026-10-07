---
id: bg-adobe
source: brandguidelines
category: guideline
status: analyzed
title: "Adobe Corporate Brand — Internal guidelines (08 Nov 2018)"
creator: "In-house"
styles: [corporate-clean, photo-led, maximalist-color]
patterns: [red-tag-logo-hanging-from-edge, title-underline-rule, artist-remix-imagery-program, micro-macro-crop, size-indexed-tracking-table, this-not-this-voice-table, infographic-anatomy-callouts, section-divider-slate]
mode: light
palette: ["#ffffff", "#ff0000", "#6a737c", "#caced1", "#00a4e4", "#5fc6cb", "#c1d82f", "#ffdd00"]
type_families: ["Adobe Clean (embedded: Light → Black, SemiCn)", "Adobe Clean Display", "Adobe Clean Serif (on request)"]
type_class: [humanist-sans, editorial-serif]
radius_px: []
motion: null
scores: {aesthetics: 6, originality: 7, usability: 7, craft: 6}
craft_signals: [tracking-per-point-size-table, two-logo-tiers-by-ownership, decision-tree-for-logo-choice, transparent-a-counter, crop-scale-micro-macro, voice-strikethrough-pairs]
anti_patterns: [light-grey-body-text, no-core-colour-palette, footer-credit-overprint-p35, dated-2012-infographic-examples]
---
# Adobe Corporate Brand, Internal guidelines — In-house

## 1. Snapshot
- **Subject:** A 74-page, 16:9 (959.76×540 pt) internal deck dated 08 November 2018 and marked "Adobe Confidential". It covers mission, values and tenets, the name and logo, visual identity, merchandise, templates, legal and editorial.
- **Why it's remarkable:** It treats the logo as a canvas for others. "Adobe Remix" commissions artists to reinterpret the "A", and those works become the corporate imagery library, cropped "micro" (whole A) or "macro" (texture). The colour system is deliberately open: "It's an open system without a defined color palette".

## 2. Composition & layout
Every content slide uses the same frame. A large title in Adobe Clean Light (~48 px cap-to-baseline on the 1400 px render, grey `#6a737c`-ish) sits at top-left, with a 3 px red rule underneath. The rule bleeds off the left edge and stops at the end of the title, so its length is the title width (pp15–16, 25–26, 29). The body starts at x≈65 px. A thin vertical hairline often separates a right-hand "tips"/notes column (x≈1085 on p29, also on pp6–10). The footer reads "NN Adobe Corporate Brand Guidelines | Adobe Confidential | 08 November 2018" at ~9 px. Section dividers are solid slate `#6a737c` slides with a white light-weight title (pp11, 24, 53, 58, 62, 65). The logo chapter (pp13–16) switches to a cool light-grey ground (`#caced1`, 87.5% of p16 per palette.json) to show the transparent "A". Density is moderate: text-heavy slides leave the right 40% empty (p25), while gallery slides pack 44 thumbnails into a 4×11 grid (pp30–32).

## 3. Typography
pdffonts lists **AdobeClean** (Light, SemiLight, Regular, Bold, ExtraBold, Black, with italics, plus SemiCondensed and Bold SemiCondensed), **AdobeCleanDisplay** (Regular, Bold) and **AdobeCleanSerif-Regular**. MuseoSlab-900, Myriad, Minion, Gill Sans and Univers appear only inside reproduced artwork and screenshots.
- Adobe Clean is proprietary and "NOT available for partner use" (p26). Adobe Clean Han covers JP/KR/SC/TC.
- **The most transferable spec is the tracking table on p26**, which gives tracking per point size: 4 pt +20 · 5 pt +16 · 6 pt +12 · 7 pt +8 · 8 pt +4 · 9–12 pt 0 · 14 pt −3 · 16 pt −4 · 18 pt −5 · 24 pt −6 · 30–36 pt −8. That is linear opening below 9 pt and tightening above 12 pt. Auto or metric kerning is recommended, and alternate glyphs exist for "g" and "1".
- Adobe Clean Serif is available "by request" for very long content such as legal documents.
- p27: if another font is needed in an illustration, it should "preferably" be an Adobe Originals face.
- Infographic scale (p47): marquee headline 42–36 px Adobe Clean Light at 90% black; section headline 26 px Light 90% black in sentence case; paragraph 12 px Light at 50% black; footnote 7 px Light 50% black; margins and section padding 35 px; marquee image 612 or 930 px wide.
- Hierarchy in the document itself: titles in Light, uppercase run-in heads in the heavy weight (grey, "WHEN USING THE RED TAG LOGOS, REMEMBER:"), and body in Light grey, which reads elegant but faint.

## 4. Colour
Red is defined on pp15–16 as **Adobe Red: PMS 485 C, C0 M100 Y100 K0, RGB 255/0/0, HEX FF0000**. The cover photo samples to `#df1f0d`/`#be0d02` (lit red cubes), not the spec value. p25 states that there is no fixed corporate palette: pair "dynamic" and "neutral" colours freely. Red is reserved for the corporate mark and should not be a primary colour or a text colour. Product colours live in product guides. The only defined palette is for **infographics (p51)**, read from its RGB labels:

| hex | role | approx share |
|---|---|---|
| #ffffff | slide ground | 70–93% of content slides |
| #ff0000 | Adobe Red: logo, title underline | <2% |
| #6a737c | section dividers, titles, heads | 100% of divider slides |
| #caced1 | logo-chapter ground | pp13–16 |
| #00a4e4 | infographic primary accent (blue, 0/164/228) | charts |
| #5fc6cb / #c1d82f / #ffdd00 | primary accents: teal, lime, yellow | charts |
| #ed1c24 / #ffa400 / #783cbd | secondary accents: red, orange, purple | sparing |

Each accent is shown as a dark/light pair, and greys are "various %". The page also suggests pulling complementary colours from the photo for vector overlays.

WCAG (contrast.py):
- `#6a737c` on white: 4.82:1, AA pass, just.
- White on `#6a737c` (dividers): 4.82:1.
- `#6a737c` on `#caced1` (logo-chapter text): **3.04:1, fails AA-normal**.
- `#ff0000` on white: 4.0:1, fails AA-normal. That is one reason red-as-text is banned. White on the red tag is also 4.0:1, fine for the large "Adobe" word.
- 50% black `#808080` on white (infographic paragraph spec): **3.95:1, fails AA** at the specified 12 px.

## 5. Depth & material
The guide's own pages are flat. Depth comes entirely from the imagery: Remix works are often 3-D renders (shattered-cube "A" by Robert Hodgin, p35; neon tubes, crystal and paper sculptures, pp30–33), and the cover photograph shows a room-sized lightbox "A" built from red and white cubes. Product imagery ("Oxidized", p38) is dark metallic 3-D. Clip-art is explicitly retired (p28, crossed-out examples).

## 6. Components & patterns
- **Two-tier logo:** the *red tag* (white "A" + "Adobe" in a red rectangle that must hang from a top or bottom edge, used once per piece, Adobe-only, always red) and the *standard logo* (red "A" + black wordmark, for closing a piece, edgeless layouts and licensed third parties). The p14 decision tree is "Who is the communication coming from?", then "Is there a top or bottom edge?".
- **Title underline:** a red rule from the slide edge to the end of the title.
- **"This / Not this" table (p68):** a grey header bar, alternating `#f4f4f4`/`#e5e5e5` rows and the rejected copy struck through.
- **Badges (p45):** a red tag "A" square plus the certification name on a grey bar, in three layouts.
- **Infographic anatomy (p47):** a labelled template with callout leaders to each zone.

## 7. Motion
None specified. The only animation reference is the "Don't animate" line in Incorrect logo use (p23).

## 8. Brand system
**Logo rules.** Red tag clear space is 0.25x on the open sides; the bottom- and top-placement versions differ and "are not interchangeable". The red tag is posted at exact size for every format up to 11×17″/A3 (8.5×11, 5×7 postcard, 6×9 booklet, A4, emails, banners, web pages, presentations) and scaled proportionally only above that. That is a rare "use the file as-is" rule that removes sizing judgement. Standard logo clear space is 0.5x on all sides, with a minimum of 0.375″ (stacked) and 0.24″ (horizontal). The "A" counter is always transparent so the ground shows through (p16, and p20 on buildings). The horizontal logo is only for very short spaces, and the stand-alone "A" graphic needs approval by Brand. p23 lists 16 numbered don'ts: no recolouring, skew, effects, outlines, staging, patterns, a tag with no edge, and more.

**Name.** Use "Adobe" everyday. The legal entity is only "Adobe Inc." when legally required, and the page bans "Adobe Systems Incorporated" and its variants with strikethrough (p12). There is also copy for copyright and the trademark attribution statement (pp63–64), including the September 2013 policy of no ™/® "bugs" on Adobe marks.

**Voice & tone.** There are four values (Genuine, Innovative, Exceptional, Involved) and five personality tenets (Clean, Community, Captivating, Forward, Inspiring). Each tenet gets its own slide (pp6–10) with an epigraph, imperatives such as "Limit superlatives and hyperbole" and "Respect the user journey", and a side column of visual and verbal tips such as "Use an apostrophe" and "Be concise". p68 rewrites product-speak into short human lines ("Deadlines just got less dangerous."). p70 gives a punctuation rule: periods on most Adobe.com and email headlines, none on page titles, feature headings, buttons/CTAs or email subject lines.

**Imagery.** There are three systems (p28):
1. Corporate and product imagery, made up of Remix artworks that must credit the artist and must not be rotated, mirrored, reflected, collaged or altered (pp34–35).
2. Reportage lifestyle photography, mixing "atmosphere / depersonalized / personal" shots. Photos used together must differ in emotion and camera angle (p40).
3. Conceptual illustration.

The micro/macro rule (p35) is the key technique. Crop to show the whole "A" on simple pieces such as cover slides, and zoom out until the image is texture on complex or small pieces such as section dividers and business cards. A series uses both.

**Document structure (74 pp):**
1. Cover, p1. Contents, p2.
2. Mission, values and personality tenets, pp3–10.
3. Our Name & Logo, pp11–23: company name, logos, which logo, red tag, standard, examples for print, online, events, facilities, non-standard and third-party, incorrect use.
4. Visual Identity, pp24–52: colour p25, typography pp26–27, imagery overview p28, corporate imagery pp29–37, product & program imagery p38, photography pp39–40, conceptual p41, logotypes p42, product logos p43, boxshots p44, badges p45, infographics pp46–52.
5. Branded Merchandise, pp53–57.
6. Corporate Templates, pp58–61: email signature, presentations, stationery.
7. Legal Guidelines, pp62–64.
8. Editorial Guidelines, pp65–73: Adobe Sensei, voice, Adobe.com differentiation, headline punctuation.
9. For More Information, p74: every use must go to brand review, with a 24-hour turnaround.

**Token decisions worth stealing.** The size-indexed tracking table. "Red is special", meaning the brand colour is withheld from text and UI so the mark keeps its force. An "open palette" for marketing paired with a closed accent palette only for data. An ownership-based logo tier (internal red tag vs licensable standard).

## 9. UX
It is navigable: a full TOC with page numbers, slate dividers per chapter, and a decision tree for the most common question. The rules are mostly concrete (exact sizes, clear-space ratios, tracking values). Weaknesses: body copy is light weight and light grey at small sizes, so it is tiring to read. "Be creative" is the entire colour guidance for non-data work. Several application examples (2012 holiday infographic, 2015 Creative Cloud banner) were already dated in 2018.

## 10. Craft signals
- The tracking table gives 13 size steps with signed values (p26).
- The red tag ships at fixed sizes for 10 named formats (p15).
- Clear-space diagrams label 0.25x (tag) and 0.5x (standard) on each side (pp15–16).
- Remix works carry the artist credit in the lower-right corner (Behance "Bē" + name) on templates (pp29, 35).
- The infographic anatomy states px sizes and % black for every text level (p47).
- Flaw: on p35 the "Robert Hodgin" credit overprints the footer text.

## 11. Reproduction recipe
```css
:root{
  --adobe-red:#ff0000;            /* PMS 485 C — logo only, never text */
  --slate:#6a737c; --cool-grey:#caced1; --ink-90:rgba(0,0,0,.9); --ink-50:rgba(0,0,0,.5);
  --acc-blue:#00a4e4; --acc-teal:#5fc6cb; --acc-lime:#c1d82f; --acc-yellow:#ffdd00;
  --acc2-red:#ed1c24; --acc2-orange:#ffa400; --acc2-purple:#783cbd;
  --font:"Adobe Clean","Source Sans 3",system-ui,sans-serif;
}
/* tracking by size (Adobe units = 1/1000 em) */
.t-6{font-size:6pt;letter-spacing:.012em}.t-8{font-size:8pt;letter-spacing:.004em}
.t-12{font-size:12pt;letter-spacing:0}.t-16{font-size:16pt;letter-spacing:-.004em}
.t-24{font-size:24pt;letter-spacing:-.006em}.t-36{font-size:36pt;letter-spacing:-.008em}
.slide-title{font:300 48px/1.1 var(--font);color:var(--slate);display:inline-block;
  position:relative;padding-bottom:12px}
.slide-title::after{content:"";position:absolute;left:-100vw;right:0;bottom:0;height:3px;background:var(--adobe-red)}
.divider{background:var(--slate);color:#fff;font:300 32px var(--font)}
.voice-table td.not{text-decoration:line-through;color:#6a737c}
.infographic{padding:35px}.infographic h2{font:300 26px/1.2 var(--font);color:var(--ink-90)}
.infographic p{font:300 12px/1.4 var(--font);color:#595959} /* darker than spec 50% to pass AA */
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 6 | A powerful cover and a vivid Remix gallery, but the rule pages are faint grey Light text on white and the examples look dated. |
| Originality | 7 | Artist-remixed logo imagery as the corporate visual language, and the micro/macro crop, are genuinely distinctive. |
| Usability | 7 | The logo decision tree, fixed-size red tag files, the tracking table and the voice table are directly usable. Colour guidance outside infographics is "be creative". |
| Craft | 6 | Consistent slide frame and precise specs, but low-contrast body and spec text (3.04:1 on grey pages), an overprinted credit, and inconsistent red between spec and imagery. |

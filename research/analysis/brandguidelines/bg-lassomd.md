---
id: bg-lassomd
source: brandguidelines
category: guideline
status: analyzed
title: "LassoMD"
creator: "Oleg Coada"
styles: [flat-illustration, playful-rounded, maximalist-color]
patterns: [logo-derived-geometric-pattern, mark-construction-grid, fractional-clearspace-units, numbered-serif-chapter-dividers, 60-30-10-colour-ratio, tint-ladder-swatches, split-panel-rule-page]
mode: mixed
palette: ["#915FF2", "#FFAE45", "#2A1468", "#F9537F", "#5833AD", "#FFFFFF"]
type_families: ["Montserrat SemiBold", "Domine Regular"]
type_class: [geometric-sans, transitional-serif]
radius_px: [12, 9999]
motion: null
scores: {aesthetics: 7, originality: 6, usability: 5, craft: 6}
craft_signals: [mark-on-10x-grid-with-55-degree-cut, clearspace-in-fractions-of-x, min-size-px-and-mm, overlap-multiply-to-dark-violet, pattern-built-from-mark-primitives, outline-line-pattern-variant]
anti_patterns: [white-on-soft-violet-below-aa-normal, white-on-orange-shown, no-type-scale, typos-thes-vilet-save-zone, mockup-heavy-second-half]
---
# LassoMD — Oleg Coada

## 1. Snapshot
- **Subject:** A 43-page, 1920×1080 pt brand guideline for Lasso (LassoMD), a video-marketing service for medical practices. It covers an "L" mark built from a pill and a quarter-drop, a violet/orange/deep-violet palette, Montserrat plus Domine type, and a modular geometric pattern derived from the mark.
- **Why it's remarkable:** The mark's own primitives (half-circles, quarter-rounds, rounded squares) become a tileable pattern system. Where shapes overlap they turn to deep violet, which makes the pattern feel layered and printable. That is the real asset here. The rules section is short.

## 2. Composition & layout
- **Rule pages:** a fixed split. The left panel is about 35% wide (0–496 px of the 1400 px render), always in Very Dark Violet #2A1468, with a white Montserrat SemiBold H2 of about 24 px at x=30/y=48 and Domine body of about 18 px at ~1.3 leading. The right panel is about 65% wide and white, with specimens floating in it.
- **Specimen cards (p14–15):** light grey #F5F5F5-ish with a radius of about 12 px, and a grey Montserrat label of about 13 px above each.
- **Chapter dividers (p3, p6, p17, p21, p25):**
  - a full-colour field;
  - a giant Domine numeral 1–5, about 520 px tall (≈66% of page height), right of centre;
  - the chapter title in white Montserrat of about 60 px bottom-left at x≈78;
  - a 1.5 px line drawing in orange or violet that traces the mark's outline (pill plus diagonal plus arc) at architectural scale.
- **Back half (p26–42):** full-bleed mockups with no rules: tote, billboard, phone case, shopfront, posters, stationery.

## 3. Typography
pdffonts confirms two embedded families: **Montserrat-SemiBold** and **Domine-Regular**.
- **Montserrat SemiBold:** the wordmark "Lasso", headlines, labels and buttons. On p22 the specimen runs from about 85 px ("Lasso") down to about 60 px lines, with 1 px dark-violet rules between specimen rows.
- **Domine Regular** (transitional/Clarendon-ish web serif): body copy and chapter numerals. The book says it "shines at 14 and 16 px" and can drop to 11–13 px.
- **UI sample (p24):**
  - headline Montserrat SemiBold at about 72 px, line-height ~1.1;
  - sub-copy Domine at about 22 px;
  - buttons in Montserrat SemiBold all caps at about 16 px with tracking of about +0.06 em, in a 270×76 px pill;
  - the primary button is filled orange #FFAE45 with dark-violet text, and the secondary is outlined with a 3 px violet stroke.
- No type scale, leading or tracking rules are given. Sizes above are measured from the renders.

## 4. Colour
Values are taken from p18/p19 (HEX, RGB, CMYK, PMS for primaries) and match palette.json (p001: #915ff2 at 38%, #2a1467 at 29%, #ffae45 at 21%).

| Hex | Name / role | Stated share |
|---|---|---|
| #915FF2 | Soft Violet: primary field (PMS 265 C) | 60% |
| #FFAE45 | Light Orange: accent shape, primary button (PMS 1365 CP) | 30% (shared with dark violet) |
| #2A1468 | Very Dark Violet: text, rule-page panel, shape overlaps (PMS 2755 C) | 30% (shared with orange) |
| #F9537F | Soft Pink: secondary | 10% (shared) |
| #5833AD | Dark Violet: secondary | 10% (shared) |
| #FFFFFF | ground for patterns and specimens | — |

- **60/30/10 rule (p20):** a usage bar gives Soft Violet 60%, Orange plus Dark Violet 30%, and Pink plus Dark Violet 10%. It is a clear, rare instruction in a small brand book.
- **Tints (p19):** each swatch carries four tints (roughly 85/60/40/15%) in a vertical strip, without values.

WCAG (contrast.py):
- White on #2A1468: **15.02:1**.
- #2A1468 on #FFAE45: **8.15:1**, the button pairing.
- White on #915FF2: **4.10:1**, which fails AA for normal text. The p24 hero uses white Domine at about 22 px on Soft Violet, which squeaks by only as large text.
- #2A1468 on #915FF2: 3.66:1.
- White on #F9537F: 3.2:1.
- **White on #FFAE45: 1.84:1.** The "alternative use" white logo on orange (p14) is shown as approved.

## 5. Depth & material
- The system is flat.
- **Overlap:** where an orange and a violet shape intersect, the intersection becomes #2A1468, a pseudo-multiply. The mark itself has a dark-violet sliver where the pill and drop overlap.
- Pattern shapes have tiny corner radii of about 4 px on their straight corners, which softens them without making them blobby.
- Mockups (flags, lanyard, bus-stop sign, billboard, letterpress-look cards) add depth only through photography.

## 6. Components & patterns
- **Identity patterns (p26–36), three variants:**
  - **(a) Loose scatter (p29):** half-discs, quarter-rounds and circles on white, repeating every ~442 px horizontally. Three repeats are visible.
  - **(b) Dense tile grid (p31, p33):** an approximately 10×6 module grid where every cell is a primitive at one of four rotations.
  - **(c) Outline lattice (p35–36):** the "L" pill shapes drawn as 3 px violet and orange strokes, interlocked into a chain-mail with four-point star negative spaces.
- **Primary UI:** pill buttons (fully rounded), filled orange and outlined violet.
- **Composition (cover, p24):** large cropped circle and pill fragments bleeding off the edges.
- **Stationery (p37–42):** pattern on the back of the business card and a large quarter-round on the letterhead footer.

## 7. Motion
None specified.

## 8. Brand system
**Logo rules:**
- **Construction (p10):** the mark sits on a 10×10 unit grid. The pill is 5x wide by 10x tall. The drop is 5x, built from a 5x circle plus a corner radius of x. The diagonal shoulder runs at 55°, and the small corner radii equal x.
- **Safe zone (p11, misspelled "Save Zone"):**
  - Horizontal lockup: x/2 on the sides, x/6 above and below the mark, x/3 between mark and wordmark, wordmark width 2.5x, wordmark cap height x/1.5.
  - Mark alone: x/2 on each side.
  - Units are fractions of the mark width x. This is precise, but it uses unusually small margins (x/6 vertical).
- **Lockups (p12):** horizontal (primary), stacked, and mark-only.
- **Minimum size (p13):** mark 20 px / 7 mm, stacked 32 px / 11 mm, horizontal 20 px / 7 mm in height.
- **Colourways (p8, p9, p14):**
  - grayscale on white or black;
  - monocolour outline (the mark drawn as a stroke);
  - primary: colour mark plus dark-violet wordmark on light;
  - secondary: on dark violet;
  - alternatives: on photo, on violet, and on orange in white or translucent.
- **Misuse (p15):** six don'ts: boxing, stretching, rotating, busy backgrounds, strokes and recolouring.

**Voice (p4):** four bullet adjectives: New Tech, Professional, Trustworthy, Confident/Competent. There is a target audience (small practices under $1M a year, ages 30–60) and a mission line, "Transform medical practices into thriving businesses." There are no writing examples.

**Imagery:** a single smiling-professional cut-out photo against violet/orange shapes (p4, p16). No photography rules.

**Document structure:**
1. Cover (p1)
2. Welcome (p2)
3. Brand Overview: voice and tone, audience, mission, flag mockups (p3–5)
4. Logo Overview: overview, grayscale, monocolour, construction, safe zone, lockups, scale, correct and incorrect use, signage mockup (p6–16)
5. Color: primary specs, palette with tints, usage ratio (p17–20)
6. Typography: Montserrat, Domine, UI sample (p21–24)
7. Brand Elements: identity patterns and mockups (p25–36), identity collateral and stationery (p37–42)
8. Closing mark and credit (p43)

**Token decisions worth stealing:**
- Clear space expressed as fractions of the mark (x/2, x/3, x/6) on a dimensioned grid.
- An explicit 60/30/10 colour ratio bar.
- A pattern library derived from the logo's construction primitives, with an overlap colour rule (orange ∩ violet = #2A1468).
- Giant serif numerals as chapter markers to contrast the geometric sans.

## 9. UX
- **Easy to follow:** logo geometry, clear space, minimum sizes and misuse.
- **Missing:**
  - a type scale, leading or hierarchy rules;
  - a grid or margins;
  - CMYK/PMS for the secondaries;
  - pattern construction rules (module size, permitted rotations, density) beyond the examples;
  - accessible colour pairings. White on Soft Violet and white on Orange are presented as valid.
- About 40% of the book (p26–42) is mockups that show but do not instruct.
- Copy has typos ("Thes", "vilet", "Save Zone").

## 10. Craft signals
- The mark is drawn on a 10×10 unit grid with a 55° diagonal and an x-radius on its corners (p10).
- Clear-space fractions (x/2, x/3, x/6, x/1.5) are labelled on a dimensioned table.
- Minimum sizes come in pixels and millimetres for three lockups.
- Pattern overlaps resolve to the darkest palette colour rather than to transparency.
- The divider line art reuses the mark's pill-plus-55°-diagonal silhouette at about 10× scale, in 1.5 px strokes.
- The pill button proportions (≈270×76 px) echo the pill in the mark.

## 11. Reproduction recipe
```css
:root{
  --violet:#915FF2; --orange:#FFAE45; --ink:#2A1468; --pink:#F9537F; --violet-dk:#5833AD; --paper:#fff;
  --font-head:"Montserrat",system-ui,sans-serif; --font-body:"Domine",Georgia,serif;
}
body{font:400 16px/1.5 var(--font-body);color:var(--ink);background:var(--paper)}
h1,h2,.btn{font-family:var(--font-head);font-weight:600}
.hero{background:var(--violet);color:#fff}
.hero h1{font-size:72px;line-height:1.1}
.btn{border-radius:9999px;padding:24px 44px;font-size:16px;letter-spacing:.06em;text-transform:uppercase}
.btn--primary{background:var(--orange);color:var(--ink)}
.btn--ghost{border:3px solid var(--violet);color:#fff;background:transparent}
.rule-page{display:grid;grid-template-columns:35% 1fr}
.rule-page aside{background:var(--ink);color:#fff;padding:30px}
.chapter-num{font:400 66vh/1 var(--font-body);color:var(--violet)}
/* pattern primitives: overlap resolves to ink */
.tile{width:120px;aspect-ratio:1;border-radius:4px}
.half{background:var(--violet);border-radius:0 9999px 9999px 0}
.quarter{background:var(--orange);border-radius:0 100% 4px 4px}
.overlap{background:var(--ink)}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 7 | The violet/orange/ink trio and the derived geometric patterns are lively and cohesive. The UI sample and dividers look good. |
| Originality | 6 | Logo-derived Bauhaus-tile patterns are a familiar move. The outline-lattice variant is the freshest bit. |
| Usability | 5 | Strong on logo maths, weak on type hierarchy, grid, pattern rules and accessible colour pairings. Half the book is mockups. |
| Craft | 6 | The construction and clear-space diagrams are precise, but there are typos, shown contrast failures and no secondary print specs. |

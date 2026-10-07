---
id: bg-mastercard-foundation
source: brandguidelines
category: guideline
status: analyzed
title: "Mastercard Foundation — Brand Architecture and Guidelines v4.3"
creator: "In-house"
styles: [corporate-clean, minimal-swiss, photo-led]
patterns: [gradient-keyline-header, logo-derived-sizing-grid, partner-lockup-optical-sizing, program-name-artwork, accessible-colour-variants-table, weight-decreases-with-size, x-unit-clearspace, sub-brand-architecture-tree]
mode: light
palette: ["#ffffff", "#141413", "#e3dfd7", "#ff671b", "#f38b00", "#ffc81f", "#2f7b6b", "#d22a2f"]
type_families: ["Mark Offc for MC (FF Mark custom, embedded)", "Mark for MC Narrow (embedded)", "Arial (internal fallback)"]
type_class: [geometric-sans, condensed]
radius_px: []
motion: null
scores: {aesthetics: 6, originality: 5, usability: 9, craft: 7}
craft_signals: [logo-height-divided-into-10-x-units, page-short-side-divided-into-7-logo-squares, wcag-variant-for-every-colour, 12-col-grid-with-pt-margins, gutter-equals-3-baseline-units, print-and-web-size-pairs]
anti_patterns: [conflicting-hex-values-between-pages, two-different-oranges, primary-orange-used-as-text-fails-aa, template-like-page-design]
---
# Mastercard Foundation Brand Architecture and Guidelines — In-house

## 1. Snapshot
- **Subject:** An 89-page, US-letter landscape (792×612 pt) manual, "Version 4.3 / June 2023". It covers the Mastercard Foundation mark, a large brand-architecture section on programs and partners, the brand elements, and applications. The original URL (mastercardfdn.org/wp-content/uploads/2023/07/…) now returns HTTP 410 Gone, so this analysis uses the copy recovered from the Wayback Machine.
- **Why it's remarkable:** It is an unglamorous manual but a very operational one. Almost every placement rule is a ratio taken from the logo (10 "x" units, 7 squares across the short side, 10 or 12 sizing lines for partner logos). It also includes a per-colour WCAG table (p57) giving an AA and an AAA-safe shade for every brand hue.

## 2. Composition & layout
Every interior page uses the same template. A running head in grey Mark Medium (~11 pt) reads "Mastercard Foundation: Brand Architecture and Guidelines", with "June, 2023" and the folio on the right. Below it sit a hairline rule at y≈87/1069 px, a bold title block at top-left and a second hairline at y≈216. A one-third text column on the left (x 64–430 of 1400 px) holds the rules, and a two-thirds stage on the right holds the specimens. A tiny pale "©2023 Mastercard Foundation" footer sits at the bottom-left. Both the cover and the back cover use one red-to-orange gradient band (~605×16 px at 1400 px width) above the wordmark. The rhythm is very regular and very white. Whitespace takes about 85–95% of most pages (palette.json shows `#ffffff` at 79–95%).

The internal print grid is specified on p71: 12 columns on letter portrait, with margins of top 27 pt, bottom 63 pt, left 40.5 pt and right 27 pt. The gutter is 13.5 pt, which is "3 baseline units", so the baseline is 4.5 pt. The large bottom margin holds the folio and logo. The three-column grids on pp74–75 sit inside this 12-column grid.

## 3. Typography
pdffonts lists **MarkOffcForMC** (Thin through Black, with italics), **MarkForMCNrw** (Book–Heavy), MarkScOffcForMC (small caps) and MarkOffcPro. These are the Mastercard-licensed cuts of FF Mark, and p45 names the face "FF Mark". Arial, Calibri, Lato, Montserrat and Myriad are also embedded, but only inside screenshots and partner artwork.
- **Roles (p48):** Mark for MC is used for headlines, subtitles, large typography and small caps. Mark for MC Narrow is used for running text, data-heavy text, graphs and legends. The cut-over point is 12 pt in print or 14 px on screen (pp46–47).
- **Scale with inverse weight (p49):** "as size increases, weight decreases". The steps are Extra Light 90 pt/120 px, Light 60/90, Regular 40/60, Book 24/36 and Book 16/24. Mark for MC Narrow (p50) runs Regular 12 pt/18 px, Book 10.5/16, Book 9/14 and Medium 7/12. Every size is given as a print/web pair at a fixed ~1.33–1.5 multiplier.
- **Contrast (p51):** contrast comes from either size (headline 70 pt against subtitle 24 pt) or weight (Bold against Book at the same 16 pt), and the page says to use only one at a time.
- **Internal comms (p52):** Arial Regular, Italic, Bold and Bold Italic, because Microsoft templates must render on any machine.
- The manual's own titles are set in Mark Bold at ~30 px with tight leading, and body text is Mark Book at ~16 px on 1400 px renders.

## 4. Colour
Values below are taken from the document's own colour pages (p7 mark, p53 brand palette, p57 accessibility). Palette.json confirms the mark red and orange as `#e41b22`/`#fa9e1a` in the render.

| hex | role | approx share |
|---|---|---|
| #ffffff | page / dominant ground | 80–95% |
| #141413 | Dark Grey background, text (p53 says HEX 141413; p57 says 231F20) | 3–10% |
| #e3dfd7 | Light Grey background, Warm Grey 2 C (p57 lists D5D0CA) | accent panels |
| #ff671b | Primary Orange, PMS 166 C | highlights, call-outs |
| #f38b00 / #ffc81f / #8db92e | Secondary Gold / Yellow / Green | charts, illustration |
| #d22a2f / #4fcdb0 | Accent Red / Teal, "one at a time" | emphasis |
| #2f7b6b | Program-names green, reserved for name artwork only | wordmarks |
| #de3c95 | Magenta, "used only for internal communications" | internal |
| #eb001b / #ff5f00 / #f79e1b | Mark Red / Orange / Yellow (p7) | logo only |

WCAG (contrast.py):
- `#000000` on `#ffffff`: 21:1. `#141413` on `#e3dfd7`: 13.87:1.
- `#2f7b6b` on white: 5.04:1, AA pass. `#d22a2f` on white: 5.11:1, AA pass.
- `#ff671b` on white: **2.91:1, fails even AA-large**. The manual's own p57 table records this (2.91:1) and recommends `#b24813` (5.55:1) or `#7f330d` (8.7:1) instead. Yet p79 sets call-out quotes in "Mastercard Orange text", so the document breaks its own accessibility page.
- Black on Yellow `#ffc81f`: 13.53:1, which suits the case-study panels (20% yellow tint).

## 5. Depth & material
The system is completely flat, with no shadows or radii. The only "effects" are the multiply overlap of the two circles in the mark (red over yellow giving `#ff5f00`) and the linear gradient keyline. The rule against effects is explicit: p28 says "Do not apply effects to name artwork", and the p10 common mistakes include a recoloured, outlined or shadowed mark. Mockups (bottles and hoodies on pp86–88) are the only 3-D renderings.

## 6. Components & patterns
- **Gradient keyline (p79):** an Orange→Yellow gradient, 10 pt thick as the running header bar at the top of consecutive pages, 2 pt as the footer keyline, and 1.1671 in (half the left column) above orange call-out text. The "title area" variant (p37) makes the band the width of the title's lower-case "L", and the band sits three band-heights above the title.
- **Case-study panel:** a 20% Mastercard Yellow tint fill with black text. A label column on the left is set in caps ("CASE STUDY") and the body sits on the right.
- **Program-name artwork (pp25–28):** program names are set in Mark for MC Bold in `#2f7b6b`, in one-line and two-line versions. They always sit flush-left below the logo and never inside a shape.
- **Icons (pp62–68):** monoline pictograms with geometric round forms matching the circles, built from a library in the "Mastercard Design Center". They come in black on light, white on dark, and a single-hue tint version (p68).
- **Charts (p80):** use two colours per chart (Mastercard Yellow and Orange) plus tints, on 20% Light Grey backgrounds.
- **Social avatars (p72):** a square and a circle, each on a 14-row grid. The logo fills the space between rows 4 and 10, and the words always stay with the symbol.

## 7. Motion
There is only static guidance (p82). The logo must be built to its final state, with the circles coming together or emerging from one circle, and it must hold long enough on the complete mark. The mark must never break apart, fragment, or morph into another object. No durations or easing are given, and the example frames show coloured dots sliding into the overlap.

## 8. Brand system
**Logo rules.** There is one configuration only: vertical, circles over a two-line lowercase "mastercard foundation". It comes in full-colour (strongly preferred), greyscale (K75 / K52 / K28) and solid (black, white or one colour), each positive and reversed (pp5, 7). The ™ is Mastercard Yellow in RGB and Pantone, and black or white in CMYK. Clear space is "x" = the combined height of the two words on all four sides (p4/p8). Minimum size is 24 px / 48 pt on screen and 8.9 mm (0.35 in) in print. On websites the logo is a fixed 160 px wide (p29). There are 12 numbered misuses on p10, from recolouring circles to enclosing the mark in a shape. The name is always "Mastercard Foundation", with a capital M and a lower-case "c" in "card" (p9: MasterCard, Master card and Master-card are all wrong).

**Placement maths (p29–31).** The logo height is divided into 10 squares, and that unit "x" drives every spacing. Space to the left of and above the logo is at least 50% of one circle's width. There are 6x below the logo, the program name is 2x tall, and there are 5x from the program name to the gradient line. Title spacing equals three gradient-line heights. The logo width is one seventh of the page's shortest side (vertical and narrow-vertical formats) or set by page height (horizontal). The billboard pages (pp33–35) apply the same rule with 12 or 8 squares for 96-sheet and 48-sheet billboards. **Partners (pp15–20, 32):** divide the Foundation logo into 10 sizing lines, bottom-align the partner logo, then size it to the nearest line so it looks optically equal (for example "sized to the eighth line"). The "In partnership with" lock-up is a supplied file and must never be retyped (p20).

**Brand architecture.** The Foundation is a branded house. Programs, events and publications sit under the masterbrand, and "EleV" and "Saving Lives and Livelihoods" are named as exceptions that keep their own identity (pp22–23). "Young Africa Works" is a strategy shown as a hashtag, never a logo (p21).

**Imagery.** Photography should be "human, natural, aspirational", "highly saturated", and show people in their natural environment doing what they normally do. Consent is required, guardian consent for under-18s, and credits use the format "[Photographer] for the Mastercard Foundation" (p58). Black-and-white photos are allowed for the Secondary Education in Africa portfolio, converted via CMYK in Photoshop for richer blacks (p60). Illustration must be commissioned from African and/or Indigenous illustrators, never be "cartoonlike or a caricature", and avoid stock (p61).

**Voice.** There is no voice chapter. The tone is set only by imagery rules and the case-study example copy.

**Document structure (89 pp):**
1. Cover, p1. Table of contents, pp2–3.
2. Our Logo, pp4–10: top five things, Brand Mark, trademark, colour specs, minimum size, name in text, mistakes.
3. Brand Architecture, pp11–43: introduction, pillars, visual treatment, co-branding (Foundation lead, partner lead, balanced, multiple, mistakes), Young Africa Works, exceptions, Enterprise Toolkit, name artwork, scale and placement, title areas, gradated band, "how it comes to life".
4. Brand Elements, pp44–68: Typography pp44–52, Colour pp53–57, Photography pp58–60, Illustration p61, Icons pp62–68.
5. Applications, pp69–88: Layouts pp69–71, Digital p72, Brochures p73, Grids pp74–75, Internal documents pp76–78, Design elements p79, Charts p80, Email headers p81, Animations p82, PowerPoint p83, Business card p84, Merchandise pp85–88.
6. Back cover, p89.

**Token decisions worth stealing.** (1) A colour table giving AA and AAA variants of every hue, with the ratio printed under each swatch. (2) Spacing expressed in logo-derived units instead of mm. (3) A body/display split by size threshold (12 pt / 14 px) between the regular and narrow cuts. (4) Inverse weight-to-size scaling for display type.

**Inconsistencies observed.** Light Grey is `#E3DFD7` on p53 and `#D5D0CA` on p57. Dark Grey is `#141413` on p53 and `#231F20` on p57. Mark Orange is `#FF5F00` but Primary Orange is `#FF671B`. The gradient is described as "Orange and Yellow" (p79) but drawn red→yellow on the cover.

## 9. UX
For a designer this manual is easy to apply. Every rule has a numeric unit, a correct/incorrect pair, or a downloadable lock-up. Each page has a single topic, and the TOC is page-exact. Weak points: the brand-architecture section (33 pages) dominates and repeats co-branding cases, and the "how it comes to life" pages are screenshots rather than rules.

## 10. Craft signals
- The logo is divided into exactly 10 units, labelled 1–10 beside the mark on pp29–33.
- A gutter of 13.5 pt = 3 × 4.5 pt baseline units (p71).
- The type spec gives a print/web pair for every step: 90 pt/120 px … 16 pt/24 px.
- p57 prints the WCAG ratio, CMYK, RGB and HEX for 22 swatches.
- Clear space is drawn as four "x" circles around the mark (p8).
- The partner sizing rule is bottom-aligned and snaps to one of 10 lines (pp15–19).

## 11. Reproduction recipe
```css
:root{
  --mcf-white:#ffffff; --mcf-ink:#141413; --mcf-light-grey:#e3dfd7;
  --mcf-orange:#ff671b; --mcf-orange-aa:#b24813; --mcf-orange-aaa:#7f330d;
  --mcf-gold:#f38b00; --mcf-yellow:#ffc81f; --mcf-green:#8db92e;
  --mcf-red:#d22a2f; --mcf-teal:#4fcdb0; --mcf-program-green:#2f7b6b;
  --mcf-keyline:linear-gradient(90deg,#ff671b 0%,#ffc81f 100%);
  --font-display:"Mark Pro","FF Mark",Arial,sans-serif;   /* Mark for MC */
  --font-text:"Mark Pro Narrow","FF Mark",Arial,sans-serif;
  --baseline:4.5pt; --gutter:calc(var(--baseline)*3);
}
.keyline{height:10pt;background:var(--mcf-keyline);}          /* running header */
.keyline--footer{height:2pt;background:var(--mcf-keyline);}
.callout{font:700 22pt/1.2 var(--font-display);color:var(--mcf-orange-aa);}
.callout::before{content:"";display:block;width:1.1671in;height:6pt;margin-bottom:12pt;background:var(--mcf-keyline);}
.case-study{background:color-mix(in srgb,var(--mcf-yellow) 20%,#fff);color:#000;display:grid;grid-template-columns:1fr 2fr;padding:16pt;}
.display-xl{font:200 120px/1 var(--font-display);}   /* Extra Light at 90pt print */
.display-l{font:300 90px/1.05 var(--font-display);}
.body{font:400 16px/1.45 var(--font-text);}
.logo-web{width:160px;}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 6 | Tidy and calm, with lots of white space and a nice gradient band, but every page is the same template with a specimen dropped in. |
| Originality | 5 | A standard corporate manual. The only distinctive devices are the gradient keyline and the logo-derived sizing grids. |
| Usability | 9 | It is unusually prescriptive: numeric spacing units, partner sizing, web logo width, a WCAG variant table and internal-comms fallbacks. |
| Craft | 7 | Precise grids and units, held back by conflicting hexes between p53 and p57, two oranges, and orange text that its own accessibility page fails. |

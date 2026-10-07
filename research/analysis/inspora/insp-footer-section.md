---
id: insp-footer-section
source: inspora
category: Web
status: analyzed
title: "footer section"
creator: "Pranav (@PranavOriginals)"
styles: [editorial-serif, duotone, dither-halftone, luxury]
patterns: [illustrated-footer-landscape, four-column-link-footer, inline-newsletter-field, short-rule-under-headings, italic-legal-links, contact-icon-list]
mode: dark
palette: ["#0c3b88", "#ede1cb", "#ded5c7", "#3a5f99", "#8291ac", "#ffffff"]
type_families: ["EB Garamond / Cormorant Garamond-style old-style serif (likely)"]
type_class: [editorial-serif]
radius_px: [0]
motion: null
scores: {aesthetics: 9, originality: 8, usability: 7, craft: 8}
craft_signals: [two-ink-duotone-etching, paper-grain-on-flat-blue, 40px-rule-under-column-heads, italic-for-voice-roman-for-links, square-cornered-input-matches-print-feel, lone-rider-on-centre-axis]
anti_patterns: [placeholder-contact-data, small-italic-legal-text]
---
# footer section — Pranav

## 1. Snapshot
- **Subject:** A single 1671×941 footer for "sequel", a tableware/decor shop. It has four link columns and a newsletter field on a royal-blue field. The bottom ~38% is an engraved, blue-on-cream desert landscape with a lone cowboy on horseback.
- **Why it's remarkable:** It is a strict two-ink print aesthetic (cobalt and cream, like blue-and-white porcelain). An engraving-style illustration turns the end of the page into a horizon, so the footer is a destination, not leftovers.

## 2. Composition & layout
- **Grid:** five columns.
  - **Brand column** (x≈110→360): star logomark with the "sequel" wordmark at about 48 px, an italic three-line mission, contact rows with icons (email, phone, location) at a 37 px pitch, and four social icons (24 px, 60 px pitch) at y≈476.
  - **Link columns:** SHOP (x≈505), ABOUT US (x≈746) and HELP & SUPPORT (x≈990), about 240 px apart.
  - **Newsletter** (x≈1283→1585).
- **Spacing:** column heads at y≈148, then a 40 px × 1.5 px cream rule at y≈180, then links starting at y≈213 with a ~36 px pitch.
- **Legal row:** italic, right-aligned at y≈498, with pipe separators.
- **Illustration:** the horizon begins at y≈570 (61% down) with mountains peaking right of centre. The rider sits at x≈760, almost exactly on the page's central axis, at y≈770, small (about 130 px) for scale and solitude.
- **Margins:** about 110 px left and 86 px right. The text block occupies the upper 55%.

## 3. Typography
- **One family:** an old-style Garamond serif (EB Garamond / Cormorant-like: small x-height, calligraphic italic).
- **Roles:**
  - column heads in caps at about 19 px with +0.12 em tracking;
  - links in roman at about 19 px;
  - the mission line, newsletter blurb, input placeholder and legal links in italic (about 19 px, legal about 17 px);
  - the wordmark in lowercase roman at about 48 px.
- **Rule:** roman = navigable, italic = voice/supporting text. Caps with tracking mark structure.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #0c3b88 | cobalt field / engraving ink | 61% |
| #ede1cb | cream paper / text / illustration ground | 15% |
| #ded5c7 / #c5c2bf | cream mid-tones in hatching | 12% |
| #3a5f99 / #8291ac | optical blend of hatching | 8% |
| #ffffff | logo star, icons | <1% |

WCAG checks:
- Cream text #ede1cb on cobalt #0c3b88 is 8.13:1, and white is 10.52:1.
- Inverse (blue ink on cream, as in the input's arrow button) is 8.13:1.
- Mid-blue #3a5f99 on cream is 4.95:1.

Everything passes AA. A strictly limited two-ink palette produces robust contrast by design.

## 5. Depth & material
- **Flat with print texture:** the blue field carries a fine speckled grain (like paper or risograph) and there are no shadows.
- **Depth through illustration only:** dense hatching for near grass, finer horizontal hatching for distant hills, and atmospheric lightening near the horizon. This is classic engraving perspective.
- **Input:** a 1.5 px cream outline rectangle with square corners and a solid cream square button with a blue arrow. No radius anywhere.

## 6. Components & patterns
- Four-column link footer with short underline rules under the headings.
- Contact list with 20 px solid glyphs.
- Social row of four glyphs: Facebook, X, Instagram, LinkedIn.
- Newsletter: italic prompt, outlined input (about 300×50 px) and a 50 px square submit button.
- Legal row in italic with "|" separators.
- An illustration band as the visual end-cap.

## 7. Motion
Still image, so no motion was observed. It would suit a subtle parallax (hills slower than grass) or the rider drifting slowly across on scroll. That is speculative.

## 8. Brand system
n/a — not a brand system, but strong identity cues:
- a four-point star logomark (compass/sparkle);
- blue-and-cream porcelain colours fitting tableware;
- Garamond for a heritage, crafted tone;
- a Western/desert engraving suggesting journey and craftsmanship ("Our Story", "Craftsmanship").

## 9. UX
- **Strengths:** Clear, conventional IA (Shop / About / Help / Newsletter); good contrast; adequately sized links; a clear newsletter affordance.
- **Risks:**
  - The placeholder contact data ("+91 00000 00000") is template content.
  - The italic placeholder may be mistaken for a label.
  - Legal links at 17 px italic are small.
  - The illustration adds page weight (needs optimised webp or SVG).

## 10. Craft signals
- The palette is two inks: every tone in the illustration is a mix of #0c3b88 and #ede1cb (hatching density, not new colours).
- A short 40 px cream rule under each column head is repeated exactly across four columns.
- Italic and roman carry roles (voice vs navigation) consistently, including the input placeholder.
- The rider is placed on the page's central axis beneath the gap between columns 2 and 3.
- Square corners on the input and button match the print and engraving idiom.
- A fine grain overlay on the flat blue avoids digital flatness.

## 11. Reproduction recipe
```css
:root{--ink:#0c3b88;--paper:#ede1cb;--serif:"EB Garamond","Cormorant Garamond",Garamond,serif}
.footer{background:var(--ink) url(grain.png);color:var(--paper);font:400 19px/1.9 var(--serif);
  display:grid;grid-template-columns:1.5fr 1fr 1fr 1.2fr 1.3fr;gap:32px;padding:120px 86px 0 110px;position:relative}
.footer h4{font:400 19px var(--serif);letter-spacing:.12em;text-transform:uppercase}
.footer h4::after{content:"";display:block;width:40px;height:1.5px;background:var(--paper);margin:14px 0 18px}
.footer a{color:var(--paper);text-decoration:none}
.footer em,.footer .legal a,.footer input::placeholder{font-style:italic}
.news{display:flex;border:1.5px solid var(--paper)}
.news input{flex:1;background:none;border:0;color:var(--paper);padding:12px 22px;font:italic 19px var(--serif)}
.news button{width:50px;background:var(--paper);color:var(--ink);border:0}
.landscape{grid-column:1/-1;margin:72px -86px 0 -110px;aspect-ratio:1671/371;
  background:url(desert-engraving.webp) bottom/cover}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 9 | A disciplined two-ink print look with an evocative engraving; elegant serif rhythm. |
| Originality | 8 | An illustrated landscape footer in porcelain blue is distinctive for e-commerce. |
| Usability | 7 | Conventional, legible IA with strong contrast; small italic legal links and placeholder data. |
| Craft | 8 | Consistent rules, type roles and palette discipline throughout. |

---
id: bg-brand-icons
source: brandguidelines
category: template
status: analyzed
title: "Brand icons"
creator: "Designer Goods (UI8 seller)"
styles: [corporate-clean, minimal-swiss, hairline-ui]
patterns: [logo-grid-on-white-cards, four-up-card-grid, scalloped-caption-band, format-chip-row, grid-claim-in-copy]
mode: dark
palette: ["#121212", "#FFFFFF", "#1D1D1F", "#2D68FF", "#00A656", "#ADB7BE"]
type_families: ["CircularXX (UI8 storefront)", "Card caption typeface not identifiable from pixels"]
type_class: [grotesk]
radius_px: [16]
motion: null
scores: {aesthetics: 6, originality: 3, usability: 6, craft: 6}
craft_signals: [five-by-three-logo-grid, scalloped-caption-edge, consistent-icon-pitch, single-white-ground-for-marks]
anti_patterns: [third-party-trademarks-as-product, generic-subject, caption-text-small]
---
# Brand icons — Designer Goods (UI8 seller)

## 1. Snapshot
- **Subject:** UI8 product page for a set of 60 social-media and digital-product brand logos sold as vector files (Sketch, SVG, PDF, PNG, EPS, IconJar), priced at $9. Captured from a Wayback Machine snapshot dated **2025-05-16** (`web/20250516235807`), with no redirect.
- **Why it's remarkable:** The preview is the product. Four white cards each hold 15 marks in a 5×3 grid, so the whole set can be judged at a glance, and the marks keep their own brand colours. The UI around them is a neutral dark storefront.

## 2. Composition & layout
- **Preview grid:** a 2×2 grid of white cards, each 652×492 px at 1440 px, with a 24 px gutter and a 16 px corner radius.
- **Marks:** about 63 px square, on a column pitch of about 125 px and a row pitch of about 119 px. Each card is 5 columns by 3 rows, so there are 60 marks in total.
- **Caption band:** the bottom 80 px of each card is a light grey band with a scalloped top edge and a centred caption.
- **Header:** the 65 px toolbar sits above an H1 at x≈56 px. The subtitle reads "60 popular social media and digital product brands on a 24px grid".
- **Mobile (390 px):** four cards stack vertically at a 16 px gutter. Each card keeps its 5-column grid, with marks at about 40 px.

## 3. Typography
- **Storefront UI:** CircularXX, the same family as the other UI8 pages in this batch. Sizes are 15 px (42), 13 px (22) and 16 px (19). The census also shows 20 px (16) and 28 px (10) headings.
- **Tracking:** −0.28 px on 129 nodes.
- **Card captions:** the caption text ("60 popular brand icons", "Premium quality, production ready") is a small bold grey, about 13 px. Its face is not identifiable from the pixels, and it looks different from the storefront UI type.

## 4. Colour
| Hex | Role | Notes |
|---|---|---|
| #121212 | page ground | census bg (18, 18, 18) on 7 nodes; ≈50% of tile pixels |
| #FFFFFF | preview card ground | palette sample; the mark field |
| #1D1D1F | format chips and dark panels | palette sample |
| #ADB7BE | body text | census text colour, 75 nodes |
| #2D68FF | Add to cart | accent, as on other UI8 pages |
| #00A656 | download bar and check icons | green accent |

The marks themselves use their owners' brand colours. The template imposes no palette on them, and the caption band is a neutral grey.

**WCAG (contrast.py), storefront pairs:**
- #FFFFFF on #121212: **18.73:1**.
- #ADB7BE on #181818: **8.70:1**.
- #2D68FF on #181818: **3.84:1** (fails AA for normal text).
- #FFFFFF on #2D68FF: **4.63:1** (passes).

The caption grey on the white band was not sampled, so it is not rated.

## 5. Depth & material
- Flat. Each card sits on the dark ground with no shadow.
- The scalloped caption band reads as the only texture. It is a shape edge, not a material.

## 6. Components & patterns
- **Logo grid:** a 5×3 grid of marks per card, four cards in a 2×2 layout.
- **Format chips:** a row of five dark circles with Sketch, Photoshop, Illustrator, Figma and IconJar glyphs.
- **Pill CTA:** the price sits in the Add to cart label, as on other UI8 pages.

## 7. Motion
Storefront transitions only, from the census: `color .2s ease` (38), `fill .2s ease` (17), `opacity .4s ease` (13). The token summary shows a single `transform .167s`. No motion is visible in the stills.

## 8. Brand system
n/a — not a brand system. The "system" is the marks themselves: 60 logos on one grid. The copy claims a 24 px grid and vector output at any size, but no construction is shown. The identity cues are the Designer Goods seller mark, a lavender-to-white "D" glyph in a white circle.

## 9. UX
- The grid lets a buyer confirm recognisability at a glance, which is what the product needs to prove.
- Format chips show all five output types without text.
- The description and highlights sit below the fold and are short.
- The set is commercially sensitive. It is a bundle of third-party trademarks, and the page does not discuss licence limits.

## 10. Craft signals
- The 5×3 grid repeats exactly across all four cards, with the same column and row pitch.
- The caption band has a consistent scalloped edge across all four cards.
- The white field gives every mark the same neutral ground.
- Card radius is consistent at 16 px.

## 11. Reproduction recipe
```css
.icon-set{display:grid;grid-template-columns:1fr 1fr;gap:24px;}
.icon-card{background:#fff;border-radius:16px;overflow:hidden;min-height:492px;}
.icon-card__grid{display:grid;grid-template-columns:repeat(5,63px);
  justify-content:space-between;row-gap:56px;padding:48px 36px 24px;}
.icon-card__grid img{width:63px;height:63px;object-fit:contain;}
.icon-card__caption{height:80px;background:#f2f2f2;color:#6b6f7a;
  font:700 13px/14px "CircularXX",sans-serif;text-align:center;
  clip-path:polygon(0 12px,4% 0,8% 12px,12% 0,16% 12px,20% 0,24% 12px,28% 0,32% 12px,36% 0,40% 12px,44% 0,48% 12px,52% 0,56% 12px,60% 0,64% 12px,68% 0,72% 12px,76% 0,80% 12px,84% 0,88% 12px,92% 0,96% 12px,100% 0,100% 100%,0 100%);}
@media (max-width:640px){.icon-set{grid-template-columns:1fr;}}
```
The caption colour and band grey are estimates, not sampled values.

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 6 | Clean white cards and a regular grid; the storefront around them is plain. |
| Originality | 3 | A grid of brand logos is a familiar format with no distinctive treatment. |
| Usability | 6 | Recognisability is easy to judge; no licence or size detail is shown. |
| Craft | 6 | Consistent grid pitch and card radius; caption type and grey are unrefined. |

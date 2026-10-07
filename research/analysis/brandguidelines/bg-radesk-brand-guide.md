---
id: bg-radesk-brand-guide
source: brandguidelines
category: template
status: failed
title: "Brand Guidelines Template - Radesk"
creator: "asylab (UI8 seller)"
styles: []
patterns: []
mode: dark
palette: ["#121212", "#181818", "#2D68FF", "#00A656", "#ADB7BE"]
type_families: ["CircularXX (UI8 storefront)"]
type_class: [grotesk]
radius_px: []
motion: null
scores: {aesthetics: null, originality: null, usability: null, craft: null}
craft_signals: []
anti_patterns: [unrendered-template-placeholders-in-capture]
---
# Brand Guidelines Template - Radesk — asylab (UI8 seller)

## 1. Snapshot
- **Failure reason:** the Wayback Machine snapshot (`web/20251010144538`, dated **2025-10-10**, no redirect) was captured **before the product template was filled**. The body shows raw Handlebars placeholders in place of product data: the H1 is literally `{{product.name}}`, the blurb is `{{product.blurb}}`, the author is `{{authorName}}`, the price is `{{ product.price | ui8Currency }}`, and the highlight is `{{feature}}`. The comments block shows `{{c.user.display_name ...}}`. The page `<title>` ("Brand Guidelines Template - Radesk") was set correctly.
- **Preview images:** none. The desktop and mobile product slots are blank frames with broken-image icons.
- **Result:** no product or design-system content can be analysed.

## 2. Composition & layout
The desktop frame shows the standard UI8 product layout with the placeholders in place: a 1440 px header, title at x≈56 px, a stack of green Download pills and a blue Add to cart pill at x≈1004–1369, and a blank preview area. The layout matches the other UI8 pages in this batch. The product layout itself is not what was sent in this capture.

## 3. Typography
CircularXX on 106 nodes, the same family as the other UI8 pages. Sizes are 15 px (41), 16 px (27) and 13 px (13). Tracking is −0.28 px on 96 nodes. This is storefront type only.

## 4. Colour
Storefront palette only. #FFFFFF on #181818 is **17.76:1** (pass), and #2D68FF on #181818 is **3.84:1** (fails AA for normal text). The template's own palette is not visible.

## 5. Depth & material
Not captured.

## 6. Components & patterns
Placeholder buttons only. Download, Add to cart, Login For Files and Preview are all present but unpopulated.

## 7. Motion
Not captured. Storefront transitions only.

## 8. Brand system
n/a — not captured. The text is unrendered template markup, so it names no system.

## 9. UX
The unrendered state would be a serious usability fault if shipped. The placeholder `Add to cart {{ product.price | ui8Currency }}` is a live-looking button, so it is a risk for a buyer. This is a capture artefact, not a verified property of the live page.

## 10. Craft signals
Not rated.

## 11. Reproduction recipe
Not applicable.

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | n/a | The capture shows template markup, not the product. |
| Originality | n/a | Not assessable. |
| Usability | n/a | Not assessable; the placeholder state is a capture failure. |
| Craft | n/a | Not assessable. |

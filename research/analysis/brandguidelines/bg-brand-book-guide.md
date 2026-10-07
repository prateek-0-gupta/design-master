---
id: bg-brand-book-guide
source: brandguidelines
category: template
status: analyzed
title: "Brand Guidelines Kit"
creator: "BrandKit (UI8 seller)"
styles: [dark-premium, corporate-clean, hairline-ui, gradient-mesh]
patterns: [product-page-two-column-overview, split-feature-card-grid, figma-kit-preview-stage, gradient-violet-backdrop, pill-add-to-cart-cta]
mode: dark
palette: ["#121212", "#000000", "#181818", "#2D68FF", "#4648FF", "#ADB7BE", "#FFFFFF", "#00A656"]
type_families: ["CircularXX (UI8 storefront, loaded 400/450/500)", "Preview-kit typeface not identifiable from pixels"]
type_class: [grotesk]
radius_px: [24, 16]
motion: null
scores: {aesthetics: 6, originality: 4, usability: 6, craft: 6}
craft_signals: [consistent-minus-0.28px-tracking, 24px-preview-card-radius, 1440px-two-column-grid, 2px-ring-around-avatars]
anti_patterns: [white-on-green-cta-below-aa, blue-text-on-dark-below-aa, tiny-13px-meta-text]
---
# Brand Guidelines Kit — BrandKit (UI8 seller)

## 1. Snapshot
- **Subject:** UI8 marketplace product page for a Figma brand-guidelines kit priced at $39, sold by the seller BrandKit. Captured from a Wayback Machine snapshot dated **2025-09-13** (`web/20250913211342`). The final URL is the same Wayback URL, with no redirect.
- **Why it's remarkable:** The preview cards show the kit's own layout system more clearly than the storefront does. Each section is a split card: a black panel with a title and check-list on the left, and a violet gradient stage holding a framed Figma screenshot on the right.

## 2. Composition & layout
- **Header:** 65 px toolbar (`--wm-toolbar-height: 65px`) on `#181818`. The H1 sits at x≈56 px and the purchase row is right-aligned to x≈1384 px, which gives a 56 px margin at 1440 px.
- **Preview grid:** two columns of 652 px (x 56–708 and 732–1384) with a 24 px gutter. Cards are about 492 px tall, with a 24 px corner radius.
- **Split card (inside a preview):** a black panel about 290 px wide holds the title and 3–5 check items. A gradient stage of about 340 px takes the rest, with a 1 px framed screenshot at about 12 px inset.
- **Overview / Highlights:** a two-column block starts at x≈200 and x≈830. Body copy is 16/24 px.
- **Mobile (390 px):** the grid becomes one column of 374 px cards with a 16 px gutter, and the purchase row stacks above the preview.

## 3. Typography
Storefront UI only, from the census. The preview typeface is not identifiable from the pixels.
- **Family:** CircularXX on 138 nodes, weights 400 / 450 / 500.
- **Sizes (node count):** 15 px (44), 16 px (35), 13 px (24), 22 px (9), 28 px (7), 64 px (3, hero).
- **Pairs:** 15/18 at 450 (25 nodes), 16/24 at 400 (25), 13/14 at 450 (24), 28/40 at 450 (7).
- **Tracking:** −0.28 px on 134 of 138 nodes. That is about −0.02 em at 14 px.
- **Preview headings:** "Color Library System" and similar titles sit at roughly 36 px over about 38 px leading (estimate from the 1440 px tile). The eyebrow "Organized Figma Styles" is a small blue caps-free label.

## 4. Colour
| Hex | Role | Approx. share (sampled) |
|---|---|---|
| #121212 | page ground | ≈47–50% of t01/t02 pixels |
| #000000 | preview card interior | ≈28% |
| #181818 | header and footer ground (census bg, 16 nodes) | — |
| #ADB7BE | body and meta text (74 text nodes) | — |
| #FFFFFF | headings, CTA label | — |
| #2D68FF | primary accent: Add to cart, Log in, text links (13 nodes) | — |
| #4648FF | "Ultramarine Blue" swatch shown in the Color Library preview | — |
| #00A656 | download bar text, check icons, Get All-Access | — |

**WCAG (contrast.py):**
- #FFFFFF on #181818: **17.76:1** (pass).
- #ADB7BE on #181818: **8.70:1** (pass).
- #00A656 on #181818: **5.57:1** (pass for text).
- White on #2D68FF: **4.63:1** (pass for the button label).
- #2D68FF on #181818: **3.84:1** (fails AA for normal text).
- #4648FF on #000000: **3.63:1** (fails AA for normal text).
- White on #00A656: **3.19:1** (fails AA for normal text).
- #5C5C5C on #181818: **2.66:1** (fails; used on the footer copyright line).

## 5. Depth & material
- Flat UI. The only elevation is a shadow of `0 8px 80px rgba(0,0,0,.4)`, used once for floating panels.
- Avatars and icon buttons use a 2 px ring in the page ground colour (`0 0 0 2px #121212`, 7 nodes). This separates them from the gradient.
- Preview frames use a soft `0 16px 16px rgba(0,0,0,.35)` lift. The gradient stage behind them is the only "material" in the set.

## 6. Components & patterns
- **Add to cart:** a pill of about 169×44 px in #2D68FF with a white label. The price sits in the label.
- **Secondary buttons:** outlined pills in a 1 px #ADB7BE-family hairline (Preview, Follow, Live Preview).
- **Download bar:** a full-width 1328 px rounded bar, about 80 px tall, with a green label and a green pill (Get All-Access).
- **Comments:** a 1040 px rounded panel with a log-in gate ("You must log in to comment.").
- **Preview stage:** the split card described in §2.

## 7. Motion
- **Census transitions:** `color .2s ease` (38), `fill .2s ease` (17), `opacity .4s ease` (13), `background .4s ease` (12), `box-shadow .4s ease` (6). One `transform .167s cubic-bezier(.33,0,0,1)`.
- **Token summary:** durations `.2s` (180 uses) and `.4s` (36 uses). Easing is `linear` on 87 entries, mostly long loops at 80 s and 160 s. Those loops are probably ambient and were not verified.
- **Visible state:** blue spinners in the comments block show loading states.

## 8. Brand system
n/a — not a brand system. This is a storefront page. The identity cues are the UI8 hexagon mark with a blue dot, and the seller's name. The kit's own design system is only visible in the preview cards: black panels, ultramarine #4648FF, and violet gradients. It is not documented as a token set.

## 9. UX
- The purchase row is at the top, and the description follows with a clear Overview / Highlights / Format structure.
- The format chip row and file size (35.3 MB in 1 File) answer the buyer's first questions.
- The comments gate and the "Be the first to join the discussion" panel take up a lot of vertical space for an empty thread.
- The hero image is blank in the capture, so the first impression cannot be verified.

## 10. Craft signals
- Preview cards share one 24 px radius and one 652 px column width at 1440 px.
- Storefront tracking is a single value (−0.28 px) applied almost everywhere.
- The avatar and icon buttons carry a 2 px ground-coloured ring.
- Primary accent is used consistently for the one call to action per block.
- The mobile layout preserves the 16 px gutter and the order of purchase, preview and description.

## 11. Reproduction recipe
```css
:root{
  --bg:#121212; --bg-deep:#000; --bg-bar:#181818;
  --ink:#fff; --ink-2:#adb7be; --accent:#2d68ff; --ultra:#4648ff; --ok:#00a656;
  --r-card:24px; --r-btn:999px;
  --font:"CircularXX","Helvetica Neue",Arial,sans-serif;
}
body{background:var(--bg);color:var(--ink);font:400 16px/24px var(--font);letter-spacing:-.28px;}
.preview{display:grid;grid-template-columns:1fr 1fr;gap:24px;}
.preview-card{border-radius:var(--r-card);background:var(--bg-deep);overflow:hidden;min-height:492px;}
.split{display:grid;grid-template-columns:290px 1fr;}
.split__stage{background:linear-gradient(160deg,#7865a5 0%,#5645a2 55%,#b1a7c2 100%);}
.btn-cart{background:var(--accent);color:#fff;border-radius:var(--r-btn);padding:12px 20px;font:500 16px/20px var(--font);transition:background .2s ease;}
.avatar{box-shadow:0 0 0 2px var(--bg);border-radius:50%;}
.shadow-float{box-shadow:0 8px 80px rgba(0,0,0,.4);}
@media (max-width:640px){.preview{grid-template-columns:1fr;}}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 6 | Competent dark storefront with a cohesive violet-and-black preview system; the storefront itself is generic. |
| Originality | 4 | Split-card kit previews and violet gradients are a common trend executed without a distinct idea. |
| Usability | 6 | Purchase and file information are clear, but the comment gate and blank hero weaken the page. |
| Craft | 6 | Consistent radius, tracking and column grid, offset by several AA failures on accent text. |

---
id: bg-cobalt-brand-guide
source: brandguidelines
category: template
status: analyzed
title: "Cobalt Brand Styleguide Template"
creator: "BrandGuidelines.net (template; kit by 1042 Studio)"
styles: [corporate-clean, minimal-swiss, photo-led]
patterns: [hero-title-with-brand-image, two-up-kit-description-card, six-slide-preview-strip, tile-grid-of-chapters, subscribe-form-pill, other-guidelines-card-pair, dark-footer-with-wordmark]
mode: light
palette: ["#f6f7fb", "#151618", "#00cdc0", "#2d3542", "#ffd150", "#ffffff"]
type_families: ["Inter (body, census)", "Switzer (display, census)", "Inter Tight (display, census)"]
type_class: [neo-grotesk, geometric-sans]
radius_px: [12, 16, 24, 32]
motion: null
scores: {aesthetics: 6, originality: 3, usability: 7, craft: 6}
craft_signals: [pale-cool-canvas-f6f7fb, one-dark-ink-151618, brand-accent-teal-as-section-fill, template-with-consistent-radii, inter-body-16-22.4-leading, switzer-display-tracking-minus-0-015em]
anti_patterns: [template-reuse-across-brands, dim-meta-text-below-aa, cover-image-dominates-brand-kit]
---
# Cobalt Brand Styleguide Template — BrandGuidelines.net (kit by 1042 Studio)

## 1. Snapshot
- **Subject:** A brandguidelines.net template page for the "Cobalt Brand Guideline", a 46-slide Figma kit. The page is the public landing for the kit. It introduces the kit, lists its contents and offers subscribe and "other guidelines" links. The capture is the final URL, with no redirect and no archive.
- **Why it's remarkable:** Not remarkable on its own. It is one of three pages (Cobalt, Form, Owire) built from the same template with identical computed styles, so the page is best read as a reusable kit landing rather than a unique identity.

## 2. Composition & layout
- **Header:** a single bar with the BrandGuidelines wordmark at x=60 and a nav (About, Resources), a dark "Submit Guidelines" pill and a light/dark toggle at x≈1370.
- **Title block:** a centred two-line H1 ("Cobalt / Brand Guideline") at about 52 px, then three grey pills ("Figma", "46 Pages", "Styles").
- **Hero image:** a 1320 px wide frame (x 60 to 1380, y 422 to 1062, so 640 px tall) with a city photo and the Cobalt logo centred.
- **Intro:** a centred 40 px statement, two lines, with a 1000 px measure.
- **Feature pair:** a dark slide-preview card (650 px) beside a teal `#00cdc0` statement card (650 px), both with radii near 24 px and a 20 px gutter.
- **Overview:** a two-column text block (about 500 px left, 300 px right) with "Highlights" and "Format" lists.
- **Other guidelines:** two 460 px preview cards (Form and Owire) with a centred H2.
- **Mobile (390 px):** a single column with about 30 px margins. The hero image becomes a 350 × 440 px portrait.

## 3. Typography
- **Families (census):** Inter carries body and UI (43 uses, plus 500 weight). Switzer appears on nine tracked display nodes. Inter Tight appears on three nodes, probably the largest display lines.
- **Scale (census):** 14 px (26 uses), 16 px (14), 13 px (9), 24 px (3), 40 px (2), 52 px (1).
- **Line heights:** 16.8 px (25 uses) for 14 px, 22.4 px (14) for 16 px, and 62.4 px for 52 px.
- **Tracking:** `normal` on 46 nodes and `-0.78px` on 9 display nodes, which is about -0.015em at 52 px.
- **Weights:** 400 (46 uses) and 500 (9).

## 4. Colour
| Hex | Role | Approx share (tile 1) |
|---|---|---|
| #f6f7fb | page canvas (census `bg`, 5 uses) | ~48% |
| #2f3541 | dark slate section (preview card) | ~11% |
| #142426 | deep teal-black, preview art | ~9% |
| #00cdc0 | brand teal, statement card | ~7% |
| #151618 | body ink (census `textColor`, 30 uses) | ~30% in tile 4 |
| #ffd150 | accent yellow (tile 2) | ~12% of tile 2 |

- **WCAG pairs (contrast.py):** #151618 on #f6f7fb **16.91:1**. #151618 on #00cdc0 **9.05:1**. #ffffff on #2d3542 **12.36:1**. #adadad on #151618 **8.07:1**. #7d838a on #f6f7fb **3.58:1**, which fails AA-normal (it is used for the secondary labels).
- The statement card uses ink on teal, so it holds up. The grey labels do not.

## 5. Depth & material
- Almost none. The census has one `box-shadow` (0 22 px 44 px at 0 alpha, so effectively none) and an inset of zero. Depth is made with colour blocks and the hero photograph.
- Radii carry the material: 12 px (35 uses), 16 px (11), 24 px (3) and 32 px (2).

## 6. Components & patterns
- **Subscribe form:** a pill input with a black "Subscribe" pill inside it, plus a "3,500+ people already subscribed!" line with three avatar faces.
- **Other-guidelines card pair:** two image cards with the other brand's logo in white, one showing Form and one showing Owire.
- **Footer:** a dark rounded block with a large "Brand" wordmark cropped at the bottom edge, and "© 1042 Studio. All rights are owned by the authors and the brand owners."
- **Preview strip:** a horizontal row of six kit slides (for example "Regular Medium Bold", "Empowering Financial Wizards") with a page-dot pager.

## 7. Motion
- Not measurable. The census has no transitions (`transition` is empty), and the page is a static template. No timings are stated.

## 8. Brand system
n/a — template page for a sample brand. The sample identity is the Cobalt logo: a teal asterisk-like mark beside a title-case sans wordmark. Its palette is a teal (#00cdc0), a warm yellow (#ffd150), a coral pink (in the kit preview), and near-black ink. The footer credit "© 1042 Studio" shows the same kit is sold on the 1042 Studio store (listed there as "Cobalt Brand Guidelines Kit Copy", $30).

## 9. UX
- The hero, the description and the highlight list give a clear sequence. A visitor can see what the kit contains in under two screens.
- The "Format" list (Figma, PDF, SVG, PNG) answers the first practical question.
- Weaknesses: the secondary labels fail AA (3.58:1), and the page is long (about 5,655 px scroll height) with mostly the same image cards repeated.

## 10. Craft signals
- The palette is kept to one canvas (#f6f7fb) and one ink (#151618), so the page reads as calm.
- Body text runs at 16/22.4 px and UI at 14/16.8 px, which gives a consistent rhythm.
- Display tracking is set once for display sizes (-0.78 px).
- Radii step through 12, 16, 24 and 32 px, and the same 24 px is used on both feature cards.

## 11. Reproduction recipe
```css
:root{
  --canvas:#f6f7fb; --ink:#151618; --ink-2:#4a4f58; --slate:#2d3542; --teal:#00cdc0; --yellow:#ffd150;
  --r-sm:12px; --r-md:16px; --r-lg:24px; --r-xl:32px;
  --font-body:"Inter",sans-serif; --font-disp:"Switzer","Inter Tight",sans-serif;
}
body{background:var(--canvas);color:var(--ink);font:400 16px/22.4px var(--font-body);}
h1{font:400 52px/62.4px var(--font-disp);letter-spacing:-.78px;}
h2{font:400 40px/48px var(--font-disp);letter-spacing:-.78px;}
.statement{background:var(--teal);color:var(--ink);border-radius:var(--r-lg);padding:48px;}
.preview{background:var(--slate);color:#fff;border-radius:var(--r-lg);}
.label{color:var(--ink-2);font-size:14px;line-height:16.8px;} /* #7d838a fails AA on the canvas */
.pill{border-radius:var(--r-md);}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 6 | Calm canvas, a clear teal accent and a clean hero; the template itself is generic. |
| Originality | 3 | The same template is shared with Form and Owire, so the look is a reused layout. |
| Usability | 7 | Clear sequence from hero to format list to subscribe; grey labels and length cost points. |
| Craft | 6 | Consistent radii and tracking; a few meta tints fail contrast. |

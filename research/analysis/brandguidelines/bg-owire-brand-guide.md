---
id: bg-owire-brand-guide
source: brandguidelines
category: template
status: analyzed
title: "Owire Brand Styleguide Template"
creator: "BrandGuidelines.net (template; kit by 1042 Studio)"
styles: [corporate-clean, luxury, photo-led]
patterns: [hero-title-with-brand-image, two-up-kit-description-card, six-slide-preview-strip, tile-grid-of-chapters, subscribe-form-pill, other-guidelines-card-pair, dark-footer-with-wordmark]
mode: light
palette: ["#f6f7fb", "#221d34", "#5c91db", "#71d7e3", "#171a46", "#151618"]
type_families: ["Inter (body, census)", "Switzer (display, census)", "Inter Tight (display, census)"]
type_class: [neo-grotesk, geometric-sans]
radius_px: [12, 16, 24, 32]
motion: null
scores: {aesthetics: 6, originality: 3, usability: 7, craft: 6}
craft_signals: [pale-cool-canvas-f6f7fb, deep-plum-section-fill, cyan-to-blue-gradient-accent, template-with-consistent-radii, inter-body-16-22.4-leading, switzer-display-tracking-minus-0-015em]
anti_patterns: [template-reuse-across-brands, dim-meta-text-below-aa, cover-image-dominates-brand-kit]
---
# Owire Brand Styleguide Template — BrandGuidelines.net (kit by 1042 Studio)

## 1. Snapshot
- **Subject:** A brandguidelines.net template page for the "Owire Brand Guideline", a 28-slide Figma kit. It is the public landing for the kit, with hero, description, highlight and format lists, and links to two other kits. The capture is the final URL with no redirect and no archive.
- **Why it's remarkable:** The hero photograph of a circuit board with a concentric-ring logo is the most texture-rich image of the three template pages. The rest is the same template as Cobalt and Form.

## 2. Composition & layout
- **Header:** a 44 px-tall bar with the wordmark at x=60, nav (About, Resources), a dark "Submit Guidelines" pill and a light/dark toggle at x≈1370.
- **Title block:** a centred two-line H1 ("Owire / Brand Guideline") at about 52 px, then three grey pills ("Figma", "28 Pages", "Styles").
- **Hero image:** a 1320 px wide frame (x 60 to 1380, y 422 to 1062, so 640 px tall) with a blue-violet photo of circuit chips and the Owire logo at centre.
- **Intro:** a centred 40 px statement over two lines.
- **Feature pair:** a deep-plum preview card (650 px) beside a plum statement card (650 px), both at 24 px radius with 30 px gutters.
- **Overview:** the same two-column text block with "Highlights" and "Format".
- **Other guidelines:** two 460 px image cards (Cobalt and Form).
- **Mobile (390 px):** a single column with a 350 px square hero.

## 3. Typography
- **Families (census):** identical to Cobalt and Form. Inter carries body and UI (43 uses), Switzer carries display and H2s (9 uses), Inter Tight appears on the largest lines (3 uses).
- **Scale (census):** 14 px (26), 16 px (14), 13 px (9), 24 px (3), 40 px (2), 52 px (1).
- **Line heights:** 16.8 px for 14 px, 22.4 px for 16 px, 62.4 px for 52 px.
- **Tracking:** `normal` on 46 nodes and `-0.78px` on 9 display nodes (about -0.015em at 52 px).
- **Kit typography (not in the page census):** the preview slides show a geometric sans specimen ("Aa Bb Cc" alphabet slides) with cyan and blue colour bars. The page itself is Inter and Switzer.

## 4. Colour
| Hex | Role | Approx share (tile 1 / 2) |
|---|---|---|
| #f6f7fb | page canvas | ~48% (tile 1) |
| #221d34 | deep plum, preview section | ~13% (tile 1), ~37% (tile 2) |
| #171a46 | deep indigo, preview art | ~7% (tile 1) |
| #5c91db | brand blue, gradient card | ~10% (tile 2) |
| #71d7e3 | cyan highlight, gradient edge | ~4% (tile 2) |
| #151618 | body ink (census, 30 uses) | ~30% (tile 4) |

- **WCAG pairs (contrast.py):** #221d34 on #f6f7fb **15.17:1**. #151618 on #f6f7fb **16.91:1**. #5c91db on #221d34 **5.05:1** (passes AA-normal). #71d7e3 on #221d34 **9.69:1**. #7d838a on #f6f7fb **3.58:1**, which fails AA-normal, as on Cobalt and Form.
- The cyan and blue text reads well on the plum section. The grey labels on the canvas do not.

## 5. Depth & material
- Almost none. The census lists one zero-alpha box-shadow and no inset. Depth comes from colour blocks and the hero photograph.
- Radii carry the only material cue: 12 px (35 uses), 16 px (11), 24 px (3), 32 px (2).

## 6. Components & patterns
- **Subscribe form:** a pill input with a black "Subscribe" pill, plus "3,500+ people already subscribed!" and three avatars.
- **Other-guidelines card pair:** Cobalt and Form cards.
- **Footer:** a dark rounded block with a cropped "Brand" wordmark and the "© 1042 Studio" credit.
- **Preview strip:** six kit slides (for example "Library Colors" and "Logo Safe Zone") with a pager.

## 7. Motion
- Not measurable. The census has no transitions and the template is static. No timings are stated.

## 8. Brand system
n/a — template page for a sample brand. The Owire identity is a concentric-ring mark beside a lowercase wordmark in a geometric sans, set on plum and cyan-blue gradients. The kit's visible rules are "Simply Vibrant" library colours (gradient-capable), a logo safe-zone with a dashed grid, and a single systemic type family. The footer credits 1042 Studio, and the 1042 store lists this kit as "Owire Brand Guidelines Kit", Figma design, $20.

## 9. UX
- The sequence is clear: hero, description, highlights, format, then the subscribe and other-kit links.
- The "Format" list (Figma, PDF, SVG, PNG) answers the practical question.
- Weaknesses: the grey labels fail AA, the template repeats image cards, and the page is about 5,632 px tall with no in-page navigation.

## 10. Craft signals
- The brand's gradient is applied to the kit slides and the hero, while the page stays on a neutral canvas.
- Body text at 16/22.4 px and UI text at 14/16.8 px keep the rhythm.
- One display tracking value (-0.78 px) covers all display sizes.
- Radii step through 12, 16, 24 and 32 px.

## 11. Reproduction recipe
```css
:root{
  --canvas:#f6f7fb; --ink:#151618; --ink-2:#4a4f58; --plum:#221d34; --indigo:#171a46;
  --blue:#5c91db; --cyan:#71d7e3;
  --r-sm:12px; --r-md:16px; --r-lg:24px; --r-xl:32px;
  --font-body:"Inter",sans-serif; --font-disp:"Switzer","Inter Tight",sans-serif;
}
body{background:var(--canvas);color:var(--ink);font:400 16px/22.4px var(--font-body);}
h1{font:400 52px/62.4px var(--font-disp);letter-spacing:-.78px;}
.statement{background:linear-gradient(120deg,var(--plum),var(--indigo));color:#fff;border-radius:var(--r-lg);padding:48px;}
.accent-text{color:var(--blue);} /* 5.05:1 on plum; do not use on the light canvas for small text */
.label{color:var(--ink-2);font-size:14px;line-height:16.8px;}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 6 | Plum and cyan-blue give a cool, tech-leaning feel, on the same calm template. |
| Originality | 3 | The layout is shared with Cobalt and Form, so the page is a reused template. |
| Usability | 7 | The sequence from hero to format list to subscribe is clear; grey labels and length cost points. |
| Craft | 6 | Consistent radii and tracking; the cyan and blue pair well on plum. |

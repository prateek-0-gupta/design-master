---
id: bg-form-brand-guide
source: brandguidelines
category: template
status: analyzed
title: "Form Brand Styleguide Template"
creator: "BrandGuidelines.net (template; kit by 1042 Studio)"
styles: [corporate-clean, photo-led, minimal-swiss]
patterns: [hero-title-with-brand-image, two-up-kit-description-card, six-slide-preview-strip, tile-grid-of-chapters, subscribe-form-pill, other-guidelines-card-pair, dark-footer-with-wordmark]
mode: light
palette: ["#f6f7fb", "#8545f6", "#823feb", "#151618", "#160d1e", "#fcf1e1"]
type_families: ["Inter (body, census)", "Switzer (display, census)", "Inter Tight (display, census)"]
type_class: [neo-grotesk, geometric-sans]
radius_px: [12, 16, 24, 32]
motion: null
scores: {aesthetics: 6, originality: 3, usability: 7, craft: 6}
craft_signals: [pale-cool-canvas-f6f7fb, one-dark-ink-151618, saturated-purple-section-fill, template-with-consistent-radii, inter-body-16-22.4-leading, switzer-display-tracking-minus-0-015em]
anti_patterns: [template-reuse-across-brands, dim-meta-text-below-aa, cover-image-dominates-brand-kit]
---
# Form Brand Styleguide Template — BrandGuidelines.net (kit by 1042 Studio)

## 1. Snapshot
- **Subject:** A brandguidelines.net template page for the "Form Brand Guideline", a 40-slide Figma kit. It is the public landing for the kit, with a hero, a short description, the highlight and format lists, and links to two other kits. The capture is the final URL, with no redirect and no archive.
- **Why it's remarkable:** Its brand colour is the most striking of the three template pages. A saturated violet (#8545f6 and #823feb in the sampled pixels) carries the hero and the preview card, against a plain cool canvas. Otherwise the page is the same template as Cobalt and Owire.

## 2. Composition & layout
- **Header:** a single bar with the wordmark at x=60, nav (About, Resources), a dark "Submit Guidelines" pill and a light/dark toggle at x≈1370.
- **Title block:** a centred two-line H1 ("Form / Brand Guideline") at about 52 px, then three grey pills ("Figma", "40 Pages", "Styles").
- **Hero image:** a 1320 px wide frame (x 60 to 1380, y 422 to 1062, so 640 px tall) with a portrait of a man in glasses and a white Form logo across the face.
- **Intro:** a centred 40 px statement over two lines with a 1000 px measure.
- **Feature pair:** a violet preview card (650 px) beside a violet statement card (650 px), both at about 24 px radius with a 20 px gutter.
- **Overview:** the same two-column text block as Cobalt, with the "Highlights" and "Format" lists.
- **Other guidelines:** two 460 px image cards (Cobalt and Owire).
- **Mobile (390 px):** a single column. The hero image becomes a 350 × 440 px portrait.

## 3. Typography
- **Families (census):** identical to Cobalt and Owire. Inter carries body and UI (43 uses), Switzer appears on nine tracked display nodes, and Inter Tight on three nodes.
- **Scale (census):** 14 px (26), 16 px (14), 13 px (9), 24 px (3), 40 px (2), 52 px (1).
- **Line heights:** 16.8 px for 14 px, 22.4 px for 16 px, 62.4 px for 52 px.
- **Tracking:** `normal` on 46 nodes and `-0.78px` on 9 display nodes (about -0.015em at 52 px).
- **Kit typography (not in the page census):** the preview slides show a serif display face ("QUILON") and a sans for text. The page itself does not use the serif.

## 4. Colour
| Hex | Role | Approx share (tile 1 / 2) |
|---|---|---|
| #f6f7fb | page canvas (census `bg`) | ~50% (tile 1) |
| #823feb | brand violet, hero and CTA wash (palette sample) | ~10% (tile 1) |
| #8545f6 | brand violet, feature card fill | ~26% (tile 2) |
| #160d1e | deep plum ink, preview art | ~16% (tile 2) |
| #151618 | body ink (census `textColor`, 30 uses) | ~30% (tile 4) |
| #fcf1e1 | cream paper on the kit preview | ~7% (tile 2) |

- **WCAG pairs (contrast.py):** #823feb on #f6f7fb **5.08:1** (passes AA-normal for text). #ffffff on #8545f6 **5.02:1** (passes AA-normal). #151618 on #f6f7fb **16.91:1**. #7d838a on #f6f7fb **3.58:1** (fails AA-normal, as on Cobalt).
- The violet works as a text colour on the canvas, which is a rare outcome for a saturated accent. It only just passes, so it should not be used for small text.

## 5. Depth & material
- Almost none, as on Cobalt. The census lists one zero-alpha box-shadow and no inset.
- Radii are the only material cue: 12 px (35 uses), 16 px (11), 24 px (3), 32 px (2).

## 6. Components & patterns
- **Subscribe form:** a pill input with a black "Subscribe" pill, plus "3,500+ people already subscribed!" and three avatars.
- **Other-guidelines card pair:** Cobalt and Owire preview cards.
- **Footer:** a dark rounded block with a cropped "Brand" wordmark and the "© 1042 Studio" credit.
- **Preview strip:** six kit slides (for example "Well Organized" and "The Logotype") with a pager.

## 7. Motion
- Not measurable. The census has no transitions and the template is static. No timings are stated.

## 8. Brand system
n/a — template page for a sample brand. The Form identity is a white "F"-shaped mark with a wordmark in a clean sans, set on violet and near-black. The kit's visible rules include a safe-zone logo spec, a colour library (2 primary and 6 secondary colours) and a serif display face. The footer credits 1042 Studio, and the 1042 store lists this kit as "Form Brand Guidelines Kit", Figma design, $30.

## 9. UX
- The page sequence is clear: hero, description, highlights, format, and then the subscribe and other-kit links.
- The "Format" list answers the buying question (Figma, PDF, SVG, PNG).
- Weaknesses: the grey labels fail AA, the template repeats image cards, and the page is about 5,655 px tall with no in-page navigation.

## 10. Craft signals
- The brand's violet is applied as a fill and as a text colour, so it reads as a system colour rather than decoration.
- Body text at 16/22.4 px and UI text at 14/16.8 px keep the rhythm.
- One display tracking value (-0.78 px) covers all display sizes.
- Radii step through 12, 16, 24 and 32 px.

## 11. Reproduction recipe
```css
:root{
  --canvas:#f6f7fb; --ink:#151618; --ink-2:#4a4f58; --brand:#823feb; --brand-2:#8545f6;
  --plum:#160d1e; --paper:#fcf1e1;
  --r-sm:12px; --r-md:16px; --r-lg:24px; --r-xl:32px;
  --font-body:"Inter",sans-serif; --font-disp:"Switzer","Inter Tight",sans-serif;
}
body{background:var(--canvas);color:var(--ink);font:400 16px/22.4px var(--font-body);}
h1{font:400 52px/62.4px var(--font-disp);letter-spacing:-.78px;}
.statement{background:var(--brand-2);color:#fff;border-radius:var(--r-lg);padding:48px;}
.brand-text{color:var(--brand);} /* 5.08:1 on the canvas; body size only at 16px+ */
.label{color:var(--ink-2);font-size:14px;line-height:16.8px;}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 6 | The violet is the strongest of the three brand colours, held against a calm canvas. |
| Originality | 3 | Shared template with Cobalt and Owire, so the layout is reused rather than made for Form. |
| Usability | 7 | Clear hero-to-format path; grey labels and repeated cards cost points. |
| Craft | 6 | Consistent radii and tracking, with the brand violet passing AA on the canvas. |

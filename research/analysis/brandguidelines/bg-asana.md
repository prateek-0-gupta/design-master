---
id: bg-asana
source: brandguidelines
category: guideline
status: analyzed
title: "Asana: Brand & Product (case study)"
creator: "Micah Daigle (portfolio page, not an Asana-owned guideline)"
styles: [editorial-serif, minimal-swiss, maximalist-color, photo-led]
patterns: [case-study-meta-sidebar, gradient-hero-with-floating-white-card, serif-section-titles, pull-quote-band, mockup-bento-grid, light-to-dark-section-switch, prev-next-project-footer]
mode: mixed
palette: ["#000000", "#ffffff", "#f4f4f4", "#222226", "#747781", "#fb7081", "#fcb65a", "#7f93f9"]
type_families: ["Utopia Std Display (Adobe Fonts, headlines)", "Helvetica Neue / system fallback (body; renders Inter-like)", "Pragmatica Extended 500 (uppercase labels)", "Clarkson (secondary, minor)"]
type_class: [transitional-serif, neo-grotesk]
radius_px: [4, 18, 26]
motion: {durations_s: [0.1, 0.14, 0.2, 0.3, 0.4], easing: [ease, linear, ease-in-out, "cubic-bezier(0.4,0,0.2,1)"], loop: false}
scores: {aesthetics: 7, originality: 5, usability: 7, craft: 6}
craft_signals: [serif-sans-pairing, one-gradient-field-per-hero, white-card-over-gradient, mockups-on-concrete-ground, role-collaborator-sidebar, dark-section-for-product-work]
anti_patterns: [video-embed-failed, secondary-grey-fails-aa, tiny-unreadable-screenshots, template-squarespace-feel]
---
# Asana: Brand & Product — Micah Daigle

## 1. Snapshot
- **Subject:** a Squarespace portfolio case study by a former Asana designer about the 2014–15 rebrand and product work. `site_meta.json` shows the request was `/design/asana` but the recorded final URL is `/design/hackpad`, the "next project" link. The census and every tile show the Asana page, so the content is correct. Subpages `d01` (Pact) and `d02` (Hackpad) are neighbouring case studies, not Asana material. This is a promoted page, not Asana's own guideline, so it is treated as a landing page.
- **Why it's remarkable:** it reproduces the Asana identity from the outside: coral-to-orange gradient trio, brand-book mockups, and a four-word personality set (Purposeful, Empowering, Approachable, Quirky). A restrained black/white editorial frame lets the borrowed colour do the work.

## 2. Composition & layout
- **Top bar:** 56 px tall, #f4f4f4, name left at x=72, five links right.
- **Hero:** a 915×610 px image on the left (x 72–987) and a 3-line serif title with role and collaborators in a sidebar at x≈1052. Meta labels are small caps.
- **Gradient band:** a 794 px full-bleed pink-orange-yellow-blue field with a 642×450 white card centred on it (x 399–1041), holding a 73 px serif headline and 16.7 px body.
- **Sections:** centred 54 px serif titles ("Brand Identity"), then left-aligned 37 px sub-heads at x=181. Image grids use 8–11 px gutters and run full-bleed in the identity section, while product work sits in a 970 px column (x 235–1205).
- **Rhythm:** white → #f4f4f4 quote band → white → full-bleed mockup bento → #222226 dark "Product Design" block. The dark section signals the older, pre-rebrand work.
- **Footer:** previous/next project links.

## 3. Typography
Census `typePairs`:
- **Display:** Utopia Std Display 400 at 73.75 / 53.0 / 37.5 px with line-heights 76.5 / 58.0 / 42.6 (ratios 1.04, 1.09, 1.14). Tight leading on large sizes, no letter-spacing.
- **Body:** "Helvetica Neue" 16.73 px / 25.09 (1.5) weight 400 is the dominant style, 54–60 uses on subpages. The screenshots render it as an Inter-like face because Helvetica Neue was not installed, so the real rendered face is a fallback. Bold 700 is used for emphasis.
- **Lead / quote:** 18.46 px; the pull quote is set in the serif at about 37 px, centred.
- **Labels:** Pragmatica Extended 500, 13.27 px / 18.6, +0.133 px tracking, uppercase ("ROLE", "COLLABORATORS", "—EXCERPT FROM MY MEDIUM ARTICLE").
- **Scale:** 13.3 / 16.7 / 18.5 / 37.5 / 53 / 73.8, with a ×1.4 jump between 37.5 and 53.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #ffffff | page ground | ~55% (palette) |
| #f4f4f4 | nav, quote band, bento gutters | ~15–20% |
| #222226 | dark product section | ~10% |
| #000000 | text, CTA button | text |
| #747781 | secondary text, sidebar links | small |
| #fb7081 / #ed598d / #fda05c / #fbcb4e / #68c0f5 / #7f93f9 | Asana gradient family in imagery | hero bands |
| #258bcf | old-product blue (before screenshots) | small |

Contrast (contrast.py): black on white 21:1; white on #222226 15.85:1; **#747781 on white 4.47:1 and on #f4f4f4 4.06:1 (both fail AA for body text)**; white on coral #ff6585 only 2.82:1, so the gradient is decorative and the text sits in a white card. Image overlay is rgba(0,0,0,.5).

## 5. Depth & material
Interfaces are flat. Depth comes from the mockups: books lying on grey concrete with soft shadows, and a laptop on a gradient arc. The only CSS shadow is `0 0 10px rgba(0,0,0,.2)`. Radii are minimal: 4 px, one 18 px and one 26 px element, and 100% for avatars.

## 6. Components & patterns
Role/collaborator sidebar; white content card over gradient; serif pull quote with attribution link; black "Read the article" button (174×55, square) with a grey "142,000+ views" proof line; bento of book spreads; four personality cards with cut-out people and spot illustrations; dark screenshot pairs with a lightly-faded second state; a prev/next card footer. The embedded video shows "Video is not available" in the capture.

## 7. Motion
Page-level only, from the census: `all 0.3s ease` on links/buttons (4 uses), `box-shadow 0.3s ease`, `opacity 0.2s ease`, `opacity 0.1s linear`, `transform 0.14s ease-in-out`, and one `opacity 0.4s cubic-bezier(0.4,0,0.2,1)` (image reveal). No scroll-driven effects were captured. Celebrations content (rocket, unicorn) is shown as stills.

## 8. Brand system (short; this is a page about a brand, not a guideline)
Shown, with sources inferred from the imagery: logo = three coral dots over lowercase "asana" wordmark; gradient circles as the brand shape; headline face "GT Haptik" (named in a spread); personality set of four adjectives with human cut-outs; illustration as quirky spot art. Process claims (Medium article, brand book roll-out) are text, not specification. No clearspace, hex or type spec is published here.

## 9. UX
Clear story order: role → problem → old look → strategy → new identity → product. Strong proof signals (client list, 142,000+ views). Weakness: screenshots are shrunk to ≈480 px so UI text is unreadable, the video fails, and grey secondary text is below AA.

## 10. Craft signals
- One serif and one sans, with the serif only at ≥37 px.
- Colour is confined to imagery; chrome stays black/white/grey.
- White card 642 px wide centred on the gradient band; type inside is left-aligned with 64 px padding.
- Sidebar labels use uppercase extended caps with +0.13 px tracking.
- Mobile (390 px) keeps the same order and the white card spans full width with 24 px margins.

## 11. Reproduction recipe
```css
:root{--ink:#000;--paper:#fff;--wash:#f4f4f4;--night:#222226;--mute:#747781;
 --serif:"utopia-std-display",Georgia,serif;--sans:"Helvetica Neue",Arial,sans-serif;
 --label:"pragmatica-extended",var(--sans);}
body{font:400 16.73px/1.5 var(--sans);color:var(--ink);background:var(--paper)}
h1{font:400 73.75px/1.04 var(--serif)} h2{font:400 53px/1.09 var(--serif)} h3{font:400 37.5px/1.14 var(--serif)}
.label{font:500 13.27px/1.4 var(--label);letter-spacing:.01em;text-transform:uppercase}
.gradient-hero{background:linear-gradient(115deg,#ff5f93,#fda05c 45%,#fbcb4e 70%,#7f93f9);min-height:794px;display:grid;place-items:center}
.card{background:#fff;width:642px;padding:56px 64px}
.dark{background:var(--night);color:#fff}
a,button{transition:all .3s ease}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 7 | The serif against vivid gradient imagery works; borrowed colour does the job. |
| Originality | 5 | Standard portfolio case-study structure. |
| Usability | 7 | Clean reading order, but small screenshots, broken video and AA-failing grey. |
| Craft | 6 | Consistent spacing and type tokens; Squarespace template limits. |

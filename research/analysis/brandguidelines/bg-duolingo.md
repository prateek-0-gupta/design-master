---
id: bg-duolingo
source: brandguidelines
category: guideline
status: analyzed
title: "Duolingo Brand Guidelines (design.duolingo.com)"
creator: "In-house"
styles: [playful-rounded, flat-illustration, maximalist-color]
patterns: [five-colour-section-cards, multilingual-greeting-hero, quick-links-rail, one-colour-per-section, illustration-peeking-from-card-corner, custom-display-face-for-headings, uppercase-tracked-cta, section-colour-css-variable]
mode: light
palette: ["#58cc02", "#1cb0f6", "#ce82ff", "#ffb100", "#ff7878", "#ffffff", "#afafaf"]
type_families: ["Feather Bold (headings, custom)", "DIN Round 400/700 (body, UI)"]
type_class: [rounded-sans, geometric-sans]
radius_px: [16]
motion: {durations_s: [0.3], easing: [ease], loop: false}
scores: {aesthetics: 7, originality: 6, usability: 5, craft: 6}
craft_signals: [section-colour-as-css-variable, single-radius-16, lowercase-display-headings, illustration-cropped-into-card-edge, hero-greeting-fading-out-of-frame]
anti_patterns: [white-text-on-saturated-brand-colours-fails-aa, grey-footer-text-2-19-contrast, home-only-coverage]
---
# Duolingo Brand Guidelines — In-house

## 1. Snapshot
- **Subject:** the front door of Duolingo's guideline site. The live domain is unreliable, so this is a Wayback Machine capture dated 2026-01-06 02:25:56 UTC (`captured_from` .../web/20260106022556if_/https://design.duolingo.com/).
- **Coverage:** only the home page was captured. No guideline subpage (identity, writing, illustration, marketing, resources) was captured. The `d01_sub_*` tiles are an unrelated blog post (blog.duolingo.com/vikram-redesign, "Redesigning Vikram", 2024) that the crawler picked up, so treat them as incidental illustration evidence only. Logo rules, clearspace, voice rules and the document structure below the home are unknown.
- **Why it's remarkable:** a guideline landing page that behaves like the product: five saturated tiles, one per discipline, each wearing a different brand colour.

## 2. Composition & layout
- A 560 px tall green hero (#58cc02) fills the first screen. Page gutter is 50 px each side (logo at x=50, tiles end at x=1390).
- Hero left: a rotating greeting in Feather ("hola / こんにちは / bonjour / jambo") at 60 px, fading to lower opacity on the neighbouring words and clipped at the viewport edge, then a 15 px intro paragraph on a 23 px line. Hero right: a "QUICK LINKS" rail, a 2×2 grid of Press Kit, Illustration Colors, Brand Colors and Duolingo.com, with chevrons.
- Below, a 3-up grid of cards 431 px wide with a 24 px gap, then a second row of 2 cards, so the sixth cell is empty. Cards are about 280 px tall. Mobile (390 px) stacks them in one column at 342 px with 24 px gaps and the header collapses to a hamburger.
- A thin "All good." strip with a green check at y≈900 is a Wayback or status overlay artefact, not part of the design.

## 3. Typography
From `census_home.json`:
- **Feather Bold** (custom, 700) for the five card titles at 36/36 px and the hero greeting at 60/60 px. Solid leading of 1.0, lowercase, no tracking.
- **DIN Round** for everything else: 15/23.25 px body (400), 14/14 px uppercase 700 at 0.75 px tracking for CTAs and nav, 16/16 px 700 at 0.6 px tracking, 19/19 px 700 for quick links.
- Scale: 14, 15, 16, 19, 36, 60. The jump from 19 to 36 skips any mid step; the two voices (rounded display, rounded text) do the hierarchy.

## 4. Colour
| Hex | Role | Approx share |
|---|---|---|
| #58cc02 | Feather Green: hero, "identity" card, `--guide-color` | 38% |
| #ffffff | page and footer | 39% |
| #1cb0f6 | "writing" card | 3.6% |
| #ce82ff | "illustration" card | 4% |
| #ffb100 | "marketing" card | 4.4% |
| #ff7878 | "resources" card | 4% |
| #afafaf | footer links (rgb 175) | small |

Contrast (contrast.py): white on #58cc02 **2.09:1**, on #1cb0f6 **2.44:1**, on #ce82ff **2.54:1**, on #ffb100 **1.82:1**, on #ff7878 **2.56:1**, #afafaf on white **2.19:1**. Every white-on-colour card fails AA even at large size; the 36 px titles read only because of weight and scale. The orange card is worst.

## 5. Depth & material
No shadows (`shadow: {}`) and no gradients. Depth comes from flat illustrations half-cropped into the bottom-right card corners (a bus stop, books, a crowd of characters, shipping boxes, a faint wireframe owl on green drawn in a lighter tint). A single radius, 16 px, on all cards.

## 6. Components & patterns
- Section card: colour field, 36 px lowercase title, 15 px description, uppercase CTA ("VIEW GUIDE ›" or "VIEW ASSETS ›") and a corner illustration.
- Quick-links rail with the two colour deep links (brand colours, illustration colours), which means colour is the most requested lookup.
- Utility nav: Downloads, Help, About, Careers.

## 7. Motion
The census lists `color 0.3s ease` (12 uses), `filter 0.3s ease` (5) and `transform 0.3s ease` (1): link colour fades and a filter shift, likely the card hover. The greeting appears to be an animated word cycle, but a static capture cannot confirm timing.

## 8. Brand system
Only the home page is captured, so this section is confined to what it shows.
- **Information architecture:** identity (logos, colour), writing (brand narrative), illustration (shape language, colour), marketing, resources (downloads). Deep links from the census: `/identity/logos`, `/identity/color#core-brand-colors`, `/writing/brand-narrative`, `/illustration/shape-language#color`, `/resources`.
- **One colour per discipline** with `--guide-color: #58cc02` as the only declared token, suggesting subpages re-theme through one variable.
- **Voice:** the intro is casual and multilingual ("Language never stands still — and neither do we").
- **Token decisions worth stealing:** single 16 px radius; lowercase display headings; per-section hue as a CSS variable.
- **Unknown:** logo clearspace, minimum size, misuse, imagery rules.

## 9. UX
Clear: five labelled doors plus a quick-link shortcut. Weaknesses: a half-empty second row, low-contrast white text on every card, 14 px grey footer, and no search.

## 10. Craft signals
- Hero greeting fades out at its right edge instead of wrapping.
- Cards share a 16 px radius and equal 431 px width with 24 px gaps.
- Illustrations are cropped by the card edge, making each card read as a window onto a scene.
- Uppercase CTAs carry 0.75 px tracking, correct for small caps.

## 11. Reproduction recipe
```css
:root{--guide-color:#58cc02;--blue:#1cb0f6;--purple:#ce82ff;--orange:#ffb100;--coral:#ff7878}
.card{border-radius:16px;padding:36px;color:#fff;min-height:280px;position:relative;overflow:hidden}
.card h1{font:700 36px/36px Feather,"DIN Round",sans-serif;text-transform:lowercase}
.card p{font:400 15px/23.25px "DIN Round",sans-serif}
.cta{font:700 14px/14px "DIN Round";letter-spacing:.75px;text-transform:uppercase;transition:color .3s ease}
.grid{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;padding:0 50px}
@media(max-width:600px){.grid{grid-template-columns:1fr}}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 7 | Joyful, instantly recognisable palette and illustration cropping. |
| Originality | 6 | Colour-coded cards are known, but the multilingual hero is on-brand. |
| Usability | 5 | Easy navigation, but white on pastel fails AA throughout; home-only evidence. |
| Craft | 6 | Consistent radius and gutters; thin token set, status overlay in capture. |

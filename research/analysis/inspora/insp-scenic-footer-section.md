---
id: insp-scenic-footer-section
source: inspora
category: Web
status: analyzed
title: "Scenic Footer Section"
creator: "elaya (@elayadesigns)"
styles: [duotone, editorial-serif, hand-drawn, corporate-clean]
patterns: [illustrated-landscape-footer, sitemap-mega-footer, vertical-social-icon-stack, ambient-sprite-drift, sky-as-text-zone]
mode: light
palette: ["#ede0d2", "#d0cbc9", "#b6bac8", "#8897b7", "#5f7aaa", "#285094", "#111111"]
type_families: ["Inter / Geist-style neo-grotesk (likely)"]
type_class: [neo-grotesk]
radius_px: []
motion: {durations_s: [7.89], easing: [linear], loop: false}
scores: {aesthetics: 9, originality: 7, usability: 7, craft: 7}
craft_signals: [toile-blue-monotone-illustration, text-placed-in-sky-negative-space, scene-weighted-right-text-left, slow-linear-boat-drift, single-ink-ui-over-duotone]
anti_patterns: [cloud-texture-behind-small-links, tiny-link-size, uneven-column-spacing]
---
# Scenic Footer Section — elaya

## 1. Snapshot
- **Subject:** A 7.9 s, 1044×720 capture of a SaaS footer for "Metricra". A blue-on-cream engraved landscape (Mediterranean coast, a domed church and campanile on a cliff, cypresses, a moored fishing boat) fills the section. A 4-column sitemap floats in the sky.
- **Why it's remarkable:** It replaces the default dark utility footer with a Delft/toile-style etching. The sitemap stays purely functional black text, and the only motion is a fishing boat slowly crossing the bay: calm, "end of journey" storytelling.

## 2. Composition & layout
- **Diagonal split:** The illustration's weight sits in the lower-right (cliff, church, tree crown at top-right, about 45% of the frame). The upper-left ~55% is sky and cloud, where all the UI lives.
- **Columns:**
  - Logo and a vertical stack of 3 social icons (Instagram, LinkedIn, X at a 38 px pitch) at x≈62.
  - Navigation at x≈241, Solutions at x≈379, Resources at x≈546, Company at x≈694.
  - The column gaps vary (138 / 167 / 148 px), so they follow content width rather than a strict grid.
- **Rows:** Headers at y≈83, links at a 22.6 px pitch. The longest column (Resources, 10 items) ends at y≈312, just above the horizon (y≈490). The text never crosses the mountains.
- **Edges:** No top border or container. The scene is full-bleed.

## 3. Typography
- One neo-grotesk (Inter/Geist-like).
- **Column headers:** about 12.5 px, weight 500, near-black.
- **Links:** about 10 px, weight 400, near-black.
- **Logo:** "Metricra" at about 18 px, weight 500, with a four-point compass/sparkle mark.
- **Overall:** The scale is very small (10 px links at 1044 capture width, about 13–14 CSS px if the original was a 1440 viewport). There are no serifs despite the "editorial" tag; the elegance comes from the image, while the type stays neutral.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #ede0d2 | cream paper / sky highlights | 19% |
| #d0cbc9 | cloud mid-tone | 28% |
| #b6bac8 / #aaacb9 / #99a6c0 | haze, sea, distant hills | 16% |
| #8897b7 / #5f7aaa / #4c689d | engraved mid-blues | 21% |
| #285094 / #3a609e | darkest ink-blue (foliage, rocks) | 9% |
| #111111 | UI text, icons | <2% |

WCAG checks:
- Text on the cream sky is 14.56:1.
- Text on the cloud grey is 11.75:1.
- Text on the haze (#b6bac8) is 7.41:1.
- The ink-blue as a potential accent is 6.08:1 on cream.

All pass, because the text stays in the bright upper half. The illustration is a strict two-colour duotone (cream plus cobalt). The UI adds only black, no third hue.

## 5. Depth & material
- **Depth:** It comes from engraving technique. Line density increases toward the foreground (rocks at #285094) and recedes into haze for the far hills (#b6bac8), classic aerial perspective in one ink.
- **Texture:** A visible paper grain and hatching across the whole frame.
- **UI:** flat, with no shadows, scrims or containers.

## 6. Components & patterns
- A mega footer sitemap with 4 groups (5 / 9 / 10 / 3 links) and title-case headers.
- Vertically stacked icon-only social links beside the logo.
- An illustrated scene as the section background, with the UI positioned to avoid the busy areas.
- No newsletter field, copyright or legal bar is visible. It is a pure sitemap and scene.

## 7. Motion
Measured: 7.89 s at 30 fps, motion_fraction **0.01**, 0 segments above threshold, not a loop (first/last diff 5.21).
- The only moving element is the boat. Across the 9 frames it travels from x≈35 to x≈210 in source px over about 7 s, roughly **25 px/s at constant speed (linear)**. That is below the detector threshold, which confirms how subtle it is.
- A gentle water-reflection shimmer may also be present (estimate). Clouds look static.
- It is ambient, sub-perceptual life rather than an interaction.

## 8. Brand system
n/a — not a brand system. Identity cues:
- the compass-rose logomark echoes the voyage and coast imagery;
- a cobalt-and-cream "Delftware" duotone that could extend to illustrations site-wide.

## 9. UX
- **Strengths:** All text contrast passes (7.4–14.6:1), groups are clear, and the motion is non-distracting.
- **Weaknesses:**
  - Links are very small (about 10 px in capture).
  - Cloud hatching behind the Solutions and Resources columns adds texture noise under glyphs.
  - Column spacing is irregular.
  - The footer lacks legal/copyright and contact affordances.
  - Mobile reflow would push text over the cliff illustration.

## 10. Critical craft signals
- The bottom of the tallest link column (y≈312) clears the horizon line (y≈490) by about 180 px. The layout respects the scene.
- The illustration is strictly two-ink, with no stray hues introduced by the UI.
- The heaviest visual mass (church plus tree) counter-weights the text block on the diagonal.
- The boat moves at a constant ~25 px/s, slow enough to be discovered rather than noticed.
- The compass logomark ties into the maritime theme.

## 11. Reproduction recipe
```css
:root{--cream:#ede0d2;--cobalt:#285094;--haze:#b6bac8;--ink:#111;--sans:"Inter",system-ui,sans-serif}
.footer{position:relative;min-height:720px;background:url(coast-etching.jpg) right bottom/cover,var(--cream);
  display:grid;grid-template-columns:180px repeat(4,max-content);column-gap:clamp(48px,6vw,96px);
  align-content:start;padding:80px 64px;font:400 14px/1.6 var(--sans);color:var(--ink)}
.footer h4{font-weight:500;font-size:16px;margin-bottom:12px}
.footer .social{display:grid;gap:14px;margin-top:28px}
.boat{position:absolute;left:0;top:67%;width:80px;animation:sail 40s linear infinite}
@keyframes sail{from{transform:translateX(-10vw)}to{transform:translateX(60vw)}}
@media (prefers-reduced-motion:reduce){.boat{animation:none}}
/* duotone any illustration */
.etch{filter:grayscale(1) sepia(1) hue-rotate(185deg) saturate(3) contrast(1.1)}
```
Use equal column gaps and 14 px or larger links. Optionally add a 40% cream wash behind the text block.

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 9 | A gorgeous one-ink etching with UI placed in the quiet sky. |
| Originality | 7 | Illustrated footers are trending, but the toile/Delft engraving style for SaaS is a distinctive choice. |
| Usability | 7 | High contrast everywhere. Links are tiny and secondary footer content is missing. |
| Craft | 7 | Thoughtful scene-text balance and subtle drift. Uneven column gaps and cloud texture under links. |

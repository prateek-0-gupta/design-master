---
id: insp-train-animation
source: inspora
category: Web
status: analyzed
title: "footer train animation"
creator: "@alimdesigner_"
styles: [hand-drawn, editorial-serif, monochrome, minimal-swiss]
patterns: [illustrated-viaduct-footer, crossing-train-loop, smoke-particle-trail, staggered-link-reveal, themed-column-headings, serif-sans-footer-pairing]
mode: light
palette: ["#ffffff", "#513423", "#654a3a", "#85736b", "#b7ada7", "#dcd8d6", "#1a1a1a", "#6b6b6b"]
type_families: ["Fraunces / Source Serif-style soft serif for wordmark and headers (likely)", "Inter (likely)"]
type_class: [transitional-serif, neo-grotesk]
radius_px: []
motion: {durations_s: [8.37], easing: [linear, ease-out], loop: true}
scores: {aesthetics: 9, originality: 8, usability: 8, craft: 8}
craft_signals: [metaphor-carried-into-ia-labels, sepia-engraving-single-ink, smoke-fades-with-distance, viaduct-as-page-baseline, staggered-link-fade-in, logo-wheel-glyph]
anti_patterns: [illustration-heavy-for-footer]
---
# footer train animation — @alimdesigner_

## 1. Snapshot
- **Subject:** A 9.6 s, 1928×1080 capture of a footer for "meridian", a project-delivery SaaS. A sepia engraved stone viaduct spans the full width, and a steam locomotive with tender and two wagons crosses it left to right, trailing billowing smoke, while a 3-column serif/sans sitemap sits above.
- **Why it's remarkable:** The metaphor goes all the way through. The tagline "The scenic route to shipped work… from station to station", the column names (Explore / Journeys / Depot), the wheel logomark and the train all tell one story. The animation is a narrative sign-off, not decoration.

## 2. Composition & layout
- **Two zones:** a text band at the top (y≈60–220) and the illustration band in the lower ~60%.
- **Viaduct deck:** at y≈695, acting as a hard horizontal baseline across 100% of the width. There are 8 arches about 240 px apart, cropped at the bottom edge.
- **Brand block:** at x=255, with the logo and wordmark, a 2-line tagline (max ~370 px) and the copyright.
- **Nav:** three columns at x≈895, 1163 and 1431, an even 268 px pitch. Headers sit at y≈73 and links at a 45 px pitch.
- **Train:** about 830 px long including the wagons, plus smoke reaching y≈400. It occupies the empty middle band, so text and animation never collide.

## 3. Typography
- **Serif:** The wordmark "meridian" and the column headers use a soft, slightly wedge-serifed text face (Fraunces- or Source Serif-like). The wordmark is about 34 px at weight 500 and the headers about 21 px at weight 600, in #1a1a1a.
- **Sans:** Links, tagline and copyright use a neutral grotesk (Inter-like). Links are about 19 px regular in #3d3d3d, the tagline about 17 px, and the copyright about 15 px in #6b6b6b.
- **Pairing:** The serif carries the heritage and journey voice while the sans keeps the SaaS utility. The pairing mirrors the engraving-meets-product theme.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #ffffff | canvas, arch voids | 65% |
| #513423 / #654a3a | dark sepia ink (arch shadows, loco) | 10% |
| #85736b / #90827b / #a79c96 | mid hatching | 9% |
| #b7ada7 / #cbc6c2 / #dcd8d6 | light hatching, far smoke | 10% |
| #1a1a1a | headers, wordmark | <1% |
| #3d3d3d / #6b6b6b | links / meta | <1% |

WCAG checks:
- Headers are 17.4:1.
- Links #3d3d3d are 10.86:1.
- Copyright #6b6b6b is 5.33:1.
- The sepia ink #513423 used as text would be 11.26:1.

Everything passes. The page is a strict single-ink sepia illustration on white, with the UI in neutral greys.

## 5. Depth & material
- **Engraving:** Depth comes from line density. The arch intrados are heavily hatched (#513423) while the piers are lighter brick, the classic etched technical-plate look.
- **Smoke:** It is drawn as outlined puffs that lighten and lose line weight as they age and trail behind. Compare the dark puffs near the chimney with the faint grey ones at x≈700 in the key frame, which gives atmospheric depth.
- **UI:** no shadows or containers. A 1 px grey rule at the very top (y=0) separates the footer from the preceding section.

## 6. Components & patterns
- Brand block: wheel/compass glyph, wordmark, tagline and copyright.
- A three-column sitemap with themed headings (Explore: Platform, Workflows, Integrations; Journeys: For Teams, Studios, Agencies; Depot: About, Journal, Contact).
- **Link reveal:** At 0.53 s "For Agencies" and "Journal" are still at about 30% opacity while the others are solid, which shows a top-to-bottom, column-by-column staggered fade-in on enter.
- **Train loop:** It enters from the left at 0.5 s, crosses, and exits right by about 8.5 s. Then the viaduct sits empty until the loop restarts.

## 7. Motion
Measured: 9.59 s at 60 fps, motion_fraction 0.70, one long segment of 0.10–8.47 s (8.37 s, peak_at 0.34, ease-out profile), `seamless_loop_likely: true`.
- **Train:** The front moves from about x=1084 at 3.73 s to about x=1719 at 5.86 s, roughly **300 px/s, constant (linear)**. A full crossing of the 1928 px screen plus the train length takes about 8.4 s, matching the measured segment.
- **Why "ease-out":** The energy peak early in the segment comes from the smoke volume being largest while the whole train and plume are on screen, plus the initial link stagger. It is not a deceleration of the train.
- **Smoke:** The puffs spawn at the chimney, grow, drift up and back, and fade out over about 2–3 s.
- **After the exit:** about 1.1 s of stillness (8.47 to 9.59 s) before the loop, a nice breath.

## 8. Brand system
n/a — not a brand system, but it carries an unusually coherent identity:
- the railway metaphor runs through the copy ("scenic route", "station to station"), the IA labels (Journeys, Depot) and the logomark (wheel);
- a sepia engraving style that would scale to empty states and onboarding.

## 9. UX
- **Strengths:** All text passes AA comfortably, the columns are even, the motion stays below the text, and the loop includes rest time.
- **Weaknesses:**
  - The large raster or SVG engraving is heavy for a footer.
  - No `prefers-reduced-motion` handling is visible. The train should park mid-viaduct when motion is reduced.
  - The themed labels ("Depot") trade a little scannability for charm.

## 10. Critical craft signals
- The IA headings are rewritten into the metaphor (Explore / Journeys / Depot), so copy and illustration agree.
- The column pitch is exactly even (268 px) and the brand block aligns to the same top as the headers.
- Smoke puffs lighten with age (line colour goes from #513423 toward #cbc6c2).
- The viaduct deck is a perfectly straight full-bleed horizon, so the train has a true track and the page a clear baseline.
- Link fade-in staggers through the columns (0.53 s frame).
- The illustration uses one ink only, and the UI greys never compete with it.

## 11. Reproduction recipe
```css
:root{--paper:#fff;--ink:#1a1a1a;--ink-2:#3d3d3d;--meta:#6b6b6b;--sepia:#513423;
  --serif:"Fraunces","Source Serif 4",Georgia,serif;--sans:"Inter",system-ui,sans-serif}
.footer{position:relative;overflow:hidden;min-height:1080px;background:var(--paper);border-top:1px solid #e6e6e6;
  display:grid;grid-template-columns:1fr repeat(3,268px);padding:60px 255px 0;font:400 19px/2.35 var(--sans);color:var(--ink-2)}
.footer h4,.wordmark{font-family:var(--serif);color:var(--ink)} .footer h4{font-size:21px;font-weight:600}
.footer li{opacity:0;animation:in .4s ease-out forwards;animation-delay:calc(var(--i)*60ms)}
@keyframes in{to{opacity:1}}
.viaduct{position:absolute;inset:auto 0 0;height:36%;background:url(viaduct.svg) repeat-x bottom/auto 100%}
.train{position:absolute;bottom:36%;left:0;width:830px;animation:cross 9.6s linear infinite}
@keyframes cross{0%{transform:translateX(-850px)}88%{transform:translateX(1928px)}100%{transform:translateX(1928px)}}
.puff{position:absolute;animation:puff 2.6s ease-out forwards}
@keyframes puff{from{transform:scale(.4);opacity:1}to{transform:translate(-120px,-90px) scale(1.4);opacity:0}}
@media (prefers-reduced-motion:reduce){.train{animation:none;transform:translateX(40vw)}.puff{display:none}}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 9 | A beautiful single-ink engraving with a clean serif/sans footer and generous white space. |
| Originality | 8 | The brand metaphor fully realised in IA, copy and motion lifts it above the generic illustrated footer. |
| Usability | 8 | Legible, evenly structured links. Motion is confined below the content. |
| Craft | 8 | Even column rhythm, ageing smoke and a staggered reveal. Asset weight and missing reduced-motion are the gaps. |

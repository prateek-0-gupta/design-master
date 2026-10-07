---
id: insp-dither-cards
source: inspora
category: Motion
status: analyzed
title: "Dither Cards"
creator: "Praveen Kumar (@praveenisomer)"
styles: [dither-halftone, editorial-serif, minimal-swiss, monochrome]
patterns: [dithered-hero-image, animated-dither-video-in-card, serif-title-sans-meta, metric-ring-footer, delta-badge, pixel-dissolve-background, tall-portrait-card]
mode: light
palette: ["#ffffff", "#dedede", "#a6a6a6", "#262626", "#616060", "#9b8cf0", "#e4def0", "#e0435a"]
type_families: ["Tiempos / Newsreader-style text serif (likely)", "Inter (likely)"]
type_class: [editorial-serif, transitional-serif, neo-grotesk]
radius_px: [0, 6]
motion: {durations_s: [5.3, 0.67], easing: [ease-in, ease-in-out], loop: false}
scores: {aesthetics: 9, originality: 8, usability: 6, craft: 8}
craft_signals: [ordered-dither-matches-background-pixel-grid, single-tint-dither-on-one-card, square-card-corners, hairline-divider-under-header, conic-ring-uses-three-hues, image-bleeds-to-card-padding-edge]
anti_patterns: [light-grey-meta-text, abstract-copy-low-information]
---
# Dither Cards — Praveen Kumar

## 1. Snapshot
- **Subject:** A 10 s, 60 fps, 1920×1440 clip of two tall finance "insight" cards side by side on a grey, pixel-dithered backdrop:
  - "Capital Metamorphosis", with a lavender-dithered dahlia;
  - "Sensitive Dependencies", with a black-and-white dithered video of a chrysalis or moth emerging that resolves into a butterfly.
- **Why it's remarkable:** Ordered or Bayer-style dithering turns stock nature imagery into a coherent 1-bit aesthetic shared by the cards and the backdrop. A metamorphosis video becomes a visual metaphor for the card copy ("Capital Metamorphosis").

## 2. Composition & layout
- **Cards:** two at about 595×1290 px (ratio about 1:2.17), with a gap of about 85 px, centred. Each has 20 px internal padding.
- **Image zone:** the top 64% (about 555×810 px). The image bleeds to the padding edge with no radius.
- **Header row:** "MY CARD" label at the left and an outlined "Add Card" button (about 120×38 px, radius about 6 px) at the right, with a 1 px divider below.
- **Meta row:** calendar and clock icons with "Dec 05" and "11:00 AM".
- **Title block:** a two-line serif title on the left, and "Today" plus a red delta badge (↘ 6.2%) on the right.
- **Body:** three lines of grey copy, max width about 65% of the card.
- **Footer:** an 84 px conic ring chart, a label ("Efficiency Delta" / "Variance Threshold") and a 40 px square arrow button at the far right.
- **Backdrop:** #dedede with large dithered grey shapes (cloud-like blobs) made of 6–10 px square pixels framing the cards.

## 3. Typography
- **Titles:** a text serif with moderate contrast and bracketed serifs, close to Tiempos Text, Newsreader or Source Serif. About 36 px Regular, leading about 0.95 (tight, lines nearly touching), tracking about −0.01 em.
- **UI sans (Inter-like):**
  - "MY CARD" about 15 px Medium, uppercase, slight tracking;
  - meta about 15 px Regular grey;
  - body about 15 px Regular #616060 with 1.3 leading;
  - footer label about 15 px #939393.
- The serif-plus-sans pairing reads as an editorial magazine on a fintech component.

## 4. Colour
| Hex | Role | Approx share |
|---|---|---|
| #ffffff | card surface | 30% |
| #dedede | backdrop base | 22% |
| #a6a6a6 / #939393 | backdrop dither pixels, footer label | 21% |
| #262626 | titles, dithered black image | 7% |
| #616060 | body copy | 2.6% |
| #9b8cf0 → #e4def0 | dahlia dither tint (periwinkle to pale lilac) | ~11% |
| #e0435a | delta badge (negative) | <0.5% |

The ring charts mix lavender, red and green arcs.

WCAG checks:
- Title #262626 on white is 15.13:1.
- Body #616060 is 6.27:1.
- Footer label #939393 is **3.07:1 (fail)**.
- Badge text #e0435a on #fdeef0 is 3.65:1 (fails at its about 11 px size).

## 5. Depth & material
- Completely flat: square-cornered white cards with no shadow on a flat grey ground. Depth comes only from the dither field behind, whose pixel clusters are coarser at the bottom right and finer at the top left, giving a faint atmospheric gradient.
- **Dither as material:**
  - The dahlia uses a single-hue ordered dither (lavender dots on white).
  - The moth uses a pure 1-bit black/white dither with visible cross-hatch Bayer patterns.
  - Pixel size inside the images is about 4 px, and in the backdrop about 8 px, so the backdrop reads as further away.

## 6. Components & patterns
- **Insight card:** a hero media slot, a header with a secondary action, a meta row, a title with trend, a description, and a metric footer with a navigation arrow.
- **Delta badge:** a pale red pill with an outline and a trending-down glyph.
- **Conic ring chart:** a thick 12 px stroke in three segments (lavender major, red and green minor) as a compact KPI.
- Outlined secondary buttons ("Add Card", arrow) with 1 px #dcdcdc borders.

## 7. Motion
- **Measured:** motion fraction 0.49 and `seamless_loop_likely: false` (first/last diff 7.95). Two segments:
  - **1.07–6.37 s (5.3 s, ease-in, peak at 1.0):** the right card's dithered video plays. The moth climbs out of the chrysalis (0.56 → 3.90 s), the camera pushes into extreme macro (5.01–6.13 s), and the energy builds to the end of the segment as the image fills the frame.
  - **7.37–8.03 s (0.67 s, symmetric):** a cut or transition to the open-winged butterfly, which then holds (8.36–9.47 s).
- The dahlia card is nearly static, with only slight dither shimmer and possibly a slow scale (its bloom size differs slightly between 0.56 s and 3.90 s, about 3%).
- The dither is applied per video frame, so the dot pattern "boils", which is part of the aesthetic.

## 8. Brand system
n/a — not a brand system. Identity cues:
- 1-bit and single-tint dither imagery;
- serif display titles;
- abstract, poetic finance copy ("Capital Metamorphosis", "Sensitive Dependencies").

## 9. UX
- The structure is clear and scannable: title, trend, explanation, KPI, next.
- The copy is atmospheric but low in information ("We track the divergence so you don't have to").
- The KPI ring has no numeric value. The red badge alone carries the number.
- Meta and footer text fail contrast. A motion-heavy dithered video inside a finance card may distract, and it needs a pause control or reduced-motion fallback.

## 10. Craft signals
- The backdrop and the images use the same square-pixel dither language at two scales (about 4 px in the images, about 8 px in the backdrop).
- Each card's image has one treatment (tinted versus 1-bit), so the pair reads as a set with variation.
- Cards have 0 px radius while the buttons have a radius of about 6 px: the sharp container contrasts with soft controls.
- A 1 px divider spans exactly the padding box under "MY CARD".
- The serif titles' two lines are set at leading below 1.0, so the descender of "Capital" nearly touches "Metamorphosis".
- The ring chart colours (lavender/red/green) echo the dahlia tint and the delta badge.

## 11. Reproduction recipe
```css
:root{--bg:#dedede;--card:#fff;--ink:#262626;--body:#616060;--muted:#6f6f6f;--tint:#9b8cf0;--neg:#d0334a;--line:#dcdcdc;
  --serif:"Newsreader","Tiempos Text",Georgia,serif;--sans:"Inter",system-ui,sans-serif}
.card{width:300px;background:var(--card);padding:10px;display:grid;gap:12px}
.card img{width:100%;aspect-ratio:.68;object-fit:cover;image-rendering:pixelated;filter:grayscale(1) contrast(1.4)}
.title{font:400 22px/.95 var(--serif);letter-spacing:-.01em;color:var(--ink)}
.eyebrow{font:500 11px var(--sans);text-transform:uppercase;letter-spacing:.04em}
.btn-ghost{border:1px solid var(--line);border-radius:6px;padding:6px 10px;font:500 12px var(--sans)}
.delta{border:1px solid color-mix(in oklab,var(--neg) 45%,#fff);background:#fdeef0;color:var(--neg);border-radius:4px;padding:2px 6px;font:500 11px var(--sans)}
.ring{width:44px;aspect-ratio:1;border-radius:50%;
  background:conic-gradient(#e0435a 0 18%,#4cd964 18% 32%,var(--tint) 32% 100%);
  -webkit-mask:radial-gradient(circle,#0000 58%,#000 60%)}
/* Dither: render the image to <canvas> and apply a 4x4 Bayer threshold per pixel; tint = mix(white, --tint, bit) */
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 9 | Striking editorial pairing of dithered nature imagery, a serif and a quiet UI, with a backdrop that matches. |
| Originality | 8 | Animated dithered video inside fintech cards, plus the metamorphosis metaphor, is fresh. |
| Usability | 6 | Clear structure, but grey meta fails contrast, the KPI ring has no value and motion runs constantly. |
| Craft | 8 | Pixel scales are consistent and the components disciplined. The tiny badge is under-contrasted. |

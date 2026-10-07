---
id: insp-stamp-style-cards
source: inspora
category: Branding
status: analyzed
title: "stamp-style cards"
creator: "@devxnuj"
styles: [minimal-swiss, photo-led, physical-material]
patterns: [perforated-stamp-card, half-image-half-text-split, alternating-image-position, numbered-card-series, woodblock-print-imagery, logo-and-index-corner-pair]
mode: dark
palette: ["#111111", "#f4f3e8", "#5a5a52", "#34739b", "#3d4c3f", "#b6ab7d", "#8baf9c"]
type_families: ["Inter / Geist-style neo-grotesk (likely)"]
type_class: [neo-grotesk]
radius_px: []
motion: null
scores: {aesthetics: 8, originality: 7, usability: 8, craft: 7}
craft_signals: [perforated-edge-made-from-background-colour, exact-50-percent-image-split, image-position-alternates-top-bottom-top, logo-left-number-right-corner-system, cream-not-white-paper, numerals-light-weight-large]
anti_patterns: [stray-capital-in-headline, perforation-scale-inconsistent-with-print-detail]
---
# stamp-style cards — @devxnuj

## 1. Snapshot
- **Subject:** One 2560×1440 slide showing three postage-stamp-shaped feature cards (01, 02, 03) for a calm "personal co-pilot" planning app. Each card pairs a Japanese woodblock-style landscape (pine-framed coast, wave-like clouds, terraced hills) with a headline and subline on cream paper.
- **Why it's remarkable:** The perforated stamp silhouette turns ordinary marketing cards into collectible objects. Ukiyo-e imagery gives a productivity app a slow, contemplative tone that is the opposite of hustle aesthetics.

## 2. Composition & layout
- Three cards, each about 609×1007 px (about 3:5), sit on #111111 with about 146 px gutters. The outer margins are about 220 px left and right and about 215 px top and bottom, so the row is optically centred.
- **Each card is split exactly in half:**
  - cards 1 and 3 have text on the upper half and image on the lower half;
  - card 2 inverts this (image upper, text lower).

  The alternation creates a top-bottom-top zigzag rhythm across the row.
- **Text halves:**
  - logomark at the top-left (about 82×48 px);
  - index numeral at the top-right (or bottom-right on card 2);
  - headline and subline set about 50 px from the left edge.
- **Perforations:** a dashed scallop of about 6 px teeth runs around all four edges.

## 3. Typography
- **Headlines:** neo-grotesk (Inter or Geist-like), medium (about 500), about 48 px with leading of about 1.2 and tight tracking (about −0.01 em). Each is two lines, for example "Your calm, / Personal co-pilot."
- **Sublines:** the same family, light/regular, about 28 px, in grey #5a5a52 with about 1.3 leading.
- **Index numerals:** "01" to "03" at about 62 px in a light weight. Large and quiet, they balance the logomark in the opposite corner.
- **Issue:** card 2 capitalises "Planning" mid-sentence, and card 1 capitalises "Personal" after a comma. The capitalisation is inconsistent.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #111111 | stage | 49% |
| #f4f3e8 / #edecd2 | cream stamp paper | 23% |
| #5a5a52 (est.) | subline grey | <1% |
| #34739b | woodblock sky/sea blue | 4% |
| #3d4c3f / #86957b / #8baf9c | pine and hill greens | 9% |
| #b6ab7d / #615f48 | terraced-field ochres | 6% |

WCAG checks:
- Headline #111111 on cream is 16.93:1.
- Subline #5a5a52 on cream is 6.24:1.
- The cream card on the black stage is 16.93:1.
- Woodblock blue on cream is 4.63:1, which would even work as an accent text colour.

Strategy: a monochrome UI (ink plus cream) with every hue delegated to the art, as with real stamps.

## 5. Depth & material
- The cards are flat, with no shadows.
- The paper look comes from:
  - the cream tone;
  - the perforated edge (the black stage bites into the card);
  - the print texture of the woodblock images (visible linework and flat colour areas).
- The images bleed to the perforation edge on three sides.

## 6. Components & patterns
- **Logomark:** a stylised black roof or gable (two stacked chevrons split by a white line), like a pagoda roofline or a paper plane.
- **Card system:**
  - one image half and one text half;
  - the logo and number always share the same row, in opposite corners;
  - the number sits opposite the logo.
- Series numbering suggests an onboarding carousel, feature trio or collectible set.

## 7. Motion
Still image, so no motion was observed. In a carousel, a gentle tilt (±2°) or a "tear-off" of the stamp would extend the metaphor.

## 8. Brand system
n/a — not a full brand system. Identity cues:
- the roof/chevron mark;
- cream and ink palette;
- Japanese landscape prints as the image library;
- a stamp silhouette as the container;
- calm, reassuring copy ("without the mental load", "so you don't have to").

## 9. UX
- The copy is short (a headline of at most 6 words and a subline of at most 9 words) and highly legible (16.9:1 and 6.2:1).
- Numbered cards make sequence and progress obvious.
- The alternating image position breaks scanning slightly, since the headlines are not on one line across cards. This is a deliberate trade for rhythm.

## 10. Craft signals
- The perforation is the stage colour cutting into the card, not a drawn border.
- The image and text halves split at exactly 50% height on all three cards.
- The logo is top-left and the number is top-right (mirrored to the bottom on card 2), keeping a corner system.
- The paper is cream (#f4f3e8), not white, which matches the aged-print imagery.
- The numerals are lighter in weight than the headlines, so they are present but secondary.
- Weak point: the perforation teeth (about 6 px) are small relative to the 609 px card. Real stamp proportions would be about 15–20 px.

## 11. Reproduction recipe
```css
:root{--stage:#111;--paper:#f4f3e8;--ink:#111;--ink-2:#5a5a52;--blue:#34739b;
  --font:"Geist","Inter",system-ui,sans-serif}
body{background:var(--stage)}
.stamp{width:609px;aspect-ratio:3/5;background:var(--paper);display:grid;grid-template-rows:1fr 1fr;
  /* perforation: radial holes punched from the edge */
  -webkit-mask:
    radial-gradient(circle 4px at 50% 0,#0000 98%,#000) 0 0/12px 51% repeat-x,
    radial-gradient(circle 4px at 50% 100%,#0000 98%,#000) 0 100%/12px 51% repeat-x;
  -webkit-mask-composite:source-in}
.stamp .art{background-size:cover}
.stamp:nth-child(2) .art{order:-1}
.stamp .copy{padding:50px;display:grid;grid-template-rows:auto 1fr auto auto}
.stamp h3{font:500 48px/1.2 var(--font);letter-spacing:-.01em;color:var(--ink)}
.stamp p{font:300 28px/1.3 var(--font);color:var(--ink-2)}
.stamp .idx{font:300 62px/1 var(--font)}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Calm cream and ink with gorgeous woodblock imagery and a strong collectible silhouette. |
| Originality | 7 | Stamp cards are a known motif; pairing them with ukiyo-e for a planner app is a fresh tonal choice. |
| Usability | 8 | High contrast, short copy and clear numbering. |
| Craft | 7 | Exact 50% split and corner system; inconsistent capitalisation and tiny perforations. |

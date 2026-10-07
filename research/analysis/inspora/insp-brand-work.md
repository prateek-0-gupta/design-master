---
id: insp-brand-work
source: inspora
category: Branding
status: analyzed
title: "Brand work"
creator: "@driceroland"
styles: [editorial-serif, photo-led, glassmorphism, hairline-ui]
patterns: [fine-art-painting-backdrop, floating-ui-card-over-art, flourish-monogram, suggestion-chip-row, pill-ghost-buttons, chat-agent-launcher, pixel-dot-grid-illustration, viewfinder-corner-brackets]
mode: mixed
palette: ["#21210a", "#ffffff", "#141414", "#d8ddce", "#a59b73", "#544c20", "#7d6d3e", "#8a8a8a"]
type_families: ["Signifier / Tiempos Headline Light-style serif (likely)", "Suisse Int'l / Inter-style neo-grotesk (likely)"]
type_class: [editorial-serif, neo-grotesk]
radius_px: [48, 64, 9999]
motion: null
scores: {aesthetics: 9, originality: 8, usability: 7, craft: 7}
craft_signals: [card-tint-sampled-from-painting, monogram-as-agent-avatar, one-pixel-pill-outlines, tight-negative-tracking-display-serif, frosted-panel-gradient-tint, white-on-black-send-button-single-filled-element]
anti_patterns: [typo-in-cta-wiew-demo, light-pill-text-on-mid-tone-art, placeholder-grey-below-aa]
---
# Brand work — @driceroland

## 1. Snapshot
- **Subject:** Four 1900×2160 slides of brand work for "figr", an AI shopping-agent company (the name appears in "Powered by figr").
- **Slides:**
  1. a dark olive hero card ("The agent who can show you") on a Hudson River School landscape;
  2. a white flourish monogram on a 19th-century harbour painting;
  3. a white chat-widget UI;
  4. a frosted prompt bar with chips over a mountain-valley painting.
- **Why it's remarkable:** It pairs museum-grade landscape oil paintings with spare hairline UI. AI is framed as craft and taste, not neon tech. Every UI tint is pulled from the painting behind it.

## 2. Composition & layout
- **Slide 1:**
  - The card is about 800×905 px at x≈549–1350 and y≈625–1530, with a radius of about 48 px. It sits off-centre right of the tree, over the painting's darkest mass.
  - The headline is top-left with about 62 px inner padding.
  - The CTAs sit below the headline with about 55 px gap.
  - A dot-matrix illustration (5×11 dots on about 48 px pitch, framed by a 3 px hairline rectangle and a "viewfinder" bracket square) fills the bottom half.
- **Slide 2:** the monogram is about 240 px wide, centred at about 46% height, in the painting's empty sky. The narrative figures stay in the bottom 20%.
- **Slide 3:**
  - The widget is about 910×1475 px with a radius of about 64 px, nested inside a larger off-white panel that is cropped by the frame.
  - Header row: avatar, name, "New session" pill, ⋯ and ✕.
  - About 500 px of empty space precedes the greeting, which is bottom-anchored like a chat.
  - Then a three-chip row, the input pill and "Powered by figr".
- **Slide 4:** a frosted panel bleeds off the right edge (x≈327→1900, about 412 px tall). Three dark suggestion tags float above it, and three outline pills sit inside.

## 3. Typography
- **Display:** a light, high-x-height serif with small bracketed serifs and tight negative tracking (about −0.03 em), resembling Signifier Light or Tiempos Headline Light.
  - "The agent who / can show you" is about 85 px with leading of about 1.0.
  - "I can help you / find what you need." is about 68 px.
  - "Ask me to find what you need" is about 100 px.
- **UI text:** a neo-grotesk (Suisse/Inter-like).
  - Name "Lana" about 30 px semibold, role about 26 px medium grey.
  - Body copy about 22 px with about 1.6 leading.
  - Chips about 24 px regular.
- **Wordmark:** "figr" in the display serif at about 30 px, preceded by the flourish monogram.
- **Monogram:** a looping calligraphic figure built from one monoline stroke (about 22 px at 240 px size) with spiral terminals. It reads as an "f" and an "x"/pretzel loop.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #21210a | hero card fill (olive-black from painting shadows) | slide 1: 15% |
| #ffffff | text on dark; widget surface | slide 3: 37% |
| #141414 | widget ink, send button | — |
| #d8ddce / #e5e8d7 | painted sky (backdrop) | slide 1: 27% |
| #544c20 / #7d6d3e | frosted panel tints (slide 4) | 11% / 7% |
| #a59b73 / #bab09a | sepia ground and harbour sky | slide 2: 40% |
| #8a8a8a (est.) | input placeholder | — |

WCAG checks:
- White on the olive card is 16.32:1.
- Widget ink on white is 18.42:1.
- White on the darker frosted area (#544c20) is 8.64:1.
- White on the lighter right-hand area (#7d6d3e) is 5.09:1, so the right part of the slide-4 headline is near the AA limit.
- The white monogram on the harbour sky (#a09c91) is only 2.74:1. It is legible through its size, but would fail as text.
- The placeholder grey on white is 3.45:1, which fails AA-normal.

## 5. Depth & material
- **Hero card:** opaque, with no shadow. Its colour, sampled from the painting, makes it feel set into the scene.
- **Slide 4 panel:** a frosted glass bar. Its tint grades from about #3d3e2e on the left to warm #8b7c66 on the right, following the painting behind it (a blur plus a colour-dodge feel).
- **Widget:** pure white with a very soft large shadow (about 0 30px 80px rgba(0,0,0,.08)) and a 1 px outer edge, nested in a second panel with a similar radius. The double-radius stack gives a layered effect.
- **Backgrounds:** the paintings keep their canvas texture and craquelure, so the backdrop has real texture.

## 6. Components & patterns
- **Buttons:**
  - primary "Try now": a 1.5 px outline pill about 62 px tall;
  - secondary "Wiew demo" (sic): text-only.
- **Chips:**
  - Suggestion chips: three equal-width outline pills ("Let me explore", "What's new?", "Try on live").
  - Context tags: filled dark-translucent pills ("Yellow lamp", "Grey cosy carpet", "70's desk").
- **Input:** a pill about 84 px tall with a 2 px #141414 outline and a filled circular send button (about 60 px, the only solid black element).
- **Header:** a 64 px avatar with a green presence dot; "New session" pill with an icon; ⋯ and ✕ in 60 px outlined circles.
- **Illustration:** a dot grid plus a camera bracket ("show you" means visual search).

## 7. Motion
Still images, so no motion was observed.

## 8. Brand system
This is a brand system in miniature (the slides are applications, not guidelines).
- **Logo:** a flourish monogram that works standalone (slide 2), as the agent's avatar (slides 3 and 4), and locked up as "monogram + figr".
- **Imagery:** 19th-century American and European landscape and genre paintings (public-domain look).
- **Colour:** derived from the image; there is no fixed accent.
- **Type:** light serif for the voice, grotesk for UI.
- **Voice:** first-person, service-like ("I can help you find what you need", "Ask me to find…").
- **UI language:** 1–2 px outline pills, with exactly one filled element per view.

## 9. UX
- The chat widget is a strong pattern:
  - a bottom-anchored greeting;
  - three starter intents;
  - a placeholder showing a natural-language example ("A relaxed linen shirt for summer");
  - clear "New session" and close controls.
- The role label is truncated ("Assistant manag…").
- The placeholder contrast fails AA.
- The typo "Wiew demo" sits in the hero CTA.
- Over art, text contrast varies with the painting: it is fine in shadows and weak in skies.

## 10. Craft signals
- The hero card's #21210a is sampled from the painting's foliage shadows, so the card belongs to the scene.
- All pills use the same about 1.5 px stroke, and only the send button is filled.
- The display serif uses about −0.03 em tracking with leading of about 1.0 on two-line headlines.
- The monogram works at about 240 px (hero), about 36 px (widget) and about 24 px (footer lockup).
- The widget's nested radii (inner about 64 px, outer about 80 px) are concentric.
- The suggestion chips are equal width (about 242 px each), so the row reads as one control.

## 11. Reproduction recipe
```css
:root{--olive:#21210a;--paper:#fff;--ink:#141414;--muted:#6b6b6b;--sky:#d8ddce;
  --serif:"Signifier","Tiempos Headline",Georgia,serif;--sans:"Suisse Int'l","Inter",system-ui,sans-serif;
  --r-card:48px;--r-widget:64px;--r-pill:9999px;--stroke:1.5px;}
.hero{background:url(landscape.jpg) center/cover}
.card{background:var(--olive);color:var(--paper);border-radius:var(--r-card);padding:62px;width:800px}
.card h1{font:300 85px/1 var(--serif);letter-spacing:-.03em}
.pill{border:var(--stroke) solid currentColor;border-radius:var(--r-pill);padding:14px 30px;font:400 22px/1 var(--sans)}
.frost{background:linear-gradient(90deg,rgba(40,38,20,.75),rgba(140,124,102,.55));backdrop-filter:blur(24px) saturate(1.2);border-radius:40px 0 0 40px}
.widget{background:var(--paper);border-radius:var(--r-widget);box-shadow:0 30px 80px rgba(0,0,0,.08)}
.input{border:2px solid var(--ink);border-radius:var(--r-pill);height:84px}
.input::placeholder{color:var(--muted)} /* #6b6b6b passes 5.3:1 */
.send{width:60px;aspect-ratio:1;border-radius:50%;background:var(--ink);color:#fff}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 9 | Fine-art backdrops plus a hairline serif UI give a calm, luxurious AI identity. |
| Originality | 8 | Painting-led AI branding is emerging but rarely this disciplined; the flourish monogram as avatar is fresh. |
| Usability | 7 | The chat pattern is excellent; there is a placeholder contrast failure and variable text-over-art contrast. |
| Craft | 7 | Sampled tints and stroke consistency; the "Wiew demo" typo and truncated role label cost points. |

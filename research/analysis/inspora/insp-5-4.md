---
id: insp-5-4
source: inspora
category: Motion
status: analyzed
title: "Floating cards"
creator: "@joshpuckett"
styles: [editorial-serif, maximalist-color, technical-wireframe, x-card-fan]
patterns: [fanned-card-deck, tilt-on-rest-straighten-on-select, card-expand-to-detail, generative-cover-art, course-module-cards]
mode: light
palette: ["#fefefe", "#d33915", "#f2e7d5", "#1a8cc0", "#56ff8f", "#1d1c1a", "#a08671", "#6b6b6b"]
type_families: ["EB Garamond / Cormorant-style old-style serif (likely)", "Inter (likely)"]
type_class: [editorial-serif, neo-grotesk]
radius_px: [30, 20]
motion: {durations_s: [0.4, 0.37, 0.33], easing: [ease-in-out, ease-out], loop: false}
scores: {aesthetics: 9, originality: 8, usability: 7, craft: 9}
craft_signals: [each-card-own-generative-motif, alternating-rotation-angles, serif-title-sans-body, title-tint-matches-card-ink, hairline-rule-above-title, cards-dock-below-on-expand]
anti_patterns: [white-on-blue-card-below-aa-for-body]
---
# Floating cards — @joshpuckett

## 1. Snapshot
- **Subject:** A 16.0 s, 2530×1844 (60 fps) hero for "Interface Craft". Five course-module cards are fanned like a hand of playing cards, and clicking one lifts it upright and expands it into a detail card. The cards are:
  - Working Knowledge (red);
  - Practical Demonstration (cream);
  - Collaborating with AI (blue);
  - Building Interface Kit (green);
  - Interface Kit (black).
- **Why it's remarkable:** Every card has its own generative cover motif in its own palette, yet they read as one family through shared serif type, radius and size.

## 2. Composition & layout
- **Header (centred):** A 115 px hairline rule at y≈255. Under it, the serif title "Interface Craft" (cap height about 70 px, font size about 95 px), then a two-line grey subtitle at about 33 px.
- **Fan:** Five cards about 360×480 px, overlapping by about 40%. Each is rotated individually (about −6°, −3°, +2°, −2°, +4°), and the fan spans about 1400 px across.
- **Expanded state:** A single card about 723 px wide, with a radius of about 30. It is upright and centred, with the rest of the deck docked and cropped at the bottom edge (y>1640), peeking out.

## 3. Typography
- **Serif:** An old-style face with a calligraphic "ft" ligature in "Craft", close to EB Garamond or Cormorant. It is used for the page title and every card title, which sits about 64 px on the expanded card in two lines with tight leading of about 0.95.
- **Sans:** Inter-like at about 30 px with leading of about 1.55, used for descriptions and the subtitle.
- **Colour:** Card titles take the card's ink colour (dark brown #3a2f24 on cream, white on blue or black, dark on green).

## 4. Colour
| Hex | Role |
|---|---|
| #fefefe | canvas |
| #d33915 | Working Knowledge card (vermilion) |
| #f2e7d5 | Practical Demonstration card (cream) |
| #a08671 | cream-card mosaic tiles (taupe range) |
| #1a8cc0 | Collaborating with AI card (cerulean) |
| #56ff8f | Building Interface Kit card (neon mint) |
| #1d1c1a | Interface Kit card (warm black) |
| #6b6b6b | subtitle grey |

WCAG:
- Title #1d1c1a on #fefefe is 16.88:1, and subtitle #6b6b6b on #fefefe is 5.28:1.
- Brown title #3a2f24 on cream is 10.65:1, and cream-card body #6a5f52 is 5.09:1.
- White on vermilion is 4.81:1.
- White on cerulean is **3.78:1**, which passes only for large text. The about 14 px body on the blue card fails.
- Dark on mint is 13.05:1, and white on black is 17.03:1.

## 5. Depth & material
- **Cards:** Flat print-like colour with no gradients, and soft shadows from the overlapping fan.
- **Cover art:** Each card has a graphic system: line-hatching waves (red, blue), a pixel mosaic (cream), a vertical barcode-like dither (green) and a wireframe UI layout (black). The motifs evoke printmaking or riso-like covers.
- **Expanded card:** It casts a broader shadow and covers the docked deck.

## 6. Components & patterns
- A fanned deck as navigation between modules.
- Card anatomy: cover-art band at the top (about 45% of the height), then a serif title, then a 3–4 line sans description.
- **Select:** the card rotates to 0°, scales about 1.9× and translates to centre. The others slide down to dock.

## 7. Motion
- **Measured:** 7 segments across 16.03 s, median 0.37 s (0.33–0.40 s). `seamless_loop_likely: false`.
  - 6.30 s: 0.37 s, peak 0.41. 8.43 s: 0.33 s, peak 0.45. Both symmetric ease-in-out: expand and collapse.
  - 9.50 s, 10.57 s, 11.37 s and 12.50 s: 0.33–0.37 s, peak 0.15–0.32, i.e. ease-out. Switching between cards, which settle softly.
- **Read:** Consistent 330–400 ms transitions. Frames show no overshoot, and rotation and scale tween together.

## 8. Brand system
n/a — not a brand system, but it behaves like a mini-system. The rules are one serif, one sans, one card size and radius, and one generative motif per module. The hairline rule plus serif title signals an "editorial library".

## 9. UX
- The fan invites exploration, and the docked deck keeps siblings reachable.
- Card titles are cropped in the fan ("Collaborat…", "Knowledg…"). This is acceptable as a teaser but hurts scanning.
- There is no explicit CTA on the expanded card in the frames seen.

## 10. Craft signals
- Rotation angles alternate sign so no two adjacent cards are parallel.
- Each motif uses only that card's palette (for example mint on mint-dark), so the covers never clash.
- The "ft" ligature in the serif title shows deliberate typesetting.
- A 115 px hairline above the title acts as an editorial cue.
- The expanded card's left text edge aligns with its mosaic edge (x≈760 in the key frame).

## 11. Reproduction recipe
```css
:root{--bg:#fefefe;--red:#d33915;--cream:#f2e7d5;--blue:#1a8cc0;--mint:#56ff8f;--black:#1d1c1a}
h1{font:400 95px/1 "EB Garamond",serif;letter-spacing:-.01em;font-feature-settings:"liga","dlig"}
.deck{display:flex;justify-content:center}
.card{width:360px;height:480px;border-radius:20px;margin-left:-140px;padding:24px;
  transform:rotate(var(--r));transition:transform .37s cubic-bezier(.4,0,.2,1),width .37s;
  box-shadow:0 10px 30px rgba(0,0,0,.12)}
.card h3{font:400 40px/.95 "EB Garamond",serif;margin-top:auto}
.card:nth-child(1){--r:-6deg;background:var(--red);color:#fff}
.card:nth-child(2){--r:-3deg;background:var(--cream);color:#3a2f24}
.card:nth-child(3){--r:2deg;background:var(--blue);color:#fff}
.card:nth-child(4){--r:-2deg;background:var(--mint);color:var(--black)}
.card:nth-child(5){--r:4deg;background:var(--black);color:#fff}
.card.is-open{transform:rotate(0) translateY(-40px) scale(1.9);z-index:5}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 9 | A bold five-colour set held together by an elegant serif, and each cover is a small artwork. |
| Originality | 8 | The playing-card fan plus generative covers is a fresh take on course navigation. |
| Usability | 7 | Discoverable and reversible, but cropped titles and blue-card body contrast hurt it. |
| Craft | 9 | Disciplined type, motifs and angles; transitions are consistent at about 0.35 s. |

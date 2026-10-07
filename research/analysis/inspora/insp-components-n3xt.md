---
id: insp-components-n3xt
source: inspora
category: Motion
status: analyzed
title: "Components N3XT"
creator: "@adriankuleszo"
styles: [minimal-swiss, data-dense, maximalist-color, micro-interaction]
patterns: [dot-matrix-unit-chart, big-number-stat-card, theme-cycling-card, stat-with-caption-and-link, staggered-dot-fill]
mode: mixed
palette: ["#f1f1f1", "#fefefe", "#1f1f1f", "#e66d07", "#f0bf95", "#1a1a1a"]
type_families: ["Inter (likely)"]
type_class: [neo-grotesk]
radius_px: [12]
motion: {durations_s: [0.63, 0.67, 0.53], easing: [ease-out, ease-in-out], loop: true}
scores: {aesthetics: 7, originality: 5, usability: 5, craft: 6}
craft_signals: [three-theme-variants-same-layout, unfilled-dots-are-tinted-not-removed, single-accent-orange, numeral-baseline-aligned-with-caption-block, card-shadow-low-and-wide]
anti_patterns: [dot-count-does-not-match-percentage, low-contrast-caption-on-orange, tiny-caption-vs-huge-number]
---
# Components N3XT — @adriankuleszo

## 1. Snapshot
- **Subject:** A 5 s, 60 fps, 956×720 loop of one stat card for "N3XT" (a personal finance brand) cycling through three themes and three statistics:
  - white "24%" (adults with no budget);
  - black "61%";
  - orange "87%".
- Each card pairs a 12×8 dot-matrix unit chart with a big percentage and a small caption plus a "learn more n3xt.com" link.
- **Why it's remarkable:** It shows one component skinned three ways (light, dark and brand-colour) with identical geometry, a compact demonstration of a themable token set.

## 2. Composition & layout
- **Card:** about 280×280 px (roughly 300×300 in the 956 frame), centred on a #f1f1f1 stage, radius about 12 px.
- **Dot grid:** 12 columns × 8 rows, 12 px dots on a 22 px pitch, inset about 16 px. It occupies the top 65% of the card.
- **Bottom band:** the percentage (about 52 px numerals, the left 40%) and, to its right, a two-line caption about 10 px with a link about 10 px below it. The caption block's top aligns with the cap height of the number.
- This is a strong two-zone layout: chart above, number and claim below, with no title.

## 3. Typography
- Inter-like neo-grotesk. The percentage is about 52 px Regular/Medium with tight tracking (about −0.03 em). The "%" is the same size as the digits.
- The caption is about 10 px Regular. The link is about 10 px in orange (white on the orange variant).
- The size ratio of number to caption is about 5:1, so all hierarchy sits in the number.

## 4. Colour
| Hex | Role | Approx share (orange key frame) |
|---|---|---|
| #f1f1f1 | stage | 83% |
| #e66d07 / #e47d2a | brand orange: card fill (variant 3) and filled dots (variants 1 and 2) | 9% |
| #fefefe | white card, white dots | 4% |
| #f0bf95 / #eee4db | unfilled dots on orange and on white (tints) | 1.7% |
| #1f1f1f | dark card | (variant 2) |
| #1a1a1a | number on white | — |

WCAG checks:
- Number #1a1a1a on white is 17.26:1.
- White on dark #1f1f1f is 16.48:1. The dark-variant caption #9a9a9a is 5.86:1.
- White number on orange #e66d07 is 3.2:1 (AA-large only, fine for 52 px).
- The orange "learn more" link on white is 3.18:1 (**fails for 10 px text**).
- The caption on orange (about #f6c9a3) is **2.11:1 (fails)**.

## 5. Depth & material
- Flat cards with a single wide, low shadow, about `0 12px 30px rgba(0,0,0,.08)`, visible as a grey halo below.
- The white card picks up a warm tint (#fdf6f0) at 4.17 s during the cross-fade from orange, a leftover of the colour transition.
- **Unfilled dots:** tinted toward the surface rather than outlined. They are #eee on white, #2a2a2a on black and translucent white (#f0bf95 equivalent) on orange.

## 6. Components & patterns
- **Unit chart (dot matrix):** a "fill N of M" visual for proportions, filled row by row from top-left.
- **Stat card:** big number, caption and an inline text link. There is no button.
- **Theme variants:** surface, filled-dot colour, unfilled-dot tint and text colour all swap together. Layout tokens stay constant.
- **Data honesty issue:** the 96-dot grid shows 38 filled dots for "24%" (3 rows + 2 = 39.6%), 63 for "61%" (65.6%) and 89 for "87%" (92.7%). The visual overstates every figure. A 10×10 grid would have been exact.

## 7. Motion
- **Measured:** 5.0 s loop with motion fraction 0.37 and `seamless_loop_likely: true` (first/last diff 0.09). There are three segments, one per theme change:
  - 0.20–0.83 s (0.63 s, ease-out, peak 0.24): white to black.
  - 1.73–2.40 s (0.67 s, symmetric ease-in-out): black to orange.
  - 3.47–4.00 s (0.53 s, symmetric): orange to white.
- Each card holds for about 1 s between changes.
- **From frames (estimate):** the card cross-fades its surface colour while the number swaps and dots re-fill. At 0.83 s the dark card shows dots already at the new count, so the dot fill is fast, staggered within about 0.3 s. A slight scale-down and up (about 0.97) of the card is visible as it dims.

## 8. Brand system
n/a — not a brand system. N3XT identity cues:
- a single saturated orange (#e66d07);
- black/white/orange as the three allowed surfaces;
- big-number "fact card" voice ("of adults…", "learn more n3xt.com").

## 9. UX
- Unit charts make proportions instantly graspable, but here the grid does not match the numbers, which undermines trust for a finance brand.
- Captions at about 10 px with 2–3:1 contrast on orange are hard to read.
- Treated as social or marketing tiles, the rotating themes work well. As in-app components, the link affordance (plain text) is weak.

## 10. Craft signals
- The three variants share identical geometry: dot pitch, padding and type positions do not move between themes.
- Unfilled dots stay visible as tints, so the full denominator is always shown.
- One accent hue drives all three variants (orange dots → orange surface).
- The caption's top edge aligns with the numeral's cap height.
- The shadow is low-opacity and wide rather than tight, so the card floats without a hard edge.

## 11. Reproduction recipe
```css
:root{--stage:#f1f1f1;--orange:#e66d07;--r:12px;--font:"Inter",system-ui,sans-serif}
.stat{--surface:#fff;--on:#1a1a1a;--dot-on:var(--orange);--dot-off:#eeeeee;--link:var(--orange);
  width:280px;padding:16px;border-radius:var(--r);background:var(--surface);color:var(--on);
  box-shadow:0 12px 30px rgba(0,0,0,.08);transition:background-color .6s cubic-bezier(.2,.8,.2,1),color .6s}
.stat[data-theme=dark]{--surface:#1f1f1f;--on:#fff;--dot-off:#2a2a2a}
.stat[data-theme=brand]{--surface:var(--orange);--on:#fff;--dot-on:#fff;--dot-off:rgba(255,255,255,.25);--link:#fff}
.dots{display:grid;grid-template-columns:repeat(10,12px);gap:10px} /* 10x10 = honest percentages */
.dots i{width:12px;height:12px;border-radius:50%;background:var(--dot-off);transition:background-color .2s calc(var(--i)*6ms)}
.dots i.on{background:var(--dot-on)}
.num{font:500 52px/1 var(--font);letter-spacing:-.03em;font-variant-numeric:tabular-nums}
.cap{font:400 12px/1.3 var(--font);opacity:.85}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 7 | Bold, tidy, three confident theme variants with one accent. |
| Originality | 5 | The dot unit-chart stat card is a common pattern. |
| Usability | 5 | Dots misrepresent the numbers (96-dot grid), and captions are tiny and low-contrast on orange. |
| Craft | 6 | Consistent geometry across themes, but the data-to-visual mapping error is a significant miss. |

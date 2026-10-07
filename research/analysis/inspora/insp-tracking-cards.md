---
id: insp-tracking-cards
source: inspora
category: Product
status: analyzed
title: "Tracking cards"
creator: "@JulienRenvoye"
styles: [dark-premium, data-dense, terminal-mono]
patterns: [hero-metric-card, dot-matrix-progress, coded-metric-rows, colour-pill-values, trend-arrow-labels, concentric-activity-rings, mixed-emphasis-sentence]
mode: dark
palette: ["#f6f6f6", "#161616", "#212121", "#b5501f", "#5c6a3a", "#9a80c8", "#7ab3c4", "#c4dc3a"]
type_families: ["wide neo-grotesk display, PP Neue Montreal / Haffer-like (likely)", "monospace caps, Space Mono / JetBrains Mono-like (likely)"]
type_class: [neo-grotesk, mono]
radius_px: [112, 32, 9999]
motion: null
scores: {aesthetics: 8, originality: 7, usability: 7, craft: 8}
craft_signals: [one-colour-per-metric-across-cards, dot-grid-as-progress-bar, mono-for-labels-grotesk-for-values, grey-vs-white-sentence-emphasis, hairline-row-dividers, trend-arrow-tinted-to-metric]
anti_patterns: [dark-text-on-olive-pill-low-contrast, unfilled-dot-low-contrast]
---
# Tracking cards — @JulienRenvoye

## 1. Snapshot
- **Subject:** Four 2048×1882 slides of dark fitness widget cards (Athletic Score, Athletic Age, a "Today, you're doing Great" breakdown, and a narrative score card) floating on #f6f6f6.
- **Why it's remarkable:** A strict four-colour metric code (rust sleep/recovery, olive strength/cardio, lavender steps/strength, teal VO2/mobility) is applied the same way across icons, pills, rings and arrows. A lime dot-matrix progress bar adds a retro-LED texture. The cards feel like a coherent widget family, not four mockups.

## 2. Composition & layout
- **Card size and frame:** Cards are about 1395×820 px (m0, ≈1.7:1) up to 1395×1290 px (m2), centred, with a 112 px corner radius (about 8% of card width) and roughly 100 px inner padding.
- **Two-column split (m0/m1):**
  - The left 35% holds the hero metric: label in mono caps, then a numeral about 170 px tall (m0 "13", m1 "25").
  - The right 65% holds 3–4 metric rows about 170 px tall, with a 48 px coloured icon disc, a tracked-caps label and a right-aligned value, separated by 2 px #2a2a2a hairlines.
- **Stacked layout (m2/m3):** eyebrow, then a big word or number, then a list or sentence, then the dot-progress bar with a mono caption ("412 / 440 PTS THIS WEEK" left, "+28 TODAY" right in lime).
- **Header (m1):** a "HELLO, JULIEN" greeting and a 160 px greyscale avatar, separated from the body by a full-width hairline.

## 3. Typography
- **Display/value face:** a wide neo-grotesk with flat "1" foot serifs and a tight aperture (close to PP Neue Montreal / Haffer). Hero numerals are about 170 px with tight −0.03 em tracking. "Great" is about 140 px. Row names ("Recovery") are about 58 px and row values ("88", "170 lbs") about 60 px.
- **Mono:** all caps, used for eyebrows ("ATHLETIC SCORE", "TODAY, YOU'RE DOING") at about 36 px with +0.15 em tracking. It is also used for pill values ("87", "22M", "100LB") and the progress caption.
- **Label sans:** row labels ("SLEEP", "STRENGTH") use the grotesk in bold caps with wide +0.12 em tracking, which is distinct from the mono eyebrows.
- **m3 sentence:** an about 58 px semibold sentence that alternates white (statement) and #8a8a8a grey (data or object). This is a typographic way to highlight "+28 pt opportunity" and "Heavy Pull".

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #f6f6f6 | canvas | 47–66% |
| #161616 | card surface | 26–36% |
| #212121 | inset list panel, chips | 13% (m2) |
| #b5501f | rust: sleep / recovery | <2% |
| #5c6a3a | olive: strength / cardio | <2% |
| #9a80c8 | lavender: steps / strength | <2% |
| #7ab3c4 | teal: VO2 max / mobility | <2% |
| #c4dc3a (→ #f6fa29 in m0) | lime: progress dots, positive delta | <1% |

WCAG checks:
- White on #161616 is 18.1:1.
- Grey eyebrow #8a8a8a on #161616 is 5.24:1.
- Grey status words #9a9a9a on #212121 are 5.72:1.
- Lime on #161616 is 11.76:1.

Pill text (#161616 on fill):
| Pill | Ratio | Result |
|---|---|---|
| rust | 3.56:1 | large only |
| olive | **3.08:1** | weakest |
| lavender | 5.43:1 | pass |
| teal | 7.82:1 | pass |

Unfilled dots (#3a3a3a on #161616) are 1.59:1. That is fine as a track, but the remaining progress is barely visible.

## 5. Depth & material
- **Shadow:** a single large soft drop shadow under each card (about 0 40px 80px rgba(0,0,0,.18)), which lifts the dark object off the light canvas.
- **Inside the card:** completely flat, with depth only from the #161616 → #212121 inset panel (radius about 32 px) in m2.
- **Rings:** the activity rings (m2 and m3) are flat concentric strokes in the four metric colours, an Apple-rings homage in the brand palette.

## 6. Components & patterns
- Hero-metric card with a delta chip ("↘ 7Y", "+2 FROM YESTERDAY"): a pill on #222 with a lime glyph.
- Metric row: coloured icon disc, caps label and value. Variant: a value pill plus name plus status word and a coloured trend arrow (↗ / ↘).
- **Dot-matrix progress:**
  - 2 rows × ~46 dots, each about 18 px with a ~8 px gap;
  - filled dots are lime and the rest #2a2a2a;
  - in m0 it becomes an 11×8 grid where 6 lit dots encode the score.
- A narrative insight card mixing data into prose.

## 7. Motion
Stills, so no motion was observed. The natural motion would be dots filling sequentially (about 20 ms stagger) and numerals counting up. This is not shown.

## 8. Brand system
n/a — not a brand system. That said, the metric colour code is a reusable mini-system: each metric owns one muted, earthy hue, and lime is reserved for "progress / positive". The palette avoids neon except for the lime.

## 9. UX
- **Strengths:** One big number per card answers "how am I doing" in under a second. Status words (Great / Low / Elite) translate numbers. Arrows give direction. The m3 sentence tells the user the single best action.
- **Risks:**
  - The olive and rust pills are weak for small text.
  - "Athletic Age 25 ↘ 7Y" is ambiguous: is it 7 years younger, or did it drop 7 years?
  - Colour carries meaning, but the icons and labels back it up, so the cards still work without colour.

## 10. Craft signals
- Each metric keeps its hue across all four cards: rust is always sleep/recovery, lavender is steps/strength, and so on.
- Mono is used for meta (eyebrows, units, captions) and the grotesk for values and names, consistently.
- Trend arrows are tinted with the row's metric colour, not generic green/red.
- Row hairlines (2 px #2a2a2a) start at the icon column, not the card edge, which aligns them to the content grid.
- The progress caption uses two values with "/" in mono and right-aligns the lime delta to the bar's end.
- There is one outer radius (112 px) and one inner panel radius (about 32 px), and pills are full-round.

## 11. Reproduction recipe
```css
:root{--canvas:#f6f6f6;--card:#161616;--panel:#212121;--line:#2a2a2a;--mute:#8a8a8a;
  --rust:#b5501f;--olive:#5c6a3a;--lav:#9a80c8;--teal:#7ab3c4;--lime:#c4dc3a;
  --display:"PP Neue Montreal","Inter",sans-serif;--mono:"Space Mono","JetBrains Mono",monospace}
.card{background:var(--card);color:#fff;border-radius:56px;padding:48px;box-shadow:0 20px 40px rgba(0,0,0,.18)}
.eyebrow{font:400 18px/1 var(--mono);letter-spacing:.15em;text-transform:uppercase;color:var(--mute)}
.hero{font:500 86px/.9 var(--display);letter-spacing:-.03em}
.row{display:grid;grid-template-columns:24px 1fr auto;gap:16px;align-items:center;padding:20px 0;border-top:2px solid var(--line)}
.row .label{font:700 16px var(--display);letter-spacing:.12em;text-transform:uppercase}
.pill{font:700 15px var(--mono);color:var(--card);border-radius:9999px;padding:6px 12px}
.dots{display:grid;grid-template-columns:repeat(46,9px);gap:4px}
.dots i{width:9px;height:9px;border-radius:50%;background:var(--line)}
.dots i.on{background:var(--lime)}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Earthy four-hue code on near-black, a lime LED accent and confident big numerals. |
| Originality | 7 | Dark fitness widgets are common; the dot-matrix progress and prose-insight card stand out. |
| Usability | 7 | Glanceable with good text contrast; weak pill contrast and an ambiguous delta. |
| Craft | 8 | Consistent colour mapping, type roles and radii across four layouts. |

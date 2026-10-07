---
id: insp-session-progress-and-recovery-timeline
source: inspora
category: Product
status: analyzed
title: "Session progress and recovery timeline"
creator: "@ShohanUIX"
styles: [dark-premium, playful-rounded, data-dense]
patterns: [activity-pill-heatmap, range-slider-with-value-bubble, weekly-bar-sparkline, stat-triplet-row, live-activity-pills, dot-matrix-timeline, hold-to-confirm-button, segmented-media-controls]
mode: dark
palette: ["#d2cecb", "#171513", "#282321", "#efe1d9", "#bf9b8d", "#d35f3c", "#a49c98", "#4e3e38"]
type_families: ["Manrope (likely)"]
type_class: [geometric-sans]
radius_px: [56, 44, 9999]
motion: null
scores: {aesthetics: 8, originality: 7, usability: 6, craft: 8}
craft_signals: [warm-black-not-neutral, dashed-outline-for-partial-state, glow-on-value-bubble, single-orange-accent, playhead-split-dot-matrix, card-stack-gap-20px, unit-in-accent-colour]
anti_patterns: [no-activity-cells-near-invisible, white-on-orange-bubble-3to1, unlabelled-heatmap-axes]
---
# Session progress and recovery timeline — @ShohanUIX

## 1. Snapshot
- **Subject:** Four 1091×1200 slides of dark widgets for "Aivo", a mindfulness app:
  1. mindfulness activity heatmap plus heart-rate range;
  2. energy forecast with a 7-day bar chart plus stat triplet;
  3. Live-Activity-style heart-rate pills over the BPM card;
  4. a "Reset Your Mind" session player with a dot-matrix timeline.
- **Why it's remarkable:** It is a **warm** dark system: near-black brown #171513, cream #efe1d9 "goal" pills and a single ember-orange accent on a stone-grey canvas. Data viz is made from friendly rounded primitives: pills, dots and capsules.

## 2. Composition & layout
- Every slide centres a card cluster about 650 px wide on #d2cecb, with about 220 px side margins. Cards are separated by a gap of about 20 px.
- **Slide 1:**
  - **Heatmap card:** 650×310 px, radius about 56 px. Header row (48 px icon disc, title, "Last Month" pill dropdown). Below it, a 10×3 grid of capsules about 52×32 px with about 7 px gaps, then a legend row.
  - **BPM card:** 650×220 px. Value left, "Last reading" right, then a full-width gradient track with an "89" bubble and lowest/peak labels.
- **Slide 2:** "78%" at about 70 px Light on the left; seven capsule bars (16×85 px) on the right labelled S M T W T F S. Below it, a stat strip in three equal columns.
- **Slide 3:** two pill banners (about 480×78 px and 605×78 px) stacked above a wider (785 px) BPM card, a widening pyramid.
- **Slide 4:** a 650×720 px player card with a top spotlight glow, an eyebrow chip, a 44 px title, a two-line description, meta, a dot-matrix timeline (about 34 columns × 5 rows with a ▼ playhead), two 290×72 px buttons and five round control buttons (the centre one is an orange pill).

## 3. Typography
- A geometric/rounded grotesk, most likely **Manrope**: double-storey "a", open "g", wide rounded terminals.
  - Card titles are about 22 px Regular in grey #a49c98.
  - Big values: "76" at about 32 px, "78%" at about 70 px Light, "Reset Your Mind" at about 44 px Light/Regular.
  - Labels are about 17 px.
- **Unit-in-accent:** "BPM" is set in orange beside a white number, and "8:30" in orange with "PM" in grey. Colour separates the number from the unit.

## 4. Colour
| Hex | Role | Share (m0) |
|---|---|---|
| #d2cecb | presentation canvas (warm stone) | 74% |
| #171513 | card surface (warm black) | 19.5% |
| #282321 / #4e3e38 | empty cells, inner discs, chips | 4% |
| #efe1d9 | "goal reached" capsules, cream | 1.3% |
| #bf9b8d | capsule shading, muted copper | 0.9% |
| #d35f3c → ~#f5a06a | accent gradient (track, bubble, bars, CTA) | 1.2% |
| #a49c98 | secondary text | — |

WCAG checks:
- White on #171513: 18.2:1.
- Grey #a49c98 on #171513: 6.75:1.
- Orange text (~#f07a48) on the card: 6.58:1.
- **White "89" on the orange bubble (#f26b3a): 3.03:1**, which passes only as large or bold text.
- Cream capsules on the card: 14.3:1.
- The "No activity" cells (#1d1b19-ish on #171513) are about 1.1:1 and nearly invisible, as is the legend swatch.

## 5. Depth & material
- Cards are flat warm-black with no border.
- The **cream capsules** have a subtle vertical gradient (#f3e6de → #e3cfc4) that makes them look like soft pebbles.
- The "Partial" state is a **dashed 1 px outline** capsule.
- The value bubble has an outer orange glow (about 0 0 24 rgba(242,107,58,.5)).
- The session card has a soft radial spotlight from the top centre (#4e3e38 → transparent).
- The bars in the week chart fade from orange at the top to transparent copper at the bottom.

## 6. Components & patterns
- **Pill heatmap:** three states (filled / dashed / empty) plus a legend.
- **Range track:** min dot, a gradient line, a value bubble at the current position with a dotted vertical marker (daily average) and lowest/peak readouts with arrows.
- **Live-activity pills:** icon disc, label with ellipsis, value, and a circular progress ring.
- **Dot-matrix timeline:** elapsed dots are white or grey, upcoming dots dim, with a ▼ playhead and vertical cursor line.
- **Hold-to-finish button:** a ghost dark pill, for a deliberate end action.
- **Take a break:** a white primary pill.
- **Control dock:** speed, −10, a highlighted orange hint/lightbulb, +10 and settings.

## 7. Motion
Still images; no motion observed. The designs imply:
- the timeline playhead sweeping across the dot matrix;
- a fill progress on "Hold to finish" (a typical 1–1.5 s press);
- progress rings on the Live Activity pills.

## 8. Brand system
n/a — not a brand system. Identity cues for "Aivo":
- warm black and cream palette with an ember accent;
- the rounded-capsule data language;
- the "Aivo recommendation" eyebrow chip with a dot.

## 9. UX
- **Strengths:**
  - The legend explains the heatmap states.
  - The range slider gives context (lowest, peak, average marker).
  - Glanceable stat triplets.
  - Hold-to-finish prevents accidental ending of a session.
- **Risks:**
  - The heatmap has no day/date labels, so you cannot tell which day is which.
  - "No activity" is near-invisible.
  - The orange bubble's white text is only about 3:1.
  - The energy bars carry no values.

## 10. Craft signals
- The surface is warm black #171513 (R > G > B), not neutral #111. It harmonises with the cream and copper.
- The partial state is encoded by a dashed stroke, a non-colour cue that works in greyscale.
- The value bubble carries an outer glow matched to the accent hue.
- A single accent hue is used across all four slides (track, bars, units, CTA).
- Card radius (~56 px) to height ratio stays pill-like; every button and chip is fully round.
- The stack of banner pills widens downward (480 → 605 → 785 px), creating a pyramid.

## 11. Reproduction recipe
```css
:root{--canvas:#d2cecb;--card:#171513;--cell:#282321;--cream:#efe1d9;--copper:#bf9b8d;--muted:#a49c98;
  --accent:#e2643a;--accent-2:#f5a06a;--r-card:56px;--font:"Manrope",system-ui,sans-serif}
.card{background:var(--card);border-radius:var(--r-card);padding:32px;color:#fff;font-family:var(--font)}
.heat{display:grid;grid-template-columns:repeat(10,1fr);gap:7px}
.heat i{height:32px;border-radius:9999px;background:var(--cell)}
.heat i.goal{background:linear-gradient(#f3e6de,#e3cfc4)}
.heat i.partial{background:transparent;border:1px dashed #6b6360}
.track{height:4px;border-radius:9999px;background:linear-gradient(90deg,var(--accent-2),var(--accent),var(--accent-2))}
.bubble{background:var(--accent);border-radius:9999px;padding:10px 22px;font-weight:600;box-shadow:0 0 24px rgba(242,107,58,.5)}
.unit{color:var(--accent)}
.hold{position:relative;overflow:hidden}.hold::after{content:"";position:absolute;inset:0;background:rgba(255,255,255,.12);transform:scaleX(0);transform-origin:left;transition:transform 1.2s linear}
.hold:active::after{transform:scaleX(1)}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | A warm, cohesive dark palette with friendly capsule data viz. |
| Originality | 7 | The pill heatmap and dot-matrix timeline are fresh; the widget card format is common. |
| Usability | 6 | Missing axes and labels, an invisible "no activity" state and a low-contrast bubble. |
| Craft | 8 | Consistent accent, warm-black surface and a non-colour partial-state cue. |

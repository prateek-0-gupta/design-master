---
id: insp-1-30
source: inspora
category: Product
status: analyzed
title: "Date Range Picker"
creator: "@jeetnirnejak"
styles: [micro-interaction, corporate-clean, minimal-swiss]
patterns: [date-range-picker, continuous-range-band-across-rows, nested-card-in-tray, preset-duration-chips, live-night-count-badge, active-field-underline, rolling-digit-text-swap]
mode: light
palette: ["#ffffff", "#f2f2f2", "#2f6ff0", "#d8e7fe", "#1f3fd6", "#1a1a1a", "#6b6b6b", "#c8c8c8"]
type_families: ["Inter (likely)"]
type_class: [neo-grotesk]
radius_px: [40, 28, 9999]
motion: {durations_s: [0.1, 0.13], easing: [ease-out, ease-in-out], loop: true}
scores: {aesthetics: 8, originality: 7, usability: 9, craft: 9}
craft_signals: [range-band-pill-caps-wrap-per-row, endpoint-circle-white-ring, underline-tracks-active-field, badge-copy-changes-with-state, preset-tint-matches-range-colour, past-days-greyed]
anti_patterns: [disabled-dates-low-contrast]
---
# Date Range Picker — @jeetnirnejak

## 1. Snapshot
- **Subject:** A 39 s, 1924×1518 screen capture of a "Trip Dates" range picker covering check-in/out fields, a month grid, preset chips (Weekend / 3 nights / 1 week / 2 weeks) and Clear.
- **Why it's remarkable:** Every state is spoken by the UI itself.
  - The header badge cycles "Add dates" → "Pick check-out" → "7 nights".
  - An underline slides to the field being edited.
  - The selected range is drawn as one continuous pill band that wraps row to row.

## 2. Composition & layout
- **Outer tray:** #f2f2f2, about 842×985 px (x 542→1384, y 268→1253 on the key frame), with a radius of about 40 px.
- **Inner card:** white, inset about 21 px, radius about 28 px. This is the tray-plus-card nesting, where the inner radius is the outer radius minus the inset (40 − 21 ≈ 19, rounded up to 28 for optical softness).
- **Header row:** "Trip Dates" (≈30 px Semibold) on the left and a badge on the right.
- **Fields row:** two columns split by a 1 px vertical rule. Each holds a caps label (≈18 px, +0.1 em tracking) above a value (≈32 px Semibold).
- **Month grid:** 7 columns on a 104 px pitch, rows 80 px apart.
- **Footer:** chips about 58 px tall with 9 px gaps; "Clear" is a text button right-aligned.

## 3. Typography
- Inter-like neo-grotesk. Weights used: Semibold for the title, values and the month name; Regular for the year (#6b6b6b), weekday initials and dates.
- **Sizes (key frame):**
  - title ≈30 px;
  - "September 2026" ≈32 px, with the two-weight split "**September** 2026";
  - date numerals ≈26 px with tabular figures (columns align on 104 px centres);
  - caps labels ≈18 px.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #ffffff | canvas + inner card | 90% |
| #f2f2f2 | tray | 7% |
| #d8e7fe | range band, active chip, badge fill | 2% |
| #2f6ff0 | endpoint circles, active underline | ~1% |
| #1f3fd6 | in-range numerals, badge text | — |
| #1a1a1a / #6b6b6b / #c8c8c8 | text / secondary / past dates | — |

WCAG checks:
- White on endpoint blue (#2f6ff0): 4.51:1, which just passes.
- In-range numerals (#1f3fd6 on #d8e7fe): 6.12:1.
- Secondary #6b6b6b on the tray: 4.76:1.
- Past dates (#c8c8c8) on white: 1.67:1. This is acceptable only because they're disabled, but it is still faint.

Alternate themes appear in later frames: a green range (#22c55e-ish endpoints with a mint band) when a preset is used, and a violet endpoint (≈#5b4cf0) at 36.8 s. Each variant keeps the same three-tint structure.

## 5. Depth & material
- The tray has a soft, wide shadow (≈0 30px 60px rgba(0,0,0,.08)) and a 1 px #e6e6e6 edge.
- Endpoint circles (≈74 px) have a 3 px white ring that separates them from the band, plus a faint shadow, so they look like beads sitting on a rail.
- The active chip uses a 1.5 px blue stroke on #d8e7fe.

## 6. Components & patterns
- **Range band:** a light-blue pill that starts mid-cell under the start circle and ends mid-cell under the end circle. It breaks at row ends with full pill caps (row 2 ends at "13" with a rounded cap; row 3 starts at "14" with a rounded cap).
- **Today marker:** a 4 px dot under "4".
- **Field focus:** a 2.5 px × ≈72 px blue underline beneath the active value, which moves between check-in and check-out.
- **Badge:** neutral grey when idle ("Add dates", "Pick check-out") and tinted blue when a range exists ("N nights").
- **Presets:** these set both dates and highlight the matching chip; the 1 week chip lights up when a range happens to equal 7 nights.

## 7. Motion
Measured: duration 38.97 s at 60 fps, motion_fraction 0.02 (the clip is mostly idle cursor time), five detected segments of 0.10–0.13 s:
- 0.87 s: ease-out;
- 8.60 s: 0.13 s symmetric;
- 14.43 s: symmetric;
- 30.30 s: ease-out;
- 33.03 s: symmetric.

seamless_loop_likely is true. These short bursts are the state transitions: band fill, circle pop and chip tint. At 28.14 s (frame 6) the field values are caught mid-roll, with "Sep 1" sliding up as "Sep 4" enters from below. This is a vertical slot-text swap of about 12 px travel with a fade (estimated at ≤0.15 s). Transitions are snappy (around 100 ms) rather than decorative, which suits a form control.

## 8. Brand system
n/a — this is a product UI component, not a brand system. No logo; the identity is a neutral blue accent with swappable hue themes.

## 9. UX
- **Strengths:**
  - Clear two-step flow, with the prompt in the badge.
  - Night count computed live.
  - Presets for common stays.
  - Reverse selection is handled (clicking before check-in moves the start; frame 6).
  - Past dates are disabled.
  - Clear is always available.
- **Missing:** there is no month navigation visible, which makes cross-month stays unclear. The disabled-state contrast is also very low.

## 10. Craft signals
- Band caps are rounded at each row break, not cut square.
- Endpoint circles carry a white ring (≈3 px) so the band appears to pass beneath them.
- The underline width matches the value text width (≈72 px under "Sep 10").
- The badge and active chip use the same #d8e7fe/#1f3fd6 pair as the band, so there is one accent token set.
- "September" is set Semibold and "2026" Regular grey: a hierarchy made with a single size.

## 11. Reproduction recipe
```css
:root{--tray:#f2f2f2;--card:#fff;--accent:#2f6ff0;--accent-soft:#d8e7fe;--accent-ink:#1f3fd6;
  --ink:#1a1a1a;--ink-2:#6b6b6b;--disabled:#c8c8c8;--r-tray:40px;--r-card:28px;}
.picker{background:var(--tray);border-radius:var(--r-tray);padding:21px;box-shadow:0 30px 60px rgb(0 0 0/.08),0 0 0 1px #e6e6e6}
.card{background:var(--card);border-radius:var(--r-card);padding:36px}
.grid{display:grid;grid-template-columns:repeat(7,1fr);row-gap:6px;font:400 26px/74px Inter;font-variant-numeric:tabular-nums;text-align:center}
.in-range{background:var(--accent-soft);color:var(--accent-ink);font-weight:500}
.range-start{border-radius:999px 0 0 999px}.range-end{border-radius:0 999px 999px 0}
.grid>:nth-child(7n of .in-range){border-radius:0 999px 999px 0}
.endpoint{background:var(--accent);color:#fff;border-radius:50%;box-shadow:0 0 0 3px #fff,0 2px 6px rgb(0 0 0/.15)}
.field[aria-current]::after{content:"";display:block;height:2.5px;width:72px;background:var(--accent);transition:transform .12s ease-out}
.value-swap{animation:roll .12s ease-out}@keyframes roll{from{transform:translateY(12px);opacity:0}}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Calm neutral tray with a precise single-accent system. |
| Originality | 7 | Familiar component, refined through the state badge and wrapping band. |
| Usability | 9 | Every step is labelled and presets shortcut common cases. Only month navigation is missing. |
| Craft | 9 | Ringed endpoints, row-break caps, consistent tokens, about 100 ms transitions. |

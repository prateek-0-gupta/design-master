---
id: insp-1-58
source: inspora
category: Product
status: analyzed
title: "Mini calendar"
creator: "@jeetnirnejak"
styles: [micro-interaction, corporate-clean, minimal-swiss]
patterns: [month-grid-with-event-dots, day-agenda-below-grid, inline-quick-add-event, colour-swatch-category-picker, category-tag-pills, today-outline-vs-selected-fill, event-count-badge, nested-card-in-tray]
mode: light
palette: ["#ffffff", "#f2f2f2", "#111111", "#3b6cf0", "#22c55e", "#f59e0b", "#8b5cf6", "#e5197e"]
type_families: ["Inter (likely)", "JetBrains Mono / Geist Mono (likely)"]
type_class: [neo-grotesk, mono]
radius_px: [40, 28, 16, 9999]
motion: {durations_s: [0.23, 0.33, 0.1, 0.17, 0.27], easing: [ease-out, ease-in-out], loop: true}
scores: {aesthetics: 8, originality: 6, usability: 9, craft: 9}
craft_signals: [today-outline-selected-fill-distinction, max-three-dots-per-day, weekend-headers-greyed, swatch-check-and-label-recolour, count-badge-increments-on-add, mono-times-slashed-zero, tray-grows-with-content]
anti_patterns: [outside-month-dates-very-faint, mono-time-grey-low-contrast]
---
# Mini calendar — @jeetnirnejak

## 1. Snapshot
- **Subject:** A 21.2 s, 1870×1538 capture of a compact month calendar ("May 2026", badge "62" events) with coloured event dots per day.
  - Selecting a day lists its agenda below (time, title, category tag).
  - An inline "Add event" row expands into a quick-add form: title, time, five colour swatches mapped to categories, × and Add.
  - Adding "Dinner 21:00 Personal" bumps the badge to 63.
- **Why it's remarkable:** A full create-event flow lives inside a 400 px-wide widget. Colour does triple duty (dot in the grid, dot in the agenda, tag pill) and is chosen through swatches that relabel the category live.

## 2. Composition & layout
- **Tray:** #f2f2f2, about 802 px wide on the key frame (x 530→1332), radius about 40 px. Its height grows with the agenda: the sheet shows the card extending as rows are added.
- **Inner card:** white, radius about 28 px.
- **Header (on the tray):** "May 2026" (≈30 px Semibold) and a count chip "62". On the right, "Today" (outline pill) and ‹ › 58 px circular buttons.
- **Grid:**
  - weekday header row (Sun/Sat greyed) over a 1 px rule;
  - 6 rows on a 103 px pitch, 7 columns on a 103 px pitch;
  - numerals ≈26 px with 7 px dots below (max three per day);
  - today (4) has a 1.5 px #d4d4d4 outline box (≈82×82, radius ≈14 px), and the selected day (9) has a #e8e8e8 filled box.
- **Agenda:**
  - caps label "SATURDAY, MAY 9 · 1 EVENT" (≈20 px, +0.08 em);
  - rows: dot, mono time, title ≈26 px, and right-aligned tag pill.
- **Quick-add:** a bordered box (radius ≈16 px) with a title input, a vertical divider, a mono time field, and a #f7f7f7 footer holding 50 px swatches, category label, × and a black Add pill.

## 3. Typography
- **Sans** (Inter-like): Semibold for the title, Regular/Medium elsewhere.
- **Mono:** times ("10:00", "9:00" placeholder) with a slashed zero, so times align in a fixed column.
- **Caps label** for the agenda date: small, tracked, grey. Hierarchy here comes from colour and case.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #ffffff | stage, card | 91.5% |
| #f2f2f2 | tray, selected day, chip | 5.5% |
| #111111 | text, Add button | — |
| #3b6cf0 | Meeting | — |
| #22c55e | category (green) | — |
| #f59e0b | Review (orange) | — |
| #8b5cf6 | Focus (violet) | — |
| #e5197e | Personal (pink) | — |

WCAG checks:
- "Personal" tag (#c0157a on #fde7f2): 4.93:1.
- "Meeting" label (#2f5be0 on white): 5.69:1.
- Count chip (#555 on #e6e6e6): 5.97:1.
- Add button: 18.88:1.
- **Mono time grey #9a9a9a: 2.81:1** and **outside-month dates #c8c8c8: 1.67:1**. Both fail AA.

## 5. Depth & material
The same tokens as the creator's other widgets (insp-1-30, -44, -48): the tray shadow is ≈0 30px 60px rgba(0,0,0,.08), and the white card inside is flat. The quick-add box is the only bordered element (1 px #e6e6e6), which marks it as an editable region. Unselected swatches are pastel (≈60% tint); the selected one becomes full saturation with a white check.

## 6. Components & patterns
- **Event dots:** up to three 7 px dots, centred under the numeral, each in its category hue.
- **Day states:**
  - today = outline;
  - selected = grey fill;
  - both can coexist (frame at 3.54 s shows 3 selected and 4 outlined);
  - out-of-month = faint.
- **Agenda rows** with category tag pills: tinted background with the darker hue as text (Meeting, Review, Focus, Personal).
- **Quick-add:** typing "Dinner", tapping the pink swatch (the label switches "Meeting" → "Personal" in pink), entering 21:00, then Add. The agenda gains a row, sorted by time, and the badge increments.

## 7. Motion
Measured: duration 21.24 s at 60 fps, motion_fraction 0.08, seamless_loop_likely true. Eight segments, 0.10–0.33 s:
- 0.80 s: 0.23 s, peak_at 0.07, ease-out;
- 2.30 s: 0.23 s, symmetric;
- 3.77 s: 0.33 s, symmetric;
- 5.30 s: 0.10 s, ease-out;
- 6.90 s: 0.33 s, symmetric;
- 8.80 s: 0.23 s, ease-out;
- 18.03 s: 0.17 s, ease-out;
- 20.60 s: 0.27 s, symmetric.

The 0.33 s symmetric segments coincide with the agenda changing length, where the tray height animates. The 0.1–0.23 s ease-outs are selection and fill changes. Typing and cursor periods (≈9–18 s) are below threshold.

## 8. Brand system
n/a — this is a product UI, not a brand system. It is part of the same personal kit as insp-1-30/44/48: tray #f2f2f2, 40/28 px radii, black primary pill, mono numerics, and a hue-per-category system.

## 9. UX
- **Strengths:**
  - Glanceable density via the dots.
  - Today and selected are clearly distinct.
  - "Today" jump plus month arrows.
  - An event-count summary.
  - Add-in-place with category, time and a cancel option.
  - Agenda sorted by time.
- **Weaknesses:**
  - Days with more than three events have no overflow cue.
  - Colours are not explained except through tags.
  - Low-contrast greys for times and out-of-month days.

## 10. Craft signals
- Today is an *outline*, selection is a *fill*, and they never conflict.
- Weekend headers (Sun, Sat) are lighter than weekday headers.
- The swatch tap recolours both the check and the category label text immediately.
- The header chip increments from 62 to 63 after adding.
- Times use mono with slashed zeros in both the list and the input.
- The tray height animates (about 0.33 s) instead of jumping when the agenda grows.

## 11. Reproduction recipe
```css
:root{--tray:#f2f2f2;--card:#fff;--ink:#111;--muted:#9a9a9a;--meet:#3b6cf0;--green:#22c55e;--review:#f59e0b;--focus:#8b5cf6;--personal:#e5197e;
  --mono:"JetBrains Mono",ui-monospace;}
.cal{background:var(--tray);border-radius:40px;padding:21px;box-shadow:0 30px 60px rgb(0 0 0/.08);transition:height .33s cubic-bezier(.45,0,.55,1)}
.month{display:grid;grid-template-columns:repeat(7,1fr);text-align:center;font:400 26px Inter}
.day{aspect-ratio:1;border-radius:14px;display:grid;place-content:center;gap:6px}
.day[aria-current=date]{box-shadow:inset 0 0 0 1.5px #d4d4d4}
.day[aria-selected=true]{background:#e8e8e8}
.day .dots{display:flex;gap:4px;justify-content:center}.dots i{width:7px;height:7px;border-radius:50%;background:var(--c)}
.day.out{color:#c8c8c8}
.tag{background:color-mix(in srgb,var(--c) 12%,#fff);color:color-mix(in srgb,var(--c) 80%,#000);border-radius:9999px;padding:4px 12px}
.time{font-family:var(--mono);font-feature-settings:"zero";color:var(--muted)}
.swatch{width:50px;height:50px;border-radius:50%;background:color-mix(in srgb,var(--c) 55%,#fff)}
.swatch[aria-checked=true]{background:var(--c)}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Tidy, airy grid with a cheerful dot palette. |
| Originality | 6 | The mini calendar is a common component. The inline quick-add with swatch-as-category is the novelty. |
| Usability | 9 | Complete flow, clear states, keyboard-friendly time field. Contrast nits. |
| Craft | 9 | Consistent tokens across the creator's set, considered day states, animated height. |

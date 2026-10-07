---
id: insp-support-analytics
source: inspora
category: Product
status: analyzed
title: "Support analytics"
creator: "Maxim Kuznetsov"
styles: [dark-premium, data-dense, terminal-mono, hairline-ui]
patterns: [kpi-with-delta-chip, channel-filter-chips, bar-chart-with-avg-line, segmented-ticket-tabs, sla-metrics-table-with-sparklines, recent-tickets-list, toast-confirmation, period-dropdown]
mode: dark
palette: ["#1d1d1d", "#101010", "#4c4e4c", "#ffffff", "#8a8a8a", "#4ade80", "#e5484d", "#f26b3a"]
type_families: ["Inter (likely)", "Geist Mono / JetBrains Mono (likely)"]
type_class: [neo-grotesk, mono]
radius_px: [28, 22, 12, 9999]
motion: {durations_s: [0.43, 0.2], easing: [ease-in, ease-in-out], loop: true}
scores: {aesthetics: 8, originality: 6, usability: 8, craft: 9}
craft_signals: [mono-caps-for-meta-sans-for-labels, avg-line-with-pill-label, sla-status-word-in-red, delta-chip-with-trend-glyph, stacked-section-cards-1px-gap, diagonal-hatch-backdrop, updated-ago-timestamp, accent-only-on-selection]
anti_patterns: [low-contrast-bars-on-surface, tiny-mono-meta]
---
# Support analytics — Maxim Kuznetsov

## 1. Snapshot
- **Subject:** A 39.8 s, 3024×1896 (57 fps) demo of a single dark "Support analytics" widget. It contains:
  - a KPI (1,318 total tickets, +7.8% vs last week);
  - channel chips (All / Email / Live chat / In-app / Social);
  - a 7-day bar chart with an AVG line;
  - All / Open / Resolved tabs;
  - an SLA metrics table with sparklines;
  - an expandable recent-tickets list;
  - a footer showing "Updated 30 sec ago" and "Open ticket queue".
- **Why it's remarkable:** Very high information density in a 740 px card that still reads calmly. It works through a rigorous **sans-for-names / mono-caps-for-meta** split, greyscale bars, and colour reserved for exactly three meanings: orange for selection, green for improvement and red for SLA breach.

## 2. Composition & layout
- **Backdrop:** #1d1d1d with a faint diagonal hatch and vertical guide lines at about 200 px and 1800 px (key px), a blueprint feel.
- **Card:** about 740×1100 key px (≈1120×1660 real), #101010, radius about 28 px. It is built from **stacked sub-cards** (KPI and chart / tabs / metrics / recent / footer), each with radius about 22 px, a 1 px #262626 border and a gap of about 4 px. This produces a segmented "bento column".
- **KPI block:**
  - the number is about 48 px;
  - the delta chip and mono caption share its baseline;
  - chips are about 40 px tall;
  - the chart is about 680×160 px, with 7 bars about 88 px wide and 10 px gaps, labelled with mono day names.
- **Metrics table:** four columns (label+meta / TREND / ACTUAL / VS PREV). Sparklines are about 80×30 px, and values are right-aligned.

## 3. Typography
- **Sans** (Inter-like):
  - the KPI is about 48 px Regular;
  - the title "Support analytics" is about 21 px;
  - metric names are about 19 px;
  - values are about 21 px Medium.
- **Mono caps** (Geist Mono feel) at about 14 px with letter-spacing of about 0.08 em, used for:
  - "TOTAL TICKETS · VS LAST WEEK";
  - column headers;
  - "MISSING · SLA 45M";
  - "UPDATED 30 SEC AGO";
  - day labels and delta numbers.
- Dots (·) separate metadata tokens throughout.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #1d1d1d | backdrop | 95% of frame |
| #101010 | card surface | 4% |
| #4c4e4c | borders, bars, inactive chips | 1% |
| #ffffff | KPI, values | — |
| #8a8a8a | secondary labels | — |
| ~#4ade80 (est.) | positive delta (+7.8%, −6.7% response time) | — |
| ~#e5484d (est.) | "MISSING" SLA status | — |
| ~#f26b3a (est.) | active filter chip "All", hovered bar (WED at 2.21 s) | — |

WCAG checks:
- White on #101010: 19.0:1.
- #8a8a8a: 5.51:1.
- Dimmer mono meta (~#6e6e6e): 3.73:1, which fails at 14 px.
- Green: 10.9:1.
- Red: 4.86:1.
- Orange chip text on its tinted fill: 5.64:1.
- **Bars and borders (#4c4e4c on #1d1d1d): 2.0:1.** This is below the 3:1 non-text minimum, so the bars are faint.

Note that green is used for *decreases* in time metrics (good), so the colour means "better", not "up". That is correct semantics.

## 5. Depth & material
- Flat. Depth comes from #101010 sub-cards on a slightly lighter #1d1d1d backdrop plus 1 px hairlines.
- Bars have a vertical gradient (lighter top → transparent bottom). The hovered bar fills with an orange gradient.
- The AVG line is a 1 px dotted white line with a white pill label ("AVG 188") and an end-dot.

## 6. Components & patterns
- **KPI + delta chip:** a green-tinted pill with a ↗ glyph.
- **Channel chips:** single-select; the active chip is orange-tinted with orange text.
- **Bar chart:** hover tooltip (frame 1: "WED, SEP 9 · 196 tickets" with a per-channel breakdown) and an average reference line.
- **Ticket tabs:** segmented control with count badges ("Open 155", "Resolved 1,163").
- **Metrics table:** label, mono status line, sparkline, value, delta.
- **Recent tickets:** expandable; each row has an avatar initials disc, name, mono status ("RESOLVED / NORMAL / EMAIL" with status in green or red), age and ticket ID.
- **Toasts:** "#HD-3567 marked as resolved" / "reopened" at the bottom.
- **Period dropdown:** This week / Last 30 days / Last 12 weeks. It re-bins the chart (7 bars → 30 bars → 12 bars W1–W12).

## 7. Motion
Measured: 39.83 s, `motion_fraction` only 0.02, `seamless_loop_likely` true. Only 2 segments cross the threshold: 22.83–23.27 s (0.43 s, ease-in, the list expanding and scrolling) and 32.07–32.27 s (0.20 s, a toast).
- Everything else is small-area change (bar heights morphing, numbers counting, chip state). It does not register at 3024 px scale.
- **From frames:**
  - the period change re-renders the bars with a height tween (2,607 → 5,369 → 13,511 KPI count-ups);
  - tab switches swap the metric rows (First reply / Avg ticket age / Awaiting reply for Open);
  - the recent-tickets list expands in place with a +/− toggle.
- The overall motion is restrained, consistent with a data tool.

## 8. Brand system
n/a — not a brand system. Identity cues:
- mono-caps metadata voice;
- orange as the selection colour;
- the hatch-pattern backdrop.

## 9. UX
- **Strengths:**
  - Excellent drill-down within one card: period, then channel, then status, then tickets.
  - The SLA breach is labelled in words ("MISSING"), not colour alone.
  - Deltas carry arrows as well as colour.
  - The freshness timestamp builds trust.
  - The primary exit is "Open ticket queue".
- **Risks:**
  - The bars are very low contrast.
  - The 14 px mono meta is small and dim.
  - Orange for "selected" and red for "breach" are close hues.

## 10. Craft signals
- Every metadata string is mono caps with "·" separators, and every human label is sentence-case sans, with no exceptions across the card.
- The AVG reference line has a pill label anchored at the left and a dot at the right end.
- Sub-cards are separated by a gap of about 4 px with their own 1 px border rather than dividers, which gives a modular stack.
- Count badges in tabs use tabular mono numerals ("1,163").
- "VS PREV" deltas are green for improvements, even when the number is negative.
- The chart binning adapts to the period (days → dates → weeks) with matching mono axis labels.
- Bottom toasts confirm destructive or state changes (resolve / reopen).

## 11. Reproduction recipe
```css
:root{--bg:#1d1d1d;--card:#101010;--line:#262626;--bar:#3a3a3a;--text:#fff;--text-2:#8a8a8a;--text-3:#7a7a7a;
  --good:#4ade80;--bad:#e5484d;--sel:#f26b3a;
  --sans:"Inter",sans-serif;--mono:"Geist Mono","JetBrains Mono",ui-monospace,monospace}
body{background:var(--bg) repeating-linear-gradient(135deg,transparent 0 18px,rgba(255,255,255,.015) 18px 19px)}
.widget{background:var(--card);border-radius:28px;padding:4px;display:grid;gap:4px}
.section{border:1px solid var(--line);border-radius:22px;padding:24px}
.meta{font:500 11px/1.3 var(--mono);letter-spacing:.08em;text-transform:uppercase;color:var(--text-3)}
.delta{font:500 12px var(--mono);color:var(--good);background:color-mix(in oklab,var(--good) 14%,transparent);border-radius:9999px;padding:2px 8px}
.chip[aria-pressed=true]{color:var(--sel);background:color-mix(in oklab,var(--sel) 16%,transparent);border-color:color-mix(in oklab,var(--sel) 40%,transparent)}
.bar{background:linear-gradient(#3a3a3a,transparent);border-radius:8px 8px 0 0;transition:height .4s cubic-bezier(.2,.8,.2,1)}
.bar:hover{background:linear-gradient(var(--sel),color-mix(in oklab,var(--sel) 10%,transparent))}
.avg{border-top:1px dashed rgba(255,255,255,.6)}
.status-missing{color:var(--bad)}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Calm, technical dark card; dense but orderly. |
| Originality | 6 | The Vercel/Linear-style analytics idiom, very well executed rather than new. |
| Usability | 8 | Strong drill-down, worded SLA states and arrows on deltas. Faint bars and tiny meta. |
| Craft | 9 | Rigid type system, semantic colour discipline and adaptive binning. |

---
id: insp-9-5
source: inspora
category: Product
status: analyzed
title: "Opt-in-performance"
creator: "Maxim Kuznetsov"
styles: [dark-premium, data-dense, terminal-mono, hairline-ui]
patterns: [kpi-widget, tick-gauge-with-marker, time-range-dropdown, expand-to-breakdown, overflow-action-menu, toast-confirmation, delta-chip]
mode: dark
palette: ["#1d1d1d", "#101010", "#2d2d2a", "#ffffff", "#8a8a8a", "#4ade80", "#ef4444", "#f97316"]
type_families: ["Inter (likely)", "Geist Mono / JetBrains Mono (likely)"]
type_class: [neo-grotesk, mono]
radius_px: [16, 10, 6, 4]
motion: {durations_s: [0.3, 0.23], easing: [ease-out], loop: true}
scores: {aesthetics: 8, originality: 6, usability: 7, craft: 8}
craft_signals: [discrete-tick-gauge, mono-uppercase-meta, accent-tinted-active-trigger, diagonal-hatch-stage, dashed-section-divider, checkmark-in-accent]
anti_patterns: [dim-mono-labels-below-aa, dropdown-occludes-target-label]
---
# Opt-in-performance — Maxim Kuznetsov

## 1. Snapshot
- **Subject:** A dark KPI card, "Opt-In Rate", recorded at 3022×1896 for 15.0 s. The user expands it into a per-source breakdown, switches the time range (24 h / 7 / 14 / 30 / 90 days) and opens an overflow menu, which ends in a "Data refreshed" toast.
- **Why it's remarkable:** The gauge is ~60 discrete vertical ticks on a red→amber→green ramp with a green triangle marker. It reads like a hardware meter, not a progress bar.

## 2. Composition & layout
- **Stage:** #1d1d1d with a faint 45° diagonal hatch, plus two dashed vertical guides that frame the card column (a Figma-canvas feel).
- **Card:** about 955 px wide native (≈478 CSS px at @2x) with a ~32 px native / 16 CSS radius. Three stacked zones:
  - **Header:** title plus expand/close icons, on #101010.
  - **Body:** a lighter inset surface. The big value sits left, the range trigger right, then the delta line, the gauge with POOR/PERFECT ends, a dashed rule and a benchmark sentence.
  - **Footer:** kebab, chart-type and share icons left; "BASED ON: 24,880 USERS" right.
- **Expanded state (t≈2.5 s):** inserts a "BY SOURCE" list of 4 bars (In-app prompt 68.9%, Onboarding 64.3%, Email capture 57.2%, Web banner 40.8%). The card grows downward only.

## 3. Typography
- **Value:** "60.2%" at ~37 CSS px, regular-weight sans (Inter-like), tight tracking.
- **Title:** ~16 CSS px regular, white.
- **Meta:** everything secondary ("↑ +1.6% VS LAST 14 DAYS", "POOR", "BASED ON…") is uppercase mono at ~11 CSS px with wide tracking. Mono reads as "computed".
- **Menu items:** ~13–14 CSS px sans with leading calendar icons. The group label "TIME RANGE" is in mono caps.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #1d1d1d | stage | 95% |
| #101010 | card header/footer | 3% |
| #2d2d2a | body surface / menu | 1% |
| #ffffff | value, titles | — |
| #8a8a8a (est.) | mono meta | — |
| #4ade80 (est.) | positive delta, marker, ≥ target chip | — |
| #ef4444 → #f97316 (est.) | gauge low end; active trigger tint, checkmark | — |

WCAG checks:
- White on #1d1d1d: 16.86:1.
- Mono grey #8a8a8a on #161616: 5.24:1.
- Green #4ade80 on #161616: 10.38:1.
- Dimmer labels like "POOR" (≈#6b6b6b on #161616): **3.4:1 (fail)**.

## 5. Depth & material
- Elevation comes from surface steps (#101010 frame → #1a1a1a body → #262626 menu) plus a 1 px lighter border on the dropdown.
- The active trigger "14 days ⌃" gets a faint warm/red tint fill and border, linking it to the orange checkmark.
- No glow, and only a subtle shadow under the menu.

## 6. Components & patterns
- **Tick gauge:** ticks past the value are dark grey; a ▼ marker sits above the current tick.
- **Range dropdown:** grouped label, icon + text rows, checkmark on the selected row, hover row lift.
- **Overflow menu:** Set target…, View as donut, Refresh data, Export CSV, Copy link. The selection fires a toast at the bottom centre ("✓ Data refreshed").
- **Target chip:** "ABOVE YOUR TARGET 60%" with a green pill.

## 7. Motion
- **Measured:** only 2 segments above threshold, 1.0–1.3 s (0.30 s) and 2.67–2.9 s (0.23 s), both ease-out with peaks at 0.17 and 0.21 of the segment. motion_fraction is 0.04, and the loop is likely seamless (first/last diff 0.55).
- **Unmeasured changes:** the dropdown opening, value swaps (62.7 → 58.4 → 60.2 → 61.1) and gauge marker moves are small-area changes below the energy threshold. From frames they look like quick fades/slides under ~200 ms.

## 8. Brand system
n/a — not a brand system. Identity cues: mono-caps meta voice, red-to-green meter, hatch-and-guides presentation stage.

## 9. UX
- Progressive disclosure: the expand icon reveals the breakdown without leaving context.
- Every number carries its comparator (vs last N days, vs target, vs industry median).
- **Risks:**
  - The open menu covers "ABOVE YOUR TARGET", the label it affects.
  - The red→green ramp is not colour-blind safe, though the marker position compensates.
  - Dim mono labels fail contrast.

## 10. Craft signals
- The gauge is built from ~60 separate 2 px ticks, not a gradient bar; values past the marker drop to neutral.
- The selected range shows as a check in the same warm accent as the trigger's tint.
- The footer meta updates with the range (12,430 → 1,840 → 24,880 → 159,400 users).
- A dashed divider separates the benchmark sentence from the gauge (a hierarchy step without weight).
- Mono uppercase is reserved for metadata; sans is used for names and values.

## 11. Reproduction recipe
```css
:root{--stage:#1d1d1d;--frame:#101010;--body:#1a1a1a;--menu:#262626;--ink:#fff;--ink-2:#8a8a8a;
  --pos:#4ade80;--accent:#f97316;--mono:"Geist Mono","JetBrains Mono",monospace}
body{background:var(--stage) repeating-linear-gradient(135deg,transparent 0 14px,rgba(255,255,255,.025) 14px 15px)}
.card{width:480px;border-radius:16px;background:var(--frame);overflow:hidden}
.meta{font:500 11px/1.2 var(--mono);letter-spacing:.08em;text-transform:uppercase;color:var(--ink-2)}
.gauge{display:flex;gap:4px;height:20px}
.gauge i{width:2px;border-radius:1px;background:#3a3a3a}
.gauge i.on{background:var(--c)} /* --c interpolated red→amber→green per index */
.trigger[aria-expanded=true]{background:rgba(249,115,22,.1);border:1px solid rgba(249,115,22,.25)}
.menu{background:var(--menu);border:1px solid #333;border-radius:10px;animation:pop .2s cubic-bezier(.2,.8,.2,1)}
@keyframes pop{from{opacity:0;transform:translateY(-4px) scale(.98)}}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Disciplined dark card; tick gauge is a strong focal device. |
| Originality | 6 | Familiar dev-tool KPI idiom, well executed. |
| Usability | 7 | Comparators everywhere and good disclosure; menu occludes target, dim labels. |
| Craft | 8 | Consistent mono/sans split, live footer data, tidy menu states. |

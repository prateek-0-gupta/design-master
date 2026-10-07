---
id: insp-8-9
source: inspora
category: Product
status: analyzed
title: "A calendar of your life"
creator: "@jeetnirnejak"
styles: [corporate-clean, data-dense, micro-interaction]
patterns: [life-in-weeks-grid, scrub-slider-drives-grid, phase-colour-legend, stat-triplet, mono-counter-pill, segmented-track-slider]
mode: light
palette: ["#ffffff", "#f2f2f2", "#1a1a1a", "#1aa0e6", "#2f6fe8", "#7c3aed", "#f59e0b", "#f6e27a"]
type_families: ["Inter / SF Pro (likely)", "SF Mono / JetBrains Mono (likely) for numerals"]
type_class: [neo-grotesk, mono]
radius_px: [48, 28, 9999, 3]
motion: {durations_s: [0.23, 0.27, 0.17, 0.43], easing: [ease-in-out, ease-out], loop: false}
scores: {aesthetics: 8, originality: 7, usability: 7, craft: 8}
craft_signals: [grid-maps-exactly-90x52, slider-track-mirrors-phase-colours, mono-tabular-counters, nested-card-in-shell, leading-cell-halo-marker, live-week-pill]
anti_patterns: [legend-grey-mono-below-aa, colour-only-phase-encoding]
---
# A calendar of your life — @jeetnirnejak

## 1. Snapshot
- **Subject:** A "Life in Weeks" widget (1920×1514, 14.8 s capture). A 4,680-cell grid fills with phase colours as a slider sets your age from 0 to 90.
- **Why it's remarkable:** One control drives three synchronised readouts (grid, stat row, header pill). The slider track uses the same phase colours as the grid, so the slider doubles as the legend.

## 2. Composition & layout
- **Shell:** a #f2f2f2 card about 1040×1055 px with a ~48 px radius on a white stage. A soft shadow falls below it.
- **Inner panel:** white, inset ~22 px, with a ~28 px radius. It holds the grid and the legend.
- **Grid:** about 950×547 px, i.e. 90 columns (years) × 52 rows (weeks). The cell pitch is ~10.5 px with ~3 px gaps, and the cells are tiny rounded squares.
- **Below the panel:**
  - a three-column stat row (left, centre, right aligned);
  - the slider with "0" and "90" end labels;
  - a centred caption ("Each cell is one week · drag to set your age").
- **Header:** title left at ~28 px, with a mono pill "Week 214 of 4,680" on the right.

## 3. Typography
- **Title:** semibold neo-grotesk at ~28 px (SF Pro / Inter-like).
- **Stat labels:** ~18 px uppercase with about +0.08 em tracking, grey.
- **Stat values:** ~32 px bold monospace ("4,467", "4.6%"). Tabular digits keep the columns from jittering while scrubbing.
- **Legend:** sans name plus mono range ("Career 18–65"), both ~20 px.
- **Caption:** ~22 px regular grey.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #ffffff | stage + inner panel | 82% |
| #f2f2f2 | outer shell, empty cells (lighter tint) | 16% |
| #1a1a1a | title, values | <1% |
| #1aa0e6 (est.) | Childhood cyan | grows with age |
| #2f6fe8 (est.) | School blue | — |
| #7c3aed (est.) | Career violet | — |
| #f59e0b (est.) | Retirement amber | — |
| #f6e27a (est.) | slider track, retirement zone (pale) | — |

Phase hues were read from the frames; palette.json only resolves #ffffff/#f2f2f2/#a1c2d8 because the cells are tiny.

WCAG checks:
- Title #1a1a1a on #f2f2f2: 15.55:1.
- Stat label #6b6b6b on #f2f2f2: 4.76:1 (pass).
- Mono legend ranges ≈#8a8a8a on #fff: **3.45:1 (fails AA normal)**.

## 5. Depth & material
- Flat, apart from one large diffuse shadow under the shell (about 0 30px 60px rgba(0,0,0,.08)).
- The slider thumb is a white pill with its own small shadow, showing the age number in the current phase colour (blue "4", violet "41", amber "75").

## 6. Components & patterns
- **Leading-edge marker:** the current week is a larger halo dot, ~16 px with a white ring. Behind it, the newest column fades in light-to-dark.
- **Segmented slider track:** filled part saturated, unfilled part as pale tints of the phase colours. The thumb is a pill that contains the value.
- **Stat triplet:** lived / remaining / elapsed %. All three update together.

## 7. Motion
- **Measured:** 8 segments with a median of 0.2 s and a motion_fraction of 0.12; the clip does not loop seamlessly.
  - The bursts are 0.17–0.43 s (e.g. 6.93–7.37 s, 0.43 s symmetric, when the user drags back from 75 to 4).
  - Mostly ease-in-out, with one ease-out at 1.13 s (0.27 s).
- **Visual behaviour:** the grid fills column by column behind the leading dot rather than snapping. Frame 10.71 s shows the new column partly drawn, which suggests a ~150–250 ms stagger per column.
- **Counters:** they change instantly with tabular digits, so values never reflow.

## 8. Brand system
n/a — not a brand system. Identity cues: the author's consistent "#f2f2f2 shell + white inner panel + mono numbers" component style, shared with insp-deploy-pipeline and insp-sandbox-boot-sequence.

## 9. UX
- Direct manipulation with immediate, three-way feedback; the caption teaches the gesture.
- The 52-row mapping makes "one column = one year" legible.
- **Risks:**
  - Phases are encoded by hue only (cyan vs blue is close for deuteranopes).
  - The legend's mono grey fails AA.
  - There is no keyboard affordance shown.

## 10. Craft signals
- 90×52 = 4,680 exactly matches the "of 4,680" pill, so the data model and grid geometry agree.
- The slider's unfilled track is pre-tinted with each phase's future colour.
- The thumb label recolours to the current phase.
- Nested radii: shell ~48 px, inner panel ~28 px (≈48 − 22 px inset).
- Stat values are tabular mono, so there is no width jitter during scrubbing.

## 11. Reproduction recipe
```css
:root{--stage:#fff;--shell:#f2f2f2;--ink:#1a1a1a;--ink-2:#6b6b6b;
  --child:#1aa0e6;--school:#2f6fe8;--career:#7c3aed;--retire:#f59e0b;
  --font:"Inter",system-ui;--mono:"JetBrains Mono",ui-monospace}
.shell{background:var(--shell);border-radius:24px;padding:20px 11px 16px;box-shadow:0 30px 60px rgba(0,0,0,.08)}
.panel{background:#fff;border-radius:14px;padding:12px}
.grid{display:grid;grid-template-columns:repeat(90,1fr);grid-template-rows:repeat(52,1fr);gap:1.5px;grid-auto-flow:column}
.cell{aspect-ratio:1;border-radius:1.5px;background:#eee;transition:background .2s ease-in-out}
.cell[data-phase=child]{background:var(--child)}
.stat b{font:700 16px/1 var(--mono);font-variant-numeric:tabular-nums}
.stat small{font:500 9px/1 var(--font);letter-spacing:.08em;text-transform:uppercase;color:var(--ink-2)}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Calm neutral shell lets four phase hues carry the story. |
| Originality | 7 | "Life in weeks" is known; the slider-as-legend is a fresh twist. |
| Usability | 7 | Immediate feedback; hue-only phases and grey legend hurt accessibility. |
| Craft | 8 | Geometry matches data exactly; nested radii and tabular digits are precise. |

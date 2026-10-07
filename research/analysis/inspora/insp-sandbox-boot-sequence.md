---
id: insp-sandbox-boot-sequence
source: inspora
category: Product
status: analyzed
title: "Sandbox Boot Sequence"
creator: "@jeetnirnejak"
styles: [corporate-clean, terminal-mono, micro-interaction]
patterns: [checklist-progress-card, cold-vs-warm-comparison, cached-step-pill, inline-terminal-output, status-pill-with-dot, elapsed-counter, rerun-cta]
mode: light
palette: ["#ffffff", "#f2f2f2", "#d0dfd9", "#879993", "#1a1a1a", "#16a34a", "#9a9a9a", "#eef7f1"]
type_families: ["Inter / SF Pro (likely)", "SF Mono / Menlo (likely)"]
type_class: [neo-grotesk, mono]
radius_px: [28, 20, 12, 9999]
motion: {durations_s: [0.27, 0.13, 0.33], easing: [ease-out, ease-in-out, ease-in], loop: false}
scores: {aesthetics: 8, originality: 7, usability: 8, craft: 9}
craft_signals: [cached-pill-explains-speedup, per-step-ms-in-mono, terminal-reveal-on-execute-step, button-label-names-next-mode, single-hue-status-system, active-row-mint-tint]
anti_patterns: [green-on-grey-status-below-aa, ms-grey-below-aa]
---
# Sandbox Boot Sequence — @jeetnirnejak

## 1. Snapshot
- **Subject:** A 12.9 s, 1924×1518 capture of a "Sandbox node26" card that steps through six boot stages, a cold run then a warm run:
  1. Allocate microVM
  2. Restore snapshot
  3. Mount ephemeral FS
  4. Boot runtime · Node 26
  5. Execute main.js
  6. Reclaim sandbox
- **Why it's remarkable:** The warm run labels the steps that got faster with a "cached" pill and shows the new timing (Restore 820 → 90 ms, Boot 1100 → 220 ms). The performance story is told in-line, not in a chart.

## 2. Composition & layout
- **Shell:** #f2f2f2, about 840 px wide native (≈420 CSS), with a ~56/28 radius and a large soft floor shadow.
- **Header:** "Sandbox" semibold, a mono "node26" pill, and status at right ("Booting ●", "Running ●", "Done ●", "Warm · Running ●"). A 4 px progress bar sits underneath.
- **List panel:** white (radius ~40/20) with six rows at ~71 px native pitch (status icon, label, right-aligned mono ms). The active row has a mint pill background.
- **Terminal block:** appears from the Execute step onward. It is a nested #f8f8f8 box with a 1.5 px #e5e5e5 border and radius ~24/12, holding four mono lines ("$ node main.js", "fetching dataset … 1.2 MB", "computed 1,284 rows", "✓ done in 312ms").
- **Footer:** an elapsed counter ("4.96s"), with "Provisioning…/Executing…" on the right. When done this becomes green "Exited 0 · 2300ms" plus a black "↻ Re-run (warm)" pill.

## 3. Typography
- **Sans:** ~28 px native for the title and ~26 px for row labels. Pending rows are lighter.
- **Mono:** ms values (~22 px, grey), terminal lines, the exit line and the node pill.
- "cached" is a tiny ~16 px lowercase label in a mint pill.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #ffffff | stage, list panel | 89% |
| #f2f2f2 | shell | 8% |
| #d0dfd9 / #eef7f1 (est.) | active row tint, cached pill | 1.5% |
| #879993 | muted green-grey (pending icons) | 1.4% |
| #16a34a (est.) | done checks, status, bar, exit line | — |
| #1a1a1a | text, Re-run button | — |
| #9a9a9a (est.) | ms values | — |

WCAG checks:
- White on the #1a1a1a button: 17.4:1.
- Green "Done" #16a34a on #f2f2f2: **2.94:1 (fail)**.
- Green on white: 3.3:1.
- ms grey #9a9a9a on white: **2.81:1**.

A single hue (green) carries all status. Unlike the sibling insp-deploy-pipeline, there is no orange "running" colour: running is a green spinner on a mint row.

## 5. Depth & material
Flat panels on a tinted shell, with one soft outer shadow. The terminal box is the only element with a visible border, which marks it as "output", distinct from UI.

## 6. Components & patterns
- **Row states:**
  - pending: hollow ring, grey text;
  - running: spinner, mint row, "···";
  - done: filled green check plus ms.
- **Cached pill:** sits between the label and the timing, so the speed-up reads left to right.
- **CTA:** after the cold run it reads "Re-run (warm)"; after the warm run it reads "Re-run".

## 7. Motion
- **Measured:** 10 segments with a median of 0.13 s; motion_fraction is 0.16, and the clip does not loop seamlessly.
  - **Row advances:** pulses at 3.6, 3.97 and 4.37 s (each 0.13 s, symmetric) and at 9.9, 10.3 and 10.67 s. That is a ~0.37–0.4 s cadence, matching the step ticks.
  - **Larger changes:** 3.23 s (0.27 s ease-out), when the terminal block expands; 7.97 s (0.33 s ease-out, peak 0.05), the warm re-run reset.
- The warm run's faster rows produce visibly shorter gaps between pulses.

## 8. Brand system
n/a — not a brand system. Identity cues: same author kit as insp-deploy-pipeline and insp-8-9 (shell + white panel + mono timings + status-dot pill).

## 9. UX
- Teaches caching value without explanation: the same list, with smaller numbers and a reason tag.
- The terminal appears only when there is output, which keeps the card compact during boot.
- **Risks:**
  - Green-only status text is below AA.
  - Totals for cold vs warm are never shown side by side; you must remember 2300 ms.

## 10. Craft signals
- The "cached" pill appears only on steps whose timing changed (Restore, Boot), not on all of them.
- Mono ms values right-align on a common edge (x≈1326 in the key frame).
- The header bar, row states and footer counter stay in sync.
- The Re-run label names the mode it will run in ("warm").
- The terminal success line reuses the same green as the row checks.

## 11. Reproduction recipe
```css
:root{--shell:#f2f2f2;--ink:#1a1a1a;--muted:#8a8a8a;--ok:#137a3a;--ok-bg:#eef7f1;--mono:"SF Mono",Menlo,monospace}
.row{display:grid;grid-template-columns:20px 1fr auto auto;gap:12px;align-items:center;padding:10px 12px;border-radius:9999px}
.row.run{background:var(--ok-bg)}
.row .ms{font:400 11px var(--mono);color:var(--muted);font-variant-numeric:tabular-nums}
.cached{font:500 9px/1 var(--font);padding:3px 6px;border-radius:9999px;background:#dcf3e5;color:var(--ok)}
.term{border:1.5px solid #e5e5e5;border-radius:12px;background:#f8f8f8;font:12px/1.6 var(--mono);
  animation:grow .27s cubic-bezier(.2,.8,.2,1)}
@keyframes grow{from{opacity:0;transform:translateY(-4px)}}
/* --ok darkened to #137a3a for AA on #f2f2f2 */
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Calm single-hue system; terminal block adds texture. |
| Originality | 7 | Cold/warm comparison with "cached" tags is a smart narrative device. |
| Usability | 8 | Self-explanatory states and timings; green contrast is low. |
| Craft | 9 | Tight sync, right-aligned mono, purposeful conditional elements. |

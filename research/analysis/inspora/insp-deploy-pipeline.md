---
id: insp-deploy-pipeline
source: inspora
category: Product
status: analyzed
title: "Deploy Pipeline"
creator: "@jeetnirnejak"
styles: [corporate-clean, terminal-mono, micro-interaction]
patterns: [stage-stepper, progress-bar-under-header, step-list-with-timings, streaming-log-panel, status-pill-with-dot, elapsed-of-total-counter, terminal-state-cta]
mode: light
palette: ["#ffffff", "#f2f2f2", "#dfdedb", "#1a1a1a", "#c2620e", "#16a34a", "#9a9a9a", "#fdf3ea"]
type_families: ["Inter / SF Pro (likely)", "SF Mono / Menlo (likely)"]
type_class: [neo-grotesk, mono]
radius_px: [28, 20, 16, 9999]
motion: {durations_s: [0.23], easing: [ease-in-out], loop: false}
scores: {aesthetics: 8, originality: 6, usability: 8, craft: 9}
craft_signals: [three-redundant-progress-views, connector-fills-toward-next-node, active-row-warm-tint, timings-in-mono, check-badge-on-stage-icon, final-state-swaps-to-black-cta, pending-shown-as-dashes]
anti_patterns: [accent-orange-below-aa, pending-grey-below-aa]
---
# Deploy Pipeline — @jeetnirnejak

## 1. Snapshot
- **Subject:** A 9.2 s, 1924×1518 capture of a deploy widget. It runs Build → Test → Preview → Production over a simulated 8.0 s, streaming logs per step, and ends at "Deployed" with a Re-deploy button.
- **Why it's remarkable:** Progress is shown three ways at once (header bar, node stepper, step list) and they never disagree. The log panel rewrites itself per stage, so the card stays a fixed size.

## 2. Composition & layout
- **Shell:** #f2f2f2, about 1120 px wide native (~560 CSS at @2x), with a ~56 native / 28 CSS radius and a soft floor shadow. Inside it, three white panels with ~40/20 radii and ~20 px gaps:
  - **Stepper:** four 72 px squircle nodes joined by 110 px connectors, each with a label and mono duration below.
  - **Step list:** four rows of ~70 px; the active row has a warm tint (#fdf3ea-ish) and a full-width radius.
  - **Log:** a mono terminal block.
- **Header:** "Deploy Pipeline", a mono branch pill "main · a3f7c1d", and right-aligned status "Running · Test ●". A 4 px progress bar sits under it.
- **Footer:** mono "4.3s / 8.0s" left, and a pill button right whose label tracks the stage ("Test…").

## 3. Typography
- **Sans:** title ~28 px semibold; row labels ~24 px regular. Pending rows are lighter grey.
- **Mono:** durations ("2.0s"), branch/hash, log lines (~20 px) and the elapsed counter. Pending durations render as "--s".
- The log uses "→" prefixes, with a green "✓ 142 passed" success line.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #ffffff | stage, panels | 83% |
| #f2f2f2 | shell, idle nodes | 15% |
| #dfdedb | connectors, pills, button idle | 1.5% |
| #1a1a1a | primary text, final CTA | — |
| #c2620e (est.) | running accent: bar, active node, status | — |
| #16a34a (est.) | done: check badges, "Deployed" bar | — |
| #fdf3ea (est.) | active row tint | — |

WCAG checks:
- Title #1a1a1a on #f2f2f2: 15.55:1.
- Orange status #c2620e on #f2f2f2: **3.72:1 (AA large only)**.
- Green #16a34a on #fff: **3.3:1**.
- Pending labels ≈#9a9a9a on #fff: **2.81:1 (fail)**.

## 5. Depth & material
- Flat panels on a tinted shell. The only shadow is a large soft one under the shell.
- The active node has an orange 1.5 px ring and a cream fill. Done nodes turn mint with a small green check badge overlapping the bottom-right corner.

## 6. Components & patterns
- **Stage stepper:** the connector from the finished node to the active node fills orange starting from a small dot. After the step completes it turns green.
- **Status pill:** "Running · {stage}" in orange with a dot, then "Deployed ●" in green.
- **Terminal-state CTA:** the disabled grey pill ("Build…") becomes a black "↻ Re-deploy" when done, and the footer left becomes green "Deployed · 8.0s".

## 7. Motion
- **Measured:** one segment above threshold, at 0.37–0.6 s (0.23 s, symmetric ease-in-out, peak 0.36). motion_fraction is 0.04, and the clip does not loop seamlessly (first/last diff 5.73).
- **Below the energy threshold:** most motion is small-area (spinners, log lines appearing, bar growth). From frames:
  - the header bar grows linearly with simulated time (≈12% at 1.1 s, ≈54% at 4.3 s);
  - log lines append one at a time, roughly every 0.3–0.4 s;
  - each step completes with an instant row-state swap rather than a long transition.

## 8. Brand system
n/a — not a brand system. Identity cues: shares its shell, mono timing and status-pill grammar with insp-sandbox-boot-sequence and insp-8-9 by the same author, a coherent personal component kit.

## 9. UX
- Excellent glanceability: the stage, elapsed time, ETA and logs are all visible without interaction.
- The step list duplicates the stepper. That is redundant, but it gives precise per-step timings (Build 2.0s, Test 2.5s, Preview 1.5s, Production 1.9s).
- **Risks:**
  - Orange and green are close to AA failure.
  - No failure state is shown.
  - The log panel's fixed height would truncate long output.

## 10. Craft signals
- Three progress views (bar, nodes, rows) stay in sync at every frame sampled.
- Durations change from "--s" to live orange to final green, so the colour encodes state, not category.
- Check badges overlap the node corner by ~25%.
- The button label mirrors the current stage ("Preview…"), then becomes a black primary when actionable.
- The radius ladder is 28 (shell) → 20 (panel) → 16 (node) → pill.

## 11. Reproduction recipe
```css
:root{--shell:#f2f2f2;--panel:#fff;--ink:#1a1a1a;--muted:#9a9a9a;--run:#c2620e;--run-bg:#fdf3ea;--ok:#16a34a;
  --mono:"SF Mono",Menlo,monospace}
.shell{background:var(--shell);border-radius:28px;padding:16px 12px;box-shadow:0 24px 48px rgba(0,0,0,.08)}
.bar{height:2px;background:#e5e5e5;border-radius:2px}.bar>i{display:block;height:100%;background:var(--run);transition:width .3s linear}
.panel{background:var(--panel);border-radius:20px;padding:16px}
.node{width:36px;height:36px;border-radius:10px;background:var(--shell)}
.node.run{background:var(--run-bg);box-shadow:inset 0 0 0 1.5px var(--run)}
.node.ok{background:#e7f7ee;position:relative}.node.ok::after{content:"✓";position:absolute;right:-4px;bottom:-4px;
  width:14px;height:14px;border-radius:50%;background:var(--ok);color:#fff;font-size:9px;display:grid;place-items:center}
.row.run{background:var(--run-bg);border-radius:9999px}
.t{font:400 11px var(--mono);color:var(--muted)}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Quiet neutral system with two meaningful accents. |
| Originality | 6 | CI pipeline widgets are common; the polish is the novelty. |
| Usability | 8 | Highly legible state and timings; borderline accent contrast. |
| Craft | 9 | Synchronized multi-view progress, radius ladder, stateful CTA. |

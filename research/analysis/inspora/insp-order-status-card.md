---
id: insp-order-status-card
source: inspora
category: Motion
status: analyzed
title: "order-status card"
creator: "@zahragr8r"
styles: [dark-premium, micro-interaction, minimal-swiss]
patterns: [segmented-progress-tracker, travelling-step-icon-thumb, text-crossfade-status, live-activity-card, card-enter-scale-down, eta-line]
mode: mixed
palette: ["#f0f0f0", "#000000", "#1f1f1f", "#2d2d2d", "#c6f432", "#7a7c73", "#ffffff"]
type_families: ["Helvetica Neue / SF Pro Text (likely)"]
type_class: [neo-grotesk]
radius_px: [96, 72, 32, 9999]
motion: {durations_s: [0.6, 5.08], easing: [ease-out], loop: true}
scores: {aesthetics: 8, originality: 6, usability: 8, craft: 8}
craft_signals: [thumb-icon-changes-per-stage, filled-segments-solid-active-segment-gradient, one-accent-colour, nested-radii-concentric, crossfade-not-slide-for-copy, eta-in-white-subtitle-in-grey]
anti_patterns: [unfilled-track-near-invisible]
---
# order-status card — @zahragr8r

## 1. Snapshot
- **Subject:** A 5.08 s, 2880×2160 loop of a black food-delivery status card (Live Activity / widget style) stepping through Preparing → Packing & Quality Check → Out for Delivery → Delivered, with a lime thumb travelling along a four-segment track.
- **Why it's remarkable:** The thumb is both progress indicator and stage pictogram — its icon swaps (cooking pot → box → bike → bell/delivered) as it crosses each segment, so the track tells the story without labels.

## 2. Composition & layout
- Light-grey stage #f0f0f0 with faint paper texture; the card is centred at ≈ 1460×740 px (original), so ≈ 50% of frame width.
- **Card anatomy:** 32 px-equivalent padding; a 235 px app-icon tile (paw mark) top-left; a text stack at x+265 (title, subtitle, ETA line); below, a full-width inner track container ≈ 1265×210 px.
- **Track:** four equal segments ≈ 275 px long with ≈ 25 px gaps, 12 px-thick capsules; thumb ≈ 115 px lime circle.
- Radii: outer card ≈ 96 px, inner track container ≈ 72 px (container inset ≈ 96 px → approximately concentric), icon tile ≈ 32 px, capsules full-round.

## 3. Typography
- Neo-grotesk (Helvetica Neue / SF Pro): title ≈ 60 px regular white; subtitle ≈ 44 px regular grey #7a7c73; ETA line ≈ 44 px white ("Est. 5 min", "Arriving soon", "Rate Restaurant").
- Ratio title:body ≈ 1.36. Only regular weight is used; hierarchy comes from colour (white vs grey) and order.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #f0f0f0 | stage | 82% |
| #000000 | card | 10% |
| #1f1f1f | inner track container, icon tile | 4.5% |
| #2d2d2d | unfilled segments | 0.6% |
| #c6f432 (est.) | lime accent: filled segments, thumb | ~1% |
| #7a7c73 | subtitle grey | 0.4% |
| #ffffff | title, ETA, paw | — |

WCAG checks:
- Title white on #000: 21:1.
- Subtitle #7a7c73 on #000: **4.96:1 (passes AA)**.
- Lime #c6f432 on track #1f1f1f: 12.86:1; dark icon inside the lime thumb: 12.86:1.
- Unfilled segment #2d2d2d on #1f1f1f: **1.2:1** — the remaining stages are barely visible.

## 5. Depth & material
- Flat card with no shadow on the light stage; elevation inside the card comes from #000 → #1f1f1f tint steps.
- The thumb has a subtle inner shading (lighter top-left) and a thin darker lime rim, making it read as a pressable bead.
- The active segment's fill is a gradient (transparent → lime) trailing the thumb, giving a comet-tail; completed segments are solid lime.

## 6. Components & patterns
- Four-stage segmented progress tracker with an icon thumb.
- Status copy block: title / description / ETA or action ("Rate Restaurant" at the end turns the ETA slot into a CTA).
- App-icon tile identifies the source (Live Activity convention).
- Text crossfade between stages (1.98 s frame shows "Preparing…" and "Packing…" overlaid mid-dissolve).

## 7. Motion
Measured (m0_motion.json): 5.08 s, 60 fps, motion_fraction 0.11, `seamless_loop_likely: true` (first/last diff 0.33). Only one segment crosses threshold: **0.00–0.60 s (0.60 s), peak_at 0.25 → ease-out** — the card's entrance: at 0.28 s it is ≈ 30% larger and content-less, then it scales down to rest by 0.85 s.
- The stage advances are small-area, so they stay below threshold; from frames: the thumb appears at 1.41 s, then reaches segment 2 at ≈ 1.98–2.54 s, segment 3 at ≈ 3.11–3.67 s and segment 4 at ≈ 4.24–4.80 s → ≈ 1.1 s per stage (estimate), each with a ≈ 0.3 s text crossfade.
- Stage pacing is uniform, which suits a demo; real ETAs would differ.

## 8. Brand system
n/a — not a brand system. Identity cues: a paw-print app mark (pet/food brand) and a single acid-lime accent on black.

## 9. UX
- Very clear: four stages, current position, human-readable status and ETA; matches iOS Live Activity / Dynamic Island mental models.
- Icon-per-stage helps glanceability and colour-blind users (the lime is not the only signal).
- **Risks:** unfilled segments at 1.2:1 hide how many steps remain; there is no stage labelling on the track itself; the final action "Rate Restaurant" is styled as plain text, not a button.

## 10. Craft signals
- The thumb icon changes at each segment boundary (pot → box → bike → delivered).
- Completed segments are solid lime, the active one a lime gradient, the pending ones #2d2d2d — three distinct states.
- Inner container radius (≈ 72 px) = outer radius (≈ 96 px) − inset, giving concentric curves.
- Copy changes crossfade in place rather than sliding, so the layout never jumps.
- One accent colour across the whole component.

## 11. Reproduction recipe
```css
:root{--stage:#f0f0f0;--card:#000;--well:#1f1f1f;--pending:#2d2d2d;--accent:#c6f432;--muted:#7a7c73}
.status{background:var(--card);border-radius:32px;padding:22px;color:#fff;font:400 17px/1.25 "SF Pro Text","Helvetica Neue",sans-serif;
  animation:enter .6s cubic-bezier(.16,1,.3,1) both}
@keyframes enter{from{transform:scale(1.3);opacity:.0}to{transform:none;opacity:1}}
.status .sub{color:var(--muted);font-size:13px}
.track{background:var(--well);border-radius:24px;padding:20px 12px;display:grid;grid-template-columns:repeat(4,1fr);gap:8px;position:relative}
.seg{height:4px;border-radius:9999px;background:var(--pending)}
.seg.done{background:var(--accent)} .seg.active{background:linear-gradient(90deg,transparent,var(--accent))}
.thumb{position:absolute;width:36px;height:36px;border-radius:50%;background:var(--accent);
  box-shadow:inset 0 -2px 0 rgba(0,0,0,.15);transition:left 1s cubic-bezier(.65,0,.35,1)}
.copy{transition:opacity .3s}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Crisp black card, one lime accent, tidy proportions. |
| Originality | 6 | Delivery trackers are familiar; the morphing-icon thumb is the twist. |
| Usability | 8 | Glanceable, multi-signal state; pending steps are too faint. |
| Craft | 8 | Concentric radii, three-state segments, in-place crossfades. |

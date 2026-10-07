---
id: insp-wos-island-animations
source: inspora
category: Motion
status: analyzed
title: "WOS Island Animations"
creator: "Murat"
styles: [micro-interaction, high-contrast-bw, organic-blob, playful-rounded]
patterns: [dynamic-island-live-activity, gooey-blob-morph, status-glow-halo, stacked-app-badges, progress-ring-to-check, alert-to-action-to-done-flow]
mode: mixed
palette: ["#dbdbdb", "#e7e7e7", "#0e0e0c", "#f5221b", "#dee84d", "#7b7ff5", "#17b44a", "#8a8a88"]
type_families: ["SF Pro Text (likely)"]
type_class: [neo-grotesk]
radius_px: [9999, 120]
motion: {durations_s: [1.1, 0.67, 0.63, 0.6, 0.8, 0.57], easing: [ease-out], loop: true}
scores: {aesthetics: 8, originality: 8, usability: 7, craft: 8}
craft_signals: [metaball-neck-on-split, coloured-halo-per-state, avatar-plus-app-badge-overlap, island-sits-in-device-top-curve, consistent-ease-out-all-transitions, seamless-loop-first-last-diff-0.1]
anti_patterns: [white-on-red-below-aa, red-for-both-brand-and-alert]
---
# WOS Island Animations — Murat

## 1. Snapshot
- **Subject:** A 14 s, 1440×1440 seamless loop of Dynamic Island "live actions" for an agent product (WOS). A black pill morphs through alert ("Ramp deal at risk!"), action ("Follow up · Draft reply ready"), working (indigo spinner plus pen) and success ("All done!" with Gmail, Calendar and Slack badges), then collapses back to a blank island.
- **Why it's remarkable:** It shows a full agent task lifecycle inside the island. Each state is coded by a coloured halo around the pill (red, indigo, green), and the shape transitions use gooey metaball necking.

## 2. Composition & layout
- **Stage:** The camera alternates between a close-up (island ~1036 px wide, 1440 frame) and a mid-shot inside a phone top edge (white device silhouette with a ~120 px corner radius).
- **Island (key frame):** 1036×225 px (x 202→1238, y 607→832), fully round ends.
  - **Left cluster:** a 134 px red WOS avatar (three white dots, playful face) with a 64 px lime app badge overlapping at the bottom right.
  - **Centre:** the label "Follow up" (~38 px white) plus the secondary "Draft reply ready" (~32 px grey) on one baseline.
  - **Right:** a 122 px red action button.
- **Padding:** ~50 px inner padding on the left. The avatar is vertically centred while the text baseline sits low, aligned with the badge.

## 3. Typography
- SF Pro Text (iOS), on-device about 15–17 pt.
- **Pairing:** a primary label in medium white and a secondary in regular #8a8a88 on the same line. This is the iOS Live Activity "title + detail" idiom.
- Short, imperative or status copy: "Ramp deal at risk!", "Follow up", "All done!".

## 4. Colour
| Hex | Role | Approx share |
|---|---|---|
| #dbdbdb / #e7e7e7 | backdrop and device body | 89% |
| #0e0e0c | island fill | 9% |
| ≈#f5221b | WOS brand avatar, alert halo, primary action | 1.5% |
| #dee84d | lime app badge | <1% |
| ≈#7b7ff5 | "working" spinner and halo (indigo) | — |
| ≈#17b44a | success check and halo | — |
| #8a8a88 | secondary label | — |

WCAG checks:
- White on island: 19.32:1.
- Grey detail #8a8a88 on island: 5.59:1.
- Red glyph #f5221b on island: 4.72:1.
- Indigo on island: 5.7:1.
- **White icon on red button: 4.1:1** (passes for large and graphical UI only).

## 5. Depth & material
- **Island:** flat matte black.
- **Depth through glow:** a 20–30 px soft outer halo in the state colour (red at 2.33–3.89 s, indigo at 8.56 s, green ring at 10.11 s), plus a thin inner coloured stroke (~3 px red in the alert state).
- **Device:** a soft grey-white gradient with a faint inner highlight, nearly skeuomorphic but low contrast.
- **Motion blur:** visible on fast morphs (10.11 s).

## 6. Components & patterns
- **Gooey split and merge:** At 0.78 s the island bulges with a neck, a metaball separation as the avatar bud emerges from the pill. At 13.22 s the pill re-forms with a slight left lobe.
- **State sequence:**
  1. compact alert: avatar plus "!" disc, red halo;
  2. expanded alert with text;
  3. action: avatar, Ramp-style lime badge, "Follow up", red button;
  4. working: indigo arc spinner plus pen disc, indigo halo;
  5. success: green ring check, then expanded "All done!" with three app badges stacked with ~−8 px overlap;
  6. collapse.
- **Badge stacking:** the app logos (Gmail, Calendar, Slack) show which tools the agent touched.

## 7. Motion
Measured profile: 14.0 s at 60 fps, `motion_fraction` 0.37, `seamless_loop_likely` **true** (first-to-last difference 0.10).
- **All nine segments are ease-out**, with peaks at 0.06–0.23:
  - 0.50 s for 1.10 s (the blob emergence; long because of the gooey settle);
  - 2.00 s for 0.67 s (expand);
  - 4.00 s for 0.63 s (alert to text);
  - 7.00 s for 0.60 s (action to working);
  - 10.00 s for 0.63 s (success);
  - 12.00 s for 0.80 s and 12.97 s for 0.57 s (expand "All done", then collapse).
- **Rhythm:** state changes land roughly every 2–3 s (2.0, 4.0, 7.0, 9.5/10.0, 12.0), a clean demo cadence.
- **Feel:** consistently front-loaded energy, so every morph snaps into place and then settles, which reads as springy without a visible overshoot.

## 8. Brand system
n/a — not a brand system. Identity cues:
- the WOS red avatar with its three-dot "face";
- black and red as the core colours;
- per-state halo colours (red for risk, indigo for working, green for done).

## 9. UX
- **Strengths:**
  - Glanceable lifecycle (risk, action, progress, done).
  - Halo colour plus icon shape (!, spinner, ✓) double-code each state.
  - App badges explain scope.
- **Risks:**
  - Red is used for the brand avatar, the alert and the primary action alike. The alert state cannot outrank the brand mark.
  - Dynamic Island text space is tiny, so "Draft reply ready" would truncate on smaller devices.
  - White-on-red is 4.1:1.

## 10. Craft signals
- A metaball neck appears during the split and merge (0.78 s, 13.22 s).
- The halo colour changes per state, with a matching thin inner stroke.
- A 64 px app badge overlaps the 134 px avatar at the bottom right (~48% scale).
- The app badges stack with consistent negative overlap.
- One easing family: all transitions are ease-out, 0.57–1.1 s (measured).
- The loop is truly seamless (first-to-last frame difference 0.10).

## 11. Reproduction recipe
```css
:root{--island:#0e0e0c;--brand:#f5221b;--lime:#dee84d;--work:#7b7ff5;--ok:#17b44a;--muted:#8a8a88}
.island{background:var(--island);border-radius:9999px;height:56px;padding:0 12px;display:flex;align-items:center;gap:10px;
  transition:width .63s cubic-bezier(.16,1,.3,1),height .63s cubic-bezier(.16,1,.3,1),box-shadow .4s ease-out}
.island[data-state=alert]{box-shadow:0 0 0 1.5px var(--brand) inset,0 0 0 8px color-mix(in srgb,var(--brand) 18%,transparent)}
.island[data-state=working]{box-shadow:0 0 0 8px color-mix(in srgb,var(--work) 20%,transparent)}
.island[data-state=done]{box-shadow:0 0 0 8px color-mix(in srgb,var(--ok) 20%,transparent)}
.avatar{width:34px;aspect-ratio:1;border-radius:50%;background:var(--brand);position:relative}
.avatar .badge{position:absolute;right:-6px;bottom:-6px;width:16px;aspect-ratio:1;border-radius:50%;background:var(--lime)}
.badges>*+*{margin-left:-6px}
/* gooey split: blur + contrast on the parent */
.goo{filter:url(#goo)}
```
```html
<svg width="0" height="0"><filter id="goo"><feGaussianBlur stdDeviation="8"/>
<feColorMatrix values="1 0 0 0 0 0 1 0 0 0 0 0 1 0 0 0 0 0 20 -9"/></filter></svg>
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Bold black, red and lime with soft state halos. Clean and punchy. |
| Originality | 8 | Agent task lifecycle in the island with metaball morphs and colour-coded halos is a fresh extension. |
| Usability | 7 | States are double-coded. Red is overloaded and text space is tight. |
| Craft | 8 | Consistent easing, a seamless loop and careful badge overlaps. |

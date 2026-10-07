---
id: insp-5-8
source: inspora
category: Motion
status: analyzed
title: "Animated thinking orbs"
creator: "@Jakubantalik"
styles: [dark-premium, micro-interaction, generative-particle, hairline-ui]
patterns: [agent-status-pill, dot-matrix-orb-icons, shimmer-text-sweep, component-showcase-cluster, state-specific-loader-shapes, scene-swap-transition]
mode: dark
palette: ["#070707", "#121212", "#252525", "#353535", "#585858", "#8c8c8c", "#ffffff"]
type_families: ["Inter (likely)"]
type_class: [neo-grotesk]
radius_px: [9999, 28]
motion: {durations_s: [0.73, 0.67], easing: [ease-out], loop: true}
scores: {aesthetics: 9, originality: 8, usability: 8, craft: 9}
craft_signals: [distinct-orb-per-verb, dots-only-iconography, pill-surface-1-step-lift, four-dot-ellipsis, label-shimmer-white-on-grey, scale-variants-sm-lg, inner-top-highlight-on-tile]
anti_patterns: [subtitle-2-8-to-1, four-period-ellipsis-nonstandard]
---
# Animated thinking orbs — @Jakubantalik

## 1. Snapshot
- **Subject:** A 10.3 s, 1700×1280, 30 fps showcase of a "Thinking orbs" component: dark pill status chips, each pairing an animated dot-matrix glyph with a verb ("Thinking....", "Searching", "Solving....", "Working....", "Listening....", "Agent shaping...", "Agent listening..."). They are shown in two scattered compositions that swap.
- **Why it's remarkable:** Each agent state gets its **own glyph behaviour** built from the same dot vocabulary: a spinning band (thinking), latitude-dotted sphere (searching), scattered cluster (working), dotted triangle/square/circle morph (shaping). It is a coherent icon system for AI states, not one generic spinner.

## 2. Composition & layout
- **Header:** centred at the top.
  - An app-icon tile of about 124×124 px (radius ≈28 px) containing a dotted ring, at y≈85–210.
  - The title "Thinking orbs" at about 40 px.
  - The subtitle "Animated thinking orbs component" at about 40 px in grey.
- **Pills:** an asymmetric cluster of pills below, in two sizes:
  - large: about 840×230 px, with a ~140 px orb and ~56 px label;
  - small: about 475×118 px, with a ~55 px glyph and ~38 px label.
- **Depth of field:** pills run off the right edge, and blurred duplicates sit behind the sharp ones, suggesting a shallow-focus product shot.
- **Spacing:** gaps between pills are about 80–110 px. The orb sits about 45 px from the pill's left edge, and the label starts about 55 px after the orb.

## 3. Typography
- An Inter-like neo-grotesk.
- The title is Medium, white, about 40 px. The subtitle is Regular, #585858, at the same size, so hierarchy comes by value only.
- Pill labels are Regular. Large ones are ~56 px, small ones ~38 px, a 1.47× ratio that matches the 1.95× pill-height ratio in proportion.
- Labels end in "...." (four dots) on the verbs and "..." on the "Agent …" labels. That is inconsistent and non-standard.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #070707 | canvas | 93% |
| #121212 | pill surface | 3.7% |
| #252525 / #353535 | pill 1 px border, tile edge | 2% |
| #585858 | subtitle, resting label tone | 0.5% |
| #8c8c8c | label base | — |
| #ffffff | title, orb dots, shimmer peak | <1% |

It is fully achromatic.

WCAG checks:
- The title is 20.14:1.
- Label base #8c8c8c on #121212 is 5.57:1, and the shimmer peak #e6e6e6 is 15.01:1.
- The subtitle (#585858 on #070707) is **2.83:1** and fails.
- The pill border vs canvas is 1.31:1, too faint alone, but the pill fill does the separating.

## 5. Depth & material
- **Pills:** fill #121212 on #070707, a single elevation step. A 1 px #252525 border has a slightly brighter top edge, which reads as a soft inner highlight.
- **Header tile:** has a stronger inner top highlight and a soft outer shadow, like an app-icon-style "glass" tile.
- **Orbs:** 3D point spheres. Dot size and brightness fall off toward the limb (edges dimmer, ~1.5 px dots vs ~3 px at centre), giving volume with no shading.
- **Blur:** background duplicates are blurred about 8–12 px for depth of field.

## 6. Components & patterns
- **Agent status pill:** glyph plus verb label in two sizes (sm/lg), the main deliverable.
- **Glyph set:**
  - thinking: a rotating ring/band of vertical dashes;
  - searching/listening: a dotted sphere rotating;
  - working: a sparse scattering that rearranges;
  - solving: a jittering dot ring;
  - shaping: a dotted outline morphing triangle → square → circle (frames 5.15, 6.29 and 7.44 s).
- **Label shimmer:** a white highlight sweeps across the grey text ("Agent searching" at 2.86 s shows a brighter "Agent").

## 7. Motion
Measured values (`m0_motion.json`):
- Only two large segments: 4.07–4.80 s (0.73 s, peak 0.16) and 9.00–9.67 s (0.67 s, peak 0.17). Both are ease-out with a fast start. These are the **scene swaps** between the two pill arrangements (the frames show composition A at 0.57–4.01 s, B at 5.15–8.58 s, A again at 9.73 s).
- Motion fraction is 0.13, and `seamless_loop_likely` is true (first/last diff 0.28).
- The scene period is about 4.95 s, so A → B → A loops at 10.3 s.

The orbs' internal motion is small-area and continuous, below the global threshold. Estimates from the frames:
- the shape morph cycles about every 1.15 s per shape (triangle 5.15 s, square 6.29 s, circle 7.44 s, triangle 8.58 s);
- sphere rotation looks slow, about 3–4 s per revolution.

## 8. Brand system
n/a — this is not a brand system. It is a UI component showcase with an app-icon tile as the component's mark.

## 9. UX
- **Strengths:** Different glyphs per state let users distinguish "searching" from "thinking" at a glance, even peripherally, which is a real usability gain for agent UIs. Label contrast passes AA even at rest.
- **Risks:**
  - The subtitle fails AA.
  - The four-dot ellipsis looks like a typo.
  - Live regions should announce state changes, and reduced motion should freeze the glyphs to their static shapes.

## 10. Craft signals
- Each verb maps to a unique dot-behaviour glyph (6+ variants), all from one dot primitive.
- Sphere dots shrink and dim toward the limb, a correct spherical projection.
- The small and large pill variants keep the same internal proportions (orb ≈60% of pill height).
- Elevation uses one surface step (#070707 → #121212) plus a 1 px border, with no drop shadows on the pills.
- The scene swap uses the same ease-out (peak ~0.16) both ways, 0.67–0.73 s.
- The shimmer on labels uses white over a #8c8c8c base, so it stays readable at all phases.

## 11. Reproduction recipe
```css
:root{--bg:#070707;--pill:#121212;--edge:#252525;--ink:#8c8c8c;--ink-hi:#e6e6e6;--sub:#7a7a7a;/* lift from #585858 for AA */
  --font:Inter,system-ui,sans-serif}
.pill{display:inline-flex;align-items:center;gap:16px;padding:12px 24px 12px 14px;border-radius:9999px;
  background:var(--pill);box-shadow:inset 0 0 0 1px var(--edge),inset 0 1px 0 rgba(255,255,255,.04)}
.pill--lg{padding:22px 48px 22px 20px;gap:28px}.pill--lg .label{font-size:28px}
.label{font:400 19px/1 var(--font);color:transparent;
  background:linear-gradient(90deg,var(--ink) 0 35%,var(--ink-hi) 50%,var(--ink) 65% 100%) 0 0/250% 100%;
  -webkit-background-clip:text;background-clip:text;animation:shine 2.2s linear infinite}
@keyframes shine{from{background-position:100% 0}to{background-position:-50% 0}}
.orb{width:28px;height:28px}.pill--lg .orb{width:70px;height:70px}
@media (prefers-reduced-motion:reduce){.label{animation:none;color:var(--ink)}}
```
Orb (canvas): generate N points on a Fibonacci sphere. Each frame, rotate around Y by `t*2π/3.5s`, project, and set `r = lerp(0.6,1.6,(z+1)/2)` and alpha `lerp(.25,1,(z+1)/2)`. For "shaping", lerp the points between triangle, square and circle outlines every 1.15 s with `cubic-bezier(.16,1,.3,1)`.

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 9 | Refined monochrome; the dot-sphere glyphs are elegant at both sizes. |
| Originality | 8 | A state-specific orb vocabulary for agent UIs is a smart step beyond one spinner. |
| Usability | 8 | Distinguishable states and passing label contrast; a weak subtitle and odd ellipsis. |
| Craft | 9 | Consistent proportions, correct sphere projection, a tight surface/border system. |

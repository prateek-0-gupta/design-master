---
id: insp-icons-for-iphone-duo
source: inspora
category: Motion
status: analyzed
title: "icons for iPhone Duo"
creator: "@helvetiica"
styles: [monochrome, minimal-swiss, micro-interaction, x-concept-icon]
patterns: [status-bar-icons, icon-morph-sequence, battery-as-ring, signal-bars-to-dots, radial-status-cluster, stroke-continuity-morph]
mode: light
palette: ["#e7e7e9", "#000000"]
type_families: []
type_class: []
radius_px: [9999, 24]
motion: {durations_s: [0.23, 1.17, 0.1], easing: [ease-in-out, linear], loop: false}
scores: {aesthetics: 8, originality: 9, usability: 5, craft: 8}
craft_signals: [single-stroke-weight-throughout, round-caps-everywhere, battery-shrinks-before-bending, dots-follow-arc-path, wifi-glyph-as-fixed-anchor, two-tone-only]
anti_patterns: [ring-battery-level-unreadable, signal-dots-lose-strength-encoding]
---
# icons for iPhone Duo — @helvetiica

## 1. Snapshot
- **Subject:** A 3.27 s, 1280×720 concept animation. The standard iOS status cluster (4 signal bars, Wi-Fi fan, horizontal battery) morphs into a compact radial badge. The battery becomes an open ring around the Wi-Fi glyph, and the signal bars become four dots that close the ring's gap at the bottom.
- **Why it's remarkable:** It reinvents three status icons as one circular composite, presumably for a round or cutout-shaped display on a speculative "iPhone Duo". It does this purely by continuous stroke morphing in one weight and one colour.

## 2. Composition & layout
- **Start (t=0.18 s):** a horizontal row centred at y≈375.
  - signal bars, about 140 px wide, 4 bars of rising height (≈18 → 48 px), each ≈14 px wide;
  - Wi-Fi fan, about 130 px wide;
  - battery, about 190×95 px with a 10 px nub.
  - Gaps are about 30 px.
- **End (t=3.09 s):** a single radial badge centred at x≈640, y≈355.
  - a ring about 236 px in diameter with a stroke of about 12 px;
  - the ring is open about 70° at the bottom, where four ≈14 px dots sit on the ring's path;
  - the Wi-Fi fan, about 100 px wide, sits centred inside.
- The composition moves from wide (≈560 px row) to compact (≈240 px circle) and re-centres.

## 3. Typography
None. The piece is pure iconography. The visual "type" is a single stroke family: about 12 px strokes with round caps, and dots equal to the stroke width.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #e7e7e9 | background (iOS light grey) | 98.9% |
| #000000 | all glyphs | ~1% |

WCAG check: black on #e7e7e9 is 17.0:1. The concept is strictly monochrome, so state cannot rely on colour (no red low-battery or green charging is shown).

## 5. Depth & material
None, deliberately. These are flat vector glyphs with no shading, matching iOS status-bar conventions. The intermediate states keep the same flat fill and stroke, so the morph never introduces a new material.

## 6. Components & patterns
- **Battery:**
  1. a filled pill (0.18–0.54 s);
  2. contracts to a rounded square, about 110×95 px with radius ≈24 (0.91 s);
  3. collapses to a vertical bar (1.27 s);
  4. tips over into an arc (1.63 s);
  5. sweeps into an almost-closed ring (2.0–2.72 s).
- **Signal:** the 4 bars shrink to 4 equal dots (1.27 s). They then travel along a curve (2.0–2.36 s) to settle into the ring's gap.
- **Wi-Fi:** stays nearly constant and acts as the anchor that everything orbits. It shrinks slightly (about 130 → 100 px).

## 7. Motion
Measured: 30 fps, 3.27 s, `motion_fraction` **0.45**, the highest in this batch. There are three segments:
- 0.83–1.07 s (0.23 s, symmetric ease-in-out): the battery collapses to a bar and the bars become dots;
- 1.43–2.60 s (1.17 s, continuous/linear): the long sweep where the bar bends into the arc and the dots follow its path;
- 3.13–3.23 s (0.10 s, ease-in): a final settle.

The 0.18–0.83 s span before the first segment holds the battery's width contraction, which is below threshold. Not looped (`first_last_diff` 10.54). The sequence reads as staged: shrink → collapse → sweep → settle, each element moving in turn rather than all at once.

## 8. Brand system
n/a — not a brand system. It is a speculative extension of Apple's SF Symbols status set, keeping its stroke and cap conventions.

## 9. UX
- **Strengths:**
  - Compact and symmetric, good for a circular camera cutout or a small secondary display.
  - Keeps the familiar Wi-Fi glyph as the recognisable anchor.
- **Risks:**
  - The final state does not show how the battery *level* is encoded (an arc length would work, but the ring here is about 290° regardless).
  - Four equal dots lose the bars' rising-height strength metaphor.
  - Charging and low states are not shown.

## 10. Craft signals
- One stroke weight (about 12 px) and round caps across every state, including the dots (diameter = stroke).
- The battery morphs through intermediate primitives (pill → square → bar → arc), so there is no cross-fade cheat.
- The dots travel along the arc's own circular path into the gap.
- The Wi-Fi glyph stays the fixed anchor, minimising cognitive change.
- Strict two-tone palette (#000 on #e7e7e9).
- The final composition is radially symmetric about the vertical axis.

## 11. Reproduction recipe
```html
<svg viewBox="0 0 120 120" width="120"><g fill="none" stroke="#000" stroke-width="6" stroke-linecap="round">
  <!-- battery ring: animate stroke-dasharray from a short bar to a 290deg arc -->
  <circle id="batt" cx="60" cy="60" r="54" pathLength="360" stroke-dasharray="0 360" transform="rotate(125 60 60)"/>
</g>
<g fill="#000"><circle class="dot" r="3.5"/><circle class="dot" r="3.5"/><circle class="dot" r="3.5"/><circle class="dot" r="3.5"/></g>
<!-- wifi glyph centered --></svg>
```
```css
#batt{animation:ring 1.17s linear .83s forwards}
@keyframes ring{0%{stroke-dasharray:24 336}100%{stroke-dasharray:290 70}}
.dot{offset-path:path("M24 96 A54 54 0 0 0 96 96");animation:ride 1.17s linear .83s forwards}
.dot:nth-child(n){offset-distance:calc(var(--i)*8%)}
@keyframes ride{from{offset-distance:0%}to{offset-distance:calc(35% + var(--i)*10%)}}
```
Use `stroke-linecap:round` everywhere. The 0.23 s pre-collapse can be done with a `d` path morph (Flubber or GSAP MorphSVG).

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Pure, consistent monochrome glyphs and an elegant circular end state. |
| Originality | 9 | Fusing three status icons into a single radial badge is a genuinely new idea. |
| Usability | 5 | Battery level and signal strength encodings are unclear in the final state. |
| Craft | 8 | Continuous stroke morphs, a constant weight and path-following dots. |

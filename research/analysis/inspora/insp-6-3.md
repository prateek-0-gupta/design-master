---
id: insp-6-3
source: inspora
category: Motion
status: analyzed
title: "Shader Mixer"
creator: "@raul_dronca"
styles: [minimal-swiss, gradient-mesh, technical-wireframe]
patterns: [two-axis-shader-mixer, dashed-connector-to-active-option, word-preset-selectors, squircle-shader-tile, hue-matched-glow-shadow]
mode: light
palette: ["#f4f3f1", "#3a6cab", "#234a86", "#5788c4", "#dddee3", "#3a3a3a", "#a8a29e"]
type_families: ["Inter / Geist-style neo-grotesk (likely)"]
type_class: [neo-grotesk]
radius_px: [72]
motion: {durations_s: [0.27, 0.2, 0.17, 0.1], easing: [ease-in-out, ease-out], loop: false}
scores: {aesthetics: 8, originality: 8, usability: 7, craft: 8}
craft_signals: [dashed-bezier-connectors-to-selection, left-motion-right-colour-axes, active-word-darkens-not-underlines, squircle-tile-coloured-glow, connector-snaps-straight-when-aligned]
anti_patterns: [inactive-options-fail-contrast]
---
# Shader Mixer — @raul_dronca

## 1. Snapshot
- **Subject:** A 19.9 s, 2876×2160 (60 fps) control built around a squircle shader tile. Three words on the left (Still, Wave, Storm) set the *motion*, and three on the right (Mist, Ocean, Abyss) set the *colour depth*. Dashed curves connect the chosen word on each side to the tile.
- **Why it's remarkable:** It turns shader parameters into a two-axis word mixer. Nine presets are reachable with six words, and the connectors draw the "patch cable" relationship.

## 2. Composition & layout
- **Tile:** About 640×640 px, centred, with a squircle radius of about 72.
- **Word columns:** About 410 px either side of the tile edges, right-aligned on the left (x≈735) and left-aligned on the right (x≈2150).
- **Rows:** Three rows at y≈777, 1083 and 1388, aligned to the tile's top quarter, centre and bottom quarter.
- **Connectors:** Dashed curves about 2 px thick with roughly 14 px dashes. They run from the active word to the tile edge at the same row, curving as an S-bezier when the rows differ ("Storm" connects to the tile at y≈1210) and straight when aligned ("Ocean" to the centre).

## 3. Typography
- Neo-grotesk (Inter or Geist-like) at about 52 px Medium for all six words.
- **Active word:** #3a3a3a.
- **Inactive words:** About #a8a29e, a warm grey.
- No other text. The words are the UI.

## 4. Colour
| Hex | Role |
|---|---|
| #f4f3f1 | canvas (warm off-white) |
| #3a6cab / #5788c4 | shader mid / highlight (Ocean) |
| #234a86 | shader shadow |
| #dddee3 | Mist-state tile, connector grey |
| #3a3a3a | active label |
| #a8a29e | inactive label |

Other states: Mist is a pale periwinkle (#c3d0e6 range), and Abyss is near-navy (#16213f range, seen at 12.13 s).

WCAG:
- Active #3a3a3a on #f4f3f1 is 10.26:1.
- Inactive #a8a29e on #f4f3f1 is **2.27:1** (fails, though they are interactive).
- If text ever sat on the Ocean tile, white on #3a6cab would be 5.37:1.

## 5. Depth & material
- **Tile:** A soft-focus fluid gradient with no grain, plus a broad coloured glow beneath it (about 0 40px 120px of the tile's hue at about 20%). The glow changes from pale lavender in Mist to blue in Ocean.
- **Surroundings:** Everything else is flat. No borders, no cards.

## 6. Components & patterns
- **Two radio groups:** motion (left) and colour (right), each with a single active item.
- **Patch-cable connectors:** They visualise which inputs feed the output.
- **The tile:** It is a live preview. Its shape distortions are Still (soft), Wave (a band sweeping across) and Storm (a sharp swirl).

## 7. Motion
- **Measured:** 4 discrete segments across 19.85 s. motion_fraction is only 0.03, so the shader animates continuously below the threshold while user changes are short.
  - 8.53 s: 0.27 s, peak 0.56. The colour switch (Mist to Ocean), symmetric.
  - 10.93 s: 0.20 s, peak 0.08 (ease-out). The connector redraw.
  - 12.33 s: 0.17 s, symmetric.
  - 12.60 s: 0.10 s, peak 0.17. Ocean to Abyss, then back.
- **Frames (estimate):**
  - The shader's internal motion is slow (a several-second drift).
  - Connectors re-route instantly, about 0.2 s.
  - The colour change crossfades in about 0.27 s.
- `seamless_loop_likely: false`.

## 8. Brand system
n/a — not a brand system. It shares the creator's language with "Shader Slider" (insp-5-7): a warm off-white canvas, shader tiles with hue-matched glows and evocative single-word naming.

## 9. UX
- Mapping is explicit (connectors), and there are few choices with a clear output.
- **Gaps:**
  - Inactive words have weak contrast and no hover state.
  - There is no indication that words are clickable.
  - Six text-only targets need adequate hit areas.
- It is a great pattern for picking presets in generative tools.

## 10. Craft signals
- The connector becomes straight when word and tile anchor are on the same row, and an S-curve otherwise.
- The rows are aligned to the tile at its 25%, 50% and 75% height.
- The active state is shown by value only (#3a3a3a vs #a8a29e), with no underline or weight change.
- The glow colour follows the shader palette.
- The squircle radius is about 11% of the tile size, matching the iOS icon proportion.

## 11. Reproduction recipe
```css
:root{--bg:#f4f3f1;--ink:#3a3a3a;--muted:#a8a29e;--wire:#c9c7c4;--tile-a:#3a6cab;--tile-b:#5788c4;--tile-c:#234a86}
.mixer{display:grid;grid-template-columns:1fr 640px 1fr;align-items:center;gap:410px}
.opts{display:grid;gap:254px}.opts--l{justify-items:end}
.opt{font:500 52px/1 Inter;color:var(--muted);transition:color .2s}.opt[aria-checked=true]{color:var(--ink)}
.tile{width:640px;aspect-ratio:1;border-radius:72px;
  background:radial-gradient(60% 50% at 35% 60%,var(--tile-b),transparent),radial-gradient(70% 60% at 70% 20%,var(--tile-c),transparent),var(--tile-a);
  box-shadow:0 40px 120px color-mix(in srgb,var(--tile-a) 25%,transparent);transition:background .27s ease-in-out}
svg.wire path{fill:none;stroke:var(--wire);stroke-width:2;stroke-dasharray:14 10;transition:d .2s cubic-bezier(.2,.8,.2,1)}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Spare, balanced layout where one colourful tile does all the work. |
| Originality | 8 | The two-axis word mixer with patch-cable connectors is a fresh preset UI. |
| Usability | 7 | Clear mapping, but inactive words fail contrast and lack affordance. |
| Craft | 8 | Row alignment, connector logic and the glow follow-through are carefully considered. |

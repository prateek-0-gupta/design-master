---
id: insp-dynamic-island-pixel-art-horse
source: inspora
category: Motion
status: analyzed
title: "Dynamic Island pixel-art horse"
creator: "@krispuckett"
styles: [retro-pixel, micro-interaction, minimal-swiss]
patterns: [dynamic-island-live-activity, pixel-art-mascot, agent-working-indicator, island-expand-collapse, dot-matrix-icon-set, parallax-pixel-landscape, mascot-name-label]
mode: mixed
palette: ["#f4f2e5", "#e9e7da", "#000000", "#121211", "#5f6057", "#a8a89d", "#a8c49a", "#e0a040"]
type_families: ["SF Pro Text / Display (system)"]
type_class: [neo-grotesk, pixel]
radius_px: [70, 9999]
motion: {durations_s: [0.97, 0.4, 0.33, 0.63, 0.13], easing: [ease-in-out, ease-out], loop: true}
scores: {aesthetics: 9, originality: 9, usability: 7, craft: 9}
craft_signals: [toolbar-icons-drawn-on-same-dot-grid, single-warm-pixel-window-light, landscape-ridges-in-two-greys, horse-gallop-cycle-on-pixel-grid, island-collapses-to-show-name, cream-paper-ui-vs-black-island]
anti_patterns: [indicator-semantics-unclear-without-label]
---
# Dynamic Island pixel-art horse — @krispuckett

## 1. Snapshot
- **Subject:** A 10 s, 1206×600 crop of an iPhone top bar where the Dynamic Island expands into a night-time pixel landscape with a white horse ("Shadowfax") galloping across — a Live Activity for the creator's AI agent — then collapses to show its name.
- **Why it's remarkable:** The agent's "working" state is a character, not a spinner, and the surrounding toolbar icons are drawn on the same dot grid, so the island and app chrome speak one pixel language.

## 2. Composition & layout
- Native 3× capture: expanded island ≈610×275 px (≈203×92 pt) centred at x≈603, top at y≈42, corner radius ≈70 px.
- Status bar time "9:23" at left (≈44 px), Wi-Fi + battery at right.
- Two 132 px circular glass buttons sit at x≈115 and x≈1092, y≈265 — menu (2×5 dots) and add (dot cross).
- Scene: stars scattered in the top 60%; terrain band in the bottom ≈30% (mountains, pines, a lit cabin window); horse ≈130×60 px.
- Collapsed state (7.2–8.3 s): island ≈230×65 px; "Shadowfax" label ≈36 px semibold appears centred below it.

## 3. Typography
- SF Pro throughout: list text ≈44 px regular, bold lead phrases ("VisionKit capture idea") as inline headings.
- Mascot name "Shadowfax" ≈36 px semibold, centred — the only label for the indicator.
- Pixel content uses ≈6 px square dots on a ≈7 px pitch; the icons reuse that pitch.

## 4. Colour
| Hex | Role | Share (key frame) |
|---|---|---|
| #f4f2e5 | cream app canvas | 63% |
| #e9e7da | list section band | 4% |
| #000000 | island | 19% |
| #f4f2e5 | horse, stars (pixel white) | — |
| #5f6057 / #a8a89d | mountain ridges (two greys) | 8% |
| #a8c49a | pine trees | — |
| #e0a040 | single cabin window light | <0.1% |
| #121211 | body text | 3% |

WCAG (contrast.py):
- Body #1c1c18 on #f4f2e5: 15.2:1; on #e9e7da band: 13.76:1.
- Horse #f4f2e5 on black: 18.68:1; trees #a8c49a: 11.03:1.
- Far ridge #5f6057 on black: 3.3:1 — intentionally recessive.

## 5. Depth & material
- Depth inside the island comes from value layering: far ridges dim grey, near ridges lighter, trees green, horse brightest.
- Toolbar buttons are frosted circles with a 1 px warm-grey rim over blurred text — iOS 26-style glass.
- A blurred header band (text behind the toolbar visibly defocused) separates chrome from content.

## 6. Components & patterns
- **Live Activity as mascot:** a running horse means "agent is working"; collapse to the compact island + name means "idle / done".
- **Dot-matrix icon set:** menu = 2×5 dots, add = dot cross; matches the pixel scene.
- **Parallax pixel terrain:** the landscape scrolls under the horse while stars stay fixed.
- Content behind (notes about LongRunningIntent, VisionKit) shows it is a dev/agent notes app.

## 7. Motion
Measured (m0_motion.json): 10.0 s at 60 fps, motion_fraction 0.19, seamless_loop_likely true, 8 segments, median 0.23 s.
- 1.47–2.43 s (0.97 s, peak 0.64, symmetric): largest move — the horse crosses/terrain scrolls (horse x≈260→300 in sheet units between 0.56 s and 1.67 s, then on to the right edge by 6.1 s).
- 3.13–3.53 s (0.40 s, ease-out) and 4.23–4.33 s (0.10 s): gallop/scene steps; much of the gallop is stepped pixel animation below the energy threshold (frame-by-frame, not tweened).
- 7.07–7.40 s (0.33 s, peak 0.05, ease-out): island collapses to compact pill and the name fades in — a fast, spring-like shrink.
- 9.13–9.77 s (0.63 s, peak 0.24, ease-out): island re-expands with the horse re-entering from the left.
Short sub-0.15 s segments (0.43, 2.57, 2.93 s) are discrete sprite steps.

## 8. Brand system
n/a — not a brand system. Identity cues: the named mascot "Shadowfax", cream paper palette, and dot-grid iconography form a personal-app identity.

## 9. UX
- A character conveys "long-running task in progress" with more warmth and glanceability than a ring.
- Collapse + name label is a clear state change.
- Risk: without the label, a horse doesn't say *what* is running or how far along; no progress measure.

## 10. Craft signals
- Toolbar icons are built from the same ≈6 px dots as the island art.
- Exactly one warm pixel (the cabin window, #e0a040-ish) in an otherwise cool scene.
- Ridges use two grey values to fake atmospheric perspective.
- The gallop is stepped (sprite frames), not smoothly tweened — authentic to pixel art.
- App canvas is cream #f4f2e5, not white, so the black island reads as an object cut into paper.

## 11. Reproduction recipe
```css
:root{--paper:#f4f2e5;--band:#e9e7da;--ink:#1c1c18;--px:6px;--pitch:7px}
.island{width:203pt;height:92pt;border-radius:24pt;background:#000;overflow:hidden;
  transition:width .35s cubic-bezier(.2,.9,.25,1.1),height .35s cubic-bezier(.2,.9,.25,1.1)}
.island.compact{width:77pt;height:22pt}
.scene{image-rendering:pixelated;background:url(terrain.png) repeat-x 0 100%/auto 30%;animation:pan 6s linear infinite}
@keyframes pan{to{background-position:-100% 100%}}
.horse{width:44px;height:20px;background:url(horse-sprite.png) 0 0/400% 100%;image-rendering:pixelated;
  animation:gallop .4s steps(4) infinite}
@keyframes gallop{to{background-position:-400% 0}}
.icon-dots{background:radial-gradient(var(--ink) 45%,transparent 46%) 0 0/var(--pitch) var(--pitch)}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 9 | Charming pixel nocturne inside a perfect black capsule on cream paper. |
| Originality | 9 | A mascot Live Activity for an AI agent, with matching dot-grid icons, is a new idea. |
| Usability | 7 | Warm, glanceable status; lacks progress or task detail. |
| Craft | 9 | Consistent dot pitch across art and icons, stepped sprite animation, single warm accent. |

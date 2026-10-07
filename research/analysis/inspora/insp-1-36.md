---
id: insp-1-36
source: inspora
category: Motion
status: analyzed
title: "Liquid metal button"
creator: "Brett (@BrettFromDJ)"
styles: [neumorphism, y2k-chrome, physical-material, monochrome]
patterns: [chrome-bezel-pill, travelling-specular-border, segmented-control-tray, recessed-track, ghost-mono-label]
mode: light
palette: ["#d3d3d3", "#c2c2c2", "#b4b4b4", "#e0e0e0", "#919091", "#000000", "#e8d3b0"]
type_families: ["Inter Display / SF Pro Display Medium (likely)", "JetBrains Mono / IBM Plex Mono (likely)"]
type_class: [neo-grotesk, mono]
radius_px: [9999, 48]
motion: {durations_s: [26.3], easing: [linear], loop: false}
scores: {aesthetics: 8, originality: 6, usability: 5, craft: 8}
craft_signals: [rim-reflects-dark-environment-on-one-side, chromatic-fringe-at-highlight-ends, tray-inner-shadow-depth, light-only-moves-not-geometry, single-black-label]
anti_patterns: [secondary-label-near-invisible, inactive-segment-undefined, slow-ambient-only-motion]
---
# Liquid metal button — Brett (@BrettFromDJ)

## 1. Snapshot
- **Subject:** A 3052×2160, 26.3 s, 30 fps macro capture of a light-grey segmented control. The selected segment "Elements" is a raised pill wrapped in a thin polished-chrome bezel whose reflections slowly slide around the perimeter. Beneath it sits a card labelled "PORTFOLIO".
- **Why it's remarkable:** A thin mirror band does the work of reflecting a dark studio environment (black and navy streaks) with prismatic orange and blue flares at the transitions. A flat grey UI reads as machined metal and glass without any colour.

## 2. Composition & layout
- **Framing:** A macro crop. The pill and tray continue off the right edge; a second, inactive segment is visible only as a darker grey rounded shape at x≈2500+ real px.
- **Selected pill:** ≈2027×635 real px (key scale 1.53), aspect ≈3.2:1, with a fully rounded radius.
- **Tray:** ≈788 px tall (pill + ≈75 px padding top and bottom), offset ≈75 px left of the pill.
- **Label:** "Elements" is centred in the pill, cap height ≈138 px, width ≈750 px (≈37% of the pill width).
- **Below:** a second surface (card) starts at y≈1680 with a ≈48 px corner radius. "PORTFOLIO" sits ≈190 px in from its left edge.

## 3. Typography
- **Label:** a neo-grotesk Medium (Inter Display / SF Pro Display-like), pure black, normal tracking. The "t" and "s" terminals are flat and the "e" has a horizontal bar.
- **Secondary label:** "PORTFOLIO" is an uppercase monospace (JetBrains Mono / Plex Mono-like) at ≈75 px cap height, tracked ≈+0.15em, in off-white #f2f2f2 on grey. It is styled as an embossed or debossed label rather than as information.
- **Pairing logic:** the sans is used for the interactive label and the mono for section metadata.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #d3d3d3 | page / tray surface | 69% |
| #e0e0e0 | selected pill face | 9% |
| #c2c2c2 | card surface | 9% |
| #b4b4b4 | recessed shadow below tray, inactive segment | 11% |
| #919091 | chrome mid-tone, deep shadow | 2% |
| #000000 | label; dark reflection in rim | <1% |
| #e8d3b0 | warm flare in chrome | 0.1% |

WCAG checks:
- The black label on the pill #e0e0e0: **15.91:1**.
- "PORTFOLIO" (#f2f2f2 on #c2c2c2): **1.59:1**, effectively invisible as text.
- The inactive segment (#b4b4b4) against the tray (#d3d3d3) is 1.39:1, so the unselected option's affordance is very weak.

## 5. Depth & material
- **Stack:** a three-level neumorphic stack.
  1. A page at #d3d3d3.
  2. A tray with a soft inner bevel: a lighter top edge, and a ≈60 px soft drop shadow below it that darkens the region at y≈1450–1650 to ≈#b4b4b4.
  3. The selected pill, raised, with a subtle vertical gradient (#e6e6e6 top → #dadada bottom).
- **Bezel:** ≈12 px thick (real) and acts as a curved mirror. Sections reflect black/navy (the dark environment) and others reflect white sky. At each black-to-white transition there is a ≈30 px chromatic fringe (orange/yellow on one side, blue on the other), which mimics dispersion in a curved, clear-coated edge.
- **Card below:** recessed, with a 1 px lighter top highlight.

## 6. Components & patterns
- **Segmented control / tab switcher:** the selected item is a raised chrome-edged pill and the others are flat recessed pills.
- **Card header:** a mono-label card header ("PORTFOLIO").
- **Pattern worth reusing:** a reflective border that conveys "selected" through material rather than colour.

## 7. Motion
- **Measured:** 26.3 s at 30 fps. motion_fraction **0.01**, mean energy 0.15, no segments above threshold. seamless_loop_likely false (first/last diff 2.02).
- **Interpretation:** the movement is a slow, continuous drift of the reflection map with no geometry change.
- **From frames (estimates):**
  - The dark reflection band shifts from the bottom-left (1.46 s) through the bottom and top (4.38–10.23 s). The warm flare reaches the top edge at 13.15–16.07 s and returns to the bottom-left by 24.84 s.
  - This is roughly one full sweep in ≈25 s, i.e. effectively linear environment rotation, like turning an HDRI.

## 8. Brand system
n/a — not a brand system. Identity cues: Dieter-Rams-grey hardware aesthetics plus chrome trim.

## 9. UX
- **Strengths:** The selected state is unmistakable, and the label contrast is very high.
- **Risks:**
  - The unselected segment and the "PORTFOLIO" label fall below 1.6:1, so a real user may not find the other options.
  - The ambient motion carries no state meaning; it should respond to pointer or tilt rather than loop.
  - Neumorphic depth relies on subtle shadows that disappear on low-quality displays.

## 10. Craft signals
- The chrome bezel shows both dark (#000/navy) and bright reflections with prismatic fringes only at transitions.
- The pill face has its own soft vertical gradient (≈#e6e6e6 → #dadada) distinct from the tray.
- The tray's drop shadow is wide and soft (≈60 px) with no hard edge.
- The animation moves only the reflections; the button geometry stays pixel-stable across all 9 frames.
- Black is used once (the label), so all hierarchy sits on it.

## 11. Reproduction recipe
```css
@property --r{syntax:"<angle>";inherits:false;initial-value:0deg}
:root{--page:#d3d3d3;--face:#e0e0e0;--tray:#cfcfcf;--shadow:#b4b4b4}
.tray{display:flex;gap:24px;padding:38px;border-radius:9999px;background:var(--tray);
  box-shadow:inset 0 2px 0 rgba(255,255,255,.6),0 30px 60px -20px rgba(0,0,0,.25)}
.seg{height:318px;padding:0 220px;border-radius:9999px;background:#c4c4c4;font:500 92px/1 "Inter Display",system-ui}
.seg[aria-selected=true]{position:relative;background:linear-gradient(#e6e6e6,#dadada);color:#000}
.seg[aria-selected=true]::before{content:"";position:absolute;inset:-6px;border-radius:inherit;padding:6px;
  background:conic-gradient(from var(--r),#111 0 18%,#ffb347 20%,#fff 24% 45%,#3a5bd9 47%,#14152a 50% 68%,#f5f5ff 72% 95%,#111);
  -webkit-mask:linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);-webkit-mask-composite:xor;mask-composite:exclude;
  animation:env 25s linear infinite}
@keyframes env{to{--r:360deg}}
.card-label{font:400 38px/1 "JetBrains Mono",monospace;letter-spacing:.15em;color:#f2f2f2;text-shadow:0 1px 0 rgba(0,0,0,.08)}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Refined monochrome hardware feel; the chrome rim is beautifully rendered. |
| Originality | 6 | A chrome/conic border on a neumorphic pill is a known trend, though done well. |
| Usability | 5 | Selected state is clear; everything else is too low-contrast to use. |
| Craft | 8 | Physically plausible reflections and stable geometry; layered surfaces handled carefully. |

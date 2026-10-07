---
id: insp-1-43
source: inspora
category: Motion
status: analyzed
title: "Emotion Shader"
creator: "@raul_dronca"
styles: [organic-blob, soft-3d, minimal-swiss, aurora-glow]
patterns: [mood-picker-wheel, depth-of-field-list, shader-orb-state, colour-coded-emotion-scale, coloured-glow-halo]
mode: light
palette: ["#f4f3f1", "#333333", "#aac3d9", "#9bccc6", "#e2b43a", "#d82648", "#ac0b03", "#88203b", "#86749c", "#4d5258"]
type_families: ["Inter / SF Pro Text (likely)"]
type_class: [neo-grotesk]
radius_px: [9999]
motion: {durations_s: [1.8], easing: [ease-in-out], loop: false}
scores: {aesthetics: 9, originality: 8, usability: 6, craft: 8}
craft_signals: [blur-increases-with-distance-in-list, glow-tinted-by-orb-colour, swirl-dimple-lighting, valence-ordered-colour-ramp, single-focus-label-weight, warm-paper-background]
anti_patterns: [neighbour-labels-illegible, colour-only-meaning]
---
# Emotion Shader — @raul_dronca

## 1. Snapshot
- **Subject:** A 2876×2160, 20.4 s, 60 fps capture of a mood picker. A soft, swirling shader sphere sits on the left, and a vertical wheel of emotion words sits on the right: Calm → Tender → Wonder → Joy → Desire → Passion → Fury → Obsession → Longing → Heavy → Void. As the wheel scrolls, the sphere's colour and internal swirl change to embody each emotion.
- **Why it's remarkable:** It maps a qualitative scale to a continuous material. Colour (pale blue → teal → gold → orange → crimson → blood red → wine → lilac → slate) and surface turbulence both shift, so choosing a feeling is visceral rather than a list tap.

## 2. Composition & layout
- **Orb:** centred at ≈x 1440, y 1075 real (key scale 1.44), diameter ≈560 px, about 26% of the frame height. A coloured glow extends ≈150 px beyond its edge.
- **Wheel:** starts ≈210 px right of the orb's edge. The active label is vertically aligned with the orb's centre. Neighbours sit on a ≈155 px pitch above and below.
- **Space:** about 80% of the canvas is empty warm off-white. The pair (orb + word) reads as a single centred unit with optical balance between the heavy orb and the light text.

## 3. Typography
- **Typeface:** a neutral neo-grotesk (Inter / SF-like). Regular weight for every item.
- **Active word:** ≈60 px real in #333333.
- **Depth of field:** neighbours at ±1 are ≈50 px, light grey and slightly blurred; neighbours at ±2 are smaller, paler and heavily blurred (≈6–10 px Gaussian). The wheel imitates a camera focus pull rather than an iOS drum picker's 3D tilt.
- There is no other text. The single word plus the orb is the whole interface.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #f4f3f1 | warm paper background | 93% |
| #333333 | active label | <0.5% |
| #aac3d9 | Calm (pale steel blue) | state |
| #9bccc6 | Wonder (sea-glass teal) | state |
| #e2b43a | Joy (marigold) | state |
| #d82648 | Passion (crimson; key frame #d22948/#ae1e3c) | 1.5% in key frame |
| #ac0b03 | Fury (blood red, darkest core #8d0205) | state |
| #88203b | Obsession (wine) | state |
| #86749c | Longing (lavender grey) | state |
| #4d5258 | Heavy / Void (slate) | state |

The orb hexes above were sampled from frame pixels per state.

WCAG checks:
- Active label #333 on #f4f3f1: **11.39:1**.
- Neighbour labels (≈#d8d6d3): **1.31:1**, which is intentional atmosphere but unreadable.

The colour ramp roughly tracks arousal and valence: cool and light for calm, saturated and warm for high arousal, desaturated and dark for low.

## 5. Depth & material
- **Orb shading:** a smooth matte, clay-like sphere lit from the upper left. A "swirl dimple" (a twisted fold of lighter and darker tone, like a cream swirl) rotates inside it. Its tightness and contrast vary: a gentle S for Calm, a sharp hooked fold with specular orange-red for Fury.
- **Halo:** a radial glow tinted with the orb's colour (pink around Passion, gold around Joy). It is the only "shadow", so the orb seems lit from within rather than resting on the page.
- **List:** depth comes from blur (depth of field) rather than shadows or perspective.

## 6. Components & patterns
- **Scroll or wheel picker** with a single selected value. The visualisation acts as live feedback for the selected value.
- **Pattern:** a "state object". One hero visual is driven by a categorical selection, which is useful for mood trackers, AI voice-tone selectors and theme pickers.

## 7. Motion
- **Measured:** 20.38 s at 60 fps. motion_fraction **0.01**, mean energy 0.06. Only one segment crosses the threshold (15.17–15.27 s, 0.10 s). seamless_loop_likely false (first/last diff 6.91, Calm → Void).
- **Interpretation:** every change is a slow, low-energy blend with no hard cuts. The sequence moves through 11 emotions in ≈20 s, about **1.8 s per emotion**.
- **From frames (estimates):**
  - The colour cross-fades continuously.
  - The swirl inside the orb rotates and re-folds throughout.
  - The wheel scrolls smoothly so the next word glides into focus, its blur dropping as it centres.
  - The halo colour lags the orb slightly.

## 8. Brand system
n/a — not a brand system.

## 9. UX
- **Strengths:**
  - A single, unambiguous selection.
  - Emotional resonance makes picking a mood feel expressive.
  - Minimal cognitive load.
- **Risks:**
  - Neighbour words are illegible, so users cannot preview options without scrolling.
  - Meaning is carried partly by colour (an accessibility issue, though the word is always shown).
  - The order is not self-evident (why Obsession after Fury?).
  - WebGL cost.
  - A slow blend makes fast selection hard.

## 10. Craft signals
- The list blur increases with distance from the focused word: about 0 / 3 / 8 px for ±0, ±1 and ±2.
- The orb's halo is tinted with the orb's current hue, not a neutral shadow.
- The swirl fold changes character per emotion (gentle for Calm, sharp with specular for Fury).
- The colours run in an ordered ramp from cool-light to hot-saturated to dark-desaturated.
- The background is warm paper (#f4f3f1) rather than pure white, so saturated orbs never look harsh.
- The active word is the only text above 1.3:1 contrast.

## 11. Reproduction recipe
```css
:root{--paper:#f4f3f1;--ink:#333;--orb:#d82648}
body{background:var(--paper);font-family:Inter,system-ui}
.orb{width:280px;aspect-ratio:1;border-radius:50%;
  background:
    radial-gradient(60% 40% at 62% 38%,color-mix(in oklab,var(--orb),#fff 25%) 0 40%,transparent 41%),
    radial-gradient(circle at 35% 30%,color-mix(in oklab,var(--orb),#fff 18%),var(--orb) 55%,color-mix(in oklab,var(--orb),#000 25%));
  box-shadow:0 0 80px 10px color-mix(in oklab,var(--orb) 45%,transparent);
  transition:--orb 1.6s ease-in-out,background 1.6s ease-in-out}
.wheel li{font:400 30px/1 Inter;color:var(--ink);transition:filter .6s,opacity .6s,font-size .6s}
.wheel li[data-d="1"]{opacity:.25;filter:blur(1.5px);font-size:25px}
.wheel li[data-d="2"]{opacity:.12;filter:blur(4px);font-size:22px}
```
For the true swirl, use a fragment shader with domain-warped noise (`p += 0.4*sin(p.yx*3.0+t)`) shaded by a Lambert term on a sphere normal, and expose `uColor` and `uTurbulence` per emotion.

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 9 | A serene composition with luscious shader material and a well-chosen colour ramp. |
| Originality | 8 | An emotion-to-material mapping is fresh; the orb-picker form is familiar. |
| Usability | 6 | Clear current value; options are hidden in blur and selection is slow. |
| Craft | 8 | Graded depth of field, tinted halos, consistent ordering. |

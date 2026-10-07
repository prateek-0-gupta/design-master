---
id: insp-6-2
source: inspora
category: Motion
status: analyzed
title: "Camera transitions"
creator: "@azhassan_"
styles: [x-comic-game-ui, playful-rounded, soft-3d, maximalist-color]
patterns: [3d-icon-shared-element-transition, skewed-comic-labels, color-collection-grid, mystery-slot-placeholders, progress-quest-card, camera-viewfinder-modal]
mode: light
palette: ["#ffffff", "#fbf7ee", "#121013", "#f7ff33", "#7f3de5", "#ef0e9b", "#b5b3b4"]
type_families: ["Inter / SF Pro-style grotesk (likely)"]
type_class: [neo-grotesk, display]
radius_px: [80, 40, 9999]
motion: {durations_s: [0.87, 0.97], easing: [ease-out], loop: false}
scores: {aesthetics: 8, originality: 9, usability: 7, craft: 8}
craft_signals: [3d-camera-flies-and-becomes-viewfinder, yellow-offset-shadow-on-black-labels, skewed-parallelogram-tags, background-blurs-during-transition, question-mark-locked-slots, jagged-speech-tail]
anti_patterns: [inactive-tab-label-low-contrast, dense-ornament-around-small-text]
---
# Camera transitions — @azhassan_

## 1. Snapshot
- **Subject:** A 7.1 s, 1920×1920 phone demo of a colour-hunting game app. A 3D purple camera icon in the "Find this color" card lifts off, spins, and expands into a full camera viewfinder ("Color Hunt"). A bottom sheet shows challenges ("Unlock 3 colors through Color Hunt").
- **Why it's remarkable:** It is a true shared-element transition with a 3D object. The same purple camera morphs from button to device frame, styled like Persona-esque game UI.

## 2. Composition & layout
- **Phone:** About 1060 px wide in the frame, on a white backdrop with a long soft shadow toward the bottom-right. The camera crops in and out across frames.
- **Collection screen:**
  - A grid of circles about 280 px wide: found colours (pink #ef0e9b, purples) and "?" placeholders.
  - A white quest card with a jagged black underline and speech-tail.
  - A black skewed "Find this color" tag with a yellow offset.
  - Bottom tabs (Capture / Collection) as tilted sticker tiles.
- **Viewfinder:** A black screen about 470×470 px inside a thick purple rounded frame (radius about 40), with a purple shutter button, a "^ ^" mascot face and a dial.

## 3. Typography
- A grotesk (Inter or SF-like).
- **Body:** Regular at about 34 px ("Still out there somewhere…").
- **Tags:** Bold at about 36 px, white on black inside skewed tags.
- **Numerals:** Chunky, outlined and skewed ("41", "0/3", "125"), like game HUD numerals.
- Labels are skewed about −8° with a yellow drop offset.

## 4. Colour
| Hex | Role |
|---|---|
| #ffffff | backdrop, cards |
| #fbf7ee | phone background (cream) |
| #121013 | tag fill, outlines |
| #f7ff33 | acid-yellow offset shadows, accents |
| #7f3de5 | 3D camera, viewfinder frame |
| #ef0e9b | discovered colour swatch |
| #b5b3b4 | inactive tab icon and label |

WCAG:
- White on #121013 tags is 18.93:1.
- Body #3a3a3a on white is 11.37:1.
- The inactive "Capture" label #b5b3b4 on #fbf7ee is **1.95:1** (fails).

## 5. Depth & material
- **3D object:** The camera is a glossy, low-poly-smooth rendered model with a purple body, silver lens and specular highlights.
- **Flat UI:** Hard offset shadows (yellow, about 8 px down-right) rather than blur shadows. The comic or manga language mixes with soft-3D.
- **During transition:** The background UI blurs (about 20 px), and colour circles become bokeh. That is depth of field focusing on the flying object.

## 6. Components & patterns
- **Colour collection grid:** Locked slots shown with "?" in white circles.
- **Quest card:** A palette emoji with "???", a hint line, and a CTA tag.
- **Sticker tab bar:** The active tab is a black tag with a yellow offset, and the inactive one is a grey label.
- **Camera modal:** A hot/cold meter (cyan to red striped bar) with an instruction line, and a close "×" tile.
- **Progress card:** Pink striped progress bars with skewed "0/3" counters and a green "125" gem reward.

## 7. Motion
- **Measured:** 2 segments across 7.07 s.
  - 0.90–1.77 s: 0.87 s, peak 0.13 (ease-out). The camera lifting, spinning and expanding into the viewfinder.
  - 3.00–3.97 s: 0.97 s, peak 0.02 (strong ease-out). The reverse: the viewfinder collapses back into the icon, then the view scrolls to challenges.
  - motion_fraction is 0.27 and `seamless_loop_likely: false`.
- **Read:** Large, energetic, front-loaded moves of about 0.9 s that launch fast and glide in. Background blur ramps up during flight.

## 8. Brand system
n/a — not a brand system. Identity cues: an acid yellow, black and purple triad, skewed sticker labels, and a "^ ^" camera mascot. It is coherent enough to be an app brand.

## 9. UX
- The shared-element transition preserves context: the user knows the camera came from "Find this color".
- Gamified progress is legible.
- **Risks:**
  - Ornament density (offsets, tails, skews) around small text.
  - The low-contrast inactive tab.
  - About 0.9 s transitions may feel slow on repeat use.

## 10. Craft signals
- The 3D camera's purple (#7f3de5) is identical to the viewfinder frame, so the morph is seamless.
- Every black tag has the same about 8 px yellow offset, skewed at the same angle.
- The background blurs only during flight and refocuses on landing.
- Locked colours use the same circle size as found ones, so the grid stays stable.
- A jagged speech-tail on the quest card ties it to the comic language.

## 11. Reproduction recipe
```css
:root{--bg:#fbf7ee;--ink:#121013;--acid:#f7ff33;--cam:#7f3de5;--pink:#ef0e9b;--muted:#8f8d8e}
.tag{display:inline-block;background:var(--ink);color:#fff;font:700 36px/1 Inter;padding:14px 24px;
  transform:skewX(-8deg);box-shadow:8px 8px 0 var(--acid)}
.slot{width:280px;aspect-ratio:1;border-radius:50%;background:#fff;display:grid;place-items:center}
.viewfinder{border:28px solid var(--cam);border-radius:40px;background:#000}
/* shared element: View Transitions API */
.cam-icon{view-transition-name:camera}.viewfinder{view-transition-name:camera}
::view-transition-group(camera){animation-duration:.9s;animation-timing-function:cubic-bezier(.05,.7,.1,1)}
::view-transition-old(root){animation:blurOut .9s both}@keyframes blurOut{to{filter:blur(20px);opacity:.6}}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | A bold game-UI language with an acid yellow, black and purple triad. |
| Originality | 9 | A 3D shared-element morph from icon to viewfinder in a comic aesthetic is rare. |
| Usability | 7 | Context-preserving transition and clear progress, but busy ornament and a weak inactive tab. |
| Craft | 8 | Consistent offsets and skews, colour-matched morph and a focused blur during flight. |

---
id: insp-3d-interactive-cassette-tape
source: inspora
category: Motion
status: analyzed
title: "3D interactive cassette-tape"
creator: "@louis_bcqt"
styles: [dark-premium, technical-wireframe, skeuomorphic, terminal-mono]
patterns: [3d-object-shelf-browser, hairline-device-frame, crosshair-registration-ticks, now-playing-panel, line-drawn-player-controls, blurred-backdrop-echo, frame-draw-on-intro]
mode: dark
palette: ["#000000", "#0f0f0f", "#242121", "#393634", "#7a837f", "#ffffff"]
type_families: ["Space Mono / JetBrains Mono uppercase (likely)"]
type_class: [mono]
radius_px: [10, 6]
motion: {durations_s: [0.43, 0.77, 1.0, 1.5], easing: [ease-in-out, ease-out], loop: false}
scores: {aesthetics: 9, originality: 8, usability: 6, craft: 8}
craft_signals: [frame-draws-itself-before-content, corner-dots-on-hairline-frame, crosshair-ticks-mid-edges, colour-only-from-tape-art, blurred-copy-of-ui-as-backdrop, mono-microcopy-uppercase, line-icon-player-hardware]
anti_patterns: [secondary-labels-1-75-to-1, micro-type-around-7px, no-loop]
---
# 3D interactive cassette-tape — @louis_bcqt

## 1. Snapshot
- **Subject:** A 6.55 s, 720×900, 60 fps recording of a music-sample library UI. A row of ~14 photoreal 3D cassette tapes stands on edge in a diagonal domino line inside a hairline-framed black panel. Scrolling fans through them, and the selected tape's title appears top-left ("LA DI DA DI / DOUG E. FRESH & SLICK").
- **Why it's remarkable:** The UI chrome is pure 1 px white line-work and mono type on black, like a technical HUD, so the only colour on screen is the vintage J-card artwork. The physical objects carry all the nostalgia; the interface stays invisible.

## 2. Composition & layout
- **Panel:** a landscape panel of about 605×385 px (x 52–657, y 260–640), radius ≈10 px, with tiny corner dots. It is centred vertically in a 4:5 frame. The area around it is a heavily blurred, darkened copy of the tapes (bokeh colour blobs).
- **Left column (~150 px):**
  - "SAMPLES 01" pill tag plus a 3-line description;
  - centred "WHAT'S PLAYING ?" with the sub-label "CLICK TO LOAD THE TAPE";
  - a line-drawn tape-deck widget (speaker grille circle, dial knob, "CHOOSE A TAPE" hatched slot, play/pause pair).
- **Right viewport (~440×355 px):** an inner frame with crosshair ticks at the mid-points of each edge. The tapes run in a diagonal from bottom-left (near, ~150 px tall) to top-right (far, ~60 px), a strong 35° leading line.
- **Captions:** top-left of the viewport for the title, bottom-left for "CLICK TO LISTEN", and a cassette line icon bottom-right.

## 3. Typography
- A single uppercase monospace (Space Mono or JetBrains Mono-like) for all UI. At this 720 px capture the labels are about 6–8 px tall, which suggests 10–12 px on the original 1440-wide UI.
- Headline "WHAT'S PLAYING ?" is bold, with a French-style space before "?" (a cue to the designer's locale).
- Tracking is about +0.08 em.
- Hierarchy: white for active labels, grey (#7a837f) for the track title, dark grey (#393634) for the artist line.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #000000 | panel, viewport | 64% |
| #0f0f0f / #242121 | blurred backdrop | 29% |
| #393634 | artist sub-line, dim UI | 4% |
| #7a837f | track title, secondary text | 2.6% |
| #ffffff | hairlines, active labels, icons | <1% |
| tape art (cyan #4fd1d9, red, yellow, magenta) | content only | — |

WCAG checks:
- White on black is 21:1.
- The title (#7a837f) is 5.38:1.
- The artist line (#393634) is **1.75:1** and effectively invisible.
- Light text on the blurred backdrop (#d9d9d9 on #0f0f0f) is 13.58:1.

## 5. Depth & material
- **Tapes:** real 3D renders with PBR plastic. They have translucent smoked shells, visible reels and screws, and a soft rim light from the upper right. There is no floor; the tapes float on black, separated by their own specular edges.
- **UI:** completely flat at a 1 px stroke. Depth contrast between the flat HUD and the photoreal objects is the core idea.
- **Backdrop:** a full-frame blur (~40 px) of the same scene at about 30% brightness, which gives ambient colour without competing.

## 6. Components & patterns
- 3D shelf or carousel browser (scroll moves the camera along the row; hover lifts a tape).
- "Now playing" metadata header that swaps per selection: "LIKE A G6", "CHANGE THE BEAT", "LA DI DA DI", "SYNTHETIC SUBSTITUTION".
- Skeuomorphic deck controls drawn as line icons.
- Instructional microcopy: "Click to load the tape" and "Click to listen".

## 7. Motion
Measured values (`m0_motion.json`):
- Four segments:
  - 0.80–1.23 s (0.43 s, symmetric ease-in-out): the UI and tapes fade in after the frame draw;
  - 2.00–2.77 s (0.77 s, peak 0.07, a sharp ease-out);
  - 3.07–4.07 s (1.00 s, peak 0.28);
  - 4.70–6.20 s (1.50 s, peak 0.28).
- The last three are scroll steps through the row with decelerating, inertial camera moves.
- Motion fraction is 0.57. `seamless_loop_likely` is false (first/last diff 14.2), so this is a demo, not a loop.

From the frames (estimate): at 0.36 s only the panel outline exists, drawn as a stroke from the top-left corner. The frame-draw intro takes about 0.5 s before content appears.

## 8. Brand system
n/a — this is not a brand system. Identity cues are the "SAMPLES 01" index tag (implying a series), the cassette line icon as logo, and the mono HUD language.

## 9. UX
- **Strengths:** Browsing physical-looking objects is intuitive and fun. The selected item's metadata is always in the same spot.
- **Risks:**
  - Micro mono type will be tiny on real screens.
  - The artist line fails contrast badly.
  - The diagonal row crops near tapes at the viewport's left edge.
  - Keyboard navigation along the row and reduced-motion camera snapping are needed.

## 10. Craft signals
- The panel outline draws itself before any content loads (frame t=0.36 s).
- Hairline frames have small filled dots at the corners and crosshair ticks at the edge midpoints, like camera viewfinder marks.
- The only colour is the album and J-card art; the UI is strictly monochrome.
- The backdrop is a blurred duplicate of the scene, so the ambient colour always matches the content.
- The deck widget repeats real hardware vocabulary (grille, knob, eject slot, piano keys) in 1 px line art.

## 11. Reproduction recipe
```css
:root{--bg:#000;--line:#fff;--dim:#7a837f;--dimmer:#5d625f;/* raise from #393634 for AA */
  --font:"Space Mono","JetBrains Mono",ui-monospace,monospace;--r:10px}
body{background:#000}
.backdrop{position:fixed;inset:0;filter:blur(40px) brightness(.3);transform:scale(1.1)}
.frame{border:1px solid var(--line);border-radius:var(--r);position:relative;
  background:radial-gradient(circle,var(--line) 1.5px,transparent 2px) 0 0/100% 100% no-repeat}
.frame::before,.frame::after{content:"";position:absolute;background:var(--line)} /* mid-edge crosshair ticks */
.frame::before{left:50%;top:0;width:1px;height:10px}.frame::after{top:50%;left:0;height:1px;width:10px}
.label{font:700 12px/1.3 var(--font);letter-spacing:.08em;text-transform:uppercase;color:var(--line)}
.meta{font:400 11px/1.3 var(--font);letter-spacing:.08em;text-transform:uppercase;color:var(--dim)}
@keyframes draw{from{stroke-dashoffset:var(--len)}to{stroke-dashoffset:0}}
.frame-svg rect{stroke:#fff;fill:none;stroke-dasharray:var(--len);animation:draw .5s cubic-bezier(.65,0,.35,1) forwards}
```
3D: three.js row of GLTF cassettes at `x=i*0.6, z=-i*0.8`, rotated 70° on Y. Lerp the camera along the row on wheel with a 0.08 factor (inertial ease-out ≈ 0.8–1.5 s settle, matching the measured segments).

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 9 | Disciplined line-HUD against lush photoreal tapes; superb tonal restraint. |
| Originality | 8 | The 3D cassette shelf as a sample browser is a fresh, on-theme metaphor. |
| Usability | 6 | Intuitive browsing, but micro type and a near-invisible artist line. |
| Craft | 8 | Frame-draw intro, viewfinder ticks and blurred-echo backdrop are well considered. |

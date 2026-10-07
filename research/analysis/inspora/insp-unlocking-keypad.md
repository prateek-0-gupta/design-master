---
id: insp-unlocking-keypad
source: inspora
category: 3D
status: analyzed
title: "Unlocking keypad"
creator: "@reijowrites"
styles: [physical-material, cinematic-3d, dark-premium, micro-interaction]
patterns: [pin-entry-feedback, masked-input-asterisks, display-inversion-on-success, key-travel-press, hero-object-on-black, celebratory-spin-reset]
mode: dark
palette: ["#000000", "#acb7b3", "#8c9794", "#57605e", "#1c1e20", "#eeeeee", "#d9a441"]
type_families: ["Neue Haas / Helvetica Now-style neo-grotesk (likely)"]
type_class: [neo-grotesk]
radius_px: [6, 10]
motion: {durations_s: [0.2, 0.13, 0.77], easing: [ease-out, ease-in], loop: false}
scores: {aesthetics: 8, originality: 7, usability: 7, craft: 8}
craft_signals: [bead-blasted-grain-on-keycaps, staggered-key-heights-cast-shadows, gold-pogo-pins-single-accent, display-polarity-flip-for-state, chamfered-edge-highlights, debossed-maker-mark]
anti_patterns: [key-labels-misaligned-across-rows, no-error-state-shown]
---
# Unlocking keypad — @reijowrites

## 1. Snapshot
- **Subject:** A 3.7 s, 1440×1080 Blender render of a brushed/bead-blasted aluminium PIN pad ("HEX HARDWARE LAB" debossed on the base). It takes a five-digit code, flips its display to "UNLOCKED", spins once and resets.
- **Why it's remarkable:** A UI state machine (empty → masked input → success → reset) told entirely through physical product language: key travel, a backlit display that changes polarity, and one celebratory rotation.

## 2. Composition & layout
- The device is a centred hero on pure #000. It occupies about 37% of the frame width (x≈380→1010 of 1440) and about 85% of the height (y≈125→945). It is shot in a three-quarter view from slightly below, so the right side rail (about 70 px thick on screen) is visible.
- **Internal grid:** a 3×4 key matrix. Each key is about 155×120 px on screen with about 4 px gaps. The display window sits top-left (about 330×95 px) and a status column sits to its right (hex icon about 40 px, three 10 px LED dots).
- **Labels:** digits sit bottom-left on each cap rather than centred, which feels typewritten and offset. CANCEL and ENTER flank the 0 key in small caps.
- A connector strip at the base (14 gold pins) plus two mounting tabs ground the object as hardware.

## 3. Typography
- The key legends are a neo-grotesk (Helvetica Now / Neue Haas-like). Digits are about 30 px on screen, regular weight, near-black (#1c1e20) printed on the metal.
- CANCEL and ENTER are about 14 px all caps with slightly open tracking (about +0.05 em).
- The display in the input state uses large white asterisks (about 45 px) and underscores as empty slots: "**___", then "****_", then "*****". The success state shows "UNLOCKED" in about 26 px wide caps with letter-spacing of about +0.08 em, dark on a light panel.
- The base mark "HEX HARDWARE LAB" is about 11 px caps, debossed (no ink).

## 4. Colour
| Hex | Role | Share (key frame) |
|---|---|---|
| #000000 | void background | 71% |
| #acb7b3 | lit aluminium face (cool green-grey) | 9% |
| #8c9794 / #9fa9a6 | aluminium mid-tones | 9% |
| #57605e / #3d4142 | shadowed sides and gaps | 4% |
| #1c1e20 | inactive display glass, legend ink | 1% |
| #eeeeee | lit display panel / asterisks | 2% |
| #d9a441 (est.) | gold connector pins, the only warm accent | <0.5% |

WCAG checks:
- Asterisks (#eeeeee) on the dark glass (#1c1e20) measure 14.41:1.
- "UNLOCKED" (#1c1e20) on the lit panel (#eeeeee) is the same 14.41:1.
- Legend ink (#1c1e20) on the key face (#acb7b3) is 8.1:1.
- The device silhouette (#acb7b3) on #000 is 10.18:1.

All pairs pass AA.

## 5. Depth & material
- **Material:** anodised aluminium with visible fine grain and sparkle (bead-blast speckle). The edge chamfers catch a cool rim light along the top and right edges.
- **Keys:** the caps are individual blocks with slightly different heights. Pressed keys sink about 8–10 px and lose their top-face highlight (frames at 0.21 s and 1.03 s show 1 and ENTER depressed).
- **Display:** the glass is recessed about 10 px into the bezel with an inner shadow.
- **Lighting:** a soft key light from upper left, no floor and no reflection. The object floats.

## 6. Components & patterns
- Masked PIN field with explicit slot placeholders (underscores), so the code length is visible before entry.
- **Success state as polarity inversion:** the dark display with light glyphs becomes a light panel with dark text. This is a brightness flip, not a hue change.
- Three-dot LED status and a hexagon "brand" button next to the display.
- Dedicated CANCEL and ENTER keys in the bottom row (the phone-keypad convention).

## 7. Motion
These timings are measured (motion_fraction 0.31, 3 segments, not a seamless loop):
- **Key press 1:** 0.13–0.33 s (0.20 s), peak at 0.08, so a fast-start ease-out. This is the snap of a key going down.
- **Key press 2:** 0.97–1.10 s (0.13 s), peak at 0.12, again an ease-out. This is the ENTER key.
- **Spin:** 2.50–3.27 s (0.77 s), peak at 0.72, an ease-in. The device yaws a full turn with heavy motion blur (frame 3.09 s) and lands back on its start pose, with the display reset to dark.

Between these, the display state changes (asterisks fill, the panel goes white, "UNLOCKED" blinks off at 1.86 s and back on at 2.27 s). These are hard cuts with no measured motion. The blink is an estimate from the frames: about 0.4 s on and off.

The rhythm is about 1.4 s of input, 1.4 s of confirmation and 0.8 s of celebration.

## 8. Brand system
n/a — not a brand system. Identity cues:
- the "HEX HARDWARE LAB" deboss;
- a hexagon glyph on the status button;
- a cool green-grey aluminium colourway with one gold accent (the pins).

## 9. UX
- As a UI metaphor, it gets the essentials right:
  - visible code length;
  - masked digits;
  - explicit confirm;
  - a success state that is unmistakable through luminance alone (works for colour-blind users).
- No failure path is shown. A "wrong PIN" shake or red LED would complete the story.
- Offset digit placement and the slight per-key rotation make the grid read as hand-built. That is charming, but the legends don't share a baseline across rows.

## 10. Craft signals
- The display flips polarity (#1c1e20 glass ↔ #eeeeee panel) to signal success, with no colour needed.
- Underscore placeholders show the remaining slots ("**___").
- Pressed keys lose their top highlight and drop about 8 px; unpressed neighbours keep their cast shadow edges.
- Gold pins are the single warm accent against an all-cool palette.
- The spin uses real motion blur at 3.09 s and resolves exactly back to the frame-0 pose.
- Debossed maker text is used instead of printed text on the base plate.

## 11. Reproduction recipe
```css
:root{--void:#000;--alu:#acb7b3;--alu-2:#8c9794;--alu-shade:#57605e;--glass:#1c1e20;--lit:#eeeeee;--pin:#d9a441;
  --font:"Helvetica Now Text","Inter",system-ui,sans-serif;}
.key{background:linear-gradient(160deg,#b9c3bf,var(--alu) 40%,var(--alu-2));border-radius:6px;
  box-shadow:inset 0 1px 0 rgba(255,255,255,.5),0 6px 0 var(--alu-shade),0 10px 18px rgba(0,0,0,.6);
  transition:transform .2s cubic-bezier(.2,.9,.3,1),box-shadow .2s cubic-bezier(.2,.9,.3,1);
  font:400 30px/1 var(--font);color:var(--glass);display:flex;align-items:flex-end;padding:12px 16px}
.key:active{transform:translateY(6px);box-shadow:inset 0 1px 0 rgba(255,255,255,.15),0 0 0 var(--alu-shade),0 3px 6px rgba(0,0,0,.6)}
.display{background:var(--glass);color:var(--lit);border-radius:10px;box-shadow:inset 0 3px 8px #000;
  font:500 44px/1 var(--font);letter-spacing:.3em}
.display[data-state=ok]{background:var(--lit);color:var(--glass);font-size:26px;letter-spacing:.08em;text-transform:uppercase;
  animation:blink .8s steps(1) 1}
@keyframes blink{50%{background:var(--lit);color:transparent}}
.device.unlocked{animation:spin .77s cubic-bezier(.55,0,.85,.35) 1.1s}
@keyframes spin{to{transform:rotateY(360deg)}}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Restrained cool-alu palette, convincing grain and lighting, and a single gold accent. |
| Originality | 7 | "Physical object as UI state demo" is a known genre; the polarity-flip success state is a nice touch. |
| Usability | 7 | Clear length, masking and confirmation feedback, but no error state is shown. |
| Craft | 8 | Real key travel, chamfer highlights and a clean loop back to pose; the legends drift off a shared baseline. |

---
id: insp-isometric-ai-computer
source: inspora
category: Illustration
status: analyzed
title: "isometric AI computer"
creator: "R"
styles: [technical-wireframe, isometric, dark-premium, monochrome]
patterns: [figure-plate-frame, live-status-readout, typeable-illustration, isometric-hairline-object, crt-glow-screen, corner-caption-labels]
mode: dark
palette: ["#131313", "#272727", "#414141", "#6e6e6e", "#9a9a9a", "#ffffff"]
type_families: ["JetBrains Mono / Geist Mono-style monospace (likely)"]
type_class: [mono]
radius_px: [40, 24]
motion: {durations_s: [], easing: [], loop: true}
scores: {aesthetics: 8, originality: 8, usability: 7, craft: 9}
craft_signals: [single-hairline-weight-everywhere, only-screen-emits-light, status-footer-echoes-input, fig-number-caption, coiled-cable-detail, pressed-key-highlight, keyboard-shortcut-spacebar-glow]
anti_patterns: [secondary-labels-3-6-to-1, wireframe-strokes-1-8-to-1, uses-third-party-logo]
---
# isometric AI computer — R

## 1. Snapshot
- **Subject:** A 31 s, 1760×1454, 120 fps capture of an interactive illustration plate: an isometric, hairline-drawn compact vintage desktop computer (one-piece CRT unit on a base tray, separate keyboard, coiled cable). Its screen shows a glowing "A\" style mark and a `>` prompt that echoes what the viewer types.
- **Why it's remarkable:** The illustration is a working toy. Every real keypress lights the matching isometric key and appends to the CRT prompt, and a footer readout reports "on · 9 chars · key space". It is a technical figure that is also an input device.

## 2. Composition & layout
- **Plate:** a rounded panel (radius ≈40 px) inset ~48 px from the capture edges, like a figure in a technical paper.
- **Four corner labels at a ~52 px inset:**
  - "Fig 2" top-left;
  - "DESK COMPUTER" top-right;
  - "TYPE ON IT · CLICK IT TO SWITCH" bottom-left;
  - live state readout bottom-right.
- **Object:** The computer sits centred with its footprint spanning about x 390–1385 (≈57% of width) and y 235–1195. The isometric axis is a true 30° projection.
- **Negative space:** about 120 px above the object and 170 px below it before the captions. The object is optically centred slightly high.

## 3. Typography
- One monospace family throughout, close to JetBrains Mono or Geist Mono Regular.
- **Captions:** about 26 px source. "Fig 2" is in sentence case. The other labels are uppercase with tracking of about +0.15 em, and the footer is lowercase with "·" separators.
- **Screen prompt:** "> qwgu8kmc" in the same mono at about 16 px, skewed to the isometric screen plane.
- The mark on the screen (~75 px) is the only non-mono glyph.
- **Hierarchy by value only:** "Fig 2" and the footer state are bright (#bdbdbd/#9a9a9a), the descriptors dim (#6e6e6e).

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #131313 | plate fill and object fill (same value) | 94% |
| #272727 | plate edge, faces in shadow, screen glow halo | 5% |
| #414141 | hairline strokes | 0.5% |
| #6e6e6e | dim captions | — |
| #9a9a9a / #bdbdbd | status readout, fig number | — |
| #ffffff | screen logo, active key outline, prompt text | <0.1% |

WCAG checks:
- "Fig 2" (#bdbdbd on #131313) is 9.89:1.
- The footer status (#9a9a9a) is 6.6:1.
- "DESK COMPUTER" and the instruction (#6e6e6e) are **3.64:1**: AA-large only, at ~13 px CSS. Fails.
- Hairlines (#414141) are 1.82:1. The object is legible mostly through its many edges.
- The screen logo is white on a #272727 glow at 14.94:1.

## 5. Depth & material
- **Rendering:** Object faces are filled with the same #131313 as the plate, so form comes only from 1 px hairlines and from slight darkening on side faces (about #101010).
- **Light source:** The only emissive element is the CRT. A radial glow (~#2a2a2a centre fading out) sits inside an inset bezel with a double outline.
- **Shadow:** A very soft ambient shadow (~60 px blur) pools under the base tray.
- **Details:** vent slats, floppy slot, power LED dot, side ports, four screws on the tray, and a coiled cable drawn as ~20 overlapping ellipses. All are kept at the same stroke weight.

## 6. Components & patterns
- **Figure-plate frame:** a caption system (index, title, instruction, live state).
- **Keyboard:** about 60 keys. The pressed key (spacebar in the key frame) gets a white outline highlight.
- **Screen:** a prompt with a block cursor (visible in frames 8.62 s and 22.42 s), plus a boot "scanline" state at t=1.72 s where a white line sweeps across the mark.
- **Footer readout:** `on · {n} chars · key {name}`. It updates per keystroke, including "backspace" and "\\", so the plate doubles as a key-event visualiser.
- **"Click it to switch":** toggles power on/off (the footer prefix "on").

## 7. Motion
Measured values (`m0_motion.json`):
- Motion fraction is 0.00, mean energy is 0.02, and there are no segments above threshold. `seamless_loop_likely` is true.
- The camera and object never move. All change is tiny and local (characters, a lit key, the cursor), which the global energy metric does not register.

From the frames (estimate):
- The char count goes 0 → 5 → 14 → 20, then resets to 9 → 17 → 7 → 11 → 15 across 1.7–29.3 s. That is roughly one character every 0.4–0.7 s at human typing pace.
- The key highlight seems to last about one keypress (~100–150 ms).
- The boot sweep at 1.72 s suggests a short power-on scan animation.

## 8. Brand system
n/a — not a brand system. It features an AI-company-style "A\" mark on the CRT as subject matter, plus "Fig 2", which implies a series of technical figures.

## 9. UX
- **Strengths:** The instructions are explicit, and the live footer gives immediate feedback that input is registered even if the tiny screen text is hard to read. The direct mapping (physical key → drawn key) is delightful.
- **Risks:**
  - Dim captions fail AA.
  - Touch devices have no keyboard path unless a soft keyboard is triggered.
  - The screen text at ~16 px on a skewed plane is hard to read; the footer compensates.

## 10. Craft signals
- One stroke weight (~1 px) is used for every edge, from the tray to the cable coils.
- The fill colour of the object equals the plate background, giving a pure line-drawing look with occlusion.
- The CRT is the sole light source; nothing else glows.
- The pressed key gets a white outline rather than a fill change, consistent with the line-art language.
- The footer uses mid-dot separators and lowercase state words, distinct from the uppercase instructions.
- The screen text is correctly skewed onto the isometric screen plane.

## 11. Reproduction recipe
```css
:root{--plate:#131313;--edge:#272727;--line:#414141;--dim:#6e6e6e;--mid:#9a9a9a;--hi:#bdbdbd;--emit:#fff;
  --font:"JetBrains Mono","Geist Mono",ui-monospace,monospace}
.plate{background:var(--plate);border:1px solid var(--edge);border-radius:40px;padding:32px;display:grid;
  grid-template:"a . b" auto ". fig ." 1fr "c . d" auto / auto 1fr auto;font:400 13px/1 var(--font);color:var(--dim);letter-spacing:.15em}
.plate .a{color:var(--hi);letter-spacing:.02em}.plate .d{color:var(--mid);letter-spacing:.06em;text-transform:none}
svg.iso *{fill:var(--plate);stroke:var(--line);stroke-width:1;vector-effect:non-scaling-stroke}
svg.iso .key.is-down{stroke:var(--emit)}
.crt{fill:url(#glow)} /* radialGradient #2b2b2b -> #131313 */
```
JS: `addEventListener('keydown', e => { keyEl(e.code)?.classList.add('is-down'); buffer += e.key.length===1?e.key:''; status.textContent = \`on · ${buffer.length} chars · key ${e.key.toLowerCase()}\` })`. Remove `is-down` on keyup.

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Austere monochrome plate with one glowing screen; very cohesive. |
| Originality | 8 | An illustration that is literally typeable, with a live key readout, is a fresh idea. |
| Usability | 7 | Clear instructions and feedback; dim captions fail AA and touch is unsupported. |
| Craft | 9 | Consistent hairline weight, true isometric, precise micro-details (screws, coil, vents). |

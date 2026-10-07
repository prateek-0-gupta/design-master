---
id: insp-mechanical-macropad
source: inspora
category: 3D
status: analyzed
title: "mechanical macropad"
creator: "@skirano"
styles: [cinematic-3d, physical-material, monochrome, hairline-ui]
patterns: [exploded-view-assembly, turntable-orbit, layered-component-reveal, single-accent-internal-part, product-hero-loop]
mode: light
palette: ["#e8e8e8", "#d3d4d5", "#c6c7c9", "#b4b5b8", "#96999d", "#3b3c43", "#7466d6"]
type_families: ["Neo-grotesk (Söhne / Inter-like, likely)"]
type_class: [neo-grotesk]
radius_px: [80, 16, 9999]
motion: {durations_s: [3.3, 1.2, 1.2, 9.0], easing: [continuous-linear, ease-in-out], loop: true}
scores: {aesthetics: 9, originality: 7, usability: 7, craft: 9}
craft_signals: [purple-stems-as-only-colour, clear-and-opaque-keycap-mix, line-icon-legends, printed-plate-microcopy, layer-stagger-in-explode, soft-floor-shadow, black-hardware-accents]
anti_patterns: [plate-microcopy-illegible]
---
# mechanical macropad — @skirano

## 1. Snapshot
- **Subject:** A 9 s, 900×900 product render loop of a 3×4-ish macropad: white rounded tray, aluminium plate, 13 keys (mix of opaque white caps with line icons and clear caps), a black rotary knob, a white dial and a spring-loaded knob. It orbits, then explodes into layers (caps above, switches below) and reassembles.
- **Why it's remarkable:** An almost totally achromatic object where the only saturated colour is the violet switch stems. You see them through the clear caps when assembled and fully when exploded, so the reveal *is* the colour moment.

## 2. Composition & layout
- **Assembled (0.5–3.5 s):** The pad fills about 65% of the frame in three-quarter isometric view. The camera orbits about 90° between 0.5 s and 2.5 s, from a corner view to a near-top-down view at 1.5 s and back to the opposite corner.
- **Exploded (4.5–7.5 s):** The keycap layer lifts about 250–400 px above the switch layer. At 5.5–6.5 s the whole group shrinks to about 45% to fit the separated stack, and the camera pulls back.
- **Grid:**
  - About 4×3 keys at an about 70 px pitch in the 900 px frame, plus one 2u key (microphone icon).
  - A 4–5 px gap between caps.
  - The tray has an about 40 px rounded rim around the plate.

## 3. Typography
- **Plate copy:** Microcopy is printed on the plate edge in a small neo-grotesk (about 7–9 px in frame): a "Work Louder | OpenAI 2026" style collab mark, "You can just build things", "Let's build". It is set along the plate edges and rotated 90° on one side.
- **Legends:** Keycaps carry 1.25 px stroke line icons (microphone, check, plus, branch-arrow, flower/asterisk, bolt), centred at about 18 px. There are no letters.

## 4. Colour
| Hex | Role | Share (key) |
|---|---|---|
| #e8e8e8 | stage | 50% |
| #d3d4d5 / #c6c7c9 | tray, plate, white caps in shade | 32% |
| #b4b5b8 / #96999d | plate shadow, microcopy | 12% |
| #3b3c43 | switch housings, knob, standoffs | 5.4% |
| #7466d6 (est.) | switch stems (only chroma) | <1% |

WCAG checks:
- Icon #1f1f22 on keycap #f4f4f4: 14.95:1.
- Housings #3b3c43 on stage: 8.96:1.
- Plate microcopy #96999d on #e8e8e8: **2.33:1**. It is decorative and unreadable at size.
- Violet stem on housing: 2.41:1, so it separates by hue, not luminance.

## 5. Depth & material
- **Materials:** Five read clearly:
  - matte white ABS (tray and caps);
  - bead-blasted aluminium plate with a 1 px chamfer highlight;
  - frosted clear polycarbonate caps with refraction rings;
  - soft-touch black rubber (knob and feet);
  - knurled metal on the encoder (striped cylinder).
- **Lighting:** A soft high key from the top-left, a large diffuse floor shadow about 30 px offset with no hard edge, and ambient occlusion in the cap gaps.

## 6. Components & patterns
- **Exploded-view assembly:** caps, stems and the knob cap separate along Z with a stagger.
- **Turntable orbit:** shows all four sides.
- **Accent in the internals:** the colour is hidden inside and revealed through transparency.
- **Hardware details:** three status LEDs (small vertical bars) and a USB-C or jack hole at the left edge.

## 7. Motion
Measured profile: 9.0 s at 30 fps, `motion_fraction` 0.64, `seamless_loop_likely: true` (first_last_diff 0.26). Three segments, all `continuous/linear`:
- **0.13–3.43 s (3.3 s, peak 0.36):** the orbit. The camera move is steady with a slightly front-loaded energy.
- **3.97–5.17 s (1.2 s, peak 0.51):** the explode. The caps lift and the camera pulls back.
- **6.80–8.00 s (1.2 s, peak 0.40):** the reassemble.

The holds between segments (3.43–3.97 s and 5.17–6.80 s, about 0.5 s and 1.6 s) let the viewer read each state. The explode and assemble are symmetric at 1.2 s each, so the loop feels mechanical and balanced.

## 8. Brand system
n/a — not a brand system. Identity cues: the plate microcopy and collab line suggest a hardware brand collaboration. The monochrome-plus-violet palette and line-icon legends form a coherent product identity.

## 9. UX
- **As product communication:** The exploded view explains construction (hot-swap switches, clear caps) better than any spec sheet.
- **Legends:** The icon-only legends are elegant but ambiguous without software labelling.
- **Risk:** The printed microcopy is illegible at real scale.

## 10. Craft signals
- Violet (#7466d6-ish) is the only saturated hue in the frame, confined to the switch stems.
- Clear and opaque caps alternate in a checker-like rhythm, so the colour peeks through in a pattern.
- The legend icons share one stroke weight (about 1.25 px) and one size.
- Microcopy is set along the plate edges and rotated to follow the perimeter, like silkscreen.
- Black standoffs sit at the plate corners as hard punctuation in a soft white object.
- The explode lifts the cap layer as a unit while the knob caps fly further, giving depth ordering.

## 11. Reproduction recipe
```css
:root{--stage:#e8e8e8;--tray:#d3d4d5;--plate:#c6c7c9;--ink:#1f1f22;--hw:#3b3c43;--accent:#7466d6}
.pad{transform-style:preserve-3d;animation:orbit 3.3s linear both}
@keyframes orbit{from{transform:rotateX(55deg) rotateZ(-35deg)}to{transform:rotateX(55deg) rotateZ(55deg)}}
.caps{transition:transform 1.2s cubic-bezier(.4,0,.2,1)}
.exploded .caps{transform:translateZ(220px)}
.exploded .knob-cap{transform:translateZ(300px)}
.cap{border-radius:16px;background:linear-gradient(#fafafa,#e9e9ea);box-shadow:inset 0 -3px 0 rgba(0,0,0,.06)}
.cap.clear{background:rgba(255,255,255,.35);backdrop-filter:blur(2px)}
.stem{background:var(--accent)}
.tray{border-radius:80px;background:var(--tray);box-shadow:0 40px 60px -30px rgba(0,0,0,.25)}
```
In Three.js: use `MeshPhysicalMaterial({transmission:.9,roughness:.25})` for the clear caps, and an HDRI soft box for the high key.

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 9 | Disciplined white-on-white product photography with a single violet secret. |
| Originality | 7 | Exploded-view product loops are common, but colour-in-the-internals is a smart twist. |
| Usability | 7 | Clearly explains the build; the icon legends and microcopy are hard to read. |
| Craft | 9 | Material fidelity, consistent icon strokes and balanced 1.2 s explode/assemble. |

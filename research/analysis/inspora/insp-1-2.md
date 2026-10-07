---
id: insp-1-2
source: inspora
category: Motion
status: analyzed
title: "Jelly Slider"
creator: "@reczko_konrad"
styles: [soft-3d, physical-material, micro-interaction, cinematic-3d]
patterns: [jelly-slider-handle, recessed-track, translucent-material-thumb, refracted-value-readout, coloured-caustic-shadow, colour-per-state]
mode: light
palette: ["#d2d2d2", "#aaaaab", "#c1c2c5", "#333e5a", "#1d3891", "#97a3ae", "#61768f", "#454140"]
type_families: ["DIN / Barlow Condensed-style condensed grotesk (likely)"]
type_class: [condensed]
radius_px: [9999]
motion: {durations_s: [0.93, 0.9, 0.67, 2.2, 0.8, 0.6], easing: [ease-in-out, ease-out], loop: false}
scores: {aesthetics: 9, originality: 9, usability: 5, craft: 9}
craft_signals: [coloured-caustic-cast-shadow, value-text-refracted-through-gel, rim-light-on-thumb, recessed-track-inner-shadow, material-stretches-with-velocity, hue-swap-per-material]
anti_patterns: [value-unreadable-under-thumb, render-not-ui]
---
# Jelly Slider — @reczko_konrad

## 1. Snapshot
- **Subject:** A 1080×1080, 29.6 s rendered concept. A slider slot is cut into a matte grey surface, and the handle is a translucent jelly block that bends, arches out of the slot and stretches as it is dragged. The percentage label sits inside the track and is refracted through the gel.
- **Why it's remarkable:** The thumb is treated as a physical soft body with coloured transmission and caustic shadows. Its deformation encodes drag velocity, and its colour changes per variant (amber, magenta, blue).

## 2. Composition & layout
- **Track:** a slot centred horizontally, x≈140→945 (805 px, about 75% of the width) by y≈462→605 (143 px tall). It is a full stadium shape cut into the surface.
- **Value:** right-aligned inside the slot ("18%", "96%"), about 60 px cap height, with about 40 px right inset.
- **Thumb:** at rest it is a gel bar inside the slot (about 160 px wide). While dragging, it arches up out of the slot by up to about 200 px (frames at t=1.64–11.50 s), with a "tail" that remains in the slot. This forms a C or U shape.
- **Backdrop:** a seamless studio sweep, light top-left (#d2d2d2) to darker bottom-right (#aaaaab). Later in the video the scene darkens (#7a7a7a range from t≈18 s), like a light change.

## 3. Typography
- **Value:** a condensed grotesk (DIN Condensed or Barlow Condensed-like), regular, about 70 px. The "%" is smaller, at about 0.8× the digits.
- **Colour:** dark warm grey (#454140) on the track's grey interior.
- **Under the gel:** the digits are refracted and mirrored ("96%" appears reversed as "%69" in the key frame and tinted navy #091e57). The type becomes part of the material show.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #d2d2d2 / #c1c2c5 | surface (lit) | about 34% |
| #aaaaab / #b6b7b8 | surface (shade) | about 53% |
| #97a3ae / #61768f | blue-variant gel body | about 7% |
| #333e5a / #1d3891 | gel dense core (blue state) | about 6% |
| amber about #e07a2a, magenta about #e01a9a | other material variants | (other frames) |

WCAG checks:
- Value #454140 on the track interior #bebebc: 5.42:1 (pass).
- Refracted value #091e57 inside the blue gel #1d3891: **1.52:1**. The value is effectively unreadable when the thumb covers it (96% state).

## 5. Depth & material
- **Slot:** recessed, with a darker inner wall at the top, a bright bevel lip at the bottom and an inner shadow of about 10 px.
- **Gel:** translucent, with subsurface colour, a specular rim highlight on the top edge and a soft internal gradient (cloudy white to saturated).
- **Shadows:** coloured caustics. Light passing through the gel casts amber, magenta or blue streaks across the surface beneath, at about 45° toward the lower right and up to about 300 px long. This is the signature detail.

## 6. Components & patterns
- A slider with a soft-body thumb.
- A value readout inside the track that the thumb passes over.
- Material or colour variants of the same component (amber → magenta → blue), a theme-able "flavour".

## 7. Motion
- **Measured:** 29.6 s, 19 segments, `motion_fraction` 0.44, median 0.60 s. Most are symmetric ease-in-out (0.93, 0.90, 0.67, 2.20, 0.80, 0.60 s). Fast-start (ease-out) settles appear at 16.40 s (0.80 s), 18.77 s (0.93 s, `peak_at` 0.02) and 25.67 s (0.60 s).
- **Observed:**
  - While dragging, the gel lifts and arches, lagging behind the cursor, then rebounds into the slot. The settle times of about 0.6–0.9 s point to an underdamped spring.
  - The value text counts through intermediate numbers: 18→32→38%, then 96%, 54%, 82%.
  - At about 18 s a global lighting change darkens the backdrop.

## 8. Brand system
n/a — not a brand system.

## 9. UX
- As a real control it is expressive but problematic:
  - The thumb covers the readout.
  - The arched pose increases the visual footprint by about 2× the slot height.
  - Precision is unclear.
- Best used as a hero or marketing moment, or a single playful setting such as a "vibe" or mood control.

## 10. Craft signals
- Caustic shadow colour matches the gel colour in every variant.
- The readout is distorted by the gel (refraction and mirroring), which proves it is a real material, not an overlay.
- The specular rim highlight follows the arch curvature.
- The slot's lip bevel is lit on the lower edge and shadowed on the upper inner wall, consistent with a top-left light.
- The backdrop sweep has no visible horizon, a seamless studio look.

## 11. Reproduction recipe
```css
:root{--surface:#d0d0d1;--surface-2:#aaaaab;--ink:#454140;--gel:#2b4bd8}
.stage{background:linear-gradient(135deg,var(--surface),var(--surface-2))}
.slot{width:805px;height:143px;border-radius:9999px;background:#bdbdbc;
  box-shadow:inset 0 12px 18px rgba(0,0,0,.35), 0 2px 0 rgba(255,255,255,.7)}
.slot .value{font:400 70px/1 "Barlow Condensed",sans-serif;color:var(--ink);position:absolute;right:40px}
.thumb{height:100%;border-radius:inherit;
  background:linear-gradient(180deg,rgba(255,255,255,.75),color-mix(in srgb,var(--gel) 70%,transparent));
  backdrop-filter:blur(2px) saturate(1.4);box-shadow:inset 0 2px 0 rgba(255,255,255,.9),0 30px 40px -10px color-mix(in srgb,var(--gel) 45%,transparent);
  transition:transform .6s cubic-bezier(.34,1.56,.64,1)} /* overshoot spring */
.thumb.dragging{transform:translateY(-35%) scaleY(1.4) skewX(-8deg)}
```
A real soft-body arch needs WebGL or a Three.js mesh with vertex displacement by drag velocity.

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 9 | Gorgeous material rendering and lighting. |
| Originality | 9 | The soft-body arching thumb with caustics is novel. |
| Usability | 5 | The readout is hidden and illegible under the gel; oversized footprint. |
| Craft | 9 | Physically coherent light, refraction and spring motion. |

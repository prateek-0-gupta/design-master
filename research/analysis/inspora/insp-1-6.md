---
id: insp-1-6
source: inspora
category: Motion
status: analyzed
title: "Liquid Glass"
creator: "@chan_k"
styles: [glassmorphism, cinematic-3d, physical-material, spatial-ui]
patterns: [liquid-glass-lens-material, refracting-toggle-thumb, glass-slider-knob, morphing-pill-to-menu, adaptive-glass-over-light-dark, component-sheet-on-grid-floor, tab-bar-glass-capsule]
mode: light
palette: ["#d9d9e4", "#b0b1bb", "#9a9aa6", "#69c071", "#1b8fd8", "#111111", "#3a3b40", "#f2b21a"]
type_families: ["SF Pro Display/Text (likely)"]
type_class: [neo-grotesk]
radius_px: [9999, 64]
motion: {durations_s: [4.63, 1.83, 2.6, 5.13, 1.63, 0.63], easing: [ease-in-out, ease-out, ease-in, linear], loop: false}
scores: {aesthetics: 9, originality: 7, usability: 6, craft: 9}
craft_signals: [edge-refraction-bends-track-under-lens, chromatic-fringe-on-rim, specular-rim-highlight-top-edge, lens-magnifies-content-beneath, depth-of-field-rack-focus, glass-tint-adapts-to-backdrop-luminance, consistent-capsule-geometry-across-components]
anti_patterns: [white-on-green-knob-unreadable-if-labelled, glass-legibility-depends-on-backdrop]
---
# Liquid Glass — @chan_k

## 1. Snapshot
- **Subject:** A 42 s, 1528×1080 cinematic 3D study of an Apple-style "Liquid Glass" component set: a capsule toolbar (+ / ○ / ‹), a morphing menu (One–Four), a refracting toggle and slider, a tab bar with a compose button, and a final layout of every component on a grid floor.
- **Why it's remarkable:** It shows the material's physics, not just a blur. Lenses refract and magnify what is beneath them (the slider track bends inside the knob, and the toggle's green fill warps under the thumb), and edges carry chromatic fringes.

## 2. Composition & layout
- **Shots:** Each is a single hero component, centred and filling 50–70% of the 1528 px width. Most are shot slightly from above with shallow depth of field.
- **Toggle (key frame):** The toggle track spans the frame (≈1320×660 px with a full radius). The glass thumb is about 810×500, deliberately oversized so the refraction reads.
- **Menu (7.06 s):** A rounded-square menu of about 260×330 px with four rows at about 77 px pitch, icons at x≈895 and labels at x≈940.
- **Finale (35–40 s):** An isometric "component sheet" of seven objects on a light-grey floor with a 1 px grid at about 60 px pitch, set up like a product spec photo.

## 3. Typography
- An SF Pro-like grotesk, medium weight, for the menu labels "One / Two / Three / Four" (about 30 px cap-to-baseline, roughly 36 px type). The labels are tightly tracked, near-black #111.
- **Icons:** stroke glyphs at about 3 px weight (circle, triangle, square, hexagon, plus, chevron), matched to the text's stem weight.
- There is very little text; type is used only to prove legibility through glass.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #d9d9e4 / #c6c6d2 | studio backdrop highlight, glass body | ~27% |
| #b0b1bb / #9a9aa6 | backdrop falloff, shadow | ~55% |
| #69c071 / #7ed287 / #57a65e | toggle "on" fill | ~15% (key) |
| #1b8fd8 (approx) | slider fill | scene |
| #3a3b40 (approx) | dark backdrop band (adaptive test, 11.76 s) | scene |
| #111111 | glyphs and labels | <1% |
| #f2b21a (approx) | yellow wallpaper blob behind toolbar (16.46 s) | scene |

WCAG checks:
- #111 on the glass at #d9d9e4 is 13.48:1. On the darkest backdrop grey (#9a9aa6) it is still 6.79:1, so dark glyphs survive the tint range.
- White on the toggle green is only 2.24:1, so labels on that fill would fail.

## 5. Depth & material
This is the subject of the piece:
- **Refraction:** The thumb behaves like a thick convex lens. The green fill and the slider track bend outward at the rim and are magnified about 1.1× in the centre (the blue track becomes a curved "U" inside the knob at 25.87 s).
- **Rim:** a bright specular line along the top edge, with a thin rainbow fringe (chromatic aberration) at the left and bottom curves.
- **Frost:** the body has a light frosted blur (the 2.35 s plus sign is heavily blurred through the capsule edge), with a soft contact shadow beneath.
- **Adaptive tint (11.76 s):** as a dark band rises behind the lens, the glass picks up the darker backdrop and stays legible, the "adaptive" behaviour of the material.
- **Camera:** depth of field racks between foreground glyphs and glass (2.35 s opening is out of focus, then resolves).

## 6. Components & patterns
- **Toolbar capsule** with + / ○ / ‹ actions, which morphs into a vertical menu (One–Four) and back.
- **Toggle:** a glass thumb over a green track, with the thumb larger than the track height.
- **Slider:** a glass lens knob over a coloured fill, including a hue-spectrum slider in the finale.
- **Tab-bar container:** a large rounded panel (≈64 px radius) with a cloud tab and a circular compose button (30.57 s).
- **Floating circular "+" button** and an empty capsule well.

## 7. Motion
Measured: 42.33 s at 30 fps, 23 segments, motion fraction 0.60 (motion-heavy), median segment 0.63 s, not a loop.
- **Slow camera moves:** 0.10–4.73 s (4.63 s, symmetric ease-in-out) is the opening rack focus and dolly. 24.37–29.50 s (5.13 s, peak 0.77 → ease-in) is a long slider-knob drag that accelerates.
- **Component morphs:** 6.97–8.80 s (1.83 s, peak 0.06 → strong ease-out) is the capsule-to-menu expansion, a fast spring-like start that settles slowly. 8.90–10.17 s (1.27 s, ease-out) is the collapse.
- **Linear segments:** 21.17–22.80 (1.63 s), 33.93–35.07 and 37.20–38.53 s are steady camera pans across the component sheet.
- **Short interactions:** 0.17–0.40 s taps at the end (40–41.8 s).
- Overall rhythm: long, eased hero moves interleaved with sub-second state changes.

## 8. Brand system
n/a — not a brand system. Identity cues: a faithful riff on Apple's 2025 Liquid Glass language (capsules, SF glyphs, iOS-green toggle, tab bar with a separate circular action).

## 9. UX
- **Strengths:** Clearly shows that controls remain distinguishable over varied content. Morphing from capsule to menu keeps spatial continuity.
- **Risks:** Real glass legibility depends on the backdrop. The demos use controlled, low-detail studio backdrops, and the 16.46 s shot over a busy yellow/blue image shows the chevron being swallowed by the yellow refraction. Exaggerated refraction would be distracting at real UI sizes.

## 10. Craft signals
- The track visibly bends at the lens rim (the edge displacement is stronger than the centre magnification).
- Chromatic fringes appear only at high-curvature corners, not along flat edges.
- There is a specular highlight on the top-right rim plus a darker refracted band at the bottom: a consistent single light source from above.
- Every component shares the capsule radius family (full-round ends, ≈64 px panel corners).
- The finale grid floor gives scale reference and shows the contact shadows.
- Glyph stroke weight (≈3 px) matches the medium text stems.

## 11. Reproduction recipe
```css
/* Approximation: true refraction needs SVG displacement or WebGL */
:root{--glass-tint:rgba(255,255,255,.18);--rim:rgba(255,255,255,.85);--ink:#111;--on:#69c071;}
.glass{border-radius:9999px;background:var(--glass-tint);
  backdrop-filter:blur(2px) saturate(1.4) url(#lens);   /* Chrome supports url() filters on backdrop in some builds */
  box-shadow:inset 0 1.5px 0 var(--rim), inset 0 -8px 16px rgba(0,0,0,.08),
             inset 2px 0 0 rgba(255,80,200,.25), inset -2px 0 0 rgba(80,200,255,.25), /* chromatic fringe */
             0 12px 30px rgba(0,0,0,.12);}
.toggle{width:132px;height:66px;border-radius:9999px;background:#e9e9ef}
.toggle[aria-checked=true]{background:var(--on)}
.toggle .thumb{position:absolute;inset:-10px auto -10px 40px;width:90px;transition:transform .55s cubic-bezier(.2,1.4,.4,1)}
.menu{transition:width .6s cubic-bezier(.16,1,.3,1),height .6s cubic-bezier(.16,1,.3,1),border-radius .6s}
```
```html
<svg width="0" height="0"><filter id="lens"><feTurbulence type="fractalNoise" baseFrequency="0.002" result="n"/>
<feDisplacementMap in="SourceGraphic" in2="n" scale="40" xChannelSelector="R" yChannelSelector="G"/></filter></svg>
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 9 | Studio lighting, refraction and DOF make the material feel tangible and premium. |
| Originality | 7 | A high-fidelity interpretation of Apple's existing language rather than a new idea. |
| Usability | 6 | It demonstrates state changes well, but glass legibility over busy content is shown to be fragile. |
| Craft | 9 | Consistent light source, rim fringes, refraction physics and geometry family. |

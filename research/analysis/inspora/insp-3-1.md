---
id: insp-3-1
source: inspora
category: 3D
status: analyzed
title: "Boat loader"
creator: "@reijowrites"
styles: [physical-material, soft-3d, playful-rounded]
patterns: [3d-mascot-loader, determinate-progress-bar, object-rides-progress, infinite-scroll-terrain, rocking-idle-motion]
mode: light
palette: ["#e2e4e3", "#84a3d1", "#b4c4d7", "#e4dac9", "#6e6a92", "#c9cbcb"]
type_families: []
type_class: []
radius_px: [9999]
motion: {durations_s: [10.0, 0.17], easing: [continuous-linear, ease-in], loop: true}
scores: {aesthetics: 8, originality: 7, usability: 6, craft: 8}
craft_signals: [felt-texture-on-waves, wood-grain-hull, soft-contact-shadow, boat-tilts-with-wave-phase, progress-bar-pill-caps, warm-cool-material-pairing]
anti_patterns: [illustration-and-progress-disconnected, low-contrast-track]
---
# Boat loader — @reijowrites

## 1. Snapshot
- **Subject:** A 10 s, 1920×1440 render of a toy wooden sailboat bobbing along a short strip of felt-textured blue waves. Under it is a thin determinate progress bar that fills over the clip.
- **Why it's remarkable:** It turns a loading bar into a tactile tabletop toy. The wave strip is the same proportion as the bar, so the scene reads as a 3D echo of the progress track.

## 2. Composition & layout
- **Placement:** The scene sits in the upper-middle of a flat #e2e4e3 field.
  - The wave block is about 700×170 px, centred near y≈700.
  - The sail peaks at about y≈330.
  - The progress bar sits at y≈870, about 390 px wide (x≈765→1155), so it is narrower than the waves and centred under them.
- **Boat position:** The boat travels along the strip and its x-position wanders over the frames: left at 0.56 s, right at 5.0 s, centre-left at 9.44 s. The strip itself also shifts, so the camera is not locked on either object.
- **Negative space:** About 95% empty, which matches a full-screen splash.

## 3. Typography
None: there is no copy, percentage or label. The progress bar is the only UI element.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #e2e4e3 | cool grey stage | 95.5% |
| #84a3d1 | wave felt (mid) | 1.9% |
| #b4c4d7 | wave highlights / fibre | 1.5% |
| #e4dac9 | birch hull, sail | 1.1% |
| #6e6a92 | progress fill (dusty violet) | <0.2% |
| #c9cbcb | progress track | <0.2% |

WCAG checks (non-text, 3:1 target):
- Fill on stage: 3.97:1 (pass).
- Fill against track: 3.11:1 (pass).
- Track on stage: **1.28:1**, so the empty part of the bar is near-invisible.
- The waves sit at 2.02:1 on the stage and stand out mainly through hue.

Colour strategy: a warm wood/linen object on cool felt over neutral grey. The violet fill is the only "UI" colour and is cooler and darker than everything else.

## 5. Depth & material
- **Waves:** Extruded sine-profile slabs, about 4 layers deep, with a fuzzy felt or flocked texture. Visible fibres and darker troughs (#5f86c4-ish) give an ambient-occlusion feel.
- **Hull and sail:** The hull is turned birch with a visible end-grain ring pattern. The sail is a matte paper or linen triangle on a dowel mast.
- **Light:** Soft studio lighting from the upper-left. The boat drops a faint contact shadow onto the felt. There is no environment reflection, so it reads as a matte toy.

## 6. Components & patterns
- **Determinate progress bar:** about 6 px tall with round caps. The fill grows left to right: about 4% at 0.56 s, about 50% at the key frame, about 98% at 9.44 s.
- **Mascot loader:** the 3D scene sits above the bar as emotional reassurance.
- **Terrain loop:** the felt strip appears to translate under the boat, which reads as forward travel.

## 7. Motion
Measured profile:
- 10.0 s at 30 fps.
- `motion_fraction` 0.03 and mean energy 0.18: almost all motion is below threshold, meaning slow, continuous drift.
- Only one detected segment: **9.13–9.30 s (0.17 s, peak_at 0.90, ease-in)**. This is likely the loop reset or the boat dipping at the end.
- `seamless_loop_likely: true` (first_last_diff 0.41).

Estimated from frames:
- The bar fills roughly linearly at about 10%/s (4% at 0.56 s, 50% at about 5 s, 98% at 9.44 s).
- The boat pitches about ±10°: bow up at 3.89 s, leaning right at 5.0 s.
- It rises and falls about 20 px with a wave period of roughly 2–2.5 s, in sinusoidal ease-in-out.

## 8. Brand system
n/a — not a brand system. Identity cues: a handcrafted-toy art direction (felt + birch) that would suit a calm, family or travel-oriented brand.

## 9. UX
- **Strengths:** A real determinate bar, and the soothing motion lowers perceived wait.
- **Risks:**
  - The boat's travel does not map to the bar's percentage, so the two progress metaphors compete.
  - There is no numeric or text status.
  - The track at 1.28:1 hides the remaining length.
  - Heavy 3D is costly to ship as a loader unless it is pre-rendered video or Lottie.

## 10. Craft signals
- The felt texture has fibre-level noise and darker crests at each wave trough.
- The wood hull shows concentric grain on the bow end.
- The boat pitch follows the wave phase rather than a fixed rock.
- The progress bar has fully round caps on both track and fill (radius = height / 2).
- The stage colour is a slightly cool #e2e4e3 rather than pure grey, which harmonises with the blue.

## 11. Reproduction recipe
```css
:root{--stage:#e2e4e3;--track:#c9cbcb;--fill:#6e6a92;--felt:#84a3d1;--birch:#e4dac9}
body{background:var(--stage)}
.progress{width:390px;height:6px;border-radius:9999px;background:var(--track);overflow:hidden}
.progress>i{display:block;height:100%;border-radius:inherit;background:var(--fill);
  width:var(--p);transition:width .3s linear}
.boat{animation:bob 2.4s ease-in-out infinite}
@keyframes bob{0%,100%{transform:translateY(0) rotate(-6deg)}50%{transform:translateY(-20px) rotate(8deg)}}
.waves{background:url(felt-waves.webp) repeat-x;animation:slide 10s linear infinite}
@keyframes slide{to{background-position:-700px 0}}
```
Darken the track to about #b3b6b6 to reach 1.6:1 or more and make the remaining length legible.

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Gorgeous material pairing (felt and birch) with a calm, neutral stage. |
| Originality | 7 | A 3D mascot over a bar is known, but the felt-toy treatment is fresh. |
| Usability | 6 | Determinate and calm, but the boat's travel is decoupled from progress and the track is faint. |
| Craft | 8 | Texture fidelity, phase-matched rocking and clean pill bar. |

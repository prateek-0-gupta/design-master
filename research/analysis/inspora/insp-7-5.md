---
id: insp-7-5
source: inspora
category: Motion
status: analyzed
title: "Folder interaction"
creator: "@raul_dronca"
styles: [soft-3d, monochrome, micro-interaction, physical-material]
patterns: [hover-fan-out-preview, folder-front-tilt, floating-object-ground-shadow, skeleton-card-thumbnails, press-to-tuck, window-zoom-intro]
mode: light
palette: ["#e0e0e0", "#232323", "#313131", "#fdfdfd", "#c9c9c9", "#767676"]
type_families: []
type_class: []
radius_px: [40, 20, 9999]
motion: {durations_s: [0.43, 0.5, 0.3, 0.5, 0.27, 0.53], easing: [ease-out, ease-in-out], loop: true}
scores: {aesthetics: 8, originality: 7, usability: 7, craft: 8}
craft_signals: [detached-contact-shadow-implies-hover, front-panel-perspective-flatten, cards-fan-with-alternating-rotation, translucent-front-blurs-cards-behind, skeleton-lines-at-low-contrast, cursor-changes-to-pointer-on-press]
anti_patterns: [card-edges-1.3-to-1-on-canvas]
---
# Folder interaction — @raul_dronca

## 1. Snapshot
- **Subject:** A 13.2 s, 1920×1264 clip of a single dark, soft-3D folder or tray icon floating on light grey. On hover its front panel tips forward and three white document cards fan out above it. On press the cards tuck back in.
- **Why it's remarkable:** A desktop folder icon is reimagined as a physical letter tray with a frosted front. The hover preview is a real "peek inside" rather than a scale-up.

## 2. Composition & layout
- **Object:** a single centred object of about 420×330 px (resting) on a #e0e0e0 canvas that fills 92% of the frame.
- **Ground shadow:** a separate soft ellipse about 170 px below the object, roughly 500×40 px. The object is levitating, not resting.
- **Hover state:**
  - The cards spread to about 830 px total width across the top (each about 330×280 px).
  - The tray front drops and shortens to about 420×130 px.
  - The back panel is revealed as a flat black rectangle.
- **Bookends:** At 0.73 s and 12.47 s the scene is framed inside a rounded window (radius about 40 px) on a dark gradient. The camera zooms from the window into the object and back, which presents the clip as an app-in-OS demo.

## 3. Typography
None. The cards use skeleton placeholders instead of text: pill bars about 14 px tall in #e6e6e8, a 50 px avatar circle and an image block. That keeps the focus on motion.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #e0e0e0 | canvas | 92% |
| #232323 / #313131 | tray body, back panel | 2% |
| #767676 → #c9c9c9 | front-panel gradient highlight | 1.5% |
| #fdfdfd | document cards | 0.8% |
| #e6e6e8 (est.) | skeleton lines | <0.5% |

WCAG checks (non-text):
- The tray #232323 on #e0e0e0 is 11.91:1, so the object reads instantly.
- Cards #fdfdfd on #e0e0e0 are only 1.3:1; their edges rely on a soft shadow.
- Skeleton lines on cards are 1.23:1, decorative by design.

The scene is strictly achromatic.

## 5. Depth & material
- **Tray front:** a translucent smoked-acrylic material. The top half shows the card behind it blurred through the panel (gradient #767676 → #3a3a3a), and there is a crisp dark lip at the bottom.
- **Back panel:** opaque matte black with a subtle radial highlight.
- **Shadows:**
  - Every card has a soft, 20–30 px blurred shadow at about 8% opacity.
  - The tray has a darker close shadow, about 30 px.
  - The detached ground ellipse grows slightly when the tray rises.
- **Card radius:** about 20 px. Tray radius about 36 px on top, tapering in perspective at the bottom.

## 6. Components & patterns
- **Folder icon with content preview on hover:** three cards fan out with rotations of about −6°, 0° and +6°, overlapping in z-order left < centre < right.
- **Press state:** the cards slide back down into the tray and the front panel returns upright. The cursor switches to a hand at 11.0 s.
- Usable as a "Files" or "Collections" entry point in a launcher or dock.

## 7. Motion
Measured (m0_motion.json, 30 fps, 13.2 s, motion_fraction 0.19, seamless_loop_likely true). Six segments:
- **0.67–1.10 s (0.43 s, peak 0.35):** ease-out, the window-to-object zoom.
- **3.40–3.90 s (0.50 s, peak 0.63):** ease-in-out, the hover fan-out.
- **5.37–5.67 s (0.30 s, peak 0.28):** ease-out, the cards collapse on hover-out.
- **7.60–8.10 s (0.50 s, peak 0.63):** the second fan-out, the same 0.50 s profile as the first. This is a consistent token.
- **10.80–11.07 s (0.27 s, peak 0.19):** ease-out, the press-to-tuck.
- **12.10–12.63 s (0.53 s, peak 0.28):** zoom back out to the window.

Pattern: the open is 0.50 s symmetric, while close and press are 0.27–0.30 s fast-start. Revealing is slower than dismissing, which is the right asymmetry. The cards appear to stagger by about 40–60 ms left → right (estimate, from 3.67 s, where the right card is still rising).

## 8. Brand system
n/a — this is an icon/interaction study, not a brand system. Identity cues: a monochrome "smoked acrylic" object language.

## 9. UX
- The hover preview reduces uncertainty about a folder's contents before a click.
- **Risks:**
  - On touch there is no hover, so it needs a long-press or a static badge.
  - The white cards nearly vanish on the grey canvas (1.3:1) and are carried only by shadow.
  - A three-card fan caps the preview at three items.

## 10. Craft signals
- The detached ground shadow sits about 170 px below the object, so the tray reads as hovering in space.
- When the front panel tilts, its top edge foreshortens and the bottom stays anchored, a correct hinge-at-base perspective.
- The card behind the front panel is shown frosted, not hidden, so the material is consistent.
- The open/close asymmetry is 0.50 s vs 0.27–0.30 s, as measured.
- Fanned cards alternate rotation sign and overlap with right-on-top z-order.
- A pointer cursor appears only at the press moment.

## 11. Reproduction recipe
```css
:root{--bg:#e0e0e0;--tray:#232323;--card:#fdfdfd;--skel:#e6e6e8;
  --open:.5s cubic-bezier(.45,0,.35,1);--close:.28s cubic-bezier(.2,.8,.2,1)}
.folder{position:relative;width:210px;height:165px;perspective:800px}
.folder .back{position:absolute;inset:0 18px 30px;border-radius:18px;background:radial-gradient(circle at 50% 20%,#2a2a2a,#111)}
.folder .front{position:absolute;inset:auto 0 0;height:110px;border-radius:18px;transform-origin:bottom;
  background:linear-gradient(180deg,rgba(120,120,120,.85),#2a2a2a 70%);backdrop-filter:blur(8px);
  box-shadow:0 18px 30px rgba(0,0,0,.25);transition:transform var(--close)}
.folder .card{position:absolute;left:50%;top:10px;width:165px;height:140px;border-radius:10px;background:var(--card);
  box-shadow:0 10px 30px rgba(0,0,0,.08);translate:-50% 0;transition:transform var(--close)}
.folder:hover .front{transform:rotateX(-28deg) scaleY(.75);transition:transform var(--open)}
.folder:hover .card:nth-child(1){transform:translate(-120px,-120px) rotate(-6deg);transition:transform var(--open)}
.folder:hover .card:nth-child(2){transform:translate(0,-130px);transition:transform var(--open) 40ms}
.folder:hover .card:nth-child(3){transform:translate(120px,-120px) rotate(6deg);transition:transform var(--open) 80ms}
.folder::after{content:"";position:absolute;left:10%;right:10%;bottom:-90px;height:20px;border-radius:50%;
  background:rgba(0,0,0,.12);filter:blur(12px)}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Calm achromatic product-shot quality; material rendering is convincing. |
| Originality | 7 | Fan-out folders exist; smoked-acrylic tray + floating shadow is a fresh take. |
| Usability | 7 | Hover preview is genuinely informative; hover-dependence and faint cards limit it. |
| Craft | 8 | Correct hinge perspective, consistent 0.50 s/0.28 s timing tokens, frosted occlusion. |

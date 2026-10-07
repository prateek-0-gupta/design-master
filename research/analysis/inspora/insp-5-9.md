---
id: insp-5-9
source: inspora
category: Motion
status: analyzed
title: "Motion blur"
creator: "@lucchaissac"
styles: [cinematic-3d, photo-led, physical-material, grain-noise]
patterns: [tilt-shift-envelope-scene, theme-toggle-pill, hover-swap-stamp-art, perforated-stamp-edge, circular-postmark-type, share-cta-pill]
mode: mixed
palette: ["#1c1c1c", "#161616", "#e6e3de", "#1935d6", "#ae2960", "#563458", "#010101"]
type_families: ["Neue Haas / Helvetica Now-style grotesk (likely)", "Japanese gothic (handwritten-style kana, likely)"]
type_class: [grotesk]
radius_px: [9999]
motion: {durations_s: [0.17], easing: [ease-in], loop: false}
scores: {aesthetics: 9, originality: 8, usability: 6, craft: 8}
craft_signals: [shallow-depth-of-field-on-ui, perforated-stamp-mask, postmark-text-on-circular-path, same-scene-two-paper-colours, saturated-art-only-on-stamp, cobalt-share-pill]
anti_patterns: [theme-toggle-label-shows-opposite-state, blurred-content-unreadable]
---
# Motion blur — @lucchaissac

## 1. Snapshot
- **Subject:** A 9.9 s, 1688×1470 (60 fps) scene. An envelope is photographed at a steep angle with strong depth-of-field blur, and carries a "26 Lovable" postage stamp and a circular "My Lovable Journey" postmark.
  - A "Dark/Light" pill toggles the envelope paper between cream (#e6e3de) and black (#1c1c1c).
  - Hovering the stamp swaps its gradient artwork (streaks, then petals, then rays).
  - A cobalt "Share" pill sits at the top-right.
- **Why it's remarkable:** UI chrome sits on top of what reads as a macro photograph. Focus falloff ("motion blur" or tilt-shift) directs the eye to the stamp.

## 2. Composition & layout
- **Diagonal:** The envelope edge runs from about the bottom-left to the top-right at about 30°, and the right portion falls into blur.
- **Stamp:** In sharp focus at about x 860→1280, y 300→820. The postmark rings overlap its left edge.
- **Text:** "Lovable Post Services" is set on the rotated baseline, and the Japanese "…みんなへ" ("to everyone") is handwritten-style near the bottom, blurred.
- **Overlay chrome:**
  - Toggle pill about 190×100 px at the top-left (inset about 30 px).
  - Share pill about 200×100 px at the top-right (inset about 30 px).

## 3. Typography
- **Chrome:** Bold grotesk at about 34 px ("Light", "Share").
- **Postmark and labels:** Wide uppercase grotesk set on circular paths ("BUILD SOMETHING LOVABLE", "STHLM", "2026").
- **Stamp numeral:** "26" in heavy italic grotesk, about 110 px in perspective, with the Lovable wordmark.
- **Kana:** A brush-like Japanese face, heavily defocused.

## 4. Colour
| Hex | Role |
|---|---|
| #1c1c1c / #161616 | dark-mode envelope / background |
| #e6e3de | light-mode envelope paper |
| #ae2960 / #563458 | stamp gradient (magenta, plum) plus blue and orange |
| #1935d6 | Share CTA |
| #010101 | toggle pill |

WCAG:
- White on #1935d6 is 8.33:1.
- Toggle label #adadad on #010101 is 9.3:1.
- Postmark ink on paper (#1c1c1c on #e6e3de) is 13.31:1 when in focus.

## 5. Depth & material
- **Depth:** It is all depth of field. Content more than about 300 px from the focal plane is Gaussian-blurred progressively (the envelope's far right and the kana).
- **Paper:** A fine grain.
- **Stamp:** A die-cut perforated edge with a white border and a slight emboss.
- **Dark mode:** It turns the envelope black while the postmark lines go light grey, the same art inverted rather than re-shot.

## 6. Components & patterns
- **Theme toggle pill:** Its label shows the *target* mode. It reads "Dark" while light is shown and "Light" while dark is shown, which is an ambiguous convention.
- **Hover-swap stamp:** Three artworks were observed (horizontal streaks at 0.55–3.84 s, petals at 6.04 s, rays from 7.13 s).
- A primary Share CTA.

## 7. Motion
- **Measured:** Only one segment crosses the threshold (threshold 0.74 at 60 fps): 5.33–5.50 s, 0.17 s, peak 0.90 (ease-in). That is the theme flip. motion_fraction is 0.10 and `seamless_loop_likely: false`.
- **Frames (estimate):**
  - Light to dark occurs between t=3.84 s and 4.94 s, as a fast whole-scene cut or crossfade.
  - The stamp art changes between 4.94 and 6.04 s and between 6.04 and 7.13 s, below the energy threshold, so they are likely soft crossfades.
  - Dark back to light at about 9.3 s.
- **Read:** Quick 170 ms state flips. The cursor shows the stamp art responding to hover.

## 8. Brand system
n/a — not a brand system, but Lovable cues are clear: the heart glyph, the "Build something lovable" postmark and the pink-orange-blue gradient. The postal metaphor is used for a year-in-review or "journey" share card.

## 9. UX
- The share flow is obvious (a single cobalt CTA).
- **Risks:**
  - The toggle label semantics are inverted.
  - Most text is intentionally unreadable through blur.
  - The perspective makes the stamp the only legible target, which is fine for a share card but not for content.

## 10. Craft signals
- Perforation teeth are evenly spaced (about 18 px) and follow perspective.
- Postmark type runs on concentric circular paths at two radii.
- The same composition is rendered on two paper colours, and only ink and paper invert. The stamp stays identical.
- Saturated colour appears only inside the stamp. The rest is achromatic, plus one cobalt CTA.
- The focus falloff is graded rather than a hard two-zone blur.

## 11. Reproduction recipe
```css
:root{--paper:#e6e3de;--ink:#1c1c1c;--cta:#1935d6}
[data-theme=dark]{--paper:#1c1c1c;--ink:#e6e3de}
.scene{perspective:1400px;background:#161616}
.envelope{background:var(--paper);color:var(--ink);transform:rotateX(52deg) rotateZ(-30deg) scale(1.6);
  transition:background .17s ease-in,color .17s ease-in}
.dof{-webkit-mask:linear-gradient(120deg,#000 35%,transparent 70%);backdrop-filter:blur(14px)} /* overlay for falloff */
.stamp{--t:9px;-webkit-mask:radial-gradient(circle at 50% 50%,#000 60%,transparent 62%) 0 0/18px 18px round,
  linear-gradient(#000 0 0) center/calc(100% - 18px) calc(100% - 18px) no-repeat;border:10px solid #fff}
.pill{border-radius:9999px;padding:28px 44px;font:700 34px/1 "Helvetica Now Display",sans-serif}
.pill--cta{background:var(--cta);color:#fff}.pill--toggle{background:#010101;color:#adadad}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 9 | Photographic depth, a perfect stamp detail and a disciplined palette. |
| Originality | 8 | Depth of field on an interactive UI share card is unusual and striking. |
| Usability | 6 | The toggle semantics are ambiguous and much content is deliberately illegible. |
| Craft | 8 | Perforation, circular type and dual theming are precise; the effects are subtle. |

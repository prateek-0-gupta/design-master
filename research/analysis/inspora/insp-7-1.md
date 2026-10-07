---
id: insp-7-1
source: inspora
category: Motion
status: analyzed
title: "Button motion"
creator: "Brett (@BrettFromDJ)"
styles: [dark-premium, skeuomorphic, physical-material, micro-interaction]
patterns: [iridescent-rim-sweep, nested-bezel-button, pill-tray-end-cap, idle-ambient-animation, extruded-glyph-icon]
mode: dark
palette: ["#181818", "#2b2b2b", "#222222", "#575959", "#333737", "#5a5a5a"]
type_families: []
type_class: []
radius_px: [9999]
motion: {durations_s: [12.23], easing: [linear], loop: true}
scores: {aesthetics: 8, originality: 7, usability: 5, craft: 8}
craft_signals: [thin-film-iridescent-rim, double-bezel-ring, hairline-tray-outline, soft-drop-shadow-under-button, glyph-top-to-bottom-gradient, near-black-tonal-steps]
anti_patterns: [icon-contrast-below-3-to-1, no-visible-state-change]
---
# Button motion — Brett (@BrettFromDJ)

## 1. Snapshot
- **Subject:** A 12.2 s, 1920×1364 loop of one dark circular "bookmark" button seated at the rounded end of a pill tray. Its outer rim carries a slowly travelling oil-slick iridescent highlight.
- **Why it's remarkable:** The only animated element is a thin-film rainbow sheen orbiting a black bezel. It gives a static, almost monochrome object a premium "alive" quality without moving its geometry at all.

## 2. Composition & layout
- **Tray:** The pill enters from the left edge and ends in a full semicircle at x≈1350. It is about 725 px tall (y 320→1045) and roughly 53% of the frame height.
- **Button:** concentric with the tray's end cap, centred at about (990, 680).
  - The outer ring is about 630 px in diameter.
  - The inner face is about 530 px.
  - The bookmark glyph is about 170×215 px, optically raised by about 6 px above centre.
- **Framing:** The crop is very tight (macro product-shot framing). The background is plain #181818 above and below the tray.

## 3. Typography
None — no text in frame. The bookmark glyph has rounded corners (about 22 px) and a soft V-notch, drawn as a filled, slightly inflated shape rather than a stroked icon.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #181818 | canvas | 71% |
| #2b2b2b | tray surface (gradient to ~#252525 at bottom) | 26% |
| #222222 | button face | — |
| #575959 / #5a5a5a | glyph top, bezel highlight | 1.6% |
| #333737 | bezel mid-tone | 1.4% |
| iridescent (violet ≈#5b4b8a, teal ≈#2f7f86, amber ≈#a07a48) | travelling rim sheen | <1% |

WCAG checks (non-text UI, 3:1 target):
- Glyph #5a5a5a on face #222222 is 2.31:1, which fails the 3:1 target.
- Tray #2b2b2b on canvas #181818 is 1.25:1, so the tray is defined only by its hairline.
- The bezel edge #575959 on tray #2b2b2b is 2.01:1.

The palette is deliberately near-black. All chroma lives in the less-than-1% iridescent band.

## 5. Depth & material
- **Three nested layers:**
  1. An outer bezel ring about 40 px thick, with a dark inner groove and an iridescent outer edge.
  2. A bright 2–3 px chamfer highlight (#6a6a6a) on its inner lip, brightest at the upper right.
  3. A recessed face with a soft radial vignette.
- **Shadow:** The button casts a broad, low-opacity drop shadow (about 60 px blur, about 20 px y-offset) onto the tray. A faint shadow continues past the tray's bottom edge onto the canvas.
- **Glyph:** a vertical gradient from #5a5a5a at the top to #4a4a4a at the bottom, with a 1 px darker outline, so it reads as embossed plastic.
- **Tray:** has a 1 px #0e0e0e hairline outline.

## 6. Components & patterns
- **Action button:** a circular icon button (bookmark/save) docked at the end of a toolbar pill, which suggests the trailing slot in a floating action bar.
- **Idle ambient animation:** The rim sheen implies "this is the primary or special action" without a colour fill.
- No pressed/active state is shown in the clip. The glyph never fills or changes.

## 7. Motion
Measured (m0_motion.json, 30 fps, 12.23 s, motion_fraction 0.0, mean energy 0.09, seamless_loop_likely true):
- No segment crossed the threshold, so the motion is continuous, very low-energy and linear.
- From frames 1.36 s apart (estimates):
  - The coloured arc travels around the ring. Its spectral order shifts between frames (violet/teal at the top at 0.68 s, amber at the left at 2.04 s, teal at the right at 3.40 s).
  - This implies a rotating conic gradient, or several overlapping ones, at an irregular rate. It is probably two sheens at different periods (about 4–6 s), which avoids an obvious mechanical spin.
- At 7.48 s a warm amber bloom appears briefly in the upper part of the face. It acts as an internal light-leak accent.
- The 12.2 s loop is seamless (first/last diff 0.08).

## 8. Brand system
n/a — this is a component study, not a brand system. Identity cues: an "obsidian with oil-slick" material language that could define a premium dark product.

## 9. UX
- The circle is a large, clearly tappable target, and its position at the tray end signals the primary slot.
- **Risks:**
  - The glyph is under 3:1 against its face, so recognisability depends on shape alone.
  - The ambient loop is decorative and does not communicate state. If every button shimmered, the signal would be lost.
  - It needs `prefers-reduced-motion` handling.
- It works best as an "attention, new feature" affordance, used once per screen.

## 10. Craft signals
- The iridescence sits on the outermost 6–10 px of the bezel only. The inner lip carries a separate neutral specular highlight, so there are two distinct materials.
- The button is exactly concentric with the tray's semicircular end cap.
- A 1 px dark hairline defines the tray where luminance contrast (1.25:1) alone would not.
- Tonal steps are tightly controlled: #181818 / #222222 / #2b2b2b / #333737 / #575959.
- The colour sheen has no fixed period, so the loop never looks like a spinner.

## 11. Reproduction recipe
```css
:root{--bg:#181818;--tray:#2b2b2b;--face:#222;--bezel:#333737;--hi:#6a6a6a}
.tray{height:180px;border-radius:9999px;background:linear-gradient(#2b2b2b,#252525);box-shadow:0 0 0 1px #0e0e0e}
.btn{--a:0deg;width:156px;aspect-ratio:1;border-radius:50%;position:relative;
  background:radial-gradient(circle at 50% 40%,#262626,var(--face) 70%);
  box-shadow:0 0 0 10px var(--bezel),inset 0 0 0 2px var(--hi),0 20px 60px rgba(0,0,0,.55)}
.btn::before{content:"";position:absolute;inset:-12px;border-radius:50%;padding:3px;
  background:conic-gradient(from var(--a),transparent 0 55%,#5b4b8a 62%,#2f7f86 70%,#a07a48 78%,transparent 85%);
  -webkit-mask:linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);-webkit-mask-composite:xor;mask-composite:exclude;
  filter:blur(1.5px);animation:sheen 5.3s linear infinite}
@property --a{syntax:"<angle>";inherits:false;initial-value:0deg}
@keyframes sheen{to{--a:360deg}}
.btn svg{fill:url(#glyphGrad);filter:drop-shadow(0 1px 0 #111)}
@media (prefers-reduced-motion:reduce){.btn::before{animation:none}}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Rich material read from almost no colour; macro framing flatters it. |
| Originality | 7 | Iridescent rim on obsidian bezel is a fresh take on "glow ring" buttons. |
| Usability | 5 | Big target, but low-contrast glyph and purely decorative motion with no state. |
| Craft | 8 | Concentric geometry, layered bezels, irregular sheen period, hairline tray. |

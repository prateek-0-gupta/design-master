---
id: insp-realistic-button
source: inspora
category: Illustration
status: analyzed
title: "realistic button"
creator: "@unrootdesign"
styles: [skeuomorphic, micro-interaction, playful-rounded]
patterns: [extruded-3d-button, press-depth-collapse, fingerprint-smudge-accumulation, cursor-press-feedback, single-cta-stage]
mode: light
palette: ["#f2f0f5", "#7436e7", "#8a5ae4", "#a37de6", "#cab4ea", "#5a1fc4", "#ffffff"]
type_families: ["Inter Display / General Sans Semibold (likely)"]
type_class: [neo-grotesk]
radius_px: [20]
motion: {durations_s: [0.1, 0.2, 0.23], easing: [ease-out], loop: true}
scores: {aesthetics: 7, originality: 9, usability: 7, craft: 8}
craft_signals: [fingerprints-persist-per-click, base-lip-disappears-on-press, top-edge-specular-line, tinted-cast-shadow, smudges-lighten-not-darken, press-travel-about-8px]
anti_patterns: [smudges-erode-label-contrast, gimmick-may-read-as-dirty]
---
# realistic button — @unrootdesign

## 1. Snapshot
- **Subject:** An 8.04 s, 970×720, 50 fps recording of a single violet "take action" 3D button. Each click physically depresses it and leaves a **semi-transparent fingerprint smudge** on its glossy top face. The smudges accumulate over the session.
- **Why it's remarkable:** It takes "realistic" literally: not just bevel and shadow but *wear*. The interface remembers touch as a material trace, a witty and novel feedback layer (the post says it was prompted with an AI model).

## 2. Composition & layout
- **Stage:** The button is centred on a flat lilac-white stage (#f2f0f5). At rest it is about 338×108 px: a ~96 px top face plus a ~12 px darker extruded lip, at roughly x 315–653, y 308–426.
- **Space:** Nothing else is on the canvas; the button takes about 5% of the frame. The negative space puts all attention on micro-feedback.
- **Label:** centred, cap height about 28 px.

## 3. Typography
- "take action" is set entirely lowercase in a neo-grotesk Semibold (~600), close to Inter Display or General Sans. Size is about 40 px with tracking around −0.01 em, in white.
- The lowercase is a friendly tone choice that fits the toy-like object.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #f2f0f5 | stage | 95% |
| #7436e7 | button top face | 3% |
| #8a5ae4 / #a37de6 | gloss highlight, fingerprint smudges | 1.7% |
| #cab4ea | soft violet cast shadow / glow | 0.6% |
| #5a1fc4 (est.) | extruded base lip | — |
| #ffffff | label, top specular line | — |

WCAG checks:
- White on #7436e7 is 6.13:1 for a clean button.
- Where smudges lighten the face to #8a5ae4 the label drops to 4.5:1 (borderline). Over the densest smudges (#a37de6) it is **3.17:1**, so wear degrades legibility over time.
- Button vs stage is 5.42:1, a strong non-text contrast.

## 5. Depth & material
- **Extrusion:** A darker lip (~12 px) under the face reads as the side wall. On press the face drops about 8–10 px and the lip almost disappears (frames 2.23 s and 4.02 s vs 0.45 s), the classic "3D push" button done convincingly.
- **Surface:** glossy. There is a 1 px white specular line along the top edge, a vertical gradient from lighter top to deeper bottom, and a subtle inner rim (lighter 1 px border, ~#a37de6).
- **Shadow:** a violet-tinted soft cast shadow (~20 px blur, #cab4ea) rather than grey, which keeps the object luminous.
- **Fingerprints:** ridged whorl textures about 70–90 px across, blended lighter (screen/overlay) at roughly 20–30% opacity, placed at each click point. By 6.70 s there are 4–5 overlapping prints.

## 6. Components & patterns
- A primary CTA with real press physics.
- **Persistent interaction trace:** a stateful texture layer that records click positions. Similar ideas are footprints in games and the wear and tear of physical buttons.
- Hover shows a pointer cursor; there is no separate hover style visible.

## 7. Motion
Measured values (`m0_motion.json`):
- Motion fraction is 0.24 over 8.04 s, with 11 short segments. The median segment is 0.10 s.
- Three longer events are ease-out with very early peaks (peak_at 0.07–0.08):
  - 1.07–1.27 s (0.20 s);
  - 5.50–5.70 s (0.20 s);
  - 7.53–7.77 s (0.23 s).
- These are press-and-release cycles with a snap-down and decelerating return. The 0.1 s symmetric segments are rapid clicks or cursor moves.
- `seamless_loop_likely` is true (first/last diff 1.12).

Estimate: the press travel completes in about 60–80 ms and the release rebounds in about 120–150 ms, with no visible overshoot. Smudge appearance is instant on press.

## 8. Brand system
n/a — this is not a brand system.

## 9. UX
- **Strengths:** The press feedback is unmistakable (depth collapse plus print). Large target (~338×108 px). Excellent at-rest contrast.
- **Risks:**
  - Accumulated smudges reduce label contrast toward 3.2:1 and could read as "dirty UI" or a rendering bug in production.
  - Prints should fade after some seconds, or cap at N.
  - Keyboard activation needs an equivalent (e.g. a centred print or none).
  - Under reduced motion, keep the colour change and drop the travel.

## 10. Craft signals
- Fingerprints are placed at the actual cursor coordinates, not randomly (compare the print positions with the cursor in frames 3.13 s and 4.02 s).
- Smudges *lighten* the violet (oily sheen on gloss) rather than darkening it, which is physically right for skin oil on a glossy plastic.
- The extruded lip disappears completely when pressed, so there is no double-shadow artefact.
- The cast shadow is hue-matched violet, not neutral grey.
- A 1 px top specular line stays on in both states.

## 11. Reproduction recipe
```css
:root{--stage:#f2f0f5;--face:#7436e7;--face-hi:#8a5ae4;--lip:#5a1fc4;--glow:#cab4ea;--r:20px;--depth:10px}
.btn{position:relative;padding:28px 56px;border:0;border-radius:var(--r);color:#fff;
  font:600 40px/1 "Inter Display",Inter,system-ui;letter-spacing:-.01em;
  background:linear-gradient(#8248f0,var(--face));
  box-shadow:inset 0 1px 0 rgba(255,255,255,.55),inset 0 0 0 1px rgba(255,255,255,.18),
    0 var(--depth) 0 var(--lip),0 calc(var(--depth) + 14px) 24px -6px var(--glow);
  transform:translateY(0);transition:transform .14s cubic-bezier(.2,.9,.3,1),box-shadow .14s cubic-bezier(.2,.9,.3,1)}
.btn:active{transform:translateY(var(--depth));transition-duration:.07s;
  box-shadow:inset 0 1px 0 rgba(255,255,255,.55),inset 0 0 0 1px rgba(255,255,255,.18),0 0 0 var(--lip),0 4px 10px -4px var(--glow)}
.print{position:absolute;width:84px;aspect-ratio:.8;background:url(fingerprint.svg) center/contain;
  mix-blend-mode:screen;opacity:.25;pointer-events:none;transform:translate(-50%,-50%) rotate(var(--rot))}
```
JS: on `pointerdown`, append a `.print` at the local x/y with a random `--rot` (±25°). Keep at most 6 prints and fade older ones over 10 s to protect contrast.

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 7 | Polished candy-gloss button; deliberately simple staging. |
| Originality | 9 | Fingerprint wear as feedback is a genuinely new micro-interaction idea. |
| Usability | 7 | Clear press feedback, but cumulative smudges erode contrast with no decay. |
| Craft | 8 | Correct lip collapse, tinted shadow and physically plausible lightening smudges. |

---
id: insp-2-8
source: inspora
category: Motion
status: analyzed
title: "AI Motion"
creator: "@__causasui"
styles: [photo-led, technical-wireframe, x-glitch-inference]
patterns: [object-detection-overlay, confidence-score-labels, bezier-connector-lines, ascii-glyph-interstitial, hard-cut-to-black, classical-reference-recomposition]
mode: mixed
palette: ["#70a6d5", "#80b7e1", "#6398c9", "#568bbd", "#3b2925", "#5e565a", "#ffffff", "#000000"]
type_families: ["Arial / Helvetica system sans (likely)", "Monospace (Consolas / Menlo-like) for ASCII intro (likely)"]
type_class: [neo-grotesk, mono]
radius_px: [0]
motion: {durations_s: [0.17, 0.21, 0.29, 0.25], easing: [ease-in], loop: false}
scores: {aesthetics: 7, originality: 7, usability: 4, craft: 6}
craft_signals: [labels-anchor-to-hand-landmarks, red-word-white-score-pairing, thumbnail-crops-beside-labels, ascii-frame-as-cut-transition, overlay-density-pulses-with-cuts]
anti_patterns: [overlay-text-illegible-at-size, labels-fail-contrast-on-sky, low-resolution-700px]
---
# AI Motion — @__causasui

## 1. Snapshot
- **Subject:** A 5.0 s, 700×700 loop-like clip that re-stages Michelangelo's *Creation of Adam* as two photographed hands reaching across a flat sky-blue backdrop. A machine-vision overlay flickers on and off: red vocabulary words ("Peripatetic", "Reticentia", "Soteriological", "Palimpsest", "Silentium", "Funereal"), white decimal scores, tiny image crops and white bezier threads. It is bookended by a black frame of scattered ASCII glyphs.
- **Why it's remarkable:** It fuses the classical image with the visual language of AI inference (detections, confidence values, embeddings). The overlay is treated as poetry rather than data.

## 2. Composition & layout
- **Hands:** They enter from the left and right edges at y≈300–420 (of 700), and the fingertip gap sits at the exact centre (x≈350–380). The upper and lower 40% of the frame is empty gradient sky, a deliberate echo of the fresco's negative space.
- **Overlay clusters:** They gather at the fingertips and knuckles. Labels are about 9 px red text, with scores about 7 px white below. Thumbnails (≈20×20 px crops of the scene) sit beside some labels.
- **Threads:** thin white curves (≈1 px) arc between detections, crossing the gap.
- **ASCII frames (0.28 s, 3.64 s):** pure black with three rows of white glyphs (`y } [ L ( ^ c ~ | ^ n J`) at about 30 px. At 3.64 s the frame is fully black (a hard cut).

## 3. Typography
- **Overlay:** a default system sans (Arial or Helvetica-like) at very small sizes, about 9 px for words and about 7 px for scores (e.g. "0.01619417"). The rawness is intentional: debug UI.
- **Words:** Latinate and rare ("Peripatetic", "Soteriological", "Palimpsest", "Somnambulant"), as if the classifier labels concepts rather than objects.
- **ASCII intro:** a monospace face, white on black, letter-spaced about 1 em, with random punctuation glyphs as a "decoding" texture.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #70a6d5 / #80b7e1 / #6398c9 | sky backdrop gradient (lighter centre) | ~80% |
| #568bbd / #4a7fb1 | backdrop vignette edges | ~17% |
| #3b2925 / #5e565a | hand shadows, sleeve | ~10% |
| #b3261e (approx) | label red | <1% |
| #ffffff | scores, threads, ASCII | <1% |
| #000000 | interstitial frames | 2 frames |

WCAG checks: everything in the overlay fails.
- Red label on sky is 2.52:1.
- White scores on #70a6d5 are 2.59:1, and on #80b7e1 they are 2.15:1.
- Only the ASCII frame (white on black, 21:1) is crisp.

The overlay is texture, not information.

## 5. Depth & material
- **Photo:** a soft studio photo with gentle vignette lighting from the centre. The hands have natural shadow and skin tone; the left sleeve is a rust-red knit.
- **Overlay:** completely flat with no shadows. The thumbnail crops are small rectangles, sometimes with an orange or rust fill, like bounding-box swatches.
- **Glitch:** frames flicker between dense overlay (0.84 s, 4.76 s), sparse (1.40 s), and none (1.96, 3.08 s). Compression artefacts are visible at 700 px.

## 6. Components & patterns
- **Detection overlay:** a label, a confidence score and an optional thumbnail, connected by bezier "attention" lines.
- **ASCII interstitial:** a glyph field used as a cut, like a terminal decoding the image.
- **Classical recomposition:** a known artwork restaged as a contemporary photo.

## 7. Motion
Measured: 5.04 s at 24 fps, 4 segments, motion fraction 0.16, very high p95 energy (136.7, from hard cuts to and from black), not a loop.
- **Segments:** 0.46–0.62 s (0.17 s), 0.96–1.17 s (0.21 s), 1.29–1.58 s (0.29 s) and 3.12–3.38 s (0.25 s). All peak late (0.88–0.93 → ease-in), which is the signature of abrupt cuts and overlay flashes rather than eased motion.
- **Between cuts:** The hands themselves drift only slightly (the fingertip gap narrows from about 40 px at 1.40 s to touching at 3.08 s, an estimate).
- **Rhythm:** dense overlay, sparse, none, black/ASCII, then dense again, on a stuttering cadence of about 0.5 s.

## 8. Brand system
n/a — not a brand system. Identity cues: classical art plus machine-vision debug UI, red/white annotation colour coding, and an obscure-vocabulary voice.

## 9. UX
Not an interface; it is a motion artwork.
- As a pattern reference, the detection-overlay idiom communicates "the system is analysing" instantly.
- The text sizes and contrast make it unreadable, which is acceptable as texture but not for a real product UI.

## 10. Craft signals
- Labels are anchored to anatomical landmarks (fingertips, knuckles) rather than placed randomly.
- Words are consistently red and numbers consistently white.
- The fingertip gap sits exactly on the vertical centre line.
- The ASCII frame is used as a transition cut, not a title.
- Overlay density varies frame to frame to imply live inference.

## 11. Reproduction recipe
```css
.stage{aspect-ratio:1;background:radial-gradient(70% 60% at 50% 45%,#80b7e1,#568bbd);position:relative;overflow:hidden}
.det{position:absolute;font:400 9px/1.1 Arial,Helvetica,sans-serif;color:#b3261e;text-shadow:0 0 1px rgba(255,255,255,.5)}
.det .score{display:block;font-size:7px;color:#fff;font-variant-numeric:tabular-nums}
.det .crop{width:20px;height:20px;background:var(--crop) center/cover;outline:1px solid #fff}
svg.threads path{fill:none;stroke:#fff;stroke-width:1;opacity:.85}
.ascii{position:absolute;inset:0;background:#000;color:#fff;font:400 30px/1.3 Menlo,monospace;letter-spacing:1em;
  display:none}
.stage.cut .ascii{display:block}
```
```js
// flicker overlay density on a ~0.5 s stutter
setInterval(()=>{ const n=[0,3,12,24][Math.floor(Math.random()*4)]; renderDetections(n); },480);
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 7 | A striking concept image with a calm sky field; the low resolution and noisy overlay cheapen it slightly. |
| Originality | 7 | Combining a classical reference with an AI-inference overlay is a timely juxtaposition, though the overlay idiom is widespread. |
| Usability | 4 | Overlay text fails contrast and is illegible; as an interface pattern it communicates mood only. |
| Craft | 6 | Good anchoring and colour coding, but a 700 px export and compression artefacts. |

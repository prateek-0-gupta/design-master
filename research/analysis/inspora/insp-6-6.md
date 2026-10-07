---
id: insp-6-6
source: inspora
category: Illustration
status: analyzed
title: "Isometric animation"
creator: "@mehmetozsoyart"
styles: [isometric, technical-wireframe, monochrome, grain-noise]
patterns: [isometric-ui-explainer, sliding-selection-puck, segmented-progress-pill, flipping-check-coin, lane-based-list, pixel-confetti-accents]
mode: light
palette: ["#f8f7f5", "#e8e8e8", "#dcdcdb", "#b3b3b3", "#9d9d9d", "#636262", "#1e1d1d", "#000000"]
type_families: []
type_class: []
radius_px: [9999, 60]
motion: {durations_s: [20.03], easing: [linear, ease-in-out], loop: true}
scores: {aesthetics: 8, originality: 7, usability: 6, craft: 8}
craft_signals: [uniform-2px-outline, true-30deg-isometric, stipple-grain-on-top-faces-only, extruded-sides-pure-white, progress-shades-step-black-to-grey, pixel-squares-as-sparkle]
anti_patterns: [meaning-of-glyphs-ambiguous, no-text-for-context]
---
# Isometric animation — @mehmetozsoyart

## 1. Snapshot
- **Subject:** A 20.1 s, 1920×1292 seamless loop of an isometric UI diorama:
  - a rounded square tray with three task lanes;
  - a black "selected" slab with a search puck that slides between lanes;
  - a floating segmented progress pill that fills black → dark grey → grey;
  - a check coin that flips each cycle.
- **Why it's remarkable:** It explains an abstract flow (search → pick → progress → done) entirely with greyscale extruded line-art. It works as product-marketing illustration for an AI or task tool and needs no copy.

## 2. Composition & layout
- **Tray:** a ~970 px wide isometric rounded square (top face radius ~60 px), centred low at about y 450–1050, with an extruded ~50 px white edge.
- **Lanes:** three diagonal capsules (~200 px wide) with a 2 px grey outline (#b3b3b3). Each lane head shows a small "check-and-lines" task glyph.
- **Selected slab:** a black capsule raised ~30 px above its lane, carrying a ~220 px white disc with a search glyph.
- **Floating elements:** the progress pill (~450×230 px in projection) floats above and behind at the top-right. The check coin (~110 px) floats to its upper-left.
- Pale grey pixel squares (~45 px) dot the periphery as sparkle accents.
- About 60% of the frame is empty #f8f7f5.

## 3. Typography
None. The glyphs are pictograms only: check-plus-dash "task" marks, a magnifier, and a check. All are drawn with the same ~6 px strokes.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #f8f7f5 | warm off-white canvas | 87% |
| #e8e8e8 / #dcdcdb | tray top face (stippled) / shadow | 7% |
| #b3b3b3 / #9d9d9d | lane outlines / third progress segment | 2.4% |
| #636262 / #1e1d1d | mid shades, second progress segment | 1.3% |
| #000000 | outlines, selected slab, first segment | 1.7% |

The system is strictly achromatic. State is expressed by luminance steps: black = active or complete, grey = pending. Black outline on the canvas is ~20:1. There is no text to test.

## 5. Depth & material
- True 30° isometric projection with uniform ~3 px black outlines on every edge, a technical-drawing look.
- Top faces carry a fine stipple grain. Side faces are flat white, so light is implied from the top.
- A single soft grey offset shadow (#dcdcdb) lies under the tray. The floating pill and coin have no cast shadow, which emphasises that they float.
- The puck has an ellipse shadow on the slab.

## 6. Components & patterns
- **List with a selected row:** the black slab moves lane to lane, acting as a selection indicator.
- **Search puck:** suggests query or focus on the selected item.
- **Segmented progress:** three segments fill in decreasing darkness, with a white dot "cursor" sliding along the divider.
- **Completion:** the check coin flips (it reads edge-on in some frames, t≈3.4 s and 12.3 s).

## 7. Motion
Measured: 30 fps, duration 20.13 s, one continuous segment of 0.03–20.07 s (motion_fraction 0.98, shape continuous/linear, energy_cv 0.34), seamless_loop_likely true (first/last diff 0.65).

So something is always moving. From the 9 frames (estimates):
- the black slab changes lanes about every 2.2 s (right → left → middle → …);
- the progress pill steps one segment per lane change;
- the coin flips on each completion;
- the pixel squares fade in and out.

The low energy variance suggests eased transitions chained back-to-back with no holds, which is typical of Rive or After Effects explainer loops.

## 8. Brand system
n/a — not a brand system. The monochrome-outline isometric language is a reusable illustration style for a product's marketing set.

## 9. UX
As an illustration it communicates "select → process → done" without words. It would work as an empty-state, onboarding or landing-page loop. However:
- the glyphs (check-and-dashes) are ambiguous without a caption;
- 20 s of non-stop motion needs a reduced-motion fallback;
- monochrome-only state works for colour-blind users, but black vs dark grey (#000 vs #1e1d1d) is barely distinguishable.

## 10. Craft signals
- The outline weight is identical on every object regardless of depth (no perspective scaling).
- The isometric axes are consistent at 30°, and the lane capsules are parallel to the tray edges.
- The stipple texture is only on top faces; side faces are flat white.
- Progress segments step black → #1e1d1d → #9d9d9d, a value-only state scale.
- Floating parts have no cast shadow, while grounded parts do.
- The pixel-square sparkles use the same grey as the tray shadow.

## 11. Reproduction recipe
```css
:root{--canvas:#f8f7f5;--face:#e8e8e8;--shadow:#dcdcdb;--line:#000;--muted:#b3b3b3;--s1:#000;--s2:#1e1d1d;--s3:#9d9d9d}
.iso{transform:rotateX(60deg) rotateZ(-45deg);transform-style:preserve-3d}
.tray{width:600px;aspect-ratio:1;border-radius:60px;border:3px solid var(--line);
  background:var(--face) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='80' height='80'%3E%3Cfilter id='n'%3E%3CfeTurbulence baseFrequency='1.2'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='.15'/%3E%3C/svg%3E");
  box-shadow:0 0 0 0 var(--line),30px 30px 0 var(--shadow)}
.slab{border-radius:9999px;background:#000;transform:translateZ(30px);transition:transform .9s cubic-bezier(.65,0,.35,1)}
.slab[data-lane="0"]{translate:0 0}.slab[data-lane="1"]{translate:200px 0}.slab[data-lane="2"]{translate:400px 0}
@keyframes flip{0%,80%{transform:rotateY(0)}100%{transform:rotateY(360deg)}}
.coin{animation:flip 2.2s ease-in-out infinite}
```
Drive lane changes with a 2.2 s interval for a 20 s seamless loop.

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Crisp monochrome isometric with tasteful grain. Calm and premium. |
| Originality | 7 | Isometric UI explainers are common. The value-only state scale is a nice twist. |
| Usability | 6 | Communicates flow, but the glyphs are ambiguous and the motion is endless with no rest. |
| Craft | 8 | Consistent axes, line weight and shading logic throughout a seamless 20 s loop. |

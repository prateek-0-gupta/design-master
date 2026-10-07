---
id: insp-8-1
source: inspora
category: Motion
status: analyzed
title: "File cabinet slide"
creator: "@samdape"
styles: [technical-wireframe, hairline-ui, skeuomorphic, photo-led]
patterns: [card-catalogue-index, tab-pull-to-preview, hover-raises-folder, letter-divider-tabs, cutout-object-preview, perspective-drawer]
mode: light
palette: ["#e0e0e0", "#111111", "#000000", "#a4a4a2", "#47372d", "#c6c5c3", "#f4ef6e"]
type_families: ["Inter (likely)"]
type_class: [neo-grotesk]
radius_px: [6, 4]
motion: {durations_s: [0.3, 0.3, 0.87, 0.27, 0.63, 0.27], easing: [ease-out, ease-in], loop: true}
scores: {aesthetics: 8, originality: 9, usability: 6, craft: 8}
craft_signals: [1px-outline-only-geometry, alternating-tab-columns, black-letter-dividers-with-counts, cutout-3d-object-rotates-in-folder, drawer-perspective-converges, yellow-label-single-accent]
anti_patterns: [details-label-1.9-to-1, dense-tabs-small-targets]
---
# File cabinet slide — @samdape

## 1. Snapshot
- **Subject:** An 11.7 s, 1080×1080 loop of a personal archive drawn as an open card-catalogue drawer ("sam's secret files"). Hovering a tab lifts that folder out, and it shows a rotating cut-out 3D capture of the object (a Sony Walkman, a person in a chair, a plant).
- **Why it's remarkable:** Pure 1 px line-drawn file folders with real photogrammetry-like cut-outs popping out of them. The "file system as a physical drawer" metaphor is rendered in the most reduced possible way, and real objects provide all the texture.

## 2. Composition & layout
- **Drawer:** drawn in one-point perspective. The front panel is about 990 px wide at y≈925, and its sides converge upward to a back width of about 790 px at y≈110.
- **Tab grid:** about 30 folders at about 26 px vertical pitch. The tabs alternate between two columns (left about x 440–660, right about x 660–880), with occasional far-left tabs ("104 quiet", "112 rum"). The stacked tabs look like a real Rolodex.
- **Letter dividers:** black filled tabs (O 010, P 012, Q 005, R 002, S 002) sit at different x positions to stagger them.
- **Label:** a yellow label "sam's secret files" (about 190×36 px) is centred on the drawer front.
- **Lifted folder:** grows to about 790×450 px, rises in front of the stack, and shows title, "details" and a centred object.

## 3. Typography
- **Typeface:** Inter or a similar neo-grotesk.
- **Tabs:** number left and name right-aligned, about 19 px Regular in #111. The numbers use tabular figures.
- **Divider tabs:** a white letter plus a three-digit count on a black fill.
- **Open folder:** title ("generic guy") about 18 px, with "details" beneath in light grey (about #a4a4a2).
- **Yellow label:** about 17 px Medium.
- **Case:** everything is lowercase except the divider letters, which gives a casual, diaristic tone.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #e0e0e0 | canvas and folder fill | 85% |
| #111111 / #000000 | 1 px outlines, text, divider tabs | ~4% |
| #a4a4a2 / #c6c5c3 | secondary label, object shading | 5% |
| #47372d / #1c1411 | photographic object tones (jacket, walkman) | 5% |
| #f4ef6e (est.) | label accent | 0.3% |

WCAG checks:
- Tab text #111 on #e0e0e0 is 14.3:1.
- White on the black divider is 21:1.
- #111 on the yellow label is 15.66:1.
- The "details" link (#a4a4a2) is **1.89:1, which fails**.

## 5. Depth & material
- Depth is constructed only from 1 px black outlines and occlusion: each folder is filled with the canvas colour so it hides the lines behind it. There are no shadows or gradients.
- The perspective drawer gives the scene its spatial depth.
- The cut-out objects are photographic with real lighting, so the only shading in the scene comes from the photos.

## 6. Components & patterns
- **Index tab:** number plus name. Hovering pulls the folder up and forward.
- **Letter divider:** a black tab with letter and count, acting as section navigation.
- **Preview folder:** title, details link and a 3D object that turns slowly (the person rotates from back view at 5.85 s to side view at 7.15 s; the walkman spins and then lies flat at 3.25 s).
- The folder-tab shape is a trapezoid with 45° shoulders and about 6 px corner rounding, consistent across all tabs.

## 7. Motion
Measured (m0_motion.json, 60 fps, 11.69 s, motion_fraction 0.25, seamless_loop_likely true). There are nine segments with a median of 0.27 s:
- **0.93–1.23 s (0.30 s, peak 0.17):** ease-out, folder 118 "sony" pulled up.
- **3.10–3.40 s (0.30 s):** symmetric, the folder sinking back.
- **4.33–5.20 s (0.87 s, peak 0.25):** ease-out, a big rise of "generic guy" with the stack re-flowing.
- **6.90–7.43 s (0.13 s + 0.27 s):** fast-start ease-outs, a tab hover hop.
- **8.37–9.00 s (0.63 s, peak 0.76):** ease-in, the folder dropping back with gravity.
- **10.00–10.27 s (0.27 s, peak 0.06):** a snappy ease-out, the "plant 003" pop.

Character: lifts are fast-start (ease-out) and returns are slow-start (ease-in, 0.63 s), which mimics paper being pulled up and then falling back. Objects inside rotate continuously at roughly 30–45° per second (estimate from frames).

## 8. Brand system
n/a — this is a personal portfolio interaction, not a brand system. Identity cues: a yellow label-maker strip, lowercase naming and a "secret files" voice.

## 9. UX
- **Strengths:**
  - Playful browsing of about 120 items with alphabetic dividers and counts.
  - Hover gives an instant preview without navigation.
- **Risks:**
  - Tab targets are about 26 px tall and overlap, which makes them hard on touch.
  - The grey "details" link fails contrast.
  - When a folder rises it hides about 60% of the index, so there is no simultaneous overview.
  - Search or keyboard navigation would be needed at scale.

## 10. Craft signals
- All geometry is 1 px #111 strokes; occlusion is done by fill, not by erasing lines.
- Tabs alternate between two columns at a consistent ~26 px pitch, with numbers in sequence (94, 96, 98 left; 95, 97, 99 right).
- Black divider tabs carry live counts (O 010, P 012) like a real catalogue.
- The drawer's sides converge to a single vanishing point, and the front label is centred on its axis.
- The lift/return easing is asymmetric: 0.27–0.30 s ease-out up, 0.63 s ease-in down.
- The only chroma is the yellow label; everything else is greyscale or comes from the photos.

## 11. Reproduction recipe
```css
:root{--paper:#e0e0e0;--ink:#111;--muted:#6f6f6d;--label:#f4ef6e;--font:"Inter",system-ui}
.drawer{perspective:1200px;background:var(--paper);font:400 13px/1 var(--font);color:var(--ink)}
.folder{position:relative;height:18px;margin-top:-1px;background:var(--paper);border-top:1px solid var(--ink);
  transform-origin:bottom;transition:transform .63s cubic-bezier(.55,0,1,.45)}
.folder .tab{position:absolute;top:-18px;left:var(--x);width:150px;height:18px;display:flex;justify-content:space-between;
  padding:0 14px;background:var(--paper);border:1px solid var(--ink);border-bottom:0;
  clip-path:polygon(10px 0,calc(100% - 10px) 0,100% 100%,0 100%);font-variant-numeric:tabular-nums}
.folder.divider .tab{background:#000;color:#fff}
.folder:hover,.folder.open{transform:translateY(-240px) scale(1.04);transition:transform .3s cubic-bezier(.2,.8,.2,1)}
.folder.open .object{animation:turn 8s linear infinite}
@keyframes turn{to{transform:rotateY(360deg)}}
.label{background:var(--label);border:1px solid var(--ink);border-radius:4px;padding:4px 12px;font-weight:500}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Striking line-art drawer with real cut-out objects; restrained palette with one yellow note. |
| Originality | 9 | Card-catalogue portfolio with rotating object captures is genuinely novel. |
| Usability | 6 | Fun to browse; dense overlapping tabs, failing "details" contrast, occlusive previews. |
| Craft | 8 | Consistent stroke weight, perspective, tab pitch and asymmetric gravity easing. |

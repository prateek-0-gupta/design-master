---
id: insp-file-upload-card
source: inspora
category: Motion
status: analyzed
title: "File upload card"
creator: "@DawoodUI"
styles: [dark-premium, micro-interaction, hairline-ui, soft-3d]
patterns: [dropzone-card, folder-metaphor-illustration, file-chip-drag, folder-opens-on-hover, absorb-glow-on-drop, title-plus-format-hint]
mode: dark
palette: ["#09090b", "#141416", "#1f1f23", "#2b2b30", "#3b3b40", "#656568", "#8e8e93", "#ffffff"]
type_families: ["Inter (likely)"]
type_class: [neo-grotesk]
radius_px: [32, 14, 12]
motion: {durations_s: [0.47, 0.17, 0.37, 0.47], easing: [ease-out, ease-in-out, ease-in], loop: true}
scores: {aesthetics: 8, originality: 6, usability: 7, craft: 8}
craft_signals: [hairline-rim-light-on-folder-edges, back-flap-rises-on-drag-over, light-burst-inside-folder-on-drop, file-chip-tilts-while-dragged, card-only-1-08-above-stage, fade-out-mask-on-folder-bottom]
anti_patterns: [no-visible-click-to-browse, card-edge-near-invisible]
---
# File upload card — @DawoodUI

## 1. Snapshot
- **Subject:** A 3.7 s, 1080×1080 loop of a dark "Upload a File" dropzone: a translucent "FinalDraft.pdf" chip is dragged in, the folder's back flap rises to receive it, and the folder flashes with an inner white glow as the file disappears inside.
- **Why it's remarkable:** The drop confirmation is light, not a checkmark — a soft bloom from inside the folder that fades in ≈0.5 s, on an otherwise near-monochrome card.

## 2. Composition & layout
- Card ≈665×748 px (x≈207→872, y≈167→915), radius ≈32 px, centred on #09090b.
- Folder illustration ≈512×330 px, upper 45% of the card; its bottom fades into the card via a gradient mask (no baseline).
- Text block left-aligned at x≈261 (≈54 px inset): title at y≈725, two-line hint below with ≈38 px line pitch, ≈80 px bottom padding.
- File chip ≈160×60 px (sheet scale ×1.69 ≈ 270×100 px in video) with a doc icon and file name.

## 3. Typography
- Inter-like: title "Upload a File" ≈32 px medium white; hint ≈26 px regular #8e8e93, leading ≈1.45.
- The hint lists formats in caps ("DOCX, PDF, PPTX, XLSX, TXT") — useful specificity.
- File chip label ≈16 px grey at low contrast.

## 4. Colour
| Hex | Role | Share (key frame) |
|---|---|---|
| #09090b | stage | 59% |
| #141416 | card surface | 31% |
| #1f1f23 / #2b2b30 | folder body gradient | 8% |
| #3b3b40 / #656568 | rim highlights, file chip | 2% |
| #8e8e93 | hint text | — |
| #ffffff | title, glow core | — |

WCAG (contrast.py):
- Title white on #141416: 18.4:1; hint #8e8e93: 5.64:1 (pass).
- Card vs. stage #141416 on #09090b: **1.08:1** — the card is almost invisible as a container.
- Chip label ≈#9a9aa6 on chip ≈#56565f: **2.61:1**.

## 5. Depth & material
- Folder front and back are dark glass panels with a 1.5 px light rim on top edges (≈rgba(255,255,255,.35)) fading toward the sides — rim lighting from above.
- Inner radial highlight on the front panel (lighter in the centre) suggests a curved surface.
- File chip is frosted grey glass with a slight tilt (≈−4°) while dragged.
- On drop, a white radial glow (≈200 px, blur ≈60 px) blooms from the folder mouth and spills onto the front panel.

## 6. Components & patterns
- **Dropzone card** with illustration + title + format hint.
- **Drag-over state:** back flap lifts ≈25 px and tilts open; the folder widens slightly (≈4%).
- **Drop state:** chip slides into the gap and vanishes; glow pulse; folder closes.
- Cursor is a custom outlined arrow drawn with the same rim-light stroke.

## 7. Motion
Measured (m0_motion.json): 3.72 s at 60 fps, motion_fraction 0.39, seamless_loop_likely true, 4 segments, median 0.42 s.
- 0.60–1.07 s (0.47 s, peak 0.25, ease-out): chip enters from top-right and the back flap rises.
- 1.63–1.80 s (0.17 s, symmetric): chip plunges into the folder.
- 1.90–2.27 s (0.37 s, peak 0.68, ease-in): glow builds to its peak (frame 2.27 s brightest).
- 2.60–3.07 s (0.47 s, peak 0.82, ease-in): glow fades and the flap settles back — energy late in the segment, so the end is a slow-start decay that snaps closed.
Unusual: two of four segments are ease-in, giving the glow a "charging" feel rather than a pop.

## 8. Brand system
n/a — not a brand system.

## 9. UX
- The metaphor is immediate: drop → it goes into the folder → light confirms.
- Format list sets expectations.
- Risks: no "browse" button or link for click/keyboard users; the card edge is barely distinguishable from the page (1.08:1), so the drop target's bounds are unclear before hover; no progress or file-name confirmation after the drop.

## 10. Craft signals
- Rim light only on top-facing edges of folder panels.
- Folder bottom dissolves into the card with a gradient mask instead of a hard edge.
- The back flap lifts on drag-over, before the drop.
- The confirmation is a glow that peaks ≈0.4 s after the drop and fades by ≈3.0 s.
- The custom cursor uses the same outline language as the folder.

## 11. Reproduction recipe
```css
:root{--stage:#09090b;--card:#141416;--panel-a:#2b2b30;--panel-b:#141416;--rim:rgba(255,255,255,.35);--text-2:#8e8e93}
.drop{background:var(--card);border-radius:32px;padding:54px;width:665px;outline:1px solid #1f1f23}
.folder .front,.folder .back{border-radius:14px;background:linear-gradient(180deg,var(--panel-a),var(--panel-b) 85%);
  box-shadow:inset 0 1.5px 0 var(--rim);-webkit-mask:linear-gradient(#000 60%,transparent)}
.folder .back{transform-origin:bottom;transition:transform .45s cubic-bezier(.2,.8,.2,1)}
.drop.is-over .folder .back{transform:translateY(-25px) rotateX(-12deg)}
.folder::after{content:"";position:absolute;inset:20% 25% auto;height:120px;border-radius:50%;
  background:radial-gradient(#fff,transparent 70%);filter:blur(30px);opacity:0}
.drop.dropped .folder::after{animation:glow 1.2s ease-in}
@keyframes glow{30%{opacity:.9}100%{opacity:0}}
h3{font:500 32px/1.2 Inter,system-ui;color:#fff} p{font:400 26px/1.45 Inter;color:var(--text-2)}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Refined dark glass folder with rim lighting; calm and premium. |
| Originality | 6 | Folder dropzones are common; the inner-glow confirmation is the distinct touch. |
| Usability | 7 | Clear metaphor and format hint; no browse fallback, faint card edge. |
| Craft | 8 | Consistent rim light, masked fade, well-staged flap lift and glow timing. |

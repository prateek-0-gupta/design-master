---
id: insp-photo-folders
source: inspora
category: Motion
status: analyzed
title: "photos folders"
creator: "@raul_dronca"
styles: [physical-material, soft-3d, minimal-swiss, micro-interaction]
patterns: [multi-select-grid, floating-action-bar, folder-as-drop-target, thumbnails-peek-from-folder, selected-thumbnail-shrink-and-check, count-badges-on-folders, grid-reflow-after-move]
mode: light
palette: ["#ffffff", "#f3f2f1", "#1d2429", "#121217", "#e3e2de", "#a3a29c", "#6e6e73", "#75604d"]
type_families: ["Inter / SF Pro Text (likely)"]
type_class: [neo-grotesk]
radius_px: [24, 12, 9999]
motion: {durations_s: [0.63, 0.73, 0.77, 0.97, 0.1], easing: [ease-out], loop: false}
scores: {aesthetics: 9, originality: 8, usability: 8, craft: 9}
craft_signals: [photos-visible-inside-folder-pocket, folder-front-blurs-contents, selected-tile-insets-8pct, check-badge-overlaps-corner, grid-bottom-fade-mask, muted-count-next-to-label, action-bar-pill-segmented]
anti_patterns: [folder-count-grey-low-contrast, no-undo-shown]
---
# photos folders — @raul_dronca

## 1. Snapshot
- **Subject:** A 23.2 s, 60 fps, 2880×2160 desktop prototype titled "Library: select photos to move them into folders".
  - The page has three glossy black 3D folders (Tennis, Office, Art) above a 4-column photo grid.
  - Selecting photos raises a floating dark action bar ("3 selected · Tennis · Office · Art · ×").
  - Choosing a folder flies the photos into it. They then peek out of the folder's pocket and the folder count increments.
- **Why it's remarkable:** Folders are rendered as physical pockets. Their contents are visible behind a frosted front flap, so the result of the action is persistent and glanceable, not just a number.

## 2. Composition & layout
- **Content column:** about 950 px wide in the 2000-px display (about 1370 px real), centred.
- **Header:** "Library" (about 28 px Semibold) and a grey subtitle on the left. "Reset" (text button) on the right appears after the first move.
- **Folder row:** three folders about 290×235 px each with about 50 px gaps, with the label and count centred below ("Office 4").
- **Photo grid:** 4 columns of 220 px square tiles with 22 px gutters and about a 12 px radius. The grid fades to white at the bottom (mask) to imply scroll.
- **Action bar:** a dark pill about 530×65 px pinned at the bottom centre, overlapping the grid.

## 3. Typography
- Inter or SF-like neo-grotesk.
  - Title: about 28 px Semibold #121217.
  - Subtitle: about 20 px Regular #6e6e73.
  - Folder labels: about 22 px Medium black, with the count in light grey (#a3a29c) after a space.
- **Action bar:** "3" in white Medium and "selected" in grey, then the folder names in white about 20 px. The hovered option gets a #3a3f44 pill.

## 4. Colour
| Hex | Role | Approx share |
|---|---|---|
| #ffffff | page | 67% |
| #121217 / #1d2429 | folder bodies, action bar | 7.5% |
| #f3f2f1 / #e3e2de | soft shadows and grid fade | 4% |
| #6e6e73 | subtitle | — |
| #a3a29c | folder counts | 2.4% (incl. photos) |
| #75604d / #3f4740 / #908b83 | photo content (warm interiors, old-master paintings, tennis greens) | ~10% |

WCAG checks:
- Title #121217 on white is 18.67:1.
- Subtitle #6e6e73 is 5.07:1.
- Folder count #a3a29c is **2.56:1 (fail)**.
- Action bar white on #1d2429 is 15.71:1, and "selected" #8a8f94 on the bar is 4.82:1.

The UI is achromatic so the photography supplies all colour.

## 5. Depth & material
- **Folders:** soft-3D black objects. The back panel has a tab, and a front flap is offset about 20 px lower with a subtle top-edge highlight and a vertical gradient (#2a2a2a → #121212). A large soft shadow sits below (about 0 30px 60px rgba(0,0,0,.18)).
- **Pocket:** moved photos sit between the back and front panels. Their tops peek above the flap and the rest is seen through a **frosted (backdrop-blurred) front flap**, a convincing translucent-plastic folder.
- **Tiles:** a subtle 1 px light border and a very soft shadow.
- **Selected state:** the selected tile shrinks to about 85% inside its cell and gains a 24 px black check badge at its top-right corner.

## 6. Components & patterns
- **Multi-select grid** with check badges and an inset scale for selected tiles.
- **Floating contextual action bar:** a count, then destination buttons, then a dismiss "×", with dividers between groups.
- **Folders** act both as a live preview and as a count.
- A **"Reset" text button** appears only once there is state to reset (progressive disclosure).
- **Grid reflow:** after a move, the remaining photos animate up to fill the gaps (compare 3.86 s with 6.43 s).

## 7. Motion
- **Measured:** 23.15 s with motion fraction 0.15 and `seamless_loop_likely: false`. The four big segments are all **ease-out with a very early peak (0.07–0.19)**, a snappy spring followed by a long settle. Each is a "move to folder" event:
  - 5.20–5.83 s (0.63 s): 3 photos to Art.
  - 10.57–11.30 s (0.73 s): 4 photos to Office.
  - 15.40–16.17 s (0.77 s): 4 photos to Tennis.
  - 20.17–21.13 s (**0.97 s**): 4 more to Office (count to 8). More items give a longer flight, which suggests a stagger of about 60–80 ms per photo.
- Short 0.1 s segments (1.67, 12.37, 16.30, 17.10 s) are the selection taps: the inset scale plus check-badge pop.
- **From frames (estimate):** photos shrink and fly to the folder, slide into the pocket and the flap blurs them, then the grid reflows over about 0.4 s.

## 8. Brand system
n/a — not a brand system. Cues:
- a monochrome UI with glossy black objects;
- curated editorial photography (old-master paintings, mid-century offices, vintage tennis).

## 9. UX
- **Strengths:**
  - Strong, direct feedback: the destination visibly contains the items.
  - Selection count plus destinations live in one bar.
  - The bar's "×" clears the selection.
  - "Reset" offers recovery.
  - Large targets.
- **Risks:**
  - Folder counts fail contrast.
  - No toast or undo after an individual move.
  - Drag-and-drop to folders is not shown, even though the folders look like drop targets.
  - At larger counts the pocket preview saturates (8 items look like 4).

## 10. Craft signals
- The moved photos are visible inside the pocket: crisp above the flap and blurred behind it, a backdrop-filter on the front panel.
- Selected tiles inset to about 85%, which leaves white space as a selection frame instead of a coloured outline.
- The check badge overhangs the tile's top-right corner by about 25% of its own size.
- The folder count is in a lighter grey right after the name ("Office 4"), the same size as the label.
- The hovered option in the action bar gets a lighter pill (#3a3f44) and the label stays white.
- The grid fades out at the bottom with a white mask (about 120 px).
- "Reset" appears only after the first change.

## 11. Reproduction recipe
```css
:root{--bg:#fff;--ink:#121217;--muted:#6e6e73;--count:#8a8a8e;--bar:#1d2429;--bar-hover:#3a3f44;--r-tile:12px;--r-folder:24px;
  --font:"Inter",-apple-system,system-ui,sans-serif;--spring:cubic-bezier(.16,1,.3,1)}
.folder{position:relative;width:240px;height:190px;filter:drop-shadow(0 30px 40px rgba(0,0,0,.18))}
.folder .back{position:absolute;inset:0 0 18% 0;border-radius:var(--r-folder);background:#1a1a1a}
.folder .pocket{position:absolute;inset:12px 18px 40% 18px;display:flex}      /* photos live here */
.folder .front{position:absolute;inset:22% -4px 0 -4px;border-radius:var(--r-folder);
  background:linear-gradient(#2a2a2acc,#121212f2);backdrop-filter:blur(14px);box-shadow:inset 0 1px 0 rgba(255,255,255,.12);
  clip-path:path("M0 24 Q0 0 24 0 H120 Q132 0 140 12 L150 26 Q156 34 168 34 H226 Q250 34 250 58 V190 H0 Z")}
.label{font:500 15px var(--font);color:var(--ink)} .label b{font-weight:400;color:var(--count)}
.tile{border-radius:var(--r-tile);transition:transform .25s var(--spring)}
.tile[aria-selected=true]{transform:scale(.85)}
.tile[aria-selected=true]::after{content:"✓";position:absolute;top:-6px;right:-6px;width:22px;height:22px;border-radius:50%;
  background:#111;color:#fff;display:grid;place-items:center;font-size:12px}
.bar{position:fixed;bottom:24px;left:50%;translate:-50% 0;background:var(--bar);color:#fff;border-radius:9999px;padding:6px;display:flex;gap:4px}
.bar button{padding:8px 14px;border-radius:9999px}.bar button:hover{background:var(--bar-hover)}
.fly{transition:transform .7s var(--spring) calc(var(--i)*70ms)}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 9 | Glossy black folders, editorial photos and a restrained white UI form a gallery-grade composition. |
| Originality | 8 | Folders that show their contents through a frosted flap turn a count into a physical artefact. |
| Usability | 8 | Clear select-then-move flow with strong feedback. Grey counts and missing undo hold it back. |
| Craft | 9 | Pocket layering, inset selection, stagger springs and progressive "Reset" are all carefully tuned. |

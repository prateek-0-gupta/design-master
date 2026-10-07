---
id: insp-4-9
source: inspora
category: Product
status: analyzed
title: "Expandable Tab Bar"
creator: "@HeyAliux"
styles: [dark-premium, micro-interaction, glassmorphism]
patterns: [morphing-container, tab-bar-to-action-grid, plus-to-close-toggle, icon-tile-grid-4-col, press-highlight-glass, detached-fab]
mode: dark
palette: ["#0e0e10", "#1c1c1e", "#28282a", "#434945", "#ffffff", "#86c529", "#b15589"]
type_families: ["SF Pro Text (likely)"]
type_class: [neo-grotesk]
radius_px: [9999, 40, 24]
motion: {durations_s: [0.57, 0.53, 1.13, 0.23, 0.17], easing: [ease-in-out, ease-out], loop: true}
scores: {aesthetics: 7, originality: 6, usability: 7, craft: 7}
craft_signals: [ios-system-gray-ramp, fab-stays-anchored-while-panel-morphs, plus-rotates-to-x, press-state-white-glass-bloom, icon-tile-squircle-on-panel, last-row-left-aligned-3-items]
anti_patterns: [surface-steps-1-1-to-1-2-contrast, panel-edges-dissolve-into-black]
---
# Expandable Tab Bar — @HeyAliux

## 1. Snapshot
- **Subject:** An 8.2 s, 720×720, 60 fps demo on an iPhone (macOS Sonoma wallpaper behind). A floating pill tab bar (Home, Inbox, Notifications, Layers) and a separate "+" button. Tapping "+" morphs the tab bar into an 11-action editing grid (Trim, Crop, Enhance, Text, Audio, Speed, Duplicate, Undo, Share, Save, Delete), and the "+" becomes an "×".
- **Why it's remarkable:** The navigation chrome itself becomes the action sheet. Nothing slides up from the bottom edge; the pill grows in place.

## 2. Composition & layout
- **Device and bar:** the phone fills the frame (cropped at top). The tab bar pill is ≈375×68 px at y≈465–533 (sheet scale ×1.125 to real 720). The round FAB is ≈68 px to its right with a ≈16 px gap.
- **Expanded panel (key frame):** ≈445×365 px (x≈88–533, y≈225–590), with a 4-column grid. Tiles are ≈90×80 px squircles at a ≈112 px column pitch and a ≈116 px row pitch.
- **Labels:** ≈13 px, sitting ≈10 px under each tile.
- **Last row:** three items, left-aligned (not centred), which preserves the grid columns.
- **FAB:** stays anchored at the bottom-right of the panel (x≈580, y≈558) in both states.

## 3. Typography
- SF Pro (Text for labels at ≈13 px Regular, Display for "Home" at ≈22 px). These are iOS system defaults.
- Labels are light grey (~#d8d8d8). The "Aa" glyph in the Text tile is the only typographic icon.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #0e0e10 / #010001 | screen background | ~60% |
| #1c1c1e | panel / pill surface | ~4% |
| #28282a | tile and FAB fill | ~14% |
| #434945 | rims / pressed state edges | ~4% |
| #ffffff | icons, title | ~2% |
| #86c529 / #b15589 | wallpaper only (green/magenta) | ~12% |

**WCAG:**
- Icons and labels pass easily: white on #1c1c1e is **17.01:1**, #d8d8d8 labels are **11.94:1**, and white on tiles is **14.71:1**.
- **Surface separations are almost nil.** Tile vs panel is **1.16:1** and panel vs screen is **1.13:1**. Shapes are perceived mainly through faint rims and blur, which fall well below the 3:1 non-text guideline.

## 5. Depth & material
- The panel and pill are dark translucent material (iOS "ultra-thin" style) with a ~1 px lighter rim at the top edge.
- Tiles are slightly lighter squircles (radius ≈24 px) with a soft inner glow; they look like frosted buttons.
- **Press state** (5.03 s frame, "Duplicate"): the tile blooms to near-white glass with a bright core. The neighbour "Undo" tile lightens to mid-grey, a liquid-glass spill effect.
- **FAB press** (3.20 s): the "×" button scales up ~1.2× and lightens to #8a8a8a-ish before release.

## 6. Components & patterns
- **Floating tab bar:** four outline icons, with the active "Home" in a lighter inner pill.
- **Detached FAB:** "+" toggles to "×" and remains the single exit point.
- **Action grid:** 4 columns, icon tiles plus text labels.
- **Destructive action:** "Delete" uses the same neutral styling as the others, with no red.

## 7. Motion
**Measured:** 8.23 s, motion fraction 0.45, 8 segments, median **0.55 s**, `seamless_loop_likely: true`.

| Time | Segment | What happens |
|---|---|---|
| 0.93–1.50 s | **0.57 s**, peak 0.50, symmetric ease-in-out | Pill expands into grid. |
| 1.80–2.03 s | 0.23 s, ease-out | Settle. |
| 2.47–3.03 s | 0.57 s, symmetric | Grid collapses back into pill. |
| 3.23–4.37 s | **1.13 s**, peak 0.01, sharp ease-out with long tail | FAB press, then expand with a spring-like overshoot. The panel appears shifted left at 3.20 s before settling. |
| 4.67–5.20 s | 0.53 s, ease-out | Tile press bloom on "Duplicate". |
| 5.47–5.63 s | 0.17 s | Press release. |
| 6.23–6.80 s | 0.57 s, symmetric | Collapse. |
| 6.97–7.30 s | 0.33 s | Re-expand / settle. |

- The core morph is a consistent **~0.57 s ease-in-out**.
- The 1.13 s ease-out segment suggests a spring with low damping.
- **From frames:**
  - Icons cross-fade between tab-bar and grid content during the size morph rather than travelling.
  - The "+" rotates 45° into "×" (estimate).

## 8. Brand system
n/a — not a brand system. Pure iOS vocabulary: SF Symbols-style outline icons, SF Pro, system grays (#1c1c1e is iOS systemGray6 dark).

## 9. UX
- **Strengths:**
  - Keeps the user's thumb in the same zone: open and close are on the same button.
  - The grid is scannable thanks to labelled icons.
  - The press-state bloom gives strong touch feedback.
- **Risks:**
  - Navigation tabs disappear while actions are open, which is a modal state with no backdrop dim, so it may be confused with a page change.
  - Delete has no destructive colour.
  - The low surface contrast makes tile boundaries hard to see on poor screens.

## 10. Craft signals
- The FAB's position is identical in both states (x≈580 center). Only its glyph changes.
- Grid tiles keep a consistent ≈22 px gutter. The panel padding (≈14 px) is smaller than the gutter, so tiles sit close to the edge — an intentional dense tray.
- The three-item last row is left-aligned, preserving column alignment.
- The surface ramp follows iOS system greys (#0e0e10 → #1c1c1e → #28282a).

## 11. Reproduction recipe
```css
:root{--bg:#0e0e10;--surface:#1c1c1e;--tile:#28282a;--rim:rgba(255,255,255,.08);--ink:#fff;--ink-2:#d8d8d8;
  --r-pill:9999px;--r-panel:40px;--r-tile:24px;--font:-apple-system,"SF Pro Text",system-ui,sans-serif;}
.dock{position:absolute;left:24px;bottom:28px;width:375px;height:68px;border-radius:var(--r-pill);
  background:color-mix(in srgb,var(--surface) 85%,transparent);backdrop-filter:blur(30px);
  box-shadow:inset 0 1px 0 var(--rim);
  transition:width .57s cubic-bezier(.65,0,.35,1),height .57s cubic-bezier(.65,0,.35,1),border-radius .57s}
.dock.open{width:445px;height:365px;border-radius:var(--r-panel)}
.grid{display:grid;grid-template-columns:repeat(4,90px);gap:36px 22px;padding:14px}
.tile{height:80px;border-radius:var(--r-tile);background:var(--tile);display:grid;place-items:center;
  transition:background .17s,transform .17s}
.tile:active{background:radial-gradient(circle,#fff 0%,#bdbdbd 70%);transform:scale(1.06)}
.fab{width:68px;height:68px;border-radius:50%;background:var(--tile);transition:transform .35s}
.fab[aria-expanded=true] svg{transform:rotate(45deg)}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 7 | Polished iOS-native dark look. Visually a little flat, black on black. |
| Originality | 6 | Tab-bar-to-menu morph is a known pattern; the press bloom adds interest. |
| Usability | 7 | Good thumb ergonomics and feedback; weak surface contrast, no destructive cue. |
| Craft | 7 | Consistent timing and anchored FAB; the spring overshoot segment is a bit long. |

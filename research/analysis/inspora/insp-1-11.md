---
id: insp-1-11
source: inspora
category: 3D
status: analyzed
title: "A highlighter marker"
creator: "@msllrs"
styles: [skeuomorphic, micro-interaction, dark-premium]
patterns: [floating-tool-dock, tool-pops-out-of-slot, expanding-pill-toolbar, segmented-mode-chips, 3d-object-as-selected-state]
mode: mixed
palette: ["#f9f9f9", "#2a292a", "#161514", "#3a3a3c", "#f04a0c", "#e6927c", "#080807"]
type_families: ["SF Pro Text / Inter (likely)"]
type_class: [neo-grotesk]
radius_px: [9999, 24]
motion: {durations_s: [0.23, 0.2, 4.3], easing: [ease-in-out, ease-in], loop: true}
scores: {aesthetics: 8, originality: 8, usability: 7, craft: 8}
craft_signals: [marker-rises-from-icon-slot, toolbar-width-grows-to-host-options, accent-matches-marker-cap, inner-top-highlight-on-dock, mode-chip-hairline-border, colour-band-on-marker-barrel]
anti_patterns: [white-on-orange-below-aa, dim-icon-glyphs]
---
# A highlighter marker — @msllrs

## 1. Snapshot
- **Subject:** A 4.3 s, 1242×712 screen recording of a whiteboard-style canvas. Clicking the pen icon in a dark floating dock makes a 3D black marker with an orange cap slide up out of the icon slot. The dock then extends to show "ink / highlight / eraser" chips.
- **Why it's remarkable:** The selected tool becomes a physical object that breaks out of the toolbar's bounds. Selection state is shown by an object rather than by a tint.

## 2. Composition & layout
- **Frame:** An off-white canvas (#f9f9f9) sits inside a salmon device/window frame (#e6927c, about 20 px visible at the left and bottom) on near-black (#080807). Only the bottom-left corner of the app is shown, so the dock is the subject.
- **Dock:** Anchored bottom-left at x≈72, y≈540–638, so about 98 px tall. Closed it is about 710 px wide with 6 icons. Open, it is about 970 px wide.
- **Icons:** About 36 px glyphs on an about 82 px pitch, separated into groups by 1 px vertical dividers (#3a3a3c) after the first icon and after the sixth.
- **Marker:** About 60 px wide and 250 px tall, rising to y≈385. That is about 155 px above the dock top, so roughly 60% of its height overhangs the canvas.

## 3. Typography
- Chip labels "ink", "highlight" and "eraser" are lowercase in a neo-grotesk at about 26 px in the 1242 px frame (about 13 px at @2x). They are close to SF Pro Text.
- The active chip "ink" is semibold white; inactive chips are regular grey (#b0b0b0-ish).
- There is no other text: hierarchy comes entirely from fill.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #f9f9f9 | canvas | 79% |
| #2a292a / #161514 | dock body gradient, chip fill | 8% |
| #3a3a3c | dividers, chip hairlines | 4% |
| #f04a0c (est.) | active chip, marker cap & band | <1% |
| #e6927c | device frame | 2.5% |
| #080807 | stage background | 2% |

WCAG checks:
- White on orange "ink" chip: **3.69:1** (passes only as large text; the label is about 13 px bold, so it fails AA).
- Grey chip label #b0b0b0 on #1a1a1a: 8.03:1.
- Icon glyph #8a8a8c on #2a292a: 4.21:1 (passes the 3:1 non-text rule).
- Dock against canvas: 13.76:1.

## 5. Depth & material
- **Dock:** A vertical gradient (#2f2e2f top → #1c1b1c bottom), a 1 px dark outer stroke, a faint lighter inner top edge, and a soft drop shadow on the canvas (about 0 6 16 rgba(0,0,0,.25)).
- **Marker:** Rendered in matte black plastic with a specular strip down the left of the barrel and a glossy orange tip. A thin orange band at about 55% of the barrel echoes the cap.
- **Slot:** The marker sits in a dark circular well about 70 px across, which reads as a hole it emerged from.

## 6. Components & patterns
- **Floating tool dock:** target, lasso/select, comment, pen, frame, delete-frame.
- **Expanding options tray:** Selecting the pen appends a divider plus three pill chips about 46 px tall with a 1 px #3a3a3c border.
- **Selected state:** the active chip is filled orange and the others are ghost pills.
- **Cursor:** changes to a crosshair while the pen is armed (frames at 1.67–2.63 s), which is good feedback.

## 7. Motion
Measured profile: 4.3 s at 30 fps, `motion_fraction` 0.10, `seamless_loop_likely: true`. Two segments were detected:
- **1.13–1.37 s (0.23 s, peak_at 0.64, symmetric ease-in-out):** the marker rises out of the slot. In frame f2 (1.19 s) the cap is just clearing the slot and the dock is already lengthening, with a ghost of the tray at the right.
- **3.33–3.53 s (0.20 s, peak_at 0.92, ease-in):** the marker drops back. The accelerating exit reads like gravity.
- The tray reveal shares the first segment, so the width change and the marker rise are a single gesture.
- Most of the clip is idle (90% still), which makes the two pops read as crisp events.

## 8. Brand system
n/a — not a brand system. Identity cues: the orange (#f04a0c) is used only on the "ink" state and the marker, so the accent equals the tool.

## 9. UX
- **Strengths:** Selection is unmistakable, and the crosshair cursor confirms the mode.
- **Risks:**
  - The marker overlaps the canvas and could cover content near the dock.
  - The icons are low-contrast grey on near-black.
  - The orange chip label falls short of AA at small size.
  - There is no text tooltip, so the icon meanings are guessable at best.

## 10. Craft signals
- The marker emerges from the exact centre of the pen icon's circular well rather than fading in on top of it.
- The dock grows in width to host the tray instead of opening a second popover.
- The orange of the cap, the barrel band and the active chip are one hue.
- Chips carry a 1 px hairline border, so the inactive state still has an edge on the dark dock.
- Vertical 1 px dividers split the dock into three functional groups.

## 11. Reproduction recipe
```css
:root{--canvas:#f9f9f9;--dock-top:#2f2e2f;--dock-bot:#1c1b1c;--line:#3a3a3c;--accent:#f04a0c;--chip-text:#b0b0b0}
.dock{display:flex;align-items:center;gap:20px;padding:12px 18px;border-radius:9999px;
  background:linear-gradient(#2f2e2f,#1c1b1c);border:1px solid #0d0d0d;
  box-shadow:inset 0 1px 0 rgba(255,255,255,.08),0 6px 16px rgba(0,0,0,.25);
  transition:width .23s cubic-bezier(.45,0,.55,1)}
.slot{position:relative;width:36px;height:36px;border-radius:50%}
.slot .marker{position:absolute;left:50%;bottom:0;translate:-50% 100%;opacity:0;
  transition:translate .23s cubic-bezier(.45,0,.55,1),opacity .1s}
.slot[aria-pressed=true] .marker{translate:-50% -60%;opacity:1}
.slot[aria-pressed=false] .marker{transition-timing-function:cubic-bezier(.55,0,1,.45);transition-duration:.2s}
.chip{height:23px;padding:0 10px;border-radius:9999px;border:1px solid var(--line);color:var(--chip-text);font:500 13px/1 "Inter",system-ui}
.chip[aria-checked=true]{background:var(--accent);color:#fff;border-color:transparent;font-weight:600}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | A tight dark dock against a bright canvas, with one hue and a beautifully rendered object. |
| Originality | 8 | The physical tool popping out of its slot is a fresh twist on toolbar selection. |
| Usability | 7 | Clear mode feedback and cursor change, but there are contrast gaps and a possible overlap with content. |
| Craft | 8 | Synced width and object motion, an ease-in exit, and a coherent accent. |

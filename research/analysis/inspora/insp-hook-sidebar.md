---
id: insp-hook-sidebar
source: inspora
category: Product
status: analyzed
title: "Hook sidebar"
creator: "@SwamiMalode"
styles: [minimal-swiss, hairline-ui, micro-interaction, dark-premium]
patterns: [table-of-contents-rail, dashed-hook-active-indicator, hover-preview-connector, opacity-based-hierarchy, caps-section-heading]
mode: dark
palette: ["#101010", "#f2f2f2", "#a1a1a1", "#777777", "#4b4b4b", "#e5341f"]
type_families: ["Inter (likely)"]
type_class: [neo-grotesk]
radius_px: [6]
motion: {durations_s: [0.3], easing: [ease-out], loop: true}
scores: {aesthetics: 8, originality: 8, usability: 7, craft: 8}
craft_signals: [dashed-line-with-rounded-elbow, red-for-active-grey-for-hover, line-grows-from-top-anchor, single-accent-colour, generous-item-pitch]
anti_patterns: [inactive-items-below-aa, accent-not-in-measured-palette]
---
# Hook sidebar — @SwamiMalode

## 1. Snapshot
- **Subject:** A 13.4 s, 3362×2160 loop of a "CONTENTS" side navigation with five items. A dashed red line runs down from the top of the list and hooks right into the active item. Hovering another item draws a grey dashed hook to it.
- **Why it's remarkable:** The active indicator is a path rather than a bar or dot. It shows where you are relative to the start of the document, and the hover preview shows where you would go.

## 2. Composition & layout
- **Heading:** "CONTENTS" at x≈620 / y≈200 in the 2000-px key frame (≈1040 / 336 native), followed by five items at a ~290 px native pitch (≈145 CSS at @2x; the recording is heavily zoomed).
- **Indent:** items are indented ~150 px native from the heading's left edge. The rail line lives in that gutter at the heading's x.
- **Hook geometry:** a vertical dashed line from the top of the list down to the active row, then a rounded elbow (~10 px radius) and a short horizontal run of ~90 px native stopping ~60 px before the label.
- The whole composition is left-aligned with nothing else on screen.

## 3. Typography
- Inter-like neo-grotesk.
- **Heading:** "CONTENTS" in caps at ~100 px native with +0.06 em tracking, medium weight, near-white.
- **Items:** ~110 px native regular, sentence case.
- **States are shown by colour value only:**
  - active and hovered items: #f2f2f2;
  - inactive items: about #777777 to #8a8a8a.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #101010 | background | 97% |
| #f2f2f2 | heading, active/hovered label | <1% |
| #a1a1a1 / #777777 | inactive labels | <1% |
| #4b4b4b / #303030 | grey hover-preview dashes | 1% |
| #e5341f (est.) | active hook (red-orange) | <0.5% |

The red dashes are too thin to form a palette cluster; the hex is estimated from frames.

WCAG checks:
- Active label on #101010: 17.0:1.
- Inactive #777777 on #101010: **4.25:1 (fails AA normal; passes large)**. At these sizes it counts as large text.

## 5. Depth & material
Completely flat. Hierarchy comes from line and value only.

## 6. Components & patterns
- **Active hook:** red, dashed (~6 px dash / 6 px gap native), ~3 px stroke, rounded elbow.
- **Preview hook:** the same geometry in dark grey, drawn from the active item's elbow down to the hovered item (frames 0.75 s and 3.73 s show red to Introduction/Overview plus grey to History/Architecture).
- Clicking promotes the preview to red and extends the red trunk.

## 7. Motion
- **Measured:** motion_fraction is 0.0 with zero segments above threshold (mean energy 0.04). The animated strokes are too thin to register. The loop is likely seamless (first/last diff 0.68).
- **From frames (estimates):**
  - the red trunk extends or retracts vertically to the new item, then the elbow and horizontal run draw in;
  - total about 0.3 s with an ease-out feel;
  - in the frame at 5.22 s the red line reaches References with a grey stub left at Architecture, so the hover line fades rather than snapping off;
  - label colour cross-fades at the same time.

## 8. Brand system
n/a — not a brand system. Identity cues: an editorial/technical-doc aesthetic with one warm accent on near-black.

## 9. UX
- Encodes reading position (how far down) and the hover target at once.
- The rail grows with depth, so a section further down gets a visibly longer line, a subtle progress cue.
- **Risks:**
  - On a long TOC the line becomes visually heavy.
  - Hover-only preview has no touch equivalent.
  - Inactive grey is borderline for small sizes.

## 10. Craft signals
- The elbow is rounded, not a mitred 90° corner, and the dash pattern continues through the curve.
- The active and preview hooks share identical geometry and differ only in colour.
- The horizontal run stops a consistent gap before every label.
- The trunk always starts at the same top anchor under the heading, so length equals position.
- One accent colour is used in the entire component.

## 11. Reproduction recipe
```html
<svg class="hook" width="48" height="H"><path d="M2 0 V{y-6} Q2 {y} 8 {y} H40" /></svg>
```
```css
:root{--bg:#101010;--ink:#f2f2f2;--ink-2:#8a8a8a;--accent:#e5341f;--preview:#4b4b4b}
.toc h6{font:500 13px/1 Inter;letter-spacing:.06em;color:var(--ink)}
.toc a{font:400 15px/1 Inter;color:var(--ink-2);transition:color .3s ease-out}
.toc a[aria-current],.toc a:hover{color:var(--ink)}
.hook path{fill:none;stroke:var(--accent);stroke-width:1.5;stroke-dasharray:3 3;stroke-linecap:round;
  transition:d .3s cubic-bezier(.2,.8,.2,1)}
.hook.preview path{stroke:var(--preview)}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Austere, typographic, one perfect accent. |
| Originality | 8 | A path-shaped active indicator with hover preview is a new take on TOC rails. |
| Usability | 7 | Clear current/target; hover-only preview, borderline greys. |
| Craft | 8 | Consistent geometry, rounded dashed elbows, coordinated fades. |

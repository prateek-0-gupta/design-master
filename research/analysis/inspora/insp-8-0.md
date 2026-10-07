---
id: insp-8-0
source: inspora
category: Product
status: analyzed
title: "Timeline concept"
creator: "@guerriero_se"
styles: [dark-premium, hairline-ui, minimal-swiss, micro-interaction]
patterns: [history-timeline-list, curved-branch-connector, active-node-accent, keyboard-focus-ring, segmented-day-week-month, icon-rail-sidebar, hover-row-fill]
mode: dark
palette: ["#0f0f0f", "#232323", "#2f2f2f", "#575454", "#8a8a8a", "#ffffff", "#ff4fa3"]
type_families: ["Inter (likely)"]
type_class: [neo-grotesk]
radius_px: [18, 14, 10]
motion: {durations_s: [0.13, 0.1, 0.23], easing: [ease-out], loop: true}
scores: {aesthetics: 8, originality: 7, usability: 9, craft: 9}
craft_signals: [s-curve-connector-from-date-to-item, accent-segment-lights-path-to-active-node, pink-tinted-active-text-not-pure-pink, visible-keyboard-focus-ring-2px-white, two-level-indent-24px, monochrome-plus-one-accent]
anti_patterns: [inactive-segment-labels-grey-only, focus-ring-and-hover-similar-weight]
---
# Timeline concept — @guerriero_se

## 1. Snapshot
- **Subject:** A 17.7 s, 1080×1080 demo of a dark "Timeline" panel in an AI-assistant app. It lists past conversations ("Asked for a high-protein meal plan", "Worked on the b402 dashboard UX"…) grouped under Today / Yesterday / Feb 8, 2026. The demo uses mouse hover and click plus keyboard focus navigation, and toggles Day → Week.
- **Why it's remarkable:** The tree connector is drawn as soft S-curves from each date node into its children. Selecting an item lights only the path segment that leads to it in pink, which makes hierarchy and selection one gesture.

## 2. Composition & layout
- The window is cropped, showing the top-left of the app at about 2× zoom.
- **Left icon rail:** ≈120 px wide in the 1080 key frame. Seven icons sit at ≈80 px pitch, and the active "timeline" icon is in a ≈70 px squircle (radius ≈14).
- **Main column:** the header row (≈120 px tall) holds "Timeline" (left) and a Day/Week/Month segmented control (right), with a hairline below it.
- **List:**
  - Date nodes sit at x≈262 and children at x≈287, so the indent step is 24 px.
  - Rows have a uniform ≈72 px pitch, which gives very airy spacing.
  - The text starts ≈24 px after its node dot.

## 3. Typography
- Inter (or a similar neo-grotesk) throughout.
- **Sizes:**
  - "Timeline" is ≈28 px Regular in white.
  - List items are ≈24 px Regular with slight positive tracking (≈+0.01 em) in grey #8a8a8a.
  - Date labels are the same size and grey. They are differentiated only by their outdent and node position.
  - Segmented labels are ≈22 px.
- The active item turns pale pink text (≈#f7c6dd) next to a saturated pink dot. The text tint is softer than the dot.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #0f0f0f | app background | ~77% |
| #2f2f2f / #232323 | outer stage, active chips, hover fill | ~22% |
| #575454 | connector lines, inactive dots | ~2% |
| #8a8a8a | list text, icons | ~1% |
| #ffffff | title, focus ring, active segment | trace |
| #ff4fa3 (est.) | active dot and path | trace |

**WCAG:**
- Grey list text on #0f0f0f is **5.55:1** (pass).
- Pink dot/path is **6.3:1**, and the pink-tinted active text is **12.85:1**.
- White on the active chip is **13.39:1**.
- The hover fill (#2f2f2f on #0f0f0f) is only **1.43:1**, so it is a subtle affordance. The white focus ring compensates for keyboard users.

## 5. Depth & material
- Flat. The window has a ≈1 px lighter border and a large radius (≈18 px real) against a #2f2f2f outer stage.
- The active rail icon and the active segment use #2f2f2f chips with an inner 1 px highlight.
- The pink active node has a soft glow (≈4 px).

## 6. Components & patterns
- **Timeline tree:** grey dots on a 1 px connector. Date-to-child transitions use an S-curve rather than an elbow.
- **Active state:** pink dot, pink connector segment from the previous node, and tinted text.
- **Hover state:** a full-width row fill (#1c1c1c-ish, radius ≈10) with a pointer cursor.
- **Keyboard focus:** a 2 px white rounded rectangle (radius ≈14) around the row, and the same ring around the segmented control when focused (12.76 s frame).
- **Segmented control:** Day/Week/Month. The selected segment is a raised #2f2f2f chip.

## 7. Motion
**Measured:**
- 17.67 s, with a very low motion fraction of **0.06**.
- Three tiny segments: 0.13 s and 0.10 s, both sharp ease-out, plus 0.23 s ease-in at 4.10 s.
- `seamless_loop_likely: true`.

**From frames:**
- State changes are almost instant (≈100–150 ms colour transitions).
- The pink path segment appears to draw from the previous node down to the selected dot.
- The focus ring jumps between rows rather than sliding.
- The Day → Week switch (≈14.7 s) moves the chip with no list re-layout.
- The calm, sub-200 ms feedback is appropriate for a productivity list.

## 8. Brand system
n/a — not a brand system. Identity cues: one hot-pink accent on a near-black monochrome UI, and curved connectors as a soft, organic signature in an otherwise rigid layout.

## 9. UX
- **Strengths:**
  - Excellent: hover, selected and keyboard-focus are three distinct, simultaneous states (8.83 s frame shows a pink selection plus a white focus ring on another row).
  - Grouping by date with a visible tree aids scanning.
  - The Day/Week/Month control scopes the history.
- **Weaknesses:**
  - Date labels and items share size and colour, so the groups rely on indent alone.
  - Inactive segment labels are grey without a hover hint.

## 10. Craft signals
- Connector S-curves have an equal radius at each date-to-child transition, and straight runs between siblings.
- Only the segment between the previous node and the active node turns pink. The rest of the path stays grey.
- Active text uses a pink tint (≈#f7c6dd), not the full accent, which avoids vibrating saturated text on black.
- The focus ring has a 2 px stroke, ≈14 px radius and a ≈4 px outset from the hover fill, so the two states can coexist.
- 24 px indent = 24 px dot-to-text gap: one spacing token.

## 11. Reproduction recipe
```css
:root{--bg:#0f0f0f;--chip:#2f2f2f;--hover:#1c1c1c;--line:#575454;--ink:#fff;--ink-2:#8a8a8a;
  --accent:#ff4fa3;--accent-text:#f7c6dd;--indent:24px;--row:72px;--font:"Inter",system-ui,sans-serif;}
.tl{font:400 24px/1 var(--font);letter-spacing:.01em;color:var(--ink-2)}
.tl li{position:relative;height:var(--row);display:flex;align-items:center;padding-left:calc(var(--indent)*2);border-radius:10px;
  transition:background .12s ease-out,color .12s ease-out}
.tl li.child{margin-left:var(--indent)}
.tl li::before{content:"";position:absolute;left:var(--indent);width:8px;height:8px;border-radius:50%;background:var(--line)}
.tl li:hover{background:var(--hover)}
.tl li[aria-current=true]{color:var(--accent-text)}
.tl li[aria-current=true]::before{background:var(--accent);box-shadow:0 0 6px var(--accent)}
.tl li:focus-visible{outline:2px solid var(--ink);outline-offset:4px;border-radius:14px}
/* connector: an SVG path per group, S-curve via cubic bezier, active segment stroked in --accent */
.seg [aria-selected=true]{background:var(--chip);color:var(--ink);border-radius:10px;box-shadow:inset 0 1px 0 rgba(255,255,255,.06)}
```
For the connector: `<path d="M262 265 C262 300 287 300 287 335 V 480" stroke="#575454"/>`, with an overlay path in `--accent` from the previous node to the selected one, animated with `stroke-dashoffset` over ~0.15 s.

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Calm, airy dark UI with one sharp accent. |
| Originality | 7 | A timeline list is common; the curved branch connectors and lit path are fresh. |
| Usability | 9 | Clear simultaneous hover/selection/focus states and AA text throughout. |
| Craft | 9 | Single spacing token, precise connector geometry, considered accent tinting. |

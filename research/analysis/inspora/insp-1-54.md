---
id: insp-1-54
source: inspora
category: Motion
status: analyzed
title: "dropdown interaction"
creator: "@dejvdesign"
styles: [minimal-swiss, micro-interaction, corporate-clean]
patterns: [multi-select-label-combobox, chip-row-sync, create-from-search, inline-colour-picker-step, hover-revealed-checkbox, flip-reflow-chips]
mode: light
palette: ["#fafafa", "#ffffff", "#f2f2f2", "#1c1c1e", "#8a8a8e", "#3478f6", "#e8962a", "#e0287a"]
type_families: ["SF Pro Text (likely)"]
type_class: [neo-grotesk]
radius_px: [9999, 20, 10, 6]
motion: {durations_s: [0.1, 0.1, 0.23], easing: [ease-out, ease-in-out], loop: true}
scores: {aesthetics: 7, originality: 6, usability: 9, craft: 8}
craft_signals: [chips-sorted-to-match-list-order, checkbox-hidden-until-hover-or-checked, colour-dot-repeats-in-chip-and-row, create-row-quotes-query-in-grey, breadcrumb-chip-in-colour-step, chips-reflow-with-gap-closing]
anti_patterns: [placeholder-grey-below-aa, lowercase-user-label-breaks-casing]
---
# dropdown interaction — @dejvdesign

## 1. Snapshot
- **Subject:** A 22 s, 1200×1248 screen recording of a label picker. A "+ Label" pill opens a searchable multi-select popover. Typing a new name offers "Create new label", then a colour step, and toggling rows adds or removes chips in the row above.
- **Why it's remarkable:** It is a complete, Linear-grade combobox flow (find → create → colour → toggle) with almost no chrome. The chips and list stay in exact sync and order.

## 2. Composition & layout
- **Chip row:** Centred horizontally at y≈488. Chips are about 52 px tall with about 12 px gaps. The "+ Label" trigger is a grey filled pill (≈145×60) rather than an outlined one.
- **Popover:** about 545 px wide, top-aligned 20 px under the chip row, left edge at x≈350. Its contents:
  - a search field about 84 px tall, with a 1 px divider below;
  - a list with 68 px row pitch (seven rows visible) and a 6 px-wide overlay scrollbar inside the right edge.
- **Row anatomy:** 20 px checkbox at x≈378, 16 px colour dot at x≈440, label at x≈470. Unchecked rows hide the checkbox entirely, so the dot column stays aligned.
- **Create step (f2):** The header turns into a breadcrumb ("Create" + preview chip "design"), followed by a "Pick a color" field and named swatches (Coral, Amber, Mint, Azure, Lilac, Rose, Teal).

## 3. Typography
- An SF Pro Text-like grotesk at a single size: about 26 px in the key frame (≈15 pt at 2× capture), weight 400 for rows and 500 for chips.
- The placeholder "Add or find a label…" is in grey #8a8a8e. In the create row, the quoted query is shown in grey after a dark "Create new label:", which separates the system's words from the user's.
- Sentence-case labels sit next to the user-typed lowercase "design", which is kept verbatim.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #fafafa | page | 96% |
| #ffffff | popover, chips | 2% |
| #f2f2f2 | hover row, "+ Label" fill | 1% |
| #1c1c1e | text, checked checkbox fill | <1% |
| #8a8a8e (approx) | placeholder | <1% |
| #3478f6 / #e8962a / #e0287a / #8b3cf0 / #1fcf98 / #ee3e48 / #5a6276 | label dots | dots only |

WCAG checks:
- Text #1c1c1e on white is 17.01:1; on the hover row (#f2f2f2) it is 15.2:1.
- The placeholder (#8a8a8e on white) is 3.44:1, which fails for normal text.

Hue lives only in 16 px dots, a "colour as tag, not surface" discipline.

## 5. Depth & material
- **Popover:** a 1 px #e5e5e5 border, about a 20 px radius, and a very soft shadow (about 0 8 24 rgba(0,0,0,.06)).
- **Chips:** a 1 px border with a white fill and a tiny shadow.
- **Hover row:** #f2f2f2 with about a 10 px radius, inset 12 px from the popover sides.
- **Checkboxes:** about a 6 px radius, filled #1c1c1e with a white tick.
- There is no blur and no gradients.

## 6. Components & patterns
- **Multi-select combobox:** search, filtered list, and create-if-missing.
- **Two-step creation:** name, then colour. Choosing a colour inserts the label into the list in alphabetical position and checks it.
- **Chip row as live mirror:** chips appear and disappear in list order, not click order (Accessibility, Copy, design, Handoff, Motion).
- **Hover-revealed checkbox:** an outline box appears only on the hovered row (f7 "Copy").
- **Trigger:** the "+ Label" pill doubles as the add action.

## 7. Motion
Measured: 22.04 s at 60 fps, motion fraction only 0.05, 7 segments almost all 0.10 s, plus one at 0.23 s (20.17–20.40 s, symmetric). `seamless_loop_likely: true`.
- The tiny durations are the point. Chip insertion and removal, hover highlights and popover opening are at or near 100 ms (single 3-frame bursts at 1.17, 4.73, 8.00/8.43, 18.33, 19.77 s), with peaks at 0.17 (ease-out) or 0.5 (symmetric).
- **Chip removal (f7, 18.36 s):** A gap is left where "Copy" was while neighbours slide, which implies a FLIP layout transition of about 0.2 s (estimated). It matches the measured 0.23 s segment at 20.17 s.
- Mostly the clip is a cursor moving over a static UI, which is product-realistic rather than showy.

## 8. Brand system
n/a — not a brand system. Identity cues: a Linear/Notion-style neutral UI where label colours have human names (Coral, Mint, Lilac), not hex.

## 9. UX
- **Strengths:**
  - Keyboard-first search.
  - The create path appears exactly when there is no match.
  - Named colours aid recall.
  - Sorted chips prevent reordering surprises.
  - Toggles are reversible in place without closing the popover.
- **Risks:**
  - Hiding unchecked checkboxes makes multi-select less obvious until hover, and on touch there is no hover.
  - Placeholder contrast is low.
  - There is no chip "×" visible, so removal only works via the list.

## 10. Craft signals
- Chip order equals list order, recomputed on every toggle.
- The dot column x stays fixed whether or not a checkbox is shown (the checkbox occupies a reserved 40 px gutter).
- The "Create new label" row quotes the query in grey, inside typographic quotes.
- The create step shows the label preview chip in its picked colour inside the breadcrumb.
- The overlay scrollbar sits inside the popover radius and does not clip the corner.
- The hover row is inset 12 px from the popover with its own radius (≈10), concentric with the 20 px outer radius.

## 11. Reproduction recipe
```css
:root{--page:#fafafa;--surface:#fff;--hover:#f2f2f2;--ink:#1c1c1e;--muted:#6e6e73;--line:#e5e5e5;
  --r-pop:20px;--r-row:10px;--fast:100ms;--ease:cubic-bezier(.2,.8,.2,1);}
.chip{display:inline-flex;gap:8px;align-items:center;height:32px;padding:0 12px;border:1px solid var(--line);
  border-radius:9999px;background:var(--surface);font:500 15px/1 -apple-system,"SF Pro Text",Inter,sans-serif}
.chip .dot,.row .dot{width:10px;height:10px;border-radius:50%;background:var(--c)}
.chip-add{background:var(--hover);border-color:transparent}
.popover{width:320px;background:var(--surface);border:1px solid var(--line);border-radius:var(--r-pop);
  box-shadow:0 8px 24px rgba(0,0,0,.06);transform-origin:top left;animation:pop var(--fast) var(--ease)}
@keyframes pop{from{opacity:0;transform:scale(.98) translateY(-4px)}}
.row{display:grid;grid-template-columns:24px 16px 1fr;gap:8px;align-items:center;height:40px;margin:0 8px;
  padding:0 8px;border-radius:var(--r-row)}
.row:hover{background:var(--hover)}
.row .box{visibility:hidden;width:14px;height:14px;border-radius:4px;border:1px solid #c7c7cc}
.row:hover .box,.row[aria-selected=true] .box{visibility:visible}
.row[aria-selected=true] .box{background:var(--ink);border-color:var(--ink)}
.chips{display:flex;gap:8px;justify-content:center}
.chips>*{transition:transform 200ms var(--ease)} /* FLIP via JS on reflow */
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 7 | Tidy neutral UI where colour appears only as dots; competent rather than striking. |
| Originality | 6 | A well-known Linear-style pattern; the inline colour step is the small twist. |
| Usability | 9 | Complete flow, sorted sync, reversible, quick 100 ms feedback. |
| Craft | 8 | Reserved checkbox gutter, concentric radii and sorted chips; the placeholder contrast is the main slip. |

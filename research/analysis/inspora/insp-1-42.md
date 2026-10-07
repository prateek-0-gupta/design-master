---
id: insp-1-42
source: inspora
category: Product
status: analyzed
title: "Morphing braille loader"
creator: "@kianbazza"
styles: [micro-interaction, minimal-swiss, retro-pixel]
patterns: [combobox-create-flow, dot-matrix-loader, icon-morph-tag-spinner-check, status-verb-tense-change, breadcrumb-header-tab, optimistic-dimming-during-async, colour-dot-label-list]
mode: light
palette: ["#ffffff", "#f4f3f3", "#111111", "#7a7a7a", "#e8173a", "#f06010", "#12e05a", "#8b3cf5"]
type_families: ["Inter (likely)"]
type_class: [neo-grotesk]
radius_px: [24, 16, 9999]
motion: {durations_s: [0.1, 0.57, 0.53], easing: [ease-out], loop: false}
scores: {aesthetics: 8, originality: 9, usability: 8, craft: 9}
craft_signals: [braille-grid-morphs-into-check, verb-tense-create-creating-created, list-desaturates-while-pending, tab-header-behind-input-card, live-dot-colour-preview-in-header, caret-colour-accent-blue]
anti_patterns: [placeholder-text-low-contrast]
---
# Morphing braille loader — @kianbazza

## 1. Snapshot
- **Subject:** An 11 s, 2268×2160 capture (with a slow camera zoom) of a label combobox. The user types "D" and chooses "Create new label", then a colour. While the label is saved, a header icon morphs: tag → animated braille dot grid → dot-matrix check mark.
- **Why it's remarkable:** The loader is built from the same dot language as the final icon, so "busy" resolves into "done" without swapping glyphs. The copy changes tense in lockstep: "Create" → "Creating" → "Created".

## 2. Composition & layout
- **Initial popover:** frame at 0.61 s, about 330 px wide at sheet scale. It holds:
  - a search input;
  - three existing labels (dot + name, 40 px rows);
  - "+ Create new label: "D"".
- **Create step:** a tab-like header strip (#f4f3f3) appears *above* the input card, showing a breadcrumb "[icon] Create • Database". The white card (radius ≈24 px in original px) sits on top of it, overlapping by its own corner radius, like a folder tab.
- **Key frame (zoomed):**
  - icon 90×60 px;
  - header text about 70 px at this zoom;
  - colour rows on a 207 px pitch, with 64 px dots and a 140 px text indent.
- **Stage:** a separate 180 px circular "+" button sits to the left on #f8f8f8 as the trigger.

## 3. Typography
- Inter-like neo-grotesk, Regular only.
- **Hierarchy by colour:** the verb "Create" is grey (#7a7a7a) and the object "Database" is near-black (#111). The placeholder "Pick color for label" is grey.
- The blue text caret (≈#3b6cf0) is the only blue in the UI chrome.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #ffffff | card, stage | 93% |
| #f4f3f3 | header tab, hovered row, + button | 3.6% |
| #111111 | primary text, checkbox fill | — |
| #7a7a7a / #8e919e | verb, placeholder | 1% |
| #e8173a, #f06010, #12e05a, #3b82f6, #8b3cf5, #e8177a | label palette (red→pink) | — |

WCAG checks:
- Primary: 18.88:1.
- Grey verb on the tab (#7a7a7a on #f4f3f3): 3.88:1, and on white 4.29:1. Both fail AA-normal, though at UI size (≈15 px real) they are close.
- During "Creating", list text fades to about #c9c9c9 (1.66:1). That is intentional as a disabled state.

## 5. Depth & material
- A flat card with a soft ambient shadow (≈0 8px 30px rgba(0,0,0,.06)) and a 1 px #ececec edge.
- The tab sits behind the card, which gives a two-layer stack without any extra shadow.
- The selected row is a #f4f4f4 pill (radius ≈16 px).
- The final checkbox is a solid #111 rounded square (radius ≈8 px) with a white tick, the darkest object on screen.

## 6. Components & patterns
- **Create-from-search:** typing a non-matching query offers "Create new label: "D"" inline.
- **Two-step create:** name, then colour. The header dot previews the hovered colour live (red → orange → violet across frames 1–4).
- **Async state:** the input placeholder and options dim to about 40% opacity while "Creating". After "Created" the input becomes "Change labels…" and the new label appears checked in alphabetical position.
- **Braille icon:** a 4×5-ish grid of 2–3 px dots. Light-grey dots form the field, and black dots travel around it as the spinner. On success, the black dots settle into a check shape over the grey grid.

## 7. Motion
Measured: duration 11.02 s at 60 fps, motion_fraction 0.14, three segments, all ease-out (fast start):
- 0.70–0.80 s (0.10 s, peak_at 0.17): popover open;
- 2.60–3.17 s (0.57 s, peak_at 0.21): header tab slides in and the list swaps to colours;
- 10.33–10.87 s (0.53 s, peak_at 0.22): final close with blur-out (frame at 10.40 s shows motion blur on the list).

The braille spinner and the slow camera zoom fall below the motion threshold, so they are not segmented. From frames, "Creating" lasts from about 6.7 s to about 8.0 s, and "Created" is shown by 9.18 s (estimate: ~2 s async). All transitions decelerate, which suits UI responding to input.

## 8. Brand system
n/a — this is a product UI, not a brand system. Identity cue: the dot-matrix/braille motif as a system-status language.

## 9. UX
- **Strengths:**
  - Creation never leaves the combobox.
  - The breadcrumb tells you what you're creating and with which colour.
  - The pending state locks the list (dimmed) to prevent double submits.
  - The final state shows the result checked, so the user doesn't need to search again.
- **Weakness:** colour is chosen by name with dots only; there is no custom hex option.

## 10. Craft signals
- The braille grid persists from loader to success (same dot pitch); only the black dots move.
- The verb conjugates with state: Create / Creating / Created.
- Options desaturate (the red dot turns pink-ish, about 50% opacity) while pending, instead of a spinner overlay.
- The header tab is tucked under the card's top radius, not a separate bar.
- The header colour dot updates on hover, before commit.

## 11. Reproduction recipe
```css
:root{--card:#fff;--tab:#f4f3f3;--ink:#111;--muted:#7a7a7a;--caret:#3b6cf0;--r:24px}
.tab{background:var(--tab);border-radius:var(--r) var(--r) 0 0;padding:14px 20px calc(14px + var(--r));display:flex;gap:8px;color:var(--muted)}
.tab b{color:var(--ink);font-weight:400}
.card{background:var(--card);border-radius:var(--r);margin-top:calc(-1*var(--r));box-shadow:0 8px 30px rgb(0 0 0/.06),0 0 0 1px #ececec}
input{caret-color:var(--caret)}
.card[aria-busy=true] .options{opacity:.4;pointer-events:none;transition:opacity .2s ease-out}
.braille{display:grid;grid-template-columns:repeat(4,3px);gap:3px}
.braille i{width:3px;height:3px;border-radius:50%;background:#d4d4d4}
.braille i.on{background:var(--ink)}
.braille[data-state=busy] i{animation:dot 1.2s steps(1) infinite;animation-delay:calc(var(--n)*80ms)}
@keyframes dot{0%,20%{background:var(--ink)}21%{background:#d4d4d4}}
```
JS: on resolve, set `.on` for the check-shape indices and `data-state=done`.

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Quiet, precise light UI. The dot-matrix glyph adds character. |
| Originality | 9 | A loader that morphs into its own success icon, plus tense-changing copy. |
| Usability | 8 | Inline create, clear async state. Greys are slightly under AA. |
| Craft | 9 | Consistent dot grammar, tab-under-card layering, decelerating timing. |

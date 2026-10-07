---
id: insp-8-6
source: inspora
category: Product
status: analyzed
title: "Invoices style"
creator: "@proskuaaa"
styles: [soft-3d, glassmorphism, playful-rounded, micro-interaction]
patterns: [folder-icon-grid, vendor-logo-on-folder, bottom-sheet-with-lifted-object, key-value-detail-list, color-wheel-picker, hex-input-chip, opacity-slider, filter-pill-tabs, grid-list-toggle]
mode: light
palette: ["#ffffff", "#ebebe9", "#999999", "#000000", "#8e8e93", "#2f6bf0", "#a09be8", "#e4ddcd"]
type_families: ["SF Pro Display / Inter-style neo-grotesk (likely)"]
type_class: [neo-grotesk]
radius_px: [48, 28, 9999]
motion: {durations_s: [1.07, 0.47, 0.77, 0.23, 0.3], easing: [ease-in-out, ease-out, ease-in], loop: false}
scores: {aesthetics: 9, originality: 8, usability: 7, craft: 8}
craft_signals: [object-breaks-sheet-top-edge, folder-tint-applied-live, paper-sheet-peeking-from-folder, paid-check-badge-on-paper, dashed-row-dividers, hex-value-shown-uppercase, signature-glyph-on-folder]
anti_patterns: [label-grey-3-3-contrast, scrim-over-content-reduces-context]
---
# Invoices style — @proskuaaa

## 1. Snapshot
- **Subject:** A 12.5 s, 1080×1080 (60 fps) demo of an invoices app.
  - Vendors (Figma, Mobbin, Framer, Dropbox, Amie, OpenAI…) are shown as soft 3D folders with the vendor logo and an invoice count.
  - Tapping "Dropbox" lifts its folder into a bottom sheet of billing details.
  - A palette button then turns the sheet into a colour-wheel picker that recolours the folder live, from #E1E1E1 to #A09BE8.
- **Why it's remarkable:** It turns a dull accounting list into a tactile desk of personalised folders. The selected object physically breaks out of the sheet's top edge, which keeps continuity between grid and detail.

## 2. Composition & layout
- **Phone:** ≈285 px wide in the sheet cell, ≈855 px in the real frame. It zooms to ≈2× for the detail moments.
- **Grid:** two columns of folders ≈115×100 px (sheet scale), each labelled "Name count" beneath. The column gap is ≈10 px.
- **Header:** "Invoices ▾" at ≈26 px Bold (sheet), with All/Paid/Unpaid pill filters below.
- **Bottom bar:** a floating Grid/List segmented pill (left) and a round search button (right), over a white fade.
- **Detail sheet (key frame):**
  - The white sheet is ≈540 px wide with a top radius of ≈48 px. The background is dimmed to #999 grey.
  - The folder (≈280 px) overlaps the sheet's top edge by ~40%.
  - Six key-value rows follow, with dashed dividers: Connected Inbox, Payment Method, Billing Cycle, Currency, Last Invoice, Reminder.
- **Picker mode:**
  - A "HEX ⇕" chip sits beside the value chip "E1E1E1".
  - The hue ring is ≈340 px outer diameter, with an inner saturation/brightness disc of ≈200 px.
  - An Opacity slider pill (32%) sits below.

## 3. Typography
- **Typeface:** neo-grotesk, close to SF Pro Display/Text.
- **Sizes:**
  - The vendor title in the sheet is ≈24 px Semibold (key-frame scale ×2 ≈48).
  - Row labels are grey Regular with a leading outline icon; row values are right-aligned black Medium.
  - Hex values are uppercase.
  - Grid captions are ≈11 px (sheet), with the count in lighter weight after the name.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #ffffff | screens, sheet | ~66% |
| #ebebe9 | default folder grey, chips | ~7% |
| #999999 | dim scrim over the background grid | ~9% |
| #000000 | device bezel, active filter pill | ~3% |
| #8e8e93 | row labels, meta | ~4% |
| #2f6bf0 (est.) | Dropbox logo, confirm check button | ~2% |
| #a09be8 | user-picked folder tint (lavender) | per state |
| #e4ddcd | yellow/cream folder variants | ~1% |

**WCAG:**
- Values are #111 on white: **18.88:1**.
- Labels are #8e8e93: **3.26:1**, which fails for small text.
- The white check on the blue button is **4.69:1**.
- Content under the #999 scrim drops to ~2.85:1, which is intended because it is backgrounded.

## 5. Depth & material
- **Folders:**
  - They are soft 3D with frosted, translucent fronts that blur the paper and logos behind them.
  - A paper sheet peeks from the top-right with a green "paid" check badge.
  - A handwritten signature glyph sits bottom-left, and the logo sticker bottom-right.
  - Each folder casts a soft shadow.
- **Lift into the sheet:** the folder rises and scales up about 2.4×. It appears to rest on the sheet edge, and its shadow falls onto the white.
- **Colour picker:** the hue ring is a full spectrum conic gradient. The thumb is a filled blue disc with a white 3 px ring.

## 6. Components & patterns
- **Grid list:** filter pills, a grid/list toggle, and floating search.
- **Detail sheet:** a palette (customise) button top-left, close × top-right, an editable title (pencil icon), key-value rows, and a chevron on the actionable "Reminder" row.
- **Picker mode:** the top-left becomes undo, the top-right becomes a blue ✓ confirm, and the folder previews the colour live.

## 7. Motion
**Measured:** 12.5 s, motion fraction 0.22, 5 segments, `seamless_loop_likely: false`.

| Time | Duration | Easing | What happens |
|---|---|---|---|
| 1.20–1.43 s | 0.23 s | ease-out | Grid scroll / tap feedback |
| 2.90–3.97 s | **1.07 s** | symmetric ease-in-out (peak 0.42) | Folder lifts from grid, sheet slides up, camera zooms in |
| 5.57–6.03 s | **0.47 s** | ease-out | Sheet content swaps to the colour picker |
| 9.77–10.07 s | 0.30 s | ease-out | Confirm; picker swaps back to details |
| 10.93–11.70 s | **0.77 s** | ease-in (peak 0.67) | Sheet dismisses, folder returns to the grid with its new lavender tint (11.81 s frame) |

- **Hierarchy of durations:** about 1 s for the hero shared-element transition, about 0.5 s for in-sheet swaps, and about 0.25 s for taps.
- **From frames:** the tint changes during 7.6–9 s while the thumb is dragged. The folder colour tracks it in real time.

## 8. Brand system
n/a — not a brand system. Identity cues: folders as the core metaphor, vendor logos as stickers, a signature glyph, and user-chosen folder colours as personalisation.

## 9. UX
- **Strengths:**
  - Recognition via logos.
  - The count per vendor is visible at a glance.
  - The shared-element transition keeps orientation.
  - Billing details are scannable as label/value pairs.
  - Personalisation is optional and hidden behind a palette icon.
- **Risks:**
  - Grey labels fail AA.
  - A full colour wheel is heavy for choosing a folder tint; swatches would be faster.
  - The paid/unpaid status lives in a tiny green badge.
  - The dim scrim hides the grid context.

## 10. Craft signals
- The selected folder overlaps the sheet's top edge, and the sheet's corner radius (≈48 px) visually rhymes with the folder's corner radius.
- Live preview: the folder tint updates continuously during the drag, not on confirm.
- The hex value chip shows uppercase "A09BE8", matching the developer-friendly mode chip "HEX ⇕".
- Dashed dividers separate rows lightly. Labels are left-aligned with icons; values are right-aligned.
- The confirm (✓ blue) and undo (↶ grey) buttons replace palette and close in the same positions, so the controls are stable.
- The paid badge sits on the paper, not the folder, which is semantically accurate.

## 11. Reproduction recipe
```css
:root{--bg:#fff;--folder:#ebebe9;--scrim:rgba(0,0,0,.4);--ink:#111;--ink-2:#8e8e93;--accent:#2f6bf0;
  --r-sheet:48px;--r-folder:28px;--font:"SF Pro Display","Inter",system-ui,sans-serif;}
.folder{--tint:var(--folder);position:relative;width:230px;aspect-ratio:1.15;border-radius:var(--r-folder);
  background:color-mix(in srgb,var(--tint) 75%,transparent);backdrop-filter:blur(14px);
  box-shadow:inset 0 1px 0 rgba(255,255,255,.8),0 12px 24px rgba(0,0,0,.08);transition:background .15s linear}
.folder::before{/* paper peeking */content:"";position:absolute;right:18%;top:-14%;width:45%;height:40%;
  background:#fff;border-radius:8px;transform:rotate(-8deg);z-index:-1}
.sheet{border-radius:var(--r-sheet) var(--r-sheet) 0 0;background:#fff;padding:120px 32px 32px;
  transform:translateY(100%);transition:transform 1.07s cubic-bezier(.65,0,.35,1)}
.sheet.open{transform:none}
.row{display:flex;justify-content:space-between;padding:14px 0;border-bottom:1px dashed #e5e5e5;color:var(--ink-2)}
.row b{color:var(--ink);font-weight:500}
.hue{width:340px;aspect-ratio:1;border-radius:50%;
  background:conic-gradient(red,#ff0,lime,cyan,blue,#f0f,red);
  -webkit-mask:radial-gradient(circle,transparent 58%,#000 59%)}
```
Use a shared-element/View Transition (`view-transition-name: folder-dropbox`) for the grid-to-sheet lift.

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 9 | Charming soft-3D folders on a crisp white UI; a cohesive, premium feel. |
| Originality | 8 | Invoices as personalised vendor folders plus a live-tint picker is a fresh concept. |
| Usability | 7 | Clear details and continuity; low-contrast labels and an over-powered colour picker. |
| Craft | 8 | Careful shared-element choreography and stable control positions. |

---
id: insp-tap-get-invoice
source: inspora
category: Motion
status: analyzed
title: "Tap Get Invoice"
creator: "@ankur5ahu"
styles: [dark-premium, physical-material, editorial-serif, micro-interaction]
patterns: [paper-fold-reveal, row-to-sheet-expansion, hand-drawn-annotation, receipt-layout, floating-download-pill, settings-list-rows]
mode: dark
palette: ["#030303", "#faf6ed", "#d4d1ca", "#6e6668", "#592b1d", "#c0392b"]
type_families: ["Instrument Serif / Newsreader-style display serif (likely)", "Inter (likely)"]
type_class: [editorial-serif, neo-grotesk]
radius_px: [9999, 12, 6, 0]
motion: {durations_s: [0.57, 0.6, 0.6, 0.2, 0.23], easing: [ease-in-out, ease-out], loop: false}
scores: {aesthetics: 8, originality: 8, usability: 7, craft: 8}
craft_signals: [square-paper-corners-vs-rounded-ui, fold-hinge-perspective-shading, red-pen-strike-and-circle, slip-thumbnail-in-row, cream-not-white-paper, background-dims-under-sheet]
anti_patterns: [low-contrast-meta-labels, cropped-heading-behind-sheet]
---
# Tap Get Invoice — @ankur5ahu

## 1. Snapshot
- **Subject:** A 13.9 s, 824×720 screen capture of a dark "Membership" settings screen. Tapping "Get Invoice" makes a tiny folded paper slip unfold upward into a full cream receipt, with red pen marks drawn over the discount and total.
- **Why it's remarkable:** The invoice is treated as a physical object. The row shows a slip thumbnail before the tap, the slip opens in hinged panels, and a hand-drawn strike and circle finish it off.

## 2. Composition & layout
- **Base screen:** One centred column about 355 px wide (x≈165→520 in the 824 px frame), with a "Membership" serif heading at y≈40–95 and six list rows on a ~63 px rhythm (Member, email + Edit, Replay Onboarding, Edit Card, Get Invoice, Library Updates, Need Help?). Each row has a 28 px rounded-square icon tile, a 15 px label and a trailing chevron or value.
- **A decorative rust credit card** (~210×110 px, rotated about −8°) bleeds off the bottom-right corner.
- **Sheet state (key frame):** The receipt is 433×580 px (x 195→628, y 78→658), so it is wider than the list column and overlaps the heading. A "Download PDF" pill (~164×42) floats centred below it at y≈697, half outside the frame.
- **Receipt grid:** 30 px inner padding, a two-column "from / bill to" block split at x≈431, a large empty middle (~190 px tall) and a summary block of three 30 px rows separated by hairlines.

## 3. Typography
- **Display:** a high-contrast serif with a soft, bookish feel, close to Instrument Serif or Newsreader. "Membership" is ~48 px in grey; "Invoice" is ~28 px in near-black.
- **UI:** a neo-grotesk (Inter-like). Receipt meta is ~13 px with grey labels ("Invoice number") and black values. "Total paid" and its amount are ~14 px semibold. List labels are ~15 px regular in #d4d1ca.
- **Numerals:** proportional, not tabular. The amounts right-align, but the digits do not form strict columns.

## 4. Colour
| Hex | Role | Approx share (key) |
|---|---|---|
| #030303 | app canvas | 51% |
| #faf6ed | receipt paper (warm cream) | 39% |
| #d4d1ca | list labels, slip thumbnail | 3% |
| #6e6668 | dimmed heading and icons under the scrim | 1% |
| #592b1d / #25120e | rust card and its shadowed edge | 5% |
| ≈#c0392b | red pen annotations | <1% |

WCAG checks:
- Receipt values #1a1a1a on #faf6ed: 16.14:1.
- Grey meta labels ≈#7a7670 on cream: **4.18:1 (fails AA normal)**.
- List labels #d4d1ca on #030303: 13.53:1.
- Dimmed rows #6e6668 on black: 3.7:1, which is acceptable only because they sit behind a modal.

## 5. Depth & material
- **Paper:** The sheet has square corners (0 px radius) while every UI element is rounded (pills at 9999 px, icon tiles at ~6 px, the Edit chip at ~12 px), so it reads as paper rather than a card.
- **Fold shading:** Mid-unfold (f3, 5.40 s), the top panel tilts back in perspective. It is ~20 px wider at the top edge and carries a light-to-grey gradient along the hinge. The lower panel stays flat.
- **No visible drop shadow:** separation from the background comes purely from the cream against black. The background rows dim to about 40% under the sheet.

## 6. Components & patterns
- **Slip thumbnail:** In the "Get Invoice" row, the chevron is replaced by a ~52×24 px cream rectangle, a preview of the object that will open.
- **Receipt:** logo mark (a 4×2 tile of magenta, mint, red, yellow and blue squares, ~48 px), meta block, "Edit" ghost chip, line items, discount row ("JUNE30 (30% Off)", −$74.70) and a bold total.
- **Red-pen annotation:** A hand-drawn strike through $249.00 and an ellipse around $174.30 are drawn on after the sheet settles (visible at 2.31 s and again at 13.12 s). They point the eye at the saving.
- **Floating "Download PDF" pill:** white, black 15 px text, radius 9999.

## 7. Motion
Measured profile: 13.89 s at 60 fps, `motion_fraction` 0.16, six segments, not a seamless loop (first-to-last difference 103).
- **0.20–0.77 s (0.57 s, peak 0.50, symmetric ease-in-out):** the end of the sheet opening.
- **3.40 s (0.20 s) and 3.80 s (0.10 s), both ease-out:** the sheet collapsing back into the row slip; the snap is fast.
- **5.07–5.67 s (0.60 s, peak 0.53):** unfold. The slip grows from the row, the top panel swings up on a hinge, then the lower panel extends. This matches f3.
- **8.13 s (0.23 s, ease-out):** dismiss.
- **9.87–10.47 s (0.60 s, peak 0.47):** a third unfold. f6 at 10.03 s shows a mid-state grey (#e6e4de) half-folded slip over the rows.
- **Annotations:** The red marks appear after the 0.6 s unfold. Estimated at about 0.4–0.6 s of stroke drawing, but too small to register as a separate segment.
- **Summary:** opening is slow and symmetric (0.6 s) while closing is fast ease-out (0.2 s), which is the right asymmetry.

## 8. Brand system
n/a — not a brand system. Identity cues:
- the multicolour tile logomark (Interface Craft);
- the editorial serif heading;
- a warm rust accent card that echoes the red pen.

## 9. UX
- **Strengths:**
  - The slip thumbnail tells the user an object will appear, and the unfold makes the origin of the sheet obvious.
  - The red annotation answers "what did I pay?" instantly.
  - "Download PDF" is the only action.
- **Risks:**
  - The sheet covers the heading with no visible close control or scrim tap target.
  - The large empty middle of the receipt wastes ~190 px.
  - The red pen relies on colour plus shape. The shape (strike, circle) carries the meaning, so it survives colour blindness.

## 10. Craft signals
- The receipt uses 0 px corners against a fully rounded UI, so the material reads as different.
- A perspective hinge gradient appears on the top fold panel at 5.40 s.
- The red strike and circle are imperfect hand strokes, not vector ellipses: the circle overshoots its start at the right.
- The cream #faf6ed is used instead of #fff, so the paper is warm on black.
- The row's trailing slip previews the destination object.
- The close is roughly 3× faster than the open (0.2 s vs 0.6 s, measured).

## 11. Reproduction recipe
```css
:root{--bg:#030303;--paper:#faf6ed;--ink:#1a1a1a;--meta:#6f6b65;--label:#d4d1ca;--pen:#c0392b;
  --serif:"Instrument Serif","Newsreader",Georgia,serif;--sans:"Inter",system-ui,sans-serif}
.receipt{width:433px;background:var(--paper);color:var(--ink);padding:30px;border-radius:0;
  transform-origin:50% 100%;perspective:900px}
.receipt .fold-top{transform-origin:50% 100%;animation:unfold .6s cubic-bezier(.45,0,.55,1) both;
  background:linear-gradient(180deg,#fff 0%,#e9e6df 100%)}
@keyframes unfold{from{transform:rotateX(-170deg)}to{transform:rotateX(0)}}
.receipt.closing{animation:collapse .2s cubic-bezier(.2,.8,.2,1) both}
@keyframes collapse{to{transform:scale(.12,.04);opacity:0}}
.pen path{stroke:var(--pen);stroke-width:1.6;fill:none;stroke-dasharray:var(--len);
  stroke-dashoffset:var(--len);animation:draw .45s .6s ease-out forwards}
@keyframes draw{to{stroke-dashoffset:0}}
.pill{border-radius:9999px;background:#fff;color:#111;padding:10px 24px;font:500 15px var(--sans)}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Black, cream and rust with a serif display is warm and restrained. |
| Originality | 8 | The paper-fold receipt with pen annotations is a fresh take on the modal sheet. |
| Usability | 7 | The origin is clear and the total is emphasised. There is no visible close and meta labels are under AA. |
| Craft | 8 | The material contrast, hinge shading and open/close asymmetry are deliberate. Proportional numerals are a miss. |

---
id: insp-1-5
source: inspora
category: Product
status: analyzed
title: "Date picker"
creator: "@malikyoloo"
styles: [playful-rounded, micro-interaction, photo-led]
patterns: [week-strip-date-picker, pill-day-cells-with-indicator, merchant-icon-as-event-dot, detached-detail-card, segmented-tabs, card-over-landscape-backdrop, emphasised-count-in-sentence]
mode: light
palette: ["#ffffff", "#f7f7f7", "#1c1c1c", "#9aa0a6", "#1ed760", "#3b82f6", "#8b3cf5", "#6c732b"]
type_families: ["Inter / SF Pro-style neo-grotesk (likely)"]
type_class: [neo-grotesk]
radius_px: [48, 28, 9999]
motion: {durations_s: [0.27, 0.27, 0.27, 0.27, 0.3], easing: [ease-out], loop: false}
scores: {aesthetics: 8, originality: 6, usability: 7, craft: 8}
craft_signals: [selected-pill-inverts-to-black, empty-day-dashed-circle, weekday-letter-bolds-with-selection, card-recentres-when-detail-hides, bold-number-in-grey-sentence, same-ease-out-every-transition]
anti_patterns: [grey-helper-text-fails-aa, no-week-navigation]
---
# Date picker — @malikyoloo

## 1. Snapshot
- **Subject:** A 7.1 s, 1920×1440 capture of a "Bills" widget: a single-week strip (Mon 9 – Sun 15) where each day shows the brand icon of a bill due (Spotify, iCloud, Internet). Selecting a day pops a detached detail card underneath ("Spotify membership $9.99, Mar 10, Subscriptions").
- **Why it's remarkable:** Event dots are replaced by actual merchant icons, so the week reads as "what's due when" without opening anything. The selected day inverts into a black capsule.

## 2. Composition & layout
- **Card:** white, about 914×732 px on the key frame (x 503→1417, y 347→1079), radius about 48 px, floating over a soft-focus grassland photo.
- **Header:** "Bills" ≈44 px Semibold at the left, and two 92 px circular icon buttons (help, settings) on #f2f2f2.
- **Segmented control:** "Upcoming Bills" (active: white with 1 px border and shadow) / "All Bills" (grey) on a #f2f2f2 track. A "Sort ⌄" outline pill is right-aligned.
- **Helper sentence:** about 30 px.
- **Week strip:** a #f7f7f7 well (radius ≈36 px) containing seven pill cells, each about 94×136 px on a 114 px pitch, with a weekday letter above each.
- **Detail card:** separate, about 610 px wide in sheet scale, radius about 28 px, 16 px below the main card. It holds a 56 px merchant icon tile, name and date on the left, and amount and category on the right.

## 3. Typography
- An Inter / SF Pro-like grotesk.
- **Weights:** Semibold for the title and amounts; Medium for active tab and date numerals; Regular for helper text.
- **Sentence emphasis:** "You have **3 bills** due within the next 7 days". The count is #111 Semibold inside a #9aa0a6 sentence.
- The weekday letter of the selected day turns black and bold ("F" at 3.55 s); the others stay grey.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #ffffff | card, day pills | 22% |
| #f7f7f7 / #f2f2f2 | week well, tab track, icon buttons | — |
| #1c1c1c | selected day pill, text | — |
| #9aa0a6 | helper text, inactive tab | — |
| #1ed760 / #3b82f6 / #8b3cf5 | merchant icons (Spotify, iCloud, Internet) | — |
| #6c732b / #a29845 / #b9c1be | backdrop grass and sky | ~45% |

WCAG checks:
- Text #111 on white: 18.88:1.
- Selected numeral (white on #1c1c1c): 17.04:1.
- **Helper grey #9aa0a6 on white: 2.64:1 (fails)**, and this sentence carries meaning.
- Inactive tab #8a8a8a on #f2f2f2: 3.08:1.

## 5. Depth & material
- The card has a soft long shadow (≈0 30px 80px rgba(0,0,0,.12)) over the photo, which gives a floating-widget feel like a macOS/iOS widget.
- Day pills are white on the #f7f7f7 well with a faint shadow (≈0 1px 2px rgba(0,0,0,.05)), slightly raised.
- The selected pill is a solid #1c1c1c with no shadow, and the active tab is white with a 1 px border.
- Empty days show a 30 px dashed-outline circle in place of an icon.

## 6. Components & patterns
- **Week strip** of pill cells: number plus indicator slot. The slot holds either a merchant icon (≈34 px) or a dashed empty circle.
- **Detail card:** appears only when the selected day has a bill. Selecting an empty day (12, 13, 14) removes it, and the main card re-centres vertically (it moves down about 32 px at sheet scale between frames 0.39 s and 1.97 s).
- Segmented tabs plus a sort dropdown.

## 7. Motion
Measured: duration 7.1 s at 30 fps, motion_fraction 0.20, five segments, each 0.27–0.30 s with peak_at 0.17–0.19, all ease-out:
- 1.20 s, 2.23 s, 3.20 s, 5.23 s and 6.20 s.

One consistent transition token (about 280 ms, fast-start decelerate) is used for every selection change: the pill fill moves, the detail card enters or exits, and the card shifts position. seamless_loop_likely is false. From the frames, the black pill appears to jump to the new day rather than slide across (no intermediate positions captured).

## 8. Brand system
n/a — this is a product UI, not a brand system. Identity cues: black-and-white UI chrome that lets third-party brand icons supply all the colour, and a pastoral photo backdrop to soften a finance task.

## 9. UX
- **Strengths:**
  - Bills are visible at a glance.
  - One tap gives details.
  - Clear selection.
  - The helper sentence summarises.
- **Weaknesses:**
  - There is no way to move to the previous or next week.
  - Multiple bills on one day aren't shown.
  - The helper text is too faint.
  - The layout jump when the detail card hides could disorient a user.

## 10. Craft signals
- The selected pill inverts fully (black fill, white numeral), and its weekday letter also bolds.
- Empty days use a dashed circle the same size as the icons, so the rhythm holds.
- The emphasised count is in a darker weight inside the grey sentence.
- All five transitions share one 0.27–0.30 s ease-out curve.
- The card radius (≈48 px) is greater than the well radius (≈36 px), which is greater than the pill radius (full); the nesting is consistent.

## 11. Reproduction recipe
```css
:root{--card:#fff;--well:#f7f7f7;--track:#f2f2f2;--ink:#1c1c1c;--muted:#9aa0a6;--ease:cubic-bezier(.2,.8,.2,1);--t:.28s}
.bills{background:var(--card);border-radius:48px;padding:40px;box-shadow:0 30px 80px rgb(0 0 0/.12);transition:transform var(--t) var(--ease)}
.week{background:var(--well);border-radius:36px;padding:20px;display:grid;grid-template-columns:repeat(7,1fr);gap:20px}
.day{background:#fff;border-radius:9999px;height:136px;display:grid;place-items:center;font:500 32px Inter;
  box-shadow:0 1px 2px rgb(0 0 0/.05);transition:background var(--t) var(--ease),color var(--t) var(--ease)}
.day[aria-selected=true]{background:var(--ink);color:#fff}
.day .slot:empty{width:30px;height:30px;border-radius:50%;border:1.5px dashed #d0d0d0}
.helper{color:var(--muted)}.helper b{color:#111;font-weight:600}
.detail{border-radius:28px;background:#fff;animation:pop var(--t) var(--ease)}
@keyframes pop{from{opacity:0;transform:translateY(-8px) scale(.98)}}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Soft, friendly widget with a pleasing photo backdrop. |
| Originality | 6 | Week strip plus icon dots is familiar. Merchant icons as indicators is the twist. |
| Usability | 7 | Glanceable and simple. Faint helper text, no week navigation. |
| Craft | 8 | Consistent radii nesting and a single motion token. |

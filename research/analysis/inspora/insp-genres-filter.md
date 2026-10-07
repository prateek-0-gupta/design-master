---
id: insp-genres-filter
source: inspora
category: Motion
status: analyzed
title: "Genres filter"
creator: "@proskuaaa"
styles: [dark-premium, micro-interaction, kinetic-type, spatial-ui]
patterns: [dual-cylinder-picker, transfer-list, inline-expanding-row, filter-sheet, count-in-cta, summary-with-plus-n, plus-icon-add-affordance]
mode: dark
palette: ["#1a1a1a", "#060606", "#232323", "#f6f6f6", "#1a5cff", "#778ab2", "#8e8e93", "#ffffff"]
type_families: ["SF Pro Text / Display (likely)"]
type_class: [neo-grotesk]
radius_px: [20, 16, 9999]
motion: {durations_s: [0.67, 0.13, 0.2, 0.73], easing: [ease-out, ease-in-out], loop: true}
scores: {aesthetics: 8, originality: 9, usability: 6, craft: 8}
craft_signals: [opposing-curvature-wheels, text-follows-cylinder-arc, edge-fade-on-wheel, two-tone-cta-label, row-summary-updates-plus-n, camera-zoom-into-expanded-row]
anti_patterns: [cta-count-low-contrast, rotated-text-hard-to-scan, count-not-updated-in-cta]
---
# Genres filter — @proskuaaa

## 1. Snapshot
- **Subject:** A 6.4 s, 60 fps, 1440×1440 iPhone demo of an events "Filters" sheet. The "Genres" row expands into two curved 3D drum lists:
  - on the left, the selected genres (Afrobeat, Bluegrass, Chant, EDM);
  - on the right, the available genres with blue "+" icons (Disco, Electronic, Experimental, Folk…).
- Tapping "+ Folk" moves it to the left wheel and the summary updates to "Afrobeat, Folk +7".
- **Why it's remarkable:** It reinvents the classic transfer list (available ↔ selected) as two iOS-style picker cylinders that bulge in opposite directions, like facing pages of a rolodex. The spatial metaphor makes "move across" literal.

## 2. Composition & layout
- **Sheet:** Filters on #1a1a1a with six stacked rows (Location, Dates, Friends attend, Genres, Time, Price). Each row is about 56 pt tall, radius about 16 pt, fill #232323, with a 12 pt gap. The row label (grey icon plus label) is on the left and the value (white) on the right.
- **Footer:** "Reset all" ghost text on the left and the pill CTA "Continue with 4" on the right (about 150×44 pt, blue).
- **Expanded Genres row:** about 3.4× taller. An inner dark well (#141414, radius about 16 pt) holds the two wheels: the selected list centred at about 40% x and the available list at about 65% x, with about 8 visible items per wheel.
- **Camera:** the video zooms into the phone (0.36 s → 1.07 s) to show the wheels at legible size, then zooms back out (5.33 → 6.04 s).

## 3. Typography
- SF Pro throughout.
  - Row labels: about 15 pt Regular #8e8e93. Values: 15 pt Regular white. The "+6" count is grey.
  - Wheel items: about 17 pt Medium white, foreshortened and rotated along the cylinder. Items rotate up to about ±25° and fade toward the ends.
  - CTA: "Continue" in white plus "with 4" in light-blue (#8ea6ff-ish), a two-tone label that separates the action from the meta.

## 4. Colour
| Hex | Role | Approx share |
|---|---|---|
| #f6f6f6 | presentation stage | 37% |
| #1a1a1a | sheet background | 51% |
| #232323 | row surfaces | — |
| #060606 / #141414 | phone bezel, wheel well | 5% |
| #1a5cff | CTA fill, "+" icons | 2% |
| #778ab2 | "MT" avatar, blue tints | 4.6% |
| #8e8e93 | labels | — |

WCAG checks:
- White on CTA #1a5cff is 5.23:1.
- "with 4" (#8ea6ff) on blue is **2.25:1 (fail)**.
- Labels #8e8e93 on #1f1f1f are 5.06:1.
- Values white on #1f1f1f are 16.48:1.
- Blue "+" icons (#2f6bff on #141414) are 4.1:1, which is acceptable for graphics (≥3:1).

## 5. Depth & material
- Flat dark surfaces with steps #141414 → #1a1a1a → #232323. There are no shadows except a soft blurred band behind "Reset all" (a frosted footer).
- **The wheels are pseudo-3D:**
  - text is perspective-rotated and scaled along concave arcs;
  - the left wheel bulges left and the right wheel bulges right, so they read like two drums seen from between them;
  - items fade to about 20% opacity at the top and bottom.

## 6. Components & patterns
- **Filter sheet:** label-value rows that expand inline (accordion) rather than pushing a new screen.
- **Transfer list as twin pickers:** the right wheel adds (each item has a ⊕ icon) and the left shows the current selection.
- The summary string truncates to two names plus "+N".
- **Friends attend:** an avatar stack (an "MT" initials avatar plus photo avatars) with a count.
- The CTA carries a count ("with 4"), though it stays "4" even as genres change (the count likely refers to results or other filters).

## 7. Motion
- **Measured:** 6.4 s with motion fraction 0.26 and `seamless_loop_likely: true`. Four segments:
  - 0.87–1.53 s (0.67 s, ease-out, peak 0.07): the zoom-in plus the row expanding into wheels. The fast start reads as a spring.
  - 2.03–2.17 s (0.13 s, ease-out): a wheel flick.
  - 4.60–4.80 s (0.2 s, symmetric): tapping "+ Folk". The item moves to the left wheel.
  - 5.03–5.77 s (**0.73 s**, ease-out, peak 0.16): collapse plus zoom-out back to the full sheet.
- **From frames (estimate):** between 2.49 and 3.91 s the right wheel scrolls about two items (Dancehall → Disco centred) with momentum. "Folk" migrates across and the left wheel re-sorts alphabetically (Afrobeat, Folk, Bluegrass…).

## 8. Brand system
n/a — not a brand system. Product cues:
- an iOS-native dark sheet with a single electric-blue accent (#1a5cff);
- "+N" summaries;
- a count in the CTA.

## 9. UX
- **Strengths:**
  - Selected and available genres are visible at once.
  - The add action is explicit (⊕).
  - The inline expansion keeps context.
  - The summary row updates immediately.
- **Risks:**
  - Rotated, perspective text is slower to scan than a flat list, so with 20+ genres the cylinders hide most options.
  - Removal affordance on the left wheel is not shown (no ⊖).
  - Two-tone CTA text fails contrast.
  - Wheels are hard to operate with VoiceOver. A flat checklist fallback is needed.

## 10. Craft signals
- The two wheels curve in opposite directions (mirror cylinders) and share a centre line at y = "Folk".
- Each item's ⊕ icon rotates with its label along the arc, not separately.
- Edge items fade and squash, faking cylinder depth without real 3D.
- The CTA label is two-tone: the verb is white and the meta is tinted, all in one pill.
- The summary text changes from "Afrobeat, Bluegrass +6" to "Afrobeat, Folk +7" after the add, so state propagates to the collapsed row.
- The presentation zooms into the phone exactly while the row is expanded, guiding attention.

## 11. Reproduction recipe
```css
:root{--sheet:#1a1a1a;--row:#232323;--well:#141414;--label:#8e8e93;--text:#fff;--accent:#1a5cff;--accent-soft:#c7d4ff;
  --r-row:16px;--font:-apple-system,"SF Pro Text",system-ui,sans-serif}
.row{background:var(--row);border-radius:var(--r-row);padding:16px;display:flex;justify-content:space-between;font:400 15px var(--font)}
.row .label{color:var(--label)}
.row[aria-expanded=true]{animation:expand .67s cubic-bezier(.16,1,.3,1)}
.wheel{perspective:600px;height:260px;overflow:hidden;
  -webkit-mask:linear-gradient(transparent,#000 25%,#000 75%,transparent)}
.wheel li{font:500 17px var(--font);color:var(--text);height:36px;
  transform-origin:var(--origin) 50%;                 /* left wheel: 100%, right wheel: 0% */
  transform:rotateX(calc(var(--d)*-18deg)) rotateY(calc(var(--d)*var(--dir)*10deg)) translateX(calc(var(--d)*var(--d)*var(--dir)*6px));
  opacity:calc(1 - abs(var(--d))*.2)}
.cta{background:var(--accent);color:#fff;border-radius:9999px;padding:12px 20px;font:500 17px var(--font)}
.cta span{color:var(--accent-soft)} /* #c7d4ff on #1a5cff ≈ 3.9:1, better than the original */
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Polished iOS dark sheet. The mirrored cylinders are visually striking. |
| Originality | 9 | A transfer list rendered as twin opposing picker drums is a genuinely new control idea. |
| Usability | 6 | Selection versus availability is clear, but curved text slows scanning, there is no remove affordance and accessibility is a concern. |
| Craft | 8 | Consistent radii, state propagating to the summary and well-choreographed zoom. The CTA meta text is under-contrasted. |

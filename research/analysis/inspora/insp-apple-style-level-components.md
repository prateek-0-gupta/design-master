---
id: insp-apple-style-level-components
source: inspora
category: Motion
status: analyzed
title: "apple style level components"
creator: "Elia (@eliakuratli)"
styles: [corporate-clean, minimal-swiss, micro-interaction, photo-led]
patterns: [folder-fan-out-hover, wallet-card-stack, cover-flow-carousel, time-zone-dial, stat-row-key-value, pill-ghost-buttons, page-dots-active-bar, component-showcase-reel]
mode: light
palette: ["#ffffff", "#f6f6f6", "#111111", "#737373", "#8a8a8a", "#e8f4ea", "#168713", "#f3d6ec"]
type_families: ["Inter / SF Pro Text (likely)", "Inter Display tight (likely) for captions"]
type_class: [neo-grotesk]
radius_px: [9999, 24, 16, 12]
motion: {durations_s: [0.27, 0.3, 0.53, 0.4, 0.47, 0.67, 0.27], easing: [ease-out, ease-in-out], loop: false}
scores: {aesthetics: 8, originality: 6, usability: 8, craft: 9}
craft_signals: [cover-flow-reflection, active-dot-becomes-bar, tabular-time-with-small-ampm, folder-tint-matches-content, two-tone-caption-name-pro, dial-arc-for-work-hours]
anti_patterns: [secondary-grey-near-aa-threshold, cursor-faint-in-light-ui]
---
# apple style level components — Elia

## 1. Snapshot
- **Subject:** A 22.4 s, 1920×1080 promo reel for a "Pro" component library (uiarc.dev) showing four interactive components:
  - Folder stack;
  - Wallet stack;
  - Cover flow;
  - Time dial.

  It ends on the end card "Everyday magic".
- **Why it's remarkable:** It revives Apple's skeuomorphic-era interactions (Cover Flow, Wallet, Finder folders) in today's flat iOS idiom, with photo-real content and tight data typography.

## 2. Composition & layout
- **Frame:** a white canvas with the component centred in the upper two-thirds. A caption sits bottom-left at x≈105, baseline y≈1005: "Cover flow" in black plus "Pro" in grey.
- **Cover flow (key frame):**
  - Centre card about 330×420 px. Flanking cards are rotated in Y by about 40–50° and overlap by about 50%.
  - The row spans x 480–1450. A mirrored reflection about 50 px deep fades under the cards.
  - Below it: title + location, then 7 page dots (the active one is a 16 px bar), a 1 px divider, then a 3-up stat row (label 17 px grey over value 26 px black) and a ghost pill "Save hike" right-aligned.
- **Time dial (f6):** a two-column layout with a 460 px dial on the left and a 4-row city list on the right. The selected row sits in a #f6f6f6 pill (radius about 24 px). A footer row has "1 of 4 offices at work" plus two ghost pills.
- **Wallet (f2, f3):** a 4-card stack with only the 30 px headers visible. The tapped card expands into a detail view with spend and transactions.

## 3. Typography
- A neo-grotesk, Inter or SF Pro.
  - Captions: about 64 px Medium with tight tracking (about −0.03 em).
  - Card titles: about 26 px Medium. Secondary: about 20 px Regular in #737373.
- **Times:** "12:30" is set at about 30 px (list) and about 60 px (dial) with tabular figures, and the AM/PM suffix is at about 50% size. This is Apple's Clock-app treatment.
- **Money:** "$1,286.44" is about 26 px, right-aligned. Positive amounts are green ("+$64.00").
- **End card:** "Everyday magic" about 90 px Semibold, "Pro components on uiarc.dev" about 36 px.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #ffffff | canvas | 77% |
| #f6f6f6 | selected row, button fill | 2% |
| #111111 | primary text, active dot | 4% |
| #737373 | secondary labels | 2% |
| #8a8a8a | "Pro" caption suffix | <1% |
| #e8f4ea / #168713 | dial work-hours arc / active-office dot | 1% |
| #f3d6ec | folder (moodboard pink) | — |
| card hues | Common Ground green, Tidewater mint, Meridian black, Fieldnote brushed silver | — |

WCAG:
- Primary #111 on white is 18.88:1, and secondary #737373 is 4.74:1 (pass).
- The "Pro" suffix #8a8a8a is 3.45:1 (large display, passes large).
- Stat labels around #8d8d8d are **3.29:1 (fail at 17 px)**.

## 5. Depth & material
- **Folder:** pale pink translucent with a soft inner gradient. Photos fan out behind it with a 2–4 px shadow.
- **Wallet cards:** each has its own material: matte green, mint, black with a fine guilloché texture, and brushed aluminium with a conic sheen. All have a 12 px radius and a gold chip.
- **Cover flow:** perspective transforms plus a floor reflection (about 30% opacity, fading to 0 within about 50 px).
- **UI chrome:** flat, with 1 px #e5e5e5 borders on ghost pills.

## 6. Components & patterns
- **Folder stack:** hover fans 5 photos out of the folder in an arc. The counter reads "7 files".
- **Wallet stack:**
  - "Jordan's cards · 1 of 4" header.
  - Tapping a card pulls it forward, the others collapse, and an "All cards" back pill appears.
- **Cover flow:** drag or click to rotate. The page dots morph so the active dot becomes a bar. Clicking "Save hike" toggles it to a black filled "Saved" pill (f5).
- **Time dial:**
  - The rotating hand sets home time.
  - A green arc marks working hours, and city markers sit on rings.
  - Rows show the delta ("3 h behind") and a "−1 day" chip, with day/night icons per city.

## 7. Motion
The motion is measured: 22.44 s, 60 fps, motion_fraction 0.23, not a loop. There are 17 segments with a **median of 0.27 s** (range 0.10–0.67 s).
- About half peak early (peak_at 0.10–0.25, ease-out), such as the card pull at 7.53 s (0.40 s) and the cover-flow advances at 9.40 s and 10.17 s (0.47 s, 0.27 s).
- The rest are symmetric: the folder fan at 3.37 s (0.53 s) and the dial sweeps at 4.50–6.70 s (0.23–0.30 s).
- The longest is 10.57–11.23 s (0.67 s, ease-out), a multi-card cover-flow swipe.
- f7 (18.7 s) is near-blank white: a fade-through-white transition to the end card.

These short (≤0.3 s) ease-out springs are the right register for Apple-like UI.

## 8. Brand system
n/a — not a brand system. The uiarc.dev end card has a 3-arch "∩" logomark and a "Name **Pro**" two-tone caption system.

## 9. UX
- The components are realistic and data-complete: units, deltas, back navigation, toggled states.
- Selected states use fill (#f6f6f6 row) rather than colour.
- The "−1 day" chip pre-empts confusion.
- Weak points: faint grey labels, and the cover flow has no visible arrows (discoverability relies on drag).

## 10. Craft signals
- The active page dot is a 16×6 px bar while the inactive dots are 6 px circles.
- AM/PM is set at about 50% size beside tabular times.
- The cover flow has a true floor reflection that fades out under the cards.
- The work-hours arc on the dial uses a tint (#e8f4ea) while the active-office dot uses the saturated #168713.
- Each wallet card has a distinct material (guilloché, brushed metal), not just a different colour.
- Captions are two-tone: name in #111 and "Pro" in #8a8a8a at the same size.

## 11. Reproduction recipe
```css
:root{--bg:#fff;--fill:#f6f6f6;--text:#111;--text-2:#737373;--border:#e5e5e5;--ok:#168713;--ok-tint:#e8f4ea}
body{font-family:Inter,"SF Pro Text",system-ui;color:var(--text);background:var(--bg)}
.time{font-variant-numeric:tabular-nums;font-size:30px;font-weight:500}.time small{font-size:.5em;margin-left:4px}
.row[aria-selected=true]{background:var(--fill);border-radius:24px}
.pill{border:1px solid var(--border);border-radius:9999px;padding:12px 20px}
.dots i{width:6px;height:6px;border-radius:3px;background:#c7c7c7;transition:width .27s cubic-bezier(.2,.8,.2,1)}
.dots i.on{width:16px;background:var(--text)}
.coverflow{perspective:1200px;display:flex}
.coverflow .card{border-radius:16px;transform:rotateY(var(--ry)) translateZ(var(--z));-webkit-box-reflect:below 4px linear-gradient(transparent 85%,rgba(0,0,0,.25));transition:transform .4s cubic-bezier(.2,.8,.2,1)}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Calm white canvas, rich photography and tidy type. Polished, if expected. |
| Originality | 6 | Faithful revivals of Apple patterns rather than new ideas. |
| Usability | 8 | States, deltas and back paths are all present, and the motion is short and purposeful. Some grey labels are weak. |
| Craft | 9 | Reflection, dot morphing, tabular times and per-card materials show very high finish. |

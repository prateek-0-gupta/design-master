---
id: insp-ai-scheduler
source: inspora
category: Product
status: analyzed
title: "AI scheduler"
creator: "@fayazara"
styles: [minimal-swiss, corporate-clean, micro-interaction]
patterns: [natural-language-command-bar, inline-entity-tokens, multi-person-availability-timeline, suggested-slot-chips, drag-to-select-slot, conflict-state-red, stepper-duration-control]
mode: light
palette: ["#ffffff", "#e7ecec", "#a5b0c1", "#eefbf7", "#3b82f6", "#2f55d4", "#1f1f1f"]
type_families: ["SF Pro Text / Inter (likely)"]
type_class: [neo-grotesk]
radius_px: [32, 16, 12, 9999]
motion: {durations_s: [0.47, 0.3, 0.23, 0.17, 0.27, 0.37], easing: [ease-out, ease-in-out], loop: false}
scores: {aesthetics: 7, originality: 7, usability: 8, craft: 8}
craft_signals: [entity-tokens-tinted-in-input, colour-coded-left-rule-on-summary, time-flag-on-drag-handle, conflict-turns-slot-red, keyboard-hint-on-book-button, checking-calendars-skeleton-rows]
anti_patterns: [light-grey-secondary-text-fails, white-on-mid-blue-button-below-4-5]
---
# AI scheduler — @fayazara

## 1. Snapshot
- **Subject:** A 28.2 s screen recording (3340×2160, 60 fps) of a command-bar scheduler. The user types "meeting with jilles and harshil", people are resolved into tokens, a three-row availability timeline appears, and the user drags a slot, hits a conflict, and picks a suggested time.
- **Why it's remarkable:** Natural-language input and a direct-manipulation timeline share one card. Every parse result (person, time, duration) is shown immediately and stays editable.

## 2. Composition & layout
- A single card about 1270×950 px in the 2000-px-wide key frame (≈2120×1590 at native) is centred on white.
- **Header row:** a 70 px icon tile, the input, and a return-key button on the right. A 1 px divider follows.
- **Body:** "Tomorrow 30 Sep" with prev/next circular buttons, then the timeline grid. The name column is about 290 px wide; 9 hour columns (9 to 6) are about 98 px each.
- **Below the grid:** the "Everyone's free at" chip row, then a nested summary card (radius ≈24 px) with stepper controls and a Book button.
- **Vertical rhythm:** rows are about 93 px tall; section gaps are 40–60 px. Density is medium.

## 3. Typography
- System neo-grotesk, very close to SF Pro Text (round dots, compact "a").
- **Input:** about 36 px Medium in the key frame.
- **Section title:** "Tomorrow" about 28 px Semibold next to a lighter grey "30 Sep" at the same size, so hierarchy comes from value, not size.
- **Names:** 24 px Semibold, with 20 px grey subtitles (city or email, truncated with an ellipsis).
- **Hour axis:** about 20 px grey tabular numerals.
- **Summary:** title 30 px Semibold, meta line 24 px grey with "·" separators.
- The scale is roughly 36/30/24/20, about a 1.2 ratio.

## 4. Colour
| Hex | Role | Approx share |
|---|---|---|
| #ffffff | canvas and card | 91% |
| #e7ecec | grid lanes, busy blocks, borders | 6% |
| #a5b0c1 | secondary text, axis, icons | 2% |
| #eefbf7 / ≈#d6f3e4 + ≈#4cc38a | selected slot fill / chip, green left rule | <1% |
| ≈#3b82f6 | Book button | <1% |
| ≈#2f55d4 on #e6edfb | person entity tokens | <1% |
| ≈#d8435a | conflict slot and rule | transient |

WCAG checks (contrast.py):
- Primary text #1f1f1f on white: **16.48:1**.
- Grey "30 Sep" ≈#a3a3a3: **2.52:1 (fail)**.
- Email subtitle ≈#8a8a8a: **3.45:1** (large only).
- White on Book #3b82f6: **3.68:1** (passes only as large/bold text).
- Green chip text #2f8a5a on #d6f3e4: **3.63:1**.
- Token blue #2f55d4 on #e6edfb: **5.3:1** (pass).
- Conflict message ≈#b4232f: **6.52:1**.

## 5. Depth & material
- The card has a very soft, wide shadow (about 0 30px 60px rgba(0,0,0,.08)) and a 1 px #e7ecec border. The inner summary card uses a border only.
- The selected slot is a translucent green column with a 2 px green stroke spanning all three lanes. The Book button has a slight inner top highlight.
- Everything else is flat.

## 6. Components & patterns
- **NL command bar:** recognised entities get a pale blue tinted background behind the word ("jilles", "harshil"), like inline mentions.
- **Empty state:** "Try one" suggestions with spark bullets. Entities in the suggestions are colour-coded by type: people in blue, time in orange, duration in green.
- **Availability grid:** lanes per person with grey busy blocks. While loading, the lanes are grey skeletons and the label reads "Checking calendars…".
- **Slot:** draggable. A time flag ("10:45 AM") rides on top while dragging. It turns red with "You already have something then" on conflict.
- **Suggested chips:** "Everyone's free at 11:00 AM / 2:30 PM / 3:30 PM"; the selected chip turns green.
- **Summary card:** coloured left rule (green ok, red conflict, grey pending), avatar stack, video toggle, −/30 min/+ stepper, and "Book ↵".

## 7. Motion
- Measured: 28.2 s, `motion_fraction` 0.08, 9 short segments with a median of **0.23 s**. Most are **ease-out (peak_at 0.10–0.31)**: 0.47 s at 0.97 s (results panel), 0.30 s, 0.17 s, 0.27 s. A symmetric 0.37 s ease-in-out at 21.5 s matches the slot jumping to a new time.
- The loop is not seamless (`first_last_diff` 10.29).
- Visible sequence (frame estimates): suggestions at 1.6 s → typed query and timeline at 4.7 s → skeleton "Checking calendars" at 7.8–11.0 s → green slot at 14.1 s → drag with flag at 17.2 s → red conflict at 20.4 s → 3:45 PM at 23.5 s → 11:00 AM chip chosen at 26.7 s.
- The UI itself animates briefly and crisply. Most of the time is spent on user input.

## 8. Brand system
n/a — not a brand system. The calendar-plus icon tile in pale blue is the only identity cue.

## 9. UX
- Strong: parse feedback is immediate and inspectable. Conflicts are explained in words and colour. Every value has a direct control (stepper, chips, drag). Keyboard-first (the ↵ glyph on the Book button and on the input).
- **Risks:**
  - Pale greys fail AA for the date and emails.
  - Green and red rely on hue, although the red state adds a message.
  - Emails are truncated with no tooltip shown.

## 10. Craft signals
- Entity tokens are highlighted inside the live text input, not converted to chips, so the text stays editable.
- The left rule colour on the summary card mirrors the slot state (green, red, grey).
- The drag flag snaps to 15-minute increments (10:45, 12:30, 3:45 observed).
- Skeleton lanes keep their exact grid geometry while loading, so nothing shifts.
- The stepper, chips and buttons share one pill radius. Cards use about 24–32 px.

## 11. Reproduction recipe
```css
:root{--bg:#fff;--line:#e7ecec;--ink:#1f1f1f;--ink-2:#6b7280;--busy:#e3e6e8;
  --ok:#4cc38a;--ok-bg:#e3f7ee;--bad:#d8435a;--bad-bg:#fbe3e7;--accent:#2563eb;--token:#e6edfb;--token-ink:#2f55d4;
  --r-card:32px;--r-inner:20px;--r-pill:9999px}
.card{background:#fff;border:1px solid var(--line);border-radius:var(--r-card);box-shadow:0 30px 60px -20px #0000001f}
.token{background:var(--token);color:var(--token-ink);border-radius:6px;padding:0 2px}
.lane{display:grid;grid-template-columns:repeat(9,1fr);height:44px;border-radius:10px;background:#f6f7f7;box-shadow:inset 0 0 0 1px var(--line)}
.slot{position:absolute;border:2px solid var(--ok);background:color-mix(in srgb,var(--ok) 18%,transparent);border-radius:12px;transition:left .37s cubic-bezier(.65,0,.35,1)}
.slot.conflict{border-color:var(--bad);background:color-mix(in srgb,var(--bad) 18%,transparent)}
.chip[aria-pressed=true]{background:var(--ok-bg);color:#1f7a4d}
.book{background:var(--accent);color:#fff;border-radius:var(--r-pill);font-weight:600}  /* #2563eb gives 5.17:1 */
.panel-enter{animation:in .47s cubic-bezier(.16,1,.3,1)}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 7 | Tidy, calm, standard SaaS polish; not visually distinctive. |
| Originality | 7 | Fusing an NL command bar with a draggable group timeline is a fresh combination. |
| Usability | 8 | Immediate, explained feedback and multiple input paths. Pale-grey contrast lapses. |
| Craft | 8 | Snapping, state-mirrored rules and stable skeletons show care. |

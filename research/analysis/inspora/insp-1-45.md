---
id: insp-1-45
source: inspora
category: Motion
status: analyzed
title: "Event Swatch"
creator: "@artntek"
styles: [maximalist-color, playful-rounded, glassmorphism, micro-interaction]
patterns: [drag-to-reschedule, tilted-drag-ghost, pile-stacking-on-drop, fan-out-cluster, live-time-tooltip-on-drag, tonal-text-on-tinted-card, week-view-calendar]
mode: light
palette: ["#fafafa", "#efefef", "#fe829f", "#c875db", "#f3fc7f", "#ffb772", "#7fd3a6", "#5f8ef7"]
type_families: ["SF Pro Rounded / Inter (likely)"]
type_class: [rounded-sans, neo-grotesk]
radius_px: [28, 9999]
motion: {durations_s: [0.6, 0.63, 0.8, 0.47, 0.83, 0.6, 0.87, 0.67], easing: [ease-out, ease-in-out], loop: false}
scores: {aesthetics: 8, originality: 8, usability: 6, craft: 8}
craft_signals: [same-hue-dark-text-on-card, translucent-overlap-shows-stack, random-tilt-on-pickup, time-preview-replaces-card-content, now-line-red-hairline, zoom-out-to-browser-context]
anti_patterns: [tinted-text-below-aa, tilted-text-hard-to-read, truncated-titles]
---
# Event Swatch — @artntek

## 1. Snapshot
- **Subject:** A 1440×1080, 22.4 s, 60 fps demo of a week-view calendar ("Juli.so", Aug 2026) whose events are candy-coloured, rounded "swatches". Dragging an event tilts it into a translucent ghost and shows a big live time ("Wed 8:00 AM"). Dropping several events into the same slot piles them up like playing cards, and they can fan out in a scattered cluster.
- **Why it's remarkable:** Events behave as physical tokens. They have rotation, translucency, stacking and scatter, which makes scheduling conflicts tangible: overlapping events literally overlap.

## 2. Composition & layout
- **Mostly macro crops** of the week grid. Day columns are ≈400 px wide at macro zoom, hour rows ≈225 px tall, with 1 px #efefef grid lines on #fafafa.
- **Day headers:** day name over date number (e.g. "Wed•" / "26"), centred per column. A dot marks days that have events.
- **Now-line:** a 1 px red/pink hairline at the current time, with a red "06:21" time pill in the zoomed-out view.
- **Event card:** ≈380×150 px at macro zoom, radius ≈28 px. An icon sits top-left, a "•••" menu top-right, the meta line ("8:00 AM - daily - UTC") and a bold title at the bottom-left.
- **Zoom-outs:** at 6.23 s and 16.21–18.70 s the camera pulls back to show the full browser window (Safari, juli.so) over a landscape wallpaper, with a floating toolbar and a bottom dock-style bar (date, apps, folder, trash). This shows the micro-interaction in product context.

## 3. Typography
- **Typeface:** rounded/neo-grotesk (SF Pro Rounded / Inter-like).
- **Event cards:** the meta line is ≈24 px medium; the title is ≈28 px semibold. Both are in a **dark shade of the card's own hue** (dark olive on yellow, plum on purple, maroon on pink), not black.
- **Drag tooltip:** "Wed 8:00 AM" at ≈40 px semibold replaces the card content while dragging.
- **Headers:** ≈28 px medium #333.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #fafafa | calendar canvas | 82.5% |
| #efefef | grid lines, toolbar pill | 2.8% |
| #fe829f | pink: birthday / personal | 3.5% |
| #c875db (#c057b6 mid) | purple: daily word | 2.6% |
| #f3fc7f | lime-yellow: meeting notes | 2.6% |
| #ffb772 | orange: spending report | ~2% |
| ≈#7fd3a6 | mint green: PR alerts (sampled visually) | state |
| ≈#5f8ef7 | blue: rent reminder (sampled visually) | state |

WCAG checks for tonal text on card:
- Yellow #606e16 on #f3fb71: **5.04:1** (pass).
- Orange #8e4b16 on #ffb772: 3.87:1.
- Pink #8d203d on #fe83a0: 3.73:1.
- Purple #721c77 on #c875db: **3.27:1**.

Three of the four tinted pairs fail AA for normal text. Headers #333 on #fafafa: 12.1:1.

## 5. Depth & material
- **Cards at rest:** opaque with a soft shadow (≈0 8px 20px rgba(0,0,0,.08)) and a 1 px white inner rim.
- **When lifted:** cards become **≈80% opaque**, so overlapping regions blend (orange plus purple shows a muddy overlap; green over yellow shows through). They rotate −8° to −20° and gain a larger shadow.
- **Piles:** dropped piles show offset edges beneath the top card (a yellow strip under the purple "Word of the Day" at 13.71 s), which signals a count.

## 6. Components & patterns
- **Week-view calendar** with recurring-automation events (e.g. daily Slack summary, weekly spend report). The product reads as an automation scheduler.
- **Drag ghost:** tilt, translucency and a time tooltip.
- **Stack-on-drop:** collisions become a pile with peeking edges; zoomed out it shows a "2 hidden" badge (16.21 s).
- **Cluster fan-out:** an explode or collect gesture (1.25 s, 21.20 s) scatters several events around the cursor at random angles.
- **Floating toolbar:** a pill with view, search, filter and add.

## 7. Motion
- **Measured:** 22.44 s at 60 fps. motion_fraction 0.26. 10 segments, median **0.63 s**:
  - front-loaded **ease-out** at 0.00 s (0.60 s, peak 0.08), 7.90 s (0.80 s, peak 0.06), 13.40 s (0.60 s, peak 0.14) and 19.07 s (0.67 s, peak 0.07);
  - symmetric at 5.23 s (0.63 s), 11.83 s (0.83 s), 14.50 s (0.87 s) and 21.43 s (0.63 s);
  - one ease-in at 9.33 s (0.47 s).
- **Interpretation:**
  - The ease-out segments are the camera zoom cuts and card drops (fast settle, like a spring landing).
  - The symmetric ones are drags across columns.
  - Cards rotate as they are picked up and straighten on drop; the frames show 0° at rest versus about −15° in flight.
- **Not a loop:** seamless_loop_likely false.

## 8. Brand system
n/a — not a brand system. Juli.so identity cues: candy pastel event colours, rounded type, glyph icons per automation type.

## 9. UX
- **Strengths:**
  - Drag feedback is rich: a big target-time label tells you exactly where the drop will land.
  - Piles make conflicts visible.
  - Colour plus icon per category supports scanning.
- **Risks:**
  - Tinted titles below AA.
  - Rotated text in clusters is hard to read.
  - Titles truncate ("Send Stale PR Alert To…").
  - Piled events hide information behind "N hidden".
  - Random rotations may feel chaotic in dense weeks.

## 10. Craft signals
- Card text uses a dark shade of the card's own hue, never black.
- Lifted cards are translucent, so overlap regions blend visibly.
- Pickup applies a rotation (≈−8° to −20°) that resets to 0° on drop.
- While dragging, the card content is replaced by a large "Wed 8:00 AM" target-time label.
- Piles show peeking offset edges of the cards underneath.
- The now-line is a 1 px pink hairline paired with a red time pill.
- The demo cuts out to a full browser on a wallpaper to show real scale.

## 11. Reproduction recipe
```css
:root{--canvas:#fafafa;--grid:#efefef;
  --pink:#fe829f;--pink-ink:#8d203d;--purple:#c875db;--purple-ink:#5e1463;
  --lime:#f3fc7f;--lime-ink:#4f5a10;--orange:#ffb772;--orange-ink:#7a3d0e}
.event{--bg:var(--pink);--ink:var(--pink-ink);background:var(--bg);color:var(--ink);border-radius:28px;padding:16px 18px;
  box-shadow:inset 0 0 0 1px rgba(255,255,255,.5),0 8px 20px rgba(0,0,0,.08);
  transition:rotate .3s cubic-bezier(.34,1.56,.64,1),opacity .2s,box-shadow .2s}
.event .meta{font:500 12px/1.2 "SF Pro Rounded",Inter}.event .title{font:600 14px/1.2 "SF Pro Rounded",Inter}
.event.dragging{rotate:-12deg;opacity:.82;box-shadow:0 24px 48px rgba(0,0,0,.18)}
.event.dragging .body{display:none}.event.dragging::after{content:attr(data-target);font:600 20px "SF Pro Rounded"}
.pile>.event:not(:last-child){translate:0 6px;scale:.97}
.now{height:1px;background:#f26b8a}
```
(Use darker ink values than the sampled ones to reach 4.5:1, e.g. purple-ink #5e1463.)

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Joyful, cohesive candy palette with tonal text; strong macro cinematography. |
| Originality | 8 | Physical pile and fan metaphors for calendar conflicts are fresh. |
| Usability | 6 | Great drag feedback, but contrast fails, rotated text and hidden piles hurt reading. |
| Craft | 8 | Considered translucency, tilt and spring settle; consistent radius and icon system. |

---
id: insp-time-zones
source: inspora
category: Product
status: analyzed
title: "Time for different time zones"
creator: "@tar_uniqueee"
styles: [dark-premium, terminal-mono, micro-interaction, hairline-ui]
patterns: [menu-bar-popover, scrub-ruler-time-offset, rolling-digit-counter, day-phase-status-labels, drag-reorder-rows, circular-icon-buttons, offset-readout]
mode: dark
palette: ["#212226", "#1b1c1f", "#dfe0e2", "#8e8f93", "#4a2f23", "#f97316", "#22c55e", "#facc15"]
type_families: ["SF Pro (likely)", "SF Mono (likely)"]
type_class: [neo-grotesk, mono]
radius_px: [40, 9999]
motion: {durations_s: [0.17, 0.27, 0.23, 0.13, 0.37, 0.2], easing: [ease-in-out, ease-out], loop: true}
scores: {aesthetics: 8, originality: 8, usability: 8, craft: 8}
craft_signals: [ruler-ticks-recolour-in-scrubbed-range, odometer-digits-with-motion-blur, status-icon-per-day-phase, offset-label-follows-drag, own-zone-row-darker, mono-meta-sans-values]
anti_patterns: [scrub-affordance-not-labelled, small-mono-caps]
---
# Time for different time zones — @tar_uniqueee

## 1. Snapshot
- **Subject:** A 13.0 s, 936×936 loop of a macOS menu-bar popover listing Warsaw (your time), San Francisco, New York and New Delhi. Dragging across a tick ruler at the top shifts every clock; the rows can also be reordered.
- **Why it's remarkable:** Each row states what the time *means* ("NIGHT ☾", "BEFORE WORK ☀", "WORKING ●", "WRAPPING UP ●"), and the labels update live while you scrub, which answers "can I call them now?" directly.

## 2. Composition & layout
- The popover is about 720×805 px with a ~40 px radius, hanging under real menu-bar icons (Figma, ChatGPT, Notion…) on a #e4e4e6 desktop.
- **Ruler band (~170 px):** "UTC+02:00" top-left, offset readout top-right ("NOW", "−7H", "−4H 29M"), and a row of grey ticks with taller ones every ~6 ticks. An orange vertical line marks "now".
- **Rows:** four at ~128 px pitch, each two-line, separated by hairlines:
  - left: mono meta ("−9H / PDT · YESTERDAY") over a city name;
  - right: mono status with an icon, over the time.
- The first row (your own zone) sits on a darker #1b1c1f band.
- **Footer:** a 72 px circular settings button left; locate and add buttons right.

## 3. Typography
- **City names:** ~28 px in the 936 frame, SF Pro regular, #dfe0e2.
- **Times:** ~30 px SF Pro with tabular figures.
- **Meta and status:** SF Mono caps at ~17 px with +0.04 em tracking, grey.
- The offset readout is mono too. Mono is used for every computed or contextual string; sans for names and times.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #212226 | popover surface | 55% |
| #1b1c1f (est.) | own-zone row | — |
| #dfe0e2 | names, times | (desktop shares it, 29%) |
| #8e8f93 | mono meta | — |
| #4a2f23 | scrubbed range fill | 7.5% (while dragging) |
| #f97316 (est.) | now-line, scrubbed ticks, "wrapping up" dot | — |
| #22c55e / #facc15 (est.) | working dot / sunrise icon | — |

WCAG checks:
- Names #dfe0e2 on #212226: 12.03:1.
- Meta #8e8f93 on #212226: 4.92:1.
- Orange #f97316 on #212226: 5.67:1.
- Ruler label #c2c2c4 on the scrub fill #4a2f23: 6.86:1.

Night times are dimmed to grey while daytime times stay bright, a second, subtle encoding.

## 5. Depth & material
- A dark slab with a 1 px lighter rim and a soft drop shadow onto the desktop.
- Footer buttons are outlined circles (1 px #3a3b3f).
- The scrubbed region is a translucent orange wash (#4a2f23) whose ticks turn solid orange.

## 6. Components & patterns
- **Scrub ruler:** drag from the now-line. The region between now and the pointer fills, and the offset reads "−6H 49M" and similar.
- **Rolling digits:** in mid-drag frames (2.17 s, 5.06 s) the minute digits are vertically motion-blurred, an odometer roll.
- **Reorder:** at 10.85 s New Delhi and New York have swapped places, after which they settle back.
- **Day-phase status:** a label plus icon/dot per row.

## 7. Motion
- **Measured:** 11 segments with a median of 0.2 s; motion_fraction is 0.14, and the loop is seamless (first/last diff 0.2).
  - Scrub-related bursts are 0.23–0.27 s symmetric (2.13 s, 3.2 s, 4.53 s).
  - Releases and reorder moves are ease-out (8.87 s, 0.37 s, peak 0.14; 10.33 s, 0.2 s).
  - There are quick 0.1–0.13 s ticks (4.9 s, 6.8 s).
- **From frames:** the release snaps the fill back to "NOW" with a decelerating ease (the 8.87 s segment), and the digits roll back to 08:45.

## 8. Brand system
n/a — not a brand system. Identity cues: native-macOS menu-bar utility styling with an orange accent.

## 9. UX
- Direct manipulation answers the core question (overlapping working hours) faster than typing a time.
- The status labels remove the mental arithmetic, and "YESTERDAY" flags date rollover.
- **Risks:**
  - The ruler has no visible "drag me" hint before first use.
  - The mono caps at ~8.5 CSS px are small.
  - Colour dots are the only differentiator between WORKING and WRAPPING UP, apart from the text.

## 10. Craft signals
- The ruler ticks inside the scrubbed range recolour to orange, not just the background.
- The offset readout updates continuously with minutes ("−4H 29M"), not just hours.
- The rows' day-phase labels change mid-drag (Warsaw goes BEFORE WORK → NIGHT as you scrub back).
- The own-zone row has a darker band and the "YOUR TIME · TUE 4 AUG" label.
- Odometer roll with motion blur on digit change.
- The circular footer buttons align to the row text margins (~24 px).

## 11. Reproduction recipe
```css
:root{--bg:#212226;--bg-self:#1b1c1f;--ink:#dfe0e2;--ink-2:#8e8f93;--accent:#f97316;--scrub:#4a2f23;
  --mono:"SF Mono",ui-monospace;--sans:-apple-system,"SF Pro Text",system-ui}
.pop{width:360px;border-radius:20px;background:var(--bg);box-shadow:0 0 0 1px rgba(255,255,255,.08),0 20px 40px rgba(0,0,0,.35)}
.ruler{height:85px;position:relative;background:linear-gradient(90deg,transparent var(--now),var(--scrub) var(--now) var(--ptr),transparent var(--ptr))}
.tick{width:1px;height:14px;background:#55565b}.tick:nth-child(6n){height:24px}.tick.in{background:var(--accent)}
.meta{font:500 9px/1.2 var(--mono);letter-spacing:.04em;text-transform:uppercase;color:var(--ink-2)}
.time{font:400 15px var(--sans);font-variant-numeric:tabular-nums}
.digit{display:inline-block;transition:transform .23s ease-in-out,filter .23s}.digit.rolling{filter:blur(1.5px)}
.row{transition:transform .37s cubic-bezier(.2,.8,.2,1)} /* reorder */
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Native-feeling dark utility with a single warm accent. |
| Originality | 8 | Scrub ruler plus semantic day-phase labels is a fresh combo. |
| Usability | 8 | Answers the real question at a glance; drag affordance is undiscovered. |
| Craft | 8 | Live labels, tick recolouring and odometer digits are carefully done. |

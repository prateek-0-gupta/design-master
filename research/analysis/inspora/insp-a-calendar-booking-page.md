---
id: insp-a-calendar-booking-page
source: inspora
category: Product
status: analyzed
title: "a calendar booking page"
creator: "Jonathan Ouyang"
styles: [glassmorphism, photo-led, dark-premium, cinematic-3d]
patterns: [time-scrub-drives-background, scrubber-timeline-day-view, two-pane-booking-panel, hatched-busy-blocks, lockscreen-clock-hero, step-swap-details-form, sticky-selection-summary]
mode: dark
palette: ["#110f12", "#1a1a22", "#272630", "#3a3740", "#4e4f58", "#84665c", "#3d231e", "#ffffff"]
type_families: ["Inter / SF Pro Display (likely)"]
type_class: [neo-grotesk]
radius_px: [44, 9999, 16]
motion: {durations_s: [1.33, 1.83, 1.07, 0.83, 0.27, 0.33], easing: [ease-in-out, ease-out, ease-in], loop: false}
scores: {aesthetics: 9, originality: 9, usability: 7, craft: 8}
craft_signals: [background-photo-keyed-to-hovered-time, clock-mirrors-cursor-time, hatched-busy-and-unavailable, frosted-panel-tints-with-sky, selected-day-white-disc, slot-label-chip-on-scrub-line]
anti_patterns: [clock-white-on-bright-sky, disabled-dates-too-dim, hover-only-discovery]
---
# a calendar booking page — Jonathan Ouyang

## 1. Snapshot
- **Subject:** A 20.6 s, 2940×1664 capture of a personal Google Meet booking page. A frosted two-pane panel (month calendar plus day timeline) floats over a full-bleed Golden Gate Bridge photo. As the cursor scrubs the timeline, the photo switches to that time of day (sunrise, noon, sunset, night) and a lockscreen-style clock shows the hovered time.
- **Why it's remarkable:** The background is data. Hovering 8:25 PM shows the bridge at night with car light trails, and 6:16 shows the sun on the horizon. Picking a slot becomes feeling what that time is like in San Francisco.

## 2. Composition & layout
- **Panel (key, ×1.47 to source):** ≈1333×1367 px source, anchored left with a ~70 px margin and a ~44 px radius.
- **Left pane (~685 px):**
  - "30 min · Google Meet" eyebrow;
  - "Book a time" title (~46 px source);
  - "Pick an open time." subtitle;
  - a month grid of 7 columns at ~85 px pitch;
  - a full-width bottom pill CTA ("Pick a time", later "Continue").
- **Right pane (~650 px):**
  - "WEDNESDAY / September 30 / 26 times available";
  - a vertical hour timeline from 8 AM to 12 AM, rows ~69 px source apart;
  - a hairline per hour;
  - hatched blocks for unavailable times and a labelled "Busy" block.
- **Hero clock:** top-right, a giant clock "8:25" (cap height ≈220 px source) right-aligned under "Wednesday, September 30", with "• San Francisco" (green dot) beneath. A "‹ Home" pill sits top-left.
- **Details step (17.1 s):** the left pane becomes "Your details": a summary (Date / Time), Name, Email and topic fields, and a white "Confirm" pill. The right timeline keeps the selected "6:30 – 7:00 PM" slot as a white bar.

## 3. Typography
- One neo-grotesk (Inter or SF Pro Display).
- **Clock:** ~300 px source, semibold, tight tracking (~−0.03 em) and lining numerals, the iOS lock-screen idiom.
- **Titles:** "Book a time" / "September 30" ~40–46 px semibold.
- **Small text:** labels ~20 px; weekday headers in small caps-like uppercase at ~17 px with +0.05 em tracking.
- **Timeline:** hour labels ~17 px grey.
- **Scrub chip:** the time label (e.g. "8:25 PM") is set ~18 px white on a dark chip at the end of the scrub line.

## 4. Colour
| Hex | Role | Approx share (key, night) |
|---|---|---|
| #110f12 / #1a1a22 | panel glass (night) and sky | 55% |
| #272630 / #3a3740 | hatched blocks, raised fills | 18% |
| #4e4f58 | disabled CTA fill | 5% |
| #84665c / #3d231e | sunset-warm tints in the glass and photo | 12% |
| #ffffff | selected day disc, clock, primary text | — |
| ≈#34c759 | "San Francisco" live dot | — |

WCAG checks:
- White on panel #1a1a22: 17.29:1.
- Grey labels ≈#9a9aa2: 6.19:1.
- **Disabled past dates ≈#5c5c64: 2.61:1.**
- Disabled CTA text #8a8a90 on #3a3a42: 3.28:1.
- **The clock in white over the bright noon or overcast sky (≈#c8cdd2) is 1.6:1** and nearly vanishes in the 11:21 and 9:51 frames.

## 5. Depth & material
- **Panel:** heavy frosted glass. The backdrop blur is ~40 px and the tint is dark (~70% opacity). The glass picks up warm or cool colour from the photo behind it: amber at sunset (6:16), blue-grey at noon.
- **Panel edge:** a hairline rim at ~8% white.
- **Busy blocks:** diagonal-hatched fills, a print-cartography convention for "unavailable".
- **Background:** a photographic time-lapse with real depth (bridge tower foreground, city skyline mid-ground). The clock floats on the photo with no backing.

## 6. Components & patterns
- **Month picker:** the selected day is a white disc with black numerals. Today ("29") is white bold, past dates are dim and future dates mid-grey.
- **Timeline scrubber:** a horizontal line follows the cursor with a time chip at the right edge. On selection, the slot becomes a white pill with a range label ("6:30 – 7:00 PM").
- **Summary card:** "Wed, Sep 30 · 6:30 – 7:00 PM · Pacific Time" appears above "Continue", so the user confirms before moving to the next step.
- **Step change:** "Your details" replaces the calendar pane with a "‹ Back" link while the timeline remains, keeping context.
- **Close:** a 40 px circular ✕ at the top right of the panel.

## 7. Motion
Measured profile: 20.55 s at 60 fps, `motion_fraction` 0.39, 12 segments with a median of 0.54 s. Not a loop.
- **2.93–4.27 s (1.33 s, ease-in, peak 0.81) and 4.73–6.57 s (1.83 s, ease-out, peak 0.17):** the long cross-dissolves of the background photo as the cursor sweeps from afternoon to morning. They are slow and cinematic.
- **7.57–8.63 s (1.07 s, symmetric) and 10.00–10.83 s (0.83 s):** further time-of-day swaps (to noon, to night).
- **13.97 s (0.27 s), 15.87 s (0.33 s) and 17.30 s (0.30 s), all ease-out:** UI state changes: the slot locking, the summary appearing and the pane swap to "Your details".
- **19.00–19.83 s (0.83 s, ease-in):** the final background change back to day.
- **Two tempos:** about 0.3 s ease-out for UI, and about 0.8–1.8 s for the atmospheric background. UI feedback stays snappy while the scenery is slow.

## 8. Brand system
n/a — not a brand system. Identity cues:
- personal branding through place (San Francisco, Golden Gate);
- the lock-screen clock idiom;
- monochrome UI with the photo supplying all colour.

## 9. UX
- **Strengths:**
  - The timezone and the time of day are made tangible.
  - The scrub chip shows the exact time before committing.
  - Busy and unavailable times are clearly differentiated (hatched versus labelled).
  - A two-step flow with persistent context.
- **Risks:**
  - The clock and date are illegible over bright skies (1.6:1).
  - The background swap is hover-driven, with no equivalent on touch.
  - Dim past dates fail contrast.
  - The large photo assets affect load time.
  - The clock and the hovered time could confuse users about the actual current time.

## 10. Craft signals
- The background photo is keyed to the hovered time, with distinct sunrise, noon, sunset and night plates.
- The giant clock mirrors the cursor time to the minute (8:25 matches the "8:25 PM" chip).
- Diagonal hatching marks unavailable time and a separate labelled block marks "Busy".
- The frosted panel inherits the photo's warm or cool cast.
- UI transitions run at about 0.3 s ease-out while the scenery dissolves over 0.8–1.8 s (measured).
- The selected day is a white disc: the only filled white element besides the primary CTA.

## 11. Reproduction recipe
```css
:root{--glass:rgba(20,19,26,.72);--rim:rgba(255,255,255,.08);--text:#fff;--muted:#9a9aa2;--dim:#6e6e76;
  --hatch:repeating-linear-gradient(135deg,rgba(255,255,255,.06) 0 2px,transparent 2px 8px)}
.scene{position:fixed;inset:0;background:center/cover var(--plate);transition:background-image 1.2s ease-in-out}
.panel{backdrop-filter:blur(40px) saturate(1.2);background:var(--glass);border:1px solid var(--rim);
  border-radius:22px;display:grid;grid-template-columns:1fr 1fr}
.day[aria-selected=true]{background:#fff;color:#000;border-radius:50%}
.slot.unavailable{background:var(--hatch);border-radius:8px}
.scrub{height:1px;background:#fff8} .scrub .chip{background:#111;color:#fff;font:500 12px Inter;padding:2px 6px;border-radius:6px}
.clock{font:600 clamp(96px,11vw,200px)/.9 Inter,sans-serif;letter-spacing:-.03em;color:#fff;
  text-shadow:0 2px 24px rgba(0,0,0,.35)} /* add for bright plates */
.ui-swap{transition:opacity .3s cubic-bezier(.2,.8,.2,1),transform .3s cubic-bezier(.2,.8,.2,1)}
```
```js
timeline.addEventListener('pointermove', e => { const t = yToTime(e.offsetY);
  scene.style.setProperty('--plate', `url(${plateFor(t)})`); clock.textContent = fmt(t); });
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 9 | Cinematic photography under refined dark glass. |
| Originality | 9 | Making the scenery respond to the hovered slot is a new idea for scheduling. |
| Usability | 7 | Clear flow and busy-state coding. Clock contrast, hover dependency and dim dates hurt. |
| Craft | 8 | Two-tempo motion, a synced clock and hatching are precise. No text protection on bright plates. |

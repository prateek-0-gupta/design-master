---
id: insp-sticky-note-app
source: inspora
category: Product
status: analyzed
title: "Sticky-note app"
creator: "Rehan Ahmed"
styles: [skeuomorphic, hand-drawn, playful-rounded, physical-material]
patterns: [swipeable-card-stack, pinned-note-hero, pager-counter, segmented-filter, list-with-mini-note-thumbs, countdown-to-join, strike-through-done-state]
mode: light
palette: ["#eff3f5", "#fefefe", "#e4e4e7", "#f1bcb2", "#ceb1af", "#5e585a", "#111111"]
type_families: ["Caveat Brush / Kalam-style marker script (likely)", "SF Pro (likely)", "JetBrains Mono / SF Mono (likely)"]
type_class: [script, neo-grotesk, mono]
radius_px: [32, 24, 9999, 4]
motion: {durations_s: [0.88, 0.67, 0.5, 0.33, 0.21], easing: [ease-in-out, ease-in, ease-out], loop: false}
scores: {aesthetics: 8, originality: 8, usability: 7, craft: 8}
craft_signals: [category-colour-per-note, stack-preview-of-next-notes, handwritten-highlight-underline, muted-connector-words, mono-metadata-strip, pushpin-with-cast-shadow, mini-note-thumbnails-in-list]
anti_patterns: [faint-today-label, connector-words-low-contrast]
---
# Sticky-note app — Rehan Ahmed

## 1. Snapshot
- **Subject:** A 16.0 s, 2000×2000 (24 fps) iPhone recording of "Pinned", a meetings app. Today's 7 meetings are a stack of pinned sticky notes you swipe through (1/7 → 7/7). Below the stack are a category filter (All / Work / School / Personal) and a list of upcoming meetings.
- **Why it's remarkable:** Each meeting is a **handwritten sticky note in its category's colour**: yellow Work, green or salmon School, blue or lilac Personal, pink Work retro, mint done. The next notes peek out underneath at slight rotations, so the stack is both a pager and a preview.

## 2. Composition & layout
- The phone screen is about 860 px wide in key px.
- **Header:**
  - a 100 px round back button;
  - a script "Pinned" wordmark (about 60 px);
  - a bell pill with count.
- **Pager row:** "7 meetings **Today**", "3/7" and ‹ › buttons.
- **Note:** about 660×660 px, centred, rotated about −1°. Two notes peek behind it at about +3° and −4°. It has a pushpin at top centre.
- **Note anatomy:**
  - a darker header band (about 90 px) with "SCHOOL" in mono caps on the left and "in 2h 54m" on the right;
  - three handwritten lines centred ("Physics lab / with Prof. Rao / at 12:30pm");
  - mono "Join in 2h 54m ↗" and an underlined meeting URL, bottom-left.
- **Below:** a segmented filter (about 800×95 px), then a white grouped list card (radius about 32 px). Each row has a mini note thumbnail (about 110 px, rotated slightly, carrying the time in script), a title and meta.

## 3. Typography
- **Three voices:**
  1. a **marker script** (Caveat Brush or Kalam style) for the note content, about 70 px. The connector words "with" and "at" are muted grey-brown, and the time gets a hand-drawn underline in a darker category tint;
  2. **SF Pro** for the UI: "7 meetings" at 38 px Semibold, "Today" in light grey, list titles at 34 px Medium and meta at 28 px grey;
  3. **mono** caps at about 22 px with wide tracking for the category and countdown, and about 24 px for "Join in…" and the URL.
- The wordmark "Pinned" uses the same script, tying the brand to the content.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #eff3f5 | screen / backdrop (cool grey) | 61% |
| #fefefe | list card, active segment | 6% |
| #e4e4e7 | segmented track, buttons | 9% |
| #f1bcb2 | salmon School note (key frame) | 9% |
| #ceb1af | note shadow and edge tint | 5% |
| #5e585a | muted text, pin | 4% |
| #111111 | script text, titles | — |

Note colours seen in the frames: yellow (~#f6e58a), green (~#b9f0a0), salmon (#f1bcb2), periwinkle (~#b9c6f5), pink (~#f2b5dc), lilac (~#d5c0f5) and mint (~#b6ebd2, done).

WCAG checks:
- Script #111 on salmon: 11.3:1.
- Muted "with/at" (~#7a6a68) on salmon: **3.08:1**, acceptable only because the script is about 70 px.
- Mono #555 on salmon: 4.46:1.
- "Today" (~#8a8f99) on #eff3f5: **2.91:1**.
- List meta on white: 5.0:1.

## 5. Depth & material
- **Paper realism:**
  - each note has a soft drop shadow (about 0 20 40 rgba(0,0,0,.12));
  - the stacked notes beneath are rotated and offset;
  - the header band is a slightly darker strip, like the adhesive edge;
  - a 3D black pushpin has a specular dot and its own cast shadow.
- **UI chrome:** neumorphic-lite round buttons (white on #eff3f5 with a soft outer shadow) and a white list card with a very soft shadow.
- **Phone frame:** silver bezel with a long, soft shadow on the light canvas.

## 6. Components & patterns
- Swipeable note stack with a "3/7" counter and ‹ › buttons, so swipe has a button alternative.
- Countdown chip ("in 2h 54m") plus a "Join ↗" deep link.
- Segmented filter by category.
- List rows with mini-note thumbnails, so the colour language carries into the list.
- **Done state** (7/7, "Stand-up with Design team"): mint note, the title struck through by hand, and "done" in place of the countdown.

## 7. Motion
Measured: 16.0 s at 24 fps, `motion_fraction` 0.28, 10 segments with a median of 0.42 s.
- **Swipe transitions:** about 0.88 s each. 1.62–2.50 s is symmetric ease-in-out (peak 0.50); 6.83–7.71 s is ease-in (peak 0.69); 9.83–10.71 s peaks at 0.64.
- **Back-swipe:** 3.04–3.71 s (0.67 s, peak 0.91, ease-in), where the finger drags first and then releases.
- **Taps:** 0.21–0.33 s (e.g. 1.04 s, peak 0.10 → fast ease-out).
- **From frames:** the outgoing note slides out sideways while the next note rises from the stack, rotating from about 3° to about −1° and scaling up. The touch indicator follows the right-edge chevron or drags across the note.

## 8. Brand system
n/a — not a brand system. Identity cues:
- the script "Pinned" wordmark;
- the pushpin;
- category colours as identity.

## 9. UX
- **Strengths:**
  - The next meeting dominates the screen with a time-to-join countdown.
  - Category colour is consistent across note, list thumb and filter.
  - Buttons back up the swipe gestures.
  - The done state is legible.
- **Risks:**
  - Script text may hurt legibility for long titles and for some users. The time is the critical datum and is set in script, though it is underlined.
  - "Today" and the muted connectors are low contrast.
  - Colour alone distinguishes categories, although a mono label backs it up.

## 10. Craft signals
- Connector words ("with", "at") are de-emphasised in grey while the nouns and time are black, giving a semantic hierarchy inside the script.
- The time underline uses a darker shade of the note colour (red on salmon, green on green, blue on periwinkle).
- The notes behind take the colours of the *next* meetings in the queue (visible as the blue and pink edges behind salmon), so the stack previews what is coming.
- Mono metadata in the header band contrasts with the script body.
- The pushpin casts a shadow offset down and right, matching the note shadow direction.
- List thumbnails repeat the note language at about 1/6 scale, with a slight rotation.

## 11. Reproduction recipe
```css
:root{--bg:#eff3f5;--card:#fefefe;--track:#e4e4e7;--ink:#111;--muted:#5e585a;
  --note-work:#f6e58a;--note-school:#f1bcb2;--note-personal:#b9c6f5;--note-done:#b6ebd2;
  --script:"Caveat Brush","Kalam",cursive;--mono:"JetBrains Mono",ui-monospace,monospace}
.stack{position:relative;width:330px;aspect-ratio:1}
.note{position:absolute;inset:0;background:var(--c);border-radius:4px;box-shadow:0 20px 40px rgba(0,0,0,.12);
  transform:rotate(var(--r,-1deg));transition:transform .88s cubic-bezier(.45,0,.55,1),opacity .88s}
.note:nth-child(2){--r:3deg;translate:6px 8px}.note:nth-child(3){--r:-4deg;translate:-8px 10px}
.note header{background:color-mix(in oklab,var(--c),#fff 35%);font:500 11px/1 var(--mono);letter-spacing:.12em;text-transform:uppercase;padding:14px 16px}
.note h2{font:400 36px/1.15 var(--script);text-align:center;color:var(--ink)}
.note h2 .conn{color:color-mix(in oklab,var(--ink),var(--c) 55%)}
.note h2 .time{text-decoration:underline;text-decoration-color:color-mix(in oklab,var(--c),#000 35%);text-decoration-thickness:3px;text-underline-offset:6px}
.note.out{transform:translateX(-120%) rotate(-12deg);opacity:0}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Charming paper metaphor, carefully balanced against clean iOS chrome. |
| Originality | 8 | Meetings as a pinned, colour-coded sticky stack is a fresh agenda pattern. |
| Usability | 7 | Clear next-up focus and countdown; script legibility and grey labels are concerns. |
| Craft | 8 | Tinted underlines, a next-in-queue stack preview and consistent thumbnails. |

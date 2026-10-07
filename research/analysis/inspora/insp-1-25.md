---
id: insp-1-25
source: inspora
category: Web
status: analyzed
title: "Team section"
creator: "@dawood_adib"
styles: [high-contrast-bw, minimal-swiss, dither-halftone, generative-particle]
patterns: [accordion-team-list, particle-portrait-morph, giant-section-title, index-counter, skill-tag-chips, hover-to-reveal-photo]
mode: light
palette: ["#f2f2f2", "#fefefe", "#010101", "#2e2e2e", "#545454", "#737373", "#dedede"]
type_families: ["Inter / Helvetica Now Display (likely)", "italic serif for index numerals (likely Times / Instrument Serif)"]
type_class: [neo-grotesk, editorial-serif]
radius_px: [16, 9999]
motion: {durations_s: [1.2, 1.17, 1.23, 1.13, 0.27, 0.2], easing: [ease-out], loop: true}
scores: {aesthetics: 9, originality: 8, usability: 7, craft: 8}
craft_signals: [particle-dissolve-between-portraits, counter-synced-to-accordion, italic-serif-parenthetical-index, plus-crosshair-grid-markers, active-row-arrow-inverts-to-black, chips-right-aligned-wrap]
anti_patterns: [collapsed-rows-hide-names, particle-portrait-low-recognisability]
---
# Team section — @dawood_adib

## 1. Snapshot
- **Subject:** A 17.4 s, 1316×720 loop of a monochrome "TEAM" section.
  - Left: a portrait rendered as thousands of black stipple particles.
  - Right: a white accordion card listing six roles.
  - Hovering a row expands it (name, bio, skill chips), and the portrait particles scatter and re-form into the next person.
- **Why it's remarkable:** The person swap is a particle morph rather than a crossfade. Identity literally reassembles from dust, and the big "0N" counter ticks in sync with the accordion.

## 2. Composition & layout
- **Two zones on a #f2f2f2 canvas.**
  - **Top band (y 0→200):** a giant "TEAM" at the left (x 35→550, about 135 px cap height). On the right, a meta grid of three columns ("Design & Branding", "Based in London", and an "Email us" black pill). Below them is a row of "+" crosshair markers at x≈671/881/1091 and the index "05" (about 52 px) flush right at x≈1290.
  - **Lower zone:** the portrait (about 540×450 px) bleeds off the bottom-left. The white list card (x 659→1288, y 280→700, radius about 16 px) sits on the right.
- **Rows:** about 53 px tall with 1 px #dedede dividers. Columns are the index (left), a centred role label and an arrow button (right). The expanded row grows to about 150 px.

## 3. Typography
- **"TEAM":** a heavy neo-grotesk at about 180 px font-size, black, with tight tracking (−0.03 em), close to Helvetica Now Display Black or Inter Display Black.
- **Meta labels and roles:** 13–14 px regular. The expanded name is about 22 px medium and the bio about 12 px grey.
- **Index numerals:** "(001)…(006)" in a tiny italic serif of about 9 px, an editorial counterpoint to the grotesk.
- **Counter "05":** about 52 px regular grotesk with tabular figures.
- **Chips:** about 11 px semibold on #e8e8e8 pills.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #f2f2f2 | page canvas | 60% |
| #fefefe | list card | 22% |
| #010101 | display type, particles, active arrow, pill | 3% plus particles |
| #2e2e2e–#737373 | particle mid-tones, body text | 6% |
| #dedede | row dividers, chip fill | 1.3% |

WCAG checks:
- Black on #f2f2f2 is 18.65:1.
- Role labels (≈#454545) on white are 9.51:1.
- Bio grey (#737373) on white is 4.70:1 (just passes).
- White on the black "Email us" pill is 20.9:1.
- Chip text on #e8e8e8 is 17:1.

This is a strictly achromatic system.

## 5. Depth & material
- It is fully flat: no shadows, and the card is separated by fill alone (#fefefe on #f2f2f2).
- The only texture is the stipple portrait, which acts as a dither/halftone rendering made of individually animatable dots. Density maps luminance.
- At t=14.5 s a full continuous-tone photo appears momentarily, which shows the stipple is generated from a real photo.

## 6. Components & patterns
- **Accordion list:** a collapsed row shows its index, role and an outline arrow chip. The expanded row shows the name, a one-line bio, wrap-aligned skill chips (right-aligned, 2 rows) and a filled black arrow chip.
- **Large running counter** (01 → 06) mirrors the active row.
- **Meta header** with crosshair "+" registration marks.
- A black pill CTA, "Email us".

## 7. Motion
Measured: 17.4 s at 60 fps. motion_fraction is 0.36, there are 9 segments and the clip is a seamless loop (first/last diff 0.62).
- **Portrait morphs:** five long segments of 1.13–1.23 s (1.60–2.80, 4.20–5.37, 6.93–8.17, 11.27–12.40, 16.00–17.17 s), all with peak_at 0.19–0.31, i.e. ease-out. The particles burst away fast and settle slowly into the new face.
- **Accordion expand/collapse:** short 0.20–0.27 s ease-in-out segments (8.97, 10.23, 13.37, 14.57 s) that happen when the row changes without a portrait change.
- **Cadence:** about one person every 2.2–2.5 s.
- **Frame evidence:** at t=4.83 s the face is mid-dissolve, and at t=16.43 s it is scattering back to "01".

## 8. Brand system
n/a — not a brand system. Identity cues:
- a Swiss-poster section title;
- a parenthetical serif index "(00N)";
- the "+" registration marks;
- an achromatic studio voice ("Based in London").

## 9. UX
- Hover/click on a row is clear: the arrow chip inverts to black and the row expands with real content. The counter gives orientation.
- **Risks:**
  - Collapsed rows show only roles, not names.
  - Stipple faces are hard to recognise at small sizes.
  - Particle morphs on every hover could tire users; reduced-motion handling is needed.
  - The index numerals are at about 9 px.

## 10. Craft signals
- The counter digit changes in the same frame as the accordion state (frames 4.83 → 6.77 s both read "03" while Julian is expanded).
- The index uses an italic serif inside parentheses, a deliberate type contrast within a single row.
- The "+" markers sit on the same column lines as the meta labels above them.
- The active arrow chip fills black (#010101) while inactive chips stay outlined on #f2f2f2: one binary state cue.
- Chips align right and wrap from the right edge, balancing the left-aligned name and bio.
- The portrait bleeds off the bottom-left, anchoring the composition against the giant title.

## 11. Reproduction recipe
```css
:root{--canvas:#f2f2f2;--card:#fefefe;--ink:#010101;--muted:#737373;--line:#dedede;--chip:#e8e8e8}
.title{font:900 180px/0.8 "Inter Display",Helvetica,sans-serif;letter-spacing:-.03em;color:var(--ink)}
.count{font:400 52px/1 Inter;font-variant-numeric:tabular-nums}
.list{background:var(--card);border-radius:16px;padding:8px 16px}
.row{display:grid;grid-template-columns:60px 1fr 24px;align-items:center;min-height:53px;border-bottom:1px solid var(--line);
  transition:min-height .25s ease-in-out}
.row .idx{font:italic 9px Times,serif}
.row[aria-expanded=true]{min-height:150px}
.row[aria-expanded=true] .arrow{background:var(--ink);color:#fff}
.chip{border-radius:9999px;background:var(--chip);font:600 11px Inter;padding:4px 10px}
```
```js
// particle morph: sample target photo luminance into N points, tween each to new target
gsap.to(points,{x:i=>next[i].x,y:i=>next[i].y,duration:1.2,ease:"power3.out",stagger:{amount:.2,from:"random"}});
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 9 | A stark, poster-grade black-and-white layout. The stipple portraits are striking. |
| Originality | 8 | A particle-morph portrait synced to an accordion is a fresh team-page idea. |
| Usability | 7 | Clear state feedback and a counter. Names are hidden until expanded and the motion is heavy. |
| Craft | 8 | Grid-aligned markers, synced counter and type contrast are deliberate. |

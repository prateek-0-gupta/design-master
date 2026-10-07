---
id: insp-4-4
source: inspora
category: Print
status: analyzed
title: "Earnings posters"
creator: "@oliverhamrin"
styles: [swiss-grid-poster, photo-led, duotone, grain-noise]
patterns: [poster-series-slideshow, single-hue-series-system, type-over-face-collage, co-brand-lockup-footer, mockup-on-neutral-backdrop, pixel-mosaic-photo-grid]
mode: mixed
palette: ["#d4d4d4", "#f1f0ea", "#14acdf", "#20b7eb", "#94d9f0", "#2f63b8", "#1f6bff", "#353434"]
type_families: ["Helvetica Now / Neue Haas Grotesk (likely)"]
type_class: [neo-grotesk]
radius_px: [0, 4]
motion: {durations_s: [4.2, 0.47], easing: [hard-cut], loop: true}
scores: {aesthetics: 8, originality: 7, usability: 6, craft: 7}
craft_signals: [one-hue-across-nine-posters, paper-grain-and-crease-texture, fixed-frame-position-across-cuts, logo-lockup-bottom-corners, small-copy-in-quiet-zone]
anti_patterns: [illegible-stacked-type, small-body-on-photo]
---
# Earnings posters — @oliverhamrin

## 1. Snapshot
- **Subject:** A 4.2 s, 1280×1280 slideshow of nine print posters and book covers. Most are announcements for Quartr earnings calls (Meta, Goldman Sachs, Altria, Alcoa), mixed with personal covers ("Clear Thinking", "Lord Jim", "Halloween").
- **Why it's remarkable:** Every piece is locked to a single blue family (cyan #14acdf through ultramarine #2f63b8 and electric #1f6bff). Very different image treatments therefore read as one series: halftone bust, silhouette echoes, clay tube maze, cloud mosaic and argyle pattern.

## 2. Composition & layout
- **Backdrop:** a flat #d4d4d4 field (65% of the frame).
- **Poster placement:** each poster is centred at about 820×1053 px (x 229→1050, y 113→1166), a 4:5 / 0.78 portrait. That leaves a margin of about 113 px at top and bottom and about 230 px at the sides. Book covers are narrower, at about 620×950 px (0.65).
- **Corporate posters:** logo top-left or bottom-left, co-brand logo bottom-right, and a small 3–5 line details block at about 12 px equivalent tucked into a quiet zone. The "Goldman" poster puts the date block bottom-left at x≈1423/1932 of the sheet, under the silhouettes.
- **"Clear Thinking" cover:** a symmetrical sandwich. Author name (≈70 px cap height) sits above five nested rectangles that step in by about 42 px each, and the title sits below at the same size. The text block width equals the image width (388→893 px), so the type is justified to the image edges.
- **"Sent from my iPhone":** an 80 px module grid of cut-out sky squares. Four words are placed on grid cells, and three corporate-jargon paragraphs (≈15 px) sit in cell-aligned boxes.

## 3. Typography
- One neo-grotesk throughout, close to Helvetica Now Display / Neue Haas Grotesk. Look at the tight "a"/"r" joins, the horizontal terminals and the "ff"/"fi" in "efficiency".
- **Display:** about 70 px Medium on the book cover ("Shane Parrish") with tracking of −0.03 em. On the cloud poster the words are about 60 px Bold, white.
- **Overprint stack:** on the portrait poster, six words in #1f6bff about 55 px Regular are stacked with negative leading (≈0.55). They collide over the subject's eyes as a censor bar made of jargon.
- **Small copy:** 11–14 px Regular in 3–5 line blocks, ragged-right. Type on a circular path wraps the Meta infinity mark.

## 4. Colour
| Hex | Role | Approx share (key frame) |
|---|---|---|
| #d4d4d4 | presentation backdrop | 65% |
| #f1f0ea | warm paper white (cover stock) | 13% |
| #14acdf / #20b7eb | outer cyan bands | 10% |
| #4ac5ef / #94d9f0 / #c1e4ed | inner bands → gradient core | 9% |
| #2f63b8 | ultramarine poster grounds (Goldman, Altria, Alcoa) | — |
| #1f6bff | electric overprint type | — |
| #353434 | near-black type | 1.4% |

WCAG checks:
- Black (#111) on paper (#f1f0ea): 16.54:1.
- White on #2f63b8: 5.84:1 (pass).
- White on mid-sky #4a7cc8: 4.19:1. This fails AA-normal, which matters for the 15 px cloud paragraphs.
- Electric blue (#1f6bff) on near-black: 3.74:1 (large text only).
- White on cyan #14acdf would be 2.63:1. The designer correctly avoids it and uses black there.

## 5. Depth & material
The work is heavily physical. Posters carry paper grain, slight creases and edge wear (visible on the "Lord Jim" and "Alcoa" scans), and the book covers show a spine shadow about 6 px wide on the left. The Altria piece is a clay or tube 3D render whose soft drop shadows fall to the bottom-right. Elsewhere there is no digital shadow: depth comes from texture and the stepped nested frames, which create a tunnel illusion.

## 6. Components & patterns
- **Co-brand footer lockup:** Quartr mark (left) and the client mark (right), both about 14 px tall, set on the baseline about 30 px above the trim.
- **Event block:** day, date, company + quarter, "Live on Quartr at [time]". It is the same information order on every poster, which is the series' data template.
- **Image-as-metaphor:** an infinity loop drawn over the eyes for Meta, a maze made of a cigarette for Altria, and stepped silhouettes for Goldman.

## 7. Motion
Measured: duration 4.2 s at 5 fps sampling, motion_fraction 1.0, a single 4.0 s segment flagged "ease-in" (peak_at 0.93) with first/last difference 35.05. The "ease-in" reading is an artefact of cuts. The nine evenly spaced frames (0.23 → 3.97 s) each show a different poster, which puts a hard cut roughly every 0.47 s (estimate) with no transitions. The poster frame position stays fixed across cuts, so the eye stays parked while content swaps. That is the key to the "flip-book" feel. The clip loops on the platform, and seamless_loop_likely is false.

## 8. Brand system
n/a — a portfolio series rather than a brand system. Identity cues work as a mini-system for Quartr: a one-hue rule (blue only), a fixed info template, and co-brand marks in opposite bottom corners.

## 9. UX
As announcements, they deliver the who/when/where within about 40 words. The headline is the image, not the company name, so recognition relies on the client logo at about 14 px. Some text sits on busy photo areas (cloud poster), and the overprinted word stack is deliberately unreadable.

## 10. Craft signals
- The same blue family (#14acdf–#2f63b8) appears in all nine frames, with no off-palette accent except the cigarette's orange filter.
- The poster occupies an identical 820×1053 box in every cut.
- On "Clear Thinking", the type width equals the image width (388→893 px) on both lines.
- The nested frames step at a constant ~42 px and lighten one tint per step.
- The cloud poster's text boxes snap to the 80 px mosaic grid.

## 11. Reproduction recipe
```css
:root{--stage:#d4d4d4;--paper:#f1f0ea;--ink:#111;
  --b1:#14acdf;--b2:#20b7eb;--b3:#4ac5ef;--b4:#94d9f0;--ultra:#2f63b8;--electric:#1f6bff;
  --font:"Helvetica Now Display","Neue Haas Grotesk Display",Arial,sans-serif;}
.stage{background:var(--stage);display:grid;place-items:center;aspect-ratio:1}
.poster{width:64%;aspect-ratio:4/5;background:var(--paper);position:relative}
.nested{background:var(--b1);padding:42px}
.nested>div{background:var(--b2);padding:42px}
.nested>div>div{background:var(--b3);padding:42px}
.nested>div>div>div{background:linear-gradient(#7fd2f2,#eef4f6);min-height:420px}
.cover-title{font:500 70px/1 var(--font);letter-spacing:-.03em}
.overprint{color:var(--electric);font:400 55px/.55 var(--font);mix-blend-mode:normal}
/* slideshow: hard cuts */
.slides>*{animation:show 4.2s steps(1) infinite}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Strong, cohesive blue series with tactile print finish. |
| Originality | 7 | The image metaphors (cigarette maze, jargon mask) are witty, and the Swiss layout is familiar. |
| Usability | 6 | Event info is clear but tiny. Some small type sits on photos below AA. |
| Craft | 7 | Consistent framing and grid snapping. Overprint stack is legibility-hostile by design. |

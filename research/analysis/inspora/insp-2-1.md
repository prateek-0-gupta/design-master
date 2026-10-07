---
id: insp-2-1
source: inspora
category: Motion
status: analyzed
title: "Confidential file animation"
creator: "@AdityaSur11"
styles: [micro-interaction, playful-rounded, physical-material]
patterns: [hover-folder-cover-swing, document-peek-on-hover, card-pull-out-and-tilt, easter-egg-copy, 3d-perspective-card, sticker-gif-in-document]
mode: light
palette: ["#f6e9e0", "#2e59c9", "#274aaf", "#647bbf", "#ffffff", "#1a1a1a", "#c3c5d0"]
type_families: ["Inter (likely)", "JetBrains Mono / IBM Plex Mono (likely)"]
type_class: [neo-grotesk, mono]
radius_px: [24, 20]
motion: {durations_s: [0.93, 0.47, 0.4, 0.8, 0.9, 0.33], easing: [ease-out, ease-in-out, ease-in], loop: true}
scores: {aesthetics: 8, originality: 7, usability: 7, craft: 8}
craft_signals: [cover-hinges-on-left-edge-with-perspective, back-cover-darker-than-front, vertical-mono-do-not-open-tab, paper-rotates-few-degrees-when-pulled, vertical-gradient-on-folder, humour-payoff-after-warning]
anti_patterns: [legal-copy-small-and-rotated, subtitle-grey-on-blue-low-contrast]
---
# Confidential file animation — @AdityaSur11

## 1. Snapshot
- **Subject:** An 18.4 s, 1346×1080 clip of a single blue folder card labelled "CONFIDENTIAL FILES / Internal use only" on a peach canvas.
  - On hover, the cover swings open in 3D, revealing a sheet stamped "DO NOT OPEN".
  - On click, the sheet slides out, tilts and turns face-up. It shows a mock-serious warning ending with a cat-sticker punchline: "You really don't follow instructions, do you?"
- **Why it's remarkable:** A tiny narrative in a component. The interaction itself enacts the joke (you are told not to open it, and you open it).

## 2. Composition & layout
- **Folder:** about 188×235 px in the 1346-px key frame (≈400×495 in the key's own scale), centred, portrait ratio about 0.8. The canvas is roughly 85% empty peach.
- **Cover content:** a 6-petal asterisk logo top-left with 14 px inset; "CONFIDENTIAL FILES" mono caps bottom-left; "Internal use only" beneath in smaller sans.
- **Revealed sheet:** about 330×460 in the key frame. It overhangs the folder right edge by about 5 px and is rotated about −4°. Text is set in a column about 280 px wide with 14 px paragraphs.
- **Rest pose:** at 5.12 s the paper sits fully to the right of the opened folder, showing "DO NOT OPEN" as a vertical mono label along its right edge.

## 3. Typography
- **Mono caps** ("CONFIDENTIAL FILES", "DO NOT OPEN"): a JetBrains or IBM Plex Mono-like face, about 17 px on the cover (key frame) with about +0.08 em tracking. "DO NOT OPEN" is rotated 90°.
- **Sans:** an Inter-like face, regular, for the subtitle (≈15 px) and the document copy (≈15 px, leading ≈1.25, three short paragraphs).
- The register is deliberate: mono for the bureaucratic "stamp", sans for the human voice.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #f6e9e0 | canvas (peach paper) | 86% |
| #2e59c9 → #274aaf | folder front, vertical gradient top → bottom | ~3% |
| #647bbf (approx) | folder back cover / inner shade | <1% |
| #ffffff | sheet, cover text | 7% |
| #1a1a1a | document text | <1% |
| #c3c5d0 (approx) | cover subtitle tint | <1% |

WCAG checks:
- White on folder blue is 6.20:1 at the top and 7.82:1 at the bottom.
- Subtitle (≈#c3c5d0 on #2e59c9) is 3.61:1 (large only; it is small).
- Document text on white is 17.4:1.
- The folder blue against the peach canvas is 5.21:1, so the object is crisp at a glance.

Complementary pairing: warm peach versus cobalt blue.

## 5. Depth & material
- **Folder:** a thick card with about a 24 px radius. The front panel has a subtle vertical gradient (lighter top). The back cover is visible as a darker, narrower panel when the cover swings (1.02 s).
- **Paper:** white with about a 20 px radius and a soft drop shadow (about 0 8 24 rgba(0,0,0,.12)) when lifted.
- **Hinge:** the cover hinges on its left edge with real perspective foreshortening (the right edge grows taller as it swings toward the camera).

## 6. Components & patterns
- **Hover:** the cover rotates about 20–25° on the Y axis and the sheet peeks out from the right.
- **Click:** the sheet pulls out, rotates about −4° and comes to the front over the folder. The document copy is readable, with an animated cat sticker (GIF-like) as the punchline.
- **Reset:** the sheet tucks back and the cover closes (7.17 s neutral state).
- The same object loops through hover-only and click states several times.

## 7. Motion
Measured: 18.43 s at 30 fps, 14 segments, motion fraction 0.26, median 0.33 s, `seamless_loop_likely: true`.
- **1.53–2.47 s (0.93 s, peak 0.66 → ease-in):** The sheet pulls out and comes forward, building speed before landing.
- **4.00–4.97 s (two ease-out segments of 0.47 and 0.40 s, peaks 0.25–0.29):** The cover swings and the paper slides aside, with fast starts.
- **8.53–9.33 s (0.80 s, symmetric):** The second reveal. 12.73–13.63 s (0.90 s, peak 0.13 → ease-out) is the tuck-back.
- **14.5–18.2 s (repeated 0.17–0.33 s segments):** Hover peeks, short and snappy.
- Overall: about 0.3 s for hover feedback and about 0.8–0.9 s for the main reveal, a sensible two-tier timing.

## 8. Brand system
n/a — not a brand system. Identity cues: an asterisk/flower mark, cobalt plus peach palette, and a "secret document" humour voice.

## 9. UX
- **Strengths:** Hover previews the content (a peek), which teaches that a click opens it. The state returns cleanly.
- **Risks:**
  - The document text is small and rotated at about −4°, which reads fine for 3 seconds but not for real content.
  - The cover subtitle is low contrast.
  - The joke depends on hover, so on touch the peek stage is lost.

## 10. Craft signals
- The cover hinge uses perspective, so the far edge scales up, not a flat skew.
- The back cover is a darker blue than the front, which gives the folder thickness.
- "DO NOT OPEN" is set vertically in mono along the sheet's tab edge, like a file label.
- The sheet tilts about −4° when out, which reads as hand-pulled.
- The folder has a top-light vertical gradient (#2e59c9 → #274aaf).
- The copy pays off: three formal paragraphs, then the sticker plus a one-line jab.

## 11. Reproduction recipe
```css
:root{--canvas:#f6e9e0;--folder-top:#2e59c9;--folder-bot:#274aaf;--folder-back:#3f5fb8;--paper:#fff;--ink:#1a1a1a;}
.stage{perspective:1200px;background:var(--canvas)}
.folder{width:400px;height:495px;position:relative;transform-style:preserve-3d}
.folder .back{position:absolute;inset:0;border-radius:24px;background:var(--folder-back)}
.folder .sheet{position:absolute;inset:16px;border-radius:20px;background:var(--paper);
  transition:transform .9s cubic-bezier(.5,0,.25,1)}
.folder .sheet .tab{position:absolute;right:16px;top:24px;writing-mode:vertical-rl;font:500 14px "JetBrains Mono";letter-spacing:.08em}
.folder .cover{position:absolute;inset:0;border-radius:24px;background:linear-gradient(var(--folder-top),var(--folder-bot));
  transform-origin:left center;transition:transform .4s cubic-bezier(.2,.8,.2,1);color:#fff}
.folder:hover .cover{transform:rotateY(-24deg)}
.folder:hover .sheet{transform:translateX(30px)}
.folder.open .sheet{transform:translate(20px,-10px) rotate(-4deg) translateZ(40px);box-shadow:0 8px 24px rgba(0,0,0,.12)}
.cover .title{font:500 17px "JetBrains Mono";letter-spacing:.08em;text-transform:uppercase}
.cover .sub{font:400 14px Inter;color:rgba(255,255,255,.8)} /* raise from #c3c5d0 for AA */
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Confident complementary palette and a clean object; the mono/sans pairing fits the theme. |
| Originality | 7 | Folder-open hovers are common; the forbidden-document joke and payoff make it memorable. |
| Usability | 7 | The peek teaches the click and the states are clear; small rotated text and hover dependence hold it back. |
| Craft | 8 | Real hinge perspective, darker back cover, vertical tab label and well-tiered timing. |

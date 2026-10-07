---
id: insp-the-lord-of-horses
source: inspora
category: Motion
status: analyzed
title: "The Lord of Horses."
creator: "@krispuckett"
styles: [retro-pixel, soft-3d, micro-interaction, playful-rounded]
patterns: [dot-matrix-strip-in-input, typing-progress-mascot, expanding-chat-composer, voice-to-send-button-morph, listening-placeholder, device-close-up-camera]
mode: light
palette: ["#f5f5f5", "#eaeae6", "#dedfdc", "#474747", "#1a1a1a", "#aab4c2", "#aaacad"]
type_families: ["SF Pro Text (likely)"]
type_class: [neo-grotesk, pixel]
radius_px: [40, 9999]
motion: {durations_s: [7.7, 0.1, 0.13], easing: [ease-in-out, linear], loop: false}
scores: {aesthetics: 8, originality: 9, usability: 6, craft: 8}
craft_signals: [dot-grid-off-dots-visible, sprite-faded-trail, composer-grows-upward, mic-becomes-send-arrow, inner-bevel-composer, slate-blue-single-accent]
anti_patterns: [decorative-strip-costs-vertical-space, low-contrast-dot-grid]
---
# The Lord of Horses. — @krispuckett

## 1. Snapshot
- **Subject:** A 17.6 s, 3840×2160 close-up of a phone chat composer. A dot-matrix strip under the text field shows a pixel horse galloping across as the user dictates or types. When input ends, the mic button turns into a send arrow.
- **Why it's remarkable:** It turns the dead "listening / typing" state into a tiny ambient game. The horse is a progress or activity companion living in an LED-style strip inside the input.

## 2. Composition & layout
- **Camera:** The frame is a tilted 3D close-up of the bottom 30% of an iPhone, with the camera drifting and re-framing throughout (rotations of ±3° visible across frames). Assistant text above it is cut off.
- **Composer card (key frame, ×1.92 to source px):** about 1990×1150 px source (≈1036×600 shown). It contains:
  - a "+" attach glyph at the left, vertically centred on the text block;
  - a multi-line text area (4 lines at 3.8K);
  - beneath, a full-width dot-matrix strip ≈1750×250 px source (≈900×130 shown), inset ~70 px from the card edges.
- **Voice button:** a 180 px (≈95 shown) circle sitting outside the card at the right, aligned to the strip's centre line, not to the text.
- **Composer growth:** The composer grows from one line ("Listening", 0.98 s) to four lines, pushing its top edge upward while the strip stays bottom-anchored.

## 3. Typography
- **Body:** a system neo-grotesk (SF Pro Text). On-device it is ~17 pt; in this 4K close-up it is ~90 px with leading ~1.25.
- **Placeholder:** "Listening" in light grey (#aaacad).
- **Dictation preview:** During live dictation (2.94 s) the text appears in *italic*, then settles to roman once committed (4.89 s onward). This is a subtle typographic state change.
- **Pixel horse:** The horse is effectively a pixel font sprite: a ~22×14 cell bitmap on the dot grid.

## 4. Colour
| Hex | Role | Approx share |
|---|---|---|
| #f5f5f5 | stage and screen background | 72% |
| #eaeae6 / #dedfdc | composer fill, bevel shade | 19% |
| ≈#d0d0cc | dot-grid "off" pixels | — |
| #474747 / #1a1a1a | text, "on" pixels, phone bezel | 4% |
| #aab4c2 | mic / send button (slate blue) | 1% |
| #aaacad | placeholder | — |

WCAG checks:
- Text #1a1a1a on composer #f0f0ed: 15.24:1.
- "On" pixels #474747 on #f5f5f5: 8.52:1.
- **Placeholder #aaacad on #f5f5f5: 2.09:1 (fails)**.
- Glyph #1a1a1a on the slate button #aab4c2: 8.3:1.

## 5. Depth & material
- **Composer:** a soft-3D slab with a 1 px lighter top rim, a slight inner shade at the bottom edge and a broad diffuse shadow (~60 px blur) on the screen. It reads like frosted ceramic.
- **Strip:** recessed. The dot grid sits in a slightly darker well with the "off" dots visible, like an unlit LED panel.
- **Mic button:** a matte slate disc with a soft top highlight and drop shadow.
- **Phone:** rendered with a stainless edge and bottom port detail. The scene is lit from the top-left.

## 6. Components & patterns
- **Dot-matrix strip:** a grid of roughly 120×16 square dots at ~1:1 pitch. The horse sprite runs left to right across it with a 2–3-frame gallop cycle, and a faded trail of half-tone dots marks its recent path.
- **Dictation flow:**
  - "Listening" placeholder;
  - streaming italic transcript;
  - committed roman text that wraps and grows the composer.
- **Send morph:** At 16.64 s the waveform icon in the slate button becomes "↑", with the same disc and colour.
- **"+" button:** an unboxed glyph inside the composer, not a separate circle, which keeps the right-side button the sole primary control.

## 7. Motion
Measured profile: 17.62 s at 60 fps, `motion_fraction` 0.45, not a seamless loop.
- **0–7.7 s (7.7 s, peak 0.39, symmetric):** one long continuous segment combining the camera drift, the horse running and the composer growing. Frame differences show the horse crossing the strip roughly once every 2–3 s (estimate). Its x-position at 0.98 s is at 25% of the strip, at 4.89 s at 75%, and at 6.85 s at 30% on a new lap.
- **7.8 s (0.10 s, ease-in) and 16.07 s (0.13 s, ease-out):** short discrete events. The latter matches the mic→send icon swap, an instant ~130 ms cut.
- **Text growth:** Composer growth happens per wrapped line, with a short height tween estimated at ~0.25 s.
- **Gallop:** Sprite motion is stepped (pixel frames) while the horizontal travel is linear, the classic retro sprite rhythm.

## 8. Brand system
n/a — not a brand system. Identity cues:
- a horse mascot;
- a dot-matrix display language;
- a single slate-blue accent on an achromatic warm-grey UI.

## 9. UX
- **Strengths:**
  - Live feedback that the system is hearing you, which a static "Listening" label does not give.
  - The italic-then-roman transcript makes provisional versus final text legible.
  - The send arrow appears only when there is content.
- **Risks:**
  - The strip costs ~130 pt of vertical space permanently.
  - If the horse is not tied to audio level or typing speed, it is decoration rather than signal (the frames suggest constant speed).
  - The placeholder fails contrast.

## 10. Craft signals
- Unlit dots stay visible in the strip, so the LED-panel illusion holds even when the horse is off-screen.
- A half-tone trail follows the sprite (visible at 6.85 s and 12.72 s).
- The composer grows upward while the strip and button keep their baseline.
- The mic morphs to a send arrow inside the identical disc.
- Italic marks provisional dictation, roman marks committed text.
- The palette is all achromatic except one desaturated slate (#aab4c2).

## 11. Reproduction recipe
```css
:root{--stage:#f5f5f5;--composer:#efefeb;--dot-off:#d6d6d2;--dot-on:#474747;--ink:#1a1a1a;--accent:#aab4c2}
.composer{background:var(--composer);border-radius:20px;padding:16px 20px;
  box-shadow:inset 0 1px 0 #fff, inset 0 -1px 0 rgba(0,0,0,.06), 0 18px 40px rgba(0,0,0,.08);
  transition:height .25s cubic-bezier(.3,.7,.4,1)}
.strip{height:64px;border-radius:10px;
  background-image:radial-gradient(circle,var(--dot-off) 1.2px,transparent 1.4px);background-size:4px 4px}
.horse{image-rendering:pixelated;animation:run 2.4s linear infinite, gallop .24s steps(3) infinite}
@keyframes run{from{transform:translateX(-10%)}to{transform:translateX(110%)}}
.voice{width:48px;aspect-ratio:1;border-radius:50%;background:var(--accent);color:var(--ink)}
.transcript.provisional{font-style:italic;opacity:.85}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Soft ceramic UI with a crisp pixel sprite: a charming contrast of materials. |
| Originality | 9 | A running mascot inside the input field is a genuinely new take on input feedback. |
| Usability | 6 | Delightful, but decorative unless coupled to input. It costs space and the placeholder fails contrast. |
| Craft | 8 | Visible off-dots, trail and icon morph are careful. Camera drift makes measuring hard. |

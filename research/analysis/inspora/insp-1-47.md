---
id: insp-1-47
source: inspora
category: Motion
status: analyzed
title: "voice note / interaction"
creator: "@proskuaaa"
styles: [micro-interaction, physical-material, playful-rounded]
patterns: [sticker-icon-action-sheet, voice-recorder-widget, scrubbing-playhead-waveform, odometer-digit-roll, scrim-dim-on-overlay, camera-push-in-on-focus, mixed-media-grid-cards]
mode: mixed
palette: ["#ffffff", "#acacac", "#262626", "#181818", "#050505", "#888683", "#a59d8e", "#2f6bff"]
type_families: ["Inter / SF Pro-style neo-grotesk (likely)"]
type_class: [neo-grotesk]
radius_px: [9999, 48, 24, 18]
motion: {durations_s: [0.27, 1.0, 0.93], easing: [ease-out, ease-in], loop: true}
scores: {aesthetics: 8, originality: 8, usability: 7, craft: 8}
craft_signals: [die-cut-sticker-icons, dot-grid-sheet-texture, odometer-timer-digits, recording-red-dot-under-play, blue-playhead-with-end-caps, scrim-greys-underlying-ui, camera-zoom-to-recorder]
anti_patterns: [light-grey-metadata-fails-contrast, play-pause-glyph-ambiguous]
---
# voice note / interaction — @proskuaaa

## 1. Snapshot
- **Subject:** A 10.9 s, 1080×1080 phone-mockup clip of a shared shopping-list app ("Sunday Brunch Prep"). The user taps "+", picks the mic from a sticker-style action board, and records a voice note in a dark hardware-like recorder card.
- **Why it's remarkable:** The add menu is a scatter of die-cut icon stickers on a dotted board, not a list. The recorder then looks like a physical gadget (dark slab, round keycaps), so it reads as a mode change.

## 2. Composition & layout
- **Phone:** An iPhone frame about 280 px wide (26% of the canvas) sits centred on pure white. From t≈2.2 s the camera pushes in about 1.5× and crops the phone bottom so the recorder fills about 60% of the frame. It pulls back out at t≈9.1 s.
- **Feed:** A two-column card grid with about 10 px gutters and cards around 112×112 px (in phone points ≈ 160×160). There are product cards (title top-left at about 13 px, size label beneath, packshot bottom-right), sticky-note cards (yellow `#e9cf8f`-ish, pink), and a full-width voice-note row with two waveforms.
- **Action board (f1):** A sheet about 400×340 px in phone points. Five 56 px icons are placed off-grid at deliberate tilts. A "Show labels" toggle pill sits bottom-left and a circled × bottom-right.
- **Recorder card:** about 600×660 px in the key frame. An inner "screen" panel (≈560×430) holds the waveform, the timer and the caption, with a row of three round buttons below (≈110 px stop/delete, ≈135 px centre).

## 3. Typography
- A neo-grotesk, SF Pro or Inter-like. The header "Sunday Brunch Prep" is about 20 pt semibold. Card titles are about 15 pt regular with tight leading (≈1.1).
- **Timer:** "00:01" is about 44 px bold in the key frame with tabular figures. The last digit rolls vertically (the frame at 6.64 s catches "0" sliding out and "3" sliding in), an odometer effect.
- **Caption:** "New Audio from you" is about 18 px regular grey `#888683` with a 24 px avatar inline. Metadata ("14 pieces | 2 days ago") is about 10 pt in light grey.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #ffffff | stage, cards, sheet | 36% |
| #acacac | scrim-dimmed feed | 18% |
| #262626 / #181818 | recorder slab / inner screen | 33% |
| #050505 | phone bezel, icons | 4% |
| #888683 | recorder caption | 3% |
| #2f6bff (approx) | playhead | <1% |
| #e31b23 (approx) | recording dot | <1% |

WCAG checks:
- White on #181818 is 17.76:1.
- Caption #888683 on #181818 is 4.89:1 (pass).
- Black on white is 19.8:1.
- Grey metadata at about #acacac on white is **2.27:1 (fail)**.
- The blue playhead on #181818 is 3.95:1, which is fine for a non-text graphic (3:1).

## 5. Depth & material
- **Recorder:** The card is a two-tier dark slab. The outer #262626 bezel has about a 48 px radius, and the inner screen is a step darker (#181818) with about a 32 px radius and a faint inner shadow, like an LCD recessed into a device.
- **Buttons:** Round with a 1 px lighter rim and an inset dark face, like keycaps.
- **Sheet:** The action sheet has a 1 px dot grid at about 12 px pitch over #f4f4f4. Each icon has a ~4 px white outline and a soft drop shadow (sticker die-cut).
- **Scrim:** When an overlay opens, the feed behind darkens to #acacac-level grey. There is no blur.

## 6. Components & patterns
- Sticker-icon action board with five actions (scan barcode, add image, add mic, add note, add person) plus a "Show labels" switch. The labels are opt-in, which keeps the board pictorial.
- **Voice-recorder widget:**
  - The live waveform grows leftwards from a fixed blue playhead, with dotted silence to the right.
  - Stop / play-pause / delete buttons.
  - A red dot under the centre button signals that recording is active.
- **Voice-note list row:** avatar, play button, static grey waveform, duration "01:09".
- A floating search pill "I need…" with sort and add icons forms the bottom bar.

## 7. Motion
Measured: 10.87 s at 60 fps, 3 segments, motion fraction 0.20, `seamless_loop_likely: true`.
- **1.03–1.30 s (0.27 s, peak 0.19 → ease-out):** The action sheet springs up from the + button while the scrim fades in.
- **2.17–3.17 s (1.00 s, peak 0.75 → ease-in):** The sheet dismisses and the recorder rises, combined with the camera push-in. The energy builds late, so the zoom accelerates into place.
- **9.07–10.00 s (0.93 s, peak 0.02 → ease-out):** The camera pulls back and the recorder dismisses with a fast start.
- **Between segments:** The waveform bars append steadily at about 10 bars/s (an estimate from frames). Timer digits roll vertically in about 0.2 s (estimate).

## 8. Brand system
n/a — not a brand system. Identity cues: hand-drawn doodles on the sticky notes (heart and arrow, "MQ" hand), die-cut sticker iconography, and grocery packshots, which together give a warm, domestic and collaborative tone.

## 9. UX
- **Strengths:** Recording state is unambiguous: dark mode change, red dot, running timer, moving waveform. Destructive delete is separated to the far right.
- **Risks:**
  - The combined play/pause glyph "▶II" on the centre key does not say which action a tap performs.
  - The sticker board with labels off relies on icon literacy.
  - Light-grey metadata fails contrast.

## 10. Craft signals
- Each sheet icon has a uniform ~4 px white outline and a shadow, so they read as die-cut stickers.
- The playhead has round end-caps (≈8 px dots) top and bottom.
- The timer's last digit animates as an odometer while the other digits stay static.
- The red recording dot sits exactly under the play glyph, inside the same keycap.
- The inner screen radius (≈32) is smaller than the outer (≈48), a concentric-radius correction.
- The scrim greys the feed but keeps the sticky-note yellow visible as desaturated ochre.

## 11. Reproduction recipe
```css
:root{--slab:#262626;--screen:#181818;--ink:#fff;--muted:#888683;--play:#2f6bff;--rec:#e31b23;
  --r-slab:48px;--r-screen:32px;--ease-out:cubic-bezier(.16,1,.3,1);}
.recorder{background:var(--slab);border-radius:var(--r-slab);padding:20px;
  box-shadow:0 30px 60px rgba(0,0,0,.25),inset 0 1px 0 rgba(255,255,255,.06)}
.recorder .screen{background:var(--screen);border-radius:var(--r-screen);
  box-shadow:inset 0 2px 8px rgba(0,0,0,.6)}
.playhead{width:4px;background:var(--play);border-radius:2px;position:relative}
.playhead::before,.playhead::after{content:"";position:absolute;left:-3px;width:10px;height:10px;border-radius:50%;background:var(--play)}
.playhead::before{top:-5px}.playhead::after{bottom:-5px}
.key{width:110px;aspect-ratio:1;border-radius:50%;background:#1e1e1e;box-shadow:inset 0 0 0 1px rgba(255,255,255,.08)}
.sticker{filter:drop-shadow(0 0 0 #fff) drop-shadow(0 2px 4px rgba(0,0,0,.2));
  /* white die-cut outline */ -webkit-text-stroke:0; outline:none}
.sticker svg{stroke:#fff;paint-order:stroke;stroke-width:8px}
.sheet{background:#f4f4f4 radial-gradient(#d6d6d6 1px,transparent 1px) 0 0/12px 12px;border-radius:36px;
  animation:rise .27s var(--ease-out)}
@keyframes rise{from{transform:translateY(40px);opacity:0}}
.digit{display:inline-block;transition:transform .2s var(--ease-out);font-variant-numeric:tabular-nums}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Calm white feed, then a dense dark gadget, with sticker charm in between. |
| Originality | 8 | The die-cut sticker action board and the hardware-like recorder are fresh for a list app. |
| Usability | 7 | Recording state is very clear. The play/pause glyph and hidden labels add ambiguity. |
| Craft | 8 | Concentric radii, playhead caps and odometer digits are carefully done. Metadata contrast is weak. |

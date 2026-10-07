---
id: insp-iphone-duo
source: inspora
category: Motion
status: analyzed
title: "This iPhone Duo animation"
creator: "@avstorm"
styles: [photo-led, cinematic-3d, corporate-clean]
patterns: [foldable-device-concept, unfold-reveal, progressive-unblur, hands-on-device-demo, ipados-style-home-grid, widget-column-reflow]
mode: light
palette: ["#e1e1e3", "#323438", "#a07c6c", "#c2ac9f", "#674d49", "#93a1a2", "#2f6fc4"]
type_families: ["SF Pro (system, likely)"]
type_class: [neo-grotesk]
radius_px: [130, 40, 34]
motion: {durations_s: [1.3, 0.67, 2.32], easing: [ease-out, ease-in-out], loop: false}
scores: {aesthetics: 8, originality: 7, usability: 6, craft: 7}
craft_signals: [blur-as-unfolded-placeholder, hinge-crease-visible, consistent-studio-backdrop, dock-moves-to-right-rail, wallpaper-continues-across-fold]
anti_patterns: [white-labels-on-light-wallpaper, concept-presented-as-real-product]
---
# This iPhone Duo animation — @avstorm

## 1. Snapshot
- **Subject:** A 2.32 s, 2840×1590 @60 fps concept clip: a hand unfolds a book-style foldable iPhone from portrait phone to a landscape mini-tablet, and the iOS home screen reflows to fill the new canvas.
- **Why it's remarkable:** The newly revealed half of the screen enters heavily blurred and sharpens over about 0.8 s, so the software appears to "catch up" with the hinge — a believable OS-level unfold transition, not just a hardware render.

## 2. Composition & layout
- Seamless studio sweep (#e1e1e3) with no horizon; device centred, occupying ~50% of frame width when open (x≈810→2080 px original, y≈305→1230).
- Live-action hands enter bottom-left and bottom-right, cropped at the frame edge; they anchor scale (unfolded device ≈ 1270×920 px ≈ a 7–8" tablet relative to a palm).
- Closed state (t=0.13 s): portrait phone ~180 px wide in the sheet frame, lower-centre; open state recentres slightly upward.
- **Home grid, open:** right half = two 2×2 widgets (Weather, Find My, ~210 px square each) above a 4×4 icon grid (~80 px icons, ~115 px pitch); left half = Now Playing widget + a tall Calendar widget; the dock is rotated into a vertical rail at the far right (Phone, Safari, Messages, Music) with time 9:41 and Wi-Fi above it.

## 3. Typography
- Apple system UI: SF Pro (Text for labels, Display/Rounded numerals in widgets). Widget numeral "54°" ≈ 60 px original, labels ≈ 18–20 px semibold white with soft shadow, widget captions ≈ 16 px.
- No title or marketing type added — the clip relies entirely on in-device type.

## 4. Colour
| Hex | Role | Approx share |
|---|---|---|
| #e1e1e3 | studio backdrop | 59% |
| #323438 | device bezel / frame | 6% |
| #a07c6c / #674d49 | skin tones, dune wallpaper shadow | 12% |
| #c2ac9f / #b3a399 | sand wallpaper highlight | 10% |
| #93a1a2 | blue-grey sky of wallpaper | 4% |
| #2f6fc4 | Weather widget blue (est.) | <2% |

WCAG checks:
- White icon labels on dune shadow #a07c6c: **3.75:1** (AA-large only).
- White labels over sand highlight #c2ac9f: **2.17:1 (fails)** — the "Siri"/"Settings" labels lose legibility; the stock OS text shadow is doing the work.
- White on Weather blue #2f6fc4: 5.01:1.
- Bezel #323438 on backdrop #e1e1e3: 9.55:1 — the silhouette reads instantly.

## 5. Depth & material
- Photographic: soft top-light, no hard shadows under the device, gentle vignette toward the left edge (#d4d3d2 band).
- Titanium-grey frame with a lighter edge highlight; the fold crease is suggested by a faint vertical seam at the screen midline and a slight bezel kink at top/bottom centre (t=0.90 s frame).
- Depth-of-field blur is applied to the unfolding half (~40 px Gaussian equivalent at t=0.90 s), reading as both motion blur and "content not yet loaded".

## 6. Components & patterns
- Foldable unfold reveal (hardware + OS in one shot).
- Widget reflow: the portrait 2-up widget row (Weather, Find My) stays put while new widgets (Now Playing, Calendar) materialise in the left half.
- Dock → vertical rail: the dock relocates to the right edge in landscape, an iPadOS-like adaptation.
- Final beat (1.93–2.19 s): the left hand releases and a finger reaches in to tap the Calendar widget — closing with an interaction cue.

## 7. Motion
Measured (m0_motion.json): 2.32 s, 60 fps, motion_fraction 0.74, two segments, not a seamless loop (first/last diff 37.5).
- **Segment 1, 0.00–1.30 s (1.30 s), peak_at 0.19 → ease-out:** the hinge swing is fastest at the start (≈0.25 s) and decelerates as the device settles flat at ~1.2 s — like a real hand flicking a fold open.
- **Hold ~1.30–1.60 s:** the blur clears on the left pane (estimated from frames 0.90→1.42→1.67 s: blurred → partially resolved → sharp).
- **Segment 2, 1.60–2.27 s (0.67 s), peak_at 0.42 → symmetric ease-in-out:** the hand moves to tap the widget.
- The ratio of ~2:1 between reveal and follow-up gesture keeps the hardware moment dominant.

## 8. Brand system
n/a — not a brand system. Identity cues imitate Apple's launch-film grammar: neutral sweep, real hands, 9:41 time, stock wallpaper. This is a fan concept, not an Apple asset.

## 9. UX
- Communicates a continuity model clearly: the existing half stays sharp and interactive, the new half "arrives" — users never lose their place.
- The blur placeholder doubles as a performance budget story (render the new area progressively).
- **Risks:** blur on half the screen for ~0.8 s would feel sluggish in a real OS; white labels over the sandy wallpaper fail contrast; the right-rail dock moves muscle-memory targets.

## 10. Craft signals
- Unblur sequence is monotonic across three sampled frames (0.90 / 1.42 / 1.67 s) — no popping.
- The wallpaper dune continues across the fold line without a seam once open.
- Bezel kink and crease visible at the midline in the 0.90 s frame — the render respects the hinge.
- Time 9:41 and Wi-Fi glyph relocate to top of the right rail, preserving status-bar function.
- Backdrop value is constant (#e1e1e3) frame to frame — no exposure flicker between plates.

## 11. Reproduction recipe
```css
.pane-new{filter:blur(24px);opacity:.7;transform:scaleX(.6);transform-origin:right center;
  animation:unfold 1.3s cubic-bezier(.16,1,.3,1) forwards, unblur .8s .5s cubic-bezier(.4,0,.2,1) forwards;}
@keyframes unfold{to{transform:scaleX(1)}}
@keyframes unblur{to{filter:blur(0);opacity:1}}
.stage{background:#e1e1e3}
.device{border-radius:130px/120px;box-shadow:0 0 0 10px #323438}
.label{color:#fff;text-shadow:0 1px 2px rgba(0,0,0,.45);font:600 13px/1.1 -apple-system,"SF Pro Text",system-ui}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Convincing Apple-grade studio look; clean neutral sweep. |
| Originality | 7 | Foldable concepts are common; the blur-as-arrival idea is the fresh part. |
| Usability | 6 | Continuity reads well, but label contrast and moved dock targets are weak. |
| Craft | 7 | Hinge detail and seamless wallpaper are good; the blurred pane is long. |

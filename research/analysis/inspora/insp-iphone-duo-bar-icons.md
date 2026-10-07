---
id: insp-iphone-duo-bar-icons
source: inspora
category: Illustration
status: analyzed
title: "iPhone Duo"
creator: "@avstorm"
styles: [minimal-swiss, monochrome, micro-interaction, x-speculative-os]
patterns: [vertical-status-rail, battery-as-ring-gauge, signal-as-dot-arc, stacked-status-glyphs, floating-round-back-button, content-dimmed-behind-chrome]
mode: light
palette: ["#dddddd", "#c0c0c0", "#010203", "#717171", "#9a9a9a", "#eaeaea"]
type_families: ["SF Pro Rounded / SF Pro Display Semibold (likely)", "SF Pro Text (body, likely)"]
type_class: [neo-grotesk, rounded-sans]
radius_px: [320, 9999]
motion: null
scores: {aesthetics: 8, originality: 8, usability: 6, craft: 8}
craft_signals: [battery-ring-wraps-wifi-glyph, dot-signal-follows-ring-curvature, centre-axis-stack-on-camera, stroke-weight-matches-time-digits, glass-button-rim-and-drop-shadow, ring-gap-at-bottom-for-dots]
anti_patterns: [faint-body-text-1-6-to-1, unlabeled-battery-percent, crop-hides-full-rail]
---
# iPhone Duo — @avstorm

## 1. Snapshot
- **Subject:** One 2560×1751 still. It is a cropped close-up of the top-right corner of a hypothetical iPhone ("Duo") whose status bar is rotated into a **vertical rail** under the punch-hole camera: time, Wi-Fi inside a battery ring, a cellular dot arc, then a round back button.
- **Why it's remarkable:** It merges three status indicators into one compound glyph. A battery arc encircles the Wi-Fi symbol, and four signal dots continue the circle's lower gap. A 3-item horizontal row becomes a single 290 px emblem.

## 2. Composition & layout
- **Crop:** The device corner fills the left ~62% of the frame. The grey backdrop (#c0c0c0) sits outside, and the screen radius is very large (≈320 px source) with a 2–3 px lighter bezel line.
- **Rail axis:** Everything is centred on one vertical axis at x≈1230 px source, the camera centre:
  - camera, 269 px diameter, y≈420;
  - "9:41", cap height ≈77 px, y≈700;
  - battery/Wi-Fi ring, ≈295 px, y≈950;
  - dot arc, y≈1080;
  - back button, ≈352 px, y≈1360.
- **Spacing:** Vertical gaps are about 90–110 px between elements, so the rhythm is even.
- **Content:** The app content (a journal: "Monday", paperclip, body text) is pushed left of the rail and dimmed. The status rail effectively becomes a sidebar.

## 3. Typography
- **Time:** "9:41" is in a rounded-terminal grotesk Semibold, consistent with SF Pro (rounded variant likely). Digits are about 105 px tall in source with tabular spacing and a tight colon.
- **Body:** The body text is about 95 px source (it is a zoomed close-up) in SF Pro Text Regular, at grey 40% value. "Monday" is set right-aligned at about 85 px in a lighter grey.
- **Hierarchy:** Hierarchy is pure value. The chrome is near-black (#010203) and the content sits at #9a9a9a/#b0b0b0, a reversal of the usual (content-forward) priority, used to spotlight the concept.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #dddddd / #eaeaea | screen surface | 53% |
| #c0c0c0 | outer backdrop | 43% |
| #010203 | camera, time, icons, full battery arc | 1.2% |
| #717171 / #b0b0b0 | depleted arc segment, inactive signal dots | ~1% |
| #9a9a9a | dimmed body copy | — |

The image is fully achromatic. The only hue is the indigo lens reflection inside the camera.

WCAG checks:
- Time #010203 on #dddddd is 15.29:1.
- The inactive dot or depleted arc (#717171) is 3.59:1, which passes as a graphic object (3:1).
- Body #9a9a9a on #dddddd is **2.07:1**, and "Monday" (#b0b0b0) is **1.6:1**. Both fail; this is intentional for the mockup but would not ship.
- Screen vs backdrop is 1.34:1, separated only by the bezel highlight.

## 5. Depth & material
- **Back button:** a soft glass-white disc with a 2 px grey rim (~#a0a0a0) on its lower half, a brighter rim highlight on top, an inner radial lift and a diffuse drop shadow (~40 px blur, 15% black, offset ~20 px down). It reads as a physical bead, in the iOS 26 "Liquid Glass" vein.
- **Everything else is flat:** stroked glyphs at about 14 px source (≈1/20 of ring diameter).
- **Screen edge:** a faint 1–2 px white highlight on the screen edge shows the glass bevel.

## 6. Components & patterns
- **Battery ring:** a ~300° arc. The black portion is the charge (about 80%) and the grey tail at right is the remainder, with a gap at the bottom.
- **Signal dots:** four dots follow the same circle radius in the gap. Two black and two grey mean 2/4 bars, a clever reuse of the arc's missing segment.
- **Wi-Fi:** the standard 3-band glyph at about 105 px wide, centred inside the ring.
- **Back control:** a circular floating button with a chevron (stroke ≈14 px, matching the icons).

## 7. Motion
Still image. The ring geometry strongly implies an animated sweep for charging (e.g. a 0.6 s ease-out arc fill) and dots filling sequentially. None was observed.

## 8. Brand system
n/a — this is not a brand system. It is a speculative Apple-style UI. Cues are the "9:41" convention, SF typography and the iOS glass button.

## 9. UX
- **Strengths:** The compound glyph saves vertical space in a rail and keeps everything readable at a glance. Ring = battery is an intuitive gauge (as on Apple Watch).
- **Risks:**
  - Without a percentage the ring's 80% vs 75% is hard to read.
  - Signal dots on the same circle as the battery may be confused as part of the battery.
  - The rail costs ~20% of the screen width in portrait.
  - Tap target: the back button at ~352 px source is roughly a 60 pt control. Generous.

## 10. Craft signals
- The battery ring's bottom gap (~60°) is exactly where the four signal dots sit, on the same radius.
- Icon stroke weight (~14 px) equals the time digits' stem weight, so the glyphs and type feel one family.
- All rail elements share one x-centre with the camera hole.
- The ring's depleted segment uses a mid-grey, not opacity, so it keeps flat colour on any background.
- The back button has a two-tone rim (light top, darker bottom) for a convex reading.

## 11. Reproduction recipe
```html
<svg viewBox="0 0 100 100" width="96" aria-label="Battery 80%, Wi-Fi, signal 2 of 4">
  <!-- arc starts at 7 o'clock (rotate 120deg), 300deg total = 83.3 of pathLength 100 -->
  <g transform="rotate(120 50 50)" fill="none" stroke-width="5" stroke-linecap="round">
    <circle cx="50" cy="50" r="40" pathLength="100" stroke="#b0b0b0" stroke-dasharray="83.3 100"/>
    <circle cx="50" cy="50" r="40" pathLength="100" stroke="#010203" stroke-dasharray="66.6 100"/> <!-- 80% charge -->
  </g>
  <!-- 4 dots along the bottom gap at r=40, angles 105°,95°,85°,75°; first two #010203, last two #b0b0b0 -->
</svg>
```
```css
:root{--screen:#dddddd;--ink:#010203;--ink-off:#b0b0b0;--rail-gap:28px}
.rail{display:flex;flex-direction:column;align-items:center;gap:var(--rail-gap)}
.time{font:600 30px/1 "SF Pro Rounded",system-ui;font-variant-numeric:tabular-nums}
.back{width:88px;aspect-ratio:1;border-radius:50%;background:radial-gradient(circle at 50% 30%,#fafafa,#e4e4e4);
  box-shadow:inset 0 1px 0 #fff,inset 0 -1.5px 0 #a0a0a0,0 12px 24px -8px rgba(0,0,0,.18)}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Calm, monochrome, beautifully aligned; the glass button adds one tactile note. |
| Originality | 8 | Fusing battery, Wi-Fi and signal into one ring is a genuinely new glyph idea. |
| Usability | 6 | The glance-gauge works, but battery precision is lost and the signal/battery distinction is ambiguous. |
| Craft | 8 | Shared radii, axis and stroke weights; the body text dimming is overdone. |

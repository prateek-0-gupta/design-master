---
id: insp-look-away-preview
source: inspora
category: Product
status: analyzed
title: "Look Away preview"
creator: "kush (@kushsolitary)"
styles: [glassmorphism, spatial-ui, micro-interaction]
patterns: [menubar-widget-panel, segmented-now-stats-toggle, countdown-hero-with-rolling-digits, snooze-chip-row, stat-rows-with-app-icon-badges, arc-gauge-score, panel-height-morph]
mode: dark
palette: ["#5b3603", "#763e08", "#e7a043", "#e57b32", "#c34529", "#091a2e", "#e3a877", "#ffffff"]
type_families: ["SF Pro Rounded / SF Pro Display (likely)"]
type_class: [rounded-sans, neo-grotesk]
radius_px: [60, 22, 9999, 10]
motion: {durations_s: [0.23, 0.2, 0.2, 0.23, 0.2], easing: [ease-out, ease-in-out], loop: false}
scores: {aesthetics: 9, originality: 6, usability: 8, craft: 9}
craft_signals: [glass-tint-sampled-from-wallpaper, rolling-digit-with-motion-blur, peach-tinted-secondary-labels, gradient-arc-gold-to-magenta, hairline-light-rim-on-panel, icon-badges-carry-the-only-saturation]
anti_patterns: [stats-view-overflows-panel]
---
# Look Away preview — kush

## 1. Snapshot
- **Subject:** A 13.9 s, 1160×1032 recording of "Look Away", a macOS menu-bar widget, over an orange Ventura-style wallpaper.
  - The **Now** tab shows "Break starts in" with a large countdown (24:29 to 24:17), a "Start break now / +1m / +5m" chip row, and two stat rows.
  - The **Stats** tab shows "Today's Screen Score" with a 100 gold-to-magenta arc gauge, an encouragement line and a Focus Score list.
- **Why it's remarkable:** It is native-feeling glass done right. The panel takes its amber-brown tint from the wallpaper, every secondary label is tinted peach rather than grey, and the countdown digits roll with motion blur.

## 2. Composition & layout
- **Panel:** about 840×750 px (x≈150–990, y≈138–888) in the key frame, with a corner radius of about 60 px (macOS Tahoe-like continuous corners).
- **Top bar:** a centred segmented control (≈345×64 px, pill) and a gear with chevron at top right.
- **Now view, centred stack:**
  - hourglass icon 30 px;
  - "Break starts in" at about 26 px;
  - countdown about 80 px Bold;
  - chip row at y≈585: primary "Start break now" ≈268×64 px and two outline chips ≈120×64 px.
- **Stat rows:** two rows of about 775×78 px with a 18 px gap, radius about 22 px. Each has an icon badge (48 px, radius 10) on the left and the value on the right.
- **Stats view:** a date pager pill with arrows, an arc gauge about 170 px wide, 2 lines of copy, and a list card. It is taller than the Now view, and the panel grows (it is cropped at the bottom in the recording).

## 3. Typography
- SF Pro (Display for the numerals, Rounded-feel at heavy weights).
  - Countdown about 80 px Bold with tabular figures; the colon is optically aligned.
  - Labels about 26 px Medium.
  - Chips about 24 px Semibold.
  - Row labels about 26 px Regular; values Semibold.
- Secondary text ("Break starts in", gear) is tinted peach (#e3a877), not grey. That keeps the warm palette through the hierarchy.

## 4. Colour
| Hex | Role | Approx share |
|---|---|---|
| #5b3603 / #763e08 / #6a2804 | panel glass (wallpaper-tinted brown) | ~46% |
| #e7a043 / #e57b32 / #d3582c / #c34529 | wallpaper ribbons | ~35% |
| #091a2e / #201d28 | wallpaper navy sky | ~11% |
| #e3a877 | secondary labels, icons | <1% |
| #ffffff | primary text | <2% |
| ≈#c9a21a / ≈#c84fd6 | focus (gold) and break (magenta) badges, gauge arc | <1% |

WCAG checks (contrast.py):
- White on the panel #5b3603: **10.64:1**. On the lighter lower panel #763e08: **8.53:1**. On a stat row ≈#7f5120: **6.77:1**.
- Peach label #e3a877 on #5b3603: **5.13:1** (pass).
- White on the "Start break now" chip ≈#8a5a30: **5.86:1**.
- Everything passes. The glass is dark enough to keep contrast stable over a bright wallpaper.

## 5. Depth & material
- **Panel:** heavy backdrop blur plus a dark brown multiply tint. A 1 px light rim runs around the edge (visible as a thin warm highlight at the top and left), with a soft dark shadow below.
- **Inner rows:** lighter translucent fills (about +8% white) with no borders.
- **Chips:** the primary chip is a light translucent fill; the secondary chips are 1 px outlines at about 20% white.
- **Segmented control:** an outline track with a filled translucent thumb.
- The icon badges are the only opaque, saturated objects: a gold lightning bolt and a magenta leaf, each with a subtle gradient.

## 6. Components & patterns
- **Segmented toggle:** Now / Stats.
- **Countdown hero** with snooze chips (+1m / +5m) and a primary "Start break now".
- **Stat rows:** icon badge, label and right-aligned value, with a "·" separator in "Short · 1 min".
- **Stats view:**
  - a date pager ("‹ Today's Screen Score ›");
  - a 270° arc gauge with an outer dotted tick ring, a gold outer arc and a magenta inner arc;
  - an encouragement copy line;
  - a Focus Score list with bullet dots in gold.

## 7. Motion
- Measured (threshold 0.43): 13.9 s, `motion_fraction` 0.08, 5 segments, all **0.20–0.23 s**.
  - Tab switches at 2.63 s (0.23 s ease-out, peak 0.21), 5.47 s (0.20 s symmetric), 8.67 s (0.20 s ease-out), 11.9 s (0.23 s symmetric) and 13.63 s (0.20 s ease-out).
  - Not looped.
- **From frames (estimates):** at 2.31 s the last countdown digit is mid-roll ("8" sliding out upward with vertical motion blur and the next digit entering), so each digit change is an odometer roll of about 0.25 s. At 8.47 s the same effect appears on "1".
- The tab switch changes panel height (Stats is taller), and the content crossfades.

## 8. Brand system
n/a — not a brand system. Identity cues: the hourglass glyph, gold = focus and magenta = break as semantic colours, and wallpaper-adaptive glass.

## 9. UX
- The primary task (when is my break, and delay or take it now) is answerable in one glance. Snooze increments are one tap.
- **Risks:**
  - The Stats view overflows the visible panel in the capture.
  - The gauge reading of "100" next to "60/60" is two different scales, which could confuse.
  - Relying on the wallpaper tint means contrast varies on light wallpapers (it is fine here).

## 10. Craft signals
- The panel tint is sampled from the wallpaper (brown #5b3603 over orange ribbons) rather than neutral grey.
- Secondary labels are peach (#e3a877), not grey, and still pass at 5.13:1.
- The countdown digits roll with directional motion blur.
- Saturation is reserved for the two icon badges and the gauge.
- A 1 px light rim on the panel separates the glass from a bright wallpaper.
- The secondary chips are outlined while the primary chip is filled, all at a 64 px height.

## 11. Reproduction recipe
```css
:root{--glass:rgb(70 38 4 / .78);--row:rgb(255 255 255 / .08);--rim:rgb(255 220 180 / .35);
  --ink:#fff;--ink-2:#e3a877;--focus:#c9a21a;--break:#c84fd6;--r-panel:30px;--r-row:11px}
.panel{background:var(--glass);backdrop-filter:blur(40px) saturate(1.6);border-radius:var(--r-panel);
  box-shadow:inset 0 0 0 1px var(--rim),0 20px 50px #0006;color:var(--ink);font-family:-apple-system,"SF Pro Display",sans-serif;
  transition:height .23s cubic-bezier(.16,1,.3,1)}
.seg{border:1px solid #ffffff26;border-radius:9999px;padding:3px}
.seg [aria-selected=true]{background:#ffffff26;border-radius:9999px}
.count{font:700 40px/1 -apple-system;font-variant-numeric:tabular-nums}
.digit{display:inline-block;overflow:hidden;height:1em}
.digit.roll>span{animation:roll .25s cubic-bezier(.3,0,.2,1)}
@keyframes roll{from{transform:translateY(100%);filter:blur(2px)}to{transform:none;filter:none}}
.chip{height:32px;border-radius:9999px;border:1px solid #ffffff33;padding:0 14px;font-weight:600}
.chip.primary{background:#ffffff2e;border-color:transparent}
.row{background:var(--row);border-radius:var(--r-row);display:flex;align-items:center;gap:10px;padding:8px 14px}
.label-2{color:var(--ink-2)}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 9 | Warm, native-quality glass; the palette is harmonised with the wallpaper. |
| Originality | 6 | macOS widget conventions executed very well; the digit roll and peach labels are refinements, not new ideas. |
| Usability | 8 | Instantly legible, one-tap actions, all contrast passes; Stats overflow and dual scales. |
| Craft | 9 | Rim lights, tabular rolling digits, tinted secondaries and consistent heights. |

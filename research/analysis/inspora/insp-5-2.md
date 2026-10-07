---
id: insp-5-2
source: inspora
category: Product
status: analyzed
title: "Balance details"
creator: "@malikyoloo"
styles: [micro-interaction, dither-halftone, photo-led, corporate-clean]
patterns: [portfolio-balance-card, led-segment-bar-chart, odometer-number-roll, asset-dropdown-chip, timeframe-tab-underline, privacy-eye-toggle, chart-reflow-on-filter]
mode: light
palette: ["#ffffff", "#111111", "#8a8a8a", "#f59e0b", "#ebebeb", "#2ecc40", "#57bfe4", "#c06147"]
type_families: ["Inter / SF Pro-style neo-grotesk (likely)"]
type_class: [neo-grotesk]
radius_px: [44, 9999]
motion: {durations_s: [0.2, 5.53], easing: [ease-in-out, linear], loop: false}
scores: {aesthetics: 8, originality: 8, usability: 6, craft: 8}
craft_signals: [grey-dollar-sign-black-digits, segmented-equalizer-bars, glow-on-active-segments, odometer-digit-roll, dot-matrix-overlay-on-photo, underline-indicator-matches-label-width]
anti_patterns: [green-delta-2-1-contrast, orange-data-on-white-low-contrast, chart-has-no-axis-or-values]
---
# Balance details — @malikyoloo

## 1. Snapshot
- **Subject:** A 6.97 s, 2000×1500, 60 fps demo of a crypto "Total portfolio value" card. The user switches the asset (USDC → SOL) via a dropdown chip and then switches the timeframe (1M → 1W). The balance rolls like an odometer, and an LED-style segmented bar chart re-levels.
- **Why it's remarkable:** The chart is drawn as an audio-equalizer of stacked dashes (lit orange vs unlit grey), which gives finance data a hi-fi hardware feel. It sits over a blurred tulip photo overlaid with a white dot-matrix pattern.

## 2. Composition & layout
- **Card:** ≈930×918 px (x≈535–1465, y≈283–1200 in the key frame), centred and fully symmetric, with a corner radius of ≈44 px.
- **Vertical stack, all centred:**
  - label "Total portfolio value" (y≈374)
  - asset chip (y≈455)
  - balance (y≈575)
  - delta line (y≈657)
  - ≈180 px of breathing room
  - chart (y≈765–1010)
  - timeframe tabs (y≈1077)
- **Chart:** 11 columns of ≈64 px wide dashes with ≈16 px gaps. Each column has 12 dash slots at ≈20 px pitch; each dash is ≈8 px tall with a fully rounded radius.
- **Tabs:** 1D/1W/1M/6M/1Y/All are evenly distributed across the card width. The active tab carries a ≈48×4 px black underline.

## 3. Typography
- **Typeface:** neo-grotesk, close to Inter or SF Pro.
- **Balance:** ≈80 px Bold. The "$" is the same size but in mid grey (#8a8a8a), so the digits dominate.
- **Label and chip:** "Total portfolio value" is ≈32 px Semibold; the chip text "SOL" is ≈34 px Medium.
- **Delta line:** ≈32 px. The percentage is green and "Last month" is grey. It uses a European decimal comma ("24,5%") while the balance uses a decimal point ("573.22"), which is inconsistent.
- **Tabs:** ≈28 px Medium; the active tab is black and the inactive tabs are grey.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #ffffff | card surface | ~24% |
| #57bfe4 / #80c1e3 | sky in backdrop | ~38% |
| #c06147 / #ab9b74 | tulips, stems (blurred) | ~11% |
| #111111 | balance digits, title, active tab | ~1% |
| #8a8a8a | "$", meta text, inactive tabs | <1% |
| #f59e0b (est.) | lit chart segments | ~1% |
| #ebebeb | unlit chart segments | ~1% |
| #2ecc40 (est.) | positive delta | trace |

**WCAG:**
- Balance #111 on white is **18.88:1**.
- Grey meta text is **3.45:1** (passes large only).
- **The green delta is 2.14:1** and fails AA.
- The orange segments are **2.15:1** against white, which is below 3:1 for graphical objects. Unlit segments are 1.19:1, which is acceptable because they are decorative.

## 5. Depth & material
- The card is flat white with a very soft shadow, floating on a heavily blurred photo (≈40 px blur).
- **Backdrop texture:** a white dot-matrix overlay (≈8 px dots on a ≈22 px grid) appears only over the red tulip shapes, which is a dither/halftone flourish.
- Lit chart segments have a soft orange glow (≈6 px blur), like LEDs. Unlit segments are flat light grey.
- The asset chip is a light grey pill (#f1f2f4) with a coin icon.

## 6. Components & patterns
- **Asset dropdown chip:** opens an inline list (USDT, SOL, BNB) overlapping the balance (frame at 1.94 s), with no separate sheet.
- **Privacy toggle:** an eye icon after the balance.
- **Odometer number change:** at 2.71 s, the digits are mid-roll ("$573.983.64" ghosting), each digit sliding vertically.
- **Segmented equalizer chart:** each column's lit stack represents the value band, with the selected period shown via tabs.
- **Timeframe tabs:** the underline indicator slides between tabs (at 5.03 s it is mid-travel between 1W and 1M).

## 7. Motion
**Measured:**
- Duration 6.97 s, motion fraction **0.84**, `seamless_loop_likely: false`.
- Two segments: 0.40–0.60 s (**0.20 s**, symmetric — the cursor/chip hover) and 1.23–6.77 s (**5.53 s**, continuous). The long segment is continuous because the backdrop dots appear to shimmer and the cursor moves, so the detector never drops below threshold.

**From frames:**
- **Dropdown:** opens about 1.5–1.9 s.
- **Balance roll:** about 2.5–3.2 s (estimated ~0.5 s, digits staggered).
- **Chart re-level:** segments light and fade per column with a left-to-right wave (2.71 s frame shows the old and new levels blended).
- **1W tab:** clicked at about 5.0 s. The underline slides in an estimated ~0.3 s, and the chart reflows to 9 columns (6.58 s frame).

## 8. Brand system
n/a — not a brand system. Identity cues: an amber LED equalizer as the data motif, a grey currency symbol, and a nature photo with a dot-matrix overlay as the ambient backdrop.

## 9. UX
- **Strengths:**
  - Strong hierarchy: one big number, a short delta, then the trend.
  - The asset chip lets you scope instantly.
  - The odometer roll signals that the value changed rather than just swapping it.
- **Risks:**
  - The chart has no values, axis or scrubbing (decorative rather than analytical).
  - The quantised segments lose precision.
  - The green and orange contrast fails.
  - Decimal separators are mixed.
  - The dropdown list covers the balance it controls.

## 10. Craft signals
- The "$" is set in grey at the same size as the digits, so the number reads first.
- Chart dashes are fully rounded with consistent ≈8 px thickness and ≈12 px spacing. Lit dashes glow; unlit dashes do not.
- The underline indicator width matches the label width (~48 px), not the tab cell.
- Digit roll is staggered per position (frame 2.71 s shows different digits mid-transition).
- The dot-matrix overlay is masked to warm regions only, so the sky stays clean behind the card.

## 11. Reproduction recipe
```css
:root{--card:#fff;--ink:#111;--ink-2:#8a8a8a;--lit:#f59e0b;--unlit:#ebebeb;--up:#16a34a;--chip:#f1f2f4;
  --r-card:44px;--font:"Inter","SF Pro Display",system-ui,sans-serif;}
.card{background:var(--card);border-radius:var(--r-card);padding:72px 44px 64px;text-align:center;
  box-shadow:0 30px 80px rgba(0,40,80,.12);font-family:var(--font)}
.balance{font:700 80px/1 var(--font);font-variant-numeric:tabular-nums;color:var(--ink)}
.balance .cur{color:var(--ink-2)}
.digit{display:inline-block;height:1em;overflow:hidden}
.digit>span{display:block;transition:transform .5s cubic-bezier(.2,.8,.2,1);transition-delay:calc(var(--i)*40ms)}
.eq{display:grid;grid-template-columns:repeat(11,1fr);gap:16px;height:245px;align-items:end}
.col{display:flex;flex-direction:column-reverse;gap:12px}
.seg{height:8px;border-radius:9999px;background:var(--unlit);transition:background .25s,box-shadow .25s}
.seg.on{background:var(--lit);box-shadow:0 0 6px rgba(245,158,11,.55)}
.tab[aria-selected=true]::after{content:"";display:block;height:4px;width:100%;background:var(--ink);border-radius:2px;margin-top:8px}
```
(The darker #16a34a "up" colour is a contrast-safe replacement for the original bright green.)

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | A fresh, playful card; the LED chart and dot-matrix photo feel distinctive. |
| Originality | 8 | An equalizer-segment chart plus odometer is an uncommon take on a balance widget. |
| Usability | 6 | Clear hierarchy, but the chart lacks values and the colour contrast fails. |
| Craft | 8 | Thoughtful digit roll and consistent segment geometry; decimal inconsistency. |

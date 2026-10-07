---
id: insp-5-1
source: inspora
category: Product
status: analyzed
title: "subscription tracker calendar"
creator: "Maxim Kuznetsov"
styles: [dark-premium, terminal-mono, data-dense, hairline-ui]
patterns: [month-grid-calendar, tile-per-day, brand-logo-as-event-marker, billing-cycle-dot-legend, today-outlined-cell, footer-summary-bar, hatched-out-of-month-days]
mode: dark
palette: ["#212121", "#111111", "#161616", "#2c2c2c", "#a8a8a8", "#ff6a2b", "#a78bfa", "#facc15"]
type_families: ["Geist / Inter-style grotesk (likely)", "Geist Mono / JetBrains Mono-style monospace (likely)"]
type_class: [neo-grotesk, mono]
radius_px: [32, 13, 9999]
motion: null
scores: {aesthetics: 8, originality: 7, usability: 8, craft: 9}
craft_signals: [diagonal-hatch-for-adjacent-month-days, dot-top-right-of-cell-encodes-cycle, mono-uppercase-weekday-chips, single-orange-accent-today-and-add, totals-in-mono-right-aligned, inset-grid-tray-on-card]
anti_patterns: [white-on-orange-plus-below-aa, cell-vs-tray-low-separation]
---
# subscription tracker calendar — Maxim Kuznetsov

## 1. Snapshot
- **Subject:** A 2560×1920 still of a dark month-view calendar widget (January 2026). Days on which a subscription bills carry the service's logo (Netflix, Adobe, Apple, Figma, Slack…). A coloured dot marks monthly or yearly billing, and a footer shows "MONTHLY TOTAL: $156.23".
- **Why it's remarkable:** It treats a billing ledger as a calendar of brand marks. The app needs almost no text because the logos are the data.

## 2. Composition & layout
- **Card:** ≈858×973 px real (≈670×760 displayed ×1.28), centred on a #212121 stage with a faint diagonal line texture and dashed construction guides. Card radius is ≈32 px real.
- **Header:** about 120 px real tall. It holds the month title, a "Today" outline pill, prev/next chevrons and an orange "+" pill at the right.
- **Grid tray:** an inset darker panel with a 7×5 grid of square cells ≈106 px real, a ≈8 px gutter and a ≈13 px radius.
- **Weekday labels:** sit in their own pill chips (≈106×48 px).
- **Below the grid:** a legend row (Monthly/Yearly dots, left) and a count ("9 SUBSCRIPTIONS / 3 NEW", right).
- **Footer toolbar:** separated by a hairline. It holds a kebab, a vertical divider, search/download/AI-sparkle icons on the left and the monthly total on the right.
- **Margins:** the left and right edges of every row align to a single ≈34 px real inset.

## 3. Typography
- **Title:** "January, 2026" is a neo-grotesk (Geist/Inter-like) at ≈32 px real Regular, in white.
- **Everything else** is monospace (Geist Mono / JetBrains Mono-like) at ≈20–22 px real. This covers day numbers, weekday chips (uppercase MON…SUN), the legend, counts and totals.
- Letterspaced uppercase mono is used for meta labels ("MONTHLY TOTAL:"). The value "$156.23" is in white for emphasis, while the label is grey.
- **Pairing logic:** sans for the human-readable title, mono for tabular and system data.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #212121 | stage | ~95% |
| #111111 / #161616 | card header/footer, grid tray | ~4% |
| #2c2c2c | day cells, weekday chips | ~1% |
| #a8a8a8 | day numbers, labels | trace |
| #ff6a2b (est.) | today outline/number, "+" button | trace |
| #35211b | today cell fill (orange-tinted) | 0.3% |
| #a78bfa / #facc15 (est.) | monthly / yearly dots | trace |

**WCAG:**
- Day numbers (#a8a8a8 on #2c2c2c) are **5.87:1**, and labels on the tray are **5.24:1** (both pass).
- The today number (#ff6a2b on #35211b) is **5.31:1**.
- The white "+" on the orange pill is **2.86:1**. That fails 3:1 for a graphical object, although the glyph is large.
- Cell vs tray is **1.3:1**. The cells read as soft bumps rather than defined boxes.

## 5. Depth & material
- There are no shadows. Depth is a value stack: stage #212121 → tray #161616 (recessed) → cells #2c2c2c (raised) → header/footer #111111.
- **Adjacent-month cells** (29/30/31 of December, 1 of February) are filled with a fine diagonal hatch instead of a flat tint. This echoes the stage's diagonal texture, a print-like "void" marker.
- **Today** is marked by a 1.5 px orange outline plus a warm-tinted fill.

## 6. Components & patterns
- **Day cell:** the number is top-centred, the brand logo (≈28 px) is centred below it, and a ≈8 px billing-cycle dot sits top-right.
- **Header controls:** a "Today" ghost pill (1 px #3a3a3a border), chevron buttons, and a primary "+" pill.
- **Legend** with dot keys, and a summary counter.
- **Footer action bar:** outline icons at 1.5 px stroke and an AI sparkle icon, which suggests smart import.

## 7. Motion
Still image, so no motion was observed.

## 8. Brand system
n/a — not a brand system. Identity cues: a single orange (#ff6a2b-ish) used only for "today" and "add", a mono-first voice, and hatch texture as a signature.

## 9. UX
- **Strengths:**
  - The logo-on-date encoding makes upcoming charges recognisable at a glance.
  - The dots distinguish billing cadence without extra text.
  - The total and count give an immediate summary.
- **Risks:**
  - Multiple subscriptions on the same day are not shown, so there is no stacking pattern.
  - Logos with dark colours (Apple grey, the 3D cube) have low contrast on #2c2c2c.
  - The "+" contrast fails.
  - The two dot colours (purple/yellow) need a non-colour cue for colour-blind users.

## 10. Craft signals
- Weekday chips use exactly the cell width, so the columns are visually locked.
- Billing dots sit at a consistent ≈10 px real inset from each cell's top-right corner.
- The diagonal hatch on out-of-month cells matches the background texture's angle (≈30°).
- Mono is used for every number, so numerals align in every cell.
- The legend's left edge, the grid's left edge and the footer kebab share one inset.
- The orange accent appears exactly twice ("+" and today).

## 11. Reproduction recipe
```css
:root{--stage:#212121;--card:#111;--tray:#161616;--cell:#2c2c2c;--ink:#fff;--ink-2:#a8a8a8;--accent:#ff6a2b;
  --monthly:#a78bfa;--yearly:#facc15;--r-card:32px;--r-cell:13px;
  --sans:"Geist","Inter",system-ui,sans-serif;--mono:"Geist Mono","JetBrains Mono",ui-monospace,monospace;}
.cal{background:var(--card);border-radius:var(--r-card);width:858px;font-family:var(--mono);color:var(--ink-2)}
.tray{background:var(--tray);border-radius:calc(var(--r-card) - 4px);padding:34px;display:grid;
  grid-template-columns:repeat(7,1fr);gap:8px}
.dow{background:var(--cell);border-radius:var(--r-cell);text-transform:uppercase;font-size:20px;text-align:center;padding:10px 0}
.day{aspect-ratio:1;background:var(--cell);border-radius:var(--r-cell);position:relative;text-align:center;padding-top:12px;font-size:22px}
.day[data-cycle]::after{content:"";position:absolute;top:10px;right:10px;width:8px;height:8px;border-radius:50%;background:var(--monthly)}
.day[data-cycle=yearly]::after{background:var(--yearly)}
.day.out{background:repeating-linear-gradient(-30deg,#1c1c1c 0 2px,#161616 2px 6px)}
.day.today{background:#35211b;box-shadow:inset 0 0 0 1.5px var(--accent);color:var(--accent)}
.add{background:var(--accent);border-radius:9999px;width:84px;height:56px;color:#fff}
.total b{color:var(--ink);font-variant-numeric:tabular-nums}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | A disciplined dark mono aesthetic; the colourful logos pop as the only chroma. |
| Originality | 7 | A calendar with logos is a strong framing of subscription data. |
| Usability | 8 | Highly glanceable, with a clear summary; same-day collisions and a dot-only legend are open issues. |
| Craft | 9 | Exacting alignment, purposeful hatch, minimal accent usage. |

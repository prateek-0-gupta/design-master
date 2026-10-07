---
id: insp-4-3
source: inspora
category: Product
status: analyzed
title: "Weather Widget"
creator: "@raul_dronca"
styles: [glassmorphism, gradient-mesh, playful-rounded, micro-interaction]
patterns: [weather-widget, half-orb-horizon, frosted-lower-band, condition-color-mapping, day-tab-strip, unit-segmented-toggle, color-morph-on-select]
mode: light
palette: ["#ffffff", "#f0f3f9", "#587196", "#475d7c", "#91a0b6", "#e86a1c", "#111111"]
type_families: ["Nunito / Nunito Sans-style rounded sans (likely)"]
type_class: [rounded-sans, humanist-sans]
radius_px: [70, 24, 18]
motion: {durations_s: [], easing: [ease-in-out], loop: true}
scores: {aesthetics: 9, originality: 8, usability: 7, craft: 8}
craft_signals: [orb-cut-by-glass-horizon, blurred-reflection-below-horizon, condition-hue-drives-orb, rounded-stroke-icons-match-type, day-strip-overflow-cue, single-accent-from-content]
anti_patterns: [inactive-day-labels-below-aa, date-label-low-contrast]
---
# Weather Widget — @raul_dronca

## 1. Snapshot
- **Subject:** A 20.0 s, 2876×2160 (60 fps) demo of a light-mode weather widget for Chicago. Each day tab (Mon 3 to Fri) re-colours a "setting sun" half-orb to match the condition: orange for Sunny, blue/orange swirl for Partly cloudy, beige/slate for Cloudy, slate blue for Rain.
- **Why it's remarkable:** The weather is encoded as a material, not an illustration. A gradient orb sinks behind a frosted glass horizon, and its blurred colour bleeds through the glass below, so the whole card is tinted by the forecast.

## 2. Composition & layout
- **Card:** ≈915×1010 px real (key frame ≈635×700 displayed ×1.44), centred on pure white, with a corner radius of ≈70 px real.
- **Header row:** city (≈40 px real) and date at top-left. A °F/°C toggle sits top-right, ≈190×85 px real.
- **Orb:** a half-disc ≈650 px wide, centred, rising from the horizon line at about 50% of card height.
- **Lower band:** frosted. It holds the temperature (≈115 px real) and condition label left, and a ≈130 px outline weather icon right, both vertically centred on the orb's blurred reflection.
- **Day strip:** at the bottom, five tabs with ≈190 px pitch. The fifth ("Fri") is cut off at the card edge, signalling horizontal scroll.

## 3. Typography
- A rounded humanist sans with soft terminals, close to Nunito / Nunito Sans. The "7" and "2" are geometric, and the "R" and "a" are open.
- **Temperature:** ≈115 px real, Regular. The degree sign is set superscript at ~45% size.
- **Other text:** the condition is ≈48 px real Medium; the city is ≈40 px Medium; date and day tabs are ≈36–40 px Regular grey.
- **Weights:** only Regular and Medium. Hierarchy comes from size.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #ffffff | stage, active tab chip | ~86% |
| #f0f3f9 | card tint (cool white) | ~5% |
| #587196 / #475d7c | Rain orb blue | ~3% |
| #91a0b6 / #7c8ba1 | blurred reflection under glass | ~2% |
| #e86a1c (est., Sunny frame) | Sunny orb orange | per state |
| #111111 | temperature, icon, active label | ~1% |

**WCAG:**
- The temperature #111 on the card is **16.99:1**. It is still **7.11:1** on the darkest reflection (#91a0b6), so the glass band keeps text readable in every state.
- The date grey (≈#7a7f88) is **3.62:1**.
- Inactive day tabs (≈#9aa0aa) are **2.32:1** and fail AA.

## 5. Depth & material
- **Horizon:** the orb is a sphere with an internal swirl gradient. Its lower half passes behind a frosted panel (heavy backdrop blur, ~60 px), which turns it into a soft reflected glow. A 1 px lighter line marks the glass edge.
- **Card:** has a large, very soft drop shadow (≈80 px blur, 6–8% black) and a faint cool tint.
- **Active chips:** the active day chip and the °F chip are solid white on the tinted card. They are raised by tint and a subtle shadow.

## 6. Components & patterns
- **Unit toggle:** a two-option segmented control (°F/°C) with a white thumb.
- **Day strip:** tabs with a white pill (≈170×95 px real, radius ≈24 px) for the active day.
- **Condition icons:** in a rounded 2 px-stroke style (sun, sun+cloud, cloud, cloud+rain) that matches the type's soft terminals.
- **Colour mapping:** the orb hue is the condition, so the visual changes even before the label is read.

## 7. Motion
**Measured:**
- The motion profile records 0 segments (motion fraction 0.00, mean energy 0.05), and `seamless_loop_likely: true`.
- This happens because the widget occupies only ~20% of a 2876×2160 frame. The colour cross-fades are slow and low-energy and fall below the detector threshold, so treat the following as frame-based estimates.

**From frames:**
- A day tab is clicked about every 2.2 s (Mon → Tue → Wed → Thu → Thu → Wed → Tue → Mon).
- The orb's gradient morphs between condition palettes over an estimated 0.6–1.0 s. At 16.68 s the orb is mid-blend (blue/orange) and the "Sunny" label is still fading in at partial opacity.
- The active-tab pill moves to the clicked day. The temperature and date update with a short fade.
- The transition reads as a smooth ease-in-out cross-fade, not a slide.

## 8. Brand system
n/a — not a brand system. Identity cues: the half-orb "horizon" mark, which could serve as an app icon, and a rounded type plus rounded icon family.

## 9. UX
- **Strengths:**
  - Glanceable: the colour gives the condition, the big number gives the temperature, and the tabs answer "which day".
  - The overflow cue on the day strip is good.
  - Text sits on a frosted band whose blur keeps contrast stable regardless of orb colour.
- **Risks:**
  - Inactive tabs and the date are below AA.
  - No high/low or precipitation figures.
  - Five days are shown but the strip scroll was not demonstrated.

## 10. Craft signals
- The orb is exactly bisected by the glass horizon. The reflection below is the same orb blurred, not a separate shape.
- Icons use the same corner rounding and stroke weight as the type's terminals.
- The active-tab white equals the stage white (#fff), so active elements read as holes through the tinted card.
- The left text column (city, temperature, first tab) shares one x-inset of ≈52 px real.
- Only one chromatic element exists at a time; everything else is cool greys.

## 11. Reproduction recipe
```css
:root{--card:#f0f3f9;--ink:#111;--ink-2:#7a7f88;--ink-3:#9aa0aa;--r-card:70px;--r-chip:24px;
  --orb-a:#587196;--orb-b:#2f4466;--font:"Nunito","Nunito Sans",system-ui,sans-serif;}
[data-cond=sunny]{--orb-a:#f2a04e;--orb-b:#d9480f}
[data-cond=cloudy]{--orb-a:#d8c3ad;--orb-b:#5f6b80}
.card{position:relative;border-radius:var(--r-card);background:var(--card);overflow:hidden;
  box-shadow:0 40px 80px rgba(20,30,50,.08)}
.orb{position:absolute;left:50%;top:21%;width:71%;aspect-ratio:1;translate:-50% 0;border-radius:50%;
  background:radial-gradient(60% 60% at 70% 40%,var(--orb-b),var(--orb-a));
  transition:background 0.8s ease-in-out}
.glass{position:absolute;inset:50% 0 0 0;backdrop-filter:blur(60px) saturate(1.2);
  background:rgba(240,243,249,.35);border-top:1px solid rgba(255,255,255,.7)}
.temp{font:400 115px/1 var(--font);color:var(--ink)}
.day[aria-selected=true]{background:#fff;border-radius:var(--r-chip);color:var(--ink)}
.day{color:var(--ink-3);transition:background .3s,color .3s}
```
`@property` registered colours (`--orb-a`, `--orb-b` as `<color>`) let the gradient itself interpolate.

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 9 | A gorgeous, restrained card whose single chromatic orb carries the mood. |
| Originality | 8 | The half-orb behind a glass horizon is a fresh weather metaphor. |
| Usability | 7 | Highly glanceable; secondary labels fail contrast and data is minimal. |
| Craft | 8 | Consistent rounded system and clever reflection-through-glass detail. |

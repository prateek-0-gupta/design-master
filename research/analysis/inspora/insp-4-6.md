---
id: insp-4-6
source: inspora
category: Web
status: analyzed
title: "Hero Section"
creator: "elaya (@elayadesigns)"
styles: [photo-led, x-anime-illustration, hairline-ui]
patterns: [illustrated-sky-hero, stat-grid-2x2, segmented-budget-bar, hatched-fill-segment, ai-video-ambient-loop, signal-metaphor-object]
mode: dark
palette: ["#105db4", "#0a76c8", "#4196cf", "#e5d6cd", "#b2bbcc", "#c69556", "#a14e29", "#ffffff"]
type_families: ["Inter Display / Geist-style neo-grotesk (likely)"]
type_class: [neo-grotesk]
radius_px: [12, 6]
motion: {durations_s: [6.06], easing: [step], loop: false}
scores: {aesthetics: 8, originality: 8, usability: 5, craft: 6}
craft_signals: [diagonal-hairline-sky-texture, hatched-vs-solid-bar-segments, hairline-leader-ticks-under-bar, metaphor-object-carries-message, white-only-type-on-photo]
anti_patterns: [text-over-busy-image-risk, inconsistent-number-formatting, label-clipped-at-bar-end, tiny-axis-labels]
---
# Hero Section — elaya

## 1. Snapshot
- **Subject:** A 1760×1080, 6.06 s clip of a hero for "Finmain", a budgeting product. It sets a white stat panel over an anime-style painted sky, and a traffic light and road signs (a "40" limit and two arrows) occupy the right third.
- **Why it's remarkable:** The headline "Know when to stop spending." is acted out by the illustration. The traffic light's red lamp blinks on and off, so the hero image carries the value proposition and no extra UI is needed.

## 2. Composition & layout
- **Frame:** The page sits inset in a presentation frame (~65 px left and right, ~40 px top) on a blurred orange/yellow/blue bezel. The page itself is about 1630×1000.
- **Left column:** It starts at x≈256 (about 16% of the frame) and is ~530 px wide. Stacked from y≈170 to y≈740:
  - logo
  - 36 px headline
  - 2-line deck
  - a 2×2 stat grid with columns at x 256 and 560 (gap ~300 px) and rows ~95 px apart
  - a 532×95 px segmented bar with a leader-tick axis beneath
- **Right side:** The x≈1120–1580 band holds the signal post. Clouds fill the bottom-right diagonal, so the text sits on the cleanest stretch of sky (upper left).
- **Balance:** The rule of thirds works well. The text block and the lit red lamp sit at roughly the same height (y≈620 for the lamp, y≈625 for the bar), which links data to signal.

## 3. Typography
- **Typeface:** A single neo-grotesk with tight apertures and a geometric "g", close to Inter Display or Geist.
  - Headline: ~36 px semibold (600), tracking about −0.01 em.
  - Deck: ~17 px regular at about 1.45 leading.
  - Stat labels: ~17 px regular.
  - Stat values: ~30 px regular with proportional figures. "3,159,224.74 €" places the euro sign after the number with a space.
  - Axis labels: ~14 px semibold values over ~12 px regular captions, which is tiny for this background.
- **Scale:** 36 / 30 / 17 / 12, which is a flat scale. Values are almost headline-size, so the numbers compete with the claim.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #105db4 | upper-sky / text field | 18% |
| #0a76c8 | mid sky | 17% |
| #4196cf / #5e9ac8 | lower sky near clouds | 11% |
| #e5d6cd / #b2bbcc | cloud highlights and shadows | 12% |
| #c69556 / #a14e29 | presentation bezel (amber/rust) | 8% |
| #ffffff | all UI text, bar fill | — |
| ~#5ce07a (est.) | logo tile accent | <0.1% |
| red lamp ~#e3242b (est.) | signal | <0.5% |

WCAG checks:
- White on #105db4 is **6.47:1** (pass).
- White on #0a76c8 is **4.73:1** (pass).
- Where the Whole Budget column drifts toward lighter sky (#4196cf) it is **3.24:1**, which fails for the 12 px axis captions.
- White over cloud (#e5d6cd) would be 1.42:1. The layout avoids this, but it breaks at narrower viewports.

## 5. Depth & material
- **Backdrop:** a painterly, flat-lit cel style (Makoto Shinkai-like clouds). Depth comes from atmospheric perspective and cloud overlap.
- **Hairline texture:** A field of 1 px diagonal white lines at about 8% opacity, spaced ~14 px at 45°, covers the upper-left quadrant and fades out toward the centre. It gives the text zone a subtle "graphic" layer that separates UI from painting.
- **Bar:** flat white with 1 px grey dividers, no shadow.

## 6. Components & patterns
- **Stat grid:** 2×2 label/value pairs, no cards.
- **Segmented budget bar** with three material states:
  - Income: a dark-grey hatched fill with 45° stripes.
  - Bills: mid-grey (#b0b0b0-ish) with vertical rules.
  - Expenses and remaining: white with vertical rules every ~19 px, a "tick ruler" feel.
- **Axis:** 1 px leader lines drop from each segment boundary to labels with a dot terminal. The last label "Whole Budget" is clipped by the bar's right edge.
- **Logo:** a green rounded-square glyph plus the wordmark at ~22 px semibold.

## 7. Motion
- **Measured:** 6.06 s at 30 fps; motion_fraction **0.0**, mean energy 0.17, no segments detected; first/last diff 6.98, so not a seamless loop.
- **What moves:** The only change is the red lamp toggling. It is lit at 0.34, 1.68, 3.03, 4.38 and 5.72 s, and dark at 1.01, 2.36, 3.70 and 5.05 s. That is an on/off cycle of about 1.35 s (estimate from frame spacing), which is too small in area to cross the energy threshold. Faint sparkle particles drift.
- **UI:** The UI is static (generated with Seedance per the post), so the flicker is a hard step rather than an eased fade.

## 8. Brand system
n/a — not a brand system. Identity cues:
- a green "ticket" logomark;
- a sky-blue world;
- the traffic-signal metaphor as a recurring brand device ("stop", "limit 40").

## 9. UX
- **Strengths:** The hero states the job in 5 words and shows real data immediately, and the bar visualises the proportion at a glance.
- **Problems:**
  - There is no CTA anywhere in the hero.
  - Numbers are inconsistent: "50,122.1 €" against "2,451,221.18 €", and the axis drops the euro sign and cents ("3,159,224").
  - Income should not be a segment of the expense budget, which is a semantic muddle.
  - The 12 px white captions on a photo are fragile.

## 10. Craft signals
- The 45° hairline texture is confined to the text quadrant and fades before the clouds.
- Three distinct fills (hatched, grey and ruled-white) distinguish bar segments without colour.
- Leader ticks drop from the exact segment boundaries at x 256, 351 and 503.
- The lamp blink is synchronised with the copy "stop", and red is the only saturated warm hue inside the page.
- The column x=256 is shared by logo, headline, labels and bar.

## 11. Reproduction recipe
```css
:root{--sky-1:#105db4;--sky-2:#0a76c8;--ink:#fff;--seg-hatch:#6b6b6b;--seg-mid:#b5b5b5;--rule:rgba(0,0,0,.18);--r-bar:12px;
  --font:"Inter Display","Geist",system-ui,sans-serif}
.hero{position:relative;background:url(sky.webp) center/cover;color:var(--ink);font-family:var(--font)}
.hero::before{content:"";position:absolute;inset:0 40% 50% 0;pointer-events:none;
  background:repeating-linear-gradient(135deg,rgba(255,255,255,.09) 0 1px,transparent 1px 14px);
  mask:radial-gradient(80% 100% at 0 0,#000 40%,transparent)}
h1{font:600 36px/1.1 var(--font);letter-spacing:-.01em}
.stat dd{font:400 30px/1.1 var(--font);font-variant-numeric:tabular-nums}
.bar{display:flex;height:95px;border-radius:var(--r-bar);overflow:hidden;background:#fff}
.bar .income{flex:18;background:repeating-linear-gradient(135deg,#555 0 1px,#8a8a8a 1px 9px)}
.bar .bills{flex:29;background:repeating-linear-gradient(90deg,var(--seg-mid) 0 18px,var(--rule) 18px 19px)}
.bar .rest{flex:53;background:repeating-linear-gradient(90deg,#fff 0 18px,var(--rule) 18px 19px)}
@keyframes lamp{0%,49%{opacity:1}50%,100%{opacity:.15}}
.lamp-red{animation:lamp 2.7s steps(1) infinite}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Lush painted sky and a restrained white UI. Strong colour story. |
| Originality | 8 | The traffic-light metaphor turns the illustration into the message. |
| Usability | 5 | No CTA, number formats are inconsistent, and small captions sit on the photo. |
| Craft | 6 | Nice bar textures and alignment, but the clipped "Whole Budget" label and number formatting are sloppy. |

# Colour systems

## Structure every palette as roles
```
canvas · surface-1 · surface-2 · surface-3          (elevation steps)
hairline (decorative) · border-control (≥3:1)
text-1 (≥12:1) · text-2 (≥7:1) · text-3 (≥4.5:1)
accent (fill) · accent-ink (text, ≥4.5:1) · on-accent (text on fill, ≥4.5:1) · accent-soft (tint)
success/warning/danger/info: fill + ink
```

**Measure, don't eyeball.** In the study, 90% of showcase pieces and 86% of brand documents shipped sub-AA text. The usual culprits:

| Culprit | Measured ratio | Fix |
|---|---|---|
| Grey meta text on white | #9a9a9a is 2.8:1 | Use ≤ #6b6b72, which is 5.3:1 |
| White on bright brand colours | 1.6–1.8:1 on light green, lilac or pink | Use dark ink on them |
| Grey on dark cards | #5c5c5c on #1c1c1c is 2.5:1 | Use ≥ #8b8b94 |
| Text over gradients or photos | swings 2.2–8.8:1 as the background moves | Put the text on a solid zone or a scrim |

Run `scripts/contrast.py`; it has a `--fix` mode that finds the nearest passing shade.

## Recipes

**One accent + tinted neutrals (default).**
- Replace #000 with a tinted near-black (e.g. #111113, #1c1917, #0b051d) and #fff with a paper (#f7f7f8 cool, #f6f3ee warm).
- Use the accent only for the primary action, the current selection and focus.

**Ink shades for text on colour.** Text on any coloured fill uses a dark ink of that fill's hue:
```css
.tag{background:var(--c);color:color-mix(in oklab,var(--c) 22%,#000)}   /* ≈5.5–8:1 on pastels */
```

**Category colour threading.** When there are categories (sources, agents, metrics, cities), give each one hue and reuse it on every layer: icon disc → value pill → progress segment → inline citation badge → legend dot. Keep one separate "selected" accent for interaction.

**Semantic colour is never colour-only.** Pair it with an icon (✓ ! ×), a word ("Failed", "+4.2%") or a shape. Deltas get both a sign and a colour.

**Dark mode is retuned, not inverted.**
- Surfaces step lighter as they rise: #0b0b0d → #141417 → #1c1c20 → #26262b.
- Accents shift lighter and less saturated. For example, #3d3dd6 on light becomes about #8a96ff on dark.
- Shadows mostly disappear; use a hairline plus an inset highlight instead.
- Body text uses #f5f5f7, not #fff.

**Colour from content.** Glass panels and scrims take their tint from what is behind them. Sample the image and darken it to reach contrast:
```css
.scrim{background:linear-gradient(to top,color-mix(in oklab,var(--img-dominant) 70%,#000) 0%,transparent 60%)}
```

**Gradients.**
- Lock the stop order and name the presets.
- Add 2–4% noise to large gradients to prevent banding:
  ```css
  background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='160' height='160'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='2' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='.06'/%3E%3C/svg%3E"),linear-gradient(…)
  ```
- Mesh and aurora gradients belong behind chrome, not behind paragraphs.

**Proportion.** State it, e.g. 60% neutral, 30% secondary, 10% accent. Brand systems that wrote proportions down were the most consistent.

## Contrast quick table (on #ffffff)

| Grey | Ratio | Use |
|---|---|---|
| #111113 | 18.9 | text-1 |
| #4a4a50 | 8.8 | text-2 |
| #6b6b72 | 5.3 | text-3 / meta |
| #8a8a93 | 3.4 | control borders, large text only |
| #a1a1aa | 2.6 | disabled fills, decorative only |

## Contrast quick table (on #0b0b0d)

| Grey | Ratio | Use |
|---|---|---|
| #f5f5f7 | 18.1 | text-1 |
| #a1a1aa | 7.7 | text-2 |
| #8b8b94 | 5.8 | text-3 |
| #6e6e78 | 3.9 | control borders |
| #3a3a40 | 1.7 | hairline-strong, decorative only |

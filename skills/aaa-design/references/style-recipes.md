# Style recipes

The rule throughout is **one structural base plus at most one expressive layer**. Each recipe gives its defining parameters, CSS, when to use it and how it fails. The studied scores (mean of 4 axes summed, max 40) are shown to calibrate how well each tends to land.

## Contents
- Bases: Neutral Swiss · Dark Premium · Editorial Warm · Hairline/Technical · Data-dense · Playful Soft
- Layers: Physical metaphor · Soft 3D/clay · Glass · Orb/shader/aurora · Pixel/dither/dot-matrix · Type-as-image · Maximalist meaningful colour
- Combination matrix

---

## Bases

### Neutral Swiss (studied mean 29.3, n=109)
- **Neo-grotesk type:** Inter, SF, Neue Montreal or Söhne-like. Weights 400/500 (600 for small labels only).
- **Hierarchy:** size and grey value, not weight.
- **Surfaces:** achromatic (#fff → #f7f7f8 → #f0f0f2). Hairlines at 6–10% ink, or none.
- **Accent and radii:** one accent; radii from {8, 14, pill}.
- **Fails when** nothing is allowed to be expressive. Three template products in the study differed only in brand colour and scored 22/40. Always add the signature moment.

### Dark Premium (29.9, n=79)
- **Canvas:** #0b0b0d.
- **Surface steps:** +6–8 L each. Hairline rgb(255 255 255/.08). No drop shadows; use `inset 0 1px 0 rgb(255 255 255/.06)`.
- **Saturation:** quarantined in one hero object. Secondary text no darker than #8b8b94 on #141417.
- **Recipe for a raised dark card:**
  ```css
  .card{background:linear-gradient(180deg,rgb(255 255 255/.03),transparent 40%),var(--surface-1);
    border:1px solid var(--hairline);border-radius:var(--radius-2);box-shadow:var(--highlight)}
  ```
- **Fails when** greys are chosen by eye. 2:1 bars and 2.5:1 labels were common in the studied dark UIs.

### Editorial Warm (30.4, n=36)
- **Type:** high-contrast serif display (Instrument Serif / Editorial New / Tiempos) at ≥ 4× body over a sans body, on paper #f6f3ee. Italic for one emphasised word.
- **Furniture:** mono caps for indexes and metadata; 0px images; generous margins (≥ 8vw).
- **Recipe:**
  ```css
  h1{font:400 var(--fs-hero)/.95 var(--font-display);letter-spacing:-0.035em}
  h1 em{font-style:italic;letter-spacing:-0.02em}
  ```
- **Fails when** serif is used for small UI text, or body text sits in long serif lines on screens.

### Hairline / Technical (29.8–30.5, n=64)
- **Lines and labels:** 1px lines at 10–20% ink, mono labels shaped "01 NAME STATE", dashed construction lines, crop marks, dimension call-outs ("236 × 292").
- **Emphasis:** exactly one dark "signal" line or value.
- **Recipe:**
  ```css
  .spec{font:500 12px/1 var(--font-mono);letter-spacing:.08em;text-transform:uppercase;color:var(--text-3)}
  .guide{background-image:linear-gradient(var(--hairline) 1px,transparent 1px),linear-gradient(90deg,var(--hairline) 1px,transparent 1px);background-size:48px 48px}
  ```
- **Fails when** the lines carry information (1.4:1 ticks).

### Data-dense (30.1, n=14)
- **Type split:** sans for names and values, mono caps for metadata (12–13px, +.08em), tabular figures throughout.
- **Colour per entity:** one hue per entity, threaded through badge → bar → inline citation → legend dot. One "selected" accent reserved for interaction.
- **Rows and alignment:** rows 40–48px, numbers right-aligned, deltas shown as both sign and colour.
- **Fails when** chart marks fall below 3:1 against their surface.

### Playful Soft (29.2, n=67)
- **Shape and type:** rounded sans (Plus Jakarta, Figtree, Nunito Sans); radii 12/24/32.
- **Colour:** candy fills with **dark** text; hue-tinted shadows.
- **Motion:** springy, with a small overshoot.
- **Fails when** white labels sit on pastel fills (1.4–1.8:1 measured).

## Expressive layers (pick one)

### Physical metaphor (highest studied: 30.7–30.9)
Borrow one real object, including its behaviour and the way it fails:
- receipt printing line by line;
- stamp that prints the chosen value;
- ticket with a perforated stub;
- folder with a frosted flap and peeking contents;
- card that tilts on a spring.

Rules:
- **The metaphor must do the job.** The confirmation *is* the data: the stamp shows the date, the receipt lists the items.
- **Shading:** use a darker shade of the object's own hue, not black. Paper is 0px radius against a rounded UI.
- **Real physics:**
  - a spring settles in ≤ 0.6s (k≈240, ζ≈7.5 gives about a 0.47s period);
  - gravity uses ease-in;
  - machines move linearly.

Recipe for a perforated ticket edge:
```css
.ticket{--r:8px;background:var(--surface-1);
  mask:radial-gradient(var(--r) at 0 50%,#0000 98%,#000) left/51% 100% no-repeat,
       radial-gradient(var(--r) at 100% 50%,#0000 98%,#000) right/51% 100% no-repeat}
.ticket hr{border:0;border-top:1.5px dashed var(--hairline)}
```
**Fails when** applied to every control, or when the metaphor hides the value.

### Soft 3D / clay (29.7, n=60)
- **Light and shadow:** key light from the top-left. `box-shadow: inset 0 2px 1px rgb(255 255 255/.6), inset 0 -6px 12px rgb(0 0 0/.08), 0 18px 40px -12px <hue at 35%>`.
- **Shape and colour:** radius 24–40; one hue per object.

### Glass (29.5, n=42)
```css
.glass{background:color-mix(in oklab,var(--surface-1) 55%,transparent);
  backdrop-filter:blur(24px) saturate(1.4);-webkit-backdrop-filter:blur(24px) saturate(1.4);
  border:1px solid rgb(255 255 255/.28);box-shadow:inset 0 1px 0 rgb(255 255 255/.45),0 12px 40px -12px rgb(0 0 0/.25)}
```
Rules:
- Use glass for chrome: nav, toolbars, popovers. Never for body copy.
- Tint it from the backdrop, and keep any chromatic fringe on the rim only.
- Test contrast against the brightest part of the backdrop.

### Orb / shader / aurora (≈29.3–30.3)
- **One luminous object** that signals state (thinking, listening, speaking), on a near-black or paper ground.
- **Grain:** add 2–6% grain to stop banding.
- **CSS-only orb:**
  ```css
  .orb{width:320px;aspect-ratio:1;border-radius:50%;
    background:radial-gradient(60% 60% at 35% 30%,#fff8 0,#fff0 40%),
               conic-gradient(from 210deg,#6d5efc,#b4a5ff,#ff8bd1,#6d5efc);
    filter:saturate(1.1);box-shadow:inset 0 0 0 1px #fff4,0 30px 120px -20px #8b7cff99;
    animation:breathe 6s var(--ease-in-out) infinite}
  @keyframes breathe{50%{transform:scale(1.035) rotate(8deg)}}
  ```
- **Fails when** it loops forever without meaning, or when text crosses its bright band.

### Pixel / dither / dot-matrix (30.0–30.5)
- **One grid cell (6–16px) shared by icons, loaders and readouts.** Unlit cells are visible at low contrast for the "off" state.
- **Depth:** dither scale encodes depth: a fine pattern on the hero, a coarse one in the background.
- **Readability:** text panels are solid, so text never sits on dither.
- **Dot-matrix readout:** `background: radial-gradient(circle,var(--text-1) 1.6px,transparent 1.8px) 0 0/6px 6px`, masked by the glyph.
- **Fails when** the grid misstates data. Use a 10×10 grid for percentages.

### Type-as-image (30.2)
- **Display type:** poster sizes (8–14vw) at line-height 0.85–0.95 and tracking −0.03 to −0.05em, in two colours at most.
- **Variants:** words can morph, mask or fill with the brand device.
- **Fails when** rotated or warped words carry essential information.

### Maximalist meaningful colour (28.6)
- **Many saturated hues are fine when each one maps to a category** (sport, city, agent, section).
- **Text on those fills is a dark ink of the same hue,** for example `color-mix(in oklab, var(--hue) 25%, #000)`.

## Combination matrix (✓ good, ~ careful, ✗ avoid)

| | Physical | Soft 3D | Glass | Orb/shader | Pixel | Type-as-image |
|---|---|---|---|---|---|---|
| Neutral Swiss | ✓ | ✓ | ~ (chrome only) | ✓ (one) | ✓ | ✓ |
| Dark Premium | ✓ | ~ | ✓ | ✓ | ✓ | ✓ |
| Editorial Warm | ✓ | ✗ | ✗ | ~ | ~ | ✓ |
| Hairline/Technical | ✓ | ✗ | ~ | ✓ | ✓ | ~ |
| Data-dense | ~ (confirmations) | ✗ | ✗ | ~ (status only) | ✓ | ✗ |
| Playful Soft | ✓ | ✓ | ~ | ~ | ~ | ✓ |

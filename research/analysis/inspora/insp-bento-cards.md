---
id: insp-bento-cards
source: inspora
category: Web
status: analyzed
title: "Bento cards."
creator: "@emblemo"
styles: [bento-grid, maximalist-color, flat-illustration, retro-pixel]
patterns: [services-bento, tinted-ink-per-card, ribbon-stroke-through-cards, checkerboard-transparency-motif, line-art-ui-spot-illustrations, stroke-draw-on-animation]
mode: light
palette: ["#ffffff", "#ff8860", "#fd97c6", "#feb52a", "#a498fe", "#af5964", "#2a1066"]
type_families: ["Familjen Grotesk / Archivo ExtraBold (likely)", "Inter (body, likely)"]
type_class: [grotesk, neo-grotesk]
radius_px: [28]
motion: {durations_s: [1.75], easing: [ease-out], loop: false}
scores: {aesthetics: 8, originality: 8, usability: 7, craft: 8}
craft_signals: [ink-colour-derived-from-card-hue, ribbon-continuity-across-gutters, checkerboard-as-photoshop-transparency-pun, uniform-20px-gutter, line-art-in-white-1-5px, brush-texture-on-ribbon-end]
anti_patterns: [white-ribbon-over-body-text, tall-card-mostly-empty]
---
# Bento cards. — @emblemo

## 1. Snapshot
- **Subject:** A 1518×1080, 5.2 s loop of a 4-card services bento:
  - Product UI & web (orange, tall)
  - Icons (pink)
  - Illustrations (yellow)
  - AI Design Setup (violet, wide)

  A single thick white ribbon draws itself through all four cards like a pen stroke.
- **Why it's remarkable:** The ribbon ties separate services into one continuous gesture. It loops into a Bézier "pen-tool" knot inside the Illustrations card, which links the cards narratively ("one designer, one hand").

## 2. Composition & layout
- **Grid:** ~720×905 px within the 1518 frame (x≈398–1120, y≈87–992), with a **20 px gutter**.
  - Row 1: a tall left card (~315×600) next to two stacked right cards (~385×290 each).
  - Row 2: a full-width card (~720×285).
- **Text:** Every card puts its title and 2–3 line description top-left with ~28 px inset. Illustrations sit bottom or right.
- **Ribbon path:** It enters from the Icons card's left edge (with a fading tail), crosses into Illustrations, knots, then sweeps down through the gutter into AI Design Setup in a ~440 px loop, rising back into the Product UI card. It crosses the gutters, so the white page shows through as continuous.

## 3. Typography
- **Titles:** a heavy grotesk with a tight, ink-trap-like "&", Familjen Grotesk or Archivo ExtraBold-like (800), ~24 px, tracking about −0.02 em.
- **Body:** ~15 px regular, about 1.4 leading, in a neo-grotesk (Inter-like).
- **Ink colour:** Both title and body are tinted per card, a deep shade of the card hue (maroon on orange, plum on pink, brown on yellow, indigo on violet), never black.
- **Labels:** The only other type is the "Aa" label in the AI card's token tile.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #ffffff | page, ribbon, line art | 62% |
| #a498fe | AI Design Setup card (violet) | 11% |
| #ff8860 | Product UI card (coral-orange) | 9% |
| #fd97c6 | Icons card (pink) | 6% |
| #feb52a | Illustrations card (amber) | 5% |
| #af5964 | checker squares / ink mid | 2% |
| ~#5c1414 / #3d0f2a / #5a2a00 / #2a1066 (est.) | per-card ink | text |

WCAG checks (per-card ink):
- Maroon on #ff8860: **5.71:1**
- Plum on #fd97c6: **8.01:1**
- Brown on #feb52a: **6.71:1**
- Indigo on #a498fe: **6.23:1**

All pass AA. However, where the white ribbon crosses text ("made", "pixel." in Illustrations; "AI", "library" in the AI card), white is 1.77:1 on amber and 2.47:1 on violet. The ribbon visibly cuts glyphs.

## 5. Depth & material
- **Overall:** Flat. There are no shadows. Depth comes from overlap order: the ribbon passes over text and over line art.
- **Ribbon:** Its end in the Illustrations card has a dry-brush texture (streaky white lines), a tactile counterpoint to the vector cleanliness. A soft white gradient tail fades in at the Icons card's left edge.
- **Checkerboards:** 2-tone pixel checkerboards (#af5964 on card colour) act as "transparent layer" swatches, a Photoshop/Figma transparency pun. They also echo pixelated image placeholders in the browser mock.

## 6. Components & patterns
- **Service card:** title, description and spot illustration, radius ~28 px.
- **Spot illustrations:** 1.5 px white line art for a browser window plus phone, an app-icon keyline grid with hand/smiley icons, a pen-tool Bézier with handles, and a Figma file plus "Aa" token tiles.
- **Placeholder pixel mosaics:** stand in for imagery (low-res thumbnails).

## 7. Motion
- **Measured:** 5.23 s at 30 fps, motion_fraction **0.0**, mean energy 0.03, no segments over threshold. The ribbon is a thin, high-contrast but small-area change.
- **Estimated from frames:**
  - The ribbon draws on from ~0.29 s (absent) to ~2.04 s (complete loop), about **1.75 s**.
  - It grows quickly at first: by 0.87 s it has already crossed Illustrations, which suggests an ease-out stroke-dashoffset animation.
  - From 2.04 s to 5.23 s the scene holds still.
- **Loop:** Not a seamless loop (first/last diff 2.8, because the ribbon is missing in frame 0).

## 8. Brand system
n/a — not a brand system. Identity cues (same creator as insp-5-3):
- confident 4-hue sherbet palette;
- per-card tinted ink;
- checkerboard and pixel motifs as a recurring "designer's tools" vocabulary.

## 9. UX
- **Strength:** As a services overview it is very scannable: four clear titles and short benefits.
- **Problems:**
  - No CTA or links per card.
  - The ribbon over body copy reduces legibility, so the path should route around text blocks.
  - The tall card has ~250 px of empty colour between text and art.

## 10. Craft signals
- Each card's ink is a ~75%-darkened shade of its fill, so all four pass AA while staying tonal.
- The gutter is exactly 20 px everywhere, and the ribbon passes through gutters without visual breaks.
- Line art uses a single 1.5 px white stroke weight across all four illustrations.
- The pen-tool Bézier handle (a line with two square endpoints) sits on the ribbon's knot, which itself becomes the path being edited.
- The checker squares are ~8 px, consistent across cards.

## 11. Reproduction recipe
```css
:root{--gap:20px;--r:28px;--orange:#ff8860;--pink:#fd97c6;--amber:#feb52a;--violet:#a498fe;
  --font-head:"Familjen Grotesk","Archivo",sans-serif;--font-body:"Inter",system-ui,sans-serif}
.bento{display:grid;grid-template-columns:315px 385px;grid-template-rows:290px 290px 285px;gap:var(--gap);position:relative}
.card{border-radius:var(--r);padding:28px;color:color-mix(in oklab,var(--c) 25%,#000)}
.card h3{font:800 24px/1.1 var(--font-head);letter-spacing:-.02em}
.card p{font:400 15px/1.4 var(--font-body)}
.ui{--c:var(--orange);background:var(--c);grid-row:1/3}.icons{--c:var(--pink);background:var(--c)}
.illu{--c:var(--amber);background:var(--c)}.ai{--c:var(--violet);background:var(--c);grid-column:1/3}
.checker{background:conic-gradient(#af5964 25%,transparent 0 50%,#af5964 0 75%,transparent 0) 0 0/16px 16px}
.ribbon{position:absolute;inset:0;pointer-events:none}
.ribbon path{fill:none;stroke:#fff;stroke-width:34;stroke-linecap:round;
  stroke-dasharray:var(--len);stroke-dashoffset:var(--len);animation:draw 1.75s cubic-bezier(.16,1,.3,1) .3s forwards}
@keyframes draw{to{stroke-dashoffset:0}}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Joyful, balanced palette with careful tinted ink. |
| Originality | 8 | A continuous ribbon threading a bento grid is a fresh way to unify cards. |
| Usability | 7 | Scannable, AA ink; the ribbon over text and missing CTAs cost points. |
| Craft | 8 | Consistent gutter, stroke weight and checker motif; text collisions are the only slip. |

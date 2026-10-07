---
id: insp-6-7
source: inspora
category: Illustration
status: analyzed
title: "3D Rolling transition"
creator: "@Designownow_"
styles: [skeuomorphic, physical-material, micro-interaction, soft-3d]
patterns: [rolling-drum-quantity-picker, ticket-strip-reveal, stepper-arrows, add-to-cart-pill, glowing-radio-swatch, odometer-number]
mode: light
palette: ["#e4e4e4", "#d8d7d5", "#c2bfbe", "#f3f3f2", "#f17329", "#3257e3", "#2a2a2a", "#9f948f"]
type_families: ["Google Sans / Product Sans (likely)", "handwritten numerals (marker script)"]
type_class: [geometric-sans, script]
radius_px: [9999, 16, 8]
motion: {durations_s: [0.27, 0.33, 0.23, 0.27, 0.23, 0.23], easing: [ease-out], loop: true}
scores: {aesthetics: 8, originality: 8, usability: 7, craft: 8}
craft_signals: [strip-extends-beyond-host-pill, drum-end-caps-orange-ribbed, handwritten-digits-on-paper-tiles, ease-out-fast-start-rolls, glow-ring-on-selected-swatch, strip-retracts-after-settle]
anti_patterns: [overflow-covers-adjacent-content, script-digits-less-legible]
---
# 3D Rolling transition — @Designownow_

## 1. Snapshot
- **Subject:** A 9.8 s, 1080×1080 loop of a product-quantity picker inside an "Add To Cart" pill. The value sits on a 3D drum with orange ribbed end caps. Pressing ▲/▼ rolls the drum, and a paper strip showing 1/2/3 briefly unfurls above and below the pill.
- **Why it's remarkable:** It replaces a flat number stepper with an odometer or ticket roll. The strip that pops out of the container shows the neighbouring values and the direction of travel, then tucks back in.

## 2. Composition & layout
- The frame is a cropped product page: a colour-option list (Cyber-Tech, Blue-Steel radio rows at ~38 px) above, "Order Today To Get It…" below, and the CTA pill in the middle running off the right edge.
- **CTA pill:** ~220 px tall, fully rounded, glossy white with a 2 px rim highlight.
- **Drum:** ~200×130 px at the left (x≈420–620).
- **Stepper:** ▲/▼ in a ~95×130 px rounded (~16 px) tile.
- **"Add To…" label:** ~56 px.
- **Number strip:** ~145 px wide, ~530 px tall when extended. It overlaps the option rows above and the delivery row below, with tiles (~100×75 px) at a ~140 px pitch.

## 3. Typography
- UI text is a geometric/humanist sans close to Google Sans or Product Sans: "Blue-Steel" in #2a2a2a at ~38 px Medium, "Cyber-Tech" at Regular in #4a4a4a, and "Add To" at ~56 px #4a4a4a.
- Quantity digits are **handwritten marker-style numerals** (~60 px) on paper tiles. This deliberate stationery contrast to the UI font implies tear-off tickets.
- A faint heading at the top is lorem ipsum in ~44 px.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #e4e4e4 | page background | 64% |
| #d8d7d5 / #c2bfbe | shadows / dividers / pill shading | 30% |
| #f3f3f2 | pill highlight, strip paper | 3% |
| #f17329 | drum end caps, accent square | <1% |
| #3257e3 | selected swatch (Blue-Steel) with glow | <1% |
| #2a2a2a | primary text and digits | — |
| #9f948f | warm-grey mid-shadow | 3% |

WCAG:
- #2a2a2a on #e4e4e4 is 11.29:1.
- #4a4a4a on #e4e4e4 is 6.97:1.
- Digits on paper (#2b2b2b on #f0f0f0) are 12.42:1.

Orange is reserved for the quantity mechanism and an urgency marker; blue appears only for the selected option.

## 5. Depth & material
- **Drum:** a white paper cylinder with shading toward the top and bottom edges (cylindrical gradient) and glossy orange ribbed caps that have metallic axles at each end.
- **Strip:** matte paper with fine grain and a soft drop shadow (~20 px blur). It reads as passing behind the pill's upper rim and in front of the lower area.
- **Pill:** glossy, with a bright 2 px top rim and a broad soft shadow underneath.
- **Swatches:** glassy beads. The selected one has an outer blue glow of ~8 px.

## 6. Components & patterns
- **Quantity selector:** a drum display, an explicit ▲/▼ stepper, and a transient value strip (a preview of neighbours).
- **Option radio list:** bead swatches. The selected item gets dark text and a glow; unselected items get grey text.
- **CTA with an embedded quantity**, which reduces form steps.
- The orange urgency square echoes the drum colour.

## 7. Motion
Measured: 60 fps, duration 9.82 s, motion_fraction 0.16, seamless_loop_likely true.

There are six segments, one per click:
- 1.40–1.67 s (0.27 s);
- 2.67–3.00 s (0.33 s);
- 4.37–4.60 s (0.23 s);
- 5.53–5.80 s (0.27 s);
- 6.93–7.17 s (0.23 s);
- 8.47–8.70 s (0.23 s).

The median is 0.25 s. Five are **ease-out with a fast start** (peak_at 0.05–0.19), so each roll snaps immediately and decelerates, like a ratchet. One is symmetric (6.93 s, peak 0.64).

From frames (estimate), the strip stays extended for about 0.8–1.0 s after a click and then retracts. The value sequence is 1 → 2 → 3 → 2 → 1 → 2 → 1, with about 1.1–1.5 s between clicks.

## 8. Brand system
n/a — not a brand system. Product names (Cyber-Tech, Blue-Steel) and the orange accent suggest a playful hardware or e-commerce identity.

## 9. UX
- **Strengths:** Direction is clear (the strip moves with the arrow), neighbouring values are previewed, and the ease-out gives immediate feedback.
- **Risks:**
  - The strip overlays adjacent rows (colour options, delivery info) for about 1 s.
  - Handwritten digits are slightly less legible than UI numerals.
  - The ▲/▼ tile targets (~95×65 px each half) are fine on desktop but tight on mobile.
  - There is no direct text input for large quantities.

## 10. Craft signals
- The paper strip extends past the pill boundaries and is clipped believably by the pill's rim.
- The drum has ribbed orange end caps plus metallic axles, with cylindrical shading on the label.
- Number tiles have a 1 px outline box and a constant ~140 px pitch along the strip.
- The roll easing is ease-out (peak 0.05–0.19 of 0.23–0.33 s), which gives a ratchet feel.
- The selected swatch glow matches its own hue (#3257e3).
- The orange accent is shared by the drum caps and the "order today" marker.

## 11. Reproduction recipe
```css
:root{--bg:#e4e4e4;--paper:#f3f3f2;--ink:#2a2a2a;--accent:#f17329;--sel:#3257e3}
.cta{border-radius:9999px;height:220px;background:linear-gradient(#f7f7f7,#e2e2e2);box-shadow:inset 0 2px 0 #fff,0 30px 50px -20px rgb(0 0 0/.2)}
.drum{width:200px;height:130px;perspective:400px;overflow:visible;position:relative}
.drum .cap{width:24px;background:repeating-linear-gradient(90deg,#ff8a3d 0 4px,#d9581a 4px 6px);border-radius:8px}
.strip{position:absolute;left:28px;width:145px;background:var(--paper);box-shadow:0 10px 20px rgb(0 0 0/.12);
  transform:translateY(calc(var(--v) * -140px));clip-path:inset(50% 0 50% 0);
  transition:transform .27s cubic-bezier(.1,.7,.2,1),clip-path .2s ease-out}
.drum.rolling .strip{clip-path:inset(-200px 0 -200px 0)}
.digit{font:400 60px/1 "Caveat Brush","Patrick Hand",cursive;color:var(--ink)}
.swatch[aria-checked=true]{box-shadow:0 0 0 2px #fff,0 0 12px 2px color-mix(in srgb,var(--sel) 60%,transparent)}
```
In JS, remove `.rolling` about 900 ms after the last click.

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Tactile drum, paper and glossy pill in a soft grey scene, with tight accent use. |
| Originality | 8 | An odometer drum plus an out-of-bounds value strip is a fresh take on the stepper. |
| Usability | 7 | Clear direction feedback and quick ease-out. The overlay briefly hides adjacent info. |
| Craft | 8 | Convincing clipping, consistent tile pitch and ratchet-like timing. |

---
id: insp-temperature-as-a-material
source: inspora
category: Product
status: analyzed
title: "Temperature as a material."
creator: "@0xSphere"
styles: [glassmorphism, physical-material, soft-3d]
patterns: [radial-dial-slider, glass-outline-numerals, glass-pill-cta, off-canvas-arc-control, tick-scale-with-major-marks, in-hand-device-mockup]
mode: dark
palette: ["#ececec", "#1f4666", "#255e80", "#2b7192", "#3b8aa5", "#6b8994", "#5bb8e0", "#0b0603"]
type_families: ["SF Pro Display (likely)", "custom rounded glass-outline numerals (SF Pro Rounded-based, likely)"]
type_class: [neo-grotesk, rounded-sans, display]
radius_px: [176, 9999]
motion: null
scores: {aesthetics: 9, originality: 8, usability: 6, craft: 8}
craft_signals: [hollow-glass-numerals-with-rim-light, dial-cropped-by-screen-edge, gradient-cools-to-warm-grey-at-bottom, glass-bead-thumb-with-specular, major-tick-every-tenth, cyan-current-value-tick]
anti_patterns: [white-on-glass-cta-low-contrast, tick-scale-unlabelled]
---
# Temperature as a material. — @0xSphere

## 1. Snapshot
- **Subject:** Two 2560×3200 slides of a single-screen AC/thermostat app ("Living Room, 24 °C"). Slide 1 is a flat phone render on #ececec. Slide 2 is the same screen in a hand-held, photographic device shot.
- **Why it's remarkable:** The temperature itself is drawn as material. The "24" is a hollow glass tube with a cyan rim, and the dial thumb is a glass bead. The whole screen is one vertical gradient from deep navy to steel grey, so the UI feels like a cold pane of frosted glass.

## 2. Composition & layout
- **Device and margins (slide 1):** The screen spans x≈664→1899 (≈1235 px wide, about 3.14× an iPhone 393 pt viewport) with a corner radius of about 176 px (≈56 pt, matching hardware). Margins on the light canvas are ≈26% left and right and ≈8% top and bottom.
- **Upper third, left-aligned:** a device glyph plus "Living Room" at about 72 px real cap height (~23 pt), then a giant "24" at about 296 px tall (~94 pt) with a superscript "°C" about a quarter of its height.
- **Middle:** deliberately empty gradient, roughly 35% of the screen height.
- **Lower half:** a ring dial whose centre sits off-screen to the bottom-right, so only a ~110° arc shows. The control becomes a horizon line sweeping from the right edge down to the bottom-left. Bottom-right holds a circular timer button (~52 pt) and a "Set Temperature" pill (~52 pt tall) aligned to a ~16 pt right margin.

## 3. Typography
- **UI text:** SF Pro Display at regular to medium weight. "Living Room" is tinted cyan (#5bb8e0-ish) instead of white, which keeps it in the material palette.
- **Numerals:** a rounded monoline outline (SF Pro Rounded skeleton) rendered as a glass tube with a highlight stroke. The form is defined by edge light alone, with no fill.
- **"°C":** semi-transparent white (#c9d3d8-like), so it sits back from the numerals.
- **Hierarchy:** about 4:1 from numerals to title, with only two text sizes plus the CTA label.

## 4. Colour
| Hex | Role | Share (slide 1) |
|---|---|---|
| #ececec | presentation canvas | 59% |
| #1f4666 | top of screen gradient, dial ring | 10% |
| #255e80 / #2b7192 | mid gradient | 15% |
| #3b8aa5 | lit centre of dial area | 7% |
| #6b8994 / #a2b3ba | warm-grey bottom of gradient | 6% |
| #5bb8e0 | accent: title, active tick, numeral rim | <1% |
| #0b0603 | hand / phone body (slide 2) | 18% (m1) |

WCAG checks:
- White CTA label on mid-gradient #2b7192 is 5.41:1, but at the actual pill position the background is about #8a9aa0, where it drops to **2.91:1 (fails)**.
- Cyan title #5bb8e0 on #1f4666 is 4.41:1, which passes only as large text (it is large).
- "°C" #c9d3d8 on #1f4666 is 6.49:1.
- Inactive ticks #4fb3e0 on #255e80 are 2.96:1, acceptable for non-text graphics at ≥3:1 only marginally.

## 5. Depth & material
- **Numerals:** an inner dark fill matching the background, a 2–3 px cyan rim on the lower-left edges and a white specular on the upper curves. This is the "glass tube" look.
- **Dial ring:** about 75 pt wide in #1f4666 with a 1 px cyan outer rim (a light-catch edge), sitting on a radial glow (#3b8aa5) centred inside the arc.
- **Thumb:** a glass sphere about 100 px across with a highlight stroke across it and a darker refracted rim, placed on the ring.
- **Buttons:** frosted glass pills with a 1 px light top-left border fading to transparent and a translucent grey fill. They follow Apple's "Liquid Glass" idiom.

## 6. Components & patterns
- **Arc dial slider with a tick scale:**
  - about 50 ticks; major ticks are longer and brighter at intervals of roughly 10 ticks;
  - the active setpoint tick is cyan;
  - the thumb sits at the current value.
- Glass numerals as the value readout.
- Circular icon button (timer) next to a primary glass pill.
- A device glyph (AC unit with air waves and snowflakes) identifies the room's appliance.

## 7. Motion
Stills, so no motion was observed. The description ("one gesture") and the off-canvas dial imply a single drag along the arc. Expect the thumb to track the finger and the numerals to tick with a spring, and the gradient warmth would plausibly shift with the value (blue cold, warmer when higher). This is not shown.

## 8. Brand system
n/a — not a brand system. Identity cues: a monochromatic cold-water blue, glass as the metaphor for temperature, and the hand-held hero shot (slide 2) as the marketing frame.

## 9. UX
- **Strengths:** There is one control and one number; the room name sets context; the giant dial is a large touch target in the thumb zone. The confirm step ("Set Temperature") prevents accidental changes.
- **Risks:**
  - The tick scale has no numeric labels or min/max, so you cannot predict where 26 °C sits.
  - The CTA contrast fails over the grey bottom.
  - The outline-only numerals lose legibility at a glance compared with a solid fill.
  - There is no current-versus-target distinction.

## 10. Craft signals
- The numerals are built from rim-light only (cyan lower edge, white upper specular) with no fill.
- The dial centre is placed off-screen bottom-right, so the arc reads as a horizon and frees the top half.
- The gradient travels from navy (#1f4666) to warm grey (#8a9aa0) at the bottom, implying condensation or fog rather than a flat blue.
- The active tick is in the accent cyan while all others are muted, and major ticks are thicker and lighter.
- The 1 px rim on the dial ring and glass pills uses the same cyan family as the numerals.
- Slide 2 reuses the exact UI in perspective with a real hand, so the material reads physically.

## 11. Reproduction recipe
```css
:root{--navy:#1f4666;--mid:#2b7192;--glow:#3b8aa5;--fog:#8a9aa0;--accent:#5bb8e0;--r-screen:56px}
.screen{border-radius:var(--r-screen);
  background:radial-gradient(70% 45% at 75% 72%,var(--glow) 0%,transparent 70%),
             linear-gradient(180deg,var(--navy) 0%,#255e80 35%,var(--mid) 60%,var(--fog) 100%)}
.temp{font:500 94px/1 "SF Pro Rounded",system-ui;color:transparent;
  -webkit-text-stroke:2px rgba(91,184,224,.9);
  text-shadow:0 -1px 0 rgba(255,255,255,.6),0 2px 8px rgba(91,184,224,.35)}
.room{font:500 23px/1.2 "SF Pro Display",system-ui;color:var(--accent)}
.dial{position:absolute;width:640px;aspect-ratio:1;right:-320px;bottom:-260px;border-radius:50%;
  border:75px solid var(--navy);box-shadow:0 0 0 1px var(--accent),inset 0 0 0 1px var(--accent)}
.glass-pill{border-radius:9999px;padding:14px 28px;color:#fff;
  background:rgba(255,255,255,.08);backdrop-filter:blur(20px) saturate(140%);
  border:1px solid rgba(255,255,255,.35);box-shadow:inset 0 1px 0 rgba(255,255,255,.4)}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 9 | A single hue family with glass rendering; restrained, atmospheric and coherent. |
| Originality | 8 | Glass-tube numerals and an off-canvas horizon dial are a fresh take on the thermostat trope. |
| Usability | 6 | Big, simple control, but an unlabelled scale and a weak-contrast CTA. |
| Craft | 8 | Consistent rim-light language across numerals, ring, thumb and pills. |

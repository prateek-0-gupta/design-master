---
id: insp-glowing-blue-orb
source: inspora
category: Motion
status: analyzed
title: "glowing blue orb"
creator: "@basit_designs"
styles: [dark-premium, neumorphism, aurora-glow, micro-interaction]
patterns: [pill-navbar, orb-as-logo-or-assistant, nested-pill-nav-items, ambient-idle-animation, cropped-hero-detail, grid-backdrop]
mode: dark
palette: ["#0c0c0c", "#171717", "#262627", "#424d5a", "#a8a8a8", "#5aa0ff"]
type_families: ["Inter (likely)"]
type_class: [neo-grotesk]
radius_px: [9999]
motion: {durations_s: [], easing: [linear], loop: true}
scores: {aesthetics: 8, originality: 6, usability: 6, craft: 8}
craft_signals: [only-chroma-is-the-orb, metallic-gradient-icons, inset-pill-items, top-edge-highlight-on-bar, soft-blue-bloom-radius, faint-grid-lines-backdrop]
anti_patterns: [cropped-labels-in-hero, orb-function-unclear]
---
# glowing blue orb — @basit_designs

## 1. Snapshot
- **Subject:** A 15 s, 2518×2160 close-up crop of a matte black pill navbar. A glossy blue "plasma" orb sits at the far left, followed by "Home" and a cut-off "Measure Adva…" item.
- **Why it's remarkable:** The whole frame is achromatic except for a 283 px sphere of swirling blue energy. The orb works as logo, AI-assistant trigger and light source all at once.

## 2. Composition & layout
- **Navbar:** a full-pill bar about 548 px tall that starts at x≈300 and bleeds off the right edge. Its vertical centre is at y≈1080, the exact frame middle.
- **Orb:** about 283 px diameter, with its centre about 280 px from the bar's left end. The inset to the bar edge (about 135 px) is about half the orb's diameter.
- **Nav items:** nested pills about 680×252 px with a ≈60 px gap. The orb-to-first-item gap is about 120 px.
- **Backdrop:** a grid of hairline lines on a ≈724 px pitch, giving a "design canvas" feel.
- **Crop:** the macro crop deliberately cuts the second label so the eye stays on the orb.

## 3. Typography
- Neo-grotesk (Inter-like), regular, at about 107 px real (the frame is a magnified UI crop, so this suggests a ≈16–18 px CSS label).
- Labels are #a8a8a8 with a subtle vertical metallic gradient: lighter at the top, darker at the bottom.
- Icons are 1.5–2 px-stroke rounded outlines (a house, a tray), carrying the same metallic gradient.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #171717 | page / bar surface | 81% |
| #0c0c0c | bar shadow, darkest areas | 8% |
| #262627 | grid squares lit by vignette, top rim | 10% |
| #424d5a | blue-tinted spill around orb | 2% |
| #5aa0ff (est., sampled visually) | orb core / bloom | <1% |
| #a8a8a8 | labels and icons | — |

WCAG checks:
- Label #a8a8a8 on #171717 is 7.54:1.
- Brighter top-of-gradient #d0d0d0 is 11.62:1.
- A dimmer #8a8a8a on the item pill (#1c1c1c) would still give 4.94:1, so the type holds AA.

## 5. Depth & material
- **Bar:** soft neumorphic. It has a 1–2 px lighter top edge (≈#2a2a2a), a large dark drop shadow below (about 80 px blur, pushing the lower grid to #0c0c0c) and no border.
- **Nav item pills:** recessed (inset), slightly darker than the bar, with a faint top inner highlight.
- **Orb:** a glass sphere with internal caustics. It has a bright specular highlight at about 1 o'clock, petal-like refraction lobes, and a cyan-blue outer bloom of about 30 px that spills light onto the bar surface.

## 6. Components & patterns
- A pill navigation bar with a brand/assistant orb at the start, and items as icon-plus-label nested pills.
- This is the "AI orb" idiom (cf. Siri or Copilot orbs) placed where a logo normally lives.
- No active-state styling is visible on any item. Both look equal.

## 7. Motion
Measured: 60 fps, 15.0 s, `motion_fraction` **0.00**, with no segments above threshold. `seamless_loop_likely` is true (`first_last_diff` 0.54).

All the motion is confined to the orb's interior: the caustic lobes rotate and swirl, and the bloom pulses. Comparing frames at 0.83, 4.17, 9.17 and 12.5 s shows the highlight pattern rearranging while the orb's position and size stay fixed. This is a continuous, linear-feeling idle loop with no easing events. The pulse period is not resolvable from 9 frames (estimate: several seconds).

## 8. Brand system
n/a — not a brand system. The orb functions as the identity mark, and the rest is a neutral UI chassis.

## 9. UX
- **Strengths:**
  - The orb is a strong focal point.
  - Labels have good contrast.
  - Generous touch targets (≈252 px real, i.e. ≈44 px CSS-scale items).
- **Risks:**
  - The orb's purpose (home? assistant? status?) is not communicated.
  - A perpetually animating element in the nav competes with content and needs a `prefers-reduced-motion` fallback.
  - There is no visible active-item state.

## 10. Craft signals
- The palette is strictly greyscale except the orb, and the blue spill is visible on the bar (#424d5a).
- Icons and labels share one top-to-bottom metallic gradient.
- Nav items are inset pills inside an outset pill bar, reusing one shape at two depths.
- The orb's inset from the bar end (≈135 px) is about half its diameter, which reads as optically centred in the bar cap.
- The bar has a 1–2 px top highlight and a long soft shadow below, so light comes from one consistent direction.
- The hairline grid backdrop sits on a ≈724 px pitch.

## 11. Reproduction recipe
```css
:root{--bg:#171717;--bar:#151515;--item:#121212;--rim:#2a2a2a;--ink:#a8a8a8;--glow:#5aa0ff}
body{background:var(--bg);background-image:linear-gradient(#0f0f0f 1px,transparent 1px),linear-gradient(90deg,#0f0f0f 1px,transparent 1px);background-size:290px 290px}
.nav{display:flex;align-items:center;gap:24px;padding:12px 16px 12px 14px;border-radius:9999px;background:var(--bar);
  box-shadow:inset 0 1px 0 var(--rim),0 30px 60px -10px rgb(0 0 0/.7)}
.nav a{display:flex;gap:10px;align-items:center;padding:14px 22px;border-radius:9999px;background:var(--item);
  box-shadow:inset 0 1px 0 rgb(255 255 255/.04);font:400 17px/1 Inter,sans-serif;
  background-clip:padding-box;color:transparent;-webkit-background-clip:text;background-image:linear-gradient(#d0d0d0,#8a8a8a)}
.orb{width:48px;height:48px;border-radius:50%;
  background:radial-gradient(circle at 65% 25%,#fff 0 6%,transparent 12%),conic-gradient(from var(--a),#1e4fd8,#7ec8ff,#2a5cff,#9fdcff,#1e4fd8);
  box-shadow:0 0 18px 2px color-mix(in srgb,var(--glow) 60%,transparent),inset 0 0 12px rgb(255 255 255/.4);animation:swirl 6s linear infinite}
@property --a{syntax:"<angle>";inherits:false;initial-value:0deg}
@keyframes swirl{to{--a:360deg}}
@media (prefers-reduced-motion:reduce){.orb{animation:none}}
```
(The clip-text gradient needs to sit on the label span, not the pill. It is shown inline here for brevity.)

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Restrained matte black with a single jewel-like light source. |
| Originality | 6 | The AI orb in a pill nav is a known trend. It is executed well but not new. |
| Usability | 6 | Labels are legible, but the orb's role and the active state are undefined. |
| Craft | 8 | Consistent light direction, metallic icon/text gradient and nested pill depth. |

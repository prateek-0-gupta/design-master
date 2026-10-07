---
id: insp-3d-gradient-cards
source: inspora
category: Motion
status: analyzed
title: "3D gradient cards"
creator: "@basit_designs"
styles: [gradient-mesh, maximalist-color, cinematic-3d, kinetic-type]
patterns: [3d-card-carousel, edge-warp-distortion, stat-hero-card, mirrored-backface-cards, radial-tick-gauge, range-slider-readout, floor-ceiling-glow-reflections]
mode: light
palette: ["#f0f0f0", "#d4775d", "#a4ad45", "#2a5a1a", "#52398c", "#9346a1", "#20000e", "#0b2a6a"]
type_families: ["Neue Haas / Helvetica Now Display (likely)"]
type_class: [neo-grotesk]
radius_px: [43]
motion: {durations_s: [1.53, 1.5, 1.6, 1.43], easing: [ease-out], loop: true}
scores: {aesthetics: 8, originality: 8, usability: 5, craft: 7}
craft_signals: [one-hero-number-per-card, gradient-centre-darkens-behind-number, consistent-card-template, edge-stretch-chromatic-smear, cyan-glow-mirrors-blue-card, 3-6s-rhythm]
anti_patterns: [white-caption-on-yellow-1-5-to-1, mirrored-text-on-side-cards, product-names-as-content]
---
# 3D gradient cards — @basit_designs

## 1. Snapshot
- **Subject:** A 14.58 s, 2700×2160, 60 fps loop of a horizontal 3D card carousel on a pale grey stage. Four feature cards rotate through centre, each a full-bleed mesh gradient with one hero stat:
  - "95th" (green/yellow/coral, model access);
  - "25%" (deep blue, AI vs human tone slider);
  - "720" (crimson, image credits);
  - "2.0" (violet, video engine).
- **Why it's remarkable:** The side cards do not just recede. They **stretch and smear toward the frame edges** like taffy or lensing, with chromatic fringes. The carousel feels like a physical warp field, not a CSS 3D ring.

## 2. Composition & layout
- **Centre card:** about 958×1200 px (≈0.8 ratio, 4:5) with radius ≈43 px, centred, about 35% of frame width.
- **Side cards:** shown from behind (mirrored text) at about 640 px wide visible. Their outer halves flare into a funnel that grows from ~800 px to ~1250 px tall at the frame edge, with cyan/magenta rims.
- **Glows:** elliptical glows (pink or cyan, matching the incoming card) sit at the top and bottom edges like floor and ceiling reflections, about 800×100 px.
- **Card template:**
  - title top-left, two lines, ~40 px, at a ~64 px inset;
  - hero number centred (~255 px cap height) with a superscript unit ("th", "%");
  - an instrument element around or below it (radial tick ring, slider, waveform ticks);
  - footer caption bottom-left (~40 px).

## 3. Typography
- A neo-grotesk, consistent with Helvetica Now Display or Neue Haas. The hero numerals are Light/Regular (~300–400) at about 340 px font size with tight tracking. The superscript units are about 40% size and top-aligned.
- Titles and captions are Regular at ~40 px in white or ~80% white, in sentence case.
- Numerals take a tint from the card (pale green on the green card, cyan on the blue, pink-red on the crimson), gradient-filled rather than flat white.

## 4. Colour
| Hex | Role | Share (key) |
|---|---|---|
| #f0f0f0 | stage | 59% |
| #d4775d / #a4ad45 / #2a5a1a | "95th" card: coral rim → yellow → green → deep green core | ~10% |
| #52398c / #9346a1 / #4c0a56 | violet "2.0" card | ~10% |
| #20000e / #320138 | crimson-black "720" card | ~9% |
| #0b2a6a (est.) | navy "25%" card | — |
| cyan #44d4ff (est.) | glow reflections, slider accents | — |

Each card's gradient darkens toward the centre (vignette inverted), so the white-ish numeral always sits on the darkest zone.

Contrast checks:
- The "95" (#dfe6c0) on the green core (#2a5a1a) is 6.3:1, and white on navy is 13.52:1. The hero numbers are fine.
- The captions do not fare well. White "Access to advanced intelligence" over the yellow zone (#e9d45a) is **1.5:1**, and over coral (#d4775d) it is 3.18:1.

## 5. Depth & material
- **Gradients:** mesh-like, with soft radial blobs and no visible banding. A thin light rim on the card edge is suggested by a brighter edge colour.
- **Warp:** the side cards' far halves are dragged outward with motion-blur streaks and RGB-split fringes (cyan outer edge, magenta inner), reading as a lens or warp effect rather than perspective.
- **No drop shadows:** depth comes from foreshortening, warp and the floor/ceiling glows.

## 6. Components & patterns
- Feature or stat cards (pricing or marketing for an AI product).
- **Data widgets inside the cards:**
  - radial tick gauge (~60 ticks, card 1);
  - AI ↔ Human range slider with a white thumb (card 2);
  - +/– stepper and waveform ruler (card 3);
  - version badge (card 4).
- Carousel with backface-visible neighbours.

## 7. Motion
Measured values (`m0_motion.json`):
- Four transition segments, each an ease-out with peak_at 0.16–0.17:
  - 1.03–2.57 s (1.53 s);
  - 4.67–6.17 s (1.50 s);
  - 8.33–9.93 s (1.60 s);
  - 12.00–13.43 s (1.43 s).
- The median is 1.52 s. Holds of about 2.1 s sit between them, giving a period of about **3.65 s** per card. Four cards make one 14.6 s loop.
- `seamless_loop_likely` is true (first/last diff 0.88). Motion fraction is 0.42.

From the frames (estimate):
- At 5.67 s the cards are edge-on (≈85–90° rotation), with the stage almost empty mid-flip. The rotation is a full card flip, not a slide.
- The fast-start ease-out (≈ cubic-bezier(.16,1,.3,1)) makes each flip snap, then settle over the last ~1 s.
- The glows at top and bottom swap colour (pink ↔ cyan) with the active card.

## 8. Brand system
n/a — this is not a brand system. It lists third-party model names on the cards; the look is generic AI-SaaS marketing.

## 9. UX
- **Strengths:** One number per card gives instant scanability, and the consistent template means the user learns where to look.
- **Risks:**
  - Mirrored text on the side cards is unreadable noise.
  - Captions over light gradient zones fail contrast.
  - An auto-rotating carousel at a 3.65 s period is too fast to read a 2-line title plus caption; it needs pause on hover and manual controls.
  - A reduced-motion alternative (static grid) is needed.

## 10. Craft signals
- The darkest gradient zone sits behind the hero number on every card, with luminance designed around the content.
- The superscript unit is ~40% of the numeral size and aligned to cap height.
- The edge warp adds RGB-split fringes only at the stretched extremities.
- The top and bottom glow colour tracks the active card's palette.
- Transitions all share the same ease-out profile (peak 0.16–0.17) and ~1.5 s length.

## 11. Reproduction recipe
```css
:root{--stage:#f0f0f0;--r-card:43px;--flip:1.5s;--ease-snap:cubic-bezier(.16,1,.3,1)}
.stage{perspective:1600px;background:var(--stage)}
.card{width:min(42vw,480px);aspect-ratio:4/5;border-radius:var(--r-card);color:#fff;padding:32px;position:absolute;
  transition:transform var(--flip) var(--ease-snap);backface-visibility:visible;
  font:400 20px/1.25 "Helvetica Now Display","Inter",system-ui}
.card--model{background:radial-gradient(55% 50% at 50% 52%,#1d4612 0%,#4f8a22 35%,#a4ad45 55%,#e9d45a 70%,#d4775d 90%,#f06aa0 100%)}
.card--tone{background:radial-gradient(60% 55% at 50% 50%,#071a46,#0b2a6a 40%,#1860ff 75%,#8fd8ff)}
.hero{font-weight:300;font-size:170px;letter-spacing:-.04em;line-height:.9;
  background:linear-gradient(#f3f6df,#9fc07a);-webkit-background-clip:text;color:transparent}
.hero sup{font-size:.4em;vertical-align:top}
.card.is-left{transform:translateX(-95%) rotateY(-155deg)}
.card.is-right{transform:translateX(95%) rotateY(155deg)}
/* the edge "taffy" warp needs WebGL: displace vertices by smoothstep(0.5,1.0,|x|)*k along x, add RGB-split in the fragment shader */
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Vivid, polished gradients; a memorable warp; a clean card template. |
| Originality | 8 | The edge-stretch carousel is a fresh take on the 3D card ring. |
| Usability | 5 | Fast auto-rotation, mirrored side text, failing caption contrast. |
| Craft | 7 | Strong consistency and easing; the caption-on-gradient placement is careless. |

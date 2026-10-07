---
id: insp-artistic-fintech
source: inspora
category: Product
status: analyzed
title: "Artistic fintech UI"
creator: "@MoizArshi29"
styles: [photo-led, glassmorphism, x-painterly]
patterns: [full-bleed-artwork-onboarding, concentric-lens-refraction, frosted-copy-plate, single-pill-cta, sunburst-logomark]
mode: dark
palette: ["#a7aa8e", "#1f2725", "#414c3d", "#323f38", "#787369", "#5c6956", "#cbcec3", "#ffffff"]
type_families: ["Inter (likely)"]
type_class: [neo-grotesk]
radius_px: [48, 28, 9999]
motion: {durations_s: [24.15], easing: [linear], loop: true}
scores: {aesthetics: 8, originality: 8, usability: 5, craft: 7}
craft_signals: [refraction-rings-sample-the-painting, copy-plate-sits-on-darkest-zone, single-white-cta-only-light-surface, inline-logomark-as-spinner]
anti_patterns: [no-headline-or-brand-name, tiny-body-copy-on-busy-art, phone-too-small-in-frame]
---
# Artistic fintech UI — @MoizArshi29

## 1. Snapshot
- **Subject:** A 24.1 s, 3136×2080 recording of one phone onboarding screen. A full-bleed impressionist oil landscape (sky, dark tree, sunlit meadow) is distorted by three concentric glass-lens rings. A white sunburst mark, a three-line value proposition on a frosted plate, and a white "Get Started" pill sit at the bottom.
- **Why it's remarkable:** It treats a finance app's first screen like a gallery wall. The "glass" effect is a refractive lens that warps the painting's brushwork, not a blur, so the painterly texture survives inside the UI.

## 2. Composition & layout
- The phone is about 615×1320 px at native size (≈385×840 in the 2000 px key frame), centred on white, occupying only about 20% of the canvas width.
- **Inside the phone:** the rings are centred at roughly 50% x and 68% y, with radii of about 0.55, 0.75 and 0.95 of the phone width, stacked up and to the right. They read as ripples or a stacked set of coins.
- **Bottom third:** the logomark at y≈66% of phone height; the copy plate (about 340×190 px in the key frame, radius ≈28 px) at 66–88%; the CTA at 91–97% with a 22 px side inset.
- The screen has no top content at all: the upper 45% is pure painting. That is a strong poster crop.

## 3. Typography
- Neo-grotesk close to Inter, Regular 400.
- **Body:** three centred lines at about 16 px (in key-frame scale), leading about 1.45, white.
- **CTA:** "Get Started" at about 16 px Medium 500, near-black.
- There is no headline or wordmark, so the type is only two sizes and the painting carries the hierarchy.

## 4. Colour
| Hex | Role | Approx share (phone only) |
|---|---|---|
| #a7aa8e / #cbcec3 | sage sky, pale ring highlights | ~30% |
| #1f2725 / #323f38 | darkest tree mass, plate backing | ~25% |
| #414c3d / #5c6956 | mid foliage greens | ~25% |
| #787369 | mauve hills | ~8% |
| #ffffff | CTA, logomark, body copy, page | — |

WCAG checks (contrast.py):
- White copy on the darkest tree zone #414c3d: **9.03:1**. On mid-green #5c6956: **5.82:1**. On mauve #787369: **4.71:1**.
- The plate sits mostly over dark foliage, so it holds, but any copy over the sage sky (#a7aa8e) would be **2.39:1**.
- CTA #111 on white: **18.88:1**.

Strategy: an earthy, desaturated palette taken from the artwork. White is the only UI colour.

## 5. Depth & material
- **Lens rings:** each ring has a bright upper rim (a 2–3 px highlight), a dark lower shadow edge, and ripple-like distortion of the brush strokes inside. This simulates thick glass discs stacked over the canvas.
- **Copy plate:** a low-opacity white fill (about 8–10%) with backdrop blur and no border. It reads as a faint frosted card.
- **Logomark:** sits on a circular dark-glass well about 70 px wide, which is a fourth, smallest ring.
- There are no drop shadows. Depth comes only from refraction.

## 6. Components & patterns
- A full-bleed artwork hero as the onboarding background.
- A sunburst / asterisk logomark with 10 tapered rays.
- A frosted copy plate.
- A full-width white pill CTA (about 340×52 px in the key frame).
- There are no pagination dots, sign-in link or skip, so this is a single-screen splash.

## 7. Motion
- Measured: 24.15 s at 60 fps. `motion_fraction` is **0.0** and there are no segments. Mean energy is 0.15 and p95 is 0.18, so motion is low, continuous and steady. `first_last_diff` is 0.1 and `seamless_loop_likely` is true.
- **From frames (estimates):** the ring edges shift position subtly between frames (e.g. the top ring rim moves about 10–20 px between 1.34 s and 4.02 s), which suggests a slow, linear lens drift or breathing over the painting.
- The CTA and copy are static. The motion is ambient, not feedback.

## 8. Brand system
n/a — not a brand system. Identity cues: the sunburst mark, the fine-art (impressionist landscape) image direction, and the earthy green palette as a counterpoint to typical neon fintech.

## 9. UX
- A clear single action. Low cognitive load.
- **Risks:**
  - No product name or headline, so the user cannot tell what the app is.
  - The body copy is small for its importance.
  - Legibility depends on the copy landing over dark foliage. A different painting or crop could break contrast.
  - The animated refraction behind text may hurt readability for some users; it needs a reduced-motion fallback.

## 10. Craft signals
- The refraction distorts actual brushwork, not a flat blur, so texture reads inside the rings.
- The copy plate is placed over the darkest region of the painting (the tree), giving 5.8–9:1 without a heavy scrim.
- The CTA is the only fully opaque light surface on screen, so it is unambiguous.
- The logomark well echoes the ring geometry (concentric with the lens set).

## 11. Reproduction recipe
```css
:root{--ink:#111;--paper:#fff;--sage:#a7aa8e;--forest:#1f2725;--moss:#414c3d;--r-device:48px;--r-plate:28px}
.screen{position:relative;border-radius:var(--r-device);overflow:hidden;background:url(painting.jpg) center/cover}
.lens{position:absolute;border-radius:50%;aspect-ratio:1;
  backdrop-filter:url(#ripple) brightness(1.05);
  box-shadow:inset 0 3px 2px #ffffff88,inset 0 -6px 12px #0000004d;}
.plate{margin:0 16px;padding:24px 20px;border-radius:var(--r-plate);
  background:#ffffff14;backdrop-filter:blur(12px);color:#fff;text-align:center;font:400 15px/1.45 Inter,sans-serif}
.cta{margin:16px;height:52px;border-radius:9999px;background:#fff;color:var(--ink);font:500 15px Inter}
@keyframes drift{50%{transform:translate(-6px,4px) scale(1.01)}}
.lens{animation:drift 12s linear infinite}
@media (prefers-reduced-motion:reduce){.lens{animation:none}}
```
```html
<svg width="0" height="0"><filter id="ripple"><feTurbulence type="fractalNoise" baseFrequency=".012 .08" numOctaves="2"/><feDisplacementMap in="SourceGraphic" scale="18"/></filter></svg>
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Rich and unusual; the painting and glass lenses feel premium and calm. |
| Originality | 8 | Fine-art refraction for fintech onboarding is uncommon. |
| Usability | 5 | One clear CTA, but no headline or brand, and legibility is image-dependent. |
| Craft | 7 | Convincing lens rims and smart copy placement; the device is tiny in the frame. |

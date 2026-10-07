---
id: insp-tiny-animated-svg
source: inspora
category: Motion
status: analyzed
title: "Tiny animated SVG"
creator: "Mike Bespalov"
styles: [editorial-serif, aurora-glow, minimal-swiss, micro-interaction]
patterns: [upgrade-celebration-modal, iridescent-wordmark-loop, svg-filter-animation, scrim-over-app, single-cta-dismiss]
mode: light
palette: ["#ffffff", "#000000", "#6d7083", "#252948", "#d23f60", "#45506a", "#fbeff5"]
type_families: ["Tiempos / GT Super-style text serif (likely)", "Inter Display (likely)"]
type_class: [editorial-serif, neo-grotesk]
radius_px: [24, 10]
motion: {durations_s: [2.5, 2.77, 2.5, 0.37, 0.43, 0.9], easing: [linear, ease-out, ease-in], loop: true}
scores: {aesthetics: 9, originality: 8, usability: 8, craft: 9}
craft_signals: [3kb-svg-budget, thermal-gradient-ink, letters-dissolve-at-different-phases, art-bleeds-off-modal-edges, tight-serif-tracking, cta-full-width-of-text-column]
anti_patterns: [scrim-hides-context-heavily]
---
# Tiny animated SVG — Mike Bespalov

## 1. Snapshot
- **Subject:** A 17.1 s, 1840×1200 capture of Refero's post-checkout "You're Pro. No more walls." modal. Its header is a looping, liquid, thermal-iridescent "PRO" wordmark built as a ~3 KB animated SVG.
- **Why it's remarkable:** Celebration usually means confetti or a Lottie file. Here a few KB of SVG filters give a heat-map fluid wordmark whose letters dissolve and re-form independently, so it never looks like a loop.

## 2. Composition & layout
- **Modal:** 778×972 px (x 528→1306, y 96→1068 in the 1840 px frame), centred over a blue-grey scrim.
- **Art zone:** the top ~400 px. The "PRO" letters are ~340 px tall and bleed off the left and right modal edges, cropped by the card's radius.
- **Text block:**
  - a two-line serif headline centred at y≈555–720;
  - a two-line grey subcopy at y≈750–830;
  - a full-width black CTA, 655×108 px, inset 62 px each side, at y≈900.
- **Bottom padding:** ~62 px, matching the side inset. That gives a single 62 px margin unit.

## 3. Typography
- **Headline:** a sharp text serif with tight tracking (~−0.03 em) and a small x-height contrast, close to Tiempos Headline or GT Super Text. Two lines at ~76 px with leading ~1.1. The full stops are deliberate.
- **Subcopy:** a neo-grotesk (Inter Display-like) at ~28 px, grey, with tight tracking (~−0.02 em), centred, leading ~1.6.
- **CTA:** "Keep researching", ~30 px medium, white.
- **Pairing:** an editorial serif for emotion and a grotesk for information. The background page echoes the serif in its "…for the AI Era" heading.

## 4. Colour
| Hex | Role | Approx share |
|---|---|---|
| #6d7083 | scrim over app (dimmed page) | 63% |
| #ffffff | modal surface | 23% |
| #000000 | CTA, headline | 3% |
| #252948 / #45506a | deep navy core of letters | 3% |
| #d23f60 / #fbeff5 | hot red to pink fringe | 3% |
| cyan to orange (unsampled) | thermal gradient mid-band | — |

WCAG checks:
- Headline #111 on white: 18.88:1.
- Subcopy ≈#6b6e7a on white: 5.08:1 (pass).
- CTA white on black: 21:1.
- Dimmed page text #252948 under the scrim on #6d7083: 2.88:1, which is intentional de-emphasis.

## 5. Depth & material
- **Flat white card:** ~24 px radius, no visible shadow. It is separated by a heavy (~55%) cool scrim.
- **Letters:** All depth lives in the letters. They are shaded like a thermal camera image (navy core, then cyan, yellow, orange, red, magenta, then white), with a fine grain or noise texture at the edges (visible in the key frame). The result reads as glowing liquid metal or heat.

## 6. Components & patterns
- **Celebration modal:** art, headline, subcopy and one CTA. A non-blocking close is implied by "Keep researching" returning to the product.
- **Wordmark animation:** each letter independently melts into a blob, evaporates into pink haze, then re-forms (at 4.76 s P is half gone; at 8.57 s "PR" is almost absent while O is solid).
- **Background:** the app stays visible under the scrim, so the user knows where they will return.

## 7. Motion
Measured profile: 17.13 s at 60 fps, `motion_fraction` 0.54, 10 segments. Not flagged as a seamless loop (first-to-last difference 5.28); the SVG itself loops, but the capture is cut mid-cycle.
- **Long continuous segments:** 3.13–5.63 s (2.50 s), 7.43–10.20 s (2.77 s) and 11.93–14.43 s (2.50 s), all `continuous/linear`. These are the fluid morph passes: a slow, steady roughly 2.5 s melt cycle per pass.
- **Short accents in between:** 0.80 s (0.37 s, ease-in), 1.27 s (0.43 s, ease-out), 5.73 s (0.27 s, ease-out) and 16.2 s (0.9 s, ease-out). These are probably letters snapping back into shape.
- **Low energy:** mean energy is 0.36, so the motion is soft and ambient rather than bursty.
- **Cadence:** a reform roughly every 4.3–4.5 s (5.63 → 10.2 → 14.43), as an estimate from segment ends.

## 8. Brand system
n/a — not a brand system. Identity cues:
- Refero's editorial serif headline voice ("No more walls.");
- a black, white and serif base with one burst of spectral colour reserved for the reward moment.

## 9. UX
- **Strengths:**
  - A clear success state.
  - Benefit-led copy.
  - A single obvious action.
  - Tiny file size means no payload cost at checkout.
- **Risks:**
  - The animated letters are partially illegible at times (8.57 s shows "PRO" as "· ·O"), which is acceptable because the headline repeats the meaning.
  - Should honour `prefers-reduced-motion` with a static frame.

## 10. Craft signals
- The asset budget is ~3 KB of SVG, not video or Lottie.
- Each letter dissolves on its own phase, so there is no visible loop seam.
- A grain or noise texture appears at the gradient edges (feTurbulence-like).
- The artwork bleeds off and is clipped by the modal radius, so the frame feels larger than the card.
- A single 62 px inset governs the CTA sides and the bottom padding.
- Colour is used only in the celebration art; the UI chrome is pure black and white.

## 11. Reproduction recipe
```html
<svg viewBox="0 0 400 160" width="100%" aria-label="Pro">
  <filter id="melt"><feTurbulence type="fractalNoise" baseFrequency=".012" numOctaves="2" seed="3">
      <animate attributeName="baseFrequency" dur="9s" values=".012;.03;.012" repeatCount="indefinite"/></feTurbulence>
    <feDisplacementMap in="SourceGraphic" scale="38"/><feGaussianBlur stdDeviation="4"/></filter>
  <linearGradient id="heat" x1="0" x2="1"><stop offset="0" stop-color="#252948"/><stop offset=".3" stop-color="#2bb3ff"/>
    <stop offset=".55" stop-color="#ffd23f"/><stop offset=".75" stop-color="#d23f60"/><stop offset="1" stop-color="#fbeff5"/></linearGradient>
  <text x="0" y="140" font-family="Inter, sans-serif" font-weight="900" font-size="170" fill="url(#heat)" filter="url(#melt)">PRO</text>
</svg>
```
```css
.modal{width:390px;border-radius:24px;background:#fff;padding:0 31px 31px;overflow:hidden;text-align:center}
.modal h2{font:400 38px/1.1 "Tiempos Headline",Georgia,serif;letter-spacing:-.03em}
.modal p{font:400 14px/1.6 "Inter Display",Inter,sans-serif;color:#6b6e7a;letter-spacing:-.02em}
.modal .cta{width:100%;height:54px;border-radius:10px;background:#000;color:#fff}
.scrim{background:rgba(48,52,80,.55)}
@media (prefers-reduced-motion:reduce){svg animate{display:none}}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 9 | The spectral liquid wordmark set against a severe black-and-white serif modal is striking and restrained. |
| Originality | 8 | Thermal-fluid type as an upgrade reward is fresh, and the 3 KB constraint is notable. |
| Usability | 8 | A clear success state and single action. The art is momentarily illegible but redundant. |
| Craft | 9 | One margin unit, clipped bleed and per-letter phase offsets. |

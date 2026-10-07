---
id: insp-fluid-liquid-card-carousel
source: inspora
category: Motion
status: analyzed
title: "Fluid liquid card carousel."
creator: "Marcelo Design X"
styles: [photo-led, maximalist-color, cinematic-3d, micro-interaction]
patterns: [coverflow-carousel, edge-stretched-side-cards, mirrored-backface-cards, motion-blur-photography, drag-scroll-key-hint, status-pill-badge]
mode: light
palette: ["#eeeeee", "#1744b1", "#d20431", "#451572", "#561b88", "#0d0f13"]
type_families: ["Inter (likely)"]
type_class: [neo-grotesk]
radius_px: [14, 9999]
motion: {durations_s: [0.33, 0.4, 0.43, 0.47, 0.43], easing: [ease-out, ease-in-out], loop: false}
scores: {aesthetics: 9, originality: 9, usability: 7, craft: 8}
craft_signals: [chromatic-fringe-on-stretched-edges, mirrored-text-on-side-cards, art-directed-blur-photos, single-hue-per-card, quiet-neutral-stage, keyboard-hint-caption]
anti_patterns: [side-card-content-unreadable, low-contrast-on-light-photo-areas]
---
# Fluid liquid card carousel. — Marcelo Design X

## 1. Snapshot
- **Subject:** A 12.06 s, 2126×1080 screen recording of a three-up card carousel. One flat centre card sits between two neighbours whose outer edges stretch like taffy to the viewport edge.
- **Why it's remarkable:** The side cards are not scaled down in the usual way. They are pulled out to the screen edge as a curved, liquid funnel with a rainbow fringe. The photography (portraits shot with heavy horizontal motion blur) carries the same "smear" idea, so content and transition share one visual language.

## 2. Composition & layout
- Neutral stage of #eeeeee filling 100% of the frame. The centre card is about 532×664 px (a 4:5 portrait), centred, with its top at y≈186 and bottom at y≈850. That leaves about 186 px of air above and about 230 px below.
- **Side cards:** their inner edges sit about 130 px from the centre card (x≈667 and x≈1458). Their visible face is a rectangle about 438 px tall, shorter than the centre card, so they read as receding. From there the outer half flares up and down in an S-curve to fill the full 1080 px height at the screen edge.
- A single caption, "Drag, scroll or use ← →", is centred at y≈1040, about 17 px from the bottom edge.
- **Card interior:** the title block is two lines top-left with about 36 px inset; the status pill is top-right; one metric line sits bottom-left about 50 px from the bottom.

## 3. Typography
- One neo-grotesk (Inter or SF-like) at weight 400–500, white.
- Card title is about 21 px over two lines with leading of about 1.25 ("Sleep / Last night"). The metric line ("Deep sleep 1 h 52 m") is about 21 px too, so hierarchy comes from position, not size.
- The status pill ("Rested", "Develop", "Offshore", "Waxing") is about 16 px medium in a translucent white pill.
- The caption is about 17 px, grey #555-ish, and uses real arrow glyphs.
- Side cards show the same type **mirrored**, as though you were seeing the card's face through glass from behind. This is a deliberate 3D cue.

## 4. Colour
| Hex | Role | Share (key frame) |
|---|---|---|
| #eeeeee | stage background | 37% |
| #1744b1 | active card (Sleep) cobalt | 5% |
| #d20431 / #b30026 | Heart-rate card crimson | 14% |
| #451572 / #561b88 | Moon-phase card violet | 10% |
| #0d0f13 | silhouette shadows inside photos | 7% |

Each card owns one saturated hue: green (surf), indigo (coffee), crimson (run), cobalt (sleep), violet (moon) and orange (solar). The stage stays achromatic, so colour only ever comes from content.

WCAG checks:
- White text on #1744b1 is 8.41:1.
- White on #d20431 is 5.52:1.
- White on the lighter cyan top of the blue card (≈#4a7fd8) is **3.95:1**, which passes for large text only.
- Caption #555 on #eeeeee is 6.43:1.

## 5. Depth & material
- No drop shadow on the centre card. Depth is faked by geometry: the side cards are shorter and their outer halves curve away like a cylinder, or film wrapping a drum.
- Along the stretched edge there is a thin spectral fringe (yellow, magenta and cyan, about 4–8 px wide), mimicking lens dispersion. It makes the stretch read as a refractive material rather than a warp filter.
- The centre card has radius ≈14 px. The pill uses a 9999 px radius with a white fill at about 20% opacity.

## 6. Components & patterns
- **Card:** a full-bleed photo, a two-line label, a status pill and a footer metric. It is a data-widget card (health, weather, coffee, solar) styled as an editorial poster.
- **Navigation:** three input modes (drag, wheel, arrow keys) are declared in one caption. A grab-hand cursor appears over the centre card.
- **During drag** (t≈8.71 s) the centre card tilts a few degrees and skews, which gives physical feedback before it snaps.

## 7. Motion
Measured: 120 fps, 12.06 s, `motion_fraction` 0.17, not a seamless loop. There are five transition segments, each 0.33–0.47 s long (median **0.43 s**):
- 0.80–1.13 s (0.33 s, symmetric);
- 2.37–2.77 s (0.40 s, peak at 0.21, ease-out);
- 4.00–4.43 s (0.43 s, ease-out);
- 6.23–6.70 s (0.47 s, ease-out);
- 8.20–8.63 s (0.43 s, symmetric).

Advances happen roughly every 1.6–2.2 s. The fast-start, decelerating shape suggests a spring or `cubic-bezier(.2,.8,.2,1)` snap. Between segments the frame is static, so the liquid stretch is a resting state rather than an idle animation. From frame differences, the card hue cross-fades through the funnel as each card slides to the centre (estimate).

## 8. Brand system
n/a — not a brand system. Identity cues:
- a motion-blur portrait series as the house photographic style;
- one hue per data domain.

## 9. UX
- **Strengths:**
  - Clear focus (one flat, readable card), with neighbours visible for context.
  - Three declared input methods.
  - The status pill provides at-a-glance state.
- **Risks:**
  - Side-card text is mirrored and blurred, so it cannot be read.
  - Only 3 of 6 cards are visible, and there are no position dots.
  - The stretch effect would be costly (WebGL) and should be reduced under `prefers-reduced-motion`.

## 10. Craft signals
- A spectral (RGB-split) fringe of 4–8 px is applied only on the curved stretched edges.
- Side-card text is horizontally mirrored, which is consistent with seeing the card from behind.
- Every photo shares the same horizontal blur direction as the swipe axis.
- Exactly one dominant hue per card, with no gradients mixing domains.
- Caption, pill and metric line all share one size family (about 16–21 px), so there is no type clutter.
- The tilt during drag at t≈8.71 s gives direct-manipulation feedback.

## 11. Reproduction recipe
```css
:root{--stage:#eeeeee;--ink-2:#555;--card-r:14px;--snap:cubic-bezier(.2,.8,.2,1);--snap-d:.43s;
  --font:"Inter",system-ui,sans-serif}
.stage{background:var(--stage);height:100vh;display:grid;place-items:center;perspective:1200px;overflow:hidden}
.card{width:min(532px,40vw);aspect-ratio:4/5;border-radius:var(--card-r);overflow:hidden;position:relative;
  transition:transform var(--snap-d) var(--snap),filter var(--snap-d) var(--snap);color:#fff;font:400 21px/1.25 var(--font)}
.card[data-pos="-1"]{transform:translateX(-62%) rotateY(55deg) scaleY(.66);filter:blur(1px)}
.card[data-pos="1"]{transform:translateX(62%) rotateY(-55deg) scaleY(.66);filter:blur(1px)}
.pill{position:absolute;top:28px;right:28px;padding:4px 12px;border-radius:9999px;background:rgb(255 255 255/.2);font-size:16px;font-weight:500}
.hint{position:fixed;bottom:16px;inset-inline:0;text-align:center;color:var(--ink-2);font-size:17px}
/* edge stretch + spectral fringe needs WebGL: displace UVs by smoothstep(0.5,1.0,|x|) and offset R/B channels by ±3px */
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 9 | Neutral stage plus single-hue blurred portraits, with the liquid funnel framing the focus card. |
| Originality | 9 | Replacing coverflow scaling with a refractive edge-stretch is a new carousel idea. |
| Usability | 7 | The focus card is clear and the inputs are declared, but there is no index indicator and neighbours cannot be read. |
| Craft | 8 | Consistent blur language and a precise spectral fringe. Some text over light photo zones drops to about 4:1. |

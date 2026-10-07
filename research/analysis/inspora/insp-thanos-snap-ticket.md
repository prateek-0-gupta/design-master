---
id: insp-thanos-snap-ticket
source: inspora
category: Motion
status: analyzed
title: "Thanos snap ticket"
creator: "Rehan Ahmed"
styles: [corporate-clean, flat-illustration, micro-interaction, generative-particle]
patterns: [particle-disintegration-swap, toggle-button-label-swap, segmented-tabs, card-content-crossfade, illustrated-hero-banner, floating-tab-bar, device-mockup-on-gradient-backdrop]
mode: light
palette: ["#f1f1f3", "#fefefe", "#e3e3e6", "#111111", "#1c1c1e", "#2db84d", "#aeb0b5", "#e8a3b4"]
type_families: ["SF Pro (likely)"]
type_class: [neo-grotesk]
radius_px: [9999, 28, 24, 14]
motion: {durations_s: [0.58, 0.67], easing: [ease-out], loop: true}
scores: {aesthetics: 8, originality: 7, usability: 7, craft: 8}
craft_signals: [directional-dust-left-to-right, qr-reassembles-from-particles, fixed-card-height-across-states, touch-indicator-ring, consistent-pill-radii, on-time-green-semantic]
anti_patterns: [green-text-low-contrast, effect-may-read-as-deletion]
---
# Thanos snap ticket — Rehan Ahmed

## 1. Snapshot
- **Subject:** An 11.3 s, 2000×2000 iPhone mock of a Shinkansen journey app (Tokyo 09:00 → Kyoto 11:12). Tapping "Show ticket" disintegrates the trip summary into dust, and the dust resolves into a QR boarding code. "Hide ticket" reverses it.
- **Why it's remarkable:** The Thanos-snap particle effect is used as a content swap inside a fixed card rather than as deletion, so one card holds two faces (itinerary and gate pass).

## 2. Composition & layout
- **Phone:** ~760 px wide in the 2000 px frame, centred on a #f1f1f3 → white backdrop with a soft contact shadow. The sheet frames at 1.89–4.41 s are push-in crops.
- **Screen stack, top to bottom:**
  - nav bar (back circle, centred "My Journeys", kebab menu);
  - a three-segment control (Overview / Live / Tickets);
  - a ~330 px illustrated hero (Mt Fuji, torii gate, sakura, N700S train);
  - the ticket card;
  - a "Journey details" list card;
  - a floating four-item tab bar.
- **Ticket card:** about 700×440 px in frame, 32 px padding. The top row holds "Nozomi 32" with a seat chip "7-E". The middle row is a departure/arrival time pair with a dotted route line and a train glyph. The bottom row is a full-width black pill CTA plus a 56 px circular map button.
- **QR state:** a ~200 px QR on the left, with "Scan at the gate", route, "Car 7 · Seat 7-E" and "E 4108 2773" on the right. The card height is unchanged.

## 3. Typography
- SF Pro throughout (iOS system).
- **Sizes (in the 2000 px frame, ≈2.0× device pt):**
  - times 09:00 / 11:12 at ~56 px (28 pt) semibold;
  - nav title ~36 px semibold;
  - card title ~30 px semibold;
  - meta ("Tokyo", "Platform 14") ~22 px regular grey;
  - tab labels ~20 px.
- **Hierarchy:** times > title > meta, with a big ~1.9× jump to the times.
- "On time" and "2 min" are set in green with no weight change.

## 4. Colour
| Hex | Role | Approx share |
|---|---|---|
| #f1f1f3 | backdrop and app background | 67% |
| #fefefe | cards, active segment | 10% |
| #e3e3e6 / #d2d3d7 | segmented track, hairlines | 13% |
| #111111 / #1c1c1e | text, CTA pill | 5% |
| #aeb0b5 | illustration mountains, inactive icons | 5% |
| ≈#2db84d | status green ("On time", "2 min") | <1% |
| ≈#e8a3b4 | sakura accent (illustration only) | <1% |

WCAG checks:
- Black text on white: 18.88:1.
- Grey meta ≈#8a8a8e on white: 3.44:1 (AA-large only).
- **Green #2db84d on white: 2.6:1, which fails even large-text AA.** The status depends on a weak colour.
- White label on the #1c1c1e CTA: 17.01:1.

## 5. Depth & material
- **Flat iOS cards:** radius ~24 px (device ≈12 pt), no visible shadow, separated from the #f1f1f3 ground by brightness alone.
- **Tab bar:** a floating white pill with a faint shadow; the active item gets a #ececef capsule.
- **Phone mock:** a realistic titanium frame and an 80 px-blur shadow beneath it.
- The illustration is flat vector with soft atmospheric gradients and no outlines.

## 6. Components & patterns
- **Toggle CTA:** "Show ticket" (QR icon) becomes "Hide ticket" (× icon) in the same 520×88 px black pill. The label and icon swap while the shape stays.
- **Simulated touch:** a 64 px grey ring marks taps for the demo.
- **Disintegration:** At 4.41–5.66 s the text glyphs on the right half break into 1–3 px dark specks drifting right and up, while the left content survives longest. At 8.18 s the QR's right two-thirds are dust while the left column of modules is still solid. The effect sweeps left to right.
- **Seat chip:** a small pill with a seat icon and "7-E".

## 7. Motion
Measured profile: 11.33 s at 24 fps, `motion_fraction` 0.11, `seamless_loop_likely` true (first-to-last difference 0.34).
- **0.92–1.50 s (0.58 s, peak 0.32, ease-out):** the itinerary dissolves and the QR forms.
- **4.29–4.96 s (0.67 s, peak 0.34, ease-out):** the reverse swap.
- **Gentle segments:** The camera push-ins and later swaps (~8 s, ~10 s) are visible in frames but fall under the energy threshold. Particles are sparse, so the motion energy is low.
- Both measured transitions decelerate (peak at about one-third): particles burst out fast and settle slowly.
- The swap is about 0.6 s long, so the effect reads as playful rather than slow.

## 8. Brand system
n/a — not a brand system. Identity cues:
- a Japanese rail travel motif (Fuji, sakura, torii);
- a monochrome UI with the illustration carrying all the colour;
- green reserved for live status.

## 9. UX
- **Strengths:**
  - The QR appears in the same card where the user tapped, with no navigation.
  - The CTA label states the reversible action.
  - Card height is fixed, so the list below does not jump.
- **Risks:**
  - Disintegration is a widely known "deleted" metaphor. The first-time user may think the trip was cancelled.
  - The status green fails contrast.
  - Gate scanning needs instant display, so particles should be skipped under `prefers-reduced-motion`.

## 10. Craft signals
- Particles stream in one direction (rightward), so the dissolve has a wind direction rather than random noise.
- The QR reassembles column by column from the left edge (8.18 s frame).
- The card keeps identical height in both states (no layout shift).
- Pill radii are consistent: the CTA, segments, tab bar and seat chip are all full-round.
- Semantic colour is used only for time-critical status ("On time", "2 min").
- The CTA keeps the same width when its label changes.

## 11. Reproduction recipe
```css
:root{--bg:#f1f1f3;--card:#fefefe;--ink:#111;--meta:#8a8a8e;--track:#e3e3e6;--ok:#1f8a3a;
  --r-card:24px;--r-pill:9999px;--font:-apple-system,"SF Pro Text",Inter,sans-serif}
.ticket{background:var(--card);border-radius:var(--r-card);padding:16px;min-height:220px;position:relative}
.ticket .face{transition:opacity .58s cubic-bezier(.2,.7,.3,1)}
.cta{border-radius:var(--r-pill);background:#1c1c1e;color:#fff;height:44px;font:600 15px var(--font)}
@media (prefers-reduced-motion:reduce){.dust{display:none}.ticket .face{transition:none}}
```
```js
// Snap: rasterise the outgoing face to a canvas, then push pixels right with a staggered start by x.
particles.forEach(p => { p.delay = (p.x / w) * 0.25; p.vx = 40 + Math.random()*80; p.vy = -20 - Math.random()*40; });
// Animate for 0.6 s with easeOutCubic, fade alpha to 0; fade the incoming face in from x=0 to x=w over the same window.
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Calm iOS monochrome with a charming illustrated hero. |
| Originality | 7 | The snap effect is known, but reusing it as a two-face card swap is a fresh application. |
| Usability | 7 | Fast in-place access to the QR. The metaphor risks reading as deletion and the green fails contrast. |
| Craft | 8 | Directional dust, column-wise reassembly and stable layout are well executed. |

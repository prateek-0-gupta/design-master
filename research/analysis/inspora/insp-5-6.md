---
id: insp-5-6
source: inspora
category: Web
status: analyzed
title: "Clucky Landing page"
creator: "@adrianabelarde_"
styles: [playful-rounded, minimal-swiss, flat-illustration, micro-interaction]
patterns: [scroll-linked-time-drums, mascot-hero, waitlist-email-capture, mission-tile-grid, feature-card-trio, live-counter-in-nav, hand-written-click-me-hint]
mode: light
palette: ["#ececec", "#ffffff", "#dbdbda", "#cecbc5", "#111111", "#92846e", "#e0662a"]
type_families: ["Inter Display / Inter Tight Bold (likely)", "handwritten script for annotation (likely Caveat-like)"]
type_class: [neo-grotesk, script]
radius_px: [24, 20, 9999]
motion: {durations_s: [0.23, 2.23, 1.40, 0.73, 0.43, 1.73], easing: [ease-out, ease-in-out], loop: true}
scores: {aesthetics: 8, originality: 9, usability: 7, craft: 8}
craft_signals: [hour-and-minute-drums-flank-content, active-digit-black-neighbours-fade, drum-arc-as-section-frame, tight-negative-tracking-display, mascot-shadow-ellipse-grounding, microcopy-voice-in-legal-line]
anti_patterns: [placeholder-text-low-contrast, decorative-drums-eat-30pct-width]
---
# Clucky Landing page — @adrianabelarde_

## 1. Snapshot
- **Subject:** A 1920×1214, 17.5 s scroll-through of "Clucky", a rooster alarm app for iPhone, shown in a Chrome window.
- **Why it's remarkable:** Two giant clock-picker drums, hours on the left and minutes on the right, frame every section and **rotate with scroll**. The page acts as an alarm time-picker: you set the time by reading it. It runs 07:00, then 10:15, 01:30, 05:50 and back to 07:00, and the theme turns into the scroll indicator.

## 2. Composition & layout
- **Framing:** The browser viewport is ~1380 px wide in the recording. Two pale-grey arcs (ring thickness ~60 px, radius ~470 px) are cropped by the left and right edges, so each half shows a semicircular drum. The digits sit along the inner edge of each ring.
- **Hero:** centred in a column ~440 px wide. Top to bottom:
  - mascot (~150 px)
  - a hand-written "↗ hey! click me" note
  - 3-line headline
  - 2-line sub
  - email field and "Notify me" pill
  - a microcopy line
- **Nav:** wordmark on the left, the live counter "300,313 clucks and counting" in the centre, and a "Coming soon" pill on the right.
- **Later sections:**
  - "Snooze Is Earned" with a 3×2 grid of ~110 px dark mission tiles (Math, Memory, Tilt, Shake, Typing, Colors).
  - A trio of ~345×435 px white feature cards with mascot illustrations.
  - A phone mock with the mascot.
  - A footer with "No accounts. No ads. No data games."

## 3. Typography
- **Headline:** a heavy neo-grotesk, Inter Display or Inter Tight Bold (700–800), ~52 px with ~0.95 leading and tracking about −0.03 em.
- **Card titles:** ~22 px bold; card body ~16 px regular grey.
- **Drum digits:** the same family, Bold Italic-like (slanted because they follow the arc). The active digit is ~80 px #111, its neighbours ~60 px #c8c8c8, and the far digits fade to ~#e0e0e0.
- **Script:** a hand-written script, Caveat-like, ~18 px for "hey! click me", in grey with an arrow.
- **Microcopy:** "One email when Clucky hits the App Store. No spam, no cluckery." at ~12 px, with humour carried even into fine print.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #ececec | page canvas | 40% |
| #ffffff | cards, browser chrome, input | 48% (key incl. chrome) |
| #dbdbda | drum ring | 7% |
| #cecbc5 | inactive drum digits | 2% |
| #111111 / #000 | headline, active digit, primary button | — |
| #92846e | mascot shading and props | 2% |
| ~#e0662a (est.) / ~#f2b52b (est.) | comb and beak orange, egg and bell gold | <1% |

WCAG checks:
- Headline #111 on #ececec is **15.98:1**.
- Grey body #666 on #ececec is **4.86:1** (pass).
- Card body #666 on #f6f6f6 is **5.31:1**.
- The "Notify me" button is 21:1.
- The input placeholder ~#999 on #fff is **2.85:1** (fails, though placeholders are commonly exempt).
- Inactive drum digits #cecbc5 on #ececec are 1.37:1, intentionally decorative.

## 5. Depth & material
- **Surfaces:** Flat with very soft lift. Feature cards are #f6f6f6 on #ececec with radius ~24 px and no visible shadow. Mission tiles are dark (#1a1a1a) with radius ~20 px.
- **Mascot:** sits on a soft grey ellipse shadow for grounding.
- **Drum rings:** a subtle radial gradient that is lighter toward the inner edge, a slight cylinder illusion.
- **Phone mock:** on a matte #d9d9d9 slab with a cloud vignette.

## 6. Components & patterns
- **Scroll-linked time drums:** decorative but semantic. They double as a progress indicator.
- **Waitlist form:** a pill input (~265×46 px) with an attached black pill button. Not joined; there is an ~10 px gap.
- **Mission tiles:** a square icon-card grid with bold, multi-coloured flat icons (red, yellow, green, violet). It is the only saturated colour block on the page.
- **Feature cards:** title, two lines, then three lines of body, centred.
- **Counter in nav:** social proof as live data.
- **Easter egg:** the "hey! click me" mascot. Clicked at 2.91 s, it triggers a reaction animation.

## 7. Motion
- **Measured:** 17.47 s at 30 fps, motion_fraction **0.37**, 6 segments with a median of **1.06 s**, **seamless_loop_likely = true** (first/last diff 0.58). The recording returns to the hero.
- **Segments:**

  | Time (s) | Duration (s) | Curve | Probable action |
  |---|---|---|---|
  | 1.50–1.73 | 0.23 | ease-out, peak 0.07 | mascot tap response |
  | 4.57–6.80 | 2.23 | ease-out | scroll |
  | 7.00–8.40 | 1.40 | ease-out | scroll |
  | 9.10–9.83 | 0.73 | ease-in-out | scroll |
  | 12.03–12.47 | 0.43 | ease-in-out | scroll |
  | 14.40–16.13 | 1.73 | ease-in-out | scroll-to-top |

- **Interpretation:** The scroll segments come from smooth-scroll inertia, and the drum digits rotate in lockstep. Hours advance about 1 step per ~150 px of scroll (estimate from frames). The return to top runs the drums backwards to 07:00.

## 8. Brand system
n/a — not a brand system, but strong identity cues:
- a rooster mascot with oversized glasses as the recurring character in multiple poses (bell, laptop, egg);
- a deadpan, punny voice ("Snarky, never mean.", "Good mornings earn eggs.");
- a monochrome page so the mascot's orange and gold own the colour.

## 9. UX
- **Strengths:**
  - The value proposition is legible in 2 s.
  - One primary action (email), repeated as a "Coming soon" pill.
  - The drums give an ambient progress sense.
- **Risks:**
  - Drums consume ~30% of horizontal space, which needs a mobile fallback (likely hidden).
  - Rotating content on scroll needs a prefers-reduced-motion stop.
  - The "click me" hint promises an interaction that is not essential.

## 10. Craft signals
- The active digit is vertically centred on the same y as the content block's optical centre (headline mid-line at y≈595 of 1214).
- The hour drum advances in whole steps while the minute drum moves in 5-min steps (00 → 15 → 30 → 50 → 55), a believable clock.
- Neighbour digits follow a 3-level grey ramp (#111 → #c8c8c8 → #e0e0e0) plus a scale ramp of about 80/60/52 px.
- Fine print matches the brand voice.
- All cards and tiles share ~20–24 px radii, and the pills are full.

## 11. Reproduction recipe
```css
:root{--bg:#ececec;--card:#f6f6f6;--ring:#dbdbda;--ink:#111;--muted:#666;--digit-off:#cecbc5;
  --r-card:24px;--r-tile:20px;--font:"Inter Display","Inter Tight",system-ui,sans-serif}
h1{font:800 clamp(36px,4vw,56px)/.95 var(--font);letter-spacing:-.03em;color:var(--ink);text-align:center}
.drum{position:fixed;top:50%;width:940px;aspect-ratio:1;border-radius:50%;border:60px solid var(--ring);translate:0 -50%}
.drum.h{left:-620px}.drum.m{right:-620px}
.drum .digits{position:absolute;inset:0;rotate:calc(var(--scroll,0) * -1turn);transition:rotate .1s linear}
.drum .d{position:absolute;font:800 60px var(--font);color:var(--digit-off)}
.drum .d.on{font-size:80px;color:var(--ink)}
.wait{display:flex;gap:10px}.wait input{border-radius:9999px;background:#fff;padding:12px 20px;border:0}
.wait button{border-radius:9999px;background:#000;color:#fff;font:600 15px var(--font);padding:12px 20px}
@media (prefers-reduced-motion:reduce){.drum .digits{rotate:none}}
```
```js
addEventListener('scroll',()=>document.documentElement.style.setProperty('--scroll',scrollY/(document.body.scrollHeight-innerHeight)),{passive:true})
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Calm greyscale page, one lovable mascot, bold type. |
| Originality | 9 | Scroll-driven hour and minute drums that turn the page into an alarm picker are a new, on-concept idea. |
| Usability | 7 | Clear single CTA; decorative drums and motion need responsive and reduced-motion handling. |
| Craft | 8 | Coherent radii, tonal digit ramp and witty microcopy everywhere. |

---
id: insp-iquid-metal
source: inspora
category: Motion
status: analyzed
title: "liquid metal"
creator: "Brett (@BrettFromDJ)"
styles: [dark-premium, physical-material, micro-interaction]
patterns: [ai-composer-bar, send-button-ring, specular-rim-sweep, idle-ambient-animation, pill-container-cropped]
mode: dark
palette: ["#1d1d1d", "#000000", "#2c2c2e", "#0c0c0c", "#4b4a4f", "#7c7b82", "#e8e8f0"]
type_families: []
type_class: []
radius_px: [9999, 530]
motion: {durations_s: [16.0], easing: [linear], loop: true}
scores: {aesthetics: 8, originality: 7, usability: 6, craft: 8}
craft_signals: [chromatic-fringe-on-highlights, rim-thickness-varies-with-light, inner-top-gradient-on-button, concentric-button-in-pill-end, icons-share-one-grey]
anti_patterns: [low-contrast-icons, ambient-motion-without-state]
---
# liquid metal — Brett

## 1. Snapshot
- **Subject:** A 16 s, 3090×2160 @60 fps loop of an AI composer's toolbar end: attach clip, sparkle, and a circular send button wrapped in a polished liquid-chrome ring whose highlights crawl around the circumference.
- **Why it's remarkable:** All the "life" lives in a 6–10 px ring; the specular streaks carry tiny RGB fringes (cyan/amber/violet) like real chromatic dispersion, turning a stock send button into a jewel.

## 2. Composition & layout
- Canvas #1d1d1d; a black pill (#000) enters from the left edge and ends in a semicircle at x≈2070 px (original), height ≈1055 px (y≈548→1603) → end radius ≈ 530 px.
- Send button: circle ≈ 830 px diameter (original) centred at x≈1540, inset ≈ 110 px from the pill's curved end, so the pill end and the button are near-concentric.
- Icons: paperclip at x≈100–350, sparkle pair at x≈580–860, both ≈ 260 px tall, vertically centred on the pill axis. Gaps between groups ≈ 280 px — generous, one-thumb spacing at UI scale.
- Framing is an extreme macro crop: this is a ~48 px button scaled ~17×.

## 3. Typography
No text. Icons are rounded-cap line/fill glyphs (SF Symbols-like: `paperclip`, `sparkles`, `arrow.up`), stroke ≈ 18 px at this scale (≈1.6 px at 1×).

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #1d1d1d | canvas | 72% |
| #000000 | pill / composer surface | 24% |
| #2c2c2e → #0c0c0c | button fill gradient (top → bottom) | 2% |
| #4b4a4f / #7c7b82 | icon grey, ring mid-tones | 1.3% |
| #e8e8f0 (est.) | specular highlight on ring | <0.5% |
| #141d2d | cool blue shadow tint in ring | trace |

WCAG checks:
- Icon grey ≈#6e6e6e on pill #000: **4.12:1** (AA-large only; fine for 24 px icons, marginal as text).
- Arrow ≈#7c7b82 on button #1a1a1a: 4.15:1.
- Pill #000 against canvas #1d1d1d: 1.25:1 — the pill edge is nearly invisible; separation relies on the button's ring.

## 5. Depth & material
- Ring: chrome torus ~2–3% of the button diameter thick, with continuous dark-to-white reflection banding; thickness appears to swell where the highlight sits (≈8 px vs 4 px at 1× scale equivalent), mimicking a liquid surface.
- Chromatic dispersion: thin cyan/amber/magenta slivers at highlight boundaries (e.g. left 9 o'clock and bottom 5 o'clock in the key frame).
- Button face: vertical gradient #2c2c2e → #000 with a soft top sheen — a convex lens read.
- A faint dark gap (~6 px at scale) between ring and pill gives the ring a floating seat.

## 6. Components & patterns
- Composer action row: attach, AI-assist (sparkles), primary send. The send is the only element with material treatment — hierarchy via finish, not colour.
- Idle ambient animation on the primary CTA, the "alive" AI-input convention.

## 7. Motion
Measured (m0_motion.json): 16.0 s, 60 fps, **motion_fraction 0.0**, mean energy 0.10 (threshold 0.35), zero segments, `seamless_loop_likely: true` (first/last diff 1.16).
- The motion is so subtle and small-area that it never clears the energy threshold: only ring pixels change. From the nine frames (every ~1.78 s) the bright arcs migrate around the ring without a fixed direction — highlights at 1–2 o'clock (0.89 s), 7 and 5 o'clock (2.67 s), 12 and 7 o'clock (4.44 s) — reading as a slow, continuous, linear noise-driven flow rather than eased keyframes.
- Estimated highlight drift ≈ 60–120° per 1.8 s, i.e. a full apparent cycle every ~6–10 s.

## 8. Brand system
n/a — not a brand system. Identity cue: "liquid chrome" as the signature of the primary AI action.

## 9. UX
- The ring cleanly says "this is the primary button" without a brand colour; good for monochrome AI products.
- No state change is shown (disabled vs enabled send, pressed, sending). Ambient motion with no meaning risks becoming noise; ideally it intensifies when the input has text.
- Grey icons at ~4.1:1 are acceptable for icons (≥3:1 non-text) but feel dim.

## 10. Craft signals
- RGB fringe is only 2–4 px wide at original scale and appears only at highlight edges — restrained, not a global chromatic-aberration filter.
- Button centre and pill-end arc are near-concentric (button inset ≈110 px all around the curve).
- Paperclip, sparkle and arrow share the same grey value and stroke weight.
- Button face gradient runs lighter at top, matching the ring's top-light reflection.
- Loop is seamless (first/last diff 1.16).

## 11. Reproduction recipe
```css
@property --a{syntax:"<angle>";inherits:false;initial-value:0deg}
.send{width:48px;aspect-ratio:1;border-radius:50%;position:relative;
  background:linear-gradient(#2c2c2e,#000 70%);color:#7c7b82;}
.send::before{content:"";position:absolute;inset:-3px;border-radius:50%;padding:3px;
  background:conic-gradient(from var(--a),#3a3a44,#f2f2fa 8%,#7fd8ff 9%,#ffd28a 10%,#555 18%,#20222c 40%,
    #e8e8f0 55%,#b28cff 56%,#30303a 65%,#f5f5ff 85%,#3a3a44);
  -webkit-mask:linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);-webkit-mask-composite:xor;mask-composite:exclude;
  animation:spin 8s linear infinite;filter:blur(.3px)}
@keyframes spin{to{--a:360deg}}
.composer{background:#000;border-radius:9999px;padding:6px 6px 6px 16px}
body{background:#1d1d1d}
```
For the non-uniform "liquid" flow, drive two conic layers at different speeds (8 s and 13 s, opposite directions) with `mix-blend-mode:screen`, or use a small WebGL noise shader on the ring.

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Luxurious restraint: one material on a black field. |
| Originality | 7 | Chrome/glow send rings are trending; dispersion detail lifts it. |
| Usability | 6 | Clear primary action but no state semantics; dim icons. |
| Craft | 8 | Convincing reflection banding, concentric geometry, seamless loop. |

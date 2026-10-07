---
id: insp-1-31
source: inspora
category: Motion
status: analyzed
title: "Liquid metal button"
creator: "@tojawuzik"
styles: [dark-premium, y2k-chrome, physical-material, micro-interaction]
patterns: [iridescent-ring-highlight, orbiting-specular-light, pill-nav-button, icon-disc-in-pill, ambient-glow-halo]
mode: dark
palette: ["#080808", "#191919", "#272729", "#3c383a", "#665c5a", "#939593", "#e5eae1"]
type_families: ["SF Pro Display / Inter (likely)"]
type_class: [neo-grotesk]
radius_px: [9999]
motion: {durations_s: [0.23, 0.33, 0.77, 4.98], easing: [ease-in-out, ease-in], loop: true}
scores: {aesthetics: 8, originality: 7, usability: 6, craft: 8}
craft_signals: [chromatic-dispersion-on-rim, light-source-orbits-ring, halo-spills-onto-pill-edge, double-bezel-pill, metallic-gradient-icon, seamless-5s-loop]
anti_patterns: [pill-edge-near-invisible-on-black, decorative-motion-without-state]
---
# Liquid metal button — @tojawuzik

## 1. Snapshot
- **Subject:** A 1080×1080, 5.0 s, 60 fps macro crop of a dark pill-shaped "Home" nav button. Its round icon well is ringed by a liquid, iridescent metal band whose bright highlight travels around the circle.
- **Why it's remarkable:** The ring behaves like polished chrome under a moving light. It produces spectral (RGB-split) fringes on the shadow side and a white-hot specular bloom on the lit side, so a static nav item feels alive and premium.

## 2. Composition & layout
- **Framing:** A tight crop. The pill enters from the left edge at x≈295 and is cut at the right frame edge, so only the icon and "Home" are visible. It is centred vertically (pill y≈300→775, so ≈475 px tall, which equals the pill radius ×2).
- **Icon well:** a circle of ≈340 px diameter at x≈380–720, with an ≈18 px gap to the inner pill bezel.
- **Label:** "Home" starts ≈95 px right of the ring. The cap height of ≈90 px aligns its x-height centre with the ring's centre (y≈540).
- **Background:** pure near-black, with a radial bloom of ≈250 px around the light hot-spot.

## 3. Typography
- **Label:** a single word in a neo-grotesk (SF Pro / Inter-like) Regular-to-Medium at ≈120 px, which is ≈60 px at a 2× preview scale. Tracking is normal and the label is pure white.
- There is no other text. Hierarchy is irrelevant here; the label is just an anchor that proves the object is a button.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #080808 | background | 65% |
| #191919 | pill body | 13% |
| #272729 / #3c383a | inner well, bezel steps | 10% |
| #665c5a / #939593 | metallic mid-tones of icon and rim | 6% |
| #e5eae1 | specular white, icon highlight, label | 3% |
| (spectral) | thin RGB dispersion in the ring: cyan, magenta, orange, at most 4 px bands | <1% |

WCAG checks:
- The label (white) on the pill #191919 reaches **17.58:1**.
- The icon #e5eae1 on the well #3c383a is 9.45:1.
- The pill outline #272729 against the background #080808 is only **1.34:1**, so the button's boundary is almost invisible without the glow.

## 5. Depth & material
- **Pill:** a double bezel. The outer pill edge is a slightly lighter (#272729) rim of ≈20 px with a soft top highlight, and an inner pill body (#191919) sits inside it.
- **Icon well:** a concave dark disc (#3c383a centre to darker edge) inside a ≈14 px thick ring.
- **Ring:** rendered as liquid chrome with a bright specular streak covering ≈90–120° of arc, chromatic dispersion where the light falls off, and a dark occluded side.
- **Glow:** the hot spot casts a warm-white additive glow onto the pill's top edge and the background (#080808 → ≈#3a3330 near the bloom).
- **Icon:** a filled house glyph with a vertical silver gradient (light top-left, grey bottom). It is metal, not a flat white glyph.

## 6. Components & patterns
- **Nav item:** a pill with a leading icon disc, as in a tab bar or sidebar item.
- **Highlight:** the "orbiting specular" pattern acts as a hover/active or attention state. It is a modern variant of the conic-gradient border.
- **Reusable decomposition:**
  - conic gradient ring + blur bloom;
  - hue-rotate fringes;
  - a rotating light angle.

## 7. Motion
- **Measured:** duration 4.98 s at 60 fps. motion_fraction 0.26, mean energy 0.31. seamless_loop_likely **true** (first/last diff 0.25).
- **Segments:**
  - 0.27–0.50 s (0.23 s, symmetric);
  - 1.73–1.83 s (0.10 s);
  - 2.07–2.40 s (0.33 s, symmetric);
  - 2.83–3.60 s (0.77 s, peak 0.89, so **ease-in**).
- **From frames (estimates):**
  - The highlight starts at about 11 o'clock (0.28 s) and swings to the top (0.83–1.38 s). It then grows into a broad white arc on the right side (1.94–2.49 s, the energy peaks), and recedes back to the top-left by 3.6–4.7 s.
  - The light behaves like a pendulum sweep rather than a constant rotation. The ring's surface also wobbles (the liquid distortion visibly reshapes the dispersion bands between frames).
- **Implied pacing:** a slow ≈5 s breathing cycle with a sharp ~0.3 s flare at the brightest moment.

## 8. Brand system
n/a — not a brand system. Identity cues: Apple-like dark chrome and "liquid glass" sensibility.

## 9. UX
- **Strengths:** The glow draws strong attention, which is good for a primary or currently selected nav item. The label contrast is excellent.
- **Risks:**
  - The motion runs perpetually without signalling a state change; in a real nav, only the active item should glow.
  - The pill boundary disappears on black (1.34:1).
  - A continuous 5 s loop needs a `prefers-reduced-motion` fallback.
  - The GPU cost of blur, blend and shader effects matters on mobile.

## 10. Craft signals
- RGB fringes appear only on the falloff side of the highlight, which is physically plausible dispersion.
- The specular glow bleeds onto the pill's top rim and background. The light affects its surroundings.
- The pill has two bezels (outer #272729 rim, inner #191919 body) and the icon well is a third level of depth.
- The house glyph has its own metallic gradient matching the ring material.
- The loop closes seamlessly at 4.98 s (first/last frame diff 0.25).

## 11. Reproduction recipe
```css
@property --a{syntax:"<angle>";inherits:false;initial-value:300deg}
.pill{display:flex;align-items:center;gap:48px;height:238px;padding:0 60px 0 22px;border-radius:9999px;
  background:#191919;box-shadow:0 0 0 10px #232325,inset 0 1px 0 rgba(255,255,255,.08)}
.well{position:relative;width:170px;aspect-ratio:1;border-radius:50%;
  background:radial-gradient(circle at 50% 40%,#3c383a,#1d1c1d)}
.well::before{content:"";position:absolute;inset:-8px;border-radius:50%;padding:7px;
  background:conic-gradient(from var(--a),#fff 0 8%,#ffd9a0 12%,#ff4fa0 16%,#3cf 20%,#111 35% 70%,#6af 80%,#fff 100%);
  -webkit-mask:linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);-webkit-mask-composite:xor;mask-composite:exclude;
  filter:saturate(1.4) drop-shadow(0 0 18px rgba(255,240,220,.55));animation:sweep 5s ease-in-out infinite}
@keyframes sweep{0%,100%{--a:300deg}50%{--a:420deg}}
.icon{color:transparent;background:linear-gradient(160deg,#fff,#9a9a9a);-webkit-background-clip:text}
.label{font:500 60px/1 "SF Pro Display",Inter,system-ui;color:#fff}
@media (prefers-reduced-motion:reduce){.well::before{animation:none}}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Gorgeous material rendering; the dark chrome and dispersion feel premium. |
| Originality | 7 | A fresh liquid-metal take on the well-worn glowing-border trend. |
| Usability | 6 | Strong focus cue, but perpetual motion with no state meaning, and a faint boundary. |
| Craft | 8 | Plausible light physics, layered bezels, a seamless loop. |

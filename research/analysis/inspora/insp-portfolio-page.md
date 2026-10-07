---
id: insp-portfolio-page
source: inspora
category: Web
status: analyzed
title: "portfolio page"
creator: "@basit_designs"
styles: [minimal-swiss, generative-particle, photo-led, aurora-glow]
patterns: [spiral-image-vortex, oval-thumbnail-particles, chromatic-motion-trail, centered-manifesto-line, two-tone-headline, single-dark-cta, corner-menu-pill]
mode: light
palette: ["#fefefe", "#111111", "#a0a0a0", "#e6e6e6", "#4d293b", "#1f1c2c", "#6b768c"]
type_families: ["Inter Display / SF Pro Display (likely)"]
type_class: [neo-grotesk]
radius_px: [9999, 12, 8]
motion: {durations_s: [2.47, 7.07], easing: [ease-in, linear], loop: false}
scores: {aesthetics: 9, originality: 8, usability: 6, craft: 8}
craft_signals: [spectral-trail-only-at-vortex-edge, thumbnails-foreshortened-by-arm-angle, white-canvas-91pct, headline-two-tone-black-to-grey, stacked-numeric-logo]
anti_patterns: [grey-headline-tail-fails-contrast, motion-heavy-no-pause, thumbnails-unlabeled]
---
# portfolio page — @basit_designs

## 1. Snapshot
- **Subject:** A 3548×2160 (60 fps) 10.7 s capture of the studio site "N2 33." Dozens of oval image thumbnails flow outward in a slow spiral vortex around a single centred manifesto line and a "Let's Talk" button. Near the frame edges the thumbnails smear into rainbow, spectral motion trails.
- **Why it's remarkable:** The portfolio is the particle system. Each particle is a project image (coffee beans, a fig, a padel racket, a peeler, a leopard print, tree bark), and the chromatic smear at the vortex rim turns speed into colour on an otherwise pure-white page.

## 2. Composition & layout
- **Canvas:** About 91% #fefefe.
- **Corners:**
  - Logo "N2 / 33." top-left, stacked numerals at ~40 px CSS.
  - A "Menu ⁘" pill top-right, ~160×52 px, #e6e6e6, radius ~12 px, with a 2×3 dot icon.
- **Centre copy:**
  - A 3-line headline at ~24 px CSS, about 500 px wide, centred at 50%/52%.
  - A black "Let's Talk" button (~100×36, radius ~8).
- **Vortex:** Three to four logarithmic-spiral arms of ovals (~40–100 px) wind around the copy. Ovals are foreshortened (elliptical) according to their angle on the arm, which suggests a tilted 3D plane. Their size grows with radius, from ~45 px near the centre to ~100 px near the rim.
- **Text clearance:** The copy keeps a ~150 px clear radius, and no thumbnail ever crosses it.

## 3. Typography
- **Typeface:** a single neo-grotesk, Inter Display or SF Pro Display.
  - Headline: Semibold (600) at ~24 px with ~1.2 leading and tracking about −0.01 em.
  - Two-tone: "We design change-making website experiences" in #111, then "that reflect what you've actually built." in ~#a0a0a0. The value shift creates a primary/secondary reading in one sentence.
  - Button: ~15 px medium, white.
  - Menu: ~17 px regular.
- **Logo:** "N2 / 33." is a stacked two-line numeric wordmark at tight leading (~0.85).

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #fefefe | canvas | 91% |
| #111111 | headline, CTA, logo | <1% |
| #a0a0a0 | headline tail | <0.5% |
| #e6e6e6 | menu pill | <0.5% |
| #4d293b / #a17b74 | coffee, fig thumbnails (wine-brown) | 1.6% |
| #1f1c2c / #525663 / #6b768c | dark metal and blue thumbnails | 2.7% |
| spectral (red→yellow→blue→violet) | motion trails at rim | ~2% |

WCAG checks:
- Black on white is **18.72:1**.
- The grey tail #a0a0a0 is **2.59:1**, which fails. At 24 px semibold it is still below the 3:1 large-text threshold.
- The CTA is white on black at 21:1.
- The menu label #1f1f1f on #e6e6e6 is 13.21:1.

## 5. Depth & material
- **3D read:** Implied by foreshortening and scale, as if the spiral sits on a plane tilted toward the viewer. Thumbnails near the rim are bigger and blurrier.
- **Trails:** At the outer boundary (top band y<200 and bottom corners) thumbnails stretch into comet trails with RGB/spectral dispersion (red-orange core with blue-violet fringes), like a long-exposure chromatic aberration. The effect is reserved for the rim only, so the centre stays crisp.
- **UI:** no shadows; flat.

## 6. Components & patterns
- **Image vortex:** a generative hero made from portfolio thumbnails. No captions are visible, so the thumbnails are not (visibly) interactive in the clip.
- **Manifesto line plus a single CTA:** the minimal agency hero formula.
- **Menu pill:** collapsed nav with a dot-grid icon.

## 7. Motion
- **Measured:** 10.73 s at 60 fps, motion_fraction **0.89** (almost always moving).
  - **0.00–2.47 s (2.47 s, ease-in, peak 0.99):** acceleration into a transition.
  - **3.63–10.70 s (7.07 s, continuous/linear, peak 0.93):** a steady rotation and outward drift.
- **Reset:** At 2.98 s the frame is almost blank (thumbnails faded, CTA ghosted), which looks like a reload or intro replay. The vortex then fades back in from the centre outward.
- **Rate:** Thumbnails advance along the arms at a roughly constant angular rate. Estimated from frames, the spiral rotates about 25° per 1.2 s, about 1 revolution per 17 s.
- **Loop:** Not a seamless loop in the capture (first/last diff 13.84), but the steady linear phase would loop naturally.

## 8. Brand system
n/a — not a brand system. Identity cues:
- the numeric "N2 33." wordmark;
- a white gallery-like canvas;
- thumbnails as a collective "body of work" texture;
- spectral trails as the only brand colour moment.

## 9. UX
- **Strengths:** The message is front and centre, there is a single obvious CTA, the work is visible immediately, and the motion is mesmerising.
- **Weaknesses:**
  - The grey half of the headline fails contrast.
  - Constant motion with no visible pause control (WCAG 2.2.2 for content moving over 5 s).
  - Thumbnails are anonymous, with no hover labels shown, so the vortex is decoration rather than navigation.
  - The almost-blank reset frame would read as a glitch.

## 10. Craft signals
- The clear zone around the copy stays at ~150 px radius throughout; no particle ever overlaps text.
- Thumbnail size and blur scale with distance from the centre (a depth cue).
- Spectral smear appears only beyond about 80% of the radius, so the effect is gated by position.
- The headline's two values come from one weight, with emphasis by luminance only.
- The palette of thumbnails is curated: warm browns, graphite and an electric blue repeat across arms for rhythm.

## 11. Reproduction recipe
```css
:root{--bg:#fefefe;--ink:#111;--ink-2:#767676;/* raised from #a0a0a0 for AA */--chip:#e6e6e6;--font:"Inter Display","SF Pro Display",system-ui,sans-serif}
.hero{position:relative;height:100vh;background:var(--bg);overflow:hidden}
.hero h1{position:absolute;inset:50% auto auto 50%;translate:-50% -50%;width:min(500px,80vw);text-align:center;
  font:600 24px/1.2 var(--font);letter-spacing:-.01em;color:var(--ink)}
.hero h1 span{color:var(--ink-2)}
.cta{background:var(--ink);color:#fff;border-radius:8px;padding:8px 16px;font:500 15px var(--font)}
.menu{position:fixed;top:16px;right:16px;background:var(--chip);border-radius:12px;padding:12px 16px}
.thumb{position:absolute;width:var(--s);aspect-ratio:1.25/1;border-radius:50%;background:var(--img) center/cover;
  transform:rotate(var(--a)) scaleY(.8);filter:blur(var(--b,0))}
@media (prefers-reduced-motion:reduce){.vortex{animation:none}}
```
```js
// log-spiral placement, rotated each frame at ~21°/s (linear)
const arms=4, per=10; let t=0;
function frame(dt){t+=dt*0.37; thumbs.forEach((el,i)=>{const arm=i%arms, k=Math.floor(i/arms)/per;
  const r=150+k*620, th=arm*2*Math.PI/arms + k*2.4 + t; const s=45+k*55;
  el.style.cssText+=`;left:${50+Math.cos(th)*r/innerWidth*100}%;top:${50+Math.sin(th)*r*.75/innerHeight*100}%;--s:${s}px;--b:${k>.8?(k-.8)*20:0}px`;});
  requestAnimationFrame(()=>frame(1/60));}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 9 | A gallery-white field with a living, colourful constellation of work; the spectral trails are gorgeous. |
| Originality | 8 | Making portfolio thumbnails the particles of a spiral, with chromatic speed trails, is fresh. |
| Usability | 6 | Clear CTA, but there are contrast failures, unlabeled work and no motion pause. |
| Craft | 8 | Disciplined clear-zone, depth scaling and rim-only dispersion; the reset frame is rough. |

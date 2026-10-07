---
id: insp-1-53
source: inspora
category: Web
status: analyzed
title: "glossy orb animation"
creator: "@basit_designs"
styles: [soft-3d, glassmorphism, luxury, minimal-swiss]
patterns: [bento-story-cards, refractive-orb-hero, logo-lozenge-on-image, pill-media-chip, ai-loading-indicator, gradient-footer-band, ghost-disc-placeholder]
mode: light
palette: ["#fdfdfd", "#f1f1f1", "#d4dbdf", "#c797a3", "#753045", "#568694", "#0a2332"]
type_families: ["Inter (likely)", "wide geometric wordmark (custom, Eurostile-like)"]
type_class: [neo-grotesk, geometric-sans]
radius_px: [40, 9999]
motion: {durations_s: [7.9], easing: [linear], loop: true}
scores: {aesthetics: 8, originality: 6, usability: 5, craft: 8}
craft_signals: [chromatic-aberration-rim-on-orb, frosted-lozenge-logo-plate, blurred-video-inside-pill, orb-crop-at-card-edge, same-copy-three-treatments, debossed-ghost-disc]
anti_patterns: [grey-footer-text-fails-aa, text-duplicated-across-cards, decorative-loading-chip-ambiguous]
---
# glossy orb animation — @basit_designs

## 1. Snapshot
- **Subject:** A 7.9 s, 3066×2160 recording of a "KODOR" quantum-processor brand board. It has three light bento columns, and the centre card holds a large refractive glass orb filled with a churning pink flower, sinking into a teal-to-ice gradient.
- **Why it's remarkable:** It is a sibling of insp-1-21 by the same creator. The flower-in-glass object is scaled up to dominate a card, with chromatic-aberration rims and a frosted logo lozenge laid across its equator. It reads as both product render and brand mark.

## 2. Composition & layout
- **Grid:** three columns about 725 px wide in the capture (x 370→1094, 1166→1892, 1966→2690 at full res), with gutters of about 72 px. The cards are about 1435 px tall and the radius is about 40 px (scaled).
- **Left card:**
  - the logo and a 3-line statement at the top;
  - a debossed ghost disc of about 550 px holding the "100+ qubit quantum executions" label;
  - a grey footnote at the bottom.
- **Centre card:**
  - the statement at the top;
  - the orb of about 725 px, cropped by the card sides, with the "KODOR" lozenge on it;
  - an overlaid tagline;
  - the logo on a gradient band at the bottom.
- **Right column (split):** a short card holding a dark blurred-video pill chip with text, and a tall card with the logo, a white ribbon swoosh, a small 95 px glossy navy ball and a 3-line intro.
- **Above the grid:** a "Mode Present…" label and a frosted input with a spinner, i.e. a presentation-mode loading cue.

## 3. Typography
- **Body:** Inter-like at regular weight throughout. Statements are about 28 px in the capture (about 14 CSS)/1.45, centred, #111. Footnotes are the same size in #8f8f8f.
- **Wordmark:** "KODOR" is a wide, heavy geometric caps face with a double-chevron "K" mark. It is set at about 36 px and repeated four times in black, white and on the lozenge.
- One text size dominates, so the board relies on objects for hierarchy.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #fdfdfd | canvas | 56.2% |
| #f1f1f1 | card fill | 29.4% |
| #d4dbdf | ice footer of the gradient | 3.3% |
| #c797a3 / #753045 | flower pinks and maroon (orb) | 5% |
| #568694 | teal mid-gradient, chip | 2.5% |
| #0a2332 | abyss navy, ball | 3.6% |

WCAG checks:
- Statement #111 on #f1f1f1 is 16.7:1.
- Footnote #8f8f8f on #f1f1f1 is 2.86:1 and fails.
- The tagline (≈#d4dbdf) on #0a2332 is 11.5:1.
- White text in the pill chip on #568694 is 4.01:1 (large only), and on the darker blur (#4f6f7a) 4.61:1. Legibility varies frame to frame as the video moves.

## 5. Depth & material
- **Orb:** a glass sphere containing a fluid floral video. The rim shows rainbow chromatic aberration (red/blue fringes of about 6–10 px) and a darker inner limb, a convincing lens effect.
- **Lozenge:** a frosted pink plate (about 330×95 px) with soft edges carrying the white wordmark. It reads as glass over glass.
- **Left-card disc:** debossed/neumorphic, with a light top rim and a soft lower shadow, nearly invisible (about 1.05:1 against the card).
- **Right card:** the ribbon is a soft white 3D form with a faint iridescent edge, and the navy ball has a sharp specular dot.
- **Pill chip:** a 1 px light rim plus an outer glow of about 8 px.

## 6. Components & patterns
- Bento brand-story cards: the same copy in three treatments (on light, on image, on chip).
- A logo lozenge on hero imagery.
- A media pill chip (a video blurred behind the text).
- A loading/presence cue ("Mode Present…" with a spinner).
- A gradient footer band that carries a reversed logo.

## 7. Motion
- **Measured:** 7.90 s at 60 fps. motion_fraction is 0.0 and mean energy 0.15, with no segments over threshold, so all motion is slow and small relative to the frame. It is not a seamless loop (first/last diff 3.85).
- **Observed across frames:**
  - The orb's flower churns continuously and the orb swells. Its top edge rises from y≈160 at t=0.44 s to y≈95 (sheet scale) by t=3.07 s, roughly a 15% scale-up, then holds.
  - The pill chip's blurred video pans.
  - The navy ball's specular highlight orbits, and the ball darkens to a near-matte black by t=7.46 s.
  - The spinner rotates.

The motion is ambient and linear in feel, with no UI transitions.

## 8. Brand system
n/a — this is a brand-moodboard presentation rather than a guideline. Identity cues:
- the "KODOR" double-chevron wordmark;
- a flower-in-glass hero object;
- a pink/maroon vs teal/navy complementary palette on near-white;
- three repeated statements that act as a voice sample.

## 9. UX
- As a presentation board it shows the brand well.
- As UI it has weaknesses:
  - duplicated copy;
  - footnotes failing contrast;
  - text over moving video;
  - a loading chip whose purpose is unclear.

## 10. Craft signals
- The orb diameter equals the card width, so the sphere is clipped by the card's rounded sides, a deliberate "too big for the frame" crop.
- The chromatic fringe sits only at the rim (where real lens dispersion occurs), not across the whole image.
- The wordmark is placed on the orb's equator inside a frosted lozenge, centred exactly on the card axis.
- The card radius (about 40 px) and pill radii stay consistent across all five panels.
- The gradient footer resolves to #d4dbdf, close to the canvas, so the dark card dissolves back into the page.

## 11. Reproduction recipe
```css
:root{--canvas:#fdfdfd;--card:#f1f1f1;--ink:#111;--muted:#8f8f8f;--abyss:#0a2332;--teal:#568694;--ice:#d4dbdf;--rose:#c797a3}
.card{border-radius:40px;background:var(--card);padding:56px 40px;text-align:center;font:400 14px/1.45 Inter}
.card--deep{background:linear-gradient(180deg,var(--card) 0 25%,var(--abyss) 60%,var(--teal) 85%,var(--ice))}
.orb{width:100%;aspect-ratio:1;border-radius:50%;overflow:hidden;position:relative;
  box-shadow:inset 0 0 0 2px rgba(255,255,255,.25),inset 6px 0 12px rgba(255,0,80,.35),inset -6px 0 12px rgba(0,120,255,.35);
  animation:swell 3s linear forwards}
@keyframes swell{from{transform:scale(.87)}to{transform:scale(1)}}
.lozenge{position:absolute;inset:auto 20% 45% 20%;height:95px;border-radius:50%;
  background:rgba(230,170,185,.55);backdrop-filter:blur(12px);display:grid;place-items:center;color:#fff}
.chip{border-radius:9999px;overflow:hidden;box-shadow:0 0 0 1px rgba(255,255,255,.6),0 0 16px rgba(86,134,148,.3)}
.chip video{filter:blur(10px)}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | A lush hero object on a calm, airy grid. Cohesive complementary palette. |
| Originality | 6 | It repeats the creator's own flower-in-glass formula (see insp-1-21), and orb heroes are widespread. |
| Usability | 5 | Grey footnotes fail AA, text sits on moving video, and copy is duplicated. |
| Craft | 8 | Convincing lens fringe, consistent radii and deliberate cropping. |

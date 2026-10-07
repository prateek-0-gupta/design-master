---
id: insp-1-3
source: inspora
category: Motion
status: analyzed
title: "Dither Motion"
creator: "@Oriku175"
styles: [dither-halftone, duotone, swiss-grid-poster, editorial-serif]
patterns: [poster-triptych, staggered-card-entrance, dithered-living-imagery, pixel-step-ornament, offset-tag-stack, numbered-process-list]
mode: light
palette: ["#f3f3f3", "#ffffff", "#0020e9", "#233fe8", "#435ce6", "#97a6ed", "#bdc6ef"]
type_families: ["Instrument Serif Italic (likely)", "Inter / Neue Haas-style grotesk (likely)"]
type_class: [editorial-serif, neo-grotesk]
radius_px: []
motion: {durations_s: [0.53, 0.87, 1.13, 0.77, 2.6, 1.23, 1.4, 0.7], easing: [ease-out, ease-in], loop: false}
scores: {aesthetics: 9, originality: 8, usability: 6, craft: 8}
craft_signals: [single-ink-duotone, two-square-pixel-step-motif, ruler-tick-edges, staircase-tag-stack, inverted-middle-poster, serif-italic-vs-grotesk-pairing]
anti_patterns: [micro-labels-too-small, video-not-looped]
---
# Dither Motion — @Oriku175

## 1. Snapshot
- **Subject:** A 1920×1084, 20.1 s showcase for the studio "Oriku": three portrait posters (white / cobalt / white) assembled one at a time. Each poster carries a dithered nature image (hummingbird with flower, two koi, chrysanthemum) that keeps moving.
- **Why it's remarkable:** It is a one-ink system. Pure ultramarine #0020e9 on white is used for type, blocks and 1-bit dithered photography, so the imagery reads like risograph print yet moves like video.

## 2. Composition & layout
- **Arrangement:** A triptych centred on #f3f3f3.
- **Poster sizes:** each ≈485×665 px (≈1:1.37, close to A-series 1:1.414). The middle poster is lifted ≈95 px higher (top y≈145 vs ≈238), which breaks the row into a gentle chevron. Gutters between posters are ≈38 px.
- **Inside each poster:**
  - a blue title block of ≈320×160 px anchored bottom-left (or top-left inverted on the centre poster);
  - a 3-line tagline column beside it;
  - a staircase of 3 tags ("Brand / Identity / Strategy") that step diagonally;
  - a 4-item numbered process list at a corner ("01 — Discover … 04 — Deliver");
  - a two-square pixel step (two ≈26 px squares touching at a corner).
- **Image placement:** imagery bleeds behind the tag stack, so type and picture interlock.

## 3. Typography
- **Wordmark "Oriku":** a high-contrast condensed italic serif at ≈50 px cap-to-baseline, close to Instrument Serif Italic.
- **Supporting text:** a neutral grotesk (Inter / Neue Haas-like) in Regular. Taglines are ≈16 px with ≈1.4 leading, and tags are ≈19 px in reversed white-on-blue or blue-on-white boxes.
- **Process list:** ≈8 px uppercase with wide tracking, which is decorative at this size.
- **Scale:** 50 / 19 / 16 / 8 px. The ratio between body and title is ~3×.
- **Pairing logic:** the serif carries brand voice and the grotesk carries information.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #f3f3f3 | stage background | 56% |
| #ffffff | poster paper, reversed type | 20% |
| #0020e9 | the ink: blocks, type, middle poster field | 13% |
| #233fe8 / #435ce6 / #687dea | dither mid-tones (anti-aliasing of 1-bit dots) | ~6% |
| #97a6ed / #bdc6ef | lightest dither speckle | ~3% |

WCAG checks:
- White on #0020e9: **8.81:1**.
- #0020e9 on the stage #f3f3f3: **7.94:1**.
- The lighter dither blue #435ce6 on white (small labels): 5.37:1.

Every text pair passes AA. The issue is size, not colour.

## 5. Depth & material
- **Shading:** flat print with no shadows; the posters separate from #f3f3f3 by value alone.
- **Paper edges:** fine ruler ticks run along the left and right edges of every poster (≈4 px marks every ≈6 px), like a printer's register strip, so each poster reads as a physical proof.
- **Images:** ordered or error-diffusion dither with visible pixel clusters of ≈3 px, which gives a tactile, printed grain.

## 6. Components & patterns
- **Poster as card:** each poster is a portfolio "service card" (branding / web / product). The ↗ arrow in the title block makes it a link.
- **Staircase tag stack:** boxes offset by one tag-height diagonally. It is a reusable, rhythmic way to list services.
- **Pixel-step motif:** two squares touching diagonally. It recurs at three positions and echoes the dither pixel.
- **Numbered process lists:** four steps per poster with different verbs per service.

## 7. Motion
- **Measured:** 20.07 s at 30 fps. motion_fraction 0.54, with 19 segments and a median of 0.70 s. seamless_loop_likely **false** (first/last diff 39.5) because it starts with one poster and ends with three.
- **Build phase (0–8 s):**
  - Segments at 2.57–3.70 s (1.13 s) and 4.00–4.77 s (0.77 s) peak early (0.28, 0.24), so they are **ease-out**. These match the 2nd and 3rd posters sliding in and the first shifting left: at 1.11 s there is one poster, at 3.34 s two, at 5.57 s three.
  - Segments 5.17–7.77 s (2.6 s, peak 0.03) and 7.87–9.10 s (1.23 s, peak 0.04) are strong front-loaded settles as the triptych re-centres and the middle poster rises.
- **Ambient phase (≈9–20 s):** shorter ease-in pulses (0.17–0.5 s, peaks 0.9+) recur roughly every 0.5 s. These are the dithered creatures animating: the hummingbird's wing pose, the koi rotating, and the flower opening and closing (compare the flower at 7.80 s and 10.03 s).

## 8. Brand system
n/a as a guideline document, though it effectively shows a studio identity kit:
- one-ink cobalt;
- serif-italic wordmark;
- pixel-step glyph;
- staircase tags;
- dithered nature photography;
- ruler-tick edges.

All of these are portable to the web, social posts and print.

## 9. UX
- **Strength:** The posters are scannable. Name, value prop and service tags are legible, and the arrow signals action.
- **Risks:**
  - The 8 px process lists fail practical legibility.
  - Motion inside every card at once competes for attention.
  - As a website hero, three animating dithers would need `prefers-reduced-motion` handling.

## 10. Craft signals
- The whole piece uses exactly one chromatic ink (#0020e9). All other blues are dither anti-aliasing.
- The two-square diagonal pixel step appears at a consistent ≈26 px module on all three posters.
- Ruler ticks run along both vertical edges of each poster.
- The centre poster inverts the scheme (blue field, white title box) and is raised ≈95 px.
- The tag staircase offsets are exactly one tag-height.
- The serif is used only for "Oriku" and never for body text.

## 11. Reproduction recipe
```css
:root{--ink:#0020e9;--paper:#fff;--stage:#f3f3f3;--serif:"Instrument Serif",serif;--sans:"Inter",system-ui;}
.poster{width:485px;aspect-ratio:1/1.37;background:var(--paper);position:relative;
  background-image:repeating-linear-gradient(0deg,#cfd6f7 0 1px,transparent 1px 6px);
  background-size:4px 100%;background-repeat:repeat-y;background-position:0 0, right 0 top 0}
.poster--inv{background-color:var(--ink);color:var(--paper);translate:0 -95px}
.title{background:var(--ink);color:#fff;padding:20px 14px}
.title h2{font:italic 400 52px/1 var(--serif);margin:0}
.tag{display:inline-block;background:var(--ink);color:#fff;font:400 19px/1 var(--sans);padding:6px 10px}
.pixel{width:26px;height:26px;background:var(--ink);box-shadow:26px 26px 0 var(--ink)}
.dither{image-rendering:pixelated;filter:grayscale(1) contrast(4);mix-blend-mode:multiply}
@keyframes enter{from{opacity:0;translate:60px 0}to{opacity:1;translate:0}}
.poster{animation:enter 1.1s cubic-bezier(.16,1,.3,1) both}
.poster:nth-child(2){animation-delay:2.4s}.poster:nth-child(3){animation-delay:4s}
```
(Real dither: render to canvas with Bayer 4×4 thresholding and colourize to #0020e9.)

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 9 | Disciplined one-ink system, a beautiful serif/grotesk contrast, and print-like grain. |
| Originality | 8 | Animated dither inside print-style posters is fresh; the cobalt-mono trend itself is known. |
| Usability | 6 | Main copy is clear, but micro lists are illegible and constant motion competes. |
| Craft | 8 | Consistent pixel module, register ticks, inversion logic. |

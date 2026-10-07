---
id: insp-4-8
source: inspora
category: Branding
status: analyzed
title: "Brand work"
creator: "@shihaabbbb"
styles: [dark-premium, dither-halftone, terminal-mono, monochrome]
patterns: [dithered-classical-statue-imagery, mono-eyebrow-with-square-bullet, boxed-tag-chips, sans-headline-mono-body, code-window-over-image, card-trio-grid, pixel-logomark]
mode: dark
palette: ["#0a0a0a", "#000000", "#211f1f", "#2d2d2d", "#ffffff", "#cac9c9", "#adacac", "#555555"]
type_families: ["Neue Montreal / Aeonik-style grotesk (likely)", "IBM Plex Mono / Courier-like mono (likely)"]
type_class: [neo-grotesk, mono]
radius_px: [12, 24, 4]
motion: null
scores: {aesthetics: 8, originality: 6, usability: 7, craft: 6}
craft_signals: [tight-negative-tracking-headlines, square-bullet-eyebrow-system, two-chip-styles-filled-vs-outline, dither-dot-pitch-consistent, single-white-surface-for-code, achromatic-only-palette]
anti_patterns: [copy-typos, repeated-body-copy-across-cards, dither-detail-lost-at-small-size]
---
# Brand work — @shihaabbbb

## 1. Snapshot
- **Subject:** Four slides of an identity for an AI-agent infrastructure product:
  - a dithered statue face with a pixel-bracket logomark (1081×608);
  - two portrait cards (2048×1156);
  - a three-card feature grid (2048×1152);
  - a hero with a white code window over dithered imagery (2048×1114).
- **Why it's remarkable:** A strictly achromatic system that pairs classical sculpture (rendered as 1-bit dither) with terminal mono and a tight grotesk. "Ancient intelligence meets machine" is told through texture alone.

## 2. Composition & layout
- **Slide 1:** Full-bleed dithered bust on black. The logomark is eight white rectangles forming a pixel ring, about 200×190 px, centred over the face's eye area.
- **Slide 2:** Two cards about 645×845 px with about 12 px radius on #211f1f, separated by a 55 px gutter. Each stacks:
  - eyebrow at y+48;
  - headline, two lines;
  - tag chip;
  - image at 16:9;
  - three-line mono body.
  - The internal margin is about 26 px.
- **Slide 3:** Hero headline top-left with a mono intro top-right (an asymmetric two-column header). Below it, three columns about 550 px wide with 58 px gutters, each holding chips, an image, a title, body text and a chip.
- **Slide 4:** Split layout of about 40/60: copy on the left; on the right a dithered image of about 950×795 px with a white code card of about 740×590 px (radius about 24 px) inset, overlapping its top-right.

## 3. Typography
- **Headlines:**
  - A geometric-leaning grotesk, close to Neue Montreal or Aeonik.
  - About 85 px on slide 2 and about 75 px on slide 4, all lowercase or sentence case.
  - Tracking is about −0.05 em and leading about 0.95. Letters nearly touch ("models to will"), which is the signature look.
- **Card titles:** about 40 px Title Case, same face.
- **Mono:** Body, eyebrows, chips and code are a typewriter-ish mono (Plex Mono-like).
  - Eyebrows are about 24 px uppercase, prefixed by a 10 px square bullet.
  - Body is about 22 px with leading of about 1.5.
- **Scale (slide 3):** 75 / 40 / 24 / 18 px. The jump from display to title is about 1.9×.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #0a0a0a / #000000 | page ground | 57–76% |
| #211f1f / #2d2d2d | card surface | 25% (slide 2) |
| #ffffff | headlines, filled chips, code window | 16% (slide 4) |
| #cac9c9 / #adacac | mono body text | ~2% |
| #555555 / #9b9b9b | dither mid-tones | 10% |

WCAG checks:
- Headline #f2f2f2 on card #211f1f: 14.65:1.
- Body #cac9c9 on card: 9.93:1.
- Body #adacac on #0a0a0a: 8.74:1.
- Code #3a3a3a on white: 11.37:1.

Everything passes AA comfortably. The palette is zero-chroma by design.

## 5. Depth & material
- **Surfaces:** Flat surfaces with a single elevation step (#0a0a0a → #211f1f) and no shadows.
- **Dither:** The imagery is ordered/Bayer-style dithering with an about 6 px dot pitch at 2048 px, in two tones plus grey.
- **Code window:** pure white, the only bright surface, with a traffic-light row of three grey squares instead of circles. The squares echo the bullet glyph.

## 6. Components & patterns
- **Eyebrow:** a square bullet plus an uppercase mono label ("BUILD ANYTHING").
- **Chips:**
  - filled white with black text ("PRODUCT", "BUILD AND RUN AGENTS"), radius about 4 px;
  - outlined, with a 1 px #555 border and light text ("NEW AI TOOLS").
- **Feature card:** chip row → dithered image → title → mono body → chip.
- **Code card:** with a black pill "RUN" button (radius about 14 px).
- **Bullet list:** square bullets with uppercase mono, about 28 px.

## 7. Motion
Still images, so no motion was observed. The dither suggests a resolve-in transition (image appears as coarse dots that refine, 0.6–0.8 s, ease-out) and a typing effect for the code card.

## 8. Brand system
These are partial brand-application slides. Identity elements:
- **Logomark:** an eight-segment pixel ring.
- **Image style:** 1-bit dither of classical busts.
- **Type pair:** a tight grotesk for statements plus mono for system voice.
- **Graphic unit:** the square as the atomic shape (bullets, window dots, logomark segments).
- **Voice:** short, confident lines ("Not your usual machine brain", "Code that thinks back").

## 9. UX
- **Strengths:** High contrast throughout and clear hierarchy.
- **Weaknesses:**
  - Identical body copy repeats across cards (slides 2 and 3), so placeholder text leaked into the presentation.
  - There are typos: "agentsa", "beyondone-off", "build,and", "it keep".
  - The dither images lose the face at thumbnail size (slide 3, right card).

## 10. Craft signals
- The square motif is consistent across the bullet, window controls and logomark.
- Headline tracking of about −0.05 em at display size and about −0.02 em at the 40 px titles: tracking is scaled with size.
- Two chip variants only (filled and outline) on a 4 px radius.
- The dither dot pitch is the same in every image.
- The code window is the only white surface, so it becomes the focal point on slide 4.

## 11. Reproduction recipe
```css
:root{--bg:#0a0a0a;--card:#211f1f;--fg:#f2f2f2;--fg-2:#cac9c9;--line:#555;--paper:#fff;
  --sans:"Neue Montreal","Aeonik","Inter",sans-serif;--mono:"IBM Plex Mono",ui-monospace,monospace}
body{background:var(--bg);color:var(--fg)}
.h-display{font:500 clamp(48px,6vw,88px)/.95 var(--sans);letter-spacing:-.05em}
.eyebrow{font:400 14px/1 var(--mono);text-transform:uppercase;letter-spacing:.02em}
.eyebrow::before{content:"";display:inline-block;width:.45em;height:.45em;background:currentColor;margin-right:.5em;vertical-align:.1em}
.chip{font:400 12px/1 var(--mono);text-transform:uppercase;padding:6px 8px;border-radius:4px;background:var(--paper);color:#111}
.chip--ghost{background:transparent;color:var(--fg);border:1px solid var(--line)}
.card{background:var(--card);border-radius:12px;padding:26px}
.body{font:400 15px/1.5 var(--mono);color:var(--fg-2)}
.dither{image-rendering:pixelated;filter:grayscale(1) contrast(1.4)} /* pre-process with Bayer 8×8 */
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Moody, cohesive black-and-white with strong typographic tension. |
| Originality | 6 | Dithered statues plus mono is a recognisable AI-brand trope in 2025–26. |
| Usability | 7 | Excellent contrast and hierarchy, but copy is repeated. |
| Craft | 6 | The motif system is tight, but typos and placeholder repetition undercut it. |

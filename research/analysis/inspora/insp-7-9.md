---
id: insp-7-9
source: inspora
category: Motion
status: analyzed
title: "Notification Cards"
creator: "@its_sslvr"
styles: [aurora-glow, playful-rounded, micro-interaction, corporate-clean]
patterns: [now-playing-pill, flowing-gradient-right-half, equaliser-glyph, dark-light-variant-stack, caps-title-with-asterisk]
mode: light
palette: ["#edeef3", "#ffffff", "#202022", "#7d7c7b", "#e6d9cd", "#beb4af", "#564944"]
type_families: ["Inter (likely)"]
type_class: [neo-grotesk]
radius_px: [9999]
motion: {durations_s: [12.72], easing: [linear], loop: true}
scores: {aesthetics: 8, originality: 7, usability: 6, craft: 7}
craft_signals: [gradient-confined-to-right-half, gradient-hue-matches-equaliser-colour, chromatic-aberration-edge-on-dark-variant, soft-ambient-shadow-on-light-canvas, uppercase-two-line-label]
anti_patterns: [subtitle-below-4.5-to-1, white-pill-on-near-white-canvas-1.16-to-1]
---
# Notification Cards — @its_sslvr

## 1. Snapshot
- **Subject:** A 12.7 s, 3840×2160 loop of three stacked pill-shaped "now playing" notifications. One is dark (OUTER.OR*, podcast) and two are light (MATCHA.TV, SAND.SURF*). Each has a slow, blurred, flowing gradient smear in its right half.
- **Why it's remarkable:** Each pill's ambient gradient acts as a mood colour per source: prismatic for the podcast, matcha green/peach for the series, sand/beige for the mix. A tiny equaliser glyph in the matching hue ties text and light together.

## 2. Composition & layout
- **Stack:** three pills about 1375×357 px (radius 9999) stacked with about 138 px gaps and centred on #edeef3. Together they take about 52% of the frame height.
- **Pill content:** left-aligned at about 110 px inner padding, as a two-line block:
  - title about 69 px;
  - subtitle about 42 px plus an equaliser glyph.
- **Gradient zone:** The right ~55% of every pill is the gradient field, blurred heavily into the base colour. The text never overlaps the brightest part.

## 3. Typography
- **Typeface:** Inter, recognisable from the "R", "S" and "2" and the flat terminals.
- **Titles:** uppercase Bold (700), about 69 px, tracking about −0.01 em. The brand-like names use a "." separator and a trailing "*" asterisk ("OUTER.OR*", "SAND.SURF*"), which reads as a nod to streetwear/label branding.
- **Subtitles:** uppercase Semibold, about 42 px, #7d7c7b, tracking about +0.02 em.
- The single family is used in two weights, with a ratio of about 1.64 between title and subtitle.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #edeef3 | canvas (cool off-white) | 83% |
| #ffffff | light pill surface | 6% |
| #202022 | dark pill surface, titles on light pills | 3.3% |
| #7d7c7b | subtitles | 1.1% |
| #e6d9cd / #beb4af / #564944 | sand gradient, shadows | 3% |
| #2dd4a0 (est.) | equaliser on dark pill | <0.2% |
| #e8935a (est.) | equaliser on light pill (matcha) | <0.2% |

WCAG checks:
- White on #202022 is 16.26:1, and #202022 on white the same.
- Subtitle #7d7c7b is **4.17:1 on white and 3.90:1 on #202022**. Both pass only as large text; at about 21 CSS px semibold they qualify as borderline large.
- The orange equaliser on white is 2.4:1 (decorative). The teal equaliser on dark is 8.55:1.
- The white pill on the canvas is 1.16:1; only its shadow separates them.

## 5. Depth & material
- **Light pills:** a very soft, wide shadow (about 60–80 px blur, roughly 6% black, slightly cool) that floats them on the near-white ground.
- **Dark pill:** a deeper shadow (about 10% black).
- **Gradient field:** looks like a heavily blurred (about 40 px) moving image or shader of light streaks. On the dark pill it has visible chromatic-aberration fringes (blue/orange edges, key frame), like light refracted through glass.
- There is no border or stroke on any pill.

## 6. Components & patterns
- **Now-playing / notification pill:** a source name, a content type, and a live equaliser indicating playback. In context these would stack in a lock-screen or Dynamic-Island-style list.
- **Variants:** dark (active or priority?) and light. It is not shown whether dark means "currently playing". The equaliser appears on all three, so the active state is ambiguous.

## 7. Motion
Measured (m0_motion.json, 60 fps, 12.72 s, motion_fraction 0.0, mean energy 0.07, p95 0.11, seamless_loop_likely true, first/last diff 0.12):
- No discrete segments were found. All motion is continuous, slow and low-amplitude: the gradient smears drift and morph across the right half of each pill.
- From frames 1.41 s apart (estimates):
  - The dark pill's light streak sweeps from an upper chevron (0.71–3.53 s) to a lower arc (4.95–6.36 s), then concentrates at the right cap (7.78–10.60 s) before returning.
  - That is a full cycle of about 12.7 s, linear and loop-matched.
- The equaliser bars change height between frames, at roughly 2–4 updates per second.
- The pills themselves never move, so the motion reads as ambient life, not as an alert.

## 8. Brand system
n/a — this is a UI component, not a brand system. Identity cues: per-source "mood light", and caps-plus-asterisk naming.

## 9. UX
- The motion is calm and non-urgent, and the right-side placement keeps text legible.
- The colour-per-source mapping could help recognition at a glance.
- **Risks:**
  - The grey subtitles sit below 4.5:1.
  - No actions (play/pause, dismiss) are visible, so as notifications they are not actionable.
  - Ambient animation across many notifications can become noisy; limit it to the active one.

## 10. Craft signals
- The gradient is masked to start about 45% across each pill, with a long feather. The text zone stays on the flat base colour.
- The equaliser colour equals the dominant hue of that pill's gradient (teal-prism, peach-green, tan).
- Chromatic fringing appears only on the dark variant, where it reads as glass. Light variants stay soft.
- The pill radius is a true full-round at 357 px height. Vertical padding equals about 1.7× the title cap height.
- The 12.7 s loop is seamless.

## 11. Reproduction recipe
```css
:root{--canvas:#edeef3;--light:#fff;--dark:#202022;--sub:#6e6d6c;--font:"Inter",system-ui}
.np{position:relative;overflow:hidden;width:360px;height:94px;border-radius:9999px;padding:0 28px;
  display:flex;flex-direction:column;justify-content:center;background:var(--light);
  box-shadow:0 18px 40px rgba(30,35,60,.07);font-family:var(--font)}
.np.dark{background:var(--dark);color:#fff;box-shadow:0 18px 40px rgba(0,0,0,.12)}
.np b{font:700 18px/1.1 var(--font);text-transform:uppercase;letter-spacing:-.01em}
.np small{font:600 11px/1.4 var(--font);text-transform:uppercase;letter-spacing:.02em;color:var(--sub)}
.np::after{content:"";position:absolute;inset:-20% -10% -20% 45%;filter:blur(24px);
  background:conic-gradient(from var(--a,0deg),#f2c9a0,#cfe8c4,#fff,#e9d6c3,#f2c9a0);
  -webkit-mask:linear-gradient(90deg,transparent,#000 35%);mask:linear-gradient(90deg,transparent,#000 35%);
  animation:drift 12.7s linear infinite}
@property --a{syntax:"<angle>";inherits:false;initial-value:0deg}
@keyframes drift{to{--a:360deg}}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Soft, premium, well-balanced; dark/light pairing adds rhythm. |
| Originality | 7 | Ambient gradient pills are known; colour-coded mood light per source is a nice twist. |
| Usability | 6 | Readable titles, but faint subtitles, unclear active state, no actions. |
| Craft | 7 | Clean masking and colour matching; light pills nearly vanish into canvas. |

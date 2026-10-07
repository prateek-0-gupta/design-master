---
id: insp-1-23
source: inspora
category: Motion
status: analyzed
title: "We're making Grok Bot more widely available."
creator: "@Grok Bot"
styles: [flat-illustration, playful-rounded, organic-blob, minimal-swiss]
patterns: [mascot-character-system, shape-morph-transitions, character-stack-reveal, logo-lockup-end-card, zoom-through-transition]
mode: light
palette: ["#ffffff", "#000000", "#3b3b3b", "#1a88f7", "#f49807", "#e54104", "#11d2a5", "#767675"]
type_families: ["Universal Sans / Inter-style neo-grotesk (likely)"]
type_class: [neo-grotesk]
radius_px: [9999]
motion: {durations_s: [0.2, 0.5, 1.37, 0.13], easing: [ease-out, ease-in-out], loop: false}
scores: {aesthetics: 8, originality: 7, usability: 8, craft: 8}
craft_signals: [two-pill-eyes-identity, eye-gesture-squash, colour-per-character-tier, logo-dot-inherits-eye-glint, flat-fills-only]
anti_patterns: [white-eyes-on-orange-low-contrast]
---
# We're making Grok Bot more widely available. — @Grok Bot

## 1. Snapshot
- **Subject:** A 1920×1080, 12.4 s announcement animation. A black circle mascot with two white pill eyes blinks, zooms through red and teal cloud-blobs, and stacks into a totem of five characters (grey cloud, blue drop, orange circle, black bean, grey ghost). The caption reads "Grok Bot, now on more plans". It resolves to a "● Grok" → "◕ Grok Bot" logo lockup.
- **Why it's remarkable:** A whole character family is built from one rule, "flat silhouette + two pill eyes". Each silhouette and colour probably maps to a plan or tier, and the stack visually says "more plans".

## 2. Composition & layout
- **Open:** white canvas with the black circle (about 360 px in diameter at 1080 p) centred-left. Two pill eyes, about 30×90 px, tilt slightly. At t=2.07 s the eyes grow and squash (an expression).
- **Zoom-through:** at t=3.45 s the frame fills with an orange-red #e54104 cloud and a teal #11d2a5 cloud with horizontal-pill eyes, a transition by scale.
- **Stack:** five characters, each about 130–180 px, stacked diagonally, bottom-centre to right (key frame x≈960→1330, y≈590→1080). They are cropped at the bottom edge, as if rising into view.
- **Caption:** "Grok Bot, now on more plans", about 46 px, centred above the stack at y≈555 (1080 p scale).
- **End card:** dot + wordmark centred, with the dot at about 70 px and the wordmark about 70 px tall in a bold weight.

## 3. Typography
- A neo-grotesk sans (Inter or Universal Sans-like).
  - Caption: regular, about 46 px, black, sentence case.
  - Wordmark: "Grok" then "Grok Bot", bold, about 72 px, tracking about −0.02 em.
- The mascot dot sits left of the wordmark at cap height, with about 0.5 em spacing. In the final frame the dot gains an eye glint (◕), which ties the logo to the mascot.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #ffffff | canvas | 97% |
| #000000 | primary mascot, text | 0.4% |
| #3b3b3b | cloud character (dark grey) | 0.8% |
| #1a88f7 | blue drop character | 0.4% |
| #f49807 | orange circle character | 0.4% |
| #767675 | grey ghost character | 0.2% |
| #e54104 / #11d2a5 | transition clouds (frame at 3.45 s) | — |

WCAG checks:
- Black text on white: 21:1.
- White eyes on the blue drop #1a88f7: 3.55:1.
- White eyes on orange #f49807: 2.25:1 (graphic, but the orange character's eyes are the faintest).

## 5. Depth & material
Completely flat: no shadows, gradients or outlines. Characters overlap without separation strokes, so depth is only stacking order.

## 6. Components & patterns
- **Mascot system:** silhouettes include a circle, a 4-lobed cloud, a teardrop, a bean and a ghost. The constant is two white rounded-pill eyes, angled per character.
- The eyes act as expression rigs: they stretch vertically (surprise), rotate to horizontal (teal cloud) and become round ovals (blue drop).
- Logo lockup with the mascot as the logomark.

## 7. Motion
- **Measured:** 12.43 s at 30 fps, `motion_fraction` 0.18 (mostly holds), 4 segments:
  - 2.37–2.57 s (0.20 s, `peak_at` 0.25, ease-out): eye squash or blink.
  - 2.77–3.27 s (0.50 s, `peak_at` 0.10, ease-out): fast zoom into the clouds.
  - 3.57–4.93 s (1.37 s, symmetric ease-in-out): the stack rises and sways in.
  - 9.20–9.33 s (0.13 s, ease-in): a quick cut to the logo.
- **Character:** snappy ease-out for expressions and zooms (fast start, soft land). Holds of 3–4 s give time to read the caption and logo.
- The stack sways or tilts between frames at t=4.84 and 6.22 s, a wobbly "jelly tower" settle.

## 8. Brand system
Not a full brand system, but strong identity cues:
- **Logomark:** a black circle with the eye glint.
- **Character family:** shape and colour per member (black, dark grey, blue #1a88f7, orange #f49807, grey).
- **Type and voice:** a bold neo-grotesk wordmark and a friendly, lowercase-adjacent voice ("now on more plans").

Rule worth stealing: one invariant feature (pill eyes) lets you vary silhouette and colour freely while staying on-brand.

## 9. UX
- The message is clear and short, and the caption appears only once the characters settle.
- Works without sound.
- The end card holds about 2 s with the full name, which is good for recall.

## 10. Craft signals
- The eye pills share the same width-to-length ratio (about 1:3) across all characters.
- The logo dot transforms into the mascot with an eye glint at the end, closing the loop.
- Flat colour only: five hues plus black on white, with no tints.
- The stack is cropped at the bottom edge, implying more characters below.
- Hard cut to the logo (0.13 s) after soft character motion gives a crisp punctuation.

## 11. Reproduction recipe
```css
:root{--ink:#000;--bg:#fff;--c-grey:#3b3b3b;--c-blue:#1a88f7;--c-orange:#f49807;--c-red:#e54104;--c-teal:#11d2a5}
.bot{width:180px;aspect-ratio:1;border-radius:50%;background:var(--ink);position:relative}
.bot .eye{position:absolute;top:30%;width:11%;height:32%;border-radius:9999px;background:#fff;transform:rotate(8deg)}
.bot .eye:first-child{left:34%}.bot .eye:last-child{left:56%}
@keyframes squash{0%{transform:scaleY(1)}40%{transform:scaleY(1.35) scaleX(1.2)}100%{transform:scaleY(1)}}
.bot:hover .eye{animation:squash .2s cubic-bezier(.16,1,.3,1)}
.lockup{display:flex;align-items:center;gap:.4em;font:700 72px/1 "Inter",sans-serif;letter-spacing:-.02em}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Bold flat shapes, crisp white space and a cheerful palette. |
| Originality | 7 | Eyes-on-blobs mascots are common, but the tier stack is a nice idea. |
| Usability | 8 | The message is clear in about 12 s; readable caption and logo. |
| Craft | 8 | Consistent eye rig, a logo/mascot tie-in, and good timing contrast. |

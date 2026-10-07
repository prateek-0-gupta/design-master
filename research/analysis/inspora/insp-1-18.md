---
id: insp-1-18
source: inspora
category: Web
status: analyzed
title: "waitlist screen"
creator: "@nachidesigner"
styles: [maximalist-color, soft-3d, technical-wireframe]
patterns: [waitlist-hero, inline-email-pill-form, blurred-countdown-numerals, selection-box-on-word, construction-grid-overlay, social-proof-counter]
mode: mixed
palette: ["#02aeff", "#018cff", "#1587fd", "#ffffff", "#a9d5fb", "#d4effd", "#70bdfb"]
type_families: ["SF Pro Rounded / SF Pro Display (likely)"]
type_class: [neo-grotesk, rounded-sans]
radius_px: [9999, 40, 56]
motion: null
scores: {aesthetics: 8, originality: 7, usability: 5, craft: 8}
craft_signals: [inner-gradient-on-headline-letters, figma-selection-handles-on-italic-word, blurred-depth-countdown, frosted-outer-bezel, construction-circles-in-background, traffic-light-dots-as-eyebrow]
anti_patterns: [white-text-on-cyan-fails-aa, low-contrast-social-proof, countdown-legibility-sacrificed]
---
# waitlist screen — @nachidesigner

## 1. Snapshot
- **Subject:** A single 2560×1733 still of a waitlist hero for "freedrw", a design-to-code tool. It is a saturated blue gradient card with a centred headline, an email pill and a giant blurred countdown bleeding off the bottom.
- **Why it's remarkable:** The page performs its product idea. The word "it's" sits inside a Figma-style selection box (corner handles and a rotate glyph, tilted about −8°), and a faint construction grid of circles and diagonals sits behind everything like a design canvas.

## 2. Composition & layout
- **Frame:** The page is a card about 2220×1395 px (x 170→2390) with a radius of about 56 px. A light-blue frosted bezel of about 14 px wraps it, set on white.
- **Grid:** A 4-column construction grid (vertical lines at about 25/50/75%) plus concentric circles centred on the form. Both are drawn as about 1 px lines at about 8% white.
- **Centred stack:**
  - eyebrow dots at y≈490;
  - two-line headline (y≈540–820);
  - email pill about 740×92 px at y≈870;
  - social proof "1,288 people already joined" at y≈1055.
- **Bottom band:** The countdown "03:10:35" is about 290 px tall, cropped by the card bottom edge, with "days / hours / min" labels aligned to the column lines.
- **Nav:** a minimal wordmark at top-left, and About / FAQs at top-right at about 28 px.

## 3. Typography
- One family throughout: a neo-grotesk with rounded terminals, reading as SF Pro Display with SF Pro Rounded for the numerals.
- **Headline:** about 140 px in the original (about 1.0 leading, −0.03 em tracking), heavy (700–800).
- **Emphasis word:** "it's" is the only italic, and the selection box frames it.
- **Form and labels:** The form placeholder and button are about 28 px regular/medium. Labels "days/hours/min" are about 22 px at 50% white.
- **Countdown:** rounded heavy numerals, Gaussian-blurred by about 8 px, used as atmospheric texture rather than readable data.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #02aeff | top of card gradient (cyan) | 26.7% |
| #018cff / #1587fd | bottom of card gradient (azure) | 32% |
| #ffffff | page surround, headline, button | 27.5% |
| #a9d5fb / #d4effd | frosted bezel, headline inner shade | 6% |
| #70bdfb / #439ffc | email field fill, countdown glow | 6% |
| red / grey / navy dots | eyebrow "traffic light" | <0.5% |

WCAG checks:
- White on the top cyan #02aeff is 2.47:1 and fails even for large text.
- White on the bottom azure #018cff is 3.39:1 (large text only).
- The social-proof line (≈#70bdfb on #018cff) is 1.67:1.
- Dark button text (≈#333) on the white button is 12.6:1.

So the only fully accessible element is the CTA.

## 5. Depth & material
- **Headline letters:** each letter has a vertical white → #d4effd inner gradient and a soft blue drop shadow (about 0 6px 12px). This gives a slightly inflated, soft-3d look.
- **Email pill:** a translucent lighter-blue fill (#70bdfb-ish at about 60%) with a white inner button that is raised with a subtle shadow. The custom pink-outlined cursor rests on it.
- **Countdown:** depth of field. Blurred numerals sit "behind" the plane, with a soft glow.
- **Outer bezel:** reads as frosted glass framing a screen.

## 6. Components & patterns
- **Inline email + submit pill:** the button is nested inside the field, with 4 px padding.
- **Social-proof counter** under the form.
- **Countdown timer** as a background graphic.
- **Editor-UI quotation:** selection handles (4 white squares at the corners plus a rotation arrow) and one vertical guide line that drops from the top edge to the box.
- **Three coloured dots:** a mac-window-control nod used as an eyebrow.

## 7. Motion
Still image, so no motion was observed. The design implies a ticking countdown, possibly a blur-in per digit, and a draggable selection box. These are not visible here.

## 8. Brand system
n/a — not a brand system. Identity cues:
- the lowercase "freedrw" wordmark;
- design-tool iconography (selection box, guides, construction circles) as the brand language;
- the single-hue blue world.

## 9. UX
- The single action is obvious and the CTA has high contrast.
- **Risks:**
  - Almost every white-on-cyan text element fails AA, including nav links and the placeholder.
  - The countdown is deliberately unreadable at the bottom, which conflicts with its function as urgency information.
  - The email placeholder at about 60% white on light blue is faint.

## 10. Craft signals
- The selection box is rotated to match the italic's lean, and its guide line aligns with a background column line.
- The countdown labels "days/hours/min" sit exactly on the three construction-grid columns.
- The concentric circles are centred on the email field, so the composition radiates from the CTA.
- The headline's per-letter gradient plus blue shadow gives it volume without a heavy 3D render.
- The frosted bezel radius (about 70 px) stays concentric with the inner card (about 56 px).

## 11. Reproduction recipe
```css
:root{--cyan:#02aeff;--azure:#018cff;--ice:#d4effd;--mist:#70bdfb;--bezel:#a9d5fb;}
.card{border-radius:56px;background:linear-gradient(180deg,var(--cyan),var(--azure));
  outline:14px solid color-mix(in srgb,var(--bezel) 70%,transparent);outline-offset:0;
  background-image:
    radial-gradient(circle at 50% 52%,transparent 0 220px,rgba(255,255,255,.08) 221px 222px,transparent 223px),
    linear-gradient(90deg,transparent calc(25% - 1px),rgba(255,255,255,.08) 0 25%,transparent 0),
    linear-gradient(180deg,var(--cyan),var(--azure));}
h1{font:800 140px/1 "SF Pro Display",system-ui;letter-spacing:-.03em;
  background:linear-gradient(#fff 40%,var(--ice));-webkit-background-clip:text;color:transparent;
  filter:drop-shadow(0 6px 12px rgba(0,60,160,.25))}
.sel{outline:2px solid #fff;transform:rotate(-8deg);position:relative}
.form{display:flex;border-radius:9999px;background:rgba(255,255,255,.3);padding:4px}
.form button{border-radius:9999px;background:#fff;color:#333;font-weight:500}
.count{font:800 290px/1 "SF Pro Rounded";color:rgba(255,255,255,.35);filter:blur(8px)}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | A bold, joyful mono-hue scene with soft-3d type. Cohesive. |
| Originality | 7 | The selection-box-on-word and construction grid are a smart nod to the product, inside a familiar waitlist template. |
| Usability | 5 | The CTA is clear, but most text fails contrast and the countdown is illegible by design. |
| Craft | 8 | Grid alignments, concentric radii and letter shading are carefully done. |

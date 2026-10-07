---
id: insp-2-6
source: inspora
category: Illustration
status: analyzed
title: "e-signature field"
creator: "@adrianabelarde_"
styles: [skeuomorphic, physical-material, micro-interaction, corporate-clean]
patterns: [toy-as-input-field, shake-to-erase, knob-and-pointer-drawing, cta-gated-by-signature, success-sticker-stamp, inline-hint-row]
mode: light
palette: ["#ffffff", "#f2f2f2", "#cd2429", "#a40d12", "#c4c5c9", "#2e2f33", "#1c1c1e", "#34c759"]
type_families: ["Inter (likely)"]
type_class: [neo-grotesk]
radius_px: [9999, 40, 120, 24]
motion: {durations_s: [0.23, 0.2, 1.37, 0.5, 0.43, 0.27], easing: [ease-out, ease-in-out], loop: false}
scores: {aesthetics: 8, originality: 9, usability: 7, craft: 9}
craft_signals: [aluminium-powder-speckle-on-glass, knurled-knob-edges, direction-arrows-above-knobs, disabled-cta-copy-explains-why, dotted-underline-for-actions, deadpan-microcopy-footer]
anti_patterns: [white-on-green-success-fails, faint-footer-text, trademark-borrowed]
---
# e-signature field — @adrianabelarde_

## 1. Snapshot
- **Subject:** A 24.7 s, 1920×1920 demo of a job-offer signing page where the signature pad is a photoreal Etch A Sketch.
- **Interactions:**
  - The user draws on the glass or turns the knobs.
  - Shaking erases the signature.
  - The "Accept Offer" button disables to "Sign above to accept" when the pad is empty.
  - Accepting turns the button green and slaps a "HIRED" sticker on the toy.
- **Why it's remarkable:** The joke is fully implemented as a real form pattern: required field, validation state, erase, confirm. Each toy behaviour maps onto a standard e-sign affordance.

## 2. Composition & layout
- A white document card (radius ~40 px, soft shadow) on #f2f2f2 holds, from top to bottom:
  - the end of the contract text ("written above.");
  - the field label "Signature of Employee *" left and "Date: July 12, 2026" right, at ~28 px;
  - the toy (~980×900 px at the key frame) centred;
  - a hint row ("Draw on the glass · or turn the knobs · Shake to erase · Sound on");
  - the CTA pill;
  - the footer disclaimer.
- During drawing, the camera zooms in so the toy fills ~70% of the frame and the page blurs behind it.
- **Toy anatomy:**
  - red frame (corner radius ~120 px at the top, flatter at the bottom);
  - inset grey screen (~640×460 px, radius ~24 px);
  - two ~220 px white knurled knobs at the bottom corners, with ◀▶ and ▲▼ hints above them;
  - the yellow script logo centred.

## 3. Typography
- Inter-like neo-grotesk throughout:
  - body ~32 px Regular;
  - label ~28 px Medium #6e6e70 with a red asterisk;
  - hints ~30 px #858586, with action words given a 2 px dotted underline;
  - CTA ~34 px Medium white on near-black;
  - footer ~24 px #a3a3a4.
- The signature is a continuous single-weight line (~8 px stroke), the way an Etch A Sketch draws.
- The toy logo is the trademark yellow script with a dark outline.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #ffffff / #f2f2f2 | card / page | 63% / 9.5% |
| #cd2429 → #a40d12 | toy red, light top → shaded bottom | ~9% |
| #61171b | deepest red shadow (screen bezel) | 1.7% |
| #c4c5c9 / #babbbe | aluminium screen | 6% |
| #2e2f33 | drawn line | — |
| #1c1c1e | primary CTA | — |
| #34c759 | success CTA ("Offer accepted ✓") | — |

WCAG:
- CTA white on #1c1c1e is 17.01:1.
- Label #6e6e70 is 5.09:1.
- Date and hints (#8a8a8a) are 3.45:1 (large only).
- Footer #a3a3a4 is **2.52:1 (fails)**.
- Ink on screen is 7.75:1.
- Success white on #34c759 is **2.22:1 (fails)**.

## 5. Depth & material
- **Frame:** glossy injection-moulded plastic. A broad specular highlight sits on the upper-left shoulder, the red deepens toward the bottom, and a dark inner bevel surrounds the screen.
- **Screen:** matte grey with fine white speckle noise (aluminium powder) and an inner shadow at the top edge.
- **Knobs:** white with radial knurling (~60 ribs), soft inner shading and a contact shadow on the frame.
- **Toy shadow:** a large soft shadow (~60 px blur) onto the card, plus a coloured red bounce.

## 6. Components & patterns
- **Signature field states:**
  - empty, with the CTA disabled ("Sign above to accept", grey pill #e8e8ec);
  - signed, with the CTA enabled ("Accept Offer", black);
  - accepted, with the CTA green plus a check, and a "HIRED" die-cut sticker tilted about 8° on the frame.
- **Erase:** the "Shake to erase" link (or physical shake) wipes the screen.
- **Two input modes:** pointer drawing on the glass (crosshair cursor) or knob control (the hand cursor rotates the knob).
- **Inline hint row:** the dotted underline distinguishes actions from descriptions.

## 7. Motion
Measured: 30 fps, duration 24.67 s, motion_fraction 0.13, 7 segments, median 0.27 s, not a seamless loop.
- Zoom-in and zoom-out camera cuts are fast ease-out:
  - 0.73–0.97 s (0.23 s, peak 0.07);
  - 11.63–11.83 s (0.20 s);
  - 17.50–17.70 s;
  - 21.53–21.80 s (0.27 s).
- **13.10–14.47 s (1.37 s, symmetric ease-in-out):** the shake-to-erase, a multi-cycle shake of the toy as the line fades.
- 15.23–15.73 s (0.50 s) and 16.00–16.43 s (0.43 s): the CTA state swap and the re-zoom.
- Line drawing itself is slow and continuous, below the motion threshold, which is why it is not segmented.
- From frames (estimate), the "HIRED" sticker appears with the green CTA at about 23 s.

## 8. Brand system
n/a — not a brand system. It borrows the Etch A Sketch trademark (logo and red), and the host document is neutral, Apple-like UI.

## 9. UX
- **Strengths:**
  - The disabled CTA's copy explains the requirement.
  - The hints enumerate every gesture.
  - Erase is explicit.
  - The success state is unmistakable.
- **Weaknesses:**
  - The toy's single-line constraint makes real signatures messy.
  - Shake-to-erase is risky on mobile, where accidental erasure is likely.
  - The green success pill and the footer fail contrast.
- It works as a delightful, legally irrelevant concept, which the footer jokes about.

## 10. Craft signals
- The screen has a speckle texture (aluminium powder) instead of a flat grey.
- The knobs carry about 60 radial knurl ribs plus direction glyphs (◀▶ and ▲▼) that match their axes.
- The disabled CTA text changes to describe the missing step, not just the colour.
- Action words in the hint row use a dotted underline; descriptions do not.
- The required asterisk in the label is red, echoing the toy.
- The signature is a single continuous stroke of constant width, faithful to the mechanism.
- The "HIRED" sticker has a white die-cut border and a slight rotation.

## 11. Reproduction recipe
```css
:root{--page:#f2f2f2;--card:#fff;--red:#cd2429;--red-deep:#a40d12;--screen:#c4c5c9;--ink:#2e2f33;--cta:#1c1c1e;--ok:#1f7a36}
.card{background:var(--card);border-radius:40px;box-shadow:0 30px 80px rgb(0 0 0/.08)}
.etch{border-radius:120px 120px 40px 40px;background:linear-gradient(170deg,#e65a5d 0%,var(--red) 35%,var(--red-deep) 100%);
  box-shadow:0 40px 60px -20px rgb(120 0 0/.35)}
.screen{border-radius:24px;background:var(--screen) url(speckle.png);box-shadow:inset 0 6px 10px rgb(0 0 0/.18),0 0 0 20px #8a0a0f}
.knob{width:220px;aspect-ratio:1;border-radius:50%;background:radial-gradient(#fff 55%,transparent 56%),repeating-conic-gradient(#ddd 0 3deg,#fff 3deg 6deg)}
.cta{border-radius:9999px;background:var(--cta);color:#fff;padding:24px 70px;font:500 34px Inter}
.cta:disabled{background:#e8e8ec;color:#8a8a8e}
.cta.done{background:var(--ok)}
.hint a{text-decoration:underline dotted 2px;text-underline-offset:6px}
@keyframes shake{0%,100%{transform:none}20%{transform:translateX(-24px) rotate(-3deg)}40%{transform:translateX(20px) rotate(2deg)}60%{transform:translateX(-14px)}80%{transform:translateX(8px)}}
.etch.erasing{animation:shake 1.37s cubic-bezier(.4,0,.6,1)}
```
Accessibility fix: use #1f7a36 for success green (white text then reaches 5.4:1).

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | A photoreal toy inside a crisp, neutral document. Strong contrast of registers. |
| Originality | 9 | Signature-as-Etch-A-Sketch, with shake-to-erase, is a genuinely new mapping. |
| Usability | 7 | Proper validation and hint states. Contrast failures and shake risk hold it back. |
| Craft | 9 | Speckled glass, knurled knobs, explanatory disabled copy and a sticker payoff: thorough. |

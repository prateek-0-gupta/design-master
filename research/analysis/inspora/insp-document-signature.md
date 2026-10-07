---
id: insp-document-signature
source: inspora
category: Product
status: analyzed
title: "document signature"
creator: "@nickpylll"
styles: [aurora-glow, glassmorphism, micro-interaction]
patterns: [bottom-sheet-confirmation, sign-button-signature-morph, blur-out-success-state, inline-entity-chip, dashed-detail-divider, ghost-plus-solid-button-pair]
mode: light
palette: ["#f6f6f6", "#7baedb", "#5699cc", "#9fc5e4", "#91badf", "#ffffff", "#545d65", "#050404"]
type_families: ["SF Pro Display (likely)"]
type_class: [neo-grotesk]
radius_px: [9999, 56]
motion: {durations_s: [0.23, 0.17], easing: [ease-out, ease-in-out], loop: true}
scores: {aesthetics: 8, originality: 7, usability: 5, craft: 8}
craft_signals: [handwritten-signature-replaces-label, background-content-blurs-not-hides, two-tone-headline-hierarchy, inline-logo-chip-in-sentence, translucent-ghost-cancel]
anti_patterns: [white-on-light-blue-fails-aa, cancel-shown-after-success]
---
# document signature — @nickpylll

## 1. Snapshot
- **Subject:** A 6.55 s, 1080×1080 mobile loop. The bottom of an iPhone shows a sky-blue sheet for agreement "ND327"; tapping "Sign" draws a signature inside the button, then the content blurs away to "Agreement ND327 is successfully signed".
- **Why it's remarkable:** The button becomes the signature field (pen icon + "Sign" → a scribbled autograph), so the act of signing happens in the control itself.

## 2. Composition & layout
- The phone is cropped to the bottom ~60%, with a white top sheet edge and grabber visible at the top. The working area is a full-bleed blue gradient sheet.
- **Left-aligned content column** (~150 px margin in frame):
  - document glyph (~40×55 px);
  - three-line headline at ~26 px in the frame;
  - "Contact / Phil Norman";
  - a dashed divider;
  - "Project APR / $12 000.00".
- **Button pair** at the bottom: ghost "Cancel" and solid white "Sign", each ~170×52 px in the sheet frame (≈285×88 px in the key frame), full-pill radius.
- **Success state:** centred icon with a green check badge and a two-line centred message.

## 3. Typography
- SF Pro Display–like at regular weight only.
- **Headline:** two tones. "Redesign discovery phase for [logo] Brick inc." is in white; "Agreement ND327" is in pale blue (#9fc5e4) as a secondary layer.
- **Labels:** "Contact", "Project APR" at ~14 px pale blue over ~20 px white values.
- **Success message:** ~28 px centred.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #5699cc → #9fc5e4 | sheet gradient top → bottom | ~50% |
| #7baedb | mid-sheet | 23% |
| #ffffff | primary text, Sign button | — |
| #9fc5e4 | secondary text | 8% |
| #545d65 | Sign / Back to Docs label | 1% |
| #f6f6f6 | stage | 42% |
| #050404 | phone bezel | 3.5% |

WCAG checks:
- White on #7baedb: **2.35:1 (fails)**.
- White on #5699cc: 3.08:1 (large only).
- Secondary #9fc5e4 on #7baedb: **1.3:1**. The "Agreement ND327" half of the headline nearly vanishes.
- Button label #545d65 on white: 6.71:1.

## 5. Depth & material
- The sheet is a soft vertical gradient with faint cloud-like highlights (an aurora/sky feel).
- **Cancel:** a translucent white ghost (~15% fill) with a 1 px lighter rim.
- **Success transition:** existing content gets a strong Gaussian blur (~20 px) and fade instead of disappearing, so it stays as a ghost layer behind the confirmation.

## 6. Components & patterns
- An inline entity chip: a tiny orange brand logo inside the sentence ("for ▣ Brick inc.").
- A download glyph after the ID.
- Signature morph inside the primary button.
- The button label changes to "Back to Docs" on success; Cancel is still present (questionable).

## 7. Motion
- **Measured:** 2 segments.
  - **2.93–3.17 s (0.23 s):** ease-out, peak 0.21, which is the blur-out/success swap.
  - **5.43–5.6 s (0.17 s):** symmetric, the return to the start state.
- motion_fraction is 0.07, and the loop is seamless (first/last diff 0.28).
- **Below threshold:** the signature drawing at ~1.1–2.5 s is a small-area stroke animation, a write-on of about 0.7 s estimated from frames.
- **Sequence:** tap → button content swaps to scribble → hold ~0.7 s → quick blur to success → hold ~2.3 s → reset.

## 8. Brand system
n/a — not a brand system. Identity cues: sky gradient as the "trust" colour, an Apple-Wallet-like sheet.

## 9. UX
- Signing in place is delightful, but a scribble in a 52 px button is a token gesture, not legally meaningful capture. A real product needs explicit consent text.
- **Risks:**
  - White-on-light-blue body text fails contrast.
  - The secondary headline half is near invisible.
  - "Cancel" after success is ambiguous.

## 10. Craft signals
- The signature glyph is centred in the same button bounds that held "✎ Sign", so there is no layout shift.
- The prior content blurs and stays in place, which preserves spatial context behind the success message.
- The headline mixes two tones within one sentence for hierarchy, with no size change.
- A dashed divider separates identity (contact) from money (APR).
- The ghost and solid buttons have equal width with a ~10 px gap.

## 11. Reproduction recipe
```css
.sheet{background:linear-gradient(180deg,#4a8fcf 0%,#7baedb 55%,#a9cdea 100%);color:#fff;padding:32px 24px}
.sheet .muted{color:#d6e8f6} /* raise from #9fc5e4 for contrast */
.btn{height:52px;border-radius:9999px;font:500 16px/1 "SF Pro Text",system-ui}
.btn.ghost{background:rgba(255,255,255,.15);box-shadow:inset 0 0 0 1px rgba(255,255,255,.3);color:#fff}
.btn.solid{background:#fff;color:#545d65}
.content{transition:filter .23s cubic-bezier(.2,.8,.2,1),opacity .23s}
.is-signed .content{filter:blur(18px);opacity:.35}
.signature path{stroke-dasharray:400;stroke-dashoffset:400;animation:write .7s ease-out forwards}
@keyframes write{to{stroke-dashoffset:0}}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Serene gradient, generous type, elegant success state. |
| Originality | 7 | Signing inside the button is a fresh micro-interaction. |
| Usability | 5 | Low contrast throughout; residual Cancel; tokenistic signature. |
| Craft | 8 | No-shift morph and blur-in-place transition are well judged. |

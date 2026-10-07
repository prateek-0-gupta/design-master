---
id: insp-404-page-2
source: inspora
category: Web
status: analyzed
title: "404 page"
creator: "@ozzyxs1a"
styles: [minimal-swiss, flat-illustration, micro-interaction, playful-rounded]
patterns: [spotlight-reveal-text, mascot-search-animation, giant-numerals-hero, delayed-cta-reveal, error-page-storytelling, center-stack-404]
mode: light
palette: ["#f9f9f9", "#e0dfe4", "#17171a", "#8e939c", "#cc9958", "#4e5e70", "#413236"]
type_families: ["Inter Display / SF Pro Display (likely)"]
type_class: [neo-grotesk]
radius_px: [8]
motion: {durations_s: [1.30, 0.25, 0.18, 1.86, 0.32], easing: [ease-in-out, ease-out], loop: false}
scores: {aesthetics: 8, originality: 8, usability: 7, craft: 8}
craft_signals: [light-cone-as-text-mask, lamp-contact-shadow-follows, cta-appears-only-after-story, mascot-occludes-glyph-top, near-white-canvas-not-pure-white]
anti_patterns: [copy-invisible-until-lit, 14s-before-cta, decorative-text-fails-contrast]
---
# 404 page — @ozzyxs1a

## 1. Snapshot
- **Subject:** A 1920×1200, 14.3 s clip of a white 404 page. A Pixar-style desk lamp hops around a pale-grey "404", and wherever its light falls the digits and copy darken into legibility. It ends perched on the "0", and a "Go Home" button appears.
- **Why it's remarkable:** The lamp's light cone is a text mask. The UI is literally invisible until the mascot "searches" it, so the illustration acts out "we looked everywhere".

## 2. Composition & layout
- **Centre stack:**
  - "404" spans x≈675–1240 (565 px) with a cap height of ~230 px from y≈485 to 715.
  - Headline at y≈780.
  - Sub-line at y≈815.
  - The CTA (final frame) is centred ~140 px below the numerals.
- **Lamp:** about 170×310 px. It moves through positions: right of the digits, then right edge, then left, and finally centred on top of the "0", where its base hides the top of the zero's bowl.
- **Canvas:** About 96% is empty #f9f9f9. The design depends on that emptiness.

## 3. Typography
- **Numerals:** a neo-grotesk display, Inter Display or SF Pro Display at Semibold (600), ~320 px, tracking about −0.02 em.
- **Headline:** "Oops… nothing to see here!" at ~22 px semibold.
- **Sub-line:** ~15 px regular.
- **Button:** "Go Home" at ~14 px medium, white on near-black.
- **Hierarchy by luminance:** Glyphs exist in two states, unlit (#e0dfe4) and lit (#17171a). The transition is a linear gradient across the glyph, so a digit can be half lit, as in "4" at 3.97 s.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #f9f9f9 | canvas | 96% |
| #e0dfe4 / #ecebee | unlit numerals and copy | 1.7% |
| #17171a | lit numerals, headline, button fill | 0.4% |
| #8e939c / #bbb8b9 | mid-gradient, partially lit text | 0.8% |
| #cc9958 | lamp shade (amber) | 0.3% |
| #4e5e70 | lamp base (steel blue) | 0.3% |
| #413236 | lamp arm (oxblood) | 0.3% |

WCAG checks:
- Lit text #17171a on #f9f9f9 is **16.99:1**.
- Unlit #e0dfe4 is **1.26:1**, and the unlit sub-line at about #ecebee is **1.13:1**, which is effectively invisible. This is intentional, but real users who arrive mid-animation or with reduced motion may see nothing.
- The partially lit grey #5f6368 is 5.75:1.
- The button is white on #17171a at 17.89:1.

## 5. Depth & material
- **Lamp:** flat vector with a 2 px dark outline and a two-tone shade (highlight band on the amber). It is the only coloured object.
- **Contact shadow:** a soft, blurred grey ellipse (~70×15 px) sits under the lamp. When the lamp jumps, the shadow stays on the "floor" and shrinks, which sells the hop (visible at 0.79 s and 7.14 s, where it hangs below the airborne lamp).
- **Text:** no other depth; the type is flat.

## 6. Components & patterns
- **Spotlight-reveal type:** a gradient mask anchored to the lamp head's direction.
- **Mascot:** a character with an implied "eye" (the black pivot dot), which gives it personality without a face.
- **Delayed CTA:** a dark pill-rectangle (~84×34 px, radius ~8 px) appears only in the last ~1 s.
- **Copy:** includes a gradient-lit tail, so "isn't here." stays lighter than the rest, as if outside the cone.

## 7. Motion
- **Measured:** 14.28 s at 28.57 fps, motion_fraction **0.37**, 13 segments with a median of **0.25 s**; not a seamless loop.
- **Long moves:** 0.60–1.89 s (1.30 s, symmetric ease-in-out, peak 0.53) and 6.69–8.54 s (1.86 s, ease-in-out) are the lamp's big relocations.
- **Short bursts:** 0.14–0.32 s each, at 2.21, 3.15, 4.38, 5.01, 8.65 and 9.00–10.96 s, are hops, head turns and settle bounces. Two have ease-out shape (peak 0.28), the snap of a landing.
- **Rhythm:** a 9.0–11.0 s cluster of five short segments (~0.3 s each, about 0.1 s apart) is the "searching" jitter on top of the "0", followed by stillness and the CTA fade at ~13.4 s (0.18 s segment).
- **Character:** The animation follows squash-and-anticipation principles: long glides are ease-in-out and landings are ease-out.

## 8. Brand system
n/a — not a brand system. No logo and no nav, which leaves a purely generic 404 component. Identity is carried by the lamp character, a clear Luxo homage.

## 9. UX
- **Good:**
  - Delightful and on-message.
  - The final state is a clean, conventional 404 with headline, explanation and a single primary action.
- **Risky:**
  - The useful content is gated behind ~13 s of animation.
  - Text before lighting fails contrast at about 1.1–1.3:1.
  - The prefers-reduced-motion state must start fully lit with the CTA visible.
  - The lamp sitting on the "0" hides part of the glyph, which is a fine joke but harms recognition of "404" at small sizes.

## 10. Craft signals
- The light cone's falloff is a soft linear gradient, about 120 px from dark to unlit, so glyphs are partially lit.
- The contact shadow is decoupled from the jumping lamp, a correct physical cue.
- The canvas is #f9f9f9, not #fff, so the lamp's white bulb highlight still reads.
- The base ellipse of the lamp aligns to the cap height of the "0" in the final pose.
- Exactly one dark action (button) appears, matching the lit-text colour #17171a.

## 11. Reproduction recipe
```css
:root{--bg:#f9f9f9;--unlit:#e0dfe4;--lit:#17171a;--r-btn:8px;--font:"Inter Display","SF Pro Display",system-ui,sans-serif}
.code{font:600 clamp(160px,17vw,320px)/1 var(--font);letter-spacing:-.02em;
  /* light position driven by JS via --lx/--ly (lamp head) */
  background:radial-gradient(260px 220px at var(--lx,50%) var(--ly,40%),var(--lit) 30%,var(--unlit) 70%);
  -webkit-background-clip:text;color:transparent;transition:--lx .3s,--ly .3s}
@property --lx{syntax:'<percentage>';inherits:false;initial-value:50%}
@property --ly{syntax:'<percentage>';inherits:false;initial-value:40%}
.lamp{animation:hop 1.3s cubic-bezier(.45,0,.55,1) both}
@keyframes hop{0%{transform:translate(0,0)}45%{transform:translate(-120px,-90px)}100%{transform:translate(-240px,0)}}
.shadow{animation:shrink 1.3s ease-in-out both}
@keyframes shrink{45%{transform:scaleX(.55);opacity:.4}}
.cta{background:var(--lit);color:#fff;border-radius:var(--r-btn);padding:8px 16px;font:500 14px var(--font);
  opacity:0;animation:in .3s ease-out 12.6s forwards}
@media (prefers-reduced-motion:reduce){.code{background:none;color:var(--lit)}.cta{opacity:1;animation:none}}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Calm white field, one coloured character, crisp type. |
| Originality | 8 | Using the lamp's light as a reveal mask for the error text is a genuinely clever mechanic. |
| Usability | 7 | The final state is exemplary, but content and CTA are delayed and initially invisible. |
| Craft | 8 | Convincing hop physics, a detached shadow and a smooth gradient falloff. |

---
id: insp-1-21
source: inspora
category: Web
status: analyzed
title: "Brand story cards"
creator: "@basit_designs"
styles: [minimal-swiss, soft-3d, luxury]
patterns: [triptych-portrait-cards, hero-object-per-card, gradient-image-header, fade-out-text-mask, thinking-indicator-orb, centred-caption-stack]
mode: light
palette: ["#fdfdfd", "#f1f1f1", "#e0e1e4", "#aec0c8", "#5d8698", "#1e415c", "#0f1a2c", "#000911"]
type_families: ["Inter (likely)"]
type_class: [neo-grotesk]
radius_px: [36]
motion: {durations_s: [6.67], easing: [linear], loop: true}
scores: {aesthetics: 8, originality: 6, usability: 5, craft: 8}
craft_signals: [object-contact-shadow-offset-down, mask-fade-on-overflow-copy, sky-to-abyss-gradient, three-cards-equal-size-equal-gaps, single-weight-type, card-tint-one-step-off-canvas]
anti_patterns: [header-copy-invisible-on-pale-gradient, faded-paragraph-unreadable, low-information-density]
---
# Brand story cards — @basit_designs

## 1. Snapshot
- **Subject:** A 6.67 s, 1920×1352 seamless loop of three portrait story cards for a fictional quantum-computing brand ("Powered by Odor").
  - Card 1: a glass bead with a swirling pink flower.
  - Card 2: a sky-to-abyss teal gradient header plus a white-paper blurb.
  - Card 3: a brushed-metal sphere labelled "Thinking…".
- **Why it's remarkable:** Each card carries one tactile hero object with a long, soft contact shadow on a near-white card. It is a gallery-like, museum-label approach to brand storytelling.

## 2. Composition & layout
- **Cards:** three cards, each about 455×900 px (x 230→685, 732→1187, 1235→1690), with equal gutters of about 48 px. They are centred with about 225 px side margins and top at y≈225. Radius is about 36 px.
- **Card 1 stack:**
  - a 2-line caption at the top (y≈316);
  - a 195 px bead at y≈405–600, with its shadow falling about 80 px below;
  - "Powered by Odor" at y≈915;
  - a grey 3-line footnote at y≈1004.
- **Card 2:** The top 555 px is a vertical gradient image with white captions at the top and bottom. Below it is a 6-line paragraph left-aligned with a 34 px inset; the last lines fade to transparent.
- **Card 3:** a caption at the top, "Powered by Odor" centred at y≈676, "Thinking…" plus a 105 px metal sphere near the bottom.
- All copy is centre-aligned except the card 2 paragraph.

## 3. Typography
- A single neo-grotesk (Inter-like), regular 400 only. Hierarchy is by colour (black vs grey), not by size.
- **Sizes:**
  - captions about 17 px/1.45;
  - "Powered by Odor" about 17 px in pure black;
  - the paragraph about 17 px/1.55 grey;
  - "Thinking…" about 14 px light grey.
- Tracking is neutral, there are no display sizes, and everything reads like a museum wall label.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #fdfdfd | page canvas | 53.8% |
| #f1f1f1 | card fill (one step darker) | 31.5% |
| #e0e1e4 | shadows, faded text | 4.4% |
| #aec0c8 → #5d8698 → #1e415c → #0f1a2c → #000911 | card 2 gradient (mist → teal → abyss) | about 10% |
| pink/magenta (bead) | hero accent, image only | <2% |

WCAG checks:
- Black (#111) on #f1f1f1 is 16.7:1.
- Grey paragraph (≈#6b6b6b) on #f1f1f1 is 4.72:1 and passes.
- White on the dark gradient bottom (#0f1a2c) is 17.4:1.
- **Fails:** white caption on the pale top (≈#c8d8e0) is 1.36:1, effectively invisible. The footnote grey (≈#9a9a9a) is 2.49:1, and the faded paragraph tail (≈#c4c4c4) is 1.54:1.

## 5. Depth & material
- **Cards:** flat, with no border and no shadow. They separate from the canvas only through #f1f1f1 vs #fdfdfd (about 1.07:1), which is very subtle.
- **Hero objects:** they carry all the depth. Each has a soft elliptical contact shadow offset about 60–80 px downward with blur of about 40 px, so they float above the card.
- **Bead:** a refractive glass bead with a magenta rim and a dark interior.
- **Sphere:** satin metal with a top-left specular highlight and a cool blue-grey body.
- **Card 2:** the gradient reads as ocean depth or "first light", matching the copy.

## 6. Components & patterns
- A triptych of story cards: a portrait ratio of about 1:2 with one idea per card.
- A gradient media header with overlaid caption.
- **Text overflow fade:** the paragraph dissolves through a mask, hinting at "read more".
- **Thinking indicator:** a label plus an object, so an AI-agent state becomes a brand element.

## 7. Motion
- **Measured:** 6.67 s at 30 fps. motion_fraction is 0.0, mean energy 0.02 and there are no segments above threshold. The clip is a seamless loop (first/last diff 0.77).
- **Observed across frames:**
  - The flower inside the bead rotates and blooms (its pink mass grows from about 30% to 80% of the bead between t=0.37 s and t=2.59 s).
  - The metal sphere's highlight drifts gently.
- All motion is confined to small objects, so energy stays sub-threshold. It is ambient, linear and continuous, with no UI transitions.

## 8. Brand system
n/a — not a brand system. Identity cues:
- "Powered by Odor" repeated as a signature line on two cards;
- a natural-light metaphor (flower bloom, dawn gradient) for "quantum utility";
- object-as-mascot (bead, sphere).

## 9. UX
- These are presentation cards, not interactive UI. Usability is low: the key header caption on card 2 is unreadable, two of the three cards carry only about 15 words, and the faded paragraph has no affordance to expand.
- Low card-to-canvas contrast weakens the card boundaries on poor screens.

## 10. Craft signals
- Three identical card sizes with equal gutters of about 48 px and an identical 36 px radius.
- The contact shadows sit offset below the objects (not centred) to suggest overhead light, and they are consistent between bead and sphere.
- The card 2 gradient runs through five measured stops from #aec0c8 to #000911 with no banding visible.
- One type size and one weight throughout. Hierarchy comes only from #111 vs #6b6b6b.
- The paragraph fade starts exactly after line 6 (y≈990), so the visible block ends on a full sentence.

## 11. Reproduction recipe
```css
:root{--canvas:#fdfdfd;--card:#f1f1f1;--ink:#111;--muted:#6b6b6b;
  --depth:linear-gradient(180deg,#dbe6ec 0%,#aec0c8 15%,#5d8698 35%,#1e415c 60%,#0f1a2c 82%,#000911 100%);}
.story{width:455px;aspect-ratio:455/900;border-radius:36px;background:var(--card);
  display:flex;flex-direction:column;align-items:center;padding:80px 34px;text-align:center;
  font:400 17px/1.45 Inter,system-ui;color:var(--ink)}
.story .media{align-self:stretch;margin:-80px -34px 0;height:555px;background:var(--depth);border-radius:36px 36px 0 0}
.obj{width:195px;aspect-ratio:1;border-radius:50%;
  filter:drop-shadow(0 70px 40px rgba(0,0,0,.12))}
.fade{-webkit-mask-image:linear-gradient(#000 60%,transparent);mask-image:linear-gradient(#000 60%,transparent);color:var(--muted)}
@keyframes bloom{to{transform:rotate(360deg) scale(1.15)}}
.obj video,.obj img{animation:bloom 6.67s linear infinite}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Calm and premium. The tactile objects and the depth gradient carry the cards. |
| Originality | 6 | Object-on-card triptychs are common in current AI branding. |
| Usability | 5 | Several captions fail contrast badly, and there is little information with no affordances. |
| Craft | 8 | Precise grid, consistent shadows and a single type style. |

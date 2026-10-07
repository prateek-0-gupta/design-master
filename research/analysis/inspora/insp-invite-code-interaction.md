---
id: insp-invite-code-interaction
source: inspora
category: Motion
status: analyzed
title: "invite code interaction"
creator: "@nitishkmrk"
styles: [playful-rounded, soft-3d, micro-interaction, minimal-swiss]
patterns: [toggle-expand-reveal, pill-to-ticket-morph, dotted-perforation-border, copy-code-button, stacked-header-pill, skew-on-transition]
mode: light
palette: ["#f1f1f1", "#ffffff", "#f6f6f6", "#0fdf43", "#2ecc55", "#222222", "#8f8f8f", "#d7d7d7"]
type_families: ["SF Pro Rounded / SF Pro Display Bold (likely)"]
type_class: [neo-grotesk]
radius_px: [9999]
motion: {durations_s: [0.27, 0.23, 0.3, 0.23, 0.3, 0.23], easing: [ease-out, ease-in-out], loop: true}
scores: {aesthetics: 7, originality: 7, usability: 6, craft: 7}
craft_signals: [white-rim-around-pill, dotted-inner-border-as-ticket, header-tab-stacks-on-top, italic-skew-velocity-cue, shadow-grows-on-lift, single-green-accent]
anti_patterns: [white-on-neon-green-1-8-to-1, header-grey-3-to-1]
---
# invite code interaction — @nitishkmrk

## 1. Snapshot
- **Subject:** A 6.67 s, 960×960 loop of a SwiftUI control.
- **Collapsed:** a pill reading "Your Invite Is Ready" with a green circular ↓ button.
- **Expanded:** on tap, it springs into a two-part ticket: a grey header pill ("Your Invite Code") stacked above a dotted-border pill showing "LoveSwiftUI" with a green COPY button. A second tap collapses it again.
- **Why it's remarkable:** It is a tiny, tactile reveal. The dotted inner border turns a plain pill into a "ticket" with zero extra assets, and the transition adds a velocity skew to the label for physicality.

## 2. Composition & layout
- Square canvas, #f1f1f1. The control is centred, with its centre at y≈485.
- **Collapsed pill:** about 717×190 px (including a ≈12 px white rim). The label is left-aligned with about 70 px padding. The green circle is about 125 px, with about 25 px inset from the right.
- **Expanded:**
  - header pill about 684×115 px at y≈270–385;
  - code pill about 720×172 px at y≈395–567, with a 10 px gap between the two.
  - Inside the code pill, a dotted inner border inset about 12 px. "LoveSwiftUI" is left-aligned, and the COPY pill (about 195×97 px) is right-aligned.
- The expanded block grows upward from the collapsed position: the code row stays at the same y as the collapsed pill, and the header appears above it.

## 3. Typography
- SF Pro Display/Rounded-style bold grotesk.
- **Collapsed label:** about 46 px semibold #222.
- **Code:** "LoveSwiftUI" at about 50 px bold #222, in proportional type. A mono face would be better for codes.
- **Header:** "Your Invite Code" at about 32 px bold #8f8f8f.
- **Button:** "COPY" at about 34 px heavy, all caps, white.
- **At t≈4.08 s** the collapsed label renders visibly *oblique* (≈10° skew) mid-transition. It is a deliberate motion-smear cue that settles back to upright.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #f1f1f1 | canvas | 86% |
| #ffffff | pill rim and surfaces | 10% |
| #f6f6f6 | inner pill fill, header fill | — |
| #0fdf43 / #2ecc55 | COPY button (neon) / ↓ circle (softer green) | 1.5% |
| #222222 | primary text | <1% |
| #8f8f8f | header label | <1% |
| #d7d7d7 | perforation dots | 1% |

WCAG checks:
- #222 on white is 15.91:1.
- White on #0fdf43 (the COPY label) is **1.8:1, a clear fail**. White on #2ecc55 (the arrow) is 2.12:1.
- #222 on the same green would give 8.83:1, so a dark label would fix it.
- The header grey #8f8f8f on #f6f6f6 is **2.99:1**.

## 5. Depth & material
- **Pills:** a two-layer construction: an outer white rim of about 12 px around an inner #f6f6f6 field. This reads as a thick, soft plastic edge.
- **Shadow:** soft, wide (blur about 40 px, ≈8% black), offset downward. It grows larger while the pill is "lifted" mid-transition (t≈1.85 s and 4.08 s frames show a longer shadow), then shrinks.
- **COPY button:** a subtle top-light gradient and a 2 px darker green bottom edge, a hint of skeuomorphic pressability.
- **Perforation:** about 40 dots of 8 px diameter at about 17 px pitch, light grey, following the pill's stadium path.

## 6. Components & patterns
- **Disclosure toggle:** the ↓ circle expands the pill. In the loop the user taps the label/area; there is no ↑ affordance once expanded.
- **Ticket reveal:** a header tab plus a code row and a COPY action.
- **Copy button:** no "Copied" confirmation state is visible in the sampled frames.

## 7. Motion
Measured: 59.94 fps, 6.67 s, `motion_fraction` 0.24, `seamless_loop_likely` **true** (`first_last_diff` 0.92). Six segments, each 0.23–0.30 s (median **0.25 s**):
- 0.50–0.77 s (0.27 s, ease-out): expand;
- 1.67–1.90 s (0.23 s, symmetric): collapse;
- 2.70–3.00 s (0.30 s): expand;
- 3.93–4.17 s (0.23 s): collapse;
- 4.83–5.13 s (0.30 s, ease-out): expand;
- 6.10–6.33 s (0.23 s): collapse.

Expands are a touch longer (0.27–0.30 s) than collapses (0.23 s), a sensible asymmetry. The cycle is about 2.2 s. The frames suggest a SwiftUI `.spring(response≈0.3, dampingFraction≈0.75)`: a slight overshoot on the lift (shadow growth) and a velocity skew on the label.

## 8. Brand system
n/a — not a brand system. "LoveSwiftUI" is a demo code. iOS-system green is the only accent.

## 9. UX
- **Strengths:**
  - Progressive disclosure keeps the code hidden until wanted.
  - The code and the COPY action sit on one row.
  - Snappy timing at about 0.25 s.
- **Risks:**
  - The white-on-neon-green COPY label is 1.8:1.
  - No copied-state feedback.
  - Proportional type for a code (l/I ambiguity in "LoveSwiftUI").
  - The collapse affordance is unclear.

## 10. Craft signals
- The two-layer pill (a 12 px white rim plus an #f6f6f6 inner field) gives a soft, thick edge.
- The dotted perforation is inset about 12 px and follows the stadium curve evenly, with no clipped dot at the ends.
- The header tab stacks 10 px above the code row and matches its width minus the rim.
- The ≈10° label skew during motion is a velocity cue that resolves at rest.
- The shadow length scales with the lift during transitions.
- Expand runs 0.27–0.30 s and collapse 0.23 s (measured).

## 11. Reproduction recipe
```css
:root{--canvas:#f1f1f1;--rim:#fff;--field:#f6f6f6;--ink:#222;--ink-2:#6f6f6f;--go:#0fdf43;--dot:#d7d7d7}
.pill{border-radius:9999px;background:var(--field);box-shadow:0 0 0 6px var(--rim),0 14px 30px rgb(0 0 0/.08);
  display:flex;align-items:center;justify-content:space-between;padding:10px 12px 10px 34px;font:600 23px -apple-system,"SF Pro Display",sans-serif;color:var(--ink);
  transition:transform .28s cubic-bezier(.34,1.4,.64,1),box-shadow .28s}
.pill.is-moving{transform:translateY(-4px) skewX(-8deg);box-shadow:0 0 0 6px var(--rim),0 24px 40px rgb(0 0 0/.12)}
.code{position:relative}
.code::before{content:"";position:absolute;inset:6px;border-radius:9999px;border:4px dotted var(--dot)}
.copy{background:linear-gradient(#25e858,var(--go));color:var(--ink);font:800 17px -apple-system;letter-spacing:.02em;padding:12px 22px;border-radius:9999px;
  box-shadow:inset 0 -2px 0 rgb(0 0 0/.12)}
.header{color:var(--ink-2);font-weight:700;text-align:center;margin-bottom:5px}
```
SwiftUI equivalent: `withAnimation(.spring(response: 0.3, dampingFraction: 0.75)) { expanded.toggle() }` with `.matchedGeometryEffect` on the pill.

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 7 | Soft and friendly, with a clever dotted ticket and a single accent. The neon green is a bit harsh. |
| Originality | 7 | Pill-to-ticket disclosure with perforation is a fresh twist on a copy-code chip. |
| Usability | 6 | Fast and clear, but the COPY contrast fails and there is no copied feedback. |
| Craft | 7 | Nice rim, perforation and velocity skew. Proportional code type and the contrast slips cost points. |

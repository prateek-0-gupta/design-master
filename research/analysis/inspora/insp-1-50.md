---
id: insp-1-50
source: inspora
category: Web
status: analyzed
title: "onboarding modal"
creator: "Maxim Kuznetsov"
styles: [dither-halftone, dark-premium, technical-wireframe, retro-pixel]
patterns: [onboarding-modal, dithered-3d-hero, three-button-footer, inline-learn-more-link, pixel-field-backdrop, dashed-layout-guides]
mode: dark
palette: ["#0c0c0c", "#111112", "#181819", "#282829", "#404040", "#8a8a8a", "#b2b1b1", "#f2f2f2"]
type_families: ["Haffer / Neue Haas-style grotesk (likely)", "monospace caption (likely JetBrains Mono / Space Mono)"]
type_class: [neo-grotesk, mono]
radius_px: [0]
motion: {durations_s: [4.77], easing: [ease-in-out], loop: true}
scores: {aesthetics: 9, originality: 7, usability: 8, craft: 9}
craft_signals: [square-corners-system-wide, media-well-divided-by-1px-rule, primary-only-filled-button, back-left-skip-continue-right, dither-object-centered-in-well, guides-align-to-modal-edges]
anti_patterns: [hairline-borders-under-2-to-1, backdrop-motion-behind-modal]
---
# onboarding modal — Maxim Kuznetsov

## 1. Snapshot
- **Subject:** A 4.81 s, 1888×1890 (about 2× retina) seamless loop of a welcome modal for "Axiom Zero", a layer-0 protocol. A dithered 3D crystal spins in a media well above a title, body copy and a Back / Skip / Continue footer, over a dark field of drifting pixel bands.
- **Why it's remarkable:** It is the same 1-bit dither language as the creator's bento card (insp-1-40), applied to a functional modal. The modal stays perfectly conventional and accessible while the art carries the brand.

## 2. Composition & layout
- **Modal:** about 1032×955 px capture (about 516×478 CSS), centred (x 430→1462, y 466→1421), square corners, a 1 px #282829 border, fill #111112.
- **Media well:** the top 475 px (about 50%), closed by a 1 px rule at y≈940. The crystal is about 400 px in the capture, centred.
- **Content area (about 62 px side padding):**
  - title at y≈1037;
  - 3-line body at y≈1114–1194;
  - button row at y≈1270–1357 (each 88 px tall in the capture, about 44 CSS).
- **Footer split:** "Back" with a chevron is alone on the left (about 220 px wide). "Skip" (about 150 px) and "Continue" (about 214 px) are grouped on the right with a 32 px gap.
- **Backdrop:** a 4-column dashed guide grid (x≈150/467/1425/1743) whose inner lines align with the modal's left and right edges. Captions sit at bottom-left (avatar plus "@DISARTO_MAX") and bottom-right ("WELCOME/ONBOARDING MODAL VIEW") in mono.

## 3. Typography
- **Title:** about 48 px capture (about 24 CSS), regular 400, near-white, in a grotesk with open, slightly squarish forms (Haffer/Unica-like).
- **Body:** about 26 px capture (13 CSS)/1.55 in #8a8a8a, with "Learn more" in white as an inline link (colour change only).
- **Buttons:** about 28 px capture (14 CSS) regular. "Continue" is medium, dark on light.
- **Captions:** uppercase mono at about 13 CSS with tracking of about 0.04 em.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #0c0c0c | page backdrop | 86.7% |
| #111112 / #181819 | modal surface | 4.4% |
| #282829 | borders, divider | 4.5% |
| #404040 | dither field pixels, guides | 2.5% |
| #8a8a8a | body text | — |
| #b2b1b1 / #f2f2f2 | object pixels, title, Continue fill | 1.9% |

WCAG checks:
- Title #f2f2f2 on #111112 is 16.9:1.
- Body #8a8a8a is 5.47:1.
- The Continue label (#111) on #f2f2f2 is 16.9:1.
- The mono captions (≈#6a6a6a on #0c0c0c) are 3.62:1.
- The outline-button borders (#404040-ish) are 1.82:1, which is below the 3:1 non-text guideline for control boundaries.

## 5. Depth & material
- **Shadow:** the modal has a very soft dark halo (a dark radial region visible around it at about 60 px) separating it from the dither bands. There is no drop shadow otherwise.
- **Crystal:** a faceted polyhedron rendered in Bayer-style 1-bit dither. Facets read via dot density and solid-white specular clusters.
- **Backdrop bands:** coarser and darker (#404040), so they read as far away. This is the same two-scale depth trick as insp-1-40.

## 6. Components & patterns
- **Onboarding modal:** a media well with title, body and a tertiary inline link.
- **Button hierarchy:**
  - **Back:** outline, with an icon.
  - **Skip:** outline.
  - **Continue:** filled light. It is the only filled element.
- No close "×" is visible, so Skip acts as the dismiss.
- **Annotation captions:** Dribbble-style presentation chrome, not product UI.

## 7. Motion
- **Measured:** 4.81 s at 55 fps. motion_fraction is 0.78, and there is one continuous 4.77 s segment with peak_at 0.53 (symmetric ease-in-out). The clip is a seamless loop (first/last diff 0.89).
- **Crystal:** rotates about one full turn per loop. Between t=1.87 s and t=3.47 s it passes through the pose where dither gets coarsest (larger pixel clusters), then returns to a fine, smooth shading at t=4.54 s, matching t=0.27 s.
- **Backdrop bands:** drift diagonally (a lower-left → upper-right swoosh is visible at 2.40–2.94 s).
- The modal itself is static, so motion is decorative only.

## 8. Brand system
n/a — not a brand system. Identity cues:
- a crystal "core" mascot in dither;
- square-cornered, hairline UI;
- mono meta captions.

It is consistent with insp-1-40, so it suggests a shared visual system for the protocol.

## 9. UX
- The flow is clear: one primary action, an escape hatch (Skip) and a Back for multi-step onboarding.
- The body explains value in two sentences with a learn-more link.
- **Risks:**
  - Outline-button borders are low contrast.
  - The link is distinguished by colour only.
  - The animated backdrop behind a modal needs reduced-motion handling.
  - No step indicator is visible, even though Back implies multiple steps.

## 10. Craft signals
- Zero border radius everywhere (modal, buttons, avatar), consistent with the dither pixel language.
- The 1 px divider between media well and content runs full-bleed to the modal border.
- All three buttons share the same 44 CSS px height and baseline. Spacing is the only grouping device (Back isolated left, Skip/Continue right).
- The dashed guide lines align to the modal's x-edges.
- Only the primary button is filled, which gives an unambiguous next step.

## 11. Reproduction recipe
```css
:root{--bg:#0c0c0c;--surface:#111112;--line:#282829;--line-2:#404040;--text:#f2f2f2;--text-2:#8a8a8a}
.modal{width:516px;background:var(--surface);border:1px solid var(--line);border-radius:0;
  box-shadow:0 0 120px 40px rgba(0,0,0,.8)}
.modal .well{height:238px;display:grid;place-items:center;border-bottom:1px solid var(--line)}
.modal .body{padding:36px 31px 31px}
.modal h2{font:400 24px/1.2 "Haffer",Inter,sans-serif;color:var(--text)}
.modal p{font:400 13px/1.55 "Haffer",Inter;color:var(--text-2)} .modal p a{color:var(--text)}
.actions{display:flex;gap:16px;margin-top:38px} .actions .back{margin-right:auto}
.btn{height:44px;padding:0 24px;border:1px solid var(--line-2);background:transparent;color:var(--text);border-radius:0}
.btn--primary{background:var(--text);color:#111;border-color:var(--text);font-weight:500}
.caption{font:400 13px "JetBrains Mono",monospace;text-transform:uppercase;letter-spacing:.04em;color:#6a6a6a}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 9 | Restrained, atmospheric, and the dither hero is gorgeous. |
| Originality | 7 | Strong execution of a standard modal. The dither art is the novelty, shared with insp-1-40. |
| Usability | 8 | Clear hierarchy and actions. Low-contrast control borders and no progress indicator. |
| Craft | 9 | Consistent square geometry, aligned guides and disciplined button hierarchy. |

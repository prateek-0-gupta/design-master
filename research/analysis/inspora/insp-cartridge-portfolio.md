---
id: insp-cartridge-portfolio
source: inspora
category: Motion
status: analyzed
title: "Cartridge portfolio"
creator: "@mamuso"
styles: [cinematic-3d, minimal-swiss, physical-material, x-retro-object]
patterns: [object-as-list-item, spine-shelf-to-face-flip, horizontal-swipe-carousel, bio-paragraph-hero, caption-under-object, bold-name-inline]
mode: light
palette: ["#d5d5d5", "#f1f1f1", "#111011", "#5a5a5c", "#6b6b6b", "#222324", "#9db59a", "#2b4fae"]
type_families: ["Inter / Söhne-style neo-grotesk (likely)", "small pixel/mono label print on cartridge faces"]
type_class: [neo-grotesk, mono]
radius_px: [56, 8]
motion: {durations_s: [0.43, 0.23, 0.37, 0.27, 0.4, 0.23, 0.37, 0.27, 0.4], easing: [ease-out], loop: false}
scores: {aesthetics: 9, originality: 9, usability: 7, craft: 9}
craft_signals: [cartridge-colour-matches-company-brand, spine-view-as-collapsed-state, label-art-per-employer, grey-body-black-name, consistent-ease-out-spring, contact-shadow-under-cartridges]
anti_patterns: [shelf-state-has-no-labels, cramped-carousel-edges]
---
# Cartridge portfolio — @mamuso

## 1. Snapshot
- **Subject:** A 19.3 s, 1080×1080 phone-mockup capture of a one-screen mobile portfolio: a short bio paragraph over a row of six 3D retro game cartridges (Famicom-style). Each cartridge is a past job. Tapping one rotates it from spine-out to face-on, revealing the label (GitHub 2019–2024, Vercel 2024–2026, SpaceXAI 2026–now). Swiping moves between them.
- **Why it's remarkable:** The CV becomes a game-cartridge shelf. Each employer becomes a collectible object whose shell colour and label art echo that company's brand, so a dry timeline turns into something you want to touch.

## 2. Composition & layout
- **Phone:** about 540×1000 px (screen about 520 px wide) on a #d5d5d5 noise-textured backdrop.
- **Screen:**
  - a 30 px black logomark (a pac-man-like blob) top-left at about 30 px inset;
  - the bio at y≈300–590 px, two paragraphs, measure about 455 px (about 30 characters per line), left-aligned at x≈310;
  - the cartridge zone about 340 px tall below.
- **Shelf state:** six cartridges stand spine-forward in perspective, about 40 px wide each, with about 8 px gaps, centred.
- **Focused state:** one cartridge rotates to face-on at about 380×250 px, centred. Neighbours peek at the screen edges (left/right about 20 px visible), and a caption (company / years) sits centred below.

## 3. Typography
- **Bio:** a neo-grotesk (Inter or Söhne) at about 28 px Regular in grey #5a5a5c, with leading of about 1.32 and tracking of about −0.01 em. The name "**mamuso**" is the only black (#111) and Medium weight, an inline emphasis instead of a headline.
- **Caption:** company name about 17 px Medium in black over years about 17 px Regular grey with tabular figures ("2024-2026").
- **Cartridge labels:** tiny mono and pixel text ("VP OF DESIGN", "2024-2026", "SFO"), like real cartridge label typography.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #d5d5d5 | backdrop | 50% |
| #f1f1f1 | screen background | 29% |
| #111011 | name, logomark, caption title | 2% |
| #5a5a5c | bio body | 3% |
| #6b6b6b | years caption | <1% |
| #222324 | black cartridges (Vercel, SpaceXAI) | 7% |
| #9db59a | sage cartridge (GitHub) | 2% |
| #2b4fae | cobalt cartridge | 2% |

Other shells are steel-blue and khaki.

WCAG:
- Body #5a5a5c on #f1f1f1 is 6.09:1, and the name is 16.81:1.
- Years #6b6b6b is 4.72:1.

All pass. The colour lives entirely in the objects.

## 5. Depth & material
- **Cartridges:** real-time 3D (or pre-rendered) matte injection-moulded plastic, with ribbed grip edges, recessed label panels, an edge-connector lip at the bottom and soft contact shadows (about 20 px blur) on the screen.
- **Label panels:** each carries its own art:
  - GitHub: a contribution-grid-like dark panel with green dots;
  - Vercel: a black panel with a chromatic-aberration triangle;
  - SpaceXAI: a black panel with a mono spec table.
- **Shelf state:** shows side-face shading, as if lit from the upper left.

## 6. Components & patterns
- A carousel of objects with two states: collapsed (spines on a shelf) and expanded (face-on with a caption).
- A caption under the focused item.
- Swipe navigation: f6 (13.96 s) shows the SpaceXAI cartridge sliding in while the caption has not yet appeared, so the caption fades in after the object settles.
- A return to shelf state (f2, f5, f8) after a focus, which is the toggle-to-collapse.

## 7. Motion
The motion is measured: 19.33 s, 60 fps, motion_fraction 0.16 (the screen is calm most of the time), not a loop.
- **10 segments, almost all ease-out:** peak_at 0.05–0.30 in 9 of 10, and one symmetric at 7.33 s (0.40 s).
- **Durations:** 0.17–0.43 s, median 0.32 s. Examples:
  - 0.23–0.67 s (0.43 s): the first flip to face-on;
  - 2.90 s (0.23 s) and 4.27 s (0.37 s): swipes;
  - 5.60 s (0.27 s): the collapse back to the shelf;
  - 16.63 s (0.40 s): the final collapse.
- The fast-start, long-settle profile reads as a spring with damping, consistent with a 3D rotation of about 90° (spine → face) plus translation.
- In f3 (7.52 s) the khaki cartridge is mid-rotation, about 45°, while the others hold, so only the selected object animates.

## 8. Brand system
n/a — personal portfolio, not a brand system. Identity cues: the blob logomark, grey prose with a bold name, and each employer re-skinned as a cartridge in its own brand language.

## 9. UX
- **Pros:** instantly understandable (tap or swipe), short copy, and accessible text contrast.
- **Cons:**
  - The shelf state shows no labels, so you cannot tell which spine is which job without tapping.
  - Peeking neighbours are cropped hard at the screen edge.
  - There is no explicit affordance (dots or arrows) for swiping.

## 10. Craft signals
- The cartridge shell colours map to employers (black for Vercel, sage-green for GitHub with a contribution-grid label).
- The spine view is a meaningful collapsed state, not just a smaller card.
- The caption appears only after the cartridge settles (f6 has no caption, f7 has one).
- Consistent ease-out timing (peak_at ≤0.3 in 9/10 segments) gives one motion personality.
- The only black text in the bio is the name, so hierarchy comes without a headline.
- Contact shadows under each cartridge are present in both states.

## 11. Reproduction recipe
```css
:root{--screen:#f1f1f1;--ink:#111011;--body:#5a5a5c;--muted:#6b6b6b}
.bio{font:400 28px/1.32 Inter,"Söhne",system-ui;letter-spacing:-.01em;color:var(--body);max-width:30ch}
.bio b{color:var(--ink);font-weight:500}
.shelf{display:flex;gap:8px;justify-content:center;perspective:900px}
.cart{width:250px;aspect-ratio:1.52;transform-style:preserve-3d;transform:rotateY(-78deg);
  transition:transform .4s cubic-bezier(.16,1,.3,1),margin .4s cubic-bezier(.16,1,.3,1);
  filter:drop-shadow(0 18px 20px rgba(0,0,0,.18))}
.cart[aria-expanded=true]{transform:rotateY(0) scale(1.5)}
.caption{opacity:0;transform:translateY(6px);transition:all .25s ease-out .3s}
.cart[aria-expanded=true]+.caption{opacity:1;transform:none}
.caption .years{font-variant-numeric:tabular-nums;color:var(--muted)}
```
```js
// three.js alt: GLTF cartridge, spring rotation y: -Math.PI*0.43 → 0, stiffness 260, damping 24
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 9 | Calm grey type with beautifully made, colour-coded 3D objects. |
| Originality | 9 | A CV as a game-cartridge shelf is a memorable, on-theme metaphor. |
| Usability | 7 | Simple interactions and AA text. The shelf lacks labels and the swipe affordance is hidden. |
| Craft | 9 | Per-company label art, consistent spring timing and staged caption reveal. |

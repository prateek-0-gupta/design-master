---
id: insp-3-4
source: inspora
category: Product
status: analyzed
title: "Two-Step Dock Menu"
creator: "@tilljanek"
styles: [micro-interaction, dark-premium, photo-led]
patterns: [morphing-container, pill-to-panel-expand, two-column-nav-menu, nested-disclosure, hover-row-highlight, sub-item-return-arrows, floating-dock]
mode: mixed
palette: ["#faf7ee", "#3e3d3b", "#4a4946", "#a3a19c", "#ffffff", "#737b59", "#b4b589"]
type_families: ["Inter (likely)"]
type_class: [neo-grotesk]
radius_px: [28, 14, 10, 8]
motion: {durations_s: [0.7, 0.73, 0.23, 0.2], easing: [ease-out, ease-in-out], loop: true}
scores: {aesthetics: 8, originality: 7, usability: 7, craft: 8}
craft_signals: [single-container-morph, icon-column-aligned-across-columns, sub-items-use-return-arrow-glyph, hover-pill-inset-6px, white-logo-tile-only-bright-element, warm-charcoal-not-black]
anti_patterns: [menu-labels-below-aa, sub-items-crop-during-collapse]
---
# Two-Step Dock Menu — @tilljanek

## 1. Snapshot
- **Subject:** A 12.2 s, 958×720 Framer prototype: a small "Acme Inc." dock pill expands into a two-column navigation panel, and a "Resources" row expands a second step with six sub-links, then everything collapses back to the pill.
- **Why it's remarkable:** One container grows in two discrete steps (pill → menu → menu + submenu) instead of spawning popovers, so spatial context is never lost.

## 2. Composition & layout
- Stage: warm cream #faf7ee sky over a blurred grass hill with two stone coins at bottom-right — a soft photographic scene in the lower ~25% of frame.
- Collapsed dock: ~180×50 px pill, centred at about y≈250 (frame 0.68 s).
- Step 1 panel: ~353×237 px (in the 958 frame) with header row (logo tile + name + layout icon) and a 2×4 grid of nav rows. Left column x≈+30 px, right column x≈+185 px.
- Step 2 panel (key frame): ~528×490 px, adding three sub-rows per column under "Resources". Row pitch ≈56 px for main items, ≈45 px for sub-items, so the second level is visibly denser.
- The camera reframes during the demo (panel shifts left/up between frames), keeping the expanding panel centred.

## 3. Typography
- Neo-grotesk, very likely Inter. Main items ≈19 px Regular; sub-items ≈16 px Regular; "Acme Inc." ≈16 px Medium in white.
- Hierarchy is by size and luminance: header white, items warm grey, sub-items dimmer grey. No bold in the menu.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #faf7ee | cream stage / sky | ~55% |
| #3e3d3b | panel surface (warm charcoal) | ~36% |
| #4a4946 | hover row fill | ~1% |
| #a3a19c | item labels and icons | ~1% |
| #ffffff | logo tile, header label | <1% |
| #737b59 / #b4b589 | grass greens | ~6% |

WCAG: white header on panel **10.85:1**. Item labels #a3a19c on #3e3d3b **4.2:1** (fails AA normal at 19 px regular; passes large only). Sub-items (≈#8f8d88) **3.27:1**. Hovered row text on #4a4946 **3.49:1**. Panel on cream **10.13:1** — strong figure/ground.

## 5. Depth & material
- Panel is flat warm charcoal with no visible border; separation comes from value contrast against the cream scene and a faint soft shadow.
- Hover state is a slightly lighter inset pill (~8–10 px radius) — elevation via surface tint.
- The photographic grass and coins give tactile depth behind the flat UI (shallow depth of field).

## 6. Components & patterns
- **Dock pill** with logo tile (white rounded square ~44 px in key frame, radius ~10) + name + panel-toggle icon.
- **Two-column nav grid** with 1.5 px outline icons (document, barcode, dollar, shapes, building, nodes, people).
- **Disclosure row** "Resources" with chevron that flips up when open.
- **Sub-items** prefixed by a "↳" return-arrow glyph, which signals hierarchy without indentation lines.
- Hover highlight on each row while the cursor passes.

## 7. Motion
Measured: 12.17 s, motion fraction only **0.19**, 6 segments; `seamless_loop_likely: true`.
- 0.37–1.07 s (**0.70 s**, peak 0.17 → ease-out): pill morphs into the step-1 panel.
- 1.30–1.53 s (0.23 s, ease-out): settle / first hover.
- 4.40–4.63 s (0.23 s, symmetric): Resources sub-panel opens (step 2).
- 7.43–7.63 s (**0.20 s**, peak 0.08 → strong ease-out): sub-panel collapses.
- 10.17–10.40 s (0.23 s) then 10.53–11.27 s (**0.73 s**, symmetric): toggle pressed, panel shrinks back to pill and the camera zooms out to show the full scene.
- Pattern: large morphs ~0.7 s, small disclosure steps ~0.2 s — size of change scales duration. From frames, rows fade/slide in after the container grows (estimate ~50–80 ms stagger).

## 8. Brand system
n/a — not a brand system. Placeholder "Acme Inc." with a four-point star mark; the cream/grass/coin scene suggests a fintech or "growth" theme.

## 9. UX
- Two-step reveal keeps the first level short (8 items) and puts 6 secondary links behind a single disclosure.
- Chevron state and the ↳ glyph make the hierarchy obvious.
- Risks: label contrast below AA; on collapse (7.44 s frame) sub-items are visibly clipped by the shrinking container before fading — slightly messy mid-state. No keyboard focus styling shown.

## 10. Craft signals
- Icons in both columns share one vertical axis per column; text starts ~38 px after icon left edge consistently.
- The white logo tile is the only bright element in the panel, anchoring the top-left.
- Warm charcoal (#3e3d3b) chosen to harmonise with the cream stage rather than neutral black.
- Duration scales with change size (0.7 s vs 0.2 s).

## 11. Reproduction recipe
```css
:root{--stage:#faf7ee;--panel:#3e3d3b;--hover:#4a4946;--label:#a3a19c;--label-2:#8f8d88;--head:#fff;
  --r-panel:28px;--r-row:10px;--font:"Inter",system-ui,sans-serif;}
.dock{background:var(--panel);border-radius:var(--r-panel);overflow:hidden;
  width:180px;height:50px;transition:width .7s cubic-bezier(.16,1,.3,1),height .7s cubic-bezier(.16,1,.3,1)}
.dock[data-open="1"]{width:353px;height:237px}
.dock[data-open="2"]{width:528px;height:490px;transition-duration:.23s}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:4px 24px;padding:8px 20px 20px}
.row{display:flex;gap:12px;align-items:center;padding:12px;border-radius:var(--r-row);
  color:var(--label);font:400 19px/1 var(--font)}
.row:hover{background:var(--hover);color:#d6d4cf}
.sub{font-size:16px;color:var(--label-2)} .sub::before{content:"↳";margin-right:12px}
.row,.sub{opacity:0;transform:translateY(4px);transition:opacity .2s,transform .2s}
.dock[data-open] .row{opacity:1;transform:none;transition-delay:calc(var(--i)*30ms)}
```
In Framer/Motion: `layout` on the container with `transition={{type:"spring",bounce:0.15,duration:0.7}}`.

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Warm charcoal on cream with a soft photo scene feels premium and calm. |
| Originality | 7 | Morphing dock menus exist; the explicit two-step growth is a nice refinement. |
| Usability | 7 | Clear hierarchy and spatial continuity; low label contrast. |
| Craft | 8 | Consistent icon grid and proportional durations; minor clipping on collapse. |

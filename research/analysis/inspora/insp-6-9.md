---
id: insp-6-9
source: inspora
category: Motion
status: analyzed
title: "Thinking states"
creator: "@xchylerdrenth"
styles: [dark-premium, monochrome, micro-interaction, technical-wireframe]
patterns: [agent-thinking-indicator, line-masked-circle-loader, icon-plus-two-line-status, variant-specimen-grid, staggered-segment-loader]
mode: dark
palette: ["#101113", "#ffffff", "#8e8e8e", "#545555", "#3b3d3d", "#cccccc"]
type_families: ["Inter (likely)"]
type_class: [neo-grotesk]
radius_px: [9999]
motion: {durations_s: [6.1], easing: [linear, ease-in-out], loop: true}
scores: {aesthetics: 7, originality: 7, usability: 7, craft: 7}
craft_signals: [circle-clipped-line-field, single-hue-luminance-animation, consistent-icon-diameter, label-baseline-aligned-to-icon-centre, seamless-6s-loop]
anti_patterns: [track-lines-below-3-to-1, ellipsis-two-dots]
---
# Thinking states — @xchylerdrenth

## 1. Snapshot
- **Subject:** A 6.1 s, 1920×1440 looping specimen of four "Agent thinking.." loaders arranged in a 2×2 grid. Each loader is a small circle built from parallel lines plus a two-line label.
- **Why it's remarkable:** All four indicators share one construction: a circle clipped from a field of 1–2 px lines. Each variant animates a different parameter (band luminance, dots, horizontal dashes, vertical bars), so the set reads as a family rather than four random spinners.

## 2. Composition & layout
- **Grid:** two columns at x≈255 and x≈1145 and two rows at y≈455 and y≈985, with about 530 px of vertical spacing. That is generous specimen spacing; it is not a production layout.
- **Unit:** each unit is an icon of about 130 px diameter, an approximately 40 px gap, then a text block. The title cap-height centre aligns with the upper third of the icon and the subtitle with the lower third, so the two lines straddle the icon centre.
- **Background:** flat #101113 covers 96% of the frame. There are no frames, cards or dividers.

## 3. Typography
- **Typeface:** Inter or a near clone, identifiable by the single-storey "g" with an open tail and the flat-terminal "t".
- **Title:** "Agent thinking.." at about 44 px Medium (500), #ffffff, tracking about −0.01 em.
- **Subtitle:** "State variant N" at about 36 px Regular in #8e8e8e.
- **Scale and copy:** a 1.22 ratio between title and subtitle, with hierarchy carried mostly by colour. The two-dot ellipsis ("..") reads as a typo rather than a deliberate rhythm.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #101113 | canvas | 96% |
| #ffffff | title, active line segments / dots | ~1% |
| #8e8e8e | subtitle, mid-state bands | 0.5% |
| #cccccc | bright-but-not-peak band | 0.3% |
| #545555 / #3b3d3d | idle line "track" | 0.8% |

WCAG checks:
- The title, #fff on #101113, is 18.89:1.
- The subtitle, #8e8e8e, is 5.77:1.
- The idle line tracks are #545555 at 2.53:1 and #3b3d3d at 1.73:1. They are decorative, but at 1 px they nearly vanish on low-quality displays.

## 5. Depth & material
- **Flat 2D.** The only illusion of volume is variant 1: horizontal bands that get thicker toward the equator and a darker elliptical "cap" at the top. Together they suggest a striped sphere seen from slightly above.
- There are no glows, shadows or blur.

## 6. Components & patterns
1. **Banded sphere:** about 6 horizontal bands. The luminance sweeps through the bands (dark grey → white → dark), like a fill rising and falling.
2. **Vertical-line circle with dots:** about 9 vertical 1.5 px lines, with three white dots (about 12 px) that bob along the lines in a wave, like a typing indicator rebuilt on a grid.
3. **Horizontal-line circle with dashes:** about 9 lines, with short white bars (about 30×8 px) sliding left and right on different lines. It reads as data "scanning".
4. **Vertical-line circle with bars:** white segments (about 8×30 px) travel up and down on alternate lines, like an equaliser.

Each variant pairs with a title and a subtitle. In a real UI the subtitle would carry the current tool step.

## 7. Motion
Measured (m0_motion.json, 30 fps, 6.10 s, seamless_loop_likely true, first/last diff 0.10):
- `motion_fraction` is 0.0 and p95 energy 0.32, below the 0.35 threshold, because the animated elements are tiny relative to the frame. The detector found no discrete segments, so the motion is continuous and low-amplitude.
- From the nine frames (0.68 s apart, estimates):
  - Variant 1's luminance cycle peaks white at about 2.37 s and 5.08 s, roughly a 2.7 s period, with symmetric ease-in-out.
  - Variants 3 and 4 move their segments every frame, at about 0.5–1 s per traverse, with linear or stepped travel.
  - Variant 2's dots shift phase each sample, in a wave of about 1 s.
- The whole 6.1 s clip loops cleanly.
- **Character:** calm and mechanical, with no overshoot or bounce. That suits "thinking" rather than "loading".

## 8. Brand system
n/a — this is a component specimen, not a brand system. Identity cues: a monochrome line-raster motif that could become an agent's "face" across a product.

## 9. UX
- A variant that conveys activity without implying progress is appropriate for indeterminate LLM work.
- Pairing the indicator with a text label is good for accessibility, because the state is not motion-only.
- **Risks:**
  - The idle tracks are under 3:1.
  - Four styles side by side invite inconsistency if all of them ship.
  - Users need `prefers-reduced-motion` fallbacks; a static striped glyph works as one.

## 10. Craft signals
- Every icon is clipped to the same ~130 px circle. The lines are cut by the circle edge, not inset.
- Line pitch is constant inside each variant: about 14 px for the vertical variants and about 12 px for the horizontal ones.
- Animation uses only luminance and position within one hue. There is no colour, so the indicator sits on any dark UI.
- The title/subtitle block is optically centred on the icon's vertical centre.
- The loop is seamless at 6.1 s.

## 11. Reproduction recipe
```css
:root{--bg:#101113;--fg:#fff;--fg-2:#8e8e8e;--track:#545555;--font:"Inter",system-ui}
.think{display:flex;align-items:center;gap:20px;font-family:var(--font)}
.think b{display:block;font:500 22px/1.2 var(--font);color:var(--fg)}
.think span{font:400 18px/1.3 var(--font);color:var(--fg-2)}
.orb{width:64px;aspect-ratio:1;border-radius:50%;position:relative;overflow:hidden;
  background:repeating-linear-gradient(90deg,var(--track) 0 1px,transparent 1px 7px)}
.orb i{position:absolute;left:var(--x);width:4px;height:14px;background:var(--fg);
  animation:bar 1.2s cubic-bezier(.45,0,.55,1) infinite alternate;animation-delay:var(--d)}
@keyframes bar{from{top:10%}to{top:75%}}
@media (prefers-reduced-motion:reduce){.orb i{animation:none;top:40%}}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 7 | Quiet, coherent monochrome set; specimen presentation is plain. |
| Originality | 7 | Line-clipped circles as a loader family is a fresh spin on dots/spinners. |
| Usability | 7 | Text plus indeterminate motion is right for agents; faint tracks and the ".." copy detract. |
| Craft | 7 | Consistent diameter and pitch; little polish beyond the glyphs. |

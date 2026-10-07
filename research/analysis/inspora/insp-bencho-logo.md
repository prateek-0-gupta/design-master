---
id: insp-bencho-logo
source: inspora
category: Branding
status: analyzed
title: "Bencho logo"
creator: "@cabralorenzo"
styles: [minimal-swiss, micro-interaction, monochrome, retro-pixel]
patterns: [interactive-logo-easter-egg, grab-to-stretch-mascot, nav-active-dim-inactive, app-window-corner-crop, hover-brighten-nav]
mode: dark
palette: ["#111113", "#ebebed", "#8e8e90", "#2d2c2e", "#606061"]
type_families: ["Inter / SF Pro Text-style neo-grotesk (likely)"]
type_class: [neo-grotesk, pixel]
radius_px: [72]
motion: {durations_s: [], easing: [], loop: true}
scores: {aesthetics: 8, originality: 8, usability: 7, craft: 8}
craft_signals: [goat-built-from-45-degree-blocks, logo-stretches-only-on-x, grab-cursor-signals-affordance, active-vs-inactive-by-grey-value-only, logo-cap-height-matches-nav, offwhite-not-pure-white]
anti_patterns: [hidden-interaction-undiscoverable, measured-motion-too-subtle-to-register]
---
# Bencho logo — @cabralorenzo

## 1. Snapshot
- **Subject:** A 9.4 s, 1720×1270 (60 fps) screen capture of the top-left corner of the "Bencho" app.
  - It shows an angular goat logomark next to a two-item nav, "Blocks" and "Bench".
  - The cursor turns into a grab hand over the goat, and dragging stretches the goat's body horizontally like taffy before it snaps back.
- **Why it's remarkable:** The logo is a toy. A hidden grab-and-stretch interaction gives a design tool personality without adding any UI.

## 2. Composition & layout
- **Frame:** the app window (#111113) sits on a #ebebed desktop. Its top-left corner is at about x=400, y=268 (of 1720×1270), with a large outer radius of about 72 px.
- **Header row:** baseline at about y=455.
  - The goat is about 190×155 px at x≈500–690.
  - "Blocks" starts at x≈865 and "Bench" at x≈1238.
  - The gap from the goat to the first nav item is about 175 px. The gap between nav items is about 135 px.
- Everything below the header is empty canvas. The composition is a crop designed to focus on the logo.

## 3. Typography
- The nav is set in a neo-grotesk (Inter or SF Pro-like) at about 72 px in the capture, which is about 18 px at 1x if the capture is at 4x zoom. The weight is regular-medium (about 450), with tight but default tracking.
- The cap height of "B" is about 58 px, and the goat's body block sits on the same baseline as the text, so mark and words share one line.
- The goat itself is pixel/stencil-like: built from straight-sided blocks with 45° cuts (horns, snout, legs), with no curves at all.

## 4. Colour
| Hex | Role | Share (key frame) |
|---|---|---|
| #111113 | app chrome (blue-tinted black) | 58% |
| #ebebed | desktop bg; logo and active nav (off-white) | 39% |
| #8e8e90 (est.) | inactive nav label | <1% |
| #2d2c2e / #606061 | antialias edges | 1% |

WCAG checks:
- Active nav (#ebebed on #111113) is 15.84:1.
- Inactive nav (#8e8e90) is 5.77:1, which passes AA while still clearly subordinate.
- The hover brightening goes toward #adadad (8.4:1) and then to full #ebebed.

Strategy: no hue at all. Every value has a slight cool cast (#111113, #ebebed) instead of neutral black and white.

## 5. Depth & material
None. The design is completely flat, with no shadows, borders or gradients. The window is separated from the desktop by value alone (15.84:1).

## 6. Components & patterns
- **Logomark:** a side-profile goat drawn as a single polygon.
  - two parallel horn bars;
  - a stepped snout;
  - a rectangular body;
  - four slanted 45° legs, in two pairs.
- **Nav state:** the active item is #ebebed and the inactive item is about #8e8e90. Hover on "Bench" lifts it to full white (frames 5.74 s and 8.87 s).
- **Easter egg:** hovering the goat shows the open-hand cursor (1.56 s, 4.69 s). On drag, the body lengthens from about 190 px to about 215 px (frames 2.61 s and 5.74 s, on x only); the head and legs keep their shapes and the torso rectangle extends.

## 7. Motion
The motion profile reports `motion_fraction 0.0`, mean energy 0.08 and `seamless_loop_likely: true`. The measured frame differences stay below the 0.35 threshold because only a ~200×150 px region changes in a 1720×1270 frame, so no segments were detected.

From the nine frames (spaced about 1.04 s apart), these are estimates:
- the stretch is about +13% body length;
- it holds while dragging and releases back to rest within about 1 s;
- the clip loops cleanly (first-to-last difference 0.07).

No easing can be measured. A spring-back (overshoot) would suit the idiom.

## 8. Brand system
n/a — not a full brand system. Identity cues:
- the goat is drawn from a 45°-and-90° grid only, like a pixel-font glyph;
- monochrome cool-grey palette;
- the brand personality lives in interaction (stretch), not in colour.

## 9. UX
- **Positive:** the cursor changes to a grab hand, which is a correct affordance, and the logo still works as a home link otherwise.
- **Risk:** the interaction is undiscoverable without the cursor change, and on touch it has no equivalent.
- The nav uses only value to show the active state (no underline or weight change). The 5.77:1 ratio is fine, but a weight or indicator would help low-vision users.

## 10. Craft signals
- The goat uses only 0°, 90° and 45° edges, so it renders crisply at small sizes.
- The stretch deforms only the torso rectangle; the horns, head and legs are preserved (9-slice style).
- The goat's body baseline aligns with the nav text baseline (about y=455).
- Off-white #ebebed is used instead of #fff on #111113, which reduces glare while keeping 15.8:1.
- Inactive nav grey sits about two-thirds of the way down the value scale (5.77:1), so it is subordinate and still AA.

## 11. Reproduction recipe
```css
:root{--chrome:#111113;--desk:#ebebed;--fg:#ebebed;--fg-dim:#8e8e90;--r-window:72px;
  --font:"Inter","SF Pro Text",system-ui,sans-serif;}
body{background:var(--desk)}
.window{background:var(--chrome);border-radius:var(--r-window) 0 0 0}
.nav a{font:450 18px/1 var(--font);color:var(--fg-dim);transition:color .15s ease-out}
.nav a[aria-current=page],.nav a:hover{color:var(--fg)}
.logo{cursor:grab;display:grid;grid-template-columns:auto var(--body,48px) auto}
.logo:active{cursor:grabbing}
.logo .torso{width:var(--body);transition:width .5s cubic-bezier(.34,1.56,.64,1)} /* spring back */
```
```js
// stretch torso with pointer drag, clamp to +25%
logo.onpointerdown=e=>{const x0=e.clientX;const move=m=>logo.style.setProperty('--body',Math.min(60,48+(m.clientX-x0)/4)+'px');
  addEventListener('pointermove',move);addEventListener('pointerup',()=>{removeEventListener('pointermove',move);logo.style.removeProperty('--body')},{once:true})}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | A strong, angular goat glyph in a calm monochrome frame. |
| Originality | 8 | A grab-to-stretch logo is a fresh, delightful easter egg. |
| Usability | 7 | Correct cursor affordance and AA nav; hidden on touch and value-only active state. |
| Craft | 8 | Baseline alignment, 45° grid and selective stretch; little else is shown to judge. |

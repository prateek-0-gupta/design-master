---
id: insp-multi-action-button
source: inspora
category: Motion
status: analyzed
title: "multi-action button"
creator: "@nickpylll"
styles: [micro-interaction, minimal-swiss, corporate-clean, x-backdrop-blur-menu]
patterns: [speed-dial-fab, fab-dissolves-into-menu, backdrop-blur-scrim, borderless-menu-items, colour-coded-action-icons, staggered-menu-reveal]
mode: light
palette: ["#f7f7f7", "#ffffff", "#060606", "#f26a3d", "#7b4dff", "#2f6bff", "#c4c4c8", "#5b5560"]
type_families: ["SF Pro Display / Text (likely)"]
type_class: [neo-grotesk]
radius_px: [9999, 24]
motion: {durations_s: [0.3, 0.2], easing: [ease-out], loop: true}
scores: {aesthetics: 8, originality: 7, usability: 7, craft: 8}
craft_signals: [fab-replaced-by-nearest-icon, menu-grows-from-fab-corner, background-gaussian-blur-instead-of-dim, labels-right-aligned-to-icons, gradient-duotone-icons, no-container-around-menu]
anti_patterns: [no-visible-close-affordance, orange-icon-low-contrast]
---
# multi-action button — @nickpylll

## 1. Snapshot
- **Subject:** A 2.47 s, 60 fps, 1080×1080 close-up of the bottom-right corner of a fintech app (balance cards, "Earn up to 7.80% APY" promo, a black "+" FAB). Tapping the FAB blurs the whole screen and fans out three labelled actions (Receive, Send, Swap) with no menu container. Tapping again collapses them back into the FAB.
- **Why it's remarkable:** The speed-dial has no background card, pills or circles behind the icons, just large text and colourful glyphs floating over a heavily blurred UI. The blur is the container.

## 2. Composition & layout
- The crop shows about 40% of the phone width. The FAB is a 72 px black circle (at 1080 capture, about 52 pt) inset about 30 px from the screen's rounded corner.
- **Expanded menu:** three rows right-aligned in a column, with icons at x≈620 and labels right-aligned at x≈535 (an icon-to-label gap of about 50 px). The rows are at y≈425 / 590 / 750, a **163 px pitch** (about 60 pt).
- The bottom row (Swap) occupies the FAB's former position, so the menu grows upward from the trigger.
- The labels and icons are about 1.4× larger than normal UI text, an accessibility-friendly target size.

## 3. Typography
- SF Pro Display. Labels are about 44 px at capture (about 20 pt) Regular/Medium, near-black #060606, with no tracking change.
- The underlying UI: balance "$3,498.41" in Semibold with a grey decimal part (".41" lighter grey), and the promo "Earn up to 7.80% APY" in 17 pt Regular.

## 4. Colour
| Hex | Role | Approx share |
|---|---|---|
| #f7f7f7 | stage outside the phone | 92% (key frame incl. blurred screen) |
| #ffffff | app surface (blurred) | — |
| #060606 | labels, FAB, bezel | 3.5% |
| #f26a3d | Receive icon (orange gradient) | <0.5% |
| #7b4dff | Send icon (violet paper plane) | <0.5% |
| #2f6bff | Swap icon (blue arrows) and blue promo icon | <0.5% |
| #c4c4c8 / #5b5560 | blurred UI greys, titanium bezel | 4% |

WCAG checks:
- Labels #060606 on white are 20.26:1.
- Icons against white: orange 3.04:1 (just passes the 3:1 graphics threshold), violet 4.83:1, blue 4.5:1.
- The FAB "+" is white on black at 20.26:1.

## 5. Depth & material
- **Expanded:** the entire app layer receives a strong Gaussian blur (about 20–30 px) with no darkening. The layer stays white and becomes frosted.
- The icons are filled with subtle vertical gradients (orange → lighter orange, violet → indigo, blue duotone), giving them a slightly 3D "app icon" quality without shadows.
- **Collapsed:** the FAB is flat black with a soft drop shadow (about 0 6px 16px rgba(0,0,0,.2)).
- Cards have about a 24 px radius with hairline #efefef borders.

## 6. Components & patterns
- **Speed dial with three actions:** a semantic colour per action (in = orange down-arrow, out = violet plane, convert = blue cycle arrows).
- The FAB "+" disappears on open rather than rotating to "×". The Swap icon takes its place.
- **Blur scrim:** tapping anywhere presumably dismisses. There is no explicit close.

## 7. Motion
- **Measured:** 2.47 s loop (`seamless_loop_likely: true`, diff 0.11) with motion fraction 0.21. Two segments:
  - **open 0.07–0.37 s (0.3 s, ease-out, peak 0.17)**;
  - **close 1.47–1.67 s (0.2 s, ease-out, peak 0.08)**.
  - Closing is about 33% faster than opening, which is correct asymmetry.
- **From frames (estimate):** at 0.14 s the items are at about 60% scale, clustered toward the FAB corner (Receive at y≈355, Swap at y≈448 in the frame) and partially transparent. By 0.41 s they reach full size and spread to the 163 px pitch, so items scale from about 0.6 to 1 and translate up and out from the FAB origin. At 1.51 s (closing) the items shrink back toward the corner and fade as the blur releases. By 1.79 s the FAB is back and the UI is sharp.
- The blur fades over the same window as the item motion.

## 8. Brand system
n/a — not a brand system. Cues:
- black primary FAB;
- a tri-colour action language (orange / violet / blue);
- a blue glossy brand mark on the promo card.

## 9. UX
- **Strengths:**
  - Large labels and spacing (about 60 pt rows) give easy targets.
  - Colour plus glyph plus label triple-codes each action.
  - The blur keeps context while removing noise.
  - The fast close respects the user's intent.
- **Risks:**
  - With no "×" there is no explicit dismiss, so users must guess to tap outside.
  - With no container, the items may lose legibility over busy, colourful content. The blur must be strong enough.
  - The orange icon sits at the 3:1 edge.

## 10. Craft signals
- The FAB vanishes and the nearest menu item (Swap) appears at its exact location, giving spatial continuity.
- Items emerge from the FAB corner (scale about 0.6 → 1 plus upward translate), not from screen centre.
- The backdrop is blurred but not dimmed, keeping a light, airy mode.
- Labels are right-aligned to a shared edge, about 50 px left of the icon column, giving a tidy ragged-left list.
- Icons share a gradient-fill style at one size (about 64 px at capture).
- The close is 0.2 s versus 0.3 s for the open.
- The balance shows decimals in grey (".41"), a typographic hierarchy for money.

## 11. Reproduction recipe
```css
:root{--ink:#060606;--recv:#f26a3d;--send:#7b4dff;--swap:#2f6bff;--font:-apple-system,"SF Pro Display",system-ui,sans-serif}
.app{transition:filter .3s cubic-bezier(.2,.8,.2,1)}
.app.menu-open{filter:blur(24px)}
.fab{width:52px;height:52px;border-radius:50%;background:var(--ink);color:#fff;box-shadow:0 6px 16px rgba(0,0,0,.2);
  transition:transform .2s ease-out,opacity .2s}
.menu-open .fab{transform:scale(.6);opacity:0}
.dial{position:fixed;right:20px;bottom:24px;display:grid;gap:28px;justify-items:end}
.dial button{display:flex;align-items:center;gap:20px;font:500 20px var(--font);color:var(--ink);background:none;border:0;
  transform-origin:100% 100%;transform:translate(0,calc(var(--i)*40px)) scale(.6);opacity:0;
  transition:transform .3s cubic-bezier(.2,.8,.2,1) calc((2 - var(--i))*30ms),opacity .3s}
.dial.open button{transform:none;opacity:1}
.dial:not(.open) button{transition-duration:.2s;transition-delay:0s}
.ico-recv{color:var(--recv)} .ico-send{color:var(--send)} .ico-swap{color:var(--swap)}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Airy and confident, with colourful glyphs over frosted white and no chrome clutter. |
| Originality | 7 | Containerless speed-dial over a blur is a fresh refinement of a familiar FAB pattern. |
| Usability | 7 | Big targets and triple-coded actions, but the dismiss affordance is implicit. |
| Craft | 8 | Origin-aware scaling, asymmetric open/close timing and the FAB-to-item handoff. |

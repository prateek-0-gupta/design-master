---
id: insp-1-61
source: inspora
category: Motion
status: analyzed
title: "Window controlled Dark mode"
creator: "@mjbarton_"
styles: [physical-material, skeuomorphic, micro-interaction]
patterns: [diegetic-theme-toggle, drag-window-shade, proportional-dim-during-drag, airplane-window-hero, timeline-flight-path, grab-cursor-affordance]
mode: mixed
palette: ["#f9f3f3", "#dadadb", "#c5bebb", "#96c9f4", "#1a1a1a", "#3e3e3e", "#757373", "#3d3dd6"]
type_families: ["Inter / Söhne-style grotesk (likely)", "JetBrains Mono-style monospace (likely)"]
type_class: [neo-grotesk, mono]
radius_px: [9999, 120]
motion: {durations_s: [0.37, 0.37, 0.5, 0.67], easing: [ease-in, ease-out, ease-in-out], loop: true}
scores: {aesthetics: 9, originality: 9, usability: 6, craft: 8}
craft_signals: [page-luminance-tracks-shade-position, grab-hand-cursor-on-shade, shade-visible-at-top-as-handle, accent-blue-lightened-for-dark, window-bezel-darkens-with-theme, sky-sliver-peeks-when-shade-lifts]
anti_patterns: [theme-toggle-not-discoverable, no-keyboard-equivalent-visible]
---
# Window controlled Dark mode — @mjbarton_

## 1. Snapshot
- **Subject:** A 7.1 s, 1132×720 clip of a portfolio hero (an airplane window above a "flight plan" timeline). The visitor grabs the window shade and pulls it down; the whole page dims to dark mode. Pushing it up restores light.
- **Why it's remarkable:** A diegetic theme switch. The control is an object in the hero illustration, and closing a cabin window shade is a universally understood "make it dark" gesture.

## 2. Composition & layout
- **Window:** The airplane window is centred at about 215×290 px (in the 1132 frame) with its top at y≈95. The shade is visible as a small lip of about 30 px at the top of the opening, which doubles as a handle.
- **Content block:** Title (≈20 px medium) and a two-line intro (≈18 px, centred, ≈545 px wide) sit about 85 px under the window.
- **Timeline:** The "FLIGHT PLAN" plane icon at x≈250 with a dashed curve leads into the timeline rail at x≈200, year "2025" at x≈160 and content at x≈226.
- This is the same site as insp-1-55 (Mike Barton portfolio). This clip isolates the theme interaction.

## 3. Typography
- **Grotesk (Inter or Söhne-like):** the title "Software Designer & Creative Technologist" is medium, about 20 px; the intro is regular, about 18 px with leading about 1.7, grey; "Studio" is about 19 px medium; "Lead Product Designer" is about 18 px medium.
- **Mono caps:** "FLIGHT PLAN" (≈8 px, tracked +0.15 em, accent blue), "CURRENT" (≈13 px accent), "NYC>MAN" over "2025" (≈13 px grey).
- Type does not change between themes except for colour inversion.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #f9f3f3 | light page | 90% (light) |
| #dadadb / #c5bebb | window bezel, shade plastic | 6% |
| #96c9f4 / #c2daec | sky through window | 1% |
| #1a1a1a | dark page | ~90% (dark) |
| #3e3e3e (approx) | dark-mode bezel | — |
| #757373 / #8a8a8a | body grey (light / dark) | 2% |
| #3d3dd6 → #4f6ef7 (approx) | accent, light → dark | <1% |

WCAG checks:
- **Light:** title #1a1a1a on #f9f3f3 is 15.86:1; body #757373 is 4.30:1 (large only).
- **Dark:** #e6e6e6 on #1a1a1a is 13.94:1; body #8a8a8a is 5.04:1; the lightened accent #4f6ef7 is 4.07:1.
- If the light accent #3d3dd6 had been kept in dark mode it would be 2.35:1, so the swap is justified.
- **Intermediate (2.76 s):** the page passes through a mid-grey (≈#d6d2d2) while the shade is half-drawn, so luminance is interpolated rather than flipped.

## 5. Depth & material
- **Window bezel:** rendered plastic: an outer cream ring with a soft outer halo, an inner moulded ring and a recessed opening.
- **Shade:** a matte plastic panel with a slight curved highlight along its lower lip.
- **Dark mode:** the bezel is re-lit as a dark grey ring with a faint rim glow, and the shade fills the opening in #2a2624 (warm brown-black).
- **Sky:** a photo of clouds and blue sky with a soft vignette.

## 6. Components & patterns
- **Diegetic toggle:** drag the shade down for dark, up for light. The cursor becomes a grab/hand on hover over the shade (0.39 → 1.97 s).
- **Proportional preview:** the page darkens as the shade moves (2.76 s mid-grey), then commits.
- **Peek:** at 5.92 s the shade is lifted slightly and a sliver of sky shows at the bottom, which gives tactile feedback.
- **Timeline:** company avatars overlap, "CURRENT" badge, dashed flight path.

## 7. Motion
Measured: 7.10 s at 60 fps, 4 segments, motion fraction 0.25, median 0.43 s, `seamless_loop_likely: true`.
- **1.93–2.30 s (0.37 s, peak 0.77 → ease-in):** The pull-down accelerates and the page begins dimming.
- **2.63–3.00 s (0.37 s, peak 0.32 → ease-out):** The shade snaps and the light/dark state commits (the frame at 3.55 s is briefly light again, consistent with a bounce or test pull).
- **3.80–4.30 s (0.50 s, symmetric):** The full close to dark mode.
- **5.73–6.40 s (0.67 s, peak 0.78 → ease-in):** The shade is pushed up and the page returns to light.
- **Theme cross-fade:** the background colour interpolation appears to span the drag itself (direct manipulation) plus about 0.3 s settle (estimate).

## 8. Brand system
n/a — not a brand system. Identity cues continue the travel metaphor of insp-1-55: cabin window, flight plan, route labels like "NYC>MAN".

## 9. UX
- **Strengths:**
  - The metaphor maps exactly to the outcome (shade down = dark).
  - Direct manipulation with a live preview.
  - The state is reversible by the same gesture.
- **Risks:**
  - There is no visible hint that the shade is interactive until hover, and none on touch.
  - It needs an accessible conventional toggle and `prefers-color-scheme` default.
  - Body grey in light mode is borderline.

## 10. Craft signals
- Page luminance interpolates with shade position (mid-grey state at 2.76 s) rather than snapping.
- The accent blue is lightened for dark mode (≈#3d3dd6 → #4f6ef7) to hold contrast.
- The window bezel itself re-renders dark, so the illustration participates in the theme.
- The shade lip is always visible in light mode as a natural drag handle.
- The cursor changes to an open hand over the shade.
- The shade lifted a few pixels reveals sky as tactile feedback.

## 11. Reproduction recipe
```css
:root{--t:0; /* 0 = shade up (light), 1 = shade down (dark); set from drag */
  --bg:color-mix(in oklab,#f9f3f3 calc((1 - var(--t))*100%),#1a1a1a);
  --ink:color-mix(in oklab,#1a1a1a calc((1 - var(--t))*100%),#e6e6e6);
  --body:color-mix(in oklab,#757373 calc((1 - var(--t))*100%),#8a8a8a);
  --accent:color-mix(in oklab,#3d3dd6 calc((1 - var(--t))*100%),#4f6ef7);}
body{background:var(--bg);color:var(--ink)}
.window{width:215px;height:290px;border-radius:120px/140px;position:relative;overflow:hidden;
  box-shadow:0 0 0 14px color-mix(in oklab,#e9e4e2 calc((1 - var(--t))*100%),#2b2b2b),0 0 40px rgba(0,0,0,.12)}
.shade{position:absolute;inset:0 0 auto;height:calc(12% + var(--t)*88%);background:#d9d4d0;cursor:grab;
  border-bottom:2px solid rgba(255,255,255,.6);transition:height .37s cubic-bezier(.2,.8,.2,1)}
.shade:active{cursor:grabbing;transition:none}
```
```js
shade.addEventListener('pointermove',e=>{ if(!dragging) return;
  const t=Math.min(1,Math.max(0,(e.clientY-top)/height)); document.documentElement.style.setProperty('--t',t); });
// on release: snap --t to 0 or 1 and persist; also expose <button aria-pressed> for keyboard users
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 9 | Calm warm-white and charcoal themes, both resolved, with a beautiful rendered window. |
| Originality | 9 | A cabin-shade theme toggle is a memorable, perfectly fitting metaphor. |
| Usability | 6 | Intuitive once found, but hidden, and it needs conventional and keyboard alternatives. |
| Craft | 8 | Interpolated luminance, an accent re-tuned for dark, and the illustration re-lit per theme. |

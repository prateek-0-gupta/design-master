---
id: insp-liquid-glass
source: inspora
category: Web
status: analyzed
title: "Liquid glass"
creator: "@jesse_vermeulen"
styles: [glassmorphism, photo-led, cinematic-3d, micro-interaction]
patterns: [refractive-dropdown, morphing-dropdown-panel, text-only-nav, chevron-rotate-on-open, staggered-item-fade, full-bleed-3d-backdrop]
mode: mixed
palette: ["#6581a3", "#8098b6", "#343f1d", "#676330", "#a6a469", "#ffffff"]
type_families: ["Inter (likely)"]
type_class: [neo-grotesk]
radius_px: [28]
motion: {durations_s: [0.67, 0.67, 0.63, 0.37, 0.33, 0.7], easing: [ease-out, ease-in-out], loop: false}
scores: {aesthetics: 8, originality: 7, usability: 5, craft: 7}
craft_signals: [displacement-refraction-not-blur, chromatic-fringe-at-edge, panel-morphs-between-triggers, chevron-flip-state, staggered-label-reveal]
anti_patterns: [legibility-depends-on-backdrop, refraction-noise-behind-text, no-hover-highlight-on-items]
---
# Liquid glass — @jesse_vermeulen

## 1. Snapshot
- **Subject:** A 15.8 s, 1960×1268 capture of a three-item text nav (Product / Resources / Company) whose dropdowns are panes of refractive "liquid glass". It sits over a slowly rotating 3D column of grass and rudbeckia flowers, against a clear sky.
- **Why it's remarkable:** The menu panel does not blur the backdrop like classic frosted glass. It distorts it with a lens displacement and chromatic edge fringing, an Apple-style "Liquid Glass" material rebuilt for the web. The single panel also slides and resizes between triggers instead of closing and reopening.

## 2. Composition & layout
- **Nav row:** centred horizontally at y≈415 px (key frame, which is native resolution). The items sit at x≈569, 843 and 1166, with a gap of about 275 px between label starts and no container behind them.
- **Dropdown:** anchored 75 px below the nav baseline (top at y≈490).
  - The Resources panel measures about 578×395 px.
  - Its left edge aligns about 65 px right of the trigger's left edge rather than flush, so it is offset toward the pointer.
  - Inner padding is about 50 px left, and item rows are spaced at a pitch of about 108 px in the key frame. In the sheet the pitch is ≈33 px at 1/3 scale, so ~100 px at native.
- **Backdrop:** The backdrop is the whole scene. The UI covers less than 15% of the frame.

## 3. Typography
- Inter-like neo-grotesk.
- **Nav labels:** about 36 px at native capture (≈18 CSS px at 2×), weight 600, white, with a small chevron of about 12 px placed 30 px after each label.
- **Dropdown items:** about 32 px native (≈16 CSS), weight 500, white.
- **Tracking and case:** Tracking is neutral, sentence case, with no secondary descriptions. There is only one type size relationship (1.125×), so hierarchy comes from position, not scale.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #6581a3 / #8098b6 / #708eaa | sky gradient (backdrop) | 49% |
| #343f1d / #212815 / #4e4c23 | foliage shadows | 21% |
| #676330 / #a6a469 / #8c7e44 | lit grass, flower ochres | 16% |
| #ffffff | all UI text | <2% |

WCAG checks (white text):
- On the dark sky #6581a3: **4.02:1**, AA-large only.
- On the light sky #8098b6: **2.96:1**, fail.
- On dark foliage #4e4c23: 8.82:1, pass.
- On lit grass #a6a469: **2.58:1**, fail.

Contrast swings from 2.6 to 8.8:1 depending on where the 3D column has rotated to. The nav has no scrim to stabilise it.

## 5. Depth & material
- **Panel material:**
  - The panel has a corner radius of about 28 px.
  - It shows near-zero blur but a strong refractive displacement. Grass blades swirl into concentric ripples, strongest near the edges (a lens profile).
  - A thin RGB chromatic fringe runs along the rim, visible at the bottom-left of the key frame.
  - A faint darkening tint of about 15% black helps the text.
- **Panel over sky:** At 2.63 s and 11.38 s, when the panel sits over the sky, it reads as a smooth grey-blue slab with a brighter top rim. This shows a specular highlight on the upper edge.
- **Backdrop:** An early shot (0.88–2.63 s) shows a glass pipe ring in the scene itself, so the art direction rhymes the UI glass with in-world glass.

## 6. Components & patterns
- A text nav with disclosure chevrons that flip up when open (visible on "Resources ^" at 4.38 s).
- Product shows 5 items (Overview, Features, Integrations, Changelog, Pricing), Resources 4 and Company 3. The panel height adapts to the item count.
- One shared panel morphs position and size between triggers (6.13 s Company leads to 7.88 s Resources, where the panel is mid-travel with labels fading).
- During transitions the items fade and stagger in top-to-bottom. "Documentation" is visible while "Guides" is still ghosted in the key frame.

## 7. Motion
Measured: 15.76 s at 55 fps, motion_fraction 0.25, 7 segments with a median of 0.67 s, not a loop (first/last diff 43.5).
- **Open or switch:** 2.73–3.40 s (0.67 s, peak 0.28, ease-out) and 6.07–6.73 s (0.67 s, peak 0.07, a strong ease-out).
- **Settle passes:** 3.67–4.33 s (0.67 s, peak 0.38) and 6.93–7.57 s (0.63 s, peak 0.50), both symmetric ease-in-out. These are likely the panel gliding and resizing to the new trigger plus the label stagger.
- **Quick switches:** 10.63–11.00 s (0.37 s) and 11.33–11.67 s (0.33 s), both symmetric.
- **Final:** 14.83–15.53 s (0.70 s, ease-out).

Pattern: about 0.35 s for a hover switch and about 0.65 s for the full open with stagger, always decelerating. Background rotation is too slow to register above the threshold.

## 8. Brand system
n/a — not a brand system. This is a component study with generic labels. Identity cues come from the nature-tech art direction: real flowers plus glass.

## 9. UX
- **Strengths:** The morphing single panel avoids flicker when the pointer sweeps across triggers (the Stripe pattern). The chevron state is explicit.
- **Risks:**
  - Text legibility is at the mercy of the moving backdrop. Refraction ripples directly behind 16 px labels add visual noise that blur would have suppressed.
  - There is no visible hover state on individual items.
  - The ghosted mid-transition labels (≈30% opacity) are unreadable for about 0.3 s.

## 10. Critical craft signals
- Displacement over blur: the backdrop detail is warped, not softened. Check the swirl in the grass inside the key-frame panel.
- A chromatic aberration fringe of 1–2 px on the lower panel rim.
- The panel position eases between triggers. At 7.88 s it sits between Resources and Company.
- The label stagger is top-down, about 60–80 ms per row (an estimate from the half-faded second row).
- The chevron rotates 180° on open.
- Panel height steps with item count (5/4/3 rows) while width holds at about 578 px.

## 11. Reproduction recipe
```html
<svg width="0" height="0"><filter id="lens" x="0" y="0" width="100%" height="100%">
  <feTurbulence type="fractalNoise" baseFrequency="0.008" numOctaves="2" seed="3" result="n"/>
  <feDisplacementMap in="SourceGraphic" in2="n" scale="38" xChannelSelector="R" yChannelSelector="G"/>
</filter></svg>
```
```css
:root{--r-glass:28px;--ink:#fff;--font:"Inter",system-ui,sans-serif}
.nav a{font:600 18px/1 var(--font);color:var(--ink);text-shadow:0 1px 8px rgb(0 0 0/.35)}
.nav [aria-expanded=true] .chev{transform:rotate(180deg);transition:transform .3s ease-out}
.panel{position:absolute;top:calc(100% + 38px);left:var(--x);width:var(--w);height:var(--h);
  border-radius:var(--r-glass);background:rgb(20 24 16/.18);
  backdrop-filter:url(#lens) saturate(1.2);/* Chromium only; fallback blur(14px) */
  box-shadow:inset 0 1px 0 rgb(255 255 255/.35),inset 0 0 0 1px rgb(255 255 255/.12),0 10px 30px rgb(0 0 0/.18);
  transition:left .65s cubic-bezier(.22,1,.36,1),width .65s cubic-bezier(.22,1,.36,1),height .65s cubic-bezier(.22,1,.36,1)}
.panel li{opacity:0;transform:translateY(6px);transition:opacity .25s ease-out,transform .25s ease-out;transition-delay:calc(var(--i)*70ms)}
.panel.open li{opacity:1;transform:none}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Lush, sunlit 3D backdrop and a glass panel that genuinely looks refractive. |
| Originality | 7 | An early, well-executed web take on the Liquid Glass material, combined with the known morphing-dropdown pattern. |
| Usability | 5 | White text over a moving, refracted photo ranges from 2.6 to 8.8:1. Item hover states are missing. |
| Craft | 7 | Lens displacement, chromatic rim and panel morph are careful. Mid-transition ghost labels feel unfinished. |

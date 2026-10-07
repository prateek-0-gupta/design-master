---
id: insp-1-4
source: inspora
category: Motion
status: analyzed
title: "Liquid gold"
creator: "@staromlynski"
styles: [luxury, physical-material, dark-premium, micro-interaction]
patterns: [gold-ring-active-tab, icon-tab-bar, theme-toggle-light-dark, camera-pan-showcase, hairline-dividers, squircle-active-tile]
mode: mixed
palette: ["#161616", "#1c1c1c", "#ebebeb", "#fefefe", "#949494", "#ffcc56", "#8f6f24", "#bdb7ad"]
type_families: []
type_class: []
radius_px: [9999, 48]
motion: {durations_s: [0.53, 0.37, 0.63, 0.53, 0.57, 0.43], easing: [ease-out, ease-in-out], loop: true}
scores: {aesthetics: 8, originality: 6, usability: 7, craft: 7}
craft_signals: [same-gold-in-both-themes, ring-reflections-flow, hairline-dividers-between-tabs, theme-toggle-icon-inverts, active-tile-recessed-in-light-raised-in-dark]
anti_patterns: [inactive-icons-3-to-1, low-res-capture]
---
# Liquid gold — @staromlynski

## 1. Snapshot
- **Subject:** A 960×720, 18.5 s, 30 fps showcase of a horizontal icon tab bar: dashboard, analytics, layers, wallet, plus a sun/moon theme toggle. The active tab is a squircle wrapped in a ring of flowing liquid gold. The camera pans along the bar and the scene flips between dark and light themes.
- **Why it's remarkable:** The gold is the single constant across both themes. On near-black it reads as jewellery; on white it reads as a brass inlay. Its reflections keep flowing, so the active state feels alive without any position or scale change.

## 2. Composition & layout
- **Framing:** a macro crop. The bar sits at the vertical centre (y≈230–485 in the key frame, ≈255 px tall) and is cut by the frame edges.
- **Camera pan:** the view pans horizontally between the active tab on the left and the theme toggle on the right (frames 3.08 s and 5.13 s show the right end).
- **Active tile:** a squircle of ≈200×200 px with a corner radius ≈48 px, inset ≈25 px from the bar's left end.
- **Tabs:** the inactive tabs sit on a ≈220 px pitch, separated by 1 px vertical hairlines ≈150 px tall.
- **Theme toggle:** a separate end-cap pill segment (darker in dark mode, grey #e0e0e0 in light mode) holding the sun or moon icon.

## 3. Typography
There is no text; the bar is icons only. The icons are a 1.5–2 px outline set, rounded, about 60 px. The active icon is pure black or white; inactive icons are mid-grey. The style is consistent with Lucide or Tabler line icons.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #161616 / #1c1c1c | dark-theme page and bar | ~75% in dark frames |
| #ebebeb / #fefefe | light-theme page and bar | 75% / 23% in the key frame |
| #949494 | inactive icons | <1% |
| #ffcc56 | gold specular highlight | <1% |
| #8f6f24 | gold shadow / body | <1% |
| #bdb7ad | warm grey reflection inside the ring | 2.6% |

WCAG checks:
- Active icon #1a1a1a on white: **17.26:1**.
- Inactive icons #949494 on white: **3.01:1**, just at the 3:1 graphic-object floor.
- Dark theme: inactive ≈#8a8a8a on #1c1c1c is 4.94:1; active white on #1c1c1c is 17.04:1.

The dark theme is actually the more legible one for inactive tabs.

## 5. Depth & material
- **Bar:** a raised pill in both themes, with a soft outer shadow and a 1 px lighter top highlight (light theme: white on #ebebeb with a ≈20 px shadow; dark theme: #1c1c1c with a darker drop and a subtle top rim).
- **Active squircle:**
  - in light mode it sits *recessed* inside a grey well, with an inner shadow ring around the white tile;
  - in dark mode it is a darker raised tile;
  - in both, the gold ring is ≈10 px thick.
- **Gold material:** a mix of saturated yellow highlights (#ffcc56), brown-olive shadows (#8f6f24) and white sparkle. The reflections occasionally show orange (#cd621c) at grazing angles. It reads as polished metal rather than flat yellow.

## 6. Components & patterns
- **Icon-only tab bar** (bottom-nav or toolbar), with dividers between items.
- **Active indicator:** a material ring instead of a fill or underline.
- **Theme toggle:** sun in dark mode, moon-and-sparkle in light mode. The icon shows the *target* theme.
- The showcase demonstrates that one component token set renders in both themes.

## 7. Motion
- **Measured:** 18.47 s at 30 fps. motion_fraction 0.16. Six segments:
  - 2.40–2.93 s (0.53 s, peak 0.09, **ease-out**);
  - 4.70–5.07 s (0.37 s, ease-out);
  - 5.90–6.53 s (0.63 s, symmetric);
  - 9.80–10.33 s (0.53 s, ease-out);
  - 11.63–12.20 s (0.57 s, ease-out);
  - 12.50–12.93 s (0.43 s, symmetric).
- seamless_loop_likely **true**.
- **Interpretation:**
  - The front-loaded ≈0.5 s segments are camera pans and the theme cross-fade. They have fast starts that decelerate into place: 2.4 s pans to the toggle, ≈4.7–5.1 s switches dark→light, ≈9.8 s pans back, ≈11.6–12.2 s switches light→dark.
  - Between the cuts, the gold ring's reflections drift continuously. The highlight positions differ in every frame (compare 13.34 s, 15.39 s and 17.44 s), with low energy below the threshold, so it is a slow ambient flow.

## 8. Brand system
n/a — not a brand system. The identity cue is a luxury fintech mood (gold plus wallet and analytics icons).

## 9. UX
- **Strengths:**
  - The active state is unmistakable in both themes.
  - The theme toggle placement at the end of the bar is conventional.
  - The 200 px tiles are generous targets.
- **Risks:**
  - Icon-only tabs need labels or tooltips.
  - The inactive icons are borderline in light mode.
  - Constant metallic shimmer may distract in a persistent nav bar.
- **Capture quality:** the 960×720 source is soft and limits detail assessment.

## 10. Craft signals
- The same gold ring material is used in dark and light themes with no recolouring.
- The ring's reflections drift between frames while its geometry is fixed.
- The active tile is recessed (inner shadow well) in light mode and raised in dark mode, a deliberate per-theme depth mapping.
- 1 px hairline dividers separate inactive tabs, with no backgrounds.
- The toggle shows the opposite theme's icon (sun in dark, moon in light).

## 11. Reproduction recipe
```css
@property --g{syntax:"<angle>";inherits:false;initial-value:0deg}
:root{--bg:#ebebeb;--bar:#fefefe;--icon:#949494;--icon-active:#1a1a1a}
[data-theme=dark]{--bg:#161616;--bar:#1c1c1c;--icon:#8a8a8a;--icon-active:#fff}
.bar{display:flex;align-items:center;height:128px;padding:0 12px;border-radius:9999px;background:var(--bar);
  box-shadow:inset 0 1px 0 rgba(255,255,255,.08),0 10px 24px rgba(0,0,0,.12)}
.tab{width:110px;height:100px;display:grid;place-items:center;color:var(--icon)}
.tab+.tab{border-left:1px solid color-mix(in srgb,var(--icon) 25%,transparent)}
.tab[aria-current]{color:var(--icon-active);border-radius:24px;position:relative}
.tab[aria-current]::before{content:"";position:absolute;inset:0;border-radius:inherit;padding:5px;
  background:conic-gradient(from var(--g),#8f6f24,#ffcc56,#fff6d8,#b8862b,#5b521b,#ffcc56,#8f6f24);
  -webkit-mask:linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);-webkit-mask-composite:xor;mask-composite:exclude;
  animation:flow 6s linear infinite}
@keyframes flow{to{--g:360deg}}
html{transition:background-color .5s cubic-bezier(.16,1,.3,1)}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Rich, restrained luxury; gold against greys works in both themes. |
| Originality | 6 | A metallic ring as active indicator is a known trend; the dual-theme demo is solid. |
| Usability | 7 | A clear active state and big targets, but no labels and borderline inactive contrast. |
| Craft | 7 | Thoughtful per-theme depth; the low-res capture hides finer detail. |

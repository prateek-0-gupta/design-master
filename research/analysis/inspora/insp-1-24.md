---
id: insp-1-24
source: inspora
category: Motion
status: analyzed
title: "Spider-Man web dropdown"
creator: "@nurpraditya"
styles: [dark-premium, micro-interaction, x-themed-ui]
patterns: [radial-fab-menu, web-shot-reveal, themed-dropdown, hover-row-highlight, fab-icon-morph, glass-menu-panel]
mode: dark
palette: ["#0a0813", "#0f0d18", "#1e1c25", "#260e19", "#cd1038", "#eeedf2", "#6f5a5e"]
type_families: ["Inter (likely)"]
type_class: [neo-grotesk]
radius_px: [9999, 16]
motion: {durations_s: [1.1, 0.7, 0.9, 0.93, 1.83], easing: [ease-out, ease-in], loop: true}
scores: {aesthetics: 7, originality: 8, usability: 6, craft: 7}
craft_signals: [web-anchors-to-fab, red-icon-tint-per-item, hover-row-red-wash, fab-icon-crosshair-to-close, line-shot-trail-before-open]
anti_patterns: [web-lines-cross-label-text, theme-over-function]
---
# Spider-Man web dropdown — @nurpraditya

## 1. Snapshot
- **Subject:** A 1282×720, 21 s loop. A glossy red circular button with a crosshair icon "shoots" a web line. On click, a 3-item menu (Web Shooter, Spider-Sense, Swing) opens above it, suspended in a white spider web that anchors to the button. Closing retracts the web.
- **Why it's remarkable:** The menu's open transition is the theme. The web replaces a generic scale/fade, with strands radiating from the FAB, which acts as the anchor point.

## 2. Composition & layout
- **Canvas:** #0a0813 (near-black violet). The FAB is about 58 px in diameter, centred at (640,470) in the key frame.
- **Menu panel:** above the button at x≈500→780 (280 px), y≈228→410 (182 px), radius about 16 px. It holds three rows of about 47 px height, at y≈270, 318 and 365.
  - Each row: a red icon of about 16 px at x≈542, then the label at x≈568.
- **Web:** spans x≈380→930 (550 px, about 2× the menu width), with its hub at the FAB. Its radial strands converge on the button, and the spiral threads connect the strands across the panel.
- **Variant:** in early frames (t=1.16 s) the FAB is bottom-left with a diagonal web line shot to the upper right before the menu forms, a shoot-then-pull narrative.

## 3. Typography
- Inter-like neo-grotesk, regular, about 20 px, colour #eeedf2. Three single-word or hyphenated labels with sentence-case capitals ("Spider-Sense").
- No secondary text.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #0a0813 | canvas | 93.6% |
| #0f0d18 / #1e1c25 | menu panel (translucent dark glass) | about 2.6% |
| #260e19 / #431523 | hovered-row red wash | about 3% |
| #cd1038 | FAB red, item icons | small |
| #eeedf2 | labels, web strands (about 70% opacity) | — |
| #6f5a5e | web strands mid-tone | 0.6% |

WCAG checks:
- Labels #eeedf2 on panel #0f0d18: 16.53:1.
- Red icons #cd1038 on #0a0813: 3.53:1, adequate for graphical objects (≥3:1).

## 5. Depth & material
- **FAB:** glossy sphere-like button with a top highlight, a darker bottom, and a red glow halo of about 20 px blur beneath.
- **Panel:** dark translucent glass with a subtle 1 px lighter border. The web lines pass both behind and in front of it (strands visibly overlay the label area), which creates a tangle depth.
- **Hovered row:** a red gradient wash (#260e19 → transparent) behind the row.

## 6. Components & patterns
- A FAB that opens an anchored dropdown upward.
- FAB icon swap: crosshair (closed) ↔ X-in-box (open).
- Hover state: the row gets a red wash (frames at t=10.48 s and 15.14 s show "Swing" highlighted).
- Themed reveal: the web forms from the FAB outward, then the panel fades in.

## 7. Motion
- **Measured:** 20.97 s, `motion_fraction` 0.33, `seamless_loop_likely: true` (first/last difference 0.01). 11 segments, median 0.70 s.
  - Opens: 1.30 s (1.10 s, `peak_at` 0.29), 7.20 s (0.90 s, 0.28) and 13.97 s (0.93 s, 0.09). These are ease-out: the web shoots fast and settles.
  - Closes: 4.10 s, 10.83 s and 15.83 s (each 0.70 s, `peak_at` 0.98). These are ease-in: the web slowly gathers, then snaps shut.
  - The last 17.70–19.53 s segment (1.83 s, ease-in) is a longer collapse with a strand drawing in (frame at t=19.80 s shows half-formed strands).
- Short 0.10 s blips (0.87 s, 7.00 s) are click flashes on the FAB.

## 8. Brand system
n/a — not a brand system (a fan-themed concept). Identity cues: red #cd1038 on deep violet-black, web line-art.

## 9. UX
- The menu itself is a clean 3-row list with good contrast and a visible hover state.
- The web adds about 0.9–1.1 s before the menu is fully usable, which is too slow for repeated use.
- Web strands cross the labels, adding visual noise.
- The FAB icon change (crosshair → close) clearly signals the toggle.

## 10. Craft signals
- The web hub sits exactly at the FAB centre, and the radial strands converge there.
- Icon colour (#cd1038) matches the FAB red and the hover wash hue.
- The open (ease-out, about 1.0 s) and close (ease-in, 0.7 s) curves are deliberately asymmetric.
- The FAB has a soft red glow, used as the only light source in the scene.
- The FAB icon morphs between states (crosshair ↔ close).

## 11. Reproduction recipe
```css
:root{--bg:#0a0813;--panel:rgba(20,17,30,.82);--red:#cd1038;--text:#eeedf2;--r:16px}
.fab{width:58px;height:58px;border-radius:50%;background:radial-gradient(circle at 40% 30%,#ff4d6d,var(--red) 60%,#7a0820);
  box-shadow:0 8px 24px rgba(205,16,56,.45)}
.menu{width:280px;padding:16px;border-radius:var(--r);background:var(--panel);border:1px solid rgba(255,255,255,.06);
  backdrop-filter:blur(8px);transform-origin:50% 100%;opacity:0;transform:translateY(16px) scale(.92);
  transition:opacity .35s .55s,transform .45s .55s cubic-bezier(.16,1,.3,1)}
.menu.open{opacity:1;transform:none}
.menu li{display:flex;gap:12px;height:47px;align-items:center;border-radius:10px;color:var(--text);font:400 20px Inter}
.menu li:hover{background:linear-gradient(90deg,rgba(205,16,56,.25),transparent)}
.menu li svg{color:var(--red)}
.web path{stroke:rgba(238,237,242,.7);stroke-width:1;stroke-dasharray:var(--len);stroke-dashoffset:var(--len);
  transition:stroke-dashoffset .9s cubic-bezier(.16,1,.3,1)}
.open .web path{stroke-dashoffset:0}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 7 | Moody red-on-violet with delicate line art, though busy around the labels. |
| Originality | 8 | A web as the dropdown transition is a memorable themed metaphor. |
| Usability | 6 | Readable menu, but the slow reveal and strand clutter hurt it. |
| Craft | 7 | Anchored geometry and asymmetric easing; web overlap could be cleaner. |

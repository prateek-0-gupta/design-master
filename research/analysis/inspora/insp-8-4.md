---
id: insp-8-4
source: inspora
category: Motion
status: analyzed
title: "Same element, new position."
creator: "@shawn_kel"
styles: [minimal-swiss, micro-interaction, flat-illustration]
patterns: [shared-element-layout-transition, segmented-view-switcher, list-card-stack-views, skeleton-placeholder-text, sliding-pill-indicator]
mode: light
palette: ["#ffffff", "#111111", "#e7e7e7", "#8a8a8a", "#2ea867", "#f5d43b", "#8a3643"]
type_families: ["Inter / SF Pro-style neo-grotesk (likely)"]
type_class: [neo-grotesk]
radius_px: [9999, 4]
motion: {durations_s: [0.33, 0.27, 0.3, 0.3, 0.33, 0.33, 0.37], easing: [ease-in-out, ease-out], loop: false}
scores: {aesthetics: 7, originality: 6, usability: 8, craft: 8}
craft_signals: [thumbnails-morph-between-layouts, pill-indicator-slides-between-tabs, skeleton-bars-reflow-with-items, image-is-only-colour, consistent-0.3s-duration, stack-view-rotates-items]
anti_patterns: [inactive-tab-label-3.45-to-1]
---
# Same element, new position. — @shawn_kel

## 1. Snapshot
- **Subject:** A 12.9 s, 1282×720 screen capture of a "Collectibles" panel with a three-way switcher (List view / Card view / Pack view). The same two illustrated artworks fly and resize between a list row, a two-up card grid and a stacked "pack" pile.
- **Why it's remarkable:** It demonstrates shared-element layout animation in its purest form. Everything except the two artworks is greyscale skeleton, so the eye tracks object continuity across three layouts.

## 2. Composition & layout
- **Panel:** about 510 px wide (x 382→890), left-aligned in a white frame with generous empty space.
- **Header:** "Collectibles" at y≈147, the segmented control at y≈193, and a 1 px hairline divider at y≈229.
- **List view:** 76 px square thumbnails, 10 px apart vertically, each followed by two skeleton bars (200×20 and 75×20 px) and a right-aligned price bar (64×20 px).
- **Card view:** two artworks of about 245×245 px side by side with a ~12 px gutter, with skeleton bars beneath.
- **Pack view:** both artworks shrink to about 90 px, stack with slight opposing rotations (about ±8°) and centre under the tabs with a single caption skeleton.

## 3. Typography
- **Typeface:** a neo-grotesk, Inter or SF Pro.
- **Title:** "Collectibles" about 16 px Medium in #111.
- **Tab labels:** about 14 px Regular. The active tab is #111 on a #e7e7e7 pill (about 98×30 px, radius 9999); inactive tabs are #8a8a8a.
- All other text is replaced by skeleton bars, which isolates the motion lesson.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #ffffff | canvas | 96.5% |
| #e7e7e7 / #f1f2f2 | active pill, skeleton bars, divider | 2.1% |
| #111111 | title, active label | <0.5% |
| #8a8a8a | inactive tab labels | <0.3% |
| #2ea867 / #f5d43b / #8a3643 | artwork colours (green, yellow, maroon) | ~1% |

WCAG checks:
- The active label (#111 on #e7e7e7) is 15.27:1.
- Inactive labels (#8a8a8a on white) are **3.45:1**, so they pass only as large text.
- The skeleton bars (#e7e7e7 on white) are 1.24:1, placeholders by design.

## 5. Depth & material
- Completely flat: no shadows, no borders except the hairline divider.
- The artwork tiles have about 4 px radius. In pack view the overlapping rotation implies stacking, without a shadow.

## 6. Components & patterns
- **Segmented control:** a sliding pill background indicator (the active state moves with the selection).
- **Collection layouts:** list (dense), card (visual) and pack (summary).
- **Shared-element morph:** each artwork keeps its identity and interpolates position, size and rotation. Skeleton rows fade or reflow around it.

## 7. Motion
Measured (m0_motion.json, 30 fps, 12.9 s, motion_fraction 0.25, not loop-seamless). There are 12 segments with a median of **0.30 s**:
- 2.03–2.37 s (0.33 s, peak 0.35), list → card;
- 2.97–3.23 s (0.27 s), card → pack;
- 3.90–4.20 s (0.30 s, peak 0.28, ease-out);
- 4.57–4.87 s (0.30 s);
- 5.23–5.57 s (0.33 s);
- 5.77–6.10 s (0.33 s);
- 8.40–8.77 s (0.37 s, peak 0.32, ease-out);
- 11.40–11.77 s (0.37 s).

Most segments are symmetric ease-in-out (peak 0.35–0.56), with a few ease-out. Durations are consistently 0.27–0.37 s, which suggests a single spring or tween token of about 0.3 s. The 0.10 s micro-segments (6.97 s, 10.60 s) are the pill indicator hopping on hover or click. Thumbnails and skeleton bars move in sync, with no visible stagger.

## 8. Brand system
n/a — this is an interaction study, not a brand system. Identity cue: bold flat illustration (green/yellow/red/purple) as the only colour in an otherwise colourless UI.

## 9. UX
- **Strengths:**
  - Object constancy across views prevents the "where did my item go" reset.
  - The segmented control has a clear active state.
  - The 0.3 s timing is fast enough for repeated switching.
- **Risks:**
  - Inactive tab labels are only 3.45:1.
  - The pack view hides individual items, so it needs a count.
  - It needs `prefers-reduced-motion` handling to cross-fade instead of fly.

## 10. Craft signals
- Artworks morph position, size and rotation continuously between all three layouts. They never cut.
- The active tab pill slides rather than appearing, and its width adapts to the label.
- Every segment duration falls in a 0.27–0.37 s band, one timing token.
- The hairline divider stays fixed while content reflows below it.
- Skeleton bars keep consistent heights (20 px) and radius across views.

## 11. Reproduction recipe
```css
:root{--ink:#111;--muted:#8a8a8a;--fill:#e7e7e7;--dur:.3s;--ease:cubic-bezier(.4,0,.2,1);--font:"Inter",system-ui}
.tabs{position:relative;display:flex;gap:8px;font:400 14px/1 var(--font)}
.tabs button{padding:8px 20px;border-radius:9999px;color:var(--muted);background:none}
.tabs button[aria-selected=true]{color:var(--ink);background:var(--fill)}
.item img{border-radius:4px;view-transition-name:var(--vt)}   /* --vt:art-1, art-2 per item */
.list .item img{width:76px}.cards .item img{width:245px}
.pack .item img{width:90px;position:absolute}.pack .item:nth-child(2) img{rotate:8deg}
::view-transition-group(*){animation-duration:var(--dur);animation-timing-function:var(--ease)}
.skel{height:20px;border-radius:4px;background:var(--fill)}
@media (prefers-reduced-motion:reduce){::view-transition-group(*){animation-duration:0s}}
```
JS: `document.startViewTransition(()=>root.className=next)`. Alternatively, use Framer Motion `layoutId` per artwork.

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 7 | Very clean; illustrations pop against grey skeleton; intentionally spare. |
| Originality | 6 | Shared-element view switching is established; the pack view adds a twist. |
| Usability | 8 | Object constancy plus fast, consistent timing; inactive labels a bit faint. |
| Craft | 8 | Single timing token, sliding indicator, smooth multi-property morphs. |

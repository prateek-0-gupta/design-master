---
id: insp-composer-mockup
source: inspora
category: Motion
status: analyzed
title: "composer mockup"
creator: "@SebCornelius"
styles: [dark-premium, micro-interaction, x-macos-utility-window]
patterns: [floating-composer-window, drop-files-to-attach, auto-reflow-media-grid, perspective-drop-landing, disabled-to-enabled-cta, dot-matrix-loader, multi-network-toggle, split-action-queue-select]
mode: dark
palette: ["#1c1a1b", "#2e2e30", "#f5f5f5", "#5ea2f0", "#2f8af5", "#e37763", "#666a7d", "#3f6679"]
type_families: ["Inter (likely)"]
type_class: [neo-grotesk]
radius_px: [60, 36, 16]
motion: {durations_s: [0.6, 0.47, 0.37, 0.57, 0.13, 0.17], easing: [ease-out], loop: true}
scores: {aesthetics: 8, originality: 7, usability: 7, craft: 8}
craft_signals: [media-tile-lands-with-perspective-tilt, grid-reflows-1-2-3-up, cta-dims-when-empty, dot-matrix-5x5-sending-state, concentric-radii-card-tiles-buttons, placeholder-hints-drop-files]
anti_patterns: [white-on-blue-cta-3-46, disabled-cta-2-22]
---
# composer mockup — @SebCornelius

## 1. Snapshot
- **Subject:** A 9.65 s, 2160×2160 loop of a dark floating composer (X + Threads) over a sunset-mountain wallpaper: text is typed, three images are dropped in and reflow into a grid, "Drop it" sends with a 5×5 dot-matrix loader, and the card resets.
- **Why it's remarkable:** Each attachment lands with a brief perspective tilt (like a card dropped onto a table) and the grid re-tiles 1 → 2 → 1+2 automatically, so adding media feels physical.

## 2. Composition & layout
- Card ≈975 px wide centred on the frame (x≈555→1530), height grows with content from ≈640 px (text only) to ≈1270 px (3 images).
- Internal padding ≈50 px; header row (network icons left, "⋯" and "✕" 66 px grey circles right) at y≈500.
- Body text block starts ≈110 px below the header; media grid sits ≈70 px below the text with a 20 px gutter; 3-up layout = one tall left tile (≈425×555) + two stacked right tiles (≈425×265).
- Footer: "+" square (≈95 px), "Queue ▾" select (≈490 px), "Drop it" CTA (≈245 px), all ≈100 px tall, 20 px gaps.

## 3. Typography
- Inter-like neo-grotesk. Body ≈46 px regular, leading ≈1.3, #f5f5f5; hashtag in #5ea2f0.
- Placeholder "Write your message or drop files" ≈38 px grey — the copy itself teaches the drop affordance.
- Footer labels ≈46 px medium.

## 4. Colour
| Hex | Role | Share (key frame) |
|---|---|---|
| #e37763 | wallpaper sky (context) | 19% |
| #666a7d / #3f6679 | wallpaper ridges | 18% |
| #1c1a1b | card surface | 15% |
| #2e2e30 | footer controls | — |
| #f5f5f5 | body text, icons | — |
| #5ea2f0 | hashtag | — |
| #2f8af5 | primary CTA | — |

WCAG (contrast.py):
- Body #f5f5f5 on #1c1a1b: 15.88:1; "Queue" white on #2e2e30: 13.55:1.
- Hashtag #5ea2f0 on #1c1a1b: 6.51:1.
- CTA white on #2f8af5: **3.46:1** (passes only as large text — fine at 46 px, but not at typical UI sizes).
- Disabled CTA (≈#4f6a8c on #1d3557): 2.22:1 — expected for disabled.
- Placeholder ≈#6b6b6b: 3.25:1.

## 5. Depth & material
- Card has a 2 px near-black outer stroke plus a soft ≈40 px shadow onto the wallpaper — macOS utility-window feel.
- Controls are flat #2e2e30 with a 1 px lighter top edge; no gradients except the wallpaper.
- Depth appears only during motion: dropped images tilt in 3D before flattening.

## 6. Components & patterns
- **Multi-network toggle:** X (active, white) and Threads (inactive, grey) logos as a header switch.
- **Media grid** with auto layout per count (1 = full width, 2 = halves, 3 = tall + 2 stacked), tile radius ≈36 px inside a ≈60 px card (concentric).
- **Split action:** "Queue" select beside "Drop it" — schedule vs. post now.
- **CTA states:** disabled dim navy with grey label when empty → bright blue once text exists.
- **Sending state:** card content clears to a centred 5×5 dot-matrix glyph animating like a pixel progress indicator, then resets to the placeholder.

## 7. Motion
Measured (m0_motion.json): 9.65 s at 60 fps, motion_fraction 0.26, seamless_loop_likely true, 8 segments, median 0.27 s.
- 2.23–2.83 s (0.60 s, peak 0.31, ease-out): first image drops in — the f2 frame at 2.68 s catches it tilted ≈5° with keystone perspective; the card grows taller in the same move.
- 3.20–3.67 s (0.47 s, ease-out) and 5.33–5.70 s (0.37 s, ease-out): second/third images and grid reflow, then the content-to-loader collapse.
- 1.70–1.83, 3.97–4.07, 4.23–4.40 s (0.10–0.17 s): small snaps (CTA enable, tile settle).
- 6.33–6.47 s (0.13 s, peak 0.88, ease-in): loader state change; 8.63–9.20 s (0.57 s, ease-out): card resets to empty composer.
Every substantive move is ease-out with energy peaking in the first third — fast arrival, soft settle.

## 8. Brand system
n/a — not a brand system. Identity cues: the cheeky "Drop it" verb and the dot-matrix loader.

## 9. UX
- Clear state model: empty → composing → attached → sending → reset; the CTA communicates readiness.
- Auto grid removes layout decisions from the user.
- Risks: blue CTA contrast is borderline; no visible per-image remove control; the loader hides the post content, so there is no preview of what was sent.

## 10. Craft signals
- Concentric radii: card ≈60 px, tiles ≈36 px, controls ≈16 px, with ≈50 px card padding.
- Dropped tiles arrive with a keystone tilt and flatten in ≈0.6 s.
- Grid re-tiles automatically for 1, 2 and 3 images.
- Disabled CTA keeps its blue hue at low luminance rather than going grey, so it is recognisably the same button.
- Footer controls share one 100 px height.

## 11. Reproduction recipe
```css
:root{--card:#1c1a1b;--ctl:#2e2e30;--text:#f5f5f5;--link:#5ea2f0;--cta:#1f7ae0;--cta-off:#1d3557;
  --r-card:60px;--r-tile:36px;--r-ctl:16px;--ease:cubic-bezier(.2,.8,.2,1)}
.composer{background:var(--card);border-radius:var(--r-card);padding:50px;box-shadow:0 0 0 2px #0a0a0a,0 30px 60px rgba(0,0,0,.35);
  transition:height .5s var(--ease)}
.media{display:grid;gap:20px;grid-template-columns:1fr 1fr;grid-auto-rows:265px}
.media:has(> :only-child){grid-template-columns:1fr}
.media:has(> :nth-child(3)) > :first-child{grid-row:span 2}
.media > *{border-radius:var(--r-tile);animation:land .6s var(--ease)}
@keyframes land{from{transform:perspective(900px) rotateX(18deg) rotateZ(-4deg) scale(1.06);opacity:0}to{transform:none;opacity:1}}
.cta{background:var(--cta);color:#fff;border-radius:var(--r-ctl);height:100px}
.cta:disabled{background:var(--cta-off);color:#4f6a8c}
```
(CTA darkened to #1f7ae0 to reach 4.5:1 with white.)

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Tight dark utility window over a warm wallpaper; flat illustrated media pops. |
| Originality | 7 | Familiar composer; the perspective landing and dot-matrix sender are the fresh parts. |
| Usability | 7 | Clear states and auto layout; CTA contrast and no remove control. |
| Craft | 8 | Concentric radii, consistent control heights, crisp ease-out timings. |

---
id: insp-3-5
source: inspora
category: Motion
status: analyzed
title: "Notification Cards"
creator: "@its_sslvr"
styles: [aurora-glow, gradient-mesh, soft-3d]
patterns: [pill-notification-stack, gradient-flame-accent, inverted-lead-card, brand-asterisk-wordmark, ambient-gradient-loop]
mode: light
palette: ["#edeef3", "#212123", "#f3f3f5", "#fcfcfc", "#ee1db9", "#f79347", "#36cdfa", "#e6afb5"]
type_families: ["Inter / SF Pro Display-style neo-grotesk (likely)"]
type_class: [neo-grotesk]
radius_px: [9999]
motion: {durations_s: [12.13], easing: [linear], loop: true}
scores: {aesthetics: 8, originality: 6, usability: 6, craft: 7}
craft_signals: [gradient-confined-to-right-third, inverted-first-card-for-priority, tracked-uppercase-meta, hue-coded-per-sender, soft-diffuse-shadow]
anti_patterns: [low-contrast-meta-on-light-cards, notifications-without-timestamp-or-action]
---
# Notification Cards — @its_sslvr

## 1. Snapshot
- **Subject:** A 12.1 s, 1920×1080 loop of three stacked pill notifications ("POLAR.*", "DUBDOT*", "VERCEL.*"). Each pill has a smeared, flame-like gradient in its right third that drifts constantly.
- **Why it's remarkable:** Each notification gets its own colour identity from a living gradient rather than from an icon or avatar. The type stays strictly achromatic.

## 2. Composition & layout
- **Stack:** Three pills are centred horizontally (x≈642→1276), so each is about 634×173 px. They have a vertical gap of about 67 px, and the block occupies y≈212→865, about 60% of the frame height.
- **Text column:** It starts about 60 px inside the left cap. The gradient starts at about 50% of the pill width and saturates toward the right cap.
- **Reading order:** The dark first card (#212123) breaks the rhythm, so the eye lands on it first and then falls down the light cards.

## 3. Typography
- **Title:** Neo-grotesk in Bold (about 700), with a cap height of about 38 px (font size ≈52 px) and slight negative tracking. Each wordmark ends in "*" or ".*" as a quirky brand tic.
- **Meta line:** About 18 px semibold uppercase, tracked at roughly +0.06 em, in grey. Title and meta are separated by about 12 px.
- **Hierarchy:** Two levels only, and it works at a glance.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #edeef3 | canvas (cool grey) | 88% |
| #212123 | lead card surface | 2% |
| #f3f3f5 / #fcfcfc | light card surfaces | 3% |
| #ee1db9 → #f79347 | Polar gradient (magenta→orange→yellow) | 1% |
| #36cdfa | Dubdot gradient (cyan) | 1% |
| #e6afb5 + cyan/yellow | Vercel gradient (pastel rainbow) | 1% |

WCAG:
- White title on #212123 is 16.07:1, and grey meta #8e8e93 on #212123 is 4.93:1 (both pass).
- Dark title #111 on #f3f3f5 is 17.04:1.
- Grey meta #8e8e93 on #f3f3f5 is **2.94:1 (fails)**, and on #fcfcfc it is 3.18:1 (fails at this size).

## 5. Depth & material
- **Shadows:** Each pill has a very wide, low-opacity drop shadow (about 0 30px 60px rgba(0,0,0,.08)). There are no borders.
- **Gradient:** It reads as blurred light (no grain) and is masked by the pill shape, so the right cap appears to glow from inside.
- **Elevation:** The light cards differ from the canvas by only about 2–4% lightness. The shadow does all the separation.

## 6. Components & patterns
- Pill notification with a sender wordmark plus a one-line event ("You made a sale", "$2000 commission", "Deployment in 24h").
- The inverted (dark) card marks the newest or most important item.
- There is no icon, timestamp, or dismiss control. This is a pure visual study.

## 7. Motion
- **Measured:** The duration is 12.13 s at 30 fps. motion_fraction is 0.0 and mean energy 0.05, so no segment crosses the 0.35 threshold. In other words, the motion is a slow, continuous, low-amplitude drift with no discrete events. `seamless_loop_likely: true` (first–last diff 0.8).
- **Frames (estimate):** The 9 frames show the gradient flames re-forming. Polar shifts from magenta-dominant (t=0.67 s) to orange/yellow (t=8.76 s). Vercel moves from rainbow to warm yellow (t=10.11 s).
- **Behaviour:** It is a noise-driven shader or animated blurred blobs on a roughly 10–12 s cycle, linear in time. The pills themselves never move.

## 8. Brand system
n/a — not a brand system. Identity cues: each sender is mapped to a gradient "aura" (Polar = fire, Dubdot = ice, Vercel = prism), and the asterisk suffix acts as a pseudo-brand mark.

## 9. UX
- The colour aura makes senders recognisable at a glance.
- The ambient motion is calm enough for a persistent surface.
- **Missing:**
  - timestamps;
  - actions;
  - unread or read state.
- The light-card meta text fails contrast.
- A constantly animated gradient behind notifications should respect `prefers-reduced-motion`.

## 10. Craft signals
- The gradient is confined to the right ~45% of each pill, so it never sits behind text.
- The first card is inverted (#212123) while the other two stay light. That is priority shown by value alone.
- The meta line is uppercase and tracked and remains readable at about 18 px.
- The pills share an identical radius (full) and identical 67 px gaps.
- The gradient bleeds to the pill's right edge with no inner stroke, which reads as light, not paint.

## 11. Reproduction recipe
```css
:root{--bg:#edeef3;--card:#fcfcfc;--card-ink:#212123;--meta:#6e6e73;}
body{background:var(--bg);font-family:Inter,system-ui,sans-serif}
.note{position:relative;width:634px;height:173px;border-radius:9999px;overflow:hidden;
  background:var(--card);box-shadow:0 30px 60px rgba(20,20,40,.08);padding:0 60px;
  display:flex;flex-direction:column;justify-content:center}
.note--lead{background:var(--card-ink);color:#fff}
.note h4{font:700 52px/1 Inter;letter-spacing:-.02em;margin:0}
.note p{font:600 18px/1 Inter;letter-spacing:.06em;text-transform:uppercase;color:var(--meta);margin:12px 0 0}
.note::after{content:"";position:absolute;inset:-20% -10% -20% 50%;filter:blur(28px);
  background:radial-gradient(40% 30% at 70% 30%,#f79347,transparent),
             radial-gradient(50% 40% at 80% 75%,#ee1db9,transparent),
             radial-gradient(30% 30% at 95% 45%,#fff36b,transparent);
  animation:drift 12s linear infinite}
@keyframes drift{50%{transform:translateX(-6%) rotate(4deg) scaleY(1.1)}}
@media (prefers-reduced-motion:reduce){.note::after{animation:none}}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Calm composition with vivid gradients kept to one zone, and a strong dark/light rhythm. |
| Originality | 6 | Gradient-aura cards are a popular trend; the per-sender hue mapping is a nice twist. |
| Usability | 6 | Readable titles, but meta fails contrast and there are no notification affordances. |
| Craft | 7 | Consistent geometry and a nicely masked glow, though the shadows are generic. |

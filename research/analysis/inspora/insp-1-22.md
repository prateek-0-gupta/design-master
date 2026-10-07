---
id: insp-1-22
source: inspora
category: Motion
status: analyzed
title: "wavy carousel"
creator: "@jmtrivedi"
styles: [spatial-ui, dark-premium, micro-interaction, glassmorphism]
patterns: [ribbon-list-carousel, gesture-driven-spline-layout, pill-list-items, perspective-depth-scaling, inertial-scroll]
mode: dark
palette: ["#272a3b", "#3b3d53", "#160707", "#bfbcba", "#b29685", "#c17e46"]
type_families: ["SF Pro Display / Text (iOS system, likely)"]
type_class: [neo-grotesk]
radius_px: [9999, 28]
motion: {durations_s: [1.1, 0.47, 0.4, 4.33, 5.6], easing: [ease-out, linear], loop: false}
scores: {aesthetics: 8, originality: 9, usability: 5, craft: 8}
craft_signals: [items-orient-to-path-tangent, depth-scale-along-ribbon, artwork-tinted-pills, inertial-ease-out-decay, on-device-60fps]
anti_patterns: [text-rotated-unreadable, no-selection-state-visible]
---
# wavy carousel — @jmtrivedi

## 1. Snapshot
- **Subject:** A 934×1662, 15.9 s, 59.94 fps hands-on recording of an iPhone prototype. A music list (song pills with album art, title and artist, such as "Falling – Opia, Wheathan", "Twin Flame – KAYTRANADA" and "Summer in NY – Sofi Tukker") is laid out along a 3D ribbon that the user bends and spins with a finger, like a snake or wave.
- **Why it's remarkable:** The list stops being a column. Every item rides a spline the gesture deforms, with perspective scaling, so scrolling becomes sculpting.

## 2. Composition & layout
- **Canvas:** the full screen in #272a3b (slate navy), with the status bar at the top. There is a darker band in the lower third of the screen (about y 1070→1350 in the key frame) and a small glowing particle near the bottom, likely a floor or horizon cue.
- **Rest state (t=0.88 s and 14.98 s):** the items stack vertically in a tapered column. The near item is about 180 px wide at the top and recedes to about 30 px pills at the bottom, a perspective tower.
- **During interaction:** the column curves into an S or arc across the screen.
  - Items are about 90×200 px pills in the key frame, rotated to follow the path tangent (−35° to −60°).
  - Near items reach about 230 px long and far items shrink to about 25 px.
- **Item:** a rounded pill (about 28 px radius on near items) with album art of about 40 px at the leading end, and a two-line title/artist set perpendicular to the path.

## 3. Typography
- iOS system font (SF Pro). Item title semibold, about 15–18 pt on near items, with the artist in a lighter weight below.
- Text rotates with the pill, so it is mostly read at 45–60° angles.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #272a3b / #3b3d53 | screen background | about 26% |
| #160707 | phone bezel, shadows | 6% |
| #bfbcba / #b29685 | pill highlights, glass | about 7% |
| item tints: lilac, yellow, blue, green | per-song pills (from art) | — |
| #c17e46 / #8c4733 / #7d3c2b | hand and wooden table (filmed) | about 40% |

WCAG check: white item text on the background #272a3b is 14.18:1. On the lighter lilac or yellow pills the text is set dark or white depending on the pill; it was not measurable at capture resolution.

## 5. Depth & material
- **Pills:** semi-translucent and frosted, each tinted from its album art (yellow pill for yellow art, blue pill for "Delilah", lilac for "TIME"). A lighter top highlight gives a glassy edge.
- **Depth:** conveyed by scale (about 8× range from near to far), plus overlap order. No blur on far items is visible.

## 6. Components & patterns
- A list or carousel on a deformable 3D spline.
- Album-tinted list rows.
- Gesture-driven layout: pinch and drag bend the curve, and release returns it to the tower.

## 7. Motion
- **Measured:** 15.86 s at 59.94 fps, `motion_fraction` 0.81, 9 segments, median 0.47 s.
  - Most are fast-start decays (ease-out): 3.07 s (0.47 s, `peak_at` 0.18), 3.80 s (0.40 s, 0.04), 4.67–9.00 s (4.33 s, 0.08) and 9.27–14.87 s (5.60 s, 0.13).
  - An early 0.80–1.90 s segment (1.10 s) is continuous/linear (the finger drag).
  - The final 15.10–15.80 s segment (0.70 s, `peak_at` 0.74, ease-in) is the snap back to the tower.
- **Reading:** Flicks produce long inertial decays (4–5.6 s) with momentum peaking at the start. This is physics-based scrolling with low friction. The item order flows along the ribbon continuously (frames at t=6.17 and 7.93 s show the same items migrating along the arc).

## 8. Brand system
n/a — not a brand system.

## 9. UX
- Highly tactile and exploratory, but legibility suffers: rotated text and tiny far items.
- No focus or selection state is shown.
- It suits browsing a library by art ("vibes") or acting as an ambient now-playing toy, not scanning a list.
- The rest-state tower gives a recognisable home pose.

## 10. Craft signals
- Items orient to the spline tangent, with no "billboard" items facing the camera wrongly.
- Pill tint is derived from each song's artwork.
- Scale falloff is smooth and continuous along the ribbon, with no popping.
- The inertial decay curves are long (about 4–5 s) with a sharp start, giving believable momentum.
- Recorded live on device at 60 fps.

## 11. Reproduction recipe
```js
// position N items along a Catmull-Rom spline whose control points follow touch
items.forEach((el,i)=>{
  const t=(i/N+offset)%1, p=spline.point(t), tan=spline.tangent(t);
  const z=p.z, s=1/(1+z*0.9);                       // perspective scale
  el.style.transform=`translate3d(${p.x}px,${p.y}px,0) rotate(${Math.atan2(tan.y,tan.x)}rad) scale(${s})`;
  el.style.zIndex=Math.round(1000-z*100);
});
// release: offset velocity decays  v*=0.985 per frame (≈4–5 s tail at 60 fps)
```
```css
.song{width:200px;height:56px;border-radius:28px;display:flex;gap:10px;align-items:center;padding:8px;
  background:color-mix(in srgb,var(--art) 55%,rgba(255,255,255,.25));backdrop-filter:blur(12px);
  box-shadow:inset 0 1px 0 rgba(255,255,255,.35);color:#fff;font:600 15px/1.1 -apple-system,sans-serif}
body{background:#272a3b}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | A colourful ribbon on calm slate; it looks sculptural. |
| Originality | 9 | Few lists let the user bend the layout itself. |
| Usability | 5 | Rotated tiny text; no clear selection; novelty over scanning. |
| Craft | 8 | Correct tangent orientation, depth scale and inertial physics. |

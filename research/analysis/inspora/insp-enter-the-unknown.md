---
id: insp-enter-the-unknown
source: inspora
category: Illustration
status: analyzed
title: "Enter the Unknown"
creator: "cem hasimi"
styles: [generative-particle, technical-wireframe, high-contrast-bw, maximalist-color]
patterns: [dashed-line-perspective-tunnel, off-centre-vanishing-point, particle-cone-emission, line-figure-in-doorway, mono-scene-colour-burst]
mode: dark
palette: ["#000000", "#ffffff", "#3ee0c8", "#c445e8", "#f05454", "#f5b05a", "#1a1b1b"]
type_families: []
type_class: []
radius_px: []
motion: {durations_s: [1.68], easing: [ease-in-out], loop: true}
scores: {aesthetics: 8, originality: 8, usability: 6, craft: 7}
craft_signals: [dash-length-scales-with-depth, vanishing-point-at-thirds, four-hue-particle-palette, particles-elongate-along-velocity, single-line-weight-figure, colour-only-in-emission]
anti_patterns: [non-seamless-loop-jump, dense-dashes-create-moire]
---
# Enter the Unknown — cem hasimi

## 1. Snapshot
- **Subject:** A 1.8 s, 1280×986 (25 fps) looping illustration.
  - A white single-line figure stands in a small black doorway at the far end of a tunnel.
  - The tunnel is drawn entirely from nested rectangles of short white dashes.
  - A cone of confetti-like particles (teal, magenta, coral, apricot) blasts from the figure's head toward the viewer and off to the right.
- **Why it's remarkable:** Everything is monochrome line except the "thought" spray. Colour equals imagination, and the dashed perspective gives depth without a single filled shape.

## 2. Composition & layout
- **Vanishing point:** about (420, 300), roughly one-third from the left and one-third from the top. This leaves a large lower-right field for the particle cone to fan into.
- **Doorway:** about 110×180 px (x≈362–472, y≈218–398), about 8.6% of the frame width. The figure is about 170 px tall inside it.
- **Tunnel:** about 30 concentric dashed rectangles expand to the frame edges. Dash length grows from about 3 px near the door to about 12 px at the edge, and the spacing also grows, which encodes perspective.
- **Particle cone:** spreads at about 35° from the head toward the upper-right and lower-right. It covers about 45% of the frame by the right edge.

## 3. Typography
None.

## 4. Colour
| Hex | Role | Share (key frame) |
|---|---|---|
| #000000 / #0b0c0c | void | 64% |
| #1a1b1b / #292a2a | anti-aliased dash haze (sampling) | 27% |
| #ffffff | dashes, figure line | — |
| #3ee0c8 (est.) | teal particles | — |
| #c445e8 (est.) | magenta/violet particles | — |
| #f05454 (est.) | coral-red particles | — |
| #f5b05a (est.) | apricot particles | — |

WCAG checks (on #000):
- White line: 21:1.
- Teal: 12.7:1.
- Coral: 6.1:1.
- Magenta: 5.36:1.

All hues are well separated from the black. The four particle hues are spread roughly 90° apart on the wheel (teal, violet, red, orange), which gives maximum variety with equal-ish saturation.

## 5. Depth & material
- Depth comes only from line logic: converging dashed frames, scaling dash size, and particles growing larger and more elongated as they approach the viewer (about 4 px near the head, about 30×10 px streaks at the right edge).
- There is no lighting, shading or blur. The figure is a 2 px white outline with no fill.

## 6. Components & patterns
- **Dashed perspective tunnel:** the classic Droste or infinite-corridor device, made with dotted strokes.
- A figure in a doorway is a threshold metaphor.
- A particle cone with directional streaks, emitted from a point (the head), equals ideas or energy.

## 7. Motion
These figures are measured: 1.80 s at 25 fps, motion_fraction 0.53, one segment of 0.04–1.72 s (1.68 s), peak_at 0.51, so symmetric ease-in-out energy across the clip.

The emission is continuous: particles stream outward the whole time, with density pulsing and peaking mid-clip. The tunnel is mostly static, with slight dash shimmer.

`seamless_loop_likely: false` (first-to-last difference 7.98). Particle positions do not match at the wrap, so a visible jump occurs every 1.8 s.

The figure appears static across frames, though its head subtly turns (an estimate from the frames).

## 8. Brand system
n/a — not a brand system. Identity cues: a white-line-on-black linework style with a four-colour confetti accent, which suits an NFT or digital-art persona.

## 9. UX
- As an illustration it reads instantly: a person, a door, ideas flying.
- The dense dashed field (about 30 rings of dashes 3–12 px long) can produce moiré or shimmer when scaled down or compressed.
- The short loop, with its jump, would be noticeable as a background.

## 10. Craft signals
- Dash length and gap scale with depth (about 3 px near the door, about 12 px at the edge), giving correct perspective foreshortening.
- The vanishing point sits on the one-third lines, not the centre, which makes room for the cone.
- Particles are motion-elongated along their trajectory and grow with proximity.
- Colour is confined to the emission; the environment and figure are strictly white on black.
- The figure is drawn with one constant stroke weight (about 2 px) matching the dash weight.

## 11. Reproduction recipe
```js
// canvas sketch: dashed tunnel + particle cone
const VP={x:W*.33,y:H*.31}, COLORS=['#3ee0c8','#c445e8','#f05454','#f5b05a'];
ctx.fillStyle='#000';ctx.fillRect(0,0,W,H);ctx.strokeStyle='#fff';ctx.lineWidth=2;
for(let i=1;i<=30;i++){const t=i/30, w=110+(W-110)*t*t, h=180+(H-180)*t*t;
  const x=VP.x-(VP.x-0)*t*t - 55*(1-t*t), y=VP.y-(VP.y-0)*t*t - 90*(1-t*t);
  ctx.setLineDash([3+9*t, 4+10*t]);ctx.strokeRect(x,y,w,h);}
// particles: spawn at head, angle in [-20°,+15°], speed ~ U(200,600)px/s, size grows with distance
p.len = 4 + p.dist*.05; ctx.fillStyle=COLORS[p.k]; drawCapsule(p.x,p.y,p.len,p.len*.35,p.angle);
```
```css
.loop{animation-duration:1.8s;animation-timing-function:cubic-bezier(.45,0,.55,1)}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Striking restraint (white dashes on black) punctured by a joyful four-hue burst. |
| Originality | 8 | A dashed-line tunnel plus a head-emitted confetti cone is a memorable, ownable image. |
| Usability | 6 | Clear metaphor; the loop jump and moiré-prone density limit reuse. |
| Craft | 7 | Good perspective scaling and colour discipline; the non-seamless loop is a miss. |

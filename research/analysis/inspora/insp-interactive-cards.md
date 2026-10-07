---
id: insp-interactive-cards
source: inspora
category: Web
status: analyzed
title: "Interactive cards."
creator: "@kaolti"
styles: [technical-wireframe, isometric, dark-premium, micro-interaction]
patterns: [hover-invert-card, hover-tilt-3d, isometric-line-chart-illustration, chamfered-corner-cards, crop-mark-frames, numbered-card-index, single-accent-highlight-datum]
mode: dark
palette: ["#2a2a2c", "#1d1d1f", "#e7e0d0", "#ee5a3a", "#7f4f45", "#b1a499"]
type_families: ["Inter Display / Neue Haas-style grotesk (likely)", "small monospace for indices (likely)"]
type_class: [neo-grotesk, mono]
radius_px: []
motion: {durations_s: [0.37, 0.33, 0.2, 0.27, 0.7], easing: [ease-in-out, ease-in], loop: false}
scores: {aesthetics: 9, originality: 8, usability: 6, craft: 8}
craft_signals: [polarity-flip-on-hover, single-coral-datum-per-chart, isometric-hairline-charts, chamfered-corners-12px, perspective-tilt-follows-cursor, glow-under-accent-element, sundial-metaphor-for-time]
anti_patterns: [hover-only-reveal, accent-on-cream-low-contrast]
---
# Interactive cards. — @kaolti

## 1. Snapshot
- **Subject:** A 14.6 s, 1916×1080 recording of three portrait insight cards: "Productive days" (isometric bar chart), "Spending patterns" (isometric pie) and "Busiest hours" (a sundial column casting a light cone). They sit on #2a2a2c. Hovering a card flips it from charcoal to cream, tilts it in 3D and animates its chart.
- **Why it's remarkable:** Each chart is a hairline isometric object with exactly one coral datum (the best day, the largest slice, the busiest hour). Hover inverts the card's polarity, so the charts read like engraved instruments brought into the light.

## 2. Composition & layout
- **Cards:** three cards about 450×560 px (≈4:5) with ~18 px gaps, spanning x≈265→1645 (72% of the width), vertically centred at y≈260→822.
- **Card anatomy:**
  - title at top-left (x+55, about 32 px semibold);
  - a mono serial at top-right ("001/002/003", about 13 px);
  - an illustration well (about 340×370 px) marked by four L-shaped crop marks;
  - the chart centred inside on a sparse dot-star field.
- **Generous margins:** about 55 px side padding and about 60 px below the crop marks.

## 3. Typography
- **Titles:** a neo-grotesk (Inter Display / Neue Haas-like) at semibold 600, about 32 px, with −0.02 em tracking. Cream (#e7e0d0) on dark and #1d1d1f on cream.
- **Serials:** a small mono at about 13 px in mid-grey, an inventory-tag tone.
- There is no body copy; the chart is the content.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #2a2a2c | stage | 67% |
| #1d1d1f | card (rest) | 20% |
| #e7e0d0 | card (hover) / line art on dark / titles | 11% |
| #ee5a3a (sampled visually; shading #7f4f45) | coral accent datum + glow | 1–2% |
| #b1a499 | line art and dots on cream | 1% |

WCAG checks:
- The title in both polarities (#e7e0d0 ↔ #1d1d1f) is 12.8:1.
- The mono serial (about #6b6b6b on #1d1d1f) is 3.16:1, decorative.
- Coral on dark is 4.94:1, but coral on cream is **2.59:1**, so the accent loses punch in the hover state; the designer compensates with a filled mass and glow.
- Cream line art #b1a499 on cream is 1.85:1, which is faint by intent.

## 5. Depth & material
- **Chamfers:** the cards are flat polygons with chamfered corners of about 12 px (the clipped corners are visible at the top-left and bottom-right of every card) and no radius.
- **Hover depth:** a 3D tilt (about 2–3° rotateZ plus a slight rotateY; the hovered card's top edge slopes from y≈255 to 262) and a ~6 px lift. There is no shadow; separation comes from the polarity flip.
- **Charts:** 1 px isometric line drawings (30° axonometric) with a soft radial coral glow beneath the accent element (the dot over the bar chart, the pie's base, the sundial's cone).

## 6. Components & patterns
- Insight card with title, serial, crop-marked figure and an animated illustration.
- **Hover:** background inverts, line colour inverts, the chart animates:
  - bar chart: the coral cube and dot pop;
  - pie: the coral slice extrudes and lifts out (frames 4.06 → 5.68 s);
  - sundial: the cone of light sweeps around the dial with the cursor (frames 7.30 → 10.54 s, cone angle changes).
- **One-hot emphasis:** exactly one card is cream at a time.

## 7. Motion
Measured: 14.6 s at 60 fps, motion fraction 0.15, not a loop.

| Segment | Duration | Shape (peak_at) | What happens |
|---|---|---|---|
| 2.50–2.87 s | 0.37 s | symmetric (0.41) | hover handoff, card 1 to card 2 |
| 6.00–6.33 s | 0.33 s | symmetric (0.35) | handoff to card 3 |
| 9.53–9.73 s, 9.83–10.10 s | 0.2 / 0.27 s | ease-in (0.69) | sundial cone tracking the cursor |
| 11.67–12.37 s | 0.7 s | ease-in (0.79) | cursor sweeps back left across all cards; frame 12.17 s catches cards 1–2 mid-crossfade as a warm grey (#8a847a-ish), so the colour flip is a ~0.3 s interpolation, not a cut |
| 13.80–14.13 s | 0.33 s | symmetric | card 1 lands |

The handoffs are a consistent ~0.33–0.37 s ease-in-out.

## 8. Brand system
n/a — not a brand system. Identity cues: charcoal/cream/coral, engineering crop marks and serials, and isometric hairline objects. Visually close kin to insp-beveled-cards (same chamfer-plus-crop-mark language).

## 9. UX
- **Strengths:** Strong, immediate hover feedback; one highlighted datum per chart answers the card's question at a glance; the metaphors are clever (a sundial for hours).
- **Risks:**
  - The charts have no values or labels, so they are decorative.
  - The hover-only animation needs focus and tap equivalents.
  - The coral loses contrast on cream.
  - Tilt plus colour flip on every pass may be heavy for repeat use; it needs `prefers-reduced-motion`.

## 10. Craft signals
- Exactly one coral element per chart, always with a soft glow beneath it.
- On hover the line art inverts with the card (cream lines become dark #1d1d1f-ish lines), not just the background.
- All three charts share one isometric projection angle and a 1 px stroke.
- Chamfers of about 12 px appear on all four corners, consistent across states.
- Crop marks and serials repeat at identical offsets in each card.
- The colour flip interpolates through warm grey (frame 12.17 s) instead of snapping.

## 11. Reproduction recipe
```css
:root{--stage:#2a2a2c;--card:#1d1d1f;--cream:#e7e0d0;--coral:#ee5a3a;--line-dim:#b1a499;--cut:12px}
.card{--fg:var(--cream);--bg:var(--card);background:var(--bg);color:var(--fg);width:450px;aspect-ratio:4/5;padding:55px;
  clip-path:polygon(var(--cut) 0,calc(100% - var(--cut)) 0,100% var(--cut),100% calc(100% - var(--cut)),
    calc(100% - var(--cut)) 100%,var(--cut) 100%,0 calc(100% - var(--cut)),0 var(--cut));
  transition:background .35s cubic-bezier(.45,0,.55,1),color .35s,transform .35s cubic-bezier(.45,0,.55,1);
  transform:perspective(900px)}
.card:hover,.card:focus-visible{--fg:var(--card);--bg:var(--cream);
  transform:perspective(900px) translateY(-6px) rotateZ(-1.5deg) rotateY(var(--ry,4deg))}
.card h3{font:600 32px/1.1 "Inter Display",sans-serif;letter-spacing:-.02em}
.card .idx{font:400 13px "JetBrains Mono",monospace;opacity:.5}
.card svg .wire{stroke:currentColor;stroke-width:1;fill:none}
.card svg .hot{fill:var(--coral);filter:drop-shadow(0 0 16px color-mix(in srgb,var(--coral) 60%,transparent))}
.card:hover .slice{transform:translateY(-10px);transition:transform .35s cubic-bezier(.2,.8,.2,1)}
@media (prefers-reduced-motion:reduce){.card,.card *{transition:none!important;transform:none!important}}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 9 | A refined three-colour system, elegant isometric line art and a satisfying inversion. |
| Originality | 8 | The polarity-flip hover plus metaphoric charts (sundial for hours) is fresh. |
| Usability | 6 | Great feedback, but the charts carry no actual data and the interaction is hover-dependent. |
| Craft | 8 | Consistent projection, stroke, chamfer and timing; smooth interpolated flips. |

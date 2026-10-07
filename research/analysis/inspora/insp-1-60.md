---
id: insp-1-60
source: inspora
category: Motion
status: analyzed
title: "Ringwriter"
creator: "@edo_lunardi"
styles: [kinetic-type, generative-particle, monochrome, terminal-mono]
patterns: [concentric-ring-text, glyph-to-dot-dissolve, press-and-hold-interaction, cursor-tooltip-coaching, differential-ring-rotation, radial-intensity-falloff]
mode: dark
palette: ["#1f1f1f", "#2c2c2c", "#393939", "#444444", "#848484", "#9b9b9b", "#f0f0f0", "#ffffff"]
type_families: ["IBM Plex Mono / JetBrains Mono-style monospace (likely)"]
type_class: [mono, kinetic-type]
radius_px: [0]
motion: {durations_s: [1.63, 0.8, 0.57, 2.07], easing: [ease-out, ease-in, ease-in-out], loop: false}
scores: {aesthetics: 8, originality: 8, usability: 6, craft: 8}
craft_signals: [type-size-scales-with-ring-radius, dot-placeholders-keep-ring-legible-when-empty, tooltip-copy-changes-per-hold-phase, inverted-label-chip-cursor, glyphs-upright-relative-to-ring-tangent, inner-rings-dimmer-than-outer]
anti_patterns: [phrase-unreadable-as-text, hidden-gesture-without-coaching-outside-demo]
---
# Ringwriter — @edo_lunardi

## 1. Snapshot
- **Subject:** An 8.1 s, 1728×1728 interactive type piece. The phrase "THE CONTENT ARCHITECTURE" repeats around about 25 concentric rings that spin at different speeds. Pressing and holding with the cursor "melts" glyphs into dots, and releasing lets them re-form.
- **Why it's remarkable:** It treats text as a particle field with a two-state material (glyph ↔ dot) driven by a single press-and-hold. It looks like a vinyl record of words.

## 2. Composition & layout
- **Rings:** The ring system is centred slightly right of and below centre (≈52% x, 50% y) and overflows all four edges, so the composition feels infinite. Ring pitch is about 40 px near the centre, growing to about 70 px at the edges.
- **Type size scales with radius:** about 14 px caps in the innermost ring, about 22 px mid-field and about 34 px at the edges (key-frame px, 1728 canvas). This creates a tunnel or perspective feel.
- **Melt zone:** The dissolve occurs in a wedge or annulus around the cursor; at 6.75 s a large ring band is mostly dots.
- **Cursor chip:** a small inverted label (white fill, black mono caps, about 13 px) offset 20 px right of the pointer: "CLICK & HOLD", then "KEEP HOLDING", then "RELEASE".

## 3. Typography
- A single monospace, close to IBM Plex Mono or JetBrains Mono, set in all caps at regular weight with generous tracking (≈+0.1 em). Glyphs are oriented tangentially and flip upside-down across the top half, as on a coin edge.
- The phrase is cut into fragments ("ARCHIT", "THE CONT", "TECTURE") because dissolved letters leave gaps, so the reading is fragmentary by design.
- **Tooltip:** the same mono at about 13 px, so the UI and the art share one voice.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #1f1f1f | canvas | 73% |
| #2c2c2c / #393939 | dot rings (dissolved glyph placeholders) | ~6% |
| #444444–#5c5c5c | mid-dim glyphs (inner rings) | ~9% |
| #848484 / #9b9b9b | mid-bright glyphs | ~6% |
| #f0f0f0 / #ffffff | outer bright glyphs, tooltip chip | ~5% |

WCAG checks:
- Bright glyphs are 14.46:1.
- Mid glyphs #848484 are 4.41:1.
- Dim inner glyphs #444 are 1.69:1, an intentional fade.
- The tooltip chip (#1f1f1f on white) is 16.48:1.

Brightness rises with radius, so the centre recedes like a well.

## 5. Depth & material
- Flat 2D. Depth is implied by:
  - type size and brightness increasing outward (perspective tunnel);
  - dot rings at about 2 px diameter and about 10 px pitch, which persist as a ghost track where glyphs are absent.
- There are no shadows or blur. Dissolved glyphs collapse to points rather than fading.

## 6. Components & patterns
- **Concentric ring text system:** each ring holds a repeating string with its own angular velocity.
- **Press-and-hold "melt":** holding progressively turns glyphs to dots in an expanding region; releasing restores them.
- **Cursor tooltip coaching:** a state-aware label teaches the gesture as it is used.
- **Intro:** the rings fade up from near-black at 0.45 s.

## 7. Motion
Measured: 8.10 s at 60 fps, 6 segments, motion fraction 0.55, not a loop.
- **0.67–2.30 s (1.63 s, peak 0.32 → ease-out):** The intro reveal, as the rings fade and scale in from dim to full brightness.
- **3.77–5.17 s (three ease-in segments of 0.13, 0.80 and 0.23 s; peaks 0.88–0.98):** The hold phase. The dissolve accelerates the longer the button is held, which matches "KEEP HOLDING" at 4.05 s.
- **5.27–5.83 s (0.57 s, peak 0.03 → sharp ease-out):** "RELEASE", where glyphs snap back.
- **5.93–8.00 s (2.07 s, symmetric):** A second hold and re-form cycle (6.75 s shows heavy dissolution).
- Throughout, the rings rotate continuously (inner rings visibly faster between frames; estimated period 20–40 s per revolution).

## 8. Brand system
n/a — not a brand system. Identity cues: the "content architecture" phrase suggests a studio or CMS tagline. The mono-on-charcoal voice reads as engineering-led and editorial.

## 9. UX
- **Strengths:** A single gesture with an immediately visible result. The tooltip copy changes with the gesture phase, which is excellent coaching for a hold interaction.
- **Risks:**
  - The phrase itself is hard to read: upside-down segments, fragments.
  - It needs a reduced-motion fallback.
  - On touch, the hold may conflict with long-press menus.

## 10. Craft signals
- Glyph size and ring spacing scale proportionally with radius.
- Dot placeholders keep the ring geometry visible even when glyphs vanish, so the structure never breaks.
- The tooltip label changes per phase: CLICK & HOLD → KEEP HOLDING → RELEASE.
- The tooltip is an inverted chip (white bg, black mono) with no radius, matching the hard-edged type voice.
- Brightness is graded from about #444 inner to #fff outer, not a flat white.
- Glyph rotation follows the ring tangent exactly; there is no faux-upright text.

## 11. Reproduction recipe
```js
// canvas sketch
const phrase = "THE CONTENT ARCHITECTURE  ";
for (let r = 0; r < 25; r++) {
  const radius = 60 + r * (40 + r * 1.2);           // spacing grows outward
  const size = 12 + r * 0.9;                          // type scales with radius
  const omega = (r % 2 ? 1 : -1) * (0.25 - r * 0.006); // rad/s, differential spin
  const lum = Math.round(68 + (255 - 68) * r / 24);   // #444 -> #fff
  ctx.font = `400 ${size}px "IBM Plex Mono"`;
  const step = size * 0.72 / radius;                  // tracking-aware angular step
  for (let i = 0; i * step < Math.PI * 2; i++) {
    const a = i * step + t * omega, ch = phrase[i % phrase.length];
    const melt = holdAmount * falloff(dist(cursor, polar(radius, a))); // 0..1, ease-in over hold
    ctx.save(); ctx.translate(cx + radius * Math.cos(a), cy + radius * Math.sin(a)); ctx.rotate(a + Math.PI/2);
    if (melt > .5) { ctx.fillStyle = "#393939"; ctx.fillRect(-1,-1,2,2); }
    else { ctx.fillStyle = `rgb(${lum},${lum},${lum})`; ctx.fillText(ch, 0, 0); }
    ctx.restore();
  }
}
```
```css
.cursor-chip{font:400 13px/1 "IBM Plex Mono";letter-spacing:.06em;background:#fff;color:#1f1f1f;padding:4px 6px;border-radius:0}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Hypnotic monochrome texture, with good brightness grading and scale. |
| Originality | 8 | Glyph-to-dot melt on rotating rings is a fresh kinetic-type mechanic. |
| Usability | 6 | Excellent gesture coaching, but the message is barely legible as text. |
| Craft | 8 | Proportional scaling, persistent dot tracks and phase-aware tooltip copy. |

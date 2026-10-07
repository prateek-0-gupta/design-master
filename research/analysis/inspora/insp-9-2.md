---
id: insp-9-2
source: inspora
category: Motion
status: analyzed
title: "status tags with glass bubble"
creator: "@Designownow_"
styles: [soft-3d, glassmorphism, playful-rounded, micro-interaction]
patterns: [status-badge-set, hover-tooltip, thought-bubble-tail, colour-coded-state, icon-plus-label-pill, coloured-glow-shadow]
mode: light
palette: ["#f6f6f6", "#f6d6c5", "#bafde3", "#faf2bb", "#b9e7f3", "#e6e0fa", "#f6c9d6", "#7a7a7a"]
type_families: ["Google Sans / Product Sans-style geometric (likely)"]
type_class: [geometric-sans, rounded-sans]
radius_px: [9999, 40]
motion: {durations_s: [0.1, 18.7], easing: [ease-out], loop: true}
scores: {aesthetics: 8, originality: 6, usability: 5, craft: 7}
craft_signals: [tinted-shadow-matches-pill-hue, inner-top-highlight-on-pills, thought-bubble-dot-tail, tooltip-header-dot-echoes-state-colour, pastel-tooltip-bottom-glow, one-icon-per-state]
anti_patterns: [pastel-text-fails-contrast, colour-only-severity, hover-only-explanation]
---
# status tags with glass bubble — @Designownow_

## 1. Snapshot
- **Subject:** A 1920×1824 recording of six status pills: Pending, Success, In review, Paused, In progress and Error. A cursor hovers each one, and a frosted "glass bubble" tooltip that explains the state appears above or below it.
- **Why it's remarkable:** Each pill is a small jelly-like candy: a pastel fill, a saturated outline, an inner highlight and a coloured glow underneath. The tooltip reuses that material with a thought-bubble tail, so the badge and its explanation feel like one family.

## 2. Composition & layout
- The six pills sit in a 3×2 grid centred horizontally at about y≈810 and y≈1000 (key frame). The vertical pitch is about 190 px and the horizontal gutter about 90–120 px. The columns are not strictly aligned: pill widths follow their labels (Pending ≈380 px, In progress ≈460 px, Error ≈300 px), and each row is centred per column.
- **Pill size:** about 128 px tall. The label cap height is about 40 px, which puts the label near 56 px at 1920 width, roughly a 14–16 px chip in a real UI scaled 3.5×.
- **Tooltip:** about 800×300 px. It has a header capsule (state dot plus title) and a two-line body. It opens above the pill for the top row and below it for the bottom row, which keeps it inside the canvas.
- More than 60% of the frame is empty #f6f6f6. This is a component showcase, not a screen.

## 3. Typography
- A geometric sans with a single-storey "g", round "e" and open "s", very close to Google Sans or Product Sans. Figtree is the nearest free option.
- **Pills:** about 56 px Regular/Medium, tinted the darker version of each hue.
- **Tooltip:** the title is about 40 px Regular in the state hue. The body is about 32 px Regular grey (#7a7a7a-ish) with leading of about 1.4.
- There is no bold anywhere. Hierarchy comes from colour and size only.

## 4. Colour
| Hex | Role | Approx share |
|---|---|---|
| #f6f6f6 | canvas | 89% |
| #f6d6c5 | Pending fill (orange family) | 2% |
| #bafde3 | Success fill (mint) | 1.3% |
| #faf2bb | In review fill (yellow) | 1.8% |
| #b9e7f3 / #bed5eb | In progress fill (sky) | 2% |
| #e6e0fa (e6e6ef sampled) | Paused fill (lavender) | 2% |
| #f6c9d6 / #bc99a4 | Error fill and its shadow | 1.5% |
| #7a7a7a | tooltip body text | <1% |

Pill text was estimated from the pixels as a deeper version of each fill. WCAG checks:
- Pending #c86a2c on #f6d6c5 is 2.76:1.
- Success #3aa982 on #bafde3 is 2.54:1.
- In review #b8961a on #faf2bb is 2.49:1.
- In progress #2c8fc4 on #b9e7f3 is 2.71:1.
- Error #d23a6a on #f6c9d6 is 3.13:1.
- Paused #8a6ad8 on #e6e0fa is 3.2:1.
- Tooltip body #7a7a7a on #f8f8f8 is 4.04:1.

All of these **fail AA-normal**. At display size they read fine, but at a real 12–14 px chip size they would not.

## 5. Depth & material
- **Pills, in four layers:**
  1. A vertical gradient fill, lighter at the top.
  2. A 2–3 px saturated outline of the same hue.
  3. A white inner highlight along the top edge.
  4. A large blurred drop glow in the pill's own hue, offset about 30 px down with roughly 60 px blur, visible as a coloured haze under each row.
- **Tooltip:** near-white frosted glass. It has a 1 px light-grey rim and a soft neutral shadow, and its bottom edge picks up a faint rainbow tint (green/yellow/pink) as if it were refracting the pills below.
- **Tail:** a small rounded nub plus a detached 14 px dot, a comic thought bubble rather than a triangle caret.

## 6. Components & patterns
- **Status badges:** each one pairs an icon with a label and has its own glyph: a refresh arrow, check-circle, document, pause-circle, spinner rays and x-circle. The icons are outline style at about 1.5 px stroke (at 1× scale), coloured like the text.
- **Tooltip:** a header capsule with an inner rounded field (about 40 px radius) holding a status dot and title, then a description. It is effectively a two-level card with a nested pill.
- A colour-coded state set with six hues.

## 7. Motion
- **Measured:** the clip runs 18.7 s at 30 fps. The motion fraction is only **0.01**, and there is a single segment above threshold, **0.1 s at 8.1 s**, with an ease-out (fast-start) profile (peak at 0.17).
- **Interpretation:** Nearly all change is low-energy, consisting of cursor travel plus the tooltip fading and scaling in place. The one detected spike is the tooltip switching between Success and In review. Frame comparison suggests each tooltip appears in about 0.2–0.3 s with a small scale-up from the tail anchor (estimate).
- The pill under the cursor shifts down about 2–4 px (Success at 7.27 s, In review at 11.43 s, In progress at 13.51 s), a press or hover-sink cue.
- `seamless_loop_likely: true`. The first and last frames are both the idle grid.

## 8. Brand system
n/a — not a brand system. The identity cue is a "candy glass" material language: hue-matched glow plus a thought-bubble tail.

## 9. UX
- Six states map to six hues and six distinct icons, so state is not encoded by colour alone, which is good.
- The explanation lives only in a hover tooltip, so touch and keyboard users need a focus or tap path.
- Body copy is grey on near-white at 4.04:1, and pill labels sit around 2.5–3.2:1. A production version needs darker text tones (about 50% luminance lower).
- The tooltip placement flips between above and below by row, which is good collision handling.

## 10. Craft signals
- The drop shadow is tinted per pill (orange haze under Pending, lavender under Paused), not neutral grey.
- A 1–2 px white inner highlight runs along the top of every pill.
- The dot in the tooltip header uses the exact state hue of the hovered pill.
- The tail is a nub plus a separate dot (about 14 px) aligned to the pill's horizontal centre.
- The bottom inside edge of the tooltip carries faint multi-hue tint, simulating refraction of the pills beneath.
- Each pill keeps the same horizontal padding (about 40 px) regardless of label length.

## 11. Reproduction recipe
```css
:root{--canvas:#f6f6f6;--tip-text:#6b6b6b;--r-pill:9999px;--font:"Google Sans","Figtree",system-ui,sans-serif}
.tag{--h:#f08a3e;--fill:#f6d6c5;font:500 15px/1 var(--font);display:inline-flex;gap:8px;align-items:center;
  padding:9px 14px;border-radius:var(--r-pill);color:color-mix(in oklab,var(--h) 70%,#000);
  background:linear-gradient(180deg,color-mix(in oklab,var(--fill) 60%,#fff),var(--fill));
  border:1px solid color-mix(in oklab,var(--h) 55%,transparent);
  box-shadow:inset 0 1px 0 rgba(255,255,255,.9),inset 0 -2px 4px color-mix(in oklab,var(--h) 25%,transparent),
             0 10px 20px -6px color-mix(in oklab,var(--h) 45%,transparent);
  transition:transform .2s cubic-bezier(.2,.8,.2,1)}
.tag:hover{transform:translateY(1px)}
.tag[data-s=success]{--h:#2fc98f;--fill:#bafde3}.tag[data-s=review]{--h:#e8c51c;--fill:#faf2bb}
.tip{border-radius:20px;background:rgba(255,255,255,.75);backdrop-filter:blur(16px);
  border:1px solid rgba(0,0,0,.05);box-shadow:0 12px 30px rgba(0,0,0,.08);padding:6px 6px 14px;
  transform-origin:50% 100%;animation:pop .24s cubic-bezier(.2,.9,.3,1.2)}
@keyframes pop{from{opacity:0;transform:scale(.92) translateY(6px)}}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Cohesive pastel candy material, with tinted glows that make the set feel lit. |
| Originality | 6 | Status chips plus tooltip is common. The thought-bubble tail and refraction tint are the fresh bits. |
| Usability | 5 | Icons back up the colours, but every text pair fails AA and explanations are hover-only. |
| Craft | 7 | Consistent four-layer material and hue matching. Column alignment is loose. |

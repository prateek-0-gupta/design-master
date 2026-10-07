---
id: insp-bankito-frozen-card
source: inspora
category: Motion
status: analyzed
title: "bankito® frozen card"
creator: "@tyka_dominik"
styles: [dark-premium, physical-material, generative-particle, cinematic-3d]
patterns: [frozen-card-state, state-as-material-texture, ambient-particle-snowfall, status-chip-on-card, circular-quick-actions, card-notch-cutout, masked-pan]
mode: dark
palette: ["#070707", "#121314", "#1c1f22", "#2b2f38", "#2e3a47", "#51606d", "#dcdcdd", "#f9f9f9"]
type_families: ["Inter (likely)", "SF Pro (status bar)"]
type_class: [neo-grotesk]
radius_px: [20, 9999]
motion: {durations_s: [1.67, 0.13, 1.57, 0.6], easing: [linear, ease-in-out, ease-in], loop: true}
scores: {aesthetics: 9, originality: 8, usability: 8, craft: 8}
craft_signals: [frost-crystals-concentrated-at-card-edges, snow-escapes-card-bounds, frozen-chip-snowflake-glyph, primary-action-swaps-to-reactivate, semicircle-notch-on-card-edge, translucent-glass-chip]
anti_patterns: [particle-motion-may-distract, no-reduced-motion-hint]
---
# bankito® frozen card — @tyka_dominik

## 1. Snapshot
- **Subject:** A 5.13 s, 60 fps, 2260×1530 crop of a dark banking app's card-detail screen. The debit card is shown in a "frozen" state: ice crystals creep in from its edges and snow drifts across the card and the whole screen.
- **Why it's remarkable:** It encodes a binary account state (card frozen) as a literal material. The texture tells you the status before you read the "FROZEN" chip. This is state-as-weather instead of a grey overlay.

## 2. Composition & layout
- **Phone mockup:** the top half of an iPhone, about 1060 px of the 2000-px displayed frame (about 2.7× a 393 pt screen).
- **Header:** two 52 pt circular buttons, back at the top-left and more ("•••") at the top-right, inset about 16 pt.
- **Card:** about 330×190 pt (ratio ≈1.72, close to the ISO 1.586 card ratio but wider), centred with a 16 pt side margin and a radius of about 20 pt.
  - Top-left: a "Debit card" label.
  - Top-right: a 40 pt circular eye (reveal) button.
  - Bottom-left: the masked number "•••• 7481".
  - Bottom-right: the "FROZEN" chip.
  - Left edge: a semicircular notch about 22 pt in diameter at mid-height.
- **Quick actions:** three 44 pt circular icon buttons below the card (Change limits, Reactivate card, Transactions) with 14 pt labels underneath, on a 3-column equal grid.

## 3. Typography
- Neo-grotesk, most likely Inter: single-storey "a"-like forms are absent and the "a" is double-storey, with a flat-topped "t". The card label is about 17 pt Regular white, the PAN about 17 pt Medium with tabular figures, and action labels about 14 pt Regular.
- **Chip:** "FROZEN" in about 11 pt Semibold all caps with roughly +4% tracking.
- The status bar uses SF Pro ("13:13").

## 4. Colour
| Hex | Role | Approx share (key frame) |
|---|---|---|
| #f9f9f9 | presentation backdrop (outside the phone) | 52% |
| #070707 / #121314 | app background | 31% |
| #1c1f22 | circular button fills | 4% |
| #2b2f38 / #2e3a47 | card body (deep frosted navy) | 8% |
| #3f4c5c / #51606d | ice crystals and frost edge (steel blue to periwinkle) | 3.4% |
| #dcdcdd | text, snowflakes | 1% |

WCAG checks:
- White on the card #2b2f38 is 13.41:1.
- White on the lighter frost #3f4c5c is 8.75:1.
- White on the app background #070707 is 20.14:1.
- Labels #dcdcdd on the button fill #1c1f22 are 12.08:1.

Everything passes comfortably. The cold palette is confined to the card, and the UI stays neutral.

## 5. Depth & material
- **Card:** a dark, smoky glass plate with photographic frost: feathery ice crystals (#3f4c5c to #51606d with periwinkle highlights) clustered along the left and bottom edges, fading to a clear dark centre. It reads as frost forming from the edges inward, physically correct for a freezing pane.
- **Snow layers:** snowflakes at two or three depth layers. Some are large and blurred (foreground bokeh), some small and sharp. They fall over the card and the surrounding screen, so the effect is not clipped to the card.
- **Chip:** translucent dark glass (rgba white about 8%) with a 1 px light border and a snowflake glyph, matching the frosted language.
- **Buttons:** flat #1c1f22 discs with no shadow.

## 6. Components & patterns
- **Card state:** "FROZEN" chip plus texture plus a changed action set. The middle quick action reads "Reactivate card" (a refresh glyph) where an active card would presumably show "Freeze".
- **Reveal-PAN** eye button on the card.
- **Notch:** the semicircle cut-out on the card's left edge echoes a ticket or physical card punch, a brand detail.
- **Circular icon-over-label quick actions**, the standard fintech pattern.

## 7. Motion
**Measured** (60 fps source, sampled at 30): motion fraction is **0.56**, so the screen is animated over half the time. There are four segments:
- 0.07–1.73 s (**1.67 s**, continuous/linear): steady snowfall drift.
- 2.10–2.23 s (0.13 s, ease-in): a brief gust or flake burst.
- 2.80–4.37 s (**1.57 s**, symmetric ease-in-out, peak 0.5): the strongest pass. The frost texture shimmers or shifts across the card (compare 2.57 s with 3.14 s, where the crystal clusters move).
- 4.47–5.07 s (0.6 s, ease-in): a build back toward the loop start.

`seamless_loop_likely: true` (first/last diff 1.84). Snow falls slowly, roughly 20–40 pt/s (estimated from flake displacement between frames 0.57 s apart). This is ambient motion rather than a transition, and nothing in the UI chrome moves.

## 8. Brand system
n/a — not a brand system. Identity cues for "bankito®":
- the semicircle card notch;
- a neutral dark UI where the card itself carries all expressive material;
- the ® in the name, suggesting a real or speculative fintech brand.

## 9. UX
- **Strengths:**
  - The frozen state is unmistakable at a glance and redundantly labelled (chip plus texture).
  - The primary recovery action (Reactivate) is placed centrally in the action row.
  - All text contrast passes AA.
- **Risks:**
  - Perpetual particle motion on a banking screen can feel distracting or drain battery, and it needs a `prefers-reduced-motion` fallback (a static frost image).
  - Snow over the eye button and chip slightly reduces legibility at moments.

## 10. Craft signals
- Frost density is highest at the card's edges and clears toward the centre where the text sits, protecting legibility.
- Snow particles escape the card bounds and fall over the header and buttons, which makes the weather feel environmental.
- The chip's snowflake glyph repeats the snowflake particles.
- The quick action changes semantically ("Reactivate card") with the state.
- A semicircle notch about 22 pt wide is cut into the card's left edge at its vertical centre.
- The PAN uses four dots plus the last four digits with consistent spacing and tabular figures.

## 11. Reproduction recipe
```css
:root{--app:#070707;--btn:#1c1f22;--card:#2b2f38;--frost:#51606d;--frost-hi:#8a96d8;--text:#fff;--r-card:20px;
  --font:"Inter",system-ui,sans-serif}
.card{position:relative;aspect-ratio:1.72;border-radius:var(--r-card);overflow:hidden;color:var(--text);
  background:
    radial-gradient(120% 90% at 50% 45%, transparent 45%, color-mix(in oklab,var(--frost) 60%,transparent) 85%),
    url(frost-crystals.webp) center/cover, var(--card);
  -webkit-mask: radial-gradient(11px at 0 50%, #0000 98%, #000) ;}
.chip{display:inline-flex;gap:6px;padding:4px 10px;border-radius:9999px;font:600 11px/1 var(--font);letter-spacing:.04em;
  text-transform:uppercase;background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.18);backdrop-filter:blur(8px)}
.snow{position:absolute;inset:0;pointer-events:none;background-image:
   radial-gradient(2px 2px at 20% 10%,#fff8 50%,transparent),radial-gradient(3px 3px at 70% 40%,#fff6 50%,transparent),
   radial-gradient(1.5px 1.5px at 40% 80%,#fffa 50%,transparent);background-size:200px 200px;
  animation:fall 5.13s linear infinite}
@keyframes fall{to{background-position:0 200px,20px 200px,-10px 200px}}
@media (prefers-reduced-motion:reduce){.snow{animation:none}}
.qa{width:44px;height:44px;border-radius:50%;background:var(--btn);display:grid;place-items:center}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 9 | Moody, cinematic frost on a restrained dark UI. The material is beautifully confined to the hero object. |
| Originality | 8 | Turning "card frozen" into literal ice is a clever, memorable state metaphor. |
| Usability | 8 | Redundant state signalling, a contextual Reactivate action and strong contrast. Motion needs an opt-out. |
| Craft | 8 | Edge-weighted frost and multi-depth particles. Snow occasionally drifts over interactive targets. |

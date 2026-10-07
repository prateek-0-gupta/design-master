---
id: insp-1-20
source: inspora
category: Motion
status: analyzed
title: "Toggle to premium plans"
creator: "@Designownow_"
styles: [soft-3d, micro-interaction, corporate-clean, playful-rounded]
patterns: [rolling-ball-toggle, pricing-plan-switch, gradient-border-premium-card, status-dot-pill, mascot-avatars, script-word-reveal]
mode: light
palette: ["#e4e4e4", "#f1f1f1", "#383838", "#787878", "#f25fb8", "#1d81bd", "#585f71", "#96a1ab"]
type_families: ["Inter / SF Pro-style neo-grotesk (likely)", "connected brush script for 'Premium' (likely Pacifico-like)"]
type_class: [neo-grotesk, script]
radius_px: [9999, 56, 40]
motion: {durations_s: [0.6, 0.4, 0.53, 0.57, 0.37], easing: [ease-in-out, ease-out], loop: true}
scores: {aesthetics: 8, originality: 8, usability: 6, craft: 8}
craft_signals: [ball-arrow-rotates-with-roll, dashed-border-hint-pill, status-dot-colour-swap, gradient-border-blue-to-pink, mascot-count-encodes-tier, nested-card-frames]
anti_patterns: [hint-text-low-contrast, toggle-affordance-unconventional]
---
# Toggle to premium plans — @Designownow_

## 1. Snapshot
- **Subject:** A 1550×1080, 21.6 s, 60 fps loop. A chrome-like 3D ball with an arrow acts as a toggle. Clicking it rolls the ball to the right and unrolls a blue→pink "Premium" script band behind it. Below, the pricing card switches from Basic ($18/m, one blue mascot) to Premium ($32/m, three mascots, gradient border).
- **Why it's remarkable:** A plan toggle is turned into a physical object: the ball "paints" the premium band as it rolls, and the number of mascots scales with the tier.

## 2. Composition & layout
- **Layout:** a centred column between two 1 px vertical guide lines at x≈278 and x≈1246 (a 968 px content column on #e4e4e4).
- **Hint pill:** "Roll To Go Premium", centred at y≈320, about 400×80 px with a dashed 1 px border and a status dot at its left.
- **Ball:** about 190 px in diameter, starting at x≈370→560 and y≈410→593. After the roll it sits at the right end (about x 1075), with a band of about 600×110 px spanning from the left (frame at t=6.0 s).
- **Plan card:** x≈367→1150 (783 px wide), top at y≈672, outer radius about 56 px.
  - It has nested frames: an outer white shell (#f1f1f1), an inner inset of about 36 px with radius 40, then the content panel.
  - Content panel: plan pill ("● Basic Plan", about 285×80), price "$18/m", a feature row ("✓ 100 Credits A Month") and a mascot at the bottom-right.

## 3. Typography
- **Sans:** neo-grotesk (Inter or SF-like), regular.
  - Price "$18/m": about 100 px, weight 400, colour #383838, tracking about −0.02 em.
  - Pill labels: about 32 px in #787878.
- **Script:** "Premium" set in a connected brush script in white, about 60 px, inside the gradient band. The emotional upgrade is signalled by a type-style change.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #e4e4e4 | canvas | 89.5% |
| #f1f1f1 / #f3f3f3 | card shell | about 5% |
| #383838 | price text | — |
| #787878 | pill and feature text | — |
| #f25fb8 | Premium dot, gradient end | — |
| #1d81bd | Basic dot, gradient start | — |
| #585f71 / #96a1ab / #cbcccd | chrome ball shading | about 5.6% |

WCAG checks:
- Price #383838 on #f1f1f1: 10.38:1.
- Pill text #787878 on #e4e4e4: **3.47:1** (fails AA for 32 px regular at 1× scale; passes only as large text).
- The pink dot #f25fb8 on #e4e4e4 is 2.32:1, but it is decorative.

## 5. Depth & material
- **Ball:** brushed chrome sphere with a grainy noise texture, a highlight at the top-left, a dark lower hemisphere and a soft ground shadow of about 30 px blur. The arrow is debossed on its surface.
- **Mascots:** glossy 3D spheres (blue, pink, navy) with simple smiley faces.
- **Card:** soft elevation with nested inner bevels. The Premium state adds a 6 px gradient stroke (blue #1d81bd → violet → pink #f25fb8) around the inner frame.

## 6. Components & patterns
- **Toggle as ball:** the roll direction indicates on/off. Its label pill updates: "Roll To Go Premium" ↔ "Roll Back To Go Basic", and the dot changes pink ↔ blue.
- **Pricing card** with plan pill, price and feature list.
- **Tier visualised:** 1 mascot for Basic, 3 for Premium.

## 7. Motion
- **Measured:** 21.6 s at 60 fps, `motion_fraction` 0.13 (long holds between clicks), `seamless_loop_likely: true`. Six segments with a median of 0.47 s:
  - 3.77 s (0.60 s, `peak_at` 0.36, symmetric);
  - 9.67 s (0.40 s, ease-out, `peak_at` 0.21);
  - 11.87 s (0.53 s, symmetric);
  - 13.73 s (0.40 s, ease-out);
  - 16.97 s (0.57 s, symmetric);
  - 20.03 s (0.37 s, ease-out).
- **Reading:** Going to Premium (roll right, band unrolls) takes about 0.53–0.60 s with ease-in-out. Going back to Basic (roll left, band retracts) is faster, about 0.37–0.40 s, with an ease-out. The asymmetric timing makes the upgrade feel more ceremonial.
- The arrow on the ball rotates with the roll. The card's border and price swap in sync.

## 8. Brand system
n/a — not a brand system. Identity cues: blue→pink gradient for premium, smiley mascot spheres, and a chrome ball as the signature control.

## 9. UX
- Fun and clear once learned, but a ball is not a recognised toggle. The dashed hint pill does the explaining.
- Price change, border and mascots give strong feedback.
- The secondary text contrast (3.47:1) is weak.
- No keyboard or ARIA semantics can be inferred; it should map to `role="switch"`.

## 10. Craft signals
- The hint copy flips with state ("Roll To…" / "Roll Back To…"), and the dot colour mirrors the destination tier.
- The arrow embossed on the ball rotates consistently with rolling distance.
- The gradient direction (blue→pink) is shared by the band and the card border.
- The mascot count is 1 vs 3 per tier, a quantity metaphor.
- The nested card radii (56 → 40) are concentric with the inset (56 − 16 ≈ 40).

## 11. Reproduction recipe
```css
:root{--bg:#e4e4e4;--card:#f1f1f1;--ink:#383838;--muted:#6a6a6a;--blue:#1d81bd;--pink:#f25fb8;
  --grad:linear-gradient(90deg,#0f4c78,#1d81bd 35%,#f25fb8)}
.hint{border:1px dashed #b5b5b5;border-radius:9999px;padding:18px 32px;color:var(--muted)}
.hint::before{content:"";width:14px;height:14px;border-radius:50%;background:var(--pink);display:inline-block;margin-right:16px}
.toggle{position:relative;width:600px;height:110px}
.toggle .band{position:absolute;inset:0;border-radius:9999px;background:var(--grad);clip-path:inset(0 100% 0 0 round 9999px);
  transition:clip-path .58s cubic-bezier(.65,0,.35,1)}
.toggle .ball{width:190px;height:190px;border-radius:50%;position:absolute;left:0;top:-40px;
  background:radial-gradient(circle at 35% 30%,#fff,#9aa3ad 40%,#3b3f4a 85%);box-shadow:0 24px 30px rgba(0,0,0,.18);
  transition:transform .58s cubic-bezier(.65,0,.35,1)}
.toggle[aria-checked=true] .band{clip-path:inset(0 0 0 0 round 9999px)}
.toggle[aria-checked=true] .ball{transform:translateX(410px) rotate(360deg)}
.toggle[aria-checked=false] *{transition-duration:.38s;transition-timing-function:cubic-bezier(.16,1,.3,1)}
.card.premium .inner{border:6px solid transparent;background:linear-gradient(#f1f1f1,#f1f1f1) padding-box,var(--grad) border-box}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | A polished soft-3D set; chrome plus candy gradient work together. |
| Originality | 8 | The rolling ball that paints the premium band is inventive. |
| Usability | 6 | Strong feedback, but the unconventional affordance needs a hint; weak grey text. |
| Craft | 8 | Concentric radii, synced state cues, and asymmetric timing. |

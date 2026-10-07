---
id: insp-404-page
source: inspora
category: Web
status: analyzed
title: "404 page"
creator: "elaya (@elayadesigns)"
styles: [photo-led, x-anime-illustration, terminal-mono, cinematic-3d]
patterns: [error-page-metaphor-scene, translucent-giant-numerals, hairline-divider, centered-single-column, ambient-particle-loop, logo-only-header]
mode: mixed
palette: ["#1c6bb5", "#3484c4", "#212f35", "#364e62", "#d9d4d0", "#aabccf", "#ffffff"]
type_families: ["Space Mono / JetBrains Mono-style monospace (likely)", "Inter-style neo-grotesk (logo)"]
type_class: [mono, neo-grotesk]
radius_px: []
motion: {durations_s: [0.23, 0.57, 0.73, 0.40, 0.23, 0.73], easing: [ease-in, ease-out, ease-in-out], loop: false}
scores: {aesthetics: 9, originality: 8, usability: 4, craft: 7}
craft_signals: [numerals-bridge-the-gap, opacity-ramp-across-digits, slashed-zero-mono, hairline-matches-text-width, gap-placed-at-optical-center]
anti_patterns: [no-visible-cta, text-over-busy-image-risk, low-contrast-over-clouds]
---
# 404 page — elaya

## 1. Snapshot
- **Subject:** A 1760×1080, 4.8 s clip of a 404 page for "Metricra". It shows a ruined stone viaduct with a missing span in the centre, painted in an anime style. A huge translucent "404" floats exactly in the gap, with a one-line mono apology below.
- **Why it's remarkable:** The error is literalised. The page is a broken bridge, and the numerals sit where the missing span would be, so they act as a ghost bridge. One image explains "the link you followed is broken" without a word.

## 2. Composition & layout
- **Symmetry:** Strict central axis.
  - The logo sits centred at y≈103.
  - "404" spans x≈605–1155 (about 550 px wide, ~31% of frame), with a cap height of ~235 px from y≈335 to 570.
  - A 1 px hairline runs at y≈625, ~525 px wide, matching the numeral block's width.
  - Two lines of mono copy are centred at y≈697 and 729.
- **Scene:** The bridge decks enter from the top-left and right and converge on the numerals. Their railings form leading lines toward the "0". The broken deck ends meet the digits' baseline region at y≈450–570, so the gap is filled by type.
- **Space:** The lower 30% is landscape (valley, river, trees) and serves as breathing room. No UI sits there.

## 3. Typography
- **Numerals:** "404" is set in a heavy monospace with a slashed zero, in the Space Mono or JetBrains Mono Bold family, at roughly 320 px font-size.
- **Body:** The same mono family at ~26 px with ~32 px leading (1.23), tracking at the font default. The straight apostrophes in "isn't"/"Let's" confirm a code face.
- **Logo:** "Metricra" in a neo-grotesk at ~24 px regular with a bar-chart-like glyph.
- **Voice:** "The path may be broken, but the journey isn't." It is warm and metaphorical, and consistent with the image.
- The mono choice adds a "system message" tone on top of a painterly, emotional scene. The contrast between the two is the point.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #212f35 / #323b40 | stone, shadowed bridge | 26% |
| #1c6bb5 | zenith sky (text field for logo) | 17% |
| #3484c4 / #4c83b3 | mid sky behind numerals | 13% |
| #364e62 | mist and distant hills | 4% |
| #d9d4d0 / #aabccf | cloud lights | 8% |
| #ffffff at ~55–85% | numerals, hairline, copy | — |

WCAG checks:
- White on #1c6bb5 is **5.5:1** (pass).
- On #3484c4 it is **4.0:1** (large only).
- Where the body copy crosses clouds (#d9d4d0) it is **1.47:1**. The words "broken", "but" and "get you" visibly break up against the cloud bank.
- White on #6f9dc6 is 2.87:1.

The copy has no scrim or text-shadow, which is the main legibility failure.

## 5. Depth & material
- **Painted depth:** atmospheric haze between the near bridge, mid-ground clouds and the far valley, plus god-ray mist at the bottom-left.
- **Numerals:** translucent white with an opacity ramp. The first "4" is about 55% opacity (stone shows through), the "0" about 70%, and the last "4" about 85%. This makes the type feel like a glass fragment floating in front of the bridge rather than printed on it.
- **Overlay discipline:** No shadows or blur on UI elements. Particles (fireflies, dust) are the only light sources.

## 6. Components & patterns
- **Header:** logo only, with no nav. That is acceptable for an error page but leaves no way out.
- **Hero:** giant code numerals, a hairline divider, and a two-line message.
- **CTA:** None is visible. "Let's get you back" promises an action the page does not provide. A cursor hovers at bottom-right over nothing.

## 7. Motion
- **Measured:** 4.8 s at 30 fps, motion_fraction **0.50**, mean energy 0.34, 6 segments with a median of 0.48 s; not a seamless loop (first/last diff 19.6).
- **Segments:**

  | Time (s) | Duration (s) | Curve |
  |---|---|---|
  | 0.37–0.60 | 0.23 | ease-in |
  | 0.87–1.43 | 0.57 | ease-out |
  | 1.53–2.27 | 0.73 | ease-in |
  | 2.37–2.77 | 0.40 | ease-in |
  | 2.87–3.10 | 0.23 | ease-out |
  | 3.70–4.43 | 0.73 | ease-in-out |

- **Interpretation:** These are low-energy bursts of particle drift and cloud shimmer. The frames show fireflies moving at the bottom-left and sparkles at the top, while the UI stays fixed. This is ambient life, not interface feedback. The varied curves read as organic, AI-generated motion (the creator's sibling post was made in Seedance).

## 8. Brand system
n/a — not a brand system. Identity cues:
- the Metricra bar-glyph mark;
- mono type as a "system voice";
- the same anime-sky world as the creator's Finmain hero, which suggests a personal visual signature.

## 9. UX
- **Strength:** Instantly understandable and emotionally soft, so the error feels like a moment rather than a failure.
- **Weaknesses:**
  - No home link, search or button.
  - The copy fails contrast where it crosses clouds.
  - The numerals' low opacity on the left makes "4" weaker than "04".
  - On mobile, the 16:10 scene would crop away the gap that carries the meaning.

## 10. Craft signals
- The numerals are positioned exactly in the bridge gap, and the deck ends align with digit edges at x≈605 and x≈1155.
- The hairline width (≈525 px) matches the numeral block, which matches the text measure.
- The slashed zero is a deliberate code reference.
- The opacity ramps left to right across the three digits.
- Ambient particles are kept off the copy zone.

## 11. Reproduction recipe
```css
:root{--ink:#fff;--sky:#1c6bb5;--stone:#212f35;--font-mono:"Space Mono","JetBrains Mono",ui-monospace,monospace}
.err{min-height:100vh;display:grid;place-items:center;text-align:center;
  background:url(broken-bridge.webp) center 40%/cover;color:var(--ink)}
.err h1{font:700 clamp(160px,18vw,320px)/.85 var(--font-mono);font-variant-numeric:slashed-zero;
  background:linear-gradient(90deg,rgba(255,255,255,.55),rgba(255,255,255,.88));
  -webkit-background-clip:text;color:transparent}
.err hr{width:30ch;border:0;border-top:1px solid rgba(255,255,255,.6);margin:48px auto 56px}
.err p{font:400 26px/1.25 var(--font-mono);max-width:32ch;text-shadow:0 1px 12px rgba(0,30,60,.55)} /* add scrim */
.particle{animation:drift 6s ease-in-out infinite alternate}
@keyframes drift{to{transform:translate3d(12px,-18px,0);opacity:.4}}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 9 | Breathtaking scene, and the numerals integrate with the composition. |
| Originality | 8 | The broken-bridge metaphor with numerals in the gap is a smart literal pun. |
| Usability | 4 | No recovery action, and the copy breaks up over clouds. |
| Craft | 7 | Precise alignment and opacity ramp. Legibility protection is missing. |

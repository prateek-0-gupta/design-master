---
id: insp-3-2
source: inspora
category: Product
status: analyzed
title: "Take your wallet everywhere."
creator: "@tojawuzik"
styles: [aurora-glow, minimal-swiss, y2k-chrome]
patterns: [onboarding-splash, iridescent-ribbon-background, centered-logomark, bottom-left-stacked-headline, dual-pill-auth-buttons, ambient-background-loop]
mode: light
palette: ["#f2f2f2", "#ffffff", "#000000", "#55659f", "#a6d6df", "#a36665", "#fefacd"]
type_families: ["Inter Display / SF Pro Display-style neo-grotesk (likely)"]
type_class: [neo-grotesk]
radius_px: [56, 9999]
motion: {durations_s: [0.43, 0.23, 0.1], easing: [ease-out, linear], loop: true}
scores: {aesthetics: 8, originality: 6, usability: 6, craft: 5}
craft_signals: [one-word-per-line-headline, ribbon-avoids-logo-zone, chromatic-fringe-on-ribbon, white-fade-into-buttons, black-only-ink]
anti_patterns: [typo-sing-up, ghost-buttons-low-separation, equal-weight-primary-secondary-cta]
---
# Take your wallet everywhere. — @tojawuzik

## 1. Snapshot
- **Subject:** A 5.0 s, 1080×1080 loop of a crypto-wallet onboarding splash: white phone screen, a black pinwheel logomark, a four-line headline and Login / Sign-up pills, with an iridescent holographic ribbon flowing down the right side.
- **Why it's remarkable:** All colour lives in one oil-slick ribbon; everything else is pure black on white. The ribbon's S-curve frames the headline and logo like a parenthesis.

## 2. Composition & layout
- Phone screen ~398×865 px centred (x≈340–738, y≈108–973) on a #f2f2f2 stage; screen corner radius ~56 px.
- Logomark (~75 px) sits at x≈537, y≈423 — horizontally centred, roughly 37% down the screen.
- Headline is left-aligned at x≈377 (≈37 px inset), occupying y≈668–838; one word per line ("Take / your / wallet / everywhere"), so the rag steps out to a long final line.
- Two pill buttons ~150×52 px at y≈903, inset 37 px each side, with a ~22 px gap; home indicator below.
- The ribbon enters at top-centre, hugs the right edge through the middle, then sweeps back to bottom-left under the buttons — an S that keeps the logo zone and the left text column clear.

## 3. Typography
- Neo-grotesk, Semibold (≈600), close to Inter Display or SF Pro Display. Headline ≈44 px with very tight leading (≈0.98) and ≈−0.02 em tracking; descenders of "y" nearly touch the next line's caps.
- Button labels ≈19 px Regular/Medium, black. Status bar uses SF-style 9:41.
- Only two type sizes on the screen; hierarchy is size + position.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #f2f2f2 | stage | ~74% |
| #ffffff | screen surface | ~15% |
| #000000 | logomark, headline, labels | ~2% |
| #55659f / #a6d6df | ribbon blue/cyan | ~2% |
| #a36665 / #d2ad9b | ribbon copper/rose | ~2% |
| #fefacd | ribbon yellow highlight | ~1% |

WCAG: black on white **21:1**; black on the palest ribbon cyan (#a6d6df) still **13.31:1**, so the headline stays legible where the ribbon passes behind "everywhere". Button fill vs screen is ~1.12:1 (white on #f2f2f2-ish) — the pills are nearly invisible as shapes.

## 5. Depth & material
- The ribbon reads as a holographic foil/thin-film material: rainbow bands with fine parallel striations and chromatic fringing at the edges, blurred where it recedes (top right) and sharp where it comes forward (mid right).
- Buttons are frosted white pills with a soft ~10 px shadow; the left "Login" pill is translucent so the ribbon tints it.
- No other shadows; the phone has no bezel, just a rounded white slab.

## 6. Components & patterns
- Onboarding splash: brand mark, value-prop headline, auth CTA pair.
- Dual pill buttons of equal size and style — neither is marked as primary.
- Ambient animated background as the only motion.

## 7. Motion
Measured: duration 5.03 s, motion fraction 0.43, mean energy only **0.35** (p95 0.37) with segment energy CV ≈0.01–0.02 — i.e. a low, near-constant drift, not discrete transitions. Detector segments are ~1 s apart (0.33, 1.33, 2.33, 3.33, 4.33 s, each 0.43–0.47 s, peak ≈0.19 → ease-out), which matches a looping texture whose undulation pulses about once per second. `seamless_loop_likely: true`.
- From frames: the ribbon's folds slide slightly and the colour bands shift hue; logo, text and buttons are static. Treat it as a continuous shader/video loop rather than UI animation.

## 8. Brand system
n/a — not a brand system. Identity cues: four-blade pinwheel mark (two pairs of opposing curved wedges), holographic ribbon as the "wallet energy" motif, strict black/white typography.

## 9. UX
- Clear single message and two obvious exits.
- Risks: the button label reads **"Sing up"** (typo). The two CTAs are visually equal, so the expected primary action (sign up for a new user) isn't prioritised. Button shapes have ~1.1:1 contrast with the surface, failing the 3:1 non-text guideline.

## 10. Craft signals
- Headline left edge and Login button left edge share the same 37 px inset.
- The ribbon's path is choreographed to stay behind the right half of the headline only, never behind the first letters of each line.
- Ribbon blur increases toward the top, giving a depth-of-field gradient.
- Monochrome UI ink (#000) with zero greys.

## 11. Reproduction recipe
```css
:root{--stage:#f2f2f2;--screen:#fff;--ink:#000;--r-screen:56px;--r-pill:9999px;
  --font:"Inter Display","SF Pro Display",system-ui,sans-serif;}
.screen{width:398px;height:865px;border-radius:var(--r-screen);background:var(--screen);
  position:relative;overflow:hidden;padding:0 37px}
.ribbon{position:absolute;inset:-10%;pointer-events:none;
  background:conic-gradient(from 200deg at 80% 40%,#55659f,#a6d6df,#fefacd,#d2ad9b,#a36665,#dccdd2,#55659f);
  -webkit-mask:url(ribbon-path.svg) center/cover no-repeat;filter:blur(6px) saturate(1.3);
  animation:drift 5s ease-in-out infinite alternate}
@keyframes drift{to{transform:translate(-8px,12px) rotate(1.5deg);filter:blur(6px) saturate(1.3) hue-rotate(20deg)}}
h1{font:600 44px/0.98 var(--font);letter-spacing:-.02em;color:var(--ink)}
.btn{height:52px;border-radius:var(--r-pill);background:rgba(255,255,255,.75);
  backdrop-filter:blur(12px);box-shadow:0 6px 20px rgba(0,0,0,.06);font:500 19px var(--font)}
```
In production, a video/WebGL thin-film shader on the ribbon is more faithful than CSS gradients.

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Striking contrast between holographic ribbon and stark black type. |
| Originality | 6 | Iridescent fluid backgrounds are a common 2024–26 trend. |
| Usability | 6 | Readable, but equal CTAs and invisible button shapes. |
| Craft | 5 | Good composition undone by the "Sing up" typo. |

---
id: insp-lookaway-ios
source: inspora
category: Motion
status: analyzed
title: "LookAway iOS"
creator: "kush (@kushsolitary)"
styles: [dark-premium, playful-rounded, aurora-glow, grain-noise]
patterns: [mascot-app-icon, expression-cycling-icon, success-state-screen, paired-device-row, particle-halo, live-activity-recording-dot]
mode: dark
palette: ["#110f11", "#252325", "#382335", "#5c5ebb", "#c8739a", "#e5be8f", "#34c759", "#ffffff"]
type_families: ["SF Pro Display / Text (likely)"]
type_class: [neo-grotesk]
radius_px: [44, 22, 9999]
motion: {durations_s: [0.1, 1.6, 14.48], easing: [ease-out], loop: true}
scores: {aesthetics: 8, originality: 7, usability: 8, craft: 8}
craft_signals: [backdrop-gradient-echoes-icon, warm-cool-split-halo, icon-squash-on-expression-swap, sparkle-particles-in-halo, secondary-text-passes-aa, grainy-backdrop]
anti_patterns: [unchanging-status-copy]
---
# LookAway iOS — kush

## 1. Snapshot
- **Subject:** A 14.5 s, 1080×1080 loop of an iOS "Mirror is now active" confirmation screen for LookAway (an eye-break app synced with a Mac); the pink blob mascot inside the app icon keeps changing its face.
- **Why it's remarkable:** A static success screen is kept alive only by the mascot's expressions (sleepy, wink, happy, squint) — personality without any layout motion.

## 2. Composition & layout
- Square frame, grainy gradient backdrop (indigo #5c5ebb top → orchid #9d6fb1 → rose #c8739a → peach #e5be8f bottom). The phone is cropped below the screen's midpoint; it sits ~110 px from left/right edges.
- Inside the phone (screen ≈ 790 px wide): status bar at y≈205; app icon ≈ 195 px (y≈325→520) centred; title at y≈598; two-line body at y≈660/698; paired-device card at y≈802→942 (≈ 730×140 px, 22 px radius).
- Strong single centre axis; vertical rhythm ≈ 78 px icon→title, 60 px title→body, 100 px body→card.

## 3. Typography
- SF Pro: title "Mirror is now active" ≈ 40 px semibold white (≈ 20 pt at device scale); body ≈ 28 px regular grey, centred, two lines with ~38 px leading (1.35); card title ≈ 28 px medium white; card meta ≈ 22 px regular grey.
- Weight + value hierarchy only; all text sentence case.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #110f11 | screen base / bezel | 25% |
| #252325 | card surface, upper screen | 19% |
| #382335 / #41352f | magenta-left, amber-right halo behind icon | 20% |
| #5c5ebb → #e5be8f | backdrop gradient (indigo→peach) | 27% |
| #c8739a | rose band of backdrop, mascot pink | 4% |
| #34c759 | iOS green bolt (connected) | <1% |
| #ff3b30 (est.) | recording dot in Dynamic Island | trace |

WCAG checks:
- Title white on halo #2a1f2a: 15.8:1.
- Body grey ≈#8e8a8e on #2a1f2a: **4.65:1 (passes AA)**.
- Card meta ≈#8a8a8a on #252325: 4.52:1 (just passes).
- Green bolt #34c759 on its tinted disc #1f3a26: 5.59:1.

## 5. Depth & material
- The halo behind the icon splits warm/cool: magenta on the left, amber on the right — the same hues as the mascot's pink-to-yellow gradient, so the icon appears to cast its colour.
- Sparse white particle specks (2–6 px) orbit the icon area at varied opacity.
- App icon: near-black squircle (≈44 px radius at this size) with a subtle top highlight; the mascot is a glossy gradient blob (#e85ad6 → #f07090 → #e5c06a).
- Backdrop carries visible film grain (~1 px noise), keeping the gradient from banding.

## 6. Components & patterns
- Success/confirmation screen: icon + headline + reassurance copy + the paired-device row.
- Paired device row: 56 px bolt in a tinted green circle, two-line label ("Kush's Mac Studio" / pairing date), trailing overflow "•••".
- Dynamic Island shows a red recording dot — the system-level "mirroring" indicator, consistent with the copy.
- Mascot expression set seen: ᵕ‿ᵕ closed-happy, >– wink, ^^ smile, >< squint, –< reverse wink.

## 7. Motion
Measured (m0_motion.json): 14.48 s, 60 fps, motion_fraction 0.05, `seamless_loop_likely: true` (first/last diff 0.5). Only one segment crosses threshold: **8.97–9.07 s (0.10 s), peak_at 0.17 → fast ease-out** — a snap of the icon.
- Frame comparison: the icon scales down noticeably at 8.85 s and 12.07 s (≈ 175 px vs 195 px, ≈ −10%) during expression swaps — a quick squash-and-pop.
- Expressions change roughly every 1.6 s (nine frames, eight distinct-or-repeated faces), estimated.
- Particles drift slowly (sub-threshold), keeping the halo shimmering.

## 8. Brand system
n/a — not a brand system, but strong identity cues: the blob mascot as the icon, its pink→gold gradient reused in the halo and backdrop, and emotive "eye" expressions that tie to the eye-break product purpose.

## 9. UX
- Tells the user the one thing they need: it's working, and you can leave the app. The copy explicitly removes the burden ("No need to keep it on screen").
- The paired-device row confirms which Mac — good trust signal; the overflow menu offers unpair.
- Contrast is genuinely AA-compliant for secondary text, unusual for dark showcase shots.
- Minor: the headline never changes while the icon animates; there's no explicit "done" action, though background-running is the point.

## 10. Craft signals
- Halo hue split (magenta left / amber right) maps to the mascot's own gradient direction.
- Icon squash of ≈10% coincides with expression swaps, hiding the cut.
- Secondary text tuned to ≈4.5–4.7:1, just over AA.
- Status icons, card and text all on one centre axis; card inset matches body text width (~730 px).
- Grain applied to the outer backdrop only, not to UI surfaces.

## 11. Reproduction recipe
```css
:root{--bg:#110f11;--card:#252325;--text:#fff;--text-2:#8e8a8e;--ok:#34c759;
  --mascot:linear-gradient(135deg,#e85ad6,#f07090 55%,#e5c06a);}
.screen{background:
  radial-gradient(40% 30% at 35% 28%,#5a2850aa,transparent 70%),
  radial-gradient(40% 30% at 65% 28%,#5a4426aa,transparent 70%),var(--bg)}
.icon{width:96px;aspect-ratio:1;border-radius:22px;background:#0c0b0c;animation:pop 1.6s infinite}
@keyframes pop{0%,88%{transform:scale(1)}92%{transform:scale(.9)}100%{transform:scale(1)}}
.title{font:600 20px/1.2 -apple-system,"SF Pro Display";color:var(--text)}
.body{font:400 14px/1.35 -apple-system;color:var(--text-2);text-align:center}
.device-row{background:var(--card);border-radius:11px;padding:12px 16px;display:flex;gap:12px}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Warm dark screen with a cohesive pink-gold glow story. |
| Originality | 7 | Mascot-as-status is known; expression cycling in the icon is charming. |
| Usability | 8 | Clear state, reassuring copy, AA-passing secondary text. |
| Craft | 8 | Colour echoing, squash timing, grain on backdrop only. |

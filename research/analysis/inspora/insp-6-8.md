---
id: insp-6-8
source: inspora
category: Motion
status: analyzed
title: "A sending animation"
creator: "@privetavdey"
styles: [dark-premium, micro-interaction, x-scanline-glyph]
patterns: [bottom-sheet-status, confirm-to-progress-to-success, scanline-3d-icon, state-tinted-sheet, mono-cta-label, camera-push-to-device]
mode: dark
palette: ["#100e0f", "#ffffff", "#1e4735", "#162820", "#3c946e", "#e6e6e6"]
type_families: ["Satoshi / General Sans-style grotesk (likely)", "Geist Mono / IBM Plex Mono-style monospace (likely)"]
type_class: [grotesk, mono]
radius_px: [9999, 40, 24]
motion: {durations_s: [0.73, 0.33, 0.53], easing: [ease-out], loop: true}
scores: {aesthetics: 8, originality: 8, usability: 8, craft: 8}
craft_signals: [vertical-scanline-fill-on-icon, outer-glow-matches-state-colour, sheet-tint-gradient-fades-to-surface, background-content-blurred-behind-sheet, mono-reserved-for-actions-and-fees, same-cta-position-across-states]
anti_patterns: [dim-helper-text-near-aa-limit]
---
# A sending animation — @privetavdey

## 1. Snapshot
- **Subject:** A 19.3 s, 1152×1152 screen recording of a crypto send flow in "Shield Wallet". It runs from a confirm screen to a "Sending…" bottom sheet with a rotating paper-plane glyph, then to a green "Sent" state with a checkmark.
- **Why it's remarkable:** Both status icons are drawn as dense vertical scanlines with a soft glow. A stock "paper plane → check" sequence reads like a CRT readout, and that suits a privacy wallet.

## 2. Composition & layout
- **Framing:** An iPhone mockup (about 465 px wide at the 1152 px frame) sits centred on pure white #ffffff, which fills about 55% of the frame. During the send states the camera pushes in about 1.5×, so the phone's top is cropped and the sheet fills the middle.
- **Confirm screen:** A stack of centred elements:
  - title at y≈257;
  - "From" chip row;
  - two stacked cards (about 395×160 px each), joined by a notched ↓ connector where the cards' corners are cut away around a small arrow;
  - a large empty gap;
  - a mono "NO NETWORK FEE" line;
  - a full-width pill CTA, about 50 px tall.
- **Status sheet:** A modal sheet with a grabber covers the bottom ~80% of the screen. The icon sits in the upper half (about 330 px box). Below it are the headline at y≈670, two lines of helper text and the DONE pill at y≈855. The pill is the same width and position in both the Sending and Sent states.

## 3. Typography
- **Headline:** "Sending privately" is about 36 px (at 1152 px) in a semibold geometric-leaning grotesk with tight tracking (≈−0.02 em), close to Satoshi or General Sans. "Sent" is about 44 px semibold.
- **Helper text:** about 20 px regular in mid-grey (#8c8c8c), on two centred lines.
- **Mono:** Used for every action and system label: "CONFIRM", "DONE", "NO NETWORK FEE". It is set at about 16 px in caps with wide tracking (≈+0.08 em). Amounts ("2,342.5 ALEO") stay in the sans.
- **"Sending…" headline:** rendered in grey (#9a9a9a) while pending and switches to pure white on "Sent", so text value itself signals completion.

## 4. Colour
| Hex | Role | Share (key frame) |
|---|---|---|
| #ffffff | stage background, CTA pill | 55% |
| #100e0f | app surface / phone screen | 22% |
| #1e4735 | success sheet tint (top) | 9% |
| #162820 / #17392b | gradient mid-stops into surface | 9% |
| #3c946e | checkmark scanlines + glow | 3% |
| #e6e6e6 | pending plane glyph (grey-white) | 1% |

WCAG checks:
- White on #100e0f is 19.24:1.
- Helper grey #8c8c8c on #100e0f is 5.72:1 (pass).
- The dimmer "1 previous send" (≈#6e6e6e) is 3.77:1 (large-only).
- "Sent" white on the green top #1e4735 is 10.46:1.
- The #100e0f DONE label on the white pill is 19.24:1.

Strategy: The UI is achromatic, and green appears only at the success moment, as a top-down gradient tint on the sheet (#1e4735 → #100e0f by about 55% height).

## 5. Depth & material
- **Sheet:** radius about 40 px on its top corners. The content behind it (the "2,342.5 ALEO" header) is Gaussian-blurred by about 12 px rather than dimmed. This is frosted occlusion and needs no scrim.
- **Glyphs:** filled with 1–2 px vertical lines at about a 4 px pitch, with an outer glow of about 8–12 px in the glyph's own colour. Faint rectangular "ghost" blocks of horizontal scanlines flicker around the glyph, like a raster/glitch halo.
- **Cards on the confirm screen:** a vertical gradient #1c1c1c → #100e0f with no border and no shadow.

## 6. Components & patterns
- **Confirm summary:** a two-card from→to stack with a notched connector, token avatar, gradient address avatar and fiat sub-value.
- **Status bottom sheet:** grabber, glyph, headline and helper text; "you can close this now" tells the user the operation is non-blocking.
- **Success state:** shown by a sheet tint change, not by a toast.
- **CTA:** a single white pill (9999 radius). Its label flips CONFIRM → DONE.

## 7. Motion
Measured (m0_motion.json, 30 fps, 19.33 s, motion_fraction 0.08, seamless_loop_likely true): three discrete segments, all ease-out (fast start):
- **1.50–2.23 s (0.73 s, peak at 0.30):** confirm → sheet. The sheet rises while the camera pushes in.
- **7.97–8.30 s (0.33 s, peak at 0.25):** Sending → Sent. The plane glyph morphs or cross-fades into the check and the green tint floods in.
- **15.63–16.17 s (0.53 s, peak at 0.28):** the sheet dismisses and the camera pulls back to the start, closing the loop.

Between segments, the plane rotates slowly in 3D (frames 3.22 → 5.37 → 7.52 s show it yawing about 30–60°) and the check wobbles the same way. This energy stays below the detector threshold, so it is a slow continuous idle of about 2 s per swing (estimate). The fast-attack, long-tail easing makes the state changes snap, and the idle keeps the wait alive.

## 8. Brand system
n/a — this is product UI, not a brand system. Identity cues:
- the scanline glyph language, which could extend to all status icons;
- mono caps for actions;
- the "privately" framing in the headline.

## 9. UX
- Clear three-step state model (confirm / pending / done), with an exit offered at every step.
- The fee-free claim sits right above the CTA, at the decision point.
- Pending helper text sets expectations ("Should take a moment").
- **Risk:** Success is coded by colour and by the icon swap. The headline word change also carries it, so this is acceptable. The dimmest captions are under 4.5:1.

## 10. Craft signals
- Glyph fill is vertical lines at a consistent ~4 px pitch. The glow colour equals the line colour: white-grey for pending, #3c946e for success.
- The sheet's green tint fades out before the headline, so "Sent" sits on near-neutral #100e0f.
- The background header is blurred, not dimmed, behind the sheet.
- The DONE pill keeps an identical x/y/width across states, so nothing jumps under the thumb.
- Mono is used only for verbs and system facts. Amounts and addresses stay in the sans.
- The camera push-in and pull-out keep the whole loop seamless (first/last diff 0.23).

## 11. Reproduction recipe
```css
:root{--surface:#100e0f;--text:#fff;--text-2:#8c8c8c;--ok:#3c946e;--ok-tint:#1e4735;
  --r-sheet:40px;--font-sans:"Satoshi","General Sans",system-ui;--font-mono:"Geist Mono",ui-monospace;}
.sheet{border-radius:var(--r-sheet) var(--r-sheet) 0 0;background:var(--surface);transition:background .33s cubic-bezier(.2,.8,.2,1)}
.sheet[data-state=sent]{background:linear-gradient(180deg,var(--ok-tint) 0%,#162820 30%,var(--surface) 55%)}
.glyph{width:220px;aspect-ratio:1;
  -webkit-mask:url(plane.svg) center/contain no-repeat;mask:url(plane.svg) center/contain no-repeat;
  background:repeating-linear-gradient(90deg,currentColor 0 1.5px,transparent 1.5px 4px);
  filter:drop-shadow(0 0 10px currentColor);color:#e6e6e6;animation:yaw 4s ease-in-out infinite alternate}
.sheet[data-state=sent] .glyph{color:var(--ok)}
@keyframes yaw{from{transform:perspective(600px) rotateY(-30deg)}to{transform:perspective(600px) rotateY(30deg)}}
.cta{border-radius:9999px;height:50px;background:#fff;color:var(--surface);font:500 16px/1 var(--font-mono);letter-spacing:.08em}
.behind{filter:blur(12px)}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Restrained black UI with one emotional green moment; the scanline glyphs are distinctive. |
| Originality | 8 | The send → check idea is common, but the raster/scanline rendering is a fresh treatment. |
| Usability | 8 | Explicit states, non-blocking copy, stable CTA; minor low-contrast captions. |
| Craft | 8 | Consistent pitch and glow, blur-not-scrim, tight timing (0.33 s state swap). |

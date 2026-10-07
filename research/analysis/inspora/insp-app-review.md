---
id: insp-app-review
source: inspora
category: Motion
status: analyzed
title: "App review"
creator: "@RobSwish"
styles: [cinematic-3d, aurora-glow, physical-material]
patterns: [status-as-weather, full-bleed-state-screen, paper-plane-progress, centered-icon-title-body, stacked-pill-actions, device-mockup-floor-glow, particle-rain-overlay]
mode: mixed
palette: ["#bfbfbf", "#a083dd", "#6f4cc7", "#349df9", "#d6fbff", "#252f48", "#42599c", "#263b68"]
type_families: ["SF Pro Display / Text (likely)"]
type_class: [neo-grotesk]
radius_px: [9999, 60]
motion: {durations_s: [0.63, 0.83, 1.93, 1.6, 0.37, 0.33], easing: [ease-in-out, ease-in, ease-out], loop: false}
scores: {aesthetics: 9, originality: 8, usability: 6, craft: 8}
craft_signals: [screen-colour-spills-onto-floor, sun-rays-from-dynamic-island-corner, plane-icon-burns-on-reject, rain-streaks-angled-15deg, same-layout-across-states, tinted-glass-buttons-per-state]
anti_patterns: [white-text-on-bright-blue-fails, white-on-lavender-sending-label]
---
# App review — @RobSwish

## 1. Snapshot
- **Subject:** A 16.4 s, 2160×2160 render of an iPhone status screen for App Store review. It has three states, each a full-bleed weather mood:
  - "Sending": a lavender sky with a paper plane flying through cloud;
  - "Sent": a sunny blue sky with light rays;
  - "Rejected": a navy night sky with rain, where the paper plane falls and burns.
- **Why it's remarkable:** It maps an anxious bureaucratic process onto weather, so the user *feels* the status before reading it. The layout stays identical across states, so only the atmosphere changes.

## 2. Composition & layout
- A frontal iPhone (about 860×1820 px of the 2160 frame, centred) on a seamless light-grey sweep (#bfbfbf) with fine noise.
- The screen's colour spills onto the floor as a soft reflection under the phone: lavender, then cyan, then cool white.
- **On-screen layout (the same in every state):**
  - icon about 90 px at about 35% of screen height;
  - 18 px gap, then the title;
  - body text centred at about 75% width;
  - actions pinned about 110 px above the home indicator.
- **Buttons:** full-width minus 64 px side margins, about 95 px tall, fully rounded. Rejected stacks two buttons with a 12 px gap.

## 3. Typography
- SF Pro (system). Title "Sent" or "Rejected" is about 46 px Semibold. Body is about 26 px Regular, two lines, centred, with leading of about 1.3.
- Button labels are about 26 px Medium.
- The "Sending" label is about 30 px Medium, white over lavender.
- Sentence case throughout, and the copy is plain and factual ("App Review left notes for you in App Store Connect.").

## 4. Colour
| Hex | Role | State |
|---|---|---|
| #bfbfbf | studio backdrop | all, ~56% |
| #a083dd / #6f4cc7 | lavender cloud sky | Sending |
| #349df9 | sky blue | Sent, ~20% |
| #d6fbff | pale-cyan "Done" button, sun glare | Sent |
| #252f48 | night navy | Rejected |
| #42599c | primary glass button | Rejected |
| #263b68 | secondary "Close" button | Rejected |

WCAG:
- **Sent:** white body on #349df9 is **2.86:1 (fails)**, and the light-blue body #e6f2ff is 2.52:1. Bright, happy colour costs legibility.
- "Done" #1c1c1e on #d6fbff is 15.48:1.
- **Rejected:** white on #252f48 is 13.3:1, body #c5cbd8 is 8.18:1, the primary button is 6.69:1 and "Close" is 11.01:1.
- **Sending:** the white label on lighter cloud #c6aff7 drops to **1.93:1**.

Ironically, the bad-news state is the most accessible.

## 5. Depth & material
- **Device:** a photoreal titanium frame with a specular edge.
- **Screen light:** casts a coloured floor glow 150–200 px tall. It changes hue per state, which is the strongest cinematic cue.
- **Atmosphere:**
  - Sending: volumetric clouds drift behind the icon.
  - Sent: radial light rays fan out from the top-right corner (beside the Dynamic Island).
  - Rejected: thin rain streaks (1–2 px, about 20–40 px long, angled about 15° from vertical) at about 30% opacity.
- **Buttons:** translucent tinted glass with a 1 px lighter top edge.

## 6. Components & patterns
- A full-screen status state with icon, title, body and actions (Apple's "result screen" template).
- **Icons:** a paper plane (Sending), a check in a white circle (Sent), a clipboard with ✕ (Rejected).
- **Transition storytelling:** at 9.99 s the paper plane falls, with a small orange flame or ember on it, into the dark state before the Rejected icon fades in.

## 7. Motion
The motion is measured: 16.35 s, 60 fps, motion_fraction 0.38, not a loop.
- **0.47–1.33 s:** two short segments, an ease-out at 0.13 s and a symmetric 0.63 s. These are the plane entrance and the cloud parallax begin.
- **2.47–3.30 s:** a 0.83 s symmetric segment, the cloud drift.
- **5.40–7.33 s:** a 1.93 s ease-in segment (peak 0.80). This is the Sending → Sent wipe, as rays and blue flood in and accelerate.
- **9.70–11.30 s:** 1.6 s symmetric with a high energy CV of 2.01. This is the plane falling plus the darkening to rain.
- **11.47–14.27 s:** three short ease-out segments (0.37 / 0.33 / 0.33 s, peak_at 0.05–0.14). These are the Rejected text and buttons popping in staggered, with a fast start and soft settle.

Between beats the screens hold still for 1–2 s, so the copy can be read.

## 8. Brand system
n/a — not a brand system. It follows Apple's native visual language: SF Pro, glass buttons, the status-screen template.

## 9. UX
- **Pro:** status is recognisable pre-attentively, the layout stays constant, and the Rejected state offers a clear primary action (Open in App Store Connect) plus Close.
- **Con:**
  - Body text on the Sent screen fails contrast.
  - The Sending label disappears into light clouds.
  - Using weather humour for a rejection may read as flippant to some developers.

## 10. Craft signals
- The floor glow under the phone changes hue with the screen state (lavender, then cyan, then white-blue).
- The sun rays originate off-screen top-right, not centred, which reads as naturalistic.
- Rain streaks share one angle (about 15°) with varying length and opacity.
- Icon, title and body positions are pixel-identical across three states, so only the content swaps.
- The button tint is derived from the state's sky (#42599c on navy, #d6fbff on blue).
- The paper-plane icon continues as a falling, burning object into the next state, a continuity cut.

## 11. Reproduction recipe
```css
:root{--sending:#7a55d6;--sent:#349df9;--rejected:#252f48}
.status{position:absolute;inset:0;display:grid;place-items:center;text-align:center;color:#fff;font-family:-apple-system,"SF Pro Text"}
.status h1{font:600 46px/1.1 -apple-system;margin-top:18px}
.status p{font:400 26px/1.3 -apple-system;max-width:75%;opacity:.9}
.status[data-state=sent]{background:radial-gradient(120% 60% at 90% 0%,#c9fbff 0%,transparent 40%),var(--sent)}
.status[data-state=sent] p{text-shadow:0 1px 8px rgba(0,60,140,.45)} /* lift contrast */
.status[data-state=rejected]{background:var(--rejected)}
.btn{height:95px;border-radius:9999px;font:500 26px -apple-system;backdrop-filter:blur(20px)}
.btn--primary{background:#42599c;box-shadow:inset 0 1px 0 rgba(255,255,255,.25)}
.btn--secondary{background:#263b68}
@keyframes rain{to{transform:translate(-60px,240px)}} /* 15° streaks, 0.6s linear infinite */
.state-enter > *{animation:pop .35s cubic-bezier(.2,.9,.3,1) both}
.state-enter > *:nth-child(2){animation-delay:.08s}.state-enter > *:nth-child(3){animation-delay:.16s}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 9 | Lush, cinematic weather states, a coloured floor glow and native polish. |
| Originality | 8 | Status-as-weather is an evocative, fresh metaphor for a mundane flow. |
| Usability | 6 | Clear state semantics and actions, but two of three states have text below AA. |
| Craft | 8 | Constant layout across states, continuity of the plane and consistent rain direction. |

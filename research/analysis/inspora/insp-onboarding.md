---
id: insp-onboarding
source: inspora
category: Motion
status: analyzed
title: "Onboarding"
creator: "@LgyLight"
styles: [playful-rounded, hand-drawn, flat-illustration, micro-interaction]
patterns: [tap-to-start-mascot, character-transition-into-app, claw-scratch-wipe, pastel-action-cards, rive-state-machine, real-device-capture]
mode: light
palette: ["#1ea6ec", "#0a0608", "#e9dcf0", "#c8ec7a", "#96e2bf", "#9b82e8", "#e595cf", "#1f1f1f"]
type_families: ["SF Pro Rounded / SF Pro Display (likely)", "PingFang SC (system CJK)"]
type_class: [neo-grotesk, rounded-sans]
radius_px: [28]
motion: {durations_s: [1.0, 0.8, 1.03, 0.7, 1.9, 15.21], easing: [ease-out, ease-in-out], loop: false}
scores: {aesthetics: 7, originality: 9, usability: 6, craft: 7}
craft_signals: [poke-hint-arrow-on-idle, claw-marks-as-transition, silhouette-on-flat-blue, card-colour-per-mode, outline-icon-style-matches-cat, localized-poke-label]
anti_patterns: [light-grey-header-label-low-contrast, no-skip-affordance-visible]
---
# Onboarding — @LgyLight

## 1. Snapshot
- **Subject:** A 15.2 s, 2160×3840 phone-camera capture of the "Sketcha" drawing app's launch: a black cat silhouette sits on a flat sky-blue screen; a finger pokes it, the cat leaps, clings with claws, and scratches its way down to reveal the pastel home menu.
- **Why it's remarkable:** The transition from splash to home is a character performance — four claw-scratch trails act as the wipe — and the captured screen shows it running as a real Rive file on device (laptop notes mention `catclaw.riv`, ~3.3 MB).

## 2. Composition & layout
- **Splash:** full-bleed #1ea6ec; the seated cat (≈ 35% of screen height) sits low, bottom-centre-left, its back to the viewer; a small curved arrow and a "戳" (poke) label sit beside its head as the only instruction.
- **Mid-transition (5.92 s):** the cat is centred and splayed facing the viewer, eyes wide, with 3–4-line scratch trails above each paw (≈ 25% of screen height long).
- **Home (Sketcha):** lilac #e9dcf0 background, large title "Sketcha" left at about 42% screen height with history and settings icons right; four full-width cards ≈ 520×170 px (phone pt ≈ 345×110), 12–16 px gaps, ≈ 28 px radius (device px), each with a left-aligned title + one-line subtitle and a right-aligned black-outline illustration.
- The second half of the clip re-shoots the device at an angle over a sketchbook of storyboard frames — context, not UI.

## 3. Typography
- Latin "Sketcha" ≈ 34 pt bold neo-grotesk (SF Pro Display); card titles ≈ 17 pt medium ("Take a photo", 导入, 撒点成画, 随机形状); subtitles ≈ 12 pt regular in PingFang SC.
- Header label "历史作品" set in light grey CJK over two lines — the weakest text on screen.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #1ea6ec | splash sky-blue | full screen during splash |
| #0a0608 | cat silhouette, outline icons | 5% |
| #e9dcf0 / #d6c4df | home background lilac | 14% |
| #c8ec7a | card 1 lime (camera) | ~6% |
| #96e2bf | card 2 mint (import) | ~6% |
| #9b82e8 | card 3 violet (dots) | ~6% |
| #e595cf | card 4 pink (random shapes) | ~6% |
| #1f1f1f | card text | — |

WCAG checks:
- Cat #000 on blue #1ea6ec: 7.72:1 — a crisp silhouette.
- Card text #1f1f1f on lime 12.35:1, mint 10.93:1, violet **5.3:1**, pink 7.48:1 — all pass AA.
- Grey header label ≈#8a8590 on lilac #e9dcf0: **2.73:1 (fails)**.

## 5. Depth & material
- Entirely flat: no shadows on cards, a solid-fill splash, a vector silhouette. Depth comes only from the cat's pose change (back view → facing the viewer → clinging to the glass) — the character pretends the screen is a pane of glass.
- Illustrations are a 2–3 px black-outline doodle style (camera on tripod, daisy, dot-cat, fish), consistent with a sketch app.

## 6. Components & patterns
- Tap-to-begin mascot with an affordance hint (arrow + "poke" label, localized per the notes on screen).
- Character-driven page transition (claw scratch = wipe).
- Mode cards colour-coded per creation method; the whole card is the tap target.
- Top-right history and settings icon buttons.

## 7. Motion
Measured (m0_motion.json): 15.21 s, 60 fps, motion_fraction 0.48, 11 segments (median 0.73 s), not a loop (first/last diff 122 — the clip ends on black). Hand-held camera shake contributes energy, so treat segments as approximate. Key ones:
- 0.97–1.97 s (1.0 s), peak_at 0.58, symmetric — the finger approaches and pokes.
- 2.20–3.00 s (0.8 s), peak_at 0.19 → ease-out — the cat's startled reaction.
- 4.70–5.73 s (1.03 s), peak_at 0.05 → sharp ease-out — the leap and claw-hang (5.92 s frame).
- 6.03–6.73 s (0.7 s), peak_at 0.26 → ease-out — the scratch slide reveals home (home is fully visible by 7.61 s).
- 7.90–9.80 s (1.9 s), peak_at 0.06 — the camera re-frame onto the sketchbook (not UI).
- 11.0–12.0 s (1.0 s) and 12.4–13.13 s (0.73 s) — a repeat run showing the cat over the menu (12.68 s).
The UI beats are dominated by fast-start ease-outs (peak ≤ 0.26), giving the cat a snappy, startled physicality.

## 8. Brand system
n/a — not a brand system. Identity cues: a black-cat mascot, flat sky-blue splash, a pastel four-colour card system and doodle line icons.

## 9. UX
- Turns an unavoidable splash into a delightful, user-triggered moment with a clear hint.
- The menu is scannable: one colour and one icon per mode, and the text passes AA on every card.
- **Risks:** a mandatory poke delays entry for returning users (no visible skip); the ~2.5 s from tap to home is long for repeat launches; the grey header label fails contrast.

## 10. Craft signals
- Idle state carries a hint arrow and a "poke" glyph next to the cat's head.
- The claw trails are 3–4 parallel strokes per paw, varying in length — hand-drawn, not duplicated.
- The splash blue is a single flat colour so the silhouette reads at 7.7:1.
- Card illustrations share the cat's black, line-weight vocabulary.
- Card titles align on one left edge (≈ 24 px inset), illustrations on one right edge.

## 11. Reproduction recipe
```css
:root{--sky:#1ea6ec;--ink:#0a0608;--bg:#e9dcf0;--lime:#c8ec7a;--mint:#96e2bf;--violet:#9b82e8;--pink:#e595cf;--r:20px}
.splash{background:var(--sky);height:100dvh}
.mode-card{display:flex;justify-content:space-between;align-items:center;border-radius:var(--r);
  padding:20px 24px;min-height:110px;color:#1f1f1f;font:500 17px/1.2 "SF Pro Rounded",system-ui}
.mode-card small{display:block;font-size:12px;opacity:.8}
.mode-card:nth-child(1){background:var(--lime)} .mode-card:nth-child(2){background:var(--mint)}
.mode-card:nth-child(3){background:var(--violet)} .mode-card:nth-child(4){background:var(--pink)}
.reveal{clip-path:inset(0 0 100% 0);animation:scratch .7s cubic-bezier(.2,.8,.2,1) forwards}
@keyframes scratch{to{clip-path:inset(0 0 0 0)}}
```
Build the cat in Rive with a state machine: `idle → poked (trigger) → leap → cling → slide`, firing an `onComplete` event to navigate.

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 7 | Charming, cohesive doodle world; the capture setting is rough. |
| Originality | 9 | A claw-scratch wipe performed by a mascot is a genuinely new transition. |
| Usability | 6 | Clear menu, but a forced poke and a slow entry for repeat users. |
| Craft | 7 | Lively character timing and good card contrast; one weak label. |

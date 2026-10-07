---
id: insp-ai-ends-motion-hiring
source: inspora
category: Motion
status: analyzed
title: "AI ends motion hiring."
creator: "Miles (@uxmiles)"
styles: [dark-premium, micro-interaction, minimal-swiss]
patterns: [ball-as-cursor-physics, slider-with-value-tooltip, notification-stack, chat-reply-field, onscreen-keyboard-keypress, squash-and-stretch, toggle-switch, dot-grid-canvas]
mode: dark
palette: ["#0d0d0f", "#1c1c1e", "#2c2c2e", "#232325", "#0a84ff", "#ffffff", "#949496", "#3a3a3c"]
type_families: ["SF Pro Text / Inter (likely)"]
type_class: [neo-grotesk]
radius_px: [9999, 22, 16, 12]
motion: {durations_s: [0.83, 2.87, 0.57, 1.83, 1.77], easing: [ease-in-out, linear, ease-in, ease-out], loop: false}
scores: {aesthetics: 7, originality: 8, usability: 6, craft: 7}
craft_signals: [ios-system-greys-exact, ball-squash-on-contact, key-depresses-under-ball, depth-of-field-blur-on-leaving-card, ghost-next-letter-in-input, dot-grid-24px]
anti_patterns: [placeholder-contrast-fails, demo-not-product]
---
# AI ends motion hiring. — Miles (@uxmiles)

## 1. Snapshot
- **Subject:** A 10 s, 1920×1080 reel of iOS-flavoured components (slider, notification stack, reply field, keyboard, toggle). The components are "operated" by a white bouncing ball instead of a cursor. Per the post, it was generated with an AI model in three prompts.
- **Why it's remarkable:** It makes a physics object the narrator. The ball falls, squashes on keys, pushes a slider and knocks notifications. This chains five unrelated components into one causal story.

## 2. Composition & layout
- The canvas is #0d0d0f with a dot grid of about 70 px pitch (1–2 px dots, #232325). It is the only texture.
- **Framing:** each scene is a tight crop, with the camera panning and zooming between components (sheet frames 0.56 → 9.49 s). The components are never all on screen at once until the zoom-out at about 8.4 s, which reveals the whole board: slider top-left, notifications right, keyboard bottom.
- **Keyboard keys:** about 145×135 px in the key frame, with an 18 px gutter and a half-key stagger between rows (iOS layout).
- **Reply field:** about 425×130 px, pill-shaped, with an 86 px send button inset about 22 px from the right.

## 3. Typography
- The face is SF Pro or its closest match, Inter. Sizes:
  - notification title about 44 px Semibold;
  - body about 40 px Regular;
  - "now" timestamp about 34 px in grey;
  - key caps about 50 px Medium, uppercase.
- **Slider tooltip:** the "80" value bubble uses tabular numerals at about 28 px, in white on a #3a3a3c chip.
- **Input:** "re" is typed in white, and the next predicted letter "t" appears as a dropped, grey, subscript-sized glyph before it settles. This ghost-letter detail sells the keystroke.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #0d0d0f | canvas | 81% |
| #1c1c1e | input, field fill | 2% |
| #2c2c2e | keys | 15% |
| #232325 | notification card, grid dots | — |
| #0a84ff | iOS system blue: slider fill, send, app icons, toggle | ~1% |
| #ffffff | ball, knob, primary text | ~1% |
| #949496 | timestamps, secondary text | <1% |

These are almost exactly Apple's dark system greys (systemGray6 #1c1c1e, #2c2c2e).

WCAG:
- White on #2c2c2e keys is 13.94:1, and white on #1c1c1e is 17.01:1.
- "now" #949496 on #232325 is 5.18:1.
- The "Reply" placeholder (#5f5f61 on #1c1c1e) is **2.67:1 (fails)**.
- The white arrow on #0a84ff is 3.65:1 (large and icon only, so OK).

## 5. Depth & material
- Flat iOS surfaces. Keys have a 3–4 px darker bottom lip (a #1a1a1c shadow), and the pressed "T" key drops about 6 px with its lip disappearing.
- Notification cards have no border; separation comes from surface tint only.
- **Departing card:** in f2 the top "Slider – Reached 100" card is heavily Gaussian-blurred (about 6 px) as it recedes. This is a depth-of-field cue rather than an opacity fade.

## 6. Components & patterns
- **Slider:** a 6 px track with blue fill, a 60 px white knob, 9 tick marks below (blue once passed) and a value tooltip that grows with the value ("7" small, "80" large).
- **Notification stack:** app-icon tile with a radius of about 12 px, title/time on row 1 and message on row 2. Card radius is about 22 px.
- **Reply field:** a pill with a 2 px #3a3a3c border and a blue circular send button.
- **Keyboard:** a QWERTY grid with a "return" key that expands into a tall key (f6).
- **Toggle (end):** a 58 px knob on a #3a3a3c track.

## 7. Motion
The motion is measured: 10.05 s, 60 fps, motion_fraction 0.79 (busy) and no seamless loop (first/last diff 2.02).
- **Five segments:**
  - 0–0.83 s: symmetric, the ball enters and hits the slider.
  - 1.6–4.47 s: 2.87 s of continuous/linear motion, as the slider fills and the notifications cascade.
  - 4.57–5.13 s: ease-in (peak 0.74), the gravity drop onto the keyboard.
  - 5.47–7.3 s: linear typing.
  - 7.5–9.27 s: ease-out (peak 0.08), the fast camera pull-back that settles.
- **Ball (estimates from frames):**
  - Squash: about 1.5:1 horizontal on impact with the "T" key (key frame: 140×85 px against 85×85 at rest).
  - Stretch: about 1:1.3 vertical in free fall (f5).
  - It accelerates downward, which is true gravity easing, not a CSS ease.

## 8. Brand system
n/a — not a brand system. Identity cues are pure iOS dark mode: system greys plus #0a84ff.

## 9. UX
- As a component demo it communicates each state change well (value tooltip, key depress, notification arrival).
- As UI it is mostly stock iOS, so the novelty is the choreography, not the components.
- The placeholder text fails contrast.

## 10. Craft signals
- Surface greys match iOS tokens (#1c1c1e, #2c2c2e) within 1 RGB step.
- The ball squashes on contact with keys and the slider knob, with volume roughly preserved.
- The pressed key depresses (y +6 px) and loses its shadow lip.
- The receding notification is blurred, not faded (f2).
- The slider tick marks change from grey to blue as the knob passes them.
- The dot grid stays registered across camera moves (it is world-space, not screen-space).

## 11. Reproduction recipe
```css
:root{--bg:#0d0d0f;--fill:#1c1c1e;--key:#2c2c2e;--card:#232325;--blue:#0a84ff;--text-2:#949496;--hair:#3a3a3c}
body{background:var(--bg) radial-gradient(circle,#232325 1.5px,transparent 1.6px) 0 0/70px 70px;font-family:"SF Pro Text",Inter,system-ui}
.key{background:var(--key);border-radius:16px;box-shadow:0 4px 0 #1a1a1c;color:#fff;font:500 50px/1 inherit;transition:transform .08s,box-shadow .08s}
.key.is-down{transform:translateY(6px);box-shadow:0 0 0 #1a1a1c}
.notif{background:var(--card);border-radius:22px;padding:24px 30px}
.notif.leaving{filter:blur(6px);transform:translateY(-20px) scale(.96);transition:all .45s ease-out}
@keyframes drop{0%{transform:translateY(-400px) scale(.9,1.15);animation-timing-function:cubic-bezier(.55,0,1,.45)}
  85%{transform:translateY(0) scale(.9,1.15)}92%{transform:translateY(0) scale(1.5,.62)}100%{transform:translateY(-40px) scale(1)}}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 7 | Restrained iOS dark palette and a nice dot grid, but visually generic. |
| Originality | 8 | Using a physics ball as the actor that strings components together is a fresh narrative device. |
| Usability | 6 | States are legible, but it is a demo choreography rather than a usable flow, and the placeholder fails contrast. |
| Craft | 7 | Squash and stretch, key depress and blur on exit are good. Camera cuts are somewhat abrupt (7.5 s ease-out jump). |

---
id: insp-voice-model
source: inspora
category: Motion
status: analyzed
title: "voice model"
creator: "Bakers Studio"
styles: [soft-3d, minimal-swiss, playful-rounded, micro-interaction]
patterns: [ribbon-waveform-visualizer, speaking-listening-state-label, karaoke-transcript-highlight, voice-to-chat-mode-switch, pill-control-row, chat-bubbles-in-same-card]
mode: light
palette: ["#ecede7", "#ffffff", "#ff933c", "#ff6a13", "#fdc48d", "#111111", "#9a9a9a", "#000000"]
type_families: ["Inter (likely)"]
type_class: [neo-grotesk]
radius_px: [56, 9999]
motion: {durations_s: [0.13, 0.2, 0.27, 0.23, 0.3], easing: [ease-in-out, ease-out], loop: false}
scores: {aesthetics: 9, originality: 8, usability: 7, craft: 8}
craft_signals: [state-label-colour-swap-orange-black, word-by-word-grey-to-black, ribbon-bleeds-card-edges, disabled-hangup-ghosted, cursor-tinted-brand-orange, active-mode-button-inverts-black]
anti_patterns: [orange-label-low-contrast, close-text-low-contrast, hangup-looks-disabled]
---
# voice model — Bakers Studio

## 1. Snapshot
- **Subject:** An 18.6 s, 1570×1570 demo of a square voice-agent card. A glossy orange 3D ribbon waveform undulates while the agent is "Speaking" or the user is "Listening". The transcript highlights word by word, and a tap on the chat button turns the same card into a text chat.
- **Why it's remarkable:** It is one card with three modes (speaking, listening, chat). The state is carried by a two-colour label system and a single sculptural ribbon instead of bars or orbs.

## 2. Composition & layout
- **Card:** an 888×888 px square (x/y 341→1229 in the 1570 frame) with a ~56 px radius, centred on a warm off-white #ecede7 stage.
- **Header row:** at y≈402, with the state glyph and label left (~36 px) and "Close" right.
- **Ribbon zone:** y≈520–870, about 40% of the card. The ribbon bleeds past both card edges and is clipped by the radius.
- **Transcript:** two lines at y≈975–1025, ~36 px.
- **Control row:** four 182×98 px pills at y≈1092–1190 with ~28 px gaps (chat, mic, speaker, hang-up). The side padding is ~38 px, so the controls span the full inner width.
- **Chat mode (15.54 s, 17.61 s):** the ribbon area is replaced by right-aligned black user bubbles and left-aligned #f0f0ee agent bubbles, plus a three-dot typing bubble.

## 3. Typography
- Inter-like neo-grotesk, single weight (regular 400). Size on-device is ~18 px for the transcript and header (half of the 36 px measured in this 2× capture).
- **Hierarchy by colour only:**
  - **State label:** orange for "Speaking" (agent), black for "Listening" (user) and "Chat".
  - **Transcript:** words already spoken are #111, upcoming words are #9a9a9a (karaoke highlight; at 1.04 s "Are you using" is black and the rest grey).

## 4. Colour
| Hex | Role | Approx share |
|---|---|---|
| #ecede7 | stage | 71% |
| #ffffff | card | 24% |
| #ff933c / #ffab5a / #fdc48d | ribbon body (orange to apricot to cream) | 3% |
| ≈#ff6a13 | "Speaking" label, cursor | <1% |
| #111111 | text, active button, user bubbles | 1% |
| #9a9a9a | pending words, Close | <1% |
| #f0f0ee | button and agent-bubble fill | — |

WCAG checks:
- Text #111 on white: 18.88:1.
- **Orange label #ff6a13 on white: 2.87:1 (fails)**.
- **"Close" #9a9a9a on white: 2.81:1 (fails)**.
- Icon #111 on the #f0f0ee pill: 16.55:1.
- User bubble white on #000: 21:1.
- The card against the stage is only about a 1.1:1 luminance step. It is separated by tone, not contrast.

## 5. Depth & material
- **Flat card:** no shadow and no border; it sits on #ecede7 purely by brightness.
- **Ribbon:** the only 3D element. A twisted satin band with specular white streaks where it folds (visible at 3.11 s and in the key), deeper #ff6a13 in shadowed troughs and a cream highlight on the crests. It reads like a rendered glossy material while the UI stays flat.
- **Pills:** #f0f0ee with no shadow. The active mode (chat) inverts to solid black with a white icon.

## 6. Components & patterns
- **State header:** a three-bar glyph plus label. Orange is reserved for when the AI is speaking.
- **Karaoke transcript:** the text is laid out fully, with progress shown by colour. There is no reflow.
- **Mode switch:** tapping the chat pill fades the ribbon out (5.18 s shows the card empty with the transcript dimmed) and slides in bubbles.
- **Hang-up pill:** a ghosted icon (#c8c8c8, 1.42:1 against the stage), which reads as disabled.
- **Custom cursor:** an orange arrow cursor ties the demo pointer to the brand accent.

## 7. Motion
Measured profile: 18.65 s at 60 fps, `motion_fraction` 0.12 (low; the ribbon motion is smooth and mostly under threshold), 11 segments with a median of 0.20 s. Not a loop.
- **4.97 s (0.13 s) and 5.20 s (0.20 s), symmetric:** the ribbon dissolving out for the state change.
- **11.83–17.0 s:** a cluster of 0.2–0.3 s segments, mostly ease-out with peaks at 0.21–0.28 (e.g. 14.60 s for 0.23 s, 15.10 s for 0.20 s, 16.70 s for 0.30 s). These are chat bubbles appearing one by one with fast-start, soft-settle entrances.
- **Ribbon:** continuous slow undulation, estimated at a ~2–3 s wave period from frame-to-frame shape change. It is not voice-reactive at high frequency.
- **Transcript highlight:** advances at roughly speech rate (~3 words/s estimated).

## 8. Brand system
n/a — not a brand system. Identity cues:
- a single orange family (#ff6a13 to #fdc48d) as the "voice" colour;
- warm-grey neutrals;
- black for user and active states.

## 9. UX
- **Strengths:**
  - It is always clear who is talking (label text plus colour).
  - The karaoke transcript supports comprehension and accessibility (captions).
  - Switching voice and chat in the same container preserves context.
- **Risks:**
  - Orange and grey text both fail contrast.
  - The hang-up control looks disabled, so ending a call should not be the least visible action.
  - Close is text-only, with no hit area shown.

## 10. Craft signals
- The state label switches colour (orange for agent, black for user) as well as text.
- Word-level progress uses #111 against #9a9a9a with no layout shift.
- The ribbon is clipped by the 56 px card radius and bleeds edge to edge.
- Four equal 182 px pills with 28 px gaps fill the inner width exactly.
- The active mode pill inverts to black, the only filled-dark control.
- The demo cursor is recoloured to the accent orange.

## 11. Reproduction recipe
```css
:root{--stage:#ecede7;--card:#fff;--ink:#111;--pending:#9a9a9a;--pill:#f0f0ee;
  --voice:#ff6a13;--voice-2:#ff933c;--voice-3:#fdc48d;--r-card:28px}
.vcard{width:444px;aspect-ratio:1;background:var(--card);border-radius:var(--r-card);padding:20px 19px;
  display:grid;grid-template-rows:auto 1fr auto auto;overflow:hidden;font:400 18px/1.3 Inter,sans-serif}
.state[data-who=agent]{color:var(--voice)} .state[data-who=user]{color:var(--ink)}
.ribbon{margin-inline:-19px;height:180px;background:
  linear-gradient(100deg,var(--voice-3),var(--voice-2) 40%,#fff4e6 55%,var(--voice) 70%,var(--voice-3));
  -webkit-mask:url(ribbon.svg) center/100% 100% no-repeat;animation:wave 2.6s ease-in-out infinite alternate}
@keyframes wave{to{transform:scaleY(.8) translateX(-3%)}}
.w{color:var(--pending);transition:color .12s linear} .w.said{color:var(--ink)}
.controls{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}
.controls button{height:49px;border-radius:9999px;background:var(--pill)}
.controls button[aria-pressed=true]{background:#000;color:#fff}
.bubble{animation:pop .25s cubic-bezier(.2,.8,.2,1) both}
@keyframes pop{from{opacity:0;transform:translateY(6px) scale(.98)}}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 9 | The satin ribbon on a flat warm-grey UI is beautiful and singular. |
| Originality | 8 | A sculptural ribbon visualiser plus three modes in one card is a fresh take on voice UI. |
| Usability | 7 | Clear who-speaks state and captions. The accent text and hang-up affordance are weak. |
| Craft | 8 | Exact pill grid, colour-only progress and an edge-bleed ribbon. Contrast misses. |

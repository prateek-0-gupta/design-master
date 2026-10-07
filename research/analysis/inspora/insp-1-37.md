---
id: insp-1-37
source: inspora
category: Product
status: analyzed
title: "AI Agent Approval Cards"
creator: "@kvnkld"
styles: [dark-premium, micro-interaction, hairline-ui]
patterns: [agent-approval-card, auto-approve-countdown, plan-todo-preview, lettered-multiple-choice, inline-free-text-option, question-pager, keyboard-hint-on-primary, collapsed-list-n-more]
mode: dark
palette: ["#0f0f0f", "#1a1a1a", "#242526", "#424346", "#787878", "#f2f2f2", "#ffffff", "#3b82f6"]
type_families: ["Inter (likely)"]
type_class: [neo-grotesk]
radius_px: [29, 14, 10, 9999]
motion: {durations_s: [0.43, 0.17, 0.2, 0.23, 0.13], easing: [ease-out, ease-in-out], loop: false}
scores: {aesthetics: 8, originality: 8, usability: 8, craft: 8}
craft_signals: [enter-key-glyph-on-primary, countdown-ring-beside-auto-approve, dashed-circle-pending-todos, letter-keycaps-for-options, disabled-continue-until-answered, coloured-icon-tile-per-card-type, nested-darker-well]
anti_patterns: [secondary-text-below-aa, auto-approve-default-risky]
---
# AI Agent Approval Cards — @kvnkld

## 1. Snapshot
- **Subject:** A 19.7 s, 1920×1556 capture of two chat-embedded cards for a coding agent. A "Plan Overview" card has a to-do preview, an "Auto Approve in 27s" countdown, and View Plan / Approve buttons. A "Questions" card steps through three lettered multiple-choice questions with Skip / Continue.
- **Why it's remarkable:** It designs human-in-the-loop control for agents as compact, keyboard-first cards.
  - A visible countdown makes the agent's default action explicit.
  - Each question offers an "Something else…" row that turns into a text field in place.

## 2. Composition & layout
Measured in original px; frames are ×1.2 from the 1600 px samples.
- **Plan card:** about 1126×770 px, centred on #0f0f0f, radius about 29 px, fill #1a1a1a.
  - Header row (≈58 px): a 48 px icon tile (green-tinted for plan, blue-tinted for questions), title, and two 24 px ghost icons (download, expand) right-aligned.
  - Body: the task title (≈32 px Medium), a two-line description (≈26 px, grey), then a nested darker well (#111, radius ≈14 px) listing To-dos with a count "6" right-aligned. Three items are shown, then "··· 3 more".
  - Footer: a spinner with "Auto Approve in 27s" on the left, and the buttons on the right: View Plan (ghost #2a2a2a) and Approve (white pill with a ↵ glyph).
- **Questions card:** about 1126×630 px (key frame x 396→1522, y 464→1093).
  - The question is ≈30 px.
  - Four option rows, each ≈70 px tall with an 82 px pitch and a 1 px #242526 border, radius ≈10 px, carrying a 34 px letter keycap.
  - Footer: "^ 2/3 v" pager, then Skip and Continue ↵.

## 3. Typography
Inter-like neo-grotesk throughout, Regular and Medium.
- **Scale (original px):** card title 30, task title 32 Medium, body 26, options 30, buttons 28. This is a narrow scale where hierarchy comes from colour value (#f2f2f2 vs #787878) more than size.
- **Keycaps:** single capitals at about 22 px Medium in #787878 on #242526.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #0f0f0f | canvas | 80% |
| #1a1a1a | card surface | 18% |
| #111111 | inner well, hovered/selected option row | — |
| #242526 / #424346 | borders, keycaps, ghost buttons | 1.4% |
| #787878 / #626262 | secondary text, pending to-dos, placeholder | 1% |
| #f2f2f2 / #ffffff | primary text, primary button | — |
| #3b82f6 / green tint | icon tiles (questions / plan) | — |

WCAG checks:
- Primary text: 15.55:1.
- Description grey (≈#a0a0a0): 6.66:1.
- Pending to-dos and the "Auto Approve" label (#787878 on #1a1a1a): 3.94:1, which **fails AA-normal** at ≈26 px.
- Disabled Continue (#2a2a2a text on #787878): 3.25:1.
- The black-on-white Approve button is 18.88:1.

## 5. Depth & material
- Flat dark layering: canvas #0f0f0f → card #1a1a1a → well #111.
- Cards carry a 1 px #242526 border and a faint outer shadow.
- There is no glass; the only "light" is the white primary pill.
- The selected option darkens (to #111) rather than lightens, a recessed "pressed in" metaphor.

## 6. Components & patterns
- **Auto-approve countdown:** a circular progress ring (≈26 px, green arc) next to "Auto Approve in Ns". It ticks 27 → 24 s across frames 0–1.
- **To-do preview:** dashed-circle status glyphs (pending), truncation to three items plus "3 more".
- **Lettered options A–D:** keyboard-mappable. Row D "Something else…" becomes a text input (at 16.4 s, typing "This is an examp|" fills the C keycap white as selected).
- **Pager "^ n/3 v":** questions navigable with arrows.
- **Primary actions with ↵:** they advertise Enter as the shortcut. Continue stays grey until an answer exists, then turns white (frame at 16.39 s).

## 7. Motion
Measured: duration 19.67 s at 30 fps, motion_fraction 0.12, and 11 short segments (median 0.17 s), not a seamless loop.
- 0.20–0.63 s (0.43 s, peak_at 0.27, ease-out) is the card entrance.
- Most UI responses are 0.13–0.23 s: 1.27 s ease-out (expand "3 more"), and 9.20, 10.97, 12.27 and 13.60 s at about 0.2 s symmetric ease-in-out. These are the question-to-question swaps.
- At 18.57 s the card fades and blurs out on Continue with a press ripple on the button (estimated ~0.3 s).
- Transitions are short and functional, with ease-out for appearance and symmetric easing for in-place content swaps.

## 8. Brand system
n/a — this is a product UI, not a brand system. Identity cues: semantic tint per card type (green for plan, blue for questions) inside a neutral greyscale shell.

## 9. UX
- **Strengths:**
  - Clear default (auto-approve with visible timer) plus an override.
  - A preview before approve.
  - An escape hatch (Skip, Something else).
  - Progress (n/3).
  - Keyboard affordances (letters, ↵).
- **Risks:**
  - Auto-approving a production migration after 27 s is a dangerous default, and a pause control isn't shown.
  - Grey secondary text is below AA.

## 10. Craft signals
- The ↵ glyph is embedded in both primary buttons ("Approve ↵", "Continue ↵").
- Pending to-dos use dashed 22 px circles, distinct from checkbox squares.
- Letter keycaps are 34 px squares with radius ≈6 px, vertically centred on 70 px rows.
- The card-type icon tile is tinted to match its semantic (green for the plan list, blue for the question bubble).
- Continue is visibly disabled until an option is chosen or text is typed.
- The inner well is darker than the card (#111 on #1a1a1a) to group to-dos without a border.

## 11. Reproduction recipe
```css
:root{--canvas:#0f0f0f;--card:#1a1a1a;--well:#111;--line:#242526;--muted:#787878;--text:#f2f2f2;
  --plan:#22c55e;--ask:#3b82f6;--r-card:29px;--r-row:10px;}
.agent-card{background:var(--card);border:1px solid var(--line);border-radius:var(--r-card);padding:28px;font-family:Inter,sans-serif;color:var(--text);
  animation:in .43s cubic-bezier(.16,1,.3,1)}
@keyframes in{from{opacity:0;transform:translateY(8px) scale(.98)}}
.icon-tile{width:48px;height:48px;border-radius:12px;background:color-mix(in srgb,var(--plan) 18%,transparent);color:var(--plan)}
.well{background:var(--well);border-radius:14px;padding:20px 24px}
.todo::before{content:"";width:22px;height:22px;border:1.5px dashed var(--muted);border-radius:50%}
.option{display:flex;gap:16px;align-items:center;height:70px;border:1px solid var(--line);border-radius:var(--r-row);padding:0 14px}
.option[aria-checked=true]{background:var(--well)}
.key{width:34px;height:34px;border-radius:6px;background:var(--line);color:var(--muted);display:grid;place-items:center}
.option[aria-checked=true] .key{background:#fff;color:#111}
.btn-primary{background:#fff;color:#111;border-radius:9999px;padding:12px 24px}
.btn-primary:disabled{background:var(--muted);color:#2a2a2a}
.countdown{--p:.9;background:conic-gradient(var(--plan) calc(var(--p)*1turn),#2a2a2a 0);border-radius:50%;mask:radial-gradient(circle,#0000 55%,#000 57%)}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Restrained dark UI with clean hierarchy and one bright action. |
| Originality | 8 | Auto-approve countdowns and lettered agent questions are fresh agent-UX patterns. |
| Usability | 8 | Keyboard-first, with clear progress and escape hatches. Low-contrast greys and the risky default count against it. |
| Craft | 8 | Consistent radii, semantic tints, considered disabled states. |

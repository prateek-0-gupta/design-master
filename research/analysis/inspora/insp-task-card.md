---
id: insp-task-card
source: inspora
category: Product
status: analyzed
title: "Task Card"
creator: "@adriankuleszo"
styles: [monochrome, micro-interaction, minimal-swiss]
patterns: [swipe-card-stack, triage-action-bar, blur-in-card-entry, inbox-zero-empty-state, mention-badge, serif-headline-sans-chrome]
mode: light
palette: ["#f7f7f7", "#e7e7e7", "#ffffff", "#111111", "#b6b7b8", "#4a6fa5"]
type_families: ["Lora / Source Serif-style text serif (likely)", "SF Pro Text / Inter (likely)"]
type_class: [editorial-serif, neo-grotesk]
radius_px: [20, 40, 6]
motion: {durations_s: [0.5, 0.5, 0.47, 0.33, 0.37], easing: [ease-in-out, ease-out], loop: true}
scores: {aesthetics: 7, originality: 6, usability: 7, craft: 7}
craft_signals: [blur-to-sharp-card-reveal, tilt-on-swipe-exit, serif-for-content-sans-for-chrome, grey-radial-glow-empty-state, dimmed-next-label-at-zero]
anti_patterns: [empty-state-text-fails-contrast, ambiguous-swipe-direction-mapping]
---
# Task Card — @adriankuleszo

## 1. Snapshot
- **Subject:** A 5.8 s, 960×720 screen recording of an iPhone "Summaries" screen. It shows Slack mentions as a stack of swipeable cards with Snooze / Complete / Next actions, ending in an inbox-zero state.
- **Why it's remarkable:** It is almost colourless. The only chroma is the Slack glyph and a pale-blue "You were mentioned" chip. Card transitions use focus blur rather than opacity, so each new card "comes into focus".

## 2. Composition & layout
- **Device and card:** The phone occupies x≈330→630 (about 300 px of the 960 px frame) on a #f7f7f7 stage. The card sits inset about 15 px from the device edge, spans y≈168→570 (about 400 px tall, roughly 0.67 aspect), and carries a ~20 px radius.
- **Header:** Centred title "Summaries" with a two-line serif timestamp ("Updated today, 09:14"), hamburger left, history and people icons right.
- **Card anatomy:** Slack glyph top-left and a "Today" pill top-right. Below that come a channel tag (`# sales`), the blue mention chip, a two-line serif title of about 24 px (frame px), 4 lines of serif body, and a footer row "Read more ↗" pinned to the bottom. The empty space between body and footer keeps every card the same height.
- **Action bar:** Three evenly spaced icon-over-label actions at y≈613–633. "Next" is black while the others are grey, so it reads as the primary action.

## 3. Typography
- **Content serif:** card titles, body and the empty-state message use a transitional text serif with a Lora-like bracketed "Q" and soft terminals. Titles are about 24 px in the frame (≈31 pt on device) at regular weight with leading of about 1.2.
- **Chrome sans:** the navigation title, chips, the "Read more" link and action labels use SF Pro / Inter. The title is semibold at about 14 px; labels are about 10 px.
- This split makes content feel like correspondence and controls feel like system UI.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #f7f7f7 | stage background | 86% |
| #e7e7e7 | device screen / card well | 11% |
| #ffffff | card surface | in-card |
| #111111 | titles, primary action | small |
| #b6b7b8 | inactive icons, dimmed labels | <1% |
| #4a6fa5 on #eaf1fb | mention chip | <1% |

WCAG checks:
- Card title #111 on #fff is 18.88:1.
- Mention chip #4a6fa5 on #eaf1fb is exactly 4.5:1 (borderline pass).
- The channel tag at about #7a7a7a on #eee is 3.7:1, which fails AA for small text.
- Action labels at #8a8a8a on #e7e7e7 are 2.79:1 (fail).
- The empty-state "Boom! You're up to date." at about #a8a8a8 on #e3e3e3 is **1.85:1**, which is decorative-level contrast for the only message on screen.

## 5. Depth & material
- **Card:** white with a very soft, wide shadow (about 0 12px 30px rgba(0,0,0,.06)), plus a second card peeking 4–6 px below to signal the stack.
- **Empty state:** a large blurred radial glow (lighter centre about #ececec fading to #dcdcdc) gives the zero state a soft, pillow-like depth instead of an illustration.

## 6. Components & patterns
- Swipe-card stack (Tinder-style triage) for notifications.
- Source glyph, a "Today" date pill with a #f0f0f0 fill and ~6 px radius, and a channel tag.
- Bottom triage bar with Snooze (timer icon), Complete (check-circle) and Next (arrow).
- A grey ~60 px circle is the recording's touch indicator, not part of the UI.
- **Inbox-zero state:** a serif message centred in the well, with "Next" dimmed to grey once nothing remains.

## 7. Motion
Measured: 5.8 s at 60 fps, motion fraction 0.39, `seamless_loop_likely: true`.

| Segment | Start–end | Duration | Shape (peak_at) | What happens |
|---|---|---|---|---|
| 1 | 0.23–0.73 s | 0.5 s | symmetric (0.37) | card swap |
| 2 | 1.33–1.83 s | 0.5 s | symmetric (0.37) | card swap |
| 3 | 2.43–2.90 s | 0.47 s | symmetric (0.39) | card swap |
| 4 | 3.53–3.87 s | 0.33 s | symmetric (0.55) | final card exits to empty state (faster) |
| 5 | 4.97–5.07 s | 0.1 s | — | flick |
| 6 | 5.20–5.57 s | 0.37 s | ease-out (0.14) | first card re-enters for the loop |

There is a ~1.1 s cadence between swaps.

Choreography seen in the frames:
- The outgoing card translates right and rotates about +8° (frame 1.61 s).
- At the same time the incoming card scales from about 0.96 to 1 and de-blurs from roughly 8 px to 0. At t=2.90 s and 5.48 s the text is still soft while the layout is already in place.

## 8. Brand system
n/a — not a brand system. Identity cues: a monochrome "paper" palette, serif correspondence voice, and the playful "Boom!" copy as the only exclamation.

## 9. UX
- **Strengths:** One item at a time reduces inbox anxiety. The three explicit buttons duplicate the swipe gesture, so the flow is accessible without gestures. The timestamp in the header sets freshness.
- **Risks:**
  - Swipe direction and its mapping (snooze vs complete) is not shown.
  - Grey labels and the empty-state message fail contrast.
  - There is no count of remaining cards ("3 of 5"), so progress is invisible until zero.

## 10. Craft signals
- Incoming cards de-blur rather than fade; the text is visibly gaussian-soft for about 0.2 s after landing.
- The exiting card rotates (about 8°) as it slides, implying a physical flick.
- Serif is used for message content and sans for system chrome, with no mixing within a role.
- The "Next" label turns from #000 to grey in the empty state; the disabled state is expressed by value only.
- The stack depth cue is a second card edge visible 4–6 px below the active card.

## 11. Reproduction recipe
```css
:root{--stage:#f7f7f7;--well:#e7e7e7;--card:#fff;--ink:#111;--mute:#8a8a8a;
  --chip-fg:#4a6fa5;--chip-bg:#eaf1fb;--r-card:20px;
  --serif:"Lora","Source Serif 4",Georgia,serif;--sans:"Inter",-apple-system,system-ui,sans-serif}
.card{background:var(--card);border-radius:var(--r-card);padding:20px;
  box-shadow:0 12px 30px rgba(0,0,0,.06);display:flex;flex-direction:column;min-height:400px}
.card h2{font:400 24px/1.2 var(--serif);color:var(--ink)}
.chip{font:500 10px/1 var(--sans);color:var(--chip-fg);background:var(--chip-bg);padding:4px 6px;border-radius:4px}
@keyframes card-in{from{filter:blur(8px);transform:scale(.96);opacity:.6}to{filter:none;transform:none;opacity:1}}
@keyframes card-out{to{transform:translateX(110%) rotate(8deg)}}
.card.enter{animation:card-in .5s cubic-bezier(.45,0,.25,1) both}
.card.exit{animation:card-out .5s cubic-bezier(.45,0,.55,1) forwards}
.empty{background:radial-gradient(60% 45% at 50% 45%,#ececec,#dcdcdc);font:400 22px/1.3 var(--serif);color:#9a9a9a}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 7 | Calm, paper-like monochrome with a nice serif/sans split; a little too grey overall. |
| Originality | 6 | Swipe-to-triage is known; the blur-focus entry is the fresh part. |
| Usability | 7 | Buttons back up the gestures and the flow is single-focus; contrast and progress feedback are weak. |
| Craft | 7 | Consistent radii and choreography with tilt and blur; low-contrast labels hurt it. |

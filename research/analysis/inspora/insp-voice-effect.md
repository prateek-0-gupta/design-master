---
id: insp-voice-effect
source: inspora
category: Motion
status: analyzed
title: "Voice effect"
creator: "@Jakubantalik"
styles: [dark-premium, aurora-glow, micro-interaction]
patterns: [edge-glow-voice-indicator, recording-pill-with-timer, expanding-voice-sheet, live-transcript-streaming, chat-composer-glow, component-variants-showcase]
mode: dark
palette: ["#050505", "#1a1a1a", "#323131", "#858181", "#d8d8d8", "#c04fd0", "#3fd6c8", "#f2b33d"]
type_families: ["Inter (likely)"]
type_class: [neo-grotesk]
radius_px: [9999, 64, 24]
motion: {durations_s: [0.2, 0.23, 0.37, 1.93, 0.73, 0.67], easing: [ease-out, ease-in-out], loop: false}
scores: {aesthetics: 9, originality: 7, usability: 8, craft: 8}
craft_signals: [glow-anchored-to-bottom-edge, spectral-arc-not-blob, 1px-top-rim-on-pill, glow-shifts-toward-active-control, transcript-fade-in-per-word, three-sizes-one-language]
anti_patterns: [timer-not-tabular-unclear, glow-only-state-signal]
---
# Voice effect — @Jakubantalik

## 1. Snapshot
- **Subject:** A 17.7 s, 1700×1280 reel of a zero-dependency "voice glow". A spectral, Siri-like light pools at the bottom edge of three component types:
  - a compact recording pill (mic · 00:02 · stop);
  - a tall voice sheet with a live transcript;
  - an "Ask me anything…" chat composer.
- **Why it's remarkable:** It does a Siri-style glow without shaders. The colour rises from the container's bottom edge like light leaking under a door, and the same effect scales cleanly from a 230 px-tall pill to a full sheet.

## 2. Composition & layout
- **Overview frames (0.98 s, 14.77 s):** an asymmetric showcase. The sheet sits top-centre, the "Libraries.dev / Voice" title is centred (~60 px "Voice" over ~20 px "Libraries.dev"), the pill is bottom-left and the composer bleeds off the right edge.
- **Detail frames:** each component isolated and centred on #050505 (4.92 s, 6.89 s, 8.86 s, 12.80 s).
- **Recording pill (key frame):** 790×230 px (x 450→1240, y 505→735 in the 1700 frame).
  - Mic glyph at x≈560.
  - Timer "00:02" centred at x≈820, ~70 px tall.
  - A 160 px stop disc inset ~35 px from the right end.
- **Voice sheet:** ~600×470 px on the sheet scale, with a bottom row of "Agent (auto)" dropdown pill, mic disc and ✕ disc. Transcript is centred at the top.

## 3. Typography
- A single neo-grotesk (Inter-like).
- **Transcript:** ~16 px regular, centred, white.
- **Timer:** ~34 px (device) light grey. The colon and digits look proportional; it is unclear whether tabular figures are used.
- **Small text:** pill labels ("Agent (auto) ⌄") are ~13 px. The "Ask me anything.." placeholder is in mid grey.
- **Streaming:** the newest words arrive at reduced opacity ("remind" at 16.74 s is grey before turning white), so a typographic fade signals streaming.

## 4. Colour
| Hex | Role | Approx share |
|---|---|---|
| #050505 | stage | 92% |
| #1a1a1a | container fill | 4% |
| #323131 | control discs, chip fills | 2% |
| #858181 / #d8d8d8 | icons, timer, text | 1% |
| ≈#c04fd0 · #3fd6c8 · #f2b33d | glow spectrum (magenta, cyan, amber) | ~1% |

WCAG checks:
- Timer ≈#9a9a9a on #1a1a1a: 6.19:1.
- Icons #d8d8d8 on #1a1a1a: 12.21:1.
- Placeholder ≈#6a6a6a on #1a1a1a: 3.22:1 (large only).
- Title white on #050505: 20.38:1.

## 5. Depth & material
- **Containers:** dark glass. A #1a1a1a fill with a 1 px lighter top rim (~rgba(255,255,255,.08)) and a faint inner gradient getting darker toward the bottom.
- **Glow:** a radial or conic spectral gradient clipped to the container and anchored below its bottom edge. A bright 1–2 px spectral line traces the lower curve, with the haze fading upward over ~40% of the height.
- **Control discs:** #323131 with a slight top highlight. The stop disc has a darker inner ring.

## 6. Components & patterns
Three variants share one glow.
- **Recording pill:** mic, elapsed time and stop.
- **Voice sheet:** transcript, agent selector, mic and close.
- **Composer:** placeholder, "+", "Agent ⌄", mic and close.
- **Directional glow:** On the tall sheet in idle (4.92 s, 6.89 s) the glow concentrates in the bottom-right corner near the mic and close controls. It then spreads full-width while speaking (0.98 s, 2.95 s), so its position carries the state (idle versus listening).

## 7. Motion
Measured profile: 17.73 s at 60 fps, `motion_fraction` 0.35, 16 segments with a median of 0.28 s. Not a loop.
- **Quick state ticks:** mostly ease-out (0.27 s for 0.10 s, 0.47 s for 0.20 s, 1.40 s for 0.23 s, peaks at 0.08–0.21), consistent with the glow reacting to voice amplitude.
- **2.97–4.90 s (1.93 s, peak 0.08, ease-out):** the cut or zoom into the sheet detail, with a big initial change and a long settle.
- **7.57–8.30 s (0.73 s, symmetric):** the sheet collapsing into the pill (8.86 s).
- **11.2 s and 13.67 s (0.67 s each, ease-out):** transitions to the composer and back to the overview.
- **Ambient:** The glow breathing itself is low-energy and mostly under threshold. Estimated drift of hue across ~2–3 s.

## 8. Brand system
n/a — not a brand system. Identity cues:
- "Libraries.dev" component-library branding;
- an achromatic dark UI with a single spectral signature reserved for voice.

## 9. UX
- **Strengths:**
  - The glow is a strong ambient "I'm listening" signal.
  - The pill provides elapsed time plus an explicit stop.
  - The transcript streams in place.
  - One visual language across sizes aids recognition.
- **Risks:**
  - The state is carried largely by colour and light. Users with low vision need the timer or mic icon to confirm recording (present in the pill, absent in the sheet).
  - The description mentions a light theme but it is not shown here.

## 10. Craft signals
- The glow is anchored below the container edge, so it reads as light from beneath, not a fill.
- A thin bright spectral rim line follows the bottom curvature exactly.
- In idle, the glow pools toward the active controls (bottom-right).
- A 1 px top rim gives the dark containers an edge on #050505.
- Streaming words fade from grey to white.
- One effect is parameterised across 230 px-tall to ~470 px-tall containers.

## 11. Reproduction recipe
```css
:root{--stage:#050505;--surface:#1a1a1a;--control:#323131;--icon:#d8d8d8;--muted:#858181}
.voice{position:relative;overflow:hidden;border-radius:9999px;background:var(--surface);
  box-shadow:inset 0 1px 0 rgba(255,255,255,.08)}
.voice::after{content:"";position:absolute;inset:auto -10% -60% -10%;height:120%;pointer-events:none;
  background:conic-gradient(from 200deg at 50% 100%,#f2b33d,#3fd6c8,#7aa7ff,#c04fd0,#f25c8a,#f2b33d);
  -webkit-mask:radial-gradient(60% 50% at 50% 100%,#000 30%,transparent 70%);
  mask:radial-gradient(60% 50% at 50% 100%,#000 30%,transparent 70%);
  filter:blur(14px) saturate(1.3);transform:scaleX(var(--level,.6));transition:transform .2s cubic-bezier(.2,.8,.2,1)}
.voice[data-state=idle]::after{transform-origin:85% 100%;--level:.35}
.timer{font:400 17px Inter,sans-serif;font-variant-numeric:tabular-nums;color:#9a9a9a}
.word.pending{opacity:.45;transition:opacity .25s ease-out}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 9 | Light leaking from the bottom edge on dark glass is elegant and scales well. |
| Originality | 7 | It is a refined take on the Siri/Apple Intelligence glow, done without shaders. |
| Usability | 8 | Clear recording affordances, a timer and a stop button. Some states rely on glow alone. |
| Craft | 8 | Rim line, directional idle glow and streaming word fades. Showcase framing crops the composer. |

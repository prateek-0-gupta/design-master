---
id: insp-1-48
source: inspora
category: Product
status: analyzed
title: "Agent Handoff"
creator: "@jeetnirnejak"
styles: [micro-interaction, corporate-clean, data-dense]
patterns: [multi-agent-pipeline-stepper, colour-per-agent, gradient-progress-track, streaming-event-log, timestamped-mono-log, pause-resume-restart-controls, live-status-footer, nested-card-in-tray]
mode: light
palette: ["#ffffff", "#f2f2f2", "#2f6ff0", "#8a2cf0", "#f08a00", "#22c55e", "#111111", "#888888"]
type_families: ["Inter (likely)", "JetBrains Mono / Geist Mono (likely)"]
type_class: [neo-grotesk, mono]
radius_px: [40, 28, 16, 9999]
motion: {durations_s: [0.1], easing: [ease-in-out, ease-out], loop: true}
scores: {aesthetics: 8, originality: 8, usability: 8, craft: 9}
craft_signals: [track-gradient-accumulates-agent-hues, done-badge-tick-in-agent-hue, handoff-rows-bold-with-arrow, log-dots-tinted-by-agent, header-timer-dot-matches-active-agent, active-icon-glow-ring, run-id-mono]
anti_patterns: [white-on-orange-icon-low-contrast, pending-labels-low-contrast]
---
# Agent Handoff — @jeetnirnejak

## 1. Snapshot
- **Subject:** A 13.9 s, 1924×1518 capture of a widget that visualises one task ("Summarize churn drivers from Q2 tickets", run_7c42) passing through four agents: Triage (router), Researcher (analyst), Writer (author) and Reviewer (approver). A timestamped handoff log streams in below.
- **Why it's remarkable:** Each agent owns a hue (blue, violet, orange, green), and that hue threads through every layer at once:
  - the icon tile;
  - the done-tick badge;
  - its segment of the progress track;
  - its log dots;
  - its name in the footer;
  - the header timer dot.

  You can read "who has the task" from any part of the card.

## 2. Composition & layout
- **Tray:** #f2f2f2, about 962×1006 px (x 482→1444, y 258→1264), radius about 40 px.
- **Inner card:** white, radius about 28 px, inset about 21 px. It is divided into three bands by 1 px dashed #e6e6e6 rules:
  1. a task row: "TASK" mono caps label, task text ≈24 px, and run id right-aligned;
  2. the agent stepper: four 72 px icon tiles on a 224 px pitch, name ≈24 px, role in mono caps ≈16 px; below them a 2 px track with a 22 px knob;
  3. a log: "HANDOFF LOG" caps plus an "11 / 19" counter, and six visible rows on a 52 px pitch.
- **Header:** "Agent Handoff" (≈30 px Semibold), a "4 agents" mono chip, and the elapsed time "6.5s" plus a status dot.
- **Footer:** status text on the left; Reset and Pause/Resume (grey pills) and Restart (black pill) on the right.

## 3. Typography
- **Sans** (Inter-like): title Semibold, body Regular. Handoff log rows set "Researcher → Writer" in Medium, followed by a Regular grey note ("6 sources attached").
- **Mono:** timestamps ("3.0s", with slashed zero), roles (ROUTER/ANALYST/AUTHOR/APPROVER, +0.1 em tracking), chips, run id, counter and footer numbers ("Paused at 6.5s").
- **Sizes (key frame):** 30 / 24 / 22 / 16 px.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #ffffff | stage, card | 88% |
| #f2f2f2 | tray, grey pills, pending tile | 8% |
| #2f6ff0 | Triage | — |
| #8a2cf0 | Researcher | — |
| #f08a00 | Writer | — |
| #22c55e | Reviewer | — |
| #111111 | Restart button, primary text | — |
| #888888 / #a0a0a0 | timestamps / pending agent labels | — |

WCAG checks:
- Log text (#4a4a4a): 8.86:1.
- Mono timestamps (#888): 3.54:1, large-only.
- Pending "Reviewer" label (#a0a0a0): 2.61:1.
- Footer grey (#6a6a6a on #f2f2f2): 4.83:1.
- Blue agent name on the tray: 4.03:1.
- **White pencil on the orange tile: 2.52:1.** The icon is legible by shape but fails non-text contrast intent.

## 5. Depth & material
- Tray shadow ≈0 30px 60px rgba(0,0,0,.08).
- The active agent tile is a solid fill with a coloured glow (≈0 8px 20px of the hue at 35%). Researcher at 3.86 s and Reviewer at 11.58 s also show a 4 px halo ring.
- Completed tiles revert to a pale 12% tint with a 22 px solid tick badge at top-right.
- Pending tiles are #f2f2f2 with grey glyphs.

## 6. Components & patterns
- **Stepper:** four states per agent: pending (grey), active (solid hue + glow), done (tint + tick), and handed-off (the arrow log row).
- **Gradient track:** the filled part is a multi-stop gradient of the completed agents' hues (blue → violet → orange), ending at a knob in the active hue.
- **Streaming log:** new rows push older ones up, and the counter increments (2/19 → 18/19). Handoff rows have a solid dot and bold names; work rows have a pale dot.
- **Controls:** Pause becomes "▷ Resume" and the footer reads "Paused at 6.5s" while the header timer freezes (frames at 6.95 and 8.49 s both show 6.5s).
- **Footer status:** "[Agent] · [current activity]" in the agent's hue, or "Handoff · Triage → Researcher" during transfers.

## 7. Motion
Measured: duration 13.9 s at 60 fps, motion_fraction 0.10, seamless_loop_likely true. Nine segments, all 0.10 s:
- 1.50 s: ease-in;
- 5.27 s: ease-out;
- 1.97, 3.70, 4.20, 4.73, 9.90, 10.80 and 13.30 s: symmetric.

These are the discrete events (tile activation, log row insert, knob jump). Everything is snappy at about 100 ms, and the continuous knob travel between agents is slow enough to fall below the threshold. Inferred from frames: the knob moves linearly with elapsed time, and colour swaps are instant.

## 8. Brand system
n/a — this is a product UI, not a brand system. The tokens are shared with insp-1-30 and insp-1-44 (#f2f2f2 tray, 40/28 px radii, black primary pill, mono data), which suggests a coherent personal component kit.

## 9. UX
- **Strengths:**
  - It makes an opaque multi-agent run inspectable: who, what, when.
  - It has pause/resume and a deterministic restart.
  - The log counter shows total expected events.
- **Weaknesses:**
  - Colour carries agent identity, but names and icons back it up.
  - The log truncates to six rows with no scroll affordance.
  - "Reset" vs "Restart" is an ambiguous distinction.

## 10. Craft signals
- The track gradient stops line up with the agent tile centres (x≈627, 851, 1075).
- The header dot changes hue with the active agent (blue → violet → orange → green).
- Done badges use the agent's own hue, not a generic green.
- Handoff log rows are emphasised: solid dot, Medium names, "→" glyph.
- Log dots are pale tints for work events and solid for handoffs.
- The mono slashed-zero timestamps align in a fixed 60 px column.

## 11. Reproduction recipe
```css
:root{--tray:#f2f2f2;--ink:#111;--muted:#888;--triage:#2f6ff0;--research:#8a2cf0;--write:#f08a00;--review:#22c55e;
  --mono:"JetBrains Mono",ui-monospace;}
.tile{width:72px;height:72px;border-radius:16px;display:grid;place-items:center;background:var(--tray);color:#aaa;position:relative}
.tile[data-state=active]{background:var(--c);color:#fff;box-shadow:0 0 0 4px color-mix(in srgb,var(--c) 25%,transparent),0 8px 20px color-mix(in srgb,var(--c) 35%,transparent)}
.tile[data-state=done]{background:color-mix(in srgb,var(--c) 14%,#fff);color:var(--c)}
.tile[data-state=done]::after{content:"✓";position:absolute;top:-8px;right:-8px;width:22px;height:22px;border-radius:50%;background:var(--c);color:#fff;font-size:12px;display:grid;place-items:center;box-shadow:0 0 0 2px #fff}
.track{height:2px;background:linear-gradient(90deg,var(--triage),var(--research) 33%,var(--write) 66%) 0/var(--p) 100% no-repeat,#e6e6e6}
.log li{display:grid;grid-template-columns:60px 14px 1fr;font:400 22px/52px Inter;animation:row .1s ease-out}
.log time{font-family:var(--mono);color:var(--muted);font-feature-settings:"zero"}
@keyframes row{from{opacity:0;transform:translateY(6px)}}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Calm neutral shell with four clear hues. |
| Originality | 8 | Agent-orchestration visualisation with colour threading across all layers is new. |
| Usability | 8 | Legible state at every level, with pause and resume. Some low-contrast greys and the orange tile. |
| Craft | 9 | Rigorous token reuse and colour logic. Considered paused state. |

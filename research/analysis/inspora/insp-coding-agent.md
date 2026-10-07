---
id: insp-coding-agent
source: inspora
category: Product
status: analyzed
title: "Coding agent"
creator: "@jeetnirnejak"
styles: [minimal-swiss, corporate-clean, micro-interaction]
patterns: [agent-run-card, phase-colour-theming, task-checklist-with-progress, streaming-thought-chips, live-token-cost-meter, tool-source-tabs, completion-summary-state]
mode: light
palette: ["#ffffff", "#f2f2f2", "#e8e6e2", "#fdf8d5", "#c2620f", "#2f5bd8", "#16a34a", "#c0157a"]
type_families: ["Inter (likely)", "SF Mono / JetBrains Mono (likely)"]
type_class: [neo-grotesk, mono]
radius_px: [44, 28, 9999]
motion: {durations_s: [0.23, 0.27, 0.27, 0.3, 0.27], easing: [ease-out, ease-in-out], loop: false}
scores: {aesthetics: 8, originality: 8, usability: 8, craft: 9}
craft_signals: [whole-card-recolours-per-phase, header-progress-bar-tracks-step-count, mono-for-cost-and-timer, thought-chips-fade-older-to-lighter, strikethrough-done-steps, inset-card-in-grey-shell]
anti_patterns: [phase-colour-text-below-aa, faded-thought-chips-illegible]
---
# Coding agent — @jeetnirnejak

## 1. Snapshot
- **Subject:** A 16.6 s, 1878×1458 recording of an agent run card working through the task "Ship dark mode toggle" in 5 steps. The phases are Reading file, Searching web, Thinking, Writing, Reviewing and Complete. Each phase recolours the header icon, status label, progress bar and checkmarks.
- **Why it's remarkable:** Phase is encoded as a whole-card accent colour (purple, blue, orange, green, magenta). You can tell what the agent is doing at a glance before reading a word. The body morphs per phase: a file skeleton, search results, thought chips, a streamed diff, a revised diff with strikethroughs, and a summary.

## 2. Composition & layout
- **Card:** about 1120×1215 px (x≈380–1500, y≈120–1335) in the key frame. A grey shell (#f2f2f2) with a 44 px radius wraps white inset cards with about 28 px radii and an 8–12 px gap. This is a "tray of cards" layout.
- **Sections in order:**
  - header: icon, title, status and dot, about 120 px;
  - a 4 px progress bar;
  - the checklist card (about 470 px, rows on a 68 px pitch);
  - the phase-content card (variable height);
  - the tools row (GitHub, Files, Figma, Linear, npm, plus a model picker "Opus 4.7");
  - the meter row (tokens, cost, timer, Pause, ✕).
- **Insets:** the left text edge sits at about 32 px inside each inner card, and icons are aligned at x≈462.

## 3. Typography
- **UI:** neo-grotesk close to Inter.
  - Title "Coding Agent" about 30 px Semibold.
  - Task title about 27 px Semibold with a grey "2 / 5".
  - Checklist about 26 px Regular.
  - Tools row about 24 px.
- **Mono** (SF Mono or JetBrains-like) at about 24 px for "5.7k tokens $0.017 0:08", file names ("tokens.css", "theme-toggle.tsx") and the search query. Mono marks machine-generated values.
- **Done steps** are struck through in grey; the active step is near-black; pending steps are dark grey.

## 4. Colour
| Hex | Role | Approx share |
|---|---|---|
| #ffffff | inner cards, page | 85% |
| #f2f2f2 | shell, tool row | 10% |
| #e8e6e2 / ≈#e5e5e5 | progress-bar track, dividers | 1% |
| ≈#8b5cf6 | "Reading file" phase | transient |
| ≈#2f5bd8 | "Searching web" phase | transient |
| ≈#c2620f | "Thinking" phase | transient |
| #fdf8d5 / ≈#7c2d12 | thought-chip fill and text | 1.4% |
| ≈#16a34a | "Writing" / "Complete" | transient |
| ≈#c0157a | "Reviewing" | transient |

WCAG checks (contrast.py):
- Body #1a1a1a on white: **17.4:1**.
- Status labels on the grey shell #f2f2f2:
  - orange #c2620f: **3.72:1 (large only)**;
  - green #16a34a: **2.94:1 (fail)**;
  - blue #2f5bd8: **5.2:1**;
  - magenta #c0157a: **5.17:1**.
- Thought chip text #7c2d12 on #fdf3c4: **8.39:1**. The faded older chip (≈#c49a7a on #fdf8e5) is **2.39:1**.
- Struck-through done steps ≈#a3a3a3: **2.52:1**. That is intentional de-emphasis, but it is unreadable.

## 5. Depth & material
- The grey shell has a soft large shadow (about 0 20px 40px rgba(0,0,0,.08)) and a 1 px lighter top highlight. The inner cards are flat white with no borders, separated by the shell gap.
- The tools-and-meter footer is one white card split by a 1 px divider. Pause and ✕ are grey pill and circle buttons.

## 6. Components & patterns
- **Phase status:** label plus a pulsing dot, colour per phase.
- **Header progress bar:** fills at 0/5 → 1/5 → … in the phase colour.
- **Checklist:** spinner arc for the active step, a filled check circle in the phase colour for done steps (so done ticks recolour with each phase), and empty rings for pending.
- **Phase cards:**
  - file-read skeleton lines in lavender;
  - search query pill plus three results (title plus mono source);
  - thought chips stacked like a stream, with older ones fading;
  - a streaming code note with a caret;
  - a revised diff with red strikethrough and inserted tokens;
  - a "Dark mode shipped" summary (5 steps · 10.5k tokens · 0:15) with a black "Run again" pill.
- **Tool tabs:** the active source is highlighted in the phase tint (Files purple, GitHub blue).
- **Live meter:** tokens, cost and timer tick upward.

## 7. Motion
- Measured: 16.6 s at 60 fps. `motion_fraction` 0.08, 5 segments, median **0.27 s**.
  - 0.23 s ease-out at start (peak 0.21);
  - 0.27 s symmetric at 3.0 s and 6.53 s (body card height changes between phases);
  - 0.30 s ease-out at 9.07 s (thinking → writing);
  - 0.27 s ease-out at 15.6 s (complete summary).
  - Not looped (`first_last_diff` 2.55).
- **From frames (estimates):** phase changes land at roughly 3 s, 6.5 s, 9 s, about 12.5 s and 15.6 s, so one phase every 2.5–3.5 s. Thought chips appear one by one at about 0.4 s intervals, with older ones fading to about 40% opacity. The meter ticks continuously (1.7k at 2.77 s, 10.5k at 15.69 s).

## 8. Brand system
n/a — not a brand system. The equaliser-bar glyph (4 vertical bars) acts as the agent's avatar and inherits the phase colour.

## 9. UX
- Excellent transparency: plan, current step, evidence (sources, diffs), cost and time are all visible. Pause and cancel are always present.
- **Risks:**
  - Colour is the primary phase signal, but the text label backs it up.
  - Several phase colours fail AA on #f2f2f2.
  - Faded thought chips are illegible when they are still informative.
  - The card height changes each phase, which can shift surrounding layout.

## 10. Craft signals
- Already-completed check icons recolour to the current phase, so the whole card stays monochrome-plus-one accent at every moment.
- The progress bar width tracks the step count exactly (2/5 ≈ 42% at 8.3 s).
- Mono is used only for tokens, cost, time, file names and queries.
- Thought chips use opacity to show recency.
- The nested radii (44 px shell, 28 px inner cards, pills) are consistent across all 9 frames.
- The diff view uses strikethrough plus colour, not colour alone.

## 11. Reproduction recipe
```css
.agent{--phase:#c2620f;--phase-ink:#9a4a0b;--phase-bg:#fdf3c4;
  background:#f2f2f2;border-radius:44px;padding:12px;box-shadow:0 20px 40px -12px #00000014;font-family:Inter,sans-serif}
.agent[data-phase=read]{--phase:#8b5cf6;--phase-ink:#6d28d9}
.agent[data-phase=search]{--phase:#2f5bd8;--phase-ink:#2f5bd8}
.agent[data-phase=write]{--phase:#16a34a;--phase-ink:#15803d}
.agent[data-phase=review]{--phase:#c0157a;--phase-ink:#c0157a}
.agent *{transition:color .27s,background-color .27s,border-color .27s}
.status{color:var(--phase-ink)} .status::after{content:"";width:10px;height:10px;border-radius:50%;background:var(--phase);animation:pulse 1.2s ease-in-out infinite}
.progress{height:4px;background:#e5e5e5;border-radius:2px}
.progress>i{display:block;height:100%;width:calc(var(--done)/5*100%);background:var(--phase);transition:width .3s cubic-bezier(.16,1,.3,1)}
.inner{background:#fff;border-radius:28px;padding:28px 32px}
.inner+.inner{margin-top:8px}
.step.done{color:#8f8f8f;text-decoration:line-through}
.step.done .tick{background:var(--phase);color:#fff;border-radius:50%}
.meter{font-family:"JetBrains Mono",ui-monospace,monospace;font-variant-numeric:tabular-nums;color:#6b7280}
.thought{background:var(--phase-bg);color:#7c2d12;border-radius:9999px;padding:8px 20px}
.thought:not(:nth-last-child(-n+2)){opacity:.55}
@keyframes pulse{50%{opacity:.4}}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Clean, calm shell; the per-phase colour adds life without clutter. |
| Originality | 8 | Phase-themed whole-card recolouring plus a phase-specific body is a strong new idiom for agent UIs. |
| Usability | 8 | Transparent plan, cost and controls; some phase colours and faded text miss AA. |
| Craft | 9 | Consistent radii, mono discipline and exact progress mapping across many states. |

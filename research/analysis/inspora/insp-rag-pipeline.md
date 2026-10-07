---
id: insp-rag-pipeline
source: inspora
category: Product
status: analyzed
title: "RAG Pipeline"
creator: "@jeetnirnejak"
styles: [technical-wireframe, data-dense, micro-interaction, corporate-clean]
patterns: [vertical-step-timeline, live-pipeline-visualizer, status-footer-with-dot, score-bars, stacked-token-bar, inline-citation-badges, streaming-text-cursor, elapsed-timer-chip]
mode: light
palette: ["#ffffff", "#f2f2f2", "#111111", "#9294a8", "#b4b5b9", "#2b6ff0", "#8b32f0", "#e8114f"]
type_families: ["Inter (likely)", "JetBrains Mono / Geist Mono (likely)"]
type_class: [neo-grotesk, mono]
radius_px: [44, 32, 12, 9999]
motion: {durations_s: [0.4, 0.3, 0.27], easing: [ease-out, ease-in-out], loop: true}
scores: {aesthetics: 8, originality: 8, usability: 8, craft: 9}
craft_signals: [source-colour-threads-through-stages, citation-badge-matches-retrieval-row, per-step-latency-in-mono, embedding-as-grey-bar-strip, stage-colour-only-when-active, card-in-card-tray, status-dot-colour-per-stage]
anti_patterns: [stage-status-colours-low-contrast-on-grey]
---
# RAG Pipeline — @jeetnirnejak

## 1. Snapshot
- **Subject:** A 38.0 s, 1924×1518 (60 fps) loop of a single card that animates a five-stage retrieval-augmented generation flow (Query → Embed → Retrieve → Assemble → Generate) for the question "How do I rotate an API key without downtime?". It ends with a streamed, cited answer and a "Grounded in 3 sources" footer.
- **Why it's remarkable:** **Colour is used as provenance.** Each retrieved chunk gets a hue: blue (security/api-keys.md, 0.92), violet (0.87) and red (0.79). That hue reappears in the assembled-prompt token bar, in the inline citation badges ①②③ of the answer and in the footer's triple dot. You can trace any sentence back to its source by colour.

## 2. Composition & layout
- **Tray:** an outer card about 960×1410 px in key px, #f2f2f2, radius about 44 px, with a header row ("RAG Pipeline" plus a mono "945 ms" timer chip).
- **Inner sheet:** white, radius about 32 px, inset about 20 px.
- **Footer:** sits on the tray (status left, buttons right).
- **Timeline:**
  - 52 px icon tiles (#f2f2f2, radius about 12 px) on a 1 px vertical connector at x≈568.
  - Step content starts at x≈622, with latency right-aligned at x≈1382.
  - The step block is a title row, then a mono description row, then a visualisation (vector strip / ranked list / stacked bar).
  - Steps are spaced about 175 px apart, and the answer sits below a dashed divider.

## 3. Typography
- **Sans** (Inter-like):
  - title about 30 px Semibold;
  - step names about 25 px Semibold #111;
  - answer text about 24 px Regular with leading of about 1.7.
- **Mono** (JetBrains/Geist Mono feel) at about 21 px #5c5c5c for every quantitative or system string:
  - "11 tok → 1,536-dim vector";
  - "top 3 of 1,284 chunks · cosine";
  - file paths, scores (tinted in their source colour) and latencies.
- The split is strict: sans for human language, mono for machine facts.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #ffffff | inner sheet, canvas | 85% |
| #f2f2f2 | tray, icon tiles | 10% |
| #111111 | titles, primary button | — |
| #b4b5b9 / #9294a8 | connector, vector cells, empty bar | 2% |
| ~#2b6ff0 (est.) | source 1 / Retrieve active / "Searching index" | — |
| ~#8b32f0 (est.) | source 2 | — |
| ~#e8114f (est.) | source 3 / Generate active / "Streaming answer" | — |
| ~#f05a1a, ~#16a34a (est.) | Query and Assemble active states | — |

WCAG checks:
- #111 on white: 18.9:1.
- Mono grey #5c5c5c on white: 6.69:1.
- Source scores on white: blue 4.53:1, violet 5.51:1, red 4.54:1. All just pass.
- Footer statuses on #f2f2f2: orange 3.2:1 and **green 2.94:1**. These fail for small text.

## 5. Depth & material
- A card-in-card construction: the tray (#f2f2f2) has a very soft outer shadow (about 0 30 60 rgba(0,0,0,.08)), and the white sheet sits flat inside it.
- Icon tiles are flat grey squircles. A tile **fills with the stage colour** (white icon) only while that stage is running; the tile returns to grey once the stage completes.
- Bars are flat with fully rounded ends.

## 6. Components & patterns
- **Vertical stepper** with per-step latency.
- **Embedding visualiser:** about 40 grey cells of varying lightness, a nice abstraction of a vector.
- **Ranked retrieval list:** number badge, path, score bar and coloured score.
- **Stacked token bar:** query (orange sliver) plus three chunks in proportion plus remaining budget (grey).
- **Streamed answer:** a block cursor ▌ while typing, with citation badges inserted inline.
- **Footer:** a coloured dot plus present-progressive status ("Reading query", "Searching index", "Assembling prompt", "Streaming answer"), changing to "Grounded in 3 sources".
- **Buttons:** "Run pipeline" (a black pill with ▷) becomes "Replay" with a ghost icon button.

## 7. Motion
Measured: 38.03 s at 60 fps, `motion_fraction` only 0.04, `seamless_loop_likely` true. There are 4 segments: 0.67–1.07 s (0.40 s, symmetric), 11.47–11.77 s (0.30 s, peak 0.17, ease-out), 19.37–19.77 s (0.40 s) and 32.43–32.70 s (0.27 s, ease-out). These are the large layout changes: the sheet growing when the answer block appears and collapsing on reset.
- Everything else is small and progressive (below threshold). From frames:
  - the timer counts 0 → 48 → 63 → 844 → 945 ms;
  - the vector cells fill left to right;
  - score bars grow;
  - the token bar segments wipe in;
  - the answer types at roughly 15–20 characters per second (14.79 s → 19.02 s).
- One run lasts about 17 s (2.1 s → 19 s), then reset and replay.

## 8. Brand system
n/a — not a brand system. Identity cues:
- the three-colour source dot (●●● blue/violet/red) as a "grounded" mark;
- mono for every number.

## 9. UX
- **Strengths:**
  - It explains a black-box process step by step, with real numbers (dimensions, chunk counts, latencies).
  - Provenance colours make citations verifiable at a glance.
  - Present-tense status copy gives continuous feedback.
  - The Replay affordance is clear.
- **Risks:**
  - Colour is the only link between badge and source, though numbers ①②③ back it up, which is good.
  - The green and orange status text is low contrast.
  - The red for a source could be misread as an error.

## 10. Craft signals
- Source hue is consistent across four places: retrieval row, token bar, inline badge and footer dot.
- The stage icon tile is tinted only while that stage is active.
- Latencies are right-aligned in mono, so the decimal places line up (42 / 11 / 2 / 890 ms).
- The embedding is drawn as a strip of grey-value cells rather than a fake chart.
- The dashed divider separates pipeline internals from the user-facing answer.
- Nested radii: tray about 44 px, sheet about 32 px, tiles about 12 px.

## 11. Reproduction recipe
```css
:root{--tray:#f2f2f2;--sheet:#fff;--ink:#111;--mono-ink:#5c5c5c;--rail:#d9d9dc;
  --src-1:#2b6ff0;--src-2:#8b32f0;--src-3:#e8114f;--q:#e8590c;--ok:#15803d;
  --sans:"Inter",sans-serif;--mono:"JetBrains Mono","Geist Mono",ui-monospace,monospace}
.tray{background:var(--tray);border-radius:44px;padding:20px;box-shadow:0 30px 60px rgba(0,0,0,.08)}
.sheet{background:var(--sheet);border-radius:32px;padding:40px}
.step{display:grid;grid-template-columns:52px 1fr auto;column-gap:28px;position:relative}
.step::before{content:"";position:absolute;left:26px;top:52px;bottom:-24px;width:1px;background:var(--rail)}
.step .icon{width:52px;height:52px;border-radius:12px;background:var(--tray);display:grid;place-items:center;transition:background .3s ease-out,color .3s}
.step[data-state=active] .icon{background:var(--c);color:#fff}
.meta,.lat{font:400 15px/1.4 var(--mono);color:var(--mono-ink)}
.bar>i{display:block;height:6px;border-radius:9999px;background:var(--c);width:calc(var(--score)*100%);transition:width .6s cubic-bezier(.2,.8,.2,1)}
.cite{display:inline-grid;place-items:center;width:22px;height:22px;border-radius:50%;background:var(--c);color:#fff;font-size:12px}
.typing::after{content:"▌";animation:blink 1s steps(1) infinite}@keyframes blink{50%{opacity:0}}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Calm neutral card with disciplined accent use; data visualisations are tasteful. |
| Originality | 8 | Colour-as-provenance across a RAG pipeline is a genuinely useful idea. |
| Usability | 8 | Explains state continuously and makes citations traceable; a few status colours are low contrast. |
| Craft | 9 | Mono/sans split, aligned latencies, consistent hue threading and nested radii. |

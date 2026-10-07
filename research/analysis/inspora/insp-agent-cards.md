---
id: insp-agent-cards
source: inspora
category: Product
status: analyzed
title: "Agent cards"
creator: "Studio Sphere"
styles: [aurora-glow, soft-3d, maximalist-color, dark-premium]
patterns: [agent-phase-cards, colour-per-phase, glowing-progress-slider, metric-triplet-row, tool-call-list-with-durations, segmented-step-progress, overlapping-phase-icon-badge, particle-progress]
mode: mixed
palette: ["#862a24", "#e7465b", "#43551d", "#d8e84a", "#5d6294", "#89a1e6", "#241212", "#ffffff"]
type_families: ["SF Pro Display / Rounded (likely)"]
type_class: [neo-grotesk]
radius_px: [112, 9999]
motion: null
scores: {aesthetics: 8, originality: 7, usability: 5, craft: 7}
craft_signals: [one-hue-per-phase-tonal-text, inner-radial-glow-per-card, glass-slider-thumb-with-rim, icon-badge-breaks-card-corner, segment-progress-partially-filled, grabber-bar-on-each-card]
anti_patterns: [tonal-secondary-text-fails-contrast, european-decimal-ambiguity-15.530, colour-only-phase-coding, inconsistent-content-across-cards]
---
# Agent cards — Studio Sphere

## 1. Snapshot
- **Subject:** Two 2560×3200 slides.
  - **Slide 1:** three isolated agent-phase cards on white: Parsing (red), Planning (olive green) and Reasoning (periwinkle), each tagged "Opus 4.6".
  - **Slide 2:** an iPhone "Agent run" screen for "Weekly content plan", stacking those cards under a four-segment progress bar ("Reasoning · step 3 of 4 · 4m 12s").
- **Why it's remarkable:** Each phase of an agent run gets its own colour world with an internal light source: a radial bloom (Parsing), a glowing slider (Planning) and floating bokeh particles (Reasoning). The cards feel "alive" without any motion shown.

## 2. Composition & layout
- **Slide 1:** three cards of ≈1466×780 px source (916×487 shown ×1.6), stacked with ~110 px gaps. Corner radius ≈112 px source (~70 shown), about 14% of the card height, giving a squircle-like look. Each card has a ~64 px inner padding and a short 300 px grabber bar centred on its bottom edge.
- **Internal layouts differ per card:**
  - **Parsing:** title at top-left, an empty glowing middle, and a three-column metric row (Tokens 15.530 · Latency 123ms · Process 86%).
  - **Planning:** title at left, a tool list (calendar / social_media / messages) in the middle with right-aligned durations (1m / 2m / 5m), and a full-width glowing slider at the bottom.
  - **Reasoning:** title plus tool list, with a big "97%" at bottom-left trailed by a field of particles.
- **Slide 2:**
  - a phone in 3/4 perspective;
  - nav (a back circle, "Agent run", a "•••" circle);
  - a large title "Weekly content plan" (~60 px shown);
  - the status line with a red dot;
  - four segments (two full, the third about 75%, the fourth empty);
  - the cards, each with a ~90 px phase icon badge overlapping the top-left corner.

## 3. Typography
- An SF Pro Display-like neo-grotesk in semibold (titles) and regular.
- **Titles:** "Parsing", "Planning" and "Reasoning" are ~56 px shown (≈90 px source) with tight tracking.
- **Metrics and tool names:** ~36 px shown. Tool names use snake_case (code identifiers shown verbatim).
- **"97%":** ~80 px bold, with a gradient fill (white to lavender).
- **Tonal hierarchy:** the secondary text is a lighter or more saturated tint of the card hue (red "Opus 4.6" on red, olive on green, lavender on blue) rather than grey.
- "15.530" uses a European thousands separator in an otherwise English UI, which is ambiguous.

## 4. Colour
| Hex | Role | Approx share (slide 1) |
|---|---|---|
| #ffffff | slide ground | 62% |
| #862a24 → #e7465b | Parsing card: deep red edge to pink bloom | 9% |
| #43551d / #485933 | Planning card base | 9% |
| #d8e84a (lime) | Planning title, slider glow | — |
| #5d6294 → #89a1e6 / #8080cd | Reasoning card: indigo to periwinkle | 9% |
| #241212 / #09080a | phone screen background (slide 2) | 22% |

WCAG checks:
- White on red #862a24: 8.86:1.
- **Tonal red values #e7465b on #862a24: 2.29:1 (fails)**.
- Lime title #d8e84a on olive: 6.09:1.
- **"Opus 4.6" olive ≈#6f8a3a on #43551d: 2.1:1 (fails)**.
- White on periwinkle #5d6294: 5.77:1.
- **Lavender subtext on blue: 2.83:1 (fails)**.

The tonal-text idea is elegant, but almost every secondary label fails contrast.

## 5. Depth & material
- **Cards:** soft-glass slabs. Each has a lit inner gradient (radial bloom from the centre for Parsing, a light band near the slider for Planning, a bottom-centre glow for Reasoning), a 1–2 px lighter rim on the top edge and a slight outer colour bleed on the dark screen.
- **Slider:** a glass track with a lime-to-white "light tube" fill and a frosted circular thumb (~95 px shown) with a bright rim and inner refraction.
- **Particles:** blurred, depth-of-field dots of varying size (8–30 px) behind the 97% value.
- **Phone:** photoreal, with a dark burgundy screen gradient picking up the red of the first card.

## 6. Components & patterns
- **Phase card:** phase name, model tag, then a phase-specific body (metrics, tool timeline or progress).
- **Step progress:** four rounded segments with a partial fill on the current one.
- **Live status line:** dot, phase, step count and elapsed time.
- **Corner badges:** circular phase icons (a scroll for Parsing, a list for Planning, a 3×3 grid for Reasoning) in each card's tint.
- **Grabber bars:** imply the cards are expandable sheets.

## 7. Motion
Still images, so no motion was observed. The design implies motion:
- a breathing radial glow (Parsing);
- a slider thumb progressing along the light tube (Planning);
- drifting bokeh particles feeding the percentage (Reasoning).

The tagline "feel alive" suggests continuous ambient loops (an estimated 3–6 s ease-in-out breathing).

## 8. Brand system
n/a — not a brand system. Identity cues:
- a three-colour phase code (red for parse, green for plan, blue for reason);
- a model tag on every card;
- iOS-native typography.

## 9. UX
- **Strengths:**
  - Phases are instantly distinguishable.
  - The tool-call lists with durations give transparency into the agent's work.
  - The step progress and elapsed time set expectations.
- **Risks:**
  - The phase is colour-coded, but the titles also name it, so this is acceptable.
  - Secondary text widely fails contrast.
  - Inconsistent card anatomy: Parsing shows tools in slide 2 but not slide 1.
  - The duration columns don't explain their meaning (time ago versus time taken).
  - "15.530" reads as fifteen point five.
  - An interactive-looking slider on a read-only status card suggests a control that does nothing.

## 10. Craft signals
- Secondary text is a tonal tint of each card's hue, not neutral grey.
- Each card has its own inner light source matched to its body content.
- The glass slider thumb has a bright 2 px rim and refraction.
- Phase icon badges overlap the card corner by about half their diameter.
- The current segment of the step progress is partially filled (~75%).
- Each card carries a centred grabber bar of a consistent width (≈300 px source).

## 11. Reproduction recipe
```css
:root{--parse-0:#862a24;--parse-1:#e7465b;--plan-0:#43551d;--plan-hi:#d8e84a;--reason-0:#5d6294;--reason-1:#89a1e6;--r-card:56px}
.phase{border-radius:var(--r-card);padding:32px;color:#fff;position:relative;overflow:hidden;
  box-shadow:inset 0 1px 0 rgba(255,255,255,.25)}
.phase.parse{background:radial-gradient(40% 60% at 50% 40%,#f08a8a,var(--parse-1) 45%,var(--parse-0) 100%)}
.phase.plan{background:radial-gradient(70% 40% at 50% 85%,#9dc07a55,transparent),var(--plan-0)}
.phase.reason{background:radial-gradient(70% 60% at 50% 90%,#8fb2ff,var(--reason-0) 70%)}
.phase .sub{color:color-mix(in srgb,currentColor 70%,transparent)} /* raise to ≥4.5:1 */
.slider{height:64px;border-radius:9999px;background:rgba(255,255,255,.12);box-shadow:inset 0 0 0 1px rgba(255,255,255,.35)}
.slider .fill{border-radius:inherit;background:linear-gradient(90deg,var(--plan-hi),#fff 30%,#fff 85%,transparent);filter:blur(2px)}
.slider .thumb{width:48px;aspect-ratio:1;border-radius:50%;backdrop-filter:blur(6px);
  background:rgba(255,255,255,.25);box-shadow:inset 0 0 0 2px rgba(255,255,255,.7)}
.badge{position:absolute;top:-22px;left:-22px;width:46px;aspect-ratio:1;border-radius:50%}
@keyframes breathe{50%{filter:brightness(1.12) saturate(1.1)}} .phase{animation:breathe 4s ease-in-out infinite}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Lush, colourful glow cards on a dark phone. Strong mood. |
| Originality | 7 | A distinct visual metaphor per phase is a fresh take on agent status. |
| Usability | 5 | Weak contrast, an ambiguous number format, a fake-looking control and inconsistent anatomy. |
| Craft | 7 | Nice rim and glass details and badge overlap. Content consistency and type tokens are loose. |

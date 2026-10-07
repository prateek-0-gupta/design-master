---
id: insp-infinite-faq
source: inspora
category: Web
status: analyzed
title: "infinite faq"
creator: "@heyimgustavo"
styles: [dark-premium, minimal-swiss, hairline-ui]
patterns: [faq-accordion-with-ai-input-row, last-row-is-input, chevron-to-arrow-affordance-swap, inline-generated-answer, thinking-status-label, stop-button-while-streaming, two-column-section-header]
mode: dark
palette: ["#0e0e0e", "#ededed", "#8a8a8a", "#676767", "#2c2c2c", "#1a1a1a"]
type_families: ["Inter / Inter Display (likely)"]
type_class: [neo-grotesk]
radius_px: [9999]
motion: {durations_s: [0.1, 0.1, 0.23, 0.2], easing: [ease-out, ease-in-out], loop: false}
scores: {aesthetics: 7, originality: 8, usability: 8, craft: 8}
craft_signals: [input-styled-identical-to-faq-row, send-button-appears-only-with-text, send-morphs-to-stop-square, status-copy-reading-the-docs, hairline-dividers-1px-2c2c2c, answer-links-underlined-inline]
anti_patterns: [placeholder-low-contrast, dividers-near-invisible]
---
# infinite faq — @heyimgustavo

## 1. Snapshot
- **Subject:** An 8.35 s, 2908×1326 (2× retina, ≈1454 css px wide) recording of a dark FAQ section for "Foglamp". There are five preset accordion questions. The sixth row looks like another question but is a text input ("Ask anything else"). The user types "can i do evals?", the row shows "Reading the docs", and a generated answer renders inline below it like an expanded accordion item.
- **Why it's remarkable:** The AI chat is disguised as the FAQ's own last row. There is no chat widget, bubble or avatar; the FAQ simply never runs out of questions.

## 2. Composition & layout
- **Two-column section:**
  - **Left (x≈155→545 display, ≈225–790 real):** "Questions" heading plus a two-line grey intro that names the assistant ("ask Foggy below").
  - **Right (x≈786→1827 display, ≈52% of the width):** the accordion list.
- **Rows:** about 89 display px tall (≈130 real, ≈65 css px), separated by 1 px #2c2c2c hairlines. Chevrons are right-aligned at x≈1805.
- **Input row:** the same height, text start and divider as the questions. The trailing chevron is replaced by a ~44 px (display) circular send button.
- **Answer:** sits below the input with no container: just paragraphs at the same left edge, about 14 css px, max width equal to the row.

## 3. Typography
- **Family:** one neo-grotesk (Inter; "Questions" set in a tighter display cut at about 34 css px, medium, −0.03 em).
- **Sizes:** questions at about 16 css px regular in #ededed; the intro and status at about 15 css px in #8a8a8a.
- **Answer:** about 13–14 css px. The first line is a confirmation sentence and the following paragraphs give detail. Links are underlined in the same white.
- The user's input is lowercase as typed; there is no auto-capitalisation, which keeps it honest.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #0e0e0e | page | 97% |
| #ededed | questions, answer, heading | ~1% |
| #8a8a8a | intro, status ("Reading the docs") | <1% |
| #676767 | input placeholder "Ask anything else" | <1% |
| #2c2c2c | hairlines, send button fill | <1% |
| #1a1a1a | hover/row tint | <1% |

WCAG checks:
- Questions #ededed on #0e0e0e are 16.49:1, and the intro grey is 5.59:1.
- The placeholder #676767 is **3.41:1** (fails for 16 px, though placeholders are often exempted, it is the key affordance here).
- The send-button arrow (white on #2c2c2c) is 13.97:1.
- Hairlines #2c2c2c on the page are 1.38:1, which is subtle but adequate as decoration.

## 5. Depth & material
- **Entirely flat:** no shadows, no surfaces. Structure comes only from 1 px dividers and whitespace.
- **Send control:** the only filled element, a #2c2c2c circle, which marks it as the sole action.

## 6. Components & patterns
- An accordion (chevron rows) with a free-text input as the terminal row.
- **Affordance swap:** the empty input shows "+"-like or "→" ghost glyphs; with text it shows a filled circular send; while generating it shows a stop square (frame 5.10 s).
- A status line ("Reading the docs") during retrieval.
- An inline streamed answer with links (docs, GitHub). After it finishes, the stop square returns to an arrow.

## 7. Motion
Measured: 8.35 s at 120 fps, motion fraction only 0.06, not a loop.

| Segment | Duration | Shape (peak_at) | What happens |
|---|---|---|---|
| 0.47–0.57 s | 0.1 s | — | hover on the latency row |
| 1.20–1.30 s | 0.1 s | ease-out | — |
| 5.70–5.93 s | 0.23 s | ease-out (0.07) | answer block appears: content pushes down |
| 6.97–7.17 s | 0.2 s | symmetric | layout shift / page scroll by ~17 px as the answer grows (frames 6.96 and 7.88 s show the header moving up) |

Typing happens between 2.32 and 4.17 s. The "thinking" state lasts about 0.6 s (5.10 → 5.70 s).

Transitions are short (0.1–0.23 s), appropriate for utility UI. Hover row emphasis is a text-colour shift from grey to white (0.46 vs 2.32 s on "What does the SDK add…").

## 8. Brand system
n/a — not a brand system. Identity cues: a named assistant ("Foggy", from Foglamp) introduced in the intro copy, and a monochrome dev-tool aesthetic.

## 9. UX
- **Strengths:**
  - Zero-friction escalation from canned answers to AI without context switching.
  - Same visual grammar for both, so users do not perceive "a chatbot".
  - Visible states (typing, reading, stop, done).
  - The answer cites documentation links.
- **Risks:**
  - The input row is too disguised; the low-contrast placeholder could make it miss being noticed.
  - Generated answers can be wrong, and there is no "AI-generated" label or feedback control.
  - It is unclear whether multiple questions stack or replace each other.

## 10. Craft signals
- The input row reuses the question row's height, padding, left edge and divider exactly.
- The trailing slot changes by state: chevron (FAQ), arrow (ready), filled circle → (has text), square (streaming).
- Status copy "Reading the docs" is specific to retrieval, not a generic spinner.
- The answer's first sentence directly answers yes/no, then the details follow.
- One hairline colour (#2c2c2c) is shared by dividers and the button fill.
- The heading's display cut uses tighter tracking than the body cut of the same family.

## 11. Reproduction recipe
```css
:root{--bg:#0e0e0e;--fg:#ededed;--mute:#8a8a8a;--ph:#7a7a7a;--line:#2c2c2c}
.faq{display:grid;grid-template-columns:5fr 7fr;gap:120px;background:var(--bg);color:var(--fg);font:400 16px/1.5 "Inter",sans-serif}
.faq h2{font:500 34px/1.1 "Inter Display","Inter";letter-spacing:-.03em}
.faq .row{display:flex;align-items:center;justify-content:space-between;min-height:64px;border-bottom:1px solid var(--line);
  color:var(--mute);transition:color .1s ease-out}
.faq .row:hover,.faq details[open] .row{color:var(--fg)}
.ask input{all:unset;flex:1;color:var(--fg)}
.ask input::placeholder{color:var(--ph)}   /* raised from #676767 for AA */
.ask button{width:32px;height:32px;border-radius:50%;background:var(--line);color:#fff;opacity:0;transition:opacity .1s}
.ask:has(input:not(:placeholder-shown)) button{opacity:1}
.ask[data-state=streaming] button::before{content:"";width:8px;height:8px;background:#fff;display:block;margin:auto}
.answer{font-size:14px;color:var(--fg);padding:16px 0;animation:in .23s ease-out}
.answer a{color:inherit;text-decoration:underline;text-underline-offset:2px}
@keyframes in{from{opacity:0;transform:translateY(-4px)}}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 7 | Clean and restrained, but deliberately plain. |
| Originality | 8 | Merging FAQ and AI chat into one continuous list is a genuinely useful idea. |
| Usability | 8 | Clear states and a natural flow; the low-contrast placeholder and missing AI disclosure hold it back. |
| Craft | 8 | Exact row reuse, considered state glyphs and tight timings. |

---
id: insp-agent-plan
source: inspora
category: Product
status: analyzed
title: "Agent Plan"
creator: "@jeetnirnejak"
styles: [minimal-swiss, corporate-clean, micro-interaction, hairline-ui]
patterns: [human-in-the-loop-plan-review, per-step-approve-skip, accordion-step-detail, status-pill-per-row, tool-tag-chip, run-progress-footer, nested-card-in-tray, completion-summary-state]
mode: light
palette: ["#ffffff", "#f2f2f2", "#111111", "#15803d", "#e8f7ee", "#e8770e", "#fff4dc", "#a39e98"]
type_families: ["Inter (likely)", "JetBrains Mono / SF Mono (likely)"]
type_class: [neo-grotesk, mono]
radius_px: [56, 32, 9999]
motion: {durations_s: [0.27, 0.33, 0.37, 0.27, 0.5, 0.23, 0.4], easing: [ease-in-out, ease-out], loop: true}
scores: {aesthetics: 8, originality: 6, usability: 8, craft: 7}
craft_signals: [tray-plus-inset-white-card, dashed-row-dividers, mono-for-counts-and-tool-tags, strikethrough-for-skipped, icon-swaps-to-spinner-then-check, header-status-mirrors-footer, cta-disabled-until-decision]
anti_patterns: [completion-copy-says-0-steps-ran, step-counter-denominator-shrinks, orange-status-text-low-contrast]
---
# Agent Plan — @jeetnirnejak

## 1. Snapshot
- **Subject:** An 18.3 s, 1832×1498 loop of a component where a user reviews a five-step agent plan:
  1. Search competitor pricing pages
  2. Extract pricing tiers
  3. Compare to our plans
  4. Draft summary doc
  5. Email draft to product team

  The user approves or skips each step, then runs the plan and watches the steps execute to "Plan executed".
- **Why it's remarkable:** It is a compact, honest human-in-the-loop pattern. Each step expands to show its intent and tool (Browser, Notion, Gmail, Web) with inline Approve/Skip. The same card then becomes the run monitor, so review and execution share one layout.

## 2. Composition & layout
- **Outer tray (key, 1832 px frame):** 960×782 px, #f2f2f2, ~56 px radius, with a soft drop shadow beneath.
- **Header:** at y≈413 inside the tray, with "Agent plan" (~30 px semibold) plus a mono chip "5 steps" on the left and the status at the right ("1 of 5 decided" or "• Running plan").
- **Inner white card:** inset ~20 px with a ~32 px radius, containing five rows at 100 px pitch separated by dashed hairlines. Each row has a 24 px icon, a ~28 px title and a right-aligned status pill.
- **Expanded row:** adds two lines of grey description, a mono tool chip and Approve (filled green) / Skip (grey) pills.
- **Footer (in the tray):** "N approved" at the left and "Approve all" (text) plus "▷ Run plan" (black pill) at the right. While running: "Running step 2 of 3" and an amber "In progress" pill.

## 3. Typography
- **UI:** Inter-like at ~14 px device (28 px in this 2× capture) for row titles and 12 px for pills and descriptions.
- **Mono:** used for the "5 steps" chip and the tool tags ("Browser", "Notion", "Gmail", "Web"), marking system and meta data.
- **Weights:** semibold for the card title, regular for the rest. Numbers in "Running step **2** of **3**" are set darker for emphasis.
- **Skipped:** the skipped step title is struck through in grey (#a39e98).

## 4. Colour
| Hex | Role | Approx share |
|---|---|---|
| #ffffff | canvas, inner card | 87% |
| #f2f2f2 | tray | 10% |
| #111111 | titles, Run plan button | 1% |
| #15803d on #e8f7ee | Approved/Done pills, check icon | <1% |
| ≈#e8770e / #c2410c on #fff4dc | Running state (dot, spinner, pill) | <1% |
| #a39e98 | skipped and disabled text | <1% |

WCAG checks:
- Titles: 18.88:1.
- Green pill text #15803d on #e8f7ee: 4.53:1 (just passes).
- Running pill #c2410c on #fff4dc: 4.74:1.
- **Header "Running plan" orange #e8770e on #f2f2f2: 2.65:1 (fails)**.
- **Skipped #9a9a9a on #ececec: 2.38:1**, intentionally de-emphasised but still below AA.
- Footer grey #6b6b6b on #f2f2f2: 4.76:1.

## 5. Depth & material
- **Two-level surface:** a grey tray holding a white card, so the footer and header live on the tray and the content on the card. This is the modern "card-in-tray" pattern.
- **Shadow:** only the outer tray carries one (≈0 20px 40px rgba(0,0,0,.08)).
- **Inner card:** flat, no shadow.
- **Pills:** flat tinted backgrounds, no borders.

## 6. Components & patterns
- **Step row states:** Planned (grey pill), Approved (green), Skipped (grey plus strikethrough), Running (amber pill plus spinner icon), Done (green plus check icon).
- **Accordion:** the focused step expands with description, tool tag and decision buttons. After a decision, focus moves to the next undecided step (1.01 s → 3.04 s → 5.07 s).
- **Bulk action:** "Approve all" as a text button. "Run plan" is disabled (grey) until at least one step is decided (17.25 s shows "0 approved" with the disabled CTA).
- **Completion:** at 15.22 s the white card collapses to a success block with a green check tile, "Plan executed", a summary line and a "↻ New plan" pill. The header shows "Plan complete" in green.
- **Bugs visible in the copy:**
  - The completion copy reads "0 steps ran. 1 skipped." although four steps ran.
  - The footer counter changes denominator mid-run ("1 of 4" → "2 of 3" → "2 of 2" → "1 of 1"), so it counts remaining steps inconsistently.

## 7. Motion
Measured profile: 18.27 s at 60 fps, `motion_fraction` 0.14, `seamless_loop_likely` **true** (first-to-last difference 1.53).
- **Review phase:** five segments between 0.77 and 5.93 s:
  - 0.77 s for 0.27 s (ease-out);
  - 1.87 s for 0.33 s, 2.93 s for 0.37 s and 4.10 s for 0.27 s (symmetric) — the accordion collapse and expand for each decision;
  - 5.43–5.93 s (0.50 s, symmetric) — the larger transition into running mode.
- **Running phase (6–14 s):** under the motion threshold; only small icon swaps (spinner → check) and pill colour changes.
- **14.77 s (0.23 s, ease-out):** the card collapses to the completion state.
- **16.40 s (0.40 s, symmetric):** the reset to a fresh plan.
- **Overall:** quick and functional, with 0.25–0.5 s height animations and nothing decorative.

## 8. Brand system
n/a — not a brand system. Identity cues:
- a neutral, shadcn-like aesthetic (Inter, a mono accent, a tray-and-card layout);
- green and amber semantic colours only.

## 9. UX
- **Strengths:**
  - Per-step consent with clear tool disclosure (what the agent will touch).
  - Batch approval.
  - A disabled run until a decision is made.
  - Live progress in place.
  - Skipped steps remain visible but struck through.
- **Risks:**
  - The completion summary is wrong ("0 steps ran") and the step counter is inconsistent, which undermines trust in exactly the place it matters.
  - The orange header status fails contrast.
  - There is no per-step cancel or stop while running.

## 10. Craft signals
- The tray-plus-card structure separates chrome (header and footer on #f2f2f2) from content (white).
- Rows are separated by dashed hairlines rather than solid lines.
- Mono is reserved for counts and tool tags.
- Each row icon cycles from its tool icon to an amber spinner to a green check.
- The header status ("Running plan") mirrors the footer pill ("In progress") in the same amber.
- The primary CTA is disabled until at least one decision is made.

## 11. Reproduction recipe
```css
:root{--tray:#f2f2f2;--card:#fff;--ink:#111;--muted:#6b6b6b;--off:#a39e98;
  --ok:#15803d;--ok-bg:#e8f7ee;--run:#c2410c;--run-bg:#fff4dc;--run-dot:#e8770e;
  --sans:Inter,system-ui,sans-serif;--mono:"JetBrains Mono",ui-monospace,monospace}
.plan{background:var(--tray);border-radius:28px;padding:10px;box-shadow:0 20px 40px rgba(0,0,0,.08);font:400 14px var(--sans)}
.plan .card{background:var(--card);border-radius:16px;padding:4px 16px}
.step{display:flex;align-items:center;gap:12px;min-height:50px;border-bottom:1px dashed #e5e5e5}
.step[data-state=skipped] .title{color:var(--off);text-decoration:line-through}
.pill{border-radius:9999px;padding:2px 8px;font-size:12px}
.pill.ok{background:var(--ok-bg);color:var(--ok)} .pill.run{background:var(--run-bg);color:var(--run)}
.chip-mono{font:400 11px var(--mono);background:#ececec;border-radius:6px;padding:1px 6px}
.step .detail{display:grid;grid-template-rows:0fr;transition:grid-template-rows .33s cubic-bezier(.4,0,.2,1)}
.step[aria-expanded=true] .detail{grid-template-rows:1fr}
.run-btn{background:var(--ink);color:#fff;border-radius:9999px}.run-btn:disabled{background:#e5e5e5;color:var(--off)}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Calm, tidy neutral UI with a tasteful semantic palette. |
| Originality | 6 | A solid execution of an emerging HITL pattern. Not novel visually. |
| Usability | 8 | Excellent consent and progress model. Marked down for wrong summary copy and contrast. |
| Craft | 7 | Good tokens and state iconography, but counter and completion copy bugs are visible. |

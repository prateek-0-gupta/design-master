# EVALS — aaa-design, with the skill vs without

## Method
- **Briefs (5):** SaaS landing page, ops dashboard, mobile onboarding flow, brand identity page and designer portfolio. They are in `evals/evals.json` and deliberately differ in subject from the bundled `examples/`.
- **Builders:** the same model (Sonnet) for both arms, under identical constraints: a single self-contained HTML file, no external images, and no questions. The **with-skill** arm was told to read `SKILL.md`. The **without-skill** arm got the brief only, but was also allowed to render and screenshot its work with Playwright.
- **Objective audit:** every output was re-audited identically with `scripts/audit.mjs` at 390, 768 and 1440px. The audit scrolls through the page first so that scroll-reveal content renders. It checks 6 hard gates: AA contrast, no overflow at 390, visible focus, reduced motion, text ≥ 12px, and alt text and accessible names.
- **Blind grading:**
  - One fresh Sonnet grader per brief scored candidates **A/B** in a randomised order.
  - Graders got screenshots plus the audit report and source. HTML comments and skill-identifying words were scrubbed from the source.
  - Scoring used `rubric.md`: 8 axes scored 1–10 for a /80 total, plus 6 hard gates. Any gate failure caps the total at 50.
  - Graders reported **raw** (uncapped) and **capped** totals.
- Workspace with every output, screenshot, audit, blind key and grading file: `skills/aaa-design-workspace/`.

## Iteration 1 (skill v1)

| Brief | With skill raw / capped | Gates | Without skill raw / capped | Gates | Blind pick |
|---|---|---|---|---|---|
| SaaS landing | 55 / 55 | 6/6 | **57** / 50 | 3/6 | with skill |
| Ops dashboard | **60** / 60 | 6/6 | 50 / 50 | 2/6 | with skill |
| Mobile onboarding | 57 / 57 | 6/6 | **59** / 50 | 5/6 | with skill |
| Brand identity page | 59 / 59 | 6/6 | 40\* / 40 | 4/6 | with skill |
| Designer portfolio | 59 / 59 | 6/6 | 59 / 50 | 4/6 | with skill |
| **Mean** | **58.0** | **30/30** | 53.0 | 18/30 | 5–0 (capped) |

\* The iteration-1 brand-page baseline score is unreliable: its grader misread the very tall screenshot as another page (see "Integrity notes").

**Verdict:** v1 won every brief on the capped score, because of the gates, but **not** on raw design quality. It lost 2 briefs, tied 1, and the mean raw margin was small at +5.

Per-axis means (with / without):

| Axis | With skill | Without skill |
|---|---:|---:|
| Direction | 7.2 | 7.4 |
| Typography | 7.4 | 7.4 |
| Colour | 7.0 | 7.0 |
| Layout | 7.2 | 6.6 |
| Craft | 7.4 | 5.8 |
| Motion | 6.4 | 5.8 |
| UX | 7.6 | 5.6 |
| Content | 7.8 | 7.4 |

**Diagnosis:** v1 produced correct but safe work: Inter for everything, a neutral base and no bespoke art. The unconstrained baselines reached for characterful serif display type and illustration, so they tied or won on direction and typography while failing accessibility.

### Changes made for v2
1. **"Restraint is not blandness."** Every design now needs:
   - a characterful **display voice**, picked from a new table in `typography.md`, with Inter-only allowed only for dense app chrome;
   - **at least one piece of bespoke art in the first viewport** that stages the signature moment.
2. Every token preset gained a `--font-display`. The example landing page now uses a display face.
3. A **template test** and a **blank-section test** were added to the critique loop.
4. **Scroll reveals are progressive enhancement**, so content is visible without JS and in full-page captures.
5. The loop wording now says that scoring below the bar after loop 1 is normal and a reason to continue. Builders also check one non-default state.

## Iteration 2 (skill v2): same baselines, new with-skill builds

| Brief | With skill raw / capped | Gates (audit) | Without skill raw / capped | Gates | Blind pick | Raw margin |
|---|---|---|---|---|---|---:|
| SaaS landing | **65** / 65 | 6/6 | 51 / 50 | 3/6 | with skill | +14 |
| Ops dashboard | **61** / 61 | 6/6 | 43 / 43 | 2/6 | with skill | +18 |
| Mobile onboarding | **63** / 63 | 6/6 | 55 / 50 | 5/6 | with skill | +8 |
| Brand identity page | **66** / 50† | 6/6 | 46 / 46 | 4/6 | with skill | +20 |
| Designer portfolio | **65** / 65 | 6/6 | 56 / 50 | 4/6 | with skill | +9 |
| **Mean** | **64.0** | **30/30** | 50.2 | 18/30 | **5–0** | **+13.8** |

† On the brand page, the grader failed G1 by eye: at 390px the decorative hero disc sat behind the hero copy. The automated audit passed it because the text itself has sufficient contrast against its declared background. The fix was folded into v2's craft pass (item 13: art never sits behind text on mobile). The skill build still won blind on raw score, 66 vs 46.

Per-axis means, iteration 2 (with / without):

| Axis | With skill | Without skill |
|---|---:|---:|
| Direction | **8.2** | 6.2 |
| Typography | **8.6** | 7.0 |
| Colour | **7.6** | 6.8 |
| Layout | **7.6** | 6.6 |
| Craft | **7.8** | 5.4 |
| Motion | **7.2** | 5.6 |
| UX | **8.2** | 5.6 |
| Content | **8.8** | 7.0 |

**Verdict:** v2 wins every brief on raw design quality, by +8 to +20 points, as well as on the gates. It leads on all 8 axes. The largest gains over v1 are in Direction (+1.0), Typography (+1.2) and Content (+1.0), which were exactly the axes the v1 diagnosis targeted.

### Objective audit summary (both iterations)

| | With skill | Without skill |
|---|---|---|
| Hard gates passed | **30/30** (both iterations) | 18/30 |
| Briefs failing AA text contrast | 0 / 5 | 5 / 5 (worst pairs 1.0:1 and 1.17:1) |
| Overflow at 390px | 0 / 5 | 1 / 5 (324px) |
| Invisible keyboard focus | 0 / 5 | 2 / 5 |
| Text < 12px | 0 / 5 | 4 / 5 |

## Integrity notes (what went wrong in the process and how it was handled)
1. **Scroll-reveal artefact.** The first round of grading saw blank sections in two baselines because their reveal-on-scroll content hadn't animated in yet in the full-page capture. That round was **discarded** (files kept as `grading_round1_biased.json`). `audit.mjs` now scrolls slowly before capture, and every pair was re-graded on full renders.
2. **Misread tall screenshots.** Two graders, in iteration 1 and in the first iteration-2 pass, claimed the brand-page baseline screenshot showed the wrong site. A crop proved it was correct (Halcyon). The iteration-2 pair was re-graded from 1800px tiles, with the grader required to name each tile's first heading (`grading_misread.json` is kept). The iteration-1 brand-page baseline score (40) stays flagged as unreliable.
3. **Grader variance.** The same baseline landing page scored 57 raw in one blind pass and 51 in another, so single-grader scores carry about ±6 noise. The iteration-2 margins (+8 to +20) exceed that on every brief, and the per-axis pattern is consistent.
4. **Limits.** n = 1 build per arm per brief. The graders are LLMs, not human designers, and the same model family that built the pages. The baselines received no design guidance at all. The skill's advantage is largest on accessibility and states, which the rubric deliberately weights through its gates.

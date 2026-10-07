# AAA design rubric

Use this to score your own output, in step 6 of `SKILL.md`, and to compare two designs. Score from the **rendered screenshots** and the audit report, not from the code.

## Hard gates (pass/fail, any fail caps the total at 50/80)

| Gate | Pass condition | How to check |
|---|---|---|
| G1 Contrast | All text ≥ 4.5:1, or ≥ 3:1 if ≥ 24px or ≥ 18.66px bold. Control borders and focus rings ≥ 3:1 | `audit.mjs` contrast gate; text over images checked by eye |
| G2 Mobile | No horizontal overflow at 390px; nav usable; touch targets ≥ 44px (minor misses become a warning) | `shot-390.png`, `noOverflow390` |
| G3 Keyboard | Visible `:focus-visible` style on every focusable element; logical order; Esc closes overlays | `focusVisible` gate + Tab test |
| G4 Motion safety | `prefers-reduced-motion` removes movement; no infinite decorative motion without a pause | `reducedMotion` gate |
| G5 Semantics | One h1, no heading skips, alt on images, names on controls, real buttons and links | `altAndNames` + warnings |
| G6 Real content | No lorem ipsum, no typos, no "Button"/"Title" placeholders | read the page |

## Quality axes (1–10 each, total /80)

Anchors: **5** = competent but forgettable (a template), **7** = clearly above average and cohesive, **9** = would be featured in a curated gallery.

1. **Direction & concept.** Is there one clear idea, the signature moment, that does a job? Is there one structural base plus at most one expressive layer?
   - 3: generic or no idea.
   - 5: a theme but no moment.
   - 7: a clear moment.
   - 9: the moment *is* the function (the confirmation is the data).
2. **Typography.**
   - Scale discipline: 6–8 steps with a consistent ratio.
   - Per-size tracking; display leading ≤ 1.1, body ~1.5; measure ≤ 72ch.
   - A second voice (mono or serif) used with intent; at most 2 weights per family per screen.
   - 3: default sizes, everything bold. 9: a confident editorial hierarchy with optical details.
3. **Colour.**
   - One accent, tinted neutrals, semantic colours with ink shades, and category hues threaded through layers.
   - Dark mode retuned rather than inverted (if present).
   - 3: many competing hues or flat greys. 9: a restrained palette where every hue has a role.
4. **Layout & composition.**
   - Grid adherence and a focal point per viewport.
   - Deliberate negative space; rhythm between sections; nested radii; alignment.
   - 3: everything centred and evenly spaced. 9: tension and hierarchy, and nothing feels arbitrary.
5. **Detail & craft.**
   - Checklist items visible in the render: hairlines, inner highlights, tabular numbers, dimmed units, consistent icon strokes, no layout shift.
   - 3: rough edges. 9: flawless at 1440 and 390.
6. **Motion & interaction.**
   - Purposeful transitions on the token scale; ease-out entries, faster exits.
   - The signature interaction works; hover, press and focus are all designed. For static deliverables, judge the defined CSS transitions and states.
   - 3: none or gratuitous. 9: motion explains state changes.
7. **UX & states.**
   - Clear primary action; all 8 states on interactive components; empty, error and loading designed.
   - Forms labelled; undo; progress in two forms.
   - 3: happy path only. 9: every state is designed and on-brand.
8. **Content & copy.**
   - Specific, plausible, scannable content: real numbers, units, names. The voice matches the tone words.
   - 3: placeholder-ish. 9: copy you could ship.

## Reporting format

```
Gates: G1 ✓  G2 ✓  G3 ✓  G4 ✓  G5 ✓  G6 ✓
Direction 8 · Type 8 · Colour 7 · Layout 8 · Craft 7 · Motion 7 · UX 8 · Content 8  = 61/80
Top 3 fixes: 1) … 2) … 3) …
```

**Pass bar:** all gates pass, every axis ≥ 7, total ≥ 64.

When comparing two designs blind (as in the evals), score each independently first, then note which one you would ship and why.

# Anti-patterns

These are the most frequent failures across 348 studied references, with the number of examples showing each. Treat every row as a check.

| # | Anti-pattern | Seen in | Measured example | Fix |
|---|---|---:|---|---|
| 1 | Low-contrast secondary, meta and placeholder text | 167 | #9a9a9a on white is 2.8:1; #b8b8bd is 2.0:1; dark-card greys 2.5:1 | text-2 ≥ 7:1, text-3 ≥ 4.5:1; on white, meta no lighter than #6b6b72 |
| 2 | White text on light or saturated fills | 81 | white on #0fdf43 is 1.8:1, on lilac #D1BAF7 1.7:1, on #ffa8cd 1.8:1 | Dark ink of the fill's hue, `color-mix(in oklab, var(--c) 25%, #000)`, or a deepened button shade |
| 3 | Text over busy imagery, gradients or motion | 80 | swings 2.2–8.8:1 as a 3D backdrop rotates | Solid text zone, a scrim tinted from the image, or a capped luminance band |
| 4 | Missing rules or states (error, empty, focus, disabled, min-size, misuse) | 81 | only 4 of 348 references show empty, error or 404 states | Design all 8 states; brand pages need min-size and misuse |
| 5 | Unreadable rotated, warped or refracted text | 24 | a jelly slider refracts its own value to 1.5:1 | Effects on rims and chrome only; content stays upright |
| 6 | Hover-only or hidden affordances | 24 | folders that reveal only on hover | Visible resting affordance, touch and keyboard equivalents |
| 7 | Decorative motion with no meaning; endless loops | 22 | chrome rings looping forever; an 8s physics swing | Every animation maps to state; ambient ≥ 3s, seamless, reduced-motion off |
| 8 | Typos, placeholder copy, lorem ipsum | 20 | "Sing up", "Wiew demo", copy pasted from another project | Real, specific, proofread copy |
| 9 | Colour-only semantics | 16 | green status text at 2.9:1 and no icon | Pair colour with an icon, word or shape |
| 10 | Contradictory specs | 16 | same colour with two hex values on two pages | One token source |
| 11 | Charts that misstate data | — | a 12×8 = 96-dot grid used for percentages | Geometry derived from the value (10×10 for %) |
| 12 | Stacked expressive layers | — | glass + aurora + gradient mesh on one screen (lowest-rated web shots) | One base plus one expressive layer |
| 13 | Novelty in core inputs | — | picker wheels for multi-select, rotated nav text | Keep native control affordance; put novelty in the feedback |
| 14 | Template sameness | — | three templates identical except brand colour | A signature moment that does a job |
| 15 | One grey reused on dark and light surfaces | — | #9a9a9a: 7.5:1 on black, 2.8:1 on white | Separate text tokens per surface |
| 16 | Desktop-only layout | — | fixed sidebar splitting words at 390px | Design 390px explicitly; collapse nav |

**Why contrast keeps failing.** Holistic judgement under-penalises it. In the study, examples with contrast failures scored about the same as those without (usability 6.64 vs 6.68). That's why `SKILL.md` treats contrast as a computed gate rather than a matter of taste.

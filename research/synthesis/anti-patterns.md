# Anti-patterns (what the weaker examples do)

The counts are distinct examples per anti-pattern cluster, from `_clusters.json`. The "Weakest" column lists examples from the bottom-ranked decile.

| # | Anti-pattern | Count | Weakest / clearest examples | Fix |
|---|---|---:|---|---|
| 1 | Low-contrast secondary, meta and placeholder text | 167 | insp-mobile-gradient (1.68:1), insp-8-0 family, insp-ai-prompt-bar (#b8b8bd 1.98:1), bg-naseem-al-faihaa body (2.14:1) | text-2 ≥ 7:1, meta ≥ 4.5:1. On white use ≤ #6b6b6b for meta (5.3:1), not #9a9a9a (2.8:1) |
| 2 | White text on light or saturated fills | 81 | insp-invite-code-interaction (#0fdf43, 1.8:1), bg-kazam (lilac, 1.74:1), bg-klarna (#ffa8cd, 1.79:1), insp-1-18 (#02aeff, 2.47:1) | Dark ink of the same hue (`color-mix(in oklab, var(--c) 25%, #000)`), or a deepened "button" shade |
| 3 | Text over busy imagery, gradients or motion | 80 | insp-interactive-footer (2.26:1), insp-liquid-glass (2.58–8.82:1 as it rotates), insp-7-8 (2.24:1 on the gold band), insp-404-page (1.47:1 over clouds) | Solid text zone; scrim sampled from the image; cap the luminance where text sits |
| 4 | Missing rules or states (min size, misuse, type scale, error/empty) | 81 | bg-kazam, bg-northalley, bg-twitch, bg-frame-io (no min size); only 4 of 348 examples show empty, error or 404 states | Checklist of required states and rules (see `gaps.md`) |
| 5 | Unreadable rotated, warped or refracted text | 24 | insp-1-2 (jelly slider hides its own value, 1.52:1), insp-genres-filter, rotated labels | Keep the effect on rims and chrome; content stays upright and undistorted |
| 6 | Hover-only or hidden affordances | 24 | insp-1-36, folder peeks, insp-hook-sidebar | Visible resting affordance; touch equivalent; keyboard path |
| 7 | Decorative motion with no meaning; constant loops | 22 | chrome-ring buttons insp-1-31/1-36/1-4 loop forever; insp-personal-site swing decays over 8.1s | Every animation maps to a state change; ambient loops ≥ 3s, seamless, pausable, disabled for reduced motion |
| 8 | Typos and copy errors | 20 | "Sing up" (insp-3-2), "Wiew demo" (insp-brand-work), "mertics" (insp-tensorlake-brand), bg-bella-nova pasted copy, bg-kia lorem ipsum | Proofread; real content, never placeholder |
| 9 | Colour-only semantics | 16 | insp-coding-agent (#16a34a on #f2f2f2, 2.94:1), red/green deltas | Pair with icon, word or shape (insp-wos-island-animations does) |
| 10 | Inconsistent or contradictory specs | 16 | bg-mastercard-foundation, bg-bolt, bg-visit-dubai, bg-fiba | One token source exported to every format |
| 11 | Data that lies | — | insp-components-n3xt (a 12×8 dot chart overstates every %), insp-follower-count, insp-4-1 (wrong face for age) | Chart geometry derived from the value (10×10 for %) |
| 12 | Stacking expressive layers | — | insp-glassmorphism-animation (24), insp-8-2 (25), insp-9-2 (26): glass + aurora + gradient-mesh at once | One expressive layer per screen |
| 13 | Novelty over convention in core controls | — | unconventional toggles, picker wheels for multi-select, rotated text nav | Keep the control's native affordance; add the novelty to feedback, not to the input |
| 14 | Template sameness | — | bg-cobalt/form/owire-brand-guide share identical computed styles and differ only in brand colour (22 each) | Commit to a proprietary device or one expressive layer |
| 15 | Same grey on dark and light surfaces | — | insp-3d-animated-cards (#9a9a9a: 7.46:1 on black, 2.81:1 on white) | Separate text tokens per surface |
| 16 | Non-collapsing sidebars and desktop-only layouts | — | bg-seat-geek (breaks mid-word on mobile), bg-super-com | Design the 390px layout explicitly |

**Score impact, measured.**

| Group | Examples | Mean usability | Mean aesthetics |
|---|---:|---:|---:|
| Tagged with one of the three contrast clusters (#1–#3) | 249 | 6.64 | 7.96 |
| Not tagged | 99 | 6.68 | 8.08 |

The difference is negligible, even though the analysts measured the failures themselves. Contrast failures persist in showcase work because they don't look bad in a screenshot, and holistic judgement, human or model, under-penalises them. The skill therefore treats contrast as a **computed gate** (`scripts/contrast.py` plus a rubric hard-fail), not a matter of taste.

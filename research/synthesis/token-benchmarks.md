# Token benchmarks (observed → recommended)

The numbers come from three measured sources:

1. **Computed styles of 41 live brand and product sites** (`_token_bench.json`, from `census_*.json`). These are the real rendered values.
2. **Measured motion profiles of 261 Inspora videos** (`_motion_stats.json`). These are frame-difference energy, 1,368 transitions of 2.5 s or less.
3. **Front matter of 348 analyses** (`_aggregate.json`). Radii, palettes and typefaces as read from pixels.

Ranges are p25–p75 unless noted.

## Typography

| Measure | Observed | Recommended default |
|---|---|---|
| Body size (desktop) | median **15px** (14–16), range 12–21 | **16px** body, 14px dense UI, 13px meta. Never below 12px |
| Display size | median 60px (37–74); poster sites 208–320px (bg-klarna) | `clamp(2.5rem, 5vw + 1rem, 4.5rem)` for hero; up to 8–12vw only for type-as-image |
| Display ÷ body | median **3.75** (2.57–4.92) | 3.5–5× for landing pages, 2–2.5× for apps |
| Distinct sizes in use | median **9** (5–10), max 21 | 6–8 named steps; more than 10 = scale drift |
| Step ratio between used sizes | median **1.167** (1.106–1.278) | 1.2 (minor third) for product UI; 1.25–1.333 for marketing |
| Body line-height | median **1.3** (1.2–1.5) | 1.5 for paragraphs ≥ 3 lines, 1.35 for UI text, 1.0–1.1 for display |
| Display tracking | median **−0.01em** (−0.029 to −0.004); extremes −0.071em | −0.02em at 40–64px, −0.03em at ≥ 72px, 0 at body, +0.06–0.1em for caps ≤ 13px |
| Measure | Brand docs: 40–75 characters per line (bg-olympic 40–70, bg-discord 50–75) | 60–72ch body, 40–50ch lead |

**Families.** Inter appears in 132 of 348 analyses (identified or closest match). Then come SF Pro (≈60 with variants), JetBrains Mono (19), Geist Mono (14), Inter Display (12), Neue Montreal, Neue Haas, Instrument Serif and Tiempos. The type classes split as follows: neo-grotesk in 229 of 287 Inspora examples, mono in 69, and an editorial serif as display in 25.

Implications:

- A neo-grotesk alone is table stakes and signals nothing.
- Differentiation comes from the **second voice**: a mono for metadata and numbers, or a serif for display.
- The pairing that recurs in top work is **neo-grotesk UI + mono metadata** (insp-rag-pipeline, insp-model-router, insp-support-analytics, insp-ticket-stub).
- The editorial variant is **serif display + neo-grotesk body** (insp-melon-jelly, insp-stamp-shader).

Tracking is tokenised per size, not set once:

- bg-adobe tracks by point size, from +20 at 4pt through 0 at 9–12pt to −8 at 30–36pt (units of 1/1000 em).
- bg-ebay-playbook uses −2.5px at 96px, −3.84px at about 150px and −4.92px at 200px.
- Framer uses −2.16px at 54px.

## Colour structure

- **Palette size per example:** median **8** sampled roles (6–8). A typical role set: canvas, 1–2 surfaces, border, text, text-2, one accent and one semantic colour.
- **Mode:** light 161, dark 77, mixed 49 (Inspora). Brand documents are mostly light pages with dark chapter openers.
- **Accent discipline:** "single accent colour, everything else neutral" is the second most frequent craft cluster (104 examples).
- **Neutrals:**
  - **Tinted near-black instead of #000** (30): #0b051d Klarna, #161616 IBM, #11190C Bolt, #1e1919 Dropbox, #1c1c1e Miro.
  - **Warm off-white instead of #fff** (45): #f7f6f4, #f4f1ea, #faf1e5 Instacart, #f7f5f2 Dropbox, #F0F0FF Twitch.
- **Dark surface ladder (dark-premium):** #000 / #0e0e0e → #121212 → #1c1c1c → #2a2a2a → #3a3a3a. Selected states use the step above. Borders are #ffffff14–#ffffff1f.
- **Contrast (the biggest gap):**
  - In 89.9% of Inspora examples and 86.2% of brand documents, at least one reported text pair is below 4.5:1.
  - The median worst pair is 2.27:1 (Inspora) and 2.82:1 (brand documents).
  - 44.5% of all text pairs reported in Inspora analyses fail AA.
- **Recommended:** build every palette as a token ladder and verify pairs in code:
  - text-1 ≥ 12:1;
  - text-2 ≥ 7:1;
  - text-3 (meta, placeholder) ≥ 4.5:1;
  - non-text UI ≥ 3:1.
- **Pairs that recur and fail:** white on light or saturated brand colours. Measured examples:
  - #1CE783 Hulu green: 1.64:1.
  - #0fdf43: 1.8:1.
  - #D1BAF7 Kazam lilac: 1.74:1.
  - #ffa8cd Klarna pink: 1.79:1.
  - #ff0099 Super.com pink: 3.68:1.
  - Fix: dark ink on the brand colour (#222 on #0fdf43 = 8.83:1), or a deepened shade for text use only (Mastercard's AA/AAA ladder: #FF671B 2.91 → #B24813 5.55 → #7F330D 8.7).

## Radius

- **Observed in pixels (analyses):**
  - full pill 9999 in 191 examples;
  - 24 (58), 12 (50), 16 (48), 40 (39), 28 (37), 8 (25), 20 (25), 4 (23);
  - 0 (21), used deliberately for "paper".
- **Observed in CSS (sites):** 16 (17 sites), 8 (11), 0 (11), 4 (9), 24 (8), 12 (8).
- **Pattern:** the best systems use **2–3 radii**: pill + one card radius + one inner radius. Odido uses only 9999 and 40; insp-glass-circle-with-a-gradient only pill and 24.
- **Nested radius rule:** inner = outer − padding. insp-1-30/44/48 nest a 40px tray around a 28px card inset by about 12px. Spotify uses 4px corners on artwork at small sizes and 8px at large.
- **Recommended presets:**
  - *precise:* 6 / 10 / pill;
  - *friendly:* 12 / 20 / pill;
  - *soft:* 20 / 28 / 40 / pill.

## Spacing and layout

- **Base unit:** 4 or 8. Olympic's digital grid is the cleanest published reference:

  | Breakpoint | Columns | Margins | Gutters |
  |---|---|---|---|
  | 1600 | 12 | 104 | 24 |
  | 1025 | 12 | 24 | 24 |
  | 577 | 6 | 32 | 24 |
  | 375 | 4 | 16 | 16 |

- **Proportional layout rules from print-derived systems:**
  - EDP margins are height ÷ 40 (top and bottom) and ÷ 25 (sides);
  - Kia's panel radius R = 0.1 × width;
  - Hulu's radius = shortest edge ÷ 6.
- **Product UI density:** row height 40–65px (insp-infinite-faq rows are 65px; insp-shader-dial 40px). Pills 32–44px high. Section spacing 96–160px on landing pages.

## Shadow and depth

Three recipes recur:

1. **None** (dark-premium: elevation by tint).
2. **Soft ambient:** `0 1px 2px rgb(0 0 0/.04), 0 8px 24px rgb(0 0 0/.06)`.
3. **Hue-matched glow** (86 examples): `0 30px 80px color-mix(in oklab, var(--accent) 25%, transparent)`.

Also recurring:

- An inner highlight or rim (119 examples): `inset 0 1px 0 rgb(255 255 255/.08–.5)`.
- Material shading in the object's own darker hue instead of black (insp-3-3, insp-2-4).
- New Breed's spec is fixed: `0 0 5px rgb(0 0 0/.2)`, multiply, and it may not be altered.

## Motion

| Measure | Observed | Recommended token |
|---|---|---|
| UI transition duration | median **0.33s** (0.2–0.57); p10 0.1, p90 0.93 | `--dur-1: 120ms` (press/hover), `--dur-2: 200ms` (small state), `--dur-3: 320ms` (container/morph), `--dur-4: 560ms` (page/shared element), `--dur-5: 900ms` (scene) |
| Shape share | ease-out 44%, symmetric 37%, ease-in 16%, linear 2% | `--ease-out: cubic-bezier(.2,.8,.2,1)` default; `--ease-in-out: cubic-bezier(.65,0,.35,1)` for moves between two rest states; `--ease-in: cubic-bezier(.5,0,.75,0)` only for exits and gravity |
| CSS transitions on sites | 0.2s (21 sites), 0.3s (15), 0.15s (11), 0.4s (11) | as above |
| Peak of motion energy | median at 38% of the segment | consistent with ease-out |
| Seamless loops | 45% of clips | ambient loops must be seamless or not exist |

Choreography rules seen in measured data:

- **Open slower than close.** Mega-menu opens in 0.37s and closes in 0.13s. The invoice receipt unfolds in 0.6s and collapses in 0.2s. The multi-action button opens in 0.3s and closes in 0.2s.
- **Ease-out for entries, ease-in for exits and gravity.** Folders lift in 0.27–0.30s ease-out and fall in 0.63s ease-in. A paper tear-off drops with ease-in (peak at 0.72).
- **Linear only for machines.** Printer paper feeds run 1.6–2.4s linear.
- **Duration scales with distance.** In insp-8-6, a tap is 0.23s, an in-sheet swap 0.47s and a shared-element lift 1.07s.
- **Springs:** insp-ticket-stub publishes k=237.6, ζ=7.5, ω=13.47 rad/s, a period of about 0.47s. Measured tilt segments are 0.4–0.5s.
- **Content swaps blur rather than slide** (62 examples): content goes from opacity 0, `filter: blur(6px)` and scale 0.97 to rest, starting about 100ms after the container.

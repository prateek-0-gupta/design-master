# Typography

## What the evidence says
- **Body size:** live sites used a median of **15px** (14–16).
- **Scale steps:** consecutive sizes differed by a median ratio of **1.167** (1.11–1.28).
- **Display size:** display was **3.75× body** (2.6–4.9).
- **Body line-height:** **1.3** (1.2–1.5); use 1.5 for long reading.
- **Display tracking:** **−0.01em** median, −0.03em in the most polished examples.
- **Number of sizes:** sites used **9** distinct sizes (up to 21). The best systems use 6–8 named steps.
- **Typefaces:** 80% of showcase work uses a neo-grotesk, with Inter the most common. The differentiator is the **second voice**: mono for metadata and numbers, or a serif for display.

## Pairings (pick one row)

| Direction | Display | Text/UI | Data/meta | Notes |
|---|---|---|---|---|
| Neutral product | Inter Display / Inter Tight 600 | Inter 400/500 | JetBrains Mono / Geist Mono | Switch to the Display optical size above 32px; `font-feature-settings:"ss01","cv11"` |
| Precise / Swiss | Neue Montreal or Söhne (fallback: Inter Tight) | same | Söhne Mono / IBM Plex Mono | Weight 400 headlines at −0.03em feel expensive |
| Editorial | Instrument Serif / PP Editorial New / Tiempos Headline | Inter / Neue Haas Text | JetBrains Mono caps | Serif ≥ 32px only; italic for one word |
| Technical / AI | Geist / Inter 500 | Geist / Inter | Geist Mono for everything computed | Mono caps labels at 12px, +0.08em |
| Playful | Plus Jakarta Sans 700 / Bricolage Grotesque | Plus Jakarta / Figtree | — | Rounded terminals; avoid bold everything |
| Poster / brand | Condensed grotesk (Anton, Oswald, PP Formula) or a mega sans at 700 | Inter | mono | Display at 8–14vw, line-height 0.85–0.95 |
| Apple-native | SF Pro Display (system-ui) | SF Pro Text | SF Mono | Use `-apple-system` stacks; tracking per Apple's size table |

Load fonts with `font-display: swap`, preload the display weight only, and keep 3 families or fewer.

## Scales

**App (ratio 1.2, base 16):** 12 · 14 · 16 · 19 · 23 · 28 · 34.

**Marketing (ratio 1.25, base 16):** 13 · 16 · 20 · 25 · 31 · 39 · 49, plus a hero at `clamp(48px, 7vw, 112px)`.

**Editorial (ratio 1.333, base 18):** 14 · 18 · 24 · 32 · 42 · 56, plus a hero at `clamp(56px, 9vw, 160px)`.

## Tracking per size

Tracking must be set per size, never once for all. The values below are in em, for neo-grotesks:

| Size | Tracking | Line-height |
|---|---|---|
| ≤ 12px caps | +0.08 to +0.12 | 1.2 |
| 12–14 | +0.005 | 1.45 |
| 16–18 | 0 | 1.5–1.6 |
| 20–28 | −0.01 | 1.3 |
| 32–48 | −0.02 | 1.1 |
| 56–80 | −0.028 | 1.02 |
| ≥ 96 | −0.035 to −0.045 | 0.92–0.98 |

Serif display tracking is about half the neo-grotesk value (−0.01 to −0.02em).

## Hierarchy rules
- Use at most 2 weights per family on a screen, e.g. 400 + 500, or 400 + 600 for tiny labels.
- Emphasise with size or colour step (text-1 vs text-2) before weight.
- Use one expressive move per headline: an italic word, a colour-split second line (insp-1-40 style: line 2 in text-3), or a serif swap.
- Sentence case everywhere. Caps only for labels of ≤ 3 words.
- Measure: prose 60–72ch, lead paragraph 40–55ch.
- Numbers: `font-variant-numeric: tabular-nums` in tables, counters and prices. Set the currency and units one size or one colour step lower.
- Hanging punctuation for pull quotes (`hanging-punctuation: first`) and optical left alignment of large display type (shift −0.04em).
- Control widows with `text-wrap: balance` on headings and `text-wrap: pretty` on paragraphs.

## Localisation
- Allow 30% string growth.
- Some brands shrink type for long languages (Slack: −10% EU, −15% JA). Prefer flexible containers.
- Use logical properties (`margin-inline`) for RTL.

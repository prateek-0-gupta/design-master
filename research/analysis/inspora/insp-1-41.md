---
id: insp-1-41
source: inspora
category: Motion
status: analyzed
title: "A country picker"
creator: "@ozzyxs1a"
styles: [micro-interaction, soft-3d, minimal-swiss]
patterns: [command-palette-picker, fuzzy-match-highlight, keyboard-hint-footer, morph-to-silhouette-confirmation, iso-code-keycaps, result-count, retry-reset-chip]
mode: light
palette: ["#f6f6f4", "#ffffff", "#dfe0dd", "#bfbcbb", "#1a1a1a", "#8a8a8a", "#fbe7a1"]
type_families: ["Inter (likely)", "JetBrains Mono / SF Mono (likely, ISO codes)"]
type_class: [neo-grotesk, mono]
radius_px: [28, 20, 10]
motion: {durations_s: [0.13, 0.33, 0.2, 0.13], easing: [ease-out, ease-in-out], loop: true}
scores: {aesthetics: 8, originality: 9, usability: 8, craft: 9}
craft_signals: [input-morphs-into-country-shape, extruded-silhouette-edge, count-in-placeholder, mono-iso-keycaps, highlighted-match-substring, separate-input-and-list-cards, keyboard-legend-footer]
anti_patterns: [inactive-keycaps-low-contrast, territories-render-as-specks]
---
# A country picker — @ozzyxs1a

## 1. Snapshot
- **Subject:** A 2410×1384, 11.6 s, 60 fps capture of a command-palette country picker ("Search 236 countries"). On selection, the search field **morphs into a white, extruded silhouette of the chosen country**: USA with Alaska, then India. A small "↻ retry" chip resets it.
- **Why it's remarkable:** The confirmation state is the data itself. The input's rectangle turns into the country's outline, so the user sees *what* they picked as a shape, not a toast. It is a memorable, information-bearing transition.

## 2. Composition & layout
- **Two stacked cards**, centred on warm off-white #f6f6f4 (key scale 1.21):
  - a search card ≈617×120 px real;
  - a gap of ≈30 px;
  - a list card ≈617×700 px.
- **List rows:** 8 visible rows on a ≈69 px pitch. Each row has a ≈30 px flag emoji, the name at x+52 px, and a right-aligned ISO-code keycap of ≈45×38 px.
- **Footer:** separated by a hairline. It holds ↑ ↓ "move", ↵ "select" and a count ("236 countries", "4 countries", "2 countries").
- **Silhouette state:** the country shape sits roughly where the input was, scaled to ≈450–700 px across. Remote territories (Alaska; Andaman/Lakshadweep specks) keep their true relative positions. The "retry" chip sits below.

## 3. Typography
- **Names:** Inter-like at ≈29 px real, regular, #1a1a1a.
- **Placeholder:** ≈29 px in #8a8a8a, with the count built in ("Search 236 countries").
- **Footer:** ≈22 px grey.
- **ISO codes and "esc":** a monospace (SF Mono / JetBrains Mono-like) at ≈20 px inside keycaps. The selected row's keycap is black text with a darker border; others are pale grey.
- **Match highlight:** the matched substring gets a pale-yellow background (≈#fbe7a1, estimated): "**Uni**ted Kingdom", "Br. **India**n Ocean Ter.".

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #f6f6f4 | warm page background | 95.8% |
| #ffffff | cards, silhouette top face | ~2% |
| #dfe0dd / #eaeae8 | card borders, selected row fill, extrusion side | 3% |
| #bfbcbb | outline of silhouette, hairlines | 0.9% |
| #1a1a1a | names, active keycap | <1% |
| #8a8a8a / #a3a3a3 | placeholder, footer, inactive keycaps | <1% |
| ≈#fbe7a1 | fuzzy-match highlight | <0.1% |

WCAG checks:
- Names #1a1a1a on white: **17.4:1**.
- Placeholder #8a8a8a: 3.45:1, acceptable for a placeholder but below 4.5:1.
- Inactive ISO keycaps (≈#a3a3a3): **2.52:1, a failure.**
- The footer on the page tone (#6f6f6f on #f6f6f4) is 4.64:1.
- Highlighted text (#1a1a1a on #fbe7a1) is 14.13:1.

## 5. Depth & material
- **Cards:** a double-border ("bezel") treatment: an outer 1 px light rim, a ≈6 px pale gutter, then an inner field. They carry a big soft shadow (≈0 30px 60px rgba(0,0,0,.08)). Radii are ≈28 px outer, ≈20 px inner, ≈10 px keycaps.
- **Selected row:** a #f2f2f0 fill with its own 1 px border, like an inset pill.
- **Silhouette:** paper-cut white with a **≈8 px downward extrusion** in light grey, a thin #bfbcbb outline, and a soft ambient shadow. It reads as a die-cut tile or embossed sticker.

## 6. Components & patterns
- **Command palette:** an input with a placeholder count and an `esc` keycap, a filterable list with flag, name and ISO keycap, a keyboard legend footer, and a live result count.
- **Fuzzy search:** substring highlighting ("india" matches both "Br. Indian Ocean Ter." and "India").
- **Confirmation:** a morph-to-silhouette state with a "retry" chip as reset. The picker reappears in its initial state (5.80 s, 10.96 s).

## 7. Motion
- **Measured:** 11.6 s at 60 fps. motion_fraction 0.10. Seven very short segments with a median of **0.13 s**:
  - 0.63–0.77 s (0.13 s, ease-out);
  - 1.73–1.83 s (0.10 s);
  - 2.03–2.37 s (0.33 s, peak 0.35, symmetric);
  - 5.10–5.30 s (0.20 s, ease-in);
  - 6.70–6.80 s;
  - 8.43–8.57 s (0.13 s, ease-out);
  - 10.47–10.60 s.
- seamless_loop_likely **true** (diff 0.03).
- **From frames (estimates):**
  - At 1.93 s the list collapses into the input. At 2.0–2.4 s the input's outline morphs into the USA shape over ≈0.33 s, shown by the blobby intermediate at 1.93 s and the partly formed India shape at 8.38 s.
  - The extrusion and shadow fade in with it. Tiny islands fly into position as specks.
  - Reset (≈5.1 s) is quick: ≈0.2 s with an ease-in.
- **Pace:** the motion is fast and snappy. Most transitions are 0.1–0.3 s, so the picker never feels slow despite the theatrics.

## 8. Brand system
n/a — not a brand system.

## 9. UX
- **Strengths:**
  - Keyboard-first, with a visible legend.
  - The result count updates live.
  - ISO codes help disambiguation.
  - Fuzzy highlight explains each match.
  - The silhouette gives an unmistakable, glanceable confirmation.
- **Risks:**
  - For small countries or territories (Andorra, Anguilla) the silhouette would be a speck. Scale-to-fit or a fallback is needed.
  - Faint ISO keycaps.
  - Flag emoji render inconsistently on Windows.
  - The morph should respect reduced motion.

## 10. Craft signals
- The input rectangle morphs directly into the country outline rather than cross-fading.
- The silhouette has an ≈8 px extruded side and a thin #bfbcbb outline, a die-cut look.
- The placeholder embeds the dataset size: "Search 236 countries".
- The footer count updates with the filter (236 → 4 → 2).
- The matched substring is highlighted in pale yellow.
- The selected row's ISO keycap darkens to #1a1a1a while the others stay pale.
- The input and the list are separate cards with matching double-bezel borders.

## 11. Reproduction recipe
```css
:root{--page:#f6f6f4;--card:#fff;--line:#dfe0dd;--ink:#1a1a1a;--muted:#8a8a8a;--hl:#fbe7a1;
  --font:"Inter",system-ui;--mono:"JetBrains Mono",ui-monospace}
.card{background:var(--card);border-radius:28px;padding:6px;
  box-shadow:0 0 0 1px var(--line),0 30px 60px -10px rgba(0,0,0,.08)}
.card>.inner{border-radius:22px;background:#fafaf8}
.row{display:flex;align-items:center;gap:14px;height:34px;padding:0 10px;border-radius:10px;font:400 15px var(--font);color:var(--ink)}
.row[aria-selected=true]{background:#f2f2f0;box-shadow:inset 0 0 0 1px var(--line)}
.kbd{font:500 10px/1 var(--mono);padding:4px 6px;border-radius:6px;border:1px solid var(--line);color:#a3a3a3;margin-left:auto}
.row[aria-selected=true] .kbd{color:var(--ink);border-color:#bfbcbb}
mark{background:var(--hl);color:inherit;border-radius:2px}
.silhouette{fill:#fff;stroke:#bfbcbb;stroke-width:1;filter:drop-shadow(0 4px 0 #e4e4e1) drop-shadow(0 20px 40px rgba(0,0,0,.08))}
```
Morph: use flubber (`interpolate(rectPath, countryPath)`) or GSAP MorphSVG over 0.33 s with `cubic-bezier(.2,.8,.2,1)`.

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Calm, warm-neutral palette; the paper-cut silhouette is lovely. |
| Originality | 9 | Morphing the input into the selected country's shape is a genuinely new confirmation idiom. |
| Usability | 8 | Keyboard-first, live counts, match highlighting; faint keycaps and tiny-country edge cases. |
| Craft | 9 | Bezelled cards, extrusion detail, snappy timings, accurate geography. |

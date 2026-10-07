---
id: insp-product-comps
source: inspora
category: Product
status: analyzed
title: "Product comps"
creator: "@Swaraj524"
styles: [glassmorphism, dark-premium, photo-led, terminal-mono]
patterns: [kpi-card-with-crop-marks, segmented-tick-progress, filter-attribute-popover, command-palette-with-key-hints, citation-hover-card, count-badges, motion-blur-photo-backdrop]
mode: mixed
palette: ["#222720", "#131c13", "#1b1b1a", "#e8e86a", "#9ebbc9", "#fcfbfc", "#000000", "#5d98b5"]
type_families: ["Neue Montreal / Aeonik-style grotesk (likely)", "Geist Mono / JetBrains Mono (likely)", "Inter (likely)"]
type_class: [neo-grotesk, mono]
radius_px: [24, 16, 10, 4, 0]
motion: null
scores: {aesthetics: 9, originality: 7, usability: 7, craft: 8}
craft_signals: [corner-crop-marks-on-card, mono-uppercase-labels, keyboard-hint-footer, fading-text-reveals-answer-streaming, glass-tinted-by-backdrop, count-badge-only-when-nonzero]
anti_patterns: [inconsistent-radius-language-across-comps, faded-body-text-unreadable]
---
# Product comps — @Swaraj524

## 1. Snapshot
- **Subject:** Four 1024×896/844 zoomed component comps, each over a motion-blurred nature photo:
  - **m0:** "Signal strength" KPI card.
  - **m1:** "Filters" attribute popover.
  - **m2:** "Search customers" command palette.
  - **m3:** AI answer with a citation hover-card ("Stripe Investor Letter").
- **Why it's remarkable:** Every comp is glass tinted by its own photo (green grass, amber blur, golden reeds, blue sky), so one component kit picks up four moods without any palette change.

## 2. Composition & layout
- **m0:** card ~690×415 px.
  - Square corners plus 12 px L-shaped crop marks at the corners (a technical drafting cue).
  - Header: breadcrumb "Threshold / Signal strength" plus a yellow value chip, then a hairline.
  - Two metrics, left and right, at ~64 px.
  - Progress: ~620 px yellow bar plus dashed remainder, with mono scale 0–100%.
  - "ACTIVE CHANNELS" with four 32 px icon tiles and a "4 INPUTS" chip.
- **m1:** a ~390 px popover (radius ~16) under a "Filters" pill.
  - Search field.
  - "User attributes" group.
  - Seven rows at ~53 px pitch with outline icons, optional count badges (2, 1, 3, 5) and chevrons.
  - The hovered row is lifted.
- **m2:** palette ~640×690 px (radius ~24) with a search row and a ⌘K chip.
  - RECENT (2) and ALL USERS (4) groups, rows ~65 px with avatar, name and email.
  - Footer with keycap hints: # tags, ↑↓ navigate, ↗ open, esc close.
- **m3:** a white answer card (radius ~24) holds body text with an inline source chip "🌐 2".
  - A black popover (~635 px, radius ~22) with a caret points at the chip: title + ↗, "1 OF 2" pager, a quoted excerpt, and "Page 14" / "View source ↗" pills.
  - The card footer has a "GPT 5.2 ⌄" model picker and "Add to Knowledge Base".

## 3. Typography
- **m0:** a wide-ish grotesk with open apertures (Neue Montreal / Aeonik feel) at ~64 px for the values; all labels in mono caps (~14 px, +0.08 em).
- **m1–m3:** Inter-like at 16–22 px.
- **m3:** body at ~24 px. Later lines fade progressively (black → #bdbdbd), implying streamed text.
- The mono is reserved for numbers and labels in m0 and for keycaps in m2.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #222720 / #131c13 | m0 tinted glass card | 41% / 5% |
| #e8e86a (est.) | m0 signal yellow (bar, chips) | — |
| #1b1b1a | m1 popover | 39% |
| #9ebbc9 / #5d98b5 | sky in backdrops | 12% |
| #fcfbfc | m3 answer card | 36% |
| #000000 | m3 citation popover | 15% |

WCAG checks:
- White on #222720: 15.23:1.
- Yellow chip text #e8e86a on its #3a3d1f chip: 8.67:1.
- Grey mono #8f948c on #222720: 4.92:1.
- m3 faded tail text #bdbdbd on #fcfbfc: **1.82:1**. This is intentional streaming, but it is unreadable if it persists.

## 5. Depth & material
- **m0 and m2:** translucent glass with heavy blur. The card picks up the photo's hue (green-black, golden-brown) and has a 1 px light hairline border.
- **m1:** near-opaque dark with a subtle border.
- **m3:** a solid black popover over a solid white card. This is the one high-contrast comp.
- Shadows are minimal; separation comes from blur and tint.

## 6. Components & patterns
- **Segmented progress:** a solid fill plus a dashed/ticked "remaining" track.
- **Count badges:** square-ish 20 px grey chips, shown only on attributes with active filters.
- **Online presence:** green dots on avatars (m2).
- **Citation chip:** inline in the prose with a favicon and count; the popover offers pagination across sources.

## 7. Motion
Stills; no motion observed. The m3 progressive fade implies a text-streaming animation, and the m1 cursor implies hover states.

## 8. Brand system
n/a — not a brand system. Identity cues: a crop-mark "spec sheet" framing and photo-tinted glass.

## 9. UX
- Strong keyboard affordances (⌘K, footer hints) and transparent AI sourcing (page reference, "View source").
- **Risks:**
  - Glass over busy photos risks legibility in real use (m2 email text on golden blur is ~3:1 in places).
  - m0's dual 56.2% / 43.8% display repeats one fact.
  - The comps use different radius systems (0, 16, 24), so they read as four kits, not one.

## 10. Craft signals
- The L-shaped corner crop marks sit ~8 px outside m0's square corners.
- The breadcrumb's current-level chip echoes the bar's yellow exactly.
- The keycap footer pairs each icon key with a lowercase verb.
- The citation popover's caret lands precisely on the "2" chip.
- The tint of each glass card is sampled from its own backdrop.

## 11. Reproduction recipe
```css
.glass{background:color-mix(in oklab,var(--tint,#1d231b) 78%,transparent);backdrop-filter:blur(30px) saturate(1.3);
  border:1px solid rgba(255,255,255,.08)}
.kpi{position:relative;border-radius:0}
.kpi::before,.kpi::after{content:"";position:absolute;width:12px;height:12px;border:1.5px solid #fff}
.kpi::before{top:-6px;left:-6px;border-right:0;border-bottom:0}.kpi::after{bottom:-6px;right:-6px;border-left:0;border-top:0}
.label{font:500 12px/1 "Geist Mono",monospace;letter-spacing:.08em;text-transform:uppercase;color:#8f948c}
.bar{display:flex;height:12px}.bar b{background:#e8e86a;width:56.2%}
.bar i{flex:1;background:repeating-linear-gradient(90deg,#3a3d33 0 4px,transparent 4px 8px)}
.kbd{border:1px solid rgba(255,255,255,.25);border-radius:6px;padding:2px 6px;font:12px "Geist Mono"}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 9 | Gorgeous photo-tinted glass; the crop-mark KPI is a standout. |
| Originality | 7 | Familiar components with distinctive framing and tints. |
| Usability | 7 | Keyboard and sourcing affordances strong; glass legibility risk. |
| Craft | 8 | Precise details; radius language differs between comps. |

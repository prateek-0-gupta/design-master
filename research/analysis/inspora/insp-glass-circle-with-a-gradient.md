---
id: insp-glass-circle-with-a-gradient
source: inspora
category: Product
status: analyzed
title: "glass circle with a gradient"
creator: "Bakers Studio"
styles: [dark-premium, glassmorphism, physical-material]
patterns: [hero-orb-status, pill-list-rows, selected-row-lift, mono-numerals, segmented-filter-chips, device-mockup-on-gradient-backdrop]
mode: dark
palette: ["#000000", "#0f0f0f", "#1c1c1c", "#3a3939", "#d9d7d3", "#31395a", "#7b3335", "#efede9"]
type_families: ["Neue Montreal / Suisse Int'l-style neo-grotesk (likely)", "monospaced numerals (likely Söhne Mono / JetBrains-like)"]
type_class: [neo-grotesk, mono]
radius_px: [9999, 48, 24, 22]
motion: null
scores: {aesthetics: 9, originality: 8, usability: 6, craft: 8}
craft_signals: [hairline-rim-on-orb, horizon-gradient-echoes-backdrop, mono-for-money, row-selection-by-surface-lift, giant-radius-rows, scene-backdrop-matches-ui-palette]
anti_patterns: [low-contrast-secondary-text, cropped-content-in-hero-slide]
---
# glass circle with a gradient — Bakers Studio

## 1. Snapshot
- **Subject:** Three 849×1200 slides for "Giza", a DeFi yield-agent app: a desktop dashboard with a glass status orb, the orb isolated on black, and a mobile market-picker.
- **Why it's remarkable:** The orb is the brand. A sunset horizon (pale sky, red band, navy ground) rendered inside a sphere is reused as the photographic backdrop behind every device, so the UI and the scene share one palette.

## 2. Composition & layout
- **Slide 1 (desktop):** The browser frame is cropped off the right edge (x≈82→849+) to imply scale. It uses a two-column layout: a narrow left rail of about 260 px holding the logo top-left and a tagline anchored bottom-left at y≈970, and a content column starting at x≈342. Two ~350 px orbs sit side by side as the hero. Below them is a stack of pill rows about 120 px tall with a ~6 px vertical gap. The eye travels from orb (motion, colour) to the "%16.54 Total APY" row to the highlighted row.
- **Slide 2:** The orb is centred on pure black and occupies about 65% of the width. The negative space is around 35% on every side. It reads as a poster or app icon.
- **Slide 3 (mobile):** A 390-style phone at about 415 px wide is centred on a blurred horizon backdrop. Inside: header, a two-line headline centred at about 36 px, a search field, a chip row that scrolls off the edge (intentional overflow cue), and cards with a 16:9-ish label/value grid.
- **Density:** Low on the desktop (large gaps, about 3 rows visible), medium on mobile.

## 3. Typography
- Neo-grotesk sans with tight apertures, close to Neue Montreal or Suisse Int'l. The headline on mobile is about 36 px with leading of about 1.05 and tracking of roughly −0.02 em.
- **Weights:** Regular (400) everywhere; hierarchy comes from size and grey value, not weight. The logo "Giza" is about 28 px regular.
- **Numerals:** Balance "$50,…" is set in a monospace face at about 24 px. Mono is used only for money and status, which gives a "machine is computing" voice.
- **Scale observed (mobile):** 36 / 17 / 15 / 13 px, a ratio of about 1.2 (minor third) for body steps, with a jump of about 2.1× for the display size.
- **Row labels:** two lines: 15 px white title over 15 px grey (#8a8a8a-ish) provider.

## 4. Colour
| Hex | Role | Share (slide 2) |
|---|---|---|
| #000000 | canvas / app background | 80% |
| #0f0f0f–#1c1c1c | row / card surfaces | — |
| #3a3939 | selected row surface | — |
| #d9d7d3 / #efede9 | orb highlight, sky | 6% |
| #31395a | navy "ground" in orb and backdrop | — |
| #7b3335 | ember-red horizon band | 1% |

WCAG checks:
- White on black is 21:1.
- Grey label #8a8a8a on #000 is 6.08:1 (pass).
- Faint row text (≈#5c5c5c on #1c1c1c) is **2.55:1 (fails AA)**. This applies to the dimmed "Morpho"/"Allocated" labels in non-selected rows.
- White on the selected row (#3a3a3a) is 11.4:1.

Strategy: an achromatic UI with all saturation quarantined inside the hero object and the backdrop photo.

## 5. Depth & material
- **Orb:** a radial-gradient sphere with a 1 px light rim (about rgba(255,255,255,.5)) that separates it from black, plus inner banding (sky, red ember, dark core) that reads as refraction.
- **Second orb:** matte white with soft grey shading, acting as the "balance" sphere.
- **Surfaces and backdrop:** No drop shadows. Elevation comes only from surface lightness steps (#000 → #141414 → #3a3a3a). The backdrop is a heavily blurred horizon photo, which gives depth of field behind the device.

## 6. Components & patterns
- The orb is a status indicator with a spinner and the label "Scanning yield…". It acts as a loading state turned into a hero.
- Pill search button (circle) plus a pill summary field.
- Full-pill list rows with a token icon pair (overlapping 40 px circles), name and provider, and right-aligned metric columns (APY, Allocated).
- **Selected state:** the row lightens to #3a3a3a, with no border.
- **Mobile:** network switcher pill ("Base •••"), wallet icon button, search field (1 px #3a3a3a border, radius about 24 px), filter chips (active chip white with black text, inactive #1c1c1c), market card (radius about 24 px) with a "More ↗" ghost pill and a "Select" checkbox-button.

## 7. Motion
Still images, so no motion was observed. The orb with its "Scanning yield…" spinner implies a slow internal gradient drift: horizon bands rotating or breathing on a 3–6 s loop with ease-in-out, which is the classic "agent thinking" idiom.

## 8. Brand system
n/a — this is a product UI, not a brand system. Identity cues:
- a four-point sparkle logomark in a 1.5 px outline;
- "horizon" colour story tying photography, orb and UI together;
- mono numerals for money.

## 9. UX
- **IA:** Deposit / Withdraw / Settings in the top nav. The portfolio is the hero and pools are listed below it.
- **Affordances:** Rows are clearly tappable (pill shape), and the overflowing chips signal horizontal scroll.
- **Risks:**
  - Dim secondary text below AA.
  - The selected-row signal relies on a luminance shift only.
  - "%16.54" puts the percent sign before the number, which is non-standard and harms scanning.
  - The desktop crop hides values.

## 10. Craft signals
- A 1 px rim light on the sphere edge keeps the circle crisp against #000.
- The backdrop horizon matches the orb's internal bands in all three slides (consistent art direction).
- Monospace is reserved for currency values only.
- Every radius is either full-pill or about 24 px: two radius values, no strays.
- Elevation comes from surface tint (#000/#141414/#3a3a3a), with no shadows on a dark UI.
- Overlapping token icons (−10 px offset) form compact pairs.

## 11. Reproduction recipe
```css
:root{
  --bg:#000; --surface-1:#141414; --surface-2:#1c1c1c; --surface-sel:#3a3a3a;
  --text:#fff; --text-2:#8a8a8a; --border:#3a3a3a;
  --sky:#d9d7d3; --ember:#b8452f; --navy:#31395a;
  --r-card:24px; --r-pill:9999px;
  --font-sans:"Neue Montreal","Inter",system-ui,sans-serif; --font-mono:"JetBrains Mono",ui-monospace,monospace;
}
.orb{width:340px;aspect-ratio:1;border-radius:50%;
  background:
    radial-gradient(120% 60% at 50% 105%, #000 35%, transparent 60%),
    linear-gradient(180deg,#3b4366 0%,#9aa3b5 45%,#c9b9a6 55%,#b8452f 62%,#141826 70%,#000 100%);
  box-shadow: inset 0 0 0 1px rgba(255,255,255,.45), inset 0 -40px 80px rgba(0,0,0,.6);}
.row{border-radius:var(--r-pill);background:var(--surface-1);padding:28px 32px;display:grid;grid-template-columns:auto 1fr auto auto;gap:24px}
.row[aria-selected=true]{background:var(--surface-sel)}
.money{font-family:var(--font-mono);font-variant-numeric:tabular-nums}
```
Tailwind: `rounded-full bg-neutral-900 aria-selected:bg-neutral-700 px-8 py-7 text-[15px] text-white`, labels `text-neutral-400`.

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 9 | Disciplined achromatic UI with one luminous hero object, and backdrop and UI share a palette. |
| Originality | 8 | Turning a loading state into a refractive "horizon orb" brand object is fresh for DeFi. |
| Usability | 6 | Clear structure, but secondary text fails contrast and the percent placement is odd. |
| Craft | 8 | Tight radius and tint system plus rim-light detail. Cropping hides some values. |

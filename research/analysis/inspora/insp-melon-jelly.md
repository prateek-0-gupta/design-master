---
id: insp-melon-jelly
source: inspora
category: Web
status: analyzed
title: "Melon Jelly"
creator: "Three.js (@threejs)"
styles: [editorial-serif, soft-3d, physical-material, x-scientific-specimen]
patterns: [specimen-control-panel, live-physics-readout, tool-toggle-segmented, variety-swatch-picker, labelled-range-sliders, editorial-title-lockup, gesture-instruction-caption]
mode: light
palette: ["#dfdcd7", "#e9e8e3", "#bfbdb6", "#1c1c1c", "#8d302f", "#2f6b2a", "#e8a020"]
type_families: ["Italic transitional serif, close to Newsreader / GT Sectra (likely)", "Inter-like grotesk for controls (likely)", "monospace for readouts (likely JetBrains Mono / IBM Plex Mono)"]
type_class: [editorial-serif, neo-grotesk, mono]
radius_px: [2, 4]
motion: {durations_s: [1.1, 0.6, 1.13, 0.5, 0.9, 1.63], easing: [ease-out, ease-in-out, linear], loop: false}
scores: {aesthetics: 9, originality: 9, usability: 7, craft: 9}
craft_signals: [slider-end-labels-in-italic, live-units-on-readouts, figure-number-on-panel, tracked-caps-microlabels, contact-shadow-on-gel, subsurface-translucency, tetrahedral-sim-footnote]
anti_patterns: [tiny-grey-captions-fail-contrast, capture-overlay-obscures-ui]
---
# Melon Jelly — Three.js (@threejs)

## 1. Snapshot
- **Subject:** An 18 s, 1920×1080 capture of a WebGPU soft-body toy. A watermelon-wedge jelly is sliced with a cleaver into wobbling cubes that can be grabbed, flung and re-coloured. The page is framed as "Material studies / No. 009".
- **Why it's remarkable:** It treats a physics demo like a museum specimen plate. It pairs an italic serif title, a lab-style control card ("The specimen, fig. 9"), and live mass, volume, kinetic and piece readouts with a convincingly gelatinous material.
- **Note:** The top-centre "Claude Opus 5.5 / 4.5$+7.98$=12.48$" box is a poster's cost annotation burned into the capture, not part of the design.

## 2. Composition & layout
- **Four corners anchor the UI; the centre is the stage:**
  - Top-left: a title lockup at x=33, with "Melon / Jelly." stacked at about 72 px and the second line indented about 40 px.
  - Top-right: a "WEBGPU · LIVE" status chip.
  - Right: a control card 190 px wide at x≈1695–1885, y≈78–532.
  - Bottom-left: an instruction caption plus a 4-cell readout strip (y≈975–1010) with 1 px vertical dividers.
  - Bottom-right: an "Inside the experiment +" disclosure.
- **Margins:** a consistent 33 px outer margin on the left and about 35 px on the right.
- **Coverage:** The specimen occupies the centre ~40% with about 60% empty paper around it. Free space is part of the play area (pieces fly off-screen at 13.03 s).

## 3. Typography
- **Title:** A high-contrast transitional italic serif (Newsreader- or GT Sectra-like), about 72 px, with tight leading of about 0.95 and the second line hung right. Below it a three-line roman serif tagline at 12 px ("A slice of summer…").
- **Microlabels:** "MATERIAL STUDIES / NO. 009", "THE SPECIMEN", "TOOL", "VARIETY" and "FIRMNESS" are 9–10 px grotesk caps with about +0.12 em tracking.
- **Readouts:** Values like "0.40" and "≈64 g" are monospaced at about 13 px with unit suffixes at about 8 px ("% of rest", "µJ").
- **Italic serif as annotation:** Slider endpoints ("trembling / set", "lively / syrupy"), swatch names ("Crimson", "Golden", "Rosé") and "fig. 9" are 9 px italic serif. Italic serif is the voice of annotation throughout, a scientific-plate idiom.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #dfdcd7 | paper canvas | 81% |
| #e9e8e3 | card / button fill | 3% |
| #bfbdb6 / #a18681 | hairlines, cast shadows | 10% |
| #1c1c1c | ink, active tool button | <2% |
| #8d302f (≈#e53a3f lit) | melon flesh | 5% |
| #2f6b2a | rind stripes | — |
| #e8a020 | "Golden" variety | swatch |

WCAG checks:
- Ink on paper is 12.46:1.
- White on the active "Knife" button (#1c1c1c) is 17.04:1.
- Secondary grey (#6b6863) is 4.06:1, AA-large only.
- The faint footnote grey (≈#9a978f) is **2.13:1, which fails**.

The palette is a warm achromatic paper. The only saturated colour lives in the specimen and in its 3-swatch picker, so the UI never competes with the subject.

## 5. Depth & material
- **Jelly:**
  - It shows subsurface translucency: red deepens to #8d302f in thick areas and highlights bloom white on the bevels.
  - There are rounded edges of about 15% of the cube size and a specular streak on each top face.
  - Seeds are suspended inside the volume, and a soft blush-tinted contact shadow (#a18681) carries the red into the floor.
- **Cleaver:** It casts a long, blurred, offset shadow onto the paper, which sells the height above the table.
- **UI:** Flat, with 1 px hairline borders (#bfbdb6), no shadows, and radii of 2–4 px. It is deliberately "printed" against the physically rendered subject.

## 6. Components & patterns
- **Segmented tool toggle:** Hand / Knife. The active state is filled black with white text and an icon.
- **Variety picker:** three 40×22 swatches drawn as mini cross-sections (rind band plus flesh) with italic captions. The selected one is outlined.
- **Sliders:** Firmness 0.40 and Internal damping 0.45, each with a 1 px track, a 9 px circular thumb, a value top-right, and semantic italic end labels.
- **Actions and options:** "Give it a nudge" / "Reset" buttons, ¼ speed and Show mesh checkboxes, and a full-width "Pause".
- **Readout strip:** Mass ≈64 g · Volume 99.7% of rest · Kinetic 0.42 µJ · Pieces 6. The values update live (Pieces goes 1→2→5→6 across the sheet).
- **Contextual instruction:** The text swaps between Knife ("Draw a line across the slice…") and Hand ("Grab any piece…") modes, as seen in the 13.03 s frame.

## 7. Motion
Measured: 18.05 s at 60 fps, motion_fraction 0.57, 18 segments with a median of 0.46 s, not a loop.
- **Cuts:** The cleaver approach plus wobble take about 1.1 s each (0–1.1 s symmetric; 3.37–4.5 s peak 0.37; 4.73–5.83 s peak 0.59). The jelly's damped oscillation fills these spans.
- **Reactions:** Short ease-out spikes of 0.10–0.6 s (2.07–2.67 s peak 0.31; 6.9–7.4 s peak 0.17; 11.4–12.3 s peak 0.09) match the knife impact followed by decaying wobble.
- **Throws:** Long continuous segments at 14.73–16.37 s (1.63 s) and 16.77–17.93 s (1.17 s) are pieces flung and settling, plus the variety switch to Golden at about 17 s.

The motion is physics-driven, not tweened: decaying oscillation with the damping exposed as a 0.45 slider. The UI chrome itself does not animate.

## 8. Brand system
n/a — not a brand system. It does carry a series identity: "Material studies / No. 009", figure numbering ("fig. 9") and the "Inside the experiment" footer imply a reusable specimen-plate template for a run of experiments.

## 9. UX
- **Strengths:**
  - The tool modes are explicit.
  - Instructions change per mode.
  - Sliders show both a number and a qualitative meaning (trembling ↔ set).
  - The live readouts reward play.
  - There are ¼ speed and Pause controls for motion-sensitive users.
- **Weaknesses:**
  - The 9–10 px microcopy and the footnote at 2.1:1 are hard to read.
  - The control card is small (190 px) for touch.
  - The cleaver cursor can overlap the panel (key frame).

## 10. Critical craft signals
- Slider endpoints are labelled in italic serif with qualitative words, not just min and max.
- Readout values carry units in a smaller size ("≈64 g", "0.42 µJ").
- The footnote explains the simulation scale ("1 sim unit ≈ 3.5 cm, gummy at 1.3 g/cm³"), which shows scientific framing taken seriously.
- The variety swatches are cross-sections of the actual object, not flat chips.
- The title's second line "Jelly." is indented and ends with a period, a classic editorial lockup.
- The contact shadows are tinted by the object colour rather than grey.

## 11. Reproduction recipe
```css
:root{
  --paper:#dfdcd7; --card:#e9e8e3; --hair:#bfbdb6; --ink:#1c1c1c; --ink-2:#6b6863;
  --serif:"Newsreader","GT Sectra",Georgia,serif; --sans:"Inter",system-ui,sans-serif; --mono:"JetBrains Mono",ui-monospace,monospace;
}
body{background:var(--paper);color:var(--ink)}
.title{font:italic 400 72px/.95 var(--serif);letter-spacing:-.02em}
.title span:last-child{display:block;padding-left:.55em}
.eyebrow{font:500 9.5px/1 var(--sans);letter-spacing:.12em;text-transform:uppercase;color:var(--ink-2)}
.card{width:190px;padding:14px;border:1px solid var(--hair);border-radius:2px;background:color-mix(in srgb,var(--card) 70%,transparent)}
.seg{display:grid;grid-template-columns:1fr 1fr;gap:4px}
.seg button{border:1px solid var(--hair);border-radius:2px;font:500 10px var(--sans);padding:7px}
.seg [aria-pressed=true]{background:var(--ink);color:#fff;border-color:var(--ink)}
.range-ends{display:flex;justify-content:space-between;font:italic 9px var(--serif);color:var(--ink-2)}
.readout{font:500 13px var(--mono)} .readout small{font-size:8px;color:var(--ink-2)}
.stats{display:grid;grid-template-columns:repeat(4,auto);border-top:1px solid var(--hair)}
.stats>div+div{border-left:1px solid var(--hair);padding-left:12px}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 9 | Editorial specimen-plate framing plus a delicious jelly render, with a quiet paper palette that lets the object sing. |
| Originality | 9 | Pairing museum-catalogue typography with a soft-body physics toy is a new register for WebGL demos. |
| Usability | 7 | Clear modes and meaningful sliders. Microtype and footnote contrast are too small and too faint. |
| Craft | 9 | Units, figure numbers, italic annotations and a tinted contact shadow, every layer considered. |

---
id: insp-collection-layout
source: inspora
category: Motion
status: analyzed
title: "interaction collection layout"
creator: "@nickpylll"
styles: [micro-interaction, corporate-clean, x-light-ios-native]
patterns: [bottom-sheet-editor, segmented-toggle, focus-and-dim-siblings, corner-crop-brackets, contextual-toolbar-swap, primary-cta-label-morph, dot-grid-canvas]
mode: light
palette: ["#e8e9eb", "#fdfdfd", "#181210", "#3c3c3c", "#8e8e8e", "#1a7fd8", "#79735e", "#acbab7"]
type_families: ["SF Pro Text / Display (likely)"]
type_class: [neo-grotesk]
radius_px: [9999, 28, 52]
motion: {durations_s: [0.3, 0.2, 0.37, 0.33, 0.2], easing: [ease-in-out, ease-out], loop: true}
scores: {aesthetics: 8, originality: 6, usability: 7, craft: 8}
craft_signals: [selected-card-blur-not-just-fade, crop-brackets-only-on-corners, cta-label-swaps-with-mode, dot-grid-workspace-signal, black-pill-primary-white-pill-secondary]
anti_patterns: [placeholder-grey-below-aa, link-blue-below-aa-at-15px]
---
# interaction collection layout — @nickpylll

## 1. Snapshot
- **Subject:** A 6.3 s, 1080×1080 loop of an iPhone bottom sheet for building a "collection" cover: three poster images fan out, one is tapped and isolated for cropping, then the fan returns.
- **Why it's remarkable:** Selection is shown by taking the siblings out of focus (opacity *and* Gaussian blur) rather than adding a border, and the toolbar and primary button both change meaning in place ("Import" → "Crop · Back · Front", "Create" → "Save").

## 2. Composition & layout
- Device is cropped top and bottom; the visible sheet spans x≈250→830 (≈580 px) with a ≈28 px top radius and a 54×4 px grabber at y≈52.
- Vertical stack, all centred on x=540: segmented toggle (y≈80–140, 286×60), image stage on a dot grid (y≈150–550), tool pill (y≈560–620), title + subtitle (y≈715–790), bottom bar (y≈855–913).
- Image stage: three posters ≈210×290 px rotated ±3–6°, overlapping by ≈40 px. In crop mode the centre poster stays sharp and slightly enlarged; the side posters drop to ≈30% opacity with ≈6 px blur.
- Bottom bar splits 2:1 — a white pill field ("Source / cargoworld 🌐", ≈360 px) and a black CTA pill (≈130 px).

## 3. Typography
- SF Pro (system) throughout; no custom face.
- Title "cargoworld" ≈30 px semibold, #111; subtitle "add subtitle" ≈22 px regular in mid-grey — a placeholder style.
- Toggle labels ≈20 px medium; tool pill ≈20 px regular grey; CTA "Save" ≈20 px semibold white.
- Link value "cargoworld" ≈20 px medium in system blue — the only chromatic text.

## 4. Colour
| Hex | Role | Share (key frame) |
|---|---|---|
| #e8e9eb | stage backdrop behind device | 62% |
| #fdfdfd | sheet surface, white pills | 22% |
| #181210 | phone bezel, primary CTA, title | 4% |
| #3c3c3c | segmented-control track | — |
| #8e8e8e | placeholder / inactive labels | — |
| #1a7fd8 | link value | <1% |
| #79735e / #acbab7 | muted poster imagery | 8% |

WCAG checks (contrast.py):
- Title #111 on #fdfdfd: 18.56:1.
- CTA white on black: 21:1.
- Placeholder #8e8e8e on #fdfdfd: **3.22:1** (large-only pass).
- Link #1a7fd8 on #fdfdfd: **4.07:1** (fails AA at 20 px regular weight).
- Inactive "Boring" #9a9a9a on #3c3c3c track: 3.92:1.

All colour is delegated to the user's content; the chrome is greyscale plus one system blue.

## 5. Depth & material
- Sheet sits on the phone with no visible shadow; separation is by tone (#fdfdfd vs. a #f0f1f3 lower blur zone).
- A frosted, blurred band (≈40 px blur) behind the title area suggests the posters' reflection — material via backdrop blur.
- Posters have a faint 2–4 px shadow, enough to lift them off the dot grid.
- Segmented control: dark #3c3c3c track with a #1c1c1c inner thumb — inverted contrast against the white sheet.

## 6. Components & patterns
- **Segmented toggle** "Boring / Custom" — the playful label pair names the two layout modes.
- **Corner crop brackets:** four 12 px L-shaped 2 px black ticks on the selected poster's corners, instead of a full crop frame.
- **Contextual pill:** "⊕ Import" swaps to "Crop · Back · Front" when a poster is selected; same pill position, so the eye stays put.
- **CTA morph:** "Create" (default) becomes "Save" during an edit and returns to "Create" at loop end.
- Dot-grid canvas (≈1.5 px dots every ≈18 px) marks the area as a manipulable workspace.

## 7. Motion
Measured (m0_motion.json): 6.3 s at 60 fps, motion_fraction 0.22, seamless_loop_likely true, 5 segments with a median of 0.3 s.
- 1.00–1.30 s (0.30 s, peak 0.39, symmetric): tap — centre poster lifts, siblings blur out, pill cross-fades to the crop tools.
- 2.27–2.47 s (0.20 s, symmetric) and 3.17–3.53 s (0.37 s, peak 0.23, ease-out): crop/rotate adjustments of the poster.
- 4.13–4.47 s (0.33 s, peak 0.15, ease-out) and 5.33–5.53 s (0.20 s, ease-out): posters re-fan and the UI returns to "Import"/"Create".
All state changes land in 0.2–0.37 s with front-loaded energy — iOS-like spring decay; nothing lingers. Static holds of ≈1 s between moves give room to read.

## 8. Brand system
n/a — not a brand system. Identity cues: the cheeky "Boring / Custom" copy and the "cargoworld" placeholder collection name.

## 9. UX
- Mode is clear: one sharp object, everything else out of focus.
- The CTA rename tells the user they are now committing an edit, not creating the collection — good state signalling.
- "Back / Front" (z-order) next to "Crop" mixes geometry and layer commands in one pill; fine for three items, crowded beyond that.
- Risks: placeholder grey and link blue fall below AA; the side posters bleed off the sheet edge, which can read as a clipping bug.

## 10. Craft signals
- Siblings get opacity *plus* blur (≈30% / ≈6 px), not just fade.
- Crop affordance is only four 2 px corner ticks.
- Primary CTA label changes with mode (Create ↔ Save) at the same 130×58 px size, so nothing reflows.
- The tool pill occupies exactly the slot of the "Import" link it replaces.
- Only two radii: full pill for every control, ≈28 px for the sheet.

## 11. Reproduction recipe
```css
:root{--stage:#e8e9eb;--sheet:#fdfdfd;--ink:#111;--muted:#8e8e8e;--track:#3c3c3c;--thumb:#1c1c1c;--link:#0a6fd1;
  --r-sheet:28px;--spring:cubic-bezier(.2,.9,.25,1);}
.canvas{background-image:radial-gradient(#d4d4d8 1.5px,transparent 1.6px);background-size:18px 18px}
.poster{transition:transform .32s var(--spring),opacity .3s ease,filter .3s ease}
.stage[data-selected] .poster:not(.is-selected){opacity:.3;filter:blur(6px)}
.stage[data-selected] .poster.is-selected{transform:scale(1.08) rotate(-3deg)}
.poster.is-selected::before{content:"";position:absolute;inset:-8px;
  background:
   linear-gradient(#000,#000) top left/12px 2px, linear-gradient(#000,#000) top left/2px 12px,
   linear-gradient(#000,#000) bottom right/12px 2px, linear-gradient(#000,#000) bottom right/2px 12px;
  background-repeat:no-repeat}
.seg{background:var(--track);border-radius:9999px;padding:4px}
.seg [aria-pressed=true]{background:var(--thumb);color:#fff;border-radius:9999px}
.cta{background:#000;color:#fff;border-radius:9999px;height:58px;min-width:130px;font:600 20px/1 system-ui}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Calm greyscale chrome lets loud poster content carry colour; tidy centred stack. |
| Originality | 6 | Familiar iOS sheet idiom; the blur-out-siblings selection is the fresh touch. |
| Usability | 7 | Clear focus state and CTA relabel; secondary text and link miss AA. |
| Craft | 8 | Consistent pills, slot-preserving swaps, crisp corner ticks, tight 0.2–0.37 s timings. |

---
id: insp-orb-loom
source: inspora
category: Product
status: analyzed
title: "orbloom"
creator: "@rickybharti"
styles: [dark-premium, generative-particle, cinematic-3d, hairline-ui]
patterns: [voice-orb, audio-reactive-visual, preset-dropdown, settings-row-stack, range-slider-with-readout, hex-colour-field, collapsible-advanced-settings, privacy-microcopy]
mode: dark
palette: ["#0f0f0f", "#1d1d1d", "#424346", "#030305", "#101b2e", "#ffffff", "#8c8c8c"]
type_families: ["Inter / Geist-style neo-grotesk (likely)", "Geist Mono / SF Mono (values, likely)"]
type_class: [neo-grotesk, mono]
radius_px: [24, 14, 9999]
motion: {durations_s: [0.42, 0.27, 0.43, 1.73, 0.7], easing: [ease-out, ease-in], loop: false}
scores: {aesthetics: 8, originality: 7, usability: 7, craft: 8}
craft_signals: [chromatic-aberration-rim, mono-for-values, label-left-value-right-rows, single-surface-step-elevation, privacy-note-under-visual, swatch-beside-hex]
anti_patterns: [dim-placeholder-labels, demo-only-ui-no-state-feedback]
---
# orbloom — @rickybharti

## 1. Snapshot
- **Subject:** A 25.85 s, 2644×1594 (60 fps) recording of "Orbloom", a web playground for an audio-reactive "living orb" for voice UIs (credited as inspired by Grok voice). It pairs a preset picker, a product-state selector, a size slider and appearance colour fields.
- **Why it's remarkable:** The orb is a glass sphere holding a starfield/nebula. Its rim has an RGB **chromatic-aberration fringe** (red/green/blue specks at the edge), which makes a 2D shader read as real refractive glass. Presets swap whole "universes" (Blue 01 nebula, Orange 02 aurora band, Cyan 02 starfield, Pink 01).

## 2. Composition & layout
- **Column:** single-column, centred, about 920 px wide at key scale and about 1215 px real, on a near-black page. Large empty gutters, about 540 px each side, focus the eye.
- **Preview card:** about 920×500 px with radius about 24 px and fill #1d1d1d. It holds two small ghost pills top-right ("Stop microphone", "Remix") and a caption bottom-left.
- **Orb:** 280 px by its own readout and about 420 px displayed. It sits slightly above the card's centre.
- **Below the card:** a one-line description, then the "Controls" heading (~26 px), then settings rows about 64 px tall with a 12 px gap, then a collapsible "More settings" that reveals "Appearance" fields.

## 3. Typography
- Neo-grotesk (Inter/Geist feel) throughout:
  - "Controls" is about 26 px Medium, in white.
  - Row labels are about 20 px Regular in grey #8c8c8c.
  - Values ("Cyan 02", "Speaking") are about 20 px Regular in white, right-aligned beside a chevron.
- **Mono** is used for numeric and code values: "280 px" and "#101B2E", "#000000". It is a deliberate tool-UI signal.
- Captions are about 19 px in grey; the dropdown group labels ("NEBULA", "SPIRAL") are about 10 px caps with wide tracking.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #0f0f0f | page background | 82% |
| #1d1d1d | card / row surfaces | 15% |
| #424346 | slider track fill, borders | 2% |
| #030305 | orb interior | 1.5% |
| #101b2e | default "base colour" (navy) | swatch |
| #ffffff | values, headings, stars | — |
| #8c8c8c | labels | — |

WCAG checks:
- White on #1d1d1d: 16.9:1.
- Label #8c8c8c on #1d1d1d: 5.0:1 (pass).
- Caption #a3a3a3 on #0f0f0f: 7.6:1.
- Dim dropdown items (≈#6b6b6b): 3.16:1 (fails AA-normal).
- The slider track #424346 on #1d1d1d is 1.7:1, which is weak for a non-text UI component (it needs 3:1).

All hue lives in the orb; the UI is strictly achromatic.

## 5. Depth & material
- The orb has three layers:
  1. a dark interior with point stars plus soft nebula wisps;
  2. a Fresnel-like grey rim glow that brightens toward the edge;
  3. RGB-split specks on the circumference.
- A small white "comet" highlight with a trailing streak sits off-centre.
- The UI chrome is flat: elevation is one step (#0f0f0f → #1d1d1d) with no shadows or borders.

## 6. Components & patterns
- **Select rows:** a full-width pill-rect (radius about 14 px) with the label on the left and value plus chevron on the right. The open state reveals a grouped list ("NEBULA", "SPIRAL") with a ✓ on the active item.
- **Range slider:** a thick track (about 18 px) with a light-grey filled portion and a thin white tick thumb. The live readout "280 px" is shown in mono.
- **Hex field:** a mono hex value beside a 22 px rounded colour swatch.
- **Ghost pills:** small (about 11 px text) on #2a2a2a.
- **Privacy microcopy:** "microphone live · audio stays in this browser".

## 7. Motion
Measured: 25.85 s at 60 fps, `motion_fraction` 0.31, 20 segments with a median of 0.42 s, no loop.
- Most segments are short UI events:
  - Dropdown opens and closes are 0.27–0.47 s. Several are ease-out (peaks 0.04–0.07 at 7.80, 8.17 and 8.83 s), which is a fast-start snap.
  - The ease-in segments (0.43–0.47 s, peaks 0.73–0.75) correspond to list collapse and scroll.
- The longest segment is 14.50–16.23 s (1.73 s, peak 0.32, ease-out). This is the page scroll back up after expanding "More settings".
- The orb itself animates continuously (stars drift, nebula breathes and reacts to the microphone). Its energy sits below the threshold at the 280 px size, so the measure is dominated by UI changes.
- From frames, preset switches appear to cross-dissolve the orb in about 0.4 s rather than cutting.

## 8. Brand system
n/a — not a brand system. Identity cues:
- the starfield orb as the mark;
- the lowercase product voice ("a living orb for … all the moments in between");
- mono for values.

## 9. UX
- **Strengths:**
  - It is a clear playground. "Product state" (Speaking, plus presumably Listening and Idle) lets designers preview states, which is the key use case for a voice orb.
  - The microphone privacy note sits right under the visual, where the concern arises.
  - Advanced settings are progressively disclosed.
- **Risks:**
  - Grey labels and dim list items are borderline.
  - The slider track lacks contrast.
  - There is no visible mic-level meter, so the user cannot tell whether the orb is reacting to their voice.

## 10. Craft signals
- Chromatic fringe (R/G/B specks) only at the orb rim, a glass-lens cue.
- Values in mono ("280 px", "#101B2E") vs labels in sans.
- Every row has the same height (~64 px) and radius; the label/value split is consistent across select, slider and colour rows.
- The hex field pairs the code with a live swatch.
- The UI uses only two neutral steps (#0f0f0f / #1d1d1d), so the orb is the only colour on screen.

## 11. Reproduction recipe
```css
:root{--bg:#0f0f0f;--surface:#1d1d1d;--track:#424346;--text:#fff;--label:#8c8c8c;
  --r-card:24px;--r-row:14px;--font:"Geist","Inter",sans-serif;--mono:"Geist Mono",ui-monospace,monospace}
.orb{width:280px;aspect-ratio:1;border-radius:50%;
  background:radial-gradient(circle at 50% 50%,#030305 55%,#14141c 80%,#5a5a66 100%);
  box-shadow:inset 0 0 40px rgba(255,255,255,.15),0 0 0 1px rgba(255,255,255,.08);
  filter:drop-shadow(1px 0 0 rgba(255,0,80,.35)) drop-shadow(-1px 0 0 rgba(0,200,255,.35))}
.row{display:flex;justify-content:space-between;align-items:center;height:64px;padding:0 18px;
  background:var(--surface);border-radius:var(--r-row);color:var(--label)}
.row .val{color:var(--text)} .row .num{font-family:var(--mono)}
input[type=range]{accent-color:#bdbdbd;height:18px}
```
Starfield and nebula: a WebGL fragment shader (fbm noise + hashed point stars), with RMS from an `AnalyserNode` driving the brightness and drift speed.

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | A cosmic, glassy orb on a disciplined two-tone dark UI. |
| Originality | 7 | Voice orbs are common; the starfield-in-glass with RGB rim and multiple universe presets is a fresh variation. |
| Usability | 7 | A clear control model with state preview, though there is no input-level feedback and some contrast is low. |
| Craft | 8 | Consistent rows, mono values and a careful rim treatment. |

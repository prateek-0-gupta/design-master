---
id: insp-airport-matrix-time
source: inspora
category: Motion
status: analyzed
title: "Airport matrix time"
creator: "HASSCO© (@itshassco)"
styles: [x-dot-matrix-led, monochrome, minimal-swiss, hairline-ui]
patterns: [split-flap-scramble, dot-matrix-display, segmented-control, city-search-autocomplete, theme-colour-swatches, settings-flyout, floating-pill-chrome]
mode: mixed
palette: ["#181818", "#232323", "#343434", "#ffffff", "#2a2a2a", "#ebebeb", "#000000", "#595959"]
type_families: ["custom 5×7 dot-matrix (FIDS-style)", "Inter / SF Pro (likely) for chrome"]
type_class: [pixel, neo-grotesk]
radius_px: [9999, 24]
motion: {durations_s: [1.17, 0.1, 0.2, 1.13, 0.3], easing: [ease-in-out, ease-out], loop: false}
scores: {aesthetics: 8, originality: 7, usability: 7, craft: 8}
craft_signals: [unlit-dots-always-visible, fixed-cell-grid-padding, random-glyph-scramble-before-settle, chrome-in-four-corners, light-theme-inverts-dot-states, tabular-time-column]
anti_patterns: [unlit-cells-nearly-invisible-light-mode, settings-panel-overlaps-board]
---
# Airport matrix time — HASSCO©

## 1. Snapshot
- **Subject:** An 18.3 s, 1728×1080 recording of a world-clock web app that renders five city times as an airport FIDS (flight information display) board in a 5×7 dot-matrix face. It includes city search, a scramble animation and a light/colour theme switcher.
- **Why it's remarkable:** The board shows every *unlit* dot as a dim cell, so the fixed grid is always visible. Changes then read as real LED hardware updating, not text replacing text.

## 2. Composition & layout
- **Board:** about 1340×510 px (x 195–1530, y 270–780) centred on a #181818 canvas.
  - Columns: a 5-cell time column ("06:28", about 310 px), a gutter of about 85 px, then a 15-cell city column.
  - Row pitch is about 109 px. Each character cell is about 60×75 px with a 5×7 dot array: dot ≈9 px, pitch ≈12 px horizontal and ≈11 px vertical, cell gap ≈4 px.
- **Chrome:** four pill clusters sit in the corners at a 40 px inset:
  - top-left: a segmented control "Watch | Focus | World Time" (about 305×56) plus a palette button;
  - top-right: X/share and fullscreen circles (75 px);
  - bottom-left: "Clock | Map";
  - bottom-centre: a location pill "San Francisco · GMT-7";
  - bottom-right: the date "Sun, 04 Oct".
- The board owns the centre and the chrome never intrudes, except for the settings flyout (f7, f8).

## 3. Typography
- **Board:** a custom dot-matrix uppercase with square-ish 5×7 glyphs. Colon cells are narrower (about 25 px). Time digits are inherently tabular because of the cell grid.
- **Chrome:** a neo-grotesk (Inter or SF Pro) at about 18 px Medium for the active segment and Regular grey for inactive ones. Section labels in the settings ("SYSTEM PREFERENCES", "SOUND", "SUPPORT") are about 14 px uppercase with +0.04 em tracking in grey.

## 4. Colour
| Hex | Role | Share (dark) |
|---|---|---|
| #181818 | canvas | 77% |
| #232323 / #343434 | unlit dots | 13% |
| #ffffff | lit dots, active labels | 3% |
| #2a2a2a | pill surfaces | 2% |
| #ebebeb | canvas (light theme) | — |
| #000000 | lit dots (light theme) | — |
| #595959 | secondary labels (light) | — |

Theme swatches offered: white, black, mint (#d9f0c8-ish), yellow (#f6f39a-ish) and pale blue. Other colours are swatches only.

WCAG:
- Lit white on #181818 is 17.76:1, and black on #ebebeb is 17.62:1.
- Unlit dot #3a3a3a on #181818 is 1.56:1. This is intentional ghosting, and correctly far below text level.
- Inactive segment grey #8e8e8e on the #2a2a2a pill is **4.38:1 (just fails AA normal)**.
- Light-mode section labels #595959 on #ebebeb are 5.88:1.

## 5. Depth & material
- Completely flat. Pills are slightly lighter than the canvas (#2a2a2a vs #181818) with no shadow. In light mode they are white on #ebebeb with a faint shadow.
- The LED is suggested only by round dots. There is no bloom or glow, so it is "printed LED", restrained.

## 6. Components & patterns
- **City search:** a pill input at the bottom centre ("Type a city name…", f2). Typing "san" opens an autocomplete stack of pills above it, each with an icon, "City · Country" and "GMT±n" in grey (f3).
- **Selecting a city:** the last row is replaced (Tokyo → San Francisco).
- **Settings flyout (palette button):** Digital/FIDS segmented control, five colour swatches (selected = ring), Sound (Mute/System/Watch), a volume slider showing "100%", a "Buy me a coffee" button and a promo card.
- A Clock/Map view toggle.

## 7. Motion
The motion is measured: 18.28 s, 60 fps, motion_fraction 0.15, so the display is mostly at rest, as a clock should be.
- **1.17–2.33 s:** a 1.17 s symmetric segment, the initial board boot.
  - f0 shows only a "W" lit while the other cells are blank. Characters are revealed left to right.
- **5.53 s and 6.0 s:** 0.10 s and 0.20 s ease-out blips, which are search UI pops.
- **10.43–11.57 s:** a 1.13 s symmetric segment, the scramble.
  - f5 shows rows filled with random glyphs ("IF86T8VZ", "DUY1OMZGPQKJ") before each settles on its city name, the classic split-flap shuffle.
  - Rows resolve top to bottom (estimated from f5).
- **15.2–15.5 s:** a 0.3 s symmetric segment, the theme cross-fade from dark to light (f7 catches the mid-dissolve with both states visible).
- Minute ticks (28 → 29 at about 12.5 s) change only the affected digits.

## 8. Brand system
n/a — not a brand system. Identity cues: the FIDS dot-matrix as the signature, and monochrome pill chrome. "CO'WATCH!" appears as a sibling-product brand in settings.

## 9. UX
- **Strengths:** glanceable, high-contrast times, an obvious city search, and chrome pushed to the corners.
- **Weaknesses:**
  - The settings flyout overlaps the board (f8) instead of shifting it.
  - In light mode the unlit dots are nearly invisible (#e4e4e4 on #ebebeb), which loses the hardware illusion.
  - The time-zone offset is only shown for the selected city.

## 10. Craft signals
- Unlit dots render in every cell, including trailing padding to a fixed 15-character width.
- Scramble uses random alphanumerics per cell before settling (f5).
- Colon cells are narrower than digit cells, as on real FIDS boards.
- Four chrome clusters sit at an identical 40 px inset from each corner.
- The light theme inverts lit and unlit states rather than just swapping the background.
- Active segment = a lighter pill plus white text. Inactive = text only.

## 11. Reproduction recipe
```css
:root{--bg:#181818;--dot-off:#2e2e2e;--dot-on:#fff;--pill:#2a2a2a;--muted:#8e8e8e}
[data-theme=light]{--bg:#ebebeb;--dot-off:#dcdcdc;--dot-on:#000;--pill:#fff;--muted:#595959}
.cell{display:grid;grid-template-columns:repeat(5,9px);grid-template-rows:repeat(7,9px);gap:3px 3px;margin-right:4px}
.dot{border-radius:50%;background:var(--dot-off);transition:background .06s steps(1)}
.dot.on{background:var(--dot-on)}
.seg{display:flex;padding:4px;border-radius:9999px;background:var(--pill)}
.seg button{padding:10px 18px;border-radius:9999px;color:var(--muted);font:500 18px Inter}
.seg button[aria-pressed=true]{background:#3a3a3a;color:#fff}
```
```js
// scramble: each cell cycles random glyphs for 0.6–1.1s, staggered 60ms per row
const G="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
function scramble(cell,target,t0){const id=setInterval(()=>{cell.set(G[Math.random()*36|0])},45);
  setTimeout(()=>{clearInterval(id);cell.set(target)},t0);}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Strict monochrome with a beautiful dot-grid texture, and the chrome is quiet. |
| Originality | 7 | Split-flap and FIDS is a known idiom, but the unlit-dot grid and theme swatches give it a fresh treatment. |
| Usability | 7 | Highly legible times and clear search. The settings overlay and inactive-label contrast are weak spots. |
| Craft | 8 | Fixed-width cells, a narrow colon, random-glyph scramble and consistent 40 px corner insets. |

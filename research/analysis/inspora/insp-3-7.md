---
id: insp-3-7
source: inspora
category: Product
status: analyzed
title: "Flight Card"
creator: "@raul_dronca"
styles: [photo-led, grain-noise, glassmorphism]
patterns: [destination-photo-card, airport-code-pair, hand-drawn-flight-path, segmented-control-switcher, bottom-fade-scrim, photo-crossfade-on-switch]
mode: mixed
palette: ["#fafafa", "#3a656b", "#5a7771", "#2f5257", "#978560", "#b4a382", "#ffffff"]
type_families: ["SF Pro Display / Inter-style neo-grotesk (likely)"]
type_class: [neo-grotesk]
radius_px: [48, 14, 12]
motion: {durations_s: [0.6, 0.63, 0.67], easing: [ease-out, ease-in], loop: false}
scores: {aesthetics: 9, originality: 7, usability: 6, craft: 8}
craft_signals: [halftone-print-texture-on-photo, warm-scrim-matches-cloud-tone, squiggle-path-not-straight-arc, symmetric-left-right-columns, photo-tinted-card-shadow, hairline-divider-above-control]
anti_patterns: [secondary-city-labels-low-contrast, text-over-busy-photo]
---
# Flight Card — @raul_dronca

## 1. Snapshot
- **Subject:** A 14.4 s, 1920×1436 demo of a flight widget card. A two-option segmented control ("San Francisco" / "New York") swaps the route (CDG→SFO or LCY→JFK) and the hero photo (Golden Gate Bridge or Statue of Liberty).
- **Why it's remarkable:** The destination photos are treated like vintage risograph posters, with teal sky, orange clouds and a visible halftone/screen texture. This gives a data card the warmth of a travel poster.

## 2. Composition & layout
- The card is ≈748×985 px (x≈588–1337, y≈222–1208) centred on a #fafafa stage. Its corner radius is ≈48 px.
- **Title:** the city name is centred at the top (y≈297).
- **Landmark:** occupies the upper 60%. Its focal point (torch or bridge tower) sits off-centre-left so the title stays clear.
- **Data block:** starts at y≈830. Two mirrored columns (origin left-aligned at x≈636, destination right-aligned at x≈1290) hold code, time and city. A plane glyph with a hand-drawn squiggle path sits between them.
- **Footer:** a 1 px divider at y≈1042, then a segmented control ≈655×78 px with 48 px side insets that match the text columns.

## 3. Typography
- Neo-grotesk, close to SF Pro Display / Inter.
- **Airport codes:** ≈56 px Bold, caps, tight tracking (≈−0.02 em). These are the loudest element.
- **Times:** ≈36 px Medium. City names are ≈26 px Regular at ~75% white.
- **Title:** ≈38 px Medium white. The segment labels are ≈26 px Medium.
- **Scale:** 56 / 38 / 36 / 26. There are only three real steps.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #fafafa | stage | ~65% |
| #3a656b / #2f5257 | teal sky | ~7% |
| #5a7771 | sky mid / scrim | ~6% |
| #978560 / #b4a382 | ochre cloud / bottom scrim | ~5% |
| #ffffff | text, active segment | ~2% |
| #1a1a1a | active segment label | trace |

**WCAG:**
- White title on teal sky is **4.87:1** (pass).
- White times on the warm bottom scrim (#978560) are **3.6:1** (large only).
- City names (#d6d3c4-ish on #807d64) are **2.78:1** (fail).
- The inactive segment label (white on #8f8c78) is **3.39:1**.
- The active label #1a1a1a on white is **17.4:1**.

## 5. Depth & material
- The photo carries a halftone/fabric screen texture (fine diagonal crosshatch visible in the sky). Combined with the two-colour grading, it reads like print.
- The bottom ~40% has a warm ochre gradient scrim that fades the landmark into the data area. The scrim colour is sampled from the clouds, not a black overlay.
- **Segmented control:** a translucent frosted track (white at ~15% opacity with blur) holds a solid white thumb with a soft shadow.
- **Card shadow:** large and soft (~60 px blur), tinted by the photo's warm/teal colours, so the card glows slightly on the stage.

## 6. Components & patterns
- **Route block:** origin and destination columns are mirror-aligned, with the plane plus a wavy path in the middle. The path is a whimsical squiggle rather than a geodesic arc.
- **Segmented control:** two options, one white thumb, and labels that invert colour (dark on white, white on track).
- **Hero photo:** a crossfade tied to the control selection, so the content and the visual swap together.

## 7. Motion
**Measured** (`seamless_loop_likely: false`, first/last diff 12.3):
- **Duration:** 14.37 s, with a very low motion fraction of **0.13**.
- **Switch events:** three segments of 0.60–0.67 s. These are the switches:
  - 2.60–3.20 s (**0.60 s**, peak 0.03 → sharp ease-out): SF → NY.
  - 7.73–8.37 s (**0.63 s**, peak 0.66 → ease-in): NY → SF.
  - 11.97–12.63 s (**0.67 s**, peak 0.12 → ease-out): SF → NY.
- **From frames:**
  - The thumb slides between segments (at 11.97 s the thumb is mid-travel and empty of text).
  - The photo crossfades while the codes and times cross-dissolve in place. Layout does not shift.
  - The ~0.6 s photo fade is slower than the thumb (estimated ~0.3 s), which layers the change.

## 8. Brand system
n/a — not a brand system. Identity cues: a poster-like two-tone photo grade (teal + ochre) applied consistently to both cities, and a playful squiggle flight path.

## 9. UX
- The control both filters and switches the hero. The scope is clear and only two options are shown.
- **Strengths:** airport codes plus times are the primary information and they dominate.
- **Risks:** secondary city labels and the inactive segment are below AA. Text legibility depends on the scrim, so a lighter photo would break it. There is no date or flight number, so the card is a concept rather than a full boarding card.

## 10. Craft signals
- The divider and segmented control share the 48 px inset of the text columns.
- The landmark's focal element is placed off-centre so the centred title never overlaps it.
- The scrim colour is sampled from the cloud ochre (#978560), which avoids a muddy black gradient.
- Both cities get an identical grade, so the swap feels like the same poster series.
- The plane glyph sits at the peak of the squiggle, centred on the column gap.

## 11. Reproduction recipe
```css
:root{--stage:#fafafa;--teal:#3a656b;--ochre:#978560;--ink-on-photo:#fff;--ink-2-on-photo:rgba(255,255,255,.75);
  --r-card:48px;--r-seg:14px;--font:"SF Pro Display","Inter",system-ui,sans-serif;}
.card{width:748px;aspect-ratio:748/985;border-radius:var(--r-card);overflow:hidden;position:relative;
  box-shadow:0 40px 80px -20px rgba(58,101,107,.35),0 10px 30px rgba(151,133,96,.25)}
.card img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;
  filter:contrast(1.1) saturate(.9);transition:opacity .6s cubic-bezier(.2,.8,.2,1)}
.card::after{content:"";position:absolute;inset:0;
  background:linear-gradient(180deg,transparent 45%,rgba(151,133,96,.85) 85%),
             url(halftone.png);mix-blend-mode:normal}
.code{font:700 56px/1 var(--font);letter-spacing:-.02em;color:#fff}
.seg{display:grid;grid-template-columns:1fr 1fr;padding:6px;border-radius:var(--r-seg);
  background:rgba(255,255,255,.18);backdrop-filter:blur(16px)}
.seg .thumb{background:#fff;border-radius:12px;box-shadow:0 2px 8px rgba(0,0,0,.12);
  transition:transform .3s cubic-bezier(.3,.7,.2,1)}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 9 | The poster-grade photography plus restrained white type is beautiful and cohesive. |
| Originality | 7 | A familiar photo-card pattern, lifted by the print texture and squiggle path. |
| Usability | 6 | Clear primary data; secondary text and the inactive segment fail contrast. |
| Craft | 8 | Consistent insets, sampled scrim, layered transition timing. |

---
id: insp-mobile-gradient
source: inspora
category: Motion
status: analyzed
title: "Mobile Gradient UI"
creator: "@basit_designs"
styles: [minimal-swiss, gradient-mesh, grain-noise, editorial-serif]
patterns: [three-phone-showcase, inverse-radius-cutout-cards, product-catalogue-scroll, bracket-count-label, spec-chip-row, sticky-bottom-cta, vertical-name-index]
mode: mixed
palette: ["#fefefe", "#efefed", "#111111", "#130a0f", "#352b55", "#9d7b9a", "#b8bbb8", "#e2d6d5"]
type_families: ["Neue Haas Grotesk / Helvetica Now Display (likely)", "Inter (likely, small labels)"]
type_class: [neo-grotesk]
radius_px: [64, 40, 24, 12]
motion: {durations_s: [3.17, 6.57, 3.6, 13.88], easing: [ease-in-out, ease-in, ease-out], loop: false}
scores: {aesthetics: 9, originality: 8, usability: 6, craft: 8}
craft_signals: [inverse-corner-cutouts, bracket-numerals-as-meta, swiss-tight-caps-headline, light-dark-light-triptych, gradient-content-carries-all-colour, active-item-black-rest-grey]
anti_patterns: [white-labels-on-pastel-gradients, very-low-contrast-inactive-list]
---
# Mobile Gradient UI — @basit_designs

## 1. Snapshot
- **Subject:** A 13.9 s, 2998×2160 showcase of three phone screens for "Grainient" / "Canvick Gradient", a store selling 8K grain-gradient image packs; all three screens auto-scroll their gradient content in parallel.
- **Why it's remarkable:** The UI is pure Swiss monochrome and lets the product (glowing ring and ribbon gradients) supply 100% of the colour; the cards use concave "inverse radius" cutouts that make the gradients look poured into the frame.

## 2. Composition & layout
- Triptych on white #fefefe: three phones ≈ 775×1600 px (original) each, gutters ≈ 75 px, outer margin ≈ 265 px; frames have a pale 1–2 px outline and ≈ 64 px outer radius.
- **Phone 1 (light, cover):** micro-label top-left ("Human made designed / 8K Gradient collection") with "[40]" top-right; a horizontal media strip at mid-height with inverted-radius side notches; chip row "ULTRA HD · 8K · 40+"; brand lockup "CANVICK® GRADIENT" bottom-left ≈ 90 px caps.
- **Phone 2 (dark, hero):** full-bleed black with two glowing gradient rings scrolling; headline "DISCOVER GRAINIENT'S ECLIPTIC" in white caps ≈ 52 px, "[40]" aligned right.
- **Phone 3 (light, catalogue):** left column vertical name index (SPECTRA, OBSCURA active, SWIFTGLOW, ECLIPTIC, MANDARIN, DENZA) beside a right column of stacked image cards with concave joins; full-width black CTA "Explore collection" ≈ 625×85 px, 24 px radius.
- Light–dark–light arrangement gives the centre phone instant focal weight.

## 3. Typography
- Neo-grotesk with tight caps (Helvetica Now Display / Neue Haas-like): brand lockup ≈ 90 px, leading ≈ 0.9, tracking ≈ −0.02 em; hero headline ≈ 52 px caps, leading ≈ 0.95.
- Micro labels ≈ 18–22 px regular, sentence case; "[40]" bracket numerals as metadata (count of assets).
- Index list ≈ 20 px caps: active item #111, inactive ≈ #b8bbb8.
- Chips ≈ 20 px semibold black on white pills.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #fefefe | stage | 47% |
| #efefed | light screen surface | 24% |
| #130a0f / #260e16 | dark hero screen | 13% |
| #111111 | type, CTA | — |
| #352b55 / #9d7b9a | gradient content (violet, mauve) | 9% |
| #b8bbb8 | inactive list items | 4% |
| #e2d6d5 | warm card tint | 3% |

WCAG checks:
- Black type #111 on #efefed: 16.4:1.
- White headline on hero #130a0f: 19.5:1.
- White CTA label on #111: 18.9:1.
- **Inactive index items #b8bbb8 on #efefed: 1.68:1 (fails badly)**.
- "OBSCURA VISUALS ©" white over pink gradient ≈#e0a8d8: **1.95:1 (fails)**.

## 5. Depth & material
- Flat UI; all depth is inside the gradient imagery (blurred light rings with chromatic RGB edges, film grain, dithered banding).
- Inverse-radius notches (≈ 40 px concave corners) where a card meets the surface create a cut-paper, tab-like depth without shadows.
- Phone frames: white with a hairline grey rim and a soft 1–2 px shadow — mockups dissolve into the stage.

## 6. Components & patterns
- Bracketed counters "[40]", "[44]" as editorial metadata.
- Spec chips (ULTRA HD / 8K / 40+).
- Stacked catalogue cards with year "2026", product name with © and a one-line tagline ("A new spectrum has entered the room.").
- Vertical text index as a filter/scroll-spy (active black, rest grey).
- Sticky full-width black CTA.

## 7. Motion
Measured (m0_motion.json): 13.88 s, 60 fps, motion_fraction 0.95 (almost always moving), 3 segments, not seamless (first/last diff 13.5).
- **0.00–3.17 s (3.17 s), peak_at 0.44 → symmetric ease-in-out.**
- **3.30–9.87 s (6.57 s), peak_at 0.65 → ease-in**, building speed as the hero rings cycle hue (blue/violet → spectral → red, frames 3.86–10.03 s).
- **10.27–13.87 s (3.60 s), peak_at 0.11 → ease-out**, a fast scroll that settles.
- All three phones scroll their media at once (phone 1 strip horizontally, phones 2–3 vertically); the chrome (type, chips, CTA) stays fixed, so the motion reads as "content flowing under a static frame". Brief pauses ≈ 0.13–0.4 s between segments.

## 8. Brand system
n/a — not a brand system, but identity cues are strong: "®" and "©" marks used decoratively, bracket numerals, all-caps tight grotesk lockups, and named gradient series (Spectra, Obscura, Ecliptic…) as product SKUs.

## 9. UX
- Clear storefront flow: cover → hero collection → catalogue with one CTA.
- Product imagery is legitimately the content, so letting it dominate is right.
- **Risks:** inactive index items are nearly invisible (1.68:1); white product titles over pale pink/peach gradients fail; micro labels at ≈ 9 pt equivalent are tiny.

## 10. Craft signals
- Concave cutout radius matches the card radius (≈ 40 px) so joins look continuous.
- "[40]" counters align to the same top-right baseline across phones 1 and 2.
- Headline and lockup share one cap style and tight leading (~0.9–0.95).
- The only black filled element on the light screens is the CTA — single primary action.
- Hero ring hue changes between frames yet the frame chrome never shifts by a pixel.

## 11. Reproduction recipe
```css
:root{--stage:#fefefe;--surface:#efefed;--ink:#111;--muted:#b8bbb8;--dark:#130a0f;--r-card:40px;--r-btn:24px;
  --font:"Helvetica Now Display","Neue Haas Grotesk Display",Inter,sans-serif}
.lockup{font:700 44px/.9 var(--font);letter-spacing:-.02em;text-transform:uppercase;color:var(--ink)}
.meta{font:400 11px/1.25 var(--font)} .count::before{content:"["} .count::after{content:"]"}
.chip{background:#fff;border-radius:6px;padding:2px 6px;font:600 10px var(--font)}
.index li{color:var(--muted);text-transform:uppercase} .index li[aria-current]{color:var(--ink)}
/* inverse-radius cutout */
.card{position:relative;border-radius:var(--r-card)}
.card::before{content:"";position:absolute;left:-40px;top:0;width:40px;height:40px;
  background:radial-gradient(circle at 0 100%,transparent 40px,var(--surface) 40.5px)}
.cta{background:var(--ink);color:#fff;border-radius:var(--r-btn);height:44px;width:100%}
.feed{animation:scroll 14s cubic-bezier(.45,0,.55,1) infinite alternate}
@keyframes scroll{to{transform:translateY(-60%)}}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 9 | Rigorous Swiss chrome against luminous gradients; balanced triptych. |
| Originality | 8 | Inverse-radius cutouts and bracket metadata feel fresh in a store UI. |
| Usability | 6 | Clear flow and CTA, but grey index and pastel overlays fail contrast. |
| Craft | 8 | Consistent radii, baselines and type rhythm across three screens. |

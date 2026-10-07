---
id: bg-frame-io
source: brandguidelines
category: guideline
status: analyzed
title: "Frame.io Brand Style Guide (October '22)"
creator: "Frame.io (In-house, Adobe)"
styles: [dark-premium, aurora-glow, photo-led, minimal-swiss]
patterns: [bold-lead-in-grey-body, optical-centering-rule, clearspace-half-symbol-height, named-gradient-presets, mark-shaped-spotlight-glows, cast-light-from-image, proportional-palette-stripes, rounded-card-mockup-grid]
mode: dark
palette: ["#000000", "#5b53ff", "#ffffff", "#47ebeb", "#8952fd", "#fc856d", "#0d0d18", "#a3a4bf"]
type_families: ["Frame Gothic (Thin, ExtraLight, Light, Regular, Medium, SemiBold, Bold, UltraBold, Italic — embedded)", "Frame Gothic Display (embedded)"]
type_class: [neo-grotesk, display]
radius_px: [16, 9999]
motion: null
scores: {aesthetics: 9, originality: 8, usability: 6, craft: 7}
craft_signals: [optical-center-at-second-bar, x-equals-symbol-height-over-2, palette-stripe-width-encodes-share, 19-step-cool-grey-ramp, light-dark-variants-per-hue, spotlight-files-spv-sph-naming, core-weights-highlighted-in-specimen, four-column-footer-breadcrumb]
anti_patterns: [electric-hex-conflict, seven-digit-hex-grey-00, wrong-breadcrumb-p3, cobalt-text-on-black-4.13, no-type-scale-or-sizes]
---
# Frame.io Brand Style Guide — Frame.io / Adobe in-house

## 1. Snapshot
- **Subject:** a 53-page, 1920×1080 pt (16:9) style guide from October 2022 for Frame.io, the Adobe-owned video review platform. It covers mission and principles, voice, the symbol and wordmark, colour, Frame Gothic type, a "Light" system, photography and composite applications.
- **Why it's remarkable:** the brand idea, film light, is turned into graphic rules. There are three named lighting treatments (cast light, spotlights, area lighting), and the glows are cut in the shape of the logo's arrow terminal. Every page is black, so colour reads as projected light.

## 2. Composition & layout
- **Chrome:** every content page shares one frame. The left margin is 58 px on the 1400 px render (about 4% of width). Copy sits top-left at y ≈ 65 px. A four-column footer at y ≈ 733 px holds:
  1. the symbol (about 16 px);
  2. a breadcrumb such as "Foundations / Logo" at x ≈ 383;
  3. "Brand Style Guide — October '22" at x ≈ 707;
  4. "© 2022 Adobe Inc." at x ≈ 1032 and the folio at x ≈ 1336.
  This is a tidy 4-column grid set in about 9 px grey text.
- **Content pages** use a 1:2 split. The text column runs about 58–430 px and the figure field about 492–1342 px. Figures sit in rounded cards (radius about 16 px at 1400 px) filled with Grey 05 #0D0D18 (sampled #0d0d17, 41.6% of p22).
- **Section openers** (p1, p3, p10, p33) are full-bleed gradient fields. A Display headline sits top-left at about 120 px on the render; "Brand Style Guide" on the cover is about 150 px cap-to-baseline per line, at about 0.95 leading.
- **Statement pages** (p4, p11, p53) set a 3–4 line declaration at about 40 px from the centre-right column (x ≈ 700). Photo pages (p6–9, p40–42, p52) run images full-bleed or in rounded crops.

## 3. Typography
- **Embedded (pdffonts):** FrameGothic Thin, ExtraLight, Light, Regular, Medium, SemiBold, Bold, UltraBold and Italic, plus FrameGothic-Display and FrameGothicDisplay. It is a proprietary neo-grotesk: compact apertures, a single-storey "a" in Display, a squarish "G".
- **Specimens** (p30–32): nine weights from Thin to Black, plus italics and the Display cut, which is "strategically spaced" for headlines. In the specimens Regular, Medium, SemiBold and Bold are white while Thin, UltraLight, Light, UltraBold and Black are dimmed to grey. That visually marks Regular–Bold as the working range, although the text never says so.
- **House paragraph style:** a white bold-ish lead-in phrase ending in a full stop, followed by grey #A3A4BF-ish body ("**Centering.** When centering the mark…"). It is about 20 px on 1400 (≈27 pt on the 1920 pt page) with leading of about 1.25. This one device carries the whole document.
- **Gaps:** no size scale, leading or tracking values. Italics are "accent and emphasis, used sparingly". The "UltraLight" in the specimen versus "ExtraLight" in the font file is a naming mismatch.

## 4. Colour
| Hex | Role | Share (p24 stripe widths) |
|---|---|---|
| #000000 Black | canvas ("black space to cinematically highlight content") | 33% |
| #5B53FF Cobalt | primary brand hue, secondary logo colour | 33% |
| #FFFFFF White | type, logo | 8% |
| #47EBEB Electric | accent | 8% |
| #8952FD Iris | accent | 8% |
| #FC856D Coral | accent | 8% |
| #0D0D18 (Grey 05) / #161722 (Grey 10) | card surfaces | — |
| #A3A4BF (Grey 70) | body copy | — |

- **Extended palette (p25):** light, base and dark for each hue: Cobalt #6369FF / #5B53FF / #5237F9; Iris #9F75F9 / #8952FD / #632CDA; Coral #FCA493 / #FC856D / #E36B52. The extended palette "should never be used as primary applications".
- **Electric conflict:** p25 lists both Electric Light and Electric as #87FFFF and Electric Dark as #00B8B9, while p24 gives Electric as #47EBEB.
- **Grey ramp (p27):** 19 cool greys, Grey 00 → Grey 100: #0D0D18, #12131D, #161722, #1D1F2C, #252736 … #D5D6EA, #E8E9F3, #F5F5F8, #FCFCFC. All are blue-tinted. Grey 00 is printed as "#0000000" (seven digits).
- **Gradients (p26):** four named presets on 45° pills: Santa Monica (coral → magenta → blue), Tribeca (violet → coral), Miami (electric → cobalt → iris), Gotham (graphite → black).

WCAG:
- White on black: 21:1.
- #A3A4BF body on black: 8.62:1; on #0D0D18 cards: 7.92:1.
- White on Cobalt: 5.09:1. White on Iris: 4.48:1 (just fails AA body).
- Cobalt on black: **4.13:1** (fails body; Cobalt Light #6369FF reaches 5.0:1, which explains the "accessibility" tints).
- Electric on black: 14.35:1. Coral on black: 8.71:1.
- Grey 50 #6A6B83 on black: 4.04:1. Grey 40 #4F5167: 2.71:1.

## 5. Depth & material
Depth comes entirely from light:
- **Cast light** (p35): an image's dominant colour bleeds outward as a soft radial glow beyond its rounded frame, with stacked offset cards behind it. Sampled colour chips in pin-shaped markers show where the glow colour comes from.
- **Spotlights** (p36–37): eight blurred blobs shaped like the mark's arrow terminal, in vertical (SPV01–04) and horizontal (SPH01–04) sets named Cobalt, Coral, Vibrance and Hendrix. The edges are sharp on one side and diffuse on the other.
- **Area lighting** (p38): glowing slabs of extruded glass for campaigns (e.g. "4KUHD").
- **Grain:** a noise texture on one spotlight card (p36).

## 6. Components & patterns
- **Symbol:** four vertical bars of decreasing height ending in a rounded play-arrow, a waveform that doubles as a play button.
- **Variants (p13):** white on dark, black on light, and Cobalt on light. **Lockup** (p17): symbol plus lowercase "frame.io" wordmark; white and black are primary, the Cobalt-symbol versions secondary.
- **Adobe co-brand** (p19–20): "An Adobe Company" sits under the wordmark, on request only.
- **Property and partner lockups** (p21): "frame.io insider" with the property name in a lighter weight; partners separated by a hairline divider (FUJIFILM, RED).
- **Misuse** (p22): four "DON'T" cards with outlined Cobalt pill tags: wordmark without symbol, stacked lockup, gradient logo, altered proportions.
- **Application cards** (p44–51): rounded dark UI cards (version management, comments with an "Approved" chip, persona tiles), a phone mock-up, social stories, a lightbox sign and the Ae/Pr/Frame app-icon trio.

## 7. Motion
None specified. The PDF has no timings, but the gradients, spotlights and "cast light" read as stills of moving light.

## 8. Brand system
**Mission and principles (p3–9).** The mission is "Empower the world's storytellers." Four principles each get one photo page:
- Undeniable;
- Premium;
- Professional;
- Cinematic.

Each is written as a bold word followed by a two-line gloss.

**Voice (p11).** "Clear. Concise. Confident. Authentic." Keep it short, and speak to professionals who "trust our platform with their life's work". There are no do/don't samples.

**Logo rules (p12–22).**
- **Optical centring (p14):** when centring the symbol, place the metric centre on the right edge of the second bar to compensate for the "arrow effect". A dashed Cobalt guide shows it. This is the most transferable logo rule in my batch.
- **Clear space:** X = symbol height ÷ 2 for both the symbol alone (a 3×3 grid with X cells) and the wordmark lockup.
- **Missing:** no minimum size.
- **Wordmark:** used for audiences outside the "immediate ecosystem"; the symbol alone is gaining standalone recognition.

**Colour logic.** Black is a third of the system and Cobalt another third. Four accents share the final third equally, and the stripe widths on p24 encode exactly that. Gradients mix only palette hues, and greys are tinted toward Cobalt.

**Light as a brand pillar (p34–38).** "We use lighting in three distinct ways": cast (from content), spotlights (from the mark) and area (bespoke campaign worlds). Each has an output naming scheme.

**Photography (p39–42).** "Aspirational storytelling": behind-the-scenes creators at work (colourists, camera operators, editors), low-key and motivated light, teal and amber grading.

**Document structure (Index p2):**
1. Cover, p1
2. Index, p2
3. 01 Mission, p3–9: mission statement p3–4, principles p5–9
4. 02 Foundations, p10–32:
   - Voice & Tone, p11
   - Logo, p12–22
   - Color, p23–27
   - Type, p28–32
5. 03 Platform, p33–52:
   - Light, p34–38
   - Brand Photography, p39–42
   - Putting It All Together, p43–52
6. 04 Contact ("That's a wrap."), p53

**Small errors:**
- the breadcrumb on p3 reads "Platform / Brand Photography";
- "workdmark" (p22);
- "nd cobalt" (p17);
- the Electric hex conflict;
- the seven-digit Grey 00.

**Tokens worth stealing:**
- optical-centre offset for asymmetric marks;
- X = ½ symbol height;
- a blue-tinted 19-step grey ramp with numeric names (05, 08, 10, 12, 15…);
- light/base/dark per accent;
- named gradient presets;
- glows shaped from the logo instead of generic blobs.

## 9. UX
It is very easy to read: one paragraph style, one frame, generous black space, and a breadcrumb plus folio on every page. A designer gets the mood and the logo mechanics right away. They will miss:
- a type scale or any sizes;
- logo minimum sizes;
- gradient stop values and angles;
- spotlight blur radii;
- guidance on when to use which accent.

The main text accent, Cobalt on black, fails AA body contrast.

## 10. Craft signals
- Optical centring on the right edge of the second bar, shown with a dashed Cobalt guide (p14).
- Clear space X = symbol height / 2, drawn as a 3×3 grid with "×" markers in the corner cells (p15, p18).
- Palette stripe widths are proportional: black and Cobalt about 283 px each, four accents about 70 px each at 1400 px (p24).
- A 19-step cool grey ramp, each step with hex and RGB (p27).
- Spotlight assets are coded SPV01–04 and SPH01–04 with colour names (p37).
- The specimen dims non-core weights, so emphasis is shown rather than stated (p30).
- The four-column footer sits on the same x positions on every page.

## 11. Reproduction recipe
```css
:root{
  --black:#000; --cobalt:#5b53ff; --cobalt-light:#6369ff; --cobalt-dark:#5237f9;
  --electric:#47ebeb; --iris:#8952fd; --coral:#fc856d; --white:#fff;
  --g05:#0d0d18; --g10:#161722; --g20:#2e2f40; --g50:#6a6b83; --g70:#a3a4bf; --g90:#dedfee;
  --font:"Frame Gothic","Inter",system-ui,sans-serif;
  --r-card:16px;
}
body{background:var(--black);color:var(--g70);font:400 1.25rem/1.25 var(--font)}
p b{color:var(--white);font-weight:500}           /* "Lead-in. grey body" */
.card{background:var(--g05);border-radius:var(--r-card)}
.display{font:500 clamp(3rem,9vw,9rem)/.95 var(--font);color:var(--white);letter-spacing:-.02em}
.grad-santa-monica{background:linear-gradient(225deg,var(--coral),#c05cff 50%,var(--cobalt-light))}
.grad-miami{background:linear-gradient(225deg,var(--electric),var(--cobalt) 50%,var(--iris))}
.cast-light{position:relative}
.cast-light::before{content:"";position:absolute;inset:-12%;z-index:-1;
  background:radial-gradient(closest-side,rgb(196 140 70 / .45),transparent);filter:blur(40px)}
.spotlight{width:240px;aspect-ratio:3/4;border-radius:40% 60% 50% 30%/30% 50% 50% 40%;
  background:linear-gradient(180deg,var(--cobalt-light),var(--iris));filter:blur(24px)}
.logo-center{transform:translateX(var(--optical-offset,-6%))} /* centre on 2nd bar's right edge */
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 9 | A cinematic black canvas, glowing palette, superb photography and a disciplined single-template layout. |
| Originality | 8 | "Light" as a codified system (cast, spot, area) with mark-shaped glows is a fresh, ownable device. |
| Usability | 6 | Clear logo mechanics and full colour specs, but no type sizes, minimum logo size or gradient/glow parameters. |
| Craft | 7 | Optical-centring and proportional palette pages show real care. Hex conflicts, a wrong breadcrumb and typos pull it down. |

---
id: bg-make
source: brandguidelines
category: guideline
status: analyzed
title: "Make"
creator: "In-house"
styles: [corporate-clean, maximalist-color, organic-blob]
patterns: [gradient-logomark, one-colour-logo-on-photo, logo-background-matrix, x-height-clearspace-box, partner-lockup-divider, gradient-palette-ramp, misuse-grid-3x4]
mode: light
palette: ["#6d00cc", "#31005c", "#f5f0f0", "#ff00ff", "#b02de9", "#00d9ee", "#ed5144", "#000000"]
type_families: ["Baton Turbo (embedded: Regular, Medium, Bold)", "Inter (specimen only, not embedded)"]
type_class: [grotesk, neo-grotesk]
radius_px: []
motion: null
scores: {aesthetics: 6, originality: 4, usability: 6, craft: 4}
craft_signals: [gradient-defined-per-bar, print-and-screen-min-sizes, logo-on-12-backgrounds, cmyk-rgb-pantone-triplets, light-and-dark-mode-backgrounds, consistent-slide-chrome]
anti_patterns: [specimen-mislabelled-italic, typo-in-min-size, min-size-aspect-wrong, palette-ramp-without-usage-rules, no-type-scale, no-imagery-chapter]
---
# Make — In-house

## 1. Snapshot
- **Subject:** A 15-slide, 1920×1080 pt PDF dated March 2023 for Make, the visual automation platform (formerly Integromat). It covers the logo, two typefaces and colour, and nothing else.
- **Why it's remarkable:** It isn't, as a system. The useful parts are the three-stop gradient logomark specified bar by bar, the 12-cell matrix of approved logo backgrounds, and the explicit light-mode and dark-mode background colours (#F5F0F0 / #31005C).

## 2. Composition & layout
- Every interior slide uses the same chrome. A purple headline sits top-left at x≈68/1400 px (≈93 pt), with body copy below in a narrow column about 310 px wide (~425 pt, roughly 22% of the width). The demonstration sits in the right ~60% starting at x≈530–620 px. A 1 px black rule at y≈710/788 runs the full live width, with "Make Brand Guidelines" bottom-left and the press URL bottom-right.
- Margins are about 68 px left and right of a 1400 px render (~93 pt, i.e. ~4.8% of width).
- The cover (p1) is the only expressive slide. It is #31005C deep violet with three cropped "liquid" blob shapes in gradients (coral→violet top, violet→lilac right, cyan→violet bottom-left) and a stacked 3-line white title at about 85 px cap height (~115 pt type).
- Density is very low. Most slides are ~85–93% white (palette.json: #ffffff 78–93%).

## 3. Typography
- **Embedded (pdffonts):** `BatonTurbo-Bold`, `BatonTurbo-Medium` and `BatonTurbo-Regular`, all Type 3. Baton Turbo is the only face actually used for setting text.
- **Primary typeface (p12):** Baton Turbo, praised for its "semi narrow" proportions. The specimen lists 10 styles: Heavy, Heavy Italic, Bold, Bold Italic, Medium, Medium Italic, Book, Book Italic, Regular, Italic. The last line, labelled "Italic", is rendered upright with collapsed word spacing, so the specimen contains a visible error.
- **Secondary typeface (p13):** Inter, described as rational and readable, shown in 9 weights from Black to Thin. It is not embedded, so the specimen is outlined artwork.
- **Hierarchy in use:** headlines are Baton Turbo Bold in #6D00CC at about 40 px per line on the 1400 px render (≈55 pt) with leading of about 1.0. Body is Baton Turbo Regular in black at about 16 px (≈22 pt) with leading of about 1.5. Captions on the misuse grid are about 10 px (≈14 pt).
- No type scale, pairing rules, tracking or role assignment (when Inter rather than Baton) is given.

## 4. Colour
| Hex | Role | Approx share |
|---|---|---|
| #6D00CC | "Dark Violet", primary; headlines, app icon, solid logo tile (Pantone 2090 U) | 4–10% of interior slides |
| #31005C | dark-mode background; cover field | 61% of cover |
| #F5F0F0 | light-mode background (warm off-white) | — |
| #FF00FF / #B02DE9 / #6D00CC | three logo-gradient stops, one per bar (Pantone 239 U / 7441 U / 2090 U) | logo only |
| #E657FF, #E38EFF, #B55DCD, #724EBF, #4000CC | secondary palette, violet family | accents |
| #FF009A, #00D9EE, #ED5144 | secondary palette, pop accents (magenta, cyan, coral) | accents |
| #000000 / #FFFFFF | logotype, body text, page | 78–93% white |

On p15 every secondary colour is paired with a gradient swatch that runs from that colour into the #6D00CC primary. In effect the palette is "anything → Dark Violet". p4 gives the three logo stops in CMYK, RGB and Pantone.

palette.json cross-check: #6d00cd (p5, p11), #31005c (p1, 60.6%), #e540f5 / #a441e1 / #6221c4 on the gradient bars (p4). The sampled bar values are lighter or darker than the spec because of the in-bar gradient.

WCAG (contrast.py):
- #6D00CC on white: **8.33:1**. On #F5F0F0: **7.38:1**.
- White on #31005C: **16.34:1**.
- Black on #00D9EE: **12.16:1** (the doc correctly uses the black logo on cyan).
- White on #ED5144: **3.58:1**. White on #FF00FF: **3.14:1**. Both are large-text only, yet the white logo is approved on the coral tile.
- White on #E657FF: **2.93:1** (fails). White on #B02DE9: 4.77:1.

## 5. Depth & material
The system is flat. The only material effect is the soft linear gradient inside each logomark bar and the cover blobs. There are no shadows; "do not add shadows" is an explicit misuse.

## 6. Components & patterns
- **Logo (p3):** the symbol is three rounded bars leaning progressively less (≈30°, ≈10°, 0°), like falling dominoes or an "m". The logotype is lowercase "make" in a heavy grotesk. Bar corner radius is about 6 px on a ~300 px-tall bar (≈2%).
- **Signatures (p5):** primary is full colour on white, or white on #6D00CC. Secondary is black, or white on black.
- **Background matrix (p6):** a 3×4 grid of approved backgrounds: black, gradient, night photo, off-white, white, sand photo, coral, two violet gradients, cyan, cobalt→cyan gradient and violet. The one-colour logo goes on colours and photos; the full colour logo goes on light flat fields.
- **App icon (p11):** white symbol on a #6D00CC square. Don't use the gradient symbol as an icon, and don't use the icon as a social avatar.
- **Partner lockup (p10):** Make logo, X gap, 1 px vertical rule, X gap, partner logo. Both logos should "feel of equal size", and the lockup is approved-partnerships only.

## 7. Motion
n/a. This is a static PDF with no motion guidance.

## 8. Brand system
**Logo rules**
- Use only the supplied files; never recreate the logo.
- **Clearspace (p7):** X = height of the "k" ascender, applied on all four sides. It is drawn as a 3×3 grid with a #E657FF "X" swatch.
- **Minimum sizes (p8):**

  | Version | Screens | Laser | Inkjet / print |
  |---|---|---|---|
  | Main | "40x47px" | 1.7×0.6 cm (printed as "1,7x06cm") | 2.3×0.8 cm |
  | Symbol | 10×16 px | 0.43×0.7 cm | 0.49×0.8 cm |

  The 40×47 px screen figure cannot be right for a ~3.4:1 horizontal logo, so read it as a typo. A dedicated small-size version is said to exist below 9 px, but the slide shows it identical to the main logo.
- **Misuse (p9, 12 cases in a 3×4 grid):** distort, outline, change typeface, non-corporate colour, additional colour, added elements, shadow, clear-space breach, framing in a shape, changed symbol-to-logotype ratio, image or pattern fill, rotation. Each is shown with a pink X.

**Colour logic:** a single primary, a dark-mode ground and a light-mode ground, plus 9 secondary colours that must be "mixed as per addressed here". In practice that means gradients into #6D00CC only. This is the most transferable decision: every accent has exactly one sanctioned gradient partner.

**Voice and tone:** none, beyond a press boilerplate paragraph (p2: visual platform for building and automating without code, 500,000+ organisations).

**Imagery and graphic devices:** there is no chapter. The cover blobs and two stock photos (city at night, desert) on p6 are the only clues.

**Document structure (15 pp.)**

| # | Chapter | Pages |
|---|---|---|
| 0 | Cover | 1 |
| 1 | Boilerplate | 2 |
| 2 | Logo: concept, gradient, signatures (×2), safe zone, scale, misuse | 3–9 |
| 3 | Partner lockups | 10 |
| 4 | App icon | 11 |
| 5 | Typography: primary (Baton Turbo), secondary (Inter) | 12–13 |
| 6 | Colour: main colour, corporate colours | 14–15 |

**Token decisions worth stealing**
- Name the light and dark canvases as tokens (`#F5F0F0`, `#31005C`) rather than defaulting to #FFF and #000. The dark ground is the primary hue at about 45% lightness.
- Give each secondary hue a single gradient into the primary, which caps the combinations at 9.
- Specify the logo gradient per bar rather than as one sweep, so each bar keeps a dominant stop.

## 9. UX
A press or partner user can find logo files, the safe zone and colour codes in under a minute: 15 slides, one idea each. A designer building anything beyond a logo placement gets no type scale, no layout grid, no imagery, no iconography and no examples. The typo'd sizes and the mislabelled specimen weaken trust in the numbers.

## 10. Craft signals
- Every slide shares identical chrome: a headline at x≈68 px, a 1 px footer rule at y≈710/788 and the same footer text left and right.
- Colours are given as HEX, RGB, CMYK and Pantone U for the logo stops (p4) and HEX, RGB and CMYK for the 9 secondaries (p15).
- Logo background guidance is shown on 12 real backgrounds, including 2 photos, not just described.
- The coral tile (#ED5144) carries a white logo at 3.58:1, acceptable only because the logo is large.
- Errors: "1,7x06cm", "40x47px" for a horizontal logo, an upright "Italic" specimen, "aditional", "to don't lose".

## 11. Reproduction recipe
```css
:root{
  --make-violet:#6d00cc;      /* primary, Pantone 2090 U */
  --make-bg-light:#f5f0f0;
  --make-bg-dark:#31005c;
  --make-magenta:#ff00ff; --make-orchid:#b02de9;   /* logo stops */
  --make-pink:#e657ff; --make-lilac:#e38eff; --make-mauve:#b55dcd;
  --make-iris:#724ebf; --make-indigo:#4000cc; --make-hot:#ff009a;
  --make-cyan:#00d9ee; --make-coral:#ed5144;
  --font-display:"Baton Turbo","Inter",system-ui,sans-serif;
  --font-ui:"Inter",system-ui,sans-serif;
}
/* every accent may only fade into the primary */
.grad-cyan {background:linear-gradient(90deg,var(--make-cyan),var(--make-violet));}
.grad-coral{background:linear-gradient(90deg,var(--make-coral),var(--make-violet));}
.slide{background:#fff;padding:0 4.8vw;}
.slide h2{font:700 2.9vw/1.0 var(--font-display);color:var(--make-violet);}
.slide p{font:400 1.15vw/1.5 var(--font-display);max-width:22vw;}
.slide footer{border-top:1px solid #000;display:flex;justify-content:space-between;font-size:.8vw;}
.mark-bar{border-radius:6px;background:linear-gradient(160deg,#ff00ff,#e540f5);}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 6 | Strong violet cover and gradient mark, but interior slides are plain template pages. |
| Originality | 4 | Standard logo-colour-type press kit. The gradient-to-primary rule is the only distinctive idea. |
| Usability | 6 | Fast to apply for logo placement and partner lockups; nothing on layout, imagery or voice. |
| Craft | 4 | Consistent chrome, but sizing typos, an impossible min size and a wrong specimen line. |

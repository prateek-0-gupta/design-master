# Brand-system anatomy

Based on 61 analysed brand documents: 21 PDFs (20 downloaded, one captured page by page from Dropbox's viewer), 31 live, hosted or archived sites, 2 Figma prototypes and 9 templates, of which 4 failed. The best-scored documents:

| Document | Score (of 40) |
|---|---|
| bg-olympic (Hulse & Durrell) | 35 |
| bg-edp (Pentagram) | 34 |
| bg-red-hat | 33 |
| bg-instacart (Wolff Olins) | 33 |
| bg-hulu (DixonBaxi) | 33 |
| bg-ibm | 32 |
| bg-odido | 32 |
| bg-seat-geek | 31 |

The weakest were bg-make (20), bg-instagram (21), bg-naseem-al-faihaa (22) and bg-northalley (23). Median guideline score: craft 7, usability 7.

## 1. The canonical chapter order (what the best documents converge on)

| # | Chapter | Present in top docs | Typical share of pages | What "complete" means |
|---|---|---|---|---|
| 0 | Cover, welcome, contents, how to use | all | 3–5% | A contents page with live links (Dubai: 65 internal links; Hulu numbers chapters 1.0–3.0) |
| 1 | Strategy: purpose, vision, values, positioning, personality | Olympic p6–7, EDP p5–20, Slack p5–15, Frame.io p3–9 | 8–15% | Personality as "we are X, never Y" pairs (Slack's seven pairs) or 4–6 attributes with one-line definitions (EDP) |
| 2 | Voice & tone | EDP p21–25, Slack, Twitch 3×2 tone matrix, Hulu's volume dial | 3–8% | Mechanical rules (numbers, currency, dates, naming, banned words), not just adjectives |
| 3 | Logo | all | 10–20% | Construction geometry, clearspace from the mark's own anatomy, min size in px and mm, colourways, backgrounds matrix, misuse grid (usually 9 tiles), co-branding |
| 4 | Colour | all | 6–12% | Roles, proportions (60/30/10 or %), HEX/RGB/CMYK/Pantone, tints, **approved pairs with contrast ratios** |
| 5 | Typography | all but weak docs | 6–10% | Families + fallbacks, a named scale with size/leading/tracking, localisation and non-Latin scripts |
| 6 | Graphic device / supergraphic | Hulu "Vessel" p58–73, EDP spiral, New Breed "loudline", Kia diagonal | 8–15% | The device as formulas (radius = shortest edge ÷ 6, stroke = longest ÷ 100), crop rules (≥ 55% visible), "once per spread" limits |
| 7 | Imagery: photo, illustration, iconography, pictograms | Olympic p69–78, Red Hat icons, Frame.io "light" | 10–15% | Casting and diversity, lighting, post-processing don'ts, icon grid and stroke |
| 8 | Layout and grids | Olympic digital grid, EDP H/40 margins, Hulu grids | 4–8% | Breakpoint table with columns, margins and gutters; print ratios |
| 9 | Motion & sound | Odido (motion + sonic), Hulu (none: a gap), IBM 0.07/0.11s on cubic-bezier(.2,0,.38,.9) | 0–5% | Duration and easing tokens, logo animation, transitions. **Missing in most docs** |
| 10 | Applications | all | 15–35% | Real artefacts: stationery, social, OOH, product, environmental, merchandise |
| 11 | Governance, legal, contacts, downloads | Slack p41–50, Afterpay merchant rules, Channel 4 per-rule downloads | 2–6% | Trademark rules, approval contacts, asset downloads beside each rule, version and changelog |

Documents that skip chapters 2, 8 and 9 and spend more than 40% of their pages on mockups score lowest:

- bg-lassomd: about 40% mockups.
- bg-naseem-al-faihaa: 14 uncaptioned mockup pages.
- bg-make: a 15-page logo, colour and type kit.

## 2. What a complete identity system needs (minimum viable → excellent)

**Minimum viable:**
- logo plus clearspace and minimum size;
- 1 primary colour, 1 neutral pair and 1 accent with roles;
- 1–2 typefaces with a size scale;
- voice in five rules;
- 3 application examples.

**Excellent adds:**
1. **Geometry as formulas.** Rules survive any format without a lookup table.
   - Olympic: ring diameter = 12 × thickness.
   - Hulu Vessel radius = shortest edge ÷ 6, clamped to 13–60px at 1080p.
   - EDP margins H/40 and H/25; logo width counted in grid columns.
   - Kia R = 0.1 × panel width.
2. **Clearspace and centring from the mark's anatomy.**
   - Slack: one octothorpe.
   - Red Hat: the height of its "e".
   - Firefox: the F, at 40% of the mark height.
   - Dubai: one "daal".
   - Frame.io: optical centre on the second bar.
   - Kazam: the "wizard hat".
3. **Colour as an API.**
   - Named roles: Kazam's Pocus, Cauldron and the error-only "uh-oh".
   - LITE and HIGHLIGHT tints per colour.
   - Approved foreground/background pairs with printed ratios (Slack, Instacart, Mastercard AA/AAA shades).
   - Tinted neutrals (#0b051d, #1e1919, #faf1e5).
4. **A type scale with tracking per size and localisation offsets.**
   - Twitch writes specs as size/leading/tracking: 80/80/−20, 30/33/−15, 16/20/−10.
   - Slack sets text 10% smaller for EU languages and 15% smaller for Japanese.
   - Olympic gives named fallbacks.
5. **One proprietary device with hard limits.**
   - New Breed's loudline: rotated ±3°, once per spread, words of 10 characters or fewer, never on all-caps.
   - EDP's spiral: at least 55% visible.
   - Hulu's Vessel.
   - Twitch's extruded wordmark used as a gradient beam.
6. **Imagery direction with the reasoning.** Olympic's diversity balance, no over-saturation and "rings recolouring" bans.
7. **A digital grid table and component radii.** Olympic's 1600/1025/577/375 breakpoints; Hulu's product radii of 4/16/24.
8. **Motion tokens.** Only IBM and Odido came close, and this is the most common gap.
9. **Accessibility built in.** AA/AAA badges per swatch (Instacart, Firefox, Mastercard), a contrast-safe text shade per brand colour, and minimum text sizes.
10. **Asset delivery.**
    - A download link beside each rule (Channel 4, Miro).
    - Click-to-copy values (Night Embassy).
    - A changelog and version date (Night Embassy, Slack's dated edition).
    - Linked asset libraries (Dubai and Bynder).

## 3. Document design (how the guideline itself is laid out)

- **Two-level navigation:**
  - persistent running header with chapter and page number (NorthAlley's rule bar, Kazam);
  - numbered chapter openers on full-bleed brand colour (Miro's 324px #ffdd33 band, Hulu's numbered chapters 1.0–3.0, Help Scout's "01 Brand Foundation").
- **Page rhythm on the page:**
  - rule statement as a large sentence;
  - specification in mono or small caps;
  - visual proof;
  - a do/don't pair.
  - Don'ts are drawn with a thin red diagonal strike (Chatham) or as a grid of 9 tiles (Olympic, EDP).
- **Formats:**
  - PDFs are 16:9 decks (1920×1080 in 9 of 21) or A4/letter.
  - Live sites use a fixed left nav plus a long scrolling page per chapter (Herman Miller, Night Embassy, SeatGeek, IBM). Their recurring mobile failure is a sidebar that doesn't collapse.
- **Self-demonstration:** the document uses its own system. Klarna sets 208–320px display type; Audi shows its rings and type as live sliders; eBay shows a 17×8 = 136-colour grid.

## 4. Errors found inside real guidelines (and the lesson)

- **Contradictory hex values between pages:**
  - Mastercard: Light Grey E3DFD7 vs D5D0CA.
  - Bella Nova: Grey 200 = sienna.
  - Bolt and Visit Dubai: HEX vs RGB disagree.
  - FIBA: "Black" = RGB 255/255/255.
  - Lesson: generate every value from one token source.
- **Approved pairs that fail contrast:**
  - Hulu's "meets contrast standards" green at 3.04:1.
  - Kazam's white on lilac at 1.74:1.
  - Olympic's white on yellow at 1.82:1.
  - Discord's suggested pairing at 2.86:1.
  - Lesson: compute, don't eyeball.
- **Missing minimum sizes and misuse pages** (Kazam, NorthAlley, Twitch, Frame.io). Lesson: they are required.
- **Copy errors, lorem ipsum and broken text layers:** Kia's fonts were stripped, Bella Nova pastes in another project's text, Kazam has "Cababra", Discord has typos. Lesson: proof the doc like a product.
- **Link rot:**
  - Of 54 guideline links on brandguidelines.net, at least 12 were dead, redirected, cert-expired or login-walled within the capture window (see `PROGRESS.md` failures log).
  - Lesson: host guidelines on a stable URL with versioned PDFs.

## 5. Template to reuse

See `skills/aaa-design/references/brand-system-template.md` for the fill-in template derived from this anatomy.

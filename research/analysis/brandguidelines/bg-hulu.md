---
id: bg-hulu
source: brandguidelines
category: guideline
status: analyzed
title: "Hulu"
creator: "DixonBaxi"
styles: [dark-premium, maximalist-color, photo-led, aurora-glow]
patterns: [the-vessel-container, ratio-based-radius-and-stroke, colour-worlds-with-proportions, aspect-ratio-unit-grid, type-expression-modes, glow-reveal-states, fix-and-flex-campaign-system, voice-volume-controls]
mode: dark
palette: ["#1ce783", "#040405", "#183949", "#29a869", "#ffffff"]
type_families: ["Graphik (Light, Regular, Medium, Semibold, Bold, Super + italics, embedded)", "Proxima Nova (Google Slides fallback, per doc)"]
type_class: [neo-grotesk, grotesk]
radius_px: [4, 16, 24]
motion: {durations_s: [], easing: [], loop: false}
scores: {aesthetics: 9, originality: 8, usability: 8, craft: 8}
craft_signals: [radius-equals-shortest-edge-over-6, stroke-equals-longest-edge-over-100, per-format-radius-min-max, type-fills-70-or-90-percent-of-vessel, colour-world-60-30-10, leading-and-tracking-table-per-style, gradient-light-source-direction-rule, glow-as-reveal-direction]
anti_patterns: [hero-green-unusable-with-white, secondary-green-overclaims-accessibility, clipped-text-on-intro-slides, placeholder-section-numbers, no-motion-timing-values]
---
# Hulu — DixonBaxi

## 1. Snapshot
- **Subject:** The "Big Green Guide", a 138-slide 1920×1080 pt brand guideline (59 MB PDF) by DixonBaxi for Hulu. It spans principles, design toolkit, product, motion and network idents, tone of voice, campaigns and evergreen channels such as social, email, web and swag.
- **Why it's remarkable:** The whole identity is generated from one device, **The Vessel**: the rounded rectangle implied by the "hulu" logotype, drawn as a green stroke. It holds type, frames talent, becomes a UI selection state, glows to reveal content and drives the network ident. Its geometry is fully parametric: radius = shortest edge ÷ 6, stroke = longest edge ÷ 100 or ÷ 50, and type fills 70% or 90% of its width.

## 2. Composition & layout
- **Slide template:** a section number top-left (e.g. "2.6") at x≈40/1400. A green pill tag with the chapter name sits at x≈150, the page number top-right, and a bold topic label in the left margin (x≈40) with a short explanation at x≈150. Content occupies the right ~65%. A 1 px vertical divider at x≈452–502 separates the rules column from the demos on spec pages.
- **Rhythm:** each chapter opens with a full Hulu Green slide (giant black all-caps in Graphik Super/Bold) or a white slide with a black title. A black "manifesto" slide follows with a 4–5-line statement in Graphik Regular at about 26 px on the 1400 px render (≈36 pt), where one phrase is highlighted green ("visual voice", "grid", "icons", "illustration"). Then come the spec pages.
- **Cover (p1):** "BIG / GREEN / GUIDE" in black Graphik at about 205 px cap height on 1400 px (≈280 pt), tight leading of about 0.9, bleeding toward the left edge, with a small black hulu badge top-right. palette.json: #1de783 68%, #040404 25%.
- **Grids (p53–57):** the format's aspect ratio becomes a 1:1 unit grid, which is then multiplied for density.
  - 16:9 → 16×9 units → 48×27 grid.
  - Social 1080×1080 → 30×30.
  - Performance banner 300×600 → 30×60.
  - Billboard 40×12 ft → 80×24.
  - A-size poster → 24×32, US Letter → 25×33 (rounded).

## 3. Typography
- **Embedded (pdffonts):** Graphik Light, Regular, RegularItalic, Medium, Semibold, Bold, BoldItalic, Super and SuperItalic. It is a single family, and the doc names Commercial Type as the vendor for licensing. Proxima Nova is the Google Slides fallback.
- **Four type expressions (p37):**
  - **Core** (everyday): campaigns, evergreen, performance.
  - **Active** (Live TV and sports): Super Italic.
  - **Narrative:** type inside the Vessel combined with imagery.
  - **Cinematic** (premium only): Graphik Light, all caps, very wide tracking. This is the only place Light is allowed.

**Core spec table (p38)**

| Style | Weight | Leading | Tracking |
|---|---|---|---|
| HEADLINE (caps) | Bold | 90% | −25 (−3%) |
| Conversational Headline | Bold | 115% | −18 (−2%) |
| Section Header | Regular | 115% | −18 (−2%) |
| Subhead | Regular | 125% | 0 |
| Body | Regular | Auto | +10 (+1%), adjusted for size and legibility |

**Active (p40)**
- SPORTS HEADLINE: Super Italic, 85% leading, −20 (−3%).
- ENTERTAINMENT HEADLINE: Bold, 85%, −20.
- News headline: Medium, 115%, −10 (−1%).

**Cinematic (p44)**
- Light, all caps, tracking from **+150 to +2000** depending on copy length.

**Narrative (p42)**
- Headline and Emphasis styles: Bold and Bold Italic, in sentence case or all caps, set inside the Vessel.

**Type don'ts (p46):** rotating type, multiple content colours, the dimensional glow on type, outlined text over imagery, covering faces with type, and mismatching type and Vessel colour.

## 4. Colour
| Hex (doc) | Name | Role | Share |
|---|---|---|---|
| #1CE783 | Hulu Green (PMS 7479 C) | logo, Vessel stroke, highlight words, chapter openers | 92% of p23; 68% of cover |
| #040405 | Hulu Black (PMS Black C) | default canvas, "only used in combination with green" | 96% of p13 |
| #040405 → #183949 | Dynamic Gradient | cinematic background; light source bottom-right for marketing, top-right for product | p138 is all gradient |
| #29A869 | Secondary Green | sparing digital use with white or light colours | — |
| #FFFFFF | White | text, Business Time background | — |
| Show colour (rainbow ramp) | Content colour | Vessel/glow colour sampled per title from key art (eyedropper method, p29–30) | — |

- **Three colour worlds (p26–33), with proportions:**
  - **Show Time 60%:** gradient or black ground, green/white type, plus content colour.
  - **Clean Green 30%:** green ground, black/white type.
  - **Business Time 10%:** white ground, black type with Secondary Green, for B2B, recruitment and product.
- palette.json cross-check: #1de783 (green), #040404 (black), #2aa869 (secondary), #082933 / #031013 (gradient on p138).

WCAG (contrast.py):
- #1CE783 on #040405: **12.5:1**. Black on green: 12.5:1. White on #040405: 20.49:1.
- Green on gradient end #183949: **7.44:1**.
- White on #1CE783, or green on white: **1.64:1**. The hero green can never carry or sit behind white text; the system correctly pairs it only with black.
- White on Secondary Green #29A869: **3.04:1**. The doc says it "meets color contrast accessibility standards", but that holds only for large text (AA-large), not body.

## 5. Depth & material
- **Dark-cinema material:** the black-to-petrol gradient (#040405 → #183949) with a stated light-source direction, plus the **Vessel glow**. The glow has four styles (p71):
  - dimensional reveal (outer bloom, motion only);
  - top-down reveal;
  - bottom-up reveal;
  - left-to-right reveal.

  Each is an inner gradient fill fading from the stroke.
- **Imagery:** "content colour" glows and gradient overlays sit under text on key art for legibility (p28).
- The swag (p133–137) carries the same glow and bolt to physical objects: a jersey, a helmet and stickers.

## 6. Components & patterns
- **Logo (p13–19):** lowercase "hulu" in green.
  - Black on green is allowed for impact.
  - Green over the gradient is preferred.
  - The badge (logo in a Vessel) is used only when the plain logo would be illegible.
  - Originals lockup: "hulu ORIGINALS" with "Originals" set in Graphik.
  - Partner lockups:
    - Premium add-ons: "ESPN+ on hulu" inside the Vessel.
    - Ongoing partners: a vertical pipe **150% of the height of the "l"**.
    - One-off partners: a white Graphik Semibold "x", raised to optical centre.
- **The Vessel (p58–73):**
  - **Behaviours:** tell stories, emphasise, act as a window, highlight, spotlight characters, guide the viewer.
  - **Radius:** shortest edge ÷ 6 (e.g. a 154 px-tall horizontal vessel gets a 38 px radius; a 196 px-wide portrait one gets 32 px), clamped per format:

    | Format | Min radius | Max radius |
    |---|---|---|
    | 3840×2160 | 26 px | 120 px |
    | 1920×1080 | 13 px | 60 px |
    | 1080×1080 | 13 px | 30 px |
    | Billboard 40×12 ft | 1.5″ | 11″ |
    | Performance banners | 4 px | 16 px |

  - With multiple Vessels, use the average radius, "not smallest, not largest".
  - **Stroke:** longest edge ÷ 100 for regular (904 px vessel → 9 pt stroke) and ÷ 50 for heavy (sports, 18 pt). Mixed strokes average out.
  - **Type padding:** wide (type = 70% of Vessel width, evergreen/Originals) or compact (90%, sports).
  - **Product radii (p72):** a three-step scale of 4 / 16 / 24 px by container size.
  - **Don'ts (p73):** overlapping Vessels, colours unrelated to the art, heavy glows over art, mismatched type/icon colour, blocking faces, multiple colours in one execution.
- **Icons (p47–51):** utility icons (monoline, roughly 2 px at 24) vs pictograms. Marketing icons are a 12-icon set in green-stroked circles. One "+" icon shifts meaning from product (Add to My Stuff) to brand to Pride campaign.
- **Illustration (p74–78):** black-line characters with green fills, built from the Vessel's rounded corners. Formats are character spots and 3D hero renders on light grey.

## 7. Motion
- p85–92 define principles, not timings. Each of the four global principles is translated into motion:
  - Always a Story: z-space push through content.
  - Delightfully Human: the stroke stretches, contracts and expands.
  - Simply Essential: snappy, simple movement, with a warm glow as the Vessel "gleams".
  - Do it Different: bold green punches and hard cuts.
- **Network ident (p89–92):** a black frame with a multicolour edge glow resolves into the green Vessel and logo, then cuts to a full-green frame. It comes in Hulu and Hulu Originals versions at 16:9 1920×1080, 4K, 1:1, 4:5 and 9:16, plus a condensed App Open variant.
- **Promo structure (p93–97):** storyboards for licensed single-show, multi-show, premium add-on and "New this Month" promos.
- No durations, frame counts or easing curves appear in the PDF, so they are unknown here. The yaml motion field is left empty for that reason.

## 8. Brand system
**Global design principles (p8):** a quadrant around "TV for TV people": Always a story, Delightfully human, Do it different, Simply essential. The same four principles organise voice (p100–104) and motion (p86). One framework is used across disciplines.

**Logo rules**
- **Safe zone:** the height of the "u" on all sides (p14).
- **Minimum size:** not specified in the PDF.
- **Fill:** green wherever possible, black on green, badge only when illegibility forces it.
- **Partner lockups** must carry "equal visual weight".

**Voice and tone (p98–108)**
- "Our voice is our superpower."
- Each principle gets "What it means / What it doesn't" plus a real example. "Hold your breath. Thrillers on Hulu" is Always a Story; "This is not a drill. All-new Hulu originals have landed." is Do it Different.
- **Volume controls (p105):** three levels.
  - Volume 1, Totally Hulu: fun, provocative, loud (OOH, tweets).
  - Volume 2, Getting Down to Business: direct, friendly, informative (customer email, renewal, B2B).
  - Volume 3, Awkward Moments: warm, human, solution-focused (error messages, missed payments, complaints).

  Every level has real copy pairs. This is the most usable voice spec in the batch.

**Campaigns (p109–118):** "Time to Have Hulu" (OOH, web banners, landing page) and Culture Campaigns run on a **Fix and Flex** system. Fixed: Hulu logo, core colours, Graphik. Flexed: a campaign logo, a line, accent colours (e.g. Earth Day blue, Pride gradient), a graphic language and an optional second typeface.

**Document structure (138 pp.)**

| # | Chapter | Pages |
|---|---|---|
| 0 | Cover, welcome, contents, system overview, Vessel intro | 1–6 |
| 1.0 | Global Design Principles | 7–8 |
| 2.0 | Design Toolkit (opener + overview) | 9–10 |
| 2.1 | Trademarks (logo, safe zone, hero palette, badge, lockups, partner lockups, app icons) | 11–20 |
| 2.2 | Color (primaries, colour worlds, content colour, proportions) | 21–33 |
| 2.3 | Typography (Graphik, Core / Active / Narrative / Cinematic, don'ts) | 34–46 |
| 2.4 | Iconography | 47–51 |
| 2.5 | Grids | 52–57 |
| 2.6 | Vessel (concept, behaviours, radius, stroke, padding, image, glow, product radii, don'ts) | 58–73 |
| 2.7 | Illustration | 74–78 |
| 3.0 | Product Design | 79–82 |
| 4.0–4.1 | Motion Toolkit / Motion Theory | 83–86 |
| 4.2 | Network Ident System | 87–92 |
| 4.3 | Promo Structure | 93–97 |
| 5.0 | Tone of Voice | 98–108 |
| 6.0 | Campaigns: Time to Have Hulu 110–114, Culture Campaigns 115–118 | 109–118 |
| 7.0 | Evergreen Brand: Social 120–124, Email 125–127, Marketing Web 128–130, Swag 131–137 | 119–137 |
| — | End slate (logo on gradient) | 138 |

**Token decisions worth stealing**
- Parametric container geometry: `radius = min(w,h)/6` clamped per format, and `stroke = max(w,h)/100`.
- Colour-world ratios (60/30/10) instead of per-colour percentages.
- Tracking and leading stated per style in both units and percent.
- Content colour picked from key art for the per-title accent.
- A voice "volume" dial mapped to channel and situation.

## 9. UX
- Every spec page names where to use the style (bullets) and shows real executions alongside.
- Deep links go out to toolkit sites ("This Is Hulu", "here" links), so the PDF acts as a hub.
- **Gaps:**
  - No logo minimum size.
  - No motion timings.
  - The hero green fails with white (1.64:1), and the secondary-green claim is overstated.
  - Intro slides p3, p5 and p6 have text clipped at the top edge.
  - "X.X" placeholder section numbers survive in the text layer.
  - On p66, the 1920×1080 "minimum" example shows 16 px while the table says 13 px.

## 10. Craft signals
- A worked example of the radius ratio: 154 px tall → 38 px radius; 196 px wide → 32 px.
- Stroke examples: a 904 px Vessel gives 9 pt regular or 18 pt heavy.
- Every slide carries the same chrome: section number, green pill tag, page number top-right.
- Graphik Light is restricted to the Cinematic expression only. Weight is a semantic signal.
- The gradient has a defined light direction per discipline (bottom-right for marketing, top-right for product).
- The same "+" icon is shown in three contexts to teach semantic flexibility.
- Swag extends the bolt and Vessel into physical goods with the same green #1CE783 (helmet, jersey, lanyard).

## 11. Reproduction recipe
```css
:root{
  --hulu-green:#1ce783; --hulu-black:#040405; --hulu-petrol:#183949;
  --hulu-green-2:#29a869; --white:#fff;
  --font:"Graphik","Inter",system-ui,sans-serif;
  --r-sm:4px; --r-md:16px; --r-lg:24px;           /* product radii */
}
body{background:linear-gradient(315deg,var(--hulu-petrol) 0%,var(--hulu-black) 70%);color:#fff;font:400 18px/1.4 var(--font);letter-spacing:.01em;}
.headline{font-weight:700;text-transform:uppercase;line-height:.9;letter-spacing:-.03em;}
.conv-headline{font-weight:700;line-height:1.15;letter-spacing:-.02em;}
.sports{font-weight:900;font-style:italic;line-height:.85;letter-spacing:-.03em;}
.cinematic{font-weight:300;text-transform:uppercase;letter-spacing:.5em;}
.hl{color:var(--hulu-green);}
/* The Vessel: set --w/--h in px on the element */
.vessel{
  --short:min(var(--w),var(--h)); --long:max(var(--w),var(--h));
  width:calc(var(--w)*1px);height:calc(var(--h)*1px);
  border:calc(var(--long)/100*1px) solid var(--hulu-green);
  border-radius:clamp(13px,calc(var(--short)/6*1px),60px);   /* 1920x1080 clamp */
  display:grid;place-items:center;
}
.vessel--heavy{border-width:calc(var(--long)/50*1px);}
.vessel > .type{width:70%;}  .vessel--compact > .type{width:90%;}
.vessel--glow{box-shadow:0 0 24px rgb(28 231 131 / .55), inset 0 0 0 0 transparent;}
.vessel--reveal-down{background:linear-gradient(180deg,rgb(28 231 131 / .35),transparent 40%);}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 9 | Cinematic black/green with a single elegant container device; consistent from cover to helmet. |
| Originality | 8 | Deriving a parametric, glowing container from the logo's counter, and using it as UI state, ident and frame, is a fresh systemic idea. |
| Usability | 8 | Formulas, clamps, spec tables and voice volumes are directly applicable; motion timing and logo min size are missing. |
| Craft | 8 | Tight template and worked examples; clipped intro text, placeholders and a radius inconsistency hold it back. |

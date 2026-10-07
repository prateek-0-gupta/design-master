---
id: bg-help-scout
source: brandguidelines
category: guideline
status: analyzed
title: "Help Scout Brand Guidelines"
creator: "In-house (Figma prototype)"
styles: [editorial-serif, corporate-clean, minimal-swiss, kinetic-type]
patterns: [figma-prototype-as-slide-deck, breadcrumb-footer-with-mono-labels, condensed-all-caps-section-openers, serif-light-plus-grotesk-bold-headline-pair, 60-30-10-colour-ratio, clearspace-in-mark-height-units, css-snippet-in-type-page, dark-indigo-vision-slide]
mode: mixed
palette: ["#131c25", "#0e0e32", "#f6f2ef", "#ffffff", "#3050e0", "#7a9ccb", "#fddfd5", "#cddce5"]
type_families: ["GT America (body, link text; ss01/ss03/ss05 on)", "Garnett (headlines, Bold)", "FK Screamer (display, all-caps condensed)", "Victor Serif (subheads, blockquotes)", "small monospace for breadcrumbs (unidentified)"]
type_class: [neo-grotesk, editorial-serif, condensed, mono]
radius_px: [8, 12]
motion: null
scores: {aesthetics: 8, originality: 7, usability: 7, craft: 8}
craft_signals: [serif-grotesk-weight-contrast-pair, mono-breadcrumb-footer, 60-30-10-ratio-diagram, clearspace-diagram-with-0.5x-and-1x, open-type-feature-flags-documented, clay-warm-neutral-ground, dark-indigo-section-slides]
anti_patterns: [prototype-chrome-hides-navigation, census-unusable-figma-ui-only, tiny-spec-labels-in-specimen-frames]
---
# Help Scout Brand Guidelines — In-house

## 1. Snapshot
- **Subject:** a Figma prototype (`figma.com/proto/...Brand-Guidelines`) of the Help Scout brand guidelines, shown as 16:9 slides. The capture is 34 unique frames at 1440×900 (the slide itself is about 1344×756 inside a black letterbox). No redirect. `census_home.json` and `tokens.json` describe Figma's own UI (Inter 11/14 px, dark chrome), so they are **not** brand data. All values below come from the pixels and `palette.json`.
- **Why it's remarkable:** the deck pairs a light editorial serif with a heavy grotesk in the same headline, then switches to a condensed all-caps display for chapter openers. It also documents OpenType feature flags and a 60/30/10 colour ratio.

I viewed 12 frames (f01, f04, f08, f12, f16, f19, f22, f26, f30, f33, f36, f39) plus the mapped home tile.

## 2. Composition & layout
- **Slide frame:** 16:9. Content starts at x≈174 on the 1440 canvas, which is about 126 px inside the slide edge, so there is a generous left margin of roughly 9% of slide width.
- **Footer bar (about 42 px tall, hairline above):** left side is a mono breadcrumb (e.g. "Brand System / Typography / Primary Fonts"); right side is the small mark plus "Help Scout Brand Guidelines". A hamburger icon sits top right at about (1364, 99).
- **Chapter openers (f08 "02 Brand Messaging"):** a dark indigo field with an orange serif numeral, then a huge all-caps condensed title at about 150 px cap height. Sub-section links are listed bottom right in about 15 px sans.
- **Content slides:**
  - Title at top left, about 44 px Garnett Bold.
  - A two-column split: a 570 px-wide copy column on the left and a visual panel on the right, or a 60/40 text and spec layout (f26).
  - Visual panels are rounded rectangles of about 8–12 px radius on clay or pastel grounds (f22 shows pale blue #cddce5 and peach #fddfd5 side by side).
- **Boilerplate slide (f39):** a single paragraph in Garnett Bold at about 30 px with a cobalt highlighted first clause.

## 3. Typography
Read from the specimen slides (f22, f26):
- **Display:** FK Screamer, all caps, extreme condensed, tight leading (about 1.0). It is used for chapter titles and for headline specimens.
- **Headline:** Garnett Bold. It is chunky with tight tracking. Sizes seen: about 44 px (slide titles), about 25 px (clearspace title) and about 30 px (boilerplate).
- **Subheads and blockquotes:** Victor Serif Light/Regular. It is large (about 38–40 px), and italic is used for emphasis ("relationships", "simplicity").
- **Body:** GT America Regular, about 16–18 px with 1.5–2.0 leading in the vision slide.
- **Mono:** a small monospace at about 10–11 px for breadcrumbs and specimen labels.
- **Headline pair (f04, f16):** a light serif line stacked over a bold grotesk line, e.g. "Great things happen when customers are happy / **People feel valued and companies grow**". The weight and style contrast is the signature.
- **Code on the type page:** `font-feature-settings: 'ss01' on, 'ss03' on, 'ss05' on;` with the text naming the alternates: single-storey g, alternate arrows, round dots.

## 4. Colour
| hex | role | approx share |
|---|---|---|
| #ffffff | content slide ground | ~40–68% of light slides |
| #f6f2ef / #ede8e5 | "Clay" warm neutral (30% of the ratio) | ~65–74% of clay slides |
| #131c25 | charcoal: logo-on-dark ground, headline text | 74% of the cover |
| #0e0e32 | deep indigo section and vision ground | ~70% of dark slides |
| #3050e0 (eyeballed; sampled dark-ground variant #4470da) | Cobalt, the actionable accent: logo mark, links, highlights | small |
| #7a9ccb | muted sky text on indigo | text |
| #fddfd5 / #cddce5 | pastel panel grounds in visual slides | panels |

The colour slide (f30) states a **60/30/10** distribution: 60% White, 30% Clay and 10% colour (full spectrum ramps, charcoal text and cobalt actions). The 10% panel shows 9+ tinted ramps (red, green, violet, cobalt and others). I did not read their hexes at a legible size.

Contrast (contrast.py):
- #131c25 on #fff: **17.21:1**.
- #f6f2ef on #131c25: **15.46:1**.
- #7a9ccb on #0e0e32: **6.6:1**.
- Cobalt #3050e0 on #fff: **6.27:1**.

## 5. Depth & material
Mostly flat. Elevation appears only inside product screenshots: soft shadowed cards (the profile popover in f22) and frosted gradient email cards in the motion slide (f39). Surfaces are separated by tone (white vs clay vs pastel) and by 1 px hairlines, not by shadow.

## 6. Components & patterns
- Breadcrumb footer with mono type.
- Hamburger menu in the corner.
- Spec captions: small mono label above each type sample ("Garnett Bold").
- A code block on a clay ground with blue syntax colouring.
- Clearspace diagram: lilac overlay boxes labelled X and 0.5X.
- Two-up cards: a visual on top and a bold title plus 3-line description beneath.

## 7. Motion
The deck itself is static slides. The Motion slide (f39) describes the brand as "engaging, energetic, and smooth", and shows a kinetic-type sequence ("But with growth comes complexity") over scattered email-subject cards with avatar chips. No durations or easings are given in the frames I saw.

## 8. Brand system
- **Chapters seen (inferred from breadcrumbs):** Brand Foundation (Overview, Boilerplate, Vision), Brand Messaging (Positioning, Content Philosophy), Brand Identity (Logo: Overview, Clearspace, plus others), Brand System (Visual Direction / Key Elements, Typography / Primary Fonts, Color / Distribution, Photography with Photo Art Direction and People & Avatars, Video & Motion / Motion). I could not read every frame, so the page-level order is partly inferred.
- **Logo:** a diagonal three-stroke mark (two leaf-like outer strokes with one long centre stroke) plus a Garnett-style wordmark. It is shown in cobalt and charcoal on white, and in a lighter blue and white on dark (f01, f19).
- **Clearspace (f20):** left and right equal one mark height, X; top and bottom equal 0.5X.
- **Visual direction (f22):** two pillars. "High-fidelity product visuals" (full screens and isolated crops, unabstracted UI) and "expressive typography".
- **Voice:** the vision and content slides use conversational, warm, human phrasing. The content philosophy slide stresses substance over surface-level jargon.
- **Photography:** "People & Avatars" and art direction sections exist (f36).
- **Token decisions worth stealing:**
  - A serif/grotesk weight-contrast headline pair.
  - A single warm neutral (Clay) as 30% of the surface.
  - A stated 60/30/10 ratio.
  - OpenType feature flags written as copy-paste CSS.

## 9. UX
Slide-by-slide with a breadcrumb and a menu is easy to follow. As a Figma prototype it works well for a read-through, but it is fixed-size and cannot be searched or deep-linked easily. Specimen labels are tiny (about 9 px mono).

## 10. Craft signals
- Mono breadcrumb footer of the same height on every slide, with a hairline.
- The serif-light plus grotesk-bold headline appears consistently across vision, motion and visual-direction slides.
- The clearspace diagram uses a repeatable unit (the mark's own height).
- The type page gives code, not only specimens.
- Chapter openers flip to dark indigo with a numeral in a warm orange for rhythm.

## 11. Reproduction recipe
```css
:root{
  --hs-charcoal:#131c25; --hs-indigo:#0e0e32; --hs-clay:#f6f2ef; --hs-white:#fff;
  --hs-cobalt:#3050e0; --hs-sky:#7a9ccb; --hs-peach:#fddfd5; --hs-mist:#cddce5;
}
body{background:var(--hs-white);color:var(--hs-charcoal);
  font:400 17px/1.6 "GT America","Inter",sans-serif;
  font-feature-settings:'ss01' on,'ss03' on,'ss05' on;}
h1,h2{font:700 44px/1.05 "Garnett","GT America",sans-serif;letter-spacing:-.02em;}
.lede{font:300 38px/1.15 "Victor Serif",Georgia,serif;} .lede b{font:700 1em "Garnett";}
.chapter{background:var(--hs-indigo);color:#f8f7f5;}
.chapter h1{font:400 150px/.9 "FK Screamer",Impact,sans-serif;text-transform:uppercase;}
.crumbs{font:400 11px/1 ui-monospace,monospace;color:#6a7495;border-top:1px solid #0000001a;}
.panel{border-radius:12px;background:var(--hs-clay);}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Confident serif/grotesk contrast, a calm clay ground and dramatic condensed openers. |
| Originality | 7 | The mixed-weight headline and the warm editorial feel are fresh for SaaS. |
| Usability | 7 | Clear structure and a code snippet, but it is a fixed prototype with small labels. |
| Craft | 8 | Consistent footer, spec labels and a unit-based clearspace diagram. |

---
id: bg-new-breed
source: brandguidelines
category: guideline
status: analyzed
title: "New Breed"
creator: "In-house"
styles: [gradient-mesh, corporate-clean, photo-led]
patterns: [loudline-tilted-highlight, topography-line-texture, blob-masked-grayscale-avatar, side-nav-chapter-rail, cool-warm-palette-split, named-gradients-with-stops, shadow-spec-card, equal-radius-boxes]
mode: mixed
palette: ["#733BF6", "#AB89FA", "#4DE5F0", "#373A36", "#EDF5FC", "#3AD531", "#FC3D48", "#FCF447"]
type_families: ["Proxima Nova (Light/Regular/Medium/Extrabold/Black + Italic)", "condensed grotesk wordmark (outlined artwork, face not named)"]
type_class: [geometric-sans, condensed]
radius_px: [13]
motion: null
scores: {aesthetics: 7, originality: 6, usability: 7, craft: 7}
craft_signals: [loudline-rotate-plus-minus-3deg, one-loudline-per-spread, topography-three-stroke-spec, shadow-multiply-20-blur-5, box-radius-13px-max-4-1-aspect, gradient-stop-order-locked, nav-rail-active-state, naming-convention-do-dont]
anti_patterns: [white-on-light-violet-fails, white-on-turquoise-and-green-in-swatches, voice-chapter-missing, sparse-logo-colour-specs]
---
# New Breed — In-house

## 1. Snapshot
- **Subject:** A 44-page, 1920×1080 pt in-house brand guideline for New Breed, a HubSpot Elite solutions partner. It covers a condensed all-caps "NEW BREED +" wordmark, a violet-to-turquoise gradient system, Proxima Nova Extrabold/Black headlines, contour "topography" line textures, and a tilted highlighter device called the "loudline".
- **Why it's remarkable:** It reads like a product design system, not a logo book. Gradients come with named stops. Shadows come with a spec card (Multiply, 20%, 0/0, 5 px blur). Boxes have a single 13 px radius. The loudline device has a precise rule set (tilt ±3°, one per spread, words of 10 characters or fewer).

## 2. Composition & layout
- **Content pages (1400 px render):**
  - A persistent left navigation rail about 103 px wide in Ice #EDF5FC. It holds the "NEW BREED +" logo at the top and the seven chapters as a list (Brand Platform, Voice & Tone, Logo, Color, Type, Elements, Photography), with the current chapter in violet. This works like a web sidebar, and it is the doc's best navigation device.
  - Next to it, a text column at x≈155: a grey uppercase eyebrow (~13 px, e.g. "COLOR"), an H2 of about 40 px in Proxima Nova Black/Extrabold in Charcoal ending in a full stop ("Color palettes."), then about 17 px Regular body.
  - The right ~63% holds specimens, often a full-height violet-gradient panel from x≈519.
- **Dividers (p6, p15, p24, p31, p38):** full Violet → Light Violet diagonal gradient with 1 px white topography lines at about 40% opacity, and a white Black-weight title of about 34 px.
- **Statement pages:** after each divider comes an Ice "statement" page with a small "+" glyph and a 4-line Extrabold manifesto of about 15 px (p7, p16, p25, p32, p39).

## 3. Typography
- **Proxima Nova** (pdffonts: ProximaNova Regular, RegularIt, Light, Medium, Extrabld, Black). The book credits Mark Simonson (2005). The rules: 8 weights are allowed, Normal width only, never Condensed or Extra Condensed.
- **Hierarchy (p27):**
  - Ultra Headline: Black, about 130 px at 1400 width, tracking about −0.01 em.
  - Headline: Extrabold, about 40 px.
  - Body: Regular, about 17 px at ~1.3 leading.
  - Eyebrow: Black, uppercase, about 14 px, tracking about +0.05 em.
  - Buttons: Extrabold uppercase, about 15 px, in a Growth Green #3AD531 rectangle of about 193×52 px with a radius of about 4 px.
  - No numeric sizes are stated; these are measured from the render. Headlines take a terminal period as a brand mannerism.
- **Wordmark:** a heavy condensed grotesk in caps ("NEW BREED") plus a bold "+". It is outlined artwork, so pdffonts does not name it. It visually resembles a DIN/Barlow Condensed Bold class.
- **Loudline (p30):** a solid rectangle behind a single headline word.
  - Only on headers, never on an all-caps word, ideally on words of fewer than 10 characters.
  - High contrast with the text.
  - Tilted exactly **3° or −3°**, with the line offset in X and Y from the text.
  - At most one per page or spread. Never used to redact. "When in doubt, leave it out."

## 4. Colour
Values are taken from the document's swatches (p17) and gradient page (p18). palette.json confirms Violet #733bf6 as the dominant cover/divider colour.

| Hex | Name / role | Approx share |
|---|---|---|
| #733BF6 | Violet: brand core, panels, gradients | ~40% |
| #AB89FA | Light Violet: gradient start | ~10% |
| #4DE5F0 / #94EFF6 | Turquoise / Light Turquoise: gradient end, accents | ~6% |
| #373A36 | Charcoal: headlines, dark boxes | ~8% |
| #FFFFFF / #EDF5FC | White / Ice: page and nav rail | ~30% |
| #3AD531 | Growth Green: CTAs only | ~2% |
| #FC3D48 / #FD8B93, #FCF447 / #FDF891 | Salsa / Light Salsa, Sunglow / Light Sunglow: "warm" Applications palette | ~4% |

**Palette strategy:**
- The cool colours (violets, turquoise, charcoal, green) are for the corporate brand and services. The warm colours (salsa, sunglow) are reserved for the software Apps sub-brand.
- Three palette strips (Brand, Services, Applications) encode this.

**Named gradients (p18):**
- Full: #AB89FA → #733BF6 → #4DE5F0.
- Violet: #AB89FA → #733BF6.
- Ice: Turquoise at 30% → Violet at 30%.
- App: #FDF891 → #FD8B93.
- Stops may shift, but the order may never change and gradients may never be combined.

WCAG (contrast.py):
- White on #733BF6: **5.70:1**, the main headline pairing.
- Charcoal on White: 11.53:1.
- Charcoal on Ice: 10.47:1.
- Charcoal on Turquoise: 7.57:1.
- Charcoal on Sunglow: 9.98:1.
- **White on Light Violet #AB89FA: 2.73:1.** The Full gradient starts here, so white text on the light end of gradients fails.
- **White on Turquoise: 1.52:1**, **White on Growth Green: 1.95:1**, White on Light Salsa: 2.26:1. The swatch labels on p17 are white on these, and the green CTA buttons on p27–28 carry white text. These are real failures.
- Turquoise on Violet: 3.74:1, used for the eyebrows on violet panels, which is large-text grade only.

## 5. Depth & material
- **Shadow spec (p36):** Multiply mode, 20% opacity, X 0, Y 0, blur 5 px, colour #000000. It applies to white shapes on White/Ice or Violet, and to white Headline/Ultra text over violets and gradients only. The rules: never scale the shadow, never move it and never recolour it.
- **Boxes (p37):** radius **13 px** on all four corners, with an aspect ratio no more extreme than 4:1.
- **Topography (p33–34):** contour lines in three stroke types: 1 px with a 2.5 pt dash, 2 px solid, and 1 px solid. Strokes must scale proportionally. The only permitted colours are 20% Charcoal on White/Ice and 40% White on gradients or Charcoal.
- **Curves (p35):** large swooping shapes that must span the full width (top/bottom) or full height (side). When masked with topography, they share edges.

## 6. Components & patterns
- **Photo avatar (p43):**
  - a high-resolution grayscale cut-out portrait whose head protrudes above an oblong organic blob;
  - the blob is filled with the Full gradient plus topography;
  - a blurred lower shadow sits over the portrait base.
  - It is reused in testimonial cards with a large violet open-quote and Extrabold quote (p44).
- **Photo trimming (p42):** grayscale people cut out and set over gradient panels with Proxima headlines and a loudline.
- **Colour-combo pages (p19–23):** stacked-card diagrams show which background/surface/accent triples to use (Ice/White, White/Charcoal/Violet, Full gradient, App warm) next to real ad, webinar and one-pager examples.
- **CTA:** a Growth Green rectangle with an uppercase Extrabold label.
- **Icon:** a standalone heavy "+" in white or charcoal, in square or circle containers (p11).

## 7. Motion
None specified.

## 8. Brand system
**Logo rules:**
- **Primary:** the horizontal "NEW BREED +" lockup, shown at about 400 px wide on white (p8).
- **Safe zone (p9):** keep other elements at least one icon ("+") width away, drawn as a dashed box.
- **Minimum height:** **15 px**.
- **Colourways (p10):** only two fills are allowed, White or Charcoal. The page shows them on white, violet, ice, the Full gradient, turquoise, charcoal and the warm App gradients, with the rule "high contrast between background and logo colour is an absolute must".
- **Icon (p11):** the "+" alone, used sparingly on owned channels (social avatars, app icons, in-app UI), in White or Charcoal only.
- **Co-branding (p13):** **two icon widths** between the New Breed and partner logos (HubSpot shown), with partners never larger than New Breed apart from overhangs.
- **Pitfalls (p14):** eight don'ts: different colours for logo and icon, strokes, gradients, tilt or skew, 3D, bending or stretching, repositioning the icon, and joining into one word.
- **Name-in-copy conventions:** "New Breed" as two capitalised words. The wrong forms listed are NewBreed, New Breed+, New breed, NEW BREED, NB+ and "New Breed Revenue".

**Voice:** the Brand Platform pages (p2–5) set out belief, market view, identity and mission ("Help companies unlock meaningful growth", with the loudline on "growth"). The nav rail lists **Voice & Tone** as a chapter, but it is greyed out in every nav and no such pages exist in this PDF. The chapter is missing from this export.

**Imagery (p40–44):** own-office photography (the "Hula" HQ in Burlington, VT), real team members preferred over stock, and branded grayscale cut-outs over brand colours.

**Document structure (from the nav rail and dividers):**
1. Cover (p1)
2. Brand Platform: believe, see, are, mission (p2–5)
3. (Voice & Tone: listed but absent)
4. Logo: intro, logo, safe zone, colourways, icon, usage, co-branding, pitfalls (p6–14)
5. Color: intro, palettes, gradients, using the palette, combos in action ×4 (p15–23)
6. Type: intro, typeface, hierarchy ×2, type colour use cases, loudline (p24–30)
7. Elements: intro, topography, topography colours, curves, shadows, boxes and corners (p31–37)
8. Photography: intro, Hula offices, team photography, trimming, avatars, avatars in action (p38–44)

**Token decisions worth stealing:**
- Gradients as named tokens with locked stop order.
- A shadow token set out as a spec card (multiply, 20%, 0, 0, 5 px).
- One radius (13 px) plus a maximum aspect ratio (4:1) for boxes.
- The loudline with angle, frequency and character-count limits.
- A cool/warm palette split to separate the corporate brand from the product sub-brand.
- A three-stroke spec for the decorative line texture.

## 9. UX
Strong for a marketing/web team. The sidebar nav shows where you are, every element has a "how" plus a "when", and the combo pages tie palettes to real deliverables. Weak points:
- No numeric type sizes or grid.
- No CMYK/PMS anywhere (digital-only).
- The missing voice chapter.
- Several pairings the book itself uses fail WCAG: white on Growth Green CTAs, white labels on turquoise, and white on the light end of the gradient.

## 10. Craft signals
- The nav rail's active state is a violet chapter label, consistent across all 30+ content pages.
- Loudline tilt is fixed at ±3° and is applied in the mission line, the type page and the trimming examples.
- Topography strokes are specified as 1 px dash 2.5 pt / 2 px / 1 px, with exact opacity per background (20% Charcoal, 40% White).
- The box corner is 13 px everywhere, including swatch cards and testimonial cards.
- Every H2 ends with a period, applied without exception.
- The text shadow is allowed only for white text over violet, which keeps it from muddying light layouts.

## 11. Reproduction recipe
```css
:root{
  --violet:#733BF6; --violet-lt:#AB89FA; --turq:#4DE5F0; --turq-lt:#94EFF6;
  --charcoal:#373A36; --ice:#EDF5FC; --white:#fff; --green:#3AD531;
  --salsa:#FC3D48; --salsa-lt:#FD8B93; --sun:#FCF447; --sun-lt:#FDF891;
  --grad-full:linear-gradient(160deg,var(--violet-lt) 0%,var(--violet) 45%,var(--turq) 100%);
  --grad-violet:linear-gradient(160deg,var(--violet-lt),var(--violet));
  --grad-app:linear-gradient(160deg,var(--sun-lt),var(--salsa-lt));
  --shadow:0 0 5px rgba(0,0,0,.2); --radius:13px;
  --font:"Proxima Nova","Montserrat",system-ui,sans-serif;
}
body{font:400 17px/1.35 var(--font);color:var(--charcoal)}
.eyebrow{font-weight:900;font-size:13px;letter-spacing:.05em;text-transform:uppercase;color:#9a9a9a}
h1.ultra{font-weight:900;font-size:clamp(64px,9vw,130px);letter-spacing:-.01em;line-height:1}
h2{font-weight:800;font-size:40px;line-height:1.1}
.panel{background:var(--grad-full);color:#fff}
.panel h1{text-shadow:var(--shadow)}
.box{border-radius:var(--radius);background:#fff;box-shadow:var(--shadow)}
.btn{background:var(--green);color:var(--charcoal);font-weight:800;text-transform:uppercase;border-radius:4px;padding:16px 40px}
.loudline{position:relative;z-index:0}
.loudline::before{content:"";position:absolute;inset:.35em -.08em -.05em .12em;background:var(--charcoal);transform:rotate(-3deg);z-index:-1}
.topo{background-image:url(topo.svg);opacity:.4} /* 1px dashed, 2px, 1px strokes */
.nav-rail{width:103px;background:var(--ice)} .nav-rail a[aria-current]{color:var(--violet)}
```
Note: the recipe sets Charcoal on Green for the button. The book's white-on-green fails (1.95:1).

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 7 | Polished SaaS-marketing look: gradients, topo lines and grayscale cut-outs are cohesive, if very of-its-era. |
| Originality | 6 | The violet-turquoise gradient with blob avatars is a common B2B trope. The ruled loudline is a nice distinctive asset. |
| Usability | 7 | Web-sidebar navigation, token-like specs for shadow, radius, gradient and strokes, and real combo examples. Missing type sizes, print specs and the voice chapter. |
| Craft | 7 | Tight, consistent templates and precise element specs, undercut by several sub-AA pairings used in its own examples. |

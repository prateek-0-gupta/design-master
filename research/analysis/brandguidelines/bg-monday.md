---
id: bg-monday
source: brandguidelines
category: guideline
status: analyzed
title: "monday.com Brand Guidelines (brand-monday.com)"
creator: "monday.com (in-house)"
styles: [corporate-clean, minimal-swiss, playful-rounded, hairline-ui]
patterns: [accordion-left-nav-with-plus-icons, eyebrow-label-over-h1, this-vs-not-this-cards, status-colour-logo-semantics, logo-capsule-on-solid-colour, per-colour-hex-cmyk-pantone-ral-card, download-kit-pill-button, section-intro-then-hairline]
mode: light
palette: ["#6161ff", "#181b34", "#f0f3ff", "#ffffff", "#00ca72", "#ffcc00", "#fb275d", "#333333", "#f3f4f5"]
type_families: ["Poppins 300/400/500/600/700"]
type_class: [geometric-sans]
radius_px: [8, 160]
motion: {durations_s: [0.1, 0.2, 0.25], easing: [ease], loop: false}
scores: {aesthetics: 6, originality: 6, usability: 8, craft: 6}
craft_signals: [logo-colours-mapped-to-product-statuses, this-not-this-copy-examples, full-colour-spec-hex-cmyk-pantone-ral, capsule-logo-variant-per-colour, lowercase-brand-name-sentence-case-rule, last-update-stamp-in-nav]
anti_patterns: [white-text-on-yellow-1.51, white-text-on-green-2.17, light-weight-300-body-grey, typo-in-typography-page, thin-visual-system-no-imagery-rules, mobile-capture-shows-only-logo-splash]
---
# monday.com Brand Guidelines — monday.com (in-house)

## 1. Snapshot
- **Subject:** The public monday.com brand-guidelines microsite at brand-monday.com (page title "brandbook"). Captured pages: Home (splash), Brand values, Tone of Voice, Logo, Typography, Colors (the site_meta final URL is `/colors`). The capture is viewport frames (`_w` files at 1440×900), not long tiles, because the page scrolls inside a fixed layout. Footer of the nav reads "Last update: 10/26".
- **Why it's remarkable:** It ties the brand mark to product meaning: the three logo shapes are the three statuses "Stuck", "Working on it" and "Done" (red, yellow, green). Copy rules are taught with paired "This:" and "Not this:" cards. The system is very plain, a single geometric typeface (Poppins), white page, one purple, so usability is strong while visual ambition is low.

## 2. Composition & layout
- **Fixed left nav (0–287 px, 1 px right hairline):** logo at (20, 62), 240×50 px; five rows each 65 px tall with a 1 px #333 divider: Brand Foundations (+), Visual Identities (+), Products (+), Resources (→), Feedback (↗ external). Rows expand as accordions into 41 px sub-rows (14 px type), the active item in blue (#0082f3). Bottom: a rule and "Last update: 10/26" (13 px).
- **Content column:** starts at x=414, width about 900 px (to x=1314); top padding 70 px. Each page begins with a small letter-spaced eyebrow ("Our DNA", "Design", 14 px, 2 px tracking, grey) and an H1 at 59 px / 80 px leading in #333, followed by an intro paragraph at 16/23 px indented 8 px from the H1, then a 1 px black rule, then content.
- **Home splash:** the whole canvas is white and centred: the three-shape mark (≈270 px wide) over the "monday.com" wordmark (≈325 px), a short rule, and "Brand guidelines" in Poppins Light 32 px (#333). Nothing else, and the two viewport frames are identical.
- **Grids:** brand values in a 2×2 grid (columns at x=414 and x=886, 28 px gutter); logo variants in a four-up strip (352, 170, 170, 170 px) over a 92 px tall grey #f3f4f5 chip row; colour swatches 2 × 439 px then 3 × 285 px with 120 px tall tiles.
- **Mobile (390 px):** the first sheet shows only the centred logo splash with a black 64×64 px "+" menu button at top right (8 px radius), nothing else, so the mobile capture shows the splash only.

## 3. Typography
Census: one family, **Poppins** (300, 400, 500, 600, 700).
- **Scale (Tone of Voice page):** 59.2 px H1 (lh 79.92 = 1.35, tracking −2 px), 24 px H2-ish (lh 31.2), 20 px (×12), 16 px body (×49, lh 23.2 = 1.45), 14 px (×14, lh 20 or 22.4) and 21.6 px. Typography page: a 140 px "Aa" specimen with −7 px tracking, 32 px labels (lh 43.2), 12.8 px captions. Weights: 300 dominates (52 of 81 nodes on Tone of Voice, 24 of 48 on Typography), 600 for H3 and bold labels, 700 only once.
- **Colour of type:** body #333333 (63 nodes), heading #222222, section titles in monday purple #6161ff (5 nodes), active nav blue #0082f3.
- **Rules (visible):** Poppins for marketing assets and PowerPoint; weights shown as Bold, Semi-bold, Regular and Light in a four-up lowercase specimen (abcdefghij / klmnopqrs / tvwz). Do's and don'ts: no ALL CAPS for emphasis; no title case (only the first word capitalised); no end punctuation in titles unless a question. The wordmark itself is lowercase "monday.com" with ".com" in a light weight.
- The Typography intro contains a small typo ("ppresentations").

## 4. Colour
| Hex | Role | Notes |
|---|---|---|
| #6161ff | monday purple, primary; section headings and links | C73 M68 Y0 K0, Pantone 2725 C |
| #181b34 | monday dark | C99 M90 Y45 K60, Pantone 539 C |
| #f0f3ff | monday light (page chips show #f3f4f5 in practice) | C7 M4 Y0 K0 |
| #ffffff | white, primary | C0 M0 Y0 K0 |
| #00ca72 | Green done | C85 M0 Y98 K0, Pantone 354 C, RAL 6037 |
| #ffcc00 | Yellow working on it | C0 M13 Y100 K0, Pantone 116 C, RAL 1003 |
| #fb275d | Red stuck | C0 M90 Y60 K0, Pantone Red 032 C, RAL 3028 |
| #00854d / #d79700 / #b1123b | capsule variants of green/yellow/red | for the logo capsule only |
| #333333 | text | most nodes |
| #f3f4f5 | chip and card background | 16 nodes |

Primary palette: purple, dark, light, white. Supportive palette: the three status colours, "to be combined with the primary monday colours". Red carries a warning caveat: "communicate warning so use responsibly". The CSS also exposes product colour tokens (for example `--brand-primary-green #00ca72`, `--dev--dev-primary #00ca72`, `--crm--crm-primary #00d2d2`, `--crm--crm-color #00b7ff`), so product lines have their own hues beyond the doc.

**WCAG (contrast.py)**
- #333 on white 12.63:1. #181b34 on white 16.86:1.
- #6161ff on white 4.50:1 (just passes AA); on #f3f4f5 4.09:1 (fails for small text, which is how the 20 px section headings read on grey chips; large text passes).
- White on purple 4.50:1. White on green #00ca72 **2.17:1**, white on yellow #ffcc00 **1.51:1**, white on red #fb275d 3.78:1 (large only), white on blue-ish nav #0082f3-on-white 3.83:1. The capsule logo darkens each field (#00854d 4.71:1, #b1123b 6.96:1, #d79700 2.53:1 with white text, which still fails) so the white wordmark stays legible, a deliberate fix except on yellow.
- Grey hex captions #bdbdc2 under the capsule logos: 1.87:1 (fail).

## 5. Depth & material
Completely flat: `shadow: {}`. Structure is 1 px rules, #f3f4f5 chips with 8 px radius and 4 px left colour bars on the this/not-this cards (green #00c875-like for do, orange-red for don't). Radius census: 8 px (×16 on Tone of Voice) and 160 px for the pill buttons.

## 6. Components & patterns
- **Pill button:** black fill, white 14 px Poppins, 190×50 px (Download logo kit) or 184×50 (Download family), fully rounded.
- **This / Not this card:** #f3f4f5 box with an 8 px radius, a 6 px left bar (green for "This:", orange for "Not this:"), a tick or cross icon (24 px, green or pink-red) and the sample sentence. A caption below states the rule.
- **Value block:** purple 24 px label (Bold, Best in class, Authentic, Direct) over a 16 px Light paragraph.
- **Logo strip:** four variants in grey chips with a 13 px grey caption (Main logo, Avatar+text, Avatar+text (small), avatar).
- **Don't-grid for the logo:** six tiles, each with a red "Don't" label: delete the symbol, use one colour, deform, change the proportions, place the text above, change the space.
- **Colour card:** 120 px tile with hex, CMYK, Pantone (and RAL for the supportive set) in 12 px white on the tile; bold name below, short rule text under it.
- **Logo on solid colour:** Primary (purple, black, light grey, white) and Capsule (green, yellow, red) rows of 213/289 px tiles.

## 7. Motion
Measured transitions: `all 0.2s ease` (×3), `transform 0.25s ease` (×3), `max-height 0.25s ease` (accordion), `all 0.1s ease` (×2). No motion guidance in the pages captured; platform motion (celebratory animation, llamas) is only referenced in the Tone of Voice text ("celebratory animation when they complete a task").

## 8. Brand system
**Section map (nav):** Brand Foundations (Brand values, Messaging, Tone of Voice, The monday Llama) · Visual Identities (Logo, Typography, Colors, Platform Elements) · Products · Resources · Feedback.

**Brand values (4):** Bold (think big), Best in class, Authentic (honesty, transparency), Direct (clear, to the point).

**Tone of voice:** "Confident | Fluff-free | Playful | Passionate". Each trait has a short description, "This:" vs "Not this:" examples. Examples: "monday.com is a human-first work platform ..." vs "a magical work platform ..."; "gain real-time insights with zero guesswork" vs "like a data ninja". Rules include being concise without being abrupt, active voice, no jargon or buzzwords, and playfulness that is celebratory, not silly (llamas on dashboards).

**Logo:**
- Meaning: three shapes = "Stuck" (red), "Working on it" (yellow), "Done" (green).
- Construction: simple shapes; the space between the three elliptical shapes and the letter M creates balance; angle marker "33°" in the construction diagram. Optical kerning and proportions.
- Variants: Main logo, Avatar + text, Avatar + text (small), avatar. Download logo kit.
- Backgrounds: purple #6161ff, black, light grey, white; capsule versions on green, yellow and red.
- Misuse (6 shown): delete the symbol, use one colour, deform or manipulate, change proportions, place the text above, change the space.

**Typography:** Poppins for marketing and PowerPoint; four weights shown; rules above.

**Colour:** primary (purple, dark, light, white) plus supportive (the three statuses), with hex, CMYK, Pantone and RAL.

**Visual voice:** nothing captured on photography or illustration; there is a "The monday Llama" page and "Platform Elements" not captured.

## 9. UX
- Compact, scannable: nav always in view, eyebrow plus H1 on every page, one rule under the intro, then content.
- Do/don't pairs are the best teaching device here.
- Weak: no search, no copy-to-clipboard on hex, mobile view only shows the logo splash, supporting colour combinations are not given as approved pairs, and the muted grey captions are low-contrast.

## 10. Craft signals
- The brand mark's colours are product statuses, so the logo explains the product.
- Do/don't examples share one component with a coloured left bar and icon.
- Each colour provides hex, CMYK, Pantone and RAL (for the supportive set).
- Capsule logo variants darken the field behind the white wordmark.
- Nav shows a "Last update" stamp.

## 11. Reproduction recipe
```css
:root{
  --m-purple:#6161ff; --m-dark:#181b34; --m-light:#f0f3ff; --m-white:#fff;
  --m-green:#00ca72; --m-yellow:#ffcc00; --m-red:#fb275d;
  --m-text:#333; --m-chip:#f3f4f5; --m-link:#0082f3;
  --font:"Poppins",sans-serif;
}
body{font:300 16px/23.2px var(--font);color:var(--m-text);background:#fff}
.nav{position:fixed;inset:0 auto 0 0;width:287px;border-right:1px solid #ddd}
.nav-row{height:65px;display:flex;align-items:center;justify-content:space-between;padding:0 20px;border-bottom:1px solid #333;font:400 16px var(--font)}
.nav-sub{height:41px;font:400 14px var(--font)} .nav-sub.active{color:var(--m-link)}
.eyebrow{font:400 14px/20px var(--font);letter-spacing:2px;color:#868686}
h1{font:400 59.2px/79.92px var(--font);letter-spacing:-2px;margin:0}
h2.accent{font:500 24px/31.2px var(--font);color:var(--m-purple)}
.rule{border-top:1px solid #000}
.btn{background:#000;color:#fff;border-radius:160px;padding:15px 24px;font:400 14px var(--font)}
.card{background:var(--m-chip);border-radius:8px;border-left:6px solid var(--m-green);padding:24px 32px 24px 70px}
.card.dont{border-left-color:#ff7a3d}
.swatch{height:120px;border-radius:4px;padding:12px;font:400 12px/19px var(--font);color:#fff}
.capsule{background:#00854d;border-radius:999px;padding:14px 24px}   /* logo capsule on green */
.accordion{transition:max-height .25s ease}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 6 | Clean and friendly, but almost entirely white and Poppins Light with little visual drama. |
| Originality | 6 | The logo-as-status story and this/not-this cards are neat; the layout is a standard docs site. |
| Usability | 8 | Clear nav, short pages, concrete rules and downloads; limited by weak contrast on greys and sparse coverage. |
| Craft | 6 | Consistent component use and full colour specs; yellow and green white-text pairs fail, a typo and thin mobile support. |

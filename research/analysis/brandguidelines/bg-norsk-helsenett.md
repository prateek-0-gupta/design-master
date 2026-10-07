---
id: bg-norsk-helsenett
source: brandguidelines
category: guideline
status: analyzed
title: "Digital profilhåndbok for Norsk helsenett"
creator: "Norsk helsenett (NHN), hosted on Brandpad"
styles: [corporate-clean, minimal-swiss, flat-illustration, playful-rounded]
patterns: [brandpad-two-column-label-and-content, pill-download-buttons, alternating-section-grounds, two-pill-symbol-from-connection-concept, shape-scale-density-ladder, allowed-vs-forbidden-combination-grid, skin-tone-palette-for-illustration, icon-set-on-24px-grid-in-three-colours]
mode: light
palette: ["#002920", "#7befb2", "#015945", "#02a67f", "#c4f2da", "#dcddde", "#f1f2f2", "#ffffff"]
type_families: ["Helvetica Now (Display 600, Text 300/500/700 + italics)", "Graphik (Brandpad UI)"]
type_class: [neo-grotesk]
radius_px: [200]
motion: {durations_s: [0.15, 0.2], easing: ["cubic-bezier(0,0.6,0.88,1)", ease-in-out], loop: false}
scores: {aesthetics: 7, originality: 6, usability: 8, craft: 7}
craft_signals: [symbol-half-width-clearspace, one-pill-primitive-shapes, base-14.4px-multiplier-scale, icon-24px-grid-with-keylines, download-button-per-asset, allowed-forbidden-matrix]
anti_patterns: [hero-video-player-error, template-downloads-not-captured, many-sections-low-text-contrast-on-grey, label-column-wastes-space-on-mobile]
---
# Digital profilhåndbok for Norsk helsenett — NHN

## 1. Snapshot
- **Subject:** the Norwegian-language digital brand handbook of Norsk helsenett (health-sector network), live on Brandpad (`brandpad.io/norsk-helsenett/`, no redirect). It is a single 36,982 px scrolling page with 15 desktop tiles and 5 mobile sheets. The two "Last ned" download links (PowerPoint and Word templates) were file downloads and could not be captured, so template contents are known only from the on-page previews.
- **Why it's remarkable:** the whole identity grows from one idea, "knytninger" (connections): two slanted pills form the symbol, and the same pill, circle and square primitives scale from two big shapes to a dense mosaic. A very practical handbook, with a download button for nearly every asset.

## 2. Composition & layout
- **Hero:** dark green (#002920) block, logo top-left (x=58), 50 px light-weight headline "Digital profilhåndbok for **Norsk helsenett**" with the second line in mint #7BEFB2. The embedded intro video shows a "Player error" in the capture.
- **Two-column system:** every chapter has a left label (x=86, 32–36 px light) and content from x=538, so the content column starts at 37% of 1440. Body width ~820 px (to x≈1360).
- **Section grounds alternate** white → #F1F2F2 → white → #DCDDDE (design/colour/co-branding sections) so chapters read as bands without rules. Bands run about 450–800 px each.
- **Index:** 13 underlined links at 26 px pitch directly after the hero.
- **Grids:** logo tiles 3-up (≈402×200, 31 px gutter); colour swatches 3-up with 187 px circles; icons 16-up with 12 px captions; design-element samples 5-up squares of 200 px.
- **Mobile (390 px):** single column, label stacked above content, full-width 18 px text; hero text wraps to 3 lines; index links stay at 26 px pitch; logo tiles 3-up shrink to ~85 px.

## 3. Typography
From the census (Helvetica Now, 261 of 267 text nodes):
| Role | Spec |
|---|---|
| Hero / big heading | 72 / 90, 600 |
| H1 | 50.4 / 63 (or 70.56), 600, −1 px tracking |
| Section label (H1/H2) | 32.4 / 35.64, 600 (28 uses) |
| Sub-head | 25.2 / 36.54, 600 |
| Lead | 18 / 26.1, 300, −0.2 px |
| Body | 14.4 / 20.88, 300 (135 uses) |
The scale is a multiplier on a 14.4 px base: ×1, ×1.25, ×1.75, ×2.25, ×3.5, ×5. Weight 300 for body is light, so small 14.4 px text on light-grey bands has less stroke contrast. The profile font is Helvetica Now with seven weights (Display Regular, Text Light and Italic, Regular and Italic, Bold and Italic).

## 4. Colour
Values listed on the page (hex), roles from the layout:
| Hex | Role | Share |
|---|---|---|
| #002920 | hero, dark ground, logo on dark | hero + 8 nodes |
| #7BEFB2 | mint: buttons, accent, logo on dark | 16 backgrounds |
| #015945 | primary logo green | logos |
| #02A67F | icon green, mid | icons |
| #C4F2DA | pale mint tint | tints |
| #DCDDDE / #F1F2F2 / #F7F5F4 / #FFFFFF | grey ladder and white | 137 white, 47 grey |
| #00467A / #372770 / #6B1E27 / #E85800 / #FFC46B | support colours (blue, purple, red, orange, yellow) | illustration |
| #3D1A13 / #723E33 / #B86853 / #E09D7B / #FBD9A5 / #F7C9BE | six skin tones, illustration only (not icons or infographics) | illustration |

Contrast: #002920 on #7BEFB2 11.08:1 (button text); #015945 on white 8.35:1; #015945 on #7BEFB2 5.89:1; black on #DCDDDE 15.44:1; **#02A67F on white 3.1:1 (large/graphic use only)**.

## 5. Depth & material
Flat vector. Swatches are 187 px circles (`border-radius:50%`), and the white swatch gets the only box-shadow (`0 3px 13px -1px rgba(100,100,100,.2)`). Photography is shown in a three-up strip with a white card on grey. Buttons are fully rounded (200 px radius), no outlines.

## 6. Components & patterns
Download button (mint pill, 119×53, "Last ned"); chapter label/content row; logo variants grid (6 tiles: mint-on-green, green-on-mint, white-on-green, green, black-on-white, white-on-black); clearspace diagram; subtitle logo variant ("Utvikling") on request; shape scale ladder; 3×4 allowed/forbidden combination matrix with red ✕ and green ✓; icon sheet with 3 colourways on dark, mint and green; 24×24 pixel grid with keylines; co-branding strip with partner logos (Statens legemiddelverk, Direktoratet for e-helse, FHI); templates (video, PowerPoint, Word, envelope, report); a long "Profilen i bruk og inspirasjon" chapter.

## 7. Motion
Real values from the census: link underline `text-decoration 0.2s ease-in-out` (44 uses) and button `background, color 0.15s cubic-bezier(0, 0.6, 0.88, 1)` (15 uses), a snappy ease-out. Brand statements say the icons suit animation and the logo may be centred on an "animated end slate". No motion spec is given.

## 8. Brand system
**Chapters (nav order):** Index → Kontaktinfo → Brand Canvas (download) → Konsept ("Knytninger") → Logo (primary, variants, Symbol, clearspace, subtitle logo) → Designelement (system, Skala, forbidden combinations) → Fargepalett (Primærfarger, Gråtoner, Støttefarger, skin tones) → Typografi → Illustrasjon → Ikonstil (+ Grid) → Fotostil → Co-branding (min distance) → Maler → Profilen i bruk og inspirasjon (website, newsletter, brochure, annual report, roll-up, T-shirt, coffee cup, lanyard, front-page layout, poster).
- **Concept:** NHN connects Norwegian healthcare; values: curious, driven, caring. The identity is "entrepreneur DNA" and meant to let other actors in the sector shine.
- **Logo rules:** symbol plus lowercase-initial wordmark. Preferred position: top or bottom **left**, never right; centred allowed for animated end slates. **Clearspace = the height and width of 50% of the symbol** on all sides (drawn with ghost pills, cf. Slack). Variants: dark green, mint-on-green, white, black. Co-branding: black or white only, with minimum spacing drawn as ghost units.
- **Design element:** three primitives (pill, circle, square), five density steps from two large forms to a fine mosaic. Forbidden: half-and-half pill splits, overhanging combinations. Allowed combinations are shown in 9 tiles.
- **Icons:** 24×24 grid, rounded keylines, filled glyphs inspired by Material; one-colour on green, mint or dark.
- **Skin tones** only for illustration. Support palette has "more values" in a downloadable full palette.
- **Token decisions worth stealing:** the 14.4 px multiplier scale; 50%-symbol clearspace; pill primitives as both logo and pattern; skin tones as a named palette.

## 9. UX
Highly practical: each asset has a download button and each chapter is anchored. Contact is a single mailbox. Weaknesses: the intro video errors, the dense label column leaves wide empty gutter on desktop, body text is a thin 300 weight, and the long single page has no sticky chapter nav after the hamburger.

## 10. Craft signals
- Clearspace expressed as a function of the symbol (50%), with the drawing.
- Type scale from a single 14.4 px base.
- Pill, circle and square primitives reused in logo, pattern, icons and buttons.
- Alternating grounds replace dividers.
- Allowed/forbidden matrix presented as a 3×4 grid with symbols.
- Colour specs give HEX+RGB for neutrals and HEX+CMYK for coloured swatches.
- Download buttons carry the same 200 px radius and 0.15 s transition everywhere.

## 11. Reproduction recipe
```css
:root{--nhn-ink:#002920;--nhn-mint:#7befb2;--nhn-green:#015945;--nhn-teal:#02a67f;--nhn-tint:#c4f2da;
 --g1:#f1f2f2;--g2:#dcddde;--base:14.4px;--font:"Helvetica Now","Helvetica Neue",Arial,sans-serif}
body{font:300 var(--base)/1.45 var(--font);color:#000}
.lead{font-size:calc(var(--base)*1.25);line-height:1.45;letter-spacing:-.2px}
h3{font:600 calc(var(--base)*2.25)/1.1 var(--font)}
h1{font:600 calc(var(--base)*3.5)/1.25 var(--font);letter-spacing:-1px}
.row{display:grid;grid-template-columns:452px 1fr;padding:56px 86px}
.row:nth-child(odd){background:var(--g1)}
.btn{background:var(--nhn-mint);color:var(--nhn-ink);border-radius:200px;padding:16px 22px;font-size:16px;transition:background .15s cubic-bezier(0,.6,.88,1),color .15s cubic-bezier(0,.6,.88,1)}
.swatch{width:187px;aspect-ratio:1;border-radius:50%}
.clearspace{padding:calc(var(--symbol-w)*.5)}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 7 | Fresh mint on deep green with friendly shapes; plain layout. |
| Originality | 6 | The pill-based connection concept is distinctive; page frame is Brandpad standard. |
| Usability | 8 | Downloads per asset, hex+CMYK, clearspace, forbidden examples, templates, contact. |
| Craft | 7 | Systematic scale and shapes; video error and thin light body text. |

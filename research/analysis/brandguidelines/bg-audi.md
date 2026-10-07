---
id: bg-audi
source: brandguidelines
category: guideline
status: analyzed
title: "Audi CI Portal (styleguide) — Renewed Brand"
creator: "AUDI AG (in-house; Frontify-hosted portal)"
styles: [corporate-clean, minimal-swiss, dark-premium, photo-led, hairline-ui]
patterns: [dark-charcoal-left-nav-accordion, hero-video-with-circled-play, slider-demo-of-variable-assets, rings-line-weight-variable, wide-extended-width-headline-type, donts-grid-with-diagonal-strike, download-row-with-file-size, per-language-font-downloads]
mode: mixed
palette: ["#333333", "#000000", "#ffffff", "#f2f2f2", "#b8b8b9", "#1b1b1c", "#101319", "#181d25"]
type_families: ["Audi Type Wide 400/700", "Audi Type Extended 400", "Audi Type 400", "Audi Type Variable (wdth 120–130, wght 230–700)", "AudiRings variable (line weight)", "Diatype / Space Grotesk Frontify (portal fallback)", "Verdana (official system fallback)"]
type_class: [geometric-sans, variable, grotesk]
radius_px: [4, 8, 999, 9999]
motion: {durations_s: [0.075, 0.15, 0.2, 0.25, 0.3, 0.35, 0.5], easing: ["cubic-bezier(0.4,0,0.2,1)", linear, ease-in-out, ease], loop: false}
scores: {aesthetics: 8, originality: 8, usability: 6, craft: 7}
craft_signals: [variable-rings-with-thickness-slider, extended-width-130-headline-rule, wide-font-as-wordmark-companion, sentence-case-lowercase-only-rule, dont-tiles-diagonal-strike, language-specific-font-packages, archived-render-keeps-grid, per-file-download-size-shown]
anti_patterns: [mobile-heading-breaks-mid-word, cookie-wall-captured-instead-of-content, grey-label-on-white-1.98, requested-url-redirected-to-different-site, left-nav-duplicates-in-tall-capture]
---
# Audi CI Portal (styleguide) — AUDI AG

## 1. Snapshot
- **Subject:** The Audi "Corporate Identity" portal, captured from `styleguide.audi.com` (the CI portal, document 1811 on Typography), not from the requested `www.audi.com/ci/en/renewed-brand.html`. site_meta marks `archived: true` and `captured_from: styleguide.audi.com`. The requested audi.com URL redirects to a German 404 page ("Oops, Seite nicht gefunden"), so the census sub2 (audi.com) is a 404, and the two audi.com tiles (d02 cookie wall in German, d03 Audi Media Center "Images", d04 "Information on accessibility") belong to the audi.com site, not to the guideline. Only the home page and sub1 (Typography) are the real guideline.
- **Why it's remarkable:** It positions the 2023 renewal as "Redefining Progress" and shows each brand asset as a variable: Audi Rings with a line-thickness slider (Light, Medium, Standard) and Audi Type Variable with weight and width sliders. The CI portal calls itself a "living styleguide" in React components.

## 2. Composition & layout
- **Left navigation (0–280 px):** charcoal #333333 panel, full height. Audi rings logo at (25, 50), 90×32 px, search field below, then an accordion of 11 groups (Brand Appearance, Basics, User Interface, Communication Media, Corporate Branding, Motion Pictures, Co-Branding, Brand in Space, Audi Motorsport, Dealer Facility, Updates, FAQ). Each row is 41 px tall with a 1 px hairline divider (#4a4a4a), 14 px label and a chevron. In the Basics group the sub-pages are Rings, Brand Claim, Colours, Typography, Layout Structure, Imagery, Illustration, Icons, Animation, Tone of Voice and Sound. A circular "DE" language switch (24 px) sits at the bottom. The sidebar repeats in the tall screenshot tiles because it is fixed.
- **Content canvas (280–1440):** a full-bleed 1160×653 px hero (video still with a circled play button, 74 px) followed by a white reading area with ~48 px padding. The title is 48 px Audi Type Wide, with body copy at 18/32 px in #333, ~1010 px wide.
- **Feature rows:** a 577×385 px dark media tile at x=328 and text at x=1001 (heading 28 px, body 18/32.4, link "More about Audi Rings >"), with 96 px between rows.
- **Typography page:** 653 px black hero with a giant grey "Aa" (about 600 px tall) cropped at the right edge and the 48 px page title overprinting it. Below: sections for "Flexible Typography", "Audi Type Variable", download rows (grey #f2f2f2 bars with a 16–24 px title, "ZIP 1.48 MB" and a 44 px circular download button), international typefaces, and "Don't"s as a three-column grid.
- **Footer:** black "Your CI-Support" band with a white "Contact us" button (158×58 px, square corners), then Legal / Imprint / © 2026 AUDI AG.
- **Mobile (390):** collapses to a charcoal header (logo, Search, burger), the hero, and the 48 px heading "Redefinin / g / Progress" breaking mid-word, a clear flaw because Audi Type Wide is too wide for the column at 390 px.

## 3. Typography
Census (home): "Audi Type Wide" 400 and 700, "Audi Type Extended" 400 and "Diatype" as portal fallbacks. Typography sub-page also loads **Audi Type 400**, **AudiVariableFont (wght 100–1000)** and **AudiRings (variable)**.
- **Scale:** 48 px (page titles, lh 57.6 px = 1.2; hero "Typography" at 60–64 px lh 60–77), 28 px headings (lh 44.8 = 1.6), 18 px body (lh 32.4 = 1.8, very open) or 27 px lh in lead, 14 px nav/labels (lh 22), 12 px captions (lh 16–19). Weights are essentially 400, with 700 used four times. Tracking is `normal` everywhere (a single 0.05px).
- **Rules (from the page):** headlines use **Audi Type Extended** at font width **130** (down to 120 at minimum); weight can be set freely from Normal to Bold. CSS in the stylesheet shows `font-variation-settings: "wdth" 130, "wght" 230/300/400/550/700`. Audi Type fonts "are not assigned to any particular vehicle model" and establish hierarchy via style.
- **Don'ts shown:** no uppercase, no outline, no colour underlay (a white bar behind the text), no vertical text, no letter-spaced lowercase, no coloured text (red). So the voice is lowercase sentence case in white.
- **Internationalisation:** downloadable language fonts: Audi Chinese Font (DF King Gothic, 12.16 MB zip), Audi Korean Font (13.02 MB, DFK Gothic), Audi Type Vietnamese (401 KB), Audi Type Arabic (136 KB), Non-Latin Characters (PDF, 50 KB). Fallback system font: **Verdana**. The audi.com site itself uses "Audi Type Variable, Verdana, Geneva, sans-serif" at 14/20.4 and 16/24.

## 4. Colour
| Hex | Role | Approx share (palette.json) |
|---|---|---|
| #ffffff | content ground | 37–58% of home tiles |
| #333333 | nav, body text (59 nodes) | 19–20% |
| #000000 | hero, black blocks, footer | 15–30% |
| #b8b8b9 | nav labels and muted text (23 nodes) | small |
| #f2f2f2 | download rows, spec boxes | ≈6% of Typography tiles |
| #757575 / #999999 | meta text, grey "Aa" in hero | small |
| #1b1b1c / #111110 | dark panels | 6% |
| #101319, #181d25, #2c343f | audi.com dark UI (media center) | full pages |
| #eb0a1e-style red (not in palette) | used in "A night out in style" don't example (red wordmark "Audi") | accent only |

The guideline section is practically monochrome: black, white and greys; colour comes from photography. The "Colours" page is not captured. audi.com's media centre pages use a navy-black #101319 with text #fcfcfd (alpha 0.7 for secondary).

**WCAG (contrast.py)**
- #333333 on white: 12.63:1. White on black: 21.0:1.
- Nav label #b8b8b9 on #333333: 6.37:1 (passes). The same grey on white is **1.98:1 (fail)**, which is how captions or breadcrumbs would read if placed on a white surface.
- #757575 on #f2f2f2 (file-size labels): 4.12:1 (fails AA for 12 px).
- audi.com media center: #fcfcfd on #101319 18.14:1; on #181d25 16.5:1.

## 5. Depth & material
- Flat. The only shadow in sub1 is a soft `0 4px 24px rgba(17,17,16,.2)` for the floating print button (60 px white tile with a printer icon, radius 8 px). On audi.com: `0 2px 8px rgba(0,0,0,.25)` and a heavy `0 16px 28px / 0 25px 55px` modal shadow on the cookie dialog.
- Depth is photographic: black silhouettes against a wide bright projected screen, car shots in dusk light.
- Rings are shown as thin white strokes (line weights from light to standard) on black, so the logo itself is "material": thickness is an expressive variable.

## 6. Components & patterns
- **Accordion nav** with hairlines; active child in bold white.
- **Slider demos** inside a black tile: a track with a 20 px circular handle and three labelled stops (Audi Rings Light / Medium / Standard); Audi Type Variable's Weight and Width sliders next to four stacked "Audi" words.
- **Download row:** #f2f2f2 bar, title 16–24 px, description 11–12 px, "ZIP" and size at right, 44 px outlined circular icon button.
- **Don't tile:** a photograph with the sample type and a thin blue (#1e90ff-like) diagonal strike line across the tile, caption below in 16 px.
- **Pill controls:** audi.com uses 999 px pills (search field, "View collection", "All albums").
- **Hero video** with a thin 74 px circle play icon.

## 7. Motion
Census transitions: `transform 0.15s cubic-bezier(0.4,0,0.2,1)` (×11), `all 0.2s linear` (×8), `background 0.2s linear` (×7), `all 0.2s ease-in-out` (×5), opacity 0.3 s and 0.5 s `cubic-bezier(0.4,0,0.2,1)`, `all 0.15s cubic-bezier(0.4,0,0.2,1)` (×9), `opacity 0.075s`, `transform 0.25s ease`. On audi.com, `all, outline, outline-offset 0.25 s / 0.35 s cubic-bezier(0.4,0,0.2,1)`. All are standard Material-style ease-in-out curves. The portal has an Animation page and a "Motion Pictures" group (not captured). The slider demos imply live variable-font and ring animation.

## 8. Brand system
- **Positioning:** "Redefining Progress", "progressive premium", **Vorsprung durch Technik** claim (set small with "Audi" in red, in the "She has a dream" poster example). The attitude is a "high degree of flexibility and the bold use of basic elements".
- **Highlights on the home page:** Flexible Rings (line thickness varies for scenarios and moods), Flexible Typography (Audi Type Variable), Adopting Core Components (Audi React Library, MVP).
- **Rings:** the four interlocking rings are shown as a thin outline drawn white on black; variants Light, Medium, Standard.
- **Menu groups (document order):** Brand Appearance · Basics (Rings, Brand Claim, Colours, Typography, Layout Structure, Imagery, Illustration, Icons, Animation, Tone of Voice, Sound) · User Interface · Communication Media · Corporate Branding · Motion Pictures · Co-Branding · Brand in Space · Audi Motorsport · Dealer Facility · Updates · FAQ.
- **Layout examples:** posters and ads with the rings top-left (≈ 65 px wide in a 510×740 tile), white headline in Audi Type Wide Bold at about 60 px lowercase sentence case over photography ("She has a dream", "Straight out of life", "Always connected"); small bottom-left claim.
- **Support:** Contact us, a CI-Support band; a PDF and zip package per resource.

## 9. UX
- Strong: sticky left accordion shows full structure; each guideline pairs an interactive demo with a download; international fonts are downloadable per language, with licence notes ("Any included Latin characters must never replace Audi Type").
- Weak: the requested URL resolves elsewhere; part of the capture is a German cookie wall and media-centre pages that are not guidelines; mobile heading breaks mid-word; 12 px grey file sizes under 4.5:1; the portal is gated and partly login-based, so most pages (Colours, Layout Structure, Tone of Voice) are not visible in this snapshot.

## 10. Craft signals
- Rings and type are shown as parametric (slider) assets, not static logos.
- Headline width rule is numeric (wdth 130, minimum 120).
- "Don't" examples are shown on one photo, repeated six times, with one variable changed each time.
- Download rows show file type and size (ZIP 1.48 MB, 401 KB).
- Open body leading of 1.8 gives long texts a calm, premium rhythm.

## 11. Reproduction recipe
```css
:root{
  --audi-black:#000; --audi-charcoal:#333; --audi-grey:#b8b8b9; --audi-surface:#f2f2f2; --audi-white:#fff;
  --font-head:"Audi Type Extended","Audi Type Wide",Verdana,sans-serif;
  --font-body:"Audi Type",Verdana,sans-serif;
}
body{font:400 18px/1.8 var(--font-body);color:var(--audi-charcoal)}
.side{position:fixed;inset:0 auto 0 0;width:280px;background:var(--audi-charcoal);color:var(--audi-grey)}
.side li{height:41px;border-bottom:1px solid #4a4a4a;font:400 14px/22px var(--font-body)}
.hero h1{font:400 48px/1.2 var(--font-head);font-variation-settings:"wdth" 130,"wght" 400;color:#fff;text-transform:none}
h2{font:400 28px/1.6 var(--font-head);font-variation-settings:"wdth" 130,"wght" 400}
.download{background:var(--audi-surface);display:grid;grid-template-columns:1fr auto 44px;padding:32px 80px;font:400 24px var(--font-body)}
.download .size{font-size:12px;color:#757575}
.btn-circle{width:44px;height:44px;border:1px solid #333;border-radius:50%;transition:all .15s cubic-bezier(.4,0,.2,1)}
.rings{stroke:#fff;fill:none;stroke-width:var(--ring-weight,6)}   /* animate with a slider */
.dont::after{content:"";position:absolute;inset:0;background:linear-gradient(to top right,transparent 49.7%,#1e90ff 50%,transparent 50.3%)}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Black/white/charcoal restraint with cinematic photography and a huge cropped "Aa"; very premium. |
| Originality | 8 | Variable rings and variable type shown as live sliders. |
| Usability | 6 | Clear navigation and downloads, but the capture is partial (cookie wall, wrong site), mobile headings break and small grey text fails AA. |
| Craft | 7 | Consistent hairlines, numeric type-width rule, language packages; poor mobile fit and tonal labels. |

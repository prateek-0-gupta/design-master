---
id: bg-ebay-playbook
source: brandguidelines
category: guideline
status: analyzed
title: "eBay Playbook (eBay Evo)"
creator: "eBay Design (in-house)"
styles: [corporate-clean, playful-rounded, photo-led, flat-illustration, maximalist-color]
patterns: [giant-tight-hero-headline, rounded-24-media-cards, 136-colour-8-shade-grid, side-nav-with-lock-icons, on-this-page-jump-grid, colour-tile-per-guideline-section, proprietary-typeface-specimen-tile, themed-colour-icon-stage]
mode: light
palette: ["#191919", "#ffffff", "#f7f7f7", "#707070", "#0968f6", "#f02d2d", "#fdbb13", "#92c821", "#e3f13c", "#b46bf0"]
type_families: ["Market Sans 400/600/700 (proprietary, eBay)"]
type_class: [neo-grotesk, geometric-sans]
radius_px: [8, 12, 16, 24, 64, 9999]
motion: {durations_s: [0.15, 0.3, 0.4, 0.5, 0.6, 0.75], easing: [ease, ease-out, "cubic-bezier(0.65,0,0.35,1)", "cubic-bezier(0.25,1,0.5,1)", "cubic-bezier(0.33,1,0.68,1)"], loop: false}
scores: {aesthetics: 8, originality: 7, usability: 8, craft: 8}
craft_signals: [measured-negative-tracking-on-display, 136-colour-token-ladder, dark-mode-toggle, gated-sections-lock-icon, on-this-page-grid, role-tokens-foreground-background, pill-and-24px-card-radii, accessible-pair-labels-AAA-AA]
anti_patterns: [video-player-error-in-capture, gated-best-practices-locked, grey-lead-paragraph-small-body]
---
# eBay Playbook (eBay Evo) — eBay Design

## 1. Snapshot
- **Subject:** playbook.ebay.com, the public brand-and-design-system site for "eBay Evo". It is a **marketing-style landing page plus guideline subpages** (Foundations, Logo, Color, Typography, Photography, Iconography). site_meta: requested `/`, final `/foundations/iconography/our-icons`, the last subpage crawled.
- **Why it's remarkable:** The home page is a poster built from one 96–200 px bold headline ("One system for everyone to love.") and large rounded colour media cards. The system then demonstrates itself: an 8-step × 17-family colour grid, a typeface specimen on a #0968f6 blue tile, an icon stage on lime. Several video players show "Player error" in the capture, so the hero video and sub-page videos are not seen; that is a capture artefact, not part of the design.

## 2. Composition & layout
- **Home (1440 wide):** top bar with the "eBay Playbook" wordmark left, six centred 14 px semi-bold links (Get started, Foundations, Design system, Expressions, Resources, Articles) and three 40 px circular icon buttons (account, dark mode moon, search) at the right. Content margin is **32 px** each side (full-bleed cards run x=32 to x=1408).
- **Hero:** three-line headline at ~164/200 px, tracking −3.84 to −4.92 px, left aligned, spanning two thirds of the width, with ~120 px of white above. Below, a 2-column row: intro copy in 20 px at x=32 (about 330 px wide) and a video card at x=507 (901×507 px, radius 24 px). The next headings ("Inspired by how people discover.", "Powered by passion.", "Designed to evolve.", "Designed to scale the world.") are set at 96 px with −2.5 px tracking, each followed by a full-width card.
- **Cards:** 1376 px full-width media (yellow #fdbb13 portrait, 24 px radius), a 2-up pair (676 px each, 24 px gap) with phone mock-up and seller card on #f7f7f7, a purple illustration carousel (#b46bf0) with prev/next/play pills, a lime #e3f13c icon stage and an orange illustration beside a dark device photo. Rhythm: heading, copy, card, 80–100 px gap.
- **Sub-pages:** left rail (≈ 316 px wide, 14–18 px items, grouped Foundations > Logo/Color/Typography/Photography/Iconography/Illustration/Motion/Writing/Brand strategy/Accessibility, with chevrons and padlocks on gated pages), then a 1000 px content column at x=408. Each page opens with a 72 px H1, a 1 px hairline, a 20 px grey lead paragraph (~700 px measure), a 1000×560 media card, an "On this page" two-column jump list with arrows, and sections with 36 px H2 and a hairline.
- **Mobile (390):** single column, hero at ~54 px, cards full width at 358 px, burger menu. Spacing stays generous.

## 3. Typography
Census (home): one family, **Market Sans** (400, 600, 700 loaded; 600 ×32, 700 ×29, 400 ×24).
- **Display:** 200 px (×8), 164 px (×1), 96 px (×4), line-height 96 px (=1.0) on the 96 px; tracking −2.5 px (×8) and −3.84 px (×4), −4.92 px (×1) which is about −0.025em to −0.03em.
- **Heading:** 72 px H1 (sub-pages, 72/72), 46/40.94 for the wordmark, 36/46 for H2, 24/32 for cards (39 uses on home), 20/28 for leads.
- **Body:** 16/24, 14/20 (36 uses on logo and colour pages), 14 px for nav at 600 weight.
- **Colour:** body #191919 (52 uses), lead and meta in #707070 (44 uses on subpages).
- **Rules from the Typography page:** "bold yet approachable"; use both Bold and Regular weights in all applications; the page shows an anatomy of the "Aa" (white outline with bezier points) on blue, a character set, support for other languages and a type tester. Market Sans has "simple, open geometric shapes".

## 4. Colour
| Hex | Role | Approx share |
|---|---|---|
| #ffffff | page ground (palette tile 4: 95%) | 58–95% |
| #f7f7f7 | card and footer ground (neutral-100) | 22 backgrounds on home |
| #191919 | text (neutral-900), logo wordmark | 52 text nodes |
| #707070 | secondary text | 44 on subpages |
| #0968f6 (B500) | Blue: accent, typeface tile, primary action | — |
| #f02d2d (R500) | Red | — |
| #fdbb13 (Y400) | Yellow: hero portrait, illustration | 10–12% of tiles 1–2 |
| #92c821 (G500) | Green | — |
| #e3f13c (avocado 400) | Lime icon stage | one card |
| #b46bf0 | Purple illustration card | 14.7% of tile 5 |

The system has **17 colour families (including neutral) × 8 shades = 136 colours** (as stated on the page), and the four logo colours are the core: G500, B500, R500, Y400. Swatches are labelled "G500", with a darker tint of the family for the label (for example dark olive on green, dark brown on yellow) so each label stays readable. Tokens: `--color-foreground-*` / `--color-background-*` roles that point into the ladder (for example `--color-background-accent` → blue-500, `--color-blue-650 #003aa5` as the link and focus blue). A dark-mode toggle swaps neutral-0/neutral-8 and neutral-900.

**WCAG (contrast.py)**
- #191919 on white: 17.58:1. #707070 on white: 4.95:1 and on #f7f7f7: 4.62:1 (passes AA, narrowly; the doc keeps muted copy at the AA floor).
- #0968f6 on white: 4.86:1 (white text on B500 passes AA). Link blue #003aa5 on white: 9.77:1.
- #191919 on yellow #fdbb13: 10.29:1; on lime #e3f13c: 14.16:1. The system pairs dark text on bright families rather than white.
- The mobile sheet shows "AAA / AA" labels on tint tiles, so the colour page publishes the grade for each accessible pair.

## 5. Depth & material
- **Cards, not shadows, make the layout:** a 24 px radius card on #f7f7f7 or a saturated field. Real shadows exist only on UI mock-ups and overlay surfaces: `0 4px 16px -2px rgba(0,0,0,.15)` (×5), `0 4px 12px rgba(0,0,0,.07)` (×4), `0 4px 15px rgba(0,0,0,.15)` (×3), and a two-layer `0 5px 17px rgba(0,0,0,.2), 0 2px 7px rgba(0,0,0,.15)` (×2).
- Photography brings warmth: golden portrait on #fdbb13, interior lifestyle shots, product shots on grey.
- Illustration is flat vector with a soft inner shading (car on a lift, comic book, a robot toy), set on saturated grounds.

## 6. Components & patterns
- **Buttons:** outlined pill "See what's new" (≈165×50 px, 1 px #191919-ish border, 9999 px radius); circular 40 px icon buttons; white 24 px-padded pills on media ("Play video"). Primary buttons use `--color-foreground-accent` (blue) with `on-accent` text.
- **Nav rail:** active item on a #f7f7f7 chip with ~8 px radius; chevron expanders; padlock icon next to gated pages ("Best practices", "Writing", "Brand strategy").
- **On this page:** a two-column grid of hairline rows, each with a label and arrow →.
- **Cards:** seller card (avatar 92 px, name 24 px bold, "98% positive", heart button), product card with four-dot carousel, search-bar overlay on a hero image ("animal print 1,400,000+ results").
- **Icon stage:** 50 line icons (about 40 px, 2 px stroke, round caps and joins, dark olive on lime) on a 10×5 grid; the home version shows seven icons in white circles of 228 px.

## 7. Motion
Real transitions from the census: `width 0.4s ease` (×17), `transform 0.6s ease` (×12), `background-color 0.4s ease` (×8), `translate, rotate, opacity 0.75s cubic-bezier(0.65,0,0.35,1)` (×7; the sticker/carousel flourishes), `opacity, visibility 0.15s ease-out` (×4, tooltips), `opacity, visibility 0.4s cubic-bezier(0.25,1,0.5,1)` and `grid-template-rows 0.3s cubic-bezier(0.33,1,0.68,1)` (nav accordions). A Motion foundation exists in the nav (not captured). Video and carousel have play/pause controls in the 40 px pill.

## 8. Brand system
This is a product-brand hub rather than a PDF, so the following is landing-page level.
- **Message:** "One system for everyone to love", tagline **Things.People.Love.** (set in the footer at ~46 px bold, tight). The page sells the system as inspired by discovery, powered by passion, designed to evolve, designed to scale.
- **Logo:** four-colour lowercase "ebay" (e red, b blue, a yellow, y green), explained as the source of the four core colours. Logo section topics: Identity, Clear space, Size (Scalability), Placement, Containers, Favicon, Avatar, Brand partnerships, Resources, Changelog. A footer variant sets the logo in #191919.
- **Section list (Foundations):** Logo (Our logo, Using our logo, Using our tagline, Best practices, Showcase) · Color (Our colors, Using color, in product, in marketing, in illustration, Best practices, Showcase) · Typography (Our typeface, Using type, in digital, in print, Best practices, Showcase) · Photography (Our photos, Visual tone, Image types, Listing imagery, Curation in layout, Best practices, Showcase) · Iconography (Our icons, Using icons, Program badges, Confirmation indicators, Icon library, Best practices, Showcase) · Illustration · Motion · Writing · Brand strategy · Accessibility. Some pages are gated (padlock).
- **Photography voice:** "real-life moments ... not manicured sets", with "everything has a story".
- **Iconography rules:** metaphorical (cart, heart, pencil, image, magnifier), platform specific, categories and characteristics.
- **Token decisions worth stealing:** an 8-step ladder per colour family with role tokens on top; label colour set to a dark tint of the swatch; both bold and regular weights only; 24 px card radius with 12/16 as intermediate.

## 9. UX
- Fast orientation: a three-level nav (top, rail, "On this page"), a hairline under every H1/H2, large type hierarchy.
- Weak spots: the lead paragraph is 20 px mid-grey (#707070), which is legible but low on emphasis; several pages are locked; video embeds fail in the capture and leave grey boxes; mobile cards leave large empty space between sections (tall white gaps in the sheet).

## 10. Craft signals
- Display tracking is set in px for each size (−2.5 at 96 px, −3.84 at ~150 px, −4.92 at 200 px), so the headline stays tight at every scale.
- Cards share one radius family (24/12/8) and a small shadow vocabulary.
- Swatch labels are tinted with their own family, not default black or white.
- Every guideline page repeats one template: H1, lead, media, "On this page", sections with hairlines.
- Accessible labels (AAA / AA) appear on colour pairs.

## 11. Reproduction recipe
```css
:root{
  --neutral-900:#191919; --neutral-0:#fff; --neutral-100:#f7f7f7; --muted:#707070;
  --blue-500:#0968f6; --blue-650:#003aa5; --red-500:#f02d2d; --yellow-400:#fdbb13; --green-500:#92c821; --lime:#e3f13c;
  --font:"Market Sans","Helvetica Neue",Arial,sans-serif;
  --r-card:24px; --r-chip:12px; --r-input:8px;
}
body{font:400 16px/24px var(--font);color:var(--neutral-900);background:#fff;margin:0 32px}
.hero{font:700 clamp(96px,14vw,200px)/.96 var(--font);letter-spacing:-.025em}
.h-section{font:700 96px/96px var(--font);letter-spacing:-2.5px}
h1.page{font:700 72px/72px var(--font)} h2{font:700 36px/46px var(--font)}
.lead{font:400 20px/28px var(--font);color:var(--muted);max-width:700px}
.card{border-radius:var(--r-card);background:var(--neutral-100);overflow:hidden}
.card--yellow{background:var(--yellow-400)} .card--lime{background:var(--lime)}
.pill{border:1px solid var(--neutral-900);border-radius:9999px;padding:14px 24px;font:400 16px var(--font);transition:background-color .4s ease}
.nav a{font:600 14px/20px var(--font)}
.shadow-ui{box-shadow:0 4px 16px -2px rgb(0 0 0/.15)}
.fade-in{transition:translate .75s cubic-bezier(.65,0,.35,1),opacity .75s cubic-bezier(.65,0,.35,1)}
.on-this-page a{display:flex;justify-content:space-between;border-top:1px solid #e5e5e5;padding:12px 8px;font:400 14px var(--font);color:var(--muted)}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Confident huge tight headline, saturated colour cards and playful illustration over lots of white. |
| Originality | 7 | The system-as-demo hero and 136-colour grid are strong, though the card layout is a trend. |
| Usability | 8 | Clear three-level navigation, "On this page" jump list, published contrast grades; locked pages and broken video hurt. |
| Craft | 8 | Per-size tracking, tinted swatch labels, consistent radii, role tokens, dark mode. |

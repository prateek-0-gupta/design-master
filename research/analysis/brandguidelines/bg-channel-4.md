---
id: bg-channel-4
source: brandguidelines
category: guideline
status: analyzed
title: "Channel 4 — 3rd Party Partner Guidelines"
creator: "Channel 4 Television Corporation (Media Assets portal)"
styles: [corporate-clean, gradient-mesh, minimal-swiss]
patterns: [single-signature-colour-arsenic-green, gradient-room-hero-banners, black-sidebar-with-green-active-chip, logo-colour-switch-by-background-lightness, print-vs-digital-colour-values, downloadable-asset-per-rule, cookie-banner-overlay]
mode: mixed
palette: ["#aaff89", "#000000", "#ffffff", "#f5f5f5", "#a5f585", "#fe647c", "#81c9fb", "#6687e7"]
type_families: ["4 Text (Channel 4 brand sans)", "4 Headline (hero titles, 60 px)", "Source Sans Pro (inline fallback)", "Inter (platform UI)"]
type_class: [geometric-sans, humanist-sans]
radius_px: [2, 4, 5, 8]
motion: {durations_s: [0.1, 0.2, 0.3, 0.5], easing: [ease, ease-in-out, "cubic-bezier(0.2,0,0,1)"], loop: false}
scores: {aesthetics: 7, originality: 6, usability: 7, craft: 6}
craft_signals: [logo-has-per-colour-optical-versions, exact-hex-rgb-cmyk-pantone-per-use, light-dark-logo-rule, chip-style-active-nav, gradient-hero-per-section]
anti_patterns: [cookie-banner-covers-content-and-button-white-on-green, sidebar-repeated-in-capture, download-links-blue-underlined-off-brand, low-contrast-manage-preferences-button]
---
# Channel 4 — 3rd Party Partner Guidelines — Channel 4

## 1. Snapshot
- **Subject:** Channel 4's hosted guidelines portal ("Media Assets" platform), guide "005. 3rd Party Partner Guidelines". `site_meta.json`: requested the guide root, final URL is a `/page/8a2dd59a…` sub-page (the "Colour" page); the home capture is the "Logo Guidelines / Overview" page. Live site, no archive.
- **Why it's remarkable:** The brand fits in one colour, Arsenic Green `#AAFF89`, plus black and white. The guide spells out when to use which logo version by background lightness and gives hex, RGB, CMYK and Pantone per use. The overview hero uses a soft 3D "gradient room" with the green 4 logo floating in it.

## 2. Composition & layout
- Top bar 110 px: centred asset search (600×40, 5 px radius, image-search icon), "Language" and "Login" at right, the black 4 logo at left (about 36 px wide). A second row (about 70 px) carries the guide title "005. 3rd Party Partner Guidelines" and "Copy link to guide".
- Left sidebar 270 px wide, solid black, white text at 16 px with 44 px row pitch. Section headers ("Logo Guidelines", "3rd Party Guidelines") are 18 px with a chevron; the active page is a green `#aaff89` pill 244×44 with black text.
- Content: a 400 px full-width banner (pink-red gradient on Overview, solid green on Colour) with a small section label (22 px) over a 60 px "4 Headline" page title and a "Copy link to page" action. Beneath, a `#f5f5f5` intro band with 22 px lead copy. Body then runs in a column starting at x≈456, with swatches in a 184×130 box at x≈1003.
- Mobile (390 px): header stacks (language/login, search, a hamburger with truncated title), the banner is 400 px, and a cookie panel covers the lower third.

## 3. Typography
- 4 Text (400 only in the census; 700 appears for bold phrases) at 14 px / 17.5 (15 uses), 16 px, 18 px / 22.5 and 22 px. Line-height is 1.25 throughout, which is tight for body.
- 4 Headline at 60 px, weight 400, for page titles; the title wraps to two lines on "Colour (Find the logos here)".
- Source Sans Pro appears on 7 body nodes in the Colour page (the inline CMS text), so the rendered text is a mix of the brand face and a fallback.
- Letter-spacing is `normal`; no scale tokens are published. The platform exposes `--fontSize200:18px`, `--fontSize600:28px`, `--fontSize700:32px`, `--fontSize800:36px`.

## 4. Colour
| Hex | Role | Approx share |
|---|---|---|
| #aaff89 | Arsenic Green (Masterbrand): banner, active chip, buttons | 20% of Colour tile |
| #a5f585 | altered green for logo on white (CMYK 33,0,46,4) | swatch |
| #000000 | sidebar, logo, headline text | 11–19% |
| #ffffff | page | 42–62% |
| #f5f5f5 | intro band | band |
| #fe647c / #fe7eb4 / #81c9fb / #6687e7 | gradient-room hero (pink to blue) | hero |
| #126dfe | download links | links |

Stated values: Arsenic Green hex #AAFF89, RGB 170,255,137; print Pantone 909 (Fluro); CMYK fallback 40,0,65,0.

Contrast: black on #aaff89 **17.37:1**; white on #000 **21:1**; white on #a5f585 **1.31:1** (the cookie "Manage Preferences" button is white on green and effectively unreadable); #126dfe link on white **4.52:1**.

## 5. Depth & material
Mostly flat. Depth lives in the hero imagery: blurred gradient "rooms" (a corridor with a red-pink ceiling fading to pink, and a blue room with a lit floor) in which the green logo sits. UI shadows are minimal: `0 1px 6px -2px rgba(0,34,51,.1)` and a 12 px blur on the floating Resources button.

## 6. Components & patterns
- Black sidebar tree with a green active pill.
- Colour-spec rows: text left, 184×130 swatch right (4 px radius), then HEX/RGB/CMYK in a small label table, and a blue "Download here" link.
- Pairing rule cards: Black logo on green, White logo on black, each 380×214, with the rule in two sentences.
- Floating dark "Resources" pill (about 130×48, 24 px radius) at lower right; prev/next chevrons at page foot.
- Collapse and scroll-top buttons next to the banner.

## 7. Motion
Platform transitions: `0.1s ease` on colour and background, `0.2s ease` and `0.2s ease-out` on transforms, `0.5s ease` for width/height of the sidebar, and `0.18s cubic-bezier(0.2,0,0,1)` on one control. The brand motion is addressed in a "Masterbrand Logo Animation" page that I did not capture.

## 8. Brand system
- **Colour:** Arsenic Green is the official Channel 4 colour and "one of our most distinctive assets". Use the digital-optimised green for most uses and a print-specific version for print. On white, use the altered **#A5F585** logo so it stays visible.
- **Logo rule:** the green logo is default. Black and white versions are exceptions that need brand-team approval. Black logo goes on lighter backgrounds, white on darker. "Never recolour" because each version is slightly different for optical balance.
- **Guide structure (sidebar):** Logo Guidelines: Overview, Our logo, Our name, Colour, Logo Position, Brand Partnerships, Minimum Sizes, Clearance, 4+1 and 4HD logos. 3rd Party Guidelines: Overview, Masterbrand Logo Animation, Logo Position, Logo use on images, App Tile. The captured nav repeats these blocks.
- **Voice:** direct, short sentences ("Never recolour").
- **Not verified:** clearspace numbers and minimum sizes live on pages not captured.

## 9. UX
Search by asset and a language switch make this a download-centred portal. Every rule has its asset link beside it. Issues: the cookie banner overlays the first content on both desktop and mobile; its button fails contrast; the same sidebar is rendered several times in the full-page capture; default blue underlined links break from the brand.

## 10. Craft signals
- One saturated signature colour with a stated digital and print variant and a stated "altered" variant for white.
- Logo versions exist per background colour for optical balance, not tinted by CSS.
- Contrast is excellent where black meets green (17.37:1).
- The active nav state uses the brand colour as a pill, not an underline.
- Hero banners vary per section but keep the same 400 px height.

## 11. Reproduction recipe
```css
:root{--c4-green:#aaff89;--c4-green-on-white:#a5f585;--ink:#000;--band:#f5f5f5;
  --font:"4 Text","Source Sans Pro",system-ui,sans-serif;--head:"4 Headline",var(--font)}
.sidebar{width:270px;background:#000;color:#fff;font:400 16px/1.25 var(--font)}
.sidebar a{display:block;height:44px;padding:0 36px;border-radius:5px;line-height:44px}
.sidebar a[aria-current]{background:var(--c4-green);color:#000}
.banner{height:400px;background:var(--c4-green);padding:0 185px;display:flex;align-items:flex-end}
.banner h1{font:400 60px/1.2 var(--head)}
.lead{background:var(--band);font:400 22px/1.2 var(--font);padding:24px 185px}
.swatch{width:184px;height:130px;border-radius:4px;background:var(--c4-green)}
a.download{color:#126dfe;font-weight:700;text-decoration:underline}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 7 | A single neon green on black and white is bold, and the gradient hero rooms are memorable. |
| Originality | 6 | The mono-colour system is distinctive; the portal chrome is a generic template. |
| Usability | 7 | Per-rule downloads and exact colour values; marred by the cookie overlay. |
| Craft | 6 | Optical logo versions and exact specs, but fallback fonts and off-brand links. |

---
id: bg-red-hat
source: brandguidelines
category: guideline
status: analyzed
title: "Red Hat Brand Standards"
creator: "Red Hat, Inc."
styles: [corporate-clean, minimal-swiss, flat-illustration, technical-wireframe]
patterns: [e-height-clearspace-rule, logo-a-b-c-hat-variants, red-50-pure-red-token, expressive-colors-never-alone, annotated-type-specimen, icon-30px-grid-125pt-stroke, tabbed-overview-swatches-accessibility, source-code-of-the-brand-headline, pill-link-getting-started-grid, ai-not-for-icons-rule]
mode: light
palette: ["#ee0000", "#151515", "#000000", "#ffffff", "#f2f2f2", "#0066cc", "#b1380b", "#1f0d3a"]
type_families: ["Red Hat Display (300–900)", "Red Hat Text (300–700 + italics)", "Red Hat Mono (300–700)"]
type_class: [geometric-sans, humanist-sans, mono]
radius_px: [6, 16, 30, 64]
motion: {durations_s: [0.3], easing: [ease, ease-out], loop: false}
scores: {aesthetics: 8, originality: 7, usability: 9, craft: 9}
craft_signals: [clearspace-defined-by-letter-e, 12-degree-angle-system-in-type-and-icons, icon-circle-overshoot-1px, cmyk-rgb-hex-pantone-all-listed, do-and-dont-thumbnails-with-red-strike, tokenised-css-rh-color, open-source-fonts-sil, dashed-underline-inline-links]
anti_patterns: [chat-widget-overlaps-content, gated-downloads-behind-login, red-text-4.5-on-white-borderline, sidebar-only-to-900px-height-in-capture]
---
# Red Hat Brand Standards — Red Hat, Inc.

## 1. Snapshot
- **Subject:** Red Hat's live brand standards site at `redhat.com/en/about/brand/standards`. `site_meta.json`: requested `/standards`, final URL `/standards/resources` (Templates) after crawling six subpages: Hybrid style handbook, Red Hat logo, Color, Fonts and typography, Icons, Templates. No archive. The sidebar also lists Foundations, Design language (Color, Fonts and typography, Photography, 3D, Illustration, Iconography), Handbooks, Resources and What's new.
- **Why it's remarkable:** Treats the brand as code ("This is the source code of the Red Hat brand."). It uses real design tokens (`red-50`, `--rh-color-*`), an open-source font family, geometry-defined clearspace (the height of the letter "e"), and rules that go down to 1.25 pt strokes on a 30 px icon grid.

## 2. Composition & layout
- Global site header 82 px: logo, six mega-menu items (14–16 px), utilities (Console, Docs, Support) and search/bell/user icons.
- Left sidebar 240 px, grey `#f2f2f2`, with a collapsible tree (Foundations, Logos, Design language, Handbooks, Resources, What's new). Active item is a white pill with a 3 px red left bar. The grey ends at 900 px in the capture (it is sticky, so the capture's lower tiles show white).
- Content column: left edge x≈336, text measure about 700 px, wide specimens to x≈1408.
- Home: 576 px photographic hero (a red wall in an office lobby), a 64 px red display headline, two short paragraphs, then 8 pill links in a 4×2 grid (each about 245×58, radius 64 px, blue text), then a black full-width feature band, and four alternating text/graphic rows (each graphic about 520×262 with 30 px outer radius).
- Sub-pages: H1 at 36 px, intro, then a tab bar (Overview / Color swatches / Accessibility; Font family / Typography / Download fonts) with a 3 px red top border on the active tab.
- Mobile (390 px): header collapses to icons, a "Brand standards" dropdown replaces the sidebar, pills stack to full width, headline wraps in red at 64 px.

## 3. Typography
Census (home) and loaded fonts: Red Hat Display 300–900, Red Hat Text 300–700 (+italic), and Red Hat Mono on the Color/Type pages.

| Role | Spec |
|---|---|
| Home hero | Red Hat Display 500, 64 / 83.2 (1.3), red |
| Section statement | Display 500, 48 / 62.4 |
| Page H1 | Display 500, 36–60 |
| H2 | Display 500, 28 / 36.4 and 24 / 31.2 |
| Body | Red Hat Text 400, 18 / 27 (53 uses on sub pages) and 16 / 24 |
| Small | Text 14 / 21 and 12 / 16 |
| Code / values | Red Hat Mono 500, 14 / 21 |
| Link / button | Display 700, 16 / 24 |

Leading is 1.3 in headings and 1.5 in text. The type page annotates Display with callouts (wide letters, open apertures, tall x-height, tight spacing, even strokes, circular forms, natural curves, a 12° angle). Display is the default; "if you're not sure which font, default to Display". Fonts are free under the SIL licence.

## 4. Colour
| Hex | Role | Approx share |
|---|---|---|
| #ee0000 | Red Hat red, `red-50`; RGB 238,0,0; CMYK 0,98,85,0; Pantone 1788 C | accent, headline |
| #151515 | body text (54 of 76 text nodes), footer | text |
| #000000 | core black (CMYK 60,40,40,100) | feature bands |
| #ffffff | core white | page |
| #f2f2f2 | sidebar, cards, footer note | surface |
| #0066cc | links and CTAs | interactive |
| #b1380b | dark orange text | callouts |
| #1f0d3a-ish deep purple | specimen and photo-card panels | feature panels |
| #fce3e3 | light red tint | specimen panels |

Color page: red tint ladder of 4 lighter and 3 darker steps around #ee0000 (the darkest near #3d0000), a 12-step neutral ladder from white to black, and "expressive colors" which are "always used in addition to core colors and never on their own".

Contrast: #ee0000 on white **4.53:1** (passes AA for normal text barely); black on #ee0000 **4.64:1**; #0066cc on white **5.57:1**; #151515 on white about 18:1. White on red is the same 4.53:1.

## 5. Depth & material
Flat, with no box shadows in the census (`shadow {}`). Depth is in photography and the 3D red hat renders on the black band. Surface layering uses grey `#f2f2f2` cards with 16–30 px radii and a dark purple panel for specimens.

## 6. Components & patterns
- Pill CTA grid (radius 64 px, 1 px grey outline, blue label).
- Alternating media rows: left heading plus link, right 520×262 rounded card (30 px top-right/bottom-right corners shape).
- Logo-variant tabs (Logo A, Logo B, Logo C, The hat) with a clearspace diagram in which four "e" glyphs mark the margins.
- Do/don't thumbnails: 4 cards, bad ones outlined in orange with a diagonal strike.
- Swatch rows: 8 red and 11 grey chips (about 90×84, radius 16 px), the core red chip spans wider.
- Icon sheet: 20 red line icons on a pink `#fce3e3` panel, then three annotated cards (Grid and stroke, Angles, Key lines).
- Chat launcher bottom right (overlaps content in captures).

## 7. Motion
Minimal: `all 0.3s ease` and `background 0.3s ease-out` on cards and links. No motion chapter among the captured pages.

## 8. Brand system
- **Logo:** a red hat plus the bold wordmark, set in the open-source font. Introduced in 2019 with the Open Brand Project. Three versions: A (preferred, wide spaces), B, C (specific circumstances) and the hat alone. **Clearspace:** minimum is the height of the letter "e" on all sides ("More is better"). Black, red, and white/reversed variants are shown on dark, light and red backgrounds. White hat on red.
- **Colour:** "Not just any red": pure red, no blue or green. Red "commands attention, so use it wisely", with pops of `red-50` in everything. Core = red, black, white plus tints and grey shades; Expressive = additional hues, never alone.
- **Type:** Display for headings, Text for body, Mono for code; open source.
- **Icons:** simple, clean, open; same stroke and corner radius; front view with flattened perspective; geometric shapes; 3 colours (red, black, white). 30 px grid, 1.25 pt strokes with rounded ends, angles 0°/45°/90° ±12° (matching the font's 12° ascenders), key lines with a circle overshooting a square by 1 px, saved with a 3 px margin to 36×36. Best at 32–128 px. Explicit rule: never use AI to generate icons.
- **Personality:** open, authentic, helpful and brave. Slogan: "No one innovates alone".
- **Structure:** Brand Standards home; Foundations; Logos (Red Hat logo, Product, Universal, Initiative, Event, Endorsement, Co-branding, Technical partner buttons); Design language (Color, Fonts and typography, Photography, 3D, Illustration, Iconography: Icons, Technology icons, UI icons); Handbooks (Hybrid style handbook); Resources; What's new. Feedback via a form or an internal Slack channel.

## 9. UX
Strong IA: a tree nav with persistent location, tab bars inside long pages, "Next topic" pill at foot, deep links. Barriers: downloads are gated behind login (lock icons), the chat bubble covers content, and the capture shows the sidebar grey only to 900 px.

## 10. Craft signals
- Clearspace defined by a glyph in the identity itself.
- A 12° angle is used in type ascenders and in the icon angle system.
- Every colour listed in hex, RGB, CMYK and Pantone.
- Icon overshoot rule (1 px) for optical sizing.
- Tokens exposed as `--rh-color-*` custom properties and as a named `red-50`.
- Do/don't cards for logo use with a consistent strike mark.
- Dashed underline on inline links distinguishes them from interactive CTAs.

## 11. Reproduction recipe
```css
:root{--rh-red-50:#ee0000;--rh-red-dark:#a60000;--rh-text:#151515;--rh-surface-lighter:#f2f2f2;
  --rh-link:#0066cc;--rh-link-hover:#003366}
body{font:400 18px/1.5 "Red Hat Text",sans-serif;color:var(--rh-text)}
h1,h2,h3{font-family:"Red Hat Display",sans-serif;font-weight:500;line-height:1.3}
.hero-title{font-size:64px;color:var(--rh-red-50)}
code,.spec{font:500 14px/1.5 "Red Hat Mono",monospace}
.pill{border:1px solid #c7c7c7;border-radius:64px;padding:16px 40px;color:var(--rh-link);transition:all .3s ease}
.nav-active{background:#fff;border-left:3px solid var(--rh-red-50);border-radius:30px}
.tab[aria-selected=true]{border-top:3px solid var(--rh-red-50);background:#fff}
.clearspace{padding:1ex} /* the height of the letter e */
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Confident red/black/white with generous spacing and crisp specimens. |
| Originality | 7 | Brand-as-source-code and glyph-based clearspace; layout is a conventional docs site. |
| Usability | 9 | Clear IA, tabs, exact values and do/don't cards; gated downloads are a minor drag. |
| Craft | 9 | Token naming, 12° geometry across type and icons, pixel-level icon rules. |

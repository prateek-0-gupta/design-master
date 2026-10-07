---
id: bg-flax-kale
source: brandguidelines
category: guideline
status: analyzed
title: "Flax+Kale Corebook - Introduction"
creator: "Flax+Kale (hosted on Corebook)"
styles: [corporate-clean, monochrome, playful-rounded]
patterns: [corebook-left-sidebar-nav, single-ink-colour-page, wordmark-with-script-glyphs, next-section-footer-block, hierarchical-brand-architecture-nav, gem-icon-row]
mode: light
palette: ["#1618ab", "#ffffff", "#89ff6a", "#f1f2f7", "#15161b"]
type_families: ["Area Normal (Regular + Bold, embedded)", "Rubik (300-700, UI chrome)"]
type_class: [geometric-sans, display]
radius_px: [3, 6]
motion: {durations_s: [0.2, 0.3, 0.55], easing: [ease, ease-in-out], loop: false}
scores: {aesthetics: 7, originality: 6, usability: 6, craft: 6}
craft_signals: [single-ink-blue-on-white, logo-reused-as-hero-and-sidebar-mark, accent-green-for-active-nav, high-contrast-pair]
anti_patterns: [only-intro-page-captured, typo-in-copy, bootstrap-default-variables-left-in]
---
# Flax+Kale Corebook - Introduction — Flax+Kale (Corebook host)

## 1. Snapshot
- **Subject:** The Introduction page of the Flax+Kale brand book on the Corebook platform (my.corebook.io/flaxandkale). **Wayback Machine snapshot dated 2024-01-06 01:42:11** (from `captured_from`). The live book is not used.
- **Coverage (explicit):** a single page only. 1 desktop tile (1440×~1357 px) and 1 mobile sheet viewed. No subpages were captured, so logo rules, colours, typography and applications are NOT seen; what I know about them comes only from the sidebar labels (nav list in census).
- **Why it's remarkable:** A one-colour brand book. The entire page, including copy, uses a single electric blue on white, with a chartreuse-green highlight for the active nav item, and a custom wordmark mixing heavy condensed capitals with a looping script "a" and "e".

## 2. Composition & layout
- Fixed left sidebar 240 px wide (blue #1618ab), logo at top (white, ~170 px wide, stacked FLAX+/KALE), nav tree below with section headings (General Information, MASTERBRAND, HOSPITALITY, DELIVERY...) and indented 12 px links.
- Main area (x 240-1440): row of four thin grey gem outlines (diamond, pyramid, faceted square, octagon) at y≈100, spaced ~77 px; a huge blue wordmark ~890 px wide at y 300-510; then four 25 px intro paragraphs left-aligned at x≈305 with ~33 px leading; footer "NEXT / General Information / Flax+Kale" as a full-width blue block (y 1165-1357) with a 12 px chevron at right.
- Mobile (390 px): top bar with hamburger and small logo, single column, wordmark scaled to full width (~360 px), paragraphs at about 22 px.

## 3. Typography
- Area Normal Regular for the body (20-25 px), Area Normal Bold used for sidebar labels (12 px / 15.6 px line height, 38 uses). Rubik loaded for 12-24 px chrome.
- Census (px / weight / line-height): 25/500/32.5 (7 runs), 24/400/28.8, 20/400/28, 16/300/22.4, 14/500/17, 12/400-700/15.6. Letter-spacing is normal everywhere. Only lowercase/sentence case in nav, uppercase for section heads (MASTERBRAND etc.).

## 4. Colour
| hex | role | approx share |
|---|---|---|
| #ffffff | content ground | 62% of the tile |
| #1618ab | sidebar, all text, footer block, wordmark | 23% |
| #89ff6a | active nav / section title in sidebar | <1% |
| #f1f2f7 | faint hairlines / tints | 3% |
| #15161b | dark overlay (modal), small | trace |
| grey #999999 approx | gem icons | trace |

- Contrast: blue on white **11.98:1**; chartreuse #89ff6a on blue **9.46:1**; white on blue **11.98:1**. All copy therefore passes AAA.
- CSS custom properties are Bootstrap 4 defaults (#007bff etc.), not brand tokens; the brand colours live in Corebook's per-book theme.

## 5. Depth & material
- Flat. The only shadows in census belong to the platform chrome (`0 4px 20px rgba(0,0,0,.45)` for a modal, white glows for a hidden loader). No gradients.

## 6. Components & patterns
- Collapsible nav tree with a small triangle toggle, one heading per sub-brand (Masterbrand, Hospitality, Delivery...), "NEXT" footer card, hamburger drawer on mobile. Content blocks are plain H2 paragraphs.

## 7. Motion
- Census: `all .2s ease` (3), `opacity .2s`, `opacity .3s ease-in-out`, `all .3s ease-in-out`, `margin .55s ease-in-out` (sidebar collapse), `all .4s ease`. No custom beziers; no brand motion captured on this page (a "Motion Graphics" subpage exists in the nav but was not captured).

## 8. Brand system
- From this page only: the wordmark FLAX+KALE with swash glyphs; the tagline "Eat Better, Be Happier and Live Longer"; the guide promises "downloadable assets and instructions of use".
- From the sidebar (labels only): General Information (Introduction, Flax+Kale, Brand Architecture, Flexi); Masterbrand (Overview, Logotype, Colors, Typography, Social Media, Audio Branding, Motion Graphics, Wayfinding & Signage, Templates); Hospitality (Overview, Logotype, Colors, Typography, Look & Feel, Applications); Delivery (Overview, Colors, Typography...). This shows a multi-brand architecture with separate rules per sub-brand, including audio and signage - but the rules themselves were not captured.
- Imagery and voice: not visible here beyond the gem icon row.

## 9. UX
- Easy to scan; the sidebar exposes the full tree. Weakness for a brand book: the intro page offers no visual of colours or type, and copy contains typos ("Adehering", "intructions"). The long sidebar text is only 12 px.

## 10. Craft signals
- One ink colour across logo, text and chrome.
- The wordmark sits at about 62% of content width with generous space above (100 px gem row) and below (~100 px).
- Active nav in chartreuse gives clear state on blue (9.46:1).

## 11. Reproduction recipe
```css
:root{--ink:#1618ab;--hi:#89ff6a;--bg:#fff}
body{font:400 20px/28px "Area Normal",Rubik,system-ui;color:var(--ink);background:var(--bg)}
.sidebar{position:fixed;inset:0 auto 0 0;width:240px;background:var(--ink);color:#fff;font:700 12px/15.6px "Area Normal"}
.sidebar .active{color:var(--hi)}
.lead p{font:500 25px/32.5px "Area Normal"}
.next{background:var(--ink);color:#fff;padding:48px 65px;transition:all .3s ease-in-out}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 7 | Bold single-colour identity with a distinctive wordmark. |
| Originality | 6 | One-colour discipline is strong; platform template is standard. |
| Usability | 6 | Good navigation; this page offers little actionable content. |
| Craft | 6 | Clean spacing and strong contrast; typos and default Bootstrap tokens. |

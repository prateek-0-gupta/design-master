---
id: bg-the-mellon-foundation
source: brandguidelines
category: guideline
status: analyzed
title: "Mellon Foundation Identity Guidelines"
creator: "Andrew W. Mellon Foundation (in-house)"
styles: [editorial-serif, monochrome, minimal-swiss]
patterns: [large-serif-welcome-statement, three-item-top-nav-with-dropdowns, black-contact-footer, hand-drawn-logomark, sonic-identity-chapter, squarespace-built-guideline-site, downloadable-assets-resource, crediting-instructions]
mode: mixed
palette: ["#eeeeec", "#000000", "#ffffff", "#464646"]
type_families: ["Joane T Light (display serif)", "Halyard Display Regular", "Halyard Text Book/Regular"]
type_class: [editorial-serif, geometric-sans]
radius_px: [300]
motion: {durations_s: [0.14, 0.4], easing: [ease-in-out, cubic-bezier(0.4,0,0.2,1), linear], loop: false}
scores: {aesthetics: 7, originality: 6, usability: 6, craft: 6}
craft_signals: [serif-display-against-sans-ui, contact-in-footer, offwhite-not-white, tight-lineheight-1-on-display]
anti_patterns: [home-only-coverage, empty-right-half-of-hero, footer-link-text-14px]
---
# Mellon Foundation Identity Guidelines — Andrew W. Mellon Foundation

## 1. Snapshot
- **Subject:** brandguidelines.mellon.org, a Squarespace-built site (customProperties are Squarespace theme variables). Wayback Machine capture dated 2025-08-16 23:22:27 UTC (`captured_from` .../web/20250816232227if_/https://www.brandguidelines.mellon.org/). The live site is not reliably reachable.
- **Coverage:** home page only, one 1472 px tile plus one mobile sheet. The chapters named in the nav were not captured, so logo, type and colour rules are unseen.
- **Why it's remarkable:** an entirely black-on-grey page: a single huge serif sentence is the whole welcome, which signals editorial confidence for a humanities funder.

## 2. Composition & layout
- Content column between x=144 and x=1296 (1152 px wide, 144 px side margin on a 1440 canvas).
- Header: logo (hand-drawn arch mark plus two-line "Mellon Foundation" wordmark) about 270×56 px at y≈78, nav right-aligned: Messaging Platform, Visual & Sonic Identity, Resources (18 px).
- Hero field #eeeeec, about 1075 px tall; headline left in about 500 px, leaving the right half empty.
- Footer #000000, 397 px: contact email at 24 px, copyright text 16 px in a 250 px column, "Follow" links right-aligned.

## 3. Typography
- Display: **Joane T Light** 60.9/60.9 px (line-height 1.0), weight 400 in a light cut, four lines sentence case; the largest and only serif on the page.
- Nav and subheads: **Halyard Display** 18.6/22.3 px, tracking 0.37 px (2%), and 26.4/29 px for the contact line.
- Body/footer: **Halyard Text** 16/18.4 px (line-height 1.15), tracking 0.32 px, weights 300 and 700; 14.3 px for small notes.
- Scale 14.3, 16, 18.6, 26.4, 60.9 (about 1.14× steps, then a jump) with +2% tracking on all sans text.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #eeeeec | page ground | 70% |
| #000000 | footer, text, logo | 25% |
| #ffffff | footer text | small |
| #464646 | mid grey (also sampled capture backdrop) | <1% |

Contrast: black on #eeeeec **18.08:1**; white on black **21:1**. The site carries no chromatic colour in the captured area, so colour rules (the "Color & Material" chapter) are not visible.

## 5. Depth & material
Flat. A 300 px radius appears once in the census (a pill, likely a button). No shadows.

## 6. Components & patterns
Top nav with grouped dropdowns, giant welcome statement, black footer with underlined links, contact line and copyright. The cart counter "0" in the nav is Squarespace residue.

## 7. Motion
`padding 0.14 s ease-in-out`, `background/padding/transform 0.3 s … ease-in-out`, `opacity 0.1 s linear`, `opacity 0.4 s cubic-bezier(0.4,0,0.2,1)`: small hover and reveal transitions, nothing expressive.

## 8. Brand system
Seen only through the navigation:
- **Chapters (nav order):** Messaging Platform (Overview, Attributes); Visual & Sonic Identity (Overview, Wordmark & Logomark, Typography, Color & Material, Photography & Video, Visual System, Sonic Identity); Resources (Downloadable Assets, Crediting Instructions, Terms of Use).
- **Identity cues visible:** the arch/squiggle logomark paired with a condensed-feeling two-line serif wordmark; serif-plus-sans pairing.
- **Governance:** contact brand@mellon.org; third-party use needs prior approval; terms of use linked.
- **Noteworthy:** sonic identity and crediting instructions are first-class chapters for a funder whose grantees must credit it.
- **Unknown:** clearspace, minimum size, palette, misuse.

## 9. UX
Three-item nav is easy; no hero imagery or call to action, and the right half of the hero is blank. Small footer links at 16 px are underlined and legible.

## 10. Craft signals
- Off-white #eeeeec avoids a harsh white.
- Display leading is exactly 1.0 with all-sentence-case.
- Footer text hierarchy: 24 px contact, 16 px legal.
- Tracking of +2% on sans text for open texture.

## 11. Reproduction recipe
```css
:root{--paper:#eeeeec;--ink:#000}
body{background:var(--paper);color:var(--ink);font:300 16px/18.4px "Halyard Text",sans-serif;letter-spacing:.32px}
h1{font:400 61px/61px "Joane T",serif;max-width:500px;margin:0}
nav a{font:400 18.6px/22.3px "Halyard Display";letter-spacing:.37px}
footer{background:#000;color:#fff;padding:60px 144px}
footer a{text-decoration:underline;transition:opacity .4s cubic-bezier(.4,0,.2,1)}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 7 | Elegant serif statement and restrained monochrome. |
| Originality | 6 | Sonic identity chapter stands out; layout is a standard template. |
| Usability | 6 | Clear nav and contrast; content unseen. |
| Craft | 6 | Tight display leading and tracking; limited evidence. |

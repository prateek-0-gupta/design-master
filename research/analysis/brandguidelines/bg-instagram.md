---
id: bg-instagram
source: brandguidelines
category: guideline
status: analyzed
title: "Instagram brand assets and guidelines (Meta Brand Resource Center)"
creator: "Meta Platforms"
styles: [minimal-swiss, corporate-clean, monochrome]
patterns: [brand-resource-center-hub, per-brand-theme-colour-header, logo-pack-download-with-consent-checkbox, do-and-dont-icon-list, two-step-approval-process, left-sidebar-brand-guidance, legal-first-guideline]
mode: light
palette: ["#ffffff", "#1c1e21", "#65676b", "#000000", "#f0f3f6", "#0866ff", "#27d367"]
type_families: ["Instagram Squircle Sans (400)", "Facebook Sans (500)", "Optimistic (400/700, brand-resource-centre headings)"]
type_class: [geometric-sans, rounded-sans]
radius_px: [50]
motion: {durations_s: [0.33, 0.67, 1.5], easing: [ease-in-out, "cubic-bezier(0.33,0,0,1)", "cubic-bezier(0.14,1,0.34,1)"], loop: false}
scores: {aesthetics: 5, originality: 4, usability: 6, craft: 6}
craft_signals: [per-brand-theme-header-colour, download-gated-by-terms-checkbox, round-pass-fail-icons, brand-specific-typeface-on-each-subsite, 36px-heading-with-tight-tracking]
anti_patterns: [no-visual-rules-on-page, legal-text-dominates, redirect-lands-on-threads, grey-disabled-download-button, no-colour-or-type-guidance]
---
# Instagram brand assets and guidelines — Meta Platforms

## 1. Snapshot
- **Subject:** requested `about.instagram.com/brand/`. The final URL is `meta.com/brand/resources/threads/` (a redirect into Meta's Brand Resource Center; the Threads page was the last one loaded). The home tiles and `d01` show the **Instagram** page. The six "subpages" are: Instagram, the BRC home, Meta, Facebook, WhatsApp and Threads. No Wayback archive. This is a promoted brand hub, not a visual guideline, so §8 is short.
- **Why it's remarkable:** a hub that gives each product a theme colour in the top bar (Instagram white, Meta pale blue, WhatsApp green) and an identical page template. It is almost entirely rules for use and legal terms, with no colour, type or composition guidance.

Viewed: home t01, t02; d01 t01 and t02 (the same page again); d02 t01 (BRC home); d03 t01 (Meta); d05 t01 (WhatsApp); mobile sheet 1. Home t03, d04 (Facebook) and d06 (Threads) were not opened.

## 2. Composition & layout
- **Header:** 80 px, white, with a 31 px Instagram glyph at the left and a small menu box at the right (it renders as an empty outlined square, a missing icon). A hairline below it.
- **Left rail:** 258 px wide with a right-hand hairline: "Brand guidance" (bold, underlined) and the page link.
- **Content column:** starts at x=393 and is about 916 px wide. H1 at 60/72 with tight tracking (-1.2 px, 2 lines). The intro paragraph is 14 px, body copy 19/28.5.
- **Logo pack card:** a 440×240 px black tile with the white glyph on the left; to the right a bordered card with a checkbox ("I have read and accept the applicable guidelines…") and a dark-grey (#4b4b4b) "Download" bar with a white circular icon, about 66 px tall.
- **Rules table:** a two-column list with a 1 px rule between rows. The left cell has a short rule title, the right has do/don't items.
- **Hub page (d02):** a centred Optimistic H1 "Brand Resource Center" over a 1072×604 photo, then a 2-column grid of product cards (a 136 px white logo tile, name and circular arrow button) on #f0f3f6.
- **Mobile:** a single column, H1 at about 56 px wrapping to 4 lines; the left rail disappears; the layout is clean and readable.

## 3. Typography
- **Instagram Squircle Sans** (400) carries almost everything, with a squircle-shaped, rounded-geometric look. Sizes from the census: 60/72 H1 (-1.2 px), 36/45 H2 (-0.72 px), 25/40 at 500 for sub-headings, 24/36, 19/28.5 body, 16/20.8 and 14/23.8 for list text, 12/19.8 at 500 labels.
- **Facebook Sans** at 14/21 appears in utility copy. **Optimistic** (Meta's brand-resource-centre face) is used in the hub and in the Meta page's wide-tracked headings.
- Each subsite uses its own typeface: WhatsApp (d05) is a plain grotesque with a green header; Meta uses wide letter-spaced Optimistic.

## 4. Colour
| hex | role | share |
|---|---|---|
| #ffffff | page ground | 85–96% |
| #1c1e21 | body text (46 uses) | text |
| #65676b | secondary text, disabled labels | text |
| #000000 | glyph tile, headings | 2–4% |
| #4b4b4b | download bar | small |
| #f0f3f6 | Meta header, hub card ground | panels |
| #27d367 | WhatsApp header | band |
| #0866ff (eyeballed, Meta blue) | Meta logo | logo |

Instagram's gradient glyph only appears on the hub (d02). Contrast: #1c1e21 on #fff **16.71:1**; #65676b on #fff **5.67:1**; white on #4b4b4b **8.72:1**; white on WhatsApp green #27d367 **1.98:1** (the header icon only, no text).

## 5. Depth & material
Entirely flat: no shadows (census) and 1 px grey hairlines. The only rounded shapes are circles (50% radius, 11 uses: icon badges, arrows).

## 6. Components & patterns
- Green check and red cross circular icons (about 24 px) for the rules ("Keep the letter I capitalised…" vs "Don't combine Insta or gram…").
- Numbered lists for restrictions.
- A "Logo pack" download card with a consent checkbox (the button is grey until accepted).
- Product cards with an arrow button in the hub.

## 7. Motion
From the CSS: 0.33 s ease-in-out for backgrounds, 0.15 s for quick state changes, 0.48 s for colour, 0.67–1 s `cubic-bezier(0.33,0,0,1)` for the background-size underline and accordions, and a long 1.5 s `cubic-bezier(0.14,1,0.34,1)` for colour and border. It is a very subtle site.

## 8. Brand system
- **Instagram page sections:** Brand guidelines and assets (permission is needed only for broadcast, radio, out-of-home or print larger than 8.5×11 in; requests in English with a mock-up), Using the Instagram brand (3 rule groups: balance with your brand, keep the word Instagram consistent, distance Instagram from other social networks), Using the Instagram brand in TV & film (a two-step approval taking 2–3 weeks or more), Legal.
- **Naming rules:** capital "I", never "Insta" or "gram", no combination with other names.
- **Visual rules (logo colour, clearspace, minimum size):** none on this page; they live in the downloadable pack, and I did not see them.
- **Document structure:** one long page of about 4 200 px; headings follow the order above.

## 9. UX
Plain, readable and quick, but sparse. The consent gate makes downloads deliberate. The glyph-only header has no wordmark. Some icons (menu box) are missing in the capture.

## 10. Craft signals
- Identical template across Meta, Instagram, WhatsApp and the others, with only the header colour and glyph swapped.
- Tight tracking at the larger heading sizes (-1.2 px at 60 px, -0.72 px at 36 px).
- Row rules and icon-coded do/don't lists keep long policy text scannable.

## 11. Reproduction recipe
```css
:root{--ink:#1c1e21;--muted:#65676b;--panel:#f0f3f6;--btn:#4b4b4b}
body{font:400 19px/28.5px "Instagram Squircle Sans",Helvetica,Arial,sans-serif;color:var(--ink)}
h1{font:400 60px/72px "Instagram Squircle Sans";letter-spacing:-1.2px}
h2{font:400 36px/45px "Instagram Squircle Sans";letter-spacing:-.72px}
.rule-row{display:grid;grid-template-columns:1fr 1fr;border-top:1px solid #e5e5e5;padding:24px 0}
.ok,.no{width:24px;height:24px;border-radius:50%}
.download{background:var(--btn);color:#fff;font-weight:700;height:66px;transition:background .33s ease-in-out}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 5 | Clean but generic; no visual identity is displayed beyond the glyph. |
| Originality | 4 | A standard policy page. |
| Usability | 6 | Easy to read, with icon-coded do/don't lists; little actionable visual guidance. |
| Craft | 6 | Consistent template with tight type tracking, but a missing icon and a legal-heavy page. |

---
id: bg-spotify
source: brandguidelines
category: guideline
status: analyzed
title: "Spotify for Developers — Design & Branding Guidelines"
creator: "Spotify (in-house)"
styles: [corporate-clean, flat-illustration, playful-rounded, minimal-swiss]
patterns: [yes-no-example-tiles, colour-bar-section-dividers, spot-illustration-per-section, when-does-this-apply-scaffold, left-rail-toc, constraint-led-rules, one-resting-colour-plus-free-expression, character-count-budgets]
mode: light
palette: ["#1ed760", "#121212", "#ffffff", "#400073", "#cbf55c", "#4100f4", "#a8c4c8", "#00394d", "#fd643f", "#f39c35"]
type_families: ["SpotifyMixUI 400/700 (body, web font)", "SpotifyMixUITitle 700 (headings)", "CircularSp script fallbacks (Arab/Hebr/Cyrl/Grek/Deva)", "Helvetica Neue / Helvetica / Arial (what partners are told to use)"]
type_class: [geometric-sans, grotesk]
radius_px: [4, 8, 17, 28, 9999]
motion: {durations_s: [0.05, 0.1, 0.15, 0.2], easing: [cubic-bezier(0.3,0,0,1), ease-in, cubic-bezier(0.8,0,1,1), cubic-bezier(0,0,0.2,1)], loop: false}
scores: {aesthetics: 7, originality: 6, usability: 8, craft: 7}
craft_signals: [encore-design-tokens-exposed, yes-no-captions-colour-coded, per-section-colour-bar, rule-on-corner-radius-by-device-size, character-count-budgets, wordmark-never-without-icon, clearspace-grid-diagram]
anti_patterns: [grey-caption-fails-aa, small-14px-body-captions-low-contrast, tiny-three-colour-palette-spec, no-lineheight-tokens-in-use]
---
# Spotify for Developers — Design & Branding Guidelines — Spotify (in-house)

## 1. Snapshot
- **Subject:** The partner-facing "Design & Branding Guidelines" page of developer.spotify.com. It is a single long scrolling page (about 17,374 px tall at 1440 px) for developers who integrate Spotify content. The capture sheet stops at the Accessibility page because the site_meta final URL is `/documentation/accessibility` (requested `/documentation/design`). The home tiles are the design page itself and the sub1 tiles are the Accessibility Guidelines.
- **Why it's remarkable:** Rules are written as constraints with a "When does this apply?" scaffold, a yes/no tile for each, hard numbers (4 px corner radius on small and medium devices, 8 px on large; max 20 items per shelf; 25/18/23 character budgets for playlist, artist and track names), and one disciplined colour statement: green is the "resting colour", everything else is free but must be high contrast.

## 2. Composition & layout
- **Chrome:** purple top bar #400073 (≈72 px tall) with the lockup left, "Documentation" in lime (#cbf55c) with a short underline and "Community" in white centred, "Log in" right. A lavender left rail (#f2edf4, 300 px wide, ≈830 px tall and not sticky in the capture) holds an 11-item in-page TOC with purple bullets.
- **Content column:** text starts at x=332 and runs to about x=1408 (≈1076 px wide, a long measure of ~150 characters at 16 px, which is too wide for comfortable reading). Illustrations are capped at ≈780 px wide and left aligned, so they do not fill the column.
- **Section rhythm:** each H2 is preceded by a 167×8 px solid colour bar that rotates through green #2c856b, navy #00394d, orange #f39c35, coral #fd643f and brand green #1ed760. After it comes an H2 at 32 px, a full-width 780×450 px flat illustration in the same hue, then H3 "When does this apply?" and the rules.
- **YES/NO grids:** four tiles per row on a roughly 4-column grid with a 30 px gutter; the label is YES in green or NO in red, with a grey 14 px caption.
- **Mobile (390 px):** single column with a hamburger on the purple bar. YES/NO tiles stay four-up and shrink to about 65 px wide, so captions wrap into a 6–8 line column of text at roughly 11 px. That is a weakness.

## 3. Typography
Census (home): 235 text nodes. Sizes: 16px ×154, 24px ×34, 14px ×32, 32px ×12, 21.28px ×2, 48px ×1. Weights: 400 ×153, 700 ×82. Line-height and letter-spacing are `normal` on every node (no tuned leading or tracking). Text transform is none except 4 uppercase nodes.
- **Families:** SpotifyMixUI (body, 188 nodes) and SpotifyMixUITitle (headings, 46 nodes), both with a CircularSp script fallback chain. Loaded: MixUI 400, MixUI 700, MixUITitle 700. Monospace appears once, for inline code.
- **Scale (page):** H1 48 → H2 32 → H3 24 → H4/bold 16 → body 16 → caption 14. Ratios of 1.5, 1.33, 1.5. Headings are visibly tight, with the kerning built into the Title cut.
- **Scale (tokens):** `--encore-text-size-*`: 0.625, 0.75, 0.875, 1, 1.25, 1.5, 2, 3, 4, 6 rem. Unused steps: 3, 4, 6 rem are display sizes.
- **What partners are told to use (Fonts section):** not the brand typeface. The page tells partners to use the platform default sans, then Helvetica Neue, Helvetica, Arial. The Spotify typeface is deliberately withheld from third parties.
- **Links** are purple #8c20df underlined, and "bright accent" #4100f4 is used on the download buttons.

## 4. Colour
| Hex | Role | Approx share (palette.json) |
|---|---|---|
| #ffffff | page ground | 67–75% of every tile |
| #f2edf4 | left rail, info callouts (lavender) | ≈10% of tile 1 |
| #400073 | header bar, H-bars, link purple family | ≈4% of tile 1 |
| #1ed760 | Spotify Green: logo, YES text, accent bars | brand accent |
| #121212 | Spotify Black (brand spec) | logo and badges |
| #000000 | body text (rgb 0,0,0 ×145 nodes) | all copy |
| #cbf55c | active nav item on purple | small |
| #4100f4 | button fill, "bright accent" | download buttons |
| #00394d / #2c856b / #a8c4c8 | illustration navy / teal / grey-blue | per illustration |
| #fd643f / #f39c35 | illustration coral / orange | per illustration |
| #e91429 | NO label (essential-negative) | 13 text nodes |

The "Using our colors" panel (light grey #eeeeee) shows only three official swatches: Green #1ED760 (RGB 30/215/96, CMYK 86/0/80/0), White #FFFFFF and Black #121212 (RGB 18/18/18). CMYK is given for Green only. Tiles below show four icon-on-colour examples: purple-to-pink gradient (yes), yellow with black (yes), pale grey-lavender (no, outside palette) and cyan (no, over-saturated for CMYK).

**WCAG (contrast.py)**
- Black on white: 21.0:1. White on #400073: 14.33:1. Lime #cbf55c on #400073: 11.43:1.
- **Spotify Green #1ed760 on white: 1.92:1 (fail).** On black it is high, and black on green is 10.94:1. The rule is therefore black text and a black icon on green, never green text on white (the green YES label is exactly this failing pairing, but it is a status word, not body copy).
- Grey captions #939393 on white: 3.07:1 (fails AA normal at 14 px). The census also shows #7f7f7f ×20. #656565 (the `--text-subdued` token) passes at 5.83:1, so the live captions ignore the system's own token.
- Red NO #e91429 on white: 4.57:1 (barely passes). Link purple #8c20df: 6.2:1. Bright accent #4100f4: 8.3:1 with white text on the buttons.

## 5. Depth & material
- Flat. `shadow: {}` and `border: {}` in the census. Depth appears only inside the illustrations, which use soft, light drop shadows under white phone and card shapes and a rotated-device view on the "Using our content" diagram.
- Logo tiles use hairline #ddd boxes with no shadow. The clearspace diagram is hatched with diagonal 1 px lines on a #30e690-ish green, with an "x" unit marked.

## 6. Components & patterns
- Download buttons: pill, 4100f4 fill, white 700 text, about 210×48 px, 9999 px radius.
- YES/NO tile: image, label, caption. It is the page's central component and is reused for logo, colour, artwork and shelf rules.
- Callout: lavender #f0eaf4 box with an (i) icon, used on the Accessibility page.
- Explicit-content badge: a "19" mark in a red ring on white and a solid red disc on dark (South Korea requirement).
- Illustrations: the Accessibility page switches to a hand-drawn black-ink WCAG map (credited to Intopia) with accent colours on the quadrant arcs: a different register from the flat geometric illustrations of the design page.
- Radius census: 50% ×11 (round avatars), 9999px ×9 (pills), 17px ×2 and 28px ×2 (buttons).

## 7. Motion
Tokens: shortest-1 50 ms, -2 100 ms, -3 150 ms, -4 200 ms; productive-accelerate `cubic-bezier(0.8,0,1,1)`, productive-decelerate `cubic-bezier(0,0,0.2,1)`, productive-exit 200 ms. Real transitions in the census: `color 0.15s cubic-bezier(0.3,0,0,1)` ×27, `outline-color 0.2s ease-in` ×13, `background-color, transform 0.15s cubic-bezier(0.3,0,0,1)` ×8. The page is static; motion is limited to hover colour changes and focus outlines. There is no motion guidance in the document.

## 8. Brand system
**Logo**
- Full logo = icon + wordmark. The wordmark may never appear without the icon; the icon alone is allowed only when space is short or the brand is already established (for example an app icon).
- Clearspace is defined by an "x" unit (the grid diagram, with x set around the icon) with hatching on all four sides.
- Colour versions: green on white, black on white, black on green, white on green, green on black. Do not use the logo in a sentence, as a letter, to make shapes, or on busy or low-contrast areas.
- Naming: your app must not include Spotify or sound/look like it ("for Spotify" is acceptable). Your logo must not use Spotify Green, the circle or the waves. No co-branding or pairing with other brands.

**Colour:** Green is the "resting colour"; the voice may be colourful (creative gradients and yellow are shown as correct) but nothing outside the palette is allowed, and over-saturated colours are banned for CMYK.

**Content rules (the real subject of the page):** use only provided artwork, uncropped, no overlays or blurs; corners 4 px on small/medium devices, 8 px on large; no brand or logo on top of artwork; never seat Spotify content beside similar services; dedicate a full shelf to it; max 20 items per content set with a link out; link text options are "GET SPOTIFY FREE", "OPEN SPOTIFY", "PLAY ON SPOTIFY" or "LISTEN ON SPOTIFY"; character budgets 25/18/23; podcasts get two lines for titles.

**Document structure (sidebar order):** Introduction · Attribution · Using our content · Browsing Spotify content · Linking to Spotify · Playing views · Showing entities · Using our logo · Using our colors · Logos and naming restrictions · Fonts · Thank you. A sibling "Accessibility Guidelines" page (Introduction, Quick Wins, Medium Term Wins, Intensive Wins) uses the same template with collapsible TOC items.

**Voice:** direct and second-person ("Follow these guidelines"), with short imperatives and a legal tone at the start. The accessibility page adds the memorable question "Who might this experience exclude?"

## 9. UX
- The "When does this apply?" scaffold lets a developer jump straight to the rule that fits their integration.
- Every rule is paired with a visual, and the YES/NO colour coding is scannable.
- Weaknesses: 1076 px line length; low-contrast 14 px grey captions; the TOC rail ends at 830 px and does not follow the scroll in the capture; the brand colour page lists only 3 colours with no extended palette values; logos have no minimum size in px.

## 10. Craft signals
- Rules specify numbers rather than adjectives (4/8 px radii, 20 items, 25/18/23 characters).
- Every H2 has a 167×8 px colour bar in a rotating hue that matches its illustration, giving the page a visual rhythm.
- Design tokens (`--encore-*`) are exposed in the CSS with systematic spacing (2, 4, 6, 8, 12, 16, 24, 32, 48, 64, 96, 128 px) and radii (2, 4, 6, 8, 16 px).
- Fallback font stack covers five non-Latin scripts.
- Logo tiles show the four legal colourways side by side.

## 11. Reproduction recipe
```css
:root{
  --green:#1ed760; --black:#121212; --white:#fff;
  --purple:#400073; --lime:#cbf55c; --lavender:#f2edf4; --accent:#4100f4;
  --text:#000; --subdued:#656565; --negative:#e91429;
  --r-sm:4px; --r-lg:8px; --pill:9999px;
  --ease:cubic-bezier(.3,0,0,1);
  --font:"SpotifyMixUI","Helvetica Neue",Helvetica,Arial,sans-serif;
}
body{font:400 16px/1.4 var(--font);color:var(--text);background:#fff}
h1{font:700 48px/1.1 var(--font);letter-spacing:-.02em}
h2{font:700 32px/1.2 var(--font)} h3{font:700 24px/1.25 var(--font)}
h2::before{content:"";display:block;width:167px;height:8px;background:var(--bar,#1ed760);margin-bottom:32px}
.topbar{background:var(--purple);height:72px;color:#fff}
.topbar .active{color:var(--lime);border-bottom:2px solid var(--lime)}
.rail{background:var(--lavender);width:300px}
.btn{background:var(--accent);color:#fff;border-radius:var(--pill);padding:12px 32px;font-weight:700;transition:background-color .15s var(--ease),transform .15s var(--ease)}
.yes,.no{font:700 14px/1 var(--font);text-transform:uppercase}
.yes{color:var(--green)} .no{color:var(--negative)}
.caption{font:400 14px/1.4 var(--font);color:var(--subdued)}  /* use token, not #939393 */
.artwork{border-radius:4px} @media(min-width:1024px){.artwork{border-radius:8px}}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 7 | Clean white page with a confident purple/lime bar and coloured section bars; flat illustrations are cohesive but sit small. |
| Originality | 6 | The rotating colour bars and tight yes/no tiles are neat; the layout is a standard docs template. |
| Usability | 8 | Rules are numeric, scoped by "When does this apply?" and illustrated; marred by long line length and grey captions failing AA. |
| Craft | 7 | Systematic Encore tokens and consistent scaffold; line-height and tracking left at `normal`, and captions ignore the subdued token. |

---
id: bg-seat-geek
source: brandguidelines
category: guideline
status: analyzed
title: "SeatGeek Brand Guidelines"
creator: "In-house"
styles: [maximalist-color, photo-led, flat-illustration, corporate-clean]
patterns: [fixed-left-sidebar-nav, section-hero-with-what-youll-find, download-button-per-asset, vintage-poster-inspiration-wall, design-principles-in-accent-colour, next-section-footer-link, brand-vs-functional-font-pairing, cmyk-rgb-hex-pms-swatch-labels]
mode: mixed
palette: ["#ff5b49", "#000000", "#f8f7f5", "#eae7e1", "#525252", "#9837ff", "#1c71ef", "#11a669", "#fdbf2d", "#a99981"]
type_families: ["Roobert (functional; DM Sans as fallback in Google Slides)", "Headliner (custom brand headline font)", "Roobert Medium/Semibold/Bold (3 weights loaded)"]
type_class: [geometric-sans, display]
radius_px: [4, 8]
motion: {durations_s: [0.5], easing: [ease], loop: false}
scores: {aesthetics: 8, originality: 8, usability: 8, craft: 7}
craft_signals: [vintage-poster-inspiration-grid, hex-cmyk-rgb-pms-on-every-swatch, usage-percentage-85-percent-primary-logo, 25-percent-clearspace-diagram, dated-sections-updated-oct-2022-2023, one-accent-colour-for-all-h3-principles, icon-set-from-typeface-curves]
anti_patterns: [white-on-gatorade-fails-aa, sidebar-nav-not-collapsed-on-mobile, mobile-headings-break-mid-word, accent-red-on-offwhite-fails]
---
# SeatGeek Brand Guidelines — In-house

## 1. Snapshot
- **Subject:** `brand.seatgeek.com`, a 10-section hosted guideline (Logo, Color, Typography, Photography, Illustration, Iconography, Treatment, Motion, Copy, Application). The request redirected to `/iconography` as the final URL. The home page is dated "Updated Oct. 2023"; the Logo, Typography, Photography, Illustration and Iconography pages show "Updated Oct. 2022". The footer says 2022. No archive.
- **Why it's remarkable:** a single hot coral ("Gatorade") on black, backed by a wall of vintage ticket, poster and trading-card references that explain the custom wedge-serif wordmark and display font.

Viewed: home t01 and t02; one tile each of Logo, Color (two tiles), Typography (two tiles), Photography, Illustration and Iconography; mobile sheet 1. Treatment, Motion, Copy and Application pages were not captured in the subpage list, so they are not analysed.

## 2. Composition & layout
- **Frame:** a fixed 240 px black left rail with the 10 section links (about 17 px, white; the current one in coral). Content runs from x=360 to x=1320, a 960 px column.
- **Top bar:** a 108 px black bar with the red wordmark at x=360, "Brand Guidelines" at x≈850 and the update date at right.
- **Section template:**
  1. A beige hero band (#eae7e1) with an H1 of about 94 px.
  2. A 1 px black rule at y≈375.
  3. A "What you'll find" bullet list in the left column, with a 3–5 line intro in a 340 px column beside it.
  4. Off-white (#f8f7f5) content blocks, each opened by a 1 px rule, with a 36 px heading in the left 240 px column, intro text at x=605 and a black "Download" button at the right edge.
- **Footer of each page:** a "Next Section" link with a large title and a black circular arrow, then the black footer with an oversized coral wordmark.
- **Home:** the black hero is empty, then an Inspiration poster wall (a horizontally cropped collage of old posters, tickets and trading cards) and the four Design Principles in a 2×2 grid.
- **Mobile (390 px):** the 240 px rail does not collapse. It squeezes the content to about 270 px, and words wrap mid-word ("Inspirati/on", "Principl/es"). This is the weakest part of the site.

## 3. Typography
- **Roobert** is the workhorse: a geometric-grotesk. Census shows 17/24 at 400 and 600 (body and nav), 36/46 at 700 (section headings), 22/32 at 700, and 94/94 at 700 (H1). Letter-spacing is normal everywhere.
- **Headliner** is the custom brand face: a condensed, italic, flared-wedge face built on vintage poster lettering. It is for brand marketing headlines only. The specimen shows it at about 98/100.
- The type page offers a Download for each font. For Google Slides, where Roobert is not available, the page names DM Sans.

## 4. Colour
Named in the doc (CMYK / RGB / HEX / PMS shown on each swatch):
| hex | name | role | note |
|---|---|---|---|
| #FF5B49 | Gatorade (PMS 178 C) | signature primary | logo, accent, H3s |
| #000000 | Black (PMS 419 C) | primary | page grounds, rail |
| #FFFFFF | White | primary | — |
| #9837FF | Purple (265 C) | secondary | — |
| #1C71EF | Blue (2174 C) | secondary | — |
| #11A669 | Green (2416 C) | secondary | — |
| #FDBF2D | Yellow (1235 C) | secondary | — |
| #A99981 | Gold (7529 C) | secondary | listed RGB 69/153/129 does not match this hex (a typo on the page) |

Site chrome: #f8f7f5 content ground, #eae7e1 hero band, #525252 secondary text.

Rules: the brand is built around the three primaries; secondaries go only on "secondary applications". Gatorade is used "as a highlight" (one word or object on a black or white layout) or "to capture attention" in crowded places like sponsorships.

Contrast:
- Gatorade on black: **6.84:1**.
- Black on Gatorade: **6.84:1**.
- White on Gatorade: **3.07:1**, so it passes for large text only.
- Gatorade #ff5b49 on #f8f7f5: **2.87:1**, which fails. The site uses it for 22 px H3 principle headings and nav active states.
- Black on Purple: **4.33:1**, which fails normal text.
- Black on Blue: 4.66:1.
- Black on Yellow: 12.67:1.

## 5. Depth & material
Flat. There are no shadows (census). Hero illustrations are grainy, stippled vector scenes (arena, concert crowd, fireworks, marquee street) in a black, coral and cream limited palette, so the depth is illustrated, not UI-based. Images are shown in 4-px-radius frames or edge to edge.

## 6. Components & patterns
- Black rectangular buttons ("Download", "Download all"), 8 px radius, about 220×44 px.
- A circular black arrow button for "Next Section".
- Logo tiles: the stacked wordmark in coral, white and black on black, black and white grounds, with a clearspace diagram: 25% margins around a 100% height box.
- Icon library: a solid glyph set (megaphone, stadium, ticket, cart, QR and others) in a 12-column grid.

## 7. Motion
Only `opacity 0.5s ease` transitions appear in the census (fades on the nav and the page). A Motion section is listed in the sidebar but was not captured.

## 8. Brand system
- **Inspiration:** old-school event posters, trading cards, marquees and memorabilia. The attitude is "bold, confident, straightforward".
- **Design principles (each in coral at about 36 px):** Bring the hype; Be enticing; Restore humanity; Emphasize our expertise.
- **Logo:**
  - Four assets: Stacked Wordmark, Inline Wordmark, App Icon and Partnership Lockups.
  - The stacked wordmark is the primary and "should be used in 85% of applications".
  - It appears in only the three primary colours.
  - Clearspace is a margin of 25% of the mark's height on every side.
- **Typography:** a brand font (Headliner) and a functional font (Roobert), described as a "universal typeface" for iOS, Android and web.
- **Photography:** Inspiration; Product Photography ("make our product a hand-held hero"); Lifestyle Photography. The inspiration wall mixes concert, sport and ticket-in-hand photos in a red-orange grade.
- **Illustration:** Hero, Functional and Category. It "differentiates the brand from the coldness of the technology and ticketing sectors".
- **Iconography:** drawn from the same rounded shapes as the functional typeface.
- **Document structure:** 10 sections: Logo, Color, Typography, Photography, Illustration, Iconography, Treatment, Motion, Copy, Application. Each starts with a "What you'll find" list.

## 9. UX
The persistent left rail with an active-state colour, a download button per asset, per-section update dates and "Next Section" links make the site very easy to navigate on desktop. The mobile layout is broken. Contrast of the coral on off-white is weak.

## 10. Craft signals
- Every swatch lists CMYK, RGB, HEX and PMS.
- The logo gets a usage percentage (85%) and a percent-based clearspace diagram.
- Per-page "Updated" stamps.
- The inspiration wall explains the typeface and logo rather than just decorating.
- The hot coral is limited to highlights (the "great" word in an italic script on black).

## 11. Reproduction recipe
```css
:root{--sg-gatorade:#ff5b49;--sg-black:#000;--sg-paper:#f8f7f5;--sg-sand:#eae7e1;
  --sg-purple:#9837ff;--sg-blue:#1c71ef;--sg-green:#11a669;--sg-yellow:#fdbf2d}
body{display:grid;grid-template-columns:240px 1fr;font:400 17px/24px "Roobert","DM Sans",sans-serif}
nav.rail{background:#000;color:#fff;font-weight:600;padding:40px}
nav.rail a.is-active{color:var(--sg-gatorade)}
.hero{background:var(--sg-sand);padding:150px 120px 100px}
.hero h1{font:700 94px/94px "Roobert"}
.block{border-top:1px solid #000;display:grid;grid-template-columns:240px 340px 1fr;gap:5px 5px}
.block h2{font:700 36px/46px "Roobert"} .principle h3{color:var(--sg-gatorade);font:700 36px/46px "Roobert"}
.btn{background:#000;color:#fff;border-radius:8px;padding:12px 24px;font-weight:600}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Black, off-white and one coral with a poster-wall reference are cohesive and energetic. |
| Originality | 8 | The vintage-ticket heritage and the custom wedge wordmark are rare in ticketing. |
| Usability | 8 | Great desktop navigation and downloads; mobile and some contrast pairs are weak. |
| Craft | 7 | Precise swatch data and a logo usage ratio, offset by a swatch typo and mid-word wraps. |

---
id: insp-5-5
source: inspora
category: Motion
status: analyzed
title: "Book animation"
creator: "@cambreedesigns"
styles: [editorial-serif, soft-3d, luxury]
patterns: [vertical-book-carousel, book-open-page-transition, wheel-list-company-names, drop-cap-article, sidebar-meta-column, diamond-active-nav]
mode: light
palette: ["#c4e4fd", "#f1f0ec", "#fefdf9", "#3ca53c", "#1a1a1a", "#31302e", "#b8b8b4", "#9a9a9a"]
type_families: ["Instrument Serif / Editorial-style condensed serif (likely)", "Inter / Neue Montreal-style grotesk (likely)"]
type_class: [editorial-serif, neo-grotesk]
radius_px: [16, 9999]
motion: {durations_s: [0.47, 0.33, 0.8, 0.6, 0.5], easing: [ease-out, ease-in], loop: false}
scores: {aesthetics: 9, originality: 8, usability: 7, craft: 8}
craft_signals: [book-cover-carries-portfolio-logo, faded-neighbour-names-wheel, italic-serif-category-and-year-flank, drop-cap-opening, page-turn-into-article, diamond-bullets-on-active-nav]
anti_patterns: [inactive-nav-and-wheel-items-below-aa, crossfade-shows-overlapping-text]
---
# Book animation — @cambreedesigns

## 1. Snapshot
- **Subject:** A 13.4 s, 1920×1180 capture of a VC portfolio site ("Chapter One") framed as a library. Each portfolio company is a hardback book, flanked by an italic category and year ("Dev Tools", "Est. 2020") and a wheel of company names on the right. Clicking "Read our story" opens the book, which transitions into a long-form article page ("The Backend for Builders").
- **Why it's remarkable:** It commits to the "authoring the future" brand metaphor literally: investments are books, and case studies are chapters you open.

## 2. Composition & layout
- **Stage:** The site sits inside a browser-like panel of about 1690×935 px (radius about 16) on a sky-blue gradient (#c4e4fd fading to white).
- **Carousel view:**
  - Left nav column at x≈145 (Home, ◆ Investments ◆, Our authors, Media, About), at about 13 px.
  - Centred book about 290×385 px, tilted about 2°.
  - Italic flanks about 340 px either side.
  - A right-aligned company wheel (about 40 px serif) with the active name black and neighbours faded.
  - The previous and next books peek, cropped at the top and bottom edges.
- **Article view:**
  - Three columns: a meta sidebar (Space, Founders, Milestones, Socials), a body column of about 560 px with an italic serif H1 of about 36 px, and an empty right column.
  - A 1 px vertical rule separates each column.

## 3. Typography
- **Serif:** A narrow, high-contrast serif (Instrument Serif-like), used upright for company names and the sidebar title, and italic for categories, years and article headings ("The Original Bet").
- **Body:** A neat grotesk at about 13 px with leading of about 1.55 in #31302e-ish grey.
- **Drop cap:** The opening "S" is a serif drop cap spanning 2 lines.
- **Sidebar:** Labels at about 11 px in grey above values at about 13 px.

## 4. Colour
| Hex | Role |
|---|---|
| #c4e4fd → #ffffff | outer sky backdrop |
| #f1f0ec | carousel paper |
| #fefdf9 | article paper (warmer white) |
| #3ca53c | Supabase book cover (each book takes its company colour: purple Mercury, white Together.ai) |
| #1a1a1a | active name, headings |
| #31302e | "Read our story" pill |
| #b8b8b4 | faded wheel names |
| #9a9a9a | nav / meta labels |

WCAG:
- #1a1a1a on #f1f0ec is 15.26:1.
- White on the #31302e pill is 13.18:1.
- Faded wheel names #b8b8b4 on #f1f0ec are **1.74:1**. This is decorative, but they are also clickable.
- Grey labels #9a9a9a on #fefdf9 are **2.76:1** (fail).
- Body #3a3a3a on #fefdf9 is 11.18:1.

## 5. Depth & material
- **Books:** Soft-3D, with a darker spine strip (about 18 px) on the left, a subtle page-edge thickness, and a soft drop shadow down-right. The open book (t≈5.2 s) shows white pages with tiny text and a green inner border.
- **Backdrop:** The sky gradient adds atmosphere. The panel itself floats with a large, soft shadow.

## 6. Components & patterns
- **Vertical book carousel:** Synced with the right-hand name wheel (the active name is black, and the others fade by distance).
- **CTA:** A "Read our story" pill appears under the active book on hover.
- **Page-turn transition:** The book opens to a spread, zooms, and crossfades to the article.
- **Article template:** Drop cap, italic H2s, a sidebar of milestones with valuations, and a top nav (Investments, Scout program, Media, Reason to exist, Contact Us).

## 7. Motion
- **Measured:** 8 segments across 13.4 s, median 0.47 s. `seamless_loop_likely: false`.
  - 0.00 s: 0.47 s, peak 0.25. 1.77 s: 0.33 s, peak 0.15. Both ease-out: carousel steps to the next book.
  - 4.50 s: 0.27 s, symmetric. The book-open beginning.
  - 6.00–6.80 s: 0.80 s, peak 0.73 (ease-in). The zoom and crossfade into the article; the key frame at 6.7 s catches the crossfade with ghosted text.
  - 7.63 s: 0.6 s, peak 0.03. 11.63 s: 0.5 s, peak 0.03. Both strongly ease-out: return and settle.
- **Read:** Carousel steps are about 0.33–0.47 s ease-out. The narrative transition is slower (0.8 s), as befits a "chapter" change.

## 8. Brand system
n/a — not a brand system, but the identity is strong:
- a book and chapter metaphor carried through the nav ("Our authors") and copy;
- an italic serif for "voice" with a grotesk for information;
- each company's logo becomes its book cover.

## 9. UX
- The metaphor is memorable and makes browsing a portfolio pleasurable.
- The name wheel gives orientation within the list.
- **Risks:**
  - Faded names and labels are low-contrast.
  - Only one book is visible at a time, which is slow for scanning 20+ companies.
  - The crossfade briefly overlays two pages of text.

## 10. Craft signals
- The italic serif is used only for metadata ("Dev Tools", "Est. 2020") and article subheads, a consistent semantic split.
- The active nav item is wrapped in ◆ diamonds rather than underlined.
- Wheel names fade with distance (about 3 opacity steps).
- The drop cap aligns to two body lines.
- The milestone list includes valuations ("Series F 2026 (val. $10B)"), so the content is designed, not lorem.
- The article paper (#fefdf9) is warmer than the carousel paper (#f1f0ec), marking a change of "material".

## 11. Reproduction recipe
```css
:root{--sky:#c4e4fd;--paper:#f1f0ec;--paper-2:#fefdf9;--ink:#1a1a1a;--muted:#6f6f6b;--faint:#b8b8b4}
body{background:linear-gradient(180deg,var(--sky),#fff 85%)}
.frame{border-radius:16px;background:var(--paper);box-shadow:0 40px 80px rgba(40,80,120,.18)}
.serif{font-family:"Instrument Serif",serif}.serif i,.meta-italic{font-style:italic}
.wheel li{font:400 40px/1.3 "Instrument Serif";color:var(--faint);transition:color .4s,transform .4s cubic-bezier(.2,.8,.2,1)}
.wheel li[aria-current]{color:var(--ink)}
.book{width:290px;aspect-ratio:3/4;transform:rotate(2deg);box-shadow:12px 18px 30px rgba(0,0,0,.18),inset 18px 0 0 rgba(0,0,0,.08);
  transition:transform .45s cubic-bezier(.2,.8,.2,1)}
.article p:first-of-type::first-letter{float:left;font:400 3.2em/.8 "Instrument Serif";margin:4px 6px 0 0}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 9 | Gorgeous serif and paper palette, with books as colourful focal objects on a sky backdrop. |
| Originality | 8 | Portfolio as library, with the case study opened like a book, is fully committed. |
| Usability | 7 | Delightful but slow to scan, and secondary text fails contrast. |
| Craft | 8 | Consistent semantic type and nice spine detail; the crossfade overlap is a little messy. |

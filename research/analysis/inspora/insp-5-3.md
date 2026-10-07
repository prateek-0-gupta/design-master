---
id: insp-5-3
source: inspora
category: Web
status: analyzed
title: "Personal portfolio"
creator: "@emblemo"
styles: [minimal-swiss, hairline-ui, micro-interaction, dark-premium]
patterns: [vertical-menu-tab, slide-out-nav-drawer, ruler-tick-nav-rail, theme-toggle-light-dark, breadcrumb-with-close, card-grid-sitemap, graph-paper-background, device-frame-zoom-out]
mode: mixed
palette: ["#242321", "#31302f", "#f7f7f7", "#235ee6", "#c4e0f6", "#6f7478", "#99a2aa"]
type_families: ["Archivo / Chivo-style grotesk (likely)", "Inter (body, likely)"]
type_class: [grotesk, neo-grotesk]
radius_px: [28, 16, 12, 9999]
motion: {durations_s: [0.56, 0.36, 1.32, 0.56, 0.56, 0.96], easing: [ease-out], loop: false}
scores: {aesthetics: 7, originality: 7, usability: 7, craft: 7}
craft_signals: [ruler-ticks-beside-nav-items, rotated-menu-label-tab, faint-grid-paper-in-both-themes, tag-pairs-bottom-right-of-card, breadcrumb-x-closes-section, pressed-tab-tint-in-active-state]
anti_patterns: [empty-cards-no-preview, low-contrast-current-nav-item, link-blue-below-aa]
---
# Personal portfolio — @emblemo

## 1. Snapshot
- **Subject:** A 2880×2160, 17.6 s screen recording of a designer's portfolio shell. A vertical "MENU" tab opens a saturated-blue drawer with a ruler-tick rail, a toggle flips the site from light graph-paper to dark, and "Playground" opens a sitemap grid of five cards.
- **Why it's remarkable:** The navigation is treated as an instrument. Ruler ticks run alongside the menu items and the menu trigger is a rotated tab, so the chrome itself carries the "designer who draws and codes" identity.

## 2. Composition & layout
- **Frame:** The site is shown inside a rounded device frame (radius ~28 px at 2880 px) floating on a pale sky gradient (#c4e0f6 → #f1f7fc), with a deep, soft drop shadow. The camera zooms between a close crop (0.98–6.8 s, 14.6 s) and the full frame (8.78 s, 16.58 s).
- **Light home:** A left rail ~130 px wide holds the rotated "MENU" tab. The content starts ~330 px in, with logo top-left and an H1 "Product design & Illustration" at ~1080 px (scaled). The body is a 3-paragraph intro at ~16 px, about 60 characters per line, on a 24 px graph-paper grid.
- **Drawer:** Blue, about 33% of the viewport width, sliding from the left. Nav items sit 43 px apart (frame scale) beside a column of ~22 tick marks.
- **Playground (dark):** A 4-column card grid (About / Works / Playgrounds / My skills) with ~460×630 px cards (real px) and ~60 px gutters. "Contact" starts a second row. The breadcrumb "emblemo / Playground ×" sits above it.

## 3. Typography
- **Headings, labels, card titles:** a grotesk with wide, flat-sided rounds, closest to Archivo or Chivo Medium. The H1 is about 40 px CSS.
- **Body:** Inter-like at ~16 px with ~1.65 leading, grey #555.
- **Card tags:** "BIO DESIGN", "PORTFOLIO CASE STUDIES" are uppercase ~11 px medium, tracking about +0.04 em, right-aligned at the card bottom.
- **Menu tab:** "MENU" is rotated 90° in ~11 px caps with tracking about +0.2 em, in blue on a light-blue tint.
- **Nav items:** ~20 px regular white. The current page ("Home") is dimmed to about 55% white, which inverts the usual convention.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #242321 | dark-theme surface (warm off-black) | 56% (key) |
| #31302f | card fill / raised surface | 1% |
| #f7f7f7 (est.) | light-theme canvas with grid lines ~#ebebeb | — |
| #235ee6 (est., light frames) | drawer, MENU label, links | — |
| #c4e0f6 / #daedfc | presentation backdrop sky | 20% |
| #6f7478 / #99a2aa | backdrop shadow, frame bezel | 6% |

WCAG checks:
- Card titles (~#d8d8d8) on #242321 are **11.02:1**.
- Tags (~#a8a8a8) on #242321 are **6.6:1**.
- White nav on #235ee6 is **5.5:1**.
- The dimmed current item (#9db4f5) on blue is **2.69:1 (fails)**.
- Body #555 on #f7f7f7 is **6.96:1**.
- The link blue "Behance" (~#5577e0) is **3.84:1**, which fails AA for 16 px text.

## 5. Depth & material
- **Dark theme:** Cards use a ~1 px lighter rim and a soft outer shadow (about 0 12px 24px rgba(0,0,0,.35)) on a nearly identical fill, a "debossed tile" feel. A faint 1 px grid is visible behind them.
- **Light theme:** flat and paper-like.
- **Drawer:** flat blue with no shadow. Depth comes from the device-frame shadow only.
- **Toggle chip:** The pill at the top of the drawer (theme / share icons) has a 1 px white 40% border.

## 6. Components & patterns
- **Vertical MENU tab:** a rounded 12 px tab spanning the rail. When the drawer is open, the tab tints light blue (pressed state).
- **Drawer nav with ruler rail:** horizontal ticks (~28 px long) at an ~11 px pitch. The tick nearest the hovered item extends, as seen at "Playground" at 6.83 s.
- **Theme toggle:** clicking the first chip icon at 4.88 s flips the whole page to dark.
- **Breadcrumb:** logo plus "/ Playground" plus an "×" to close the section.
- **Sitemap cards:** title top-left, tag pair bottom-right, and an empty body, presumably for hover previews. Not shown.

## 7. Motion
- **Measured:** 17.56 s at 25 fps, motion_fraction **0.25**, 6 segments with a median of **0.56 s**. **5 of 6 segments are ease-out** (peak_at 0.11–0.29), the classic UI "fast start, soft land".
- **Segments:**

  | Time (s) | Duration (s) | Probable action |
  |---|---|---|
  | 1.44–2.00 | 0.56 | drawer slide-in |
  | 4.16–4.52 | 0.36 | theme flip |
  | 6.88–8.20 | 1.32 | page change plus camera zoom-out |
  | 10.12–10.68 | 0.56 | zoom in |
  | 14.20–14.76 | 0.56 | zoom |
  | 15.52–16.48 | 0.96 | final pull-back (symmetric) |

- **Rhythm:** The recurring 0.56 s duration suggests one shared transition token. Not a loop (first/last diff 135).

## 8. Brand system
n/a — not a brand system. Identity cues:
- the smiley-face outline logo with the lowercase wordmark "emblemo";
- one electric blue as the only chroma;
- graph paper plus ruler ticks as a "drafting table" motif.

## 9. UX
- **IA:** The IA is tiny and clear: 5 items, repeated as cards.
- **Affordances:** The breadcrumb with × gives an obvious exit.
- **Issues:**
  - The current page is shown by dimming, which reads as disabled.
  - The cards are empty, so there is no information scent beyond two tags.
  - The theme toggle is unlabeled, an icon inside a chip.
  - Link blue fails AA on light.

## 10. Craft signals
- Ruler ticks align at an ~11 px pitch, and the active tick lengthens to point at the hovered item.
- The rotated "MENU" label is centred in a 12 px-radius tab that persists across both themes.
- Graph-paper grid lines stay visible in both light (#ebebeb on #f7f7f7) and dark (a ~3% lighter line on #242321).
- Each card carries a two-word tag pair, consistently baseline-aligned ~40 px from the card bottom.
- The dark theme uses warm #242321, not neutral #222, matching the warm-grey card rims.

## 11. Reproduction recipe
```css
:root{--bg:#f7f7f7;--grid:#ebebeb;--ink:#1e1e1e;--muted:#555;--accent:#235ee6;--r-tab:12px;--r-card:16px;
  --font-head:"Archivo","Chivo",sans-serif;--font-body:"Inter",system-ui,sans-serif;--t:.56s cubic-bezier(.16,1,.3,1)}
[data-theme=dark]{--bg:#242321;--grid:#2c2b29;--ink:#d8d8d8;--muted:#a8a8a8;--card:#272624}
body{background:var(--bg) linear-gradient(var(--grid) 1px,transparent 1px) 0 0/24px 24px,
  linear-gradient(90deg,var(--grid) 1px,transparent 1px) 0 0/24px 24px;color:var(--ink);transition:background-color var(--t)}
.menu-tab{writing-mode:vertical-rl;transform:rotate(180deg);font:500 11px/1 var(--font-head);letter-spacing:.2em;
  color:var(--accent);border:1px solid var(--grid);border-radius:var(--r-tab);padding:20px 10px}
.drawer{position:fixed;inset:0 auto 0 0;width:33vw;background:var(--accent);transform:translateX(-100%);transition:transform var(--t)}
.drawer.open{transform:none}
.ticks{width:28px;background:repeating-linear-gradient(#fff6 0 1px,transparent 1px 11px)}
.card{background:var(--card);border-radius:var(--r-card);box-shadow:inset 0 0 0 1px #ffffff0d,0 12px 24px #0006;
  display:flex;flex-direction:column;justify-content:space-between;padding:28px;aspect-ratio:3/4}
.card .tags{align-self:flex-end;font:500 11px var(--font-head);letter-spacing:.04em;text-transform:uppercase;color:var(--muted)}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 7 | Confident blue and graph-paper restraint. The dark state is handsome but empty. |
| Originality | 7 | Ruler-tick nav and the rotated MENU tab are fresh details on a familiar portfolio shell. |
| Usability | 7 | Clear IA and an exit, but there is a dimmed-current-item confusion and empty cards. |
| Craft | 7 | Consistent 0.56 s ease-out transitions and theme parity; link contrast slips. |

---
id: insp-1-17
source: inspora
category: Product
status: analyzed
title: "analytics dashboard"
creator: "@_heyrico"
styles: [dark-premium, data-dense, terminal-mono]
patterns: [kpi-tile-row, highlighted-bar-chart, sidebar-nav-with-favorites, mono-for-metrics, delta-badge-with-arrow, horizontal-progress-bars, cropped-app-mockup]
mode: dark
palette: ["#1b1b1b", "#262626", "#383433", "#ffffff", "#ff7a1a", "#ff5a5f", "#2fd16a", "#1fb8ff"]
type_families: ["Inter (likely)", "JetBrains Mono / Geist Mono (likely)"]
type_class: [neo-grotesk, mono]
radius_px: [32, 24, 20, 12]
motion: null
scores: {aesthetics: 8, originality: 6, usability: 7, craft: 8}
craft_signals: [single-bar-highlight-gradient, mono-for-all-numbers-and-labels, pill-bars-fully-rounded, sidebar-meta-tags-right-aligned-mono, tile-dividers-1px, delta-colour-plus-arrow]
anti_patterns: [cropped-content-right-edge, red-green-only-delta-semantics, repeated-placeholder-values]
---
# analytics dashboard — @_heyrico

## 1. Snapshot
- **Subject:** A single 2560×2048 still of a dark CRM/analytics dashboard ("Leads Report", workspace "Acme Inc"). The window is cropped off the right and bottom edges.
- **Why it's remarkable:** It splits typography by data role. A neo-grotesk is used for names and navigation, and a monospace for every number, unit and tag. One orange-gradient bar is the only saturated mass in a near-black field.

## 2. Composition & layout
Measured in original px; the display was ×1.28.
- **Window:** starts at about (123, 123) on a #262626 backdrop, and its top-left corner radius is about 32 px.
- **Sidebar:** about 615 px wide (x 123→738), with a 1 px divider. Nav rows are about 74 px apart, and the active row "Leads Report" sits on a #262626 pill of about 570×70 px with a radius of about 16 px.
- **Groups:** separated by about 90 px gaps and introduced by mono caps labels ("FAVORITES", "SEARCHES").
- **Main column:**
  - A header bar about 100 px tall: "Leads Report" plus a mono count "13487 LEADS".
  - A three-up KPI strip about 335 px tall, split by 1 px vertical rules, with a 24 px outer radius.
  - A Sales Revenue chart card about 920 px tall containing 12 month bars, each about 134 px wide with gaps of about 16 px.
  - Two half cards below (Leads by Status, Web Visits).
- **Padding:** cards use about 36 px internal padding, and the space between cards is about 60 px.

## 3. Typography
- **Sans** (Inter-like): nav items about 37 px (≈28.9 pt at 1.28 scale), card titles about 32 px, and the workspace name about 37 px Regular. All are Regular weight.
- **Mono** (JetBrains Mono / Geist Mono-like, with a slashed zero in "$485,0ØØ"):
  - KPI values about 64 px Medium; the revenue value about 72 px.
  - Deltas and captions about 32 px.
  - Axis months about 30 px caps.
  - Sidebar meta tags ("COMPANY", "INVESTOR") right-aligned at about 30 px in grey.
- Scale: 30 / 32 / 37 / 64 / 72, so the hierarchy jumps once, from about 37 to about 64 (×1.7).

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #1b1b1b | app surface | 70% |
| #262626 | backdrop, inactive bars, active nav, chip fill | 22% |
| #383433 | borders / hairlines | 4% |
| #ffffff / #e6e6e6 | primary text | — |
| #ff7a1a → #ff9b3d | highlighted bar gradient, "Contacted" progress | ~3% |
| #ff5a5f | negative delta | — |
| #2fd16a | positive delta | — |
| #1fb8ff | "New Leads" progress bar | — |

WCAG checks:
- White on #1b1b1b: 17.22:1.
- Grey meta (#9a9a9a): 6.12:1.
- Red delta (#ff5a5f): 5.64:1.
- Green delta (#2fd16a): 8.57:1.
- The dimmest labels (≈#7a7a7a, axis months) are 4.01:1, which fails AA-normal at about 30 px but passes as large.

## 5. Depth & material
Depth comes from flat tone only: #1b1b1b cards on a #1b1b1b canvas are separated by 1 px #2e2e2e borders, and the backdrop is #262626. There are no shadows. The orange bar has a vertical gradient (lighter at top) and an inner highlight that reads as slightly glossy. The progress bars are also gradient pills.

## 6. Components & patterns
- **KPI tile:** a label (sans 32 px), a value (mono 64 px), and a footer delta of the form "12.5% ↓ vs Last Months". The delta is colour-coded and carries a direction arrow.
- **Growth chips:** 3m / 6m / 1y, each about 290×130 px with radius about 20 px on #262626. The chip row scrolls off the right edge.
- **Bar chart:** the bars are fully rounded at the top (radius = width/2 ≈ 67 px at top) with flat bottoms. Inactive bars are #262626; the selected month (MAY) is orange.
- **Status bars:** label in mono caps, a 52 px pill track, and the count right-aligned.
- **Sidebar:** search with a "/" shortcut key-cap, a collapse toggle icon, entity favourites with logos, and saved searches with coloured 32 px app-icon squares.

## 7. Motion
Still image, so no motion was observed. Likely affordances: hover on bars lifting #262626 → #303030, plus a tooltip, but none is shown.

## 8. Brand system
n/a — this is a product UI, not a brand system. Identity cues: a three-dot "Acme" logomark, orange as the single brand accent, and mono-as-voice.

## 9. UX
- **IA:** the IA is clear: nav, favourites and saved searches on the left, and metrics before chart before breakdown on the right.
- **Strengths:**
  - Deltas pair colour with an arrow, so colour isn't the only signal.
  - Tabular mono numbers align.
- **Weaknesses:**
  - The copy is placeholder-like: "12.5%" repeats five times, and "vs Last Months" is ungrammatical.
  - The chart has no y-axis or values, so the bar heights are uninterpretable.
  - The crop hides the third chip and the December bar.

## 10. Craft signals
- Only one bar is saturated (May); the other 11 share #262626.
- Every number on the page is mono, including "13487" in the header and "134"/"121" in the status rows.
- Sidebar meta tags are right-aligned to the same x (≈695 px).
- Bar caps are perfect semicircles matching the bar width; the progress tracks are full pills.
- The KPI strip uses 1 px internal dividers instead of three separate cards.

## 11. Reproduction recipe
```css
:root{--bg:#262626;--surface:#1b1b1b;--line:#2e2e2e;--muted:#9a9a9a;--text:#fff;
  --accent:#ff7a1a;--accent-2:#ff9b3d;--neg:#ff5a5f;--pos:#2fd16a;--info:#1fb8ff;
  --sans:"Inter",system-ui;--mono:"JetBrains Mono","Geist Mono",ui-monospace;}
.card{background:var(--surface);border:1px solid var(--line);border-radius:24px;padding:36px}
.kpi-row{display:grid;grid-template-columns:repeat(3,1fr)}.kpi-row>*+*{border-left:1px solid var(--line)}
.value{font:500 64px/1 var(--mono);font-feature-settings:"zero","tnum"}
.delta{font:400 30px var(--mono)}.delta.neg{color:var(--neg)}.delta.pos{color:var(--pos)}
.bar{width:134px;border-radius:67px 67px 24px 24px;background:#262626}
.bar[aria-current]{background:linear-gradient(#ff9b3d,#ff6a00)}
.tag{font:400 28px var(--mono);letter-spacing:.04em;text-transform:uppercase;color:var(--muted)}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Calm near-black with one hot accent. The sans/mono split looks sharp. |
| Originality | 6 | The dark-dashboard-with-one-highlighted-bar pattern is common. |
| Usability | 7 | Good contrast and arrow+colour deltas. The chart lacks a scale and the data is placeholder. |
| Craft | 8 | Consistent radii and alignment. Repeated values look unfinished. |

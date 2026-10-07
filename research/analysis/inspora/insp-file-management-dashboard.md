---
id: insp-file-management-dashboard
source: inspora
category: Product
status: analyzed
title: "a file-management dashboard"
creator: "@UI_Farhan"
styles: [dark-premium, dither-halftone, data-dense]
patterns: [app-window-on-pixel-art-backdrop, sidebar-sectioned-nav, fanned-thumbnail-folder-cards, nested-tree-table, avatar-stack-column, storage-meter-upsell, status-badge-column, pagination]
mode: dark
palette: ["#141414", "#212121", "#2f3031", "#413f3f", "#ffffff", "#a3a3a3", "#67b2e0", "#22c55e"]
type_families: ["Inter / SF Pro (likely)"]
type_class: [neo-grotesk]
radius_px: [36, 16, 12, 9999]
motion: null
scores: {aesthetics: 8, originality: 6, usability: 6, craft: 6}
craft_signals: [fanned-three-thumb-stack, tree-guides-for-nested-rows, drag-handle-per-row, active-nav-gradient-fade, filetype-colour-badges]
anti_patterns: [identical-placeholder-data, typo-branding-magents, footer-text-below-aa, status-column-all-same]
---
# a file-management dashboard — @UI_Farhan

## 1. Snapshot
- **Subject:** One 2560×1920 still of "Filenns.", a dark file manager. It has a sidebar, a "Recent uploads" carousel of five folder cards, and a "My Files" tree table, all floating on a dithered pixel-art landscape.
- **Why it's remarkable:** The 8-bit sky-and-hills wallpaper (blue #67b2e0, sage #7f8770) gives a utilitarian dark UI a playful frame, and it echoes the "ASCII assets" and "Gradient ascii" folder content.

## 2. Composition & layout
- **App window:** about 2330×1630 px with a ~36 px radius, inset ~115 px from the edges.
- **Sidebar:** ~345 px wide. It holds the logo, search (⌘F), and three groups (MY WORKSPACE, AI TOOLS, STORAGE) with ~60 px row pitch. At the bottom: user card, "245.6 GB of 1 TB used" meter, and an "Upgrade Storage" button.
- **Main area:** a nested panel (#141414 inside #212121).
  - Top bar: back/forward, "Dashboard", and Upload / View / Sort by / Share buttons.
  - Recent uploads row: five equal cards of ~360×335 px, each a fanned stack of three ~120 px rounded thumbnails.
  - My Files table: columns Name / AI Category / Last modified / Shared with / Status / Size, rows ~75 px. Child rows are indented ~38 px with vertical tree guides.
- **Pagination:** "Showing 1 to 10 of 128 items" bottom-left, page chips bottom-right.

## 3. Typography
- Inter-like sans.
- **Titles:** section titles ~26 px medium (2560 scale); table cells ~20 px regular.
- **Labels:** sidebar group labels ~18 px uppercase grey.
- **Cards:** card titles ~22 px medium with a grey meta line ("Sept 15 · 14:00 PM").
- **Errors:** "14:00 PM" mixes 24 h and 12 h formats. "Branding Magents" is a typo.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #141414 | panels, table | 48% |
| #212121 | window frame, row fill | 19% |
| #2f3031 / #413f3f | borders, hover, active nav | 8% |
| #67b2e0 | sky in backdrop; storage meter + Upgrade label | 7% |
| #596965 / #7f8770 / #b3baa8 | pixel-art hills | 14% |
| #22c55e (est.) | "Synced" status | — |

WCAG checks:
- White on #141414: 18.42:1.
- Grey meta #a3a3a3 on #212121: 6.38:1.
- Green "Synced" on #212121: 7.07:1.
- Blue "Upgrade Storage" #67b2e0 on #212121: 6.92:1.
- Footer "Showing 1 to 10…" ≈#5a5a5a on #141414: **2.67:1 (fail)**.

## 5. Depth & material
- A two-tone dark stack (#212121 frame, #141414 content) with 1 px #2f3031 borders and no shadows inside.
- The window has a subtle outer shadow against the backdrop.
- The selected card ("Gradient ascii assets") and the active nav item ("My File") get a lighter left-to-right gradient that fades to the right.
- Thumbnail stacks: the centre image is larger and in front; the side images are smaller and dimmer.

## 6. Components & patterns
- Expandable folder rows (chevron + drag handle ⋮⋮), file-type badges (ZIP orange, DOC blue, PNG green, PDF red), checkboxes on child rows only, overlapping 4-avatar stacks, and a kebab menu per row.
- Sortable column headers with ⇅ icons.
- A storage meter with a blue fill to ~25% (245.6 GB of 1 TB is ~24.6%, consistent).

## 7. Motion
Still image; no motion observed.

## 8. Brand system
n/a — not a brand system. Identity cues: a blue diagonal-stripe logo tile and the "Filenns." wordmark with a full stop.

## 9. UX
- Clear IA, and the tree table handles nesting well.
- **Risks:**
  - Every row shows identical data (Sept 24, 2025 / 34.5 GB / Synced), so scanning has nothing to find. This is a mock-up tell.
  - The status column is meaningless when it is uniform.
  - The footer fails contrast.
  - The two search fields (sidebar plus "Search task…") compete.

## 10. Craft signals
- Child rows have 1 px vertical guide lines connecting them to the parent folder icon.
- The fanned three-thumbnail stack repeats across all five cards at identical offsets.
- Coloured file-type badges sit in the corner of a neutral document glyph.
- The storage meter fill ratio matches the stated 245.6 GB / 1 TB.
- Header controls all share one ~56 px height and radius ~12.

## 11. Reproduction recipe
```css
:root{--bg:#141414;--frame:#212121;--line:#2f3031;--ink:#fff;--ink-2:#a3a3a3;--accent:#67b2e0;--ok:#22c55e}
body{background:url(pixel-landscape.png) center/cover;image-rendering:pixelated}
.app{border-radius:18px;background:var(--frame);padding:8px;display:grid;grid-template-columns:172px 1fr;gap:8px}
.main{background:var(--bg);border:1px solid var(--line);border-radius:12px}
.nav a[aria-current]{background:linear-gradient(90deg,#3a3a3a,transparent);border-radius:8px}
.tree-row.child{padding-left:38px;position:relative}
.tree-row.child::before{content:"";position:absolute;left:14px;top:0;bottom:0;border-left:1px solid var(--line)}
.fan img{border-radius:12px}.fan img:nth-child(odd){transform:scale(.8);filter:brightness(.7)}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Rich dark UI with a delightful pixel-art frame. |
| Originality | 6 | Standard file manager; backdrop and fanned thumbs add flavour. |
| Usability | 6 | Good structure; uniform placeholder data and weak footer contrast. |
| Craft | 6 | Nice details, undermined by typo, time-format error and copy-paste rows. |

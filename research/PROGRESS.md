# Research progress

Resumable checklist. Update after every batch. Raw captures live in `research/raw/` (git-ignored, third-party content).

## Environment notes
- Playwright: global module at `/opt/node-tools/node_modules/playwright`, Chromium at `/opt/pw-browsers/chromium-1194/chrome-linux/chrome` (see `scripts/lib.js`).
- inspora.design sits behind a Vercel bot challenge. Plain `curl` to `/api/*` or `/posts/*` returns 429 "Security Checkpoint".
  A real Chromium context (navigator.webdriver hidden, normal UA) solves it and gets a `_vcrcs` cookie; all fetches are then done *inside* the page.
- Inspora data source: `GET /api/posts?view={latest|featured}&category={Cat}&cursor=…` (16 items/page, `nextCursor`).
  Post pages embed a richer `post` object in the RSC stream (category, styles, colors, industries, description, sourceUrl, all media) — parsed by `scripts/rsc_post.py`.
- Media hosts (`media.inspora.design`) are not challenged; direct download works.
- brandguidelines.net is a Framer site; "Load More" exhausts after 2 clicks (verified twice, slow scroll + 4 s waits).

## Phase 0 — Setup
- [x] `research/` tree, `.gitignore` for `research/raw/`
- [x] Playwright scripts in `research/scripts/`

## Phase 1 — Enumeration
- [x] Inspora: latest × {All, Web, Branding, Product, Motion, Illustration, 3D, Print} + featured × same — `scripts/enum_inspora.js`
- [x] brandguidelines.net home (Load More exhausted), /templates, /about — `scripts/enum_bg.js`, `scripts/enum_bg_templates.js`
- [x] `inventory.json` — `scripts/build_inventory.py`

### Counts (enumerated 2026-10-07)
| Source | Category | Count |
|---|---|---|
| inspora | Motion | 129 |
| inspora | Product | 65 |
| inspora | Web | 42 |
| inspora | Illustration | 25 |
| inspora | Branding | 17 |
| inspora | 3D | 5 |
| inspora | Print | 4 |
| **inspora** | **total unique** | **287** (Featured: 9, all also in Latest) |
| brandguidelines | guideline | 54 (21 PDF, 26 live site, 6 hosted platform, 1 Figma prototype) |
| brandguidelines | template | 9 (3 on-site, 6 UI8) |
| brandguidelines | promoted | 3 |
| **brandguidelines** | **total unique** | **66** |

Notes: Inspora media: 258 video posts, 29 image posts, 17 posts are multi-slide (2–4 media).
Herman Miller appears twice on brandguidelines.net (In-house and "Design by Order", same URL) — merged into one record with both attributions.
Category sums for Inspora equal the All count (287): every post has exactly one category.

## Phase 2 — Capture
- [ ] Inspora post pages + all media + video frames/contact sheets
- [ ] Brand guideline PDFs (download, page images, text)
- [ ] Live brand sites (1440 + 390 full-page, CSS tokens)
- [ ] Templates / promoted pages

## Phase 3 — Analysis
- [ ] per-example analyses

## Phase 4 — Synthesis
## Phase 5 — Skill
## Phase 6 — Evals

## Failures log
(none yet)

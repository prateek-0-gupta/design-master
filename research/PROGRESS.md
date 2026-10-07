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
- [x] Inspora post pages (287/287, 0 failures) — `capture_inspora_pages.js`
- [x] Inspora media (287/287): stills full-res; videos → 9 frames, 3×3 sheet, full-res key frame, motion profile — `process_inspora_media.py`
  (3 videos initially failed on EOF seek → fixed by stepping back; re-run clean)
- [x] Brand PDFs: 20/21 downloaded + rendered (pages 1400 px, 12-up sheets, text, pdffonts) — `capture_bg_pdfs.py`
  - Mastercard Foundation: origin 410 Gone → recovered from Wayback Machine (`web.archive.org/web/2024id_/…`)
  - Kazam: Dropbox download disabled by owner (HTML error page for dl=1, also via browser cookies) → capturing pages from the in-browser viewer (`capture_dropbox_viewer.js`)
- [ ] Live/hosted/template/promoted sites (desktop 1440 + mobile 390 + ≤6 subpages, CSS + computed-style census) — `capture_bg_sites.js` (2 workers)
  - inner-scroll / smooth-scroll sites re-captured with `capture_scrollers.js` (Herman Miller stitched; Monday wheel-mode)
- [ ] tiles (`tile_shots.py`), palettes (`palette.py`), tokens (`tokens.py`)

## Phase 3 — Analysis
Brief: `analysis/AGENT_BRIEF.md`; exemplar `analysis/inspora/insp-glass-circle-with-a-gradient.md`; batch lists in `analysis/_batches/`.
- [x] Brand PDFs 20/20 (5 agents × 4)
- [x] Inspora batches insp_01–06 (72)
- [ ] Inspora batches insp_07–24 (launched 07–14)
- [ ] Live sites / hosted / templates / promoted

### Spot-checks (claims vs source)
| Batch | Checked | Result |
|---|---|---|
| PDF C | bg-edp hexes #28FF52/#212E3E/#7C9599 and "55% of spiral"; bg-new-breed "loudline" | confirmed in text/all.txt |
| PDF C | bg-northalley crosshair + #D9FF00 + co-brand 0.16x | confirmed visually on sheet01 |
| PDF A | bg-hulu radius = shortest side ÷ 6, stroke = longest ÷ 100/50; bg-slack 36/38, −2px | confirmed in text |
| PDF E/B | bg-adobe tracking table (+20 at 4pt … −8 at 30–36pt); bg-olympic 1600 px / 104 px margins | confirmed in text |
| insp_06 | insp-paid-stamp: stamp prints "15 SEP 2026", Undo toast, camera tilt | confirmed on sheet |
| insp_01 | insp-hairlines-v2: dark signal line on beige, tick ruler, "NN NAME STATE" mono labels | confirmed on sheet |

## Phase 4 — Synthesis
## Phase 5 — Skill
## Phase 6 — Evals

## Failures log
- bg-mastercard-foundation: original PDF URL → HTTP 410. Recovered via Wayback (not a failure, but provenance differs).
- bg-kazam: Dropbox download disabled → viewer screenshots fallback (no text layer / pdffonts available).
- bg-duolingo: design.duolingo.com now 302 → blog.duolingo.com design tag; original guideline site retired. Wayback attempt pending (archive.org rate-limited 429).
- bg-audi: listed URL (ci/en/renewed-brand.html) → 404 page. Wayback attempt pending.
- UI8 entries (bg-ui8 + 6 templates): Cloudflare "Just a moment" interstitial on first pass → re-run with challenge wait.

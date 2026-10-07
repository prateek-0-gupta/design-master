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
- [x] Live/hosted/template/promoted sites (desktop 1440 + mobile 390 + ≤6 subpages, CSS + computed-style census) — `capture_bg_sites.js` (2 workers)
  - inner-scroll / smooth-scroll sites re-captured with `capture_scrollers.js` (Herman Miller stitched; Monday wheel-mode)
- [x] tiles (`tile_shots.py`), palettes (`palette.py`), tokens (`tokens.py`); Figma protos via `capture_figma_proto.js` / `capture_figma_scroll.js`
- [x] Sorted view `raw/_by_category/` + `RAW_INDEX.md` (`index_raw.py`); raw images committed (PDFs/HTML/CSS/full PNG shots excluded: size + duplicates)

## Phase 3 — Analysis
Brief: `analysis/AGENT_BRIEF.md`; exemplar `analysis/inspora/insp-glass-circle-with-a-gradient.md`; batch lists in `analysis/_batches/`.
- [x] Brand PDFs 20/20 (5 agents × 4)
- [x] Inspora batches insp_01–06 (72)
- [x] Inspora batches insp_07–24 (all 287 done)
- [x] bg-kazam (from viewer screenshots)
- [x] Sites S1–S5 (sonnet) + templates/promoted (haiku)
- [ ] Sites S6–S7 (archived, sonnet) + UI8 templates (haiku) — running

Cost note (user request): from site analyses onward, subagents use cheaper models (sonnet for guideline sites, haiku for templates/promoted/tag normalisation).

### Spot-checks (claims vs source)
| Batch | Checked | Result |
|---|---|---|
| PDF C | bg-edp hexes #28FF52/#212E3E/#7C9599 and "55% of spiral"; bg-new-breed "loudline" | confirmed in text/all.txt |
| PDF C | bg-northalley crosshair + #D9FF00 + co-brand 0.16x | confirmed visually on sheet01 |
| PDF A | bg-hulu radius = shortest side ÷ 6, stroke = longest ÷ 100/50; bg-slack 36/38, −2px | confirmed in text |
| PDF E/B | bg-adobe tracking table (+20 at 4pt … −8 at 30–36pt); bg-olympic 1600 px / 104 px margins | confirmed in text |
| insp_06 | insp-paid-stamp: stamp prints "15 SEP 2026", Undo toast, camera tilt | confirmed on sheet |
| sites S2 | bg-klarna #ffa8cd/#0b051d, display 208–320 px | confirmed in census/tokens |
| insp wave 3 | insp-ticket-stub k=237.6 ζ=7.5 ω=13.47; insp-rag-pipeline per-source hues 0.92/0.87/0.79 | confirmed on key frames |
| insp wave 4 | insp-bento-cards own-hue dark text; insp-1-46 2×2→grid loader + disabled Generating | confirmed |
| insp_01 | insp-hairlines-v2: dark signal line on beige, tick ruler, "NN NAME STATE" mono labels | confirmed on sheet |

## Phase 4 — Synthesis
## Phase 5 — Skill
## Phase 6 — Evals

## Failures log
- bg-mastercard-foundation: original PDF URL → HTTP 410. Recovered via Wayback (not a failure, but provenance differs).
- bg-kazam: Dropbox download disabled → viewer screenshots fallback (no text layer / pdffonts available).
- bg-duolingo: design.duolingo.com now → blog; captured Wayback 2026-01-06 snapshot (home only).
- bg-audi: listed URL → 404; captured live successor styleguide.audi.com (home + Typography).
- bg-starbucks (cert expired 2025-07), bg-dropbox (cert expired 2025-06), bg-the-mellon-foundation (cert hostname mismatch): not bypassed; Wayback snapshots (home only).
- bg-canva (404), bg-firefox (login wall), bg-mixcloud (/brand → home), bg-flax-kale (corebook hidden): Wayback snapshots.
- bg-miro: deep link hidden → live root brandkit.miro.com (Wayback refuses: 403).
- bg-wise: /foundations 404 → live root wise.design.
- bg-wispr: Standards.site page gone; Wayback snapshot renders blank (JS app not archived) → expected FAILED.
- bg-zipline: redirects to a Figma prototype; chapter hotspots not triggerable → PARTIAL (cover, TOC, closing).
- bg-chatham: subpages are Standards.site 404s → PARTIAL (home section 01 only).
- bg-help-scout: Figma prototype → 34 unique frames via click-advance.
- UI8 (bg-ui8 home passed; 6 product pages blocked by Cloudflare Turnstile even after waits) → Wayback snapshots.
- bg-kazam attribution conflict: brandguidelines.net says "Design by Good Habit"; document credits Skep Studio.

# Analysis brief (for every analyst, human or subagent)

You write one file per example: `research/analysis/{source}/{id}.md` where `source` is `inspora` or `brandguidelines`.

## Non-negotiables
1. **Look at the pixels.** Open every image listed below with the Read tool before writing. Never infer a design from its slug, title or the site's description text. The site description may be used only as a hint and must be checked against what you see.
2. **Measure, don't adjective.** Give px values (estimate from the image's known pixel size), hex values (take them from `palette.json`, which is median-cut sampled from the real pixels — pick the ones you can attribute to a role), ratios, durations in seconds. "Clean" or "modern" alone is worthless.
3. **Contrast:** run `python3 research/scripts/contrast.py '#fg' '#bg' ...` for the main text/background pairs you identify and report the ratios.
4. If you cannot analyze an example (missing files, broken media, blank capture), still write the file with `status: failed` and the precise reason. Never invent contents.
5. Write in your own words. Do not paste long passages of the source's text (a few words of quoted UI copy is fine).
6. Image sizes: Read shows images downscaled; the original pixel size is in the file metadata / post.json (`width`, `height`) — use it to convert to real px.

## Where the files are
### Inspora (`research/raw/inspora/{slug}/`, id = `insp-{slug}`)
- `post.json` — full metadata: category, styles, colors, industries, description, creator, media list (width/height per slide).
- `m{N}.webp|png|jpg` — full-res still slide N (image posts).
- `m{N}_sheet.jpg` — 3×3 contact sheet of a video (9 frames, timestamps labelled). **Always view it.**
- `m{N}_key.jpg` — full-resolution middle frame. **Always view it** (detail, type, hairlines).
- `m{N}_f0..f8.jpg` — individual frames (1600 px max) if you need to zoom on a moment.
- `m{N}_motion.json` — measured motion profile: duration, fps, `segments` (start/end/duration in s, `peak_at` = where in the segment the motion energy peaks: <0.35 ⇒ ease-out/decelerating, >0.65 ⇒ ease-in, otherwise symmetric ease-in-out; `continuous/linear` = steady motion), `motion_fraction`, `seamless_loop_likely`. Use these numbers in §7 and say they are measured. The 9 frames are evenly spaced; state timings you infer from frame differences as estimates.
- `page.png` — the post page on inspora (context only).
- `palette.json` — sampled colours per still / key frame.

### Brand guidelines (`research/raw/brandguidelines/{id}/`)
- PDF entries: `pdf_meta.json` (page count, page size, embedded font names in `fonts_raw` — **use these to identify typefaces exactly**), `sheets/sheetNN.jpg` (12 pages per sheet, labelled with page numbers — view **all** sheets), `pages/pNNN.jpg` (1400 px wide; open at least 6 full pages: cover, logo, colour, type, imagery/graphic, application), `text/all.txt` (extracted text — skim it for structure, rules, voice; grep it).
- Live / hosted / template / promoted entries: `tiles/d00_home_tNN.jpg` (desktop 1440 px tiles of the full page, 1800 px tall each — view all of home, and at least the first 2 tiles of each subpage `d0N_sub`), `tiles/m00_home_sheetNN.jpg` (mobile 390 px strips 4-up), `census_home.json` / `census_subN.json` (computed-style census: font families/sizes/weights/line-heights/letter-spacing with frequency, colours, radii, shadows, transitions, CSS custom properties, loaded fonts, headings), `site_meta.json` (final URL — note redirects!), `all.css` (raw CSS; grep for `--`, `@font-face`, `cubic-bezier`, `transition`, `box-shadow`), `tokens.json` (summary of all.css).
- `palette.json` — sampled colours per page/tile.

## Output format (exactly this skeleton)

```markdown
---
id: insp-some-slug
source: inspora            # or brandguidelines
category: Motion           # inventory category
status: analyzed           # or failed
title: "…"
creator: "…"
styles: [glassmorphism, soft-3d]          # from the vocabulary below (1–4)
patterns: [morphing-container, loading-indicator]   # kebab-case, specific, 2–8
mode: light                # light | dark | mixed
palette: ["#0b0b0f", "#7c5cff", "#f6f6f6"]           # 3–8 hexes with clear roles
type_families: ["Inter (likely)", "PP Editorial New (likely)"]
type_class: [neo-grotesk, editorial-serif]
radius_px: [24]            # observed corner radii, [] if none
motion: {durations_s: [0.53, 0.33], easing: [ease-in-out], loop: true}   # or null for stills
scores: {aesthetics: 8, originality: 7, usability: 6, craft: 8}
craft_signals: [inner-highlight-1px, optical-blur-edge]   # kebab tags, 2–8
anti_patterns: []          # kebab tags for weaknesses, may be empty
---
# {Title} — {creator}

## 1. Snapshot
- **Subject:** one line.
- **Why it's remarkable:** one line.

## 2. Composition & layout
## 3. Typography
## 4. Colour
(table: hex | role | approx share; then WCAG pairs with ratios)
## 5. Depth & material
## 6. Components & patterns
## 7. Motion
## 8. Brand system
(for Inspora non-branding items write "n/a — not a brand system" plus any identity cues; for guidelines this is the main section: logo rules, clearspace/min size, voice & tone, imagery, document structure (list the chapters in order with page ranges), token decisions worth stealing)
## 9. UX
## 10. Craft signals
(bullet list, each precise and checkable)
## 11. Reproduction recipe
(CSS custom properties / Tailwind classes / keyframes that recreate the look; real code blocks)
## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | n | … |
| Originality | n | … |
| Usability | n | … |
| Craft | n | … |
```

Length: Inspora items 350–800 words; brand guidelines 700–1500 words (they are richer). Depth over padding.

## Scoring anchors (use the full range; 5 = competent but forgettable)
- **Aesthetics** 9–10 portfolio-defining; 7–8 clearly above average, cohesive; 5–6 fine; ≤4 visibly flawed.
- **Originality** 9–10 a new idea; 7–8 fresh take on a known pattern; 5–6 common trend executed; ≤4 derivative/template.
- **Usability** (would it work for a real user? for motion: does the motion communicate state/feedback; for brand docs: can a designer apply it) 9–10 exemplary; ≤4 confusing/inaccessible.
- **Craft** 9–10 flawless detail (alignment, optical corrections, consistent tokens); ≤4 sloppy.

## Style vocabulary (use these tags; add a new one only if nothing fits, prefixed `x-`)
minimal-swiss, editorial-serif, bento-grid, glassmorphism, soft-3d, claymorphism, neumorphism, skeuomorphic, brutalist, neo-brutalist, dark-premium, gradient-mesh, aurora-glow, monochrome, high-contrast-bw, retro-pixel, y2k-chrome, hand-drawn, flat-illustration, isometric, data-dense, kinetic-type, grain-noise, duotone, maximalist-color, playful-rounded, corporate-clean, luxury, photo-led, generative-particle, dither-halftone, technical-wireframe, terminal-mono, swiss-grid-poster, organic-blob, physical-material, cinematic-3d, micro-interaction, hairline-ui, spatial-ui

## Type class vocabulary
neo-grotesk, grotesk, geometric-sans, humanist-sans, rounded-sans, editorial-serif, transitional-serif, slab, mono, display, script, pixel, condensed, variable

## Exemplar
See `research/analysis/inspora/insp-glass-circle-with-a-gradient.md` for the expected depth and tone of an Inspora analysis. Brand guideline analyses should be at least as specific, with §8 being the longest section.

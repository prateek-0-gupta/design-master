# Prompt: Full design study → AAA UI/UX skill

Paste everything below the line into a fresh Claude Code session on this repo.

---

You are a senior design researcher and design-systems engineer. Your job runs in two stages:

1. Study every example on two reference sites until you understand why each one works.
2. Turn what you learned into a skill (a `SKILL.md` plus reference files). A coding agent will load this skill to produce UI and UX that matches or beats the best work on these sites.

This is a long task. Work methodically and save progress to disk as you go. Don't summarize from memory or skim. **Every** example must get its own analysis.

## Sources

- **https://www.inspora.design/** is a gallery of design shots. Its filter categories are Web, Branding, Product, Motion, Illustration, 3D and Print (`/?category=…`), and it has Latest and Featured tabs. Entry pages live at `/posts/{slug}`, and some entries are multi-slide. The page is rendered with JavaScript and updates hourly, so a plain fetch will miss content.
- **https://www.brandguidelines.net/** is a showcase of real brand guideline documents. Some are hosted PDFs (often on Dropbox), some are live brand sites (for example `design.duolingo.com` and `brand.klarna.com`), and some are paid templates under `/templates/*`. The list loads more entries through a "Load More" button.

## Phase 0: Setup

- Create the working folder `research/`. Add `research/raw/` (screenshots, PDFs, HTML snapshots) to `.gitignore`, because that material is third-party copyrighted content. Commit only your own notes, analysis and derived principles.
- Drive a real browser with Playwright. Chromium is pre-installed at `/opt/pw-browsers/chromium`; don't run `playwright install`. Write the scripts in `research/scripts/`.
- Keep a `research/PROGRESS.md` checklist and update it after every batch, so a later session can resume the work.

## Phase 1: Exhaustive enumeration

Don't trust the first page load.

- **Inspora:** visit All plus every category, on both Latest and Featured. Scroll until no new items appear and capture the network/API responses that feed the grid; the JSON is usually richer than the DOM. Deduplicate by slug.
- **brandguidelines.net:** click "Load More" until it disappears, and cover every homepage section and `/templates`. Record the brand, the attribution (In-house, Design by X or Promoted) and the target URL for each entry.
- Write `research/inventory.json` with one record per example: id, source, url, category, title or brand, creator, slide count and asset type. Report the final count for each source and each category before you move on. If a site blocks or rate-limits you, slow down and retry. Don't skip entries silently; log each failure in `PROGRESS.md`.

## Phase 2: Capture

- **Inspora:** for each post, take full-resolution screenshots of every slide, plus the post page itself. If an entry is motion or video, capture several frames, and note the timing and easing you observe.
- **Brand guidelines:**
  - PDFs: download each one and extract page images and text.
  - Live brand sites: take full-page screenshots at 1440 and 390 px widths. Also extract the real tokens from the CSS: font families, the type scale, colour custom properties, spacing, radii, shadows and motion durations.
- Save everything under `research/raw/{source}/{id}/`.

## Phase 3: Per-example analysis (the core)

Look at every image yourself with the Read tool, which gives you vision. Never infer a design from its slug. For each example, write `research/analysis/{source}/{id}.md` using this template:

1. **Snapshot:** the subject in one line, and what makes it remarkable in one line.
2. **Composition and layout:** the grid, columns, margins, alignment, focal point, how the eye travels, density, and use of negative space.
3. **Typography:** the typefaces (identify them or name the closest match), the scale ratio, weights, tracking, leading, measure, and how the hierarchy is built.
4. **Colour:** the palette as hex values sampled from the pixels, the role of each colour, contrast (check WCAG pairs), use of gradients, light versus dark mode, and saturation strategy.
5. **Depth and material:** shadows, blur or glass, borders, textures and noise, lighting, and 3D treatment.
6. **Components and patterns:** the UI elements present and their states, plus any novel interaction patterns.
7. **Motion:** the implied or observed choreography, durations, easing and purpose.
8. **Brand system** (for guidelines): logo rules, voice and tone, imagery direction, how the guideline document itself is structured, and which token decisions are worth stealing.
9. **UX:** information architecture, affordances, feedback, accessibility risks and friction.
10. **Craft signals:** the specific details that separate this example from average work. Name them precisely, for example "optical kerning on display sizes" or "1px inner highlight on cards at 8% white".
11. **Reproduction recipe:** concrete CSS and Tailwind values, or a token set, that would recreate the look, with code snippets.
12. **Rating:** score 1–10 on aesthetics, originality, usability and craft, with one-line justifications.

Work in batches. Parallel subagents are fine, for example one per category, but each subagent must follow the same template and must look at the actual images. After each batch, spot-check two analyses against their images to catch hallucinated detail.

## Phase 4: Cross-example synthesis

Write `research/synthesis/` with one file per topic:

- **Recurring patterns** for each category, with a frequency count and the example ids behind each pattern.
- **A taxonomy of styles:** for example glassmorphism, bento grids, editorial serif, brutalist and soft 3D. For each style, give its defining parameters, when to use it, and when it fails.
- **Token benchmarks:** the distribution of type scales, spacing bases, radii, shadow recipes and palette structures you actually observed, plus the defaults you recommend.
- **The craft checklist:** the 50–100 specific details that keep appearing in the top-rated work.
- **Brand-system anatomy:** how the best guideline documents are structured, and what a complete identity system needs.
- **Anti-patterns:** what the weaker examples do wrong.
- **Gaps:** what none of these examples does well (for example accessibility, states, responsiveness or empty and error states). This is where the skill can outshine the references.

## Phase 5: Build the skill

Load the `skill-creator` skill and follow its process. Create `skills/aaa-design/`:

- **`SKILL.md`:** keep it lean, ideally under about 500 lines, and make it procedural. Cover:
  - how to read a brief
  - how to choose a direction from the style taxonomy
  - how to commit to a token system before writing any component
  - layout and type rules
  - the craft checklist as a final pass
  - a self-critique loop: render the result, screenshot it, compare it against the rubric, and iterate
  - required UX coverage: all states, keyboard and focus handling, reduced motion, contrast, and responsive breakpoints
- **`references/`:** the style taxonomy with recipes, token presets, typography pairings, colour systems, motion specs, component patterns, brand-system templates and anti-patterns. Each file must be self-contained so the agent loads only what it needs.
- **`examples/`:** three to five small reference implementations in HTML, Tailwind or React that demonstrate the top styles and pass the checklist.
- **A scoring rubric** the agent applies to its own output.

Write principles and recipes in your own words. Don't copy third-party assets or long passages of text into the skill.

## Phase 6: Prove it

Write five varied design briefs:

- a SaaS landing page
- a dashboard
- a mobile onboarding flow
- a brand identity page
- a portfolio

Have one subagent build each brief **without** the skill and another build it **with** the skill. Screenshot every result and score it with the rubric. Then iterate on the skill until it wins clearly on every brief. Record the before-and-after scores in `skills/aaa-design/EVALS.md`.

## Ground rules

- Be thorough over fast. If you can't analyze an example, mark it as failed and give the reason; never invent its contents.
- Make concrete, measurable claims with values and ids, not vague adjectives.
- Commit after each phase with a clear message and push to the working branch.
- When you finish, report:
  - the example counts covered per source
  - the failures
  - the top ten insights
  - how the skill is structured
  - the eval results

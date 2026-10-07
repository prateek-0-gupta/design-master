# Gaps: what none of the references do well

These gaps are where an agent can beat the showcase work. Every claim is backed by a count from the 348 analysed examples.

## 1. Accessible contrast (the largest gap)
- **Inspora:**
  - 89.9% of examples have at least one text pair below 4.5:1, and 73.8% have one below 3:1.
  - The median worst pair is 2.27:1.
  - 44.5% of the 1,320 reported pairs fail AA.
- **Brand documents:**
  - 86.2% have at least one failing pair.
  - Several *approve* failing pairs in print: Hulu "meets standards" at 3.04:1, Olympic white on yellow at 1.82:1, Kazam white on lilac at 1.74:1.
- **Analyst scores don't penalise it** (see `anti-patterns.md`).
- **To win:** compute every pair, ship AA-safe "ink" shades per hue, and make contrast a hard gate.

## 2. States beyond the happy path
- Only 4 examples show empty, error or 404 states. The two 404 pages, insp-404-page and insp-404-page-2, are illustrations; neither offers recovery beyond a link.
- Toast, confirmation and undo appear in 18.
- Loading or "thinking" appears in 42. These are the strongest area, and AI products drove it.
- Disabled, focus-visible, validation errors, offline and permission states are essentially absent.
- **To win:** design all eight states per interactive component:
  - default
  - hover
  - focus-visible
  - active/pressed
  - disabled
  - loading
  - error
  - empty/success

## 3. Keyboard and focus
- One reference explicitly separates hover from a keyboard focus ring (insp-8-0: a 2px ring offset 4px).
- Keyboard hints appear on actions in about 3 (insp-1-30's "Approve ↵").
- No brand document specifies focus styles.
- **To win:**
  - a visible 2px focus ring in the accent's AA shade with a 2–3px offset;
  - logical tab order;
  - Esc closes overlays;
  - arrow keys inside composite widgets.

## 4. Reduced motion
- 261 videos and 0 demonstrations of a reduced-motion variant.
- Measured motion often runs ≥ 0.9s (p90) with large travel and parallax, exactly what `prefers-reduced-motion` should tame.
- **To win:** every motion token has a reduced variant: crossfade ≤ 150ms, no parallax, no auto-advancing carousels.

## 5. Responsiveness
- Inspora shots are single-viewport, desktop-sized compositions (median video 1920×1350).
- Live brand sites broke on mobile in several cases: SeatGeek's fixed sidebar splits words mid-way, Super.com's sticky nav repeats, and Klarna's reveal-on-scroll leaves blank tiles until triggered.
- **To win:** design at 390, 768 and 1280+, using fluid type (`clamp`), container-aware components, and touch targets ≥ 44px.

## 6. Data truthfulness
- Decorative charts misstate data. insp-components-n3xt's 96-dot chart is 39.6% for "24%"; insp-follower-count's crowd isn't 5,000.
- **To win:** derive chart geometry from data, label units, and give charts a text alternative.

## 7. Motion documentation in brand systems
- Of 53 brand documents, only IBM and Odido specify motion tokens. Hulu's 138-page book has none.
- **To win:** ship duration and easing tokens with the identity (`token-benchmarks.md`).

## 8. Content realism
- 20 examples had typos, lorem ipsum, pasted copy or repeated placeholder values.
- **To win:** write real, specific microcopy: numbers, units, names, plausible data.

## 9. Performance and implementation cost
- Shader, glass and 3D work is shown as video with no fallback. The live glass examples drop contrast as the backdrop moves.
- **To win:** CSS-first effects; a static fallback for WebGL; `backdrop-filter` only on small surfaces; images sized and lazy-loaded.

## 10. Internationalisation
- Only Slack (EU strings 10% smaller, Japanese 15% smaller), EDP (12 scripts) and Dubai and Naseem (Arabic) address it. The Naseem document justifies its Arabic text by stretching the connecting strokes between letters, which is incorrect.
- **To win:** leave room for 30% string growth, avoid fixed-width text containers, and support RTL with logical CSS properties.

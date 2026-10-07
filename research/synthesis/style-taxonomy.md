# Style taxonomy

Built from the `styles:` tags of 347 analysed examples. Here `n` is the number of examples carrying the tag and `mean` is the mean of the summed 4-axis score (max 40). Each style lists what defines it, the values observed in the best examples, when to use it and when it fails. Example ids point to `research/analysis/`.

Two cross-cutting findings:

- Styles are layers, not choices. The median example combines 2–3 tags, for example `minimal-swiss` + `micro-interaction` + `physical-material`.
- The top work almost always pairs a **quiet structural style** (minimal-swiss, hairline-ui, corporate-clean, dark-premium) with **one expressive layer** (a material, a shader object, a physical metaphor, a pixel texture). Examples that stack two or more expressive layers score lower. glassmorphism + aurora-glow + gradient-mesh appear together in the weakest web entries: insp-glassmorphism-animation scored 24, insp-8-2 scored 25.

---

## A. Structural bases (pick exactly one)

### 1. Minimal-Swiss / neutral product UI (n=109, mean 29.3)
- **Defining parameters:**
  - Neo-grotesk type (229/287 Inspora examples use one), regular to medium weights.
  - Hierarchy comes from size and grey value, not weight.
  - Achromatic surfaces (#fff/#f7f7f7/#f2f2f2), one accent at most.
  - 1px borders at 6–10% black or none.
  - Radii from a 2–3 value set.
- **Best:** insp-1-41 (search field morphs into country silhouette), insp-cartridge-portfolio, insp-photo-folders, insp-1-42 (verb tense as state), insp-tiny-animated-svg.
- **Use for:** SaaS, tools, dashboards, anything where content or data is the hero.
- **Fails when:** nothing is allowed to be expressive. Low-ranked members are generic marketplace templates (bg-cobalt/form/owire-brand-guide all scored 22). Without an expressive layer it reads as a template.

### 2. Dark premium (n=79, mean 29.9)
- **Defining parameters:**
  - Canvas #000–#0e0e0e, with surfaces stepped by lightness: #000 → #121212 → #1c1c1c → #2a2a2a.
  - No drop shadows. Elevation comes from tint plus a 1px #ffffff0f–1f border.
  - All saturation is quarantined in one hero object (orb, shader, photo).
  - Secondary text is #8a8a8a or lighter (6:1 on #000).
- **Best:** insp-5-8 (AI states as shape-morphing dot loaders), bg-edp, insp-bankito-frozen-card, insp-1-40, insp-color-text-in-notes, insp-glass-circle-with-a-gradient.
- **Use for:** AI products, fintech, developer tools, media.
- **Fails when:** greys are picked by eye. Dark UIs had the most sub-3:1 secondary text, for example #5c5c5c on #1c1c1c at 2.55:1 and #4c4e4c bars at 2.0:1 (insp-support-analytics). Pure #000 with pure #fff text also halates at large sizes.

### 3. Corporate-clean (n=80, mean 28.3)
- **Defining parameters:** brand colour on white, rounded 8–16px, humanist or geometric sans, photography.
- **Best:** bg-edp, insp-1-48, insp-1-30.
- **Use for:** enterprise, institutions.
- **Fails when:** it becomes the default. Its lowest members (bg-make 20, bg-instagram 21) are the lowest-rated guidelines overall.

### 4. Editorial serif (n=36, mean 30.4)
- **Defining parameters:**
  - A high-contrast serif for display (PP Editorial / Tiempos / GT Super-like) over a neo-grotesk body; the ratio display ÷ body is ≥ 4.
  - Italic used as emphasis inside headlines, not as a separate style.
  - Warm paper ground (#f4f1ea–#f7f6f4).
- **Best:** insp-melon-jelly (scientific-specimen sliders with plain-word end labels), insp-tiny-animated-svg, insp-stamp-shader, insp-1-55.
- **Use for:** portfolios, culture, premium consumer, research.
- **Fails when:** body text is also serif at small sizes on screens, or when the serif is used for UI labels.

### 5. Hairline / technical-wireframe (hairline n=37 mean 29.8; technical n=27 mean 30.5)
- **Defining parameters:**
  - 1px lines at 10–20% ink.
  - Mono labels in "NN NAME STATE" form.
  - Dashed construction lines, crop marks and dimension call-outs (e.g. "236 × 292").
  - Exactly one dark "signal" line.
- **Best:** insp-ticket-stub (prints its own spring constants k=237.6, ζ=7.5), insp-hairlines-v2, insp-model-router, insp-rag-pipeline.
- **Use for:** developer and infra tools, AI pipelines, portfolios of engineers.
- **Fails when:** hairlines carry information. insp-hairlines-v2's object lines are 1.42:1, and insp-follower-count's ticks are 1.4:1.

### 6. Data-dense (n=14, mean 30.1)
- **Defining parameters:**
  - Mono caps metadata (~12–14px, +0.08em) with sans names and values.
  - Tabular figures.
  - One hue per entity, threaded through every layer (insp-rag-pipeline, insp-1-48, insp-model-router).
- **Use for:** analytics, observability, agent consoles.
- **Fails when:** greyscale chart marks drop below 3:1 against the surface.

## B. Expressive layers (add one)

### 7. Physical material / skeuomorphic (physical n=63 mean 30.7; skeuomorphic n=29 mean 30.9) — the highest-rated layer
- **Defining parameters:** the interface borrows one real object, its behaviour and its failure mode. Examples:
  - a stamp that prints the chosen date (insp-paid-stamp);
  - a receipt that prints line by line (insp-1-35);
  - a ticket that springs (insp-ticket-stub);
  - a folder with a frosted flap (insp-photo-folders);
  - an Etch-A-Sketch signature (insp-2-6).
- **Material cues:**
  - shading in a darker shade of the object's own hue, not black (insp-2-4: #17852f under #2bc955);
  - perforations;
  - a 0px-radius "paper" next to a rounded UI (insp-tap-get-invoice).
- **Use for:** confirmations, empty states, onboarding moments, portfolio signatures.
- **Fails when:** applied to every control, or when the metaphor hides the value (insp-1-2: the jelly slider refracts its own number to 1.52:1).

### 8. Soft 3D / clay (soft-3d n=60, mean 29.7)
- **Defining parameters:** rendered or CSS-faked volume, large radii (24–48px), soft key light from top-left, ambient-occlusion shadow 0 20–40px 60–120px at 10–20%, pastel or saturated single hues.
- **Best:** insp-melon-jelly, insp-1-41, insp-ghost-pass.
- **Fails when:** white labels sit on pastel volumes. insp-bright-candy-icons scored 24; its tinted glyphs measure 1.39–1.56:1.

### 9. Glassmorphism / spatial (glass n=42, mean 29.5; spatial n=9, mean 30.4)
- **Defining parameters:**
  - backdrop blur 16–40px;
  - a 1px inner rim at 20–40% white;
  - a tint sampled from what is behind (insp-look-away-preview tints from the wallpaper, #5b3603);
  - refraction or chromatic fringe only at the rim (insp-9-8: refraction index 1.52, aberration 0.01).
- **Use for:** overlays, navigation, media-heavy apps, AR/OS concepts.
- **Fails when:**
  - text sits on glass over moving or bright content: liquid-glass swings 2.58–8.82:1, insp-1-2 drops to 1.52:1;
  - the glass is the only idea: insp-glassmorphism-animation, insp-8-7 and insp-9-2 are the lowest in the group.
- Rule: glass carries chrome, never body copy.

### 10. Orb / shader / aurora / gradient-mesh (aurora n=32, gradient-mesh n=22, grain n=21, generative n=19)
- **Defining parameters:** a single luminous object (orb, mesh, liquid metal) as the brand or state signifier, with grain at 2–6% to kill banding, on a near-black or paper ground.
- **Best:** insp-5-8, insp-stamp-shader, insp-shader-dial, insp-1-14, insp-glass-circle-with-a-gradient.
- **Use for:** AI "thinking", voice, hero moments.
- **Fails when:**
  - it loops constantly without signalling state (chrome rings insp-1-31, insp-1-36, insp-1-4);
  - text crosses its bright band: insp-7-8 drops to 2.24:1 where the gold band crosses.

### 11. Retro-pixel / dither / ASCII / dot-matrix (pixel n=17 mean 30.5; dither n=13 mean 30.0)
- **Defining parameters:**
  - Everything snaps to a single grid (≈6–16px cells).
  - Iconography is drawn on the same grid as the scene (insp-dynamic-island-pixel-art-horse).
  - Dither scale encodes depth: about 8px cells on the hero and 16px on the background (insp-1-40, insp-1-50).
  - The text panel is solid, so text never sits on dither.
- **Use for:** AI and dev brands wanting warmth without illustration, loaders (insp-1-46 tile-grid loader), LED readouts.
- **Fails when:** the grid is decorative only (insp-components-n3xt: a 12×8 = 96-dot chart misstates every percentage).

### 12. Maximalist colour / flat illustration (maximalist n=44, mean 28.6; flat-illustration n=24)
- **Defining parameters:** many saturated hues, each tied to a meaning (sport, section, city, agent); illustration in 2–3 stroke weights.
- **Best:** bg-olympic, bg-edp, bg-instacart, insp-5-4.
- **Use for:** consumer brands, events, education.
- **Fails when:** the meaning is missing (bg-duolingo guide: colours per discipline with white text at 1.8–2.6:1).

### 13. Kinetic / editorial type as image (n=14, mean 30.2)
- **Defining parameters:**
  - Type is the visual. Mega display sizes run 208–320px with line-height 0.85 and −1% tracking (bg-klarna).
  - Words morph (insp-eleven-v4: words fade by distance from the selection).
  - Text fields are built from the brand's own letters (insp-maple-research-cards).
- **Fails when:** rotated or warped text carries essential information. This was tagged as an anti-pattern 24 times.

## C. Choosing quickly

| Brief signal | Base | Expressive layer | Avoid |
|---|---|---|---|
| B2B SaaS, analytics, dev tools | minimal-swiss or dark-premium | hairline/technical **or** one shader object | glass on data |
| AI assistant / agent | dark-premium or minimal-swiss | orb/shader for state, mono metadata | constant decorative loops |
| Fintech / payments | minimal-swiss | physical material (card, receipt, stamp) | white text on brand green/blue |
| Consumer / playful | corporate-clean → playful-rounded | soft-3D or maximalist colour with meaning | pastel + white text |
| Portfolio / studio | editorial-serif or hairline | one physical metaphor or pixel scene | three expressive layers |
| Brand identity page | editorial or swiss-grid-poster | brand's own device as texture | template look |
| Mobile onboarding | minimal-swiss | soft-3D illustration or glass, one per screen | hover-only affordances |

# Brand system template

Use this to build a **brand or identity page**, or a full guideline document. It is distilled from 53 real guidelines; the best were Olympic, EDP (Pentagram), Red Hat, Instacart, Hulu and IBM. The best documents write rules as **formulas** and ship **assets beside rules**.

## Chapter order

| # | Chapter | Must contain | "Excellent" adds |
|---|---|---|---|
| 0 | Cover + contents | Linked contents, version/date | "How to use this guide" in 3 lines |
| 1 | Brand idea | Purpose, promise, 3–5 values with one-line definitions | "We are X, never Y" pairs |
| 2 | Voice & tone | 4 attributes with do/don't sentences | Mechanical rules (numbers, dates, currency, naming, banned words), a tone dial by context |
| 3 | Logo | Primary, secondary, mark-only; clearspace; min size (px **and** mm); colourways; backgrounds; misuse grid (6–9 tiles) | Construction geometry; clearspace from the mark's own anatomy (e.g. the height of its "e"); optical centring note; co-branding lockup with separator rules |
| 4 | Colour | Roles, HEX/RGB/CMYK/PMS, proportions (e.g. 60/30/10) | **Approved pairs with contrast ratios and AA/AAA badges**; an AA-safe "ink" shade per brand colour; tints ladder; web-only tints |
| 5 | Typography | Families + fallbacks, a named scale (size/leading/tracking) | Per-size tracking, localisation offsets, non-Latin scripts, numerals |
| 6 | Signature device | What it is and where it appears | Formulas (e.g. radius = shortest edge ÷ 6; ≥ 55% visible when cropped; once per spread; rotated exactly ±3°) |
| 7 | Imagery | Photo direction with examples; illustration style; icon grid and stroke | Casting/diversity rules, lighting, post-processing don'ts, an icon keyline grid |
| 8 | Layout | Grid per format and breakpoint (columns/margins/gutters) | Proportional margins (e.g. H ÷ 40) |
| 9 | Motion & sound | Duration and easing tokens, logo animation | Transition library, sonic logo. *Missing from most real guides; include it.* |
| 10 | Applications | 6–12 real artefacts (product UI, social, OOH, stationery, merch) | Templates downloadable beside each |
| 11 | Governance | Contacts, trademark/legal, downloads, changelog | Per-rule download links, click-to-copy values |

## Brand page layout (web)
- **Hero:** the mark at large scale on the brand colour, the brand idea in one sentence, and a version/date stamp.
- **Sticky chapter nav:** numbered labels ("01 Logo"). Each chapter opens with a full-bleed band in a brand colour (heights of 240–360px).
- **Each rule block** follows the same order:
  1. the rule stated as a large sentence;
  2. the spec in mono (values, ratios);
  3. visual proof;
  4. a do/don't pair (don'ts crossed with a 1.5px red diagonal);
  5. a download or copy button.
- **Swatches:** large chips with name, role, HEX/RGB/CMYK/PMS (click-to-copy), the contrast ratio against white and black, and an AA/AAA badge.
- **Type specimen:** the scale rendered live (each step's size/leading/tracking printed beside it), plus a paragraph at body size.
- **Logo section:**
  - clearspace diagram drawn with the unit shown (dashed guides);
  - the minimum-size row at the real minimum px;
  - the background matrix (full colour / mono / reversed);
  - the misuse grid.
- **Motion section:** live demos of the brand easing, respecting reduced motion.

## Formulas worth reusing
- **Clearspace** = height of a glyph or part of the mark (the "e", a cap, a symbol's bar).
- **Minimum size:** about 24px digital / 8mm print for wordmarks; about 16px / 5mm for symbols.
- **Background switching:** use the light logo on backgrounds darker than about 55% lightness.
- **Proportions:** primary colour ≥ 60%; signal colour ≤ 10%.
- **Device geometry:** radius = shortest edge ÷ 6; stroke = longest edge ÷ 100.

## Errors to avoid (all found in real guides)
- **Different hex values for the same colour on two pages.** Generate every format from one token source.
- **Approved colour pairs that fail contrast.** Compute them.
- **No minimum size and no misuse page.**
- **Lorem ipsum, pasted copy from another project, typos.**
- **A desktop-only site whose sidebar breaks on mobile.**

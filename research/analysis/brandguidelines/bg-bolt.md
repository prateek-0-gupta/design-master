---
id: bg-bolt
source: brandguidelines
category: guideline
status: analyzed
title: "Bolt"
creator: "Koto"
styles: [maximalist-color, high-contrast-bw, photo-led, corporate-clean]
patterns: [acid-accent-on-warm-neutrals, lightning-bolt-supergraphic, persistent-sidebar-nav, sanctioned-colour-pair-tiles, keyword-highlight-colour, co-brand-ratio-spacing, rounded-card-panels]
mode: mixed
palette: ["#e1ff00", "#11190c", "#787664", "#cac4b7", "#f3f1ee", "#ffffff"]
type_families: ["Agrandir Narrow (Bold, Medium) by Pangram Pangram — per doc; fonts embedded as unnamed Type 3", "Inter (Medium, Semi Bold) — per doc"]
type_class: [grotesk, condensed, neo-grotesk]
radius_px: [12, 9999]
motion: null
scores: {aesthetics: 8, originality: 7, usability: 6, craft: 6}
craft_signals: [logo-letterform-is-the-symbol, warm-tinted-black, print-fallback-order-for-neon, ratio-based-cobrand-gap, approved-colour-pair-grid, nav-sidebar-with-active-state]
anti_patterns: [hex-rgb-mismatch, tov-principles-without-explanation, missing-spaces-in-copy, divider-type-inconsistent, mid-grey-pairs-below-aa, thin-chapter-coverage]
---
# Bolt — Koto

## 1. Snapshot
- **Subject:** A 19-slide, 1920×1080 pt "Brand Guidelines / January 2024" PDF from Koto's rebrand of Bolt, the one-click checkout company. It covers tone-of-voice headlines, logo, colour and typography, and is labelled a media kit.
- **Why it's remarkable:** It is a two-colour brand pushed to its limit: acid "Lightning Yellow" #E1FF00 against a green-tinted near-black #11190C, softened by three warm greys. The wordmark's own L/T junction is the lightning bolt, so the logo carries the symbol and no separate icon is needed.

## 2. Composition & layout
- **Divider slides (p2, p4, p11, p14):** a #F2F1ED field crossed by a giant Lightning Yellow zig-zag bolt that bleeds off two or three edges and covers about 27–33% of the slide (palette.json). The chapter title (~110 px cap height on the 1400 px render, ≈150 pt) overlaps the bolt. A small logo sits top-left at 28/1400 px.
- **Content slides:** a fixed #11190C sidebar 123/1400 px wide (≈169 pt, 8.8%) holding the logo and a four-item nav (Tone of Voice / Logo / Color / Typography). The active item is in Lightning Yellow and the page number sits bottom-left. Next to it is a ~250 px text column at x≈167, and from x≈414 a demonstration area of large panels with about 8 px radius (≈12 pt) and about 20 px gutters.
- The cover (p1) is a 97.7% yellow field with the wordmark at about 312×86 px, left-centred, and a tiny 2-line date label. It is extremely confident.

## 3. Typography
- **pdffonts:** all 22 embedded fonts are Type 3 with the name `[none]`, so faces cannot be confirmed from metadata. The names below come from the document's own type pages (p15–17) and match the visible letterforms.
- **Primary:** Agrandir Narrow (Pangram Pangram), Bold for headlines and Medium for sublines. It has a high x-height, ball-ish terminals on "y" and "g", and moderate stroke contrast. The doc calls it "loud and proud hero or a humble supporting actor."
- **Secondary:** Inter. Medium is used for body, annotation and buttons; Semi Bold for highlighted key words.
- **Hierarchy (p17), measured on 1400 px:**
  - Headline: about 62 px (≈85 pt), tight leading ~1.0, slight negative tracking.
  - Subline: about 28 px (≈38 pt), leading ~1.15.
  - Body: Inter about 18 px (≈25 pt), leading ~1.3.
  - Annotation: about 15 px.
  - Button: Inter in Lightning Yellow on a Bolt Black pill about 128×44 px.
  - The headline-to-body ratio is about 3.4×.
- **Inconsistency:**
  - The "Tone of Voice" divider (p2) is set in a tight neo-grotesk (Inter-like Bold), not Agrandir, while "Color" and "Typography" use Agrandir.
  - The p7 body copy is in Agrandir Bold rather than Inter, with dropped spaces ("printapplications", "shouldnever", "sizebelow").

## 4. Colour
| Hex (doc) | Name | Role | Share on colour slides |
|---|---|---|---|
| #E1FF00 | Lightning Yellow | hero accent, logo on dark, highlight words, bolt supergraphic | 27–33% on dividers, 98% cover |
| #11190C | Bolt Black | sidebar, panels, text, logo on light | 15–57% |
| #787664 | Dark Grey | panel background, secondary fields | 3–28% |
| #CAC4B7 | Mid Grey | light fields, photo backdrops | 9–16% |
| #F3F1EE | Light Grey | default canvas, text on dark | 28–70% |

- p12 gives HEX, RGB, CMYK and Pantone for each (Lightning Yellow = 809 U, Bolt Black = 419 C, Dark Grey = 403 CP, Mid Grey = P 178-1 U, Light Grey = P 134-9 U).
- The print fallback order for the neon is a strong touch: Safety Yellow 13-0630 TN first, then 809 U/C, then CMYK 16/0/100/0 as a last resort.
- **Spec errors:** Lightning Yellow's RGB is listed as 230/255/0, which is #E6FF00, not #E1FF00. Dark Grey's RGB 124/122/106 is #7C7A6A, not #787664. palette.json measures #e1ff01 and #787765, so the hex values are the truth.

WCAG (contrast.py):
- #11190C on #E1FF00: **15.84:1**. #E1FF00 on #11190C: 15.84:1. #F3F1EE on #11190C: **15.95:1**.
- #11190C on #CAC4B7: 10.35:1.
- **Weak pairs the doc approves on p18:**
  - #F3F1EE on Dark Grey #787664: **4.07:1**.
  - #E1FF00 on #787664: **4.05:1**.
  - Dark Grey text on yellow: **4.05:1**.

  All three are large-text only. The p19 highlight example uses the #787664 background at headline size, which is acceptable.
- Yellow on Light Grey is **1.01:1**. It is invisible as text and works only as the bolt supergraphic.

## 5. Depth & material
The system is flat. The only depth is in photography: low-angle billboard, phone in hand, tote bag under hard sunlight. Panels use about 8–12 px radius with no shadows. "Don't make it 3D" and "Don't add gradients" are explicit logo rules.

## 6. Components & patterns
- **Wordmark:** custom heavy all-caps "BOLT". The L's foot and the T's left arm are cut on a shared diagonal so the negative space between them forms a lightning bolt. There is no separate symbol, and adding one is a listed misuse ("⚡BOLT").
- **Logo colour (p6):** black on yellow, light grey on dark, black on light, and yellow or light grey on photos. It is never in the secondary greys.
- **Logo usage (p8):** primary use as a huge billboard element, or secondary as a small sign-off under a headline. Logo and adjacent elements should not "feel exactly the same" in weight.
- **Highlight (p19):** one or two keywords in a sentence switch to Lightning Yellow ("one-click.", "(half)") on a Dark Grey or Bolt Black panel.
- **Application collage (p13):** sunglasses portrait, a billboard ("Shockingly simple checkout."), phone splash, a black tote with a yellow bolt, a dashboard UI ("Put the 'dash' in dashboard.") and a flat illustration of a hand making an OK sign with sparkles in grey/yellow. The collage is the only evidence of imagery and illustration style, and it has no written rules.

## 7. Motion
n/a. This is a static PDF with no motion guidance. The bolt supergraphic suggests fast diagonal wipes, but the doc says nothing.

## 8. Brand system
**Logo rules**
- **Clearspace (p7):** 1x on every side, where x is the wordmark's cap height. A 3×3 construction grid shows equal cells.
- **Minimum size:** 30 pt wide (labelled "30pt"). No px value is given for screens.
- **Co-branding (p9):** gap = **0.28x, where x is the width of the BOLT wordmark**, with a "×" glyph centred in the gap. The partner logo must not exceed the wordmark's height except for small overhangs, with optical alignment to the wordmark rather than outer bounds (the text names Fanatics' flag as the example, but Fanatics is not pictured). Shown with Stripe, Klarna and Revolve.
- **Misuse (p10, 8 tiles):** rotation (uncaptioned), gradients, 3D, stretch, added bolt icon (uncaptioned), filling the bolt counter, multiple colours, stroke. The slide is headed "Our logo is our most sacred asset. Please treat it with the utmost respect. Thank you." That line is itself a voice sample.

**Voice and tone (p3):** three principles: "Thoughtfully concise", "Knowingly playful", "Comfortably at ease". There are no definitions, do/don't pairs or example copy. The voice is learned only from sample lines elsewhere: "Shockingly simple.", "The quickest, safest effortless-est way to pay", "Checkout in (half) the blink of an eye.", "Put the 'dash' in dashboard." These are punny, comparative, short.

**Imagery:** there is no chapter. From p13 the signature is real people and objects with a single Lightning Yellow prop (sunglasses, tote lining) against warm neutral grounds. That colour-prop casting is very stealable but undocumented.

**Document structure (19 pp.)**

| # | Chapter | Pages |
|---|---|---|
| 0 | Cover | 1 |
| 1 | Tone of Voice: divider, ToV principles | 2–3 |
| 2 | Logo: divider, our logo, logo colour, clearspace + min size, logo usage, co-branding, misuse | 4–10 |
| 3 | Color: divider, primary colours, application collage | 11–13 |
| 4 | Typography: divider, primary type, secondary type, type hierarchy, type colour use cases, highlights | 14–19 |

**Token decisions worth stealing**
- A tinted black (#11190C, a green cast that harmonises with the yellow) instead of #000.
- One neon plus three warm greys. The neon is never a text colour on light grounds.
- A print fallback ladder for a fluorescent colour.
- A co-brand gap defined as a ratio of logo width (0.28x).
- Approved fg/bg pairs presented as headline tiles (p18): 8 combos, which a designer can copy directly.

## 9. UX
- The sidebar nav with an active state makes the PDF feel like a site and keeps orientation across 19 slides.
- Each slide has one job, with a short rationale on the left and a demo on the right.
- **Gaps:** voice principles with no explanation, no imagery/illustration/iconography rules despite showing all three, no grid or layout system, no digital min size, and spec errors in the RGB values.
- A designer could make a convincing poster from this. A product team would be short of guidance.

## 10. Craft signals
- The sidebar is exactly 123/1400 px on every content slide, and the active nav item changes to #E1FF00.
- Panels share one radius (about 8 px at 1400 px ≈ 12 pt) and one gutter (about 20 px).
- The supergraphic bolt repeats the angle of the wordmark's L/T cut.
- The CTA button is a full pill (9999 radius) in black with yellow label; it is the only pill shape in the doc.
- The colour spec lists four systems plus a recommended print order.
- Errors: two RGB/HEX mismatches; missing spaces on p7; the Tone of Voice divider uses a different headline face.

## 11. Reproduction recipe
```css
:root{
  --bolt-yellow:#e1ff00;  /* Lightning Yellow, Pantone 809 U */
  --bolt-black:#11190c;   /* Pantone 419 C */
  --bolt-grey-dark:#787664;
  --bolt-grey-mid:#cac4b7;
  --bolt-grey-light:#f3f1ee;
  --font-head:"Agrandir Narrow","Arial Narrow",sans-serif;
  --font-body:"Inter",system-ui,sans-serif;
  --r-panel:12px; --r-pill:9999px; --gutter:20px;
}
body{background:var(--bolt-grey-light);color:var(--bolt-black);font:500 18px/1.35 var(--font-body);}
.h1{font:700 clamp(48px,6vw,85px)/1 var(--font-head);letter-spacing:-.01em;}
.subline{font:500 clamp(24px,2.6vw,38px)/1.15 var(--font-head);}
.panel{border-radius:var(--r-panel);padding:48px;background:var(--bolt-black);color:var(--bolt-grey-light);}
.panel mark{background:none;color:var(--bolt-yellow);}   /* highlight words */
.btn{border-radius:var(--r-pill);background:var(--bolt-black);color:var(--bolt-yellow);
     font:600 15px/1 var(--font-body);padding:15px 36px;}
.sidebar{width:8.8vw;background:var(--bolt-black);color:var(--bolt-grey-light);}
.sidebar a[aria-current]{color:var(--bolt-yellow);}
.divider{background:var(--bolt-grey-light) url(bolt-zigzag.svg) no-repeat right/70%;}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Fearless neon/near-black contrast with warm greys; the bolt supergraphic and collage look art-directed. |
| Originality | 7 | A bolt built from the L/T junction and the neon-on-warm-neutral palette are fresh for fintech, though acid green-yellow is a 2023–24 trend. |
| Usability | 6 | Good colour-pair, hierarchy and co-brand specs; voice, imagery and layout are only implied. |
| Craft | 6 | Consistent sidebar chrome and radii, but HEX/RGB mismatches, mixed divider type and copy typos. |

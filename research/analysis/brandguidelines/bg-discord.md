---
id: bg-discord
source: brandguidelines
category: guideline
status: analyzed
title: "Discord Brand Guidelines v1.0"
creator: "In-house"
styles: [maximalist-color, playful-rounded, kinetic-type, cinematic-3d]
patterns: [split-slide-white-rail-dark-stage, squircle-colour-swatches, layered-swatch-pairings, imagine-a-place-headline-system, community-dot-pattern, ui-chrome-in-marketing, comma-baseline-tweak, mascot-expression-set]
mode: mixed
palette: ["#5865f2", "#23272a", "#ffffff", "#57f287", "#fee75c", "#eb459e", "#ed4245"]
type_families: ["Ginto Nord (Ultra / Black / Medium)", "Whitney (Book, Semibold)"]
type_class: [display, geometric-sans, humanist-sans]
radius_px: [44, 22, 9999]
motion: null
scores: {aesthetics: 8, originality: 8, usability: 7, craft: 6}
craft_signals: [clear-space-from-rotated-o, line-height-by-copy-length, manual-comma-baseline-shift, paired-do-dont-quadrants, ui-status-colour-mapping, fallback-fonts-named]
anti_patterns: [suggested-pairs-fail-contrast, chapter-label-typos, typeface-role-contradiction-p42, fonts-converted-to-type3-not-searchable]
---
# Discord Brand Guidelines v1.0 — In-house

## 1. Snapshot
- **Subject:** A 74-page, 16:10 (1440×900 pt) deck labelled "Version 1.0" (source filename "…Brand-Guideline-May-14"), for the "Imagine a Place" identity. It covers intro and voice, logo/Clyde/wordmark/tagline, colour, typography and "brand in use".
- **Why it's remarkable:** The deck itself is the brand at full volume. Wall-to-wall Blurple, Ginto Nord Ultra set at ~80% leading, squircle swatches stacked to teach pairings, and 3-D character illustration. It sits on top of unusually concrete micro-rules: clear space built from the wordmark's rotated "o", leading tied to copy length, and manually raised commas.

## 2. Composition & layout
There are two templates.
- **Chapter and statement slides** are full-bleed single colour: Blurple `#5865f2` (84% of p1 per palette.json), Yellow (78% of p7), Fuchsia (74% of p8), Green (89% of p9). Each carries centred or bottom-left Ginto Nord Ultra headlines in all caps. On p1 "BRAND GUIDELINES" spans ~430/480 thumbnail px wide, about 90% of the slide.
- **Rule slides** split the slide at x≈530/1400 (38%). A ~48 px Blurple vertical rail sits at the far left with a rotated "Discord Brand Guidelines" folio. A white text column holds an overline ("04 TYPOGRAPHY", ~13 px caps), a 2–4 line title in Ginto Nord Black (~30 px cap height, with "USAGE" in Blurple above black for usage pages) and Whitney body at ~14 px / 135%. The right 62% is a near-black `#23272a` stage, often divided into 2×2 quadrants by 1 px grey hairlines. Each quadrant has a numbered ring, green for correct and red for incorrect, and wrong examples get a red diagonal slash (pp25, 31, 38, 45, 51).

Download links are pill buttons (`#f0f1f5`-ish fill, Blurple underlined label, download glyph) anchored bottom-left of the white column.

## 3. Typography
pdffonts reports only unnamed Type 3 fonts ("[none]"), meaning text was converted on export. The typefaces below are therefore taken from the document's own type pages (pp41–42), and the specimens match visually.
- **Ginto Nord** (Dinamo) is the primary face, described as "geometric-humanist" with tension between circular and rectangular forms. Headlines are always uppercase. The roles are Ultra Headline (Ultra, e.g. 90 pt, 80% leading short / 95% longer copy, 0 tracking), Primary Headline (Black, e.g. 50 pt, 90% short / 110% longer) and Secondary Headline (24 pt, 90%).
- **Whitney** (Book, Book Italic, Semibold, Semibold Italic) is used for paragraphs at e.g. 15 pt / 130% (p42) and "always" 135% line height on p45, a 5-point internal discrepancy. Measure is 50–75 characters, about 11 words (p45).
- **Fallbacks are named:** Poppins Black (all caps) for Ginto Nord, and Roboto for Whitney (p41).
- **Contradiction:** p42's text says Secondary Headline = Whitney, but the specimen beside it is labelled and set as "GINTO NORD MEDIUM — Secondary Headline".
- **Optical detail (p47):** in tightly leaded Ultra headlines, commas must be manually nudged up off the baseline so they do not collide with the cap below. Green/red magnifier circles show the before and after.
- 3-D type (p52) is reserved for special occasions (Art Basel, Pride, Steep Day, Dog Day): extruded, furry or inflated lettering.

## 4. Colour
From pp27–28 (the document's values). Palette.json confirms `#5865f2`, `#23272a`, `#ed4245`, `#ed459f`/`#ec459f` and `#fee75d` in the renders.

| hex | role | approx share |
|---|---|---|
| #5865f2 | Blurple, core brand (PMS 2726 C), chapter grounds, rail | ~40% across deck |
| #23272a | "Black" (PMS 426 C), rule-slide stages, UI | ~35% |
| #ffffff | White, text column, type on colour | ~15% |
| #57f287 | Green (PMS 3385 C), online status, statement slides | accent |
| #fee75c | Yellow (PMS 102 C), user-content colour, idle status | accent |
| #eb459e | Fuchsia (Rhodamine Red), user-content colour | accent |
| #ed4245 | Red (PMS 032 C), DND / LIVE / end-call | UI-only accent |

The p28 rationale is that Blurple, green and red come from the product UI, while yellow and fuchsia "represent the colorful content from the users".

WCAG (contrast.py) on the deck's own *suggested* pairings (p30):
- White on Blurple: 4.61:1, AA pass.
- `#23272a` on Blurple ("Blurple + Black"): **3.27:1**, large text only.
- Blurple on Yellow: 3.69:1, large only.
- White on Fuchsia: **3.57:1**, large only.
- **Fuchsia + Yellow: 2.86:1, fails even AA-large**, though it is listed as a suggested pairing.
- White on Red: 3.84:1, large only.
- `#23272a` on Green: 10.36:1. White on `#23272a`: 15.05:1.

The forbidden pairs (p31) are rightly forbidden: Green on Yellow 1.16:1, Fuchsia on Blurple 1.29:1. In practice the system depends on huge headline sizes to pass, and body copy must be white or black on Blurple or Black only.

## 5. Depth & material
The layouts are flat, and depth comes from content. Glossy 3-D characters (Clyde-ish creatures, a balloon dog, a gingerbread man) are rendered with soft studio lighting. Phone mockups sit on `#23272a` with soft drop shadows (p55). The p36 server-channel spec adds "25% opacity Black with Multiply" circles above and below, and reaction chips use white at 25% or 60% transparency over colour. Swatches are squircles at ~28% radius (~44 px on a 160 px tile at 1400 px render). UI cards use ~22 px radii, and download buttons are full pills.

## 6. Components & patterns
- **Layered squircle pairings (pp29–33):** two overlapping rounded squares teach "background + text" pairs. Three-layer stacks teach "background / text / decorative" schemes, and the order matters.
- **Community Pattern (p39):** a polka-dot field (yellow dots on fuchsia) where some dots become user avatars. It must be white when behind content, may take one scheme colour when standalone, and must never mix colours outside the scheme.
- **Headline card system:** "IMAGINE A PLACE…" brand lines and "@user#0000" community quotes, framed by a dotted ticker border ("IMAGINE A PLACE ·:·:·:") top and bottom (p35, p61), with reaction-count chips beneath.
- **UI-fidelity rules (pp35–36):** online = green, DND = red, idle = yellow, invisible = black. Server lists stay white or black. Call buttons use white icons on black or red and can never be inverted.
- **Clyde expressions (p17):** a 4×5 grid of the mascot with only the eyes changed.

## 7. Motion
No timings are given. The deck references motion only as rules. Taglines are placed "center of the canvas" for animated or masked compositions (p20). Text must not be frozen on motion frames: in intros and outros it must land "aligned in the centre… free of distortions" (p51). End cards are specified (p67), and 3-D type animations are for special occasions (p52).

## 8. Brand system
**Logo rules.** The logo is the Clyde icon plus the custom "Discord" wordmark. The clear-space unit is unusually literal (p15): take the wordmark's letter "o", rotate it 90°, and duplicate it, so **x = two rotated o's**. That is applied on all sides, with x/2 between icon and wordmark. The Small Discord Logo (optimised kerning) is used below **80×15 px (60×11.25 pt)** (p14). Preferred order for Clyde alone (p16): white on Blurple, then Blurple on white, then white on black, then black on white, and the same for the wordmark (p18). Tagline "Imagine a Place" lock-ups exist in vertical and horizontal versions, with the tagline sized to the wordmark x-height (p21). Partner lock-ups are separated by a 1 px white stroke with x spacing (p22). Approved colour combinations are on p23, and don'ts on p25: no off-palette colours, no glows/shadows/gradients, no rotation, no restacking.

**Voice & tone.** Mission: "Create space for everyone to find belonging." Vision: "An inclusive world where no one feels like an outsider." Positioning: "Playfully purposeful." The narrative is "Imagine a Place", with *Belonging* as protagonist and *Isolation* as antagonist (p10). There are four values: Playful, Original, Relatable, Reliable (p11). Messaging comes in three tiers (p12): "That Discord feeling", "Community belonging" and "Product value". There are two copy sources: brand lines written by Discord, and user quotes collected from community events. The writing itself is self-aware ("OMG IT'S SENTIENT! Not quite…").

**Imagery.** Imagery is commissioned 3-D character illustration, not photography. p34 shows how to pick a colour scheme from an illustration. Use a colour that is *not* the illustration's dominant hue for the background (e.g. a fuchsia-heavy illustration goes on yellow or Blurple). Let illustration elements break the frame.

**Document structure (74 pp):**
1. Cover, p1. Welcome, p2. Index, p3.
2. 01 Introduction, pp4–12: what is Discord, mission, vision, positioning, tone of voice, messaging variations.
3. 02 Logo, Symbol, Wordmark & Tagline, pp13–25: logo, clear space, Clyde, expressions, wordmark, placement, partners, colour combos, do/don't.
4. 03 Brand Colors, pp26–39: Blurple, palette, applying, pairings, schemes, UI colours, usage, community pattern.
5. 04 Typography, pp40–52: typefaces, typestyles, line heights, lockups, comma tweak, user quotes, placement, usage, 3-D type.
6. 05 Brand in Use, pp53–71: brand lines, community lines, user quotes, chat and audio dialog, end cards, stationery and merch.
7. Asset Library, p72. Questions, p73. End logo, p74.

**Token decisions worth stealing.** Leading as a function of copy length (80% → 95% for Ultra, 90% → 110% for Black). Colour roles split by origin (product colours vs "user content" colours). Teaching colour as stacked layer pairs instead of a swatch grid. A clear-space unit derived from a glyph in the wordmark.

## 9. UX
It is highly scannable. Every rule slide uses the same white-rail/dark-stage split, the green/red numbered rings, and a download pill for the relevant asset. The index has page numbers for 38 sub-topics. The gaps: no minimum size for Clyde alone and no print-size table. Body text in the white column is small (~14 px on a 1440 pt slide). Contrast guidance is purely visual, never numeric, which is how Fuchsia + Yellow (2.86:1) was approved.

## 10. Craft signals
- Clear space x = two 90°-rotated "o" glyphs, with x/2 between icon and wordmark (p15).
- The small-logo threshold is stated in px and pt: 80×15 px = 60×11.25 pt (p14).
- Every type style is captioned with size / leading / tracking (p42: "90pt / 80% / 0%").
- Comma baseline correction is shown in magnified callouts (p47).
- UI status colours map 1:1 to the palette (p35).
- Flaws: p15 numbers the steps "Step 1, Step 2, Step 2". p30's overline reads "04 BRAND COLORS" inside chapter 03. A p44 example begins "OREM IPSUM". All text is outlined Type 3 fonts.

## 11. Reproduction recipe
```css
:root{
  --blurple:#5865f2; --ink:#23272a; --white:#fff;
  --green:#57f287; --yellow:#fee75c; --fuchsia:#eb459e; --red:#ed4245;
  --font-display:"Ginto Nord","Poppins",system-ui,sans-serif;   /* fallback per p41 */
  --font-text:"Whitney","Roboto",system-ui,sans-serif;
  --r-swatch:28%; --r-card:22px;
}
.ultra{font:900 90pt/0.8 var(--font-display);text-transform:uppercase;letter-spacing:0}
.ultra--long{line-height:.95}
.primary{font:800 50pt/.9 var(--font-display);text-transform:uppercase}
.primary--long{line-height:1.1}
.body{font:400 15pt/1.35 var(--font-text);max-width:66ch}
.comma-lift{position:relative;top:-.12em}   /* manual comma tweak, p47 */
.rule-slide{display:grid;grid-template-columns:48px 34fr 62fr;min-height:100vh}
.rule-slide__rail{background:var(--blurple)}
.rule-slide__stage{background:var(--ink);display:grid;grid-template:1fr 1fr/1fr 1fr;gap:1px}
.pair{position:relative;width:160px;aspect-ratio:1}
.pair>i{position:absolute;inset:0;border-radius:var(--r-swatch)}
.pair>i:last-child{transform:translate(30px,-30px)}
.community-pattern{background:radial-gradient(circle,var(--yellow) 38%,transparent 40%) 0 0/56px 56px,var(--fuchsia)}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Loud and consistent: full-bleed colour, monumental Ginto Nord Ultra and rich 3-D illustration, all held together by a disciplined split template. |
| Originality | 8 | Stacked-squircle colour teaching, the community dot pattern with avatars, and the rotated-"o" clear space are fresh. The voice is genuinely distinctive. |
| Usability | 7 | Concrete leading and UI-colour rules and downloads everywhere, but no numeric contrast guidance, missing icon minimum sizes, and a typeface-role contradiction. |
| Craft | 6 | Strong micro-typography (comma lift) undermined by typos in step numbers and chapter labels, outlined fonts, and suggested pairs that fail WCAG. |

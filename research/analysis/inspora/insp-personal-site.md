---
id: insp-personal-site
source: inspora
category: Web
status: analyzed
title: "personal site"
creator: "Sam Cheng (@samfcheng)"
styles: [editorial-serif, minimal-swiss, physical-material, micro-interaction]
patterns: [draggable-physics-badge, edge-to-edge-name-wordmark, corner-microcopy-pair, lanyard-rope-simulation, pill-employer-tags, badge-occludes-wordmark]
mode: light
palette: ["#ffffff", "#050505", "#1f2bea", "#ededed", "#95949e", "#d6324a", "#4b1fb0"]
type_families: ["Ionic/Clarendon-style serif, close to Larken or GT Super Display (likely)", "same serif, italic for labels"]
type_class: [editorial-serif, slab]
radius_px: [9999, 12]
motion: {durations_s: [4.4, 0.4, 8.1, 1.03], easing: [ease-in-out, ease-out], loop: true}
scores: {aesthetics: 8, originality: 7, usability: 7, craft: 8}
craft_signals: [badge-shadow-separated-from-object, wordmark-bleeds-both-edges, two-tone-name-on-badge, translucent-sleeve-rim, chromatic-employer-tags, bracketed-more-link]
anti_patterns: [grey-more-link-low-contrast, badge-covers-headline]
---
# personal site — Sam Cheng

## 1. Snapshot
- **Subject:** An 18 s, 2920×2026 capture of a personal landing page. A plastic-sleeve conference ID badge on a black lanyard swings and can be dragged over a white page, above an edge-to-edge serif "Sam Cheng".
- **Why it's remarkable:** The whole bio sits on a physical object you can grab. The badge carries the details (Currently / Previously plus employer pills) and the page keeps only the name and two sentences. This is a popular three.js/Rapier rope pattern, styled with editorial restraint.

## 2. Composition & layout
Key frame px are source px ×1.46.
- **Three bands:**
  - Two corner microcopy blocks at y≈150–190, one left-aligned at x≈160 and one right-aligned to x≈1848. These are mirrored 160 px margins.
  - A vast white middle.
  - The giant name with baseline at y≈1280, cap height about 290 px. It is set to the full viewport width so the "S" and "g" touch or crop both edges.
- **Badge:** about 470×650 px, hanging from the top edge on a rope roughly 30 px thick. Its rest position at 9.00 s is centred around x≈1030 (sheet), overlapping the "Ch" of the wordmark.
- **Hierarchy:** The page is almost entirely white (85%), so all attention splits between the badge (motion) and the wordmark (scale).

## 3. Typography
- **Typeface:** A wide, soft-bracketed Clarendon/Ionic serif with ball terminals and a heavy "g" ear. It is closest to Larken or GT Super Display.
- **Wordmark:** about 400 px font-size in a weight around 500, with tight tracking of about −0.02 em.
- **Microcopy:** the same family at about 22 px with 1.25 leading. The "[more]" link is bracketed, grey, and underlined.
- **Badge:**
  - The name is stacked: "Sam" in black at about 90 px and "Cheng" in electric blue (#1f2bea) beneath. The lines overlap slightly, so "Cheng"'s cap touches "Sam"'s baseline. The face is printed with a slight ink-bleed texture.
  - The labels "Currently" and "Previously" are 14 px italic.
  - Values are 14 px roman grey.
- Everything is one serif family, so the identity is purely typographic.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #ffffff | page | 85% |
| #050505 | wordmark, copy, lanyard | 4% |
| #ededed / #e2e2e3 / #d7d7d8 | badge sleeve, shadow | 5% |
| #1f2bea | "Cheng" accent | <1% |
| #95949e | "[more]" link, secondary | 1.5% |
| #d6324a / #4b1fb0 / #111 | employer pills (Oracle, Multiply, KP Fellows) | <1% |

WCAG checks:
- Black on white is 20.38:1.
- Blue on the badge card (#f4f4f4) is 7.37:1.
- The "[more]" grey is **3.0:1**, so it fails for 22 px regular text.
- White on the Oracle red pill is 4.76:1 and on the Multiply violet pill 9.9:1.

## 5. Depth & material
- **Badge:** a clear PVC sleeve with a 1 px light-grey rim, two punched holes, a slot, a translucent inner insert, and a metal swivel clip with highlights.
- **Shadow:** offset about 60 px down-right and blurred about 30 px. It detaches from the badge and grows as the badge swings toward the viewer (11.00 s), which implies a light source above-left and z-distance.
- **Lanyard:** casts its own soft grey shadow on the page.
- **The rest:** totally flat. Depth exists only on the interactive object.

## 6. Components & patterns
- A draggable rope-physics badge with a grab-hand cursor on hover (key frame).
- An edge-bleeding name wordmark that serves as both logo and footer.
- A corner microcopy pair: a "what I do" statement and a "where I am" status.
- Pill tags for past affiliations, each in the employer's brand colour, about 30 px tall with fully rounded ends.
- A bracketed inline "[more]" link expanding the bio.

## 7. Motion
Measured: 18.0 s at 60 fps, motion_fraction 0.76, `seamless_loop_likely: true`, 4 segments with a median of 2.72 s.
- **1.1–5.5 s (4.4 s, symmetric ease-in-out):** a drag-and-swing arc up to the top right, with the badge rotated about −35°.
- **5.9–6.3 s (0.4 s, ease-in, peak 0.71):** the user flick, an acceleration at release.
- **6.43–14.53 s (8.1 s, ease-out, peak 0.24):** a long damped pendulum decay after release. The badge rotates about ±70° (7.00 s and 11.00 s), then settles near vertical by about 15 s.
- **15.27–16.3 s (1.03 s):** the final small sway.

The physics feel slightly underdamped: an 8 s decay is generous and playful, but it would distract on a reading page.

## 8. Brand system
n/a — not a brand system. It is a personal identity:
- the serif name in two forms, a giant black wordmark and a stacked black/blue lockup on the badge;
- electric blue #1f2bea as the single personal accent;
- the "badge" metaphor (student, fellow, conference) as the personality.

## 9. UX
- **Strengths:** Immediate playfulness, and the essential bio is visible without interaction. The grab cursor signals that the badge is draggable.
- **Risks:**
  - When the badge rests it covers "Ch" of the main name.
  - The badge text rotates and is only about 14 px, so its content is hard to read while moving.
  - The "[more]" link fails contrast.
  - Long decay without a reduced-motion option.

## 10. Critical craft signals
- The badge name's lockup has "Cheng" in blue overlapping "Sam" with a negative line gap, not just a colour change.
- The wordmark is sized so both outer glyphs meet the viewport edges exactly (an intentional bleed).
- The corner blocks mirror each other: the left is ragged-right at x=160 and the right is ragged-left ending at x=1848, with equal margins.
- The drop shadow is a separate layer offset from the badge, scaling with rotation (11.00 s).
- The employer pills use brand colours with white text, all of which pass AA.
- The plastic sleeve has a visible 1 px inner rim and punched holes, which signals real-object reference.

## 11. Reproduction recipe
```css
:root{--paper:#fff;--ink:#050505;--accent:#1f2bea;--muted:#95949e;
  --serif:"Larken","GT Super Display","Georgia",serif}
body{background:var(--paper);color:var(--ink);font:400 22px/1.25 var(--serif)}
.corner{position:absolute;top:100px;max-width:20ch} .corner.l{left:110px} .corner.r{right:110px;text-align:right}
.corner a{color:#6b6a73;text-decoration:underline;text-underline-offset:3px} /* raise from #95949e to pass AA */
.wordmark{position:fixed;bottom:-.08em;left:0;width:100vw;font:500 clamp(120px,20.5vw,420px)/1 var(--serif);
  letter-spacing:-.02em;white-space:nowrap;text-align:center}
.badge{width:320px;aspect-ratio:.72;border-radius:12px;background:#f4f4f4;
  box-shadow:inset 0 0 0 1px #d7d7d8,40px 50px 40px -10px rgb(0 0 0/.12)}
.badge .name{font:500 62px/.82 var(--serif);letter-spacing:-.03em}.badge .name span{color:var(--accent);display:block}
.pill{border-radius:9999px;padding:2px 8px;font:500 12px var(--serif);color:#fff}
```
Physics: a Verlet rope of about 12 segments plus a rigid-body card (three.js + Rapier). Use angular damping of about 0.6 to settle in about 4 s instead of 8 s.

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | A single serif, a single accent, a lot of white and a tactile badge: confident and personal. |
| Originality | 7 | The lanyard-badge is a known WebGL trend. The editorial serif treatment and two-tone lockup freshen it. |
| Usability | 7 | The core bio is static and readable. Badge content is hard to read in motion and it occludes the name. |
| Craft | 8 | Sleeve detail, separated shadow and edge-fit wordmark. The grey link contrast slips. |

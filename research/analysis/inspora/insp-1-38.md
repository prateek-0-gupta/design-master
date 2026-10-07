---
id: insp-1-38
source: inspora
category: Motion
status: analyzed
title: "Sidebar sub menu"
creator: "@ThatsPranav"
styles: [minimal-swiss, hairline-ui, micro-interaction]
patterns: [accordion-nav, tree-connector-lines, active-indicator-bar, per-section-accent-color, hover-highlight-branch, icon-colorize-on-hover]
mode: light
palette: ["#fefefe", "#111111", "#5e5e5e", "#a0a0a3", "#e7691d", "#2c5de0", "#7c25ee", "#dddddd"]
type_families: ["Inter (likely)"]
type_class: [neo-grotesk]
radius_px: [18]
motion: {durations_s: [0.23, 0.23, 0.2], easing: [ease-in, ease-out], loop: true}
scores: {aesthetics: 8, originality: 7, usability: 7, craft: 8}
craft_signals: [connector-colors-only-up-to-hovered-item, elbow-radius-on-tree-lines, accent-per-section, rail-indicator-matches-section-accent, weight-shift-on-hover, single-open-accordion]
anti_patterns: [inactive-parents-below-aa, orange-accent-low-contrast]
---
# Sidebar sub menu — @ThatsPranav

## 1. Snapshot
- **Subject:** A 3620×2160, 10.3 s, 60 fps capture of a docs-style sidebar with three sections: "Transactional Email", "Email Analytics" and "AI Email Templates". Only one section is expanded at a time. Each child item hangs off an L-shaped tree connector that colours in up to the hovered child.
- **Why it's remarkable:** Each section owns an accent: orange #e7691d, blue #2c5de0, violet #7c25ee. The rail marker, the branch line and the hovered icon all adopt it, so a plain text list gains wayfinding colour without any filled backgrounds.

## 2. Composition & layout
- **Layout:** One centred column on near-white. A full-height 2 px vertical rail (#dddddd) sits at x≈1142 real px (key scale 1.81). Parents are indented ≈172 px from the rail.
- **Rhythm:**
  - parent rows ≈217 px apart;
  - children ≈179 px apart, indented a further ≈240 px with a ≈70 px icon column before the label.
- **Tree connector:** a vertical stem drops from below the parent label at the children's left edge. Each child gets a horizontal tick (≈80 px) with a rounded elbow (radius ≈36 px real) on the last segment.
- **Active marker:** a ≈6×100 px bar on the rail, aligned with the open parent.

## 3. Typography
- **Typeface:** Inter-like neo-grotesk throughout.
- **Parents:** ≈90 px real font size. Medium #111 when open; Regular grey (#a0a0a3) when closed.
- **Children:** ≈69 px real (ratio ≈1.3 to parents), Regular #5e5e5e. The hovered child switches to **Semibold #111**. The weight change is the hover signal, reinforced by colour on the icon.
- Labels are sentence or title case with no truncation. Ampersands appear in labels ("Engagement & clicks").

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #fefefe | background | 96.6% |
| #dddddd | rail, idle connectors | 0.4% |
| #a0a0a3 | closed parents | ~1% |
| #5e5e5e | child labels, idle icons | ~0.5% |
| #111111 | open parent, hovered child | <0.5% |
| #e7691d | Transactional accent (orange) | <0.1% |
| #2c5de0 | Analytics accent (blue) | <0.1% |
| #7c25ee | AI Templates accent (violet) | <0.1% |

(Accent hexes were sampled from frame pixels; the median-cut palette drops them below its share floor.)

WCAG checks:
- Open parent #111: **18.72:1**.
- Children #5e5e5e: 6.43:1.
- **Closed parents #a0a0a3: 2.59:1, a failure.**
- Accents as glyph and line colours: blue 5.55:1 and violet 6.2:1. **Orange is 3.24:1**, enough for graphics but weak if used for text.

## 5. Depth & material
- Fully flat: no shadows, fills or cards.
- Hierarchy comes from value (grey → black), weight, and 2 px hairlines.
- The only "material" is the soft cursor shadow of the screen recorder.

## 6. Components & patterns
- **Accordion navigation:** one section is open and the others collapse.
- **Tree connectors:** they show parent→child ownership and act as a progress-like "path" to the hovered item. The stem is coloured from the parent down to the hovered child, while ticks for children below stay grey (see 0.57 s: "React Email supported" is coloured, "Webhooks" is grey).
- **Icons:** each child has an outline icon (≈40 px real) that takes the accent on hover.
- **Rail indicator:** the active-section bar on the outer rail takes the section's accent.

## 7. Motion
- **Measured:** 10.28 s at 60 fps. motion_fraction 0.07. Three short segments:
  - 2.47–2.70 s (**0.23 s**, peak 0.79, ease-in);
  - 5.93–6.17 s (**0.23 s**, ease-in);
  - 9.90–10.10 s (**0.20 s**, peak 0.25, ease-out).
- seamless_loop_likely **true**.
- **Interpretation:** the two 0.23 s segments are the accordion switches (Transactional → Analytics at ≈2.5 s, Analytics → AI at ≈6 s). Children of the old section collapse while the new set expands, the parent list re-flows, and the rail indicator jumps to the new parent. The last segment is the loop reset.
- **Hover changes** (connector colour, weight, icon colour) are below the motion threshold. They read as instant to ≈100 ms tweens in the frames.

## 8. Brand system
n/a — not a brand system. A product-area colour-coding system (orange = sending, blue = analytics, violet = AI) is the identity cue and is reusable as tokens.

## 9. UX
- **Strengths:**
  - Strong information scent.
  - The open section is obvious by weight, colour and rail bar.
  - Hover feedback is triple-coded (weight, icon colour, connector), so it survives colour-blindness.
  - A single open section keeps the list short.
- **Risks:**
  - Closed section titles at 2.59:1 are hard to read.
  - The orange accent is the weakest.
  - Hover-only states need a matching keyboard focus style.
  - Auto-collapsing the previous section can disorient users who want to compare sections.

## 10. Craft signals
- The connector stem is coloured only down to the hovered child; ticks below it remain #dddddd.
- The last tree elbow has a rounded corner (≈36 px real) rather than a hard L.
- The rail indicator bar, the branch line and the hovered icon all share one section accent.
- Hover is signalled by Regular→Semibold weight plus icon colour, with no background chip.
- The vertical rhythm is consistent: parents ≈217 px apart, children ≈179 px.
- Only one section is open at any time.

## 11. Reproduction recipe
```css
:root{--rail:#ddd;--ink:#111;--ink-2:#5e5e5e;--ink-3:#a0a0a3;
  --acc-send:#e7691d;--acc-analytics:#2c5de0;--acc-ai:#7c25ee;--font:"Inter",system-ui}
.nav{border-left:1px solid var(--rail);padding-left:48px;font-family:var(--font)}
.section>button{font:400 25px/1.2 var(--font);color:var(--ink-3);position:relative;padding:14px 0}
.section[open]>button{color:var(--ink);font-weight:500}
.section[open]>button::before{content:"";position:absolute;left:-49px;top:50%;translate:0 -50%;
  width:2px;height:28px;background:var(--acc)}
.children{display:grid;grid-template-rows:0fr;transition:grid-template-rows .23s cubic-bezier(.4,0,.2,1)}
.section[open] .children{grid-template-rows:1fr}
.child{position:relative;padding:12px 0 12px 64px;font:400 19px/1 var(--font);color:var(--ink-2)}
.child::before{content:"";position:absolute;left:0;top:0;bottom:50%;width:22px;
  border-left:1.5px solid var(--rail);border-bottom:1.5px solid var(--rail);border-bottom-left-radius:10px}
.child.is-path::before{border-color:var(--acc)}
.child:hover{color:var(--ink);font-weight:600}
.child:hover svg{color:var(--acc)}
```
(Set `--acc` per section. Mark `.is-path` on every child up to and including the hovered one.)

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Airy, precise hairline UI with tasteful per-section accents. |
| Originality | 7 | Tree connectors that fill to the hovered item are a fresh touch on a standard accordion. |
| Usability | 7 | Clear wayfinding; closed titles fail AA and focus states are unproven. |
| Craft | 8 | Consistent rhythm, rounded elbows, coherent accent mapping. |

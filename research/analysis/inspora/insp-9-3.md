---
id: insp-9-3
source: inspora
category: Illustration
status: analyzed
title: "Retro CRT"
creator: "@bartuiux"
styles: [dark-premium, isometric, technical-wireframe, hairline-ui]
patterns: [onboarding-step-card, step-counter-label, isometric-hero-illustration, ambient-typing-loop, keycap-glow-pattern]
mode: dark
palette: ["#0a0a0a", "#111111", "#1d1d1d", "#343434", "#585858", "#7f7f7f", "#eaeaea"]
type_families: ["Inter Display / Geist-style neo-grotesk (likely)"]
type_class: [neo-grotesk]
radius_px: [24, 32]
motion: {durations_s: [6.57], easing: [linear], loop: true}
scores: {aesthetics: 8, originality: 6, usability: 7, craft: 8}
craft_signals: [hairline-isometric-construction-lines, lit-keycaps-as-only-highlight, double-card-halo, tonal-step-surfaces, step-counter-at-caption-size]
anti_patterns: [motion-too-subtle-to-read-at-thumbnail, illustration-bleeds-into-card-edge]
---
# Retro CRT — @bartuiux

## 1. Snapshot
- **Subject:** A single 1080×1080 looping video, 6.57 s long. It shows one onboarding or feature card, "06 / 08 · Empowering Developers", for a product called AO Starter. The card is topped by an isometric line drawing of a beige-box CRT computer and keyboard, rendered in near-black greys.
- **Why it's remarkable:** The whole illustration is drawn in four grey values. The only "light" comes from a few glowing keycaps and a single bright cursor line on the screen. This makes the ambient animation feel like the machine is typing.

## 2. Composition & layout
- **Canvas:** #0a0a0a. The card sits centred at x≈243→833 (590 px wide) and y≈168→910 (742 px tall), so it occupies about 55% of the width. Side margins are about 243 px.
- **Halo:** A second, slightly lighter rounded rectangle about 20 px larger on every side (x≈222→855) sits behind the card. The two read as a card with a soft outer glow, not as a border.
- **Upper area (about 70%):** The isometric illustration. The CRT bounding box is about 380×380 px with its top-left near (400,220). The keyboard lies in front at a 30° isometric angle. Faint construction grid lines extend past the objects and fade out before the card edge.
- **Text block:** Left-aligned at x≈281, an inset of about 38 px from the card edge. Spacing: the counter at y≈733, the title baseline at about 795, and the body at 830/860. The bottom padding is about 50 px.

## 3. Typography
- One neo-grotesk family with a single-storey "g" and tight apertures, close to Inter Display or Geist.
- **Title:** "Empowering Developers", about 36 px, medium (500), tracking about −0.01 em, colour #eaeaea.
- **Body:** two lines of about 21 px regular in #7f7f7f, with leading of about 30 px (1.43).
- **Counter:** "06 / 08", about 18 px regular in #7d7d7d, with spaced slashes. This is the "carousel step" cue.
- **Scale:** 18 / 21 / 36, a step of about 1.7 from body to title. Hierarchy comes from size and grey value, with weight barely changing.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #0a0a0a | page canvas | 90% |
| #111111 | card surface | (inside the 90% bucket) |
| #1d1d1d | halo, CRT faces | 8% |
| #343434 / #585858 | line work, edges | about 1.3% |
| #a8a8a8 → #eaeaea | lit keycaps, cursor, title | about 0.5% |
| #7f7f7f | body and counter text | — |

WCAG checks:
- Title #eaeaea on #111111: 15.7:1.
- Body #7f7f7f on #111111: 4.72:1 (passes AA by a small margin).
- Counter #7d7d7d on #111111: 4.59:1.

Strategy: monochrome, with luminance reserved for the "active" elements: keys being pressed and the line being written.

## 5. Depth & material
- No shadows inside the card. Volume on the CRT comes from three face tones (top lightest, front mid, side darkest), separated by roughly 1 px lighter edge strokes.
- The grid floor recedes into darkness, which gives an implied vignette.
- **Card elevation:** halo plus surface step (#0a0a0a → #1d1d1d halo → #111111 card). It is an inverted bevel: the halo is lighter than the card itself.

## 6. Components & patterns
- **Onboarding step card:** counter + title + 2-line description. It is evidently one card of an 8-card series ("06 / 08").
- **Hero illustration** contained within the card, sharing its corner radius (about 24 px inner, about 32 px halo).
- **Keycap glow cluster:** about 12 keys lit in a scattered pattern, which reads as a typing heat-map.

## 7. Motion
- Measured: duration 6.57 s at 30 fps, `motion_fraction` 0.0, mean energy 0.07, and no segments above threshold. `seamless_loop_likely: true` (first/last difference 0.13).
- The motion is tiny in area. Across the 9 frames, the bright cursor line on the CRT jumps between about 6 vertical positions, and its length grows and shrinks (about 20 to 70 px). The lit keycaps reshuffle every frame.
- The estimated cadence is about 0.7 s per "typed line", with stepwise (not tweened) changes, like a terminal. The rest of the frame is static.
- It is a seamless ambient loop, intended to sit behind a static UI without competing.

## 8. Brand system
n/a — not a brand system. Identity cues: a grey-on-black hairline isometric illustration style, likely shared across the 8 cards; "AO Starter" naming; developer and terminal metaphors.

## 9. UX
- The counter tells the user where they are in the sequence. The copy is short (two lines of about 35 characters).
- **Risks:**
  - The body text passes AA only by 0.2. On lower-quality displays the #111 vs #0a0a0a card edge disappears, so the card may read as floating text.
  - Motion is very subtle, which is good for calm but invisible in a thumbnail.

## 10. Craft signals
- Every isometric edge is about a 1 px #343434–#585858 stroke. There are no fills brighter than #1d1d1d except active keys.
- Highlights are reserved for state (keys and cursor), never decoration.
- The card has a 20 px halo ring one tone lighter than the card, a dark-mode alternative to a drop shadow.
- The text inset (38 px) matches the illustration's left construction line at about x 281.
- Grid lines fade out before the card edge rather than being clipped.

## 11. Reproduction recipe
```css
:root{--bg:#0a0a0a;--halo:#161616;--card:#111;--line:#3a3a3a;--hi:#eaeaea;--muted:#7f7f7f;--r:24px}
body{background:var(--bg);font-family:"Inter Display","Inter",system-ui,sans-serif}
.card{width:590px;border-radius:var(--r);background:var(--card);
  box-shadow:0 0 0 20px var(--halo);padding:0 38px 50px}
.card .count{font-size:18px;color:var(--muted);letter-spacing:.02em}
.card h3{font-size:36px;font-weight:500;letter-spacing:-.01em;color:var(--hi);margin:18px 0 12px}
.card p{font-size:21px;line-height:1.43;color:var(--muted);max-width:16em}
.key.on{fill:#d8d8d8;filter:drop-shadow(0 0 4px rgba(255,255,255,.35))}
@keyframes cursor{0%,100%{transform:translateY(0) scaleX(1)}33%{transform:translateY(24px) scaleX(.4)}66%{transform:translateY(72px) scaleX(.8)}}
.cursor{animation:cursor 2.1s steps(3) infinite}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Restrained four-grey illustration; one light source makes it cohesive. |
| Originality | 6 | Isometric hairline retro tech is a known dev-tool trope. |
| Usability | 7 | Clear step card; body text only just passes contrast. |
| Craft | 8 | Consistent stroke weights, tonal halo, and a seamless loop. |

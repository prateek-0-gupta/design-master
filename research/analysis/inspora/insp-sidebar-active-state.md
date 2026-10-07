---
id: insp-sidebar-active-state
source: inspora
category: Product
status: analyzed
title: "Sidebar Active State"
creator: "@heyimgustavo"
styles: [minimal-swiss, micro-interaction, photo-led]
patterns: [sidebar-nav, active-indicator-dot, indent-on-active, section-colour-coding, new-badge, scroll-fade-mask, grouped-nav-with-icons]
mode: light
palette: ["#fafafa", "#1a1a1a", "#707070", "#ebebe9", "#dcfce7", "#3b82f6", "#d9206a", "#e0712a"]
type_families: ["Inter (likely)"]
type_class: [neo-grotesk]
radius_px: [9999, 8]
motion: {durations_s: [0.37, 0.47], easing: [ease-out, ease-in], loop: false}
scores: {aesthetics: 8, originality: 6, usability: 8, craft: 8}
craft_signals: [dot-inherits-section-hue, text-shifts-to-make-room-for-dot, hover-darkens-only, top-and-bottom-scroll-fades, colour-coded-section-icons, soft-green-pill-badges, photo-strip-gives-context]
anti_patterns: [badge-text-under-3to1, colour-only-transient-state]
---
# Sidebar Active State — @heyimgustavo

## 1. Snapshot
- **Subject:** An 11.0 s, 936×1190 (120 fps) recording of a documentation sidebar for a design-craft knowledge base. Groups are Craft, Typography, Color, Layout and Motion, with items such as "Tabular Numbers", "OKLCH" and "Nested Border Radius". The sidebar sits beside a blurred landscape photo.
- **Why it's remarkable:** The active item is marked by a **small dot in its section's colour**, and the label **slides right about 16 px** to make room for it. The selection is a tiny typographic event rather than a heavy highlight bar.

## 2. Composition & layout
- **Photo strip:** the left 150 px of the frame shows the scenic backdrop (sky, cumulus, green field, heavily motion-blurred). A 1 px light divider and a soft shadow separate it from the sidebar panel (#fafafa), which runs from x≈165 to the right edge.
- **Nav column:** starts at x≈228.
  - Section headers have a 22 px tinted icon with a 16 px gap before the label.
  - Items are spaced about 48 px apart (line-height plus padding), with about 96 px between sections.
- **Badges:** "New" pills about 60×28 px, set about 14 px after the label.
- **Scroll fades:** items within about 60 px of the top and bottom edges fade to near-transparent ("Taste Is Trained", "Scroll Fades").

## 3. Typography
- Inter-like neo-grotesk:
  - Items are about 23 px Regular in grey #707070.
  - Section headers are about 24 px Regular in #1a1a1a.
  - The active and hover item becomes #1a1a1a. The active item may go slightly heavier, though the change looks colour-only.
  - The "New" badge is about 15 px Medium green.
- The tracking is default; there is no uppercase anywhere, so the tone is calm and editorial.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #fafafa | panel | 77% |
| #1a1a1a | headers, active text | — |
| #707070 | idle items | — |
| #ebebe9 | divider / panel edge | 2.4% |
| #dcfce7 + ~#2fa24f | "New" badge fill and text | — |
| ~#3b82f6 | Typography section (icon, dot, transient text) | — |
| ~#d9206a | Color section | — |
| ~#e0712a | Layout / Craft section | — |
| ~#8b5cf6 | Motion section icon | — |
| #a7a097 / #7a939d / #6f671e / #d6ae88 | backdrop photo (sky, field, cloud) | 14% |

WCAG checks:
- Idle #707070 on #fafafa: 4.74:1 (passes AA).
- Active #1a1a1a: 16.7:1.
- **"New" green on mint: 2.99:1 (fails).**
- The transient coloured labels: blue 3.52:1, orange 3.06:1, magenta 4.61:1.

The section accent hues only appear in the icon and dot, so they never have to carry text contrast once the state settles.

## 5. Depth & material
- The panel is flat. Its only depth is a soft left-edge shadow over the photo and the vertical scroll fades (mask gradients).
- The badges are flat mint pills with a 1 px slightly darker green border.

## 6. Components & patterns
- **Grouped sidebar:** each section has a coloured glyph (Aa, three circles, layout grid, motion arc, pen nib), so the section colour comes from the icon.
- **Item states:**
  - idle: grey;
  - hover: #1a1a1a with no background;
  - pressed / just selected: text in the section colour plus the dot (e.g. "Tabular Numbers" blue at 4.28 s, "Hit Areas" orange at 3.06 s, "Novelty Budget" orange at 9.17 s);
  - settled active: #1a1a1a text with a coloured dot.
- **New badge:** green pill.
- **Top-level links** (Index, GOATs, Resources) carry no icons and sit above the sections.

## 7. Motion
Measured: 11.0 s at 120 fps, `motion_fraction` 0.08. Only 2 segments pass the threshold:
- 3.03–3.40 s (0.37 s, peak 0.86 → ease-in);
- 7.40–7.87 s (0.47 s, peak 0.25 → ease-out).

These are the two scroll movements (the list scrolling up to the top at about 7.4 s).

The dot and indent change is small (about 16 px) and sits below the threshold. From the frames:
- the dot appears and the label translates right as one move, estimated at 0.15–0.2 s ease-out;
- the section-colour text holds for about 1 s, then settles to black;
- hovering darkens the text instantly (about 0.1 s).

## 8. Brand system
n/a — not a brand system. Identity cues:
- a section-colour taxonomy (blue for type, magenta for colour, orange for layout and craft, violet for motion);
- nature photography as atmosphere.

## 9. UX
- **Strengths:**
  - The selected item is unmistakable without a heavy fill.
  - Section hue gives wayfinding.
  - "New" badges call out fresh content.
  - Scroll fades hint at more content.
  - Rows are about 48 px tall, a good hit area.
- **Risks:**
  - The dot is only about 6 px, a small target for the eye.
  - The coloured transient labels and the green badge fail AA.
  - The fades can make the first and last items look disabled.

## 10. Craft signals
- The active dot takes the hue of its section's icon, consistently across four sections.
- The label translates right by about the dot's width plus gap, so the dot never overlaps the text.
- Hover changes only the text colour (no background), keeping the list airy.
- Scroll fades are applied at both ends of the scroll container.
- Badges are vertically centred on the label's x-height and have a 1 px border one shade darker than their fill.
- Section icons all share one size (22 px) and line weight (about 1.5 px).

## 11. Reproduction recipe
```css
:root{--panel:#fafafa;--ink:#1a1a1a;--idle:#707070;--badge-bg:#dcfce7;--badge-fg:#15803d;/* AA-safe */
  --sec-type:#3b82f6;--sec-color:#d9206a;--sec-layout:#e0712a;--sec-motion:#8b5cf6}
.nav{background:var(--panel);overflow-y:auto;
  mask-image:linear-gradient(transparent,#000 60px,#000 calc(100% - 60px),transparent)}
.nav a{display:flex;align-items:center;gap:10px;height:48px;color:var(--idle);position:relative;
  transition:color .12s ease-out,transform .18s cubic-bezier(.2,.8,.2,1)}
.nav a:hover{color:var(--ink)}
.nav a::before{content:"";position:absolute;left:-16px;width:6px;height:6px;border-radius:50%;background:var(--sec);
  opacity:0;transform:scale(.4);transition:opacity .18s,transform .18s cubic-bezier(.2,.8,.2,1)}
.nav a[aria-current=page]{color:var(--ink);transform:translateX(16px)}
.nav a[aria-current=page]::before{opacity:1;transform:none}
.section[data-s=type]{--sec:var(--sec-type)} .section[data-s=color]{--sec:var(--sec-color)}
.badge{font:500 12px/1 Inter;padding:5px 8px;border-radius:9999px;background:var(--badge-bg);color:var(--badge-fg);border:1px solid #bbf7d0}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Airy, editorial list with tasteful section hues against a lush photo. |
| Originality | 6 | Dot-and-indent active states exist (Vercel, Linear docs); the colour-coded variant is a nice refinement. |
| Usability | 8 | Clear states, wayfinding and generous hit areas. Badge contrast fails. |
| Craft | 8 | Consistent hue logic, matched indent and both-end fades. |

---
id: insp-gooey-navbar-component
source: inspora
category: Motion
status: analyzed
title: "navbar component"
creator: "@SwamiMalode"
styles: [dark-premium, micro-interaction, minimal-swiss]
patterns: [split-and-merge-navbar, active-item-detaches, gooey-segment-transition, icon-label-nav-items, single-accent-active-state]
mode: dark
palette: ["#111111", "#222222", "#3c3b40", "#8e8e98", "#ec3304", "#ffffff"]
type_families: ["Inter (likely)"]
type_class: [neo-grotesk]
radius_px: [30]
motion: {durations_s: [], easing: [ease-in-out], loop: true}
scores: {aesthetics: 7, originality: 8, usability: 7, craft: 7}
craft_signals: [neighbours-regroup-around-active, equal-60px-split-gaps, accent-only-on-active, accent-edge-leads-transition, icon-weight-matches-text]
anti_patterns: [white-on-orange-4-17-to-1, surface-barely-separates-from-page]
---
# navbar component — @SwamiMalode

## 1. Snapshot
- **Subject:** A 12.4 s, 2474×1404 recording of a four-item dark navbar (Home, Changelog, Career, About). Selecting an item makes it **detach** from the bar as a separate orange-red pill, and the remaining items **re-fuse** into grey groups on either side.
- **Why it's remarkable:** The bar's topology itself encodes the selection. Instead of a highlight sliding along a fixed track, the track splits around the active item and closes back up like liquid ("gooey").

## 2. Composition & layout
- Centred horizontally at y≈685 (the frame middle) on a #111111 page.
- **Items:** about 118 px tall, radius ≈30 px (a rounded rectangle, not a full pill: about 25% of the height). Horizontal padding is about 60 px, with about 40 px between icon-label pairs inside a group.
- **Splits:** when an item is active, a ≈60 px gap opens on each side of it. Changelog active gives [Home] · [Changelog] · [Career About]. About active gives [Home Changelog Career] · [About].
- Total width varies from about 1370 to about 1440 px as the groups re-form. The bar stays centred, so its ends breathe.

## 3. Typography
- Neo-grotesk (Inter-like) at about 42 px real (≈21 CSS at 2×).
- **Inactive:** medium #8e8e98 (a cool grey). **Active:** semibold white.
- Icons are 1.5 px outline glyphs (house, open book, briefcase, info-circle) sized about 40 px, the same optical weight as the text.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #111111 | page | 96% |
| #222222 | nav group surface | 2.5% |
| #3c3b40 | icon strokes / hover lift | <1% |
| #8e8e98 | inactive labels | — |
| #ec3304 | active item fill | 1% |
| #ffffff | active label | — |

WCAG checks:
- Inactive #8e8e98 on #222222 is 4.9:1.
- White on #ec3304 is **4.17:1**, which passes for large text only. At about 21 CSS px semibold it qualifies as large (≥18.66 px bold), so it is borderline acceptable.
- The group surface #222 against the page #111 is only 1.19:1. The bar's shape is barely visible, so the split relies on gaps that are hard to perceive.

## 5. Depth & material
- Entirely flat: no shadows, borders or gradients.
- **Mid-transition** (t≈11.72 s): the departing active item shows a faint red-brown tint (≈#2b1f1d) and a 2 px red edge on its leading side. That edge is the residue of the gooey merge, which suggests an SVG goo filter (blur plus alpha threshold) or animated widths with colour bleed.

## 6. Components & patterns
- **Split navbar:** the active item is a standalone accent pill, and inactive items are grouped into neutral bars.
- The groups change membership on every selection: three, two or one items per group.
- The hand cursor only appears on hover, and hover has no visible fill change in the sampled frames.

## 7. Motion
Measured: 120 fps, 12.4 s, `motion_fraction` 0.04 with **no segments above threshold**, because the changes are small relative to the large dark frame. `seamless_loop_likely` is true (`first_last_diff` 1.65).

From frames, about one selection every 1.4 s: Changelog → About → Changelog → About → Changelog → (about 7.58 s, all grey) → About → Changelog → About.
- The frame at 7.58 s shows all items grey with gaps in unusual places ([Home Changelog] · [Career] · [About]). This is an in-between state, so a split/merge passes through intermediate topologies.
- The frame at 8.96 s shows About at a darker red (≈#b8320f), with the fill still fading in.

Estimated transition length is about 0.4–0.6 s with an ease-in-out feel (inferred from the partial states caught in 3 of 9 frames).

## 8. Brand system
n/a — not a brand system. A single "signal orange" (#ec3304) accent on graphite is the only identity cue.

## 9. UX
- **Strengths:**
  - The active item is unmistakable (colour plus isolation).
  - Labels sit next to icons.
  - Equal visual weight across items.
- **Risks:**
  - The bar keeps changing width and grouping, so item positions shift by up to about 60 px on every click. That hurts muscle memory and can move a target out from under the cursor.
  - The surface/page contrast is 1.19:1.
  - Accent contrast is borderline.

## 10. Craft signals
- The gaps opened around the active item are equal (≈60 px) on both sides.
- Accent colour is used only on the active item, with no hover tint.
- Icon stroke weight (≈1.5 px) visually equals the label stem weight.
- The leading-edge red line during the merge (t≈11.72 s) indicates direction of travel.
- The whole cluster recentres as widths change, so the composition stays symmetric.

## 11. Reproduction recipe
```html
<svg width="0" height="0"><filter id="goo"><feGaussianBlur in="SourceGraphic" stdDeviation="8"/>
  <feColorMatrix values="1 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 22 -10"/><feComposite in="SourceGraphic" operator="atop"/></filter></svg>
```
```css
:root{--page:#111;--surface:#222;--ink-2:#8e8e98;--accent:#ec3304;--r:15px;--gap:30px;--t:.5s cubic-bezier(.65,0,.35,1)}
.nav{display:flex;filter:url(#goo)}
.nav a{display:flex;gap:10px;align-items:center;padding:16px 28px;background:var(--surface);color:var(--ink-2);
  font:500 21px Inter,sans-serif;border-radius:0;transition:margin var(--t),background-color var(--t),color var(--t),border-radius var(--t)}
.nav a:first-child{border-radius:var(--r) 0 0 var(--r)} .nav a:last-child{border-radius:0 var(--r) var(--r) 0}
.nav a[aria-current]{background:var(--accent);color:#fff;font-weight:600;border-radius:var(--r);margin-inline:var(--gap)}
.nav a:has(+ [aria-current]){border-radius:0 var(--r) var(--r) 0}
.nav [aria-current] + a{border-radius:var(--r) 0 0 var(--r)}
```
(The goo filter fuses neighbouring blobs while the margins animate, which gives the liquid split.)

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 7 | Tidy graphite plus a single orange accent. Pleasant but sparse. |
| Originality | 8 | Encoding selection as bar topology (split/merge) is an uncommon idea. |
| Usability | 7 | The active state is very clear, but shifting item positions and a low surface contrast cost points. |
| Craft | 7 | Consistent gaps and icon weights. Transitional colour residue is visible mid-merge. |

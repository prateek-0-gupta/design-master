---
id: insp-6-1
source: inspora
category: Motion
status: analyzed
title: "Light work"
creator: "@Designownow_"
styles: [dark-premium, skeuomorphic, monochrome, physical-material]
patterns: [toggle-driven-light-beam, icon-cast-shadow, chrome-switch, status-chip-label, bracket-corner-frame]
mode: dark
palette: ["#1a1a1a", "#181818", "#262626", "#555555", "#696969", "#b2b2b2", "#fdfdfd"]
type_families: ["Lexend / Outfit-style wide geometric sans (likely)"]
type_class: [geometric-sans]
radius_px: [40, 24, 9999]
motion: {durations_s: [0.23, 0.27, 0.3], easing: [ease-out, ease-in-out], loop: true}
scores: {aesthetics: 8, originality: 8, usability: 6, craft: 8}
craft_signals: [light-bar-casts-icon-shadow-upward, beam-spills-beyond-card-top, chrome-toggle-with-inner-track, dashed-outline-status-chip, offset-bracket-corners-around-card, monochrome-only-luminance]
anti_patterns: [secondary-text-low-contrast-on-dark, status-chip-barely-visible]
---
# Light work — @Designownow_

## 1. Snapshot
- **Subject:** A 17.2 s, 1506×1502 (60 fps) dark card titled "Light Work". A chrome toggle switches "Easy Mode" on and off, and when it is on, a horizontal light bar ignites inside the card. The bar throws a beam upward, lights the feather/leaf icon and casts the icon's shadow up the wall.
- **Why it's remarkable:** The toggle state is expressed as real lighting (beam, falloff and cast shadow), monochrome only, with progressive blur on the shadow.

## 2. Composition & layout
- **Card:** About 728×980 px (x 390→1118, y 248→1228), centred, with a radius of about 40.
- **Bracket frame:** Corner arcs offset about 24 px outside the card, opening at the corners.
- **Upper half:** A lit recess about 508 px wide with the light bar at y≈745 (about 6 px tall). The icon, about 104 px, is centred at y≈515.
- **Lower block:**
  - Title "Light Work" at about 44 px, at x≈438.
  - Two-line description at about 28 px.
  - A 1 px rule under the description (about 410 px).
  - A chrome toggle about 190×80 px at the bottom-right.
  - A dashed "Easy Mode Off/On" chip about 190×56 px above the toggle.

## 3. Typography
- A wide geometric sans (Lexend or Outfit-like) with round "o" and "g".
- **Title:** About 44 px Medium in #f2f2f2 with wide letterforms.
- **Description:** About 28 px Regular, Title-Cased, in #8a8a8a.
- **Chip:** About 20 px in #6a6a6a.

## 4. Colour
| Hex | Role |
|---|---|
| #1a1a1a | page |
| #181818 / #262626 | card body / recess |
| #555555 → #696969 | lit wall (beam gradient) |
| #fdfdfd | light bar core |
| #b2b2b2 | chrome toggle housing |
| #000000 | toggle track (off) |

This is a strictly achromatic system with no hue at all.

WCAG:
- Title #f2f2f2 on #1a1a1a is 15.55:1.
- Description #8a8a8a on #1a1a1a is 5.04:1 (passes).
- Chip text about #5a5a5a on #1a1a1a is **2.52:1** (fails).

## 5. Depth & material
- **Light bar:** A thin emissive line with a bloom (about 10 px glow). It lights a trapezoid of wall above (a wider spill at the top, about 60% opacity falloff) and drops a hard shadow edge below.
- **Icon:** It casts a soft, elongated shadow upward. The shadow is sharper near the icon and blurrier further away (progressive blur, as the post description says).
- **Toggle:** Machined-metal chrome with a bevel highlight on top, a recessed black track, and a pale grey thumb.

## 6. Components & patterns
- A skeuomorphic chrome toggle. Off shows the thumb left on a black track, and on shows a white track.
- A status chip with a dashed outline that echoes the state ("Easy Mode Off" / "Easy Mode On").
- An icon "projection" area.
- Bracket-corner framing around the card.

## 7. Motion
- **Measured:** 8 segments across 17.2 s, median 0.29 s (0.23–0.30 s). motion_fraction is 0.13 and `seamless_loop_likely: true`.
  - 0.90 s: 0.23 s, peak 0.21. 6.03 s: 0.23 s, peak 0.07. 12.83 s: 0.30 s, peak 0.17. All ease-out: light ignition, fast on and soft settle.
  - 2.07 s, 2.93 s and 6.77 s: about 0.27–0.30 s, peak about 0.4 (symmetric). The toggle thumb travel and the light switching off.
- **Read:** About 250–300 ms transitions. Ignition is front-loaded like a real lamp. The beam fade and shadow appear together.

## 8. Brand system
n/a — not a brand system. Cue: a feather-in-pin icon plus the "Light Work" wordplay (light as illumination and as easy).

## 9. UX
- The metaphor maps state to outcome very clearly (on = lit).
- The redundant chip label helps clarify the state.
- **Risks:**
  - The chip is low-contrast.
  - The toggle is small relative to the card.
  - The title-cased description reads awkwardly.
  - Light versus dark-only states should also be announced via `aria-checked`.

## 10. Craft signals
- The beam extends beyond the card's top edge into the page background, as light would spill.
- The icon shadow is cast upward, consistent with a light source below it.
- The chrome toggle has a separate housing, inner track and thumb, each with its own highlight.
- The bracket corners are offset from the card by a constant about 24 px.
- The whole piece uses only greys from #000 to #fdfdfd.

## 11. Reproduction recipe
```css
:root{--page:#1a1a1a;--card:#181818;--wall:#262626;--lit:#696969;--ink:#f2f2f2;--muted:#8a8a8a}
.card{width:728px;height:980px;border-radius:40px;background:var(--card);position:relative;
  box-shadow:inset 0 1px 0 rgba(255,255,255,.05)}
.recess{position:absolute;left:110px;right:110px;top:0;height:497px;background:var(--wall);
  transition:background .25s cubic-bezier(.1,.8,.2,1)}
.on .recess{background:linear-gradient(to top,var(--lit),#3a3a3a 70%,transparent)}
.bar{position:absolute;left:110px;right:110px;top:497px;height:6px;border-radius:3px;background:#2a2a2a;transition:.25s}
.on .bar{background:#fdfdfd;box-shadow:0 0 12px #fff,0 -30px 80px rgba(255,255,255,.25)}
.icon-shadow{filter:blur(2px);-webkit-mask:linear-gradient(to top,#000,transparent);transform:translateY(-60px) scaleY(1.6);opacity:0;transition:opacity .25s}
.on .icon-shadow{opacity:.5}
.switch{width:190px;height:80px;border-radius:24px;background:linear-gradient(#d9d9d9,#9a9a9a);box-shadow:inset 0 2px 0 #fff,0 6px 14px rgba(0,0,0,.5)}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Moody monochrome with a single light source is cinematic and cohesive. |
| Originality | 8 | Expressing toggle state as physical lighting with cast shadow is fresh. |
| Usability | 6 | The state is clear, but the chip is low-contrast and the control small. |
| Craft | 8 | Physically consistent light direction, a detailed chrome switch, and tight timing. |

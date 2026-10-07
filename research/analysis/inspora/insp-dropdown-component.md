---
id: insp-dropdown-component
source: inspora
category: Product
status: analyzed
title: "Dropdown Component"
creator: "@gabriell_lab"
styles: [glassmorphism, monochrome, micro-interaction]
patterns: [share-permissions-popover, segmented-access-toggle, invite-by-email-field, copy-link-row, squircle-avatar-list, canvas-dim-on-open, avatar-stack-trigger]
mode: mixed
palette: ["#aaadac", "#ffffff", "#676a6a", "#808280", "#9d9f9e", "#4a4b49", "#282a2a"]
type_families: ["Inter (likely)"]
type_class: [neo-grotesk]
radius_px: [40, 28, 20, 9999]
motion: {durations_s: [0.2, 0.2], easing: [ease-in-out], loop: true}
scores: {aesthetics: 8, originality: 6, usability: 6, craft: 7}
craft_signals: [whole-canvas-desaturates-behind-popover, squircle-avatars-match-icon-tiles, hairline-group-dividers, segmented-control-inset-thumb, popover-anchored-under-trigger]
anti_patterns: [typo-full-acces, secondary-text-low-contrast, edit-icons-without-role-label]
---
# Dropdown Component — @gabriell_lab

## 1. Snapshot
- **Subject:** A 3.8 s, 1920×1440 loop. On a design-tool canvas (dotted grid, media frames with W/H badges), clicking the collaborators avatar stack opens a grey glass sharing popover. It holds an access toggle, an email invite field, a project link row, team, and three people.
- **Why it's remarkable:** Opening the popover dims and greys the whole canvas into the same tone as the panel. The popover reads as a lens over the workspace rather than a box on top of it.

## 2. Composition & layout
- **Top-right cluster:**
  - avatar stack in a pill (~240×88 px) with a chevron;
  - "Invite" button (~160×88, radius ~20);
  - current-user squircle avatar (~88 px).
- **Popover:** about 912×1000 px with a ~40 px radius, anchored ~32 px below the trigger and right-aligned to the Invite button's left edge.
- **Internal stack:**
  - segmented control (~104 px tall, inset thumb);
  - email field (~104 px) with an ↑ submit arrow;
  - hairline divider;
  - Project Link row with a "Copy" button;
  - divider;
  - Team row;
  - three people rows (~104 px avatars at ~126 px pitch) with pencil icons.
- Left padding is a consistent ~22 px. Text starts at x≈820, aligned across all rows, whether icon tile or avatar.

## 3. Typography
- Inter-like neo-grotesk.
- **Titles:** row titles ~34 px (≈17 CSS) white; subtitles "Anyone can view" ~32 px in a light grey.
- **Segmented labels:** ~32 px. The active one is white; "View Only" is dimmer.
- Weight is regular/medium only.
- **Typo:** the active tab reads "Full Acces".

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #aaadac | dimmed canvas | 24% |
| #ffffff | canvas (closed), text | 17% |
| #676a6a / #727574 | popover surface | 20% |
| #808280 / #9d9f9e | segmented thumb, inputs, buttons | 19% |
| #4a4b49 / #282a2a | video thumbnails, shadows | 11% |

WCAG checks:
- White on popover #676a6a: 5.46:1.
- Subtitle ≈#c8cbcb on #676a6a: **3.34:1 (large only)**.
- White on the lighter thumb #808280: **3.87:1**.

The palette is entirely achromatic; colour comes only from avatar photos (teal, lime).

## 5. Depth & material
- The popover is translucent grey with backdrop blur. The thumbnails beneath bleed through as dark smudges at the bottom.
- Inner controls are one step lighter (inset fills, no borders), and the segmented thumb is lighter again.
- A large soft shadow sits under the popover, and the canvas behind gets a grey scrim (~35%).

## 6. Components & patterns
- **Segmented control:** two options with an inset rounded thumb.
- **Invite field:** placeholder "name@gmail.com" with an inline send arrow.
- **Link row:** icon tile, title/subtitle, and a trailing "Copy" pill.
- **People rows:** squircle photo, name, pencil (edit permission). There is no role label, so the current permission per person is not visible.

## 7. Motion
- **Measured:** 2 segments.
  - **Open, 0.3–0.5 s (0.20 s):** symmetric ease-in-out, peak 0.42.
  - **Close, 3.23–3.43 s (0.20 s):** peak 0.58.
- motion_fraction is 0.11, and the loop is seamless (first/last diff 0.15).
- **From frames:** the canvas scrim and popover arrive together. The popover appears to scale/fade from its top edge (origin under the trigger), with no bounce.
- 200 ms is a standard, snappy menu duration.

## 8. Brand system
n/a — not a brand system. Identity cues: a monochrome grey-glass UI that lets user photos supply colour.

## 9. UX
- Covers the full sharing model in one surface: invite, link, team, individuals.
- **Risks:**
  - Pencils with no role text hide each person's permission.
  - The segmented "Full Access / View Only" applies to the invite but sits far from the field it modifies.
  - Grey-on-grey secondary text is weak.
  - The typo undermines polish.

## 10. Craft signals
- Avatars and icon tiles share one squircle size (~104 px) and radius (~20 px), so text columns align.
- The canvas scrim matches the popover tone, which makes the overlay feel continuous.
- Hairline dividers separate only the three groups (invite / link / people), not every row.
- The popover's right edge aligns to the trigger cluster's right edge.

## 11. Reproduction recipe
```css
.scrim{position:fixed;inset:0;background:rgba(90,92,92,.35);backdrop-filter:grayscale(.6);transition:opacity .2s ease-in-out}
.pop{width:456px;border-radius:20px;padding:11px;background:rgba(103,106,106,.82);backdrop-filter:blur(24px);
  box-shadow:0 30px 60px rgba(0,0,0,.25);color:#fff;transform-origin:top right;animation:pop .2s ease-in-out}
@keyframes pop{from{opacity:0;transform:scale(.96) translateY(-6px)}}
.seg{display:grid;grid-template-columns:1fr 1fr;padding:4px;border-radius:14px;background:rgba(255,255,255,.08)}
.seg [aria-selected=true]{background:rgba(255,255,255,.18);border-radius:10px}
.tile,.avatar{width:52px;height:52px;border-radius:10px}
.sub{color:#dfe1e1} /* lift from #c8cbcb for AA */
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Cohesive grey-glass mood; photos supply colour. |
| Originality | 6 | Standard share popover; the canvas-tinting scrim is the twist. |
| Usability | 6 | Complete feature set, but hidden roles and weak contrast. |
| Craft | 7 | Strong alignment and tile system; a typo in the primary control. |

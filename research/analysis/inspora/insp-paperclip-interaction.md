---
id: insp-paperclip-interaction
source: inspora
category: Product
status: analyzed
title: "Paperclip interaction"
creator: "@SyadySyarief"
styles: [micro-interaction, corporate-clean, skeuomorphic]
patterns: [share-modal, document-preview-card, stacked-paper-preview, paperclip-hover-delight, integration-icon-row, copy-link-field, fade-out-text-preview]
mode: light
palette: ["#ffffff", "#f3f3f3", "#1a1a1a", "#555555", "#a4b5c7", "#5aa2f8"]
type_families: ["Inter (likely)"]
type_class: [neo-grotesk]
radius_px: [32, 16, 12, 9999]
motion: {durations_s: [0.13, 0.23], easing: [ease-out], loop: false}
scores: {aesthetics: 8, originality: 8, usability: 8, craft: 8}
craft_signals: [skeuomorphic-object-in-flat-ui, paper-stack-fans-on-hover, gradient-fade-truncation, soft-tile-icons, shortcut-hint-in-cta, origin-anchored-modal]
anti_patterns: [white-on-light-blue-cta]
---
# Paperclip interaction — @SyadySyarief

## 1. Snapshot
- **Subject:** A 6.3 s, 1186×1080 (60 fps) clip of the "Share transcript" modal for a meeting tool ("Meetball"). It contains a preview card of the meeting summary, an "Add to" row of five integrations and a copy-link field.
- **Why it's remarkable:** A tiny realistic **paperclip** clips onto the preview card, and on hover the card **fans into a stack of pages**. A single physical metaphor turns a generic share dialog into a "here is your document" moment.

## 2. Composition & layout
- **Top bar:** top-right of the page, with a "Share" ghost pill (about 140×64 px, 1 px border) and an "Ask Meetball ⌘E" primary pill (about 250×64 px, blue).
- **Modal:** about 620×930 px at key scale, radius about 32 px, white on a #f3f3f3-tinted page. It drops directly below the Share button, so it is anchored to its trigger.
- **Internal stack, with padding of about 40 px:**
  - title row (Share transcript + ×);
  - preview area, with the card about 385×420 px centred;
  - "Add to" label;
  - a 5-up icon grid of about 72 px tiles with labels underneath, evenly spaced about 117 px apart;
  - the link field (about 540×70 px pill).
- The vertical rhythm is about 40 px between groups.

## 3. Typography
- Inter-like neo-grotesk:
  - The modal title is about 30 px Medium, #1a1a1a.
  - The card headline is about 26 px Medium with leading of about 1.5 over three lines.
  - Card body is about 18 px Regular #555 with leading of about 1.65. It is truncated by a fade to near-white over the last three lines.
- Integration labels are about 18 px Regular grey; "Copy link" is about 22 px Medium.
- The URL is about 20 px grey, with its end fading out instead of showing an ellipsis.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #ffffff | modal, card, page highlight | 84% |
| #f3f3f3 | page tint, icon tiles, link field | 12% |
| #a4b5c7 | paperclip steel, cool shadow tint | 4% |
| #1a1a1a | headings, × | — |
| #555555 | body, labels | — |
| ~#5aa2f8 (estimated from pixels) | primary CTA | — |

WCAG checks:
- #1a1a1a on white: 17.4:1.
- #555 on white: 7.46:1.
- #555 on #f3f3f3: 6.72:1.
- **White on the blue CTA (~#5aa2f8): 2.64:1, which fails.** The blue is too light.
- The clip's grey #a4b5c7 is decorative at 2.1:1.

The palette is almost entirely neutral, with the third-party logos supplying the only colour inside the modal.

## 5. Depth & material
- The modal has a very large, soft ambient shadow (about 0 30px 80px rgba(0,0,0,.08)) plus a 1 px #ececec border.
- **The preview card is paper:**
  - a white sheet with a 1 px hairline and a short soft shadow;
  - two sheets behind it, offset about ±4 px and rotated about ±1.5°, that appear on hover;
  - a metallic paperclip rendered with grey and white gradients that overlaps the top-left corner, so part of it sits "behind" the sheet.
- Icon tiles are #f3f3f3 squircles with radius about 16 px and no shadow.

## 6. Components & patterns
- **Share modal** with three tiers: preview → destinations → link.
- **Integration grid** (Drive, Notion, Linear, Jira, Slack): brand-colour glyphs on neutral tiles.
- **Copy-link pill:** the read-only URL with a fade-out on the left, and a link icon plus "Copy link" action on the right inside the same field.
- **Primary CTA** with a shortcut hint ("⌘E" at about 50% opacity).

## 7. Motion
Measured: 6.32 s, `motion_fraction` only 0.05, 2 segments. These are 0.73–0.87 s (0.13 s, peak 0.12 → ease-out) and 2.37–2.60 s (0.23 s, peak 0.07 → strong ease-out).
- **From frames:**
  - At 1.05 s the modal is open with an empty card outline. By 1.75 s the text has populated, so the content fades in after the shell (about 0.3–0.5 s stagger).
  - Between 1.75 and 2.46 s the paperclip appears and the card picks up its fanned back sheets (the 0.23 s snap).
- Afterwards, hovering the card makes the back sheets splay further (visible at 3.16 s and 5.26 s) with low energy, a small rotate of about 1–2°.
- The quick, front-loaded easing (peaks at 7–12% of the segment) gives a crisp "clip" feel.

## 8. Brand system
n/a — not a brand system. Identity cues:
- "Meetball" with a sparkle glyph on a blue pill;
- neutral, Linear-adjacent product chrome.

## 9. UX
- **Strengths:**
  - The preview confirms what is being shared before the user picks a destination.
  - Destinations use recognisable logos plus labels.
  - The copy action sits inside the field, which reduces targets.
  - The modal is spatially anchored to the Share button.
- **Risks:**
  - There is no visibility or permission control (who can view).
  - The white-on-sky-blue CTA fails contrast.
  - The faded URL hides the slug end.

## 10. Craft signals
- The paperclip overlaps the card edge with correct occlusion (one leg in front, one behind).
- Back sheets are offset by a few px and rotated about 1–2°, not merely duplicated.
- Body text is truncated with a gradient mask rather than "…".
- The URL truncation also uses a mask.
- Integration tiles are equal-sized squircles with brand glyphs at about 50% of the tile.
- The modal radius (~32 px) is twice the tile radius (~16 px), a consistent ratio.

## 11. Reproduction recipe
```css
:root{--bg:#f3f3f3;--surface:#fff;--ink:#1a1a1a;--muted:#555;--tile:#f3f3f3;--clip:#a4b5c7;--primary:#2f7ff0;/* darker than source for AA */
  --r-modal:32px;--r-tile:16px;--r-pill:9999px}
.modal{background:#fff;border:1px solid #ececec;border-radius:var(--r-modal);box-shadow:0 30px 80px rgba(0,0,0,.08);padding:40px}
.sheet{position:relative;background:#fff;border:1px solid #e6e6e6;border-radius:6px;box-shadow:0 6px 16px rgba(0,0,0,.06)}
.sheet::before,.sheet::after{content:"";position:absolute;inset:0;background:#fff;border:1px solid #e6e6e6;border-radius:6px;z-index:-1;
  transition:transform .23s cubic-bezier(.15,.9,.3,1)}
.preview:hover .sheet::before{transform:translate(-6px,4px) rotate(-2deg)}
.preview:hover .sheet::after{transform:translate(6px,6px) rotate(1.5deg)}
.sheet .body{mask-image:linear-gradient(#000 55%,transparent)}
.clip{position:absolute;left:12px;top:-14px;animation:clipOn .23s cubic-bezier(.15,.9,.3,1) both}
@keyframes clipOn{from{transform:translateY(-12px) rotate(-8deg);opacity:0}}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | A quiet neutral modal lifted by one tactile object. |
| Originality | 8 | The paperclip and page-fan metaphor for "share document" is a fresh, memorable micro-delight. |
| Usability | 8 | Clear three-tier structure and anchored placement; permissions are missing and the CTA contrast is weak. |
| Craft | 8 | Correct clip occlusion, mask-based truncation and consistent radii. |

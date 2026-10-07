---
id: insp-payment-links
source: inspora
category: Product
status: analyzed
title: "payment links"
creator: "@gabriell_lab"
styles: [corporate-clean, micro-interaction, soft-3d]
patterns: [share-modal, network-illustration-header, avatar-orbit, copy-link-field, share-target-row, scrim-over-table, nested-hero-panel]
mode: light
palette: ["#fffffd", "#f0f0ee", "#535559", "#696a6c", "#8d8e8e", "#111111", "#226bc7"]
type_families: ["Inter (likely)"]
type_class: [neo-grotesk]
radius_px: [44, 36, 9999]
motion: {durations_s: [0.23], easing: [ease-in-out], loop: false}
scores: {aesthetics: 7, originality: 6, usability: 7, craft: 7}
craft_signals: [nested-radius-hero-panel, avatars-on-curved-path, link-node-among-people, filled-black-close-button, two-tone-copy-icon, grey-scrim-not-blur]
anti_patterns: [illustration-cropped-by-panel-edge, mixed-brand-icon-styles]
---
# payment links — @gabriell_lab

## 1. Snapshot
- **Subject:** A 3.03 s, 2560×1920 clip in which a "Share payment link" modal opens over a recipients table in a fintech dashboard ("grain.payment").
- **Why it's remarkable:** The modal's header is an illustration rather than an icon. Customer avatars sit like stations on a thin curved line, with a chain-link node among them, so "this link travels between people" is drawn literally.

## 2. Composition & layout
- **Background:** a recipients table (columns Preferred Name / Country / Method / Account Details; rows about 130 px tall at key scale) dimmed by a mid-grey scrim.
- **Modal:**
  - about 810×930 px at key scale (≈1040×1190 real);
  - radius about 44 px, with about 18 px padding around an **inset hero panel** (#f0f0ee, radius about 36 px) that takes the top half (~460 px).
  - In the panel, the illustration fills the upper 60% and the title and description sit bottom-left.
- **Lower half:** "Share your link" label → URL pill field (about 715×80 px) → "Share to" label → five 90 px app icons with labels, spaced evenly about 152 px apart.
- **Close button:** a solid black 80 px circle that overlaps the panel at top-right, about 18 px in from each edge.

## 3. Typography
- Inter-like neo-grotesk, with no display face:
  - The title is about 31 px Medium #111.
  - The description is about 29 px Regular #535559 over two lines with leading of about 1.6.
  - Section labels ("Share your link", "Share to") are about 26 px Medium.
  - The URL is about 30 px Regular #535559; icon captions are about 26 px.
- Tight scale: everything sits between 26 and 31 px. Hierarchy is weight and colour only, which is calm but flat.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #8d8e8e / #767779 / #696a6c | scrimmed table background | 73% |
| #fffffd | modal surface | 10% |
| #f0f0ee | hero panel, field tint | 13% |
| #535559 | secondary text, link path | 3% |
| #111111 | titles, close button | — |
| #226bc7 | LinkedIn blue (third-party) | 0.3% |

WCAG checks:
- #111 on #fffffd: 18.9:1.
- Description #535559 on the #f0f0ee panel: 6.55:1.
- White × on #111: 18.9:1.
- The scrimmed table text (#111 on #696a6c) is 3.49:1, which is appropriate for de-emphasised background content.

## 5. Depth & material
- The scrim is a flat grey wash with no backdrop blur. The table stays legible, keeping context.
- The modal has a large, soft shadow and a 1 px light rim at the top.
- In the hero panel:
  - each avatar is a 90 px white disc with a soft drop shadow (about 0 8 20 rgba(0,0,0,.12)) holding a 60 px photo, so they read as tokens on a board;
  - the connecting path is a 1–2 px grey line with a faint double-stroke;
  - a blurred grey blob at the top centre adds depth of field.

## 6. Components & patterns
- **Share modal:** illustration header → copy-link → share targets.
- **URL field:** pill with a 1 px #e6e6e6 border and a two-square copy icon on the right (the front square black, the back one grey).
- **Share targets:** native app-icon squircles (Email, iMessage, LinkedIn, X, WhatsApp) with grey captions.
- **Close:** a filled black circle rather than a ghost ×, the strongest element on screen.

## 7. Motion
- **Measured:** 3.03 s, one segment from 0.23 to 0.47 s (0.23 s, peak 0.36, symmetric ease-in-out). It is the modal entrance plus the scrim fade, and `first_last_diff` is 92.6 because the scrim darkens the whole frame.
- **From frames:**
  - After the entrance, the avatars **drift along the curved path**. A fifth avatar slides in from the right edge (visible at 1.52 s and settled by 1.85 s) and the top avatar fades to about 40%.
  - This is a slow conveyor motion below the energy threshold, so it is estimated at about 1–1.5 s per step, linear.
  - The modal itself scales in from about 0.96 with a fade.

## 8. Brand system
n/a — not a brand system. Identity cues:
- warm off-white (#fffffd / #f0f0ee) instead of pure white;
- black as the only accent.

## 9. UX
- **Strengths:**
  - The copy field comes first (the most common action).
  - The share targets cover email, chat and social.
  - The modal is centred while the table remains readable underneath.
- **Risks:**
  - There is no confirmation state shown for copy.
  - The illustration crops an avatar at the panel's right edge, which reads as a bug rather than intent.
  - Third-party icons in full brand colour compete with the restrained UI.
  - There is no amount, expiry or recipient shown, so for a payment link the user cannot verify what they are sharing.

## 10. Craft signals
- Nested radii: the modal is about 44 px and the inner panel about 36 px, an ≈8 px difference that matches the ≈18 px inset.
- Avatars are mounted in white rings with soft shadow; the link node uses the same ring, so it reads as one of the participants.
- The copy icon uses two overlapping squares in black and grey (a duotone glyph).
- The close button overlaps the hero panel corner instead of floating in the white margin.
- Warm whites (#fffffd, #f0f0ee) avoid a clinical feel.

## 11. Reproduction recipe
```css
:root{--surface:#fffffd;--panel:#f0f0ee;--ink:#111;--muted:#535559;--line:#e6e6e6;--scrim:rgba(40,42,46,.45);
  --r-modal:44px;--r-panel:36px;--r-pill:9999px}
.scrim{position:fixed;inset:0;background:var(--scrim);animation:fade .23s ease-in-out both}
.modal{background:var(--surface);border-radius:var(--r-modal);padding:18px;box-shadow:0 40px 100px rgba(0,0,0,.18);
  animation:pop .23s cubic-bezier(.45,0,.55,1) both}
.hero{background:var(--panel);border-radius:var(--r-panel);padding:28px;position:relative;overflow:hidden}
.token{width:72px;height:72px;border-radius:50%;background:#fff;padding:6px;box-shadow:0 8px 20px rgba(0,0,0,.12);
  offset-path:path("M-40 180 C 120 40, 360 260, 720 120");animation:travel 9s linear infinite}
.close{width:64px;height:64px;border-radius:50%;background:var(--ink);color:#fff;position:absolute;top:18px;right:18px}
.url{border:1px solid var(--line);border-radius:var(--r-pill);padding:0 24px;height:64px;color:var(--muted)}
@keyframes pop{from{opacity:0;transform:scale(.96)}} @keyframes fade{from{opacity:0}}
@keyframes travel{to{offset-distance:100%}}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 7 | Warm-neutral, tidy modal with a pleasant illustrative header. |
| Originality | 6 | "People on a network path" is a known trope, though well applied to payment links. |
| Usability | 7 | Clear actions; lacks payment context and copy feedback. |
| Craft | 7 | Good nested radii and shadows; the cropped avatar and loud icons detract. |

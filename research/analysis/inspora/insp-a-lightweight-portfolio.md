---
id: insp-a-lightweight-portfolio
source: inspora
category: Web
status: analyzed
title: "A lightweight portfolio"
creator: "Blake (@cyze_dev)"
styles: [minimal-swiss, soft-3d, aurora-glow, playful-rounded]
patterns: [object-as-entry-gate, zoom-through-screen-transition, single-column-bio, icon-prefixed-link-list, prismatic-header-glow, underline-tab-nav, theme-toggle-dots]
mode: light
palette: ["#f4f7ff", "#fcdc6a", "#face38", "#b7930b", "#1a1c24", "#4a4d57", "#2b47c9", "#534b38"]
type_families: ["Inter (likely)"]
type_class: [neo-grotesk]
radius_px: [9999]
motion: {durations_s: [0.8, 0.1], easing: [ease-in-out], loop: false}
scores: {aesthetics: 8, originality: 8, usability: 6, craft: 7}
craft_signals: [screen-contents-preview-the-site, cool-tinted-off-white-canvas, link-colour-single-blue, prismatic-conic-glow-header, cast-shadow-under-3d-object, index-label-tracked]
anti_patterns: [entry-gate-delays-content, click-affordance-tiny]
---
# A lightweight portfolio — Blake

## 1. Snapshot
- **Subject:** An 8.9 s, 1646×1080 capture of a personal portfolio. The entrance is a single yellow retro all-in-one computer (Macintosh-like) whose CRT shows a "Click" button. Clicking zooms into the screen and lands on a sparse one-column bio page topped by a prismatic glow.
- **Why it's remarkable:** It makes the click into the site a physical act of "turning on" a computer. The CRT already shows a miniature of the site (collaged thumbnails behind the button), so the transition feels like passing through the glass.

## 2. Composition & layout
- **Entrance:**
  - the computer, about 240×235 px, is centred slightly left of centre (x≈680→915, y≈430→665) on an empty #f4f7ff canvas;
  - about 97% of the frame is negative space;
  - a soft drop shadow falls to the lower right, implying a key light from the upper left.
- **Landing page:**
  - a single column about 520 px wide starting at x≈514 (left of the true centre, about 31% from the left);
  - the header block ("Hi, I'm Blake / Product Engineer") with a two-dot toggle right-aligned to the column's end;
  - three short paragraphs at about 22 px with a 36 px line pitch;
  - a ~110 px gap, then four icon-prefixed links;
  - the footer has "Index" at the bottom left (tracked, small) and tabs "Featured / Projects / Snippets" at the bottom right with an underline on the active tab.

## 3. Typography
- **Family:** a single neo-grotesk (Inter-like: flat-topped "t", double-storey "a", open "e").
- **Name and text sizes:** the name is semibold at about 22 px in #1a1c24, the role is regular in grey, and body text is regular at about 22 px in #4a4d57 with leading of about 1.6.
- **Links:** regular in #2b47c9 with no underline; a 16 px glyph (asterisk, LinkedIn, GitHub, X) acts as the affordance.
- **Footer:** "Index" uses wide +0.1 em tracking at about 18 px, a quiet label that contrasts with the regular-tracked tabs.
- The CRT's "Click" label uses a rounded sans inside a pill with a 3 px black outline, a mock-OS button.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #f4f7ff | canvas (cool off-white) | 97% |
| #fcdc6a / #face38 | computer body yellow | <1% |
| #b7930b / #534b38 | yellow shading, shadow | <1% |
| #1a1c24 | name / headings | small |
| #4a4d57 | body | small |
| #2b47c9 | links | small |
| conic rainbow | header glow (landing only) | top 20% |

WCAG checks:
- Heading #1a1c24 on #f4f7ff is 15.86:1.
- Body #4a4d57 is 7.87:1.
- Link blue #2b47c9 is 6.88:1.
- The grey role line (about #6b6e78) is 4.75:1, which passes.

All text contrast is solid.

## 5. Depth & material
- **Computer:** a glossy plastic 3D render (likely a Spline/Three.js or pre-rendered sequence) with a bevelled bezel, floppy slot, LED dot and a curved CRT glass with grey reflection. The cast shadow sits about 40 px offset to the lower right, blurred, which grounds it.
- **Landing page:** completely flat. The only atmosphere is a blurred conic/radial rainbow (pink core, cyan, green, amber) bleeding down from the top edge, about 220 px deep. It is a modern counterpart to the retro object.

## 6. Components & patterns
- Object-as-gate entrance with a single CTA embedded in the object's screen.
- Bio paragraphs, then an icon link list (a social "linktree" inside the page).
- A two-dot control (filled ring and small dot), probably a theme or mode toggle.
- Bottom-anchored tab navigation with an underline indicator (2 px, aligned to the text width).

## 7. Motion
Measured: 8.92 s at 60 fps, motion fraction 0.11 (very still), not a loop. Segments:
- 0.03–0.13 s (0.1 s): the CRT powers on from black to UI between frames 0.50 and 1.49 s.
- 6.57–7.37 s (0.8 s, symmetric ease-in-out, peak 0.44): the zoom-through transition from the computer to the landing page.

From the frames:
- The screen content shifts subtly as the cursor approaches (2.48–5.45 s), as if the miniature site inside is scrolling or parallaxing.
- At 6.44 s the cursor is on "Click" and the screen darkens.
- By 7.43 s the full page is present.
- The prismatic glow fades in afterwards (absent at 7.43 s, present at 8.42 s), so it is staggered by about 0.5–1 s.

## 8. Brand system
n/a — not a brand system. Identity cues: a yellow retro computer as a personal mascot, a cool #f4f7ff paper and a single link blue, plus a casual voice ("matcha lattes or software").

## 9. UX
- **Strengths:** A memorable first impression; content is minimal and scannable; links are explicit URLs, which aids trust.
- **Risks:**
  - The gate adds a mandatory click and about 1 s before any content, which is costly for recruiters.
  - "Click" is small (about 90×40 px) inside the object.
  - There is no hint that the whole computer is clickable.
  - Keyboard and screen-reader access to the 3D gate is unknown.

## 10. Craft signals
- The CRT shows a miniature collage of the real site, previewing the destination.
- The canvas is a blue-tinted off-white (#f4f7ff), not #fff, which harmonises with the link blue.
- One link colour (#2b47c9) is used, with service glyphs tinted to match.
- The light direction is consistent: highlight top-left, shadow bottom-right.
- The rainbow glow arrives after the page settles (a staggered reveal).
- The footer label "Index" is letter-spaced while the tabs are not, giving a hierarchy of meta vs nav.

## 11. Reproduction recipe
```css
:root{--paper:#f4f7ff;--ink:#1a1c24;--body:#4a4d57;--link:#2b47c9;--yellow:#face38}
body{background:var(--paper);font:400 17px/1.6 "Inter",system-ui;color:var(--body)}
.bio{max-width:520px;margin:96px 0 0 31vw}
.bio h1{font:600 17px/1.3 "Inter";color:var(--ink)}
.links a{color:var(--link);text-decoration:none;display:flex;gap:10px;align-items:center}
.glow{position:fixed;inset:-40vh 0 auto;height:70vh;pointer-events:none;filter:blur(60px);opacity:0;
  background:conic-gradient(from 180deg at 50% 0%,#ffd9a0,#9ff0c0,#7fd8ff,#ff7aa8,#a0f0ff,#ffe0a0);
  -webkit-mask:radial-gradient(60% 100% at 50% 0,#000,transparent);animation:glow .9s .6s ease-out forwards}
@keyframes glow{to{opacity:.85}}
.gate{transition:transform .8s cubic-bezier(.45,0,.55,1),opacity .8s}
.gate.enter{transform:scale(8);opacity:0}  /* zoom through the CRT */
.tabs a[aria-current]{border-bottom:2px solid var(--ink)}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | A charming hero object, a calm page and a tasteful prismatic accent. |
| Originality | 8 | The computer-as-door entrance with a site preview in the CRT is a witty idea. |
| Usability | 6 | Good text and contrast, but the gate delays content and its affordance is small. |
| Craft | 7 | Consistent light and colour logic and a staggered reveal; the landing layout is somewhat generic. |

---
id: insp-portfolio-gameboy
source: inspora
category: Web
status: analyzed
title: "Portfolio Gameboy"
creator: "@Angaisb_"
styles: [skeuomorphic, retro-pixel, editorial-serif, physical-material]
patterns: [device-as-navigation, keyboard-mapped-controls-legend, pixel-menu-list, split-hero-three-column, status-dot-availability, handwritten-annotation-arrow, side-quest-card]
mode: light
palette: ["#eceee2", "#d5d7cd", "#a4b28a", "#2f3a22", "#6b6d62", "#2a2b26", "#9b2350", "#2c3a5c"]
type_families: ["condensed editorial serif, close to Instrument Serif / Editorial New Condensed (likely)", "geometric humanist sans, close to Manrope / DM Sans (likely)", "spaced mono caps (likely Space Mono / IBM Plex Mono)", "pixel font on LCD (Press Start-like, narrower)"]
type_class: [editorial-serif, humanist-sans, mono, pixel]
radius_px: [9999, 8, 40]
motion: {durations_s: [], easing: [step], loop: true}
scores: {aesthetics: 8, originality: 7, usability: 6, craft: 8}
craft_signals: [real-key-bindings-documented, lcd-tint-matches-page-tint, selected-row-inverted-pixel-bar, numbered-menu-items, availability-status-dot, serif-roman-italic-colour-split]
anti_patterns: [faint-meta-labels-fail-contrast, content-locked-in-tiny-lcd, ai-built-generic-persona]
---
# Portfolio Gameboy — @Angaisb_

## 1. Snapshot
- **Subject:** A 20 s, 2560×1440 capture of "pocketfolio.", a portfolio presented as a tilted, photoreal Game Boy-style handheld branded "pocket — portfolio system". Its dot-matrix LCD hosts the entire site (About me / Selected work / My toolkit / Say hello).
- **Context:** The post credits the build to an AI model ("GPT-6 Astra"), and the persona "Milo Bennett" is a demo name.
- **Why it's remarkable:** The device is the information architecture. The D-pad, A/B and Start buttons are the navigation, and a "How to play" legend maps each to a keyboard key, turning a gimmick into a documented control scheme.

## 2. Composition & layout
Key frame is ×1.28 to source.
- **Three columns over a warm off-white page:**
  - Left (x≈130): an eyebrow "01 THE POCKET EDITION", then a 2-line headline, a 3-line intro, the name/role and a scripted "Made to be explored." with a hand-drawn arrow pointing at the device.
  - Centre: the handheld, about 580×890 px, rotated about −4°. It is the hero and occupies about 30% of the width.
  - Right (x≈1540–1850): the "How to play" legend with 4 rows at an 80 px pitch, plus a "A little side quest?" card.
- **Header:** about 115 px tall with a 1 px rule. Wordmark at left, "AN INTERACTIVE PORTFOLIO" at centre, "● OPEN TO GOOD PROJECTS" at right.
- **Spacing:** generous. About 60% of the page is empty paper.

## 3. Typography
- **Headline:** about 85 px condensed serif with tight leading of about 1.05. "Small screen." is roman in near-black; "Big ideas." is italic in olive (#6b7a4f), a colour-and-style split.
- **Body:** intro and legend titles in a humanist sans at about 17 px with 1.8 leading. Legend subtitles are 13 px grey.
- **Meta:** "AN INTERACTIVE PORTFOLIO", "HOW TO PLAY", "LESS SCROLL. MORE PLAY." and "NO HIGH SCORE REQUIRED." are spaced mono caps at 10–11 px with +0.25 em tracking.
- **LCD:** a pixel font in caps. The name is about 2× size.
- **Script:** "Made to be explored." is an italic serif at about 26 px, rotated about −6°.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #eceee2 | page (warm green-grey paper) | 75% |
| #d5d7cd / #c6cbba | device shell, rules | 15% |
| #a4b28a | LCD green | 5% |
| #2f3a22 | LCD pixels | — |
| #6b6d62 | bezel grey, secondary text | 5% |
| #9b2350 | A/B buttons, bezel stripe | accent |
| #2c3a5c | "pocket" logo navy | accent |

WCAG checks:
- Ink #2a2b26 on paper is 12.16:1.
- The olive italic #6b7a4f is 3.96:1, which passes only because it is large.
- Legend subtitles (#8a8c82) are **2.91:1, fail**.
- The faintest mono notes (≈#b8bab0) are **1.67:1**.
- LCD pixels on green are 5.32:1.

The page tint #eceee2 is a desaturated cousin of the LCD green, so the device and the page belong together.

## 5. Depth & material
- **Shell:** an off-white plastic body with bevelled edges and a cut corner at the bottom-right (radius about 40 px, an authentic Game Boy reference).
- **Details:** recessed speaker grille slots and rubber Select/Start pills. The magenta A/B buttons have specular highlights. The D-pad is matte black with an embossed arrow mark.
- **Grounding:** a large soft shadow of about 60 px blur, offset down-right.
- **LCD:** an inset dark grey bezel with a "DOT MATRIX WITH PERSONALITY" label, a red battery LED, and a faint pixel-grid texture on the green.
- **The rest:** totally flat, with 1 px rules.

## 6. Components & patterns
- **LCD menu:** "PLAYER 01" with ♥♥♥ lives, an avatar sprite, and a numbered list 01–04. The selection is an inverted dark bar with a ▶ caret. A footer hint reads "A LITTLE CURIOUS? PRESS A."
- **Screens seen:** Splash (pocket loader), Main menu, About ("Off the clock"), Selected work ("Fieldnotes" project card with an [OPEN PROJECT] button), Toolkit (pixel bar charts), Say hello ("Let's make something good" with a [COPY EMAIL] button).
- **Toast:** at 16.66 s a toast appears at the bottom: "Copy this demo address…". This is copy-to-clipboard feedback.
- **Controls legend:** icon (D-pad / A / B / Start pill) plus title plus key mapping.
- **Availability chip:** a green dot plus mono caps.

## 7. Motion
Measured: 19.99 s at 60 fps, motion_fraction **0.03**, 0 segments above threshold, `seamless_loop_likely: true`.
- The page itself is static. All change happens inside the roughly 350×300 px LCD, which is too small an area to register as motion energy.
- From the 9 evenly spaced frames (~2.2 s apart): screen swaps are hard cuts (step transitions, period-appropriate), the menu caret jumps row to row, and button presses show as cursor-on-button with no visible scale.
- **Easing:** effectively `steps()`, no tweening. Authentic, but it gives no press feedback on the 3D buttons themselves (estimate).

## 8. Brand system
n/a — not a brand system, though it carries a mini-identity:
- the "pocketfolio." wordmark with a pixel-cluster mark;
- the "pocket — portfolio system" device logo in navy;
- game-voice microcopy ("Less scroll. More play.", "No high score required.", "A little side quest?").

## 9. UX
- **Strengths:**
  - The control mapping is explicit (arrow keys, Z, X, Enter).
  - Numbered menu items give orientation.
  - The availability status is above the fold.
  - The copy-email toast confirms the action.
- **Weaknesses:**
  - All real content lives in a roughly 350 px pixel screen, so case studies will be cramped.
  - Screen readers are unlikely to get the LCD text.
  - Meta and legend subtitles fail contrast.
  - Mobile would need the device to become full-screen.

## 10. Critical craft signals
- The LCD green (#a4b28a) and the page (#eceee2) share hue, and so does the olive italic headline (#6b7a4f).
- The headline splits roman/ink from italic/olive across its two sentences.
- The legend icons literally redraw the device's controls (cross, A circle, B circle, Start pill).
- The selected menu row uses full-width inverse video plus a ▶ caret plus a right-aligned number "02".
- A small "01" boxed index precedes "THE POCKET EDITION", the editorial edition numbering.
- The device is rotated about −4° while all text stays orthogonal. Only the playful object tilts.

## 11. Reproduction recipe
```css
:root{--paper:#eceee2;--shell:#d5d7cd;--lcd:#a4b28a;--pix:#2f3a22;--ink:#2a2b26;--olive:#6b7a4f;
  --muted:#6e7066;--berry:#9b2350;--navy:#2c3a5c;
  --serif:"Instrument Serif",serif;--sans:"DM Sans",system-ui,sans-serif;--mono:"Space Mono",monospace;--pixel:"Silkscreen","Press Start 2P",monospace}
body{background:var(--paper);color:var(--ink);font:400 17px/1.8 var(--sans)}
h1{font:400 85px/1.02 var(--serif);letter-spacing:-.02em} h1 em{color:var(--olive)}
.meta{font:400 11px var(--mono);letter-spacing:.25em;text-transform:uppercase;color:var(--muted)}
.device{width:580px;aspect-ratio:.65;background:var(--shell);border-radius:14px 14px 80px 14px;transform:rotate(-4deg);
  box-shadow:inset 0 2px 0 #fff,inset 0 -6px 12px rgb(0 0 0/.08),30px 40px 60px rgb(0 0 0/.12)}
.lcd{background:var(--lcd);color:var(--pix);font:12px/1.9 var(--pixel);
  background-image:linear-gradient(rgb(0 0 0/.04) 1px,transparent 1px),linear-gradient(90deg,rgb(0 0 0/.04) 1px,transparent 1px);background-size:3px 3px}
.lcd [aria-selected=true]{background:var(--pix);color:var(--lcd)}
.btn-ab{width:64px;aspect-ratio:1;border-radius:50%;background:radial-gradient(circle at 35% 30%,#c4467a,var(--berry) 60%)}
.btn-ab:active{transform:translateY(2px) scale(.97)}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | A cohesive green-paper palette, a lovely device render and a refined serif/mono pairing. |
| Originality | 7 | Device-as-portfolio is known (Game Boy and iPod sites), but the documented key legend and editorial framing are well done. |
| Usability | 6 | Explicit controls and feedback, but content is trapped in a tiny screen and meta text fails contrast. |
| Craft | 8 | Hue-matched LCD, a consistent control iconography and edition numbering. Buttons lack visible press states. |

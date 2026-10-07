---
id: insp-1-57
source: inspora
category: Web
status: analyzed
title: "404 page"
creator: "@dqnamo"
styles: [skeuomorphic, soft-3d, retro-pixel, playful-rounded]
patterns: [interactive-handheld-console, drag-cartridge-to-slot, loading-progress-bar, used-item-desaturates, component-showcase-with-code-tabs, keyboard-key-labelled-dpad]
mode: light
palette: ["#fcfcfc", "#f0f0f0", "#3a3f43", "#212429", "#0b110d", "#75756f", "#dedede", "#e5452f"]
type_families: ["Inter (likely)", "pixel/mono for in-screen HUD (likely Geist Mono / JetBrains Mono)"]
type_class: [neo-grotesk, mono]
radius_px: [48, 22, 14, 10]
motion: {durations_s: [0.1], easing: [ease-out], loop: true}
scores: {aesthetics: 8, originality: 8, usability: 7, craft: 9}
craft_signals: [inserted-cartridge-greys-out-in-tray, cartridge-peeks-from-top-slot, dpad-keys-map-to-wasd, crt-green-phosphor-hud, speaker-grille-dot-array, model-number-pa-03-microtype]
anti_patterns: [title-mismatch-no-404-visible, red-button-label-under-aa, hud-hint-text-tiny]
---
# 404 page — @dqnamo

## 1. Snapshot
- **Subject:** A 21.4 s, 3840×2160 (2× retina, about 1920 CSS) recording of a "Pocket Arcade" component: a charcoal handheld console with three tilted game cartridges around it. Clicking or dropping a cartridge loads it ("READING MODULE" plus a progress bar) and the game becomes playable.
- **Note:** The post title and description call it a 404 page, but no "404" or error copy is visible in any of the 9 frames. The recording shows the component in a code-showcase page (tabs PocketArcade.tsx / game-engine.ts / styles.css / Usage.tsx).
- **Why it's remarkable:** It is real tactile skeuomorphism in CSS. The active cartridge physically sits in the top slot, and its tray copy desaturates to grey to show it is "in use".

## 2. Composition & layout
- **Page:** a left-aligned intro (title plus a 3-line description, about 15 CSS px, max-width about 480 CSS) at the top. Below it is a large showcase panel (about 970×1000 CSS, #f0f0f0-ish border, radius about 14) with a code-tab bar at the bottom.
- **Console:** about 395×610 CSS px, centred, radius about 48.
  - a screen bezel of about 345×310 CSS;
  - a branding strip "POCKET ARCADE · PA-03";
  - a D-pad with keys W/A/S/D on the left;
  - a red action key on the right;
  - "INTERFACE LONDON" microtype and a 2×6 speaker-dot grille at the bottom.
- **Cartridges:** about 140 CSS square, scattered asymmetrically at −8° to +6° rotations: two on the left, one on the right, plus one in the slot.

## 3. Typography
- **Page:** Inter at about 15 px. The title is medium #1a1a1a and the description is #75756f.
- **Console branding:** "POCKET" is an italic bold grotesk at about 10 px, followed by small-caps "ARCADE" in tracked caps at about 7 px. These are hardware-label cues.
- **In-screen HUD:** a small sans/mono at about 11 px in phosphor grey-green ("Brick Stack", score "00000", "Lines 0"). Hints ("Space Rotate", "↓ Drop") are at about 8 px.
- **Code tabs:** mono at about 13 px. The active tab has a #f0f0f0 pill fill.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #fcfcfc / #f0f0f0 | page and showcase panel | 83% |
| #3a3f43 / #212429 | console shell, key caps | 7.5% |
| #0b110d | screen (green-black phosphor) | 3.8% |
| #75756f | secondary text | 1.6% |
| #dedede | key glyphs, borders | 1.6% |
| #e5452f | action button | <1% |
| cartridge art | saturated pixel-art labels (red/yellow/green/navy) | — |

WCAG checks:
- Page title #1a1a1a on #fcfcfc is 17.0:1.
- Description #75756f is 4.52:1 (borderline pass).
- HUD #c6c6c6 on #0b110d is 11.2:1.
- Dim green playfield lines (≈#3f6b48) are 3.1:1.
- Key glyphs #dedede on #3a3f43 are 7.9:1.
- Shell microtype (≈#8a8f93) is 3.26:1.
- White on the red key (#e5452f) is 4.02:1.

## 5. Depth & material
- **Shell:** matte plastic, with a soft long drop shadow (about 0 30px 60px rgba(0,0,0,.25)), an inner top highlight and a darker inset screen bezel.
- **Keys:** raised caps with a 2–3 px bottom edge. The red key has a darker lower lip (#b3321f-ish), which reads as pressable.
- **Cartridges:** a thick label inset, a gold-pin connector strip at the bottom edge (yellow tick pattern) and individual drop shadows matching their rotation.
- **Screen:** a near-black green with a subtle inner vignette, like a CRT/LCD.

## 6. Components & patterns
- A cartridge picker as physical objects, using drag or click to insert.
- A loading state ("READING MODULE" plus a 70 px progress bar).
- Three playable mini-games: Night Patrol (space invaders), Brick Stack (Tetris), Garden Snake.
- A D-pad that shows keyboard equivalents (W/A/S/D) and an action key mapped to Space.
- A component docs frame with file tabs and a "Copy" button.

## 7. Motion
- **Measured:** 21.39 s at 29.97 fps. motion_fraction is 0.01, mean energy 0.03, and there are only two 0.10 s ease-out spikes (1.13 s and 9.04 s, the cartridge-swap moments). The detector flags it as a seamless loop.
- Game motion (invaders, falling blocks, snake) is tiny relative to the 4K frame, so it stays under threshold.
- **Frame evidence:**
  - Night Patrol loads at t=1.19 s, playing by 3.56 s.
  - Brick Stack is inserted by 10.69 s (its tray card turns grey).
  - Garden Snake loads at 15.45 s ("READING MODULE" again).
- The swaps themselves are fast (≤0.1 s at the sample rate), i.e. snappy ease-out, not floaty.

## 8. Brand system
n/a — not a brand system. Identity cues:
- the "POCKET ARCADE PA-03" hardware branding;
- the "INTERFACE LONDON" maker's mark;
- the cartridge label art as mini-brands.

## 9. UX
- **Affordances:** objects look grabbable, keys show their keyboard mapping, and the in-use state is explicit through desaturation. Loading feedback is present.
- As a 404 page it would be a delightful distraction, but this capture shows no error message or way-home link, so its 404 function can't be verified.
- **Risks:** tiny HUD hints and low-contrast shell microtype.

## 10. Craft signals
- The inserted cartridge peeks about 40 px out of the top slot, showing the same label art as the one greyed out in the tray.
- D-pad caps are labelled W/A/S/D, teaching the controls without any instructions.
- The tilts differ per cartridge (about −8°, +4°, +6°), and each shadow follows its own rotation.
- The speaker is a 2×6 dot grid aligned to the screen's right edge.
- Model-number microtype "PA-03" is right-aligned to the screen bezel.
- The playfield uses a thin green border on the near-black screen, which evokes phosphor without heavy scanlines.

## 11. Reproduction recipe
```css
:root{--page:#fcfcfc;--shell:#3a3f43;--shell-d:#212429;--screen:#0b110d;--key:#dedede;--action:#e5452f}
.console{width:395px;height:610px;border-radius:48px;background:linear-gradient(#41464a,var(--shell));
  box-shadow:inset 0 2px 0 rgba(255,255,255,.08),0 30px 60px rgba(0,0,0,.25)}
.screen{margin:22px;height:310px;border-radius:22px;background:var(--shell-d);padding:10px}
.screen > .lcd{height:100%;border-radius:10px;background:var(--screen);box-shadow:inset 0 0 40px rgba(0,0,0,.6);
  font:500 11px/1.2 "Geist Mono",monospace;color:#c6c6c6}
.key{width:30px;height:30px;border-radius:6px;background:var(--shell-d);color:var(--key);
  box-shadow:0 2px 0 #15171a;font:600 11px Inter}
.action{width:56px;height:56px;border-radius:14px;background:var(--action);box-shadow:0 4px 0 #b3321f}
.action:active{transform:translateY(3px);box-shadow:0 1px 0 #b3321f}
.cart{width:140px;aspect-ratio:1;border-radius:14px;transform:rotate(var(--tilt));box-shadow:0 12px 20px rgba(0,0,0,.25)}
.cart[data-inserted]{filter:grayscale(1) opacity(.7)}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | A charming, credible hardware render against a clean docs page. |
| Originality | 8 | A playable cartridge console as a web component (and a 404 page) is an inventive idea. |
| Usability | 7 | Excellent affordances. Small HUD text, and no visible 404 messaging. |
| Craft | 9 | Desaturating the used cartridge, labelled keys and per-object shadows show care. |

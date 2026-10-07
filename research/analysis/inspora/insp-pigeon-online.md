---
id: insp-pigeon-online
source: inspora
category: Illustration
status: analyzed
title: "pigeon online"
creator: "@maiko_pixel"
styles: [retro-pixel, x-pixel-scene, playful-rounded]
patterns: [over-the-shoulder-scene, window-stack-cycling, low-fps-pixel-loop, screen-as-light-source, sticky-note-props]
mode: dark
palette: ["#040613", "#26262d", "#38373b", "#5b5c7b", "#1449d0", "#8b847b", "#5b3d3c", "#253666"]
type_families: ["hand-pixelled lettering (custom)"]
type_class: [pixel]
radius_px: []
motion: {durations_s: [0.7, 0.7, 2.1], easing: [steps], loop: true}
scores: {aesthetics: 8, originality: 8, usability: 6, craft: 8}
craft_signals: [screen-blue-as-only-saturated-field, limited-ramp-shading, sticky-note-color-coding, low-fps-intentional, pigeon-themed-ui-jokes]
anti_patterns: [loop-not-seamless]
---
# pigeon online — @maiko_pixel

## 1. Snapshot
- **Subject:** An 896×896 pixel-art loop lasting 2.1 s at 7.14 fps. Seen over the shoulder, a pigeon sits at a beige 90s CRT PC whose blue desktop keeps popping new windows: dove pictures, a "Burger" ad, a flower, a rain app, a coffee cup, and Solitaire.
- **Why it's remarkable:** The screen is the only saturated, lit area in a night-time scene. The windows are bird-themed parodies of OS content, told through a rapid window-stack cycle.

## 2. Composition & layout
- **Pixel grid:** about 7 px per art pixel, so the effective canvas is about 128×128.
- **Monitor:** fills the left 55% (x≈0→480, y≈60→560). The CRT screen area is x≈0→440, y≈145→530, cropped by the left frame edge, which brings the viewer into the scene.
- **Tower PC:** right of the monitor (x≈480→780), with a second small pigeon perched on top at (600,40).
- **Main pigeon:** foreground, bottom-right (x≈470→896, y≈455→896). It occupies about 20% of the frame. Its head and eye at (590,515) point at the screen, which leads the gaze.
- **Props:** sticky notes in yellow, orange, green and blue on the bezel and tower, plus a pink note with a heart below the screen.
- **Keyboard:** foreground bottom-left, in near-black.

## 3. Typography
- Hand-pixelled lettering only:
  - "Burger" in a yellow script-like pixel face, about 50 px tall on screen;
  - a small "zoo"-style logo on the monitor chin;
  - squiggles in the weather window.
- No system font is used. The text is decorative and illegible by design, since sticky notes carry dashes, not words.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #040613 | night background, deep shadow | 21% |
| #26262d / #38373b / #141114 | PC casing, keyboard, desk | about 38% |
| #5b5c7b | pigeon body (lit by screen) | 15% |
| #1449d0 | screen desktop blue | 8% |
| #253666 | screen edge / glow | 3% |
| #8b847b | beige bezel highlight | 5% |
| #5b3d3c | desk / mousepad | 5% |
| Accents (yellow, orange, green, pink) | sticky notes, icons | small amounts |

Contrast: not a text UI. Luminance hierarchy runs screen blue (#1449d0) → pigeon lavender (#5b5c7b) → casing (#26262d) → background (#040613). The brightest pixels are the window contents.

## 5. Depth & material
- **Shading:** limited ramps of 3–4 tones per material: beige plastic, black plastic, lavender feathers.
- **Lighting:** The screen glow is implied by a lighter rim on the pigeon's chest and the tower's left edge. There is no gradient; it is done with stepped tones.
- **Depth:** The back wall is near-black with no detail, which pushes all depth into the foreground objects.

## 6. Components & patterns
Parodied OS UI:
- a desktop icon column on the left of the screen (bread, colourful ball, fish, "M"-like fries icon);
- top-right tray icons (apple, fish);
- stacked windows with title bars;
- a full-window Solitaire at t=1.75 s;
- a "Burger" ad pop-up featuring a pigeon (an in-world banner ad).

## 7. Motion
- **Measured:** 2.1 s at 7.14 fps (about 15 frames). Two motion segments: 0.00–0.70 s and 1.12–1.82 s, each 0.70 s with `peak_at` 0.90 (ease-in: energy ramps up to a pop). `motion_fraction` 0.69. `seamless_loop_likely: false` (first/last difference 4.66).
- **Observed sequence:**
  1. Dove windows multiply (0.12→0.35 s).
  2. The Burger ad pops over them (0.58–1.05 s).
  3. Flower and rain windows replace it (1.28 s).
  4. A coffee window is added (1.52 s).
  5. Solitaire goes full-window (1.75 s).
  6. Back to flower/rain/coffee (1.98 s).
- **Behaviour:** Windows appear instantly (hard cuts, no tween), which is appropriate for pixel art and retro OS behaviour. The pigeon itself barely moves; only its eye glint shifts by 1 art pixel.
- **Rhythm:** about one window event per 0.23 s (every 2 frames at 7 fps), which gives a frantic channel-surfing rhythm.

## 8. Brand system
n/a — not a brand system. Identity cues: the creator's consistent pigeon character and a night-time indigo palette with one glowing screen.

## 9. UX
- As a narrative loop it is legible at small sizes: the screen is the brightest patch and the pigeon's beak points at it.
- The loop is not seamless (it ends on a different window stack than it starts), so it reads as a jump when repeated.

## 10. Craft signals
- The screen blue (#1449d0) is the only saturated large field. Everything else sits below about 35% luminance.
- Every material uses at most 4 tones, and there are no anti-aliased gradients.
- Sticky-note colours (yellow, orange, green, blue, pink) are the only accents. They are distributed around the screen frame and balance the composition.
- The window content is semantically themed (doves, a burger ad starring a pigeon, Solitaire). The joke survives at about 128 px resolution.
- A low frame rate (7 fps) suits the pixel medium and reduces visual noise.

## 11. Reproduction recipe
```css
:root{--night:#040613;--case:#26262d;--case-2:#38373b;--bird:#5b5c7b;--screen:#1449d0;--bezel:#8b847b}
.scene{width:128px;height:128px;transform:scale(7);transform-origin:0 0;image-rendering:pixelated;background:var(--night)}
.win{position:absolute;visibility:hidden}
.win:nth-child(n){animation:pop 2.1s steps(1,end) infinite}
@keyframes pop{0%{visibility:hidden}10%{visibility:visible}100%{visibility:visible}}
/* stagger with animation-delay: 0s, .23s, .46s, .7s … */
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | A disciplined night palette with one glowing screen; charming. |
| Originality | 8 | The pigeon-themed OS parody is a fresh, witty idea. |
| Usability | 6 | Reads well, but the loop seam is visible. |
| Craft | 8 | Clean tonal ramps, coherent pixel grid, and well-paced cuts. |

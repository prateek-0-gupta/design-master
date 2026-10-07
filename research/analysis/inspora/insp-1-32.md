---
id: insp-1-32
source: inspora
category: Illustration
status: analyzed
title: "Mechanical keyboard for iphone"
creator: "@LynelDesign"
styles: [skeuomorphic, soft-3d, physical-material, playful-rounded]
patterns: [keycap-two-tier-bevel, ios-keyboard-reskin, accent-return-key, predictive-bar, device-closeup-perspective]
mode: light
palette: ["#f6f6f6", "#dee1e7", "#f8f8f8", "#3a3a3a", "#369efa", "#6a6f94", "#919fa7", "#000000"]
type_families: ["SF Pro Text (likely)"]
type_class: [neo-grotesk]
radius_px: [256, 100, 28, 18]
motion: null
scores: {aesthetics: 8, originality: 7, usability: 7, craft: 8}
craft_signals: [inset-dished-top-face, base-shadow-offset-down, return-key-same-geometry-in-colour, bottom-radius-matches-device-corner, stagger-preserved-from-ios, perspective-shot-proves-3d]
anti_patterns: [white-on-blue-below-aa, keycap-height-reduces-glyph-area]
---
# Mechanical keyboard for iphone — @LynelDesign

## 1. Snapshot
- **Subject:** The iOS QWERTY keyboard re-rendered with chunky, two-tier mechanical keycaps. Two 2560×2560 slides: a flat front view, and an angled close-up of the keyboard inside a pale-blue iPhone frame.
- **Why it's remarkable:** It keeps Apple's exact layout, glyphs and predictive bar, and changes only the key material. The layout stays fully familiar while the feel changes completely.

## 2. Composition & layout
- **Slide 1:** the keyboard panel (~1376×1170 px) sits centred on a #f6f6f6 field with ~600 px margins.
- **Panel corners:** the top corners are ~100 px. The bottom corners are much larger (~256 px), mirroring the iPhone display corner, which is how the key panel sits at the bottom of a real device.
- **Keys:**
  - Letter keys are ~122×173 px with ~10 px gaps.
  - Row 2 is inset by half a key, as on iOS.
  - Shift and delete keys are ~190 px wide.
  - The bottom row is ABC (~310 px), space (~680 px) and return (~315 px).
- A predictive bar of three equal columns ("The" / the / to) sits above. The emoji and mic icons sit in a ~250 px bottom band.
- **Slide 2:** a roughly 20° rotated perspective close-up with the phone's metallic frame, black bezel and speaker grille. It proves the caps have real height.

## 3. Typography
- SF Pro Text-style neo-grotesk, Regular. Glyphs are ~64 px x-height on 173 px keys.
- Key legends are #3a3a3a, not black. Predictive words are black at ~56 px. "ABC" uses caps at ~50 px.
- **Icons:** SF Symbols-style shift, delete and return at a ~5 px stroke. Emoji and mic are in a muted violet-grey (#6a6f94).

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #f6f6f6 | page background | 83% |
| #dee1e7 | keyboard tray (cool grey) | 14% |
| #f8f8f8 → #f3f3f3 | keycap top face / skirt | (inside tray) |
| #bfc3c8 | keycap base shadow | 1.7% |
| #3a3a3a | legends | — |
| #369efa | return key | 1.2% |
| #6a6f94 | emoji / mic icons | — |
| #919fa7 | device frame (slide 2) | 4.5% |

WCAG:
- Legends #3a3a3a on #f7f7f7 are 10.62:1.
- Predictive words in black on #dee1e7 are 16.03:1.
- The icons #6a6f94 on #dee1e7 are 3.72:1 (large/graphic pass only).
- The white return glyph on #369efa is **2.83:1 (fails 3:1 for graphics)**.

## 5. Depth & material
- Each key has **two tiers**: an outer skirt (#f3f3f3) and an inner dished top face (#f8f8f8) inset ~19 px with an ~18 px radius. The skirt's outer radius is ~28 px.
- A tight drop shadow (~4 px offset down, ~6 px blur, #bfc3c8) creates a crisp base line, with a soft ambient shadow around it.
- Light comes from the top: the upper skirt is brighter and the lower skirt slightly darker.
- **Return key:** the same geometry in blue, with a lighter top face (#3aa0f8) over a darker skirt (#2b8ff0).
- **Device (slide 2):** a satin aluminium frame with a specular streak, and antenna lines as lighter grey bands.

## 6. Components & patterns
- Standard iOS keyboard IA: predictive bar, three letter rows, a modifier row, and an emoji/dictation band.
- The primary action (return) is the only coloured key. On iOS that would be a contextual "Go/Send" key, so the accent signals the primary action.
- The space bar has no legend and is defined only by its long dished top.

## 7. Motion
None: still images. The two-tier cap implies a press state in which the top face shifts down 4 px and the shadow collapses, but this is not shown.

## 8. Brand system
n/a — not a brand system. It is an Apple-ecosystem pastiche (SF type, iPhone frame, iOS blue).

## 9. UX
- **Strengths:** The layout is fully conventional, so there is zero learning cost. Legends are high-contrast, and the big caps make the hit area visible.
- **Risks:**
  - The bevel eats about 22% of each key's width, which reduces glyph area.
  - The return glyph contrast is low.
  - The heavy chrome adds visual noise while typing, a familiar trade-off of skeuomorphic keyboards.

## 10. Craft signals
- The keycap top face is inset by a constant ~19 px on every key, including wide keys and space.
- The panel's bottom radius (~256 px) differs from its top radius (~100 px) to match the device corner.
- The return key reuses the exact two-tier geometry in blue instead of a flat fill.
- Legends are #3a3a3a rather than #000, which softens them against near-white caps.
- The half-key stagger of row 2 and the wide shift/delete keys are kept from native iOS.
- The perspective slide shows a consistent shadow direction (down) at an angle.

## 11. Reproduction recipe
```css
:root{--page:#f6f6f6;--tray:#dee1e7;--cap-skirt:#f1f1f1;--cap-top:#f9f9f9;--legend:#3a3a3a;--accent:#2b8ff0;--accent-top:#3aa0f8}
.tray{background:var(--tray);border-radius:100px 100px 256px 256px;padding:24px 20px}
.key{position:relative;height:173px;border-radius:28px;background:var(--cap-skirt);
  box-shadow:0 4px 0 #c4c8cd,0 8px 14px rgba(0,0,0,.08);color:var(--legend);font:400 64px/1 "SF Pro Text",system-ui}
.key::before{content:"";position:absolute;inset:14px 19px 24px;border-radius:18px;
  background:linear-gradient(#fbfbfb,#f4f4f4);box-shadow:inset 0 2px 3px rgba(0,0,0,.05)}
.key:active{transform:translateY(4px);box-shadow:0 0 0 #c4c8cd,0 2px 4px rgba(0,0,0,.08)}
.key.primary{background:var(--accent);box-shadow:0 4px 0 #1f6fc0}
.key.primary::before{background:var(--accent-top)}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Soft, cohesive cool-grey material with one blue accent. Charming and tidy. |
| Originality | 7 | Mechanical-keycap reskins exist, but keeping the exact iOS IA is a sharp constraint. |
| Usability | 7 | Familiar layout and high legend contrast. The bevel shrinks glyph area and the return glyph is low contrast. |
| Craft | 8 | Constant insets, a device-matched radius and a consistent shadow direction across both views. |

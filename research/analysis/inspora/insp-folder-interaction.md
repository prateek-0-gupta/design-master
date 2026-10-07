---
id: insp-folder-interaction
source: inspora
category: Motion
status: analyzed
title: "folder interaction"
creator: "@shedsgns"
styles: [soft-3d, glassmorphism, micro-interaction, playful-rounded]
patterns: [context-menu-create, inline-rename-on-object, color-swatch-picker, freehand-sticker-annotation, glossy-folder-icon, object-centric-editing]
mode: light
palette: ["#e7e7e7", "#eeeeee", "#4a4a4a", "#558fef", "#77adfa", "#9cc3fa", "#d94fe0", "#ffffff"]
type_families: ["SF Pro Text (likely)"]
type_class: [neo-grotesk]
radius_px: [36, 58, 9999]
motion: {durations_s: [0.13], easing: [ease-in-out], loop: false}
scores: {aesthetics: 8, originality: 7, usability: 6, craft: 8}
craft_signals: [inner-glow-pocket-gradient, white-paper-sheet-peek, swatches-with-own-gloss, outline-text-field-on-object, soft-coloured-halo-shadow, menu-divider-before-info]
anti_patterns: [white-label-on-light-blue-fails-contrast, swatches-unlabelled]
---
# folder interaction — @shedsgns

## 1. Snapshot
- **Subject:** A 10.9 s, 2880×2880 square recording on a flat grey canvas. A three-item context menu creates "New folder 65" as a large glossy folder. The user then switches its colour with a four-dot swatch row, renames it in place to "@shedsgns" and doodles a heart on the front.
- **Why it's remarkable:** Every edit happens *on the object itself*: the label is a text field printed on the folder's pocket, and the swatches hang directly below it. There is no inspector panel and no dialog.

## 2. Composition & layout
- Square canvas, #e7e7e7, with everything dead-centre.
- **Context menu** (t≈0.6 s): about 820×520 px, radius ≈36 px. It holds three rows of about 165 px with a hairline divider separating "Get info" from the two creation actions.
- **Folder:** about 893×713 px (x≈948–1840, y≈1034–1747 real). The tab occupies the left 35% of the width.
- **Swatch row:** four dots of about 55 px with about 72 px pitch, centred about 105 px below the folder's bottom edge.
- **Label:** centred about 70% of the way down the front pocket.

## 3. Typography
- One SF Pro-style neo-grotesk.
- **Menu items:** about 79 px real (≈26 pt at 3×), regular, #4a4a4a, with 1.5 px-stroke outline icons (folder, doc, info-circle) at a 30 px gap.
- **Folder label:** about 70 px medium white. In edit mode it gets a 1.5 px translucent-white outline box (radius ≈8 px) and a text caret.
- The handwritten heart is a single white stroke of about 6 px with round caps. It is the only non-type mark, deliberately loose against the precise sans.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #e7e7e7 | canvas | 92% |
| #eeeeee | menu surface | — |
| #4a4a4a | menu text and icons | — |
| #558fef → #9cc3fa | folder back (deep) → pocket highlight | 6% |
| #ffffff | paper insert, label | <1% |
| #d94fe0 | magenta folder variant | (t≈4.2 s) |
| swatches | orange ≈#f06020, green ≈#4cd964, blue #4a8ff0, magenta #e040e0 | <1% |

WCAG checks:
- Menu #4a4a4a on #eeeeee is 7.64:1.
- The white label on the pocket fails. It is 2.3:1 on the mid pocket (#77adfa) and 1.81:1 on the highlight (#9cc3fa). On the deepest blue (#558fef) it reaches 3.2:1, and on magenta 3.42:1. These pass only for large text.

## 5. Depth & material
- The folder is soft-3D "jelly glass".
- The back panel is a saturated blue with a 2 px lighter rim.
- A white paper sheet (radius ≈12 px) peeks out between the back and the front.
- The front pocket has a vertical gradient (light top, more saturated middle) plus inner glows on the left and right edges, which reads as a thick translucent material. It also has a light 2 px top rim.
- **Shadow:** a wide, very soft halo (blur about 120 px, low opacity) tinted with the folder colour rather than black.
- Swatches carry their own tiny top highlight, a miniature of the same material.

## 6. Components & patterns
- **Context menu:** icon plus label rows, and a divider grouping create versus inspect.
- **Swatch picker:** four circular buttons. Selection is shown only by the folder changing colour; there is no ring on the active swatch.
- **Inline rename:** clicking the label converts it into an outlined field with a caret, and the user types directly.
- **Freehand sticker:** a hand-drawn heart is drawn top-right on the pocket and persists as decoration.

## 7. Motion
Measured: 60 fps, 10.9 s. The detector found `motion_fraction` 0.01 and a single 0.13 s symmetric segment at 1.63–1.77 s, which is the menu dismissing as the folder appears.

The other changes cover too small a fraction of the 8.3 MP frame to cross the 0.35 threshold. These are the colour swap (≈4.2 s), typing (≈5.4–6.6 s) and the heart stroke (≈6.7–7.9 s). From the frames, they look like quick crossfades of about 0.2 s (estimate). The heart appears to be revealed stroke-by-stroke, following the pointer. Between 9.1 s and 10.3 s the heart disappears again, an undo or reset; it is not a loop (`seamless_loop_likely` false).

## 8. Brand system
n/a — not a brand system. The creator's handle appears as the folder name, a self-signature.

## 9. UX
- **Strengths:**
  - Very low indirection: create, colour, name and decorate without leaving the object.
  - The swatches sit close to their target.
- **Risks:**
  - The white label on a light pocket is under 2.5:1.
  - The swatches have no accessible names and no selected ring.
  - The heart doodle has no visible tool affordance, so it is unclear how a user starts drawing.
  - The menu lacks keyboard hints.

## 10. Craft signals
- The shadow is tinted with the folder hue, not grey.
- A white paper insert (radius ≈12 px) sits behind the pocket and adds a layer.
- The pocket's inner edge glows are on the left and right only, so the material reads as thick.
- The swatches repeat the folder's gloss highlight at small scale.
- The edit-mode field is a 1.5 px translucent outline that does not break the object's surface.
- The menu divider separates "create" from "info".
- The two radii are consistent: about 36 px on the menu and about 58 px on the folder front.

## 11. Reproduction recipe
```css
:root{--canvas:#e7e7e7;--menu:#eeeeee;--ink:#4a4a4a;--f-deep:#558fef;--f-mid:#77adfa;--f-hi:#cfdef5;--r-menu:12px;--r-folder:20px}
.menu{background:var(--menu);border-radius:var(--r-menu);padding:6px;box-shadow:0 1px 2px rgb(0 0 0/.08),0 8px 24px rgb(0 0 0/.06);font:400 15px/1 -apple-system,"Inter",sans-serif;color:var(--ink)}
.menu hr{border:0;border-top:1px solid rgb(0 0 0/.06);margin:4px}
.folder{position:relative;width:300px;aspect-ratio:1.25}
.folder .back{position:absolute;inset:0;border-radius:var(--r-folder);background:var(--f-deep);clip-path:path("…tab shape…")}
.folder .front{position:absolute;inset:22% 0 0;border-radius:var(--r-folder);
  background:linear-gradient(180deg,var(--f-hi) 0%,var(--f-mid) 55%,#8fb6f8 100%);
  box-shadow:inset 0 2px 0 rgb(255 255 255/.5),inset 18px 0 24px -12px var(--f-deep),inset -18px 0 24px -12px var(--f-deep),
             0 30px 60px -20px color-mix(in srgb,var(--f-deep) 45%,transparent)}
.folder .label{color:#fff;font-weight:500;font-size:22px;text-shadow:0 1px 2px rgb(0 0 0/.15)}
.folder .label:focus{outline:1.5px solid rgb(255 255 255/.6);border-radius:4px}
.swatch{width:18px;height:18px;border-radius:9999px;box-shadow:inset 0 1px 1px rgb(255 255 255/.5),0 1px 2px rgb(0 0 0/.2)}
.front,.back{transition:background-color .2s ease}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Lovely jelly-glass folder on a quiet grey stage with a tight palette. |
| Originality | 7 | Object-centric editing plus a doodle sticker is a fresh, playful take on a Finder idiom. |
| Usability | 6 | Fast flow, but the label contrast fails and the swatches and drawing tool lack clear affordances. |
| Craft | 8 | Tinted shadows, a paper insert and consistent material across the swatches. |

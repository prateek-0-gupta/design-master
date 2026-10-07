---
id: insp-9-4
source: inspora
category: Motion
status: analyzed
title: "toss your note to the bin"
creator: "@proskuaaa"
styles: [skeuomorphic, physical-material, micro-interaction, corporate-clean]
patterns: [destructive-action-as-gesture, crumple-transition, pull-to-aim, sticky-note-card, colour-swatch-picker, bottom-sheet-settings, action-tile-row, exit-sign-back-button]
mode: light
palette: ["#ffffff", "#f3f4f6", "#fad78b", "#f1c87b", "#9d9fa0", "#000000", "#22d14b", "#f9c0c6"]
type_families: ["SF Pro Text / Display (likely)", "SF Pro Rounded-like semibold for note body (likely)"]
type_class: [neo-grotesk]
radius_px: [24, 20, 16, 9999]
motion: {durations_s: [0.1, 0.83, 0.37, 0.2, 0.33], easing: [ease-out, ease-in, ease-in-out], loop: false}
scores: {aesthetics: 7, originality: 9, usability: 6, craft: 7}
craft_signals: [note-tilted-2deg, swatch-ring-selected-state, crumple-keeps-note-colour, concentric-aim-arcs, photoreal-bin-from-mac-trash, exit-sign-as-back-affordance, horizontal-chip-overflow-cue]
anti_patterns: [hint-text-low-contrast, gesture-only-destructive-action, no-visible-undo]
---
# toss your note to the bin — @proskuaaa

## 1. Snapshot
- **Subject:** A 10.2 s, 1920×1920 iPhone mockup of a shopping-list notes app. A pink sticky note is recoloured yellow, "Toss" is tapped, the note crumples into a paper ball, the user pulls down to aim, the ball is flung into a wire-mesh bin, and the app returns to a "Sunday Brunch Prep" grid.
- **Why it's remarkable:** Deleting is turned into a physical game, crumple then pull-to-aim then throw, using skeuomorphic objects (a photoreal mesh bin and a crumpled paper ball) inside an otherwise flat iOS UI.

## 2. Composition & layout
- **Phone and editor screen:** The phone is centred at about 860 px wide, roughly 2.2× a 393 pt iPhone. On the editor screen the note card takes the upper 45%: about 480×470 px (at 1600-px frame scale) and rotated about −2°, with a 24 pt-ish radius.
- **Settings sheet:** The bottom 45% is a light-grey sheet (#f3f4f6) with three labelled groups (Note color, Category, Collaboration) and a row of four equal action tiles (Copy link / Share / Draw / Toss).
- **Toss screen:** The bin sits centred at the top third (about 270 px wide in the 1920 key frame) and the ball at the lower third (about 350 px). A hint, "Pull down to aim your toss", plus an arrow sits at y≈1640. The vertical axis between the ball and the bin is the throw line.
- **Final screen:** a two-column product card grid with a pinned voice-memo row and a search pill plus sort and add icons at the bottom.

## 3. Typography
- System iOS type (SF Pro). Labels in the sheet are about 13 pt Regular grey ("Note color"), chips about 15 pt Regular black and tile captions about 13 pt Medium.
- **Note body:** about 17 pt Semibold near-black with tight 1.2 leading, rotated with the card so the text tilts too.
- **Final screen:** the title "Sunday Brunch Prep" is about 17 pt Semibold centred, with a 11 pt grey meta line ("14 pieces | 2 days ago").

## 4. Colour
| Hex | Role | Approx share |
|---|---|---|
| #ffffff | screen and canvas | 88% |
| #f3f4f6 | settings sheet surface | ~4% (editor screen) |
| #fad78b / #f1c87b | yellow note and crumpled ball | 2% |
| #f9c0c6 | pink note (initial) | — |
| #9d9fa0 / #74787a | bin metal, hint text | 2.4% |
| #000000 | device bezel, icons | 2.6% |
| #22d14b | green exit-sign back button | <1% |

The swatch row offers pink, yellow, green, sky, periwinkle and magenta pastels.

WCAG checks:
- Note text #1f1a10 on #fad78b is 12.49:1.
- Black chip text on white is 18.88:1.
- The hint "Pull down to aim your toss" (#9d9fa0 on #fff) is **2.66:1 (fail)**.
- Sheet labels #8a8a8e on #f3f4f6 are 3.12:1.
- White glyphs on the green exit sign #22d14b are 2.04:1, an iconic sign rather than text.

## 5. Depth & material
- Two material worlds collide:
  - Flat iOS chrome: white chips with no border and very soft shadows, and action tiles with a radius of about 16 pt on #f3f4f6.
  - Photoreal 3D: the bin has a metal rim and mesh, with white crumpled balls already inside. The yellow ball has strong directional shading, light from the top-left and a hard-ish shadow at the bottom-right.
- The note card has a faint lower drop shadow and a slight perspective tilt that reads as paper lying on a table.
- **Aim mode (7.39 s):** three concentric hairline arcs (#e5e5e5) radiate from the ball like a slingshot range indicator.

## 6. Components & patterns
- **Colour swatch picker:** six 32 pt dots. The selected one gets a 2 px black ring with a white gap.
- **Chips:** horizontal-scroll chip rows with a leading "+" chip. Collaborator chips include a 24 pt avatar. The last chip is clipped at the edge as an overflow cue.
- **Action tiles:** four equal tiles, each with a 1.5 px line icon over a label. "Toss" uses a bin glyph that foreshadows the object.
- **Back button:** a green emergency-exit-sign pictogram (arrow plus running figure), a witty "leave" affordance.
- **Result grid:** product cards (radius about 16 pt) with a cut-out product photo, a name, a size, and a check-circle at the bottom-left.

## 7. Motion
**Measured:** 10.23 s at 30 fps, motion fraction 0.18, with five segments:
- 1.73–1.83 s (0.1 s, ease-out, peak 0.17): the colour swap from pink to yellow is a near-instant cross-fade.
- 3.00–3.83 s (**0.83 s**, ease-out, peak 0.22): the note crumples into the ball, the longest and most energetic beat. It starts fast and settles.
- 6.30–6.67 s (0.37 s, **ease-in**, peak 0.68): the pull-back and release of the throw. It accelerates into the launch.
- 7.87–8.07 s (0.2 s, symmetric): the ball flies in and lands in the bin.
- 8.90–9.23 s (0.33 s, symmetric): the screen transitions to the list grid.

`seamless_loop_likely: false` (first/last diff 9.62). The easing choices are semantically right: the crumple decelerates, while the throw accelerates as in physics. Between 3.98 s and 6.25 s the ball idles with a subtle wobble while the user is cued to pull.

## 8. Brand system
n/a — not a brand system. Identity cues:
- the green exit-sign back button;
- pastel sticky notes;
- a playful, object-based vocabulary for actions.

## 9. UX
- **Strengths:** It makes an irreversible action deliberate. A second gesture (pull-to-aim) is required after "Toss", which works as a natural confirmation step. Recolouring and categorising sit in one sheet with clear labels.
- **Risks:**
  - The hint text fails contrast.
  - The aim gesture has no accessible alternative, and no undo or snackbar is shown after landing.
  - The fun wears thin if users delete many notes, so it would need a bulk-delete path.

## 10. Craft signals
- The crumpled ball keeps the exact yellow of the note (#fad78b / #f1c87b), which preserves object identity across the transformation.
- The note card is rotated about −2° along with its text, so it reads as paper rather than a UI card.
- The selected swatch uses a black ring plus white gap instead of a checkmark.
- The aim arcs are concentric, hairline and centred on the ball, communicating range without labels.
- The bin already contains white paper balls, so the destination is pre-filled to signal what happens there.
- The "Toss" tile icon is the same bin silhouette as the 3D bin.
- The chip rows deliberately clip "Household Items" and "Sop…" at the sheet edge.

## 11. Reproduction recipe
```css
:root{--bg:#fff;--sheet:#f3f4f6;--chip:#fff;--muted:#6e6e73;--note-yellow:#fad78b;--note-pink:#f9c0c6;
  --r-note:24px;--r-tile:16px;--font:-apple-system,"SF Pro Text",system-ui,sans-serif}
.note{width:300px;aspect-ratio:1;border-radius:var(--r-note);background:var(--note-yellow);transform:rotate(-2deg);
  padding:20px;font:600 17px/1.2 var(--font);box-shadow:0 2px 0 rgba(0,0,0,.04),0 12px 24px -12px rgba(0,0,0,.15);
  transition:background-color .1s ease-out}
.note.crumple{animation:crumple .83s cubic-bezier(.15,.8,.3,1) forwards}
@keyframes crumple{60%{transform:rotate(8deg) scale(.55);border-radius:45%}to{transform:rotate(14deg) scale(.6);border-radius:50%}}
.ball.throw{animation:throw .37s cubic-bezier(.55,0,1,.45) forwards}
@keyframes throw{to{transform:translateY(-520px) scale(.35)}}
.swatch{width:32px;height:32px;border-radius:50%}
.swatch[aria-checked=true]{box-shadow:0 0 0 2px #fff,0 0 0 4px #111}
.tile{background:#fff;border-radius:var(--r-tile);padding:10px 0;display:grid;place-items:center;gap:4px;font:500 13px var(--font)}
.hint{color:var(--muted)} /* #6e6e73 on #fff = 5.1:1, fixes the 2.66:1 original */
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 7 | Clean iOS shell, but the photoreal bin and ball clash slightly with the flat chrome (which is intentional). |
| Originality | 9 | Delete as crumple-and-throw, with pull-to-aim as the confirmation, is a genuinely new interaction idea. |
| Usability | 6 | The gesture doubles as confirmation, but there is no undo, no accessible path and a faint hint. |
| Craft | 7 | Colour continuity and physics-correct easing. The ball's hard shadow looks pasted-on against white. |

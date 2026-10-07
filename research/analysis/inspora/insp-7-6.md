---
id: insp-7-6
source: inspora
category: Motion
status: analyzed
title: "Delete this file"
creator: "@nilseller"
styles: [corporate-clean, soft-3d, micro-interaction, playful-rounded]
patterns: [gamified-destructive-confirm, flick-to-throw, miss-counter-feedback, morph-dialog-to-toast, undo-toast, physical-bin-target]
mode: light
palette: ["#f9f9f9", "#ffffff", "#111111", "#5f5f5f", "#d8d8d7", "#cdcccb", "#d61f3c"]
type_families: ["Inter (likely)"]
type_class: [neo-grotesk]
radius_px: [40, 32, 12, 9999]
motion: {durations_s: [0.1, 0.37], easing: [ease-in, ease-out], loop: false}
scores: {aesthetics: 7, originality: 9, usability: 5, craft: 8}
craft_signals: [copy-swaps-on-miss, live-miss-counter, paper-ball-scale-with-depth, dialog-morphs-into-toast, undo-always-offered, red-reserved-for-final-state]
anti_patterns: [destructive-action-made-skill-based, footer-text-below-3-to-1]
---
# Delete this file — @nilseller

## 1. Snapshot
- **Subject:** A 9.4 s, 1920×1361 clip of a playful delete-confirmation card. Instead of a "Delete" button, the user crumples the file and flicks it into a 3D paper bin. Misses are counted, and a successful throw collapses the dialog into a "File deleted / Undo" toast.
- **Why it's remarkable:** It replaces a modal confirm with a physical gesture that is intentionally effortful. The delete becomes deliberate and delightful, and an Undo remains as the safety net.

## 2. Composition & layout
- **Stage:** a single card (about 790×1105 px, radius about 40 px) centred on a #f9f9f9 canvas, with an approximately 58 px inner padding.
- **Card structure, top to bottom:**
  - title at y≈210;
  - one-line instruction at y≈266;
  - a large empty "throw zone";
  - the bin (about 180×230 px) at the optical centre, y≈540–760;
  - the file icon (about 95×120 px) with its filename about 230 px below the bin;
  - a footer row with status text left-aligned and the miss counter right-aligned at y≈1156.
- **Toast:** about 660×165 px (radius about 32 px), centred where the card was.

## 3. Typography
- **Typeface:** Inter, recognisable from the "D", "e", the tabular "1" and the single-storey "g".
- **Title:** "Delete this file?" at about 40 px Semibold (600), #111.
- **Body:** about 23 px Regular in #5f5f5f.
- **Footer:** about 22 px. The status is in #5f5f5f ("Missed. Have another go."); the default hint and the counter are lighter (about #9a9a9a).
- **Toast:** title about 22 px Semibold; filename about 20 px grey; "Undo" about 20 px in a 1 px outlined button.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #f9f9f9 | canvas | 97% |
| #ffffff | card / toast surface | — |
| #111111 | titles | <1% |
| #5f5f5f | body copy | <1% |
| #d8d8d7 / #cdcccb / #e7e7e5 | bin ceramic shading, file icon | 2.6% |
| #d61f3c (est.) | delete badge in toast | <0.5% |

WCAG checks:
- The title, #111 on #fff, is 18.88:1.
- Body text #5f5f5f is 6.39:1.
- The footer hint and miss counter, about #9a9a9a, are **2.81:1 (fail)**. The faint "Flick up, or drop it straight in." hint (about #b0b0b0) is 2.17:1.
- White glyph on the red badge, #d61f3c, is 5.1:1.

Red appears only after the deletion is done, so it signals the consequence rather than decorating the prompt.

## 5. Depth & material
- **Card:** very soft elevation, roughly `0 30px 60px rgba(0,0,0,.06)`.
- **Bin:** a rendered matte-ceramic cylinder with a vertical specular stripe left of centre, a darker inner rim ellipse and a tiny contact shadow. It is the only 3D object.
- **File icon:** a flat document with a dog-ear and a placeholder image glyph.
- **Paper ball:** a small white sphere (about 30 px) with soft shading. It shrinks as it flies "into" depth toward the bin (1.57 s vs 6.79 s frames).

## 6. Components & patterns
- **Gamified confirm dialog:** drag or flick the file. A miss returns it to its spot and increments the counter ("0 misses" → "1 miss", with correct singular/plural). The status copy swaps from the hint to "Missed. Have another go."
- **Success:** the ball drops into the bin, and the dialog collapses into an undo toast with an icon badge, title, filename and outlined Undo button.

## 7. Motion
Measured (m0_motion.json, 30 fps, 9.4 s, motion_fraction 0.04, not loop-seamless, first/last diff 4.41 because it ends on the toast):
- **0.57–0.67 s (0.10 s, peak 0.83):** ease-in, the file crumpling on press (a quick snap).
- **7.90–8.27 s (0.37 s, peak 0.05):** a very fast-start ease-out, the card morphing into the toast. The large card shrinks to toast size, and the instant start reads as "done".

The throws themselves (1.0–2.6 s and about 6.5–7.8 s) are small objects and stay under the energy threshold. From frames, the ball follows a ballistic arc with depth scaling, lasting about 0.6–0.8 s per throw (estimate). A miss rolls the ball off to the lower right (2.61 s frame).

## 8. Brand system
n/a — this is an interaction concept, not a brand system. Identity cue: the "make software fun again" tone, expressed through copy ("Have another go") and a single tactile object.

## 9. UX
- **Pros:**
  - A friction-by-design destructive action.
  - Explicit instructions and a drop-in alternative ("or drop it straight in"), which matters for users who can't flick.
  - Clear miss feedback, and Undo is preserved.
- **Cons:**
  - Delete becomes a skill test. For repeated or bulk deletes, or for motor-impaired and keyboard users, it is a barrier unless there is a keyboard or button path.
  - There is no visible Cancel.
  - The footer text is under 3:1.
- Best suited to rare, consequential deletes or to onboarding delight.

## 10. Craft signals
- The miss counter pluralises correctly ("0 misses" / "1 miss").
- Footer copy swaps state-specifically while the counter keeps its right alignment.
- The paper ball scales down as it travels toward the bin, a correct depth cue.
- The dialog morphs into the toast in 0.37 s rather than cutting, which keeps continuity.
- Red appears only in the post-action toast.
- The bin has a contact shadow, and the throw zone is generous empty space above it.

## 11. Reproduction recipe
```css
:root{--canvas:#f9f9f9;--surface:#fff;--ink:#111;--ink-2:#5f5f5f;--ink-3:#8a8a8a;--danger:#d61f3c;
  --r-card:40px;--r-toast:32px;--font:"Inter",system-ui}
.confirm{width:395px;padding:29px;border-radius:var(--r-card);background:var(--surface);
  box-shadow:0 30px 60px rgba(0,0,0,.06);font-family:var(--font);
  transition:all .37s cubic-bezier(.05,.7,.1,1)}
.confirm h2{font:600 20px/1.2 var(--font);color:var(--ink)}
.confirm p{font:400 12px/1.4 var(--font);color:var(--ink-2)}
.confirm footer{display:flex;justify-content:space-between;font-size:11px;color:var(--ink-3)}
.confirm.done{width:330px;height:82px;border-radius:var(--r-toast)}
.ball{animation:throw .7s cubic-bezier(.3,.6,.4,1) forwards}
@keyframes throw{0%{transform:translate(0,0) scale(1)}50%{transform:translate(var(--dx),-180px) scale(.7)}100%{transform:translate(var(--dx2),-120px) scale(.5)}}
.toast .badge{width:30px;aspect-ratio:1;border-radius:50%;background:linear-gradient(#e8344f,var(--danger));color:#fff}
.toast button{border:1px solid #e3e3e3;border-radius:12px;padding:6px 10px}
```
Add a keyboard path: Enter on the focused file should equal "drop it straight in".

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 7 | Clean Inter card with one well-rendered object; deliberately quiet. |
| Originality | 9 | Turning delete-confirm into a paper toss with a miss counter is a genuinely new idea. |
| Usability | 5 | Delightful once, frustrating at scale; accessibility path not shown; faint footer text. |
| Craft | 8 | Pluralised counter, depth-scaled ball, smooth dialog-to-toast morph, Undo kept. |

---
id: insp-7-3
source: inspora
category: Product
status: analyzed
title: "Assets overview carousel"
creator: "@proskuaaa"
styles: [micro-interaction, kinetic-type, dark-premium, maximalist-color]
patterns: [inline-emoji-sentence-summary, metric-chip-tap-to-expand, arc-carousel-of-thumbnails, background-blur-focus, camera-zoom-on-focus, ai-prompt-bar, suggestion-chips]
mode: mixed
palette: ["#0860f6", "#080808", "#131213", "#ffffff", "#e1e0e0", "#8d92ad", "#4e474a"]
type_families: ["SF Pro Display / Inter-style neo-grotesk (likely)"]
type_class: [neo-grotesk]
radius_px: [64, 28, 24, 9999]
motion: {durations_s: [0.67, 0.43, 0.3, 0.8], easing: [ease-out], loop: true}
scores: {aesthetics: 8, originality: 8, usability: 6, craft: 8}
craft_signals: [two-tone-sentence-bold-entities-dim-connectors, inline-avatar-and-calendar-glyphs, arc-path-with-per-item-rotation, depth-blur-on-underlying-ui, dotted-divider-inside-header, camera-push-in-on-expand]
anti_patterns: [dim-connector-words-2-5-contrast, carousel-occludes-actions]
---
# Assets overview carousel — @proskuaaa

## 1. Snapshot
- **Subject:** A 6.7 s, 1920×1920 loop of a mobile app called "Tickr". A blue header summarises activity as a sentence, using inline avatars, a speech-bubble glyph and a calendar glyph. Tapping the "14 images" metric zooms the camera in and fans the file's image assets out along a curved arc carousel on the right, while the dark content below blurs.
- **Why it's remarkable:** The metric becomes a physical reveal. The count "14" turns into the 14 actual things, flowing along a wheel-like path over a depth-blurred UI.

## 2. Composition & layout
- **Resting state (0.37 s frame):** the phone is ≈285 px wide in the 640 px sheet cell, about 855 px in the real 1920 frame, and centred.
- **Blue header card:** occupies the top ~45% of the screen and has rounded bottom corners (≈64 px real).
- **Header contents:**
  - a nav row (back, "Tickr", stats and settings icons);
  - a five-line sentence;
  - a dotted divider;
  - a meta row: "3 hours ago • 📎 12 • 🖼 14 • 🔗 2".
- **Lower section:**
  - a drag handle, a segmented pill and description text;
  - two suggestion chips ("Change background to gradient", "Enable light mode toggle");
  - an "Ask to build…" prompt bar.
- **Expanded state (key frame):** the camera has pushed in about 2.2×.
  - Thumbnails (≈270 px real squares, radius ≈28 px) sit on an arc that bulges toward the screen centre. The centre item is the largest (≈275 px) and the items shrink and rotate (±8–12°) toward the top and bottom.
  - Share and download circular buttons (≈96 px) sit to the left of the focused item.

## 3. Typography
- **Typeface:** neo-grotesk, close to SF Pro Display.
- **Header sentence:** ≈24 px in the resting screen, about 70 px in the zoomed frame, Semibold.
  - Entities ("prosku.a", "In Progress", "5 unread comments", "1 meeting.") are white.
  - Connective words ("Hey,", "Your file is", "edits by", "You have", "and scheduled") are a translucent light blue.
  - This "highlighted sentence" makes the summary skimmable by entities alone.
- **Meta row:** Medium weight, with icons in the same tint. Body text below is ≈15 px Regular in white or grey.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #0860f6 | header card (electric blue) | ~11% |
| #080808 / #131213 | screen background, cards | ~38% |
| #ffffff | stage, key text | ~36% |
| #8d92ad | blue-tinted dim text | ~3% |
| #e1e0e0 | device frame | ~4% |
| #4e474a | chip surfaces | ~4% |

**WCAG:**
- White on blue: **5.23:1** (pass).
- Connector words (≈#8db3fb on #0860f6): **2.48:1** (fail).
- Meta row (≈#bcd2fc): **3.43:1** (large only).
- On black, white is **20.03:1** and the grey body text is **5.8:1**.

## 5. Depth & material
- When the carousel opens, the underlying dark UI gets a strong Gaussian blur (≈20 px), and the header stays sharp, so the carousel sits on a middle depth plane.
- Thumbnails have a white 4–6 px border and a soft shadow. They read as stickers or polaroid tiles.
- The device has a light silver frame on a white stage.

## 6. Components & patterns
- **Rich-text summary** with inline media: avatars, a speech bubble with an unread dot, and a calendar day "5".
- **Meta row of counters** (attachments, images, links); each one implies a drill-in.
- **Arc carousel:** items move along a circular path with rotation tied to position, and the focused item gets action buttons.
- **AI prompt bar** with a magic-wand icon, a paperclip and a send button. Suggestion chips use a gradient swatch and a toggle.

## 7. Motion
Measured: duration 6.70 s, motion fraction 0.33, 4 segments, all ease-out (peaks at 0.07–0.35), `seamless_loop_likely: true`.

| Segment | Duration | Peak | Interpretation |
|---|---|---|---|
| 1.50–2.17 s | **0.67 s** | 0.07 (sharp ease-out) | Camera push-in, blur in, carousel fans out |
| 2.43–2.87 s | 0.43 s | — | Carousel rotates one step |
| 3.93–4.23 s | 0.30 s | — | Carousel rotates another step |
| 4.77–5.57 s | **0.80 s** | 0.19 | Carousel collapses, blur out, camera pulls back (4.84 s frame shows motion blur on the header) |

- From frames, items slide along the arc and keep their rotation relative to the curve, like a wheel.
- The 6.33 s frame is back to the resting state, which closes the loop.

## 8. Brand system
n/a — not a brand system. Identity cues: an electric blue (#0860f6) header block, a sentence-style status summary, and collage-like asset thumbnails (sketches, scans, photos).

## 9. UX
- **What works:**
  - The sentence summary is an efficient, friendly overview.
  - Tapping a count to preview its contents is a natural drill-in.
  - Blur keeps focus on the carousel.
- **Risks:**
  - Connector words fail contrast.
  - The carousel covers the suggestion chips and prompt bar with no visible close affordance.
  - An arc layout fits only about 6–7 items, which is awkward for 14.
  - Camera zoom is a presentation device, not real UI.

## 10. Craft signals
- Entities and connectors in the same sentence differ only in opacity, not size or weight, which keeps the rhythm intact.
- Inline glyphs (avatars ≈ cap height, calendar tile ≈1.2× cap height) sit on the baseline.
- Thumbnail rotation increases with distance from the arc centre, so the path reads as a wheel.
- The dotted divider in the header separates narrative from metadata without a hard rule.
- All four motion segments are ease-out, which gives a consistent "responsive" feel.

## 11. Reproduction recipe
```css
:root{--blue:#0860f6;--bg:#080808;--ink:#fff;--dim-on-blue:rgba(255,255,255,.55);--r-head:64px;--r-thumb:28px;
  --font:"SF Pro Display","Inter",system-ui,sans-serif;}
.head{background:var(--blue);border-radius:0 0 var(--r-head) var(--r-head);padding:24px;color:var(--dim-on-blue);
  font:600 24px/1.3 var(--font)}
.head b{color:var(--ink);font-weight:600}
.head hr{border:0;border-top:2px dotted rgba(255,255,255,.3)}
.below{transition:filter .67s cubic-bezier(.16,1,.3,1)}
.open .below{filter:blur(20px)}
.arc{position:absolute;right:8%;top:50%;}
.thumb{position:absolute;width:90px;aspect-ratio:1;border-radius:var(--r-thumb);border:4px solid #fff;
  box-shadow:0 10px 24px rgba(0,0,0,.4);
  transform:rotate(calc(var(--k)*10deg)) translateX(-260px) rotate(calc(var(--k)*-10deg + var(--k)*-4deg))
            scale(calc(1 - abs(var(--k))*.12));
  transition:transform .43s cubic-bezier(.2,.9,.2,1)}
```
`--k` is the item's offset from the focused index (…, −1, 0, 1, …). The pivot is placed to the right of the screen so items trace a left-bulging arc.

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Bold blue against black with collage thumbnails; lively and modern. |
| Originality | 8 | Count-to-arc-carousel is a memorable drill-in; the sentence summary is distinctive. |
| Usability | 6 | Great overview, but there are contrast failures and the carousel occludes actions. |
| Craft | 8 | Consistent ease-out timing, careful inline glyph sizing, and coherent arc maths. |

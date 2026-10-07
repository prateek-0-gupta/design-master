---
id: insp-sticker-footer
source: inspora
category: Web
status: analyzed
title: "Footer"
creator: "@oiharshit"
styles: [flat-illustration, maximalist-color, micro-interaction, minimal-swiss]
patterns: [draggable-sticker-pile, illustrated-landmark-stickers, three-column-footer-nav, typewriter-wordmark, lift-shadow-on-drag, bottom-bleed-collage]
mode: light
palette: ["#ffffff", "#e6e1e3", "#111111", "#6b6b6b", "#93c9dd", "#1f798b", "#b9885c", "#834731"]
type_families: ["typewriter slab for wordmark, close to American Typewriter / Courier Prime Bold (likely)", "Inter (likely)"]
type_class: [slab, neo-grotesk]
radius_px: [9999]
motion: {durations_s: [0.73, 0.8, 0.3, 0.8, 0.6], easing: [ease-in, ease-in-out, ease-out], loop: false}
scores: {aesthetics: 8, originality: 7, usability: 8, craft: 7}
craft_signals: [die-cut-white-border-stickers, lifted-sticker-gains-shadow, stickers-overlap-text-row, single-illustration-style-across-set, quiet-ui-loud-collage-split]
anti_patterns: [sticker-can-cover-footer-copy, inconsistent-sticker-border-width]
---
# Footer — @oiharshit

## 1. Snapshot
- **Subject:** A 10 s, 2856×1588 capture of a travel-planning brand "wandor"'s footer. A plain white footer with a 3-column nav sits above a pile of die-cut landmark stickers that bleed off the bottom edge. Each sticker can be dragged and reshuffled.
- **Landmarks:** Sagrada Família, Park Güell mosaic, Sydney Opera House, Santorini, Gateway of India, Blue Mosque, Big Ben, Eiffel Tower, Colosseum and the Pyramids.
- **Why it's remarkable:** It makes the end of the page a tactile souvenir scrapbook that maps directly to the product (travel). The UI above stays almost Swiss-neutral.

## 2. Composition & layout
Key frame is ×1.43 to source.
- **Upper 45%:** quiet UI.
  - Wordmark at x=160, y≈235, with the tagline below.
  - Nav columns at x≈1330, 1522 and 1730 (gap about 200 px), each with headers at y≈218 and 3 links at a 43 px pitch.
  - A bottom row at y≈500 with "wandor. © 2026" on the left and "Made for curious travelers." on the right. Both align to the 160 px outer margins.
- **Lower 55%:** the sticker collage, full-bleed and cropped at the bottom and sides. The stickers are about 350–550 px wide, overlap one another and rise as high as y≈470, so they intrude on the copyright row (the Eiffel Tower covers "travelers").
- **Top edge:** A rounded pale bar at the top (y≈0–25) is the bottom of the previous section's card, which shows a stacked-section layout.

## 3. Typography
- **Wordmark** "wandor" is a lowercase typewriter slab (American Typewriter / Courier-like), about 55 px, with an inked, rough edge.
- **UI:** Inter-like grotesk.
  - Column headers are about 20 px uppercase at weight 500 with no extra tracking.
  - Links are about 18 px regular in #3a3a3a.
  - The tagline is about 18 px in grey (#6b6b6b).
  - The bottom row is 18 px.
- **Pairing:** The typewriter face carries the "travel journal" flavour; everything else is neutral.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #ffffff | canvas | 59% |
| #e6e1e3 | sticker die-cut borders | 7% |
| #111111 / #3a3a3a | wordmark, links | 2% |
| #6b6b6b | tagline | <1% |
| #93c9dd / #1f798b | sky, sea in stickers | 6% |
| #b9885c / #ab7045 / #834731 / #9f5e39 | terracotta, stone landmarks | 10% |
| #e8a33a (sun) | accent dots | — |

WCAG checks:
- Wordmark #111 on white is 18.88:1.
- Links #3a3a3a are 11.37:1.
- The grey tagline #6b6b6b is 5.33:1.

All text passes. The colour is quarantined entirely in the stickers: warm terracotta and teal on a white page.

## 5. Depth & material
- **At rest:** Each sticker has a light pinkish-grey die-cut border of about 12–16 px (#e6e1e3) and a faint 1–2 px shadow, so they read as vinyl stickers lying flat.
- **Dragged:** The sticker lifts. At 1.68 s (the mosque) and 7.26 s (Gateway of India) it gains a large soft drop shadow of about 30 px blur, offset down, and comes to the top of the stack. This is a classic pick-up affordance.
- **Rotation:** Stickers rotate a few degrees (−5° to +8°) for a hand-placed feel.

## 6. Components & patterns
- A three-column footer nav: Explore / Company / Legal × 3 links.
- A brand block: wordmark plus tagline.
- A legal row: copyright plus sign-off.
- **Draggable sticker collage:** grab cursor (key frame), lift shadow, z-order raise on pick, and stickers stay where dropped. The layout changes permanently across the 9 frames: Pyramids at 0.56 s, then replaced or covered by the mosque; Gateway moved left at 7.26 s; Santorini moved at 9.49 s.

## 7. Motion
Measured: 10.05 s at 60 fps, motion_fraction 0.34, 6 segments with a median of 0.67 s, not a loop.
- **Drags:** 0.87–1.60 s (0.73 s, ease-in, peak 0.84) is the pick-up and a fast fling. 2.97–3.77 s (0.80 s, symmetric) and 6.50–7.30 s (0.80 s, ease-out, peak 0.23) are drag-and-drop moves that decelerate into place.
- **Short adjustments:** 5.13–5.43 s (0.30 s) and 8.27–8.87 s (0.60 s, ease-in).
- **Result:** Motion is direct-manipulation, 1:1 with the pointer, and the drop settles in about 0.2–0.3 s. No idle animation runs, so the footer is calm until touched.

## 8. Brand system
n/a — not a brand system. Identity cues:
- the typewriter "wandor" wordmark (travel journal, luggage tag);
- the sticker-on-luggage metaphor;
- a warm, heritage-landmark illustration style with consistent flat shading, cloud puffs and orange sun dots across all stickers.

## 9. UX
- **Strengths:** Fully legible nav (all ≥ 5.3:1), the play is optional and separated from the links, and the drag affordance is clear (grab cursor plus lift).
- **Weaknesses:**
  - Stickers can be dropped over the copyright row (already happening at "travelers"). Clamp their max-y below the text row.
  - The heavy raster illustrations add page weight to a footer.
  - It needs touch support, plus scroll-vs-drag disambiguation on mobile.

## 10. Critical craft signals
- Die-cut borders follow each illustration's silhouette, not a rectangle.
- A lifted sticker gets a bigger shadow and a top z-index (compare the mosque at 1.68 s with the rest).
- All stickers share one illustration language (flat shading, blue sky puffs, orange sun disc), so the collage is cohesive.
- The UI uses only greys; every colour lives in the collage.
- 160 px outer margins are mirrored left and right on the brand block and the legal row.

## 11. Reproduction recipe
```css
:root{--bg:#fff;--ink:#111;--ink-2:#3a3a3a;--muted:#6b6b6b;--die:#e6e1e3;
  --sans:"Inter",system-ui,sans-serif;--type:"American Typewriter","Courier Prime",serif}
.footer{position:relative;overflow:hidden;min-height:100vh;padding:150px 112px 0;background:var(--bg);font:400 18px/2.4 var(--sans);color:var(--ink-2)}
.wordmark{font:700 56px/1 var(--type);color:var(--ink)}
.cols h4{font:500 20px var(--sans);text-transform:uppercase;color:var(--ink)}
.sticker{position:absolute;cursor:grab;transform:rotate(var(--rot,0deg));
  filter:drop-shadow(0 0 0 var(--die)) drop-shadow(0 1px 2px rgb(0 0 0/.08));
  transition:filter .2s ease-out,transform .25s cubic-bezier(.2,.9,.3,1.2)}
.sticker.dragging{cursor:grabbing;z-index:99;transform:rotate(var(--rot)) scale(1.04);
  filter:drop-shadow(0 18px 24px rgb(0 0 0/.22))}
/* die-cut border: bake into PNG, or outline via SVG feMorphology dilate radius=8 + flood #e6e1e3 */
```
```js
// pointer drag with max-y clamp so stickers never cover the legal row
el.onpointerdown=e=>{el.setPointerCapture(e.pointerId);el.classList.add('dragging');el.style.zIndex=++z};
el.onpointermove=e=>{if(!el.hasPointerCapture(e.pointerId))return;
  el.style.left=e.clientX-ox+'px';el.style.top=Math.max(minTop,e.clientY-oy)+'px'};
el.onpointerup=()=>el.classList.remove('dragging');
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | A joyful, cohesive sticker set against a crisp white Swiss footer. |
| Originality | 7 | Draggable sticker footers are a recognised trend; the brand-to-content fit (travel souvenirs) lifts it. |
| Usability | 8 | Links are fully legible and separated from the play area. Stickers can cover copy. |
| Craft | 7 | Good lift feedback and die-cut borders. Border widths and illustration resolution vary a bit. |

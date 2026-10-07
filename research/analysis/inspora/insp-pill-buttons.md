---
id: insp-pill-buttons
source: inspora
category: Product
status: analyzed
title: "pill buttons"
creator: "@wherescz"
styles: [micro-interaction, minimal-swiss, monochrome]
patterns: [morphing-container, pill-to-card-expand, confirm-dialog, destructive-confirmation, payment-confirm-sheet, flight-tracker-card, blur-crossfade-content]
mode: light
palette: ["#e5e5e5", "#dbdbd9", "#1e1e1e", "#ad6368", "#b6b2b1", "#cccac8"]
type_families: ["Inter (likely)"]
type_class: [neo-grotesk]
radius_px: [9999, 40, 24]
motion: {durations_s: [0.43, 0.3, 0.33, 0.4, 0.27, 0.17], easing: [ease-out], loop: true}
scores: {aesthetics: 7, originality: 7, usability: 8, craft: 8}
craft_signals: [container-morph-from-trigger, blur-plus-fade-plus-scale-content, button-colour-predicts-sheet-colour, label-persists-as-title, consistent-ease-out-timing, safe-action-left-destructive-right]
anti_patterns: [low-contrast-body-on-grey-sheet, destructive-red-borderline-aa]
---
# pill buttons — @wherescz

## 1. Snapshot
- **Subject:** A 40.8 s, 1920×1080 (60 fps) loop showing three compact trigger pills, each morphing in place into a full card:
  - "Track my flight" → dark flight-status card;
  - "Delete project" → destructive confirm dialog;
  - "Pay $24.00" → payment confirmation sheet.
- **Why it's remarkable:** The button **is** the dialog. Each pill grows into its card from the same spot, its label survives as the card title, and the inner content arrives with blur, fade and scale. That gives perfect spatial continuity with no overlay or scrim.

## 2. Composition & layout
- Everything is centred on a flat #e5e5e5 canvas, one component at a time.
- **Trigger pills:** about 90–140 px wide by 36 px tall (sheet scale ×3 for real px). "Delete project" is a tinted pill; "Pay $24.00" is a black pill.
- **Expanded cards (real px):**
  - **Flight card:** about 810×555 px. Header row (title, ×); meta row (MI765 · Sky Wing · SKYFLY); big route row "NYC ✈ LON" with an arced dashed path; footer with "● On Time / Landing in 24 min" and "1h 30min".
  - **Delete dialog:** about 775×375 px. Title, two-line body, and buttons "Keep it" (ghost) and "Delete" (filled), each about 335×72 px.
  - **Pay sheet:** about 715×680 px. A centred "$24.00" at about 70 px; label/value rows (From / Status / Fee) with values right-aligned; Cancel / Confirm.

## 3. Typography
- Inter-like neo-grotesk throughout:
  - Dialog title about 34 px Semibold #1e1e1e.
  - Body about 30 px Regular #6b6b6b with leading of about 1.5.
  - Button labels about 30 px Medium.
- In the flight card, the airport codes are about 60 px Bold, and the meta row is about 22 px caps grey with wide spacing.
- The pay amount is about 70 px Medium with tabular figures. Row labels are grey and values black, right-aligned.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #e5e5e5 | canvas | 94% |
| #dbdbd9 | light sheet surface | 3% |
| #1e1e1e | dark sheet, primary button, text | — |
| #ad6368 (sampled, anti-aliased) / ~#bc4b55 core | destructive red | 1.3% |
| #b6b2b1 / #cccac8 | sheet edges, shadows | 2% |

WCAG checks:
- #1e1e1e on #dbdbd9: 12.0:1.
- **Body #6b6b6b on #dbdbd9: 3.84:1 (fails AA-normal).**
- White on the red Delete button: 4.41:1 (sampled) to 4.91:1 (core), which is borderline.
- The "Delete project" trigger (red text on pink) is 3.63:1.
- White on the dark flight card: 16.7:1.

The colour of each trigger pill predicts its sheet: the black pill opens a black or confirm-black sheet, and the red-tinted pill opens a red-CTA dialog.

## 5. Depth & material
- The sheets are barely elevated: #dbdbd9 on #e5e5e5 with a very soft, broad shadow and a faint light edge. They are closer to a raised panel than a modal.
- There is no scrim; the rest of the page stays visible.
- The dark flight card has a subtle top highlight. Its arced route path is drawn as a solid line behind the plane and dashed ahead of it.

## 6. Components & patterns
- **Morphing container:** one element whose width, height and radius tween from pill (full radius) to card (about 40 px radius).
- **Destructive confirm:** the safe action ("Keep it") is a plain text button on the left and the red filled pill sits on the right, with copy that states the consequence.
- **Payment confirm:** the amount is the hero, then a three-row summary, then Cancel / Confirm (black pill).
- **Flight status:** a live-state dot ("On Time" in green) plus an ETA.

## 7. Motion
Measured: 40.8 s, `motion_fraction` 0.15, 23 segments with a median of 0.27 s, `seamless_loop_likely` true.
- **Expand/collapse:** 0.30–0.43 s, all **ease-out**. Examples: 2.20–2.63 s (0.43 s, peak 0.27), 6.70–7.13 s (0.43 s, peak 0.19), 9.00–9.33 s (0.33 s, peak 0.25) and 10.47–10.87 s (0.40 s, peak 0.29).
- **Hover and press feedback:** 0.13–0.20 s symmetric segments (16.07, 18.53, 23.30, 24.97 s), for example hover on × and on buttons.
- **From frames:** at 6.80 s the flight card is mid-morph. The container is already at about 70% size, and the meta labels ("Sky Wing", "SKYFLY") are **visibly blurred and half-transparent**. This confirms the content enters with a blur(≈6px)→0 + opacity + slight scale after the shell leads.
- The shell is roughly 0.4 s, with content staggered about 80–120 ms behind.

## 8. Brand system
n/a — not a brand system. It is a component study with no identity marks.

## 9. UX
- **Strengths:**
  - Spatial continuity, so the user always knows where the dialog came from.
  - Labels persist as titles.
  - Consequence-first copy on delete.
  - Payment details are shown before the confirm.
  - × close on every card.
- **Risks:**
  - Without a scrim, focus trapping is not visually signalled.
  - Grey body copy fails AA.
  - The red is borderline.
  - Morphing in place may overlap neighbouring content in a dense layout; this demo avoids that by isolating each component.

## 10. Craft signals
- All expand transitions are ease-out with front-loaded peaks (0.19–0.29 of the segment), consistent across three different components.
- Inner content blurs in rather than simply fading (visible at 6.80 s).
- Button placement is consistent: the secondary action is unfilled on the left and the primary is a filled pill on the right, in both the delete and pay dialogs.
- The arced flight route changes stroke style (solid before the plane, dashed after) to encode progress.
- Value rows in the pay sheet are right-aligned with tabular numerals ("$0.00", "··4821").

## 11. Reproduction recipe
```css
:root{--canvas:#e5e5e5;--sheet:#dbdbd9;--ink:#1e1e1e;--muted:#5c5c5c;/* AA-safe */--danger:#b83f4a;
  --ease-out:cubic-bezier(.16,1,.3,1);--t-shell:.4s;--t-content:.3s}
.morph{border-radius:9999px;background:var(--sheet);overflow:hidden;
  transition:width var(--t-shell) var(--ease-out),height var(--t-shell) var(--ease-out),border-radius var(--t-shell) var(--ease-out)}
.morph[data-open]{border-radius:40px;box-shadow:0 20px 60px rgba(0,0,0,.08)}
.morph .content{opacity:0;filter:blur(6px);transform:scale(.97);
  transition:opacity var(--t-content) var(--ease-out) .1s,filter var(--t-content) var(--ease-out) .1s,transform var(--t-content) var(--ease-out) .1s}
.morph[data-open] .content{opacity:1;filter:blur(0);transform:none}
.btn-danger{background:var(--danger);color:#fff;border-radius:9999px;height:48px}
```
In React, Framer Motion's `layout` / `layoutId` shared between the pill and the card gives the same effect, with `transition={{type:"spring",bounce:0,duration:.4}}`.

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 7 | Restrained grey-on-grey with a single accent per component. Tasteful but plain. |
| Originality | 7 | Pill-to-card morphs (Dynamic Island style) are known, but three varied real use cases make it a reusable system. |
| Usability | 8 | Strong continuity, clear action hierarchy and consequence copy. Some contrast misses. |
| Craft | 8 | Consistent ease-out timings, blurred content entry and careful button logic. |

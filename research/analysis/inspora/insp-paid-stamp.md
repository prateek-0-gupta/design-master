---
id: insp-paid-stamp
source: inspora
category: Motion
status: analyzed
title: "3D paid stamp"
creator: "@SolutionB2u"
styles: [soft-3d, skeuomorphic, corporate-clean, micro-interaction]
patterns: [date-picker-becomes-stamp, 3d-tilt-to-document, rubber-stamp-imprint, undo-toast, segmented-status-control, colour-swatch-picker, post-action-summary]
mode: light
palette: ["#fcfcfc", "#e9e8ec", "#dbdadf", "#cecdd2", "#cf4a4a", "#1c1c1e", "#111111", "#8e8e93"]
type_families: ["Poppins (likely)", "condensed grotesk for stamp (Oswald / Barlow Condensed-like)"]
type_class: [geometric-sans, condensed]
radius_px: [40, 24, 9999]
motion: {durations_s: [0.97, 0.17, 0.3, 0.7, 8.77], easing: [ease-in-out, ease-out], loop: false}
scores: {aesthetics: 8, originality: 9, usability: 8, craft: 8}
craft_signals: [picker-extrudes-into-stamp-block, stamp-date-matches-picker-value, slight-stamp-rotation, double-border-stamp, undo-toast-after-commit, stamp-colour-from-swatch, keyboard-hint-under-cta]
anti_patterns: [stamp-red-just-below-aa, grey-helper-text-low-contrast]
---
# 3D paid stamp — @SolutionB2u

## 1. Snapshot
- **Subject:** An 8.77 s, 1080×720 Figma Motion prototype: pick a payment date on a wheel picker, press "Mark as paid", the camera tilts into 3D, the picker card extrudes into a rubber stamp and presses "PAID 15 SEP 2026" onto the invoice, then returns to a flat invoice view with Download PDF / Next invoice.
- **Why it's remarkable:** The input control literally becomes the tool: the date picker's card grows a black base and is the stamp, so the value you chose is physically printed — a perfect metaphor for "record this date".

## 2. Composition & layout
- **Step 1 (0–1.5 s):** centred column on #f4f4f6: micro-label "NORTHWIND PTY LTD · $1,572.50" (≈ 6 px caps, tracked); title "Invoice FUI-0067" ≈ 17 px semibold; helper line; wheel picker card ≈ 275×160 px (radius ≈ 40 px) with DAY / MONTH / YEAR columns and a "PAID" label + red dot; resolved date line; segmented control (Paid / Received / Approved / Due) + five colour swatches (red, blue, green, violet, black); black pill CTA "Mark as paid" ≈ 90×24 px with "or press Enter" beneath.
- **Step 2 (2–5.4 s):** perspective view of an A4 invoice tilted back ~35°; the picker hovers as an extruded block (≈ 300×250 px at its closest) and descends; after impact a red rectangular stamp sits bottom-right of the invoice; a floating toast "● Marked as paid · 15 Sep 2026 | Undo | Done" appears at the bottom.
- **Step 3 (6.3 s→):** flat invoice preview ≈ 200×290 px with a status line "● Marked as paid on Tuesday, 15 September 2026" and two buttons.

## 3. Typography
- Geometric sans (Poppins): title semibold; invoice headings in Poppins italic ("Invoice", "Description of services"); picker numerals ≈ 16 px semibold with fading neighbours.
- Stamp: condensed bold caps "15 SEP 2026" with a tiny tracked "PAID" above, in a double-rule rectangle — a rubber-stamp typographic idiom.
- Micro labels ≈ 6–7 px caps, tracking ≈ +0.15 em.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #fcfcfc | paper, picker face | 26% |
| #e9e8ec / #dbdadf / #cecdd2 | stage gradients, 3D floor | 72% |
| #cf4a4a (est.) | stamp ink, "PAID" status dot | ~1% |
| #1c1c1e | CTA, stamp base, Done | <1% |
| #111111 | text | — |
| #8e8e93 | helper text (est.) | — |

WCAG checks:
- Stamp red #cf4a4a on paper: **4.33:1** (AA-large only — fine since the stamp text is large and bold).
- Text #111 on stage #f4f4f6: 17.2:1.
- White on black CTA: 17.0:1.
- Helper "or press Enter" ≈#8e8e93 on #f4f4f6: **2.97:1 (fails)**.

## 5. Depth & material
- The picker card has a soft-3D face (white → #e5e5ea vertical gradient, inner top highlight); in 3D it extrudes ≈ 100 px of white "rubber" with a ≈ 10 px black base — the stamp pad.
- The invoice is a flat sheet with a long, soft cast shadow on the grey floor; the stamp imprint has slightly rough, ink-like edges and ≈ −3° rotation.
- The camera move uses a strong perspective (vanishing toward the top), so the stamp block looks heavy.

## 6. Components & patterns
- 3-column wheel date picker with a selected-row pill highlight.
- Segmented status control (Paid / Received / Approved / Due) driving the stamp word; colour swatches driving the ink colour.
- Primary pill CTA with a keyboard shortcut hint.
- Undo toast after a commit — the destructive-ish action stays reversible.
- Post-action screen with secondary (Download PDF, grey pill) and primary (Next invoice, black pill) actions.

## 7. Motion
Measured (m0_motion.json): 8.77 s, 60 fps, motion_fraction 0.23, 4 segments, not a loop (first/last diff 9.39):
- **2.03–3.00 s (0.97 s), peak_at 0.47 → symmetric ease-in-out:** the camera tilts into 3D and the picker lifts off as a block.
- **3.17–3.33 s (0.17 s), peak_at 0.50:** the quick downward press.
- **3.47–3.77 s (0.30 s), peak_at 0.28 → ease-out:** impact and rebound; the imprint appears.
- **5.40–6.10 s (0.70 s), peak_at 0.02 → sharp ease-out:** the camera snaps back to the flat summary view.
- Between 1.46 s and 2.03 s the picker wheel scrolls from 13 to 15 (a sub-threshold movement). The press beat (0.17 + 0.30 s) is a real-world-speed stamp, framed by slower ~1 s camera moves — a good anticipation/impact/settle rhythm.

## 8. Brand system
n/a — not a brand system. Identity cues: a black cat logo on the invoice, "FeralUI Studio / feralui.dev" (a fictional sender).

## 9. UX
- Makes a mundane status change memorable and confirms exactly what was recorded (date and status) three times: the stamp, the toast and the status line.
- Undo is offered immediately; Enter works as a shortcut; status and colour are explicit choices.
- **Risks:** the ≈ 4 s theatrical sequence would grate on bulk invoice processing — it needs a reduced-motion / fast path. The helper text fails contrast.

## 10. Craft signals
- The stamp's printed date (15 SEP 2026) equals the final picker value (15 / SEP / 2026).
- The picker card's corner radius is retained on the extruded block, so the identity of the object is preserved.
- The stamp imprint is rotated ≈ −3° with a double border and a small tracked "PAID" — authentic stamp grammar.
- The status dot in the picker, toast and summary line uses the same red as the ink.
- The toast is a pill with a white Undo (secondary) and a black Done (primary) — consistent button hierarchy with the main CTA.

## 11. Reproduction recipe
```css
:root{--paper:#fcfcfc;--stage:#f4f4f6;--ink:#cf4a4a;--black:#1c1c1e;--muted:#8e8e93;--r-card:40px}
.picker{border-radius:var(--r-card);background:linear-gradient(#fff,#e9e8ec);
  box-shadow:inset 0 1px 0 #fff,0 20px 40px rgba(0,0,0,.08)}
.scene{perspective:1200px} .doc{transform-style:preserve-3d;transition:transform .97s cubic-bezier(.45,0,.55,1)}
.scene.stamping .doc{transform:rotateX(35deg) translateY(-40px)}
.stamp-block{animation:press .47s cubic-bezier(.3,0,.2,1) 1s both}
@keyframes press{0%{transform:translateZ(160px)}36%{transform:translateZ(0) scale(.98)}100%{transform:translateZ(30px)}}
.imprint{color:var(--ink);border:2px solid currentColor;outline:1px solid currentColor;outline-offset:3px;
  transform:rotate(-3deg);font:700 28px/1 "Oswald","Barlow Condensed",sans-serif;
  mask:url(grunge.png);animation:ink .2s ease-out 1.17s both}
@keyframes ink{from{opacity:0;transform:rotate(-3deg) scale(1.08)}}
@media (prefers-reduced-motion:reduce){.doc,.stamp-block{animation:none;transition:none}}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Soft, neutral, Apple-like surfaces with one red accent. |
| Originality | 9 | Picker-becomes-stamp is a genuinely new, meaningful metaphor. |
| Usability | 8 | Triple confirmation, Undo, keyboard path; needs a fast mode. |
| Craft | 8 | Value continuity, stamp details and consistent button hierarchy. |

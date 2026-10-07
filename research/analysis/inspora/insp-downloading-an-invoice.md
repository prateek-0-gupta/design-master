---
id: insp-downloading-an-invoice
source: inspora
category: Product
status: analyzed
title: "downloading an invoice"
creator: "Gabriel (@gabriell_lab)"
styles: [minimal-swiss, physical-material, micro-interaction]
patterns: [receipt-prints-from-slot, side-sheet-over-blurred-table, success-icon-header, paired-secondary-primary-buttons, mono-bracketed-invoice-labels, perforated-paper-edge]
mode: light
palette: ["#ffffff", "#cfcfcf", "#e0e0df", "#999a9d", "#141414", "#2e9e4f", "#efefef"]
type_families: ["Inter (likely)", "JetBrains Mono / IBM Plex Mono (likely)"]
type_class: [neo-grotesk, mono]
radius_px: [40, 9999, 4]
motion: {durations_s: [0.37, 2.03], easing: [ease-in], loop: true}
scores: {aesthetics: 8, originality: 8, usability: 7, craft: 9}
craft_signals: [slot-line-as-printer-mouth, scalloped-tear-edge-on-paper, mono-bracket-section-labels, background-table-blurred-not-dimmed-only, green-only-on-success-and-total, sheet-inset-inside-app-frame]
anti_patterns: [micro-type-in-preview, green-total-below-aa]
---
# downloading an invoice — Gabriel

## 1. Snapshot
- **Subject:** A 2.0 s looping clip (2878×2160) of a right-side sheet saying "Your invoice is ready" over a blurred invoice table. A miniature PDF of a "Grain" invoice slides down out of a thin horizontal slot like a receipt from a printer, and stops above the "New invoice" and "Download Invoice" buttons.
- **Why it's remarkable:** A static success state becomes a physical metaphor. The grey rule under the copy is the printer's mouth, and the paper emerges from behind it with a torn, scalloped bottom edge. It is a delightful, on-topic way to show a document was generated.

## 2. Composition & layout
- **App frame:** about 1775×1360 px in the 2000-px key frame, cropped at the left, with a 40 px radius and a grey (#cfcfcf) blurred table behind.
- **Sheet:** x≈1130–1750 (≈620 px, about 890 px native) and y≈100–1400, inset about 25 px from the app frame on top, right and bottom. Radius about 36 px.
- **Sheet stack (centred):**
  - success icon 44 px at y≈250;
  - title at y≈307;
  - 2-line body at y≈346–376;
  - the slot rule at y≈433 (≈455 px wide, 3 px thick);
  - the paper (≈450×640 px) beneath it;
  - buttons pinned to the bottom at y≈1333: two equal halves, each ≈265×60 px, with a 10 px gap.
- The close ✕ is a 40 px circle at top right.

## 3. Typography
- **UI:** neo-grotesk close to Inter.
  - Title "Your invoice is ready" about 24 px Medium.
  - Body about 19 px Regular, centred, leading about 1.55.
  - Buttons about 20 px Medium.
- **Invoice:**
  - The "Grain" wordmark is a light grotesk.
  - Labels are tiny mono uppercase in brackets ("[ FROM ]", "[ BILL TO ]", "[ PAY BY STABLECOIN ]") at about 7–8 px in the key frame.
  - Values and amounts are in mono. The total "$144.38 USD" is in green mono.
- The bracketed-mono label system gives the document a machine-printed, receipt-like voice.

## 4. Colour
| Hex | Role | Approx share |
|---|---|---|
| #ffffff | sheet, paper, page | 43% |
| #cfcfcf | blurred app background | 41% |
| #e0e0df | frame edge, slot rule, paper header band | 14% |
| #999a9d | blurred table text, secondary labels | 2.5% |
| ≈#141414 | primary button, title | <1% |
| ≈#efefef | secondary button | <1% |
| ≈#2e9e4f | success icon, total due | <1% |

WCAG checks (contrast.py):
- Title #111 on white: **18.88:1**.
- Primary button white on #141414: **18.42:1**.
- Secondary button #111 on #efefef: **16.42:1**.
- Body ≈#3a3a3a: **11.37:1**.
- Total due green ≈#2e9e4f on white: **3.43:1** (large only).
- Grey mono labels ≈#8a8a8a: **3.45:1**.

## 5. Depth & material
- **Background:** the app is blurred (about 6–8 px) and greyed rather than covered by a dark scrim, so context stays legible as shape.
- **Sheet:** white with no shadow, separated by the grey frame around it.
- **Paper:**
  - a very soft shadow (about 0 20px 40px rgba(0,0,0,.06));
  - a grey header band (#f4f4f4) for From / Bill to;
  - a **scalloped / perforated bottom edge** (a semicircle pattern about 8 px), signalling torn-off paper.
- **The slot:** a 3 px grey line with slightly rounded ends. The paper is masked so that it appears to emerge from under it.

## 6. Components & patterns
- **Success header:** a green download-tray icon with a dashed-corner frame, then the title and body.
- **Document preview** that is generated, not a thumbnail: the full invoice layout at reduced scale.
- **Paired buttons:** secondary grey pill "New invoice" and primary black pill "Download Invoice" with a cloud-download icon. They are equal width, with the primary on the right.
- **Close button:** a circular ghost.

## 7. Motion
- Measured: 2.03 s at 30 fps. `motion_fraction` 0.19. One segment: **0.37 s ease-in (peak_at 0.68) from 0.53 to 0.90 s**. `seamless_loop_likely: true`.
- **From frames (estimates):**
  - 0.11–0.34 s: only the bottom footer strip of the invoice is visible below the slot, so the paper starts mostly "inside" the printer.
  - 0.56 s: about 40% has emerged.
  - 0.79 s: about 95%.
  - 1.02 s: the paper sits about 20 px lower (a small overshoot as it drops).
  - 1.24 s onward: it settles back. A settle of about 0.2 s.
- The ease-in (accelerating) profile reads as paper being pushed out with increasing speed, then a gentle catch. It is an apt physical cue.

## 8. Brand system
n/a — not a brand system. Within the mock invoice, "Grain" uses a leaf mark, a light grotesk wordmark and the bracket-mono labelling, which form a coherent mini identity.

## 9. UX
- Clear success feedback, with the artefact previewed before download. The primary action is unambiguous.
- **Risks:**
  - The preview text is too small to verify any amount except the total.
  - The total-due green is below AA.
  - The animation should respect reduced motion.
  - "New invoice" and "Download" share equal weight in width, though colour separates them.

## 10. Craft signals
- The divider under the body copy doubles as the printer slot (a functional rule reused as a metaphor).
- The paper's bottom edge is scalloped like a tear-off receipt.
- Labels inside the invoice are wrapped in brackets and set in uppercase mono (e.g. "[ PAY BY BANK TRANSFER ]").
- Green appears only on the success icon and the total due, which links "done" to the amount.
- The sheet is inset inside the rounded app frame with an even 25 px margin rather than flush to the edge.
- The background is blurred, which keeps the invoice list readable as context without competing.

## 11. Reproduction recipe
```css
:root{--ink:#111;--muted:#8a8a8a;--line:#e0e0df;--ok:#1f8a43;--btn:#141414;--btn-2:#efefef;--r-sheet:36px}
.sheet{background:#fff;border-radius:var(--r-sheet);padding:120px 40px 24px;display:grid;justify-items:center}
.slot{width:74%;height:3px;border-radius:2px;background:var(--line);position:relative;z-index:2}
.paper-window{width:73%;overflow:hidden;margin-top:-2px}            /* masks paper above the slot */
.paper{background:#fff;box-shadow:0 20px 40px -10px #0000000f;font:400 8px/1.4 "JetBrains Mono",monospace;
  -webkit-mask:radial-gradient(4px at 50% 100%,#0000 98%,#000) 0 0/8px 100%;   /* scalloped bottom */
  animation:print .37s cubic-bezier(.55,0,1,.45) .53s both, settle .22s ease-out .9s both}
@keyframes print{from{transform:translateY(-92%)}to{transform:translateY(3%)}}
@keyframes settle{from{transform:translateY(3%)}to{transform:none}}
.label{text-transform:uppercase;color:var(--muted)} .label::before{content:"[ "} .label::after{content:" ]"}
.actions{display:grid;grid-template-columns:1fr 1fr;gap:10px;width:100%}
.actions .primary{background:var(--btn);color:#fff;border-radius:9999px;height:60px}
.actions .secondary{background:var(--btn-2);color:var(--ink);border-radius:9999px}
@media (prefers-reduced-motion:reduce){.paper{animation:none}}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Monochrome restraint; the paper and receipt detailing are charming. |
| Originality | 8 | The divider-as-printer-slot metaphor is a genuinely clever reuse. |
| Usability | 7 | Clear success and CTA; the preview is unreadable and the total is low-contrast. |
| Craft | 9 | Scalloped edge, bracket-mono labels, settle overshoot and even insets. |

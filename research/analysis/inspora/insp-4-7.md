---
id: insp-4-7
source: inspora
category: Motion
status: analyzed
title: "Receipt Printer"
creator: "@dqnamo"
styles: [physical-material, dark-premium, terminal-mono, skeuomorphic]
patterns: [receipt-print-out-confirmation, device-slot-reveal, status-line-progress, mono-receipt-ledger, zigzag-tear-edge, replay-control]
mode: mixed
palette: ["#111111", "#171717", "#1e1d1b", "#e8e8e6", "#1d1c1a", "#359a5e", "#a1a1a1", "#fdfdfd"]
type_families: ["Inter (likely)", "Geist Mono / JetBrains Mono-style monospace (likely)"]
type_class: [neo-grotesk, mono]
radius_px: [28, 20, 12, 9999]
motion: {durations_s: [0.83, 1.74], easing: [ease-in-out, ease-in], loop: false}
scores: {aesthetics: 8, originality: 8, usability: 7, craft: 9}
craft_signals: [zigzag-tear-edge-on-receipt, slot-lip-overlaps-paper, mono-for-receipt-sans-for-ui, status-copy-changes-with-stage, barcode-encodes-order-id, tabular-right-aligned-amounts]
anti_patterns: [receipt-meta-labels-low-contrast]
---
# Receipt Printer — @dqnamo

## 1. Snapshot
- **Subject:** A 12.5 s, 1920×1080 capture of a checkout success state. A dark "printer" card (Pro plan, £230.40) feeds out a paper receipt from its bottom slot, cycling the status from "Processing your order" to "Printing your receipt" to "Order complete". It is shown in light mode first (t≈0.7–3.5 s), then dark.
- **Why it's remarkable:** It turns a post-payment confirmation into a physical artefact: the receipt is the success state.

## 2. Composition & layout
- **Page:** A component-gallery page with the title "Receipt Printer" (about 20 px Medium) and a two-line description (about 18 px). Both sit left-aligned at x≈495 above a framed stage of about 950 px with a radius of about 20.
- **Printer card:** About 474 px wide (x 724→1198), with a radius of about 28. It contains:
  - a header row with the logo tile and a "Home" pill;
  - an inner summary panel (radius about 12) holding "Pro plan / Annual subscription" on the left and "Total £230.40" on the right, plus a status row;
  - a slot bar about 414 px wide at the bottom.
- **Receipt:** About 380 px wide (x 770→1150) and about 490 px tall. It is inset about 46 px from each card edge, so it visibly comes out of the slot.
- **Replay:** A ghost button sits at the top-right of the stage.

## 3. Typography
- **UI:** Inter-like sans. "Pro plan" is about 18 px Medium and "£230.40" about 21 px Semibold. Labels are about 15 px in grey.
- **Receipt:** Set in monospace.
  - Uppercase tracked headers ("PRO PLAN", "TOTAL PAID") at about 11 px Bold with about +0.12 em tracking.
  - Amounts right-aligned, with "£230.40" at about 18 px.
  - Meta rows ("Order", "Paid with", "Date") at about 10 px.
- The sans-to-mono switch marks the boundary between screen and paper.

## 4. Colour
| Hex | Role |
|---|---|
| #111111 | page (dark mode) |
| #171717 / #1e1d1b | stage and printer surfaces |
| #e8e8e6 | receipt paper (warm off-white) |
| #1d1c1a | receipt ink, logo tile |
| #359a5e | success check |
| #a1a1a1 | secondary UI text |
| #fdfdfd | page (light mode) |

WCAG:
- White on #171717 is 17.93:1.
- Grey #a1a1a1 on #111 is 7.31:1.
- Receipt ink #1d1c1a on #e8e8e6 is 13.88:1.
- Receipt meta grey (about #8a8a88) on paper is **2.82:1** (fails).

## 5. Depth & material
- **Printer:** It sits on the stage with a soft drop shadow and a faint 1 px lighter top edge. The inner panel is darker (inset look).
- **Slot:** The bar is the darkest element and overlaps the receipt top, which sells the "paper behind the lip" illusion.
- **Receipt:** Matte paper with no gloss. A saw-tooth bottom edge (about 8 px teeth) reads as torn thermal paper, and a 1 px dotted rule divides its sections.

## 6. Components & patterns
- A status row with an icon that morphs from spinner to green check, with copy that tracks the stage.
- **Receipt ledger:**
  - logo tile;
  - item line;
  - subtotal and tax;
  - an emphasised total;
  - order meta (ORD-2048, "Visa •••• 4242", "11 AUG 2026 · 14:32");
  - a barcode with the order ID caption.
- A Replay button to re-trigger the sequence.

## 7. Motion
- **Measured:** Two segments across 12.48 s, `seamless_loop_likely: false` (it is a replay demo, not a loop).
  - 1.94–2.77 s: 0.83 s, peak 0.50 (symmetric ease-in-out). The receipt feeding out in light mode.
  - 8.01–9.74 s: 1.74 s, peak 0.68 (ease-in). The dark-mode print, a slower feed that accelerates and settles out of the slot.
- **Frames (estimate):** The status text changes about 0.5 s before paper moves, so the copy leads the motion. The receipt grows downward and stays clipped at the slot.

## 8. Brand system
n/a — not a brand system. Identity cues: a four-point sparkle logomark repeated in the header tile and the receipt, and a warm-black and paper palette.

## 9. UX
- Strong reassurance: the user sees processing, then printing, then complete, with a tangible record.
- The receipt includes every field a real receipt needs.
- **Risks:**
  - The animation delays access to the "Home" action.
  - Small mono meta text is low-contrast.
  - A real implementation needs a way to download or email the receipt.

## 10. Craft signals
- Saw-tooth tear edge at the receipt bottom.
- The slot lip overlaps the paper by about 4 px so it emerges from behind.
- Sans is used for the device UI and mono for the receipt: two voices with one meaning each.
- Amounts are right-aligned on one column edge (x≈1121).
- The barcode caption repeats the order ID (ORD 2048).
- The same layout is fully themed in both light and dark modes.

## 11. Reproduction recipe
```css
:root{--page:#111;--stage:#171717;--device:#1e1d1b;--paper:#e8e8e6;--ink:#1d1c1a;--ok:#359a5e;--muted:#a1a1a1}
.printer{width:474px;border-radius:28px;background:var(--device);padding:16px;box-shadow:0 20px 50px rgba(0,0,0,.5),inset 0 1px 0 rgba(255,255,255,.06)}
.slot{height:8px;margin:18px 14px 0;border-radius:9999px;background:#0b0b0b;position:relative;z-index:2}
.receipt{width:380px;margin:-4px auto 0;background:var(--paper);color:var(--ink);font:12px/1.6 "Geist Mono",ui-monospace,monospace;
  padding:32px 30px 40px;clip-path:inset(0 0 100% 0);animation:feed 1.7s cubic-bezier(.55,0,.35,1) forwards;
  -webkit-mask:linear-gradient(#000 0 0) top/100% calc(100% - 8px) no-repeat,
    conic-gradient(from -45deg at bottom,#0000,#000 1deg 89deg,#0000 90deg) bottom/16px 8px repeat-x}
@keyframes feed{to{clip-path:inset(0 0 0 0)}}
.receipt .amt{font-variant-numeric:tabular-nums;text-align:right}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Warm-black device against paper is tactile and refined in both themes. |
| Originality | 8 | The receipt-as-success-state is a memorable reframing of checkout. |
| Usability | 7 | Clear staged feedback, but the delay and low-contrast meta matter in real use. |
| Craft | 9 | Tear edge, slot overlap, mono ledger and barcode ID show meticulous detail. |

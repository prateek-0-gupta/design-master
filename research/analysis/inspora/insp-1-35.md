---
id: insp-1-35
source: inspora
category: Motion
status: analyzed
title: "Print Receipt"
creator: "@jeetnirnejak"
styles: [skeuomorphic, micro-interaction, terminal-mono, corporate-clean]
patterns: [print-out-reveal, line-by-line-progress-counter, zigzag-paper-edge, tear-off-reset, container-height-morph, qr-payment-block, status-label-swap]
mode: light
palette: ["#ffffff", "#f2f2f2", "#e3e3e4", "#d0d0d2", "#adacae", "#111111"]
type_families: ["Inter / SF Pro Text (likely)", "JetBrains Mono / Geist Mono (likely)"]
type_class: [neo-grotesk, mono]
radius_px: [48, 9999, 12]
motion: {durations_s: [0.23, 0.3, 0.27, 1.07], easing: [ease-out, ease-in], loop: false}
scores: {aesthetics: 8, originality: 8, usability: 8, craft: 9}
craft_signals: [line-counter-printing-n-of-14, zigzag-perforation-top-and-bottom, mono-only-on-paper, dashed-rule-section-breaks, tabular-right-aligned-amounts, container-grows-with-paper, contextual-footer-hint]
anti_patterns: [faint-footer-hint-text]
---
# Print Receipt — @jeetnirnejak

## 1. Snapshot
- **Subject:** A 1924×1518, 5.57 s, 60 fps capture of a "Receipt #4471" card. It goes from "Order ready → Print receipt" to a thermal-paper receipt that prints line by line (with a "printing 13/14" counter) and ends with a QR "Scan to pay" block and a "Tear off" reset.
- **Why it's remarkable:** A mundane confirmation becomes a believable physical event. Paper extrudes from a slot with a zigzag tear edge, the header counts printed lines in mono, and the final affordance ("Tear off") completes the metaphor as the reset action.

## 2. Composition & layout
- **Card:** a single centred card (key frame is ~1:1 with the source) ≈722 px wide, on pure white.
- **Header bar:** "Receipt" + "#4471" chip on the left and a status on the right, at y≈405, with ≈48 px side padding.
- **Paper:** a white strip ≈680 px wide, inset ≈21 px from the card edge, with ≈40 px internal padding.
- **Footer:** a hint line sits ≈60 px below the paper.
- **Growth:** the card grows in height as the receipt prints. ≈240 px tall in the idle state (0.31 s), ≈835 px at 13/14 lines, ≈930 px at completion (3.40 s). It stays centred, so it expands up and down symmetrically.
- **Receipt structure:** merchant block (centred, 4 lines), dashed rule, items, dashed rule, subtotal / service / tax, **TOTAL**, dashed rule, "Thank you ✦", "Scan to pay · UPI", ≈160 px QR, UPI ID.

## 3. Typography
- **UI chrome:** a neo-grotesk. "Receipt" is ≈28 px semibold. Footer hints are ≈20 px regular in grey.
- **Paper:** a monospace (JetBrains Mono / Geist Mono-like) in two sizes:
  - merchant name at ≈26 px, uppercase, tracking ≈+0.15em, bold;
  - body at ≈21 px, with line pitch ≈45 px for an airy thermal-print feel;
  - "TOTAL ₹494.50" in bold at ≈26 px.
- **Amounts:** right-aligned on the same column edge (x≈1262), with tabular figures.
- **Status counter** "printing 13/14": mono, grey, in the header. The grotesk–mono split cleanly separates *interface* from *artifact*.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #ffffff | page, receipt paper | 91% |
| #f2f2f2 | card shell (printer body) | 6% |
| #e3e3e4 | #4471 chip, hairline | 1% |
| #d0d0d2 / #adacae | dashed rules, card shadow, footer grey | 1% |
| #111111 | receipt ink, button fill (#1a1a1a) | <1% |

WCAG checks:
- Ink #111 on paper: **18.88:1**.
- Grey meta lines (≈#6b6b70) on white: 5.3:1.
- White label on the black "Print receipt" button: 17.4:1.
- The chip's text: 5.79:1.
- **The footer hint "Printing… / Tear off the receipt to reset" (≈#9a9a9e on #f2f2f2) is 2.5:1, a failure.**

## 5. Depth & material
- **Card:** the card shell is the "printer". It is light grey with a large soft shadow (≈0 30px 60px rgba(0,0,0,.08)) and a radius of ≈48 px.
- **Paper:** flat white with no shadow. It is defined by the shell colour around it and a crisp **zigzag edge** of ≈14 px teeth at both the top and the bottom.
- **Feed slot:** the top zigzag suggests the paper emerges from under the header, as if from a feed slot.
- **Rules:** dashed hairlines (1 px, ≈4/4 dash) replace solid dividers, a thermal-receipt idiom.

## 6. Components & patterns
- **Idle state:** a white inner panel with a document icon in a 44 px circle, "Order ready", item summary, and a black pill CTA "Print receipt".
- **Header status slot:** cycles "Ready" → "printing 4/14" → "printing 8/14" → "printing 13/14" → a "↻ Tear off" pill button. One slot carries state, progress and the next action.
- **Footer hint:** contextual: "Tap print to issue…" → "Printing…" → "Tear off the receipt to reset".
- **Tag chip:** "#4471" in a 12 px-radius grey chip.

## 7. Motion
- **Measured:** 5.57 s at 60 fps. motion_fraction 0.33. Four segments:
  - 1.00–1.23 s (0.23 s, peak 0.21, **ease-out**): the idle panel collapsing into the paper;
  - 1.37–1.67 s (0.30 s, ease-in);
  - 1.83–2.10 s (0.27 s, symmetric);
  - 2.23–3.30 s (1.07 s, peak 0.83, **ease-in**): the long print feed that accelerates toward the QR and the final card growth.
- **Not a loop:** seamless_loop_likely is false.
- **From frames (estimates):**
  - The click lands at ≈0.93 s.
  - Printing runs ≈1.0–3.3 s for 14 lines, about 0.16 s per line, stepwise like a real thermal printer.
  - The card height animates in sync with the paper, so the container is never taller than its content.
  - From 3.40 to 5.26 s it is static in the done state.

## 8. Brand system
n/a — not a brand system. A merchant identity ("Blue Tokai Coffee", Bangalore, ₹, UPI) gives realistic local context.

## 9. UX
- **Strengths:**
  - Progress is explicit (n/14).
  - The flow has a clear start CTA and a clear, metaphor-consistent reset ("Tear off").
  - The QR is the end goal and lands last, at the bottom, where attention ends.
  - Amounts are easy to scan because of the shared right edge and tabular mono.
- **Risks:**
  - The faint footer hints are below AA.
  - A 2.3 s print time is charming once but slow for repeated cashier use; it needs a skip or instant mode.

## 10. Craft signals
- The header counter reads "printing 4/14 → 8/14 → 13/14" in mono, so it maps to actual line count.
- Zigzag perforation appears on **both** the top and bottom paper edges, with a tooth pitch of ≈14 px.
- Monospace is confined to the paper; the chrome uses the grotesk.
- Dashed 1 px rules group merchant, items, totals and payment.
- All currency values share one right edge at x≈1262 with tabular digits.
- The card height grows in lockstep with the paper (≈240 → 835 → 930 px).
- The status slot turns into the "Tear off" button, reusing the same location for the next action.

## 11. Reproduction recipe
```css
:root{--shell:#f2f2f2;--paper:#fff;--ink:#111;--muted:#6b6b70;--rule:#d0d0d2;
  --sans:"Inter",system-ui;--mono:"JetBrains Mono","Geist Mono",ui-monospace}
.printer{width:361px;border-radius:24px;background:var(--shell);box-shadow:0 15px 30px rgba(0,0,0,.08);
  padding:16px 10px 20px;transition:height .25s cubic-bezier(.3,0,.2,1);overflow:hidden}
.paper{background:var(--paper);font:400 10.5px/22px var(--mono);color:var(--ink);padding:20px;
  --z:7px;-webkit-mask:
   conic-gradient(from -45deg at bottom,#0000,#000 1deg 89deg,#0000 90deg) bottom/calc(2*var(--z)) 51% repeat-x,
   conic-gradient(from 135deg at top,#0000,#000 1deg 89deg,#0000 90deg) top/calc(2*var(--z)) 51% repeat-x}
.paper hr{border:0;border-top:1px dashed var(--rule)}
.amt{text-align:right;font-variant-numeric:tabular-nums}
.paper .line{clip-path:inset(0 0 100% 0);animation:feed .16s steps(4) forwards}
@keyframes feed{to{clip-path:inset(0)}}
.status{font:400 11px var(--mono);color:var(--muted)}
```
JS: append each line with a delay of `i*160ms` and update `status.textContent = \`printing ${i}/${n}\``.

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Restrained greys, with a believable thermal-paper artifact against neat chrome. |
| Originality | 8 | The physical-print metaphor carried all the way to a "tear off" reset is delightful. |
| Usability | 8 | Explicit progress, clear CTAs, scannable totals; faint hints and the print delay cost a point. |
| Craft | 9 | Mono/sans split, zigzag on both edges, synced container growth, consistent right edge. |

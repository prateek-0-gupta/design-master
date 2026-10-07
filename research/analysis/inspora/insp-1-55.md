---
id: insp-1-55
source: inspora
category: Motion
status: analyzed
title: "Portfolio Boarding Pass"
creator: "@cameronmoll"
styles: [physical-material, skeuomorphic, editorial-serif, micro-interaction]
patterns: [swipe-to-enter-gate, boarding-pass-identity-card, card-reader-status-lcd, white-flash-scene-transition, timeline-flight-path, progressive-blur-footer, shimmer-hint-text]
mode: light
palette: ["#f9f3f3", "#ebe6e6", "#dad3d5", "#0a0a0b", "#757373", "#9b9899", "#3d3dd6", "#f5c400"]
type_families: ["Inter / Söhne-style grotesk (likely)", "JetBrains Mono / Space Mono-style monospace (likely)"]
type_class: [neo-grotesk, mono]
radius_px: [24, 16, 9999]
motion: {durations_s: [0.27, 0.4, 0.97], easing: [ease-in, ease-in-out], loop: false}
scores: {aesthetics: 9, originality: 9, usability: 6, craft: 9}
craft_signals: [lcd-status-ready-to-reading, amber-led-glow-on-read, full-boarding-pass-microtype, tracked-mono-coordinates, dashed-flight-path-into-timeline, bottom-progressive-blur-under-nav, airplane-window-hero, skip-link-escape-hatch]
anti_patterns: [hint-and-meta-grey-below-aa, gimmick-gate-delays-content]
---
# Portfolio Boarding Pass — @cameronmoll

## 1. Snapshot
- **Subject:** An 8.4 s, 2192×1730 recording of a personal portfolio intro. The visitor drags a rendered boarding pass ("MIKE BARTON, MAN → REM") into a white card-reader whose LCD flips from "READY" to "READING" with an amber LED. The screen washes to white, then reveals an airplane-window hero and a "flight plan" career timeline.
- **Why it's remarkable:** The whole travel metaphor is carried through convincingly: ticket microtype, reader hardware, window view, coordinates, "RETURN TO GATE" nav. The gate is a single gesture.

## 2. Composition & layout
- **Gate screen:** a single centred column on a warm off-white (#f9f3f3).
  - The pass is about 620×305 px in the 1600-px frame (≈850×420 real), centred at y≈440.
  - The reader is about 630×210 px, 130 px below the pass.
  - The hint "Swipe boarding pass to enter" sits 65 px below the reader, and "Skip" sits bottom-right.
- **Portfolio screen (f5):**
  - A centred header of four mono lines (name, city, coordinates, timezone).
  - An airplane window about 260×350 px.
  - Title plus a two-line intro centred about 650 px wide.
  - A left-hanging timeline: year column at x≈290, node at x≈362, content at x≈394, so the content column is about 800 px wide and left-aligned.
- **Nav:** pinned bottom-centre ("RETURN TO GATE · X · LINKEDIN · EMAIL") over a progressive blur and fade band of about 150 px.

## 3. Typography
- **Mono:** for every "system" string, tracked wide (≈+0.15 em) and in caps: name, coordinates, "FLIGHT PLAN", "CURRENT", nav, year labels, and the ticket fields (MIKE BARTON, TD1887, 08:45). Header lines are about 17 px, with the name in black and the rest grey.
- **Sans:** an Inter or Söhne-like grotesk for human content: role "Software Designer & Creative Technologist" about 22 px medium; intro about 21 px regular grey at about 1.75 line-height; company "Studio" about 22 px medium; role title about 20 px medium; descriptions about 20 px regular.
- **LCD:** the reader display uses a segmented dot-matrix face ("READY", "READING").
- The split is clear: mono for data the "machine" knows, sans for the person's own words.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #f9f3f3 | page (warm blush white) | ~90% |
| #ebe6e6 / #dad3d5 | reader body, pass paper | 5% |
| #0a0a0b | primary text, LCD bezel | 2% |
| #757373 | body grey | 2% |
| #9b9899 | meta grey (coordinates, hint) | 1% |
| #3d3dd6 (approx) | accent: "CURRENT", plane icon, ticket labels, timeline nodes | <1% |
| #f5c400 (approx) | reader LED and LCD while reading | moment |

WCAG checks:
- Black on page is 18.04:1.
- Accent blue is 6.75:1.
- Body grey #757373 is 4.30:1 (large text only, and body runs at about 20 px so it is borderline).
- Meta grey #9b9899 is **2.61:1 (fails)**.

## 5. Depth & material
- **Boarding pass:** a textured paper card with a topographic line pattern in faint violet, a stub with a perforation, a barcode, and a circular globe seal. Corners are about 24 px, and the card has a soft ground shadow.
- **Reader:** a white plastic box with a slot lip, subtle speckle texture, an inset black LCD and a round LED. On read, the LED blooms amber with about a 30 px glow.
- **Window:** the airplane window is a 3D-rendered bezel with layered rings and a sky/cloud photo, with a large soft halo around it.
- **Timeline:** company logos sit as overlapping 40 px circles. A dashed curved path runs from the "FLIGHT PLAN" plane down into the solid timeline rule.

## 6. Components & patterns
- **Swipe-to-enter gate:** drag the pass downward into the slot. The pass tilts about 8° when lifted (f2) and slides into the reader (f3).
- **Status LCD:** READY → READING (amber).
- **Skip link** for the impatient.
- **Career timeline:** year plus route ("NYC→MAN" micro-label), a node, a company with a "CURRENT" badge, the role, a description, and a nested project row (thumbnail plus name plus one-liner).
- **Live header:** the coordinates change between frames (53.2964° vs 53.4888°), suggesting live or animated values.

## 7. Motion
Measured: 8.36 s at 60 fps, 3 segments, motion fraction 0.19, not a loop.
- **2.60–2.87 s (0.27 s, peak 0.94 → ease-in):** The pass accelerates into the slot.
- **3.17–3.57 s (0.40 s, peak 0.79 → ease-in):** The reader state and a white flood cut away the gate. The key frame at about 4.2 s is an almost blank #f9f3f3, the hold between scenes.
- **6.27–7.23 s (0.97 s, peak 0.50 → symmetric ease-in-out):** A smooth scroll down the timeline.
- **Between segments:** The portfolio reveal (4.2 → 5.1 s) is a fade-in from the blank page, about 0.6 s (estimate, below the motion threshold so soft). The hint text shows a left-to-right shimmer (in f0, "pass to en" is darker than the surrounding words).

## 8. Brand system
n/a — not a brand system, but a coherent personal identity. Cues: the fictional "Northern Air" ticket livery (globe mark, blue diagonal stripes); travel vocabulary for navigation ("Flight plan", "Return to gate", "Skip"); and the mono-caps "manifest" voice for metadata.

## 9. UX
- **Strengths:** A memorable first impression with an escape hatch ("Skip"). The timeline is clearly structured, and the nav stays reachable.
- **Risks:**
  - The gate costs about 4 s before any content appears.
  - The drag gesture needs a keyboard or click alternative (presumably Skip).
  - Grey hint and meta text fail AA.
  - The heavy bottom blur hides the next item until scrolled.

## 10. Craft signals
- The ticket carries real-looking microtype: GATE A12, BOARDING 08:45, SEAT 18A, CLASS J, SEQ 0029, plus a duplicated stub.
- The LCD changes copy and colour on read, and the LED gets an amber bloom.
- The pass rotates about 8° while dragged, a physical "pick-up" cue.
- A dashed bezier path connects the "FLIGHT PLAN" plane icon to the first timeline node.
- The mono metadata is tracked wide; the sans body is not.
- The bottom nav sits on a progressive blur plus fade, not a hard bar.
- Accent blue is used only for the plane, "CURRENT", nodes and ticket labels.

## 11. Reproduction recipe
```css
:root{--page:#f9f3f3;--ink:#0a0a0b;--body:#5f5d5d;--meta:#757373;--accent:#3d3dd6;--led:#f5c400;
  --mono:"JetBrains Mono",ui-monospace,monospace;--sans:"Inter",system-ui,sans-serif;}
body{background:var(--page);color:var(--ink);font-family:var(--sans)}
.meta{font:400 15px/1.8 var(--mono);letter-spacing:.15em;text-transform:uppercase;color:var(--meta);text-align:center}
.pass{border-radius:24px;box-shadow:0 20px 40px rgba(60,40,40,.12);cursor:grab;transition:transform .27s cubic-bezier(.5,0,.75,0)}
.pass:active{transform:rotate(-8deg) translateY(-6px)}
.reader .lcd{background:#0d0d0d;font-family:"DotGothic16",var(--mono);color:#8a8a8a;letter-spacing:.2em}
.reader[data-state=reading] .lcd{color:var(--led)}
.reader[data-state=reading] .led{background:var(--led);box-shadow:0 0 30px 8px rgba(245,196,0,.6)}
.hint{background:linear-gradient(90deg,#9b9899 40%,#0a0a0b 50%,#9b9899 60%) 0/300% 100%;
  -webkit-background-clip:text;color:transparent;animation:shimmer 2.4s linear infinite}
@keyframes shimmer{to{background-position:-100% 0}}
.dock{position:fixed;inset:auto 0 0;height:150px;backdrop-filter:blur(8px);
  mask:linear-gradient(transparent,#000 60%);background:linear-gradient(transparent,var(--page))}
.timeline .node{width:14px;height:14px;border:1px solid var(--accent);border-radius:50%}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 9 | Warm, quiet palette with beautifully rendered props and a disciplined mono/sans split. |
| Originality | 9 | A swipe-to-board gate is a fresh portfolio entrance, and the metaphor extends into the nav and timeline. |
| Usability | 6 | Gated entry plus grey meta text below AA; it is rescued by Skip and a clear timeline. |
| Craft | 9 | Ticket microtype, LCD states, dashed flight path, progressive blur: obsessive detail. |

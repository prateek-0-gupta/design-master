---
id: insp-boarding-pass-printer
source: inspora
category: Motion
status: analyzed
title: "boarding pass printer"
creator: "Damir Sokolovsky (@heydamir)"
styles: [skeuomorphic, minimal-swiss, micro-interaction, physical-material]
patterns: [receipt-printer-reveal, ticket-stub-perforation, scalloped-tear-edge, key-value-ticket-grid, mono-labels-sans-values, sticky-primary-cta, slot-mask-gradient, tear-off-gesture]
mode: light
palette: ["#e4e5e9", "#ffffff", "#1a1a1a", "#2a2a2c", "#8e8e8e", "#8a8aa0", "#5e5aa0", "#f25b6a"]
type_families: ["Suisse Int'l / Neue Haas-style grotesk (likely) for values", "Fragment Mono / IBM Plex Mono-style (likely) for labels"]
type_class: [neo-grotesk, mono]
radius_px: [9999, 56, 28]
motion: {durations_s: [2.37, 0.23, 0.63, 2.4, 0.13, 0.53, 1.6], easing: [linear, ease-in-out, ease-in], loop: false}
scores: {aesthetics: 9, originality: 8, usability: 7, craft: 9}
craft_signals: [slot-shadow-gradient-masks-paper, perforation-notches-at-stub, scalloped-bottom-edge, mono-label-sans-value-pairs, paper-curls-on-tear, linear-feed-speed]
anti_patterns: [mono-labels-below-aa, cta-overlaps-printing-ticket]
---
# boarding pass printer — Damir Sokolovsky

## 1. Snapshot
- **Subject:** An 11.3 s, 1244×2160 iPhone prototype of an "Upcoming Trip" screen. A boarding pass is fed out of a dark slot like a thermal receipt printer, pauses, is torn off (it rotates and falls away), and a new one prints.
- **Why it's remarkable:** One physical metaphor (a printer slot) explains loading, the reveal and dismissal. The paper genuinely emerges from *behind* the slot, with a gradient shadow selling the depth.

## 2. Composition & layout
- **Phone:** about 860×1840 px within the 1244×2160 frame, on a #e4e5e9 backdrop. It has a 10 px dark-grey bezel and a screen radius of about 56 px.
- **Header:**
  - back circle (90 px, white, soft shadow) on the left;
  - "Upcoming Trip" about 36 px Semibold centred, over "Minsk → Almaty" about 26 px grey;
  - a "…" circle with a red notification dot on the right.
- **Printer slot:** a dark (#2a2a2c → #3f3f3f) rounded bar of about 730×175 px with a radius of about 28 px, at y≈380.
- **Ticket:** about 625 px wide (about 54 px inset from each slot edge), white.
  - Sections: airline wordmark + PNR; Departure/Arrival (MSQ → ALA, IATA codes about 52 px); Date + "Economy class" chip; Passenger; Flight/Boarding; Terminal/Gate/Seat in 3 columns; Duration/Baggage.
  - Hairline dividers (#ececec) separate the sections.
  - A dashed perforation with semicircular side notches about 30 px across, then the barcode stub (about 540×110 px) and "Valid for boarding".
  - A scalloped bottom edge with 9 scallops.
- **Bottom:** a full-width black pill "Add to Apple Wallet" (about 750×95 px) with the Wallet icon, and an underlined text link "View trip details" below.

## 3. Typography
- **Labels:** "Departure", "Passenger Name", "Gate" are in a monospace at about 20 px Regular in grey #8e8e8e. This is the typewriter or thermal-print voice.
- **Values:** in a neo-grotesk at about 30 px Medium, #1a1a1a. IATA codes are about 52 px Semibold.
- **Times:** "20:00" and "03:10" are about 46 px in a muted lavender-grey (#8a8aa0), subordinate to the airport codes.
- **Airline wordmark:** about 30 px, in an indigo #5e5aa0.
- The mono-label plus sans-value pairing is the system's signature.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #e4e5e9 | backdrop | 40% |
| #ffffff | screen + ticket | 42% |
| #1a1a1a | values, barcode | 5% |
| #2a2a2c / #3f3f3f | printer slot, CTA | 5% |
| #8e8e8e | mono labels | 2% |
| #8a8aa0 | times | <1% |
| #5e5aa0 | airline wordmark | <1% |
| #f25b6a | notification dot | <1% |

WCAG:
- Values #1a1a1a on white are 17.4:1, and the CTA (white on #2a2a2c) is 14.32:1.
- Mono labels #8e8e8e are **3.28:1 at about 20 px (fail)**.
- Times #8a8aa0 are 3.37:1 (large, pass-large).
- The wordmark #5e5aa0 is 6.09:1.

## 5. Depth & material
- **The slot is the hero:**
  - a matte dark bar with a slightly lighter top lip;
  - an inner dark recess;
  - a strong gradient overlay (black to transparent over about 100 px) where the paper emerges, so the top of the ticket is in shadow inside the slot.
- **The ticket:** casts a large, very soft shadow (about 60 px blur, 6% black) onto the screen. When torn away it shows paper curl (f2: a slight skew/warp of about 3° and a wavy top edge).
- **Buttons:** white circles with a 0 4px 16px soft shadow.

## 6. Components & patterns
- A printer-feed reveal as the loading state.
- **Ticket anatomy:** label/value grid with left, centre and right alignment for 3-up rows, a pill chip ("Economy class") with a 1 px border and a light shadow, a dashed route line with a plane icon, a perforation with notches and a barcode stub.
- **Tear-off:** the ticket rotates about 3–5° clockwise and drops, as feedback for dismiss or regenerate.
- A sticky primary CTA plus a secondary link.

## 7. Motion
The motion is measured: 11.26 s, 60 fps, motion_fraction 0.69, not a loop.
- **0.07–2.43 s:** 2.37 s **continuous/linear**. The paper feeds at a constant speed (about 450 px/s), as a real printer would, not with an ease.
- **2.80 s and 3.33–3.97 s:** a 0.23 s symmetric and a 0.63 s symmetric segment. This is the tear: the paper lifts and falls away with rotation (f2).
- **4.77–7.17 s:** 2.4 s linear, the second print.
- **7.60 s and 8.10–8.63 s:** 0.13 s and 0.53 s ease-in (peak 0.72). This is the second tear, which accelerates as it falls, like gravity.
- **9.53–11.13 s:** 1.6 s linear, the third feed (f8).

The linear feed paired with ease-in drops is a correct physical vocabulary choice.

## 8. Brand system
n/a — not a brand system. The airline wordmark appears as content. Product cues: a monochrome UI with a red notification dot, and mono labels as an "issued document" voice.

## 9. UX
- **Pros:** delight that also communicates "your pass is being issued". All key fields are scannable in a strict grid, and there is a clear Wallet CTA.
- **Cons:**
  - The ticket overlaps the CTA zone during the print (f2), so the CTA covers the barcode.
  - Mono labels are low contrast.
  - Repeating the print on every visit would grow tiresome, so it should play once.

## 10. Craft signals
- The paper is masked by the slot with a dark gradient, not just clipped (f5, top 100 px).
- The perforation has semicircular side notches aligned exactly to the dashed line.
- The bottom edge is scalloped (9 arcs) like torn thermal paper.
- The labels are mono and the values sans, consistently in every field.
- Feed speed is constant (linear segments of 2.37 / 2.4 / 1.6 s), while the tear is accelerated (ease-in).
- 3-up rows are aligned left, centre and right on a shared baseline (Terminal/Gate/Seat).

## 11. Reproduction recipe
```css
:root{--bg:#e4e5e9;--paper:#fff;--ink:#1a1a1a;--label:#6f6f6f;--slot:#2a2a2c;--accent:#5e5aa0}
.slot{height:175px;border-radius:28px;background:linear-gradient(#3f3f3f,#2a2a2c);position:relative;z-index:2}
.slot::after{content:"";position:absolute;left:40px;right:40px;bottom:-100px;height:100px;
  background:linear-gradient(rgba(0,0,0,.55),transparent);pointer-events:none;z-index:3}
.ticket{width:625px;margin:-120px auto 0;background:var(--paper);padding:40px 46px 60px;
  box-shadow:0 30px 60px rgba(0,0,0,.06);
  -webkit-mask:radial-gradient(18px at 18px 100%,#0000 98%,#000) -18px 100%/36px 100% repeat-x; /* scallops */
  animation:feed 2.4s linear both}
@keyframes feed{from{transform:translateY(-100%)}to{transform:translateY(0)}}
.ticket.tear{animation:tear .55s cubic-bezier(.55,0,1,.45) forwards}
@keyframes tear{to{transform:translateY(120%) rotate(4deg);opacity:0}}
.label{font:400 20px "IBM Plex Mono",monospace;color:var(--label)} /* 5.1:1 */
.value{font:500 30px "Suisse Intl",Inter,sans-serif;color:var(--ink)}
.perf{border-top:2px dashed #cfcfcf;position:relative}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 9 | A crisp monochrome ticket, a beautiful slot shadow and a disciplined grid. |
| Originality | 8 | A receipt-printer reveal for a boarding pass is a fresh, fitting metaphor. |
| Usability | 7 | Clear data hierarchy and CTA. Labels fail AA, and the ticket collides with the CTA mid-print. |
| Craft | 9 | Perforation notches, scallops, physically correct easing and a consistent type pairing. |

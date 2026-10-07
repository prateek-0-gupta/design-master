---
id: insp-1-34
source: inspora
category: Product
status: analyzed
title: "card details microinteraction"
creator: "@bodya_zhk"
styles: [dark-premium, micro-interaction, physical-material]
patterns: [bottom-sheet-reveal, background-blur-on-modal, copy-to-clipboard-rows, metallic-card-hero, dimmed-decimal-currency, circular-action-buttons, device-mockup-on-light-stage]
mode: dark
palette: ["#f7f7f7", "#050505", "#1a1a1a", "#2c2c2c", "#3a3a3a", "#8a8a8a", "#ffffff", "#e8501f"]
type_families: ["Satoshi / General Sans-style grotesk (likely)"]
type_class: [grotesk]
radius_px: [44, 24, 9999]
motion: {durations_s: [0.4, 0.37, 0.33], easing: [ease-in-out, ease-out], loop: true}
scores: {aesthetics: 8, originality: 6, usability: 8, craft: 8}
craft_signals: [dimmed-decimals-in-balance, blur-plus-dim-backdrop, card-notch-cutout-bottom, per-field-copy-pill, sheet-grabber-handle, metallic-gradient-card]
anti_patterns: [full-card-number-shown-unmasked]
---
# card details microinteraction — @bodya_zhk

## 1. Snapshot
- **Subject:** A 4.03 s, 1080×1080 loop of a dark banking app ("spark" Visa card) on a light stage. Tapping "Details" blurs the home screen and slides up a "Card details" sheet with copyable fields, which then dismisses.
- **Why it's remarkable:** A sensitive-data reveal is handled as one spatial gesture. The card lifts and blurs, the whole background defocuses, and a sheet holds only three rows, each with its own Copy pill.

## 2. Composition & layout
- **Stage:** a light #f7f7f7 stage with the phone cropped at the bottom, about 690 px wide on the key frame (x 195→885).
- **Home screen:**
  - status bar;
  - an avatar (≈44 px) and an "Earn $50" pill to the left, and a bell with a red badge to the right;
  - the metallic card shown portrait (≈205×180 visible on the sheet frame), cropped by the top edge, with a semicircular notch cut into its bottom edge;
  - "Balance - USD" (≈12 px) over "5,293.00" (≈38 px);
  - four 52 px circular action buttons (Receive, Send, Details, Scan QR) on about a 75 px pitch;
  - a Transactions card.
- **Sheet (key frame):** about 590 px wide (x 248→838), top at y≈662, radius about 44 px, with a grabber 50×4 px at 18 px from the top. Inside:
  - title "Card details" ≈30 px;
  - three rows on a 100 px pitch, each a label (≈20 px grey) over a value (≈24 px white);
  - a "Copy" pill (≈92×50 px, #2c2c2c) right-aligned at x≈803.

## 3. Typography
- A geometric-leaning grotesk with a flat-topped "t" and a round "a", close to Satoshi or General Sans. Weights: Medium for values and the title, Regular for labels.
- **Balance:** the integer "5,293" is white and the ".00" is dimmed to about #6a6a6a, a classic currency hierarchy.
- **Sizes (key, 1080 frame):** title 30, value 24, label 20, button 20. Numbers look proportional; the card number groups in 4s with word spaces.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #f7f7f7 | stage | 29% |
| #050505 / #1a1a1a | app background / sheet | 41% |
| #2c2c2c / #3a3a3a | Copy pills, action buttons, cards | 13% |
| #8a8a8a | labels | — |
| #ffffff | values, title | — |
| #c8c8c8 → #ebebeb | metallic card gradient | 6% |
| #e8501f | notification badge, "Earn" dot | <1% |

WCAG checks:
- White on sheet (#1a1a1a): 17.4:1.
- Grey labels (#8a8a8a): 5.04:1.
- White on Copy pill (#2c2c2c): 13.97:1.
- The dimmed decimals (≈#5c5c5c on #050505) are 3.05:1, which passes only as large text. They are about 38 px, so they pass.

## 5. Depth & material
- **Card:** a brushed-metal gradient from top-left white to grey with a soft sheen. When lifted, its edge softens with motion blur.
- **Backdrop on reveal:** a heavy gaussian blur (≈30 px) plus darkening (black at about 40%). The background shapes become unrecognisable, so the sheet is the only legible layer.
- **Sheet:** has a top-lighter gradient (#222 → #161616) and a faint 1 px top highlight. There are no hard shadows inside the app.
- **Phone:** a long soft shadow onto the light stage.

## 6. Components & patterns
- **Bottom sheet** with grabber, title, and key/value rows, each with a trailing Copy pill.
- **Circular icon buttons with labels below:** 52 px, #2c2c2c fill, white 20 px glyph.
- **Transaction row:** a white circular merchant logo (Apple), name over "Spark •••• 8920", amount right-aligned over the time.

## 7. Motion
Measured: duration 4.03 s at 30 fps, motion_fraction 0.28, seamless_loop_likely true. Three segments:
- 0.90–1.30 s (0.40 s, peak_at 0.46, symmetric ease-in-out): the card scales up about 5% and shifts down about 20 px, and the balance starts blurring (frames at 1.12 s and 1.57 s).
- 1.50–1.87 s (0.37 s, peak_at 0.32, ease-out): the backdrop blurs and the sheet slides up from below. It is fully settled by 2.02 s.
- 2.93–3.27 s (0.33 s, symmetric): dismissal, with the sheet down and the blur clearing (home is restored by 3.36 s).

The hold on the sheet is about 1.0 s. The sequence staggers about 0.2 s between the card lift and the sheet entrance, so the cause (card) moves before the effect (sheet).

## 8. Brand system
n/a — this is a product UI, not a brand system. Identity cues: the "spark" wordmark with a four-point star on a silver card, an achromatic UI with a single orange-red notification accent.

## 9. UX
- **Strengths:**
  - The reveal is user-initiated and focused.
  - Per-field copy reduces transcription errors.
  - Blurring the balance and card behind the sheet avoids double exposure.
- **Gaps:**
  - The card number is shown in full with no masking or reveal toggle, and there is no copied-state feedback in the frames.
  - The CVV is absent (fine for security, but the sheet may be expected to have it).

## 10. Craft signals
- The ".00" decimals are dimmed at the same size, not shrunk.
- The card has a semicircular bottom notch (≈60 px diameter) echoing a physical card slot.
- The background is blurred and darkened on sheet open, not just dimmed.
- The Copy pills share one x (right edge ≈803 px) and are vertically centred on each two-line row.
- The grabber is 50×4 px, centred, #4a4a4a.

## 11. Reproduction recipe
```css
:root{--bg:#050505;--sheet:#1a1a1a;--fill:#2c2c2c;--label:#8a8a8a;--text:#fff;--accent:#e8501f;--r-sheet:44px}
.app.has-sheet .content{filter:blur(30px) brightness(.6);transform:scale(1.02);transition:filter .37s cubic-bezier(.2,.8,.2,1)}
.card{background:linear-gradient(135deg,#fafafa,#c8c8c8 60%,#ebebeb);border-radius:24px;
  mask:radial-gradient(circle 30px at 50% 100%,#0000 98%,#000);transition:transform .4s cubic-bezier(.45,0,.55,1)}
.app.has-sheet .card{transform:translateY(20px) scale(1.05)}
.sheet{position:absolute;inset:auto 16px 0;border-radius:var(--r-sheet) var(--r-sheet) 0 0;
  background:linear-gradient(#222,#161616);padding:40px 34px;transform:translateY(100%);transition:transform .37s cubic-bezier(.2,.8,.2,1)}
.app.has-sheet .sheet{transform:none}
.row{display:flex;justify-content:space-between;align-items:center}
.row small{color:var(--label);font-size:20px}.row b{font:500 24px "Satoshi",sans-serif}
.copy{background:var(--fill);border-radius:9999px;padding:12px 18px;color:#fff}
.balance .dec{color:#5c5c5c}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Premium monochrome with a tactile metal card. |
| Originality | 6 | The blur-and-sheet reveal is a known iOS pattern. The card-lift staging is the twist. |
| Usability | 8 | Focused task with per-field copy. Masking and copy feedback are missing. |
| Craft | 8 | Clean stagger and consistent pills and radii. |

---
id: insp-8-2
source: inspora
category: Motion
status: analyzed
title: "Liquid Glow Button"
creator: "@Designownow_"
styles: [soft-3d, aurora-glow, micro-interaction, physical-material]
patterns: [hover-state-swap, sliding-knob-cta, glow-under-shadow, nested-pill-button, avatar-stack-badge, ghost-secondary-button]
mode: light
palette: ["#afafaf", "#999999", "#1b00f3", "#f6f5fb", "#6b8be0", "#0c0e1b", "#646466", "#8b92bc"]
type_families: ["Figtree / Gilroy-style geometric sans (likely)", "high-contrast condensed display serif, Gloock / Ogg-like (likely)"]
type_class: [geometric-sans, editorial-serif]
radius_px: [9999]
motion: {durations_s: [0.37, 0.33, 0.43, 0.4, 0.39], easing: [ease-out, ease-in-out], loop: true}
scores: {aesthetics: 7, originality: 6, usability: 5, craft: 7}
craft_signals: [coloured-glow-instead-of-grey-shadow, knob-travels-full-track, rim-highlight-on-bezel, glow-repeated-on-badge, label-swap-masked-by-fill]
anti_patterns: [white-on-mid-grey-label, low-contrast-hover-label, decorative-glow-everywhere]
---
# Liquid Glow Button — @Designownow_

## 1. Snapshot
- **Subject:** A 10.5 s, 1082×1080 screen recording of a hero CTA, "Get Started", which on hover turns into a glowing white track reading "Lets Grow!" with an ultramarine knob carrying an arrow.
- **Why it's remarkable:** The shadow is replaced by coloured light. The #1b00f3 knob throws a violet bloom onto the grey page below the button, so the button reads as lit from inside, not lifted.

## 2. Composition & layout
- The frame is a cropped section of a consulting landing page. At the top is a giant serif headline (cap height about 110 px, clipped by the frame). Below it is a 2-line subhead of about 40 px centred at y≈190–250.
- A faint panel (1 px lighter hairlines at x≈90 and x≈990, y≈355–780) frames the CTA zone like an inset tile.
- **Primary CTA:** an outer bezel of about 630×195 px (x 225–855, y 455–650) with an inner pill of about 525×115 px. The knob is about 120 px across.
- Below it, a ghost "Learn More" pill (about 275×85) sits on the panel's bottom hairline, then a "Dozens Of Case Studies" pill (about 615×80) with a 4-avatar stack and an "84+" blue badge.
- Everything is on one centre axis at x≈540. The cursor only moves vertically through the CTA.

## 3. Typography
- **UI sans:** a geometric sans with round "o"/"e", close to Figtree or Gilroy, in Regular. Sizes: CTA label about 40 px, subhead about 40 px, "Learn More" and "Dozens…" about 28 px. All copy uses Title Case On Every Word, which reads as template-y.
- **Display:** a high-contrast condensed serif with ball terminals and a long "g" descender, close to Gloock or a narrow Ogg. Its size is about 150 px, set in #0c0e1b over a blue-tinted top band.

## 4. Colour
| Hex | Role | Share (key frame) |
|---|---|---|
| #afafaf / #999999 | page grey, idle inner pill | ~65% |
| #1b00f3 | knob, badge, glow source | ~4% |
| #f6f5fb | hover track fill | ~6% |
| #6b8be0 | hover label "Lets Grow!" | <1% |
| #0c0e1b | display serif | ~5% |
| #8b92bc | blue haze behind headline | ~8% |
| #646466 | ghost-button label | <1% |

WCAG:
- White arrow on #1b00f3 is 8.97:1.
- Hover label #6b8be0 on #f6f5fb is **3.03:1** (passes large text only; the label is about 40 px, so it is borderline acceptable).
- Idle "Get Started" white on #999999 is about **2.8:1 (fails)**.
- "Learn More" #2c2c2e on its #646466 surround is 2.36:1, and the case-study label is 2.9:1. Both fail.
- Headline #0c0e1b on #8b92bc is 6.34:1.

## 5. Depth & material
- The button is a three-layer stack: a grey bezel with a bright 2 px top rim and a dark lower rim (chrome-like edge), an inset track, and a knob.
- The knob has a 1–2 px lighter ring and an outer glow of roughly 0 0 30px #3a2bff.
- Under the bezel, a soft violet radial (#5f5989 measured at the shadow core) replaces a neutral drop shadow. The glow grows in hover when the track turns white, as if the white is emitting.
- The "84+" badge repeats the same glow at small scale.

## 6. Components & patterns
- **Sliding-knob CTA:**
  - Idle: knob left with a white dot, grey track, white label.
  - Hover: the knob translates about 405 px to the right, the dot becomes "→", the track floods white from the left and the label swaps.
- A ghost secondary button with a 1 px darker outline.
- A social-proof pill with an overlapping avatar stack (−12 px overlap) ending in a count badge.

## 7. Motion
The motion is measured: 10.53 s at 60 fps, motion_fraction 0.29 (the button is static about 70% of the time) and seamless_loop_likely true.
- **Transitions:** 8 segments of 0.33–0.43 s (median 0.39 s), one per hover-in or hover-out.
- **Easing:** 4 of the 8 peak early (peak_at 0.23–0.29, ease-out) and the rest are symmetric (0.35–0.54).
- **Frame f6 (7.61 s)** catches the knob mid-track at x≈345 with the white fill trailing behind it and the label half-masked ("Lets" visible, "Grow!" clipped). This shows the label is revealed by the fill, not cross-faded.
- **Glow:** its intensity ramps with the fill, so the bloom peaks once the knob reaches the right side.

## 8. Brand system
n/a — not a brand system. Identity cues: an ultramarine #1b00f3 single accent on warm-neutral grey, and a serif display paired with a geometric sans.

## 9. UX
- The hover state clearly signals "this goes somewhere" (arrow, motion to the right).
- The idle label fails contrast, and the hover copy differs from the idle copy ("Get Started" → "Lets Grow!"), which can confuse anyone who never sees the hover state, such as touch users. The missing apostrophe in "Let's" is a copy flaw.
- The ~0.4 s duration is on the slow side for hover, but it is acceptable for a hero CTA.

## 10. Craft signals
- Shadow hue is the accent hue (#5f5989 core under the button), not black.
- The knob travels the full track length and ends flush with the inner pill's right inset (about 12 px on both ends).
- The bezel has an asymmetric rim: light top edge, dark bottom.
- The badge "84+" reuses the knob colour and glow, which ties the secondary element to the CTA.
- The label is revealed by the white fill mask during travel (f6).

## 11. Reproduction recipe
```css
:root{--page:#afafaf;--accent:#1b00f3;--track-on:#f6f5fb;--label-on:#6b8be0;--r:9999px}
.cta{position:relative;padding:20px;border-radius:var(--r);background:linear-gradient(#b9b9bb,#a2a2a4);
  box-shadow:inset 0 2px 0 rgba(255,255,255,.7),inset 0 -2px 0 rgba(0,0,0,.25),0 30px 60px -20px rgba(58,43,255,.45)}
.track{position:relative;height:115px;border-radius:var(--r);background:#999;overflow:hidden}
.track::before{content:"";position:absolute;inset:0;background:var(--track-on);transform:scaleX(0);transform-origin:left;
  transition:transform .39s cubic-bezier(.2,.8,.2,1);box-shadow:0 0 40px rgba(120,130,255,.8)}
.knob{position:absolute;left:8px;top:50%;width:100px;aspect-ratio:1;border-radius:50%;background:var(--accent);
  translate:0 -50%;box-shadow:0 0 0 2px rgba(255,255,255,.35),0 0 30px #3a2bff;transition:left .39s cubic-bezier(.2,.8,.2,1)}
.cta:hover .track::before{transform:scaleX(1)}
.cta:hover .knob{left:calc(100% - 108px)}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 7 | The light-as-shadow glow is attractive, but the grey page is muddy and the copy is Title-Case heavy. |
| Originality | 6 | A slide-to-arrow pill with glow is a widely seen 2024–25 trend. |
| Usability | 5 | Clear hover affordance, but the idle label fails contrast and the copy changes on hover. |
| Craft | 7 | Consistent pill radii, rim lighting and a glow echoed on the badge. The secondary pills are low contrast. |

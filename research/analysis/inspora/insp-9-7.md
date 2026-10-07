---
id: insp-9-7
source: inspora
category: Product
status: analyzed
title: "OTP"
creator: "@bollmann0x"
styles: [soft-3d, corporate-clean, playful-rounded]
patterns: [illustrated-hero-auth, phone-otp-flow, six-cell-code-input, horizontal-step-slide, door-ajar-progress-metaphor, label-morph-button]
mode: light
palette: ["#eeeeee", "#fefefe", "#020003", "#b47b4e", "#9b5a35", "#6a3a26", "#e4e1e2"]
type_families: ["SF Pro Text (likely)", "rounded display for WELCOME mat (illustration)"]
type_class: [neo-grotesk, rounded-sans]
radius_px: [12, 10, 9999]
motion: {durations_s: [0.23], easing: [ease-out], loop: true}
scores: {aesthetics: 8, originality: 8, usability: 6, craft: 7}
craft_signals: [hero-illustration-changes-with-step, warm-light-spill-from-door, button-label-crossfade, active-otp-cell-2px-border, hero-fades-into-white]
anti_patterns: [placeholder-zeros-near-invisible, grey-subtitle-below-aa, decorative-logo-ambiguous]
---
# OTP — @bollmann0x

## 1. Snapshot
- **Subject:** A 4.0 s, 1080×1080 phone-auth loop. "Sign in" (phone number) slides to "Confirm Your Number" (6-digit code) under a 3D-rendered white door and orange "WELCOME" doormat.
- **Why it's remarkable:** The hero illustration tracks progress. After you submit your number the door opens a crack and warm light spills onto the mat, a literal "you're almost in" cue.

## 2. Composition & layout
- **Phone:** about 414×896 px in the 1080 frame, centred on #eeeeee. The screen is white.
- **Hero:** the illustration takes the top ~42% (door y≈150–360, mat y≈360–480). It fades into white at the bottom with no hard edge.
- **Form block:**
  - centred title (~19 px semibold);
  - two-line grey subtitle (~15 px);
  - input row;
  - full-width black button (~330×66 px, radius ~12).
- **Footer:** a grey line-art logo mark at ~36 px, then "Don't have an account? Sign up" with "Sign up" underlined.
- **OTP row:** six cells of ~48×58 px with ~8 px gaps, spanning the same 330 px as the button.

## 3. Typography
- SF Pro-style system sans throughout.
- **Weights:** semibold for the title and button label, regular for the subtitle.
- **Subtitle:** 15 px at ~1.4 line height.
- **Doormat:** "WELCOME" is a chunky rounded display face, embossed into the mat as part of the render, not live text.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #eeeeee | stage | 76% |
| #fefefe | screen | 16% |
| #020003 | primary button, active cell border, title | 2% |
| #b47b4e / #9b5a35 | doormat tan / border | 3% |
| #6a3a26 | doormat shadow | <1% |
| #e4e1e2 | door / inactive cell borders | 1% |

WCAG checks:
- White on the black button: 21:1.
- Subtitle ≈#8e8e93 on #fff: **3.26:1 (fails AA)**.
- OTP placeholder zeros ≈#d4d4d4 on #fff: **1.48:1**. They are decorative, but they read as almost-empty.

## 5. Depth & material
- The illustration is soft-3D: matte white door panels with ambient occlusion and a fibrous orange mat with a bevelled border.
- The open-door state adds a warm (#f5d9a0-ish) light wedge on the right of the door and across the mat.
- The UI itself is flat: no shadows on inputs or the button.

## 6. Components & patterns
- Phone input with country selector "+1 ⌄" and a hairline separator inside one 1 px bordered field (radius ~10).
- **OTP cells:** the active cell has a ~2 px black border; inactive cells have a 1 px #eee border.
- **Primary button:** its label crossfades from "Continue" to "Confirm" (frame 1.57 s shows the letters mid-dissolve) while the form slides.

## 7. Motion
- **Measured:** a single segment at 1.53–1.77 s (0.23 s), ease-out with its peak at 0.21. motion_fraction is 0.06, and the loop is likely seamless (first/last diff 1.32).
- **Visible in that 0.23 s:**
  - the Sign-in block translates left and out while the Confirm block enters from the right (frame 1.57 s shows both, offset by ~150 px);
  - the button label morphs;
  - the door opens slightly and the light spill appears. The spill persists through the frames at 2.02–3.81 s.
- One fast decelerating move is the right energy for a step change.

## 8. Brand system
n/a — not a brand system. Identity cues: the home/door metaphor and a line-art house-like logomark that echoes an open door.

## 9. UX
- A standard SMS-OTP flow with clear copy ("Enter the code sent to +1 123 4567890.").
- The illustration rewards progress without blocking.
- **Risks:**
  - No resend-code or edit-number link is visible on the confirm step.
  - The subtitle and placeholders are low contrast.
  - The large hero pushes the form toward the keyboard zone on smaller phones.

## 10. Craft signals
- The door state is bound to the flow step (closed → ajar plus light).
- The OTP row width equals the button width (≈330 px), so the column edges align.
- The button label morphs in place instead of the button swapping out.
- The hero image bottom dissolves into #fefefe (no visible seam at y≈480).
- The active OTP cell uses border weight (2 px vs 1 px), not colour alone.

## 11. Reproduction recipe
```css
:root{--ink:#020003;--muted:#6e6e73;--line:#e8e8e8;--r:12px}
.hero{height:42%;background:url(door.png) center/cover;mask-image:linear-gradient(#000 80%,transparent)}
.otp{display:grid;grid-template-columns:repeat(6,1fr);gap:8px}
.otp input{height:58px;border:1px solid var(--line);border-radius:10px;text-align:center;font:600 22px system-ui}
.otp input:focus{border:2px solid var(--ink);outline:none}
.btn{height:66px;border-radius:var(--r);background:var(--ink);color:#fff;font:600 17px system-ui}
.step{transition:transform .23s cubic-bezier(.2,.8,.2,1),opacity .23s}
.step[data-state=exit]{transform:translateX(-40%);opacity:0}
.step[data-state=enter]{transform:translateX(40%);opacity:0}
.door-light{opacity:0;transition:opacity .4s ease-out}.is-confirm .door-light{opacity:1}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Charming tactile hero against strict monochrome UI. |
| Originality | 8 | The progress-aware door is a memorable, on-theme idea. |
| Usability | 6 | Clear flow; missing resend/edit; low-contrast helper text. |
| Craft | 7 | Good alignment and morph; placeholder legibility and logo meaning are weak. |

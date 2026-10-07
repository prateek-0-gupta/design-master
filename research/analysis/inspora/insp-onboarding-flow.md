---
id: insp-onboarding-flow
source: inspora
category: Product
status: analyzed
title: "onboarding flow"
creator: "@nickpylll"
styles: [minimal-swiss, gradient-mesh, micro-interaction]
patterns: [step-colour-gradient-header, collapsing-step-list, sign-in-with-apple-sheet, otp-entry-with-resend-timer, setup-progress-checklist, word-carousel-hero, black-pill-primary-cta]
mode: mixed
palette: ["#fefefe", "#f2f2f3", "#d4d4dd", "#1ec8f5", "#f5a623", "#a35cf0", "#37373a", "#111111"]
type_families: ["SF Pro Display / SF Pro Text (likely)"]
type_class: [neo-grotesk]
radius_px: [9999, 24, 12]
motion: {durations_s: [0.37, 0.27, 0.67, 0.3, 0.33, 0.37, 0.33], easing: [ease-out], loop: false}
scores: {aesthetics: 8, originality: 7, usability: 7, craft: 8}
craft_signals: [one-gradient-hue-per-security-step, done-steps-collapse-to-grey-list-above, icon-colour-matches-step-gradient, otp-digits-scatter-on-success, native-ios-components-reused, final-list-resolves-to-green-check]
anti_patterns: [white-eyebrow-on-bright-gradient-fails, grey-body-copy-2-6-to-1]
---
# onboarding flow — @nickpylll

## 1. Snapshot
- **Subject:** A 24.7 s, 1080×1080 recording of an iPhone onboarding for "Fuse", a seedless crypto wallet.
  1. A dark welcome screen with a rotating word list (Earn / Invest / Spend…) and "Your money, upgraded".
  2. The Sign in with Apple sheet.
  3. Three security steps, each with its own vertical gradient header: **Device Key** (cyan), **2FA Key** (amber to orange to pink) and **Recovery Key** (violet). The Recovery Key step includes email entry and a 6-digit OTP.
  4. A setup checklist that ends with "Your wallet is ready!".
- **Why it's remarkable:** Each security factor has a colour identity. The header gradient changes hue per step while completed steps collapse into a quiet grey list above the current one. Progress is felt through colour and stacking, not a progress bar.

## 2. Composition & layout
- The phone is about 480×1020 px in the 1080 square, centred on a #f2f2f3 backdrop.
- **Step screen anatomy:**
  - eyebrow "Secure your wallet" top-left plus a ✕ at top right;
  - a gradient that fills the top 40–60% and fades to white;
  - the completed-step list (grey icon plus label, about 30 px row pitch);
  - the current step: icon about 18 px in the step colour, a title about 26 px Bold, and a 3-line body;
  - pending steps below in grey;
  - a full-width black pill CTA ("Create Device Key", "Create 2FA Key") about 225×38 px at the bottom, with a 20 px side margin.
- **Recovery step:** the CTA is replaced by a pill email field with an arrow submit, then an OTP row of 6 boxes on the iOS numeric keypad, and a "Resend (59s)" countdown chip.
- Left-aligned text column at x≈365 (key frame), about 55 px inset.

## 3. Typography
- SF Pro throughout (native iOS).
  - Step titles about 30 px Bold (key frame) with tight tracking.
  - Body about 15 px Regular in light grey, leading about 1.4, wrapped at about 250 px (3 short lines).
  - Eyebrow about 15 px Medium, two lines.
  - CTA about 13 px Semibold with an icon.
- **Welcome screen:** large about 28 px words in a vertical carousel, the active one white and the others faded.

## 4. Colour
| Hex | Role | Approx share |
|---|---|---|
| #fefefe | screen background | 63% |
| #f2f2f3 | page backdrop | 19% |
| #d4d4dd / #b9b9bf | keyboard, grey step list | 13% |
| ≈#1ec8f5 | Device Key gradient (cyan) | step-only |
| ≈#f5a623 → #f26b3a → pink | 2FA gradient | step-only |
| ≈#a35cf0 | Recovery gradient, envelope icon | step-only |
| #37373a / #111111 | titles, CTA pill | 4% |

WCAG checks (contrast.py):
- Title #1d1d1f on white: **16.83:1**.
- CTA white on #111: **18.88:1**.
- Body grey ≈#a1a1a6: **2.57:1 (fail)**. The pending-step grey ≈#c7c7cc is **1.68:1**.
- White eyebrow on the cyan gradient #1ec8f5: **1.97:1**; on amber #f5a623: **2.03:1**; on violet #a35cf0: **3.93:1**. All fail for small text.

## 5. Depth & material
- Mostly flat. The gradients are soft vertical fades, with the hue saturated at the top and dissolving to white by about 45–55% height, like a light source behind the status bar.
- **Sign in with Apple sheet:** the system bottom sheet, with a white account card on #f2f2f7.
- **Finale:** an app-icon reveal with a black squircle and a neon-green glyph that drops from the Dynamic Island area at about 20.6 s.
- The CTA is flat black with no shadow.

## 6. Components & patterns
- **Word carousel hero:** a vertical list with the active item bright and the neighbours dimmed.
- **System auth sheet:** Sign in with Apple.
- **Step stack:** done steps above in grey, the current step expanded, pending steps below in grey.
- **Email field:** a pill input with a circular arrow button that is disabled (grey) until valid. A QuickType email suggestion appears above the keyboard.
- **OTP:** 6 boxes, the active one with a caret, and a "Resend (59s)" countdown pill. On success the digits fly apart ("1 3 4 9 6 5" scattering at 17.8 s).
- **Setup checklist:** a spinner ("Setting up your wallet / Hold tight…") that resolves to a green check, "Your wallet is ready!".

## 7. Motion
- Measured (threshold 0.87; the screen-recording noise is high): 24.7 s at 60 fps. `motion_fraction` 0.16 and 12 segments, median **0.32 s**. **10 of 12 are ease-out** (peak_at 0.05–0.32). The longest is **0.67 s** at 5.03 s (the welcome → Device Key transition, where the gradient sweeps in). Step changes are 0.30–0.37 s (10.43, 11.23, 13.37, 14.87 s). A symmetric 0.33 s at 17.57 s is the OTP digits scattering. Not looped.
- **From frames (estimates):**
  - The step gradient crossfades hue (cyan → orange by 9.6 s → violet by 17.8 s).
  - The completed step slides up into the grey list as the next expands.
  - The setup spinner runs about 2.7 s (20.6 → 23.3 s) before the green check.

## 8. Brand system
n/a — not a brand system. Identity cues: the per-factor colour coding (cyan = device, amber = 2FA/cloud, violet = email recovery), the black pill CTA, and the neon-green "Fuse" app icon.

## 9. UX
- A seedless wallet setup broken into three understandable factors, with a plain-language explanation for each. Native components (Apple sign-in, QuickType, the numeric keypad) reduce friction, and the resend timer is explicit.
- **Risks:**
  - The grey body copy and the white eyebrow on bright gradients fail contrast.
  - Pending steps at 1.68:1 are nearly invisible.
  - Progress is implicit; there is no "2 of 3".

## 10. Craft signals
- Each step's icon colour matches its gradient (cyan face-ID glyph, orange cloud, violet envelope).
- Completed steps collapse into a single-line grey list in the same position on the next screen, so continuity is preserved.
- The CTA label names the exact action ("Create 2FA Key") with a matching icon.
- The OTP digits scatter on success instead of a generic checkmark.
- The final checklist recaps all three factors and resolves to a single green check.
- The submit arrow in the email field stays disabled grey until the input is valid.

## 11. Reproduction recipe
```css
:root{--ink:#1d1d1f;--ink-2:#6e6e73;--ink-3:#8e8e93;--cta:#111;--bg:#fff;
  --step:#1ec8f5;--ease:cubic-bezier(.16,1,.3,1)}
.step[data-step=device]{--step:#1ec8f5}
.step[data-step=twofa]{--step:#f5a623;--step-2:#f26b3a;--step-3:#f7a6c4}
.step[data-step=recovery]{--step:#a35cf0}
.screen{background:linear-gradient(180deg,var(--step) 0%,var(--step-2,var(--step)) 22%,var(--step-3,#fff0) 38%,#fff 55%);
  transition:--step .67s var(--ease)}
@property --step{syntax:"<color>";inherits:true;initial-value:#fff}
.eyebrow{color:#fff;font:500 15px/1.2 -apple-system;text-shadow:0 1px 8px #0003}   /* mitigates low contrast */
.done{color:var(--ink-3);font:500 15px -apple-system;transition:transform .33s var(--ease)}
.current h1{font:700 28px/1.1 -apple-system;letter-spacing:-.02em;color:var(--ink)}
.current p{color:var(--ink-2);max-width:250px}   /* #6e6e73 = 5.07:1 */
.cta{height:50px;border-radius:9999px;background:var(--cta);color:#fff;font:600 16px -apple-system;width:calc(100% - 40px)}
.otp input{width:44px;height:52px;border-radius:12px;border:1px solid #d4d4dd;text-align:center;font:600 22px -apple-system}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Clean iOS-native look lifted by bold per-step gradients. |
| Originality | 7 | Colour-coding security factors with a collapsing step stack is a nice twist on a standard flow. |
| Usability | 7 | Clear steps and native inputs; several text pairs fail contrast, and progress is implicit. |
| Craft | 8 | Consistent icon and colour mapping, careful state continuity and a playful OTP success. |

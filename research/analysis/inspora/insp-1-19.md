---
id: insp-1-19
source: inspora
category: Web
status: analyzed
title: "Sign-Up page"
creator: "@coleHardik"
styles: [dark-premium, cinematic-3d, aurora-glow]
patterns: [split-auth-card, hero-media-panel, social-sso-first, or-divider, filled-dark-inputs, white-primary-button, ambient-video-loop]
mode: dark
palette: ["#080a05", "#161714", "#242222", "#413f47", "#b3adb3", "#ffffff", "#e8692e", "#4f86c6"]
type_families: ["Inter / SF Pro Display (likely)"]
type_class: [neo-grotesk]
radius_px: [36, 12, 10]
motion: {durations_s: [20.44], easing: [linear], loop: true}
scores: {aesthetics: 8, originality: 6, usability: 8, craft: 7}
craft_signals: [focus-state-by-1px-border-only, card-image-bleeds-into-page, single-white-cta, password-eye-toggle, hairline-or-divider, warm-cool-complementary-orb]
anti_patterns: [placeholder-as-label, low-contrast-or-divider, ai-stock-imagery]
---
# Sign-Up page — @coleHardik

## 1. Snapshot
- **Subject:** A 20.4 s, 1920×1200 loop of a "SoundCore AI" sign-up screen. A rounded split card pairs a glowing, slowly rotating glass orb hovering over an open hand (left) with a minimal dark form (right).
- **Why it's remarkable:** The form is entirely standard. The quality comes from a cinematic left panel whose blue and orange light leaks out of the card onto the near-black page, so the card feels lit by its own image.

## 2. Composition & layout
- **Card:** about 1446×872 px (x 238→1684, y 162→1034), centred, radius about 36 px, with a 1 px border at about 8% white.
- **Split:** 54/46. The image panel is about 786 px wide and the form panel about 660 px. The form column is about 490 px wide (x 1110→1598), centred in its panel.
- **Vertical rhythm in the form:**
  - eyebrow at y≈257;
  - H1 at y≈347;
  - Google button (54 px tall) at y≈407;
  - OR divider at y≈506;
  - three 48 px inputs with about 14 px gaps;
  - CTA (50 px) at y≈757;
  - log-in line at y≈852;
  - legal line at y≈936.
- The wordmark "SoundCore AI" sits at top-left of the image panel (about 24 px, x≈291).

## 3. Typography
- A single neo-grotesk (Inter or SF Pro Display) at regular weight only.
- **Sizes:**
  - H1 "Join SoundCore AI" about 44 px with tracking of about −0.02 em;
  - wordmark about 24 px medium;
  - inputs and buttons about 17 px;
  - eyebrow and secondary lines about 16 px grey;
  - "OR" about 14 px uppercase dark grey.
- **Links:** "Log in", "Terms" and "Privacy Policy" are distinguished by white vs grey only, with no underline.

## 4. Colour
| Hex | Role | Share (key) |
|---|---|---|
| #080a05 | page and form panel background | 65.7% |
| #161714 / #242222 | input fills, image-panel shadow | 22% |
| #413f47 | borders, focused-input stroke | 7% |
| #b3adb3 | secondary text | 5% |
| #ffffff | H1, CTA fill, links | — |
| ≈#e8692e / #4f86c6 | orb's orange flare and blue glass (image only) | — |

WCAG checks:
- White on #080a05 is 19.9:1.
- Secondary grey (≈#8a8a8a) on black is 5.76:1.
- Placeholder (≈#9a9a9a) on the #161714 input is 6.4:1.
- The dark CTA label on white is 18.9:1.
- The "OR" and divider (≈#3a3a3a) are 1.75:1, which is acceptable only because they are decorative.

## 5. Depth & material
- There are no shadows on the form. Inputs are filled (#161714) with no visible border in the rest state.
- The focused "John Doe" field gains a 1 px #413f47-ish stroke and a slightly lighter fill. This is the only focus signal.
- The image panel has a soft vignette, and its light rays extend beyond the card edge onto the page (about 200 px of blue streak at the left). This breaks the box and adds atmosphere.
- The orb is a translucent glass sphere with internal blue caustics and an orange rim flare. The warm/cool complementary pairing is the scene's only saturation.

## 6. Components & patterns
- **Social-first sign-up:** an outlined "Sign up with Google" button with a 1 px border and radius of about 12 px.
- **"OR" divider:** hairline rules on both sides.
- **Inputs:** three filled fields with radius of about 12 px. The password field has an eye toggle at the right inset of about 24 px.
- **Primary button:** white, full width, with a chevron "›" after the label ("Start Building").
- **Below the CTA:** a log-in switch and legal consent.

## 7. Motion
- **Measured:** 20.44 s at 30 fps. motion_fraction is only 0.04 and mean energy is 0.2, with just two tiny 0.10–0.13 s segments at 13.43 s and 18.50 s (cursor or caret blips). The detector flags it as a seamless loop (first/last diff 0.77).
- **Observed across the 9 frames:** the orb rotates continuously and very slowly, and its flare position cycles around the sphere (about 1 revolution every ~7 s, estimated). The motion is sub-threshold, so it reads as linear and ambient. The form is static and the caret blinks in "John Doe|".

## 8. Brand system
n/a — not a brand system. Identity cues:
- the plain "SoundCore AI" wordmark;
- an orb-in-hand motif (an "AI as energy you hold" metaphor);
- a warm/cool complementary light palette.

## 9. UX
- The hierarchy is textbook: SSO first, a short three-field form and one primary action. The CTA has high contrast and the switch to log in is easy to find.
- **Risks:**
  - Placeholders act as labels and disappear on typing.
  - The focus ring is a faint 1 px stroke (about 1.8:1 against the background), which is weak for keyboard users.
  - Links rely on colour alone.

## 10. Craft signals
- The form column (490 px) is centred exactly in its panel, and all controls share one width.
- Control heights are consistent: 54 px Google, 48 px inputs, 50 px CTA, all with the same radius of about 12 px.
- Light from the hero image spills beyond the card bounds, so the page and card share one lighting.
- One white element (the CTA) carries all the emphasis.
- The image is still while the form idles, with only the orb's slow spin, so it does not distract.

## 11. Reproduction recipe
```css
:root{--bg:#080a05;--field:#161714;--line:#413f47;--text:#fff;--muted:#8a8a8a;--r-card:36px;--r-ctl:12px}
body{background:var(--bg);color:var(--text);font:400 17px/1.4 Inter,system-ui}
.auth{display:grid;grid-template-columns:54fr 46fr;width:1446px;border-radius:var(--r-card);
  border:1px solid rgba(255,255,255,.08);overflow:visible}
.auth .media{background:url(orb.mp4);border-radius:var(--r-card) 0 0 var(--r-card)}
.field{height:48px;border-radius:var(--r-ctl);background:var(--field);border:1px solid transparent;padding:0 16px;color:#fff}
.field:focus{border-color:var(--line);background:#1c1c1a;outline:none}
.btn-primary{height:50px;border-radius:var(--r-ctl);background:#fff;color:#111;width:100%}
.btn-sso{height:54px;border-radius:var(--r-ctl);border:1px solid #2a2a2a;background:transparent;color:#fff}
.or{display:flex;gap:12px;align-items:center;color:#3a3a3a;font-size:14px}
.or::before,.or::after{content:"";flex:1;height:1px;background:#1f1f1f}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Moody, restrained form against a vivid hero. The light spill is atmospheric. |
| Originality | 6 | The split auth card is a common pattern. The orb-in-hand AI imagery is trendy. |
| Usability | 8 | A clear, short flow with SSO and a strong CTA. Only labels and focus are weak. |
| Craft | 7 | Tidy, consistent control sizing. The imagery looks AI-generated and the focus state is subtle. |

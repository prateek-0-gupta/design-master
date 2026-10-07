---
id: insp-1-12
source: inspora
category: Motion
status: analyzed
title: "Glass shader"
creator: "@jmtrivedi"
styles: [glassmorphism, physical-material, spatial-ui, generative-particle]
patterns: [draggable-glass-lens, refraction-over-text, chromatic-dispersion-rim, onboarding-welcome-screen, sso-button-pair, emoji-bubble-burst]
mode: light
palette: ["#f1c6b3", "#f9e0cc", "#22040c", "#310c03", "#3e0001", "#c59b8c", "#656d65", "#90531e"]
type_families: ["SF Pro Display (iOS system, likely)"]
type_class: [neo-grotesk]
radius_px: [9999, 56]
motion: {durations_s: [0.57, 0.53, 0.4, 14.23, 1.63], easing: [ease-out, ease-in-out], loop: false}
scores: {aesthetics: 9, originality: 8, usability: 6, craft: 9}
craft_signals: [rgb-split-at-lens-edge, text-magnified-and-wrapped, lens-has-frosted-rim, bubbles-refract-content, on-device-recording, two-tone-sso-hierarchy]
anti_patterns: [lens-occludes-content, ui-concept-over-function]
---
# Glass shader — @jmtrivedi

## 1. Snapshot
- **Subject:** A 2000×3556, 26.2 s, 60 fps phone recording of an onboarding screen for "Wabi" ("Meet Wabi. The first personal software platform."). A circular glass lens is dragged with a finger. It refracts and chromatically disperses the text and the colourful app-bubble icons that burst from the top.
- **Why it's remarkable:** A real-time custom shader on device. The lens magnifies and bends type into an arc ("Meet Wab") and splits RGB at its rim, so glass becomes a toy-like interaction, not a static blur.

## 2. Composition & layout
- **Screen:** a standard iPhone 15 Pro-class screen held in hand over a wooden table, with a window behind.
- **States observed:**
  1. **Intro:** "A new era of software is here." centred at about 45% of the height, with a large lens (about 55% of the screen width) parked at the bottom over a "Swipe up to…" hint. A blue-violet dispersion arc glows on the lens at t=1.46 s.
  2. **Swiping up** grows the lens over the text.
  3. **Welcome:** a small lens (about 18% of the screen width) at about 48% height. Below it sits the three-line headline. Above it, app-icon bubbles burst towards the top.
- **SSO buttons:** two at the bottom, each about 88% of the screen width. "Continue with Google" is light, "Continue with Apple" is dark. Each is about 80 px tall at device scale, with about 18 px between them.
- **Headline:** centred and set in three lines, about 6% of the screen height as a block.

## 3. Typography
- iOS system font (SF Pro Display). The headline is regular weight, about 30 pt on device. Line 1 "Meet Wabi." is darker (#310c03 in the warm capture) and lines 2–3 are mid-grey (on the first appearance at t=7.28 s, a two-tone headline).
- **Button labels:** about 15 pt. The Google label is medium grey; the Apple label is semibold white.
- **Lens distortion:** Letters behind the lens are magnified about 1.6× and bent along the circle's curvature, with coloured fringes.

## 4. Colour
The capture is warm-cast by room light. The real UI is likely off-white (#f6f2f0-ish) with a near-black #111.

| Hex | Role | Share |
|---|---|---|
| #f1c6b3 | screen background (as filmed) | 25% |
| #f9e0cc | Google button fill | — |
| #22040c / #3e0001 | Apple button, phone bezel | 9% |
| #310c03 | headline text | — |
| #656d65 / #a4acab | background window / foliage | about 14% |
| #90531e / #75482b | wooden table | about 9% |
| multicolour (bubbles) | app-bubble icons, dispersion | small |

WCAG checks (as filmed):
- Headline #310c03 on #f0cab5: 11.67:1.
- Google label #522f29 on #f9e0cc: 9.21:1.
- White on the Apple button #22040c: 19.25:1.

## 5. Depth & material
- **Lens:** frosted rim (a thin whitish ring of about 4 px), clear centre with magnification, and edge dispersion (RGB separation of about 3–6 px, the blue/violet/orange fringes visible around "Meet Wab"). A subtle soft shadow beneath it offsets the lens from the screen plane.
- **App bubbles:** spheres with their own refraction and saturated content (bell, horse, donut). Size varies from about 10 to 60 px on device, which conveys depth.
- The screen background has a faint fine diagonal texture (visible at 2000 px width), a paper-like grain.

## 6. Components & patterns
- Draggable glass lens (a magnifier as a playful onboarding object).
- Bubble burst ("all your apps") radiating from the lens and floating up.
- SSO pair with primary and secondary contrast (dark Apple button as the primary).
- A swipe-up hint inside the lens at the intro.

## 7. Motion
Measured: 26.2 s, 7 segments, `motion_fraction` 0.68, not a loop.
- **Short hand-driven moves:**
  - 3.87–4.43 s (0.57 s, `peak_at` 0.32, ease-out);
  - 4.87–5.27 s (0.40 s, ease-in);
  - 6.13–6.67 s (0.53 s, `peak_at` 0.28, ease-out).
  These are the lens snapping after release, so the physics settle.
- **Long segment, 8.33–22.57 s (14.23 s, symmetric):** continuous dragging and bubble animation.
- **Final segment, 24.53–26.17 s:** continuous/linear.
- **Observed:**
  - The lens grows from small to large when dragged up and shrinks back when released at the welcome position.
  - The bubbles spawn from the lens and drift upward with a stagger.
  - The median segment of 0.53 s suggests spring settle times of about 0.4–0.6 s.

## 8. Brand system
n/a — not a brand system. Identity cues for "Wabi": a warm off-white canvas, a glass-orb motif, a playful bubble cloud of user-made apps.

## 9. UX
- The lens is delightful, but it hides the headline while it is being dragged (t=13.1 s and t=16.0 s show the text occluded by the finger and lens).
- The core action (sign in) stays clear and stable at the bottom.
- The SSO hierarchy is clear: Apple dark, Google light.
- Discoverability relies on the "Swipe up" hint inside the lens.

## 10. Craft signals
- Chromatic dispersion is limited to the lens rim, while the centre stays clean, just as real glass does.
- Text under the lens is magnified and also curved, an actual refraction shader, not a scale transform.
- The lens has a thin frosted ring and a soft shadow, which makes it a physical layer.
- The bubbles also refract their content, so the material language is consistent.
- Recorded live on a device: proof that it is real-time.

## 11. Reproduction recipe
```css
:root{--bg:#f6f2ee;--ink:#1b1b1b;--muted:#8a8580;--btn-dark:#141010;--btn-light:#fbefe6}
.lens{position:absolute;width:180px;aspect-ratio:1;border-radius:50%;
  backdrop-filter:url(#refract) blur(.3px); /* SVG feDisplacementMap for refraction */
  box-shadow:inset 0 0 0 3px rgba(255,255,255,.55),0 12px 24px rgba(0,0,0,.08);
  transition:width .5s cubic-bezier(.2,.9,.3,1.2)}
.sso{height:52px;border-radius:9999px;font:600 15px/1 -apple-system,"SF Pro Text",sans-serif}
.sso.apple{background:var(--btn-dark);color:#fff}.sso.google{background:var(--btn-light);color:#4a2c26}
```
```glsl
// fragment: refraction + dispersion in a disc
vec2 d=uv-center; float r=length(d)/radius; if(r<1.){
  float k=pow(r,3.)*0.35;           // stronger bend near rim
  vec2 o=normalize(d)*k*radius;
  col=vec3(texture(t,uv-o*1.00).r, texture(t,uv-o*1.04).g, texture(t,uv-o*1.08).b);
  col=mix(col,vec3(1),smoothstep(.93,1.,r)*.5); }  // frosted rim
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 9 | A warm, airy screen and jewel-like refractive objects. |
| Originality | 8 | Glass is trendy, but a draggable dispersive lens over live type is fresh. |
| Usability | 6 | Playful, but the lens occludes copy; little functional value. |
| Craft | 9 | Physically plausible refraction, dispersion and springs on device. |

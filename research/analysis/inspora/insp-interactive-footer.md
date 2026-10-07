---
id: insp-interactive-footer
source: inspora
category: Web
status: analyzed
title: "interactive footer"
creator: "@AdityaSur11"
styles: [cinematic-3d, playful-rounded, monochrome, micro-interaction]
patterns: [mascot-footer, cursor-following-eyes, hover-camera-dolly, four-column-footer-nav, inset-rounded-viewport-card, oversized-email-cta]
mode: light
palette: ["#97a9f4", "#7685cf", "#5667b6", "#0b117d", "#2d44a8", "#e5e6f5", "#ffffff"]
type_families: ["Inter / SF Pro-style neo-grotesk (likely)", "heavy rounded display caps, close to Rubik Mono One / Bagel Fat One (likely)", "brush-script wordmark (custom)"]
type_class: [neo-grotesk, display, script]
radius_px: [24]
motion: {durations_s: [0.5, 1.57, 0.43, 0.57, 0.33], easing: [ease-out, linear], loop: true}
scores: {aesthetics: 8, originality: 8, usability: 4, craft: 7}
craft_signals: [eyes-track-cursor, depth-of-field-on-zoom, single-hue-tonal-palette, fur-rim-light-silhouette, heavy-caps-vs-light-links-contrast]
anti_patterns: [white-text-on-pastel-fails-contrast, nav-blurred-during-camera-move, motion-without-reduced-motion-fallback]
---
# interactive footer — @AdityaSur11

## 1. Snapshot
- **Subject:** An 18.8 s, 3456×2160 screen recording of a footer for "Oobi" studio. A furry periwinkle 3D blob with sleepy eyes fills a rounded card, with four link columns above it and a giant email address at the bottom. The post says it was made with Hailuo AI video.
- **Why it's remarkable:** The footer behaves like a camera. When you hover a link the shot dollies toward it, and the creature's eyes follow the pointer, so a list of links becomes a scene with a character.

## 2. Composition & layout
- **Frame:** A deep-blue blurred ground (#0b117d / #2d44a8) has an inset card on top of it. The card runs from x≈128 to 3328 and y≈80 to 2080 in source px, so it has about 128 px side margins and a corner radius of about 40 px in source (≈24 CSS px at 1.7× DPR).
- **Grid:** The links split into two left columns (x≈215 and 600) and two right columns (x≈2620 and 3005). This leaves a centre void about 1900 px wide for the wordmark and the creature's head.
- **Symmetry:** The creature is centred. Its crown peaks at y≈600, and the eyes sit at about 57% of the height, right on the optical centre.
- **CTA:** The email "HELLO@OOBI.STUDIO" is centred at y≈1965, about 690 px wide, and sits over the fur.

## 3. Typography
- **Column headers** ("EXPLORE", "ELSEWHERE", "TINY STUFF", "SAY HELLO") are heavy rounded display caps of about 30 source px (≈18 CSS px) in cream white. They have a slight inner shadow that reads as embossed.
- **Links** are a light neo-grotesk (Inter or SF-like) at about 38 source px (≈22 CSS px), weight 400–500, in white at roughly 70% opacity. The row pitch is about 103 source px (≈60 CSS px), which gives the links generous 2.7× line spacing.
- **Wordmark** "Oobi" is a slanted brush script about 400 px wide in solid white.
- **Email** uses the same heavy display caps as the headers at about 60 source px, so headers and CTA form one voice.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #97a9f4 | card sky / ambient | 52% |
| #7685cf / #6978c4 / #5667b6 | fur body tones | 22% |
| #0b117d / #2d44a8 | outer ground, vignette | 12% |
| #c6ccf0 / #e5e6f5 | fur rim light, eye whites | 7% |
| #ffffff | logo, headers, email | <2% |

WCAG checks:
- White on #97a9f4 is **2.26:1**, which fails even AA-large. This is the main problem for the links.
- Translucent link text (≈#e5e6f5) on the sky is **1.83:1**.
- The email over darker fur (#7685cf) is 3.48:1, which passes AA-large only.

The scheme is a one-hue (periwinkle 230°) tonal ramp. All differentiation comes from value, and the only true black is the pupils.

## 5. Depth & material
- **Creature:** Rendered fur with backlit rim strands (#e5e6f5) gives a soft halo silhouette against the flat sky. The eyelids are fur-covered domes and the eyeballs are glossy porcelain spheres with a specular highlight.
- **Focus pull:** During hover zooms the background links go to a gaussian blur of about 6–10 px while the hovered item stays sharp (frames 5.23 s and 7.32 s). This is real depth-of-field, not a flat scale.
- **Shadows:** The card has no drop shadow. It separates from the ground only by the value jump from #97a9f4 to #0b117d.

## 6. Components & patterns
- A four-column footer nav (Explore / Elsewhere / Tiny Stuff / Say hello) with four links each, a uniform 4×4 grid.
- A mascot hero acting as the footer backdrop.
- Hover-to-zoom on links: the camera pushes toward the Instagram link at x≈1460 in the sheet.
- Logo hover: at 13.59 s the wordmark ghosts to about 50% opacity.
- An oversized email address as the closing CTA.

## 7. Motion
Measured: 18.82 s at 60 fps, motion_fraction 0.24, `seamless_loop_likely: true`, and 7 segments with a median of 0.5 s.
- **Eye glances:** 3.2–3.7 s (0.50 s, peak_at 0.03) and 6.77–7.2 s (0.43 s). These are snappy ease-out saccades, like real eyes.
- **Camera push to link:** 4.3–5.87 s (1.57 s, continuous/linear, peak 0.10). This is a long dolly that decelerates only gently.
- **Return:** 8.53–9.1 s (0.57 s, ease-out).
- **Final push into the creature and email:** 16.6–17.1 s (0.50 s), 17.43–17.77 s (0.33 s) and 18.07–18.63 s (0.57 s).

The rhythm is long idle holds, about 76% still, broken by short ease-out bursts. That is characterful, but the zooms will move content the user is trying to click.

## 8. Brand system
n/a — not a brand system. Identity cues:
- the brush-script "Oobi" wordmark;
- the periwinkle mascot as a brand character;
- heavy rounded caps for headers and email;
- a "Tiny stuff / Colophon / Now" column that signals an indie studio voice.

## 9. UX
- **IA:** The 16 links are clearly grouped and the labels are scannable.
- **Risks:**
  - Link contrast fails everywhere (1.8–2.3:1).
  - The camera zoom moves and blurs the other targets, so the hit areas move under the pointer.
  - No `prefers-reduced-motion` fallback is shown.
  - Video-driven fur at 3456 px is heavy for a footer.
- **Strength:** The eyes follow the cursor, which gives immediate feedback that the page is alive and rewards exploration.

## 10. Critical craft signals
- The pupils shift direction between frames (1.05 s looks left, 3.14 s looks right toward the cursor at x≈1190), so gaze is mapped to the pointer.
- The headers and the email share the same heavy display face; the links use a light grotesk. That makes two type voices with clear jobs.
- The hovered link stays sharp while its neighbours blur during the zoom.
- The palette sits on one hue from #0b117d to #e5e6f5 with no accent colour.
- The card's outer margin of about 128 px equals the inner left padding to "EXPLORE" (x≈215 − 128 ≈ 87 px, near equal), which keeps the edge rhythm.

## 11. Reproduction recipe
```css
:root{
  --ground:#0b117d; --sky:#97a9f4; --fur:#7685cf; --fur-deep:#5667b6;
  --rim:#e5e6f5; --ink:#fff; --r-card:24px;
  --font-ui:"Inter",system-ui,sans-serif; --font-display:"Rubik Mono One","Bagel Fat One",sans-serif;
}
body{background:radial-gradient(80% 60% at 20% 40%,#3b2fc0,var(--ground))}
.footer{margin:48px 74px;border-radius:var(--r-card);background:var(--sky);aspect-ratio:16/10;
  position:relative;overflow:hidden;display:grid;grid-template-columns:repeat(2,180px) 1fr repeat(2,180px);padding:48px}
.footer h4{font:400 18px/1 var(--font-display);color:var(--ink);text-transform:uppercase}
.footer a{font:450 22px/2.7 var(--font-ui);color:rgb(255 255 255 / .75)}
.stage{transition:transform 1.5s cubic-bezier(.2,.6,.3,1),filter .5s ease-out}
.footer:has(a:hover) .stage{transform:scale(1.6) translate(var(--tx),var(--ty))}
.footer:has(a:hover) a:not(:hover){filter:blur(6px)}
.pupil{transition:transform .45s cubic-bezier(.1,.8,.2,1)} /* JS sets translate from pointer angle */
@media (prefers-reduced-motion:reduce){.stage{transition:none;transform:none}}
```
Fix: put the links on a 40% #0b117d scrim, or use #0b117d text (8.3:1 on #97a9f4).

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | A tonal one-hue world with a charming fur render and a confident type pairing. |
| Originality | 8 | A footer as a camera with a character who watches you is a fresh take on the "fun footer" trend. |
| Usability | 4 | All link text fails contrast, and the zoom moves and blurs the targets. |
| Craft | 7 | Gaze tracking and focus pull are thoughtful. Video-based rendering and the jumpy zooms reveal its AI-video origin. |

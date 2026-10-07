---
id: insp-eleven-v4
source: inspora
category: Motion
status: analyzed
title: "Eleven v4"
creator: "@lorenzodossi"
styles: [kinetic-type, minimal-swiss, organic-blob]
patterns: [curved-word-wheel-picker, bracketed-selection, emotion-reactive-orb, ghost-inline-sample-line, drag-to-select, hero-split-orb-and-list, scroll-hint-pill]
mode: light
palette: ["#fdfdfd", "#1a1a1a", "#8b8a8a", "#c8c8c8", "#d9715e", "#c0392b", "#2f6b3a", "#e8e4e3"]
type_families: ["Inter (likely)"]
type_class: [neo-grotesk]
radius_px: [9999]
motion: {durations_s: [0.6, 1.0, 1.63, 0.23, 0.63, 0.47, 0.57, 0.67, 0.5], easing: [ease-out, ease-in-out, ease-in], loop: false}
scores: {aesthetics: 9, originality: 9, usability: 7, craft: 8}
craft_signals: [words-ride-a-cylinder-arc, square-brackets-as-selection-frame, orb-hue-tracks-selected-emotion, ghost-text-speaks-sample-line, coral-only-for-selected, opacity-falloff-by-distance-from-centre]
anti_patterns: [coral-selection-3-19, ghost-sample-text-1-64, long-list-without-search]
---
# Eleven v4 — @lorenzodossi

## 1. Snapshot
- **Subject:** A 20.9 s, 2814×2160 screen recording of a localhost concept landing page for an expressive TTS model: a tall list of ≈40 emotion words curves around an invisible cylinder beside a fluid green/coral orb; dragging the wheel selects an emotion in coral brackets, and a sample line ("You came back!") appears beside it.
- **Why it's remarkable:** The picker *is* the hero — a kinetic typographic wheel whose selection recolours the orb and changes the spoken line, so choosing an emotion feels like tuning a voice.

## 2. Composition & layout
- Browser window inset on a blurred landscape wallpaper; page content on #fdfdfd.
- Home layout: orb ≈460 px diameter left of centre (x≈280–740 in window units), word wheel to its right, selection row on the vertical centre line; the wheel's top and bottom words bend away (≈±30°) as if wrapped on a drum.
- Bottom-left text block (≈220 px wide): "Meet the highest EQ model" ≈20 px, grey sub-line, 3 lines of ≈12 px body, then a black pill "Use v4" + text link "Learn more".
- Focused states fill the window: a 3-item picker (Bored / [Playful] / Mad) centred with prompt "What's your voice feeling?" and "Scroll to explore" + a mouse-wheel glyph pill; or a single sentence "[ Excited ] Some things never make it onto the page!".

## 3. Typography
- Inter-like grotesk only. Wheel words ≈70 px at centre (key frame), shrinking and fading with distance; prompt ≈34 px medium #1a1a1a; hint ≈30 px grey.
- Selection: word in coral with square brackets set apart by spaces — "[ Playful ]" — brackets as a typographic frame, not a box.
- Wordmark "IIElevenLabs" ≈18 px bold top-left.

## 4. Colour
| Hex | Role | Share (key frame) |
|---|---|---|
| #fdfdfd | page | 99% |
| #1a1a1a | prompt, nav, CTA pill | — |
| #8b8a8a | unselected neighbours | — |
| #c8c8c8 | far words, ghost sample line | — |
| #d9715e | selected emotion + brackets | — |
| #2f6b3a / coral / cream | orb fluid colours | — |
| #e8e4e3 | hint pill | 0.3% |

WCAG (contrast.py):
- Prompt #1a1a1a: 17.11:1; "Use v4" white on #111: 18.88:1.
- Selected coral #d9715e: **3.19:1** — passes only as large text (it is ≈70 px, so OK there; fails in the 20 px list state). A deeper #c0392b would reach 5.35:1.
- Neighbours #8b8a8a: 3.38:1; ghost sample text #c8c8c8: **1.64:1**.

## 5. Depth & material
- The orb is the only volumetric element: a sphere filled with swirling fluid (green, coral, cream), soft shading at the rim — like a marbled glass ball.
- Depth in the type comes from perspective: words on the drum foreshorten and rotate (e.g. "Trusting", "Disapproving" tilted ≈15–25°).
- Everything else is flat and shadowless.

## 6. Components & patterns
- **Cylindrical word wheel** (like an iOS picker, but with ≈40 options and visible curvature).
- **Bracketed selection** in coral with a ghost sample sentence to its right that changes per emotion ("You came back", "This is real!").
- **Emotion-reactive orb:** more green when "Disappointed", warmer coral for "Excited".
- **Drag-to-select** with a grab-hand cursor; "Scroll to explore" hint pill.

## 7. Motion
Measured (m0_motion.json): 20.86 s at 60 fps, motion_fraction 0.32, seamless_loop_likely false, 10 segments, median 0.58 s.
- 0.00–0.60 s (0.60 s, peak 0.14, ease-out): wheel spin settle.
- 1.10–2.10 s (1.0 s, symmetric) and 2.30–3.93 s (1.63 s, peak 0.99, ease-in): zoom into the wheel — accelerating camera push that ends in a cut to the focused picker.
- 4.67–4.90 s and 10.53–10.77 s (0.23 s each): small picker steps (word-to-word snaps).
- 11.20–11.83 s (0.63 s, symmetric): transition back out to the full page with the orb.
- 12.60–13.07, 14.37–14.93, 18.63–19.30, 19.43–19.93 s (0.47–0.67 s, peaks 0.07–0.26, ease-out): wheel drags that flick and decelerate, plus a layout mirror (orb moves right, wheel left) at ≈19.7 s.
Pattern: snap steps ≈0.23 s, flicks ≈0.5–0.67 s ease-out, scene transitions ≈0.6–1.6 s.

## 8. Brand system
n/a — a concept page, not a brand system. Identity cues: wordmark top-left, black pill CTA, coral as the "emotion" accent, fluid orb as the voice avatar.

## 9. UX
- Picking an emotion by spinning a wheel is playful and makes the large option set feel explorable.
- Immediate preview (sample line + orb colour) closes the feedback loop.
- Risks: ≈40 options need search or grouping for real tasks; coral selection and ghost text are low-contrast; drag on a curved list may be hard with a keyboard (needs arrow-key support).

## 10. Craft signals
- Words are laid along an arc with per-word rotation, not a flat list.
- Brackets frame the selection without a box or background.
- Opacity steps down with distance from centre (≈#1a1a1a → #8b8a8a → #c8c8c8).
- Coral is used only for the selected emotion.
- Orb colours change with the chosen emotion.
- Layout mirrors (orb left ↔ right) between states.

## 11. Reproduction recipe
```css
:root{--bg:#fdfdfd;--ink:#1a1a1a;--near:#8b8a8a;--far:#c8c8c8;--sel:#c94f3a;--ease:cubic-bezier(.16,1,.3,1)}
.wheel{perspective:900px;height:100vh;overflow:hidden}
.wheel ul{transform-style:preserve-3d;transition:transform .5s var(--ease)}
.wheel li{position:absolute;font:400 36px/1 Inter,system-ui;color:var(--far);
  transform:rotateX(calc(var(--i) * -9deg)) translateZ(420px) rotateZ(calc(var(--i) * 1.5deg));
  backface-visibility:hidden}
.wheel li[data-d="1"]{color:var(--near)}
.wheel li[aria-selected=true]{color:var(--sel)}
.wheel li[aria-selected=true]::before{content:"[ "} .wheel li[aria-selected=true]::after{content:" ]"}
.sample{color:var(--far);margin-left:1ch}
.cta{background:#111;color:#fff;border-radius:9999px;padding:6px 12px}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 9 | Typographic restraint plus one living orb; airy and confident. |
| Originality | 9 | Emotion selection as a 3D word drum with live voice preview is new. |
| Usability | 7 | Delightful and immediate; long list, low-contrast accents, keyboard unknown. |
| Craft | 8 | Consistent opacity falloff, bracket framing, coordinated orb colour; some jitter in motion. |

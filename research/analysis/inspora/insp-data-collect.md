---
id: insp-data-collect
source: inspora
category: Motion
status: analyzed
title: "Data Collect"
creator: "@slavakornilov"
styles: [gradient-mesh, maximalist-color, data-dense, dark-premium]
patterns: [phone-carousel-reel, widget-card-fan, dot-matrix-numerals, gradient-tinted-widget-cards, radial-tick-dial-scrubber, ai-prompt-blur-splash, step-counter-badge]
mode: mixed
palette: ["#080808", "#f1f1f1", "#7728ca", "#baedbb", "#f08a3a", "#c7929f", "#979e6d", "#111111"]
type_families: ["SF Pro Display / Inter-style grotesk (likely)", "custom dot-matrix display numerals"]
type_class: [neo-grotesk, pixel]
radius_px: [44, 32, 9999]
motion: {durations_s: [19.97], easing: [linear], loop: false}
scores: {aesthetics: 9, originality: 8, usability: 6, craft: 8}
craft_signals: [dot-matrix-numerals-against-soft-gradients, one-gradient-per-metric-category, tick-dial-scrubber-with-red-index, step-counter-red-badge, white-chrome-frames-saturated-cards, blur-splash-for-ai-generation]
anti_patterns: [faint-labels-on-gradients, horizontal-reel-too-fast-to-read]
---
# Data Collect — @slavakornilov

## 1. Snapshot
- **Subject:** A 20 s, 1600×1600 reel of a health/lifestyle widget-builder app: a row of iPhones slides continuously left across black, showing "Ring", "Screens", "Watch", "Weather", "Analytics" screens and AI-prompt splash screens ("Create widgets with for my sport watch").
- **Why it's remarkable:** Every metric gets its own saturated gradient card (orange sun, purple sleep, lime alarm, pink wind), and the big numbers are set in a dotted dot-matrix face, so soft colour fields meet crisp, technical numerals.

## 2. Composition & layout
- Three phones visible at once (≈620 px wide each, ≈150 px gaps) on #080808; centre phone fully in frame, neighbours cropped — a film-strip.
- Screen anatomy (Weather, f2): large title ≈38 px bold top-left at y≈280; hero numeral "29°" ≈110 px tall centred; sun-arc chart; 2-up metric cards (≈270×330); bottom bar with ✕ (left), tick dial with index (centre), ✓ (right) at y≈1365.
- "Screens" view: a single ≈395×790 widget card centred with a 48 px vertical icon rail at left and layer button at right — an editor layout.
- "Watch" view: 2×2 grid of square widget cards with 12 px gaps.

## 3. Typography
- UI: SF Pro / Inter-like grotesk; titles ≈38–48 px bold, card labels two-line ("Enhance / Mood") ≈20 px semibold over a ≈20 px muted line.
- Numerals: a custom **dot-matrix** display ("29°", "93", "03") built from ≈8 px dots, plus a clean tabular grotesk for times ("09:50", "6:14 / 17:21").
- Micro labels ("Sunrise", "Nice", "AM / PM") ≈16 px at low opacity.

## 4. Colour
| Hex | Role | Share (key frame) |
|---|---|---|
| #080808 | stage background | 35% |
| #f1f1f1 | app chrome / light screens | 22% |
| #7728ca | sleep / AI-splash violet | 4% |
| #baedbb | alarm lime-mint gradient | 3% |
| #f08a3a | weather orange (f2) | — |
| #c7929f / #c1b1b2 | pink analytics card, blurred splash | 11% |
| #979e6d | olive "Artificial" card | 4% |
| #111111 | titles, numerals, icons | — |

WCAG (contrast.py):
- Title #111 on #f1f1f1: 16.72:1; #111 on orange #f08a3a: 7.55:1 — black ink holds on every gradient.
- White on violet #7728ca: 7.14:1.
- White on mint #baedbb: **1.32:1** (white labels on light cards fail badly).
- Tone-on-tone labels (≈#c46a3a on #f08a3a): **1.54:1**.
- Red step badge #e01b24 on #f1f1f1: 4.27:1.

## 5. Depth & material
- Cards are luminous mesh gradients with internal glow and soft edges, lifted by wide ≈40 px pale shadows on the light chrome.
- Fanned card stacks on "Ring" are tilted ≈±10° with perspective, giving a deck-of-cards depth.
- AI-generation screens are pure blurred colour fields (≈80 px blur) with sparkle particles, implying content materialising.

## 6. Components & patterns
- **Widget cards** keyed to metrics, each with label, dot-matrix value, mini chart (bar ticks, scatter, sun arc, compass pie).
- **Tick-dial scrubber:** a semicircular ruler of ≈60 ticks with a red index line and dot — used as a mode/step selector.
- **Step badge:** red circle "1/2/3" under the dial counts progress through the builder.
- **Editor rail:** 48 px circular icon buttons (shapes, folder, code) and a layers button.
- **Prompt splash:** blurred gradient with a typed prompt fading in.

## 7. Motion
Measured (m0_motion.json): 20.0 s at 60 fps, motion_fraction 1.0, one continuous segment of 19.97 s (peak_at 0.61, energy CV 0.2, "continuous/linear"), seamless_loop_likely false.
- This is a constant-speed horizontal pan — estimated ≈1 phone pitch (≈770 px) every ≈2.2 s, judged from the nine evenly spaced frames.
- Inside phones, cards fan, flip and blur in (e.g. the Ring card deck rotating between 1.1 s and 3.3 s), but the global linear pan dominates the energy signal.
No easing on the reel — a showreel device, not product motion.

## 8. Brand system
n/a — not a brand system. Identity cues: dot-matrix numerals, a red index/badge accent, and one-gradient-per-metric colour coding behave like a mini identity.

## 9. UX
- Strong glanceability: hue tells you the metric category before you read.
- The ✕ / dial / ✓ bottom bar gives a consistent commit/cancel pattern across builder steps.
- Risks: faint tone-on-tone labels and white text on pale gradients fail contrast; dot-matrix numerals at small sizes would be hard to read; the reel moves too fast to study any screen.

## 10. Craft signals
- Dot-matrix numerals are used only for hero values; times use a solid tabular grotesk.
- Each metric owns exactly one gradient family, reused between the "Watch" grid and the detail screen.
- Red is reserved for the dial index and step badge.
- Bottom bar buttons are ≈80 px circles symmetric about the dial on every screen.
- Light screens use #f1f1f1, not pure white, so the gradient cards are the brightest things.

## 11. Reproduction recipe
```css
:root{--stage:#080808;--chrome:#f1f1f1;--ink:#111;--accent:#e01b24;--r-card:32px;--r-screen:44px;
  --g-sun:radial-gradient(120% 80% at 50% 70%,#f5e34a 0,#f08a3a 45%,#f2b7a6 100%);
  --g-sleep:linear-gradient(160deg,#d9c9f2 0,#7728ca 60%,#5a0fb0 100%);
  --g-alarm:radial-gradient(100% 80% at 50% 60%,#9ef58a 0,#baedbb 50%,#9fd2ff 100%)}
.widget{border-radius:var(--r-card);padding:20px;color:var(--ink);box-shadow:0 30px 60px -20px rgba(0,0,0,.15)}
.widget.sun{background:var(--g-sun)} .widget.sleep{background:var(--g-sleep);color:#fff}
.dotnum{font-family:"Doto","DotGothic16",monospace;font-size:110px;letter-spacing:.02em}
.dial{width:260px;height:130px;border-radius:130px 130px 0 0;
  background:repeating-conic-gradient(from -90deg at 50% 100%,#bbb 0 .4deg,transparent .4deg 3deg);
  -webkit-mask:radial-gradient(circle at 50% 100%,transparent 100px,#000 101px 128px,transparent 129px)}
.step{background:var(--accent);color:#fff;border-radius:9999px;width:32px;height:32px}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 9 | Vivid mesh gradients framed by neutral chrome and crisp dot numerals; very cohesive. |
| Originality | 8 | Dot-matrix numerals plus per-metric gradients and a tick-dial stepper feel distinctive. |
| Usability | 6 | Colour-coding aids scanning, but many labels fail contrast. |
| Craft | 8 | Consistent bottom bar, reserved red accent, careful card system across many screens. |

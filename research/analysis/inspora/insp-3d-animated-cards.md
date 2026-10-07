---
id: insp-3d-animated-cards
source: inspora
category: Web
status: analyzed
title: "3D animated cards"
creator: "Praveen Kumar (@praveenisomer)"
styles: [soft-3d, cinematic-3d, minimal-swiss]
patterns: [3d-render-media-card, inverted-twin-cards, inset-media-frame, mono-body-sans-title, looping-object-animation, ghost-button-cta]
mode: mixed
palette: ["#c1c1c1", "#000000", "#ffffff", "#fce6cf", "#f7b071", "#f8c192", "#2a2a2a", "#9a9a9a"]
type_families: ["Plus Jakarta Sans (likely)", "light monospace, Fragment Mono / IBM Plex Mono Light-like (likely)"]
type_class: [geometric-sans, mono]
radius_px: [24, 16, 10]
motion: {durations_s: [0.9, 0.87, 1.1, 1.13], easing: [ease-in, ease-out, linear], loop: true}
scores: {aesthetics: 8, originality: 6, usability: 6, craft: 7}
craft_signals: [inset-media-with-concentric-radius, single-peach-hue-renders, black-white-twin-polarity, mono-body-for-technical-tone, translucent-glass-coin-render, depth-of-field-on-falling-discs]
anti_patterns: [grey-mono-body-on-white-fails, button-merges-into-black-card]
---
# 3D animated cards — Praveen Kumar

## 1. Snapshot
- **Subject:** A 15.1 s, 1600×1200 loop of two feature cards (black "AI Browser Content", white "Optical Fibers"), each topped by a looping peach-orange 3D render: a glass coin with a logo, and a cascade of falling discs.
- **Why it's remarkable:** It is a minimal card template where all the expression lives in the 3D media. Both renders share one peach/orange material palette, so the black and white cards read as a matched pair.

## 2. Composition & layout
- **Cards:** two cards about 586×772 px, gap about 110 px, centred on a #c1c1c1 stage at y≈210→983.
- **Card anatomy:**
  - an 11 px frame of the card colour around an inset media panel of about 566×420 px (≈4:3) with a ~16 px radius, inside an outer radius of ~24 px;
  - a title at about 40 px, 48 px below the media;
  - about 4 lines of mono body;
  - a "Learn More" button bottom-left, about 126×50 px with a ~10 px radius.
- **Spacing:** left content inset is about 30 px and the body measure about 52 characters. Generous empty space sits between body and button (about 60 px).

## 3. Typography
- **Titles:** a geometric sans with a single-storey "a" and round "C/O" (very close to Plus Jakarta Sans) at regular 400, about 40 px, with −0.02 em tracking.
- **Body:** a light monospace at about 17 px with line height about 1.05. It is unusually tight for mono and reads almost like a code comment block. Grey #9a9a9a.
- **Button label:** the sans at 15 px medium, white.
- The sans/mono pairing gives a "tech-spec" voice to marketing copy.

## 4. Colour
| Hex | Role | Share (key frame) |
|---|---|---|
| #c1c1c1 | stage | 52% |
| #fce6cf | render backdrop (peach) | 18% |
| #000000 | dark card | 10% |
| #ffffff | light card | 10% |
| #f7b071 / #f8c192 | orange 3D material | 5% |
| #2a2a2a | button fill | <1% |
| #9a9a9a | mono body | <1% |

WCAG checks:
- Title white on #000 and black on #fff are both 21:1.
- Mono body #9a9a9a on #000 is 7.46:1, but the same grey on the white card is **2.81:1 (fails)**. The designer reused one grey for both polarities.
- The button text white on #2a2a2a is 14.35:1. On the black card the button fill is only 1.46:1 against the card, so the button boundary nearly disappears.

## 5. Depth & material
- **Card surfaces:** flat colour with no shadow on the grey stage. All depth is inside the media.
- **Left render:** a translucent orange glass coin with a frosted rim, inner glow and embossed "W"-like mark, floating on a peach backdrop with a soft contact shadow.
- **Right render:** about a dozen matte orange discs tumbling, with strong depth of field (foreground discs crisp, background discs heavily blurred at the top edge), which suggests camera optics.

## 6. Components & patterns
- A media-led feature card in two polarities (inverted twin), the same component with background and text swapped.
- An inset media frame, where the card colour forms a ~11 px mat around the image, echoing a device bezel.
- Primary button in near-black (#2a2a2a) on both cards.

## 7. Motion
Measured: 15.15 s at 60 fps, motion fraction 0.24, `seamless_loop_likely: true`. Segments:

| Start–end | Duration | Shape (peak_at) |
|---|---|---|
| 0.60–1.50 s | 0.9 s | ease-in (0.69) |
| 4.77–5.63 s | 0.87 s | ease-out (0.21) |
| 8.67–9.77 s | 1.1 s | ease-out (0.32) |
| 12.53–13.67 s | 1.13 s | continuous/linear |

That is about one motion beat every 3.9 s, with idle drift between. In the frames:
- The coin tilts and rotates about its axis between roughly 20° and 35° (compare 0.84 s and 2.52 s, where the logo is lost to specular glare).
- The discs rotate in place and shift their spin phases.

Nothing on the cards themselves (title, button) moves; the motion is confined to the media wells. There is no visible hover state.

## 8. Brand system
n/a — not a brand system. Identity cues: monochromatic peach-orange renders as the "product colour", and the black/white card duality.

## 9. UX
- **Strengths:** A clear title, body and CTA hierarchy, and the large media draws attention.
- **Risks:**
  - The body fails contrast on the white card.
  - "Learn More" twice is non-descriptive for screen readers.
  - The dark card's button lacks an edge.
  - Continuous 3D loops need a `prefers-reduced-motion` fallback.

## 10. Craft signals
- The inner media radius (about 16 px) is roughly the outer radius (about 24 px) minus the 11 px mat, so the corners are concentric.
- Both renders use the same peach backdrop (#fce6cf) and orange material, so a pair of unrelated topics feels systematic.
- The mono body is set at very tight leading (about 1.05), which reads as a deliberate typographic texture.
- The falling-disc render applies depth-of-field blur to distant discs at the top edge.
- The title baseline and button position match across both cards (y≈712 and y≈921).

## 11. Reproduction recipe
```css
:root{--stage:#c1c1c1;--peach:#fce6cf;--orange:#f7b071;--btn:#2a2a2a;--mute:#9a9a9a;
  --r-card:24px;--mat:11px;--r-media:calc(var(--r-card) - var(--mat) + 3px)}
.card{width:586px;border-radius:var(--r-card);padding:var(--mat);background:#000;color:#fff}
.card.light{background:#fff;color:#000}
.card.light p{color:#6b6b6b} /* fix: #9a9a9a fails on white */
.media{aspect-ratio:4/3;border-radius:var(--r-media);background:var(--peach);overflow:hidden}
.card h3{font:400 40px/1.1 "Plus Jakarta Sans",sans-serif;letter-spacing:-.02em;margin:48px 20px 24px}
.card p{font:300 17px/1.05 "Fragment Mono","IBM Plex Mono",monospace;color:var(--mute);margin:0 20px}
.btn{font:500 15px "Plus Jakarta Sans";background:var(--btn);color:#fff;border-radius:10px;padding:14px 24px;
  box-shadow:inset 0 0 0 1px rgba(255,255,255,.08)}
@keyframes coin{0%,100%{transform:rotateY(-20deg) rotateX(10deg)}50%{transform:rotateY(25deg) rotateX(18deg)}}
.coin{animation:coin 7.6s cubic-bezier(.45,0,.55,1) infinite}
@media (prefers-reduced-motion:reduce){.coin{animation:none}}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | A cohesive peach material story, and the black/white pairing is crisp. |
| Originality | 6 | A standard media card; the 3D renders carry the novelty. |
| Usability | 6 | Readable on the dark card, but the light card's body fails and the CTAs are generic. |
| Craft | 7 | Concentric radii and aligned baselines; one grey was reused across polarities. |

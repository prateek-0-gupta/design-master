---
id: insp-2-7
source: inspora
category: Motion
status: analyzed
title: "Stamp Folder animation"
creator: "@AdityaSur11"
styles: [glassmorphism, physical-material, micro-interaction, playful-rounded]
patterns: [frosted-folder-cover, hover-peek-contents, click-fan-out-items, colour-variant-swatches, 3d-perspective-card, selected-swatch-ring]
mode: light
palette: ["#f3f3f3", "#e3bd4a", "#d6249f", "#1d1d1d", "#3d4342", "#7aa39b", "#eeeadf", "#786b6d"]
type_families: ["Noto Sans JP / Hiragino Sans (likely)", "Inter / SF Pro (likely)"]
type_class: [neo-grotesk, humanist-sans]
radius_px: [28, 9999]
motion: {durations_s: [0.57, 0.37, 0.5, 0.6, 0.77], easing: [ease-out, ease-in-out], loop: false}
scores: {aesthetics: 8, originality: 7, usability: 7, craft: 8}
craft_signals: [frosted-cover-blurs-contents-behind, label-text-adapts-to-cover-colour, perforated-stamp-edges, stamps-tilt-at-different-angles, double-hairline-at-cover-foot, swatch-ring-offset-2px, back-panel-same-hue-darker]
anti_patterns: [yellow-swatch-low-contrast-on-grey, frost-blur-hides-content-identity]
---
# Stamp Folder animation — @AdityaSur11

## 1. Snapshot
- **Subject:** A 22.5 s, 1920×1918 clip of a "集めたもの / Mini Archive" folder holding Japanese postage stamps. The cover is a frosted, translucent panel in yellow, magenta or black, chosen by three colour dots.
  - On hover, the cover swings open and stamps peek out.
  - On click, the cover folds aside and two stamps fan out at full size.
- **Why it's remarkable:** The frosted-glass cover lets the stamps' colours bleed through as blurred shapes, so the closed folder already hints at its contents. A colour-variant picker shows the material holding up across light, saturated and dark tints.

## 2. Composition & layout
- **Folder:** about 455×615 px in the 1920-px key frame, centred slightly above middle (top y≈455). The canvas is #f3f3f3 with about 75% empty space.
- **Swatches:** three 85 px dots spaced 125 px apart centre-to-centre, 270 px below the folder. The selected dot gets a 2 px ring with about 4 px offset.
- **Cover label:** bottom-left with a 40 px inset. "集めたもの" in about 34 px Japanese sans, "Mini Archive" in about 19 px Latin below, and two 1 px hairlines about 20 px apart near the foot of the cover.
- **Open state (18.72 s):** the cover rotates to a narrow sliver at the left (≈90 px wide perspective). A pale inner card and two stamps (≈250×330 each) spread rightward, slightly overlapping and tilted.

## 3. Typography
- **Japanese title:** a Noto Sans JP or Hiragino-like gothic, regular weight, at about 34 px.
- **Latin subtitle:** "Mini Archive" in an Inter or SF-like sans, about 19 px, at about 55% opacity of the label colour.
- **Label colour adapts per variant:** near-black on yellow, white on magenta and black.
- **Stamp art:** bold display kanji ("自由な鳥"), "84円", "NIPPON" and vertical mincho "静かな時間" carry the illustration's own typographic flavour.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #f3f3f3 | canvas | 89% |
| #e3bd4a / #d4b23d | yellow cover / swatch | variant |
| #d6249f | magenta cover / swatch | variant |
| #1d1d1d / #303031 | black cover / swatch | 3% (key) |
| #3d4342 / #7aa39b | stamp teal and wave art showing through | 4% |
| #eeeadf / #dcd5c0 | stamp paper | 1% |
| #786b6d | stamp shadow tones | <1% |

WCAG checks:
- **Label on cover:** white on black #1d1d1d is 16.86:1; "Mini Archive" grey #8a8a8a on black is 4.88:1; white on magenta is 4.55:1 (just passes); dark #3d3d3d on yellow is 6.02:1. Label colour is switched per variant to stay legible.
- **Swatches on canvas:** the yellow swatch is 1.85:1 (it fails the 3:1 non-text guideline), and the magenta swatch is 4.10:1.

## 5. Depth & material
- **Cover:** a frosted translucent material with heavy backdrop blur (≈30 px). The stamps' teal, cream and red show through as soft blobs, and the cover is visibly brighter where stamps sit beneath.
- **Edges:** a light inner highlight along the top-left edge, and about a 28 px radius.
- **Back panel:** the same hue, darker, peeking about 30 px on the right to give thickness (black variant: #303031).
- **Stamps:** perforated (scalloped) edges about 6 px deep, cream paper, with soft shadows. They sit at different small rotations (≈−3° to +5°).
- **Perspective:** the cover hinge on the left produces a trapezoid when partially open.

## 6. Components & patterns
- **Variant swatch row:** three colour radios with a ring-offset selection indicator.
- **Hover:** the cover lifts and swings about 15–20°, and the stamps slide out about 15% (1.25 s, 6.24 s, 11.23 s).
- **Rest:** stamps tuck fully inside, visible only through the frost (3.74, 8.74, 13.73 s).
- **Click open:** the cover folds back to about 80° and the stamps fan out fully (16.23, 18.72, 21.22 s).

## 7. Motion
Measured: 22.47 s at 30 fps, 16 segments, motion fraction 0.28, median 0.37 s, not a loop.
- **Mostly ease-out:** 1.40–1.97 s (0.57 s, peak 0.26), 2.57–2.93 s (0.37 s, peak 0.23), and many 0.37 s segments with peak about 0.23, which reads as snappy settle-heavy springs.
- **Longer open/fan sequences:** 15.27–15.87 s (0.60 s, ease-out), 17.87–18.63 s (0.77 s, symmetric) and 20.80–21.40 s (0.60 s, symmetric) are the click-open plus stamp fan.
- **Colour switch:** cover hue changes (≈6.2 s, 11.1 s) register as short 0.2–0.3 s segments, consistent with a quick cross-fade.
- **Pattern:** hover is about 0.37 s, open about 0.6–0.77 s, recolour about 0.2–0.3 s, a clear three-tier timing.

## 8. Brand system
n/a — not a brand system. Identity cues: Japanese collector aesthetic (furoshiki-wave stamp art, kanji titles), CMY-ish variant set (yellow / magenta / key black), and the same folder-object family as insp-2-1 by the same creator.

## 9. UX
- **Strengths:**
  - The frosted cover previews contents without opening.
  - Label colour adapts per variant for legibility.
  - Hover and click have distinct depths of reveal.
- **Risks:**
  - The yellow swatch fails non-text contrast on #f3f3f3.
  - The swatches have no labels.
  - Blurred contents through the frost are atmospheric but not identifiable.
  - Hover-dependent peek is lost on touch.

## 10. Craft signals
- The frosted cover shows the blurred colours of the exact stamps inside (teal and cream bleed visible on all three variants).
- The label flips between dark and light ink per cover colour.
- Two 1 px hairlines at the cover foot imply a printed folder lining.
- The stamps carry real perforation geometry and differing rotations.
- The selected swatch gets a 2 px ring with offset, so the dot itself is unchanged.
- The back panel uses the same hue at lower lightness for a thickness cue.

## 11. Reproduction recipe
```css
:root{--canvas:#f3f3f3;--cover:#e3bd4a;--label:#2b2b2b;}
[data-variant=magenta]{--cover:#d6249f;--label:#fff}
[data-variant=black]{--cover:#1d1d1d;--label:#fff}
.stage{perspective:1400px;background:var(--canvas)}
.folder{position:relative;width:455px;height:615px;transform-style:preserve-3d}
.folder .back{position:absolute;inset:0 -30px 0 30px;border-radius:28px;background:color-mix(in oklab,var(--cover),#000 25%)}
.stamp{position:absolute;width:250px;aspect-ratio:3/4;background:#eeeadf;
  -webkit-mask:radial-gradient(circle 6px at 6px 6px,transparent 98%,#000) -6px -6px/16px 16px; /* perforation */
  transition:transform .6s cubic-bezier(.16,1,.3,1)}
.cover{position:absolute;inset:0;border-radius:28px;color:var(--label);
  background:color-mix(in srgb,var(--cover) 82%,transparent);backdrop-filter:blur(30px) saturate(1.3);
  box-shadow:inset 1px 1px 0 rgba(255,255,255,.35),0 20px 40px rgba(0,0,0,.12);
  transform-origin:left center;transition:transform .37s cubic-bezier(.2,.8,.2,1),background-color .25s}
.folder:hover .cover{transform:rotateY(-18deg)}
.folder.open .cover{transform:rotateY(-80deg)}
.folder.open .stamp:nth-child(1){transform:translateX(240px) rotate(-3deg)}
.folder.open .stamp:nth-child(2){transform:translateX(480px) rotate(4deg)}
.swatch{width:42px;height:42px;border-radius:9999px;background:var(--c)}
.swatch[aria-checked=true]{outline:2px solid #1d1d1d;outline-offset:3px}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Frosted tinted covers over illustrated stamps are rich yet calm, and all three variants are resolved. |
| Originality | 7 | It extends a familiar folder hover, but the frosted preview of contents is a nice twist. |
| Usability | 7 | The preview and adaptive labels are good; the swatch contrast and touch hover are weak. |
| Craft | 8 | Perforations, adaptive ink, hairline lining and consistent three-tier timing. |

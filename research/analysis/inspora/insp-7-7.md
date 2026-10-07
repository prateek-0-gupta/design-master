---
id: insp-7-7
source: inspora
category: Print
status: analyzed
title: "Stamp designs"
creator: "@nilseller"
styles: [swiss-grid-poster, maximalist-color, flat-illustration]
patterns: [curated-specimen-slideshow, object-on-dark-stage, rotated-edge-typography, geometric-pictogram, denomination-as-display-type]
mode: dark
palette: ["#262626", "#eeeaeb", "#d63388", "#5e397f", "#d72923", "#d9bccb"]
type_families: ["Crouwel-style square grid lettering (Gridnik / New Alphabet family, likely)", "Helvetica / Univers (other stamps)"]
type_class: [display, neo-grotesk]
radius_px: [0]
motion: {durations_s: [6.5, 0.72], easing: [hard-cut], loop: true}
scores: {aesthetics: 8, originality: 5, usability: 6, craft: 7}
craft_signals: [constant-stage-colour-across-cuts, centred-object-fixed-scale, perforation-edge-preserved, three-face-isometric-cube-from-flat-tints]
anti_patterns: [no-attribution-of-original-designers, mixed-scan-quality]
---
# Stamp designs — @nilseller

## 1. Snapshot
- **Subject:** A 6.5 s, 960×720 slideshow of nine modernist postage stamps scanned and centred on a charcoal stage. The set includes Dutch PTT stamps (cube, maze, "Flower field"), Munich 1972 Olympic pictogram stamps for Australia, Yugoslavia 1979, Iceland Europa, Venezuela 1979, and a 2012 Stedelijk Museum issue.
- **Why it's remarkable:** It is a curated mood board, not original work. Its value is showing how stamps compress a whole identity (country, value, theme) into roughly 35×25 mm with flat tints and one grotesk or grid face.

## 2. Composition & layout
- **Stage:** solid #262626 (72% of frame).
- **Key-frame stamp:** about 535×365 px (x 211→746, y 177→542), a 1.47:1 landscape. It is optically centred, with about 177 px margin above and 178 px below.
- **Stamp anatomy:**
  - The country name runs vertically along the left edge, rotated 90° and reading bottom-to-top, at about 330 px long.
  - The denomination "20 c + 10" runs along the right edge rotated the other way.
  - The image (an isometric cube about 370 px wide) fills the centre.
  - The white border inside the perforations is about 25 px.
- The other stamps repeat the edge-text/central-glyph grid. One example is the Munich stamp, which has "Australia" at top, "Munich 1972" stacked vertically, and a pictogram at centre.

## 3. Typography
- **Key frame:** "NEDERLAND" and "20 c + 10" are set in a square, monoline grid face with right-angle terminals and open counters, in the Wim Crouwel tradition (closest match: Gridnik or Foundry Fabriek). Stroke is about 7 px at about 50 px cap height, in magenta #d63388.
- **Other frames:**
  - Helvetica Bold for "nederland 40+20 cent", lowercase and set large (cap height about 1/4 of the stamp).
  - A Univers/Helvetica Light for "Munich 1972".
  - An oversized red Helvetica-style "SM" on the Stedelijk stamp.
  - A Didone or Bodoni caps "ÍSLAND".
- **The denomination is display type, not small print:** it gets equal billing to the country name.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #262626 | presentation stage | 72% |
| #eeeaeb | stamp paper | 11.5% |
| #d63388 | magenta type + left cube face | 5.2% |
| #5e397f | violet top face | 4.2% |
| #d72923 | vermilion front face | 4.2% |
| #d9bccb | pink paper tint (ink spread) | 1.9% |

WCAG checks:
- Paper on stage: 12.69:1.
- Magenta type on paper: 3.75:1 (large-only, fine at 50 px).
- Vermilion on paper: 4.16:1.
- Violet on paper: 7.44:1.

The three cube faces get three hues of similar value (magenta, violet, red) rather than light/mid/dark. The cube reads by hue difference alone, which is a bold choice.

## 5. Depth & material
The only depth is the isometric illusion. Material is real print: visible flexo/gravure mottling inside the colour fields (the leather-like texture on each cube face), ink-spread halos and torn perforation teeth spaced about 18 px apart. There are no digital shadows, so each stamp sits flat on the stage.

## 6. Components & patterns
- **Rotated edge labels:** country on one side and value on the other, an efficient frame for any square motif.
- **Pictogram systems:** Otl Aicher-style figures (cyclist, swimmer) paired with an abstract field such as a running track or wave scallops.
- **Series logic:** recurring Olympic rings, recurring "NEDERLAND" placement.

## 7. Motion
Measured: duration 6.5 s, sampled at 4 fps, motion_fraction 1.0, a single 6.0 s segment labelled "continuous/linear" (peak_at 0.65, energy CV 0.2). As with any cut-based reel, the "continuous" label reflects a change at almost every sample. Each of the nine evenly spaced frames (0.36 → 6.14 s) shows a different stamp, so the estimated dwell is about 0.72 s per stamp with hard cuts. The stage colour and centre stay fixed, so only the object changes. seamless_loop_likely is false.

## 8. Brand system
n/a — not a brand system. Several stamps are themselves fragments of brand systems: the Munich 1972 pictograms, and the Stedelijk "SM" wordmark crossing its own architectural line drawing.

## 9. UX
As a reference reel it works: there is one object per beat, at consistent scale. It fails as documentation, because there are no captions, no years beyond what's printed, and no designer credits. At 0.72 s per stamp the small type is unreadable in real time.

## 10. Craft signals
- The stage hex #262626 is identical across all nine frames, and every stamp is centred.
- The perforation edge is kept rather than cropped to the image, which reads instantly as "stamp".
- On the key frame the vertical "NEDERLAND" (x≈240–270) and "20 c + 10" (x≈690–720) are symmetric about the cube's centre axis.
- The cube's faces meet at a single vertex at the exact stamp centre (≈480, 360).

## 11. Reproduction recipe
```css
:root{--stage:#262626;--paper:#eeeaeb;--mag:#d63388;--vio:#5e397f;--ver:#d72923;
  --grid-face:"Gridnik","Foundry Fabriek","Eurostile",sans-serif;}
.stage{background:var(--stage);aspect-ratio:4/3;display:grid;place-items:center}
.stamp{width:56%;aspect-ratio:1.47;background:var(--paper);padding:25px;display:grid;
  grid-template-columns:auto 1fr auto;align-items:center;
  -webkit-mask:radial-gradient(circle 6px at 9px 9px,#0000 98%,#000) -9px -9px/18px 18px;}
.edge{writing-mode:vertical-rl;transform:rotate(180deg);font:400 50px/1 var(--grid-face);color:var(--mag)}
.edge.right{transform:none}
.cube{clip-path:polygon(50% 0,100% 25%,100% 75%,50% 100%,0 75%,0 25%);
  background:conic-gradient(from 60deg at 50% 50%,var(--vio) 0 120deg,var(--ver) 0 240deg,var(--mag) 0)}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Strong selection; the dark stage makes the tints pop. |
| Originality | 5 | A curation of existing historical work, with no new design. |
| Usability | 6 | Consistent framing, but too fast and unlabelled to study. |
| Craft | 7 | Clean, consistent presentation. Scan quality varies (mottling on some). |

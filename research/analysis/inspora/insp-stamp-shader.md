---
id: insp-stamp-shader
source: inspora
category: Motion
status: analyzed
title: "Stamp Shader"
creator: "@loficosmos1"
styles: [editorial-serif, physical-material, terminal-mono, grain-noise]
patterns: [postage-stamp-project-cards, scattered-collage-hero, hover-tooltip-label, focus-mode-lightbox, drag-down-to-dismiss, material-shader-on-hover, mono-meta-labels]
mode: mixed
palette: ["#fbf8f3", "#2b2a27", "#8a8780", "#23221e", "#3f3e3d", "#646464", "#9a9893", "#a8d48a"]
type_families: ["Newsreader / Source Serif-style text serif (likely)", "Space Mono / JetBrains-like monospace (likely)", "Inter (likely, body)"]
type_class: [editorial-serif, mono, neo-grotesk]
radius_px: [0, 8]
motion: {durations_s: [0.37, 0.17, 0.6, 11.24], easing: [ease-out], loop: true}
scores: {aesthetics: 9, originality: 9, usability: 7, craft: 9}
craft_signals: [perforated-stamp-edge-geometry, embossed-type-in-shader, collage-random-rotations, page-dims-before-focus, gesture-hint-in-mono-caps, italic-nav-active-state, warm-paper-off-white]
anti_patterns: [grey-mono-labels-below-aa, gesture-only-dismiss]
---
# Stamp Shader — @loficosmos1

## 1. Snapshot
- **Subject:** An 11.2 s, 3412×1904 @120 fps capture of a designer portfolio ("Bill Guo", CMU) whose hero scatters case studies as postage stamps; hovering one shows a black tag, clicking it dims the page into a dark focus view where the stamp becomes an embossed obsidian/wood-grain 3D shader, and "drag down to escape" returns.
- **Why it's remarkable:** Projects as collectible physical objects, with a real-time material shader (embossed type, wood-grain swirl, a woven snake-scale ring) — portfolio craft demonstrated by the navigation itself.

## 2. Composition & layout
- **Home (light):** a 12-column editorial grid on warm paper #fbf8f3:
  - top-left identity block in mono caps;
  - "MENU" column (Work / About / Craft / Writing in serif, active "Work" italic bold);
  - "PROFILE" and "HOW" text columns top-right (≈ 15 px sans, 1.5 leading);
  - a contact column of mono caps links.
- Hero headline bottom-left "Designing *artifacts* that feel alive." ≈ 76 px serif (at 1600 px width), leading ≈ 1.0, with "artifacts" in italic.
- Stamps (≈ 180–240 px each) are scattered diagonally from centre to bottom-right at random rotations (−15° to +20°), overlapping; category labels (PRODUCT, VISUAL) float near clusters; a "Works" card peeks from the right edge with a "VIEW ALL →" link. A "SCROLL ↓ FOR WORK" chip is centred at the bottom.
- **Focus view (dark):** the page fades to #23221e; one stamp centred at ≈ 500×630 px (in the 2000 px key frame); "VIEW CASE STUDY →" mono below it and "DRAG DOWN TO ESCAPE." at the bottom edge.

## 3. Typography
- **Display/nav:** a text serif with sharp, calligraphic italics (Newsreader / Source Serif-like), ≈ 76 px for the headline and ≈ 18 px for the nav.
- **Meta:** monospace caps (≈ 11 px, tracking +0.08 em) for labels — MENU, PROFILE, CONTACT, SCROLL ↓ FOR WORK, DRAG DOWN TO ESCAPE.
- **Body:** a neo-grotesk ≈ 13–14 px (#4a4844) with underlined links (CMU, Feather, Kensho).
- On the stamps themselves: mono numerals (05, 2026, 08), CJK + Latin "GAO HAN", script "Specimen." — each stamp has its own typographic voice.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #fbf8f3 | paper background (light) | ~85% light state |
| #2b2a27 | headline, nav | — |
| #4a4844 | body text | — |
| #8a8780 | mono labels | — |
| #23221e | focus-mode backdrop | 89% dark state |
| #3f3e3d / #646464 / #777777 | obsidian shader mid-tones | 7% |
| #141416 | deepest grooves | 0.8% |
| #a8d48a (est.) | sage-green stamp art (accent) | small |

WCAG checks:
- Headline #2b2a27 on paper: 13.55:1.
- Body #4a4844 on paper: 8.61:1.
- **Mono labels #8a8780 on paper: 3.38:1** (AA-large only, and they are 11 px).
- "VIEW CASE STUDY" ≈#9a9893 on #23221e: 5.52:1.
- "DRAG DOWN TO ESCAPE." ≈#5a5955 on #23221e: **2.27:1 (fails)** — the dismiss instruction is the faintest text.

## 5. Depth & material
- **Light state:** stamps cast soft drop shadows (≈ 20 px blur, 10% black) and sit at varied z-orders; perforated edges are geometric half-circle bites (≈ 14 bites per long side).
- **Focus state:** the shader renders an obsidian/lacquer surface with a swirling wood-grain normal map, raised embossed letters ("KENSHO TECHNOLGIES", "05", "2026", "08") catching a top-left light, and an inset ring of checkered snake scales (the "kogei" craft texture). Specular highlights move with the cursor (the hand cursor is visible).

## 6. Components & patterns
- Stamp cards as project thumbnails; a black pill tooltip on hover ("KENSHO TECHNOLOGIES" ≈ 8 px mono caps, white on #1a1a1a).
- Focus lightbox: page dims (≈ 4.37 s shows a ~60% dark overlay mid-transition), then the stamp scales up and centres.
- Gesture dismissal (drag down) with a text hint; a secondary "View case study →" link.
- Italic-as-active-state in the nav (Work).

## 7. Motion
Measured (m0_motion.json): 11.24 s at 120 fps, motion_fraction 0.10, three segments, all ease-out, `seamless_loop_likely: true` (first/last diff 1.71):
- **4.17–4.53 s (0.37 s), peak_at 0.32:** dim + zoom into focus mode;
- **7.33–7.50 s (0.17 s), peak_at 0.10:** quick tilt/drag on the stamp;
- **8.13–8.73 s (0.60 s), peak_at 0.19:** drag-down dismiss, with the stamp flying back into the collage and the page brightening (home by 9.37 s).
Hover at 1.87–3.12 s swaps the stamp to its dark material in place and shows the tooltip (sub-threshold). The open is faster (0.37 s) than the close (0.60 s), which lets the object "settle" back into the pile.

## 8. Brand system
n/a — not a brand system, but a coherent personal identity: paper-and-ink palette, serif + mono pairing, the stamp/collectible metaphor, and "artifacts" as the conceptual keyword echoed in the headline.

## 9. UX
- Delightful and on-message for a craft-focused designer; hover labels name each project before commitment.
- **Risks:**
  - Gesture-only dismissal (drag down) needs Esc / a close button for mouse and keyboard users.
  - The dismiss hint fails contrast.
  - Rotated, overlapping stamps make the click targets ambiguous.
  - Mono labels at 11 px and 3.4:1 are hard to read.

## 10. Craft signals
- Perforation bites are evenly spaced and the corners resolve cleanly (a bite never lands on a corner).
- The embossed letters in the shader keep the same mono typeface as the flat stamp ("05 / 2026 / 08" positions match between the light and dark versions).
- The page fades to dark before the stamp enlarges — no flash of overlapping UI.
- The headline italicises only the key noun ("artifacts").
- The nav's active state uses italic + weight, not colour.
- The background is a warm off-white (#fbf8f3), not #fff, to evoke paper.

## 11. Reproduction recipe
```css
:root{--paper:#fbf8f3;--ink:#2b2a27;--body:#4a4844;--meta:#8a8780;--night:#23221e;
  --serif:"Newsreader","Source Serif 4",serif;--mono:"Space Mono","JetBrains Mono",monospace}
body{background:var(--paper);color:var(--body)}
.hero{font:400 clamp(40px,5vw,76px)/1 var(--serif);color:var(--ink)} .hero em{font-style:italic}
.meta{font:400 11px/1.4 var(--mono);letter-spacing:.08em;text-transform:uppercase;color:var(--meta)}
.stamp{--b:7px;width:200px;aspect-ratio:4/5;background:#fff;
  -webkit-mask:radial-gradient(circle var(--b) at var(--b) var(--b),#0000 98%,#000) calc(-1*var(--b)) calc(-1*var(--b))/calc(2*var(--b)) calc(2*var(--b));
  filter:drop-shadow(0 10px 20px rgba(0,0,0,.1));transform:rotate(var(--r,-8deg));transition:transform .37s cubic-bezier(.2,.8,.2,1)}
.focus{position:fixed;inset:0;background:var(--night);opacity:0;transition:opacity .37s ease-out}
.focus[open]{opacity:1}
.tip{background:#1a1a1a;color:#fff;font:10px var(--mono);border-radius:8px;padding:4px 8px}
```
Shader (three.js): a stamp-shaped plane with a normal map from a swirl noise (`fbm(rot(uv)*8)`), roughness ≈ 0.2, a dark albedo #1a1a1a, an embossed height from the rendered text texture, and an environment light following the pointer.

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 9 | Editorial paper layout plus a striking obsidian material moment. |
| Originality | 9 | Projects as shader-rendered postage stamps is a distinctive concept. |
| Usability | 7 | Clear hover labels; gesture-only exit and faint meta text. |
| Craft | 9 | Perforation geometry, type continuity across states, careful transitions. |

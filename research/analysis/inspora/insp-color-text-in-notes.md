---
id: insp-color-text-in-notes
source: inspora
category: Motion
status: analyzed
title: "color text in Notes"
creator: "Damir Sokolovsky"
styles: [dark-premium, micro-interaction, aurora-glow]
patterns: [text-color-picker-popover, recent-colors-history-list, focus-paragraph-dim-others, glow-sweep-on-apply, selection-highlight-tinted, camera-zoom-to-detail]
mode: dark
palette: ["#08090b", "#131416", "#27282b", "#3a3b3e", "#f2f2f2", "#5ee08a", "#ee5fa8", "#e3b341"]
type_families: ["SF Pro Text (likely)"]
type_class: [neo-grotesk]
radius_px: [28, 9999]
motion: {durations_s: [0.37, 0.63, 0.13, 0.8], easing: [ease-out], loop: true}
scores: {aesthetics: 9, originality: 8, usability: 7, craft: 9}
craft_signals: [selection-tint-takes-new-hue, glow-bloom-sweeps-left-to-right, history-rows-show-colored-snippet, swatch-grid-3x3-with-custom-ring, inactive-paragraphs-dimmed-to-1-65, native-ios-chrome-unchanged]
anti_patterns: [dimmed-paragraphs-unreadable, violet-text-below-aa]
---
# color text in Notes — Damir Sokolovsky

## 1. Snapshot
- **Subject:** A 19.3 s, 1800×2160 concept for coloured text in Apple Notes (dark mode): select a phrase, a small popover offers 9 swatches plus a history of recently coloured snippets, and the chosen hue sweeps through the text with a glow.
- **Why it's remarkable:** The colour change is staged as light — the new hue blooms through the selection left to right with a soft halo, then settles to flat coloured text — while the rest of the note recedes to near-black.

## 2. Composition & layout
- Phone ≈940 px wide centred on a #08090b field with a faint green radial vignette (≈#0f1a14) behind the device.
- Native Notes chrome: status bar, nav bar "‹ Notes / Next week plans / Done" (≈30 px semibold title). Body paragraphs at x≈525 left margin, ≈770 px measure, ≈60 px line pitch, ≈45 px paragraph gap.
- Popover ≈420×190 px, anchored above the selection with a ≈16 px caret, left half a 3×3 swatch grid (≈40 px dots, ≈52 px pitch), right half a 4-row history list.
- From ≈11.8 s the camera blurs, re-frames and zooms ≈2× into a second paragraph, then pulls back by 18 s.

## 3. Typography
- SF Pro Text throughout; body ≈37 px in the 1800 px video (≈17 pt iOS body at the mockup's ≈2.2× scale), regular, leading ≈1.5.
- History list items ≈18 px medium with a 3 px coloured leading bar per row — each row previews the snippet in its own colour.
- No custom faces: the concept passes as a native feature because typography is untouched.

## 4. Colour
| Hex | Role | Share (key frame) |
|---|---|---|
| #08090b | backdrop around phone | 24% |
| #131416 | Notes canvas | 66% |
| #27282b | popover surface | 6% |
| #3a3b3e | dimmed (unfocused) paragraphs | — |
| #f2f2f2 | focused text, nav | — |
| #5ee08a / #2fd0c8 | applied green / teal glow | 4% |
| #ee5fa8, #e3b341, #8a5cf0 | other swatch hues seen in text | <1% each |

WCAG (contrast.py):
- Focused text #f2f2f2 on #131416: 16.46:1.
- Green #5ee08a: 10.98:1; pink #ee5fa8: 6.0:1; yellow #e3b341: 9.47:1 — all pass.
- Violet #8a5cf0 ("Frame 2847"): **4.27:1**, fails AA body.
- Dimmed paragraphs #3a3b3e: **1.65:1** — intentionally illegible focus effect.
- Teal text over its own selection tint (#2fd0c8 on #2a6a4a): 3.37:1 during the transient.

## 5. Depth & material
- Popover: #27282b with ≈28 px radius, a subtle top highlight and a ≈30 px dark shadow; reads as a native UIMenu.
- Swatches are glossy spheres (radial highlight top-left), the last one a hollow conic-gradient ring = custom colour.
- The glow: ≈12–20 px blurred copy of the text in the new hue, strongest at the sweep front, giving an emissive "ink being lit" look.

## 6. Components & patterns
- **Text colour popover** with swatch grid + **recent snippets** list (what you coloured, not just which colours) — reusable history is the novel bit.
- Selection highlight takes on the chosen hue at ≈40% (green selection band #2a6a4a) before collapsing to coloured text.
- Paragraph focus mode: everything except the paragraph being edited drops to ≈20% luminance.
- Existing coloured words ("bigger" yellow, "smaller" teal, "Rent"/"Dentist" red/pink) show the end state across the note.

## 7. Motion
Measured (m0_motion.json): 19.28 s at 60 fps, motion_fraction 0.10 (mostly holds and cursor travel below threshold), seamless_loop_likely true, 4 segments.
- 11.00–11.37 s (0.37 s, peak 0.05) and 11.77–12.40 s (0.63 s, peak 0.13): the camera blur-and-zoom transition — sharply front-loaded, ease-out.
- 15.47–15.60 s (0.13 s, peak 0.88, ease-in): a quick colour snap on "Frame 2847" (pink → yellow).
- 16.73–17.53 s (0.80 s, peak 0.10, ease-out): zoom back out to the full phone.
- Estimated from frames: the glow sweep across a 4-line selection takes ≈0.5–0.8 s (between 7.5 s and 9.64 s frames the selection goes purple → green with the front at line 2).

## 8. Brand system
n/a — not a brand system. Identity cues: faithful iOS Notes chrome and copy written in a dry designer voice ("make the logo bigger. Also smaller.").

## 9. UX
- Familiar entry point (selection → popover) and a history list that lets users re-apply a meaning-coded colour quickly.
- The glow confirms the action without a toast.
- Risks: the history list truncates snippets at ≈20 characters; violet fails AA; focus-dimming would hide context a real user may need while editing.

## 10. Craft signals
- History rows each carry a 3 px bar in their colour and are set in that colour.
- Glow front moves left to right along the reading direction, then decays to flat text.
- The custom-colour swatch is a hollow conic ring among filled dots.
- Unfocused paragraphs dimmed to a measured 1.65:1, so focus is unmistakable.
- No new chrome invented — only one popover is added to stock Notes.

## 11. Reproduction recipe
```css
:root{--canvas:#131416;--pop:#27282b;--text:#f2f2f2;--dim:#3a3b3e;--ease-out:cubic-bezier(.16,1,.3,1)}
.note p{color:var(--dim);transition:color .35s ease}
.note p.is-focused{color:var(--text)}
.popover{background:var(--pop);border-radius:28px;padding:16px;display:grid;grid-template-columns:repeat(3,40px) 1fr;gap:12px;
  box-shadow:0 20px 40px rgba(0,0,0,.6),inset 0 1px 0 rgba(255,255,255,.06)}
.swatch{width:40px;height:40px;border-radius:50%;background:radial-gradient(circle at 35% 30%,#fff8 0 15%,transparent 40%),var(--c)}
.swatch.custom{background:conic-gradient(red,yellow,lime,cyan,blue,magenta,red);-webkit-mask:radial-gradient(circle,transparent 55%,#000 57%)}
@keyframes ink{from{background-position:100% 0}to{background-position:0 0}}
.inked{color:transparent;background:linear-gradient(90deg,var(--c) 50%,var(--text) 50%) 100% 0/200% 100%;
  -webkit-background-clip:text;background-clip:text;animation:ink .6s var(--ease-out) forwards;
  filter:drop-shadow(0 0 12px color-mix(in srgb,var(--c) 60%,transparent))}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 9 | Near-black canvas with emissive colour feels premium; restraint makes the hues glow. |
| Originality | 8 | Colour history as text snippets and a light-sweep apply are fresh for a text editor. |
| Usability | 7 | Clear flow, but dimming and violet fail contrast; snippet truncation. |
| Craft | 9 | Native-perfect chrome, glossy swatches, directional glow and clean camera moves. |

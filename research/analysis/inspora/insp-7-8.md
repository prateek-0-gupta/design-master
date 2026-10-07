---
id: insp-7-8
source: inspora
category: Motion
status: analyzed
title: "Shader Credit Card"
creator: "@raul_dronca"
styles: [aurora-glow, grain-noise, gradient-mesh, micro-interaction]
patterns: [card-theme-picker, shader-gradient-surface, swatch-row-with-check, reveal-on-hover-controls, masked-pan-mono-name, crossfade-theme-swap]
mode: light
palette: ["#ffffff", "#0b0303", "#35090a", "#d4a727", "#956b25", "#663116", "#4d6552", "#f0eee9"]
type_families: ["Inter / SF Pro-style neo-grotesk (likely)", "Geist Mono / JetBrains Mono-style monospace (likely)"]
type_class: [neo-grotesk, mono]
radius_px: [42, 20, 9999]
motion: {durations_s: [0.33, 0.33, 0.43, 0.47], easing: [ease-out, ease-in-out], loop: false}
scores: {aesthetics: 9, originality: 7, usability: 7, craft: 8}
craft_signals: [film-grain-over-shader, swatch-is-miniature-of-theme, translucent-check-badge-on-swatch, card-lifts-to-reveal-swatches, card-ratio-iso-1.6, palette-icon-glass-button]
anti_patterns: [text-over-bright-shader-band-2.2-to-1]
---
# Shader Credit Card — @raul_dronca

## 1. Snapshot
- **Subject:** A 16.9 s, 3840×2156 at 60 fps clip of a virtual payment card whose face is a live, grainy aurora shader. Hovering reveals a row of four theme swatches (emerald, ember, graphite, ocean). Picking one cross-fades the shader to a new palette and flow shape.
- **Why it's remarkable:** The card's "material" is a living, film-grained light field rather than a static gradient. The theme picker previews each shader as a miniature linear gradient, so choice and result stay tied.

## 2. Composition & layout
- **Card:** about 1642×1027 px (an ISO ID-1-like 1.6 ratio), radius about 42 px, centred on pure white (#ffffff covers 75% of the frame).
- **Hover reveal:** On first hover (0.94 s → 2.82 s) the card rises about 230 px. A swatch row then appears about 85 px below it: four tiles of about 288×180 px with about 50 px gaps, the row centred and roughly 75% of the card width.
- **Card internals:**
  - Logomark (a dotted radial burst, about 100 px) top-left at a 96 px inset.
  - Palette-icon button (a 115 px translucent circle) top-right.
  - Masked number "•••• •••• •••• 4242" at about 58% height.
  - Cardholder name in mono below it, all on a left margin of about 96 px.

## 3. Typography
- **Last four "4242":** about 80 px Regular, in a neo-grotesk close to Inter or SF Pro, with tabular figures.
- **Masked groups:** solid 14 px dots in groups of four, with group gaps of about 1.6× the dot gap.
- **Name "RAUL DRONCA":** about 50 px uppercase monospace (Geist Mono or JetBrains Mono-like) in warm off-white (#e0d6cc), tracking about +0.04 em. Mono for the embossed-name line is a nice nod to physical card printing.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #ffffff | stage | 75% |
| #0b0303 | shader shadow core (ember theme) | 6% |
| #35090a / #663116 | ember mid-tones | 4% |
| #d4a727 / #956b25 | gold light band | 4% |
| #4d6552 / #b0b296 | transitional greens (from emerald theme) | 3% |
| #f0eee9 | name/label tint | 1% |

Themes seen in frames: emerald (#0f5a46 → #12233d), ember (#d4a727 → #35090a), graphite (#5a5a5e → #141416) and ocean (#7cc6e8 → #0c3c5c). All of these are estimated from frames.

WCAG checks:
- White on the shadow core (#0b0303) is 20.42:1.
- White on the mid gold (#956b25) is 4.76:1.
- Where the bright band crosses text, white on #d4a727 is **2.24:1**. The "4242" sits near that band in the ember theme.
- The name #e0d6cc on #35090a is 12.27:1.

## 5. Depth & material
- **Shader:** domain-warped, smoke-like gradient flow with heavy film grain (about 1–2 px noise, visible in the key frame's yellow band). The grain stops banding and gives a printed-metal feel.
- **Card shadow:** a broad soft shadow (about 60 px blur, 30 px y, roughly 20% black) on the white stage.
- **Swatches:** radius about 20 px with a subtle shadow. The selected one carries a translucent white circle (about 60 px) with a check.
- **Palette button:** a frosted circle (white at about 20% opacity) over the shader.

## 6. Components & patterns
- **Theme picker:** a hover or long-press reveal of swatches. The selected state is a check badge on the swatch; the hovered state is the cursor only, with no scale.
- **Shader card:** masked PAN, holder name, issuer mark, and a customise button that opens the picker.

## 7. Motion
Measured (m0_motion.json, 60 fps, 16.9 s, motion_fraction 0.09, mean energy 0.16, not loop-seamless, first/last diff 18.41 because it ends on a different theme). Four segments, one per interaction:
- **2.20–2.53 s (0.33 s, peak 0.25):** ease-out, the emerald flow re-forms after the card lift.
- **6.30–6.63 s (0.33 s, peak 0.55):** ease-in-out, the theme swap to ember.
- **10.13–10.57 s (0.43 s, peak 0.04):** a very fast-start ease-out, the swap to graphite.
- **14.60–15.07 s (0.47 s, peak 0.46):** ease-in-out, the swap to ocean.

Between swaps the shader keeps drifting slowly but stays under threshold. Successive frames show the plume shape evolving over about 2 s (6.57 s → 8.45 s → 10.33 s), so it is continuous, roughly linear time-driven warp. Theme swaps take 0.33–0.47 s and are fast enough to feel direct. The palette interpolates in-shader rather than as an opacity cross-fade: the 6.57 s frame shows olive (green into yellow) mid-transition.

## 8. Brand system
n/a — this is a product component, not a brand system. Identity cues: the dotted-burst mark and "light-as-material" card faces that make each user's card unique.

## 9. UX
- Personalisation with a direct preview is good.
- Swatches are large (about 144×90 CSS px) and easy to hit.
- **Risks:**
  - The bright shader regions can drop text contrast to 2.2:1. Pin a dark scrim under the number zone, or constrain the shader's luminance there.
  - Hover reveal needs a touch equivalent; the palette button provides it.
  - Continuous GPU animation on a wallet screen has battery and reduced-motion implications.

## 10. Craft signals
- Grain overlay over the shader prevents gradient banding at 4K.
- Each swatch is a static linear-gradient summary of its theme: same hue order, same dark corner.
- The check badge is translucent white, so it works on all four swatch colours.
- The card's text block shares one left margin, about 96 px, with the logomark.
- Mono is used only for the cardholder name, echoing embossed type.
- Palette interpolation happens in the shader (olive midpoint visible), not as a plain cross-fade.

## 11. Reproduction recipe
```css
:root{--stage:#fff;--r-card:21px;--r-swatch:10px;--font:"Inter",system-ui;--mono:"Geist Mono",ui-monospace;
  --ember:radial-gradient(60% 80% at 65% 20%,#d4a727,transparent 60%),radial-gradient(70% 70% at 90% 80%,#663116,transparent 70%),#0b0303;
  --emerald:radial-gradient(60% 80% at 40% 10%,#2fae86,transparent 60%),#0f2a2d}
.card{width:428px;aspect-ratio:1.6;border-radius:var(--r-card);background:var(--ember);position:relative;
  box-shadow:0 15px 30px rgba(0,0,0,.2);transition:transform .45s cubic-bezier(.2,.8,.2,1),background .4s}
.card::after{content:"";position:absolute;inset:0;border-radius:inherit;opacity:.18;mix-blend-mode:overlay;
  background:url("data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' width='120' height='120'><filter id='n'><feTurbulence baseFrequency='.9'/></filter><rect width='100%' height='100%' filter='url(%23n)'/></svg>")}
.card:hover{transform:translateY(-60px)}
.pan{font:400 21px/1 var(--font);color:#fff;font-variant-numeric:tabular-nums}
.name{font:400 13px/1 var(--mono);letter-spacing:.04em;text-transform:uppercase;color:#e0d6cc}
.swatch{width:75px;height:47px;border-radius:var(--r-swatch)}
.swatch[aria-checked=true]::after{content:"✓";display:grid;place-items:center;width:16px;height:16px;margin:auto;border-radius:50%;background:rgba(255,255,255,.35)}
```
For the live surface, use a WebGL fragment shader: fbm domain warp, a 3-stop palette uniform lerped over 0.4 s, and additive hash grain.

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 9 | Gorgeous grainy aurora faces, restrained card typography, clean white stage. |
| Originality | 7 | Shader card faces are trending; the in-shader palette lerp and swatch picker are well executed. |
| Usability | 7 | Clear picker and selection state; text contrast can fail over bright bands. |
| Craft | 8 | Grain, consistent margins, swatch-as-summary, crisp 0.33–0.47 s swaps. |

---
id: insp-1-28
source: inspora
category: Illustration
status: analyzed
title: "Liquid Glass"
creator: "@LynelDesign"
styles: [skeuomorphic, soft-3d, glassmorphism, physical-material]
patterns: [debossed-label-text, frosted-glyph-icon, glass-send-button, day-picker-pill, window-traffic-lights-tray, cropped-detail-crop]
mode: light
palette: ["#f6f6f6", "#ffffff", "#9a948c", "#5ac9fa", "#d90e10", "#ffc303", "#02c94a", "#e7e8ea"]
type_families: ["SF Pro Display (likely)"]
type_class: [neo-grotesk]
radius_px: [9999, 300, 120, 56]
motion: null
scores: {aesthetics: 8, originality: 6, usability: 5, craft: 9}
craft_signals: [debossed-text-with-light-lower-edge, double-bezel-pill-rim, coloured-glow-shadows, darker-same-hue-glyphs, active-pill-taller-than-siblings, radial-centre-weighted-fill]
anti_patterns: [low-contrast-labels, white-on-cyan-fails, crops-hide-context]
---
# Liquid Glass — @LynelDesign

## 1. Snapshot
- **Subject:** Four 2560×2560 macro crops of glossy, tactile UI parts:
  - an "Add to My Calendar" pill with a frosted calendar icon;
  - a cyan glass send/up-arrow button in a card corner;
  - a W/T/F day picker with a red selected "6";
  - a macOS-style traffic-light tray.
- **Why it's remarkable:** It is a study in material rendering rather than layout. Every element gets bevels, rim lights and tinted shadows at a zoom level where those details are judged, a reaction to Apple's "Liquid Glass" pushed back toward skeuomorphism.

## 2. Composition & layout
- Each slide is an extreme crop (roughly 4–8× an on-screen size) that cuts the object off at the right or top edge. This forces the viewer to read the material, not the layout.
- **Slide 1:** the pill runs from x≈240 to beyond 2560 and is ~1450 px tall (y≈490–1940), with an outer bezel ~45 px thick. The icon is ~520 px; the two text lines are "Add to" at ~130 px cap height over "My Cale…" at ~200 px cap height.
- **Slide 2:** a card corner with a ~300 px radius and a ~860 px circular button inset ~260 px from the edges. A 1 px-scaled (~20 px) divider line runs across the card.
- **Slide 3:** three day pills on a centred row. The selected one is ~620×880 px and larger than its ~510×750 px neighbours. A ▼ marker sits above the selected column.
- **Slide 4:** a tray of ~1450×640 px holding three ~340 px discs with ~85 px gaps, inside a window with a ~500 px corner radius.

## 3. Typography
- A neo-grotesk close to SF Pro Display, Regular to Medium weight.
- The text is **debossed:** a warm grey fill (~#9a948c) with a darker top-inner shadow and a light 1–2 px lower edge, so letters look stamped into the surface.
- Day initials (W/T/F) at ~70 px cap height and numerals at ~150 px are debossed the same way. The selected "6" is white with a soft drop shadow.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #f6f6f6 | canvas | 93–97% |
| #ffffff | card / pill surfaces | 83–85% (slides 2, 4) |
| #e7e8ea | tray chrome, bezel shading | 8% |
| #9a948c | debossed text (warm grey) | <2% |
| #5ac9fa → #cef0ff | send button radial fill (centre → rim) | 9% |
| #d90e10 | selected day, close | 3% |
| #ffc303 / #02c94a | minimise / zoom | 1.5% each |

WCAG:
- Debossed label #9a948c on #f4f2f0 is **2.69:1 (fails)**.
- White arrow on #5ac9fa is **1.88:1 (fails)**.
- White "6" on #d90e10 is 5.22:1 (passes).
- The close glyph #ae0002 on its red disc is 1.71:1. This is decorative, but it is the only cue other than colour.

## 5. Depth & material
- **Pill:** two concentric rims, a white outer bezel and an inner surface, with a 1–2 px grey hairline between them. A soft drop shadow (~80 px blur) falls downward.
- **Calendar icon:** a frosted, translucent body over a yellow→blue gradient header that shows through, with milky-white ring tabs.
- **Send button:** a radial gradient that is saturated at the centre and fades to near-white at the rim. It has a thin bright inner rim and a 2 px grey outer edge, like a glass lens.
- **Traffic lights:** flat-filled discs with a 6–8 px lighter rim. The glyphs are recessed in a darker shade of the same hue. Each disc casts a **tinted glow** (pink, yellow, green) onto the white card below.

## 6. Components & patterns
- **Add-to-calendar CTA:** icon plus two-line label in a pill.
- **Floating action button:** the send button in the card corner.
- **Segmented day picker:** the active item is scaled up about 1.2× with a red disc and a pointer above. Inactive items are ghosted.
- **Window controls tray:** the macOS traffic lights wrapped in a capsule.

## 7. Motion
None: four still images. The scaled selected day suggests a scale-and-fill transition of about 0.25 s, which is not shown.

## 8. Brand system
n/a — not a brand system. The consistent material language (warm-grey deboss, rim lights, tinted shadows) would carry across a set of icons or components.

## 9. UX
- **Positives:** The affordances are strong; everything looks pressable. Selection is triple-coded by size, colour and pointer.
- **Risks:**
  - The main label text and the white-on-cyan arrow both fail contrast.
  - The heavy bevels would get muddy at 1× (16–44 px), which is where these controls actually live.
  - The crops show no real context.

## 10. Craft signals
- Debossed letters have a darker top inner edge and a lighter bottom edge, consistent with top lighting.
- The pill bezel is a double rim: white band, grey hairline, inner surface.
- Shadows are tinted by their source colour under each traffic-light disc.
- Glyphs use a darker shade of the same hue (#ae0002 on red) instead of black.
- The selected day pill is about 1.2× its neighbours and keeps the same corner logic (full capsule).
- The send button gradient is radial and centre-weighted (#5ac9fa → #cef0ff), with a white inner rim.

## 11. Reproduction recipe
```css
:root{--canvas:#f6f6f6;--surface:#fff;--deboss:#9a948c;--cyan:#5ac9fa;--red:#d90e10;--yellow:#ffc303;--green:#02c94a}
.pill{border-radius:9999px;background:linear-gradient(#fbfbfa,#efedeb);
  box-shadow:0 0 0 14px #fff,0 0 0 15px #d4d4d4,0 30px 60px -20px rgba(0,0,0,.12)}
.deboss{color:var(--deboss);text-shadow:0 1px 0 rgba(255,255,255,.9),0 -1px 0 rgba(0,0,0,.18)}
.glass-btn{border-radius:50%;background:radial-gradient(circle,var(--cyan) 0,#a8e3fd 60%,#e6f7ff 100%);
  box-shadow:inset 0 0 0 4px rgba(255,255,255,.7),0 0 0 1px #9aa,0 10px 20px rgba(0,0,0,.12)}
.light{border-radius:50%;box-shadow:inset 0 0 0 3px rgb(255 255 255/.25),0 24px 40px -10px color-mix(in srgb,currentColor 25%,transparent)}
.light.close{background:var(--red);color:#ae0002}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Cohesive soft-white material set with a disciplined accent per slide. |
| Originality | 6 | A well-trodden "skeuo Liquid Glass" exercise and recognisable Apple parts. |
| Usability | 5 | Affordances are excellent, but text contrast fails and the bevels will not survive at real size. |
| Craft | 9 | The bevels, tinted shadows and debossing are precise and consistent with one light source. |

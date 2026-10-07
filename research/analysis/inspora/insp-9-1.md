---
id: insp-9-1
source: inspora
category: Branding
status: analyzed
title: "App icon"
creator: "@dmiiiitrii"
styles: [playful-rounded, glassmorphism, soft-3d]
patterns: [mascot-app-icon, sticker-outline-glyph, sky-photo-fill, device-corner-mockup, dimmed-neighbour-icons]
mode: mixed
palette: ["#ffffff", "#0a90fe", "#1dabfb", "#c3e9fe", "#dcf1fe", "#0e88de", "#000000"]
type_families: []
type_class: []
radius_px: [240, 9999]
motion: null
scores: {aesthetics: 8, originality: 6, usability: 7, craft: 8}
craft_signals: [double-outline-sticker-offset, rim-light-on-squircle-edge, vertical-gradient-inside-glyph, clouds-cropped-by-corners, tilted-eyes-and-smirk-asymmetry, neighbour-icons-dimmed-to-focus]
anti_patterns: [white-glyph-low-contrast-on-light-cloud-area]
---
# App icon — @dmiiiitrii

## 1. Snapshot
- **Subject:** Two slides of an app icon: a smiling ghost/cloud blob mascot with a sticker outline on a sky-blue squircle with photographic clouds. The first slide is the icon alone at 2406×2004; the second is in a tilted phone corner at 1650×1884.
- **Why it's remarkable:** It merges three icon trends (mascot, sticker outline, glassy sky fill) into one friendly glyph that still reads at home-screen size.

## 2. Composition & layout
- **Slide 1:**
  - The squircle is centred and about 1056 px wide (x≈672→1728 of 2406), about 44% of the width, with white space of about 470 px above and below.
  - The corner radius is about 240 px (about 23% of the side), close to the iOS continuous-corner proportion.
  - The ghost glyph is about 700 px wide (66% of the icon), set slightly right of centre and tilted about 10° clockwise, so the "head" leans in toward the top-right.
- **Clouds:** soft photo clouds cluster in the top-right and bottom-left corners. This creates a diagonal that echoes the glyph's tilt.
- **Slide 2:**
  - The phone is shot in a three-quarter view, cropped to its top-left corner on a #149afe→#3ac1fe gradient. The icon sits in the first home-screen slot at about 440 px on screen.
  - The neighbouring Messages and other icons are dimmed to about 10% luminance (#0f1a0e greens), so the hero icon is the only lit object.

## 3. Typography
None. The post is purely iconographic, with no wordmark or label.

## 4. Colour
| Hex | Role | Share (slide 1) |
|---|---|---|
| #ffffff | canvas; sticker outline | 79% |
| #0a90fe | top-left sky (deepest) | 3% |
| #1dabfb / #23a1ea | mid sky | 4% |
| #c3e9fe / #dcf1fe | glyph body gradient, clouds | 7% |
| #0e88de | glyph line art (eyes, smile, contour) | 1% |
| #000000 | phone screen (slide 2) | 44% (slide 2) |

WCAG and non-text checks:
- Line art #0e88de on glyph fill #dcf1fe is 3.23:1, which passes the 3:1 non-text threshold.
- The white sticker rim against mid sky #1dabfb is only 2.54:1. Its separation depends on the rim's width (about 35 px) rather than on contrast.
- The icon (#1dabfb) on the black home screen is 8.27:1, so it pops strongly in dark mode.

Strategy: a monochrome blue ramp with white as the only other value, so the icon stays on-brand for "cloud/sky".

## 5. Depth & material
- **Squircle:** has a 1–2 px lighter rim (#80d7fc) all round, like a glass edge. The fill grades from #0a90fe at the top-left to #23b5fb at the bottom-right.
- **Ghost:** carries a vertical gradient (white at the top → #c3e9fe at the bottom) to suggest volume. It has a soft drop shadow of about 20 px blur in deeper blue below, so it floats above the sky.
- **Sticker treatment:** a white outline of about 35 px, then a #0e88de contour line of about 22 px, then a lighter inner fill. This is the classic die-cut sticker read.
- **Mockup:** the phone renders a chrome stainless-steel band with a specular streak.

## 6. Components & patterns
- Mascot glyph with a minimal face: two slanted pill eyes and a hooked smirk. The smile starts with a short upward tick at the left, giving a wink-like personality.
- **Shape:** a three-lobed bottom edge (the ghost "skirt") doubles as a cloud bottom.
- The sky photo fill is cropped by the squircle mask, and the clouds bleed out at the corners.

## 7. Motion
Still images, so no motion was observed. The design invites a gentle bob (translateY of about 4 px, about 2 s ease-in-out) and cloud parallax inside the mask.

## 8. Brand system
n/a — not a full brand system. Identity cues:
- one-colour blue ramp;
- mascot with an asymmetric smirk (friendly, slightly mischievous);
- sticker outline that would carry over to emoji, stickers and empty states.

## 9. UX
- **Recognisability:** the silhouette (blob with a three-lobed base) is distinct at 60 px, and the face lines (about 22 px at 1056 px, roughly 1.3 px at 60 px) will thin out. The contour line may vanish at small sizes, while the white sticker rim survives.
- Slide 2 proves it on a dark wallpaper. A light-mode test against white is missing, and with a white rim the icon would partly merge with a white background.

## 10. Craft signals
- The double outline (white 35 px plus blue 22 px) follows the glyph's contour with a constant offset, including the inner notches of the skirt.
- The squircle has a lighter 1–2 px inner rim (#80d7fc), not a stroke.
- The eyes are parallel pills both tilted about 10°, matching the glyph's lean.
- The clouds are placed only on the diagonal, opposite corners, which keeps the face area clear.
- In the mockup, neighbouring icons are dimmed (not blurred), so the hero icon focuses attention without depth-of-field fakery.

## 11. Reproduction recipe
```css
:root{--sky-1:#0a90fe;--sky-2:#1dabfb;--sky-3:#23b5fb;--rim:#80d7fc;--glyph-top:#ffffff;--glyph-bot:#c3e9fe;--line:#0e88de;}
.app-icon{width:1024px;aspect-ratio:1;border-radius:23%;
  background:url(clouds.png) center/cover, linear-gradient(135deg,var(--sky-1),var(--sky-3));
  box-shadow:inset 0 0 0 2px var(--rim);display:grid;place-items:center}
.ghost{width:66%;rotate:10deg;filter:drop-shadow(0 18px 20px rgba(10,100,200,.35))}
.ghost path.body{fill:url(#g);stroke:var(--line);stroke-width:22;paint-order:stroke}
.ghost path.sticker{fill:none;stroke:#fff;stroke-width:70;stroke-linejoin:round}
/* <linearGradient id="g" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff"/><stop offset="1" stop-color="#c3e9fe"/></linearGradient> */
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Cohesive blue ramp, charming smirk and well-balanced cloud diagonal. |
| Originality | 6 | Mascot-in-squircle with a sticker outline is a well-trodden 2024–26 trend. |
| Usability | 7 | Strong silhouette and works on dark; the thin face lines and a white-on-white light mode are at risk. |
| Craft | 8 | Constant-offset outlines, a rim light and considered tilt alignment. |

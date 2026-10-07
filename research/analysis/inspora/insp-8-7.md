---
id: insp-8-7
source: inspora
category: Product
status: analyzed
title: "Apple's new macOS window controls"
creator: "@avstorm"
styles: [glassmorphism, hairline-ui, micro-interaction]
patterns: [traffic-light-controls, glass-capsule-toolbar-button, sidebar-toggle-with-chevron, light-dark-pair, oversized-window-radius]
mode: mixed
palette: ["#e2eaeb", "#d5dedf", "#32424f", "#424b54", "#5380a3", "#a1a5ae"]
type_families: []
type_class: []
radius_px: [40, 9999]
motion: null
scores: {aesthetics: 7, originality: 4, usability: 7, craft: 8}
craft_signals: [concentric-capsule-and-window-radius, hairline-toolbar-divider, glass-capsule-rim-light, traffic-light-inner-gradient, dark-mode-tinted-not-grey]
anti_patterns: [low-contrast-capsule-on-light-chrome, screenshot-crop-lacks-context]
---
# Apple's new macOS window controls — @avstorm

## 1. Snapshot
- **Subject:** Two tight crops (438×388 light, 464×360 dark) of a macOS window's top-left corner: traffic lights plus a glass capsule holding a sidebar toggle and a chevron, over a cloudy-sky wallpaper.
- **Why it's remarkable:** It documents a system-level shift: toolbar buttons become floating glass capsules whose radius nests inside a much rounder window corner.

## 2. Composition & layout
- Window corner enters at roughly x≈106, y≈134 (light crop). Its corner radius is about 40 px in the capture (≈20 pt at @2x), noticeably rounder than older macOS windows.
- Traffic lights: three discs of about 28 px at roughly 46 px centre-to-centre, sitting on the same baseline as the capsule's centre (y≈186).
- Capsule: about 128×72 px, starting ~48 px right of the green light. It holds a sidebar glyph (~38×30 px) and a 14 px chevron.
- A 1 px hairline divides the toolbar band (~105 px tall) from the content area.

## 3. Typography
No text is visible. The glyphs are SF Symbols (`sidebar.left`, `chevron.down`) at about 2 px stroke in the capture, i.e. a regular weight.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #e2eaeb | light window chrome | 47% (m0) |
| #d5dedf | light content area / hairline | 1% |
| #32424f | dark chrome (blue-tinted) | 36% (m1) |
| #424b54 | dark capsule fill | 5% |
| #5380a3 | wallpaper sky | 28% |
| #a1a5ae | cloud | 16% |

Traffic lights (red/amber/green) are standard system colours. They are not separate palette clusters because each covers <1% of pixels.

WCAG checks:
- Glyph #2b2b2b on light chrome #e2eaeb: 11.6:1.
- Light glyph #e8e8e8 on dark chrome #32424f: 8.45:1.

The capsule boundary itself (white glass on #e2eaeb) is under 1.2:1. It reads only through its rim highlight and soft shadow.

## 5. Depth & material
- The capsule is translucent glass: a slightly lighter fill, a 1 px inner highlight on the top edge and a very soft outer shadow. In dark mode it becomes a lighter tinted slab (#424b54-ish) with the same rim.
- The traffic lights have a subtle top-to-bottom gradient and darker rim, giving a faint domed look.
- The dark window picks up the blue of the wallpaper (#32424f rather than neutral grey), which suggests vibrancy/desktop tinting.

## 6. Components & patterns
- Window controls (close/minimise/zoom) unchanged in position but aligned to a taller toolbar.
- Grouped toolbar control: a capsule containing a primary toggle and a menu chevron (split-button idiom).
- Light/dark pairs shown side by side as a spec.

## 7. Motion
Stills only; no motion observed.

## 8. Brand system
n/a — not a brand system. Identity cues: Apple's glass-material language, SF Symbols, concentric radii.

## 9. UX
- Larger hit targets: the capsule is ~64×36 pt versus older ~28 pt icon buttons.
- Grouping toggle and menu signals the chevron opens related options.
- **Risk:** on light chrome the capsule barely separates from the toolbar, so the affordance depends on the glyphs alone.

## 10. Craft signals
- The capsule's full-pill radius sits concentrically inside the ~40 px window corner: inner radius = outer radius − inset.
- The traffic-light centres and capsule centre share one horizontal axis (y≈186 in m0).
- The 1 px divider stops at the window edge with no visible overshoot at the curved corner.
- Dark mode is tinted by the wallpaper (blue-grey #32424f), not a flat #2a2a2a.

## 11. Reproduction recipe
```css
:root{--chrome:#e2eaeb;--glass:rgba(255,255,255,.55);--rim:rgba(255,255,255,.9);--r-window:20px}
@media (prefers-color-scheme:dark){:root{--chrome:#32424f;--glass:rgba(255,255,255,.08);--rim:rgba(255,255,255,.18)}}
.window{border-radius:var(--r-window);background:var(--chrome);overflow:hidden}
.toolbar{height:52px;display:flex;align-items:center;gap:24px;padding:0 20px;border-bottom:1px solid rgba(0,0,0,.08)}
.lights{display:flex;gap:9px}.lights i{width:14px;height:14px;border-radius:50%;
  background:linear-gradient(#ff6159,#e0443e);box-shadow:inset 0 0 0 .5px rgba(0,0,0,.2)}
.capsule{height:36px;padding:0 14px;border-radius:9999px;display:flex;gap:14px;align-items:center;
  background:var(--glass);backdrop-filter:blur(20px) saturate(1.6);
  box-shadow:inset 0 1px 0 var(--rim),0 1px 6px rgba(0,0,0,.08)}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 7 | Calm, precise material, but the crop shows very little. |
| Originality | 4 | A screenshot of an OS vendor's design, not new work. |
| Usability | 7 | Larger, grouped targets; weak capsule edge on light chrome. |
| Craft | 8 | Concentric radii, axis alignment and tinted dark mode are exact. |

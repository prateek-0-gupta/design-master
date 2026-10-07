---
id: insp-1-52
source: inspora
category: Illustration
status: analyzed
title: "curved browser tabs"
creator: "@Ryan__Stephen"
styles: [glassmorphism, spatial-ui, micro-interaction, gradient-mesh]
patterns: [corner-wrapping-tab-strip, text-on-path-label, vertical-tab-overflow, translucent-pill-tabs, hover-reveal-close, tab-tinted-by-wallpaper]
mode: light
palette: ["#fefefe", "#8b87ee", "#9696fa", "#7374e2", "#c285bc", "#3b7042", "#989f8d", "#222222"]
type_families: ["SF Pro Text (likely)"]
type_class: [neo-grotesk]
radius_px: [9999, 40]
motion: {durations_s: [0.1, 0.1, 0.13], easing: [ease-in], loop: false}
scores: {aesthetics: 8, originality: 9, usability: 6, craft: 7}
craft_signals: [label-follows-tab-curvature, tab-corner-concentric-with-window, close-x-stays-upright, inactive-tabs-desaturated, wallpaper-shows-through-tabs, truncation-ellipsis-on-curve]
anti_patterns: [inactive-tab-text-near-invisible, rotated-text-hard-to-scan, instant-content-swap]
---
# curved browser tabs — @Ryan__Stephen

## 1. Snapshot
- **Subject:** A 7.38 s, 1080×1080 prototype of a browser whose tab strip runs along the top edge and then bends around the window's top-right corner into a vertical column. A tab can sit on the bend, with its title set on the curve.
- **Why it's remarkable:** It merges horizontal and vertical tabs into one continuous track, so overflow tabs flow down the side instead of shrinking. The corner tab's text literally follows the path.

## 2. Composition & layout
- The window is cropped top-right. Its content area starts at y≈225 and ends at x≈862, with a ~40 px corner radius.
- **Horizontal tabs:** ~95 px tall pills with a ~20 px gap, sitting ~30 px above the content in the wallpaper margin.
- **Vertical tabs:** in a ~95 px gutter to the right (x≈888–983).
- **Corner tab:** "Hawaiian Airlines – Flights to Hawaii, Plane Ti…" starts horizontal at x≈552, bends through a ~110 px outer radius concentric with the window corner, and continues vertically to y≈510. Its close × sits at the vertical end.
- Below it are "The New York Times…" (vertical, active) and "Spotify" (faded, cropped).
- The page content is real sites (NYT, Google Maps, Hawaiian Airlines, Airbnb) swapped in as tabs are clicked.

## 3. Typography
- SF Pro Text-style neo-grotesk, Regular, at ~26 px in the tabs.
- Vertical tab labels are rotated 90° clockwise and read top-to-bottom.
- The corner label is set on a path, with each glyph rotated along the arc ("Flights to" visibly fans out). Letter spacing stays even through the curve.
- Truncation uses an ellipsis at the end of the path.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #fefefe / #eeeeee | page content | 31% / 5% |
| #8b87ee / #7374e2 / #9696fa | violet wallpaper and tab tint | ~25% |
| #c285bc | pink wallpaper band | 3.5% |
| #3b7042 / #989f8d | green wallpaper / tab over green | ~10% |
| #222222 | active tab text | — |

WCAG:
- Active text #222 on a violet-tinted tab (#9696fa) is 6.09:1.
- Active text on a green-tinted tab (#989f8d) is 5.82:1.
- Inactive labels (≈#8a7fc0 on #b67bcb) are **1.14:1** and are effectively invisible ("Airbnb | Vacation rentals" and "Spotify" read as ghost text).

The tabs have no colour of their own. Each is a translucent white layer that takes the wallpaper hue behind it, so the same component reads violet at the top and green at the bottom.

## 5. Depth & material
- **Tabs:** frosted glass. Inactive tabs are at about 20% white overlay. Active and hovered tabs are at about 45%, with a 1 px lighter rim and no drop shadow.
- **Window:** pure white with a faint shadow onto the wallpaper.
- **Wallpaper:** a macOS Sonoma-style curved colour field (pink/violet/blue above, green hills below). It provides all the chroma and makes the translucency legible.

## 6. Components & patterns
- **Unified tab track:** horizontal, then a corner bend, then vertical.
- **Active vs inactive:** the active tab is opaque-ish with dark text, while inactive tabs fade to about 40% text opacity.
- **Close ×:** appears on the active or hovered tab at the trailing end. It stays upright and is not rotated with the text.
- **Hover on a horizontal tab:** the × fades in ("Airbnb | Vacation rent… ×", t≈6.15 s).
- **Selection:** clicking a tab swaps the page content.

## 7. Motion
Measured: 60 fps, duration 7.38 s, motion_fraction 0.05, not a seamless loop (first/last diff 42.8). The three detected segments are short:
- 0.27–0.37 s (0.10 s, ease-in, peak 0.83);
- 5.97–6.07 s (0.10 s, ease-in);
- 6.40–6.53 s (0.13 s, ease-in, peak 0.88).

These are near-instant content swaps on click, not animated transitions. From frames (estimate), tab highlight changes between t≈3.69 s and 4.51 s with a soft fade, and the cursor dwell is about 0.8 s per tab. The tabs themselves do not slide or reflow in this clip.

## 8. Brand system
n/a — not a brand system. It reads as an Arc- or Safari-adjacent concept and relies on the macOS wallpaper for identity.

## 9. UX
- **Strengths:** It solves tab overflow without shrinking titles. The corner shows more of a title than a fixed-width tab would.
- **Risks:**
  - Curved and rotated text is slow to scan.
  - Inactive tabs at about 1.1:1 contrast are unreadable.
  - Reorder and drag along a bend is undefined.
  - Hit-testing a curved pill is harder.
  - The instant content swap (0.1 s) gives no spatial link between tab and page.

## 10. Craft signals
- The corner tab's outer radius (~110 px) is concentric with the window's ~40 px corner plus the ~30 px gutter.
- Glyphs on the bend are individually rotated to the path normal, with even tracking.
- The close × stays upright on both horizontal and vertical tabs.
- Vertical labels truncate with an ellipsis before the ×.
- The tab tint is not a fixed colour: the same translucent fill reads violet or green by position.
- The tab gutter equals the tab height (~95 px), so the horizontal and vertical tracks share one thickness.

## 11. Reproduction recipe
```html
<svg class="corner-tab" viewBox="0 0 440 420">
  <path id="tabPath" d="M20 48 H300 A110 110 0 0 1 410 158 V400" fill="none"/>
  <path d="M20 48 H300 A110 110 0 0 1 410 158 V400" stroke="rgba(255,255,255,.45)" stroke-width="95" stroke-linecap="round" fill="none"/>
  <text font-family="SF Pro Text, Inter, system-ui" font-size="26" fill="#222">
    <textPath href="#tabPath" startOffset="10" dominant-baseline="middle">Hawaiian Airlines – Flights to Hawaii, Plane Ti…</textPath>
  </text>
</svg>
```
```css
.tab{height:95px;border-radius:9999px;background:rgb(255 255 255/.2);backdrop-filter:blur(20px) saturate(1.4);
  box-shadow:inset 0 0 0 1px rgb(255 255 255/.25);color:rgb(34 34 34/.4);font:400 26px/1 "SF Pro Text",system-ui;transition:background .2s ease-out,color .2s}
.tab[aria-selected=true],.tab:hover{background:rgb(255 255 255/.45);color:#222}
.tab.vertical{writing-mode:vertical-rl}
.tab .close{opacity:0;transition:opacity .15s}.tab:hover .close,.tab[aria-selected=true] .close{opacity:1}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Elegant continuous track, with the glass taking on the wallpaper colour. |
| Originality | 9 | Bending one tab strip around the window corner, with text on the path, is new. |
| Usability | 6 | Solves overflow, but rotated and curved text and invisible inactive tabs hurt scanning. |
| Craft | 7 | The concentric geometry and on-path typesetting are careful. Content swaps are abrupt. |

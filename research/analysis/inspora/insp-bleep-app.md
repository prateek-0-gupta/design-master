---
id: insp-bleep-app
source: inspora
category: Motion
status: analyzed
title: "Bleep App"
creator: "@rnmp"
styles: [glassmorphism, photo-led, spatial-ui, playful-rounded]
patterns: [translucent-window-over-photo, sidebar-rooms-with-emoji-icons, masonry-card-grid, zoom-into-card-to-document, breadcrumb-chips, macos-traffic-lights, camera-zoom-transition]
mode: light
palette: ["#fcf7f3", "#f2e8e1", "#dde6f5", "#5f7498", "#314161", "#6e4e48", "#1a1a1a", "#ff5f57"]
type_families: ["SF Pro Text / Display (likely)"]
type_class: [neo-grotesk]
radius_px: [24, 16, 12, 9999]
motion: {durations_s: [0.53, 0.53, 1.3, 1.8, 0.73, 0.47, 0.7, 0.5], easing: [ease-out, ease-in, ease-in-out], loop: false}
scores: {aesthetics: 8, originality: 7, usability: 6, craft: 7}
craft_signals: [window-tint-follows-backdrop, emoji-tile-icons-in-sidebar, motion-blur-on-zoom, card-to-page-continuity, breadcrumb-on-every-card, generous-24px-window-radius]
anti_patterns: [faint-section-headers, busy-photo-behind-translucent-ui, low-res-capture]
---
# Bleep App — @rnmp

## 1. Snapshot
- **Subject:** A 17.1 s, 960×720 screen capture of "Bleep", a macOS notes/bookmarks app. A translucent window floats over full-bleed photographs (a cloudy sky, then a graffiti-covered building). The camera zooms between sidebar, card grid and an open document.
- **Why it's remarkable:** Very aggressive translucency. The window is a frosted pane that takes on the hue of whatever photo is behind it: blue-tinted over the sky, warm peach over the brick. The camera choreography (zoom into a card, it becomes the page) makes navigation feel spatial.

## 2. Composition & layout
- **Window (key frame):** about 855×580 px of the 960×720 frame, inset about 52 px left, 72 px top, with a radius of about 16 px at this scale (about 24 px at native).
- **Sidebar:** about 200 px wide.
  - Library items: Everything, Notes, Bookmarks, Images.
  - A "Rooms" section with + add: Focus, Backpacking, Code, Demos, Design, DIY, Explore, Games, Home, Interior, Life. Each has an emoji-style 20 px tile icon and a disclosure chevron.
  - Archive and Settings are pinned at the bottom.
- **Content:** a document column starting at x≈317, with a measure of about 500 px (about 75 characters).
- **Grid view (f7):** a masonry of 4 columns, each card about 120 px at this scale, with a 12 px gap. Cards hold link previews, notes and images, each with a "(a) Focus › (b) Bleep › Product" breadcrumb.
- **Toolbar:** traffic lights, a sidebar toggle, back/forward in a pill, a "…" menu, and in grid view a title "Design" plus filter chips (Charts, Typography, Websites).

## 3. Typography
- SF Pro throughout.
- **Document:** H1 "Organization tools" at about 18 px Semibold (at 960 px capture; about 26 px native), H2 about 14 px Bold, body about 12.5 px Regular, leading about 1.6.
- Bullets use native disc and circle nesting.
- **Sidebar:** items are about 11 px Regular in dark grey, and "Rooms" is about 10 px in a much lighter grey.
- **Card titles:** about 13 px Semibold, with an 11 px grey snippet.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #fcf7f3 | document pane (warm white) | 45% |
| #f2e8e1 | frosted sidebar over brick | 14% |
| #dde6f5 | frosted sidebar over sky | — |
| #5f7498 / #314161 | sky photo | 14% |
| #6e4e48 / #908074 | brick, graffiti photo | 10% |
| #1a1a1a | body text | ~2% |
| #ff5f57 / #febc2e / #28c840 | traffic lights | <1% |

WCAG:
- Body #1a1a1a on #fcf7f3 is 16.36:1.
- Sidebar items #4a4f57 on #dde6f5 are 6.56:1.
- The "Rooms" header #9aa3ad on #dce6f2 is **2.03:1 (fails)**.
- Over the brick the sidebar labels (#6b6560 on #f2e8e1) are 4.76:1. Contrast varies with the wallpaper, which is the core risk of this material.

## 5. Depth & material
- **Window:** heavy backdrop blur (about 40 px or more) with about 80% white overlay. Edges have a 1 px white highlight and a large soft shadow.
- **Sidebar:** about 10% more transparent than the content pane, so the photo shows through more in the sidebar.
- **Cards:** in the grid view they are another frosted layer (white about 70%) with a 16 px radius.
- **During camera moves (f2, f8):** strong motion blur, rendered as a directional smear, which sells the speed.

## 6. Components & patterns
- **Sidebar list:** the selected or hovered item sits in a white 12 px-radius pill with a soft shadow ("Bookmarks", "Design").
- **Back/forward:** a joined pill segmented control. The sidebar toggle is a separate circular button.
- **Filter chips:** small rounded chips with a ring icon.
- **Cards:** link previews (favicon, title, domain), note excerpts and image thumbnails, each with a breadcrumb trail.
- **Document:** plain structured notes; a technical spec about "BlockRelation".

## 7. Motion
The motion is measured: 17.08 s, 60 fps, motion_fraction 0.42, not a loop. There are 10 segments with a median of 0.53 s.
- **1.40 s and 3.33 s:** 0.53 s ease-out (peak 0.22). These are sidebar hover zooms.
- **4.40–5.70 s:** 1.3 s ease-in (peak 0.83), the accelerating zoom into a card (f2 blur).
- **6.00–7.80 s:** 1.8 s ease-out (peak 0.05), the card expanding into the full document and decelerating into place (f4).
- **8.80–9.90 s:** about 1.0 s, a scroll through the doc.
- **11.83 s:** 0.47 s ease-out, the zoom back to the toolbar.
- **13.77–15.30 s:** symmetric 0.5–0.7 s segments, the grid reveal.
- **16.03 s:** 0.43 s ease-out, the exit with blur.

The ease-in-then-ease-out pairing (1.3 s then 1.8 s) forms one continuous "dive" transition.

## 8. Brand system
n/a — not a brand system. Cues: the name "Bleep", the tagline "thinking was never this fun", and the emoji-tile room icons give a playful personal-knowledge tone.

## 9. UX
- **Pros:** a familiar macOS structure, clear spatial navigation (grid → card → doc), and breadcrumbs on cards.
- **Cons:**
  - Translucency over busy photos makes chrome contrast unpredictable.
  - Section headers are too faint.
  - Long zoom transitions (1.3–1.8 s) would feel slow on repeated use.

## 10. Craft signals
- The sidebar tint changes with the backdrop (blue-grey #dde6f5 over sky, peach #f2e8e1 over brick).
- Room icons are consistent 20 px rounded tiles with emoji-like glyphs.
- The selected sidebar row is a white pill with a shadow rather than a coloured fill.
- The card in the grid and the opened document share the title and bullets, so continuity holds through the zoom.
- Motion blur is applied during camera moves (f2, f8), not a plain cross-fade.
- The document caret is a pink 1 px insertion bar (key frame, x≈317).

## 11. Reproduction recipe
```css
:root{--pane:rgba(252,247,243,.86);--side:rgba(255,255,255,.55);--text:#1a1a1a;--text-2:#55514d;--r-win:24px;--r-item:12px}
.window{border-radius:var(--r-win);background:var(--pane);backdrop-filter:blur(40px) saturate(1.4);
  box-shadow:inset 0 0 0 1px rgba(255,255,255,.6),0 30px 80px rgba(0,0,0,.25)}
.sidebar{background:var(--side);backdrop-filter:blur(30px)}
.sidebar .item{display:flex;gap:10px;padding:8px 10px;border-radius:var(--r-item);font:400 15px -apple-system;color:var(--text-2)}
.sidebar .item[aria-current]{background:#fff;box-shadow:0 2px 8px rgba(0,0,0,.08);color:var(--text)}
.sidebar h6{font:600 12px -apple-system;color:#6d737b} /* fix 2.0:1 header */
.icon-tile{width:22px;height:22px;border-radius:6px;display:grid;place-items:center}
.dive-in{transition:transform 1.3s cubic-bezier(.6,0,.9,.4),filter 1.3s}.dive-out{transition:transform 1.8s cubic-bezier(.1,.8,.2,1)}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Photographic backdrops plus frosted panes are beautiful and warm. |
| Originality | 7 | Spatial zoom navigation in a notes app is a fresh take on Finder-like UI. |
| Usability | 6 | A familiar structure, but contrast depends on wallpaper and the transitions are long. |
| Craft | 7 | Good continuity and icon consistency. The capture is low-res (960×720), which hides finer detail. |

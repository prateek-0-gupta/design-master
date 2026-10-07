---
id: insp-gpt-6-astra
source: inspora
category: Motion
status: analyzed
title: "generating UI using GPT-6 Astra"
creator: "@MSchwaibold"
styles: [corporate-clean, bento-grid, minimal-swiss, technical-wireframe]
patterns: [widget-gallery, widget-focus-zoom, spec-overlay-grid, height-radius-annotation, timer-dial-widget, weather-widget, news-list-widget, mood-board-tile]
mode: light
palette: ["#ffffff", "#f2f2f0", "#161821", "#9bd5e8", "#8cbeda", "#85a2b7", "#e5efe0", "#fdf3b0"]
type_families: ["Inter (likely)", "Instrument Serif / Times-style display serif (note)", "monospace for spec labels"]
type_class: [neo-grotesk, editorial-serif, mono]
radius_px: [24, 9999, 8]
motion: {durations_s: [0.63, 0.8, 0.77, 0.13], easing: [ease-out, ease-in-out], loop: false}
scores: {aesthetics: 8, originality: 6, usability: 7, craft: 8}
craft_signals: [uniform-24px-radius-across-widgets, spec-grid-matches-widget-bounds, mono-uppercase-spec-labels, map-fades-into-white-caption, serif-reserved-for-note-content, section-labels-above-cards]
anti_patterns: [white-on-light-blue-weather-fails, ai-generated-claim-unverifiable]
---
# generating UI using GPT-6 Astra — @MSchwaibold

## 1. Snapshot
- **Subject:** A 27.6 s, 60 fps, 3248×2160 screen recording of a generated widget gallery: music player, focus timer, flight tracker, map, weather, news, inbox, quick note and mood board.
- The camera zooms into individual widgets (Activity, Location, Quick note, Focus, Mood board, Shader Experiments). Several appear beside a pink and lilac blueprint grid with mono spec labels ("HEIGHT 240 PX / RADIUS 24 PX").
- **Why it's remarkable:** It shows a coherent widget system with tokenised geometry: every card shares a 24 px radius and the spec overlay exposes heights (240/304/350/352 px). Generated or not, it is a clean reference for an iOS-style widget kit.

## 2. Composition & layout
- **Gallery:** a 3-column grid of cards about 420×(220–470) px in the 2000-px display (about 680 px real at 3248), with roughly 60 px gutters and a small grey section label above each ("Location", "Weather", "News", "Inbox", "Quick note", "Mood board"). Card heights vary by content, giving a masonry-like bento.
- **Focus views:** one widget sits left of centre and a ghost grid of identical size sits to its right with spec text further right. Annotated sizes:
  - Quick note: 240 px tall, 24 px radius;
  - Focus timer: 304 px tall;
  - Mood board: 350 px tall;
  - Shader Experiments: 352 px tall.
- A soft circular cursor (about 50 px) indicates hover and click.

## 3. Typography
- **UI:** Inter-like neo-grotesk. Card titles about 15 px Medium ("New stories", "Inbox"), body about 13 px Regular grey with leading of about 1.55, and meta about 12 px grey.
- **Big numerals:** "58°" about 40 px Light, "13:28" about 40 px Regular, "3.1 km" about 28 px.
- **Quick note body:** a high-contrast display serif ("Leave a little room for the unexpected.") about 22 px, close to Instrument Serif or Times Ten. Serif signals user-authored content.
- **Spec labels:** monospace uppercase, about 9 px, letter-spaced ("HEIGHT", "RADIUS").

## 4. Colour
| Hex | Role | Approx share |
|---|---|---|
| #ffffff | canvas, card surfaces | 78% |
| #f2f2f0 / #d9dddc | card borders, dividers, inbox search field | 4% |
| #161821 | focus timer card (dark navy-black) | 2.4% |
| #9bd5e8 / #8cbeda | map water, weather gradient top | 4.4% |
| #85a2b7 | weather gradient bottom | 2% |
| #e5efe0 | map land | 1.9% |
| #fdf3b0 | "Draft · This session" highlight chip | <0.5% |

The spec grid uses pink lines (about #e9b9e6) and pale lilac lines.

WCAG checks:
- White on the weather gradient (#8cbeda) is **2.0:1**, and 2.68:1 on #85a2b7 (fails).
- White on the focus card #161821 is 17.7:1.
- Body grey #6b6b6b on white is 5.33:1. Meta grey #8a8a8a is 3.45:1 (fail).
- The draft chip (#8a6d00 on #fdf3b0) is 4.36:1.

## 5. Depth & material
- Cards: white, 1 px #ececec border, very soft shadow (about 0 8px 24px rgba(0,0,0,.04)), radius 24 px.
- The map card fades its bottom 30% to white behind the caption: a gradient scrim instead of a dark overlay.
- The focus timer is a dark slate card with a subtle vertical gradient and a ring of 60 tick marks forming a dial.
- The weather card is a sky-blue vertical gradient. The mood board holds a 2×2 grid of photos with 8 px radius.

## 6. Components & patterns
Widget catalogue:
- media scrubber (2:25 / −1:45);
- focus timer (dial, reset and Pause pills);
- flight progress (SFO→JFK with a plane glyph on a progress line);
- map;
- weather (current and a five-day row);
- news list (48 px thumbnail, title, source);
- inbox (unread dots, agent names, timestamps, attachment thumbnails);
- quick note (serif content and a draft chip);
- mood board;
- activity bar chart (a weekday bar series with today in saturated blue).

There is also a spec overlay: a ghost grid with a 16 px cell, the same size as the widget, plus annotation labels.

## 7. Motion
- **Measured:** 27.55 s with motion fraction 0.22 and 26 segments (median **0.13 s**), mostly short ease-out spikes (cursor clicks and content swaps). The larger ones:
  - 1.17–1.80 s (0.63 s, symmetric) and 1.97–2.77 s (**0.8 s**, ease-out, peak 0.23): gallery scroll and zoom into Activity.
  - 13.27–14.03 s (0.77 s, symmetric): zoom back out to the gallery.
  - 14.83–20.3 s: a cluster of 0.17–0.27 s ease-out events, the focus timer counting down and the spec grid appearing.
- **From frames (estimate):** focus transitions cross-fade the gallery to white while the target widget scales up about 2× around its own centre over about 0.6–0.8 s. The timer digits tick each second (13:25 → 13:22 across 3.06 s).

## 8. Brand system
n/a — not a brand system. A demo of AI-generated UI. Identity cues:
- a neutral Apple-widget aesthetic;
- 24 px radius as the governing token;
- serif for human notes and mono for specs.

## 9. UX
- Widgets are well-scoped, glanceable and consistent. Section labels above cards aid scanning.
- Failures: white text on the light-blue weather card and light meta grey.
- The spec overlay is a nice handoff affordance, showing dimensions with no need to inspect.
- The "generated by GPT-6 Astra" claim cannot be verified from the pixels. Judge it only as a UI kit.

## 10. Craft signals
- Every widget, light or dark, uses one 24 px radius, confirmed by the on-screen "RADIUS 24 PX" annotation.
- The spec grid exactly matches the focused widget's bounding box and height.
- Spec labels are mono uppercase with wide tracking, visually separated from the product type.
- Serif type appears only in user content (quick note), never in chrome.
- The map uses a white gradient scrim for the caption instead of a dark overlay.
- The activity chart highlights today in a saturated blue while the other days are pale tints.
- Inbox unread dots are about 6 px #3b9ed8 circles aligned to the first line's x-height.

## 11. Reproduction recipe
```css
:root{--bg:#fff;--card:#fff;--line:#ececec;--ink:#111;--muted:#6b6b6b;--meta:#737373;--r:24px;
  --sky-1:#9bd5e8;--sky-2:#5f87a6;--slate:#161821;--draft:#fdf3b0;
  --sans:"Inter",system-ui,sans-serif;--serif:"Instrument Serif","Times New Roman",serif;--mono:ui-monospace,"JetBrains Mono",monospace}
.grid{display:grid;grid-template-columns:repeat(3,300px);gap:28px 36px;align-items:start}
.label{font:400 11px var(--sans);color:var(--meta);margin-bottom:8px}
.widget{background:var(--card);border:1px solid var(--line);border-radius:var(--r);padding:16px;box-shadow:0 8px 24px rgba(0,0,0,.04)}
.widget.weather{background:linear-gradient(180deg,var(--sky-1),var(--sky-2));color:#fff} /* darker end fixes 2:1 */
.widget.focus{background:linear-gradient(180deg,#232838,var(--slate));color:#fff}
.note-body{font:400 22px/1.2 var(--serif)}
.draft{background:var(--draft);color:#6b5400;border-radius:6px;padding:2px 6px;font:500 11px var(--sans)}
.spec{background:
  linear-gradient(#e9b9e6 1px,transparent 1px) 0 0/16px 16px,
  linear-gradient(90deg,#e9b9e6 1px,transparent 1px) 0 0/16px 16px;border-radius:var(--r);opacity:.6}
.spec-label{font:500 9px/1.4 var(--mono);letter-spacing:.12em;text-transform:uppercase;color:#777}
.focus-in{animation:focus .7s cubic-bezier(.2,.8,.2,1)}
@keyframes focus{from{transform:scale(.5);opacity:0}}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Calm, cohesive widget kit with tasteful serif accents and a nice spec overlay. |
| Originality | 6 | Apple-widget idiom. The spec-grid presentation is the fresher idea. |
| Usability | 7 | Glanceable and consistent. The weather card and meta greys fail contrast. |
| Craft | 8 | Strict radius token and exact spec overlays, though one card scale family varies (240–352 px heights). |

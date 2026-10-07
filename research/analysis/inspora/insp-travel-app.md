---
id: insp-travel-app
source: inspora
category: Product
status: analyzed
title: "travel app"
creator: "@FarzadGodarz"
styles: [aurora-glow, playful-rounded, photo-led, micro-interaction]
patterns: [glowing-route-map, map-pin-callout, title-carousel-with-ghost-neighbours, postage-stamp-photo-card, stamp-flip-to-detail, mood-chip, zoom-pill-pair]
mode: light
palette: ["#ffffff", "#64d1e9", "#9ce1f0", "#d2eef5", "#2e4a52", "#bb8c6f", "#a5bbd6", "#eff2f3"]
type_families: ["SF Pro Display / Rounded (likely)"]
type_class: [neo-grotesk]
radius_px: [44, 9999, 28]
motion: {durations_s: [0.8, 1.07, 0.7], easing: [ease-in-out], loop: false}
scores: {aesthetics: 8, originality: 8, usability: 6, craft: 7}
craft_signals: [glow-stroke-route-on-sky-gradient, perforated-stamp-edge-mask, ghosted-adjacent-titles, stamp-tilt-variation, dark-teal-ink-instead-of-black, route-draws-on-entry]
anti_patterns: [white-subtitle-on-cyan-invisible, grey-meta-low-contrast]
---
# travel app — @FarzadGodarz

## 1. Snapshot
- **Subject:** An 8.85 s, 1080×1350 recording of an Italy itinerary screen. A cyan "sky" map card with a glowing white route sits above a carousel of destinations shown as tilted postage-stamp photos. A tap flips or enlarges a stamp into a detail card.
- **Why it's remarkable:** The postage stamp is a literal, tactile travel metaphor. Each destination photo is masked with a perforated edge and rotated a few degrees. The map is an abstract luminous line on a blurred aurora rather than real cartography.

## 2. Composition & layout
- **Phone and map card:** The phone spans x≈188→892 (≈704 px) with a #f5f5f5 bezel area. The map card covers y≈170→695 (≈525 px, ~40% of the screen) with a radius of about 44 px.
- **Inside the map card:**
  - circular glass buttons top-left (history) and top-right (edit), each about 68 px;
  - a centred "Italy" title (about 64 px bold white) with a subtitle;
  - the route spline with 4 nodes;
  - a mood chip ("Happy!" with a memoji) bottom-left and a zoom −/+ pill bottom-right.
- **Lower card:** white with a ~44 px radius. It has an eyebrow ("4 Place Planned for you", grey), a centred destination title (about 40 px bold, dark teal), and meta ("28min · Open") with line icons.
- **Carousel:** neighbouring titles ("Duomo", "Tower") are ghosted at about 10% opacity and cropped at the edges, which signals horizontal paging.
- **Stamp:** about 500×300 px, rotated −4°, bleeding off the bottom edge.

## 3. Typography
- One family throughout: SF Pro Display Bold for the titles ("Italy", "Colosseum Rome") with tight −0.02 em tracking, and Regular for meta. Callouts ("Colosseum Rome" on the map) are about 20 px regular on frosted pills.
- **Stamp caption:** about 26 px medium title plus an about 18 px "let's be brave" tagline, rotated with the stamp. The type is treated as printed on the object.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #ffffff | page, lower card, route stroke | 65% |
| #64d1e9 / #7ed9ec | saturated sky core | 7% |
| #9ce1f0 / #b3e9f5 / #d2eef5 | sky haze, stamp border, buttons | 18% |
| #2e4a52 | ink: titles, pin ring, icons | small |
| #bb8c6f / #6e4834 | photo warmth (Colosseum) | 5% |
| #a5bbd6 | photo sky | 4% |

WCAG checks:
- Dark-teal title #2e4a52 on #fff is 9.47:1, and 7.8:1 on the pale stamp #d2eef5.
- White "Italy" on #64d1e9 is **1.77:1**, and the white subtitle on #9ce1f0 is **1.45:1**. It is effectively invisible, as the key frame shows.
- Grey eyebrow #9aa4a8 on #fff is 2.55:1 (fail).
- Ghost neighbour titles are about 1.19:1, which is intended as a hint.

## 5. Depth & material
- **Map card:** a layered cyan gradient with diagonal white light streaks (like sun through water or aurora) and a soft white vignette fading at the bottom.
- **Route:** a 10 px white stroke with an outer glow (about 12 px blur) and frosted node dots of about 30 px.
- **Glass buttons and chips:** semi-opaque white (about 50%) with a soft backdrop blur.
- **Stamp:** sits on the white card with a subtle shadow under the tilted edge and a pale-blue (#d2eef5) perforated border of about 30 px, scalloped with semicircles of about 24 px.

## 6. Components & patterns
- Abstract route map with a current-location ring pin (dark teal, about 40 px, 4 px stroke) and a callout pill.
- A destination carousel synchronised with the map: changing the destination moves the pin and callout (Milan Duomo → Colosseum Rome).
- **Stamp card:**
  - rest state: a photo bleeding off the card;
  - tapped state: a tilted stamp with caption, tagline and an "Open" status pill with a clock icon.
- A mood chip with avatar, a zoom segmented pill, and circular icon buttons.

## 7. Motion
Measured: 8.85 s at 30 fps, motion fraction 0.29, not a seamless loop.

| Segment | Start–end | Duration | Shape (peak_at) | What happens |
|---|---|---|---|---|
| 1 | 0.17–0.97 s | 0.8 s | symmetric (0.48) | the route draws on (stroke-dashoffset feel) from the top node, the subtitle fades in and the stamp rises (frames 0.49 → 1.48 s) |
| 2 | 3.63–4.70 s | 1.07 s | symmetric (0.64, slightly ease-in weighted) | carousel swap from Duomo to Colosseum; the pin and callout travel along the route while titles slide horizontally |
| 3 | 6.73–7.43 s | 0.7 s | symmetric (0.36) | tap on the stamp; it lifts, rotates from about −4° to −10° and reveals the caption and "Open" pill |

These are long, gentle durations (0.7–1.07 s) that fit a leisure/travel mood.

## 8. Brand system
n/a — not a brand system. Identity cues: a sky-cyan aurora, postage stamps as the souvenir motif, dark teal instead of black for ink, and playful copy ("Happy!", "let's be brave").

## 9. UX
- **Strengths:** The map and list are linked (one selected destination drives both). Ghosted neighbours teach swiping. Travel time and open status are shown up front.
- **Risks:**
  - The white subtitle on cyan is unreadable.
  - The map has no geography, so it is decorative rather than navigational.
  - The stamp crops the photo at the bottom in the rest state.
  - The zoom controls on an abstract map are questionable.

## 10. Craft signals
- The perforated stamp edge is a true scalloped mask with even semicircles, not a dashed border.
- The stamp tilt changes between rest (−4°) and active (about −10°) states.
- Adjacent carousel titles render at about 10% opacity and are clipped by the card edge.
- Ink colour is #2e4a52 teal everywhere (title, pin ring, icons), harmonising with the cyan.
- The route nodes glow with the same white as the stroke; the active node is the only dark element on the map.
- The map's bottom edge fades to white before the card radius, which softens the panel join.

## 11. Reproduction recipe
```css
:root{--sky:#64d1e9;--haze:#b3e9f5;--pale:#d2eef5;--ink:#2e4a52;--mute:#9aa4a8;--r:44px}
.map{border-radius:var(--r);position:relative;overflow:hidden;
  background:linear-gradient(115deg,transparent 30%,rgba(255,255,255,.55) 38%,transparent 46%),
             radial-gradient(80% 60% at 50% 40%,var(--sky),var(--haze) 70%,#e9f8fb 100%)}
.route{fill:none;stroke:#fff;stroke-width:10;stroke-linecap:round;filter:drop-shadow(0 0 8px #fff);
  stroke-dasharray:1200;stroke-dashoffset:1200;animation:draw .8s cubic-bezier(.45,0,.55,1) forwards}
@keyframes draw{to{stroke-dashoffset:0}}
.stamp{--s:12px;padding:30px;background:var(--pale);transform:rotate(-4deg);transition:transform .7s cubic-bezier(.45,0,.55,1);
  -webkit-mask:radial-gradient(var(--s) at var(--s) var(--s),#0000 98%,#000) calc(-1*var(--s)) calc(-1*var(--s))/calc(2*var(--s)) calc(2*var(--s))}
.stamp.open{transform:rotate(-10deg) scale(1.06)}
.title{font:700 40px/1.1 "SF Pro Display",system-ui;color:var(--ink);letter-spacing:-.02em}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Fresh sky palette, a warm photo accent and a charming stamp motif. |
| Originality | 8 | Stamp cards plus a luminous abstract route are memorable and on-theme. |
| Usability | 6 | The map is decorative and the hero subtitle and meta fail contrast. |
| Craft | 7 | Careful masks, tilt states and ink colour; some text is lost in the gradient. |

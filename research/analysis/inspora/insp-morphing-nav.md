---
id: insp-morphing-nav
source: inspora
category: Product
status: analyzed
title: "morphing nav bar"
creator: "@renzobianchi_"
styles: [glassmorphism, spatial-ui, monochrome, micro-interaction]
patterns: [morphing-pill-nav, active-item-expands-to-label, search-field-grows-from-icon, nav-to-popover-container-morph, staggered-list-reveal, unread-dot-badges]
mode: dark
palette: ["#686a6b", "#9a9b9b", "#3f4950", "#2d3135", "#555e63", "#b8b8b4", "#e3b23c", "#ffffff"]
type_families: ["Inter (likely)"]
type_class: [neo-grotesk]
radius_px: [9999, 60, 40]
motion: {durations_s: [0.63, 0.33, 0.27, 0.47, 0.1, 0.33, 0.23, 1.03], easing: [ease-out], loop: true}
scores: {aesthetics: 8, originality: 7, usability: 7, craft: 9}
craft_signals: [one-container-morphs-bar-to-panel, label-clips-during-width-tween, list-rows-stagger-0-5s, hover-row-lift-in-panel, amber-unread-dot-only-colour, architectural-render-backdrop]
anti_patterns: [amber-dot-low-contrast, secondary-grey-on-glass-borderline]
---
# morphing nav bar — @renzobianchi_

## 1. Snapshot
- **Subject:** A 16.3 s, 1840×1320 looping clip of a smoky-glass pill nav (Home, Search, Archive, Notifications, Settings) floating over a grey architectural 3D render.
  - The active item expands into an icon-plus-label pill.
  - Search grows into a text field ("liquid glass").
  - Notifications morphs the whole bar into a tall popover with four notification rows, then collapses back to Home.
- **Why it's remarkable:** It is one continuous container. The bar never spawns a separate dropdown; it reshapes itself into the panel. That keeps spatial continuity and makes the state obvious.

## 2. Composition & layout
- **Collapsed bar:** about 275×50 px at 0.91 s (sheet scale), at top centre. The camera then zooms and pans: in later frames the bar is shown about 2× larger and shifts left and right.
- **Active pill:** about 95 px wide inside a 46 px-tall bar. Icons sit on a ~44 px pitch.
- **Search state:** the field takes about 50% of the bar width, and the other icons are pushed outward.
- **Notifications state (key frame, about 1040×710 px):** the bar row is on top. The rows are 62 px tall in the sheet (≈170 px in the key frame) with avatar or icon at 48 px, title, and a right-aligned time ("2m", "14m", "1h", "3h"). Panel radius ≈60 px in the key frame.

## 3. Typography
- Neo-grotesk close to Inter.
  - Nav label "Home" / "Notifications" about 15 px Medium (sheet scale), white.
  - Notification rows: the actor in Semibold white ("Ana", "Deploy", "Billing") and the rest in Regular light grey, a bold-lead pattern.
  - Times about 12 px grey with tabular figures.
- **Icons:** 1.75 px rounded-stroke outline set (Lucide-like).

## 4. Colour
| Hex | Role | Approx share |
|---|---|---|
| #686a6b / #555e63 / #505255 | glass tint over the render | ~43% |
| #9a9b9b / #b8b8b4 | light concrete planes | ~20% |
| #3f4950 / #2d3135 / #242629 | blue-grey shadow planes | ~33% |
| #ffffff | labels, active icons | <1% |
| ≈#c8c8c8 | secondary row text | <1% |
| ≈#e3b23c | unread dot | <0.1% |

WCAG checks (contrast.py):
- White on the glass #686a6b: **5.44:1**. On the darker glass #555e63: **6.63:1**.
- Secondary row text ≈#c8c8c8 on #686a6b: **3.25:1 (large only)**. Over darker regions (#505255) it rises to **5.08:1**, so contrast varies with the backdrop.
- Amber dot #e3b23c on #686a6b: **2.77:1 (below 3:1 for non-text)**.

## 5. Depth & material
- **Smoky glass:** about 60% neutral-grey fill, strong backdrop blur, a 1 px light top rim and a soft outer shadow.
- **Active pill and hovered row:** a slightly lighter, more opaque inner surface (about +10% white) with its own faint rim. That is a "glass on glass" second layer.
- **Backdrop:** a monochrome 3D architecture render with blue-grey shadow planes. Its strong diagonals show off the refraction and blur.

## 6. Components & patterns
- **Morphing pill nav:** icon-only items, with the active one expanding to icon plus label.
- **Inline search:** the icon becomes a field with placeholder "Search…" and a caret, and the bar widens.
- **Notifications popover:** the container grows downward, rows reveal with a stagger, and the hovered row (Deploy) gets a lighter pill highlight.
- **Unread state:** a small amber dot on the bell and on the avatars of unread items.
- **Settings:** a gear at the end, never expanded in the clip.

## 7. Motion
- Measured: 16.3 s at 60 fps (threshold 0.37). `motion_fraction` 0.23 and 12 segments, median **0.25 s**. **Every segment is ease-out (peak_at 0.03–0.25)** except one 0.13 s symmetric. `seamless_loop_likely: true`.
- **Key measured beats:**
  - 1.03–1.67 s: **0.63 s** (Home → Search expansion, with camera zoom).
  - 1.93 s: 0.33 s (field settles).
  - 7.93–8.40 s: **0.47 s** (bar → notifications panel morph).
  - 9.63, 10.13, 10.63 and 11.13 s: four **0.10 s** segments exactly 0.5 s apart (the hover highlight stepping down the rows).
  - 11.83 s: 0.33 s.
  - 13.33 s: 0.23 s (panel collapse).
  - 14.47–15.50 s: **1.03 s** (return to Home with camera pull-back).
- **From frames:** at 8.15 s only two rows are visible and the second is half-faded, so rows stagger in at about 80–100 ms each. At 13.58 s the label "Hom" is clipped mid-tween, so the label is masked by the width animation, not faded separately.

## 8. Brand system
n/a — not a brand system.

## 9. UX
- Spatial continuity reduces disorientation, and the active state is labelled, not icon-only. Notifications show the actor in bold plus a relative time.
- **Risks:**
  - The glass contrast depends on the backdrop.
  - The amber unread dot is faint.
  - The container morph changes the bar's width, so the icon positions shift between states, which hurts muscle memory.
  - The motion needs a reduced-motion fallback.

## 10. Craft signals
- Bar, search field and notification panel are the same element: the radius morphs from a pill to about 30 px corners.
- The label is revealed by clipping during the width tween ("Notifica", "Hom" mid-frame).
- The list stagger and hover steps are evenly timed (measured 0.5 s spacing).
- Amber is the only hue in the UI, used only for unread.
- Bold actor and regular remainder in each row.
- The backdrop is chosen with hard diagonals so the blur and refraction read clearly.

## 11. Reproduction recipe
```css
:root{--glass:rgb(90 92 94 / .62);--glass-2:rgb(255 255 255 / .12);--rim:rgb(255 255 255 / .22);
  --ink:#fff;--ink-2:#d0d0d0;--unread:#f0c24a;--ease:cubic-bezier(.16,1,.3,1)}
.nav{display:flex;flex-direction:column;background:var(--glass);backdrop-filter:blur(24px) saturate(1.2);
  border-radius:28px;box-shadow:inset 0 1px 0 var(--rim),0 12px 40px #0005;padding:6px;
  interpolate-size:allow-keywords;transition:width .47s var(--ease),height .47s var(--ease),border-radius .47s var(--ease)}
.nav[data-open=notifications]{border-radius:30px}
.item{display:flex;align-items:center;gap:8px;height:40px;padding:0 12px;border-radius:9999px;overflow:hidden;white-space:nowrap;color:var(--ink-2)}
.item[aria-current]{background:var(--glass-2);color:var(--ink);box-shadow:inset 0 1px 0 var(--rim)}
.item .label{max-width:0;transition:max-width .33s var(--ease)}
.item[aria-current] .label{max-width:140px}
.row{opacity:0;transform:translateY(-6px);animation:row .33s var(--ease) forwards;animation-delay:calc(var(--i)*90ms)}
.row:hover{background:var(--glass-2);border-radius:20px}
.row b{color:var(--ink)} .row{color:var(--ink-2)}
.dot{width:8px;height:8px;border-radius:50%;background:var(--unread);box-shadow:0 0 0 2px #0004}
@keyframes row{to{opacity:1;transform:none}}
@media (prefers-reduced-motion:reduce){.nav,.item .label,.row{transition:none;animation:none;opacity:1}}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Restrained monochrome glass over a moody render; very cohesive. |
| Originality | 7 | "Dynamic Island"-style container morphing for web nav is a known trend, executed well. |
| Usability | 7 | State is clear and continuous; contrast varies with the backdrop, and icon positions shift. |
| Craft | 9 | Consistently ease-out, single-container morph, clipped labels and evenly timed staggers. |

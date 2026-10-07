---
id: insp-portfolio
source: inspora
category: Web
status: analyzed
title: "portfolio"
creator: "@moguzbulbul"
styles: [minimal-swiss, soft-3d, spatial-ui, terminal-mono]
patterns: [3d-carousel-drum, window-chrome-project-cards, scroll-driven-rotation, sticky-project-label, client-logo-strip, mono-nav-links, pill-cta-outline]
mode: light
palette: ["#ffffff", "#f3f3f3", "#e3e3e3", "#000000", "#0a0e08", "#848b8a", "#8fd14f"]
type_families: ["Inter / Neue Haas-style grotesk (likely)", "monospace caps, close to JetBrains Mono / Geist Mono (likely)"]
type_class: [neo-grotesk, mono]
radius_px: [9999, 16]
motion: {durations_s: [0.63, 0.43, 0.73, 0.7, 0.9], easing: [ease-in-out, ease-in, ease-out], loop: false}
scores: {aesthetics: 8, originality: 7, usability: 6, craft: 8}
craft_signals: [traffic-light-dots-as-card-chrome, kebab-case-project-slugs, radial-floor-shadow, dated-eyebrow-labels, receding-cards-fade-and-compress, uniform-logo-tiles]
anti_patterns: [project-content-tiny-in-card, grey-mono-labels-low-contrast]
---
# portfolio — @moguzbulbul

## 1. Snapshot
- **Subject:** A 21.7 s, 3420×1970 capture of a designer's portfolio. Product-UI shots sit on white "window" cards stacked on a vertical 3D drum. Scrolling rotates the drum so each card swings to face the viewer while a left label updates (date plus project name).
- **Why it's remarkable:** It turns a list of Dribbble-style shots into a physical rolodex. The only depth on an otherwise flat white page is the drum's perspective and a soft elliptical floor shadow, which keeps it calm and premium.

## 2. Composition & layout
Key frame is ×1.71 to source.
- **Header:** about 60 px tall.
  - Avatar at the left (x≈90).
  - Centred mono links "X · LINKEDIN · DRIBBBLE" at about 112 px intervals.
  - An outline pill "GET IN TOUCH" at the right, about 140×32 px.
- **Stage:** The drum is centred. The active card is about 672×460 px (x≈663–1335, y≈390–850), and the cards above and below are foreshortened to about 15–25% height.
- **Project label:** fixed at the left, vertically centred at x=75, y≈555–600.
- **Footer:** a "WORKED WITH/" strip at y≈1080 holding 10 client logos (Interfacer, Forte, Cube, Fyxer.ai, Nansen, UXtools, Geode, Flott, Abs.xyz, Nexus) at an even pitch of about 172 px. Each is a 40 px tile with its name in 12 px below.

## 3. Typography
- **Two voices:**
  - A grotesk for the project names ("Signal Radar", about 22 px, weight 500).
  - Spaced mono caps for everything meta: "SEP 2026", nav, "WORKED WITH/" and the card slugs "SIGNAL-RADAR". These are 12–14 px with +0.2 em tracking.
- **Card titles:** set in grey mono kebab-case (like a filename or window title), so each shot reads as an app window.
- **Logo captions:** 12 px grotesk, centred.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #ffffff | canvas | 78% |
| #f3f3f3 / #e3e3e3 | card frames, floor shadow | 10% |
| #000000 / #0a0e08 | dark project screens | 8% |
| #848b8a | mono meta labels | 3% |
| #8fd14f | in-shot accent (radar, Yield Agent face) | <1% |
| #ff5f57 / #febc2e / #28c840 | macOS traffic lights | dots |

WCAG checks:
- Near-black on white is 18.88:1.
- The grey mono label #848b8a is **3.48:1**, AA-large only, which is weak at 12 px.
- Lime on black is 11.4:1 inside the shots.

The page is neutral, so each project brings its own colour.

## 5. Depth & material
- **Drum:** perspective of about 1200 px. The cards are white slabs with about 16 px radius and a 24–40 px light-grey frame around the screenshot. The active card has a darker top band carrying the traffic lights and slug.
- **Grounding:** A large elliptical radial shadow (#e3e3e3 fading to white, about 1300×700 px) sits behind the drum and grounds it.
- **Lighting:** Receding cards lighten and lose contrast (atmospheric falloff), and the faces above the active card show their undersides in pale grey.

## 6. Components & patterns
- A 3D vertical carousel of project windows, at least 9 projects seen: Analysis Intro, Markets Hero, Micro animation, Protocol Welcome, Signal Radar, Aesthetic Tests, Sponsor Analytics, Yield Agent.
- A sticky project caption (date eyebrow plus name) that swaps per card.
- macOS window chrome as a card frame (3 dots plus a mono slug).
- A client logo row with uniform 40 px tiles.
- An outline pill CTA and centred social links.

## 7. Motion
Measured: 21.68 s at 60 fps, motion_fraction 0.28, 17 segments with a median of 0.30 s, not a loop.
- **Card advances:** The main rotations are about 0.6–0.9 s: 1.03–1.67 s (0.63 s, symmetric), 3.23–3.87 s (0.63 s, ease-in peak 0.76), 9.93–10.67 s (0.73 s), 11.9–12.6 s (0.70 s) and 13.4–14.3 s (0.90 s, ease-in).
- **In-shot animations:** Short 0.1–0.3 s blips (5.23 s, 7.7 s, 9.67 s, 15.73 s) are the micro animations inside the screens, such as the radar sweep and the Yield Agent face blinking.
- **Cadence:** The holds between advances are about 1.5–2.4 s, consistent with scroll-snap stepping, one card per wheel notch.

## 8. Brand system
n/a — not a brand system. Personal identity cues:
- mono-caps metadata;
- kebab-case slugs as a "builder" voice;
- the lime #8fd14f accent recurring across projects (Signal Radar, Yield Agent) as the designer's signature.

## 9. UX
- **Strengths:** It shows one project at a time with a clear date and name, the CTA stays visible, and the social proof strip is always on screen.
- **Weaknesses:**
  - The shots render at about 590 px wide inside 3420 px captures, so UI details are unreadable without a click-through.
  - It is unclear whether cards are clickable.
  - Scroll-jacked rotation may fight trackpad momentum.
  - Grey mono labels are under 4.5:1.

## 10. Critical craft signals
- Every card has identical chrome: 3 traffic-light dots, then a mono slug 25 px to the right.
- The project label's date eyebrow ("SEP 2026") is spaced mono caps above a grotesk title, aligned to the same x=75 as "WORKED WITH/".
- The ellipse shadow stays fixed while the cards rotate, so the ground plane is stable.
- The logo strip uses equal-size tiles and equal pitch irrespective of logo shape.
- Receding cards fade in contrast as well as foreshortening.

## 11. Reproduction recipe
```css
:root{--bg:#fff;--frame:#f3f3f3;--shadow:#e3e3e3;--ink:#111;--meta:#6f7575;
  --sans:"Inter",system-ui,sans-serif;--mono:"Geist Mono","JetBrains Mono",ui-monospace,monospace}
.meta{font:500 12px/1 var(--mono);letter-spacing:.2em;text-transform:uppercase;color:var(--meta)}
.cta{border:1.5px solid var(--ink);border-radius:9999px;padding:8px 16px}
.stage{perspective:1200px;height:100vh;display:grid;place-items:center;
  background:radial-gradient(40% 35% at 50% 50%,var(--shadow),transparent 70%)}
.drum{transform-style:preserve-3d;transition:transform .7s cubic-bezier(.65,0,.35,1)}
.card{position:absolute;width:672px;border-radius:16px;background:var(--frame);padding:52px 36px 36px;
  transform:rotateX(calc(var(--i)*-36deg)) translateZ(560px);backface-visibility:hidden}
.card::before{content:"";position:absolute;top:18px;left:18px;width:10px;height:10px;border-radius:50%;
  background:#ff5f57;box-shadow:16px 0 #febc2e,32px 0 #28c840}
```
```js
// step one card per wheel notch
let i=0;addEventListener('wheel',e=>{i+=Math.sign(e.deltaY);drum.style.transform=`rotateX(${i*36}deg)`},{passive:true});
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | A restrained white field with a single sculptural drum, and mono/grotesk pairing that feels engineered. |
| Originality | 7 | The 3D rolodex is known, but the window-chrome framing and floor ellipse make it its own. |
| Usability | 6 | Clear one-at-a-time focus, but shots are too small to read and scroll-jacking is risky. |
| Craft | 8 | Consistent card chrome, aligned labels, and tidy logo tiles. |

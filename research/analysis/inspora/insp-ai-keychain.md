---
id: insp-ai-keychain
source: inspora
category: Motion
status: analyzed
title: "AI keychain."
creator: "Tân Tân Nguyễn (@premiumtantan)"
styles: [glassmorphism, cinematic-3d, playful-rounded, physical-material]
patterns: [draggable-3d-object, physics-pendulum, character-mascots, letter-as-hero-copy, sky-backdrop, grab-cursor-affordance, refraction-over-text]
mode: light
palette: ["#4580a2", "#74a7bc", "#bdcbd1", "#e9ebea", "#1d3e55", "#36688b", "#f5d21e", "#111111"]
type_families: ["Courier / American Typewriter-style mono (likely Courier Prime)", "handwritten script signature", "humanist serif in 'Instinct' charm label"]
type_class: [mono, script]
radius_px: [9999, 40]
motion: {durations_s: [0.4, 0.7, 0.37, 0.33, 0.87, 7.23, 1.0], easing: [ease-out, ease-in-out, ease-in], loop: false}
scores: {aesthetics: 9, originality: 9, usability: 5, craft: 9}
craft_signals: [real-refraction-of-text-behind-glass, fresnel-rim-on-discs, ball-chain-pendulum, mixed-materials-per-charm, typewriter-letter-narrative, cursor-changes-to-grab-hand]
anti_patterns: [body-text-over-busy-sky, glass-obscures-copy]
---
# AI keychain. — Tân Tân Nguyễn

## 1. Snapshot
- **Subject:** A 16 s, 3840×2160 web demo ("…keychain.vercel.app"). A bunch of glass charm discs hangs on a bead chain over a cloudy sky. Each charm holds a toy-like AI bot: a fuzzy yellow bell-shaped bot with glasses and a bow tie, a black ball with eyes, a felt ghost, a palm-tree tile, and an "Instinct" stick-figure tag.
- **Why it's remarkable:** It treats AI assistants as collectible physical trinkets. Real-time glass refraction, fresnel rims and a draggable pendulum make the interface tactile, and a typewritten "Dear finder" letter frames it as a lost-and-found story.

## 2. Composition & layout
- **Layout:** two zones. On the left (x 0–750 px at 2000-wide display, about 38%) is a typewritten letter column: date, salutation, five short paragraphs and a script signature "With thanks, Tan Tan". On the right is the hanging cluster, about 900×700 px at display scale, centred around x≈800.
- **Chain:** it drops from the top edge at x≈805 to a split ring at y≈380, so the cluster hangs like a pendant.
- **Camera:** the camera zooms and pans. Frames f0–f3 are tight, and f4–f8 pull back to show the browser chrome, with a toolbar holding the URL, icon buttons and a "Chat" pill top-right. Around 9.8–11.6 s the cluster is thrown off-frame top-right.

## 3. Typography
- **Letter:** a typewriter monospace (Courier-like, with slab serifs and an even 0.6 em advance) at about 34 px at 4K (about 17 px CSS), with leading of about 1.55. It is set ragged-right, with a date line indented to the centre the way a real typed letter would be.
- **Signature:** a handwritten script at about 2× the body size.
- **Charm label:** the "Instinct" tag uses a light humanist serif or sans, slightly tracked and printed onto the frosted disc.
- **No UI headline:** the letter *is* the copy.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #4580a2 / #36688b | upper sky, deep glass tint | ~25% |
| #74a7bc / #9bbbc5 | mid sky | ~20% |
| #bdcbd1 / #e9ebea | clouds, frosted glass | ~40% |
| #1d3e55 (approx.) | typewriter ink | ~2% |
| #f5d21e | yellow bot (only warm accent) | ~2% |
| #111111 | black ball bot, bow tie | ~2% |
| gold (#c9a65a-ish) | name tag coin behind ring | <1% |

WCAG:
- Ink #1d3e55 on mid sky #74a7bc is **4.27:1** (large only).
- On the upper sky #4a85a7 it is **2.78:1 (fails)**.
- On cloud #bdcbd1 it is 7.03:1.

Legibility of the letter depends on where the clouds fall.

## 5. Depth & material
This is the star.
- **Glass discs:** clear glass with a thick bevel. Each shows:
  - a bright fresnel rim (about 6–10 px at 4K);
  - a blue-tinted refracted copy of the sky;
  - **refraction of the letter text behind it** (the glyphs bend and magnify inside the left disc).
- **Frosted discs:** one is frosted milk-glass with a centre hole (washer shape).
- **Mixed materials:** felt or flocked fuzz on the yellow and blue bots, glossy enamel on the black ball (two specular highlights as "eyes"), sparkled resin on the palm tile, brushed gold on the name coin, and polished silver ball-chain beads.
- **Light:** soft and overcast, which matches the sky. No hard shadows.

## 6. Components & patterns
- A draggable 3D object (cursor turns into an open hand, then a grab hand, frames f1/f3).
- Each charm is a bot persona (the letter names Dots, Muse, Instinct, Grok Bot and Poke), so the charms double as a character-select.
- Browser chrome with a "Chat" pill suggests clicking a charm opens a chat.

## 7. Motion
The motion is measured: 16.09 s, 60 fps, motion_fraction 0.62, not a loop.
- **0.0–3.23 s:** four short segments (0.40, 0.70, 0.37, 0.33 s), all ease-out (peak_at 0.05–0.31). These are the drag-flicks: fast start, then a damped swing.
- **3.8–4.67 s:** a 0.87 s symmetric sway.
- **6.4–13.63 s:** one long 7.23 s ease-in segment (peak 0.66). This is the camera pull-back plus the cluster being flung up and swinging back, gaining energy before release.
- **14.33–15.33 s:** a 1.0 s symmetric settle.

The charms collide and rotate independently around the ring (f2 vs f5 show re-ordering), which indicates a rigid-body or verlet chain, not keyframes.

## 8. Brand system
n/a — not a brand system. Identity cues: the "Tan Tan" name coin, the sky and typewriter art direction, and the bot characters as mascots.

## 9. UX
- **Strengths:** the playful discovery affordance is clear (grab cursor), and it is memorable.
- **Weaknesses:**
  - The glass overlaps and obscures the letter.
  - Letter contrast fails on the darker sky.
  - Function (which charm does what) is implicit.
  - It is heavy on GPU, and 4K refraction will challenge low-end devices.

## 10. Craft signals
- The letter glyphs are visibly refracted and magnified inside the left glass disc (key frame, x≈400–560).
- Each disc has a fresnel rim, brighter at grazing edges.
- Each charm has a distinct material (felt, enamel, resin, frosted glass, gold) that maps to a distinct bot.
- The bead chain is made of individual spheres, about 6 px at display scale.
- The typewritten date is centred and the body is ragged-left aligned like a real letter.
- The cursor state changes from open hand to closed grab hand.

## 11. Reproduction recipe
```css
:root{--sky-hi:#4580a2;--sky-mid:#74a7bc;--cloud:#e9ebea;--ink:#1d3e55;--accent:#f5d21e}
body{background:linear-gradient(180deg,var(--sky-hi),var(--sky-mid) 45%,var(--cloud));font:17px/1.55 "Courier Prime",Courier,monospace;color:var(--ink)}
.letter{max-width:38ch;padding:64px;text-shadow:0 0 12px rgba(233,235,234,.6)} /* lifts contrast on dark sky */
.charm{cursor:grab}.charm:active{cursor:grabbing}
```
```js
// three.js glass charm
new THREE.MeshPhysicalMaterial({transmission:1,thickness:0.6,roughness:0.05,ior:1.45,
  clearcoat:1,attenuationColor:new THREE.Color('#bcd7e6'),attenuationDistance:2});
// frosted disc: roughness:0.45 ; chain: verlet rope of 40 spheres, damping .98
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 9 | A cohesive dreamy sky, glass and toy material world with one yellow accent. |
| Originality | 9 | AI agents as glass keychain charms, plus a lost-letter narrative, is a new metaphor. |
| Usability | 5 | Delightful but functionally opaque. Glass covers the copy and the ink fails contrast on the dark sky. |
| Craft | 9 | True refraction of text, per-charm materials and physical chain dynamics. |

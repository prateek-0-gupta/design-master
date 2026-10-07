---
id: insp-orb-interation
source: inspora
category: Motion
status: analyzed
title: "Orb interaction"
creator: "@vanjek"
styles: [dark-premium, monochrome, soft-3d, micro-interaction]
patterns: [voice-agent-orb, four-state-ai-indicator, state-list-with-active-dot, autoplay-vs-manual-toggle, hover-pill-highlight, ring-to-sphere-morph]
mode: dark
palette: ["#0c0c0c", "#171717", "#29292a", "#343436", "#484849", "#b9b9b9", "#ffffff"]
type_families: ["SF Pro Text (likely)"]
type_class: [neo-grotesk]
radius_px: [9999]
motion: {durations_s: [0.23, 0.33, 1.43, 0.5, 0.27], easing: [ease-in-out, ease-out, ease-in], loop: true}
scores: {aesthetics: 8, originality: 7, usability: 7, craft: 8}
craft_signals: [distinct-silhouette-per-state, greyscale-only-orb, rim-light-arc-for-thinking, inner-texture-for-speaking, state-label-right-aligned-with-dot, hover-pill-same-as-active-pill]
anti_patterns: [inactive-labels-1.7-contrast-in-autoplay, states-differ-mainly-by-luminance]
---
# Orb interaction — @vanjek

## 1. Snapshot
- **Subject:** A 27.6 s, 60 fps, 1282×958 prototype of a voice-assistant orb with four states (Idle, Listening, Thinking, Speaking), driven by a right-aligned text list and a Stop/Play toggle.
  - The first half auto-cycles the states.
  - The second half shows manual hover and selection of each state.
- **Why it's remarkable:** Each AI state has a distinct, readable form in pure greyscale:
  - Idle: a thin glowing ring on a dark disc;
  - Listening: a bright white halo sphere;
  - Thinking: a dark glass sphere with a rim-light arc orbiting;
  - Speaking: a pearly, textured, moon-like sphere.
- It is a compact, colour-free state vocabulary for agents.

## 2. Composition & layout
- **Two columns:** the state list is right-aligned at x≈485 (1282 frame) and the orb is centred at x≈835, y≈485 with a diameter of about 205 px (about 130 px for the Idle disc's ring). The column gap is about 250 px.
- **List:** four labels at a 72 px pitch, then the Stop/Play button 96 px below the last label.
- **Active-state marker:** in autoplay, a 6 px white dot sits 18 px right of the active label. In manual mode, a #29292a pill (radius full, padding about 8×16 px) wraps the active or hovered label.

## 3. Typography
- SF Pro Text, about 26 px at capture (about 15–17 pt) Regular.
- **Tone by state:**
  - active white #e6e6e6;
  - inactive #8a8a8a in manual mode;
  - in autoplay, inactive labels drop to about #3a3a3a, almost invisible.
- No weights or sizes change, only tone.

## 4. Colour
| Hex | Role | Approx share |
|---|---|---|
| #0c0c0c | canvas | 96.5% |
| #171717 | Idle disc body, faint halo | 1.3% |
| #29292a / #343436 | active pill, sphere mid-tones | 1.6% |
| #484849 | sphere shading | 0.3% |
| #b9b9b9 → #ffffff | ring, rim lights, Listening halo | 0.2–4% (state-dependent) |

WCAG checks:
- Active label #e6e6e6 on pill #29292a is 11.65:1.
- Manual-mode inactive #8a8a8a on #0c0c0c is 5.67:1.
- Autoplay inactive (about #3a3a3a) is **1.72:1 (fail)**: intentionally receded, but unreadable.
- #b9b9b9 on canvas is 9.97:1.

## 5. Depth & material
- **Idle:** a #171717 disc with a soft dark halo plus a 4–5 px white ring inset about 18% with an inner glow, like a powered-down button with an LED ring.
- **Listening:** the disc inflates to a sphere with a blinding white outer band (a thick white rim, about 20% of the radius) and a grey radial core. It reads as the "mic open, receiving light" state.
- **Thinking:** a dark glossy sphere with a single thin specular crescent travelling around its rim (bottom at 7.66 s, top-left plus right at 22.97 s), like a loading spinner made of reflection.
- **Speaking:** a light pearly sphere with internal cloudy blotches and radial streaks (10.72 s, 16.85 s). The texture animates, implying voice energy.

## 6. Components & patterns
- **State list:**
  - doubles as legend and control;
  - the hover pill is identical to the active pill (13.78 s: the cursor over "Listening" while "Idle" is pilled);
  - in manual mode at 16.85 s, both the selected "Thinking" and the hovered "Speaking" show pills.
- **Stop/Play:** a pill button that toggles autoplay. Its label becomes "Play" when stopped.
- **The orb as single status object:** a voice-AI indicator pattern (similar to ChatGPT voice or Siri orbs) but monochrome.

## 7. Motion
- **Measured:** 27.57 s with motion fraction 0.23, 22 segments (median **0.25 s**), and `seamless_loop_likely: true`. Key segments:
  - 2.50–2.73 s (0.23 s, symmetric): Idle → Listening inflate.
  - 8.30–8.63 s (0.33 s, symmetric): Thinking → Speaking.
  - 9.87–10.13 s (0.27 s, ease-out, peak 0.06): a snappy settle.
  - **14.07–15.50 s (1.43 s, ease-out, peak 0.10):** the longest morph, during manual selection (Idle ring to Speaking sphere), a fast start with a long tail, so a spring.
  - 21.40–21.90 s (0.5 s, **ease-in**): collapse into Thinking.
  - 23.33–23.83 s (0.5 s, symmetric): Thinking → Idle.
- **From frames (estimate):** within a state, motion is ambient and low-energy. Thinking's rim arc orbits at about one revolution per 1.5–2 s, and Speaking's texture churns. State changes morph scale (the ring disc at about 130 px grows to about 205 px) and luminance together in 0.25–0.5 s.

## 8. Brand system
n/a — not a brand system. The cue is a monochrome "AI presence" object that would sit well in a neutral, premium assistant brand.

## 9. UX
- **Strengths:**
  - Four states with four distinct silhouettes and luminance levels, readable at small size and colour-blind-safe.
  - The list makes the mapping learnable.
- **Weaknesses:**
  - In autoplay the inactive labels nearly vanish (1.72:1).
  - Listening and Speaking are both bright spheres. Their difference is the inner texture, which may blur at a 32 px in-app size.
  - Real products also need an error or "muted" state.

## 10. Craft signals
- Each state changes silhouette (ring / halo / crescent / textured), not just colour, which is critical in greyscale.
- The Thinking state uses a single moving specular arc: a spinner expressed as reflected light.
- The Idle ring has an inner glow, not a flat stroke.
- The hover and active pills share one token (#29292a), so feedback and state feel consistent.
- The state dot sits 18 px right of the right-aligned labels and aligns to the label x-height centre.
- The Stop/Play label swaps in place without the pill resizing jarringly.

## 11. Reproduction recipe
```css
:root{--bg:#0c0c0c;--pill:#29292a;--on:#e6e6e6;--off:#8a8a8a;--font:-apple-system,"SF Pro Text",system-ui,sans-serif}
.states{display:grid;gap:24px;justify-items:end;font:400 16px var(--font);color:var(--off)}
.states button{padding:6px 12px;border-radius:9999px;transition:background .2s,color .2s}
.states button:is(:hover,[aria-pressed=true]){background:var(--pill);color:var(--on)}
.orb{width:130px;aspect-ratio:1;border-radius:50%;transition:all .45s cubic-bezier(.2,.9,.25,1.1)}
.orb[data-s=idle]{background:#171717;box-shadow:inset 0 0 0 22px #171717,inset 0 0 0 26px #fff,0 0 40px #0008;filter:drop-shadow(0 0 6px #fff4)}
.orb[data-s=listening]{width:205px;background:radial-gradient(circle,#6f6f6f 0 35%,#d9d9d9 62%,#fff 72%)}
.orb[data-s=thinking]{width:205px;background:radial-gradient(circle at 40% 35%,#3a3a3a,#111 70%);position:relative}
.orb[data-s=thinking]::after{content:"";position:absolute;inset:4px;border-radius:50%;
  border:2px solid transparent;border-bottom-color:#fff;filter:blur(.5px);animation:spin 1.6s linear infinite}
.orb[data-s=speaking]{width:205px;background:radial-gradient(circle at 50% 40%,#f2f2f2,#9a9a9a 75%,#fff 95%);animation:churn 2s ease-in-out infinite alternate}
@keyframes spin{to{transform:rotate(1turn)}}
@keyframes churn{to{filter:contrast(1.2) brightness(1.05)}}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Elegant monochrome objects on black, with lovely light behaviour per state. |
| Originality | 7 | Voice orbs are common. The colourless four-silhouette system is a distinctive take. |
| Usability | 7 | States are well distinguished by form. Autoplay labels are unreadable, and Listening versus Speaking may blur when small. |
| Craft | 8 | Consistent pill token, careful specular details and spring-like morphs. |

---
id: insp-chat-component-interaction
source: inspora
category: Product
status: analyzed
title: "Chat component interaction"
creator: "@flohoeller"
styles: [minimal-swiss, hairline-ui, micro-interaction]
patterns: [composer-with-attached-tray, tray-flips-above-or-below, permission-toggle-chip, blur-crossfade-label-swap, dashed-construction-guides]
mode: light
palette: ["#faf9f7", "#ffffff", "#efeeec", "#e1e1e0", "#a2a8ab", "#555555", "#c2410c", "#38bdf8"]
type_families: ["Inter (likely)"]
type_class: [neo-grotesk]
radius_px: [36, 9999]
motion: {durations_s: [0.27], easing: [ease-in-out], loop: false}
scores: {aesthetics: 7, originality: 7, usability: 7, craft: 8}
craft_signals: [tray-tucked-under-card-radius, dashed-layout-guides-in-canvas, warm-off-white-canvas, blur-in-state-swap, red-tint-chip-for-risky-permission]
anti_patterns: [placeholder-text-2-to-1, cropped-right-edge-hides-send]
---
# Chat component interaction — @flohoeller

## 1. Snapshot
- **Subject:** A 6.7 s, 1090×1238 recording of a chat composer. A white input card ("Start by typing…", "+", "Request approval") has a grey tray tucked behind it. The tray first appears below with "Connect apps" (Gmail, Slack and ClickUp glyphs), then above with "Select a project". Clicking "Request approval" swaps it, with a blur transition, to a red "Unrestricted access" chip.
- **Why it's remarkable:** The contextual tray is a second surface that slides out from behind the composer on whichever side fits. Permission level is shown as a toggle chip whose risky state turns red. That is a clean way to surface agent autonomy in chat.

## 2. Composition & layout
- The composer is cropped on the right: it starts at x≈242 and runs off-frame. It is about 305 px tall (y≈520–825) in the key frame.
- **Tray:** about 105 px tall, peeking 55 px beyond the card edge. The card's 36 px radius overlaps the tray, so the tray reads as tucked behind it.
- **Dashed guides:** vertical at x≈242 and horizontal at y≈415 and y≈827. They align exactly with the component's edges, a deliberate "spec sheet" framing.
- **Inner padding:** 56 px left. The placeholder baseline is at y≈625 and the action row at y≈757, a gap of about 132 px.

## 3. Typography
- Neo-grotesk close to Inter, Regular 400.
- **Placeholder:** about 40 px (native), light grey.
- **Actions:** "Request approval" and "Select a project" at about 34 px in mid-grey.
- **Icon set:** 1.5 px outline icons (plus, hand) sized to the cap height. The app icons are full-colour.

## 4. Colour
| Hex | Role | Approx share |
|---|---|---|
| #faf9f7 | warm off-white canvas | 93% |
| #ffffff | composer card | (in canvas sample) |
| #efeeec | tray surface | 5.6% |
| #e1e1e0 | dashed guides, card hairline | <1% |
| #a2a8ab | placeholder / icons | <1% |
| ≈#555555 | action label | <1% |
| ≈#c2410c on ≈#fde8e2 | "Unrestricted access" chip | <1% |
| ≈#38bdf8 | folder icon | <1% |

WCAG checks (contrast.py):
- Placeholder ≈#b5b5b5 on white: **2.05:1 (fail)**.
- Action label ≈#555 on white: **7.46:1**.
- Tray label ≈#7d7d7d on #efeeec: **3.55:1 (large only)**.
- Red chip text ≈#c2410c on #fde8e2: **4.39:1 (just under AA)**.
- The card (white) on the canvas (#faf9f7) is 1.05:1, so the card relies on its 1 px hairline and a soft bottom shadow.

## 5. Depth & material
- Two layers. The white card has a 1 px #e8e8e6 border and a faint 0 2px 4px shadow at the bottom edge. The tray is flat #efeeec, sitting behind the card with the same horizontal extent.
- No blur materials. Depth comes from overlap order only.

## 6. Components & patterns
- **Composer:** placeholder, an attach "+", and an approval-mode chip.
- **Contextual tray:** below for integrations ("Connect apps" with an overlapping logo row), above for scope ("Select a project" with a folder icon).
- **Approval toggle:**
  - Default: "Request approval" with a hand icon, plain.
  - Hover: the label darkens to near-black and the cursor becomes a pointer.
  - Active risky state: "Unrestricted access" with a shield icon, a red-tinted pill fill and red text.

## 7. Motion
- Measured: 6.7 s at 60 fps. `motion_fraction` 0.04. One measured segment: **0.27 s symmetric ease-in-out (peak 0.44) at 2.27–2.53 s**, which is the tray swapping from below to above. Not a seamless loop (`first_last_diff` 3.14).
- **From frames (estimates):**
  - 3.35 s: hover darkens the label (instant).
  - 4.84 s: the chip is mid-transition. The old label is blurred and faded, with a faint red tint already present, so a blur and opacity crossfade of about 0.2–0.3 s.
  - 5.58 s: the red chip has settled.
- Every transition is short and symmetric, with no overshoot or bounce.

## 8. Brand system
n/a — not a brand system.

## 9. UX
- The approval mode is visible at the point of input, and the risky state is colour-coded and labelled in words with an icon. That is good for agent-safety affordances.
- The tray shows context (project, apps) without adding a toolbar row.
- **Risks:**
  - The placeholder is very faint.
  - Toggling to "Unrestricted access" with a single click has no confirmation step.
  - The tray's position switches between above and below, so its location is less predictable.

## 10. Craft signals
- The tray sits behind the card's rounded corner (overlap of about 36 px), so the corners nest without a seam.
- The dashed guides align exactly to the component's bounding box.
- The canvas is warm (#faf9f7) rather than grey, so the white card glows slightly.
- The state swap blurs out the old label instead of simply fading it, which adds motion texture without movement.
- The red chip uses a tinted fill rather than a solid fill, so it alerts without shouting.

## 11. Reproduction recipe
```css
:root{--canvas:#faf9f7;--card:#fff;--tray:#efeeec;--line:#e6e5e3;--ink:#1c1c1c;--ink-2:#555;--ph:#9a9a9a;--danger:#b4380a;--danger-bg:#fde8e2;--r:36px}
.composer{position:relative;isolation:isolate}
.card{position:relative;z-index:1;background:var(--card);border:1px solid var(--line);border-radius:var(--r);padding:40px 28px 28px;box-shadow:0 2px 4px #0000000a}
.tray{position:absolute;inset-inline:0;height:calc(var(--r) + 52px);background:var(--tray);z-index:0;
  transition:transform .27s cubic-bezier(.45,0,.55,1)}
.tray.below{top:calc(100% - var(--r));border-radius:0 0 var(--r) var(--r);padding-top:var(--r)}
.tray.above{bottom:calc(100% - var(--r));border-radius:var(--r) var(--r) 0 0}
.chip{display:inline-flex;gap:6px;padding:6px 10px;border-radius:9999px;color:var(--ink-2);transition:filter .25s,opacity .25s,background .25s}
.chip:hover{color:var(--ink)}
.chip.swapping{filter:blur(6px);opacity:0}
.chip.danger{background:var(--danger-bg);color:var(--danger)}
textarea::placeholder{color:var(--ph)}  /* raise from #b5b5b5 */
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 7 | Quiet, warm and precise; restrained to the point of sparse. |
| Originality | 7 | The tucked tray that flips sides and the permission chip are thoughtful takes on a common composer. |
| Usability | 7 | Clear modes and an explicit risk state; weak placeholder and no confirm on escalation. |
| Craft | 8 | Nested radii, aligned guides and a crisp 0.27 s transition. |
